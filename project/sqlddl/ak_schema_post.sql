-- Post load
-- create indexes

-- Chain tables
CREATE INDEX alpha_chain_hash_infer_vdj_sequence ON "AlphaChain" ("hash_infer_vdj_sequence");
CREATE INDEX alpha_chain_hash_infer_vdj_sequence_aa ON "AlphaChain" ("hash_infer_vdj_sequence_aa");
CREATE INDEX alpha_chain_junction_aa ON "AlphaChain" ("junction_aa");
CREATE INDEX alpha_chain_v_call ON "AlphaChain" ("v_call");
CREATE INDEX alpha_chain_v_gene ON "AlphaChain" ("v_gene");
CREATE INDEX alpha_chain_v_subgroup ON "AlphaChain" ("v_subgroup");
CREATE INDEX alpha_chain_j_call ON "AlphaChain" ("j_call");
CREATE INDEX alpha_chain_j_gene ON "AlphaChain" ("j_gene");
CREATE INDEX alpha_chain_j_subgroup ON "AlphaChain" ("j_subgroup");

CREATE INDEX beta_chain_hash_infer_vdj_sequence ON "BetaChain" ("hash_infer_vdj_sequence");
CREATE INDEX beta_chain_hash_infer_vdj_sequence_aa ON "BetaChain" ("hash_infer_vdj_sequence_aa");
CREATE INDEX beta_chain_junction_aa ON "BetaChain" ("junction_aa");
CREATE INDEX beta_chain_v_call ON "BetaChain" ("v_call");
CREATE INDEX beta_chain_v_gene ON "BetaChain" ("v_gene");
CREATE INDEX beta_chain_v_subgroup ON "BetaChain" ("v_subgroup");
CREATE INDEX beta_chain_j_call ON "BetaChain" ("j_call");
CREATE INDEX beta_chain_j_gene ON "BetaChain" ("j_gene");
CREATE INDEX beta_chain_j_subgroup ON "BetaChain" ("j_subgroup");

CREATE INDEX gamma_chain_hash_infer_vdj_sequence ON "GammaChain" ("hash_infer_vdj_sequence");
CREATE INDEX gamma_chain_hash_infer_vdj_sequence_aa ON "GammaChain" ("hash_infer_vdj_sequence_aa");
CREATE INDEX gamma_chain_junction_aa ON "GammaChain" ("junction_aa");
CREATE INDEX gamma_chain_v_call ON "GammaChain" ("v_call");
CREATE INDEX gamma_chain_v_gene ON "GammaChain" ("v_gene");
CREATE INDEX gamma_chain_v_subgroup ON "GammaChain" ("v_subgroup");
CREATE INDEX gamma_chain_j_call ON "GammaChain" ("j_call");
CREATE INDEX gamma_chain_j_gene ON "GammaChain" ("j_gene");
CREATE INDEX gamma_chain_j_subgroup ON "GammaChain" ("j_subgroup");

CREATE INDEX delta_chain_hash_infer_vdj_sequence ON "DeltaChain" ("hash_infer_vdj_sequence");
CREATE INDEX delta_chain_hash_infer_vdj_sequence_aa ON "DeltaChain" ("hash_infer_vdj_sequence_aa");
CREATE INDEX delta_chain_junction_aa ON "DeltaChain" ("junction_aa");
CREATE INDEX delta_chain_v_call ON "DeltaChain" ("v_call");
CREATE INDEX delta_chain_v_gene ON "DeltaChain" ("v_gene");
CREATE INDEX delta_chain_v_subgroup ON "DeltaChain" ("v_subgroup");
CREATE INDEX delta_chain_j_call ON "DeltaChain" ("j_call");
CREATE INDEX delta_chain_j_gene ON "DeltaChain" ("j_gene");
CREATE INDEX delta_chain_j_subgroup ON "DeltaChain" ("j_subgroup");

CREATE INDEX heavy_chain_hash_infer_vdj_sequence ON "HeavyChain" ("hash_infer_vdj_sequence");
CREATE INDEX heavy_chain_hash_infer_vdj_sequence_aa ON "HeavyChain" ("hash_infer_vdj_sequence_aa");
CREATE INDEX heavy_chain_junction_aa ON "HeavyChain" ("junction_aa");
CREATE INDEX heavy_chain_v_call ON "HeavyChain" ("v_call");
CREATE INDEX heavy_chain_v_gene ON "HeavyChain" ("v_gene");
CREATE INDEX heavy_chain_v_subgroup ON "HeavyChain" ("v_subgroup");
CREATE INDEX heavy_chain_j_call ON "HeavyChain" ("j_call");
CREATE INDEX heavy_chain_j_gene ON "HeavyChain" ("j_gene");
CREATE INDEX heavy_chain_j_subgroup ON "HeavyChain" ("j_subgroup");

CREATE INDEX kappa_chain_hash_infer_vdj_sequence ON "KappaChain" ("hash_infer_vdj_sequence");
CREATE INDEX kappa_chain_hash_infer_vdj_sequence_aa ON "KappaChain" ("hash_infer_vdj_sequence_aa");
CREATE INDEX kappa_chain_junction_aa ON "KappaChain" ("junction_aa");
CREATE INDEX kappa_chain_v_call ON "KappaChain" ("v_call");
CREATE INDEX kappa_chain_v_gene ON "KappaChain" ("v_gene");
CREATE INDEX kappa_chain_v_subgroup ON "KappaChain" ("v_subgroup");
CREATE INDEX kappa_chain_j_call ON "KappaChain" ("j_call");
CREATE INDEX kappa_chain_j_gene ON "KappaChain" ("j_gene");
CREATE INDEX kappa_chain_j_subgroup ON "KappaChain" ("j_subgroup");

CREATE INDEX lambda_chain_hash_infer_vdj_sequence ON "LambdaChain" ("hash_infer_vdj_sequence");
CREATE INDEX lambda_chain_hash_infer_vdj_sequence_aa ON "LambdaChain" ("hash_infer_vdj_sequence_aa");
CREATE INDEX lambda_chain_junction_aa ON "LambdaChain" ("junction_aa");
CREATE INDEX lambda_chain_v_call ON "LambdaChain" ("v_call");
CREATE INDEX lambda_chain_v_gene ON "LambdaChain" ("v_gene");
CREATE INDEX lambda_chain_v_subgroup ON "LambdaChain" ("v_subgroup");
CREATE INDEX lambda_chain_j_call ON "LambdaChain" ("j_call");
CREATE INDEX lambda_chain_j_gene ON "LambdaChain" ("j_gene");
CREATE INDEX lambda_chain_j_subgroup ON "LambdaChain" ("j_subgroup");

-- Epitope
CREATE INDEX epitope_sequence_aa ON "Epitope" ("sequence_aa");

-- Receptor composites
CREATE INDEX assay_receptor_composites_index ON "Assay_receptor_composites" ("receptor_composites_akc_id");

CREATE INDEX ab_receptor_composites_trb_chain ON "AlphaBetaReceptorComposite" ("trb_chain");
CREATE INDEX ab_receptor_composites_tra_chain ON "AlphaBetaReceptorComposite" ("tra_chain");
CREATE INDEX ab_receptor_composites_antigen ON "AlphaBetaReceptorComposite" ("antigen");
CREATE INDEX ab_receptor_composites_epitope ON "AlphaBetaReceptorComposite" ("epitope");
CREATE INDEX ab_receptor_composites_species ON "AlphaBetaReceptorComposite" ("species");
CREATE INDEX ab_receptor_composites_mhc ON "AlphaBetaReceptorComposite" ("mhc");

CREATE INDEX pab_receptor_composites_trb_chain ON "PairedAlphaBetaReceptorComposite" ("trb_chain");
CREATE INDEX pab_receptor_composites_tra_chain ON "PairedAlphaBetaReceptorComposite" ("tra_chain");
CREATE INDEX pab_receptor_composites_antigen ON "PairedAlphaBetaReceptorComposite" ("antigen");
CREATE INDEX pab_receptor_composites_epitope ON "PairedAlphaBetaReceptorComposite" ("epitope");
CREATE INDEX pab_receptor_composites_species ON "PairedAlphaBetaReceptorComposite" ("species");
CREATE INDEX pab_receptor_composites_mhc ON "PairedAlphaBetaReceptorComposite" ("mhc");

CREATE INDEX gd_receptor_composites_trg_chain ON "GammaDeltaReceptorComposite" ("trg_chain");
CREATE INDEX gd_receptor_composites_trd_chain ON "GammaDeltaReceptorComposite" ("trd_chain");
CREATE INDEX gd_receptor_composites_antigen ON "GammaDeltaReceptorComposite" ("antigen");
CREATE INDEX gd_receptor_composites_epitope ON "GammaDeltaReceptorComposite" ("epitope");
CREATE INDEX gd_receptor_composites_species ON "GammaDeltaReceptorComposite" ("species");
CREATE INDEX gd_receptor_composites_mhc ON "GammaDeltaReceptorComposite" ("mhc");

CREATE INDEX pgd_receptor_composites_trg_chain ON "PairedGammaDeltaReceptorComposite" ("trg_chain");
CREATE INDEX pgd_receptor_composites_trd_chain ON "PairedGammaDeltaReceptorComposite" ("trd_chain");
CREATE INDEX pgd_receptor_composites_antigen ON "PairedGammaDeltaReceptorComposite" ("antigen");
CREATE INDEX pgd_receptor_composites_epitope ON "PairedGammaDeltaReceptorComposite" ("epitope");
CREATE INDEX pgd_receptor_composites_species ON "PairedGammaDeltaReceptorComposite" ("species");
CREATE INDEX pgd_receptor_composites_mhc ON "PairedGammaDeltaReceptorComposite" ("mhc");

CREATE INDEX ig_receptor_composites_igh_chain ON "BCellReceptorComposite" ("igh_chain");
CREATE INDEX ig_receptor_composites_igk_chain ON "BCellReceptorComposite" ("igk_chain");
CREATE INDEX ig_receptor_composites_igl_chain ON "BCellReceptorComposite" ("igl_chain");
CREATE INDEX ig_receptor_composites_antigen ON "BCellReceptorComposite" ("antigen");
CREATE INDEX ig_receptor_composites_epitope ON "BCellReceptorComposite" ("epitope");
CREATE INDEX ig_receptor_composites_species ON "BCellReceptorComposite" ("species");

CREATE INDEX pig_receptor_composites_igh_chain ON "PairedBCellReceptorComposite" ("igh_chain");
CREATE INDEX pig_receptor_composites_igk_chain ON "PairedBCellReceptorComposite" ("igk_chain");
CREATE INDEX pig_receptor_composites_igl_chain ON "PairedBCellReceptorComposite" ("igl_chain");
CREATE INDEX pig_receptor_composites_antigen ON "PairedBCellReceptorComposite" ("antigen");
CREATE INDEX pig_receptor_composites_epitope ON "PairedBCellReceptorComposite" ("epitope");
CREATE INDEX pig_receptor_composites_species ON "PairedBCellReceptorComposite" ("species");

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
