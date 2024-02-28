# First create the Python module
# by running this from the repository root:
#
#     gen-python src/ak_schema/schema/ak_schema.yaml > examples/iedb/ak_schema.py
#
# To refresh the example data,
# fetch it from Google Sheets:
#
#     curl -L -o examples/iedb/tcell.tsv "https://docs.google.com/spreadsheets/d/1oQYrlF7yxG_rjH_fNzMCK8bJMtcY6Xajhr9qGE6VYEk/export?format=tsv&gid=883146061"

import dataclasses
import click
import csv

from linkml_runtime.dumpers import yaml_dumper, json_dumper, tsv_dumper
from ak_schema import *


prefixes = {
    'iedb_reference': 'http://www.iedb.org/reference/',
    'iedb_epitope': 'http://www.iedb.org/epitope/',
    'iedb_assay': 'http://www.iedb.org/assay/',
    'OBI': 'http://purl.obolibrary.org/obo/OBI_',
}


def curie(input):
    """Convert a URL to a CURIE."""
    for prefix, url in prefixes.items():
        if input.startswith(url):
            return input.replace(url, prefix + ':')
    return input


def id(input):
    """Convert a URL to an ID."""
    for prefix, url in prefixes.items():
        if input.startswith(url):
            return input.replace(url, '')
    return input


@click.command()
@click.argument('input')
@click.argument('output')
def convert(input, output):
    """Convert an input TCell TSV file to YAML."""

    # First read the TCell table into a list
    # of two-level dictionaries
    # using the first and second header rows.
    rows = []
    with open(input) as t:
        rs = csv.reader(t, delimiter='\t')
        header1 = list(next(rs))
        header2 = list(next(rs))
        for r in rs:
            row = {}
            for c in range(0, len(r)):
                if header1[c] not in row:
                    row[header1[c]] = {}
                value = r[c]
                if value.strip() == '':
                    value = None
                row[header1[c]][header2[c]] = value
            rows.append(row)

    ref_id = id(rows[0]['Reference']['IEDB IRI'])

    investigation = Investigation(
        f'example:investigation_{ref_id}',
        name=row['Reference']['Title'],
        description=None
    )
    reference = Reference(
        f'example:reference_{ref_id}',
        sources=[f"PMID:{rows[0]['Reference']['PMID']}"],
        investigations=[investigation.id],
        title=rows[0]['Reference']['Title'],
        authors=rows[0]['Reference']['Authors'].split('; '),
        issue=None,
        journal=rows[0]['Reference']['Journal'],
        month=None,
        year=rows[0]['Reference']['Date'],
        pages=None,
    )
    container = Container(
        investigations=[investigation],
        references=[reference]
    )

    # For each row in the TCell table, generate:
    # 1 arm
    # 1 study events: specimen collection
    # 1 participant
    # 2 life events: 1st in vivo Process, specimen collection
    # 1 immune exposure: 1st in vivo Process
    # 0 assessments
    # 1 specimen
    # 1 assay
    # 1 dataset
    # 1 conclusion
    for row in rows:
        assay_id = row['Assay ID']['IEDB IRI'].split('/')[-1]
        arm = Arm(
            f'example:arm-{assay_id}',
            name=f'arm 1 of {assay_id}',
            description=f'study arm for assay {assay_id}',
            investigation=investigation.id
        )
        study_event = StudyEvent(
            f'example:study_event-{assay_id}',
            name=f'',
            description=f'',
            arms=[arm.id]
        )
        participant = Participant(
            f'example:participant-{assay_id}',
            name=f'participant 1 of {assay_id}',
            description=f'study participant for assay {assay_id}',
            species=row['Host']['Name'],
            biological_sex=row['Host']['Sex'],
            race=None,
            ethnicity=None,
            geolocation=None
            # geolocation=row['Host']['Geolocation']
        )
        life_event_1 = LifeEvent(
            f'example:life_event-{assay_id}-1',
            name=f'1st in vivo immune exposure event of assay {assay_id}',
            description=f'participant 1 of assay {assay_id} participated in this 1st in vivo immune exposure event',
            participant=participant.id,
            study_event=None,
            life_event_type=row['1st in vivo Process']['Process Type'],
            geolocation=None,
            t0_event=None,
            t0_event_type=None,
            start=None,
            duration=None,
            time_unit=None
        )
        life_event_2 = LifeEvent(
            f'example:life_event-{assay_id}-2',
            name=f'specimen collection event of assay {assay_id}',
            description=f'specimen 1 was collected from participant 1 of assay {assay_id} in this event',
            participant=participant.id,
            study_event=study_event.id,
            life_event_type='specimen collection',
            geolocation=None,
            t0_event=None,
            t0_event_type=None,
            start=None,
            duration=None,
            time_unit=None
        )
        immune_exposure = ImmuneExposure(
            f'example:immune_exposure-{assay_id}',
            name=f'details of 1st in vivo immune exposure event of assay {assay_id}',
            description=f'participant 1 of assay {assay_id} participated in this 1st in vivo immune exposure event, with these details',
            life_event=life_event_1.id,
            exposure_material=row['1st immunogen']['Source Organism'],
            disease=row['1st in vivo Process']['Disease'],
            disease_stage=row['1st in vivo Process']['Disease Stage'],
            disease_severity=None
        )
        # assessment
        specimen = Specimen(
            f'example:specimen-{assay_id}',
            name=f'specimen 1 of assay {assay_id}',
            description=f'specimen 1 from participant 1 of assay {assay_id}',
            life_event=life_event_2.id,
            specimen_type=None,
            tissue=row['Effector Cell']['Source Tissue'],
            process=None
        )
        assay = Assay(
            f'example:assay-{assay_id}',
            name=f'assay {assay_id}',
            description=f'assay {assay_id} has specified input specimen 1',
            specimen=specimen.id,
            assay_type=curie(row['Assay']['IRI']), # TODO: use label
            target_entity_type=row['Assay']['Response measured'],
            value=row['Assay']['Qualitative Measurement'],
            unit=None
        )
        dataset = Dataset(
            f'example:dataset-{assay_id}',
            name=f'dataset 1 about assay {assay_id}',
            description=f'dataset 1 is about assay {assay_id}',
            assessments=None,
            assays=[assay.id]
        )
        conclusion = Conclusion(
            f'example:conclusion-{assay_id}',
            name=f'conclusion 1 about assay {assay_id}',
            description=f'conclusion 1 about investigation {ref_id} was drawn from dataset 1 of assay {assay_id}',
            investigations=investigation.id,
            datasets=dataset.id,
            result=row['Assay']['Qualitative Measurement'],
            data_location_type=None,
            data_location_value=row['Assay']['Location of Assay Data in Reference'],
            organism=row['Host']['Name'],
            experiment_type=curie(row['Assay']['IRI']) # TODO: use label
        )

        container.arms[arm.id] = arm
        container.study_events[study_event.id] = study_event
        container.participants[participant.id] = participant
        container.life_events[life_event_1.id] = life_event_1
        container.life_events[life_event_2.id] = life_event_2
        container.immune_exposures[immune_exposure.id] = immune_exposure
        # container.assessments[assessment.id] = assessment
        container.specimens[specimen.id] = specimen
        container.assays[assay.id] = assay
        container.datasets[dataset.id] = dataset
        container.conclusions[conclusion.id] = conclusion

        break

    yaml_dumper.dump(container, output)

    # Write everything to TSV
    container_fields = [x.name for x in dataclasses.fields(container)]
    for container_field in container_fields:
        rows = list(container[container_field].values())
        if len(rows) < 1:
            continue
        with open(f'tsv/{container_field}.tsv', 'w') as f:
            fieldnames = [x.name for x in dataclasses.fields(rows[0])]
            w = csv.DictWriter(f, fieldnames, delimiter='\t', lineterminator='\n')
            w.writeheader()
            for row in rows:
                w.writerow(row.__dict__)


if __name__ == "__main__":
    convert()
