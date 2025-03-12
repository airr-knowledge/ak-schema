
.PHONY: all
all: receptor.yaml

clean:
	rm -rf __pycache__
	rm -f ak_schema.py
	rm -f receptor.yaml receptor.json receptor.ttl
	rm -rf tsv

tsv/:
	mkdir -p $@

ak_schema.py: ../../../project/linkml/ak_schema.yaml
	gen-python $< > $@

receptor.yaml: ak_schema.py receptor.py | tsv/
	python $(wordlist 2,3,$^) $@

convert: receptor.json receptor.ttl

receptor.json: ../../../project/linkml/ak_schema.yaml receptor.yaml
	linkml-convert -s $< -C AIRRKnowledgeCommons -t json $(word 2,$^) > $@

receptor.ttl: ../../../project/linkml/ak_schema.yaml receptor.yaml
	linkml-convert -s $< -C AIRRKnowledgeCommons -t rdf $(word 2,$^) > $@
