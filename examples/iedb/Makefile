
.PHONY: all
all: example.yaml example.json example.ttl

tsv/:
	mkdir -p $@
	mkdir -p $@

ak_schema.py: ../../project/linkml/ak_schema.yaml
	gen-python $< > $@

example.yaml: ak_schema.py convert.py tcell.tsv tcr.tsv | tsv/
	python $(wordlist 2,4,$^) $@

example.json: ../../project/linkml/ak_schema.yaml example.yaml
	linkml-convert -s $< -C AIRRKnowledgeCommons -t json $(word 2,$^) > $@

example.ttl: ../../project/linkml/ak_schema.yaml example.yaml
	linkml-convert -s $< -C AIRRKnowledgeCommons -t rdf $(word 2,$^) > $@

full: iedb_tcr.yaml

iedb_tcr.yaml: ak_schema.py convert.py tcell_full_v3.tsv tcr_full_v3.tsv | tsv/
	python $(wordlist 2,4,$^) $@
