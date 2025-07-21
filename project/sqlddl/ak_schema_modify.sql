-- # Class: "AKObject" Description: "Anything uniquely identifiable in the AKC."
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "ForeignObject" Description: "An object held outside of the AK."
--     * Slot: source_uri Description: AKC reference to a foreign thing.
-- # Class: "AIRRStandards" Description: "An object directly converted from the AIRR schema."
--     * Slot: id Description: 
-- # Class: "AIRRStandards_v1p5" Description: "An object directly converted from AIRR schema version 1.5."
--     * Slot: id Description: 
-- # Class: "AIRRStandards_v2p0" Description: "An object directly converted from AIRR schema version 2.0."
--     * Slot: id Description: 
-- # Class: "NamedThing" Description: "Name and description for AKC things."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "Process" Description: "A generic process."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "PlanSpecification" Description: "A plan with specified actions to meet some objectives."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "Investigation" Description: "A scientific investigation."
--     * Slot: investigation_type Description: Type of study design
--     * Slot: archival_id Description: Identifier for external archival resource for the investigation, e.g., BioProject
--     * Slot: inclusion_exclusion_criteria Description: List of criteria for inclusion/exclusion for the study
--     * Slot: release_date Description: Date of this release
--     * Slot: update_date Description: Subsequence updates to the investigation or its data
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "Reference" Description: "A document about an investigation."
--     * Slot: title Description: The title of a reference
--     * Slot: journal Description: The journal in which a reference was published
--     * Slot: issue Description: The issue of the journal in which a reference was published
--     * Slot: month Description: The month of the issue of the journal in which a reference was published
--     * Slot: year Description: The year of the issue of the journal in which a reference was published
--     * Slot: pages Description: The pages of the issue of the journal in which a reference was published
--     * Slot: source_uri Description: AKC reference to a foreign thing.
-- # Class: "StudyArm" Description: "A population of participants of an investigation."
--     * Slot: investigation Description: An investigation in which the study arm participates
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "Participant" Description: "A participant in an investigation."
--     * Slot: study_arm Description: The study arm that a participant is a member of
--     * Slot: species Description: Binomial designation of subject's species
--     * Slot: sex Description: Biological sex of subject
--     * Slot: age Description: The age of a participant relative to age_event
--     * Slot: age_unit Description: Unit of age range
--     * Slot: age_event Description: Event in the study schedule to which `Age` refers. For NCBI BioSample this MUST be `sampling`. For other implementations submitters need to be aware that there is currently no mechanism to encode to potential delta between `Age event` and `Sample collection time`, hence the chosen events should be in temporal proximity.
--     * Slot: race Description: Racial group of subject (as defined by NIH)
--     * Slot: ethnicity Description: Ethnic group of subject (defined as cultural/language-based membership)
--     * Slot: geolocation Description: The geolocation of a participant at birth
--     * Slot: strain Description: The strain of the participant (non-human study participants)
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "StudyEvent" Description: "An event that is part of the study design of an investigation."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "LifeEvent" Description: "An event in which a study participant participates."
--     * Slot: type Description: 
--     * Slot: participant Description: The participant of a life event
--     * Slot: study_event Description: The study event corresponding to a life event
--     * Slot: life_event_type Description: The specific type of a life event
--     * Slot: geolocation Description: The geolocation of a participant at birth
--     * Slot: t0_event Description: The T0 event used to specify the time of this life event
--     * Slot: start Description: The start time of this life event, relative to the T0 event
--     * Slot: duration Description: The duration of this life event
--     * Slot: time_unit Description: The time unit used to measure the start and duration of this life event
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "ImmuneExposure" Description: "An event involving the immune system of a study participant."
--     * Slot: exposure_material Description: The material relevant to an immune exposure
--     * Slot: disease Description: The disease relevant to an immune exposure
--     * Slot: disease_stage Description: Stage of disease at current intervention
--     * Slot: disease_severity Description: The severity of the disease relevant to an immune exposure
--     * Slot: type Description: 
--     * Slot: participant Description: The participant of a life event
--     * Slot: study_event Description: The study event corresponding to a life event
--     * Slot: life_event_type Description: The specific type of a life event
--     * Slot: geolocation Description: The geolocation of a participant at birth
--     * Slot: t0_event Description: The T0 event used to specify the time of this life event
--     * Slot: start Description: The start time of this life event, relative to the T0 event
--     * Slot: duration Description: The duration of this life event
--     * Slot: time_unit Description: The time unit used to measure the start and duration of this life event
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "Assessment" Description: ""
--     * Slot: life_event Description: The life event corresponding to an immune exposure
--     * Slot: assessment_type Description: The specific type of an assessment
--     * Slot: target_entity_type Description: The type of the entity being measured
--     * Slot: measurement_value Description: The measurement result value
--     * Slot: measurement_unit Description: The measurement result value unit
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "Specimen" Description: ""
--     * Slot: life_event Description: The life event corresponding to an immune exposure
--     * Slot: tissue Description: The actual tissue sampled, e.g. lymph node, liver, peripheral blood
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "SpecimenCollection" Description: ""
--     * Slot: specimen Description: The specimen that was input for an assay
--     * Slot: type Description: 
--     * Slot: participant Description: The participant of a life event
--     * Slot: study_event Description: The study event corresponding to a life event
--     * Slot: life_event_type Description: The specific type of a life event
--     * Slot: geolocation Description: The geolocation of a participant at birth
--     * Slot: t0_event Description: The T0 event used to specify the time of this life event
--     * Slot: start Description: The start time of this life event, relative to the T0 event
--     * Slot: duration Description: The duration of this life event
--     * Slot: time_unit Description: The time unit used to measure the start and duration of this life event
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "SpecimenProcessing" Description: ""
--     * Slot: specimen Description: The specimen that was input for an assay
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
--     * Slot: Assay_akc_id Description: Autocreated FK slot
--     * Slot: AIRRSequencingAssay_akc_id Description: Autocreated FK slot
--     * Slot: TCellReceptorEpitopeBindingAssay_akc_id Description: Autocreated FK slot
--     * Slot: AntibodyAntigenBindingAssay_akc_id Description: Autocreated FK slot
-- # Class: "CellIsolationProcessing" Description: ""
--     * Slot: tissue_processing Description: Enzymatic digestion and/or physical methods used to isolate cells from sample
--     * Slot: cell_subset Description: Commonly-used designation of isolated cell population
--     * Slot: cell_phenotype Description: List of cellular markers and their expression levels used to isolate the cell population
--     * Slot: cell_species Description: Binomial designation of the species from which the analyzed cells originate. Typically, this value should be identical to `species`, in which case it SHOULD NOT be set explicitly. However, there are valid experimental setups in which the two might differ, e.g., chimeric animal models. If set, this key will overwrite the `species` information for all lower layers of the schema.
--     * Slot: single_cell Description: TRUE if single cells were isolated into separate compartments
--     * Slot: cell_number Description: Total number of cells that went into the experiment
--     * Slot: cells_per_reaction Description: Number of cells for each biological replicate
--     * Slot: cell_storage Description: TRUE if cells were cryo-preserved between isolation and further processing
--     * Slot: cell_quality Description: Relative amount of viable cells after preparation and (if applicable) thawing
--     * Slot: cell_isolation Description: Description of the procedure used for marker-based isolation or enrich cells
--     * Slot: cell_processing_protocol Description: Description of the methods applied to the sample including cell preparation/ isolation/enrichment and nucleic acid extraction. This should closely mirror the Materials and methods section in the manuscript.
--     * Slot: specimen Description: The specimen that was input for an assay
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "LibraryPreparationProcessing" Description: ""
--     * Slot: template_class Description: The class of nucleic acid that was used as primary starting material for the following procedures
--     * Slot: template_quality Description: Description and results of the quality control performed on the template material
--     * Slot: template_amount Description: Amount of template that went into the process
--     * Slot: template_amount_unit Description: Unit of template amount
--     * Slot: library_generation_method Description: Generic type of library generation
--     * Slot: library_generation_protocol Description: Description of processes applied to substrate to obtain a library that is ready for sequencing
--     * Slot: library_generation_kit_version Description: When using a library generation protocol from a commercial provider, provide the protocol version number
--     * Slot: complete_sequences Description: To be considered `complete`, the procedure used for library construction MUST generate sequences that 1) include the first V gene codon that encodes the mature polypeptide chain (i.e. after the leader sequence) and 2) include the last complete codon of the J gene (i.e. 1 bp 5' of the J->C splice site) and 3) provide sequence information for all positions between 1) and 2). To be considered `complete & untemplated`, the sections of the sequences defined in points 1) to 3) of the previous sentence MUST be untemplated, i.e. MUST NOT overlap with the primers used in library preparation. `mixed` should only be used if the procedure used for library construction will likely produce multiple categories of sequences in the given experiment. It SHOULD NOT be used as a replacement of a NULL value.
--     * Slot: physical_linkage Description: In case an experimental setup is used that physically links nucleic acids derived from distinct `Rearrangements` before library preparation, this field describes the mode of that linkage. All `hetero_*` terms indicate that in case of paired-read sequencing, the two reads should be expected to map to distinct IG/TR loci. `*_head-head` refers to techniques that link the 5' ends of transcripts in a single-cell context. `*_tail-head` refers to techniques that link the 3' end of one transcript to the 5' end of another one in a single-cell context. This term does not provide any information whether a continuous reading-frame between the two is generated. `*_prelinked` refers to constructs in which the linkage was already present on the DNA level (e.g. scFv).
--     * Slot: specimen Description: The specimen that was input for an assay
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "Assay" Description: ""
--     * Slot: specimen Description: The specimen that was input for an assay
--     * Slot: type Description: 
--     * Slot: assay_type Description: The specific type of an assay
--     * Slot: has_specified_output Description: output data item
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "AIRRSequencingAssay" Description: ""
--     * Slot: repertoire_id Description: 
--     * Slot: sequencing_run_id Description: ID of sequencing run assigned by the sequencing facility
--     * Slot: total_reads_passing_qc_filter Description: Number of usable reads for analysis
--     * Slot: sequencing_platform Description: Designation of sequencing instrument used
--     * Slot: sequencing_facility Description: Name and address of sequencing facility
--     * Slot: sequencing_run_date Description: Date of sequencing run
--     * Slot: sequencing_kit Description: Name, manufacturer, order and lot numbers of sequencing kit
--     * Slot: specimen Description: The specimen that was input for an assay
--     * Slot: type Description: 
--     * Slot: assay_type Description: The specific type of an assay
--     * Slot: has_specified_output Description: output data item
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
--     * Slot: sequencing_files_id Description: Set of sequencing files produced by the sequencing run
-- # Class: "TCellReceptorEpitopeBindingAssay" Description: ""
--     * Slot: epitope Description: The epitope being measured
--     * Slot: specimen Description: The specimen that was input for an assay
--     * Slot: type Description: 
--     * Slot: assay_type Description: The specific type of an assay
--     * Slot: has_specified_output Description: output data item
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
--     * Slot: measurement_category Description: The measurement result category
-- # Class: "AntibodyAntigenBindingAssay" Description: ""
--     * Slot: specimen Description: The specimen that was input for an assay
--     * Slot: type Description: 
--     * Slot: assay_type Description: The specific type of an assay
--     * Slot: has_specified_output Description: output data item
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "DataItem" Description: ""
--     * Slot: id Description: 
-- # Class: "MeasurementDatum" Description: ""
--     * Slot: id Description: 
--     * Slot: measurement_value Description: The measurement result value
--     * Slot: measurement_unit Description: The measurement result value unit
-- # Class: "MeasurementCategory" Description: ""
--     * Slot: id Description: 
--     * Slot: measurement_category Description: The measurement result category
-- # Class: "TCellReceptorEpitopeSpecificityMeasurement" Description: ""
--     * Slot: id Description: 
--     * Slot: measurement_category Description: The measurement result category
-- # Class: "DataSet" Description: ""
--     * Slot: id Description: 
-- # Class: "AKDataItem" Description: "data item with an akc_id"
--     * Slot: type Description: 
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "AKDataSet" Description: ""
--     * Slot: type Description: 
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "SequenceData" Description: "sequence data items are given an akc_id"
--     * Slot: type Description: 
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "AIRRSequencingData" Description: ""
--     * Slot: sequencing_data_id Description: Persistent identifier of raw data stored in an archive (e.g. INSDC run ID). Data archive should  be identified in the CURIE prefix.
--     * Slot: file_type Description: File format for the raw reads or sequences
--     * Slot: filename Description: File name for the raw reads or sequences. The first file in paired-read sequencing.
--     * Slot: read_direction Description: Read direction for the raw reads or sequences. The first file in paired-read sequencing.
--     * Slot: read_length Description: Read length in bases for the first file in paired-read sequencing
--     * Slot: paired_filename Description: File name for the second file in paired-read sequencing
--     * Slot: paired_read_direction Description: Read direction for the second file in paired-read sequencing
--     * Slot: paired_read_length Description: Read length in bases for the second file in paired-read sequencing
--     * Slot: index_filename Description: File name for the index file
--     * Slot: index_length Description: Read length in bases for the index file
--     * Slot: type Description: 
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "RNATranscriptomeData" Description: ""
--     * Slot: type Description: 
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "DataTransformation" Description: ""
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "InputOutputDataMap" Description: ""
--     * Slot: id Description: 
--     * Slot: data_transformation Description: a process that transforms input data into output data
--     * Slot: has_specified_input Description: input data item
--     * Slot: has_specified_output Description: output data item
-- # Class: "Conclusion" Description: ""
--     * Slot: result Description: The content of the conclusion
--     * Slot: data_location_type Description: The type of location where data was found, e.g. figure, table
--     * Slot: data_location_value Description: An identifier for the location of the data, e.g. figure 2
--     * Slot: organism Description: The type of organism that the conclusion is about
--     * Slot: experiment_type Description: The type of experiment that supports the conclusion
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "ImmuneSystem" Description: ""
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "Chain" Description: ""
--     * Slot: species Description: Binomial designation of subject's species
--     * Slot: aa_hash Description: 
--     * Slot: junction_aa_vj_allele_hash Description: 
--     * Slot: junction_aa_vj_gene_hash Description: 
--     * Slot: complete_vdj Description: Complete VDJ flag.
--     * Slot: sequence Description: Nucleotide sequence.
--     * Slot: sequence_aa Description: Amino acid translation of the query nucleotide sequence.
--     * Slot: locus Description: 
--     * Slot: v_call Description: 
--     * Slot: d_call Description: 
--     * Slot: j_call Description: 
--     * Slot: c_call Description: Constant region gene with allele. If referring to a known reference sequence in a database the relevant gene/allele nomenclature should be followed (e.g., IGHG1*01 if using IMGT/GENE-DB).
--     * Slot: junction_aa Description: Amino acid translation of the junction.
--     * Slot: cdr1_aa Description: Amino acid translation of the cdr1 field.
--     * Slot: cdr2_aa Description: Amino acid translation of the cdr2 field.
--     * Slot: cdr3_aa Description: Amino acid translation of the cdr3 field.
--     * Slot: cdr1_start Description: 
--     * Slot: cdr1_end Description: 
--     * Slot: cdr2_start Description: 
--     * Slot: cdr2_end Description: 
--     * Slot: cdr3_start Description: 
--     * Slot: cdr3_end Description: CDR3 end position in the query sequence (1-based closed interval).
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "ImmuneReceptor" Description: ""
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "TCellReceptor" Description: ""
--     * Slot: type Description: 
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "AlphaBetaTCR" Description: ""
--     * Slot: tra_chain Description: T cell receptor alpha chain
--     * Slot: trb_chain Description: T cell receptor beta chain
--     * Slot: type Description: 
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "GammaDeltaTCR" Description: ""
--     * Slot: trg_chain Description: T cell receptor gamma chain
--     * Slot: trd_chain Description: T cell receptor delta chain
--     * Slot: type Description: 
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "BCellReceptor" Description: ""
--     * Slot: igh_chain Description: IG heavy chain
--     * Slot: igk_chain Description: IG kappa light chain
--     * Slot: igl_chain Description: IG lambda light chain
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "Antigen" Description: ""
--     * Slot: source_protein Description: The protein that this epitope comes from
--     * Slot: source_organism Description: The organism that the source protein comes from
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "Epitope" Description: ""
--     * Slot: type Description: 
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "PeptidicEpitope" Description: ""
--     * Slot: sequence_aa Description: Amino acid translation of the query nucleotide sequence.
--     * Slot: source_protein Description: The protein that this epitope comes from
--     * Slot: source_organism Description: The organism that the source protein comes from
--     * Slot: type Description: 
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "AntibodyAntigenComplex" Description: ""
--     * Slot: antibody Description: B cell receptor, immunoglobulin antibody
--     * Slot: antigen Description: A material entity with antigen role
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "TCRpMHCComplex" Description: ""
--     * Slot: tcell_receptor Description: T cell receptor
--     * Slot: epitope Description: The epitope being measured
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
--     * Slot: mhc_id Description: Major histocompatibility complex
-- # Class: "Model" Description: ""
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "ConceptualModel" Description: ""
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "CommunicativeModel" Description: ""
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "ModelSpecification" Description: ""
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "ModelingFramework" Description: ""
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "Simulation" Description: ""
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "SimilarityCalculation" Description: ""
--     * Slot: chain_domain Description: Immune receptor chain element in binary relation domain
--     * Slot: chain_codomain Description: Immune receptor chain element in binary relation codomain
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "ChainSimilarity" Description: ""
--     * Slot: chain_similarity_type Description: Type of similarity calculation between two immune receptor chains
--     * Slot: chain_domain Description: Immune receptor chain element in binary relation domain
--     * Slot: chain_codomain Description: Immune receptor chain element in binary relation codomain
--     * Slot: akc_id Description: A unique identifier for a thing in the AKC.
-- # Class: "TimePoint" Description: ""
--     * Slot: id Description: 
--     * Slot: time_point_label Description: Informative label for the time point
--     * Slot: time_point_value Description: Value of the time point
--     * Slot: time_point_unit Description: Unit of the time point
-- # Class: "Acknowledgement" Description: ""
--     * Slot: id Description: 
--     * Slot: acknowledgement_id Description: unique identifier of this Acknowledgement within the file
--     * Slot: individual_full_name Description: Full name of individual
--     * Slot: institution_name Description: Individual's department and institution name
--     * Slot: orcid_id Description: Individual's ORCID identifier
-- # Class: "RearrangedSequence" Description: ""
--     * Slot: id Description: 
--     * Slot: sequence_id Description: 
--     * Slot: sequence Description: Nucleotide sequence.
--     * Slot: derivation Description: The class of nucleic acid that was used as primary starting material
--     * Slot: observation_type Description: The type of observation from which this sequence was drawn, such as direct sequencing or  inference from repertoire sequencing data.
--     * Slot: curation Description: 
--     * Slot: repository_name Description: 
--     * Slot: repository_ref Description: Queryable id or accession number of the sequence published by the repository
--     * Slot: deposited_version Description: Version number of the sequence within the repository
--     * Slot: sequence_start Description: 
--     * Slot: sequence_end Description: 
-- # Class: "UnrearrangedSequence" Description: ""
--     * Slot: id Description: 
--     * Slot: sequence_id Description: 
--     * Slot: sequence Description: Nucleotide sequence.
--     * Slot: curation Description: 
--     * Slot: repository_name Description: 
--     * Slot: repository_ref Description: Queryable id or accession number of the sequence published by the repository
--     * Slot: patch_no Description: Genome assembly patch number in which this gene was determined
--     * Slot: gff_seqid Description: Sequence (from the assembly) of a window including the gene and preferably also the promoter region.
--     * Slot: gff_start Description: Genomic co-ordinates of the start of the sequence of interest described in this record in  Ensemble GFF version 3.
--     * Slot: gff_end Description: Genomic co-ordinates of the end of the sequence of interest described in this record in  Ensemble GFF version 3.
--     * Slot: strand Description: sense (+ or -)
-- # Class: "SequenceDelineationV" Description: ""
--     * Slot: id Description: 
--     * Slot: sequence_delineation_id Description: Unique identifier of this SequenceDelineationV within the file. Typically, generated by the  repository hosting the record.
--     * Slot: delineation_scheme Description: Name of the delineation scheme
--     * Slot: unaligned_sequence Description: entire V-sequence covered by this delineation
--     * Slot: aligned_sequence Description: Aligned sequence if this delineation provides an alignment. An aligned sequence should always be  provided for IMGT delineations.
--     * Slot: fwr1_start Description: 
--     * Slot: fwr1_end Description: 
--     * Slot: cdr1_start Description: 
--     * Slot: cdr1_end Description: 
--     * Slot: fwr2_start Description: 
--     * Slot: fwr2_end Description: 
--     * Slot: cdr2_start Description: 
--     * Slot: cdr2_end Description: 
--     * Slot: fwr3_start Description: 
--     * Slot: fwr3_end Description: 
--     * Slot: cdr3_start Description: 
-- # Class: "AlleleDescription" Description: ""
--     * Slot: id Description: 
--     * Slot: allele_description_id Description: Unique identifier of this AlleleDescription within the file. Typically, generated by the  repository hosting the record.
--     * Slot: allele_description_ref Description: Unique reference to the allele description, in standardized form (Repo:Label:Version)
--     * Slot: maintainer Description: Maintainer of this sequence record
--     * Slot: lab_address Description: 
--     * Slot: release_version Description: 
--     * Slot: release_date Description: Date of this release
--     * Slot: release_description Description: Brief descriptive notes of the reason for this release and the changes embodied
--     * Slot: label Description: 
--     * Slot: sequence Description: Nucleotide sequence.
--     * Slot: coding_sequence Description: Nucleotide sequence of the core coding region, such as the coding region of a D-, J- or C- gene  or the coding region of a V-gene excluding the leader.
--     * Slot: locus Description: 
--     * Slot: chromosome Description: chromosome on which the gene is located
--     * Slot: sequence_type Description: Sequence type (V, D, J, C)
--     * Slot: functional Description: True if the gene is functional, false if it is a pseudogene
--     * Slot: inference_type Description: Type of inference(s) from which this gene sequence was inferred
--     * Slot: species Description: Binomial designation of subject's species
--     * Slot: species_subgroup Description: Race, strain or other species subgroup to which this subject belongs
--     * Slot: species_subgroup_type Description: 
--     * Slot: status Description: Status of record, assumed active if the field is not present
--     * Slot: subgroup_designation Description: Identifier of the gene subgroup or clade, as (and if) defined
--     * Slot: gene_designation Description: Gene number or other identifier, as (and if) defined
--     * Slot: allele_designation Description: 
--     * Slot: allele_similarity_cluster_designation Description: ID of the similarity cluster used in this germline set, if designated
--     * Slot: allele_similarity_cluster_member_id Description: Membership ID of the allele within the similarity cluster, if a cluster is designated
--     * Slot: j_codon_frame Description: Codon position of the first nucleotide in the 'coding_sequence' field. Mandatory for J genes.  Not used for V or D genes. '1' means the sequence is in-frame, '2' means that the first bp is  missing from the first codon, and '3' means that the first 2 bp are missing.
--     * Slot: gene_start Description: Co-ordinate in the sequence field of the first nucleotide in the coding_sequence field.
--     * Slot: gene_end Description: Co-ordinate in the sequence field of the last gene-coding nucleotide in the coding_sequence field.
--     * Slot: utr_5_prime_start Description: Start co-ordinate in the sequence field of the 5 prime UTR (V-genes only).
--     * Slot: utr_5_prime_end Description: End co-ordinate in the sequence field of the 5 prime UTR (V-genes only).
--     * Slot: leader_1_start Description: Start co-ordinate in the sequence field of L-PART1 (V-genes only).
--     * Slot: leader_1_end Description: End co-ordinate in the sequence field of L-PART1 (V-genes only).
--     * Slot: leader_2_start Description: Start co-ordinate in the sequence field of L-PART2 (V-genes only).
--     * Slot: leader_2_end Description: End co-ordinate in the sequence field of L-PART2 (V-genes only).
--     * Slot: v_rs_start Description: Start co-ordinate in the sequence field of the V recombination site (V-genes only).
--     * Slot: v_rs_end Description: End co-ordinate in the sequence field of the V recombination site (V-genes only).
--     * Slot: d_rs_3_prime_start Description: Start co-ordinate in the sequence field of the 3 prime D recombination site (D-genes only).
--     * Slot: d_rs_3_prime_end Description: End co-ordinate in the sequence field of the 3 prime D recombination site (D-genes only).
--     * Slot: d_rs_5_prime_start Description: Start co-ordinate in the sequence field of the 5 prime D recombination site (D-genes only).
--     * Slot: d_rs_5_prime_end Description: End co-ordinate in the sequence field of 5 the prime D recombination site (D-genes only).
--     * Slot: j_cdr3_end Description: In the case of a J-gene, the co-ordinate in the sequence field of the first nucelotide of the  conserved PHE or TRP (IMGT codon position 118).
--     * Slot: j_rs_start Description: Start co-ordinate in the sequence field of J recombination site (J-genes only).
--     * Slot: j_rs_end Description: End co-ordinate in the sequence field of J recombination site (J-genes only).
--     * Slot: j_donor_splice Description: Co-ordinate in the sequence field of the final 3' nucleotide of the J-REGION (J-genes only).
--     * Slot: curation Description: 
-- # Class: "GermlineSet" Description: ""
--     * Slot: id Description: 
--     * Slot: germline_set_id Description: Unique identifier of the GermlineSet within this file. Typically, generated by the  repository hosting the record.
--     * Slot: author Description: Corresponding author
--     * Slot: lab_name Description: 
--     * Slot: lab_address Description: 
--     * Slot: release_version Description: 
--     * Slot: release_description Description: Brief descriptive notes of the reason for this release and the changes embodied
--     * Slot: release_date Description: Date of this release
--     * Slot: germline_set_name Description: descriptive name of this germline set
--     * Slot: germline_set_ref Description: 
--     * Slot: pub_ids Description: 
--     * Slot: species Description: Binomial designation of subject's species
--     * Slot: species_subgroup Description: Race, strain or other species subgroup to which this subject belongs
--     * Slot: species_subgroup_type Description: 
--     * Slot: locus Description: 
--     * Slot: curation Description: 
-- # Class: "GenotypeSet" Description: ""
--     * Slot: id Description: 
--     * Slot: receptor_genotype_set_id Description: A unique identifier for this Receptor Genotype Set, typically generated by the repository  hosting the schema, for example from the underlying ID of the database record.
-- # Class: "Genotype" Description: ""
--     * Slot: id Description: 
--     * Slot: receptor_genotype_id Description: A unique identifier within the file for this Receptor Genotype, typically generated by the  repository hosting the schema, for example from the underlying ID of the database record.
--     * Slot: locus Description: 
--     * Slot: inference_process Description: Information on how the genotype was acquired. Controlled vocabulary.
-- # Class: "DocumentedAllele" Description: ""
--     * Slot: id Description: 
--     * Slot: label Description: 
--     * Slot: germline_set_ref Description: 
--     * Slot: phasing Description: Chromosomal phasing indicator. Alleles with the same value are inferred to be located on the  same chromosome.
-- # Class: "UndocumentedAllele" Description: ""
--     * Slot: id Description: 
--     * Slot: allele_name Description: Allele name as allocated by the inference pipeline
--     * Slot: sequence Description: Nucleotide sequence.
--     * Slot: phasing Description: Chromosomal phasing indicator. Alleles with the same value are inferred to be located on the  same chromosome.
-- # Class: "DeletedGene" Description: ""
--     * Slot: id Description: 
--     * Slot: label Description: 
--     * Slot: germline_set_ref Description: 
--     * Slot: phasing Description: Chromosomal phasing indicator. Alleles with the same value are inferred to be located on the  same chromosome.
-- # Class: "MHCGenotypeSet" Description: ""
--     * Slot: id Description: 
--     * Slot: mhc_genotype_set_id Description: A unique identifier for this MHCGenotypeSet
-- # Class: "MHCGenotype" Description: ""
--     * Slot: id Description: 
--     * Slot: mhc_genotype_id Description: A unique identifier for this MHCGenotype, assumed to be unique in the context of the study
--     * Slot: mhc_class Description: 
--     * Slot: mhc_genotyping_method Description: Information on how the genotype was determined. The content of this field should come from a list of recommended terms provided in the AIRR Schema documentation.
-- # Class: "MHCAllele" Description: ""
--     * Slot: id Description: 
--     * Slot: allele_designation Description: 
--     * Slot: gene Description: The MHC gene to which the described allele belongs
--     * Slot: reference_set_ref Description: Repository and list from which it was taken (issuer/name/version)
-- # Class: "SubjectGenotype" Description: ""
--     * Slot: id Description: 
--     * Slot: receptor_genotype_set_id Description: Immune receptor genotype set for this subject.
--     * Slot: mhc_genotype_set_id Description: MHC genotype set for this subject.
-- # Class: "Study" Description: ""
--     * Slot: id Description: 
--     * Slot: study_id Description: Unique ID assigned by study registry such as one of the International Nucleotide Sequence Database Collaboration (INSDC) repositories.
--     * Slot: study_title Description: Descriptive study title
--     * Slot: study_type Description: Type of study design
--     * Slot: study_description Description: Generic study description
--     * Slot: inclusion_exclusion_criteria Description: List of criteria for inclusion/exclusion for the study
--     * Slot: grants Description: Funding agencies and grant numbers
--     * Slot: study_contact Description: Full contact information of the contact persons for this study This should include an e-mail address and a persistent identifier such as an ORCID ID.
--     * Slot: collected_by Description: Full contact information of the data collector, i.e. the person who is legally responsible for data collection and release. This should include an e-mail address and a persistent identifier such as an ORCID ID.
--     * Slot: lab_name Description: 
--     * Slot: lab_address Description: 
--     * Slot: submitted_by Description: Full contact information of the data depositor, i.e., the person submitting the data to a repository. This should include an e-mail address and a persistent identifier such as an ORCID ID. This is supposed to be a short-lived and technical role until the submission is relased.
--     * Slot: pub_ids Description: 
--     * Slot: adc_publish_date Description: Date the study was first published in the AIRR Data Commons.
--     * Slot: adc_update_date Description: Date the study data was updated in the AIRR Data Commons.
-- # Class: "Subject" Description: ""
--     * Slot: id Description: 
--     * Slot: subject_id Description: Subject ID assigned by submitter, unique within study. If possible, a persistent subject ID linked to an INSDC or similar repository study should be used.
--     * Slot: synthetic Description: TRUE for libraries in which the diversity has been synthetically generated (e.g. phage display)
--     * Slot: species Description: Binomial designation of subject's species
--     * Slot: sex Description: Biological sex of subject
--     * Slot: age_min Description: Specific age or lower boundary of age range.
--     * Slot: age_max Description: Upper boundary of age range or equal to age_min for specific age. This field should only be null if age_min is null.
--     * Slot: age_unit Description: Unit of age range
--     * Slot: age_event Description: Event in the study schedule to which `Age` refers. For NCBI BioSample this MUST be `sampling`. For other implementations submitters need to be aware that there is currently no mechanism to encode to potential delta between `Age event` and `Sample collection time`, hence the chosen events should be in temporal proximity.
--     * Slot: ancestry_population Description: Broad geographic origin of ancestry (continent)
--     * Slot: ethnicity Description: Ethnic group of subject (defined as cultural/language-based membership)
--     * Slot: race Description: Racial group of subject (as defined by NIH)
--     * Slot: strain_name Description: Non-human designation of the strain or breed of animal used
--     * Slot: linked_subjects Description: Subject ID to which `Relation type` refers
--     * Slot: link_type Description: Relation between subject and `linked_subjects`, can be genetic or environmental (e.g.exposure)
--     * Slot: genotype_id Description: 
-- # Class: "Diagnosis" Description: ""
--     * Slot: id Description: 
--     * Slot: study_group_description Description: Designation of study arm to which the subject is assigned to
--     * Slot: disease_diagnosis Description: Diagnosis of subject
--     * Slot: disease_length Description: Time duration between initial diagnosis and current intervention
--     * Slot: disease_stage Description: Stage of disease at current intervention
--     * Slot: prior_therapies Description: List of all relevant previous therapies applied to subject for treatment of `Diagnosis`
--     * Slot: immunogen Description: Antigen, vaccine or drug applied to subject at this intervention
--     * Slot: intervention Description: Description of intervention
--     * Slot: medical_history Description: Medical history of subject that is relevant to assess the course of disease and/or treatment
-- # Class: "Sample" Description: ""
--     * Slot: id Description: 
--     * Slot: sample_id Description: Sample ID assigned by submitter, unique within study. If possible, a persistent sample ID linked to INSDC or similar repository study should be used.
--     * Slot: sample_type Description: The way the sample was obtained, e.g. fine-needle aspirate, organ harvest, peripheral venous puncture
--     * Slot: tissue Description: The actual tissue sampled, e.g. lymph node, liver, peripheral blood
--     * Slot: anatomic_site Description: The anatomic location of the tissue, e.g. Inguinal, femur
--     * Slot: disease_state_sample Description: Histopathologic evaluation of the sample
--     * Slot: collection_time_point_relative Description: Time point at which sample was taken, relative to `Collection time event`
--     * Slot: collection_time_point_relative_unit Description: Unit of Sample collection time
--     * Slot: collection_time_point_reference Description: Event in the study schedule to which `Sample collection time` relates to
--     * Slot: biomaterial_provider Description: Name and address of the entity providing the sample
-- # Class: "CellProcessing" Description: ""
--     * Slot: id Description: 
--     * Slot: tissue_processing Description: Enzymatic digestion and/or physical methods used to isolate cells from sample
--     * Slot: cell_subset Description: Commonly-used designation of isolated cell population
--     * Slot: cell_phenotype Description: List of cellular markers and their expression levels used to isolate the cell population
--     * Slot: cell_species Description: Binomial designation of the species from which the analyzed cells originate. Typically, this value should be identical to `species`, in which case it SHOULD NOT be set explicitly. However, there are valid experimental setups in which the two might differ, e.g., chimeric animal models. If set, this key will overwrite the `species` information for all lower layers of the schema.
--     * Slot: single_cell Description: TRUE if single cells were isolated into separate compartments
--     * Slot: cell_number Description: Total number of cells that went into the experiment
--     * Slot: cells_per_reaction Description: Number of cells for each biological replicate
--     * Slot: cell_storage Description: TRUE if cells were cryo-preserved between isolation and further processing
--     * Slot: cell_quality Description: Relative amount of viable cells after preparation and (if applicable) thawing
--     * Slot: cell_isolation Description: Description of the procedure used for marker-based isolation or enrich cells
--     * Slot: cell_processing_protocol Description: Description of the methods applied to the sample including cell preparation/ isolation/enrichment and nucleic acid extraction. This should closely mirror the Materials and methods section in the manuscript.
-- # Class: "PCRTarget" Description: ""
--     * Slot: id Description: 
--     * Slot: pcr_target_locus Description: Designation of the target locus. Note that this field uses a controlled vocubulary that is meant to provide a generic classification of the locus, not necessarily the correct designation according to a specific nomenclature.
--     * Slot: forward_pcr_primer_target_location Description: Position of the most distal nucleotide templated by the forward primer or primer mix
--     * Slot: reverse_pcr_primer_target_location Description: Position of the most proximal nucleotide templated by the reverse primer or primer mix
-- # Class: "NucleicAcidProcessing" Description: ""
--     * Slot: id Description: 
--     * Slot: template_class Description: The class of nucleic acid that was used as primary starting material for the following procedures
--     * Slot: template_quality Description: Description and results of the quality control performed on the template material
--     * Slot: template_amount Description: Amount of template that went into the process
--     * Slot: template_amount_unit Description: Unit of template amount
--     * Slot: library_generation_method Description: Generic type of library generation
--     * Slot: library_generation_protocol Description: Description of processes applied to substrate to obtain a library that is ready for sequencing
--     * Slot: library_generation_kit_version Description: When using a library generation protocol from a commercial provider, provide the protocol version number
--     * Slot: complete_sequences Description: To be considered `complete`, the procedure used for library construction MUST generate sequences that 1) include the first V gene codon that encodes the mature polypeptide chain (i.e. after the leader sequence) and 2) include the last complete codon of the J gene (i.e. 1 bp 5' of the J->C splice site) and 3) provide sequence information for all positions between 1) and 2). To be considered `complete & untemplated`, the sections of the sequences defined in points 1) to 3) of the previous sentence MUST be untemplated, i.e. MUST NOT overlap with the primers used in library preparation. `mixed` should only be used if the procedure used for library construction will likely produce multiple categories of sequences in the given experiment. It SHOULD NOT be used as a replacement of a NULL value.
--     * Slot: physical_linkage Description: In case an experimental setup is used that physically links nucleic acids derived from distinct `Rearrangements` before library preparation, this field describes the mode of that linkage. All `hetero_*` terms indicate that in case of paired-read sequencing, the two reads should be expected to map to distinct IG/TR loci. `*_head-head` refers to techniques that link the 5' ends of transcripts in a single-cell context. `*_tail-head` refers to techniques that link the 3' end of one transcript to the 5' end of another one in a single-cell context. This term does not provide any information whether a continuous reading-frame between the two is generated. `*_prelinked` refers to constructs in which the linkage was already present on the DNA level (e.g. scFv).
-- # Class: "SequencingRun" Description: ""
--     * Slot: id Description: 
--     * Slot: sequencing_run_id Description: ID of sequencing run assigned by the sequencing facility
--     * Slot: total_reads_passing_qc_filter Description: Number of usable reads for analysis
--     * Slot: sequencing_platform Description: Designation of sequencing instrument used
--     * Slot: sequencing_facility Description: Name and address of sequencing facility
--     * Slot: sequencing_run_date Description: Date of sequencing run
--     * Slot: sequencing_kit Description: Name, manufacturer, order and lot numbers of sequencing kit
--     * Slot: sequencing_files_id Description: Set of sequencing files produced by the sequencing run
-- # Class: "SequencingData" Description: ""
--     * Slot: id Description: 
--     * Slot: sequencing_data_id Description: Persistent identifier of raw data stored in an archive (e.g. INSDC run ID). Data archive should  be identified in the CURIE prefix.
--     * Slot: file_type Description: File format for the raw reads or sequences
--     * Slot: filename Description: File name for the raw reads or sequences. The first file in paired-read sequencing.
--     * Slot: read_direction Description: Read direction for the raw reads or sequences. The first file in paired-read sequencing.
--     * Slot: read_length Description: Read length in bases for the first file in paired-read sequencing
--     * Slot: paired_filename Description: File name for the second file in paired-read sequencing
--     * Slot: paired_read_direction Description: Read direction for the second file in paired-read sequencing
--     * Slot: paired_read_length Description: Read length in bases for the second file in paired-read sequencing
--     * Slot: index_filename Description: File name for the index file
--     * Slot: index_length Description: Read length in bases for the index file
-- # Class: "DataProcessing" Description: ""
--     * Slot: id Description: 
--     * Slot: data_processing_id Description: 
--     * Slot: primary_annotation Description: If true, indicates this is the primary or default data processing for the repertoire and its rearrangements. If false, indicates this is a secondary or additional data processing.
--     * Slot: software_versions Description: Version number and / or date, include company pipelines
--     * Slot: paired_reads_assembly Description: How paired end reads were assembled into a single receptor sequence
--     * Slot: quality_thresholds Description: How/if sequences were removed from (4) based on base quality scores
--     * Slot: primer_match_cutoffs Description: How primers were identified in the sequences, were they removed/masked/etc?
--     * Slot: collapsing_method Description: The method used for combining multiple sequences from (4) into a single sequence in (5)
--     * Slot: data_processing_protocols Description: General description of how QC is performed
--     * Slot: germline_database Description: Source of germline V(D)J genes with version number or date accessed.
--     * Slot: germline_set_ref Description: 
--     * Slot: analysis_provenance_id Description: Identifier for machine-readable PROV model of analysis provenance
-- # Class: "Repertoire" Description: ""
--     * Slot: id Description: 
--     * Slot: repertoire_id Description: 
--     * Slot: repertoire_name Description: Short generic display name for the repertoire
--     * Slot: repertoire_description Description: 
--     * Slot: study_id Description: Study object
--     * Slot: subject_id Description: Subject object
-- # Class: "RepertoireGroupDetail" Description: ""
--     * Slot: id Description: 
--     * Slot: repertoire_id Description: 
--     * Slot: repertoire_description Description: 
--     * Slot: time_point_id Description: Time point designation for this repertoire within the group
-- # Class: "RepertoireGroup" Description: ""
--     * Slot: id Description: 
--     * Slot: repertoire_group_id Description: Identifier for this repertoire collection
--     * Slot: repertoire_group_name Description: Short display name for this repertoire collection
--     * Slot: repertoire_group_description Description: Repertoire collection description
-- # Class: "Alignment" Description: ""
--     * Slot: id Description: 
--     * Slot: sequence_id Description: 
--     * Slot: segment Description: The segment for this alignment. One of V, D, J or C.
--     * Slot: rev_comp Description: 
--     * Slot: call Description: Gene assignment with allele.
--     * Slot: score Description: Alignment score.
--     * Slot: identity Description: Alignment fractional identity.
--     * Slot: support Description: Alignment E-value, p-value, likelihood, probability or other similar measure of support for the gene assignment as defined by the alignment tool.
--     * Slot: cigar Description: Alignment CIGAR string.
--     * Slot: sequence_start Description: 
--     * Slot: sequence_end Description: 
--     * Slot: germline_start Description: Alignment start position in the reference sequence (1-based closed interval).
--     * Slot: germline_end Description: Alignment end position in the reference sequence (1-based closed interval).
--     * Slot: rank Description: Alignment rank.
--     * Slot: data_processing_id Description: 
-- # Class: "Rearrangement" Description: ""
--     * Slot: id Description: 
--     * Slot: sequence_id Description: 
--     * Slot: sequence Description: Nucleotide sequence.
--     * Slot: quality Description: The Sanger/Phred quality scores for assessment of sequence quality. Phred quality scores from 0 to 93 are encoded using ASCII 33 to 126 (Used by Illumina from v1.8.)
--     * Slot: sequence_aa Description: Amino acid translation of the query nucleotide sequence.
--     * Slot: rev_comp Description: 
--     * Slot: productive Description: True if the V(D)J sequence is predicted to be productive.
--     * Slot: vj_in_frame Description: True if the V and J gene alignments are in-frame.
--     * Slot: stop_codon Description: True if the aligned sequence contains a stop codon.
--     * Slot: complete_vdj Description: Complete VDJ flag.
--     * Slot: locus Description: 
--     * Slot: v_call Description: 
--     * Slot: d_call Description: 
--     * Slot: d2_call Description: Second D gene with allele. If referring to a known reference sequence in a database the relevant gene/allele nomenclature should be followed (e.g., IGHD3-10*01 if using IMGT/GENE-DB).
--     * Slot: j_call Description: 
--     * Slot: c_call Description: Constant region gene with allele. If referring to a known reference sequence in a database the relevant gene/allele nomenclature should be followed (e.g., IGHG1*01 if using IMGT/GENE-DB).
--     * Slot: sequence_alignment Description: 
--     * Slot: quality_alignment Description: Sanger/Phred quality scores for assessment of sequence_alignment quality. Phred quality scores from 0 to 93 are encoded using ASCII 33 to 126 (Used by Illumina from v1.8.)
--     * Slot: sequence_alignment_aa Description: Amino acid translation of the aligned query sequence.
--     * Slot: germline_alignment Description: 
--     * Slot: germline_alignment_aa Description: 
--     * Slot: junction Description: 
--     * Slot: junction_aa Description: Amino acid translation of the junction.
--     * Slot: np1 Description: Nucleotide sequence of the combined N/P region between the V gene and first D gene alignment or between the V gene and J gene alignments.
--     * Slot: np1_aa Description: Amino acid translation of the np1 field.
--     * Slot: np2 Description: Nucleotide sequence of the combined N/P region between either the first D gene and J gene alignments or the first D gene and second D gene alignments.
--     * Slot: np2_aa Description: Amino acid translation of the np2 field.
--     * Slot: np3 Description: Nucleotide sequence of the combined N/P region between the second D gene and J gene alignments.
--     * Slot: np3_aa Description: Amino acid translation of the np3 field.
--     * Slot: cdr1 Description: Nucleotide sequence of the aligned CDR1 region.
--     * Slot: cdr1_aa Description: Amino acid translation of the cdr1 field.
--     * Slot: cdr2 Description: Nucleotide sequence of the aligned CDR2 region.
--     * Slot: cdr2_aa Description: Amino acid translation of the cdr2 field.
--     * Slot: cdr3 Description: Nucleotide sequence of the aligned CDR3 region.
--     * Slot: cdr3_aa Description: Amino acid translation of the cdr3 field.
--     * Slot: fwr1 Description: Nucleotide sequence of the aligned FWR1 region.
--     * Slot: fwr1_aa Description: Amino acid translation of the fwr1 field.
--     * Slot: fwr2 Description: Nucleotide sequence of the aligned FWR2 region.
--     * Slot: fwr2_aa Description: Amino acid translation of the fwr2 field.
--     * Slot: fwr3 Description: Nucleotide sequence of the aligned FWR3 region.
--     * Slot: fwr3_aa Description: Amino acid translation of the fwr3 field.
--     * Slot: fwr4 Description: Nucleotide sequence of the aligned FWR4 region.
--     * Slot: fwr4_aa Description: Amino acid translation of the fwr4 field.
--     * Slot: v_score Description: Alignment score for the V gene.
--     * Slot: v_identity Description: Fractional identity for the V gene alignment.
--     * Slot: v_support Description: V gene alignment E-value, p-value, likelihood, probability or other similar measure of support for the V gene assignment as defined by the alignment tool.
--     * Slot: v_cigar Description: CIGAR string for the V gene alignment.
--     * Slot: d_score Description: Alignment score for the first or only D gene alignment.
--     * Slot: d_identity Description: Fractional identity for the first or only D gene alignment.
--     * Slot: d_support Description: D gene alignment E-value, p-value, likelihood, probability or other similar measure of support for the first or only D gene as defined by the alignment tool.
--     * Slot: d_cigar Description: CIGAR string for the first or only D gene alignment.
--     * Slot: d2_score Description: Alignment score for the second D gene alignment.
--     * Slot: d2_identity Description: Fractional identity for the second D gene alignment.
--     * Slot: d2_support Description: D gene alignment E-value, p-value, likelihood, probability or other similar measure of support for the second D gene as defined by the alignment tool.
--     * Slot: d2_cigar Description: CIGAR string for the second D gene alignment.
--     * Slot: j_score Description: Alignment score for the J gene alignment.
--     * Slot: j_identity Description: Fractional identity for the J gene alignment.
--     * Slot: j_support Description: J gene alignment E-value, p-value, likelihood, probability or other similar measure of support for the J gene assignment as defined by the alignment tool.
--     * Slot: j_cigar Description: CIGAR string for the J gene alignment.
--     * Slot: c_score Description: Alignment score for the C gene alignment.
--     * Slot: c_identity Description: Fractional identity for the C gene alignment.
--     * Slot: c_support Description: C gene alignment E-value, p-value, likelihood, probability or other similar measure of support for the C gene assignment as defined by the alignment tool.
--     * Slot: c_cigar Description: CIGAR string for the C gene alignment.
--     * Slot: v_sequence_start Description: Start position of the V gene in the query sequence (1-based closed interval).
--     * Slot: v_sequence_end Description: End position of the V gene in the query sequence (1-based closed interval).
--     * Slot: v_germline_start Description: Alignment start position in the V gene reference sequence (1-based closed interval).
--     * Slot: v_germline_end Description: Alignment end position in the V gene reference sequence (1-based closed interval).
--     * Slot: v_alignment_start Description: 
--     * Slot: v_alignment_end Description: 
--     * Slot: d_sequence_start Description: Start position of the first or only D gene in the query sequence. (1-based closed interval).
--     * Slot: d_sequence_end Description: End position of the first or only D gene in the query sequence. (1-based closed interval).
--     * Slot: d_germline_start Description: Alignment start position in the D gene reference sequence for the first or only D gene (1-based closed interval).
--     * Slot: d_germline_end Description: Alignment end position in the D gene reference sequence for the first or only D gene (1-based closed interval).
--     * Slot: d_alignment_start Description: 
--     * Slot: d_alignment_end Description: 
--     * Slot: d2_sequence_start Description: Start position of the second D gene in the query sequence (1-based closed interval).
--     * Slot: d2_sequence_end Description: End position of the second D gene in the query sequence (1-based closed interval).
--     * Slot: d2_germline_start Description: Alignment start position in the second D gene reference sequence (1-based closed interval).
--     * Slot: d2_germline_end Description: Alignment end position in the second D gene reference sequence (1-based closed interval).
--     * Slot: d2_alignment_start Description: Start position of the second D gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).
--     * Slot: d2_alignment_end Description: End position of the second D gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).
--     * Slot: j_sequence_start Description: Start position of the J gene in the query sequence (1-based closed interval).
--     * Slot: j_sequence_end Description: End position of the J gene in the query sequence (1-based closed interval).
--     * Slot: j_germline_start Description: Alignment start position in the J gene reference sequence (1-based closed interval).
--     * Slot: j_germline_end Description: Alignment end position in the J gene reference sequence (1-based closed interval).
--     * Slot: j_alignment_start Description: Start position of the J gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).
--     * Slot: j_alignment_end Description: End position of the J gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).
--     * Slot: c_sequence_start Description: Start position of the C gene in the query sequence (1-based closed interval).
--     * Slot: c_sequence_end Description: End position of the C gene in the query sequence (1-based closed interval).
--     * Slot: c_germline_start Description: Alignment start position in the C gene reference sequence (1-based closed interval).
--     * Slot: c_germline_end Description: Alignment end position in the C gene reference sequence (1-based closed interval).
--     * Slot: c_alignment_start Description: Start position of the C gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).
--     * Slot: c_alignment_end Description: End position of the C gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).
--     * Slot: cdr1_start Description: 
--     * Slot: cdr1_end Description: 
--     * Slot: cdr2_start Description: 
--     * Slot: cdr2_end Description: 
--     * Slot: cdr3_start Description: 
--     * Slot: cdr3_end Description: CDR3 end position in the query sequence (1-based closed interval).
--     * Slot: fwr1_start Description: 
--     * Slot: fwr1_end Description: 
--     * Slot: fwr2_start Description: 
--     * Slot: fwr2_end Description: 
--     * Slot: fwr3_start Description: 
--     * Slot: fwr3_end Description: 
--     * Slot: fwr4_start Description: FWR4 start position in the query sequence (1-based closed interval).
--     * Slot: fwr4_end Description: FWR4 end position in the query sequence (1-based closed interval).
--     * Slot: v_sequence_alignment Description: Aligned portion of query sequence assigned to the V gene, including any indel corrections or numbering spacers.
--     * Slot: v_sequence_alignment_aa Description: Amino acid translation of the v_sequence_alignment field.
--     * Slot: d_sequence_alignment Description: Aligned portion of query sequence assigned to the first or only D gene, including any indel corrections or numbering spacers.
--     * Slot: d_sequence_alignment_aa Description: Amino acid translation of the d_sequence_alignment field.
--     * Slot: d2_sequence_alignment Description: Aligned portion of query sequence assigned to the second D gene, including any indel corrections or numbering spacers.
--     * Slot: d2_sequence_alignment_aa Description: Amino acid translation of the d2_sequence_alignment field.
--     * Slot: j_sequence_alignment Description: Aligned portion of query sequence assigned to the J gene, including any indel corrections or numbering spacers.
--     * Slot: j_sequence_alignment_aa Description: Amino acid translation of the j_sequence_alignment field.
--     * Slot: c_sequence_alignment Description: Aligned portion of query sequence assigned to the constant region, including any indel corrections or numbering spacers.
--     * Slot: c_sequence_alignment_aa Description: Amino acid translation of the c_sequence_alignment field.
--     * Slot: v_germline_alignment Description: Aligned V gene germline sequence spanning the same region as the v_sequence_alignment field and including the same set of corrections and spacers (if any).
--     * Slot: v_germline_alignment_aa Description: Amino acid translation of the v_germline_alignment field.
--     * Slot: d_germline_alignment Description: Aligned D gene germline sequence spanning the same region as the d_sequence_alignment field and including the same set of corrections and spacers (if any).
--     * Slot: d_germline_alignment_aa Description: Amino acid translation of the d_germline_alignment field.
--     * Slot: d2_germline_alignment Description: Aligned D gene germline sequence spanning the same region as the d2_sequence_alignment field and including the same set of corrections and spacers (if any).
--     * Slot: d2_germline_alignment_aa Description: Amino acid translation of the d2_germline_alignment field.
--     * Slot: j_germline_alignment Description: Aligned J gene germline sequence spanning the same region as the j_sequence_alignment field and including the same set of corrections and spacers (if any).
--     * Slot: j_germline_alignment_aa Description: Amino acid translation of the j_germline_alignment field.
--     * Slot: c_germline_alignment Description: Aligned constant region germline sequence spanning the same region as the c_sequence_alignment field and including the same set of corrections and spacers (if any).
--     * Slot: c_germline_alignment_aa Description: Amino acid translation of the c_germline_aligment field.
--     * Slot: junction_length Description: 
--     * Slot: junction_aa_length Description: 
--     * Slot: np1_length Description: Number of nucleotides between the V gene and first D gene alignments or between the V gene and J gene alignments.
--     * Slot: np2_length Description: Number of nucleotides between either the first D gene and J gene alignments or the first D gene and second D gene alignments.
--     * Slot: np3_length Description: Number of nucleotides between the second D gene and J gene alignments.
--     * Slot: n1_length Description: Number of untemplated nucleotides 5' of the first or only D gene alignment.
--     * Slot: n2_length Description: Number of untemplated nucleotides 3' of the first or only D gene alignment.
--     * Slot: n3_length Description: Number of untemplated nucleotides 3' of the second D gene alignment.
--     * Slot: p3v_length Description: Number of palindromic nucleotides 3' of the V gene alignment.
--     * Slot: p5d_length Description: Number of palindromic nucleotides 5' of the first or only D gene alignment.
--     * Slot: p3d_length Description: Number of palindromic nucleotides 3' of the first or only D gene alignment.
--     * Slot: p5d2_length Description: Number of palindromic nucleotides 5' of the second D gene alignment.
--     * Slot: p3d2_length Description: Number of palindromic nucleotides 3' of the second D gene alignment.
--     * Slot: p5j_length Description: Number of palindromic nucleotides 5' of the J gene alignment.
--     * Slot: v_frameshift Description: True if the V gene in the query nucleotide sequence contains a translational frameshift relative to the frame of the V gene reference sequence.
--     * Slot: j_frameshift Description: True if the J gene in the query nucleotide sequence contains a translational frameshift relative to the frame of the J gene reference sequence.
--     * Slot: d_frame Description: Numerical reading frame (1, 2, 3) of the first or only D gene in the query nucleotide sequence, where frame 1 is relative to the first codon of D gene reference sequence.
--     * Slot: d2_frame Description: Numerical reading frame (1, 2, 3) of the second D gene in the query nucleotide sequence, where frame 1 is relative to the first codon of D gene reference sequence.
--     * Slot: consensus_count Description: Number of reads contributing to the UMI consensus or contig assembly for this sequence. For example, the sum of the number of reads for all UMIs that contribute to the query sequence.
--     * Slot: duplicate_count Description: Copy number or number of duplicate observations for the query sequence. For example, the number of identical reads observed for this sequence.
--     * Slot: umi_count Description: 
--     * Slot: cell_id Description: 
--     * Slot: clone_id Description: 
--     * Slot: repertoire_id Description: 
--     * Slot: sample_processing_id Description: 
--     * Slot: data_processing_id Description: 
-- # Class: "Clone" Description: ""
--     * Slot: id Description: 
--     * Slot: clone_id Description: 
--     * Slot: repertoire_id Description: 
--     * Slot: data_processing_id Description: 
--     * Slot: v_call Description: 
--     * Slot: d_call Description: 
--     * Slot: j_call Description: 
--     * Slot: junction Description: 
--     * Slot: junction_aa Description: Amino acid translation of the junction.
--     * Slot: junction_length Description: 
--     * Slot: junction_aa_length Description: 
--     * Slot: germline_alignment Description: 
--     * Slot: germline_alignment_aa Description: 
--     * Slot: v_alignment_start Description: 
--     * Slot: v_alignment_end Description: 
--     * Slot: d_alignment_start Description: 
--     * Slot: d_alignment_end Description: 
--     * Slot: j_alignment_start Description: Start position of the J gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).
--     * Slot: j_alignment_end Description: End position of the J gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).
--     * Slot: junction_start Description: Junction region start position in the alignment (1-based closed interval).
--     * Slot: junction_end Description: Junction region end position in the alignment (1-based closed interval).
--     * Slot: umi_count Description: 
--     * Slot: clone_count Description: Absolute count of the size (number of members) of this clone in the repertoire. This could simply be the number of sequences (Rearrangement records) observed in this clone, the number of distinct cell barcodes (unique cell_id values), or a more sophisticated calculation appropriate to the experimental protocol. Absolute count is provided versus a frequency so that downstream analysis tools can perform their own normalization.
--     * Slot: seed_id Description: sequence_id of the seed sequence. Empty string (or null) if there is no seed sequence.
-- # Class: "Tree" Description: ""
--     * Slot: id Description: 
--     * Slot: tree_id Description: Identifier for the tree.
--     * Slot: clone_id Description: 
--     * Slot: newick Description: Newick string of the tree edges.
-- # Class: "Node" Description: ""
--     * Slot: id Description: 
--     * Slot: sequence_id Description: 
--     * Slot: sequence_alignment Description: 
--     * Slot: junction Description: 
--     * Slot: junction_aa Description: Amino acid translation of the junction.
-- # Class: "Cell" Description: ""
--     * Slot: id Description: 
--     * Slot: cell_id Description: 
--     * Slot: repertoire_id Description: 
--     * Slot: data_processing_id Description: 
--     * Slot: expression_study_method Description: Keyword describing the methodology used to assess expression. This values for this field MUST  come from a controlled vocabulary.
--     * Slot: expression_raw_doi Description: DOI of raw data set containing the current event
--     * Slot: expression_index Description: Index addressing the current event within the raw data set.
--     * Slot: virtual_pairing Description: boolean to indicate if pairing was inferred.
-- # Class: "CellExpression" Description: ""
--     * Slot: id Description: 
--     * Slot: expression_id Description: Identifier of this expression property measurement.
--     * Slot: cell_id Description: 
--     * Slot: repertoire_id Description: 
--     * Slot: data_processing_id Description: 
--     * Slot: property_type Description: Keyword describing the property type and detection method used to measure the property value. The following keywords are recommended, but custom property types are also valid: "mrna_expression_by_read_count", "protein_expression_by_fluorescence_intensity", "antigen_bait_binding_by_fluorescence_intensity", "protein_expression_by_dna_barcode_count" and "antigen_bait_binding_by_dna_barcode_count".
--     * Slot: property Description: Name of the property observed, typically a gene or antibody identifier (and label) from a  canonical resource such as Ensembl (e.g. ENSG00000275747, IGHV3-79) or  Antibody Registry (ABREG:1236456, Purified anti-mouse/rat/human CD27 antibody).
--     * Slot: property_value Description: Level at which the property was observed in the experiment (non-normalized).
-- # Class: "Receptor" Description: ""
--     * Slot: id Description: 
--     * Slot: receptor_id Description: ID of the current Receptor object, unique within the local repository.
--     * Slot: receptor_hash Description: The SHA256 hash of the receptor amino acid sequence, calculated on the concatenated ``receptor_variable_domain_*_aa`` sequences and represented as base16-encoded string.
--     * Slot: receptor_type Description: The top-level receptor type, either Immunoglobulin (Ig) or T Cell Receptor (TCR).
--     * Slot: receptor_variable_domain_1_aa Description: Complete amino acid sequence of the mature variable domain of the Ig heavy, TCR beta or TCR delta chain. The mature variable domain is defined as encompassing all AA from and including first AA after the the signal peptide to and including the last AA that is completely encoded by the J gene.
--     * Slot: receptor_variable_domain_1_locus Description: Locus from which the variable domain in receptor_variable_domain_1_aa originates
--     * Slot: receptor_variable_domain_2_aa Description: Complete amino acid sequence of the mature variable domain of the Ig light, TCR alpha or TCR gamma chain. The mature variable domain is defined as encompassing all AA from and including first AA after the the signal peptide to and including the last AA that is completely encoded by the J gene.
--     * Slot: receptor_variable_domain_2_locus Description: Locus from which the variable domain in receptor_variable_domain_2_aa originates
-- # Class: "ReceptorReactivity" Description: ""
--     * Slot: id Description: 
--     * Slot: ligand_type Description: Classification of ligand binding to receptor
--     * Slot: antigen_type Description: The type of antigen before processing by the immune system.
--     * Slot: antigen Description: A material entity with antigen role
--     * Slot: antigen_source_species Description: The species from which the antigen was isolated
--     * Slot: peptide_start Description: Start position of the peptide within the reference protein sequence
--     * Slot: peptide_end Description: End position of the peptide within the reference protein sequence
--     * Slot: mhc_class Description: 
--     * Slot: mhc_gene_1 Description: The MHC gene to which the mhc_allele_1 belongs
--     * Slot: mhc_allele_1 Description: Allele designation of the MHC alpha chain
--     * Slot: mhc_gene_2 Description: The MHC gene to which the mhc_allele_2 belongs
--     * Slot: mhc_allele_2 Description: Allele designation of the MHC class II beta chain or the invariant beta2-microglobin chain
--     * Slot: reactivity_method Description: The methodology used to assess expression (assay implemented in experiment)
--     * Slot: reactivity_readout Description: Reactivity measurement read-out
--     * Slot: reactivity_value Description: The absolute (processed) value of the measurement
--     * Slot: reactivity_unit Description: The unit of the measurement
-- # Class: "SampleProcessing" Description: ""
--     * Slot: id Description: 
--     * Slot: sample_processing_id Description: 
--     * Slot: sample_id Description: Sample ID assigned by submitter, unique within study. If possible, a persistent sample ID linked to INSDC or similar repository study should be used.
--     * Slot: sample_type Description: The way the sample was obtained, e.g. fine-needle aspirate, organ harvest, peripheral venous puncture
--     * Slot: tissue Description: The actual tissue sampled, e.g. lymph node, liver, peripheral blood
--     * Slot: anatomic_site Description: The anatomic location of the tissue, e.g. Inguinal, femur
--     * Slot: disease_state_sample Description: Histopathologic evaluation of the sample
--     * Slot: collection_time_point_relative Description: Time point at which sample was taken, relative to `Collection time event`
--     * Slot: collection_time_point_relative_unit Description: Unit of Sample collection time
--     * Slot: collection_time_point_reference Description: Event in the study schedule to which `Sample collection time` relates to
--     * Slot: biomaterial_provider Description: Name and address of the entity providing the sample
--     * Slot: tissue_processing Description: Enzymatic digestion and/or physical methods used to isolate cells from sample
--     * Slot: cell_subset Description: Commonly-used designation of isolated cell population
--     * Slot: cell_phenotype Description: List of cellular markers and their expression levels used to isolate the cell population
--     * Slot: cell_species Description: Binomial designation of the species from which the analyzed cells originate. Typically, this value should be identical to `species`, in which case it SHOULD NOT be set explicitly. However, there are valid experimental setups in which the two might differ, e.g., chimeric animal models. If set, this key will overwrite the `species` information for all lower layers of the schema.
--     * Slot: single_cell Description: TRUE if single cells were isolated into separate compartments
--     * Slot: cell_number Description: Total number of cells that went into the experiment
--     * Slot: cells_per_reaction Description: Number of cells for each biological replicate
--     * Slot: cell_storage Description: TRUE if cells were cryo-preserved between isolation and further processing
--     * Slot: cell_quality Description: Relative amount of viable cells after preparation and (if applicable) thawing
--     * Slot: cell_isolation Description: Description of the procedure used for marker-based isolation or enrich cells
--     * Slot: cell_processing_protocol Description: Description of the methods applied to the sample including cell preparation/ isolation/enrichment and nucleic acid extraction. This should closely mirror the Materials and methods section in the manuscript.
--     * Slot: template_class Description: The class of nucleic acid that was used as primary starting material for the following procedures
--     * Slot: template_quality Description: Description and results of the quality control performed on the template material
--     * Slot: template_amount Description: Amount of template that went into the process
--     * Slot: template_amount_unit Description: Unit of template amount
--     * Slot: library_generation_method Description: Generic type of library generation
--     * Slot: library_generation_protocol Description: Description of processes applied to substrate to obtain a library that is ready for sequencing
--     * Slot: library_generation_kit_version Description: When using a library generation protocol from a commercial provider, provide the protocol version number
--     * Slot: complete_sequences Description: To be considered `complete`, the procedure used for library construction MUST generate sequences that 1) include the first V gene codon that encodes the mature polypeptide chain (i.e. after the leader sequence) and 2) include the last complete codon of the J gene (i.e. 1 bp 5' of the J->C splice site) and 3) provide sequence information for all positions between 1) and 2). To be considered `complete & untemplated`, the sections of the sequences defined in points 1) to 3) of the previous sentence MUST be untemplated, i.e. MUST NOT overlap with the primers used in library preparation. `mixed` should only be used if the procedure used for library construction will likely produce multiple categories of sequences in the given experiment. It SHOULD NOT be used as a replacement of a NULL value.
--     * Slot: physical_linkage Description: In case an experimental setup is used that physically links nucleic acids derived from distinct `Rearrangements` before library preparation, this field describes the mode of that linkage. All `hetero_*` terms indicate that in case of paired-read sequencing, the two reads should be expected to map to distinct IG/TR loci. `*_head-head` refers to techniques that link the 5' ends of transcripts in a single-cell context. `*_tail-head` refers to techniques that link the 3' end of one transcript to the 5' end of another one in a single-cell context. This term does not provide any information whether a continuous reading-frame between the two is generated. `*_prelinked` refers to constructs in which the linkage was already present on the DNA level (e.g. scFv).
--     * Slot: sequencing_run_id Description: ID of sequencing run assigned by the sequencing facility
--     * Slot: total_reads_passing_qc_filter Description: Number of usable reads for analysis
--     * Slot: sequencing_platform Description: Designation of sequencing instrument used
--     * Slot: sequencing_facility Description: Name and address of sequencing facility
--     * Slot: sequencing_run_date Description: Date of sequencing run
--     * Slot: sequencing_kit Description: Name, manufacturer, order and lot numbers of sequencing kit
--     * Slot: sequencing_files_id Description: Set of sequencing files produced by the sequencing run
-- # Class: "Investigation_participants" Description: ""
--     * Slot: Investigation_akc_id Description: Autocreated FK slot
--     * Slot: participants_akc_id Description: The participants involved with the investigation
-- # Class: "Investigation_assays" Description: ""
--     * Slot: Investigation_akc_id Description: Autocreated FK slot
--     * Slot: assays_akc_id Description: The assays performed by the investigation
-- # Class: "Investigation_simulations" Description: ""
--     * Slot: Investigation_akc_id Description: Autocreated FK slot
--     * Slot: simulations_akc_id Description: The simulations performed by the investigation
-- # Class: "Investigation_documents" Description: ""
--     * Slot: Investigation_akc_id Description: Autocreated FK slot
--     * Slot: documents_source_uri Description: The documents produced by the investigation
-- # Class: "Investigation_conclusions" Description: ""
--     * Slot: Investigation_akc_id Description: Autocreated FK slot
--     * Slot: conclusions_akc_id Description: The conclusions from the investigation
-- # Class: "Reference_sources" Description: ""
--     * Slot: Reference_source_uri Description: Autocreated FK slot
--     * Slot: sources Description: The source URLs for a reference
-- # Class: "Reference_investigations" Description: ""
--     * Slot: Reference_source_uri Description: Autocreated FK slot
--     * Slot: investigations_akc_id Description: The investigations that a reference or conclusion are about
-- # Class: "Reference_authors" Description: ""
--     * Slot: Reference_source_uri Description: Autocreated FK slot
--     * Slot: authors Description: The authors of a reference
-- # Class: "StudyEvent_study_arms" Description: ""
--     * Slot: StudyEvent_akc_id Description: Autocreated FK slot
--     * Slot: study_arms_akc_id Description: The study arms that are relevant for a study event
-- # Class: "LibraryPreparationProcessing_pcr_target" Description: ""
--     * Slot: LibraryPreparationProcessing_akc_id Description: Autocreated FK slot
--     * Slot: pcr_target_id Description: If a PCR step was performed that specifically targets the IG/TR loci, the target and primer locations need to be provided here. This field holds an array of PCRTarget objects, so that multiplex PCR setups amplifying multiple loci at the same time can be annotated using one record per locus. PCR setups not targeting any specific locus must not annotate this field but select the appropriate library_generation_method instead.
-- # Class: "AIRRSequencingAssay_tcell_receptors" Description: ""
--     * Slot: AIRRSequencingAssay_akc_id Description: Autocreated FK slot
--     * Slot: tcell_receptors_akc_id Description: The T cell receptors being measured
-- # Class: "AIRRSequencingAssay_tcell_chains" Description: ""
--     * Slot: AIRRSequencingAssay_akc_id Description: Autocreated FK slot
--     * Slot: tcell_chains_akc_id Description: The T cell receptor chains being measured
-- # Class: "TCellReceptorEpitopeBindingAssay_tcell_receptors" Description: ""
--     * Slot: TCellReceptorEpitopeBindingAssay_akc_id Description: Autocreated FK slot
--     * Slot: tcell_receptors_akc_id Description: The T cell receptors being measured
-- # Class: "DataSet_data_items" Description: ""
--     * Slot: DataSet_id Description: Autocreated FK slot
--     * Slot: data_items_akc_id Description: set of data items
-- # Class: "AKDataItem_data_item_types" Description: ""
--     * Slot: AKDataItem_akc_id Description: Autocreated FK slot
--     * Slot: data_item_types Description: semantic types of the data
-- # Class: "AKDataSet_data_items" Description: ""
--     * Slot: AKDataSet_akc_id Description: Autocreated FK slot
--     * Slot: data_items_akc_id Description: set of data items
-- # Class: "AKDataSet_data_item_types" Description: ""
--     * Slot: AKDataSet_akc_id Description: Autocreated FK slot
--     * Slot: data_item_types Description: semantic types of the data
-- # Class: "SequenceData_data_item_types" Description: ""
--     * Slot: SequenceData_akc_id Description: Autocreated FK slot
--     * Slot: data_item_types Description: semantic types of the data
-- # Class: "AIRRSequencingData_data_item_types" Description: ""
--     * Slot: AIRRSequencingData_akc_id Description: Autocreated FK slot
--     * Slot: data_item_types Description: semantic types of the data
-- # Class: "RNATranscriptomeData_data_item_types" Description: ""
--     * Slot: RNATranscriptomeData_akc_id Description: Autocreated FK slot
--     * Slot: data_item_types Description: semantic types of the data
-- # Class: "DataTransformation_was_generated_by" Description: ""
--     * Slot: DataTransformation_akc_id Description: Autocreated FK slot
--     * Slot: was_generated_by_id Description: direct provenance link of one entity (input) to another (output) for a data transformation
-- # Class: "DataTransformation_data_transformation_types" Description: ""
--     * Slot: DataTransformation_akc_id Description: Autocreated FK slot
--     * Slot: data_transformation_types Description: semantic types of the data transformation
-- # Class: "Conclusion_investigations" Description: ""
--     * Slot: Conclusion_akc_id Description: Autocreated FK slot
--     * Slot: investigations_akc_id Description: The investigations that a reference or conclusion are about
-- # Class: "Conclusion_datasets" Description: ""
--     * Slot: Conclusion_akc_id Description: Autocreated FK slot
--     * Slot: datasets_akc_id Description: The datasets that support a conclusion
-- # Class: "SequenceDelineationV_alignment_labels" Description: ""
--     * Slot: SequenceDelineationV_id Description: Autocreated FK slot
--     * Slot: alignment_labels Description: One string for each codon in the aligned_sequence indicating the label of that codon according to  the numbering of the delineation scheme if it provides one.
-- # Class: "AlleleDescription_acknowledgements" Description: ""
--     * Slot: AlleleDescription_id Description: Autocreated FK slot
--     * Slot: acknowledgements_id Description: 
-- # Class: "AlleleDescription_aliases" Description: ""
--     * Slot: AlleleDescription_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names for this sequence
-- # Class: "AlleleDescription_v_gene_delineations" Description: ""
--     * Slot: AlleleDescription_id Description: Autocreated FK slot
--     * Slot: v_gene_delineations_id Description: 
-- # Class: "AlleleDescription_unrearranged_support" Description: ""
--     * Slot: AlleleDescription_id Description: Autocreated FK slot
--     * Slot: unrearranged_support_id Description: 
-- # Class: "AlleleDescription_rearranged_support" Description: ""
--     * Slot: AlleleDescription_id Description: Autocreated FK slot
--     * Slot: rearranged_support_id Description: 
-- # Class: "AlleleDescription_paralogs" Description: ""
--     * Slot: AlleleDescription_id Description: Autocreated FK slot
--     * Slot: paralogs Description: Gene symbols of any paralogs
-- # Class: "AlleleDescription_curational_tags" Description: ""
--     * Slot: AlleleDescription_id Description: Autocreated FK slot
--     * Slot: curational_tags Description: Controlled-vocabulary tags applied to this description
-- # Class: "GermlineSet_acknowledgements" Description: ""
--     * Slot: GermlineSet_id Description: Autocreated FK slot
--     * Slot: acknowledgements_id Description: 
-- # Class: "GermlineSet_allele_descriptions" Description: ""
--     * Slot: GermlineSet_id Description: Autocreated FK slot
--     * Slot: allele_descriptions_id Description: list of allele_descriptions in the germline set
-- # Class: "GenotypeSet_genotype_class_list" Description: ""
--     * Slot: GenotypeSet_id Description: Autocreated FK slot
--     * Slot: genotype_class_list_id Description: List of Genotypes included in this Receptor Genotype Set.
-- # Class: "Genotype_documented_alleles" Description: ""
--     * Slot: Genotype_id Description: Autocreated FK slot
--     * Slot: documented_alleles_id Description: List of alleles documented in reference set(s)
-- # Class: "Genotype_undocumented_alleles" Description: ""
--     * Slot: Genotype_id Description: Autocreated FK slot
--     * Slot: undocumented_alleles_id Description: List of alleles inferred to be present and not documented in an identified GermlineSet
-- # Class: "Genotype_deleted_genes" Description: ""
--     * Slot: Genotype_id Description: Autocreated FK slot
--     * Slot: deleted_genes_id Description: Array of genes identified as being deleted in this genotype
-- # Class: "MHCGenotypeSet_mhc_genotype_list" Description: ""
--     * Slot: MHCGenotypeSet_id Description: Autocreated FK slot
--     * Slot: mhc_genotype_list_id Description: List of MHCGenotypes included in this set
-- # Class: "MHCGenotype_mhc_alleles" Description: ""
--     * Slot: MHCGenotype_id Description: Autocreated FK slot
--     * Slot: mhc_alleles_id Description: List of MHC alleles of the indicated mhc_class identified in an individual
-- # Class: "Study_keywords_study" Description: ""
--     * Slot: Study_id Description: Autocreated FK slot
--     * Slot: keywords_study Description: Keywords describing properties of one or more data sets in a study. "contains_schema" keywords indicate that the study contains data objects from the AIRR Schema of that type (Rearrangement, Clone, Cell, Receptor) while the other keywords indicate that the study design considers the type of data indicated (e.g. it is possible to have a study that "contains_paired_chain" but does not "contains_schema_cell").
-- # Class: "Subject_diagnosis" Description: ""
--     * Slot: Subject_id Description: Autocreated FK slot
--     * Slot: diagnosis_id Description: Diagnosis information for subject
-- # Class: "NucleicAcidProcessing_pcr_target" Description: ""
--     * Slot: NucleicAcidProcessing_id Description: Autocreated FK slot
--     * Slot: pcr_target_id Description: If a PCR step was performed that specifically targets the IG/TR loci, the target and primer locations need to be provided here. This field holds an array of PCRTarget objects, so that multiplex PCR setups amplifying multiple loci at the same time can be annotated using one record per locus. PCR setups not targeting any specific locus must not annotate this field but select the appropriate library_generation_method instead.
-- # Class: "DataProcessing_data_processing_files" Description: ""
--     * Slot: DataProcessing_id Description: Autocreated FK slot
--     * Slot: data_processing_files Description: Array of file names for data produced by this data processing.
-- # Class: "Repertoire_sample" Description: ""
--     * Slot: Repertoire_id Description: Autocreated FK slot
--     * Slot: sample_id Description: List of Sample Processing objects
-- # Class: "Repertoire_data_processing" Description: ""
--     * Slot: Repertoire_id Description: Autocreated FK slot
--     * Slot: data_processing_id Description: List of Data Processing objects
-- # Class: "RepertoireGroup_repertoires" Description: ""
--     * Slot: RepertoireGroup_id Description: Autocreated FK slot
--     * Slot: repertoires_id Description: List of repertoires in this collection with an associated description and time point designation
-- # Class: "Clone_sequences" Description: ""
--     * Slot: Clone_id Description: Autocreated FK slot
--     * Slot: sequences Description: List sequence_id strings that act as keys to the Rearrangement records for members of the clone.
-- # Class: "Tree_nodes" Description: ""
--     * Slot: Tree_id Description: Autocreated FK slot
--     * Slot: nodes_id Description: Dictionary of nodes in the tree, keyed by sequence_id string
-- # Class: "Cell_rearrangements" Description: ""
--     * Slot: Cell_id Description: Autocreated FK slot
--     * Slot: rearrangements Description: Array of sequence identifiers defined for the Rearrangement object
-- # Class: "Cell_receptors" Description: ""
--     * Slot: Cell_id Description: Autocreated FK slot
--     * Slot: receptors Description: Array of receptor identifiers defined for the Receptor object
-- # Class: "Receptor_receptor_ref" Description: ""
--     * Slot: Receptor_id Description: Autocreated FK slot
--     * Slot: receptor_ref Description: Array of receptor identifiers defined for the Receptor object
-- # Class: "Receptor_reactivity_measurements" Description: ""
--     * Slot: Receptor_id Description: Autocreated FK slot
--     * Slot: reactivity_measurements_id Description: Records of reactivity measurement
-- # Class: "SampleProcessing_pcr_target" Description: ""
--     * Slot: SampleProcessing_id Description: Autocreated FK slot
--     * Slot: pcr_target_id Description: If a PCR step was performed that specifically targets the IG/TR loci, the target and primer locations need to be provided here. This field holds an array of PCRTarget objects, so that multiplex PCR setups amplifying multiple loci at the same time can be annotated using one record per locus. PCR setups not targeting any specific locus must not annotate this field but select the appropriate library_generation_method instead.

CREATE TABLE "AKObject" (
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "ForeignObject" (
	source_uri TEXT NOT NULL, 
	PRIMARY KEY (source_uri)
);
CREATE TABLE "AIRRStandards" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "AIRRStandards_v1p5" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "AIRRStandards_v2p0" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "NamedThing" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "Process" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "PlanSpecification" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "Investigation" (
	investigation_type VARCHAR, 
	archival_id TEXT, 
	inclusion_exclusion_criteria TEXT, 
	release_date TIMESTAMP WITHOUT TIME ZONE, 
	update_date TIMESTAMP WITHOUT TIME ZONE, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "Reference" (
	title TEXT, 
	journal TEXT, 
	issue TEXT, 
	month TEXT, 
	year INTEGER, 
	pages TEXT, 
	source_uri TEXT NOT NULL, 
	PRIMARY KEY (source_uri)
);
CREATE TABLE "StudyEvent" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "DataItem" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "MeasurementDatum" (
	id INTEGER NOT NULL, 
	measurement_value INTEGER, 
	measurement_unit VARCHAR, 
	PRIMARY KEY (id)
);
CREATE TABLE "MeasurementCategory" (
	id INTEGER NOT NULL, 
	measurement_category TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "TCellReceptorEpitopeSpecificityMeasurement" (
	id INTEGER NOT NULL, 
	measurement_category VARCHAR(21), 
	PRIMARY KEY (id)
);
CREATE TABLE "DataSet" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "AKDataItem" (
	type TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "AKDataSet" (
	type TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "SequenceData" (
	type TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "AIRRSequencingData" (
	sequencing_data_id TEXT, 
	file_type VARCHAR(5), 
	filename TEXT, 
	read_direction VARCHAR(7), 
	read_length INTEGER, 
	paired_filename TEXT, 
	paired_read_direction VARCHAR(7), 
	paired_read_length INTEGER, 
	index_filename TEXT, 
	index_length INTEGER, 
	type TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "RNATranscriptomeData" (
	type TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "DataTransformation" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "Conclusion" (
	result TEXT, 
	data_location_type TEXT, 
	data_location_value TEXT, 
	organism VARCHAR, 
	experiment_type TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "ImmuneSystem" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "Chain" (
	species VARCHAR, 
	aa_hash TEXT, 
	junction_aa_vj_allele_hash TEXT, 
	junction_aa_vj_gene_hash TEXT, 
	complete_vdj BOOLEAN, 
	sequence TEXT, 
	sequence_aa TEXT, 
	locus VARCHAR(3), 
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
);
CREATE TABLE "ImmuneReceptor" (
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "TCellReceptor" (
	tra_chain TEXT, 
	trb_chain TEXT, 
	trg_chain TEXT, 
	trd_chain TEXT, 
	type TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(tra_chain) REFERENCES "Chain" (akc_id), 
	FOREIGN KEY(trb_chain) REFERENCES "Chain" (akc_id),
	FOREIGN KEY(trg_chain) REFERENCES "Chain" (akc_id), 
	FOREIGN KEY(trd_chain) REFERENCES "Chain" (akc_id)
);
CREATE TABLE "Antigen" (
	source_protein TEXT, 
	source_organism TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "Epitope" (
	sequence_aa TEXT, 
	source_protein TEXT, 
	source_organism TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "PeptidicEpitope" (
	sequence_aa TEXT, 
	source_protein TEXT, 
	source_organism TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "Model" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "ConceptualModel" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "CommunicativeModel" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "ModelSpecification" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "ModelingFramework" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "Simulation" (
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id)
);
CREATE TABLE "TimePoint" (
	id INTEGER NOT NULL, 
	time_point_label TEXT, 
	time_point_value FLOAT, 
	time_point_unit VARCHAR, 
	PRIMARY KEY (id)
);
CREATE TABLE "Acknowledgement" (
	id INTEGER NOT NULL, 
	acknowledgement_id TEXT, 
	individual_full_name TEXT, 
	institution_name TEXT, 
	orcid_id TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "RearrangedSequence" (
	id INTEGER NOT NULL, 
	sequence_id TEXT, 
	sequence TEXT, 
	derivation VARCHAR(3), 
	observation_type VARCHAR(25), 
	curation TEXT, 
	repository_name TEXT, 
	repository_ref TEXT, 
	deposited_version TEXT, 
	sequence_start INTEGER, 
	sequence_end INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "UnrearrangedSequence" (
	id INTEGER NOT NULL, 
	sequence_id TEXT, 
	sequence TEXT, 
	curation TEXT, 
	repository_name TEXT, 
	repository_ref TEXT, 
	patch_no TEXT, 
	gff_seqid TEXT, 
	gff_start INTEGER, 
	gff_end INTEGER, 
	strand VARCHAR(1), 
	PRIMARY KEY (id)
);
CREATE TABLE "SequenceDelineationV" (
	id INTEGER NOT NULL, 
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
);
CREATE TABLE "AlleleDescription" (
	id INTEGER NOT NULL, 
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
	locus VARCHAR(3), 
	chromosome INTEGER, 
	sequence_type VARCHAR(1), 
	functional BOOLEAN, 
	inference_type VARCHAR(22), 
	species VARCHAR, 
	species_subgroup TEXT, 
	species_subgroup_type VARCHAR(10), 
	status VARCHAR(9), 
	subgroup_designation TEXT, 
	gene_designation TEXT, 
	allele_designation TEXT, 
	allele_similarity_cluster_designation TEXT, 
	allele_similarity_cluster_member_id TEXT, 
	j_codon_frame VARCHAR(1), 
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
);
CREATE TABLE "GermlineSet" (
	id INTEGER NOT NULL, 
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
	species VARCHAR, 
	species_subgroup TEXT, 
	species_subgroup_type VARCHAR(10), 
	locus VARCHAR(3), 
	curation TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "GenotypeSet" (
	id INTEGER NOT NULL, 
	receptor_genotype_set_id TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Genotype" (
	id INTEGER NOT NULL, 
	receptor_genotype_id TEXT, 
	locus VARCHAR(3), 
	inference_process VARCHAR(21), 
	PRIMARY KEY (id)
);
CREATE TABLE "DocumentedAllele" (
	id INTEGER NOT NULL, 
	label TEXT, 
	germline_set_ref TEXT, 
	phasing INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "UndocumentedAllele" (
	id INTEGER NOT NULL, 
	allele_name TEXT, 
	sequence TEXT, 
	phasing INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "DeletedGene" (
	id INTEGER NOT NULL, 
	label TEXT, 
	germline_set_ref TEXT, 
	phasing INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "MHCGenotypeSet" (
	id INTEGER NOT NULL, 
	mhc_genotype_set_id TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "MHCGenotype" (
	id INTEGER NOT NULL, 
	mhc_genotype_id TEXT, 
	mhc_class VARCHAR(16), 
	mhc_genotyping_method TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "MHCAllele" (
	id INTEGER NOT NULL, 
	allele_designation TEXT, 
	gene VARCHAR, 
	reference_set_ref TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Study" (
	id INTEGER NOT NULL, 
	study_id TEXT, 
	study_title TEXT, 
	study_type VARCHAR, 
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
);
CREATE TABLE "Diagnosis" (
	id INTEGER NOT NULL, 
	study_group_description TEXT, 
	disease_diagnosis VARCHAR, 
	disease_length TEXT, 
	disease_stage TEXT, 
	prior_therapies TEXT, 
	immunogen TEXT, 
	intervention TEXT, 
	medical_history TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Sample" (
	id INTEGER NOT NULL, 
	sample_id TEXT, 
	sample_type TEXT, 
	tissue VARCHAR, 
	anatomic_site TEXT, 
	disease_state_sample TEXT, 
	collection_time_point_relative FLOAT, 
	collection_time_point_relative_unit VARCHAR, 
	collection_time_point_reference TEXT, 
	biomaterial_provider TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "CellProcessing" (
	id INTEGER NOT NULL, 
	tissue_processing TEXT, 
	cell_subset VARCHAR, 
	cell_phenotype TEXT, 
	cell_species VARCHAR, 
	single_cell BOOLEAN, 
	cell_number INTEGER, 
	cells_per_reaction INTEGER, 
	cell_storage BOOLEAN, 
	cell_quality TEXT, 
	cell_isolation TEXT, 
	cell_processing_protocol TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "PCRTarget" (
	id INTEGER NOT NULL, 
	pcr_target_locus VARCHAR(3), 
	forward_pcr_primer_target_location TEXT, 
	reverse_pcr_primer_target_location TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "NucleicAcidProcessing" (
	id INTEGER NOT NULL, 
	template_class VARCHAR(3), 
	template_quality TEXT, 
	template_amount FLOAT, 
	template_amount_unit VARCHAR, 
	library_generation_method VARCHAR(24), 
	library_generation_protocol TEXT, 
	library_generation_kit_version TEXT, 
	complete_sequences VARCHAR(20), 
	physical_linkage VARCHAR(16), 
	PRIMARY KEY (id)
);
CREATE TABLE "SequencingData" (
	id INTEGER NOT NULL, 
	sequencing_data_id TEXT, 
	file_type VARCHAR(5), 
	filename TEXT, 
	read_direction VARCHAR(7), 
	read_length INTEGER, 
	paired_filename TEXT, 
	paired_read_direction VARCHAR(7), 
	paired_read_length INTEGER, 
	index_filename TEXT, 
	index_length INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "DataProcessing" (
	id INTEGER NOT NULL, 
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
);
CREATE TABLE "RepertoireGroup" (
	id INTEGER NOT NULL, 
	repertoire_group_id TEXT, 
	repertoire_group_name TEXT, 
	repertoire_group_description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Alignment" (
	id INTEGER NOT NULL, 
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
);
CREATE TABLE "Rearrangement" (
	id INTEGER NOT NULL, 
	sequence_id TEXT, 
	sequence TEXT, 
	quality TEXT, 
	sequence_aa TEXT, 
	rev_comp BOOLEAN, 
	productive BOOLEAN, 
	vj_in_frame BOOLEAN, 
	stop_codon BOOLEAN, 
	complete_vdj BOOLEAN, 
	locus VARCHAR(3), 
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
);
CREATE TABLE "Clone" (
	id INTEGER NOT NULL, 
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
);
CREATE TABLE "Tree" (
	id INTEGER NOT NULL, 
	tree_id TEXT, 
	clone_id TEXT, 
	newick TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Node" (
	id INTEGER NOT NULL, 
	sequence_id TEXT, 
	sequence_alignment TEXT, 
	junction TEXT, 
	junction_aa TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Cell" (
	id INTEGER NOT NULL, 
	cell_id TEXT, 
	repertoire_id TEXT, 
	data_processing_id TEXT, 
	expression_study_method VARCHAR(25), 
	expression_raw_doi TEXT, 
	expression_index TEXT, 
	virtual_pairing BOOLEAN, 
	PRIMARY KEY (id)
);
CREATE TABLE "CellExpression" (
	id INTEGER NOT NULL, 
	expression_id TEXT, 
	cell_id TEXT, 
	repertoire_id TEXT, 
	data_processing_id TEXT, 
	property_type TEXT, 
	property VARCHAR, 
	property_value FLOAT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Receptor" (
	id INTEGER NOT NULL, 
	receptor_id TEXT, 
	receptor_hash TEXT, 
	receptor_type VARCHAR(3), 
	receptor_variable_domain_1_aa TEXT, 
	receptor_variable_domain_1_locus VARCHAR(3), 
	receptor_variable_domain_2_aa TEXT, 
	receptor_variable_domain_2_locus VARCHAR(3), 
	PRIMARY KEY (id)
);
CREATE TABLE "StudyArm" (
	investigation TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(investigation) REFERENCES "Investigation" (akc_id)
);
CREATE TABLE "InputOutputDataMap" (
	id INTEGER NOT NULL, 
	data_transformation TEXT, 
	has_specified_input TEXT, 
	has_specified_output TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(data_transformation) REFERENCES "DataTransformation" (akc_id), 
	FOREIGN KEY(has_specified_input) REFERENCES "AKDataItem" (akc_id), 
	FOREIGN KEY(has_specified_output) REFERENCES "AKDataItem" (akc_id)
);
CREATE TABLE "AlphaBetaTCR" (
	tra_chain TEXT, 
	trb_chain TEXT, 
	type TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(tra_chain) REFERENCES "Chain" (akc_id), 
	FOREIGN KEY(trb_chain) REFERENCES "Chain" (akc_id)
);
CREATE TABLE "GammaDeltaTCR" (
	trg_chain TEXT, 
	trd_chain TEXT, 
	type TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(trg_chain) REFERENCES "Chain" (akc_id), 
	FOREIGN KEY(trd_chain) REFERENCES "Chain" (akc_id)
);
CREATE TABLE "BCellReceptor" (
	igh_chain TEXT, 
	igk_chain TEXT, 
	igl_chain TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(igh_chain) REFERENCES "Chain" (akc_id), 
	FOREIGN KEY(igk_chain) REFERENCES "Chain" (akc_id), 
	FOREIGN KEY(igl_chain) REFERENCES "Chain" (akc_id)
);
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
);
CREATE TABLE "SimilarityCalculation" (
	chain_domain TEXT, 
	chain_codomain TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(chain_domain) REFERENCES "Chain" (akc_id), 
	FOREIGN KEY(chain_codomain) REFERENCES "Chain" (akc_id)
);
CREATE TABLE "ChainSimilarity" (
	chain_similarity_type VARCHAR(26), 
	chain_domain TEXT, 
	chain_codomain TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(chain_domain) REFERENCES "Chain" (akc_id), 
	FOREIGN KEY(chain_codomain) REFERENCES "Chain" (akc_id)
);
CREATE TABLE "SubjectGenotype" (
	id INTEGER NOT NULL, 
	receptor_genotype_set_id INTEGER, 
	mhc_genotype_set_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(receptor_genotype_set_id) REFERENCES "GenotypeSet" (id), 
	FOREIGN KEY(mhc_genotype_set_id) REFERENCES "MHCGenotypeSet" (id)
);
CREATE TABLE "SequencingRun" (
	id INTEGER NOT NULL, 
	sequencing_run_id TEXT, 
	total_reads_passing_qc_filter INTEGER, 
	sequencing_platform TEXT, 
	sequencing_facility TEXT, 
	sequencing_run_date TIMESTAMP WITHOUT TIME ZONE, 
	sequencing_kit TEXT, 
	sequencing_files_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(sequencing_files_id) REFERENCES "SequencingData" (id)
);
CREATE TABLE "RepertoireGroupDetail" (
	id INTEGER NOT NULL, 
	repertoire_id TEXT, 
	repertoire_description TEXT, 
	time_point_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(time_point_id) REFERENCES "TimePoint" (id)
);
CREATE TABLE "ReceptorReactivity" (
	id INTEGER NOT NULL, 
	ligand_type VARCHAR(15), 
	antigen_type VARCHAR(12), 
	antigen TEXT, 
	antigen_source_species VARCHAR, 
	peptide_start INTEGER, 
	peptide_end INTEGER, 
	mhc_class VARCHAR(16), 
	mhc_gene_1 VARCHAR, 
	mhc_allele_1 TEXT, 
	mhc_gene_2 VARCHAR, 
	mhc_allele_2 TEXT, 
	reactivity_method VARCHAR(19), 
	reactivity_readout VARCHAR(24), 
	reactivity_value FLOAT, 
	reactivity_unit TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(antigen) REFERENCES "Antigen" (akc_id)
);
CREATE TABLE "SampleProcessing" (
	id INTEGER NOT NULL, 
	sample_processing_id TEXT, 
	sample_id TEXT, 
	sample_type TEXT, 
	tissue VARCHAR, 
	anatomic_site TEXT, 
	disease_state_sample TEXT, 
	collection_time_point_relative FLOAT, 
	collection_time_point_relative_unit VARCHAR, 
	collection_time_point_reference TEXT, 
	biomaterial_provider TEXT, 
	tissue_processing TEXT, 
	cell_subset VARCHAR, 
	cell_phenotype TEXT, 
	cell_species VARCHAR, 
	single_cell BOOLEAN, 
	cell_number INTEGER, 
	cells_per_reaction INTEGER, 
	cell_storage BOOLEAN, 
	cell_quality TEXT, 
	cell_isolation TEXT, 
	cell_processing_protocol TEXT, 
	template_class VARCHAR(3), 
	template_quality TEXT, 
	template_amount FLOAT, 
	template_amount_unit VARCHAR, 
	library_generation_method VARCHAR(24), 
	library_generation_protocol TEXT, 
	library_generation_kit_version TEXT, 
	complete_sequences VARCHAR(20), 
	physical_linkage VARCHAR(16), 
	sequencing_run_id TEXT, 
	total_reads_passing_qc_filter INTEGER, 
	sequencing_platform TEXT, 
	sequencing_facility TEXT, 
	sequencing_run_date TIMESTAMP WITHOUT TIME ZONE, 
	sequencing_kit TEXT, 
	sequencing_files_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(sequencing_files_id) REFERENCES "SequencingData" (id)
);
CREATE TABLE "Investigation_simulations" (
	investigation_akc_id TEXT, 
	simulations_akc_id TEXT, 
	PRIMARY KEY (investigation_akc_id, simulations_akc_id), 
	FOREIGN KEY(investigation_akc_id) REFERENCES "Investigation" (akc_id), 
	FOREIGN KEY(simulations_akc_id) REFERENCES "Simulation" (akc_id)
);
CREATE TABLE "Investigation_documents" (
	investigation_akc_id TEXT, 
	documents_source_uri TEXT, 
	PRIMARY KEY (investigation_akc_id, documents_source_uri), 
	FOREIGN KEY(investigation_akc_id) REFERENCES "Investigation" (akc_id), 
	FOREIGN KEY(documents_source_uri) REFERENCES "Reference" (source_uri)
);
CREATE TABLE "Investigation_conclusions" (
	investigation_akc_id TEXT, 
	conclusions_akc_id TEXT, 
	PRIMARY KEY (investigation_akc_id, conclusions_akc_id), 
	FOREIGN KEY(investigation_akc_id) REFERENCES "Investigation" (akc_id), 
	FOREIGN KEY(conclusions_akc_id) REFERENCES "Conclusion" (akc_id)
);
CREATE TABLE "Reference_sources" (
	"Reference_source_uri" TEXT, 
	sources TEXT, 
	PRIMARY KEY ("Reference_source_uri", sources), 
	FOREIGN KEY("Reference_source_uri") REFERENCES "Reference" (source_uri)
);
CREATE TABLE "Reference_investigations" (
	"Reference_source_uri" TEXT, 
	investigations_akc_id TEXT, 
	PRIMARY KEY ("Reference_source_uri", investigations_akc_id), 
	FOREIGN KEY("Reference_source_uri") REFERENCES "Reference" (source_uri), 
	FOREIGN KEY(investigations_akc_id) REFERENCES "Investigation" (akc_id)
);
CREATE TABLE "Reference_authors" (
	"Reference_source_uri" TEXT, 
	authors TEXT, 
	PRIMARY KEY ("Reference_source_uri", authors), 
	FOREIGN KEY("Reference_source_uri") REFERENCES "Reference" (source_uri)
);
CREATE TABLE "DataSet_data_items" (
	"DataSet_id" INTEGER, 
	data_items_akc_id TEXT, 
	PRIMARY KEY ("DataSet_id", data_items_akc_id), 
	FOREIGN KEY("DataSet_id") REFERENCES "DataSet" (id), 
	FOREIGN KEY(data_items_akc_id) REFERENCES "AKObject" (akc_id)
);
CREATE TABLE "AKDataItem_data_item_types" (
	"AKDataItem_akc_id" TEXT, 
	data_item_types VARCHAR(29), 
	PRIMARY KEY ("AKDataItem_akc_id", data_item_types), 
	FOREIGN KEY("AKDataItem_akc_id") REFERENCES "AKDataItem" (akc_id)
);
CREATE TABLE "AKDataSet_data_items" (
	"AKDataSet_akc_id" TEXT, 
	data_items_akc_id TEXT, 
	PRIMARY KEY ("AKDataSet_akc_id", data_items_akc_id), 
	FOREIGN KEY("AKDataSet_akc_id") REFERENCES "AKDataSet" (akc_id), 
	FOREIGN KEY(data_items_akc_id) REFERENCES "AKObject" (akc_id)
);
CREATE TABLE "AKDataSet_data_item_types" (
	"AKDataSet_akc_id" TEXT, 
	data_item_types VARCHAR(29), 
	PRIMARY KEY ("AKDataSet_akc_id", data_item_types), 
	FOREIGN KEY("AKDataSet_akc_id") REFERENCES "AKDataSet" (akc_id)
);
CREATE TABLE "SequenceData_data_item_types" (
	"SequenceData_akc_id" TEXT, 
	data_item_types VARCHAR(29), 
	PRIMARY KEY ("SequenceData_akc_id", data_item_types), 
	FOREIGN KEY("SequenceData_akc_id") REFERENCES "SequenceData" (akc_id)
);
CREATE TABLE "AIRRSequencingData_data_item_types" (
	"AIRRSequencingData_akc_id" TEXT, 
	data_item_types VARCHAR(29), 
	PRIMARY KEY ("AIRRSequencingData_akc_id", data_item_types), 
	FOREIGN KEY("AIRRSequencingData_akc_id") REFERENCES "AIRRSequencingData" (akc_id)
);
CREATE TABLE "RNATranscriptomeData_data_item_types" (
	"RNATranscriptomeData_akc_id" TEXT, 
	data_item_types VARCHAR(29), 
	PRIMARY KEY ("RNATranscriptomeData_akc_id", data_item_types), 
	FOREIGN KEY("RNATranscriptomeData_akc_id") REFERENCES "RNATranscriptomeData" (akc_id)
);
CREATE TABLE "DataTransformation_data_transformation_types" (
	"DataTransformation_akc_id" TEXT, 
	data_transformation_types VARCHAR(29), 
	PRIMARY KEY ("DataTransformation_akc_id", data_transformation_types), 
	FOREIGN KEY("DataTransformation_akc_id") REFERENCES "DataTransformation" (akc_id)
);
CREATE TABLE "Conclusion_investigations" (
	"Conclusion_akc_id" TEXT, 
	investigations_akc_id TEXT, 
	PRIMARY KEY ("Conclusion_akc_id", investigations_akc_id), 
	FOREIGN KEY("Conclusion_akc_id") REFERENCES "Conclusion" (akc_id), 
	FOREIGN KEY(investigations_akc_id) REFERENCES "Investigation" (akc_id)
);
CREATE TABLE "Conclusion_datasets" (
	"Conclusion_akc_id" TEXT, 
	datasets_akc_id TEXT, 
	PRIMARY KEY ("Conclusion_akc_id", datasets_akc_id), 
	FOREIGN KEY("Conclusion_akc_id") REFERENCES "Conclusion" (akc_id), 
	FOREIGN KEY(datasets_akc_id) REFERENCES "AKDataSet" (akc_id)
);
CREATE TABLE "SequenceDelineationV_alignment_labels" (
	"SequenceDelineationV_id" INTEGER, 
	alignment_labels TEXT, 
	PRIMARY KEY ("SequenceDelineationV_id", alignment_labels), 
	FOREIGN KEY("SequenceDelineationV_id") REFERENCES "SequenceDelineationV" (id)
);
CREATE TABLE "AlleleDescription_acknowledgements" (
	"AlleleDescription_id" INTEGER, 
	acknowledgements_id INTEGER, 
	PRIMARY KEY ("AlleleDescription_id", acknowledgements_id), 
	FOREIGN KEY("AlleleDescription_id") REFERENCES "AlleleDescription" (id), 
	FOREIGN KEY(acknowledgements_id) REFERENCES "Acknowledgement" (id)
);
CREATE TABLE "AlleleDescription_aliases" (
	"AlleleDescription_id" INTEGER, 
	aliases TEXT, 
	PRIMARY KEY ("AlleleDescription_id", aliases), 
	FOREIGN KEY("AlleleDescription_id") REFERENCES "AlleleDescription" (id)
);
CREATE TABLE "AlleleDescription_v_gene_delineations" (
	"AlleleDescription_id" INTEGER, 
	v_gene_delineations_id INTEGER, 
	PRIMARY KEY ("AlleleDescription_id", v_gene_delineations_id), 
	FOREIGN KEY("AlleleDescription_id") REFERENCES "AlleleDescription" (id), 
	FOREIGN KEY(v_gene_delineations_id) REFERENCES "SequenceDelineationV" (id)
);
CREATE TABLE "AlleleDescription_unrearranged_support" (
	"AlleleDescription_id" INTEGER, 
	unrearranged_support_id INTEGER, 
	PRIMARY KEY ("AlleleDescription_id", unrearranged_support_id), 
	FOREIGN KEY("AlleleDescription_id") REFERENCES "AlleleDescription" (id), 
	FOREIGN KEY(unrearranged_support_id) REFERENCES "UnrearrangedSequence" (id)
);
CREATE TABLE "AlleleDescription_rearranged_support" (
	"AlleleDescription_id" INTEGER, 
	rearranged_support_id INTEGER, 
	PRIMARY KEY ("AlleleDescription_id", rearranged_support_id), 
	FOREIGN KEY("AlleleDescription_id") REFERENCES "AlleleDescription" (id), 
	FOREIGN KEY(rearranged_support_id) REFERENCES "RearrangedSequence" (id)
);
CREATE TABLE "AlleleDescription_paralogs" (
	"AlleleDescription_id" INTEGER, 
	paralogs TEXT, 
	PRIMARY KEY ("AlleleDescription_id", paralogs), 
	FOREIGN KEY("AlleleDescription_id") REFERENCES "AlleleDescription" (id)
);
CREATE TABLE "AlleleDescription_curational_tags" (
	"AlleleDescription_id" INTEGER, 
	curational_tags VARCHAR(18), 
	PRIMARY KEY ("AlleleDescription_id", curational_tags), 
	FOREIGN KEY("AlleleDescription_id") REFERENCES "AlleleDescription" (id)
);
CREATE TABLE "GermlineSet_acknowledgements" (
	"GermlineSet_id" INTEGER, 
	acknowledgements_id INTEGER, 
	PRIMARY KEY ("GermlineSet_id", acknowledgements_id), 
	FOREIGN KEY("GermlineSet_id") REFERENCES "GermlineSet" (id), 
	FOREIGN KEY(acknowledgements_id) REFERENCES "Acknowledgement" (id)
);
CREATE TABLE "GermlineSet_allele_descriptions" (
	"GermlineSet_id" INTEGER, 
	allele_descriptions_id INTEGER, 
	PRIMARY KEY ("GermlineSet_id", allele_descriptions_id), 
	FOREIGN KEY("GermlineSet_id") REFERENCES "GermlineSet" (id), 
	FOREIGN KEY(allele_descriptions_id) REFERENCES "AlleleDescription" (id)
);
CREATE TABLE "GenotypeSet_genotype_class_list" (
	"GenotypeSet_id" INTEGER, 
	genotype_class_list_id INTEGER, 
	PRIMARY KEY ("GenotypeSet_id", genotype_class_list_id), 
	FOREIGN KEY("GenotypeSet_id") REFERENCES "GenotypeSet" (id), 
	FOREIGN KEY(genotype_class_list_id) REFERENCES "Genotype" (id)
);
CREATE TABLE "Genotype_documented_alleles" (
	"Genotype_id" INTEGER, 
	documented_alleles_id INTEGER, 
	PRIMARY KEY ("Genotype_id", documented_alleles_id), 
	FOREIGN KEY("Genotype_id") REFERENCES "Genotype" (id), 
	FOREIGN KEY(documented_alleles_id) REFERENCES "DocumentedAllele" (id)
);
CREATE TABLE "Genotype_undocumented_alleles" (
	"Genotype_id" INTEGER, 
	undocumented_alleles_id INTEGER, 
	PRIMARY KEY ("Genotype_id", undocumented_alleles_id), 
	FOREIGN KEY("Genotype_id") REFERENCES "Genotype" (id), 
	FOREIGN KEY(undocumented_alleles_id) REFERENCES "UndocumentedAllele" (id)
);
CREATE TABLE "Genotype_deleted_genes" (
	"Genotype_id" INTEGER, 
	deleted_genes_id INTEGER, 
	PRIMARY KEY ("Genotype_id", deleted_genes_id), 
	FOREIGN KEY("Genotype_id") REFERENCES "Genotype" (id), 
	FOREIGN KEY(deleted_genes_id) REFERENCES "DeletedGene" (id)
);
CREATE TABLE "MHCGenotypeSet_mhc_genotype_list" (
	"MHCGenotypeSet_id" INTEGER, 
	mhc_genotype_list_id INTEGER, 
	PRIMARY KEY ("MHCGenotypeSet_id", mhc_genotype_list_id), 
	FOREIGN KEY("MHCGenotypeSet_id") REFERENCES "MHCGenotypeSet" (id), 
	FOREIGN KEY(mhc_genotype_list_id) REFERENCES "MHCGenotype" (id)
);
CREATE TABLE "MHCGenotype_mhc_alleles" (
	"MHCGenotype_id" INTEGER, 
	mhc_alleles_id INTEGER, 
	PRIMARY KEY ("MHCGenotype_id", mhc_alleles_id), 
	FOREIGN KEY("MHCGenotype_id") REFERENCES "MHCGenotype" (id), 
	FOREIGN KEY(mhc_alleles_id) REFERENCES "MHCAllele" (id)
);
CREATE TABLE "Study_keywords_study" (
	"Study_id" INTEGER, 
	keywords_study VARCHAR(29), 
	PRIMARY KEY ("Study_id", keywords_study), 
	FOREIGN KEY("Study_id") REFERENCES "Study" (id)
);
CREATE TABLE "NucleicAcidProcessing_pcr_target" (
	"NucleicAcidProcessing_id" INTEGER, 
	pcr_target_id INTEGER, 
	PRIMARY KEY ("NucleicAcidProcessing_id", pcr_target_id), 
	FOREIGN KEY("NucleicAcidProcessing_id") REFERENCES "NucleicAcidProcessing" (id), 
	FOREIGN KEY(pcr_target_id) REFERENCES "PCRTarget" (id)
);
CREATE TABLE "DataProcessing_data_processing_files" (
	"DataProcessing_id" INTEGER, 
	data_processing_files TEXT, 
	PRIMARY KEY ("DataProcessing_id", data_processing_files), 
	FOREIGN KEY("DataProcessing_id") REFERENCES "DataProcessing" (id)
);
CREATE TABLE "Clone_sequences" (
	"Clone_id" INTEGER, 
	sequences TEXT, 
	PRIMARY KEY ("Clone_id", sequences), 
	FOREIGN KEY("Clone_id") REFERENCES "Clone" (id)
);
CREATE TABLE "Tree_nodes" (
	"Tree_id" INTEGER, 
	nodes_id INTEGER, 
	PRIMARY KEY ("Tree_id", nodes_id), 
	FOREIGN KEY("Tree_id") REFERENCES "Tree" (id), 
	FOREIGN KEY(nodes_id) REFERENCES "Node" (id)
);
CREATE TABLE "Cell_rearrangements" (
	"Cell_id" INTEGER, 
	rearrangements TEXT, 
	PRIMARY KEY ("Cell_id", rearrangements), 
	FOREIGN KEY("Cell_id") REFERENCES "Cell" (id)
);
CREATE TABLE "Cell_receptors" (
	"Cell_id" INTEGER, 
	receptors TEXT, 
	PRIMARY KEY ("Cell_id", receptors), 
	FOREIGN KEY("Cell_id") REFERENCES "Cell" (id)
);
CREATE TABLE "Receptor_receptor_ref" (
	"Receptor_id" INTEGER, 
	receptor_ref TEXT, 
	PRIMARY KEY ("Receptor_id", receptor_ref), 
	FOREIGN KEY("Receptor_id") REFERENCES "Receptor" (id)
);
CREATE TABLE "Participant" (
	study_arm TEXT, 
	species VARCHAR, 
	sex VARCHAR, 
	age TEXT, 
	age_unit VARCHAR, 
	age_event TEXT, 
	race TEXT, 
	ethnicity TEXT, 
	geolocation VARCHAR(24), 
	strain VARCHAR(20), 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(study_arm) REFERENCES "StudyArm" (akc_id)
);
CREATE TABLE "AntibodyAntigenComplex" (
	antibody TEXT, 
	antigen TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(antibody) REFERENCES "BCellReceptor" (akc_id), 
	FOREIGN KEY(antigen) REFERENCES "Antigen" (akc_id)
);
CREATE TABLE "Subject" (
	id INTEGER NOT NULL, 
	subject_id TEXT, 
	synthetic BOOLEAN, 
	species VARCHAR, 
	sex VARCHAR(13), 
	age_min FLOAT, 
	age_max FLOAT, 
	age_unit VARCHAR, 
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
);
CREATE TABLE "StudyEvent_study_arms" (
	"StudyEvent_akc_id" TEXT, 
	study_arms_akc_id TEXT, 
	PRIMARY KEY ("StudyEvent_akc_id", study_arms_akc_id), 
	FOREIGN KEY("StudyEvent_akc_id") REFERENCES "StudyEvent" (akc_id), 
	FOREIGN KEY(study_arms_akc_id) REFERENCES "StudyArm" (akc_id)
);
CREATE TABLE "DataTransformation_was_generated_by" (
	"DataTransformation_akc_id" TEXT, 
	was_generated_by_id INTEGER, 
	PRIMARY KEY ("DataTransformation_akc_id", was_generated_by_id), 
	FOREIGN KEY("DataTransformation_akc_id") REFERENCES "DataTransformation" (akc_id), 
	FOREIGN KEY(was_generated_by_id) REFERENCES "InputOutputDataMap" (id)
);
CREATE TABLE "RepertoireGroup_repertoires" (
	"RepertoireGroup_id" INTEGER, 
	repertoires_id INTEGER, 
	PRIMARY KEY ("RepertoireGroup_id", repertoires_id), 
	FOREIGN KEY("RepertoireGroup_id") REFERENCES "RepertoireGroup" (id), 
	FOREIGN KEY(repertoires_id) REFERENCES "RepertoireGroupDetail" (id)
);
CREATE TABLE "Receptor_reactivity_measurements" (
	"Receptor_id" INTEGER, 
	reactivity_measurements_id INTEGER, 
	PRIMARY KEY ("Receptor_id", reactivity_measurements_id), 
	FOREIGN KEY("Receptor_id") REFERENCES "Receptor" (id), 
	FOREIGN KEY(reactivity_measurements_id) REFERENCES "ReceptorReactivity" (id)
);
CREATE TABLE "SampleProcessing_pcr_target" (
	"SampleProcessing_id" INTEGER, 
	pcr_target_id INTEGER, 
	PRIMARY KEY ("SampleProcessing_id", pcr_target_id), 
	FOREIGN KEY("SampleProcessing_id") REFERENCES "SampleProcessing" (id), 
	FOREIGN KEY(pcr_target_id) REFERENCES "PCRTarget" (id)
);
CREATE TABLE "LifeEvent" (
	type TEXT, 
	participant TEXT, 
	study_event TEXT, 
	life_event_type VARCHAR, 
	geolocation VARCHAR(24), 
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
);
CREATE TABLE "Repertoire" (
	id INTEGER NOT NULL, 
	repertoire_id TEXT, 
	repertoire_name TEXT, 
	repertoire_description TEXT, 
	study_id INTEGER, 
	subject_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(study_id) REFERENCES "Study" (id), 
	FOREIGN KEY(subject_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Investigation_participants" (
	investigation_akc_id TEXT, 
	participants_akc_id TEXT, 
	PRIMARY KEY (investigation_akc_id, participants_akc_id), 
	FOREIGN KEY(investigation_akc_id) REFERENCES "Investigation" (akc_id), 
	FOREIGN KEY(participants_akc_id) REFERENCES "Participant" (akc_id)
);
CREATE TABLE "Subject_diagnosis" (
	"Subject_id" INTEGER, 
	diagnosis_id INTEGER, 
	PRIMARY KEY ("Subject_id", diagnosis_id), 
	FOREIGN KEY("Subject_id") REFERENCES "Subject" (id), 
	FOREIGN KEY(diagnosis_id) REFERENCES "Diagnosis" (id)
);
CREATE TABLE "ImmuneExposure" (
	exposure_material VARCHAR, 
	disease VARCHAR, 
	disease_stage TEXT, 
	disease_severity TEXT, 
	type TEXT, 
	participant TEXT, 
	study_event TEXT, 
	life_event_type VARCHAR, 
	geolocation VARCHAR(24), 
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
);
CREATE TABLE "Assessment" (
	life_event TEXT, 
	assessment_type TEXT, 
	target_entity_type TEXT, 
	measurement_value INTEGER, 
	measurement_unit VARCHAR, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(life_event) REFERENCES "LifeEvent" (akc_id)
);
CREATE TABLE "Specimen" (
	life_event TEXT, 
	tissue VARCHAR, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(life_event) REFERENCES "LifeEvent" (akc_id)
);
CREATE TABLE "Repertoire_sample" (
	"Repertoire_id" INTEGER, 
	sample_id INTEGER, 
	PRIMARY KEY ("Repertoire_id", sample_id), 
	FOREIGN KEY("Repertoire_id") REFERENCES "Repertoire" (id), 
	FOREIGN KEY(sample_id) REFERENCES "SampleProcessing" (id)
);
CREATE TABLE "Repertoire_data_processing" (
	"Repertoire_id" INTEGER, 
	data_processing_id INTEGER, 
	PRIMARY KEY ("Repertoire_id", data_processing_id), 
	FOREIGN KEY("Repertoire_id") REFERENCES "Repertoire" (id), 
	FOREIGN KEY(data_processing_id) REFERENCES "DataProcessing" (id)
);
CREATE TABLE "SpecimenCollection" (
	specimen TEXT, 
	type TEXT, 
	participant TEXT, 
	study_event TEXT, 
	life_event_type VARCHAR, 
	geolocation VARCHAR(24), 
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
);
CREATE TABLE "CellIsolationProcessing" (
	tissue_processing TEXT, 
	cell_subset VARCHAR, 
	cell_phenotype TEXT, 
	cell_species VARCHAR, 
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
);
CREATE TABLE "LibraryPreparationProcessing" (
	template_class VARCHAR(3), 
	template_quality TEXT, 
	template_amount FLOAT, 
	template_amount_unit VARCHAR, 
	library_generation_method VARCHAR(24), 
	library_generation_protocol TEXT, 
	library_generation_kit_version TEXT, 
	complete_sequences VARCHAR(20), 
	physical_linkage VARCHAR(16), 
	specimen TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(specimen) REFERENCES "Specimen" (akc_id)
);
CREATE TABLE "Assay" (
	repertoire_id TEXT, 
	sequencing_run_id TEXT, 
	total_reads_passing_qc_filter INTEGER, 
	sequencing_platform TEXT, 
	sequencing_facility TEXT, 
	sequencing_run_date TIMESTAMP WITHOUT TIME ZONE, 
	sequencing_kit TEXT, 
	sequencing_files_id INTEGER, 

	epitope TEXT, 
	measurement_category VARCHAR(21), 

	specimen TEXT, 
	type TEXT, 
	assay_type VARCHAR, 
	has_specified_output TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(specimen) REFERENCES "Specimen" (akc_id), 
	FOREIGN KEY(has_specified_output) REFERENCES "AKDataItem" (akc_id),
	FOREIGN KEY(sequencing_files_id) REFERENCES "SequencingData" (id),
	FOREIGN KEY(epitope) REFERENCES "Epitope" (akc_id)
);
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
	assay_type VARCHAR, 
	has_specified_output TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	sequencing_files_id INTEGER, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(specimen) REFERENCES "Specimen" (akc_id), 
	FOREIGN KEY(has_specified_output) REFERENCES "AKDataItem" (akc_id), 
	FOREIGN KEY(sequencing_files_id) REFERENCES "SequencingData" (id)
);
CREATE TABLE "TCellReceptorEpitopeBindingAssay" (
	epitope TEXT, 
	specimen TEXT, 
	type TEXT, 
	assay_type VARCHAR, 
	has_specified_output TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	measurement_category VARCHAR(21), 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(epitope) REFERENCES "Epitope" (akc_id), 
	FOREIGN KEY(specimen) REFERENCES "Specimen" (akc_id), 
	FOREIGN KEY(has_specified_output) REFERENCES "AKDataItem" (akc_id)
);
CREATE TABLE "AntibodyAntigenBindingAssay" (
	specimen TEXT, 
	type TEXT, 
	assay_type VARCHAR, 
	has_specified_output TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(specimen) REFERENCES "Specimen" (akc_id), 
	FOREIGN KEY(has_specified_output) REFERENCES "AKDataItem" (akc_id)
);
CREATE TABLE "SpecimenProcessing" (
	specimen TEXT, 
	name TEXT, 
	description TEXT, 
	akc_id TEXT NOT NULL, 
	"Assay_akc_id" TEXT, 
	"AIRRSequencingAssay_akc_id" TEXT, 
	"TCellReceptorEpitopeBindingAssay_akc_id" TEXT, 
	"AntibodyAntigenBindingAssay_akc_id" TEXT, 
	PRIMARY KEY (akc_id), 
	FOREIGN KEY(specimen) REFERENCES "Specimen" (akc_id), 
	FOREIGN KEY("Assay_akc_id") REFERENCES "Assay" (akc_id), 
	FOREIGN KEY("AIRRSequencingAssay_akc_id") REFERENCES "AIRRSequencingAssay" (akc_id), 
	FOREIGN KEY("TCellReceptorEpitopeBindingAssay_akc_id") REFERENCES "TCellReceptorEpitopeBindingAssay" (akc_id), 
	FOREIGN KEY("AntibodyAntigenBindingAssay_akc_id") REFERENCES "AntibodyAntigenBindingAssay" (akc_id)
);
CREATE TABLE "Investigation_assays" (
	investigation_akc_id TEXT, 
	assays_akc_id TEXT, 
	PRIMARY KEY (investigation_akc_id, assays_akc_id), 
	FOREIGN KEY(investigation_akc_id) REFERENCES "Investigation" (akc_id), 
	FOREIGN KEY(assays_akc_id) REFERENCES "Assay" (akc_id)
);
CREATE TABLE "LibraryPreparationProcessing_pcr_target" (
	"LibraryPreparationProcessing_akc_id" TEXT, 
	pcr_target_id INTEGER, 
	PRIMARY KEY ("LibraryPreparationProcessing_akc_id", pcr_target_id), 
	FOREIGN KEY("LibraryPreparationProcessing_akc_id") REFERENCES "LibraryPreparationProcessing" (akc_id), 
	FOREIGN KEY(pcr_target_id) REFERENCES "PCRTarget" (id)
);
CREATE TABLE "AIRRSequencingAssay_tcell_receptors" (
	"AIRRSequencingAssay_akc_id" TEXT, 
	tcell_receptors_akc_id TEXT, 
	PRIMARY KEY ("AIRRSequencingAssay_akc_id", tcell_receptors_akc_id), 
	FOREIGN KEY("AIRRSequencingAssay_akc_id") REFERENCES "AIRRSequencingAssay" (akc_id), 
	FOREIGN KEY(tcell_receptors_akc_id) REFERENCES "TCellReceptor" (akc_id)
);
CREATE TABLE "AIRRSequencingAssay_tcell_chains" (
	"AIRRSequencingAssay_akc_id" TEXT, 
	tcell_chains_akc_id TEXT, 
	PRIMARY KEY ("AIRRSequencingAssay_akc_id", tcell_chains_akc_id), 
	FOREIGN KEY("AIRRSequencingAssay_akc_id") REFERENCES "AIRRSequencingAssay" (akc_id), 
	FOREIGN KEY(tcell_chains_akc_id) REFERENCES "Chain" (akc_id)
);
CREATE TABLE "TCellReceptorEpitopeBindingAssay_tcell_receptors" (
	"TCellReceptorEpitopeBindingAssay_akc_id" TEXT, 
	tcell_receptors_akc_id TEXT, 
	PRIMARY KEY ("TCellReceptorEpitopeBindingAssay_akc_id", tcell_receptors_akc_id), 
	FOREIGN KEY("TCellReceptorEpitopeBindingAssay_akc_id") REFERENCES "TCellReceptorEpitopeBindingAssay" (akc_id), 
	FOREIGN KEY(tcell_receptors_akc_id) REFERENCES "TCellReceptor" (akc_id)
);

CREATE TABLE "Assay_tcell_receptors" (
	assay_akc_id TEXT, 
	tcell_receptors_akc_id TEXT, 
	PRIMARY KEY (assay_akc_id, tcell_receptors_akc_id), 
	FOREIGN KEY(assay_akc_id) REFERENCES "Assay" (akc_id), 
	FOREIGN KEY(tcell_receptors_akc_id) REFERENCES "TCellReceptor" (akc_id)
);

CREATE INDEX "Chain_junction_aa" ON "Chain" ("junction_aa");
CREATE INDEX "Chain_cdr3_aa" ON "Chain" ("cdr3_aa");
CREATE INDEX "Chain_aa_hash" ON "Chain" ("aa_hash");
