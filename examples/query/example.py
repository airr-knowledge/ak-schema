
import dataclasses
import click
import csv
import uuid
import json

from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.dumpers import yaml_dumper, json_dumper, tsv_dumper
from linkml_runtime.loaders import json_loader, yaml_loader

# AK schema data classes
from ak_schema import *

# for access to linkml metadata for the AK schema
ak_schema_view = SchemaView("../../project/linkml/ak_schema.yaml")

def load_akc_objects(container, container_field, container_class, path):
    container_slot = ak_schema_view.get_slot(container_field)
    tname = container_slot.range
    akc_file = f'{path}/{tname}.jsonl'
    with open(akc_file, 'r') as f:
        for line in f:
            #print(line)
            x = json.loads(line)
            y = json_loader.load_any(x[container_field], container_class)
            if container_field == 'references':
                if container[container_field].get(y.source_uri) is None:
                    container[container_field][y.source_uri] = y
            else:
                if container[container_field].get(y.akc_id) is None:
                    container[container_field][y.akc_id] = y

# load up IEDB objects from the transformed AKC json
def load_iedb_container(container):
    path = 'iedb_jsonl'
    load_akc_objects(container, 'investigations', Investigation, path)
    print(f"Loaded example data with {len(container['investigations'])} investigations")
    load_akc_objects(container, 'references', Reference, path)
    load_akc_objects(container, 'study_arms', StudyArm, path)
    load_akc_objects(container, 'study_events', StudyEvent, path)
    load_akc_objects(container, 'participants', Participant, path)
    load_akc_objects(container, 'life_events', LifeEvent, path)
    load_akc_objects(container, 'immune_exposures', ImmuneExposure, path)
    load_akc_objects(container, 'specimens', Specimen, path)
    load_akc_objects(container, 'assays', TCellReceptorEpitopeBindingAssay, path)
    load_akc_objects(container, 'ab_tcell_receptors', AlphaBetaTCR, path)
    print(f"Loaded example data with {len(container['ab_tcell_receptors'])} AlphaBetaTCR")
    load_akc_objects(container, 'epitopes', PeptidicEpitope, path)
    print(f"Loaded example data with {len(container['epitopes'])} epitopes")
    load_akc_objects(container, 'chains', Chain, path)
    print(f"Loaded example data with {len(container['chains'])} chains")
    return

# load up ADC objects from the transformed AKC json
def load_adc_container(container):
    path = '2314581927515778580-242ac117-0001-012'
    # TODO: should just do a loop, but not sure how to get the class
    load_akc_objects(container, 'investigations', Investigation, path)
    print(f"Loaded example data with {len(container['investigations'])} investigations")
    load_akc_objects(container, 'references', Reference, path)
    load_akc_objects(container, 'study_arms', StudyArm, path)
    load_akc_objects(container, 'study_events', StudyEvent, path)
    load_akc_objects(container, 'participants', Participant, path)
    load_akc_objects(container, 'life_events', LifeEvent, path)
    load_akc_objects(container, 'immune_exposures', ImmuneExposure, path)
    load_akc_objects(container, 'specimens', Specimen, path)
    #load_akc_objects(container, 'specimen_processings', CellIsolationProcessing)
    load_akc_objects(container, 'assays', AIRRSequencingAssay, path)
    load_akc_objects(container, 'sequence_data', AIRRSequencingData, path)
    load_akc_objects(container, 'ab_tcell_receptors', AlphaBetaTCR, path)
    print(f"Loaded example data with {len(container['ab_tcell_receptors'])} AlphaBetaTCR")
    load_akc_objects(container, 'chains', Chain, path)
    print(f"Loaded example data with {len(container['chains'])} chains")

@click.command()
@click.argument('yaml_path')
def create_object(yaml_path):
    """Construct an example query object for AK API and save to YAML."""

    # we load up some actual AKC data
    container = AIRRKnowledgeCommons()
    load_adc_container(container)

    reader = csv.DictReader(open('2314581927515778580-242ac117-0001-012/Assay_tcell_receptors.csv', 'r'))
    for row in reader:
        break
    print(row)
    assay_id = row['assay_akc_id']
    tcr_id = row['tcell_receptors_akc_id']
    print(container['assays'][row['assay_akc_id']])

    assay = container['assays'][assay_id]
    specimen_id = assay['specimen']
    specimen = container['specimens'][specimen_id]
    life_event = container['life_events'][specimen['life_event']]
    participant = container['participants'][life_event['participant']]
    study_arm = container['study_arms'][participant['study_arm']]
    investigation = container['investigations'][study_arm['investigation']]
    investigation.participants = None
#    experiment = QueryExperiment(akc_id=assay_id, assay=assay, specimen=specimen, participant=participant, investigation=investigation)
    experiment = QueryExperiment(akc_id=assay_id)
    for field in dataclasses.fields(assay):
        print(field.name)
        setattr(experiment, field.name, getattr(assay, field.name))
    experiment.specimen = specimen
    experiment.participant = participant
    experiment.investigation = investigation
#    experiment = QueryExperiment(akc_id=assay_id, specimen=specimen, participant=participant, investigation=investigation)

    ab_receptor = container['ab_tcell_receptors'][tcr_id]
    #print(container['chains'][ab_receptor.tra_chain])
    #receptor = QueryAlphaBetaTCR(akc_id=tcr_id, tra_chain=Chain(akc_id=ab_receptor.tra_chain))
    #receptor = QueryAlphaBetaTCR(akc_id=tcr_id, tra_chain=ab_receptor.tra_chain)
    receptor = QueryAlphaBetaTCR(akc_id=tcr_id,
                                 tra_chain=container['chains'][ab_receptor.tra_chain],
                                 trb_chain=container['chains'][ab_receptor.trb_chain])
    #print(receptor)

#    tcr = QueryTCR(receptor=container['ab_tcell_receptors'][tcr_id])
#    tcr['receptor']['tra_chain'] = container['chains'][tcr.receptor.tra_chain]
    tcr = QueryTCR(receptor=receptor)
    obj = QueryObject(tcr=tcr, assay=experiment)
    print(obj)
    #print(container['chains'][obj.tcr.receptor.tra_chain])

    print(f"Writing output file: {yaml_path}")
    yaml_dumper.dump(obj, yaml_path)
    json_path = yaml_path.replace('.yaml','.json')
    print(f"Writing output file: {json_path}")
    json_dumper.dump(obj, json_path)

@click.command()
@click.argument('yaml_path')
def create_iedb_object(yaml_path):
    """Construct an example query object for AK API and save to YAML."""

    # we load up some actual AKC data
    container = AIRRKnowledgeCommons()
    load_iedb_container(container)

    for assay_id in container['assays']:
        break
    print(assay_id)
    assay = container['assays'][assay_id]
    specimen_id = assay['specimen']
    specimen = container['specimens'][specimen_id]
    life_event = container['life_events'][specimen['life_event']]
    participant = container['participants'][life_event['participant']]
    #study_arm = container['study_arms'][participant['study_arm']]
    #investigation = container['investigations'][study_arm['investigation']]
    #experiment = QueryExperiment(akc_id=assay_id, assay=assay, specimen=specimen, participant=participant)
    experiment = QueryExperiment(akc_id=assay_id)
    for field in dataclasses.fields(assay):
        print(field.name)
        setattr(experiment, field.name, getattr(assay, field.name))
    experiment.specimen = specimen
    experiment.participant = participant
    #experiment.investigation = investigation

    epitope_id = container['assays'][assay_id]['epitope']
    tcr_id = container['assays'][assay_id]['tcell_receptors'][0]
    print(epitope_id)
    print(tcr_id)

    ab_receptor = container['ab_tcell_receptors'][tcr_id]
    receptor = QueryAlphaBetaTCR(akc_id=tcr_id,
                                 tra_chain=container['chains'][ab_receptor.tra_chain],
                                 trb_chain=container['chains'][ab_receptor.trb_chain])
    epitope = container['epitopes'][epitope_id]
    tcr = QueryTCR(receptor=receptor, epitope=epitope)

    obj = QueryObject(tcr=tcr, assay=experiment)
    print(obj)
    #print(container['chains'][obj.tcr.receptor.tra_chain])

    print(f"Writing output file: {yaml_path}")
    yaml_dumper.dump(obj, yaml_path)
    json_path = yaml_path.replace('.yaml','.json')
    print(f"Writing output file: {json_path}")
    json_dumper.dump(obj, json_path)

if __name__ == "__main__":
    #create_object()
    create_iedb_object()
