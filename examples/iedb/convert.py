# First create the Python module
# by running this from the repository root:
#
#     gen-python src/ak_schema/schema/ak_schema.yaml > examples/iedb/ak_schema.py
#
# To refresh the example data,
# fetch it from Google Sheets:
#
#     curl -L -o examples/iedb/tcell.tsv "https://docs.google.com/spreadsheets/d/1oQYrlF7yxG_rjH_fNzMCK8bJMtcY6Xajhr9qGE6VYEk/export?format=tsv&gid=883146061"
#     curl -L -o examples/iedb/tcr.tsv "https://docs.google.com/spreadsheets/d/1oQYrlF7yxG_rjH_fNzMCK8bJMtcY6Xajhr9qGE6VYEk/export?format=tsv&gid=2131098483"

import dataclasses
import click
import csv
import uuid
import json

from linkml_runtime.dumpers import yaml_dumper, json_dumper, tsv_dumper
from ak_schema import *


prefixes = {
    'iedb_reference': 'http://www.iedb.org/reference/',
    'iedb_epitope': 'http://www.iedb.org/epitope/',
    'iedb_assay': 'http://www.iedb.org/assay/',
    'iedb_receptor': 'http://www.iedb.org/receptor/',
    'OBI': 'http://purl.obolibrary.org/obo/OBI_',
}


def curie(input):
    """Convert a URL to a CURIE."""
    if input is None:
        return input
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

# this is fake
# we don't generate new IDs every time the code is run
akc_id_last = 0
def akc_id():
    """Returns a new AKC ID."""
    global akc_id_last
    akc_id_last += 1
    return 'AKC:' + str(akc_id_last)


def read_double_header(path):
    """Read a TSV file with two header rows,
    and return a list of dictionaries:
    row[header1][header2] = value"""
    rows = []
    with open(path) as t:
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
    return rows

chain_types = {
    'alpha': 'TRA',
    'beta': 'TRB',
    'gamma': 'TRG',
    'delta': 'TRD',
}

def make_chain(row, chain_name):
    '''Given a row dictionary and a chain name ("Chain 1" or "Chain 2"),
    return a new Chain object.
    Prefer Calculated columns to Curated columns.'''
    tcr_curie = curie(row['Receptor']['Group IRI'])
    chain = row[chain_name]
    junction_aa = None
    cdr3 = chain['CDR3 Calculated'] or chain['CDR3 Curated']
    if cdr3 and cdr3.startswith('C') and (cdr3.endswith('F') or cdr3.endswith('W')):
        junction_aa = cdr3
    return Chain(
        tcr_curie + '-' + chain['Type'],
        sequence=chain['Nucleotide Sequence'],
        sequence_aa=chain['Protein Sequence'],
        chain_type=chain_types[chain['Type']],
        v_call=chain['Calculated V Gene'] or chain['Curated V Gene'],
        d_call=chain['Calculated D Gene'] or chain['Curated D Gene'],
        j_call=chain['Calculated J Gene'] or chain['Curated J Gene'],
        # c_call='',
        junction_aa=junction_aa,
        cdr1_aa=chain['CDR1 Calculated'] or chain['CDR1 Curated'],
        cdr2_aa=chain['CDR2 Calculated'] or chain['CDR2 Curated'],
        cdr3_aa=chain['CDR3 Calculated'] or chain['CDR3 Curated'],
        cdr1_start=chain['CDR1 Start Calculated'] or chain['CDR1 Start Curated'],
        cdr1_end=chain['CDR1 End Calculated'] or chain['CDR1 End Curated'],
        cdr2_start=chain['CDR2 Start Calculated'] or chain['CDR2 Start Curated'],
        cdr2_end=chain['CDR2 End Calculated'] or chain['CDR2 End Curated'],
        cdr3_start=chain['CDR3 Start Calculated'] or chain['CDR3 Start Curated'],
        cdr3_end=chain['CDR3 End Calculated'] or chain['CDR3 End Curated']
    )


@click.command()
@click.argument('tcell_path')
@click.argument('tcr_path')
@click.argument('yaml_path')
def convert(tcell_path, tcr_path, yaml_path):
    """Convert an input TCell and TCR TSV file to YAML."""

    # First read the TCell table into a list
    # of two-level dictionaries
    # using the first and second header rows.
    tcell_rows = read_double_header(tcell_path)
    tcr_rows = read_double_header(tcr_path)

#     ref_id = id(tcell_rows[0]['Reference']['IEDB IRI'])
# 
#     investigation = Investigation(
#         akc_id(),
#         name=tcell_rows[0]['Reference']['Title'],
#         description=None
#     )
#     reference = Reference(
#         f"PMID:{tcell_rows[0]['Reference']['PMID']}",
#         sources=[f"PMID:{tcell_rows[0]['Reference']['PMID']}"],
#         investigations=[investigation.akc_id],
#         title=tcell_rows[0]['Reference']['Title'],
#         authors=tcell_rows[0]['Reference']['Authors'].split('; '),
#         issue=None,
#         journal=tcell_rows[0]['Reference']['Journal'],
#         month=None,
#         year=tcell_rows[0]['Reference']['Date'],
#         pages=None,
#     )
    container = AIRRKnowledgeCommons(
#        investigations=[investigation],
#        references=[reference]
    )

    # For each row in the TCell table, generate:
    # 1 study arm
    # 1 study events: specimen collection
    # 1 participant
    # 2 life events: 1st in vivo Process, specimen collection
    # 1 immune exposure: 1st in vivo Process
    # 0 assessments
    # 1 specimen
    # 1 assay
    # 1 epitope
    # 1+ t cell receptors
    # 2 chains per TCR
    # 1 dataset
    # 1 conclusion
    row_cnt = 0
    current_reference = None
    for row in tcell_rows:
        if current_reference != row['Reference']['PMID']:
            current_reference = row['Reference']['PMID']
            investigation = Investigation(
                akc_id(),
                name=row['Reference']['Title'],
                description=None
            )
            ref_id = id(row['Reference']['IEDB IRI'])
            reference = Reference(
                f"PMID:{row['Reference']['PMID']}",
                sources=[f"PMID:{row['Reference']['PMID']}"],
                investigations=[investigation.akc_id],
                title=row['Reference']['Title'],
                authors=row['Reference']['Authors'].split('; '),
                issue=None,
                journal=row['Reference']['Journal'],
                month=None,
                year=row['Reference']['Date'],
                pages=None,
            )
            container.investigations[investigation.akc_id] = investigation
            container.references[reference.source_uri] = reference

        assay_id = row['Assay ID']['IEDB IRI'].split('/')[-1]
        arm = StudyArm(
            akc_id(),
            name=f'arm 1 of {assay_id}',
            description=f'study arm for assay {assay_id}',
            investigation=investigation.akc_id
        )
        study_event = StudyEvent(
            akc_id(),
            name=f'',
            description=f'',
            study_arms=[arm.akc_id]
        )
        participant = Participant(
            akc_id(),
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
            akc_id(),
            name=f'1st in vivo immune exposure event of assay {assay_id}',
            description=f'participant 1 of assay {assay_id} participated in this 1st in vivo immune exposure event',
            participant=participant.akc_id,
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
            akc_id(),
            name=f'specimen collection event of assay {assay_id}',
            description=f'specimen 1 was collected from participant 1 of assay {assay_id} in this event',
            participant=participant.akc_id,
            study_event=study_event.akc_id,
            life_event_type='specimen collection',
            geolocation=None,
            t0_event=None,
            t0_event_type=None,
            start=None,
            duration=None,
            time_unit=None
        )
        immune_exposure = ImmuneExposure(
            akc_id(),
            name=f'details of 1st in vivo immune exposure event of assay {assay_id}',
            description=f'participant 1 of assay {assay_id} participated in this 1st in vivo immune exposure event, with these details',
            life_event=life_event_1.akc_id,
            exposure_material=row['1st immunogen']['Source Organism'],
            disease=row['1st in vivo Process']['Disease'],
            disease_stage=row['1st in vivo Process']['Disease Stage'],
            disease_severity=None
        )
        # assessment
        specimen = Specimen(
            akc_id(),
            name=f'specimen 1 of assay {assay_id}',
            description=f'specimen 1 from participant 1 of assay {assay_id}',
            life_event=life_event_2.akc_id,
            specimen_type=None,
            tissue=row['Effector Cell']['Source Tissue'],
            process=None
        )
        epitope = PeptidicEpitope(
            curie(row['Epitope']['IEDB IRI']),
            sequence_aa=row['Epitope']['Name'],
            source_protein=curie(row['Epitope']['Molecule Parent IRI']),
            source_organism=curie(row['Epitope']['Source Organism IRI'])
        )
        # For each row in the TCR table that matches this assay ID, generate:
        # 2 chains
        # 1 receptor: AlphaBetaTCR or GammaDeltaTCR
        chains = []
        tcell_receptors = []
        for tcr_row in tcr_rows:
            if tcr_row['Assay']['IEDB IDs'] != assay_id:
                continue
            tcr_curie = curie(tcr_row['Receptor']['Group IRI'])
            chain_1 = None
            chain_2 = None
            if tcr_row['Chain 1']['Type']:
                chain_1 = make_chain(tcr_row, 'Chain 1')
                chains.append(chain_1)
            if tcr_row['Chain 2']['Type']:
                chain_2 = make_chain(tcr_row, 'Chain 2')
                chains.append(chain_2)
            if tcr_row['Receptor']['Type'] == 'alphabeta':
                tcr = AlphaBetaTCR(
                    tcr_curie,
                    TRA_chain=chain_1.akc_id if chain_1 else None,
                    TRB_chain=chain_2.akc_id if chain_2 else None,
                )
                tcell_receptors.append(tcr)
            elif tcr_row['Receptor']['Type'] == 'gammadelta':
                tcr = GammaDeltaTCR(
                    tcr_curie,
                    TRG_chain=chain_1.akc_id if chain_1 else None,
                    TRD_chain=chain_2.akc_id if chain_2 else None,
                )
                tcell_receptors.append(tcr)
            else:
                raise Exception(f"Unknown TCR type {tcr_row['Receptor']['Type']}")
        assay = TCellReceptorEpitopeBindingAssay(
            akc_id(),
            name=f'assay {assay_id}',
            description=f'assay {assay_id} has specified input specimen 1',
            specimen=specimen.akc_id,
            assay_type=curie(row['Assay']['IRI']), # TODO: use label
            epitope=epitope.akc_id,
            tcell_receptors=[t.akc_id for t in tcell_receptors],
            value=row['Assay']['Qualitative Measurement'],
            unit=None
        )
        dataset = Dataset(
            akc_id(),
            name=f'dataset 1 about assay {assay_id}',
            description=f'dataset 1 is about assay {assay_id}',
            assessments=None,
            assays=[assay.akc_id]
        )
        conclusion = Conclusion(
            akc_id(),
            name=f'conclusion 1 about assay {assay_id}',
            description=f'conclusion 1 about investigation {ref_id} was drawn from dataset 1 of assay {assay_id}',
            investigations=investigation.akc_id,
            datasets=dataset.akc_id,
            result=row['Assay']['Qualitative Measurement'],
            data_location_type=None,
            data_location_value=row['Assay']['Location of Assay Data in Reference'],
            organism=row['Host']['Name'],
            experiment_type=curie(row['Assay']['IRI']) # TODO: use label
        )

        container.study_arms[arm.akc_id] = arm
        container.study_events[study_event.akc_id] = study_event
        container.participants[participant.akc_id] = participant
        container.life_events[life_event_1.akc_id] = life_event_1
        container.life_events[life_event_2.akc_id] = life_event_2
        container.immune_exposures[immune_exposure.akc_id] = immune_exposure
        # container.assessments[assessment.id] = assessment
        container.specimens[specimen.akc_id] = specimen
        container.assays[assay.akc_id] = assay
        container.datasets[dataset.akc_id] = dataset
        container.conclusions[conclusion.akc_id] = conclusion
        container.epitopes[epitope.akc_id] = epitope
        for chain in chains:
            container.chains[chain.akc_id] = chain
        for tcell_receptor in tcell_receptors:
            container.ab_tcell_receptors[tcell_receptor.akc_id] = tcell_receptor
            
        #break
        row_cnt += 1
        if row_cnt % 1000 == 0:
            print(f"Processed {row_cnt} rows from {tcell_path}")
        if row_cnt == 2000:
            break

    yaml_dumper.dump(container, yaml_path)

    # Write everything to JSONL
    container_fields = [x.name for x in dataclasses.fields(container)]
    for container_field in container_fields:
        with open(f'jsonl/{container_field}.jsonl', 'w') as f:
            for key in container[container_field]:
                s = json.loads(json_dumper.dumps(container[container_field][key]))
                f.write(json.dumps(s))
                f.write('\n')

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
