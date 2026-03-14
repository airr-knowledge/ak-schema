-- We modify a few tables to roll-up fields
-- until we can use single table inheritance with linkml

-- roll-up fields from AlphaBetaTCR and GammaDeltaTCR
ALTER TABLE "TCellReceptor"
ADD COLUMN tra_chain TEXT REFERENCES "Chain" (akc_id),
ADD COLUMN trb_chain TEXT REFERENCES "Chain" (akc_id),
ADD COLUMN trg_chain TEXT REFERENCES "Chain" (akc_id),
ADD COLUMN trd_chain TEXT REFERENCES "Chain" (akc_id);

-- roll-up fields from PeptidicEpitope
ALTER TABLE "Epitope"
ADD COLUMN sequence_aa TEXT,
ADD COLUMN source_protein TEXT,
ADD COLUMN source_organism TEXT REFERENCES "TaxonomicSpecies" (term_id);

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
CREATE TABLE "Assay_tcr_complexes" (
	assay_akc_id TEXT, 
	tcr_complexes_akc_id TEXT, 
	PRIMARY KEY (assay_akc_id, tcr_complexes_akc_id), 
	FOREIGN KEY(assay_akc_id) REFERENCES "Assay" (akc_id), 
	FOREIGN KEY(tcr_complexes_akc_id) REFERENCES "TCRpMHCComplex" (akc_id)
);

-- tables to support the query API
CREATE TABLE "QueryAssay" (
       akc_id TEXT,
       assay_object JSONB,
       PRIMARY KEY (akc_id)
);

-- some useful indexes
CREATE INDEX "Chain_junction_aa" ON "Chain" ("junction_aa");
CREATE INDEX "Chain_cdr3_aa" ON "Chain" ("cdr3_aa");
CREATE INDEX "Chain_aa_hash" ON "Chain" ("aa_hash");
