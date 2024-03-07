

CREATE TABLE "Conclusion" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	investigations TEXT, 
	datasets TEXT, 
	result TEXT, 
	data_location_type TEXT, 
	data_location_value TEXT, 
	organism VARCHAR(20), 
	experiment_type TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Container" (
	investigations TEXT, 
	"references" TEXT, 
	arms TEXT, 
	study_events TEXT, 
	participants TEXT, 
	life_events TEXT, 
	immune_exposures TEXT, 
	assessments TEXT, 
	specimens TEXT, 
	assays TEXT, 
	datasets TEXT, 
	conclusions TEXT, 
	PRIMARY KEY (investigations, "references", arms, study_events, participants, life_events, immune_exposures, assessments, specimens, assays, datasets, conclusions)
);

CREATE TABLE "Dataset" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	assessments TEXT, 
	assays TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Reference" (
	id TEXT NOT NULL, 
	investigations TEXT, 
	title TEXT, 
	journal TEXT, 
	issue TEXT, 
	month TEXT, 
	year INTEGER, 
	pages TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "StudyDesign" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "StudyEvent" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	arms TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Investigation" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	study_design TEXT, 
	participants TEXT, 
	documents TEXT, 
	assays TEXT, 
	conclusions TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(study_design) REFERENCES "StudyDesign" (id)
);

CREATE TABLE "StudyArm" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	inclusion_criteria TEXT, 
	exclusion_criteria TEXT, 
	"StudyDesign_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("StudyDesign_id") REFERENCES "StudyDesign" (id)
);

CREATE TABLE "Reference_sources" (
	backref_id TEXT, 
	sources TEXT, 
	PRIMARY KEY (backref_id, sources), 
	FOREIGN KEY(backref_id) REFERENCES "Reference" (id)
);

CREATE TABLE "Reference_authors" (
	backref_id TEXT, 
	authors TEXT, 
	PRIMARY KEY (backref_id, authors), 
	FOREIGN KEY(backref_id) REFERENCES "Reference" (id)
);

CREATE TABLE "Arm" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	investigation TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(investigation) REFERENCES "Investigation" (id)
);

CREATE TABLE "Participant" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	arm TEXT, 
	species VARCHAR(20), 
	biological_sex VARCHAR(6), 
	race VARCHAR(41), 
	ethnicity VARCHAR(22), 
	geolocation VARCHAR(24), 
	PRIMARY KEY (id), 
	FOREIGN KEY(arm) REFERENCES "Arm" (id)
);

CREATE TABLE "LifeEvent" (
	id TEXT NOT NULL, 
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
	time_unit TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(participant) REFERENCES "Participant" (id), 
	FOREIGN KEY(study_event) REFERENCES "StudyEvent" (id)
);

CREATE TABLE "Assessment" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	life_event TEXT, 
	assessment_type TEXT, 
	target_entity_type TEXT, 
	value TEXT, 
	unit TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(life_event) REFERENCES "LifeEvent" (id)
);

CREATE TABLE "ImmuneExposure" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	life_event TEXT, 
	exposure_material VARCHAR(36), 
	disease VARCHAR(29), 
	disease_stage VARCHAR(22), 
	disease_severity TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(life_event) REFERENCES "LifeEvent" (id)
);

CREATE TABLE "Specimen" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	life_event TEXT, 
	specimen_type TEXT, 
	tissue TEXT, 
	process TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(life_event) REFERENCES "LifeEvent" (id)
);

CREATE TABLE "Assay" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	specimen TEXT, 
	assay_type TEXT, 
	target_entity_type TEXT, 
	value TEXT, 
	unit TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(specimen) REFERENCES "Specimen" (id)
);
