CREATE TYPE "SpeciesOntology" AS ENUM ();CREATE TYPE "BiologicalSexOntology" AS ENUM ();CREATE TYPE "AgeUnitOntology" AS ENUM ();CREATE TYPE "GeolocationOntology" AS ENUM ('US: New York', 'US: California', 'US: Connecticut', 'US: Georgia', 'US: Texas', 'Canada', 'Nicaragua', 'US: Maryland', 'US: Minnesota', 'United States of America', 'Uganda', 'China', 'England', 'India', 'US: Massachusetts', 'US: Colorado', 'Gambia', 'Papua New Guinea', 'Metropolitan France', 'Sri Lanka', 'Switzerland', 'US: Washington', 'geographic location', 'Colombia', 'US: Florida', 'US: Kansas');CREATE TYPE "StrainEnum" AS ENUM ('1D2beta', 'BALB/cByJ', 'Balb/c', 'C57BL/6', 'C57BL/6J', 'JHD-/- MRL/MpJ-Faslp', 'LDLR+/+', 'LDLR-/-', 'pet shop mouse');CREATE TYPE "LifeEventProcessOntology" AS ENUM ();CREATE TYPE "ExposureMaterialOntology" AS ENUM ();CREATE TYPE "DiseaseOntology" AS ENUM ();CREATE TYPE "MeasurementUnitOntology" AS ENUM ();CREATE TYPE "InvestigationTypeOntology" AS ENUM ();CREATE TYPE "TissueOntology" AS ENUM ();CREATE TYPE "CellSubsetOntology" AS ENUM ();CREATE TYPE "CellSpeciesOntology" AS ENUM ();CREATE TYPE "TemplateClassEnum" AS ENUM ('DNA', 'RNA');CREATE TYPE "TemplateAmountUnitOntology" AS ENUM ();CREATE TYPE "LibraryGenerationMethodEnum" AS ENUM ('PCR', 'RT(RHP)+PCR', 'RT(oligo-dT)+PCR', 'RT(oligo-dT)+TS+PCR', 'RT(oligo-dT)+TS(UMI)+PCR', 'RT(specific)+PCR', 'RT(specific)+TS+PCR', 'RT(specific)+TS(UMI)+PCR', 'RT(specific+UMI)+PCR', 'RT(specific+UMI)+TS+PCR', 'RT(specific)+TS', 'other');CREATE TYPE "CompleteSequencesEnum" AS ENUM ('partial', 'complete', 'complete+untemplated', 'mixed');CREATE TYPE "PhysicalLinkageEnum" AS ENUM ('none', 'hetero_head-head', 'hetero_tail-head', 'hetero_prelinked');CREATE TYPE "AssayTypeOntology" AS ENUM ();CREATE TYPE "CategoricalSpecificityEnum" AS ENUM ('Positive', 'Negative', 'Positive-Low', 'Positive-High', 'Positive-Intermediate');CREATE TYPE "FileTypeEnum" AS ENUM ('fasta', 'fastq');CREATE TYPE "ReadDirectionEnum" AS ENUM ('forward', 'reverse', 'mixed');CREATE TYPE "PairedReadDirectionEnum" AS ENUM ('forward', 'reverse', 'mixed');CREATE TYPE "LocusEnum" AS ENUM ('IGH', 'IGI', 'IGK', 'IGL', 'TRA', 'TRB', 'TRG', 'TRD');CREATE TYPE "ChainSimilarityTypeEnum" AS ENUM ('exact_match', 'exact_aa_match', 'cdr3_exact_match', 'cdr3_exact_aa_match', 'cdr3_exact_aa_and_vj_match');CREATE TYPE "TimePointUnitOntology" AS ENUM ();CREATE TYPE "DerivationEnum" AS ENUM ('DNA', 'RNA');CREATE TYPE "ObservationTypeEnum" AS ENUM ('direct_sequencing', 'inference_from_repertoire');CREATE TYPE "StrandEnum" AS ENUM ('+', '-');CREATE TYPE "SequenceTypeEnum" AS ENUM ('V', 'D', 'J', 'C');CREATE TYPE "InferenceTypeEnum" AS ENUM ('genomic_and_rearranged', 'genomic_only', 'rearranged_only');CREATE TYPE "SpeciesSubgroupTypeEnum" AS ENUM ('breed', 'strain', 'inbred', 'outbred', 'locational');CREATE TYPE "StatusEnum" AS ENUM ('active', 'draft', 'retired', 'withdrawn');CREATE TYPE "JCodonFrameEnum" AS ENUM ('1', '2', '3');CREATE TYPE "InferenceProcessEnum" AS ENUM ('genomic_sequencing', 'repertoire_sequencing');CREATE TYPE "MhcClassEnum" AS ENUM ('MHC-I', 'MHC-II', 'MHC-nonclassical');CREATE TYPE "GeneOntology" AS ENUM ();CREATE TYPE "StudyTypeOntology" AS ENUM ();CREATE TYPE "SexEnum" AS ENUM ('male', 'female', 'pooled', 'hermaphrodite', 'intersex');CREATE TYPE "DiseaseDiagnosisOntology" AS ENUM ();CREATE TYPE "CollectionTimePointRelativeUnitOntology" AS ENUM ();CREATE TYPE "PcrTargetLocusEnum" AS ENUM ('IGH', 'IGI', 'IGK', 'IGL', 'TRA', 'TRB', 'TRD', 'TRG');CREATE TYPE "ExpressionStudyMethodEnum" AS ENUM ('flow_cytometry', 'single-cell_transcriptome');CREATE TYPE "ReceptorTypeEnum" AS ENUM ('Ig', 'TCR');CREATE TYPE "ReceptorVariableDomain1LocusEnum" AS ENUM ('IGH', 'TRB', 'TRD');CREATE TYPE "ReceptorVariableDomain2LocusEnum" AS ENUM ('IGI', 'IGK', 'IGL', 'TRA', 'TRG');CREATE TYPE "LigandTypeEnum" AS ENUM ('MHC:peptide', 'MHC:non-peptide', 'protein', 'peptide', 'non-peptidic');CREATE TYPE "AntigenTypeEnum" AS ENUM ('protein', 'peptide', 'non-peptidic');CREATE TYPE "AntigenSourceSpeciesOntology" AS ENUM ();CREATE TYPE "MhcGene1Ontology" AS ENUM ();CREATE TYPE "MhcGene2Ontology" AS ENUM ();CREATE TYPE "ReactivityMethodEnum" AS ENUM ('SPR', 'ITC', 'ELISA', 'cytometry', 'biological_activity');CREATE TYPE "ReactivityReadoutEnum" AS ENUM ('binding_strength', 'cytokine_release', 'dissociation_constant_kd', 'on_rate', 'off_rate', 'pathogen_inhibition');CREATE TYPE "DataItemTypeEnum" AS ENUM ('sequence_reads', 'sequence_quality', 'sequence_forward_paired_reads', 'sequence_reverse_paired_reads', 'sequence', 'primer_sequence', 'forward_primer_sequence', 'reverse_primer_sequence', 'barcode_sequence', 'vdj_sequence_annotation', 'quality_statistics', 'annotation_statistics', 'assigned_clones', 'physiochemical_annotation', 'gene_usage', 'gene_combo_usage', 'length_distribution', 'diversity_profile', 'mutational_profile', 'similarity_comparison', 'study_arm_comparison', 'archive', 'compressed');CREATE TYPE "CurationalTagsEnum" AS ENUM ('likely_truncated', 'likely_full_length');CREATE TYPE "KeywordsStudyEnum" AS ENUM ('contains_ig', 'contains_tr', 'contains_paired_chain', 'contains_schema_rearrangement', 'contains_schema_clone', 'contains_schema_cell', 'contains_schema_receptor');
CREATE TABLE "AKObject" (
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "AKObject" IS 'Anything uniquely identifiable in the AKC.';COMMENT ON COLUMN "AKObject".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "ForeignObject" (
	source_uri TEXT NOT NULL, 
	PRIMARY KEY (source_uri)
);COMMENT ON TABLE "ForeignObject" IS 'An object held outside of the AK.';COMMENT ON COLUMN "ForeignObject".source_uri IS 'AKC reference to a foreign thing.';
CREATE TABLE "AIRRStandards" (
	id SERIAL NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "AIRRStandards" IS 'An object directly converted from the AIRR schema.';
CREATE TABLE "AIRRStandards_v1p5" (
	id SERIAL NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "AIRRStandards_v1p5" IS 'An object directly converted from AIRR schema version 1.5.';
CREATE TABLE "AIRRStandards_v1p6" (
	id SERIAL NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "AIRRStandards_v1p6" IS 'An object directly converted from AIRR schema version 1.6.';
CREATE TABLE "AIRRStandards_v2p0" (
	id SERIAL NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "AIRRStandards_v2p0" IS 'An object directly converted from AIRR schema version 2.0.';
CREATE TABLE "NamedThing" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "NamedThing" IS 'Name and description for AKC things.';COMMENT ON COLUMN "NamedThing".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "NamedThing".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "NamedThing".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "Process" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "Process" IS 'A generic process.';COMMENT ON COLUMN "Process".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "Process".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "Process".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "PlanSpecification" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "PlanSpecification" IS 'A plan with specified actions to meet some objectives.';COMMENT ON COLUMN "PlanSpecification".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "PlanSpecification".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "PlanSpecification".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "OntologyTable" (
	id SERIAL NOT NULL, 
	term_id TEXT NOT NULL, 
	term_label TEXT, 
	parent_term_id TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "OntologyTable" IS 'standard schema for an ontology table';COMMENT ON COLUMN "OntologyTable".term_id IS 'ontology term ID';COMMENT ON COLUMN "OntologyTable".term_label IS 'ontology term descriptive label';COMMENT ON COLUMN "OntologyTable".parent_term_id IS 'parent ID for ontology term';
CREATE TABLE "Reference" (
	title TEXT, 
	journal TEXT, 
	issue TEXT, 
	month TEXT, 
	year INTEGER, 
	pages TEXT, 
	source_uri TEXT NOT NULL, 
	PRIMARY KEY (source_uri)
);COMMENT ON TABLE "Reference" IS 'A document about an investigation.';COMMENT ON COLUMN "Reference".title IS 'The title of a reference';COMMENT ON COLUMN "Reference".journal IS 'The journal in which a reference was published';COMMENT ON COLUMN "Reference".issue IS 'The issue of the journal in which a reference was published';COMMENT ON COLUMN "Reference".month IS 'The month of the issue of the journal in which a reference was published';COMMENT ON COLUMN "Reference".year IS 'The year of the issue of the journal in which a reference was published';COMMENT ON COLUMN "Reference".pages IS 'The pages of the issue of the journal in which a reference was published';COMMENT ON COLUMN "Reference".source_uri IS 'AKC reference to a foreign thing.';
CREATE TABLE "StudyEvent" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "StudyEvent" IS 'An event that is part of the study design of an investigation.';COMMENT ON COLUMN "StudyEvent".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "StudyEvent".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "StudyEvent".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "InvestigationType" (
	id SERIAL NOT NULL, 
	term_id "InvestigationTypeOntology" NOT NULL, 
	term_label TEXT, 
	parent_term_id "InvestigationTypeOntology", 
	PRIMARY KEY (id)
);COMMENT ON TABLE "InvestigationType" IS 'None';COMMENT ON COLUMN "InvestigationType".term_id IS 'ontology term ID';COMMENT ON COLUMN "InvestigationType".term_label IS 'ontology term descriptive label';COMMENT ON COLUMN "InvestigationType".parent_term_id IS 'parent ID for ontology term';
CREATE TABLE "DataItem" (
	id SERIAL NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "DataItem" IS 'None';
CREATE TABLE "MeasurementDatum" (
	id SERIAL NOT NULL, 
	measurement_value INTEGER, 
	measurement_unit "MeasurementUnitOntology", 
	PRIMARY KEY (id)
);COMMENT ON TABLE "MeasurementDatum" IS 'None';COMMENT ON COLUMN "MeasurementDatum".measurement_value IS 'The measurement result value';COMMENT ON COLUMN "MeasurementDatum".measurement_unit IS 'The measurement result value unit';
CREATE TABLE "MeasurementCategory" (
	id SERIAL NOT NULL, 
	measurement_category TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "MeasurementCategory" IS 'None';COMMENT ON COLUMN "MeasurementCategory".measurement_category IS 'The measurement result category';
CREATE TABLE "TCellReceptorEpitopeSpecificityMeasurement" (
	id SERIAL NOT NULL, 
	measurement_category "CategoricalSpecificityEnum", 
	PRIMARY KEY (id)
);COMMENT ON TABLE "TCellReceptorEpitopeSpecificityMeasurement" IS 'None';COMMENT ON COLUMN "TCellReceptorEpitopeSpecificityMeasurement".measurement_category IS 'The measurement result category';
CREATE TABLE "DataSet" (
	id SERIAL NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "DataSet" IS 'None';
CREATE TABLE "AKDataItem" (
	type TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "AKDataItem" IS 'data item with an akc_id';COMMENT ON COLUMN "AKDataItem".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "AKDataSet" (
	type TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "AKDataSet" IS 'None';COMMENT ON COLUMN "AKDataSet".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "SequenceData" (
	type TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "SequenceData" IS 'sequence data items are given an akc_id';COMMENT ON COLUMN "SequenceData".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "AIRRSequencingData" (
	sequencing_data_id TEXT, 
	file_type "FileTypeEnum", 
	filename TEXT, 
	read_direction "ReadDirectionEnum", 
	read_length INTEGER, 
	paired_filename TEXT, 
	paired_read_direction "PairedReadDirectionEnum", 
	paired_read_length INTEGER, 
	index_filename TEXT, 
	index_length INTEGER, 
	type TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "AIRRSequencingData" IS 'None';COMMENT ON COLUMN "AIRRSequencingData".sequencing_data_id IS 'Persistent identifier of raw data stored in an archive (e.g. INSDC run ID). Data archive should  be identified in the CURIE prefix.';COMMENT ON COLUMN "AIRRSequencingData".file_type IS 'File format for the raw reads or sequences';COMMENT ON COLUMN "AIRRSequencingData".filename IS 'File name for the raw reads or sequences. The first file in paired-read sequencing.';COMMENT ON COLUMN "AIRRSequencingData".read_direction IS 'Read direction for the raw reads or sequences. The first file in paired-read sequencing.';COMMENT ON COLUMN "AIRRSequencingData".read_length IS 'Read length in bases for the first file in paired-read sequencing';COMMENT ON COLUMN "AIRRSequencingData".paired_filename IS 'File name for the second file in paired-read sequencing';COMMENT ON COLUMN "AIRRSequencingData".paired_read_direction IS 'Read direction for the second file in paired-read sequencing';COMMENT ON COLUMN "AIRRSequencingData".paired_read_length IS 'Read length in bases for the second file in paired-read sequencing';COMMENT ON COLUMN "AIRRSequencingData".index_filename IS 'File name for the index file';COMMENT ON COLUMN "AIRRSequencingData".index_length IS 'Read length in bases for the index file';COMMENT ON COLUMN "AIRRSequencingData".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "RNATranscriptomeData" (
	type TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "RNATranscriptomeData" IS 'None';COMMENT ON COLUMN "RNATranscriptomeData".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "DataTransformation" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "DataTransformation" IS 'None';COMMENT ON COLUMN "DataTransformation".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "DataTransformation".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "DataTransformation".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "Conclusion" (
	result TEXT, 
	data_location_type TEXT, 
	data_location_value TEXT, 
	organism "SpeciesOntology", 
	experiment_type TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "Conclusion" IS 'None';COMMENT ON COLUMN "Conclusion".result IS 'The content of the conclusion';COMMENT ON COLUMN "Conclusion".data_location_type IS 'The type of location where data was found, e.g. figure, table';COMMENT ON COLUMN "Conclusion".data_location_value IS 'An identifier for the location of the data, e.g. figure 2';COMMENT ON COLUMN "Conclusion".organism IS 'The type of organism that the conclusion is about';COMMENT ON COLUMN "Conclusion".experiment_type IS 'The type of experiment that supports the conclusion';COMMENT ON COLUMN "Conclusion".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "Conclusion".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "Conclusion".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "ImmuneSystem" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "ImmuneSystem" IS 'None';COMMENT ON COLUMN "ImmuneSystem".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "ImmuneSystem".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "ImmuneSystem".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "Chain" (
	species "SpeciesOntology", 
	aa_hash TEXT, 
	junction_aa_vj_allele_hash TEXT, 
	junction_aa_vj_gene_hash TEXT, 
	complete_vdj BOOLEAN, 
	sequence TEXT, 
	sequence_aa TEXT, 
	locus "LocusEnum", 
	v_call TEXT, 
	d_call TEXT, 
	j_call TEXT, 
	c_call TEXT, 
	junction_aa TEXT, 
	cdr1_aa TEXT, 
	cdr2_aa TEXT, 
	cdr3_aa TEXT, 
	cdr1_start INTEGER, 
	cdr1_end INTEGER, 
	cdr2_start INTEGER, 
	cdr2_end INTEGER, 
	cdr3_start INTEGER, 
	cdr3_end INTEGER, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "Chain" IS 'None';COMMENT ON COLUMN "Chain".species IS 'Binomial designation of subject''s species';COMMENT ON COLUMN "Chain".complete_vdj IS 'Complete VDJ flag.';COMMENT ON COLUMN "Chain".sequence IS 'Nucleotide sequence.';COMMENT ON COLUMN "Chain".sequence_aa IS 'Amino acid translation of the query nucleotide sequence.';COMMENT ON COLUMN "Chain".c_call IS 'Constant region gene with allele. If referring to a known reference sequence in a database the relevant gene/allele nomenclature should be followed (e.g., IGHG1*01 if using IMGT/GENE-DB).';COMMENT ON COLUMN "Chain".junction_aa IS 'Amino acid translation of the junction.';COMMENT ON COLUMN "Chain".cdr1_aa IS 'Amino acid translation of the cdr1 field.';COMMENT ON COLUMN "Chain".cdr2_aa IS 'Amino acid translation of the cdr2 field.';COMMENT ON COLUMN "Chain".cdr3_aa IS 'Amino acid translation of the cdr3 field.';COMMENT ON COLUMN "Chain".cdr3_end IS 'CDR3 end position in the query sequence (1-based closed interval).';COMMENT ON COLUMN "Chain".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "ImmuneReceptor" (
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "ImmuneReceptor" IS 'None';COMMENT ON COLUMN "ImmuneReceptor".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "TCellReceptor" (
	type TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "TCellReceptor" IS 'None';COMMENT ON COLUMN "TCellReceptor".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "Antigen" (
	source_protein TEXT, 
	source_organism TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "Antigen" IS 'None';COMMENT ON COLUMN "Antigen".source_protein IS 'The protein that this epitope comes from';COMMENT ON COLUMN "Antigen".source_organism IS 'The organism that the source protein comes from';COMMENT ON COLUMN "Antigen".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "Antigen".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "Antigen".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "Epitope" (
	type TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "Epitope" IS 'None';COMMENT ON COLUMN "Epitope".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "Epitope".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "Epitope".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "PeptidicEpitope" (
	sequence_aa TEXT, 
	source_protein TEXT, 
	source_organism TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "PeptidicEpitope" IS 'None';COMMENT ON COLUMN "PeptidicEpitope".sequence_aa IS 'Amino acid translation of the query nucleotide sequence.';COMMENT ON COLUMN "PeptidicEpitope".source_protein IS 'The protein that this epitope comes from';COMMENT ON COLUMN "PeptidicEpitope".source_organism IS 'The organism that the source protein comes from';COMMENT ON COLUMN "PeptidicEpitope".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "PeptidicEpitope".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "PeptidicEpitope".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "Model" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "Model" IS 'None';COMMENT ON COLUMN "Model".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "Model".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "Model".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "ConceptualModel" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "ConceptualModel" IS 'None';COMMENT ON COLUMN "ConceptualModel".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "ConceptualModel".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "ConceptualModel".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "CommunicativeModel" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "CommunicativeModel" IS 'None';COMMENT ON COLUMN "CommunicativeModel".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "CommunicativeModel".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "CommunicativeModel".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "ModelSpecification" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "ModelSpecification" IS 'None';COMMENT ON COLUMN "ModelSpecification".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "ModelSpecification".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "ModelSpecification".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "ModelingFramework" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "ModelingFramework" IS 'None';COMMENT ON COLUMN "ModelingFramework".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "ModelingFramework".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "ModelingFramework".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "Simulation" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);COMMENT ON TABLE "Simulation" IS 'None';COMMENT ON COLUMN "Simulation".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "Simulation".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "Simulation".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "TimePoint" (
	id SERIAL NOT NULL, 
	time_point_label TEXT, 
	time_point_value FLOAT, 
	time_point_unit "TimePointUnitOntology", 
	PRIMARY KEY (id)
);COMMENT ON TABLE "TimePoint" IS 'None';COMMENT ON COLUMN "TimePoint".time_point_label IS 'Informative label for the time point';COMMENT ON COLUMN "TimePoint".time_point_value IS 'Value of the time point';COMMENT ON COLUMN "TimePoint".time_point_unit IS 'Unit of the time point';
CREATE TABLE "Acknowledgement" (
	id SERIAL NOT NULL, 
	acknowledgement_id TEXT, 
	individual_full_name TEXT, 
	institution_name TEXT, 
	orcid_id TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Acknowledgement" IS 'None';COMMENT ON COLUMN "Acknowledgement".acknowledgement_id IS 'unique identifier of this Acknowledgement within the file';COMMENT ON COLUMN "Acknowledgement".individual_full_name IS 'Full name of individual';COMMENT ON COLUMN "Acknowledgement".institution_name IS 'Individual''s department and institution name';COMMENT ON COLUMN "Acknowledgement".orcid_id IS 'Individual''s ORCID identifier';
CREATE TABLE "RearrangedSequence" (
	id SERIAL NOT NULL, 
	sequence_id TEXT, 
	sequence TEXT, 
	derivation "DerivationEnum", 
	observation_type "ObservationTypeEnum", 
	curation TEXT, 
	repository_name TEXT, 
	repository_ref TEXT, 
	deposited_version TEXT, 
	sequence_start INTEGER, 
	sequence_end INTEGER, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "RearrangedSequence" IS 'None';COMMENT ON COLUMN "RearrangedSequence".sequence IS 'Nucleotide sequence.';COMMENT ON COLUMN "RearrangedSequence".derivation IS 'The class of nucleic acid that was used as primary starting material';COMMENT ON COLUMN "RearrangedSequence".observation_type IS 'The type of observation from which this sequence was drawn, such as direct sequencing or  inference from repertoire sequencing data.';COMMENT ON COLUMN "RearrangedSequence".repository_ref IS 'Queryable id or accession number of the sequence published by the repository';COMMENT ON COLUMN "RearrangedSequence".deposited_version IS 'Version number of the sequence within the repository';
CREATE TABLE "UnrearrangedSequence" (
	id SERIAL NOT NULL, 
	sequence_id TEXT, 
	sequence TEXT, 
	curation TEXT, 
	repository_name TEXT, 
	repository_ref TEXT, 
	patch_no TEXT, 
	gff_seqid TEXT, 
	gff_start INTEGER, 
	gff_end INTEGER, 
	strand "StrandEnum", 
	PRIMARY KEY (id)
);COMMENT ON TABLE "UnrearrangedSequence" IS 'None';COMMENT ON COLUMN "UnrearrangedSequence".sequence IS 'Nucleotide sequence.';COMMENT ON COLUMN "UnrearrangedSequence".repository_ref IS 'Queryable id or accession number of the sequence published by the repository';COMMENT ON COLUMN "UnrearrangedSequence".patch_no IS 'Genome assembly patch number in which this gene was determined';COMMENT ON COLUMN "UnrearrangedSequence".gff_seqid IS 'Sequence (from the assembly) of a window including the gene and preferably also the promoter region.';COMMENT ON COLUMN "UnrearrangedSequence".gff_start IS 'Genomic co-ordinates of the start of the sequence of interest described in this record in  Ensemble GFF version 3.';COMMENT ON COLUMN "UnrearrangedSequence".gff_end IS 'Genomic co-ordinates of the end of the sequence of interest described in this record in  Ensemble GFF version 3.';COMMENT ON COLUMN "UnrearrangedSequence".strand IS 'sense (+ or -)';
CREATE TABLE "SequenceDelineationV" (
	id SERIAL NOT NULL, 
	sequence_delineation_id TEXT, 
	delineation_scheme TEXT, 
	unaligned_sequence TEXT, 
	aligned_sequence TEXT, 
	fwr1_start INTEGER, 
	fwr1_end INTEGER, 
	cdr1_start INTEGER, 
	cdr1_end INTEGER, 
	fwr2_start INTEGER, 
	fwr2_end INTEGER, 
	cdr2_start INTEGER, 
	cdr2_end INTEGER, 
	fwr3_start INTEGER, 
	fwr3_end INTEGER, 
	cdr3_start INTEGER, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "SequenceDelineationV" IS 'None';COMMENT ON COLUMN "SequenceDelineationV".sequence_delineation_id IS 'Unique identifier of this SequenceDelineationV within the file. Typically, generated by the  repository hosting the record.';COMMENT ON COLUMN "SequenceDelineationV".delineation_scheme IS 'Name of the delineation scheme';COMMENT ON COLUMN "SequenceDelineationV".unaligned_sequence IS 'entire V-sequence covered by this delineation';COMMENT ON COLUMN "SequenceDelineationV".aligned_sequence IS 'Aligned sequence if this delineation provides an alignment. An aligned sequence should always be  provided for IMGT delineations.';
CREATE TABLE "AlleleDescription" (
	id SERIAL NOT NULL, 
	allele_description_id TEXT, 
	allele_description_ref TEXT, 
	maintainer TEXT, 
	lab_address TEXT, 
	release_version INTEGER, 
	release_date TIMESTAMP WITHOUT TIME ZONE, 
	release_description TEXT, 
	label TEXT, 
	sequence TEXT, 
	coding_sequence TEXT, 
	locus "LocusEnum", 
	chromosome INTEGER, 
	sequence_type "SequenceTypeEnum", 
	functional BOOLEAN, 
	inference_type "InferenceTypeEnum", 
	species "SpeciesOntology", 
	species_subgroup TEXT, 
	species_subgroup_type "SpeciesSubgroupTypeEnum", 
	status "StatusEnum", 
	subgroup_designation TEXT, 
	gene_designation TEXT, 
	allele_designation TEXT, 
	allele_similarity_cluster_designation TEXT, 
	allele_similarity_cluster_member_id TEXT, 
	j_codon_frame "JCodonFrameEnum", 
	gene_start INTEGER, 
	gene_end INTEGER, 
	utr_5_prime_start INTEGER, 
	utr_5_prime_end INTEGER, 
	leader_1_start INTEGER, 
	leader_1_end INTEGER, 
	leader_2_start INTEGER, 
	leader_2_end INTEGER, 
	v_rs_start INTEGER, 
	v_rs_end INTEGER, 
	d_rs_3_prime_start INTEGER, 
	d_rs_3_prime_end INTEGER, 
	d_rs_5_prime_start INTEGER, 
	d_rs_5_prime_end INTEGER, 
	j_cdr3_end INTEGER, 
	j_rs_start INTEGER, 
	j_rs_end INTEGER, 
	j_donor_splice INTEGER, 
	curation TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "AlleleDescription" IS 'None';COMMENT ON COLUMN "AlleleDescription".allele_description_id IS 'Unique identifier of this AlleleDescription within the file. Typically, generated by the  repository hosting the record.';COMMENT ON COLUMN "AlleleDescription".allele_description_ref IS 'Unique reference to the allele description, in standardized form (Repo:Label:Version)';COMMENT ON COLUMN "AlleleDescription".maintainer IS 'Maintainer of this sequence record';COMMENT ON COLUMN "AlleleDescription".release_date IS 'Date of this release';COMMENT ON COLUMN "AlleleDescription".release_description IS 'Brief descriptive notes of the reason for this release and the changes embodied';COMMENT ON COLUMN "AlleleDescription".sequence IS 'Nucleotide sequence.';COMMENT ON COLUMN "AlleleDescription".coding_sequence IS 'Nucleotide sequence of the core coding region, such as the coding region of a D-, J- or C- gene  or the coding region of a V-gene excluding the leader.';COMMENT ON COLUMN "AlleleDescription".chromosome IS 'chromosome on which the gene is located';COMMENT ON COLUMN "AlleleDescription".sequence_type IS 'Sequence type (V, D, J, C)';COMMENT ON COLUMN "AlleleDescription".functional IS 'True if the gene is functional, false if it is a pseudogene';COMMENT ON COLUMN "AlleleDescription".inference_type IS 'Type of inference(s) from which this gene sequence was inferred';COMMENT ON COLUMN "AlleleDescription".species IS 'Binomial designation of subject''s species';COMMENT ON COLUMN "AlleleDescription".species_subgroup IS 'Race, strain or other species subgroup to which this subject belongs';COMMENT ON COLUMN "AlleleDescription".status IS 'Status of record, assumed active if the field is not present';COMMENT ON COLUMN "AlleleDescription".subgroup_designation IS 'Identifier of the gene subgroup or clade, as (and if) defined';COMMENT ON COLUMN "AlleleDescription".gene_designation IS 'Gene number or other identifier, as (and if) defined';COMMENT ON COLUMN "AlleleDescription".allele_similarity_cluster_designation IS 'ID of the similarity cluster used in this germline set, if designated';COMMENT ON COLUMN "AlleleDescription".allele_similarity_cluster_member_id IS 'Membership ID of the allele within the similarity cluster, if a cluster is designated';COMMENT ON COLUMN "AlleleDescription".j_codon_frame IS 'Codon position of the first nucleotide in the ''coding_sequence'' field. Mandatory for J genes.  Not used for V or D genes. ''1'' means the sequence is in-frame, ''2'' means that the first bp is  missing from the first codon, and ''3'' means that the first 2 bp are missing.';COMMENT ON COLUMN "AlleleDescription".gene_start IS 'Co-ordinate in the sequence field of the first nucleotide in the coding_sequence field.';COMMENT ON COLUMN "AlleleDescription".gene_end IS 'Co-ordinate in the sequence field of the last gene-coding nucleotide in the coding_sequence field.';COMMENT ON COLUMN "AlleleDescription".utr_5_prime_start IS 'Start co-ordinate in the sequence field of the 5 prime UTR (V-genes only).';COMMENT ON COLUMN "AlleleDescription".utr_5_prime_end IS 'End co-ordinate in the sequence field of the 5 prime UTR (V-genes only).';COMMENT ON COLUMN "AlleleDescription".leader_1_start IS 'Start co-ordinate in the sequence field of L-PART1 (V-genes only).';COMMENT ON COLUMN "AlleleDescription".leader_1_end IS 'End co-ordinate in the sequence field of L-PART1 (V-genes only).';COMMENT ON COLUMN "AlleleDescription".leader_2_start IS 'Start co-ordinate in the sequence field of L-PART2 (V-genes only).';COMMENT ON COLUMN "AlleleDescription".leader_2_end IS 'End co-ordinate in the sequence field of L-PART2 (V-genes only).';COMMENT ON COLUMN "AlleleDescription".v_rs_start IS 'Start co-ordinate in the sequence field of the V recombination site (V-genes only).';COMMENT ON COLUMN "AlleleDescription".v_rs_end IS 'End co-ordinate in the sequence field of the V recombination site (V-genes only).';COMMENT ON COLUMN "AlleleDescription".d_rs_3_prime_start IS 'Start co-ordinate in the sequence field of the 3 prime D recombination site (D-genes only).';COMMENT ON COLUMN "AlleleDescription".d_rs_3_prime_end IS 'End co-ordinate in the sequence field of the 3 prime D recombination site (D-genes only).';COMMENT ON COLUMN "AlleleDescription".d_rs_5_prime_start IS 'Start co-ordinate in the sequence field of the 5 prime D recombination site (D-genes only).';COMMENT ON COLUMN "AlleleDescription".d_rs_5_prime_end IS 'End co-ordinate in the sequence field of 5 the prime D recombination site (D-genes only).';COMMENT ON COLUMN "AlleleDescription".j_cdr3_end IS 'In the case of a J-gene, the co-ordinate in the sequence field of the first nucelotide of the  conserved PHE or TRP (IMGT codon position 118).';COMMENT ON COLUMN "AlleleDescription".j_rs_start IS 'Start co-ordinate in the sequence field of J recombination site (J-genes only).';COMMENT ON COLUMN "AlleleDescription".j_rs_end IS 'End co-ordinate in the sequence field of J recombination site (J-genes only).';COMMENT ON COLUMN "AlleleDescription".j_donor_splice IS 'Co-ordinate in the sequence field of the final 3'' nucleotide of the J-REGION (J-genes only).';
CREATE TABLE "GermlineSet" (
	id SERIAL NOT NULL, 
	germline_set_id TEXT, 
	author TEXT, 
	lab_name TEXT, 
	lab_address TEXT, 
	release_version INTEGER, 
	release_description TEXT, 
	release_date TIMESTAMP WITHOUT TIME ZONE, 
	germline_set_name TEXT, 
	germline_set_ref TEXT, 
	pub_ids TEXT, 
	species "SpeciesOntology", 
	species_subgroup TEXT, 
	species_subgroup_type "SpeciesSubgroupTypeEnum", 
	locus "LocusEnum", 
	curation TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "GermlineSet" IS 'None';COMMENT ON COLUMN "GermlineSet".germline_set_id IS 'Unique identifier of the GermlineSet within this file. Typically, generated by the  repository hosting the record.';COMMENT ON COLUMN "GermlineSet".author IS 'Corresponding author';COMMENT ON COLUMN "GermlineSet".release_description IS 'Brief descriptive notes of the reason for this release and the changes embodied';COMMENT ON COLUMN "GermlineSet".release_date IS 'Date of this release';COMMENT ON COLUMN "GermlineSet".germline_set_name IS 'descriptive name of this germline set';COMMENT ON COLUMN "GermlineSet".species IS 'Binomial designation of subject''s species';COMMENT ON COLUMN "GermlineSet".species_subgroup IS 'Race, strain or other species subgroup to which this subject belongs';
CREATE TABLE "GenotypeSet" (
	id SERIAL NOT NULL, 
	receptor_genotype_set_id TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "GenotypeSet" IS 'None';COMMENT ON COLUMN "GenotypeSet".receptor_genotype_set_id IS 'A unique identifier for this Receptor Genotype Set, typically generated by the repository  hosting the schema, for example from the underlying ID of the database record.';
CREATE TABLE "Genotype" (
	id SERIAL NOT NULL, 
	receptor_genotype_id TEXT, 
	locus "LocusEnum", 
	inference_process "InferenceProcessEnum", 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Genotype" IS 'None';COMMENT ON COLUMN "Genotype".receptor_genotype_id IS 'A unique identifier within the file for this Receptor Genotype, typically generated by the  repository hosting the schema, for example from the underlying ID of the database record.';COMMENT ON COLUMN "Genotype".inference_process IS 'Information on how the genotype was acquired. Controlled vocabulary.';
CREATE TABLE "DocumentedAllele" (
	id SERIAL NOT NULL, 
	label TEXT, 
	germline_set_ref TEXT, 
	phasing INTEGER, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "DocumentedAllele" IS 'None';COMMENT ON COLUMN "DocumentedAllele".phasing IS 'Chromosomal phasing indicator. Alleles with the same value are inferred to be located on the  same chromosome.';
CREATE TABLE "UndocumentedAllele" (
	id SERIAL NOT NULL, 
	allele_name TEXT, 
	sequence TEXT, 
	phasing INTEGER, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "UndocumentedAllele" IS 'None';COMMENT ON COLUMN "UndocumentedAllele".allele_name IS 'Allele name as allocated by the inference pipeline';COMMENT ON COLUMN "UndocumentedAllele".sequence IS 'Nucleotide sequence.';COMMENT ON COLUMN "UndocumentedAllele".phasing IS 'Chromosomal phasing indicator. Alleles with the same value are inferred to be located on the  same chromosome.';
CREATE TABLE "DeletedGene" (
	id SERIAL NOT NULL, 
	label TEXT, 
	germline_set_ref TEXT, 
	phasing INTEGER, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "DeletedGene" IS 'None';COMMENT ON COLUMN "DeletedGene".phasing IS 'Chromosomal phasing indicator. Alleles with the same value are inferred to be located on the  same chromosome.';
CREATE TABLE "MHCGenotypeSet" (
	id SERIAL NOT NULL, 
	mhc_genotype_set_id TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "MHCGenotypeSet" IS 'None';COMMENT ON COLUMN "MHCGenotypeSet".mhc_genotype_set_id IS 'A unique identifier for this MHCGenotypeSet';
CREATE TABLE "MHCGenotype" (
	id SERIAL NOT NULL, 
	mhc_genotype_id TEXT, 
	mhc_class "MhcClassEnum", 
	mhc_genotyping_method TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "MHCGenotype" IS 'None';COMMENT ON COLUMN "MHCGenotype".mhc_genotype_id IS 'A unique identifier for this MHCGenotype, assumed to be unique in the context of the study';COMMENT ON COLUMN "MHCGenotype".mhc_genotyping_method IS 'Information on how the genotype was determined. The content of this field should come from a list of recommended terms provided in the AIRR Schema documentation.';
CREATE TABLE "MHCAllele" (
	id SERIAL NOT NULL, 
	allele_designation TEXT, 
	gene "GeneOntology", 
	reference_set_ref TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "MHCAllele" IS 'None';COMMENT ON COLUMN "MHCAllele".gene IS 'The MHC gene to which the described allele belongs';COMMENT ON COLUMN "MHCAllele".reference_set_ref IS 'Repository and list from which it was taken (issuer/name/version)';
CREATE TABLE "Study" (
	id SERIAL NOT NULL, 
	study_id TEXT, 
	study_title TEXT, 
	study_type "StudyTypeOntology", 
	study_description TEXT, 
	inclusion_exclusion_criteria TEXT, 
	grants TEXT, 
	study_contact TEXT, 
	collected_by TEXT, 
	lab_name TEXT, 
	lab_address TEXT, 
	submitted_by TEXT, 
	pub_ids TEXT, 
	adc_publish_date TIMESTAMP WITHOUT TIME ZONE, 
	adc_update_date TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Study" IS 'None';COMMENT ON COLUMN "Study".study_id IS 'Unique ID assigned by study registry such as one of the International Nucleotide Sequence Database Collaboration (INSDC) repositories.';COMMENT ON COLUMN "Study".study_title IS 'Descriptive study title';COMMENT ON COLUMN "Study".study_type IS 'Type of study design';COMMENT ON COLUMN "Study".study_description IS 'Generic study description';COMMENT ON COLUMN "Study".inclusion_exclusion_criteria IS 'List of criteria for inclusion/exclusion for the study';COMMENT ON COLUMN "Study".grants IS 'Funding agencies and grant numbers';COMMENT ON COLUMN "Study".study_contact IS 'Full contact information of the contact persons for this study This should include an e-mail address and a persistent identifier such as an ORCID ID.';COMMENT ON COLUMN "Study".collected_by IS 'Full contact information of the data collector, i.e. the person who is legally responsible for data collection and release. This should include an e-mail address and a persistent identifier such as an ORCID ID.';COMMENT ON COLUMN "Study".submitted_by IS 'Full contact information of the data depositor, i.e., the person submitting the data to a repository. This should include an e-mail address and a persistent identifier such as an ORCID ID. This is supposed to be a short-lived and technical role until the submission is relased.';COMMENT ON COLUMN "Study".adc_publish_date IS 'Date the study was first published in the AIRR Data Commons.';COMMENT ON COLUMN "Study".adc_update_date IS 'Date the study data was updated in the AIRR Data Commons.';
CREATE TABLE "Diagnosis" (
	id SERIAL NOT NULL, 
	study_group_description TEXT, 
	disease_diagnosis "DiseaseDiagnosisOntology", 
	disease_length TEXT, 
	disease_stage TEXT, 
	prior_therapies TEXT, 
	immunogen TEXT, 
	intervention TEXT, 
	medical_history TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Diagnosis" IS 'None';COMMENT ON COLUMN "Diagnosis".study_group_description IS 'Designation of study arm to which the subject is assigned to';COMMENT ON COLUMN "Diagnosis".disease_diagnosis IS 'Diagnosis of subject';COMMENT ON COLUMN "Diagnosis".disease_length IS 'Time duration between initial diagnosis and current intervention';COMMENT ON COLUMN "Diagnosis".disease_stage IS 'Stage of disease at current intervention';COMMENT ON COLUMN "Diagnosis".prior_therapies IS 'List of all relevant previous therapies applied to subject for treatment of `Diagnosis`';COMMENT ON COLUMN "Diagnosis".immunogen IS 'Antigen, vaccine or drug applied to subject at this intervention';COMMENT ON COLUMN "Diagnosis".intervention IS 'Description of intervention';COMMENT ON COLUMN "Diagnosis".medical_history IS 'Medical history of subject that is relevant to assess the course of disease and/or treatment';
CREATE TABLE "Sample" (
	id SERIAL NOT NULL, 
	sample_id TEXT, 
	sample_type TEXT, 
	tissue "TissueOntology", 
	anatomic_site TEXT, 
	disease_state_sample TEXT, 
	collection_time_point_relative FLOAT, 
	collection_time_point_relative_unit "CollectionTimePointRelativeUnitOntology", 
	collection_time_point_reference TEXT, 
	biomaterial_provider TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Sample" IS 'None';COMMENT ON COLUMN "Sample".sample_id IS 'Sample ID assigned by submitter, unique within study. If possible, a persistent sample ID linked to INSDC or similar repository study should be used.';COMMENT ON COLUMN "Sample".sample_type IS 'The way the sample was obtained, e.g. fine-needle aspirate, organ harvest, peripheral venous puncture';COMMENT ON COLUMN "Sample".tissue IS 'The actual tissue sampled, e.g. lymph node, liver, peripheral blood';COMMENT ON COLUMN "Sample".anatomic_site IS 'The anatomic location of the tissue, e.g. Inguinal, femur';COMMENT ON COLUMN "Sample".disease_state_sample IS 'Histopathologic evaluation of the sample';COMMENT ON COLUMN "Sample".collection_time_point_relative IS 'Time point at which sample was taken, relative to `Collection time event`';COMMENT ON COLUMN "Sample".collection_time_point_relative_unit IS 'Unit of Sample collection time';COMMENT ON COLUMN "Sample".collection_time_point_reference IS 'Event in the study schedule to which `Sample collection time` relates to';COMMENT ON COLUMN "Sample".biomaterial_provider IS 'Name and address of the entity providing the sample';
CREATE TABLE "CellProcessing" (
	id SERIAL NOT NULL, 
	tissue_processing TEXT, 
	cell_subset "CellSubsetOntology", 
	cell_phenotype TEXT, 
	cell_species "CellSpeciesOntology", 
	single_cell BOOLEAN, 
	cell_number INTEGER, 
	cells_per_reaction INTEGER, 
	cell_storage BOOLEAN, 
	cell_quality TEXT, 
	cell_isolation TEXT, 
	cell_processing_protocol TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "CellProcessing" IS 'None';COMMENT ON COLUMN "CellProcessing".tissue_processing IS 'Enzymatic digestion and/or physical methods used to isolate cells from sample';COMMENT ON COLUMN "CellProcessing".cell_subset IS 'Commonly-used designation of isolated cell population';COMMENT ON COLUMN "CellProcessing".cell_phenotype IS 'List of cellular markers and their expression levels used to isolate the cell population';COMMENT ON COLUMN "CellProcessing".cell_species IS 'Binomial designation of the species from which the analyzed cells originate. Typically, this value should be identical to `species`, in which case it SHOULD NOT be set explicitly. However, there are valid experimental setups in which the two might differ, e.g., chimeric animal models. If set, this key will overwrite the `species` information for all lower layers of the schema.';COMMENT ON COLUMN "CellProcessing".single_cell IS 'TRUE if single cells were isolated into separate compartments';COMMENT ON COLUMN "CellProcessing".cell_number IS 'Total number of cells that went into the experiment';COMMENT ON COLUMN "CellProcessing".cells_per_reaction IS 'Number of cells for each biological replicate';COMMENT ON COLUMN "CellProcessing".cell_storage IS 'TRUE if cells were cryo-preserved between isolation and further processing';COMMENT ON COLUMN "CellProcessing".cell_quality IS 'Relative amount of viable cells after preparation and (if applicable) thawing';COMMENT ON COLUMN "CellProcessing".cell_isolation IS 'Description of the procedure used for marker-based isolation or enrich cells';COMMENT ON COLUMN "CellProcessing".cell_processing_protocol IS 'Description of the methods applied to the sample including cell preparation/ isolation/enrichment and nucleic acid extraction. This should closely mirror the Materials and methods section in the manuscript.';
CREATE TABLE "PCRTarget" (
	id SERIAL NOT NULL, 
	pcr_target_locus "PcrTargetLocusEnum", 
	forward_pcr_primer_target_location TEXT, 
	reverse_pcr_primer_target_location TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "PCRTarget" IS 'None';COMMENT ON COLUMN "PCRTarget".pcr_target_locus IS 'Designation of the target locus. Note that this field uses a controlled vocubulary that is meant to provide a generic classification of the locus, not necessarily the correct designation according to a specific nomenclature.';COMMENT ON COLUMN "PCRTarget".forward_pcr_primer_target_location IS 'Position of the most distal nucleotide templated by the forward primer or primer mix';COMMENT ON COLUMN "PCRTarget".reverse_pcr_primer_target_location IS 'Position of the most proximal nucleotide templated by the reverse primer or primer mix';
CREATE TABLE "NucleicAcidProcessing" (
	id SERIAL NOT NULL, 
	template_class "TemplateClassEnum", 
	template_quality TEXT, 
	template_amount FLOAT, 
	template_amount_unit "TemplateAmountUnitOntology", 
	library_generation_method "LibraryGenerationMethodEnum", 
	library_generation_protocol TEXT, 
	library_generation_kit_version TEXT, 
	complete_sequences "CompleteSequencesEnum", 
	physical_linkage "PhysicalLinkageEnum", 
	PRIMARY KEY (id)
);COMMENT ON TABLE "NucleicAcidProcessing" IS 'None';COMMENT ON COLUMN "NucleicAcidProcessing".template_class IS 'The class of nucleic acid that was used as primary starting material for the following procedures';COMMENT ON COLUMN "NucleicAcidProcessing".template_quality IS 'Description and results of the quality control performed on the template material';COMMENT ON COLUMN "NucleicAcidProcessing".template_amount IS 'Amount of template that went into the process';COMMENT ON COLUMN "NucleicAcidProcessing".template_amount_unit IS 'Unit of template amount';COMMENT ON COLUMN "NucleicAcidProcessing".library_generation_method IS 'Generic type of library generation';COMMENT ON COLUMN "NucleicAcidProcessing".library_generation_protocol IS 'Description of processes applied to substrate to obtain a library that is ready for sequencing';COMMENT ON COLUMN "NucleicAcidProcessing".library_generation_kit_version IS 'When using a library generation protocol from a commercial provider, provide the protocol version number';COMMENT ON COLUMN "NucleicAcidProcessing".complete_sequences IS 'To be considered `complete`, the procedure used for library construction MUST generate sequences that 1) include the first V gene codon that encodes the mature polypeptide chain (i.e. after the leader sequence) and 2) include the last complete codon of the J gene (i.e. 1 bp 5'' of the J->C splice site) and 3) provide sequence information for all positions between 1) and 2). To be considered `complete & untemplated`, the sections of the sequences defined in points 1) to 3) of the previous sentence MUST be untemplated, i.e. MUST NOT overlap with the primers used in library preparation. `mixed` should only be used if the procedure used for library construction will likely produce multiple categories of sequences in the given experiment. It SHOULD NOT be used as a replacement of a NULL value.';COMMENT ON COLUMN "NucleicAcidProcessing".physical_linkage IS 'In case an experimental setup is used that physically links nucleic acids derived from distinct `Rearrangements` before library preparation, this field describes the mode of that linkage. All `hetero_*` terms indicate that in case of paired-read sequencing, the two reads should be expected to map to distinct IG/TR loci. `*_head-head` refers to techniques that link the 5'' ends of transcripts in a single-cell context. `*_tail-head` refers to techniques that link the 3'' end of one transcript to the 5'' end of another one in a single-cell context. This term does not provide any information whether a continuous reading-frame between the two is generated. `*_prelinked` refers to constructs in which the linkage was already present on the DNA level (e.g. scFv).';
CREATE TABLE "SequencingData" (
	id SERIAL NOT NULL, 
	sequencing_data_id TEXT, 
	file_type "FileTypeEnum", 
	filename TEXT, 
	read_direction "ReadDirectionEnum", 
	read_length INTEGER, 
	paired_filename TEXT, 
	paired_read_direction "PairedReadDirectionEnum", 
	paired_read_length INTEGER, 
	index_filename TEXT, 
	index_length INTEGER, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "SequencingData" IS 'None';COMMENT ON COLUMN "SequencingData".sequencing_data_id IS 'Persistent identifier of raw data stored in an archive (e.g. INSDC run ID). Data archive should  be identified in the CURIE prefix.';COMMENT ON COLUMN "SequencingData".file_type IS 'File format for the raw reads or sequences';COMMENT ON COLUMN "SequencingData".filename IS 'File name for the raw reads or sequences. The first file in paired-read sequencing.';COMMENT ON COLUMN "SequencingData".read_direction IS 'Read direction for the raw reads or sequences. The first file in paired-read sequencing.';COMMENT ON COLUMN "SequencingData".read_length IS 'Read length in bases for the first file in paired-read sequencing';COMMENT ON COLUMN "SequencingData".paired_filename IS 'File name for the second file in paired-read sequencing';COMMENT ON COLUMN "SequencingData".paired_read_direction IS 'Read direction for the second file in paired-read sequencing';COMMENT ON COLUMN "SequencingData".paired_read_length IS 'Read length in bases for the second file in paired-read sequencing';COMMENT ON COLUMN "SequencingData".index_filename IS 'File name for the index file';COMMENT ON COLUMN "SequencingData".index_length IS 'Read length in bases for the index file';
CREATE TABLE "DataProcessing" (
	id SERIAL NOT NULL, 
	data_processing_id TEXT, 
	primary_annotation BOOLEAN, 
	software_versions TEXT, 
	paired_reads_assembly TEXT, 
	quality_thresholds TEXT, 
	primer_match_cutoffs TEXT, 
	collapsing_method TEXT, 
	data_processing_protocols TEXT, 
	germline_database TEXT, 
	germline_set_ref TEXT, 
	analysis_provenance_id TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "DataProcessing" IS 'None';COMMENT ON COLUMN "DataProcessing".primary_annotation IS 'If true, indicates this is the primary or default data processing for the repertoire and its rearrangements. If false, indicates this is a secondary or additional data processing.';COMMENT ON COLUMN "DataProcessing".software_versions IS 'Version number and / or date, include company pipelines';COMMENT ON COLUMN "DataProcessing".paired_reads_assembly IS 'How paired end reads were assembled into a single receptor sequence';COMMENT ON COLUMN "DataProcessing".quality_thresholds IS 'How/if sequences were removed from (4) based on base quality scores';COMMENT ON COLUMN "DataProcessing".primer_match_cutoffs IS 'How primers were identified in the sequences, were they removed/masked/etc?';COMMENT ON COLUMN "DataProcessing".collapsing_method IS 'The method used for combining multiple sequences from (4) into a single sequence in (5)';COMMENT ON COLUMN "DataProcessing".data_processing_protocols IS 'General description of how QC is performed';COMMENT ON COLUMN "DataProcessing".germline_database IS 'Source of germline V(D)J genes with version number or date accessed.';COMMENT ON COLUMN "DataProcessing".analysis_provenance_id IS 'Identifier for machine-readable PROV model of analysis provenance';
CREATE TABLE "RepertoireGroup" (
	id SERIAL NOT NULL, 
	repertoire_group_id TEXT, 
	repertoire_group_name TEXT, 
	repertoire_group_description TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "RepertoireGroup" IS 'None';COMMENT ON COLUMN "RepertoireGroup".repertoire_group_id IS 'Identifier for this repertoire collection';COMMENT ON COLUMN "RepertoireGroup".repertoire_group_name IS 'Short display name for this repertoire collection';COMMENT ON COLUMN "RepertoireGroup".repertoire_group_description IS 'Repertoire collection description';
CREATE TABLE "Alignment" (
	id SERIAL NOT NULL, 
	sequence_id TEXT, 
	segment TEXT, 
	rev_comp BOOLEAN, 
	call TEXT, 
	score FLOAT, 
	identity FLOAT, 
	support FLOAT, 
	cigar TEXT, 
	sequence_start INTEGER, 
	sequence_end INTEGER, 
	germline_start INTEGER, 
	germline_end INTEGER, 
	rank INTEGER, 
	data_processing_id TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Alignment" IS 'None';COMMENT ON COLUMN "Alignment".segment IS 'The segment for this alignment. One of V, D, J or C.';COMMENT ON COLUMN "Alignment".call IS 'Gene assignment with allele.';COMMENT ON COLUMN "Alignment".score IS 'Alignment score.';COMMENT ON COLUMN "Alignment".identity IS 'Alignment fractional identity.';COMMENT ON COLUMN "Alignment".support IS 'Alignment E-value, p-value, likelihood, probability or other similar measure of support for the gene assignment as defined by the alignment tool.';COMMENT ON COLUMN "Alignment".cigar IS 'Alignment CIGAR string.';COMMENT ON COLUMN "Alignment".germline_start IS 'Alignment start position in the reference sequence (1-based closed interval).';COMMENT ON COLUMN "Alignment".germline_end IS 'Alignment end position in the reference sequence (1-based closed interval).';COMMENT ON COLUMN "Alignment".rank IS 'Alignment rank.';
CREATE TABLE "Rearrangement" (
	id SERIAL NOT NULL, 
	sequence_id TEXT, 
	sequence TEXT, 
	quality TEXT, 
	sequence_aa TEXT, 
	rev_comp BOOLEAN, 
	productive BOOLEAN, 
	vj_in_frame BOOLEAN, 
	stop_codon BOOLEAN, 
	complete_vdj BOOLEAN, 
	locus "LocusEnum", 
	v_call TEXT, 
	d_call TEXT, 
	d2_call TEXT, 
	j_call TEXT, 
	c_call TEXT, 
	sequence_alignment TEXT, 
	quality_alignment TEXT, 
	sequence_alignment_aa TEXT, 
	germline_alignment TEXT, 
	germline_alignment_aa TEXT, 
	junction TEXT, 
	junction_aa TEXT, 
	np1 TEXT, 
	np1_aa TEXT, 
	np2 TEXT, 
	np2_aa TEXT, 
	np3 TEXT, 
	np3_aa TEXT, 
	cdr1 TEXT, 
	cdr1_aa TEXT, 
	cdr2 TEXT, 
	cdr2_aa TEXT, 
	cdr3 TEXT, 
	cdr3_aa TEXT, 
	fwr1 TEXT, 
	fwr1_aa TEXT, 
	fwr2 TEXT, 
	fwr2_aa TEXT, 
	fwr3 TEXT, 
	fwr3_aa TEXT, 
	fwr4 TEXT, 
	fwr4_aa TEXT, 
	v_score FLOAT, 
	v_identity FLOAT, 
	v_support FLOAT, 
	v_cigar TEXT, 
	d_score FLOAT, 
	d_identity FLOAT, 
	d_support FLOAT, 
	d_cigar TEXT, 
	d2_score FLOAT, 
	d2_identity FLOAT, 
	d2_support FLOAT, 
	d2_cigar TEXT, 
	j_score FLOAT, 
	j_identity FLOAT, 
	j_support FLOAT, 
	j_cigar TEXT, 
	c_score FLOAT, 
	c_identity FLOAT, 
	c_support FLOAT, 
	c_cigar TEXT, 
	v_sequence_start INTEGER, 
	v_sequence_end INTEGER, 
	v_germline_start INTEGER, 
	v_germline_end INTEGER, 
	v_alignment_start INTEGER, 
	v_alignment_end INTEGER, 
	d_sequence_start INTEGER, 
	d_sequence_end INTEGER, 
	d_germline_start INTEGER, 
	d_germline_end INTEGER, 
	d_alignment_start INTEGER, 
	d_alignment_end INTEGER, 
	d2_sequence_start INTEGER, 
	d2_sequence_end INTEGER, 
	d2_germline_start INTEGER, 
	d2_germline_end INTEGER, 
	d2_alignment_start INTEGER, 
	d2_alignment_end INTEGER, 
	j_sequence_start INTEGER, 
	j_sequence_end INTEGER, 
	j_germline_start INTEGER, 
	j_germline_end INTEGER, 
	j_alignment_start INTEGER, 
	j_alignment_end INTEGER, 
	c_sequence_start INTEGER, 
	c_sequence_end INTEGER, 
	c_germline_start INTEGER, 
	c_germline_end INTEGER, 
	c_alignment_start INTEGER, 
	c_alignment_end INTEGER, 
	cdr1_start INTEGER, 
	cdr1_end INTEGER, 
	cdr2_start INTEGER, 
	cdr2_end INTEGER, 
	cdr3_start INTEGER, 
	cdr3_end INTEGER, 
	fwr1_start INTEGER, 
	fwr1_end INTEGER, 
	fwr2_start INTEGER, 
	fwr2_end INTEGER, 
	fwr3_start INTEGER, 
	fwr3_end INTEGER, 
	fwr4_start INTEGER, 
	fwr4_end INTEGER, 
	v_sequence_alignment TEXT, 
	v_sequence_alignment_aa TEXT, 
	d_sequence_alignment TEXT, 
	d_sequence_alignment_aa TEXT, 
	d2_sequence_alignment TEXT, 
	d2_sequence_alignment_aa TEXT, 
	j_sequence_alignment TEXT, 
	j_sequence_alignment_aa TEXT, 
	c_sequence_alignment TEXT, 
	c_sequence_alignment_aa TEXT, 
	v_germline_alignment TEXT, 
	v_germline_alignment_aa TEXT, 
	d_germline_alignment TEXT, 
	d_germline_alignment_aa TEXT, 
	d2_germline_alignment TEXT, 
	d2_germline_alignment_aa TEXT, 
	j_germline_alignment TEXT, 
	j_germline_alignment_aa TEXT, 
	c_germline_alignment TEXT, 
	c_germline_alignment_aa TEXT, 
	junction_length INTEGER, 
	junction_aa_length INTEGER, 
	np1_length INTEGER, 
	np2_length INTEGER, 
	np3_length INTEGER, 
	n1_length INTEGER, 
	n2_length INTEGER, 
	n3_length INTEGER, 
	p3v_length INTEGER, 
	p5d_length INTEGER, 
	p3d_length INTEGER, 
	p5d2_length INTEGER, 
	p3d2_length INTEGER, 
	p5j_length INTEGER, 
	v_frameshift BOOLEAN, 
	j_frameshift BOOLEAN, 
	d_frame INTEGER, 
	d2_frame INTEGER, 
	consensus_count INTEGER, 
	duplicate_count INTEGER, 
	umi_count INTEGER, 
	cell_id TEXT, 
	clone_id TEXT, 
	repertoire_id TEXT, 
	sample_processing_id TEXT, 
	data_processing_id TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Rearrangement" IS 'None';COMMENT ON COLUMN "Rearrangement".sequence IS 'Nucleotide sequence.';COMMENT ON COLUMN "Rearrangement".quality IS 'The Sanger/Phred quality scores for assessment of sequence quality. Phred quality scores from 0 to 93 are encoded using ASCII 33 to 126 (Used by Illumina from v1.8.)';COMMENT ON COLUMN "Rearrangement".sequence_aa IS 'Amino acid translation of the query nucleotide sequence.';COMMENT ON COLUMN "Rearrangement".productive IS 'True if the V(D)J sequence is predicted to be productive.';COMMENT ON COLUMN "Rearrangement".vj_in_frame IS 'True if the V and J gene alignments are in-frame.';COMMENT ON COLUMN "Rearrangement".stop_codon IS 'True if the aligned sequence contains a stop codon.';COMMENT ON COLUMN "Rearrangement".complete_vdj IS 'Complete VDJ flag.';COMMENT ON COLUMN "Rearrangement".d2_call IS 'Second D gene with allele. If referring to a known reference sequence in a database the relevant gene/allele nomenclature should be followed (e.g., IGHD3-10*01 if using IMGT/GENE-DB).';COMMENT ON COLUMN "Rearrangement".c_call IS 'Constant region gene with allele. If referring to a known reference sequence in a database the relevant gene/allele nomenclature should be followed (e.g., IGHG1*01 if using IMGT/GENE-DB).';COMMENT ON COLUMN "Rearrangement".quality_alignment IS 'Sanger/Phred quality scores for assessment of sequence_alignment quality. Phred quality scores from 0 to 93 are encoded using ASCII 33 to 126 (Used by Illumina from v1.8.)';COMMENT ON COLUMN "Rearrangement".sequence_alignment_aa IS 'Amino acid translation of the aligned query sequence.';COMMENT ON COLUMN "Rearrangement".junction_aa IS 'Amino acid translation of the junction.';COMMENT ON COLUMN "Rearrangement".np1 IS 'Nucleotide sequence of the combined N/P region between the V gene and first D gene alignment or between the V gene and J gene alignments.';COMMENT ON COLUMN "Rearrangement".np1_aa IS 'Amino acid translation of the np1 field.';COMMENT ON COLUMN "Rearrangement".np2 IS 'Nucleotide sequence of the combined N/P region between either the first D gene and J gene alignments or the first D gene and second D gene alignments.';COMMENT ON COLUMN "Rearrangement".np2_aa IS 'Amino acid translation of the np2 field.';COMMENT ON COLUMN "Rearrangement".np3 IS 'Nucleotide sequence of the combined N/P region between the second D gene and J gene alignments.';COMMENT ON COLUMN "Rearrangement".np3_aa IS 'Amino acid translation of the np3 field.';COMMENT ON COLUMN "Rearrangement".cdr1 IS 'Nucleotide sequence of the aligned CDR1 region.';COMMENT ON COLUMN "Rearrangement".cdr1_aa IS 'Amino acid translation of the cdr1 field.';COMMENT ON COLUMN "Rearrangement".cdr2 IS 'Nucleotide sequence of the aligned CDR2 region.';COMMENT ON COLUMN "Rearrangement".cdr2_aa IS 'Amino acid translation of the cdr2 field.';COMMENT ON COLUMN "Rearrangement".cdr3 IS 'Nucleotide sequence of the aligned CDR3 region.';COMMENT ON COLUMN "Rearrangement".cdr3_aa IS 'Amino acid translation of the cdr3 field.';COMMENT ON COLUMN "Rearrangement".fwr1 IS 'Nucleotide sequence of the aligned FWR1 region.';COMMENT ON COLUMN "Rearrangement".fwr1_aa IS 'Amino acid translation of the fwr1 field.';COMMENT ON COLUMN "Rearrangement".fwr2 IS 'Nucleotide sequence of the aligned FWR2 region.';COMMENT ON COLUMN "Rearrangement".fwr2_aa IS 'Amino acid translation of the fwr2 field.';COMMENT ON COLUMN "Rearrangement".fwr3 IS 'Nucleotide sequence of the aligned FWR3 region.';COMMENT ON COLUMN "Rearrangement".fwr3_aa IS 'Amino acid translation of the fwr3 field.';COMMENT ON COLUMN "Rearrangement".fwr4 IS 'Nucleotide sequence of the aligned FWR4 region.';COMMENT ON COLUMN "Rearrangement".fwr4_aa IS 'Amino acid translation of the fwr4 field.';COMMENT ON COLUMN "Rearrangement".v_score IS 'Alignment score for the V gene.';COMMENT ON COLUMN "Rearrangement".v_identity IS 'Fractional identity for the V gene alignment.';COMMENT ON COLUMN "Rearrangement".v_support IS 'V gene alignment E-value, p-value, likelihood, probability or other similar measure of support for the V gene assignment as defined by the alignment tool.';COMMENT ON COLUMN "Rearrangement".v_cigar IS 'CIGAR string for the V gene alignment.';COMMENT ON COLUMN "Rearrangement".d_score IS 'Alignment score for the first or only D gene alignment.';COMMENT ON COLUMN "Rearrangement".d_identity IS 'Fractional identity for the first or only D gene alignment.';COMMENT ON COLUMN "Rearrangement".d_support IS 'D gene alignment E-value, p-value, likelihood, probability or other similar measure of support for the first or only D gene as defined by the alignment tool.';COMMENT ON COLUMN "Rearrangement".d_cigar IS 'CIGAR string for the first or only D gene alignment.';COMMENT ON COLUMN "Rearrangement".d2_score IS 'Alignment score for the second D gene alignment.';COMMENT ON COLUMN "Rearrangement".d2_identity IS 'Fractional identity for the second D gene alignment.';COMMENT ON COLUMN "Rearrangement".d2_support IS 'D gene alignment E-value, p-value, likelihood, probability or other similar measure of support for the second D gene as defined by the alignment tool.';COMMENT ON COLUMN "Rearrangement".d2_cigar IS 'CIGAR string for the second D gene alignment.';COMMENT ON COLUMN "Rearrangement".j_score IS 'Alignment score for the J gene alignment.';COMMENT ON COLUMN "Rearrangement".j_identity IS 'Fractional identity for the J gene alignment.';COMMENT ON COLUMN "Rearrangement".j_support IS 'J gene alignment E-value, p-value, likelihood, probability or other similar measure of support for the J gene assignment as defined by the alignment tool.';COMMENT ON COLUMN "Rearrangement".j_cigar IS 'CIGAR string for the J gene alignment.';COMMENT ON COLUMN "Rearrangement".c_score IS 'Alignment score for the C gene alignment.';COMMENT ON COLUMN "Rearrangement".c_identity IS 'Fractional identity for the C gene alignment.';COMMENT ON COLUMN "Rearrangement".c_support IS 'C gene alignment E-value, p-value, likelihood, probability or other similar measure of support for the C gene assignment as defined by the alignment tool.';COMMENT ON COLUMN "Rearrangement".c_cigar IS 'CIGAR string for the C gene alignment.';COMMENT ON COLUMN "Rearrangement".v_sequence_start IS 'Start position of the V gene in the query sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".v_sequence_end IS 'End position of the V gene in the query sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".v_germline_start IS 'Alignment start position in the V gene reference sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".v_germline_end IS 'Alignment end position in the V gene reference sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".d_sequence_start IS 'Start position of the first or only D gene in the query sequence. (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".d_sequence_end IS 'End position of the first or only D gene in the query sequence. (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".d_germline_start IS 'Alignment start position in the D gene reference sequence for the first or only D gene (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".d_germline_end IS 'Alignment end position in the D gene reference sequence for the first or only D gene (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".d2_sequence_start IS 'Start position of the second D gene in the query sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".d2_sequence_end IS 'End position of the second D gene in the query sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".d2_germline_start IS 'Alignment start position in the second D gene reference sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".d2_germline_end IS 'Alignment end position in the second D gene reference sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".d2_alignment_start IS 'Start position of the second D gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".d2_alignment_end IS 'End position of the second D gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".j_sequence_start IS 'Start position of the J gene in the query sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".j_sequence_end IS 'End position of the J gene in the query sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".j_germline_start IS 'Alignment start position in the J gene reference sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".j_germline_end IS 'Alignment end position in the J gene reference sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".j_alignment_start IS 'Start position of the J gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".j_alignment_end IS 'End position of the J gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".c_sequence_start IS 'Start position of the C gene in the query sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".c_sequence_end IS 'End position of the C gene in the query sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".c_germline_start IS 'Alignment start position in the C gene reference sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".c_germline_end IS 'Alignment end position in the C gene reference sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".c_alignment_start IS 'Start position of the C gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".c_alignment_end IS 'End position of the C gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".cdr3_end IS 'CDR3 end position in the query sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".fwr4_start IS 'FWR4 start position in the query sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".fwr4_end IS 'FWR4 end position in the query sequence (1-based closed interval).';COMMENT ON COLUMN "Rearrangement".v_sequence_alignment IS 'Aligned portion of query sequence assigned to the V gene, including any indel corrections or numbering spacers.';COMMENT ON COLUMN "Rearrangement".v_sequence_alignment_aa IS 'Amino acid translation of the v_sequence_alignment field.';COMMENT ON COLUMN "Rearrangement".d_sequence_alignment IS 'Aligned portion of query sequence assigned to the first or only D gene, including any indel corrections or numbering spacers.';COMMENT ON COLUMN "Rearrangement".d_sequence_alignment_aa IS 'Amino acid translation of the d_sequence_alignment field.';COMMENT ON COLUMN "Rearrangement".d2_sequence_alignment IS 'Aligned portion of query sequence assigned to the second D gene, including any indel corrections or numbering spacers.';COMMENT ON COLUMN "Rearrangement".d2_sequence_alignment_aa IS 'Amino acid translation of the d2_sequence_alignment field.';COMMENT ON COLUMN "Rearrangement".j_sequence_alignment IS 'Aligned portion of query sequence assigned to the J gene, including any indel corrections or numbering spacers.';COMMENT ON COLUMN "Rearrangement".j_sequence_alignment_aa IS 'Amino acid translation of the j_sequence_alignment field.';COMMENT ON COLUMN "Rearrangement".c_sequence_alignment IS 'Aligned portion of query sequence assigned to the constant region, including any indel corrections or numbering spacers.';COMMENT ON COLUMN "Rearrangement".c_sequence_alignment_aa IS 'Amino acid translation of the c_sequence_alignment field.';COMMENT ON COLUMN "Rearrangement".v_germline_alignment IS 'Aligned V gene germline sequence spanning the same region as the v_sequence_alignment field and including the same set of corrections and spacers (if any).';COMMENT ON COLUMN "Rearrangement".v_germline_alignment_aa IS 'Amino acid translation of the v_germline_alignment field.';COMMENT ON COLUMN "Rearrangement".d_germline_alignment IS 'Aligned D gene germline sequence spanning the same region as the d_sequence_alignment field and including the same set of corrections and spacers (if any).';COMMENT ON COLUMN "Rearrangement".d_germline_alignment_aa IS 'Amino acid translation of the d_germline_alignment field.';COMMENT ON COLUMN "Rearrangement".d2_germline_alignment IS 'Aligned D gene germline sequence spanning the same region as the d2_sequence_alignment field and including the same set of corrections and spacers (if any).';COMMENT ON COLUMN "Rearrangement".d2_germline_alignment_aa IS 'Amino acid translation of the d2_germline_alignment field.';COMMENT ON COLUMN "Rearrangement".j_germline_alignment IS 'Aligned J gene germline sequence spanning the same region as the j_sequence_alignment field and including the same set of corrections and spacers (if any).';COMMENT ON COLUMN "Rearrangement".j_germline_alignment_aa IS 'Amino acid translation of the j_germline_alignment field.';COMMENT ON COLUMN "Rearrangement".c_germline_alignment IS 'Aligned constant region germline sequence spanning the same region as the c_sequence_alignment field and including the same set of corrections and spacers (if any).';COMMENT ON COLUMN "Rearrangement".c_germline_alignment_aa IS 'Amino acid translation of the c_germline_aligment field.';COMMENT ON COLUMN "Rearrangement".np1_length IS 'Number of nucleotides between the V gene and first D gene alignments or between the V gene and J gene alignments.';COMMENT ON COLUMN "Rearrangement".np2_length IS 'Number of nucleotides between either the first D gene and J gene alignments or the first D gene and second D gene alignments.';COMMENT ON COLUMN "Rearrangement".np3_length IS 'Number of nucleotides between the second D gene and J gene alignments.';COMMENT ON COLUMN "Rearrangement".n1_length IS 'Number of untemplated nucleotides 5'' of the first or only D gene alignment.';COMMENT ON COLUMN "Rearrangement".n2_length IS 'Number of untemplated nucleotides 3'' of the first or only D gene alignment.';COMMENT ON COLUMN "Rearrangement".n3_length IS 'Number of untemplated nucleotides 3'' of the second D gene alignment.';COMMENT ON COLUMN "Rearrangement".p3v_length IS 'Number of palindromic nucleotides 3'' of the V gene alignment.';COMMENT ON COLUMN "Rearrangement".p5d_length IS 'Number of palindromic nucleotides 5'' of the first or only D gene alignment.';COMMENT ON COLUMN "Rearrangement".p3d_length IS 'Number of palindromic nucleotides 3'' of the first or only D gene alignment.';COMMENT ON COLUMN "Rearrangement".p5d2_length IS 'Number of palindromic nucleotides 5'' of the second D gene alignment.';COMMENT ON COLUMN "Rearrangement".p3d2_length IS 'Number of palindromic nucleotides 3'' of the second D gene alignment.';COMMENT ON COLUMN "Rearrangement".p5j_length IS 'Number of palindromic nucleotides 5'' of the J gene alignment.';COMMENT ON COLUMN "Rearrangement".v_frameshift IS 'True if the V gene in the query nucleotide sequence contains a translational frameshift relative to the frame of the V gene reference sequence.';COMMENT ON COLUMN "Rearrangement".j_frameshift IS 'True if the J gene in the query nucleotide sequence contains a translational frameshift relative to the frame of the J gene reference sequence.';COMMENT ON COLUMN "Rearrangement".d_frame IS 'Numerical reading frame (1, 2, 3) of the first or only D gene in the query nucleotide sequence, where frame 1 is relative to the first codon of D gene reference sequence.';COMMENT ON COLUMN "Rearrangement".d2_frame IS 'Numerical reading frame (1, 2, 3) of the second D gene in the query nucleotide sequence, where frame 1 is relative to the first codon of D gene reference sequence.';COMMENT ON COLUMN "Rearrangement".consensus_count IS 'Number of reads contributing to the UMI consensus or contig assembly for this sequence. For example, the sum of the number of reads for all UMIs that contribute to the query sequence.';COMMENT ON COLUMN "Rearrangement".duplicate_count IS 'Copy number or number of duplicate observations for the query sequence. For example, the number of identical reads observed for this sequence.';
CREATE TABLE "Clone" (
	id SERIAL NOT NULL, 
	clone_id TEXT, 
	repertoire_id TEXT, 
	data_processing_id TEXT, 
	v_call TEXT, 
	d_call TEXT, 
	j_call TEXT, 
	junction TEXT, 
	junction_aa TEXT, 
	junction_length INTEGER, 
	junction_aa_length INTEGER, 
	germline_alignment TEXT, 
	germline_alignment_aa TEXT, 
	v_alignment_start INTEGER, 
	v_alignment_end INTEGER, 
	d_alignment_start INTEGER, 
	d_alignment_end INTEGER, 
	j_alignment_start INTEGER, 
	j_alignment_end INTEGER, 
	junction_start INTEGER, 
	junction_end INTEGER, 
	umi_count INTEGER, 
	clone_count INTEGER, 
	seed_id TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Clone" IS 'None';COMMENT ON COLUMN "Clone".junction_aa IS 'Amino acid translation of the junction.';COMMENT ON COLUMN "Clone".j_alignment_start IS 'Start position of the J gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).';COMMENT ON COLUMN "Clone".j_alignment_end IS 'End position of the J gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).';COMMENT ON COLUMN "Clone".junction_start IS 'Junction region start position in the alignment (1-based closed interval).';COMMENT ON COLUMN "Clone".junction_end IS 'Junction region end position in the alignment (1-based closed interval).';COMMENT ON COLUMN "Clone".clone_count IS 'Absolute count of the size (number of members) of this clone in the repertoire. This could simply be the number of sequences (Rearrangement records) observed in this clone, the number of distinct cell barcodes (unique cell_id values), or a more sophisticated calculation appropriate to the experimental protocol. Absolute count is provided versus a frequency so that downstream analysis tools can perform their own normalization.';COMMENT ON COLUMN "Clone".seed_id IS 'sequence_id of the seed sequence. Empty string (or null) if there is no seed sequence.';
CREATE TABLE "Tree" (
	id SERIAL NOT NULL, 
	tree_id TEXT, 
	clone_id TEXT, 
	newick TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Tree" IS 'None';COMMENT ON COLUMN "Tree".tree_id IS 'Identifier for the tree.';COMMENT ON COLUMN "Tree".newick IS 'Newick string of the tree edges.';
CREATE TABLE "Node" (
	id SERIAL NOT NULL, 
	sequence_id TEXT, 
	sequence_alignment TEXT, 
	junction TEXT, 
	junction_aa TEXT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Node" IS 'None';COMMENT ON COLUMN "Node".junction_aa IS 'Amino acid translation of the junction.';
CREATE TABLE "Cell" (
	id SERIAL NOT NULL, 
	cell_id TEXT, 
	repertoire_id TEXT, 
	data_processing_id TEXT, 
	expression_study_method "ExpressionStudyMethodEnum", 
	expression_raw_doi TEXT, 
	expression_index TEXT, 
	virtual_pairing BOOLEAN, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Cell" IS 'None';COMMENT ON COLUMN "Cell".expression_study_method IS 'Keyword describing the methodology used to assess expression. This values for this field MUST  come from a controlled vocabulary.';COMMENT ON COLUMN "Cell".expression_raw_doi IS 'DOI of raw data set containing the current event';COMMENT ON COLUMN "Cell".expression_index IS 'Index addressing the current event within the raw data set.';COMMENT ON COLUMN "Cell".virtual_pairing IS 'boolean to indicate if pairing was inferred.';
CREATE TABLE "CellExpression" (
	id SERIAL NOT NULL, 
	expression_id TEXT, 
	cell_id TEXT, 
	repertoire_id TEXT, 
	data_processing_id TEXT, 
	property_type TEXT, 
	property TEXT, 
	property_value FLOAT, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "CellExpression" IS 'None';COMMENT ON COLUMN "CellExpression".expression_id IS 'Identifier of this expression property measurement.';COMMENT ON COLUMN "CellExpression".property_type IS 'Keyword describing the property type and detection method used to measure the property value. The following keywords are recommended, but custom property types are also valid: "mrna_expression_by_read_count", "protein_expression_by_fluorescence_intensity", "antigen_bait_binding_by_fluorescence_intensity", "protein_expression_by_dna_barcode_count" and "antigen_bait_binding_by_dna_barcode_count".';COMMENT ON COLUMN "CellExpression".property IS 'Name of the property observed, typically a gene or antibody identifier (and label) from a  canonical resource such as Ensembl (e.g. ENSG00000275747, IGHV3-79) or  Antibody Registry (ABREG:1236456, Purified anti-mouse/rat/human CD27 antibody).';COMMENT ON COLUMN "CellExpression".property_value IS 'Level at which the property was observed in the experiment (non-normalized).';
CREATE TABLE "Receptor" (
	id SERIAL NOT NULL, 
	receptor_id TEXT, 
	receptor_hash TEXT, 
	receptor_type "ReceptorTypeEnum", 
	receptor_variable_domain_1_aa TEXT, 
	receptor_variable_domain_1_locus "ReceptorVariableDomain1LocusEnum", 
	receptor_variable_domain_2_aa TEXT, 
	receptor_variable_domain_2_locus "ReceptorVariableDomain2LocusEnum", 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Receptor" IS 'None';COMMENT ON COLUMN "Receptor".receptor_id IS 'ID of the current Receptor object, unique within the local repository.';COMMENT ON COLUMN "Receptor".receptor_hash IS 'The SHA256 hash of the receptor amino acid sequence, calculated on the concatenated ``receptor_variable_domain_*_aa`` sequences and represented as base16-encoded string.';COMMENT ON COLUMN "Receptor".receptor_type IS 'The top-level receptor type, either Immunoglobulin (Ig) or T Cell Receptor (TCR).';COMMENT ON COLUMN "Receptor".receptor_variable_domain_1_aa IS 'Complete amino acid sequence of the mature variable domain of the Ig heavy, TCR beta or TCR delta chain. The mature variable domain is defined as encompassing all AA from and including first AA after the the signal peptide to and including the last AA that is completely encoded by the J gene.';COMMENT ON COLUMN "Receptor".receptor_variable_domain_1_locus IS 'Locus from which the variable domain in receptor_variable_domain_1_aa originates';COMMENT ON COLUMN "Receptor".receptor_variable_domain_2_aa IS 'Complete amino acid sequence of the mature variable domain of the Ig light, TCR alpha or TCR gamma chain. The mature variable domain is defined as encompassing all AA from and including first AA after the the signal peptide to and including the last AA that is completely encoded by the J gene.';COMMENT ON COLUMN "Receptor".receptor_variable_domain_2_locus IS 'Locus from which the variable domain in receptor_variable_domain_2_aa originates';
CREATE TABLE "Investigation" (
	archival_id TEXT, 
	inclusion_exclusion_criteria TEXT, 
	release_date TIMESTAMP WITHOUT TIME ZONE, 
	update_date TIMESTAMP WITHOUT TIME ZONE, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	investigation_type_id INTEGER, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(investigation_type_id) REFERENCES "InvestigationType" (id)
);COMMENT ON TABLE "Investigation" IS 'A scientific investigation.';COMMENT ON COLUMN "Investigation".archival_id IS 'Identifier for external archival resource for the investigation, e.g., BioProject';COMMENT ON COLUMN "Investigation".inclusion_exclusion_criteria IS 'List of criteria for inclusion/exclusion for the study';COMMENT ON COLUMN "Investigation".release_date IS 'Date of this release';COMMENT ON COLUMN "Investigation".update_date IS 'Subsequence updates to the investigation or its data';COMMENT ON COLUMN "Investigation".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "Investigation".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "Investigation".akc_id IS 'A unique identifier for a thing in the AKC.';COMMENT ON COLUMN "Investigation".investigation_type_id IS 'Type of study design';
CREATE TABLE "InputOutputDataMap" (
	id SERIAL NOT NULL, 
	data_transformation TEXT, 
	has_specified_input TEXT, 
	has_specified_output TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(data_transformation) REFERENCES "DataTransformation" (akc_id), 
	FOREIGN KEY(has_specified_input) REFERENCES "AKDataItem" (akc_id), 
	FOREIGN KEY(has_specified_output) REFERENCES "AKDataItem" (akc_id)
);COMMENT ON TABLE "InputOutputDataMap" IS 'None';COMMENT ON COLUMN "InputOutputDataMap".data_transformation IS 'a process that transforms input data into output data';COMMENT ON COLUMN "InputOutputDataMap".has_specified_input IS 'input data item';COMMENT ON COLUMN "InputOutputDataMap".has_specified_output IS 'output data item';
CREATE TABLE "AlphaBetaTCR" (
	tra_chain TEXT, 
	trb_chain TEXT, 
	type TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(tra_chain) REFERENCES "Chain" (akc_id), 
	FOREIGN KEY(trb_chain) REFERENCES "Chain" (akc_id)
);COMMENT ON TABLE "AlphaBetaTCR" IS 'None';COMMENT ON COLUMN "AlphaBetaTCR".tra_chain IS 'T cell receptor alpha chain';COMMENT ON COLUMN "AlphaBetaTCR".trb_chain IS 'T cell receptor beta chain';COMMENT ON COLUMN "AlphaBetaTCR".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "GammaDeltaTCR" (
	trg_chain TEXT, 
	trd_chain TEXT, 
	type TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(trg_chain) REFERENCES "Chain" (akc_id), 
	FOREIGN KEY(trd_chain) REFERENCES "Chain" (akc_id)
);COMMENT ON TABLE "GammaDeltaTCR" IS 'None';COMMENT ON COLUMN "GammaDeltaTCR".trg_chain IS 'T cell receptor gamma chain';COMMENT ON COLUMN "GammaDeltaTCR".trd_chain IS 'T cell receptor delta chain';COMMENT ON COLUMN "GammaDeltaTCR".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "BCellReceptor" (
	igh_chain TEXT, 
	igk_chain TEXT, 
	igl_chain TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(igh_chain) REFERENCES "Chain" (akc_id), 
	FOREIGN KEY(igk_chain) REFERENCES "Chain" (akc_id), 
	FOREIGN KEY(igl_chain) REFERENCES "Chain" (akc_id)
);COMMENT ON TABLE "BCellReceptor" IS 'None';COMMENT ON COLUMN "BCellReceptor".igh_chain IS 'IG heavy chain';COMMENT ON COLUMN "BCellReceptor".igk_chain IS 'IG kappa light chain';COMMENT ON COLUMN "BCellReceptor".igl_chain IS 'IG lambda light chain';COMMENT ON COLUMN "BCellReceptor".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "TCRpMHCComplex" (
	tcell_receptor TEXT, 
	epitope TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	mhc_id INTEGER, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(tcell_receptor) REFERENCES "TCellReceptor" (akc_id), 
	FOREIGN KEY(epitope) REFERENCES "Epitope" (akc_id), 
	FOREIGN KEY(mhc_id) REFERENCES "MHCAllele" (id)
);COMMENT ON TABLE "TCRpMHCComplex" IS 'None';COMMENT ON COLUMN "TCRpMHCComplex".tcell_receptor IS 'T cell receptor';COMMENT ON COLUMN "TCRpMHCComplex".epitope IS 'The epitope being measured';COMMENT ON COLUMN "TCRpMHCComplex".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "TCRpMHCComplex".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "TCRpMHCComplex".akc_id IS 'A unique identifier for a thing in the AKC.';COMMENT ON COLUMN "TCRpMHCComplex".mhc_id IS 'Major histocompatibility complex';
CREATE TABLE "SimilarityCalculation" (
	chain_domain TEXT, 
	chain_codomain TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(chain_domain) REFERENCES "Chain" (akc_id), 
	FOREIGN KEY(chain_codomain) REFERENCES "Chain" (akc_id)
);COMMENT ON TABLE "SimilarityCalculation" IS 'None';COMMENT ON COLUMN "SimilarityCalculation".chain_domain IS 'Immune receptor chain element in binary relation domain';COMMENT ON COLUMN "SimilarityCalculation".chain_codomain IS 'Immune receptor chain element in binary relation codomain';COMMENT ON COLUMN "SimilarityCalculation".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "ChainSimilarity" (
	chain_similarity_type "ChainSimilarityTypeEnum", 
	chain_domain TEXT, 
	chain_codomain TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(chain_domain) REFERENCES "Chain" (akc_id), 
	FOREIGN KEY(chain_codomain) REFERENCES "Chain" (akc_id)
);COMMENT ON TABLE "ChainSimilarity" IS 'None';COMMENT ON COLUMN "ChainSimilarity".chain_similarity_type IS 'Type of similarity calculation between two immune receptor chains';COMMENT ON COLUMN "ChainSimilarity".chain_domain IS 'Immune receptor chain element in binary relation domain';COMMENT ON COLUMN "ChainSimilarity".chain_codomain IS 'Immune receptor chain element in binary relation codomain';COMMENT ON COLUMN "ChainSimilarity".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "SubjectGenotype" (
	id SERIAL NOT NULL, 
	receptor_genotype_set_id INTEGER, 
	mhc_genotype_set_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(receptor_genotype_set_id) REFERENCES "GenotypeSet" (id), 
	FOREIGN KEY(mhc_genotype_set_id) REFERENCES "MHCGenotypeSet" (id)
);COMMENT ON TABLE "SubjectGenotype" IS 'None';COMMENT ON COLUMN "SubjectGenotype".receptor_genotype_set_id IS 'Immune receptor genotype set for this subject.';COMMENT ON COLUMN "SubjectGenotype".mhc_genotype_set_id IS 'MHC genotype set for this subject.';
CREATE TABLE "SequencingRun" (
	id SERIAL NOT NULL, 
	sequencing_run_id TEXT, 
	total_reads_passing_qc_filter INTEGER, 
	sequencing_platform TEXT, 
	sequencing_facility TEXT, 
	sequencing_run_date TIMESTAMP WITHOUT TIME ZONE, 
	sequencing_kit TEXT, 
	sequencing_files_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(sequencing_files_id) REFERENCES "SequencingData" (id)
);COMMENT ON TABLE "SequencingRun" IS 'None';COMMENT ON COLUMN "SequencingRun".sequencing_run_id IS 'ID of sequencing run assigned by the sequencing facility';COMMENT ON COLUMN "SequencingRun".total_reads_passing_qc_filter IS 'Number of usable reads for analysis';COMMENT ON COLUMN "SequencingRun".sequencing_platform IS 'Designation of sequencing instrument used';COMMENT ON COLUMN "SequencingRun".sequencing_facility IS 'Name and address of sequencing facility';COMMENT ON COLUMN "SequencingRun".sequencing_run_date IS 'Date of sequencing run';COMMENT ON COLUMN "SequencingRun".sequencing_kit IS 'Name, manufacturer, order and lot numbers of sequencing kit';COMMENT ON COLUMN "SequencingRun".sequencing_files_id IS 'Set of sequencing files produced by the sequencing run';
CREATE TABLE "RepertoireFilter" (
	id SERIAL NOT NULL, 
	repertoire_id TEXT, 
	repertoire_description TEXT, 
	time_point_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_point_id) REFERENCES "TimePoint" (id)
);COMMENT ON TABLE "RepertoireFilter" IS 'None';COMMENT ON COLUMN "RepertoireFilter".time_point_id IS 'Time point designation for this repertoire within the group';
CREATE TABLE "ReceptorReactivity" (
	id SERIAL NOT NULL, 
	ligand_type "LigandTypeEnum", 
	antigen_type "AntigenTypeEnum", 
	antigen TEXT, 
	antigen_source_species "AntigenSourceSpeciesOntology", 
	peptide_start INTEGER, 
	peptide_end INTEGER, 
	mhc_class "MhcClassEnum", 
	mhc_gene_1 "MhcGene1Ontology", 
	mhc_allele_1 TEXT, 
	mhc_gene_2 "MhcGene2Ontology", 
	mhc_allele_2 TEXT, 
	reactivity_method "ReactivityMethodEnum", 
	reactivity_readout "ReactivityReadoutEnum", 
	reactivity_value FLOAT, 
	reactivity_unit TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(antigen) REFERENCES "Antigen" (akc_id)
);COMMENT ON TABLE "ReceptorReactivity" IS 'None';COMMENT ON COLUMN "ReceptorReactivity".ligand_type IS 'Classification of ligand binding to receptor';COMMENT ON COLUMN "ReceptorReactivity".antigen_type IS 'The type of antigen before processing by the immune system.';COMMENT ON COLUMN "ReceptorReactivity".antigen IS 'A material entity with antigen role';COMMENT ON COLUMN "ReceptorReactivity".antigen_source_species IS 'The species from which the antigen was isolated';COMMENT ON COLUMN "ReceptorReactivity".peptide_start IS 'Start position of the peptide within the reference protein sequence';COMMENT ON COLUMN "ReceptorReactivity".peptide_end IS 'End position of the peptide within the reference protein sequence';COMMENT ON COLUMN "ReceptorReactivity".mhc_gene_1 IS 'The MHC gene to which the mhc_allele_1 belongs';COMMENT ON COLUMN "ReceptorReactivity".mhc_allele_1 IS 'Allele designation of the MHC alpha chain';COMMENT ON COLUMN "ReceptorReactivity".mhc_gene_2 IS 'The MHC gene to which the mhc_allele_2 belongs';COMMENT ON COLUMN "ReceptorReactivity".mhc_allele_2 IS 'Allele designation of the MHC class II beta chain or the invariant beta2-microglobin chain';COMMENT ON COLUMN "ReceptorReactivity".reactivity_method IS 'The methodology used to assess expression (assay implemented in experiment)';COMMENT ON COLUMN "ReceptorReactivity".reactivity_readout IS 'Reactivity measurement read-out';COMMENT ON COLUMN "ReceptorReactivity".reactivity_value IS 'The absolute (processed) value of the measurement';COMMENT ON COLUMN "ReceptorReactivity".reactivity_unit IS 'The unit of the measurement';
CREATE TABLE "SampleProcessing" (
	id SERIAL NOT NULL, 
	sample_processing_id TEXT, 
	sample_id TEXT, 
	sample_type TEXT, 
	tissue "TissueOntology", 
	anatomic_site TEXT, 
	disease_state_sample TEXT, 
	collection_time_point_relative FLOAT, 
	collection_time_point_relative_unit "CollectionTimePointRelativeUnitOntology", 
	collection_time_point_reference TEXT, 
	biomaterial_provider TEXT, 
	tissue_processing TEXT, 
	cell_subset "CellSubsetOntology", 
	cell_phenotype TEXT, 
	cell_species "CellSpeciesOntology", 
	single_cell BOOLEAN, 
	cell_number INTEGER, 
	cells_per_reaction INTEGER, 
	cell_storage BOOLEAN, 
	cell_quality TEXT, 
	cell_isolation TEXT, 
	cell_processing_protocol TEXT, 
	template_class "TemplateClassEnum", 
	template_quality TEXT, 
	template_amount FLOAT, 
	template_amount_unit "TemplateAmountUnitOntology", 
	library_generation_method "LibraryGenerationMethodEnum", 
	library_generation_protocol TEXT, 
	library_generation_kit_version TEXT, 
	complete_sequences "CompleteSequencesEnum", 
	physical_linkage "PhysicalLinkageEnum", 
	sequencing_run_id TEXT, 
	total_reads_passing_qc_filter INTEGER, 
	sequencing_platform TEXT, 
	sequencing_facility TEXT, 
	sequencing_run_date TIMESTAMP WITHOUT TIME ZONE, 
	sequencing_kit TEXT, 
	sequencing_files_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(sequencing_files_id) REFERENCES "SequencingData" (id)
);COMMENT ON TABLE "SampleProcessing" IS 'None';COMMENT ON COLUMN "SampleProcessing".sample_id IS 'Sample ID assigned by submitter, unique within study. If possible, a persistent sample ID linked to INSDC or similar repository study should be used.';COMMENT ON COLUMN "SampleProcessing".sample_type IS 'The way the sample was obtained, e.g. fine-needle aspirate, organ harvest, peripheral venous puncture';COMMENT ON COLUMN "SampleProcessing".tissue IS 'The actual tissue sampled, e.g. lymph node, liver, peripheral blood';COMMENT ON COLUMN "SampleProcessing".anatomic_site IS 'The anatomic location of the tissue, e.g. Inguinal, femur';COMMENT ON COLUMN "SampleProcessing".disease_state_sample IS 'Histopathologic evaluation of the sample';COMMENT ON COLUMN "SampleProcessing".collection_time_point_relative IS 'Time point at which sample was taken, relative to `Collection time event`';COMMENT ON COLUMN "SampleProcessing".collection_time_point_relative_unit IS 'Unit of Sample collection time';COMMENT ON COLUMN "SampleProcessing".collection_time_point_reference IS 'Event in the study schedule to which `Sample collection time` relates to';COMMENT ON COLUMN "SampleProcessing".biomaterial_provider IS 'Name and address of the entity providing the sample';COMMENT ON COLUMN "SampleProcessing".tissue_processing IS 'Enzymatic digestion and/or physical methods used to isolate cells from sample';COMMENT ON COLUMN "SampleProcessing".cell_subset IS 'Commonly-used designation of isolated cell population';COMMENT ON COLUMN "SampleProcessing".cell_phenotype IS 'List of cellular markers and their expression levels used to isolate the cell population';COMMENT ON COLUMN "SampleProcessing".cell_species IS 'Binomial designation of the species from which the analyzed cells originate. Typically, this value should be identical to `species`, in which case it SHOULD NOT be set explicitly. However, there are valid experimental setups in which the two might differ, e.g., chimeric animal models. If set, this key will overwrite the `species` information for all lower layers of the schema.';COMMENT ON COLUMN "SampleProcessing".single_cell IS 'TRUE if single cells were isolated into separate compartments';COMMENT ON COLUMN "SampleProcessing".cell_number IS 'Total number of cells that went into the experiment';COMMENT ON COLUMN "SampleProcessing".cells_per_reaction IS 'Number of cells for each biological replicate';COMMENT ON COLUMN "SampleProcessing".cell_storage IS 'TRUE if cells were cryo-preserved between isolation and further processing';COMMENT ON COLUMN "SampleProcessing".cell_quality IS 'Relative amount of viable cells after preparation and (if applicable) thawing';COMMENT ON COLUMN "SampleProcessing".cell_isolation IS 'Description of the procedure used for marker-based isolation or enrich cells';COMMENT ON COLUMN "SampleProcessing".cell_processing_protocol IS 'Description of the methods applied to the sample including cell preparation/ isolation/enrichment and nucleic acid extraction. This should closely mirror the Materials and methods section in the manuscript.';COMMENT ON COLUMN "SampleProcessing".template_class IS 'The class of nucleic acid that was used as primary starting material for the following procedures';COMMENT ON COLUMN "SampleProcessing".template_quality IS 'Description and results of the quality control performed on the template material';COMMENT ON COLUMN "SampleProcessing".template_amount IS 'Amount of template that went into the process';COMMENT ON COLUMN "SampleProcessing".template_amount_unit IS 'Unit of template amount';COMMENT ON COLUMN "SampleProcessing".library_generation_method IS 'Generic type of library generation';COMMENT ON COLUMN "SampleProcessing".library_generation_protocol IS 'Description of processes applied to substrate to obtain a library that is ready for sequencing';COMMENT ON COLUMN "SampleProcessing".library_generation_kit_version IS 'When using a library generation protocol from a commercial provider, provide the protocol version number';COMMENT ON COLUMN "SampleProcessing".complete_sequences IS 'To be considered `complete`, the procedure used for library construction MUST generate sequences that 1) include the first V gene codon that encodes the mature polypeptide chain (i.e. after the leader sequence) and 2) include the last complete codon of the J gene (i.e. 1 bp 5'' of the J->C splice site) and 3) provide sequence information for all positions between 1) and 2). To be considered `complete & untemplated`, the sections of the sequences defined in points 1) to 3) of the previous sentence MUST be untemplated, i.e. MUST NOT overlap with the primers used in library preparation. `mixed` should only be used if the procedure used for library construction will likely produce multiple categories of sequences in the given experiment. It SHOULD NOT be used as a replacement of a NULL value.';COMMENT ON COLUMN "SampleProcessing".physical_linkage IS 'In case an experimental setup is used that physically links nucleic acids derived from distinct `Rearrangements` before library preparation, this field describes the mode of that linkage. All `hetero_*` terms indicate that in case of paired-read sequencing, the two reads should be expected to map to distinct IG/TR loci. `*_head-head` refers to techniques that link the 5'' ends of transcripts in a single-cell context. `*_tail-head` refers to techniques that link the 3'' end of one transcript to the 5'' end of another one in a single-cell context. This term does not provide any information whether a continuous reading-frame between the two is generated. `*_prelinked` refers to constructs in which the linkage was already present on the DNA level (e.g. scFv).';COMMENT ON COLUMN "SampleProcessing".sequencing_run_id IS 'ID of sequencing run assigned by the sequencing facility';COMMENT ON COLUMN "SampleProcessing".total_reads_passing_qc_filter IS 'Number of usable reads for analysis';COMMENT ON COLUMN "SampleProcessing".sequencing_platform IS 'Designation of sequencing instrument used';COMMENT ON COLUMN "SampleProcessing".sequencing_facility IS 'Name and address of sequencing facility';COMMENT ON COLUMN "SampleProcessing".sequencing_run_date IS 'Date of sequencing run';COMMENT ON COLUMN "SampleProcessing".sequencing_kit IS 'Name, manufacturer, order and lot numbers of sequencing kit';COMMENT ON COLUMN "SampleProcessing".sequencing_files_id IS 'Set of sequencing files produced by the sequencing run';
CREATE TABLE "Reference_sources" (
	"Reference_source_uri" TEXT, 
	sources TEXT, 
	PRIMARY KEY ("Reference_source_uri", sources), 
	FOREIGN KEY("Reference_source_uri") REFERENCES "Reference" (source_uri)
);COMMENT ON TABLE "Reference_sources" IS 'None';COMMENT ON COLUMN "Reference_sources"."Reference_source_uri" IS 'Autocreated FK slot';COMMENT ON COLUMN "Reference_sources".sources IS 'The source URLs for a reference';
CREATE TABLE "Reference_authors" (
	"Reference_source_uri" TEXT, 
	authors TEXT, 
	PRIMARY KEY ("Reference_source_uri", authors), 
	FOREIGN KEY("Reference_source_uri") REFERENCES "Reference" (source_uri)
);COMMENT ON TABLE "Reference_authors" IS 'None';COMMENT ON COLUMN "Reference_authors"."Reference_source_uri" IS 'Autocreated FK slot';COMMENT ON COLUMN "Reference_authors".authors IS 'The authors of a reference';
CREATE TABLE "DataSet_data_items" (
	"DataSet_id" INTEGER, 
	data_items_akc_id TEXT, 
	PRIMARY KEY ("DataSet_id", data_items_akc_id), 
	FOREIGN KEY("DataSet_id") REFERENCES "DataSet" (id), 
	FOREIGN KEY(data_items_akc_id) REFERENCES "AKObject" (akc_id)
);COMMENT ON TABLE "DataSet_data_items" IS 'None';COMMENT ON COLUMN "DataSet_data_items"."DataSet_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "DataSet_data_items".data_items_akc_id IS 'set of data items';
CREATE TABLE "AKDataItem_data_item_types" (
	"AKDataItem_akc_id" TEXT, 
	data_item_types "DataItemTypeEnum", 
	PRIMARY KEY ("AKDataItem_akc_id", data_item_types), 
	FOREIGN KEY("AKDataItem_akc_id") REFERENCES "AKDataItem" (akc_id)
);COMMENT ON TABLE "AKDataItem_data_item_types" IS 'None';COMMENT ON COLUMN "AKDataItem_data_item_types"."AKDataItem_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "AKDataItem_data_item_types".data_item_types IS 'semantic types of the data';
CREATE TABLE "AKDataSet_data_items" (
	"AKDataSet_akc_id" TEXT, 
	data_items_akc_id TEXT, 
	PRIMARY KEY ("AKDataSet_akc_id", data_items_akc_id), 
	FOREIGN KEY("AKDataSet_akc_id") REFERENCES "AKDataSet" (akc_id), 
	FOREIGN KEY(data_items_akc_id) REFERENCES "AKObject" (akc_id)
);COMMENT ON TABLE "AKDataSet_data_items" IS 'None';COMMENT ON COLUMN "AKDataSet_data_items"."AKDataSet_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "AKDataSet_data_items".data_items_akc_id IS 'set of data items';
CREATE TABLE "AKDataSet_data_item_types" (
	"AKDataSet_akc_id" TEXT, 
	data_item_types "DataItemTypeEnum", 
	PRIMARY KEY ("AKDataSet_akc_id", data_item_types), 
	FOREIGN KEY("AKDataSet_akc_id") REFERENCES "AKDataSet" (akc_id)
);COMMENT ON TABLE "AKDataSet_data_item_types" IS 'None';COMMENT ON COLUMN "AKDataSet_data_item_types"."AKDataSet_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "AKDataSet_data_item_types".data_item_types IS 'semantic types of the data';
CREATE TABLE "SequenceData_data_item_types" (
	"SequenceData_akc_id" TEXT, 
	data_item_types "DataItemTypeEnum", 
	PRIMARY KEY ("SequenceData_akc_id", data_item_types), 
	FOREIGN KEY("SequenceData_akc_id") REFERENCES "SequenceData" (akc_id)
);COMMENT ON TABLE "SequenceData_data_item_types" IS 'None';COMMENT ON COLUMN "SequenceData_data_item_types"."SequenceData_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "SequenceData_data_item_types".data_item_types IS 'semantic types of the data';
CREATE TABLE "AIRRSequencingData_data_item_types" (
	"AIRRSequencingData_akc_id" TEXT, 
	data_item_types "DataItemTypeEnum", 
	PRIMARY KEY ("AIRRSequencingData_akc_id", data_item_types), 
	FOREIGN KEY("AIRRSequencingData_akc_id") REFERENCES "AIRRSequencingData" (akc_id)
);COMMENT ON TABLE "AIRRSequencingData_data_item_types" IS 'None';COMMENT ON COLUMN "AIRRSequencingData_data_item_types"."AIRRSequencingData_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "AIRRSequencingData_data_item_types".data_item_types IS 'semantic types of the data';
CREATE TABLE "RNATranscriptomeData_data_item_types" (
	"RNATranscriptomeData_akc_id" TEXT, 
	data_item_types "DataItemTypeEnum", 
	PRIMARY KEY ("RNATranscriptomeData_akc_id", data_item_types), 
	FOREIGN KEY("RNATranscriptomeData_akc_id") REFERENCES "RNATranscriptomeData" (akc_id)
);COMMENT ON TABLE "RNATranscriptomeData_data_item_types" IS 'None';COMMENT ON COLUMN "RNATranscriptomeData_data_item_types"."RNATranscriptomeData_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "RNATranscriptomeData_data_item_types".data_item_types IS 'semantic types of the data';
CREATE TABLE "DataTransformation_data_transformation_types" (
	"DataTransformation_akc_id" TEXT, 
	data_transformation_types "DataItemTypeEnum", 
	PRIMARY KEY ("DataTransformation_akc_id", data_transformation_types), 
	FOREIGN KEY("DataTransformation_akc_id") REFERENCES "DataTransformation" (akc_id)
);COMMENT ON TABLE "DataTransformation_data_transformation_types" IS 'None';COMMENT ON COLUMN "DataTransformation_data_transformation_types"."DataTransformation_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "DataTransformation_data_transformation_types".data_transformation_types IS 'semantic types of the data transformation';
CREATE TABLE "Conclusion_datasets" (
	"Conclusion_akc_id" TEXT, 
	datasets_akc_id TEXT, 
	PRIMARY KEY ("Conclusion_akc_id", datasets_akc_id), 
	FOREIGN KEY("Conclusion_akc_id") REFERENCES "Conclusion" (akc_id), 
	FOREIGN KEY(datasets_akc_id) REFERENCES "AKDataSet" (akc_id)
);COMMENT ON TABLE "Conclusion_datasets" IS 'None';COMMENT ON COLUMN "Conclusion_datasets"."Conclusion_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Conclusion_datasets".datasets_akc_id IS 'The datasets that support a conclusion';
CREATE TABLE "SequenceDelineationV_alignment_labels" (
	"SequenceDelineationV_id" INTEGER, 
	alignment_labels TEXT, 
	PRIMARY KEY ("SequenceDelineationV_id", alignment_labels), 
	FOREIGN KEY("SequenceDelineationV_id") REFERENCES "SequenceDelineationV" (id)
);COMMENT ON TABLE "SequenceDelineationV_alignment_labels" IS 'None';COMMENT ON COLUMN "SequenceDelineationV_alignment_labels"."SequenceDelineationV_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "SequenceDelineationV_alignment_labels".alignment_labels IS 'One string for each codon in the aligned_sequence indicating the label of that codon according to  the numbering of the delineation scheme if it provides one.';
CREATE TABLE "AlleleDescription_acknowledgements" (
	"AlleleDescription_id" INTEGER, 
	acknowledgements_id INTEGER, 
	PRIMARY KEY ("AlleleDescription_id", acknowledgements_id), 
	FOREIGN KEY("AlleleDescription_id") REFERENCES "AlleleDescription" (id), 
	FOREIGN KEY(acknowledgements_id) REFERENCES "Acknowledgement" (id)
);COMMENT ON TABLE "AlleleDescription_acknowledgements" IS 'None';COMMENT ON COLUMN "AlleleDescription_acknowledgements"."AlleleDescription_id" IS 'Autocreated FK slot';
CREATE TABLE "AlleleDescription_aliases" (
	"AlleleDescription_id" INTEGER, 
	aliases TEXT, 
	PRIMARY KEY ("AlleleDescription_id", aliases), 
	FOREIGN KEY("AlleleDescription_id") REFERENCES "AlleleDescription" (id)
);COMMENT ON TABLE "AlleleDescription_aliases" IS 'None';COMMENT ON COLUMN "AlleleDescription_aliases"."AlleleDescription_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "AlleleDescription_aliases".aliases IS 'Alternative names for this sequence';
CREATE TABLE "AlleleDescription_v_gene_delineations" (
	"AlleleDescription_id" INTEGER, 
	v_gene_delineations_id INTEGER, 
	PRIMARY KEY ("AlleleDescription_id", v_gene_delineations_id), 
	FOREIGN KEY("AlleleDescription_id") REFERENCES "AlleleDescription" (id), 
	FOREIGN KEY(v_gene_delineations_id) REFERENCES "SequenceDelineationV" (id)
);COMMENT ON TABLE "AlleleDescription_v_gene_delineations" IS 'None';COMMENT ON COLUMN "AlleleDescription_v_gene_delineations"."AlleleDescription_id" IS 'Autocreated FK slot';
CREATE TABLE "AlleleDescription_unrearranged_support" (
	"AlleleDescription_id" INTEGER, 
	unrearranged_support_id INTEGER, 
	PRIMARY KEY ("AlleleDescription_id", unrearranged_support_id), 
	FOREIGN KEY("AlleleDescription_id") REFERENCES "AlleleDescription" (id), 
	FOREIGN KEY(unrearranged_support_id) REFERENCES "UnrearrangedSequence" (id)
);COMMENT ON TABLE "AlleleDescription_unrearranged_support" IS 'None';COMMENT ON COLUMN "AlleleDescription_unrearranged_support"."AlleleDescription_id" IS 'Autocreated FK slot';
CREATE TABLE "AlleleDescription_rearranged_support" (
	"AlleleDescription_id" INTEGER, 
	rearranged_support_id INTEGER, 
	PRIMARY KEY ("AlleleDescription_id", rearranged_support_id), 
	FOREIGN KEY("AlleleDescription_id") REFERENCES "AlleleDescription" (id), 
	FOREIGN KEY(rearranged_support_id) REFERENCES "RearrangedSequence" (id)
);COMMENT ON TABLE "AlleleDescription_rearranged_support" IS 'None';COMMENT ON COLUMN "AlleleDescription_rearranged_support"."AlleleDescription_id" IS 'Autocreated FK slot';
CREATE TABLE "AlleleDescription_paralogs" (
	"AlleleDescription_id" INTEGER, 
	paralogs TEXT, 
	PRIMARY KEY ("AlleleDescription_id", paralogs), 
	FOREIGN KEY("AlleleDescription_id") REFERENCES "AlleleDescription" (id)
);COMMENT ON TABLE "AlleleDescription_paralogs" IS 'None';COMMENT ON COLUMN "AlleleDescription_paralogs"."AlleleDescription_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "AlleleDescription_paralogs".paralogs IS 'Gene symbols of any paralogs';
CREATE TABLE "AlleleDescription_curational_tags" (
	"AlleleDescription_id" INTEGER, 
	curational_tags "CurationalTagsEnum", 
	PRIMARY KEY ("AlleleDescription_id", curational_tags), 
	FOREIGN KEY("AlleleDescription_id") REFERENCES "AlleleDescription" (id)
);COMMENT ON TABLE "AlleleDescription_curational_tags" IS 'None';COMMENT ON COLUMN "AlleleDescription_curational_tags"."AlleleDescription_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "AlleleDescription_curational_tags".curational_tags IS 'Controlled-vocabulary tags applied to this description';
CREATE TABLE "GermlineSet_acknowledgements" (
	"GermlineSet_id" INTEGER, 
	acknowledgements_id INTEGER, 
	PRIMARY KEY ("GermlineSet_id", acknowledgements_id), 
	FOREIGN KEY("GermlineSet_id") REFERENCES "GermlineSet" (id), 
	FOREIGN KEY(acknowledgements_id) REFERENCES "Acknowledgement" (id)
);COMMENT ON TABLE "GermlineSet_acknowledgements" IS 'None';COMMENT ON COLUMN "GermlineSet_acknowledgements"."GermlineSet_id" IS 'Autocreated FK slot';
CREATE TABLE "GermlineSet_allele_descriptions" (
	"GermlineSet_id" INTEGER, 
	allele_descriptions_id INTEGER, 
	PRIMARY KEY ("GermlineSet_id", allele_descriptions_id), 
	FOREIGN KEY("GermlineSet_id") REFERENCES "GermlineSet" (id), 
	FOREIGN KEY(allele_descriptions_id) REFERENCES "AlleleDescription" (id)
);COMMENT ON TABLE "GermlineSet_allele_descriptions" IS 'None';COMMENT ON COLUMN "GermlineSet_allele_descriptions"."GermlineSet_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "GermlineSet_allele_descriptions".allele_descriptions_id IS 'list of allele_descriptions in the germline set';
CREATE TABLE "GenotypeSet_genotype_class_list" (
	"GenotypeSet_id" INTEGER, 
	genotype_class_list_id INTEGER, 
	PRIMARY KEY ("GenotypeSet_id", genotype_class_list_id), 
	FOREIGN KEY("GenotypeSet_id") REFERENCES "GenotypeSet" (id), 
	FOREIGN KEY(genotype_class_list_id) REFERENCES "Genotype" (id)
);COMMENT ON TABLE "GenotypeSet_genotype_class_list" IS 'None';COMMENT ON COLUMN "GenotypeSet_genotype_class_list"."GenotypeSet_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "GenotypeSet_genotype_class_list".genotype_class_list_id IS 'List of Genotypes included in this Receptor Genotype Set.';
CREATE TABLE "Genotype_documented_alleles" (
	"Genotype_id" INTEGER, 
	documented_alleles_id INTEGER, 
	PRIMARY KEY ("Genotype_id", documented_alleles_id), 
	FOREIGN KEY("Genotype_id") REFERENCES "Genotype" (id), 
	FOREIGN KEY(documented_alleles_id) REFERENCES "DocumentedAllele" (id)
);COMMENT ON TABLE "Genotype_documented_alleles" IS 'None';COMMENT ON COLUMN "Genotype_documented_alleles"."Genotype_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Genotype_documented_alleles".documented_alleles_id IS 'List of alleles documented in reference set(s)';
CREATE TABLE "Genotype_undocumented_alleles" (
	"Genotype_id" INTEGER, 
	undocumented_alleles_id INTEGER, 
	PRIMARY KEY ("Genotype_id", undocumented_alleles_id), 
	FOREIGN KEY("Genotype_id") REFERENCES "Genotype" (id), 
	FOREIGN KEY(undocumented_alleles_id) REFERENCES "UndocumentedAllele" (id)
);COMMENT ON TABLE "Genotype_undocumented_alleles" IS 'None';COMMENT ON COLUMN "Genotype_undocumented_alleles"."Genotype_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Genotype_undocumented_alleles".undocumented_alleles_id IS 'List of alleles inferred to be present and not documented in an identified GermlineSet';
CREATE TABLE "Genotype_deleted_genes" (
	"Genotype_id" INTEGER, 
	deleted_genes_id INTEGER, 
	PRIMARY KEY ("Genotype_id", deleted_genes_id), 
	FOREIGN KEY("Genotype_id") REFERENCES "Genotype" (id), 
	FOREIGN KEY(deleted_genes_id) REFERENCES "DeletedGene" (id)
);COMMENT ON TABLE "Genotype_deleted_genes" IS 'None';COMMENT ON COLUMN "Genotype_deleted_genes"."Genotype_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Genotype_deleted_genes".deleted_genes_id IS 'Array of genes identified as being deleted in this genotype';
CREATE TABLE "MHCGenotypeSet_mhc_genotype_list" (
	"MHCGenotypeSet_id" INTEGER, 
	mhc_genotype_list_id INTEGER, 
	PRIMARY KEY ("MHCGenotypeSet_id", mhc_genotype_list_id), 
	FOREIGN KEY("MHCGenotypeSet_id") REFERENCES "MHCGenotypeSet" (id), 
	FOREIGN KEY(mhc_genotype_list_id) REFERENCES "MHCGenotype" (id)
);COMMENT ON TABLE "MHCGenotypeSet_mhc_genotype_list" IS 'None';COMMENT ON COLUMN "MHCGenotypeSet_mhc_genotype_list"."MHCGenotypeSet_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "MHCGenotypeSet_mhc_genotype_list".mhc_genotype_list_id IS 'List of MHCGenotypes included in this set';
CREATE TABLE "MHCGenotype_mhc_alleles" (
	"MHCGenotype_id" INTEGER, 
	mhc_alleles_id INTEGER, 
	PRIMARY KEY ("MHCGenotype_id", mhc_alleles_id), 
	FOREIGN KEY("MHCGenotype_id") REFERENCES "MHCGenotype" (id), 
	FOREIGN KEY(mhc_alleles_id) REFERENCES "MHCAllele" (id)
);COMMENT ON TABLE "MHCGenotype_mhc_alleles" IS 'None';COMMENT ON COLUMN "MHCGenotype_mhc_alleles"."MHCGenotype_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "MHCGenotype_mhc_alleles".mhc_alleles_id IS 'List of MHC alleles of the indicated mhc_class identified in an individual';
CREATE TABLE "Study_keywords_study" (
	"Study_id" INTEGER, 
	keywords_study "KeywordsStudyEnum", 
	PRIMARY KEY ("Study_id", keywords_study), 
	FOREIGN KEY("Study_id") REFERENCES "Study" (id)
);COMMENT ON TABLE "Study_keywords_study" IS 'None';COMMENT ON COLUMN "Study_keywords_study"."Study_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Study_keywords_study".keywords_study IS 'Keywords describing properties of one or more data sets in a study. "contains_schema" keywords indicate that the study contains data objects from the AIRR Schema of that type (Rearrangement, Clone, Cell, Receptor) while the other keywords indicate that the study design considers the type of data indicated (e.g. it is possible to have a study that "contains_paired_chain" but does not "contains_schema_cell").';
CREATE TABLE "NucleicAcidProcessing_pcr_target" (
	"NucleicAcidProcessing_id" INTEGER, 
	pcr_target_id INTEGER, 
	PRIMARY KEY ("NucleicAcidProcessing_id", pcr_target_id), 
	FOREIGN KEY("NucleicAcidProcessing_id") REFERENCES "NucleicAcidProcessing" (id), 
	FOREIGN KEY(pcr_target_id) REFERENCES "PCRTarget" (id)
);COMMENT ON TABLE "NucleicAcidProcessing_pcr_target" IS 'None';COMMENT ON COLUMN "NucleicAcidProcessing_pcr_target"."NucleicAcidProcessing_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "NucleicAcidProcessing_pcr_target".pcr_target_id IS 'If a PCR step was performed that specifically targets the IG/TR loci, the target and primer locations need to be provided here. This field holds an array of PCRTarget objects, so that multiplex PCR setups amplifying multiple loci at the same time can be annotated using one record per locus. PCR setups not targeting any specific locus must not annotate this field but select the appropriate library_generation_method instead.';
CREATE TABLE "DataProcessing_data_processing_files" (
	"DataProcessing_id" INTEGER, 
	data_processing_files TEXT, 
	PRIMARY KEY ("DataProcessing_id", data_processing_files), 
	FOREIGN KEY("DataProcessing_id") REFERENCES "DataProcessing" (id)
);COMMENT ON TABLE "DataProcessing_data_processing_files" IS 'None';COMMENT ON COLUMN "DataProcessing_data_processing_files"."DataProcessing_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "DataProcessing_data_processing_files".data_processing_files IS 'Array of file names for data produced by this data processing.';
CREATE TABLE "Clone_sequences" (
	"Clone_id" INTEGER, 
	sequences TEXT, 
	PRIMARY KEY ("Clone_id", sequences), 
	FOREIGN KEY("Clone_id") REFERENCES "Clone" (id)
);COMMENT ON TABLE "Clone_sequences" IS 'None';COMMENT ON COLUMN "Clone_sequences"."Clone_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Clone_sequences".sequences IS 'List sequence_id strings that act as keys to the Rearrangement records for members of the clone.';
CREATE TABLE "Tree_nodes" (
	"Tree_id" INTEGER, 
	nodes_id INTEGER, 
	PRIMARY KEY ("Tree_id", nodes_id), 
	FOREIGN KEY("Tree_id") REFERENCES "Tree" (id), 
	FOREIGN KEY(nodes_id) REFERENCES "Node" (id)
);COMMENT ON TABLE "Tree_nodes" IS 'None';COMMENT ON COLUMN "Tree_nodes"."Tree_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Tree_nodes".nodes_id IS 'Dictionary of nodes in the tree, keyed by sequence_id string';
CREATE TABLE "Cell_rearrangements" (
	"Cell_id" INTEGER, 
	rearrangements TEXT, 
	PRIMARY KEY ("Cell_id", rearrangements), 
	FOREIGN KEY("Cell_id") REFERENCES "Cell" (id)
);COMMENT ON TABLE "Cell_rearrangements" IS 'None';COMMENT ON COLUMN "Cell_rearrangements"."Cell_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Cell_rearrangements".rearrangements IS 'Array of sequence identifiers defined for the Rearrangement object';
CREATE TABLE "Cell_receptors" (
	"Cell_id" INTEGER, 
	receptors TEXT, 
	PRIMARY KEY ("Cell_id", receptors), 
	FOREIGN KEY("Cell_id") REFERENCES "Cell" (id)
);COMMENT ON TABLE "Cell_receptors" IS 'None';COMMENT ON COLUMN "Cell_receptors"."Cell_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Cell_receptors".receptors IS 'Array of receptor identifiers defined for the Receptor object';
CREATE TABLE "Receptor_receptor_ref" (
	"Receptor_id" INTEGER, 
	receptor_ref TEXT, 
	PRIMARY KEY ("Receptor_id", receptor_ref), 
	FOREIGN KEY("Receptor_id") REFERENCES "Receptor" (id)
);COMMENT ON TABLE "Receptor_receptor_ref" IS 'None';COMMENT ON COLUMN "Receptor_receptor_ref"."Receptor_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Receptor_receptor_ref".receptor_ref IS 'Array of receptor identifiers defined for the Receptor object';
CREATE TABLE "StudyArm" (
	investigation TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(investigation) REFERENCES "Investigation" (akc_id)
);COMMENT ON TABLE "StudyArm" IS 'A population of participants of an investigation.';COMMENT ON COLUMN "StudyArm".investigation IS 'An investigation in which the study arm participates';COMMENT ON COLUMN "StudyArm".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "StudyArm".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "StudyArm".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "AntibodyAntigenComplex" (
	antibody TEXT, 
	antigen TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(antibody) REFERENCES "BCellReceptor" (akc_id), 
	FOREIGN KEY(antigen) REFERENCES "Antigen" (akc_id)
);COMMENT ON TABLE "AntibodyAntigenComplex" IS 'None';COMMENT ON COLUMN "AntibodyAntigenComplex".antibody IS 'B cell receptor, immunoglobulin antibody';COMMENT ON COLUMN "AntibodyAntigenComplex".antigen IS 'A material entity with antigen role';COMMENT ON COLUMN "AntibodyAntigenComplex".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "AntibodyAntigenComplex".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "AntibodyAntigenComplex".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "Subject" (
	id SERIAL NOT NULL, 
	subject_id TEXT, 
	synthetic BOOLEAN, 
	species "SpeciesOntology", 
	sex "SexEnum", 
	age_min FLOAT, 
	age_max FLOAT, 
	age_unit "AgeUnitOntology", 
	age_event TEXT, 
	ancestry_population TEXT, 
	ethnicity TEXT, 
	race TEXT, 
	strain_name TEXT, 
	linked_subjects TEXT, 
	link_type TEXT, 
	genotype_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(genotype_id) REFERENCES "SubjectGenotype" (id)
);COMMENT ON TABLE "Subject" IS 'None';COMMENT ON COLUMN "Subject".subject_id IS 'Subject ID assigned by submitter, unique within study. If possible, a persistent subject ID linked to an INSDC or similar repository study should be used.';COMMENT ON COLUMN "Subject".synthetic IS 'TRUE for libraries in which the diversity has been synthetically generated (e.g. phage display)';COMMENT ON COLUMN "Subject".species IS 'Binomial designation of subject''s species';COMMENT ON COLUMN "Subject".sex IS 'Biological sex of subject';COMMENT ON COLUMN "Subject".age_min IS 'Specific age or lower boundary of age range.';COMMENT ON COLUMN "Subject".age_max IS 'Upper boundary of age range or equal to age_min for specific age. This field should only be null if age_min is null.';COMMENT ON COLUMN "Subject".age_unit IS 'Unit of age range';COMMENT ON COLUMN "Subject".age_event IS 'Event in the study schedule to which `Age` refers. For NCBI BioSample this MUST be `sampling`. For other implementations submitters need to be aware that there is currently no mechanism to encode to potential delta between `Age event` and `Sample collection time`, hence the chosen events should be in temporal proximity.';COMMENT ON COLUMN "Subject".ancestry_population IS 'Broad geographic origin of ancestry (continent)';COMMENT ON COLUMN "Subject".ethnicity IS 'Ethnic group of subject (defined as cultural/language-based membership)';COMMENT ON COLUMN "Subject".race IS 'Racial group of subject (as defined by NIH)';COMMENT ON COLUMN "Subject".strain_name IS 'Non-human designation of the strain or breed of animal used';COMMENT ON COLUMN "Subject".linked_subjects IS 'Subject ID to which `Relation type` refers';COMMENT ON COLUMN "Subject".link_type IS 'Relation between subject and `linked_subjects`, can be genetic or environmental (e.g.exposure)';
CREATE TABLE "Investigation_simulations" (
	"Investigation_akc_id" TEXT, 
	simulations_akc_id TEXT, 
	PRIMARY KEY ("Investigation_akc_id", simulations_akc_id), 
	FOREIGN KEY("Investigation_akc_id") REFERENCES "Investigation" (akc_id), 
	FOREIGN KEY(simulations_akc_id) REFERENCES "Simulation" (akc_id)
);COMMENT ON TABLE "Investigation_simulations" IS 'None';COMMENT ON COLUMN "Investigation_simulations"."Investigation_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Investigation_simulations".simulations_akc_id IS 'The simulations performed by the investigation';
CREATE TABLE "Investigation_documents" (
	"Investigation_akc_id" TEXT, 
	documents_source_uri TEXT, 
	PRIMARY KEY ("Investigation_akc_id", documents_source_uri), 
	FOREIGN KEY("Investigation_akc_id") REFERENCES "Investigation" (akc_id), 
	FOREIGN KEY(documents_source_uri) REFERENCES "Reference" (source_uri)
);COMMENT ON TABLE "Investigation_documents" IS 'None';COMMENT ON COLUMN "Investigation_documents"."Investigation_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Investigation_documents".documents_source_uri IS 'The documents produced by the investigation';
CREATE TABLE "Investigation_conclusions" (
	"Investigation_akc_id" TEXT, 
	conclusions_akc_id TEXT, 
	PRIMARY KEY ("Investigation_akc_id", conclusions_akc_id), 
	FOREIGN KEY("Investigation_akc_id") REFERENCES "Investigation" (akc_id), 
	FOREIGN KEY(conclusions_akc_id) REFERENCES "Conclusion" (akc_id)
);COMMENT ON TABLE "Investigation_conclusions" IS 'None';COMMENT ON COLUMN "Investigation_conclusions"."Investigation_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Investigation_conclusions".conclusions_akc_id IS 'The conclusions from the investigation';
CREATE TABLE "Reference_investigations" (
	"Reference_source_uri" TEXT, 
	investigations_akc_id TEXT, 
	PRIMARY KEY ("Reference_source_uri", investigations_akc_id), 
	FOREIGN KEY("Reference_source_uri") REFERENCES "Reference" (source_uri), 
	FOREIGN KEY(investigations_akc_id) REFERENCES "Investigation" (akc_id)
);COMMENT ON TABLE "Reference_investigations" IS 'None';COMMENT ON COLUMN "Reference_investigations"."Reference_source_uri" IS 'Autocreated FK slot';COMMENT ON COLUMN "Reference_investigations".investigations_akc_id IS 'The investigations that a reference or conclusion are about';
CREATE TABLE "DataTransformation_was_generated_by" (
	"DataTransformation_akc_id" TEXT, 
	was_generated_by_id INTEGER, 
	PRIMARY KEY ("DataTransformation_akc_id", was_generated_by_id), 
	FOREIGN KEY("DataTransformation_akc_id") REFERENCES "DataTransformation" (akc_id), 
	FOREIGN KEY(was_generated_by_id) REFERENCES "InputOutputDataMap" (id)
);COMMENT ON TABLE "DataTransformation_was_generated_by" IS 'None';COMMENT ON COLUMN "DataTransformation_was_generated_by"."DataTransformation_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "DataTransformation_was_generated_by".was_generated_by_id IS 'direct provenance link of one entity (input) to another (output) for a data transformation';
CREATE TABLE "Conclusion_investigations" (
	"Conclusion_akc_id" TEXT, 
	investigations_akc_id TEXT, 
	PRIMARY KEY ("Conclusion_akc_id", investigations_akc_id), 
	FOREIGN KEY("Conclusion_akc_id") REFERENCES "Conclusion" (akc_id), 
	FOREIGN KEY(investigations_akc_id) REFERENCES "Investigation" (akc_id)
);COMMENT ON TABLE "Conclusion_investigations" IS 'None';COMMENT ON COLUMN "Conclusion_investigations"."Conclusion_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Conclusion_investigations".investigations_akc_id IS 'The investigations that a reference or conclusion are about';
CREATE TABLE "RepertoireGroup_repertoires" (
	"RepertoireGroup_id" INTEGER, 
	repertoires_id INTEGER, 
	PRIMARY KEY ("RepertoireGroup_id", repertoires_id), 
	FOREIGN KEY("RepertoireGroup_id") REFERENCES "RepertoireGroup" (id), 
	FOREIGN KEY(repertoires_id) REFERENCES "RepertoireFilter" (id)
);COMMENT ON TABLE "RepertoireGroup_repertoires" IS 'None';COMMENT ON COLUMN "RepertoireGroup_repertoires"."RepertoireGroup_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "RepertoireGroup_repertoires".repertoires_id IS 'List of repertoires in this collection with an associated description and time point designation';
CREATE TABLE "Receptor_reactivity_measurements" (
	"Receptor_id" INTEGER, 
	reactivity_measurements_id INTEGER, 
	PRIMARY KEY ("Receptor_id", reactivity_measurements_id), 
	FOREIGN KEY("Receptor_id") REFERENCES "Receptor" (id), 
	FOREIGN KEY(reactivity_measurements_id) REFERENCES "ReceptorReactivity" (id)
);COMMENT ON TABLE "Receptor_reactivity_measurements" IS 'None';COMMENT ON COLUMN "Receptor_reactivity_measurements"."Receptor_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Receptor_reactivity_measurements".reactivity_measurements_id IS 'Records of reactivity measurement';
CREATE TABLE "SampleProcessing_pcr_target" (
	"SampleProcessing_id" INTEGER, 
	pcr_target_id INTEGER, 
	PRIMARY KEY ("SampleProcessing_id", pcr_target_id), 
	FOREIGN KEY("SampleProcessing_id") REFERENCES "SampleProcessing" (id), 
	FOREIGN KEY(pcr_target_id) REFERENCES "PCRTarget" (id)
);COMMENT ON TABLE "SampleProcessing_pcr_target" IS 'None';COMMENT ON COLUMN "SampleProcessing_pcr_target"."SampleProcessing_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "SampleProcessing_pcr_target".pcr_target_id IS 'If a PCR step was performed that specifically targets the IG/TR loci, the target and primer locations need to be provided here. This field holds an array of PCRTarget objects, so that multiplex PCR setups amplifying multiple loci at the same time can be annotated using one record per locus. PCR setups not targeting any specific locus must not annotate this field but select the appropriate library_generation_method instead.';
CREATE TABLE "Participant" (
	study_arm TEXT, 
	species "SpeciesOntology", 
	sex "BiologicalSexOntology", 
	age TEXT, 
	age_unit "AgeUnitOntology", 
	age_event TEXT, 
	race TEXT, 
	ethnicity TEXT, 
	geolocation "GeolocationOntology", 
	strain "StrainEnum", 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(study_arm) REFERENCES "StudyArm" (akc_id)
);COMMENT ON TABLE "Participant" IS 'A participant in an investigation.';COMMENT ON COLUMN "Participant".study_arm IS 'The study arm that a participant is a member of';COMMENT ON COLUMN "Participant".species IS 'Binomial designation of subject''s species';COMMENT ON COLUMN "Participant".sex IS 'Biological sex of subject';COMMENT ON COLUMN "Participant".age IS 'The age of a participant relative to age_event';COMMENT ON COLUMN "Participant".age_unit IS 'Unit of age range';COMMENT ON COLUMN "Participant".age_event IS 'Event in the study schedule to which `Age` refers. For NCBI BioSample this MUST be `sampling`. For other implementations submitters need to be aware that there is currently no mechanism to encode to potential delta between `Age event` and `Sample collection time`, hence the chosen events should be in temporal proximity.';COMMENT ON COLUMN "Participant".race IS 'Racial group of subject (as defined by NIH)';COMMENT ON COLUMN "Participant".ethnicity IS 'Ethnic group of subject (defined as cultural/language-based membership)';COMMENT ON COLUMN "Participant".geolocation IS 'The geolocation of a participant at birth';COMMENT ON COLUMN "Participant".strain IS 'The strain of the participant (non-human study participants)';COMMENT ON COLUMN "Participant".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "Participant".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "Participant".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "Repertoire" (
	id SERIAL NOT NULL, 
	repertoire_id TEXT, 
	repertoire_name TEXT, 
	repertoire_description TEXT, 
	study_id INTEGER, 
	subject_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(study_id) REFERENCES "Study" (id), 
	FOREIGN KEY(subject_id) REFERENCES "Subject" (id)
);COMMENT ON TABLE "Repertoire" IS 'None';COMMENT ON COLUMN "Repertoire".repertoire_name IS 'Short generic display name for the repertoire';COMMENT ON COLUMN "Repertoire".study_id IS 'Study object';COMMENT ON COLUMN "Repertoire".subject_id IS 'Subject object';
CREATE TABLE "StudyEvent_study_arms" (
	"StudyEvent_akc_id" TEXT, 
	study_arms_akc_id TEXT, 
	PRIMARY KEY ("StudyEvent_akc_id", study_arms_akc_id), 
	FOREIGN KEY("StudyEvent_akc_id") REFERENCES "StudyEvent" (akc_id), 
	FOREIGN KEY(study_arms_akc_id) REFERENCES "StudyArm" (akc_id)
);COMMENT ON TABLE "StudyEvent_study_arms" IS 'None';COMMENT ON COLUMN "StudyEvent_study_arms"."StudyEvent_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "StudyEvent_study_arms".study_arms_akc_id IS 'The study arms that are relevant for a study event';
CREATE TABLE "Subject_diagnosis" (
	"Subject_id" INTEGER, 
	diagnosis_id INTEGER, 
	PRIMARY KEY ("Subject_id", diagnosis_id), 
	FOREIGN KEY("Subject_id") REFERENCES "Subject" (id), 
	FOREIGN KEY(diagnosis_id) REFERENCES "Diagnosis" (id)
);COMMENT ON TABLE "Subject_diagnosis" IS 'None';COMMENT ON COLUMN "Subject_diagnosis"."Subject_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Subject_diagnosis".diagnosis_id IS 'Diagnosis information for subject';
CREATE TABLE "LifeEvent" (
	type TEXT, 
	participant TEXT, 
	study_event TEXT, 
	life_event_type "LifeEventProcessOntology", 
	geolocation "GeolocationOntology", 
	t0_event TEXT, 
	start INTEGER, 
	duration INTEGER, 
	time_unit TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(participant) REFERENCES "Participant" (akc_id), 
	FOREIGN KEY(study_event) REFERENCES "StudyEvent" (akc_id), 
	FOREIGN KEY(t0_event) REFERENCES "LifeEvent" (akc_id)
);COMMENT ON TABLE "LifeEvent" IS 'An event in which a study participant participates.';COMMENT ON COLUMN "LifeEvent".participant IS 'The participant of a life event';COMMENT ON COLUMN "LifeEvent".study_event IS 'The study event corresponding to a life event';COMMENT ON COLUMN "LifeEvent".life_event_type IS 'The specific type of a life event';COMMENT ON COLUMN "LifeEvent".geolocation IS 'The geolocation of a participant at birth';COMMENT ON COLUMN "LifeEvent".t0_event IS 'The T0 event used to specify the time of this life event';COMMENT ON COLUMN "LifeEvent".start IS 'The start time of this life event, relative to the T0 event';COMMENT ON COLUMN "LifeEvent".duration IS 'The duration of this life event';COMMENT ON COLUMN "LifeEvent".time_unit IS 'The time unit used to measure the start and duration of this life event';COMMENT ON COLUMN "LifeEvent".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "LifeEvent".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "LifeEvent".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "Investigation_participants" (
	"Investigation_akc_id" TEXT, 
	participants_akc_id TEXT, 
	PRIMARY KEY ("Investigation_akc_id", participants_akc_id), 
	FOREIGN KEY("Investigation_akc_id") REFERENCES "Investigation" (akc_id), 
	FOREIGN KEY(participants_akc_id) REFERENCES "Participant" (akc_id)
);COMMENT ON TABLE "Investigation_participants" IS 'None';COMMENT ON COLUMN "Investigation_participants"."Investigation_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Investigation_participants".participants_akc_id IS 'The participants involved with the investigation';
CREATE TABLE "Repertoire_sample" (
	"Repertoire_id" INTEGER, 
	sample_id INTEGER, 
	PRIMARY KEY ("Repertoire_id", sample_id), 
	FOREIGN KEY("Repertoire_id") REFERENCES "Repertoire" (id), 
	FOREIGN KEY(sample_id) REFERENCES "SampleProcessing" (id)
);COMMENT ON TABLE "Repertoire_sample" IS 'None';COMMENT ON COLUMN "Repertoire_sample"."Repertoire_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Repertoire_sample".sample_id IS 'List of Sample Processing objects';
CREATE TABLE "Repertoire_data_processing" (
	"Repertoire_id" INTEGER, 
	data_processing_id INTEGER, 
	PRIMARY KEY ("Repertoire_id", data_processing_id), 
	FOREIGN KEY("Repertoire_id") REFERENCES "Repertoire" (id), 
	FOREIGN KEY(data_processing_id) REFERENCES "DataProcessing" (id)
);COMMENT ON TABLE "Repertoire_data_processing" IS 'None';COMMENT ON COLUMN "Repertoire_data_processing"."Repertoire_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Repertoire_data_processing".data_processing_id IS 'List of Data Processing objects';
CREATE TABLE "ImmuneExposure" (
	exposure_material "ExposureMaterialOntology", 
	disease "DiseaseOntology", 
	disease_stage TEXT, 
	disease_severity TEXT, 
	type TEXT, 
	participant TEXT, 
	study_event TEXT, 
	life_event_type "LifeEventProcessOntology", 
	geolocation "GeolocationOntology", 
	t0_event TEXT, 
	start INTEGER, 
	duration INTEGER, 
	time_unit TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(participant) REFERENCES "Participant" (akc_id), 
	FOREIGN KEY(study_event) REFERENCES "StudyEvent" (akc_id), 
	FOREIGN KEY(t0_event) REFERENCES "LifeEvent" (akc_id)
);COMMENT ON TABLE "ImmuneExposure" IS 'An event involving the immune system of a study participant.';COMMENT ON COLUMN "ImmuneExposure".exposure_material IS 'The material relevant to an immune exposure';COMMENT ON COLUMN "ImmuneExposure".disease IS 'The disease relevant to an immune exposure';COMMENT ON COLUMN "ImmuneExposure".disease_stage IS 'Stage of disease at current intervention';COMMENT ON COLUMN "ImmuneExposure".disease_severity IS 'The severity of the disease relevant to an immune exposure';COMMENT ON COLUMN "ImmuneExposure".participant IS 'The participant of a life event';COMMENT ON COLUMN "ImmuneExposure".study_event IS 'The study event corresponding to a life event';COMMENT ON COLUMN "ImmuneExposure".life_event_type IS 'The specific type of a life event';COMMENT ON COLUMN "ImmuneExposure".geolocation IS 'The geolocation of a participant at birth';COMMENT ON COLUMN "ImmuneExposure".t0_event IS 'The T0 event used to specify the time of this life event';COMMENT ON COLUMN "ImmuneExposure".start IS 'The start time of this life event, relative to the T0 event';COMMENT ON COLUMN "ImmuneExposure".duration IS 'The duration of this life event';COMMENT ON COLUMN "ImmuneExposure".time_unit IS 'The time unit used to measure the start and duration of this life event';COMMENT ON COLUMN "ImmuneExposure".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "ImmuneExposure".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "ImmuneExposure".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "Assessment" (
	life_event TEXT, 
	assessment_type TEXT, 
	target_entity_type TEXT, 
	measurement_value INTEGER, 
	measurement_unit "MeasurementUnitOntology", 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(life_event) REFERENCES "LifeEvent" (akc_id)
);COMMENT ON TABLE "Assessment" IS 'None';COMMENT ON COLUMN "Assessment".life_event IS 'The life event corresponding to an immune exposure';COMMENT ON COLUMN "Assessment".assessment_type IS 'The specific type of an assessment';COMMENT ON COLUMN "Assessment".target_entity_type IS 'The type of the entity being measured';COMMENT ON COLUMN "Assessment".measurement_value IS 'The measurement result value';COMMENT ON COLUMN "Assessment".measurement_unit IS 'The measurement result value unit';COMMENT ON COLUMN "Assessment".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "Assessment".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "Assessment".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "Specimen" (
	life_event TEXT, 
	tissue "TissueOntology", 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(life_event) REFERENCES "LifeEvent" (akc_id)
);COMMENT ON TABLE "Specimen" IS 'None';COMMENT ON COLUMN "Specimen".life_event IS 'The life event corresponding to an immune exposure';COMMENT ON COLUMN "Specimen".tissue IS 'The actual tissue sampled, e.g. lymph node, liver, peripheral blood';COMMENT ON COLUMN "Specimen".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "Specimen".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "Specimen".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "SpecimenCollection" (
	specimen TEXT, 
	type TEXT, 
	participant TEXT, 
	study_event TEXT, 
	life_event_type "LifeEventProcessOntology", 
	geolocation "GeolocationOntology", 
	t0_event TEXT, 
	start INTEGER, 
	duration INTEGER, 
	time_unit TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(specimen) REFERENCES "Specimen" (akc_id), 
	FOREIGN KEY(participant) REFERENCES "Participant" (akc_id), 
	FOREIGN KEY(study_event) REFERENCES "StudyEvent" (akc_id), 
	FOREIGN KEY(t0_event) REFERENCES "LifeEvent" (akc_id)
);COMMENT ON TABLE "SpecimenCollection" IS 'None';COMMENT ON COLUMN "SpecimenCollection".specimen IS 'The specimen that was input for an assay';COMMENT ON COLUMN "SpecimenCollection".participant IS 'The participant of a life event';COMMENT ON COLUMN "SpecimenCollection".study_event IS 'The study event corresponding to a life event';COMMENT ON COLUMN "SpecimenCollection".life_event_type IS 'The specific type of a life event';COMMENT ON COLUMN "SpecimenCollection".geolocation IS 'The geolocation of a participant at birth';COMMENT ON COLUMN "SpecimenCollection".t0_event IS 'The T0 event used to specify the time of this life event';COMMENT ON COLUMN "SpecimenCollection".start IS 'The start time of this life event, relative to the T0 event';COMMENT ON COLUMN "SpecimenCollection".duration IS 'The duration of this life event';COMMENT ON COLUMN "SpecimenCollection".time_unit IS 'The time unit used to measure the start and duration of this life event';COMMENT ON COLUMN "SpecimenCollection".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "SpecimenCollection".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "SpecimenCollection".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "SpecimenProcessing" (
	specimen TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(specimen) REFERENCES "Specimen" (akc_id)
);COMMENT ON TABLE "SpecimenProcessing" IS 'None';COMMENT ON COLUMN "SpecimenProcessing".specimen IS 'The specimen that was input for an assay';COMMENT ON COLUMN "SpecimenProcessing".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "SpecimenProcessing".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "SpecimenProcessing".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "CellIsolationProcessing" (
	tissue_processing TEXT, 
	cell_subset "CellSubsetOntology", 
	cell_phenotype TEXT, 
	cell_species "CellSpeciesOntology", 
	single_cell BOOLEAN, 
	cell_number INTEGER, 
	cells_per_reaction INTEGER, 
	cell_storage BOOLEAN, 
	cell_quality TEXT, 
	cell_isolation TEXT, 
	cell_processing_protocol TEXT, 
	specimen TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(specimen) REFERENCES "Specimen" (akc_id)
);COMMENT ON TABLE "CellIsolationProcessing" IS 'None';COMMENT ON COLUMN "CellIsolationProcessing".tissue_processing IS 'Enzymatic digestion and/or physical methods used to isolate cells from sample';COMMENT ON COLUMN "CellIsolationProcessing".cell_subset IS 'Commonly-used designation of isolated cell population';COMMENT ON COLUMN "CellIsolationProcessing".cell_phenotype IS 'List of cellular markers and their expression levels used to isolate the cell population';COMMENT ON COLUMN "CellIsolationProcessing".cell_species IS 'Binomial designation of the species from which the analyzed cells originate. Typically, this value should be identical to `species`, in which case it SHOULD NOT be set explicitly. However, there are valid experimental setups in which the two might differ, e.g., chimeric animal models. If set, this key will overwrite the `species` information for all lower layers of the schema.';COMMENT ON COLUMN "CellIsolationProcessing".single_cell IS 'TRUE if single cells were isolated into separate compartments';COMMENT ON COLUMN "CellIsolationProcessing".cell_number IS 'Total number of cells that went into the experiment';COMMENT ON COLUMN "CellIsolationProcessing".cells_per_reaction IS 'Number of cells for each biological replicate';COMMENT ON COLUMN "CellIsolationProcessing".cell_storage IS 'TRUE if cells were cryo-preserved between isolation and further processing';COMMENT ON COLUMN "CellIsolationProcessing".cell_quality IS 'Relative amount of viable cells after preparation and (if applicable) thawing';COMMENT ON COLUMN "CellIsolationProcessing".cell_isolation IS 'Description of the procedure used for marker-based isolation or enrich cells';COMMENT ON COLUMN "CellIsolationProcessing".cell_processing_protocol IS 'Description of the methods applied to the sample including cell preparation/ isolation/enrichment and nucleic acid extraction. This should closely mirror the Materials and methods section in the manuscript.';COMMENT ON COLUMN "CellIsolationProcessing".specimen IS 'The specimen that was input for an assay';COMMENT ON COLUMN "CellIsolationProcessing".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "CellIsolationProcessing".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "CellIsolationProcessing".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "LibraryPreparationProcessing" (
	template_class "TemplateClassEnum", 
	template_quality TEXT, 
	template_amount FLOAT, 
	template_amount_unit "TemplateAmountUnitOntology", 
	library_generation_method "LibraryGenerationMethodEnum", 
	library_generation_protocol TEXT, 
	library_generation_kit_version TEXT, 
	complete_sequences "CompleteSequencesEnum", 
	physical_linkage "PhysicalLinkageEnum", 
	specimen TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(specimen) REFERENCES "Specimen" (akc_id)
);COMMENT ON TABLE "LibraryPreparationProcessing" IS 'None';COMMENT ON COLUMN "LibraryPreparationProcessing".template_class IS 'The class of nucleic acid that was used as primary starting material for the following procedures';COMMENT ON COLUMN "LibraryPreparationProcessing".template_quality IS 'Description and results of the quality control performed on the template material';COMMENT ON COLUMN "LibraryPreparationProcessing".template_amount IS 'Amount of template that went into the process';COMMENT ON COLUMN "LibraryPreparationProcessing".template_amount_unit IS 'Unit of template amount';COMMENT ON COLUMN "LibraryPreparationProcessing".library_generation_method IS 'Generic type of library generation';COMMENT ON COLUMN "LibraryPreparationProcessing".library_generation_protocol IS 'Description of processes applied to substrate to obtain a library that is ready for sequencing';COMMENT ON COLUMN "LibraryPreparationProcessing".library_generation_kit_version IS 'When using a library generation protocol from a commercial provider, provide the protocol version number';COMMENT ON COLUMN "LibraryPreparationProcessing".complete_sequences IS 'To be considered `complete`, the procedure used for library construction MUST generate sequences that 1) include the first V gene codon that encodes the mature polypeptide chain (i.e. after the leader sequence) and 2) include the last complete codon of the J gene (i.e. 1 bp 5'' of the J->C splice site) and 3) provide sequence information for all positions between 1) and 2). To be considered `complete & untemplated`, the sections of the sequences defined in points 1) to 3) of the previous sentence MUST be untemplated, i.e. MUST NOT overlap with the primers used in library preparation. `mixed` should only be used if the procedure used for library construction will likely produce multiple categories of sequences in the given experiment. It SHOULD NOT be used as a replacement of a NULL value.';COMMENT ON COLUMN "LibraryPreparationProcessing".physical_linkage IS 'In case an experimental setup is used that physically links nucleic acids derived from distinct `Rearrangements` before library preparation, this field describes the mode of that linkage. All `hetero_*` terms indicate that in case of paired-read sequencing, the two reads should be expected to map to distinct IG/TR loci. `*_head-head` refers to techniques that link the 5'' ends of transcripts in a single-cell context. `*_tail-head` refers to techniques that link the 3'' end of one transcript to the 5'' end of another one in a single-cell context. This term does not provide any information whether a continuous reading-frame between the two is generated. `*_prelinked` refers to constructs in which the linkage was already present on the DNA level (e.g. scFv).';COMMENT ON COLUMN "LibraryPreparationProcessing".specimen IS 'The specimen that was input for an assay';COMMENT ON COLUMN "LibraryPreparationProcessing".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "LibraryPreparationProcessing".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "LibraryPreparationProcessing".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "Assay" (
	specimen TEXT, 
	type TEXT, 
	assay_type "AssayTypeOntology", 
	has_specified_output TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(specimen) REFERENCES "Specimen" (akc_id), 
	FOREIGN KEY(has_specified_output) REFERENCES "AKDataItem" (akc_id)
);COMMENT ON TABLE "Assay" IS 'None';COMMENT ON COLUMN "Assay".specimen IS 'The specimen that was input for an assay';COMMENT ON COLUMN "Assay".assay_type IS 'The specific type of an assay';COMMENT ON COLUMN "Assay".has_specified_output IS 'output data item';COMMENT ON COLUMN "Assay".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "Assay".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "Assay".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "AIRRSequencingAssay" (
	repertoire_id TEXT, 
	sequencing_run_id TEXT, 
	total_reads_passing_qc_filter INTEGER, 
	sequencing_platform TEXT, 
	sequencing_facility TEXT, 
	sequencing_run_date TIMESTAMP WITHOUT TIME ZONE, 
	sequencing_kit TEXT, 
	specimen TEXT, 
	type TEXT, 
	assay_type "AssayTypeOntology", 
	has_specified_output TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	sequencing_files_id INTEGER, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(specimen) REFERENCES "Specimen" (akc_id), 
	FOREIGN KEY(has_specified_output) REFERENCES "AKDataItem" (akc_id), 
	FOREIGN KEY(sequencing_files_id) REFERENCES "SequencingData" (id)
);COMMENT ON TABLE "AIRRSequencingAssay" IS 'None';COMMENT ON COLUMN "AIRRSequencingAssay".sequencing_run_id IS 'ID of sequencing run assigned by the sequencing facility';COMMENT ON COLUMN "AIRRSequencingAssay".total_reads_passing_qc_filter IS 'Number of usable reads for analysis';COMMENT ON COLUMN "AIRRSequencingAssay".sequencing_platform IS 'Designation of sequencing instrument used';COMMENT ON COLUMN "AIRRSequencingAssay".sequencing_facility IS 'Name and address of sequencing facility';COMMENT ON COLUMN "AIRRSequencingAssay".sequencing_run_date IS 'Date of sequencing run';COMMENT ON COLUMN "AIRRSequencingAssay".sequencing_kit IS 'Name, manufacturer, order and lot numbers of sequencing kit';COMMENT ON COLUMN "AIRRSequencingAssay".specimen IS 'The specimen that was input for an assay';COMMENT ON COLUMN "AIRRSequencingAssay".assay_type IS 'The specific type of an assay';COMMENT ON COLUMN "AIRRSequencingAssay".has_specified_output IS 'output data item';COMMENT ON COLUMN "AIRRSequencingAssay".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "AIRRSequencingAssay".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "AIRRSequencingAssay".akc_id IS 'A unique identifier for a thing in the AKC.';COMMENT ON COLUMN "AIRRSequencingAssay".sequencing_files_id IS 'Set of sequencing files produced by the sequencing run';
CREATE TABLE "TCellReceptorEpitopeBindingAssay" (
	epitope TEXT, 
	specimen TEXT, 
	type TEXT, 
	assay_type "AssayTypeOntology", 
	has_specified_output TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	measurement_category "CategoricalSpecificityEnum", 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(epitope) REFERENCES "Epitope" (akc_id), 
	FOREIGN KEY(specimen) REFERENCES "Specimen" (akc_id), 
	FOREIGN KEY(has_specified_output) REFERENCES "AKDataItem" (akc_id)
);COMMENT ON TABLE "TCellReceptorEpitopeBindingAssay" IS 'None';COMMENT ON COLUMN "TCellReceptorEpitopeBindingAssay".epitope IS 'The epitope being measured';COMMENT ON COLUMN "TCellReceptorEpitopeBindingAssay".specimen IS 'The specimen that was input for an assay';COMMENT ON COLUMN "TCellReceptorEpitopeBindingAssay".assay_type IS 'The specific type of an assay';COMMENT ON COLUMN "TCellReceptorEpitopeBindingAssay".has_specified_output IS 'output data item';COMMENT ON COLUMN "TCellReceptorEpitopeBindingAssay".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "TCellReceptorEpitopeBindingAssay".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "TCellReceptorEpitopeBindingAssay".akc_id IS 'A unique identifier for a thing in the AKC.';COMMENT ON COLUMN "TCellReceptorEpitopeBindingAssay".measurement_category IS 'The measurement result category';
CREATE TABLE "AntibodyAntigenBindingAssay" (
	specimen TEXT, 
	type TEXT, 
	assay_type "AssayTypeOntology", 
	has_specified_output TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(specimen) REFERENCES "Specimen" (akc_id), 
	FOREIGN KEY(has_specified_output) REFERENCES "AKDataItem" (akc_id)
);COMMENT ON TABLE "AntibodyAntigenBindingAssay" IS 'None';COMMENT ON COLUMN "AntibodyAntigenBindingAssay".specimen IS 'The specimen that was input for an assay';COMMENT ON COLUMN "AntibodyAntigenBindingAssay".assay_type IS 'The specific type of an assay';COMMENT ON COLUMN "AntibodyAntigenBindingAssay".has_specified_output IS 'output data item';COMMENT ON COLUMN "AntibodyAntigenBindingAssay".name IS 'A human-readable name for a thing';COMMENT ON COLUMN "AntibodyAntigenBindingAssay".description IS 'A human-readable description for a thing';COMMENT ON COLUMN "AntibodyAntigenBindingAssay".akc_id IS 'A unique identifier for a thing in the AKC.';
CREATE TABLE "Investigation_assays" (
	"Investigation_akc_id" TEXT, 
	assays_akc_id TEXT, 
	PRIMARY KEY ("Investigation_akc_id", assays_akc_id), 
	FOREIGN KEY("Investigation_akc_id") REFERENCES "Investigation" (akc_id), 
	FOREIGN KEY(assays_akc_id) REFERENCES "Assay" (akc_id)
);COMMENT ON TABLE "Investigation_assays" IS 'None';COMMENT ON COLUMN "Investigation_assays"."Investigation_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Investigation_assays".assays_akc_id IS 'The assays performed by the investigation';
CREATE TABLE "LibraryPreparationProcessing_pcr_target" (
	"LibraryPreparationProcessing_akc_id" TEXT, 
	pcr_target_id INTEGER, 
	PRIMARY KEY ("LibraryPreparationProcessing_akc_id", pcr_target_id), 
	FOREIGN KEY("LibraryPreparationProcessing_akc_id") REFERENCES "LibraryPreparationProcessing" (akc_id), 
	FOREIGN KEY(pcr_target_id) REFERENCES "PCRTarget" (id)
);COMMENT ON TABLE "LibraryPreparationProcessing_pcr_target" IS 'None';COMMENT ON COLUMN "LibraryPreparationProcessing_pcr_target"."LibraryPreparationProcessing_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "LibraryPreparationProcessing_pcr_target".pcr_target_id IS 'If a PCR step was performed that specifically targets the IG/TR loci, the target and primer locations need to be provided here. This field holds an array of PCRTarget objects, so that multiplex PCR setups amplifying multiple loci at the same time can be annotated using one record per locus. PCR setups not targeting any specific locus must not annotate this field but select the appropriate library_generation_method instead.';
CREATE TABLE "Assay_specimen_processing" (
	"Assay_akc_id" TEXT, 
	specimen_processing_akc_id TEXT, 
	PRIMARY KEY ("Assay_akc_id", specimen_processing_akc_id), 
	FOREIGN KEY("Assay_akc_id") REFERENCES "Assay" (akc_id), 
	FOREIGN KEY(specimen_processing_akc_id) REFERENCES "SpecimenProcessing" (akc_id)
);COMMENT ON TABLE "Assay_specimen_processing" IS 'None';COMMENT ON COLUMN "Assay_specimen_processing"."Assay_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Assay_specimen_processing".specimen_processing_akc_id IS 'A series of zero or more specimen processing steps that precede an assay';
CREATE TABLE "AIRRSequencingAssay_tcell_receptors" (
	"AIRRSequencingAssay_akc_id" TEXT, 
	tcell_receptors_akc_id TEXT, 
	PRIMARY KEY ("AIRRSequencingAssay_akc_id", tcell_receptors_akc_id), 
	FOREIGN KEY("AIRRSequencingAssay_akc_id") REFERENCES "AIRRSequencingAssay" (akc_id), 
	FOREIGN KEY(tcell_receptors_akc_id) REFERENCES "TCellReceptor" (akc_id)
);COMMENT ON TABLE "AIRRSequencingAssay_tcell_receptors" IS 'None';COMMENT ON COLUMN "AIRRSequencingAssay_tcell_receptors"."AIRRSequencingAssay_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "AIRRSequencingAssay_tcell_receptors".tcell_receptors_akc_id IS 'The T cell receptors being measured';
CREATE TABLE "AIRRSequencingAssay_tcell_chains" (
	"AIRRSequencingAssay_akc_id" TEXT, 
	tcell_chains_akc_id TEXT, 
	PRIMARY KEY ("AIRRSequencingAssay_akc_id", tcell_chains_akc_id), 
	FOREIGN KEY("AIRRSequencingAssay_akc_id") REFERENCES "AIRRSequencingAssay" (akc_id), 
	FOREIGN KEY(tcell_chains_akc_id) REFERENCES "Chain" (akc_id)
);COMMENT ON TABLE "AIRRSequencingAssay_tcell_chains" IS 'None';COMMENT ON COLUMN "AIRRSequencingAssay_tcell_chains"."AIRRSequencingAssay_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "AIRRSequencingAssay_tcell_chains".tcell_chains_akc_id IS 'The T cell receptor chains being measured';
CREATE TABLE "AIRRSequencingAssay_specimen_processing" (
	"AIRRSequencingAssay_akc_id" TEXT, 
	specimen_processing_akc_id TEXT, 
	PRIMARY KEY ("AIRRSequencingAssay_akc_id", specimen_processing_akc_id), 
	FOREIGN KEY("AIRRSequencingAssay_akc_id") REFERENCES "AIRRSequencingAssay" (akc_id), 
	FOREIGN KEY(specimen_processing_akc_id) REFERENCES "SpecimenProcessing" (akc_id)
);COMMENT ON TABLE "AIRRSequencingAssay_specimen_processing" IS 'None';COMMENT ON COLUMN "AIRRSequencingAssay_specimen_processing"."AIRRSequencingAssay_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "AIRRSequencingAssay_specimen_processing".specimen_processing_akc_id IS 'A series of zero or more specimen processing steps that precede an assay';
CREATE TABLE "TCellReceptorEpitopeBindingAssay_tcell_receptors" (
	"TCellReceptorEpitopeBindingAssay_akc_id" TEXT, 
	tcell_receptors_akc_id TEXT, 
	PRIMARY KEY ("TCellReceptorEpitopeBindingAssay_akc_id", tcell_receptors_akc_id), 
	FOREIGN KEY("TCellReceptorEpitopeBindingAssay_akc_id") REFERENCES "TCellReceptorEpitopeBindingAssay" (akc_id), 
	FOREIGN KEY(tcell_receptors_akc_id) REFERENCES "TCellReceptor" (akc_id)
);COMMENT ON TABLE "TCellReceptorEpitopeBindingAssay_tcell_receptors" IS 'None';COMMENT ON COLUMN "TCellReceptorEpitopeBindingAssay_tcell_receptors"."TCellReceptorEpitopeBindingAssay_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "TCellReceptorEpitopeBindingAssay_tcell_receptors".tcell_receptors_akc_id IS 'The T cell receptors being measured';
CREATE TABLE "TCellReceptorEpitopeBindingAssay_specimen_processing" (
	"TCellReceptorEpitopeBindingAssay_akc_id" TEXT, 
	specimen_processing_akc_id TEXT, 
	PRIMARY KEY ("TCellReceptorEpitopeBindingAssay_akc_id", specimen_processing_akc_id), 
	FOREIGN KEY("TCellReceptorEpitopeBindingAssay_akc_id") REFERENCES "TCellReceptorEpitopeBindingAssay" (akc_id), 
	FOREIGN KEY(specimen_processing_akc_id) REFERENCES "SpecimenProcessing" (akc_id)
);COMMENT ON TABLE "TCellReceptorEpitopeBindingAssay_specimen_processing" IS 'None';COMMENT ON COLUMN "TCellReceptorEpitopeBindingAssay_specimen_processing"."TCellReceptorEpitopeBindingAssay_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "TCellReceptorEpitopeBindingAssay_specimen_processing".specimen_processing_akc_id IS 'A series of zero or more specimen processing steps that precede an assay';
CREATE TABLE "AntibodyAntigenBindingAssay_specimen_processing" (
	"AntibodyAntigenBindingAssay_akc_id" TEXT, 
	specimen_processing_akc_id TEXT, 
	PRIMARY KEY ("AntibodyAntigenBindingAssay_akc_id", specimen_processing_akc_id), 
	FOREIGN KEY("AntibodyAntigenBindingAssay_akc_id") REFERENCES "AntibodyAntigenBindingAssay" (akc_id), 
	FOREIGN KEY(specimen_processing_akc_id) REFERENCES "SpecimenProcessing" (akc_id)
);COMMENT ON TABLE "AntibodyAntigenBindingAssay_specimen_processing" IS 'None';COMMENT ON COLUMN "AntibodyAntigenBindingAssay_specimen_processing"."AntibodyAntigenBindingAssay_akc_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "AntibodyAntigenBindingAssay_specimen_processing".specimen_processing_akc_id IS 'A series of zero or more specimen processing steps that precede an assay';
