-- We modify a few tables to roll-up fields
-- until we can use single table inheritance with linkml

-- roll-up fields from PeptidicEpitope
ALTER TABLE "Epitope"
ADD COLUMN sequence_aa TEXT,
ADD COLUMN modifications TEXT;

-- roll-up fields from ImmuneExposure
ALTER TABLE "LifeEvent"
-- ImmuneExposure
ADD COLUMN exposure_material VARCHAR, 
ADD COLUMN disease TEXT REFERENCES "Diseases" (term_id), 
ADD COLUMN disease_stage TEXT, 
ADD COLUMN disease_severity TEXT;

-- roll-up fields from AIRRSequencingData
ALTER TABLE "SequenceData"
ADD COLUMN sequencing_data_id TEXT, 
ADD COLUMN file_type VARCHAR(5), 
ADD COLUMN filename TEXT, 
ADD COLUMN read_direction VARCHAR(7), 
ADD COLUMN read_length INTEGER, 
ADD COLUMN paired_filename TEXT, 
ADD COLUMN paired_read_direction VARCHAR(7), 
ADD COLUMN paired_read_length INTEGER, 
ADD COLUMN index_filename TEXT, 
ADD COLUMN index_length INTEGER;

-- roll-up fields from subclasses
ALTER TABLE "Assay"
-- AIRRSequencingAssay
ADD COLUMN repertoire_id TEXT, 
ADD COLUMN sequencing_run_id TEXT, 
ADD COLUMN total_reads_passing_qc_filter INTEGER, 
ADD COLUMN sequencing_platform TEXT, 
ADD COLUMN sequencing_facility TEXT, 
ADD COLUMN sequencing_run_date TIMESTAMP WITHOUT TIME ZONE, 
ADD COLUMN sequencing_kit TEXT, 
ADD COLUMN sequence_files TEXT REFERENCES "SequenceData" (akc_id), 
-- TCellReceptorEpitopeBindingAssay
ADD COLUMN mhc_evidence TEXT,
ADD COLUMN measurement_category VARCHAR(21);
-- AntibodyAntigenBindingAssay

-- tables to support the query API
CREATE TABLE "QueryAssay" (
       akc_id TEXT,
       assay_object JSONB,
       PRIMARY KEY (akc_id)
);
CREATE INDEX idx_query_assay_fts ON "QueryAssay" USING GIN (to_tsvector('english', assay_object));
