
.PHONY: all
all: example.yaml example.json example.ttl

tsv/:
	mkdir -p $@

ak_schema.py: ../../src/ak_schema/schema/ak_schema.yaml
	gen-python $< > $@

example.yaml: ak_schema.py convert.py tcell.tsv | tsv/
	python $(wordlist 2,3,$^) $@

example.json: ../../src/ak_schema/schema/ak_schema.yaml example.yaml
	linkml-convert -s $< -C Container -t json $(word 2,$^) > $@

example.ttl: ../../src/ak_schema/schema/ak_schema.yaml example.yaml
	linkml-convert -s $< -C Container -t rdf $(word 2,$^) > $@
