all: studies ak_schema.py convert

clean:
	rm -rf studies
	rm ak_schema.py

studies:
	mkdir studies

ak_schema.py: ../../../project/linkml/ak_schema.yaml
	gen-python ../../../project/linkml/ak_schema.yaml > ak_schema.py

convert: PRJNA248411 PRJNA248475 PRJNA300878 PRJNA280743 PRJNA381394 PRJNA509910 PRJNA680539 PRJNA724733 PRJNA472381 PRJNA608742 IR-T1D-000003

PRJNA248411:
	bash akc-convert-study.sh ipa1.ireceptor.org PRJNA248411 studies
PRJNA248475:
	bash akc-convert-study.sh vdjserver.org PRJNA248475 studies
PRJNA300878:
	bash akc-convert-study.sh vdjserver.org PRJNA300878 studies
PRJNA280743:
	bash akc-convert-study.sh ipa1.ireceptor.org PRJNA280743 studies
PRJNA381394:
	bash akc-convert-study.sh ipa5.ireceptor.org PRJNA381394 studies
PRJNA509910:
	bash akc-convert-study.sh ipa6.ireceptor.org PRJNA509910 studies
PRJNA680539:
	bash akc-convert-study.sh vdjserver.org PRJNA680539 studies
PRJNA724733:
	bash akc-convert-study.sh vdjserver.org PRJNA724733 studies
PRJNA472381:
	bash akc-convert-study.sh vdjserver.org PRJNA472381 studies
PRJNA608742:
	bash akc-convert-study.sh vdjserver.org PRJNA608742 studies
IR-T1D-000003:
	bash akc-convert-study.sh t1d-2.ireceptor.org IR-T1D-000003 studies
