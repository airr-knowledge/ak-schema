# Background

This code is designed to take AIRR Repertoire data and transform
that data to the AIRR Knowledge Commons data model. 

This code is based on the iReceptor data loader available here:

https://github.com/sfu-ireceptor/dataloading-mongo

This code is developed with the license that is included in this
directory.

# Usage

Get a set of repertoires, 8 in this case from covid19-1.ireceptor.org

curl -d '{"size":8}' https://covid19-1.ireceptor.org/airr/v1/repertoire > covid19-1-8.json

or all the repertoires from a given study from vdjserver.org

curl -H 'content-type: application/json' -d '{"filters":{"op":"=", "content": {"field":"study.study_id", "value":"PRJNA300878"}}}' https://vdjserver.org/airr/v1/repertoire > vdjserver-PRJNA300878.json

Convert the data to LinkML using the AKC schema.

python dataloader.py -v --repertoire -f covid19-1-8.json   --mapfile AIRR-iReceptorMapping-v1.4-2024-07-30.txt

AIRR mapping file is custom at the moment from the AKC branch in github.

https://github.com/sfu-ireceptor/config/tree/AKC

Needs to be run in the docker container as documented here:

https://github.com/airr-knowledge/ak-schema/blob/main/README.md

sudo docker run -v $PWD:/work -it airrknowledge/ak-schema bash

If you need to build the container:

sudo docker build -f Dockerfile -t airrknowledge/ak-schema:latest .

Need to build the ak_schema.py file as per this command (inside the container).

gen-python project/linkml/ak_schema.yaml > src/scripts/akc-convert/ak_schema.py

