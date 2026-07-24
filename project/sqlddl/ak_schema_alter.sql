-- We modify a few tables to roll-up fields
-- until we can use single table inheritance with linkml

-- TODO: not sure this is needed anymore
-- roll-up fields from PeptidicEpitope
-- ALTER TABLE "Epitope"
-- ADD COLUMN sequence_aa TEXT,
-- ADD COLUMN source_protein TEXT,
-- ADD COLUMN source_organism TEXT REFERENCES "TaxonomicSpecies" (term_id);

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

-- roll-up fields from AIRRSequencingAssay and TCellReceptorEpitopeBindingAssay
ALTER TABLE "Assay"
-- AIRRSequencingAssay
ADD COLUMN repertoire_id TEXT, 
ADD COLUMN sequencing_run_id TEXT, 
ADD COLUMN total_reads_passing_qc_filter INTEGER, 
ADD COLUMN sequencing_platform TEXT, 
ADD COLUMN sequencing_facility TEXT, 
ADD COLUMN sequencing_run_date TIMESTAMP WITHOUT TIME ZONE, 
ADD COLUMN sequencing_kit TEXT, 
ADD COLUMN sequencing_files TEXT REFERENCES "SequenceData" (akc_id), 
-- TCellReceptorEpitopeBindingAssay
ADD COLUMN epitope TEXT REFERENCES "Epitope" (akc_id), 
ADD COLUMN measurement_category VARCHAR(21);

-- custom mapping table
CREATE TABLE "Assay_receptor_composites" (
	assay_akc_id TEXT, 
	receptor_composites_akc_id TEXT, 
	PRIMARY KEY (assay_akc_id, receptor_composites_akc_id), 
	FOREIGN KEY(assay_akc_id) REFERENCES "Assay" (akc_id), 
	FOREIGN KEY(receptor_composites_akc_id) REFERENCES "ReceptorComposite" (akc_id)
);

-- tables to support the query API
CREATE TABLE "QueryAssay" (
       akc_id TEXT,
       assay_object JSONB,
       PRIMARY KEY (akc_id)
);
CREATE INDEX idx_query_assay_fts ON "QueryAssay" USING GIN (to_tsvector('english', assay_object));

-- some useful indexes
CREATE INDEX chain_hash_infer_vdj_sequence ON "Chain" ("hash_infer_vdj_sequence");
CREATE INDEX chain_hash_infer_vdj_sequence_aa ON "Chain" ("hash_infer_vdj_sequence_aa");
CREATE INDEX chain_junction_aa ON "Chain" ("junction_aa");
CREATE INDEX chain_v_call ON "Chain" ("v_call");
CREATE INDEX chain_v_gene ON "Chain" ("v_gene");
CREATE INDEX chain_v_subgroup ON "Chain" ("v_subgroup");
CREATE INDEX chain_j_call ON "Chain" ("j_call");
CREATE INDEX chain_j_gene ON "Chain" ("j_gene");
CREATE INDEX chain_j_subgroup ON "Chain" ("j_subgroup");
