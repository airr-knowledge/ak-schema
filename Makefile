MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

# environment variables
.EXPORT_ALL_VARIABLES:
ifdef LINKML_ENVIRONMENT_FILENAME
include ${LINKML_ENVIRONMENT_FILENAME}
else
include config.public.mk
endif

RUN = uv run
SCHEMA_NAME = $(LINKML_SCHEMA_NAME)
SOURCE_SCHEMA_PATH = $(LINKML_SCHEMA_SOURCE_DIR)/$(SCHEMA_NAME).yaml
SOURCE_SCHEMA_DIR = $(LINKML_SCHEMA_SOURCE_DIR)
SRC = src
DEST = project
PYMODEL = $(SRC)/$(SCHEMA_NAME)/datamodel
DOCDIR = docs
DOCTEMPLATES = $(SRC)/docs/templates
EXAMPLEDIR = examples

SQL_DDL_PATH = $(DEST)/sqlddl/ak_schema.sql
POSTGRESQL_DDL_PATH = $(DEST)/sqlddl/ak_postgres_schema.sql

# Use += to append variables from the variables file
CONFIG_YAML =
ifdef LINKML_GENERATORS_CONFIG_YAML
CONFIG_YAML += "--config-file"
CONFIG_YAML += ${LINKML_GENERATORS_CONFIG_YAML}
endif

GEN_DOC_ARGS =
ifdef LINKML_GENERATORS_DOC_ARGS
GEN_DOC_ARGS += ${LINKML_GENERATORS_DOC_ARGS}
endif

GEN_OWL_ARGS =
ifdef LINKML_GENERATORS_OWL_ARGS
GEN_OWL_ARGS += ${LINKML_GENERATORS_OWL_ARGS}
endif

GEN_JAVA_ARGS =
ifdef LINKML_GENERATORS_JAVA_ARGS
GEN_JAVA_ARGS += ${LINKML_GENERATORS_JAVA_ARGS}
endif

GEN_TS_ARGS =
ifdef LINKML_GENERATORS_TYPESCRIPT_ARGS
GEN_TS_ARGS += ${LINKML_GENERATORS_TYPESCRIPT_ARGS}
endif


# basename of a YAML file in model/
.PHONY: all clean setup gen-project gen-examples gendoc git-init-add git-init git-add git-commit git-status

# note: "help" MUST be the first target in the file,
# when the user types "make" they should get help info
help: status
	@echo ""
	@echo "Setup:"
	@echo "make setup -- initial setup (run this first)"
	@echo "make install -- install dependencies"
	@echo "make update -- updates linkml version"
	@echo "make help -- show this help"
	@echo "make status -- project status"
	@echo ""
	@echo "Build:"
	@echo "make all -- generates all project artefacts"
	@echo "make sqlddl -- make SQL DDL"
	@echo "make site -- makes site locally"
	@echo "make docker -- build docker image"
	@echo ""
	@echo "Testing:"
	@echo "make test -- runs tests"
	@echo "make lint -- perform linting"
	@echo "make testdoc -- builds docs and runs local test server"
	@echo "make deploy -- deploys site"
	@echo ""

status: check-config
	@echo "Project: $(SCHEMA_NAME)"
	@echo "Source: $(SOURCE_SCHEMA_PATH)"

# generate products and add everything to github
setup: check-config git-init install gen-project gen-examples gendoc git-add git-commit

# install any dependencies required for building
install:
	poetry install
.PHONY: install

# build docker image
docker:
	docker build . -t airrknowledge/ak-schema
.PHONY: docker

# ---
# Project Synchronization
# ---
#
# check we are up to date
check: copier-check
copier-check:
	copier update --trust --skip-answered --skip-tasks --pretend

update: update-template update-linkml
update-template:
	copier update --trust --skip-answered --skip-tasks

# todo: consider pinning to template
update-linkml:
	poetry add -D linkml@latest

# EXPERIMENTAL
create-data-harmonizer:
	npm init data-harmonizer $(SOURCE_SCHEMA_PATH)

# generate linkml without imports
$(SOURCE_SCHEMA_PATH): src/ak_schema/schema/ak_top.yaml
	mkdir -p project/linkml
	$(RUN) gen-linkml -f yaml --no-materialize-attributes $< -o $@

# generate SQL DDL
sqlddl: src/ak_schema/schema/ak_top_sqlddl.yaml
	mkdir -p project/linkml
	# generate schema without the global container (would be better if gen-sqltables supported a schema subset)
	$(RUN) gen-linkml -f yaml --no-materialize-attributes $< -o $(SOURCE_SCHEMA_PATH)
	mkdir -p project/sqlddl
	# default dialect
	$(RUN) gen-sqltables project/linkml/ak_schema.yaml > $(SQL_DDL_PATH).txt
	tail --lines=+2 $(SQL_DDL_PATH).txt | sed -e 's/DATETIME/TIMESTAMP WITHOUT TIME ZONE/g' | sed -e 's/"Investigation_akc_id"/investigation_akc_id/g' > $(SQL_DDL_PATH)
	rm -f $(SQL_DDL_PATH).txt
	# postgresql dialect
	$(RUN) gen-sqltables --dialect postgresql project/linkml/ak_schema.yaml > $(POSTGRESQL_DDL_PATH).txt
	tail --lines=+2 $(POSTGRESQL_DDL_PATH).txt > $(POSTGRESQL_DDL_PATH)
	rm -f $(POSTGRESQL_DDL_PATH).txt
	# regenerate original schema
	$(RUN) gen-linkml -f yaml --no-materialize-attributes src/ak_schema/schema/ak_top.yaml -o $(SOURCE_SCHEMA_PATH)

all: site
site: gen-project gendoc
%.yaml: gen-project
deploy: all mkd-gh-deploy

# In future this will be done by conversion
gen-examples:
	cp -r src/data/examples/* $(EXAMPLEDIR)

# generates all project files

gen-project: $(SOURCE_SCHEMA_PATH) $(PYMODEL)
	$(RUN) gen-project ${CONFIG_YAML} -d $(DEST) $(SOURCE_SCHEMA_PATH) && mv $(DEST)/*.py $(PYMODEL)


# non-empty arg triggers owl (workaround https://github.com/linkml/linkml/issues/1453)
ifneq ($(strip ${GEN_OWL_ARGS}),)
	mkdir -p ${DEST}/owl || true
	$(RUN) gen-owl ${GEN_OWL_ARGS} $(SOURCE_SCHEMA_PATH) >${DEST}/owl/${SCHEMA_NAME}.owl.ttl
endif
# non-empty arg triggers java
ifneq ($(strip ${GEN_JAVA_ARGS}),)
	$(RUN) gen-java ${GEN_JAVA_ARGS} --output-directory ${DEST}/java/ $(SOURCE_SCHEMA_PATH)
endif
# non-empty arg triggers typescript
ifneq ($(strip ${GEN_TS_ARGS}),)
	mkdir -p ${DEST}/typescript || true
	$(RUN) gen-typescript ${GEN_TS_ARGS} $(SOURCE_SCHEMA_PATH) >${DEST}/typescript/${SCHEMA_NAME}.ts
endif

test: test-schema test-python test-examples

test-schema: $(SOURCE_SCHEMA_PATH)
	$(RUN) gen-project ${CONFIG_YAML} -d tmp $(SOURCE_SCHEMA_PATH)

test-python:
	$(RUN) python -m pytest

lint:
	$(RUN) linkml-lint $(SOURCE_SCHEMA_PATH)

check-config:
ifndef LINKML_SCHEMA_NAME
	$(error **Project not configured**:\n\n - See '.env.public'\n\n)
else
	$(info Ok)
endif

convert-examples-to-%:
	$(patsubst %, $(RUN) linkml-convert  % -s $(SOURCE_SCHEMA_PATH) -C Person, $(shell ${SHELL} find src/data/examples -name "*.yaml"))

examples/%.yaml: src/data/examples/%.yaml
	$(RUN) linkml-convert -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@
examples/%.json: src/data/examples/%.yaml
	$(RUN) linkml-convert -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@
examples/%.ttl: src/data/examples/%.yaml
	$(RUN) linkml-convert -P EXAMPLE=http://example.org/ -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@

test-examples: examples/output

examples/output: $(SOURCE_SCHEMA_PATH)
	mkdir -p $@
	$(RUN) linkml-run-examples \
		--output-formats json \
		--output-formats yaml \
		--counter-example-input-directory src/data/examples/invalid \
		--input-directory src/data/examples/valid \
		--output-directory $@ \
		--schema $< > $@/README.md

# Test documentation locally
serve: mkd-serve

# Python datamodel
$(PYMODEL):
	mkdir -p $@


$(DOCDIR):
	mkdir -p $@

gendoc: $(DOCDIR)
	cp -rf $(SRC)/docs/files/* $(DOCDIR) ; \
	$(RUN) gen-doc ${GEN_DOC_ARGS} -d $(DOCDIR) $(SOURCE_SCHEMA_PATH)

testdoc: gendoc serve

MKDOCS = $(RUN) mkdocs
mkd-%:
	$(MKDOCS) $*

git-init-add: git-init git-add git-commit git-status
git-init:
	git init
	git add .
git-commit:
	git commit -m 'chore: make setup was run' -a
git-status:
	git status

clean:
	rm -rf $(DEST)
	rm -rf tmp
	rm -fr $(DOCDIR)/*
	rm -fr $(PYMODEL)/*

include project.Makefile
