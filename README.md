# ak-schema

AIRR Knowledge Data Model

## Website

[https://airr-knowledge.github.com/ak-schema](https://airr-knowledge.github.com/ak-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [ak_schema](src/ak_schema)
    * [schema](src/ak_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/ak_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

Use the docker container to have a consistent development environment.

* `docker pull airrknowledge/ak-schema:tag`: pull published container for specific tagged version.
* `docker pull airrknowledge/ak-schema`: pull published container with latest code.
* `docker build . -t airrknowledge/ak-schema`: build container with local code.
* `docker run -v $PWD:/work -it airrknowledge/ak-schema bash`: run container shell with local code mounted at /work.

With the container shell, use the `make` command to generate project artefacts:

* `make`: display help with available make targets
* `make all`: generates all the project artefacts
* `make test`: run tests
* `make docker`: builds docker image

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
