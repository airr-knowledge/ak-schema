

CREATE TABLE "AIRRKnowledgeCommons" (
	investigations TEXT, 
	"references" TEXT, 
	study_arms TEXT, 
	study_events TEXT, 
	participants TEXT, 
	life_events TEXT, 
	immune_exposures TEXT, 
	assessments TEXT, 
	specimens TEXT, 
	specimen_collections TEXT, 
	assays TEXT, 
	datasets TEXT, 
	conclusions TEXT
);

CREATE TABLE "Assay" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	specimen TEXT, 
	assay_type TEXT, 
	target_entity_type TEXT, 
	value TEXT, 
	unit TEXT
);

CREATE TABLE "Assessment" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	life_event TEXT, 
	assessment_type TEXT, 
	target_entity_type TEXT, 
	value TEXT, 
	unit TEXT
);

CREATE TABLE "Cell" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT
);

CREATE TABLE "Conclusion" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	investigations TEXT, 
	datasets TEXT, 
	result TEXT, 
	data_location_type TEXT, 
	data_location_value TEXT, 
	organism VARCHAR(20), 
	experiment_type TEXT
);

CREATE TABLE "Dataset" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	assessments TEXT, 
	assays TEXT
);

CREATE TABLE "ImmuneExposure" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	life_event TEXT, 
	exposure_material VARCHAR(36), 
	disease VARCHAR(29), 
	disease_stage VARCHAR(22), 
	disease_severity TEXT
);

CREATE TABLE "ImmuneSystem" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT
);

CREATE TABLE "Investigation" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	study_type VARCHAR, 
	archival_id TEXT, 
	inclusion_criteria TEXT, 
	exclusion_criteria TEXT, 
	release_date DATETIME, 
	update_date DATETIME, 
	participants TEXT, 
	assays TEXT, 
	simulations TEXT, 
	documents TEXT, 
	conclusions TEXT
);

CREATE TABLE "LifeEvent" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	participant TEXT, 
	study_event TEXT, 
	life_event_type VARCHAR(79), 
	geolocation VARCHAR(24), 
	t0_event TEXT, 
	t0_event_type TEXT, 
	start TEXT, 
	duration TEXT, 
	time_unit TEXT
);

CREATE TABLE "ModelingFramework" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT
);

CREATE TABLE "ModelSpecification" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT
);

CREATE TABLE "Participant" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	study_arm TEXT, 
	species VARCHAR(20), 
	biological_sex VARCHAR(6), 
	phenotypic_sex VARCHAR(13), 
	age TEXT, 
	age_unit TEXT, 
	age_event TEXT, 
	race VARCHAR(41), 
	ethnicity VARCHAR(32), 
	geolocation VARCHAR(24), 
	strain VARCHAR(20)
);

CREATE TABLE "Reference" (
	source_uri TEXT NOT NULL, 
	sources TEXT, 
	investigations TEXT, 
	title TEXT, 
	authors TEXT, 
	journal TEXT, 
	issue TEXT, 
	month TEXT, 
	year INTEGER, 
	pages TEXT
);

CREATE TABLE "Simulation" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT
);

CREATE TABLE "Specimen" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	life_event TEXT, 
	specimen_type TEXT, 
	tissue TEXT, 
	process TEXT
);

CREATE TABLE "SpecimenCollection" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	specimen TEXT
);

CREATE TABLE "StudyArm" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	investigation TEXT, 
	inclusion_criteria TEXT, 
	exclusion_criteria TEXT
);

CREATE TABLE "StudyEvent" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	study_arms TEXT
);

CREATE TABLE "Tissue" (
	akc_id TEXT NOT NULL, 
	name TEXT, 
	description TEXT
);
