
import dataclasses
import click
import csv
import airr
import os
import hashlib

from linkml_runtime.dumpers import yaml_dumper, json_dumper, tsv_dumper
from ak_schema import *

adc_cache_dir = '/work/data/immune/ADC/cache'

def make_chain(container, akc_id, obj):
    chain = Chain(
        f'AKC:{akc_id}',
        complete_vdj = obj['complete_vdj'],
        sequence = obj['sequence'],
        sequence_aa = obj['sequence_aa'],
        chain_type = ChainType(obj['locus']),
        junction_aa = obj['junction_aa'],
        v_call = obj['v_call'],
        j_call = obj['j_call'],
    )
    container.chains[f'AKC:{akc_id}'] = chain
    return chain

def make_receptor(container, akc_id, chains):

    if len(chains) != 2:
        print('ERROR: make_receptor assumes only 2 chains.')
        return None

    receptor = None

    # T cell receptors
    if str(chains[0]['chain']['chain_type']) == 'TRB' and str(chains[1]['chain']['chain_type']) == 'TRA':
        receptor = AlphaBetaTCR(
            f'AKC:{akc_id}',
            TRA_chain=chains[1]['chain']['akc_id'],
            TRB_chain=chains[0]['chain']['akc_id']
        )
        container.ab_tcell_receptors[f'AKC:{akc_id}'] = receptor
    elif str(chains[1]['chain']['chain_type']) == 'TRB' and str(chains[0]['chain']['chain_type']) == 'TRA':
        receptor = AlphaBetaTCR(
            f'AKC:{akc_id}',
            TRA_chain=chains[0]['chain']['akc_id'],
            TRB_chain=chains[1]['chain']['akc_id']
        )
        container.ab_tcell_receptors[f'AKC:{akc_id}'] = receptor
    elif str(chains[0]['chain']['chain_type']) == 'TRG' and str(chains[1]['chain']['chain_type']) == 'TRD':
        receptor = GammaDeltaTCR(
            f'AKC:{akc_id}',
            TRG_chain=chains[0]['chain']['akc_id'],
            TRD_chain=chains[1]['chain']['akc_id']
        )
        container.gd_tcell_receptors[f'AKC:{akc_id}'] = receptor
    elif str(chains[1]['chain']['chain_type']) == 'TRG' and str(chains[0]['chain']['chain_type']) == 'TRD':
        receptor = GammaDeltaTCR(
            f'AKC:{akc_id}',
            TRG_chain=chains[1]['chain']['akc_id'],
            TRD_chain=chains[0]['chain']['akc_id']
        )
        container.gd_tcell_receptors[f'AKC:{akc_id}'] = receptor

    # B cell receptors
    elif str(chains[0]['chain']['chain_type']) == 'IGH':
        if str(chains[1]['chain']['chain_type']) == 'IGK':
            receptor = BCellReceptor(
                f'AKC:{akc_id}',
                IGH_chain=chains[0]['chain']['akc_id'],
                IGK_chain=chains[1]['chain']['akc_id']
            )
            container.bcell_receptors[f'AKC:{akc_id}'] = receptor
        elif str(chains[1]['chain']['chain_type']) == 'IGL':
            receptor = BCellReceptor(
                f'AKC:{akc_id}',
                IGH_chain=chains[0]['chain']['akc_id'],
                IGL_chain=chains[1]['chain']['akc_id']
            )
            container.bcell_receptors[f'AKC:{akc_id}'] = receptor
    elif str(chains[1]['chain']['chain_type']) == 'IGH':
        if str(chains[0]['chain']['chain_type']) == 'IGK':
            receptor = BCellReceptor(
                f'AKC:{akc_id}',
                IGH_chain=chains[1]['chain']['akc_id'],
                IGK_chain=chains[0]['chain']['akc_id']
            )
            container.bcell_receptors[f'AKC:{akc_id}'] = receptor
        elif str(chains[0]['chain']['chain_type']) == 'IGL':
            receptor = BCellReceptor(
                f'AKC:{akc_id}',
                IGH_chain=chains[1]['chain']['akc_id'],
                IGL_chain=chains[0]['chain']['akc_id']
            )
            container.bcell_receptors[f'AKC:{akc_id}'] = receptor
        else:
            print('ERROR: unknown IG chain')


    return receptor

@click.command()
@click.argument('output')
def receptor_integrate(output):
    """Convert ADC rearrangements to AK chains and receptors."""

    exact_match = {}
    exact_aa_match = {}
    junction_exact_match = {}
    junction_exact_aa_match = {}
    junction_exact_aa_and_vj_match = {}
    studies = os.listdir(adc_cache_dir)

    container = AIRRKnowledgeCommons()

    akc_id = 1
    tot_row_cnt = 0
    for study in studies:
        if study == '.DS_Store':
            continue
        print('Processing study cache:', study)

        # Load the AIRR data
        row_cnt = 0
        data = airr.read_airr(adc_cache_dir + '/' + study + '/repertoires.airr.json')
        # loop through the repertoires
        for rep in data['Repertoire']:
            print('Processing repertoire:', rep['repertoire_id'])

            # match up paired chains using cell_id, but only within the repertoire
            cell_id = {}

            reader = airr.read_rearrangement(adc_cache_dir + '/' + study + '/' + rep['repertoire_id'] + '.airr.tsv')
            prod_cnt = 0
            for row in reader:
                row_cnt = row_cnt + 1
                #print(row)
                #break

                if not row['productive']:
                    continue
                if row.get('junction_aa') is None:
                    continue
                if len(row['junction_aa']) < 3:
                    continue
                cnt = 1
                if row['duplicate_count']:
                    cnt = row['duplicate_count']

                # TODO: if we stick with letters then need to canonicalize it, uppercase etc 
                # exact nucleotide sequence match, most stringent
                h = hashlib.sha256(row['sequence'].encode('ascii')).hexdigest()
                if exact_match.get(h) is None:
                    exact_match[h] = { 'chain': make_chain(container, akc_id, row), 'count': cnt }
                    akc_id += 1
                chain = exact_match[h]
                #print(chain)

                # exact aa sequence match
                h = hashlib.sha256(row['sequence_aa'].encode('ascii')).hexdigest()
                if exact_aa_match.get(h) is None:
                    exact_aa_match[h] = { 'chains': [ chain ] }
                else:
                    exact_aa_match[h]['chains'].append(chain)

                # exact CDR3 nucleotide sequence match, don't bother with hash
                h = row['junction']
                if junction_exact_match.get(h) is None:
                    junction_exact_match[h] = { 'chains': [ chain ] }
                else:
                    junction_exact_match[h]['chains'].append(chain)

                # exact CDR3 aa sequence match, don't bother with hash
                h = row['junction_aa']
                if junction_exact_aa_match.get(h) is None:
                    junction_exact_aa_match[h] = { 'chains': [ chain ] }
                else:
                    junction_exact_aa_match[h]['chains'].append(chain)

                # exact CDR3 aa sequence and V and J alleles, use separator just in case
                c = row['junction_aa'] + '|' + row['v_call'] + '|' + row['j_call']
                h = hashlib.sha256(c.encode('ascii')).hexdigest()
                if junction_exact_aa_and_vj_match.get(h) is None:
                    junction_exact_aa_and_vj_match[h] = { 'chains': [ chain ] }
                else:
                    junction_exact_aa_and_vj_match[h]['chains'].append(chain)

                if row['cell_id'] is not None:
                    if cell_id.get(row['cell_id']) is None:
                        cell_id[row['cell_id']] = [ chain ]
                    else:
                        cell_id[row['cell_id']].append(chain)

                prod_cnt = prod_cnt + 1
                if prod_cnt % 10000 == 0:
                    print('Processed', prod_cnt, 'productive rearrangements.')


            # generate receptors for pairs
            # we create the receptors for single chains in the outer loop
            print(len(cell_id), 'unique cell ids')
            dist = [ 0, 0, 0, 0 ]
            for c in cell_id:
                lenc = len(cell_id[c])
                if lenc < 2: # validation error?
                    dist[0] += 1
                elif lenc == 3:
                    dist[2] += 1
                elif lenc > 3:
                    dist[3] += 1
                else: # 2 chains, obvious case
                    dist[1] += 1
                    make_receptor(container, akc_id, cell_id[c])
                    akc_id += 1

            print('cell_id distribution:', dist)

            print(prod_cnt, 'productive rearrangements for repertoire:', rep['repertoire_id'])
            print(row_cnt, 'records for study cache:', study)
            break

    # single chain

    print()
    print(len(container['chains']), 'total chains')
    print(len(container['ab_tcell_receptors']), 'total alpha/beta TCRs')
    print(len(container['gd_tcell_receptors']), 'total gamma/delta TCRs')
    print(len(container['bcell_receptors']), 'total BCRs')
    print()
    print(len(exact_match), 'nucleotide match')
    print(len(junction_exact_match), 'junction nucleotide match')
    print(len(exact_aa_match), 'aa match')
    print(len(junction_exact_aa_match), 'junction aa match')
    print(len(junction_exact_aa_and_vj_match), 'junction aa and V/J gene match')
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
    receptor_integrate()
#    convert()
