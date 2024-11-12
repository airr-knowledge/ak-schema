# Background

This code is designed to take AIRR Repertoire data and transform
that data to the AIRR Knowledge Commons data model. 

This code is based on the iReceptor data loader available here:

https://github.com/sfu-ireceptor/dataloading-mongo
 
This code is developed with the license that is included in this directory.

# Usage

Get a set of repertoires, 8 in this case from covid19-1.ireceptor.org

```
curl -d '{"size":8}' https://covid19-1.ireceptor.org/airr/v1/repertoire > covid19-1-8.json
```
or all the repertoires from a given study from vdjserver.org
```
curl -H 'content-type: application/json' -d '{"filters":{"op":"=", "content": {"field":"study.study_id", "value":"PRJNA300878"}}}' https://vdjserver.org/airr/v1/repertoire > vdjserver-PRJNA300878.json
```
Convert the data to LinkML using the AKC schema.
```
python dataloader.py -v --repertoire -f ADC/covid19-1-1.json --mapfile ./config/AIRR-iReceptorMapping.txt
```
Convert a study from the ADC into AKC LinkML. In this case, the script will search the
ADC repository `t1d-2.ireceptor.org`, download the ADC JSON for that study, and convert
it to AKC LinkML JSON. The output of both the ADC and AKC data will be stored in the `studies` directory
in this case in files named `t1d-2.ireceptor.org_IR-T1D-000003_ADC.json` and `t1d-2.ireceptor.org_IR-T1D-000003_AKC.json`.
```
bash akc-convert-study.sh t1d-2.ireceptor.org IR-T1D-000003 studies
```
AIRR mapping file is custom at the moment from the AKC branch in github.

https://github.com/sfu-ireceptor/config/tree/AKC

# Running

This code needs to be run in the docker container as documented here:

https://github.com/airr-knowledge/ak-schema/blob/main/README.md
```
sudo docker run -v $PWD:/work -it airrknowledge/ak-schema bash
```
If you need to build the container, in the root directory of this github repo do:
```
sudo docker build -f Dockerfile -t airrknowledge/ak-schema:latest .
```
You will need a current version of the ak_schema file in the local directory, in order to generate
from the current schema perform the following from the root directory of this github repository:
```
gen-python project/linkml/ak_schema.yaml > src/scripts/akc-convert/ak_schema.py
```
