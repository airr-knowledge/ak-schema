
.PHONY: all
all: example.yaml example.json

ak_schema.py: ../../project/linkml/ak_schema.yaml
	gen-python $< > $@

example.yaml example.json: ak_schema.py example.py
	python example.py $@

clean:
	rm -f example.yaml example.json ak_schema.py
