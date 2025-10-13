from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'ak_schema',
     'default_range': 'string',
     'description': 'Common data model schema for the AIRR Knowledge Commons',
     'id': 'https://github.com/airr-knowledge/ak-schema',
     'license': 'GNU GPL v3.0',
     'name': 'ak-schema',
     'prefixes': {'AKC': {'prefix_prefix': 'AKC',
                          'prefix_reference': 'https://airr-knowledge.org/airrkb/api/v1/id/'},
                  'APOLLO_SV': {'prefix_prefix': 'APOLLO_SV',
                                'prefix_reference': 'http://purl.obolibrary.org/obo/APOLLO_SV_'},
                  'BFO': {'prefix_prefix': 'BFO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/BFO_'},
                  'CL': {'prefix_prefix': 'CL',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/CL_'},
                  'DOID': {'prefix_prefix': 'DOID',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/DOID_'},
                  'EXO': {'prefix_prefix': 'EXO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/EXO_'},
                  'GAZ': {'prefix_prefix': 'GAZ',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/GAZ_'},
                  'GO': {'prefix_prefix': 'GO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/GO_'},
                  'IAO': {'prefix_prefix': 'IAO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/IAO_'},
                  'NCBITAXON': {'prefix_prefix': 'NCBITAXON',
                                'prefix_reference': 'http://purl.obolibrary.org/obo/NCBITaxon_'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'OBI': {'prefix_prefix': 'OBI',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OBI_'},
                  'OGMS': {'prefix_prefix': 'OGMS',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/OGMS_'},
                  'OMRSE': {'prefix_prefix': 'OMRSE',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/OMRSE_'},
                  'ONTIE': {'prefix_prefix': 'ONTIE',
                            'prefix_reference': 'https://ontology.iedb.org/ontology/ONTIE_'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'PMID': {'prefix_prefix': 'PMID',
                           'prefix_reference': 'https://pubmed.ncbi.nlm.nih.gov/'},
                  'RO': {'prefix_prefix': 'RO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/RO_'},
                  'SBO': {'prefix_prefix': 'SBO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/SBO_'},
                  'UBERON': {'prefix_prefix': 'UBERON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UBERON_'},
                  'UNIPROT': {'prefix_prefix': 'UNIPROT',
                              'prefix_reference': 'http://www.uniprot.org/uniprot/'},
                  'VO': {'prefix_prefix': 'VO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/VO_'},
                  'ak_schema': {'prefix_prefix': 'ak_schema',
                                'prefix_reference': 'https://github.com/airr-knowledge/ak-schema/'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/'},
                  'dc': {'prefix_prefix': 'dc',
                         'prefix_reference': 'http://purl.org/dc/elements/1.1/'},
                  'doi': {'prefix_prefix': 'doi',
                          'prefix_reference': 'https://www.doi.org/'},
                  'example': {'prefix_prefix': 'example',
                              'prefix_reference': 'https://example.org/'},
                  'iedb_assay': {'prefix_prefix': 'iedb_assay',
                                 'prefix_reference': 'http://www.iedb.org/assay/'},
                  'iedb_epitope': {'prefix_prefix': 'iedb_epitope',
                                   'prefix_reference': 'http://www.iedb.org/epitope/'},
                  'iedb_receptor': {'prefix_prefix': 'iedb_receptor',
                                    'prefix_reference': 'http://www.iedb.org/receptor/'},
                  'iedb_reference': {'prefix_prefix': 'iedb_reference',
                                     'prefix_reference': 'http://www.iedb.org/reference/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'shex': {'prefix_prefix': 'shex',
                           'prefix_reference': 'http://www.w3.org/ns/shex#'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://airr-knowledge.org'],
     'source_file': 'project/linkml/ak_schema.yaml',
     'title': 'AIRR Knowledge Schema',
     'types': {'boolean': {'base': 'Bool',
                           'description': 'A binary (true or false) value',
                           'exact_mappings': ['schema:Boolean'],
                           'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                           'name': 'boolean',
                           'notes': ['If you are authoring schemas in LinkML YAML, '
                                     'the type is referenced with the lower case '
                                     '"boolean".'],
                           'repr': 'bool',
                           'uri': 'xsd:boolean'},
               'curie': {'base': 'Curie',
                         'comments': ['in RDF serializations this MUST be expanded '
                                      'to a URI',
                                      'in non-RDF serializations MAY be serialized '
                                      'as the compact representation'],
                         'conforms_to': 'https://www.w3.org/TR/curie/',
                         'description': 'a compact URI',
                         'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                         'name': 'curie',
                         'notes': ['If you are authoring schemas in LinkML YAML, '
                                   'the type is referenced with the lower case '
                                   '"curie".'],
                         'repr': 'str',
                         'uri': 'xsd:string'},
               'date': {'base': 'XSDDate',
                        'description': 'a date (year, month and day) in an '
                                       'idealized calendar',
                        'exact_mappings': ['schema:Date'],
                        'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                        'name': 'date',
                        'notes': ["URI is dateTime because OWL reasoners don't "
                                  'work with straight date or time',
                                  'If you are authoring schemas in LinkML YAML, '
                                  'the type is referenced with the lower case '
                                  '"date".'],
                        'repr': 'str',
                        'uri': 'xsd:date'},
               'date_or_datetime': {'base': 'str',
                                    'description': 'Either a date or a datetime',
                                    'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                                    'name': 'date_or_datetime',
                                    'notes': ['If you are authoring schemas in '
                                              'LinkML YAML, the type is referenced '
                                              'with the lower case '
                                              '"date_or_datetime".'],
                                    'repr': 'str',
                                    'uri': 'linkml:DateOrDatetime'},
               'datetime': {'base': 'XSDDateTime',
                            'description': 'The combination of a date and time',
                            'exact_mappings': ['schema:DateTime'],
                            'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                            'name': 'datetime',
                            'notes': ['If you are authoring schemas in LinkML '
                                      'YAML, the type is referenced with the lower '
                                      'case "datetime".'],
                            'repr': 'str',
                            'uri': 'xsd:dateTime'},
               'decimal': {'base': 'Decimal',
                           'broad_mappings': ['schema:Number'],
                           'description': 'A real number with arbitrary precision '
                                          'that conforms to the xsd:decimal '
                                          'specification',
                           'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                           'name': 'decimal',
                           'notes': ['If you are authoring schemas in LinkML YAML, '
                                     'the type is referenced with the lower case '
                                     '"decimal".'],
                           'uri': 'xsd:decimal'},
               'double': {'base': 'float',
                          'close_mappings': ['schema:Float'],
                          'description': 'A real number that conforms to the '
                                         'xsd:double specification',
                          'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                          'name': 'double',
                          'notes': ['If you are authoring schemas in LinkML YAML, '
                                    'the type is referenced with the lower case '
                                    '"double".'],
                          'uri': 'xsd:double'},
               'float': {'base': 'float',
                         'description': 'A real number that conforms to the '
                                        'xsd:float specification',
                         'exact_mappings': ['schema:Float'],
                         'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                         'name': 'float',
                         'notes': ['If you are authoring schemas in LinkML YAML, '
                                   'the type is referenced with the lower case '
                                   '"float".'],
                         'uri': 'xsd:float'},
               'integer': {'base': 'int',
                           'description': 'An integer',
                           'exact_mappings': ['schema:Integer'],
                           'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                           'name': 'integer',
                           'notes': ['If you are authoring schemas in LinkML YAML, '
                                     'the type is referenced with the lower case '
                                     '"integer".'],
                           'uri': 'xsd:integer'},
               'jsonpath': {'base': 'str',
                            'conforms_to': 'https://www.ietf.org/archive/id/draft-goessner-dispatch-jsonpath-00.html',
                            'description': 'A string encoding a JSON Path. The '
                                           'value of the string MUST conform to '
                                           'JSON Point syntax and SHOULD '
                                           'dereference to zero or more valid '
                                           'objects within the current instance '
                                           'document when encoded in tree form.',
                            'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                            'name': 'jsonpath',
                            'notes': ['If you are authoring schemas in LinkML '
                                      'YAML, the type is referenced with the lower '
                                      'case "jsonpath".'],
                            'repr': 'str',
                            'uri': 'xsd:string'},
               'jsonpointer': {'base': 'str',
                               'conforms_to': 'https://datatracker.ietf.org/doc/html/rfc6901',
                               'description': 'A string encoding a JSON Pointer. '
                                              'The value of the string MUST '
                                              'conform to JSON Point syntax and '
                                              'SHOULD dereference to a valid '
                                              'object within the current instance '
                                              'document when encoded in tree form.',
                               'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                               'name': 'jsonpointer',
                               'notes': ['If you are authoring schemas in LinkML '
                                         'YAML, the type is referenced with the '
                                         'lower case "jsonpointer".'],
                               'repr': 'str',
                               'uri': 'xsd:string'},
               'ncname': {'base': 'NCName',
                          'description': 'Prefix part of CURIE',
                          'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                          'name': 'ncname',
                          'notes': ['If you are authoring schemas in LinkML YAML, '
                                    'the type is referenced with the lower case '
                                    '"ncname".'],
                          'repr': 'str',
                          'uri': 'xsd:string'},
               'nodeidentifier': {'base': 'NodeIdentifier',
                                  'description': 'A URI, CURIE or BNODE that '
                                                 'represents a node in a model.',
                                  'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                                  'name': 'nodeidentifier',
                                  'notes': ['If you are authoring schemas in '
                                            'LinkML YAML, the type is referenced '
                                            'with the lower case '
                                            '"nodeidentifier".'],
                                  'repr': 'str',
                                  'uri': 'shex:nonLiteral'},
               'objectidentifier': {'base': 'ElementIdentifier',
                                    'comments': ['Used for inheritance and type '
                                                 'checking'],
                                    'description': 'A URI or CURIE that represents '
                                                   'an object in the model.',
                                    'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                                    'name': 'objectidentifier',
                                    'notes': ['If you are authoring schemas in '
                                              'LinkML YAML, the type is referenced '
                                              'with the lower case '
                                              '"objectidentifier".'],
                                    'repr': 'str',
                                    'uri': 'shex:iri'},
               'sparqlpath': {'base': 'str',
                              'conforms_to': 'https://www.w3.org/TR/sparql11-query/#propertypaths',
                              'description': 'A string encoding a SPARQL Property '
                                             'Path. The value of the string MUST '
                                             'conform to SPARQL syntax and SHOULD '
                                             'dereference to zero or more valid '
                                             'objects within the current instance '
                                             'document when encoded as RDF.',
                              'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                              'name': 'sparqlpath',
                              'notes': ['If you are authoring schemas in LinkML '
                                        'YAML, the type is referenced with the '
                                        'lower case "sparqlpath".'],
                              'repr': 'str',
                              'uri': 'xsd:string'},
               'string': {'base': 'str',
                          'description': 'A character string',
                          'exact_mappings': ['schema:Text'],
                          'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                          'name': 'string',
                          'notes': ['In RDF serializations, a slot with range of '
                                    'string is treated as a literal or type '
                                    'xsd:string.   If you are authoring schemas in '
                                    'LinkML YAML, the type is referenced with the '
                                    'lower case "string".'],
                          'uri': 'xsd:string'},
               'time': {'base': 'XSDTime',
                        'description': 'A time object represents a (local) time of '
                                       'day, independent of any particular day',
                        'exact_mappings': ['schema:Time'],
                        'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                        'name': 'time',
                        'notes': ['URI is dateTime because OWL reasoners do not '
                                  'work with straight date or time',
                                  'If you are authoring schemas in LinkML YAML, '
                                  'the type is referenced with the lower case '
                                  '"time".'],
                        'repr': 'str',
                        'uri': 'xsd:time'},
               'uri': {'base': 'URI',
                       'close_mappings': ['schema:URL'],
                       'comments': ['in RDF serializations a slot with range of '
                                    'uri is treated as a literal or type '
                                    'xsd:anyURI unless it is an identifier or a '
                                    'reference to an identifier, in which case it '
                                    'is translated directly to a node'],
                       'conforms_to': 'https://www.ietf.org/rfc/rfc3987.txt',
                       'description': 'a complete URI',
                       'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                       'name': 'uri',
                       'notes': ['If you are authoring schemas in LinkML YAML, the '
                                 'type is referenced with the lower case "uri".'],
                       'repr': 'str',
                       'uri': 'xsd:anyURI'},
               'uriorcurie': {'base': 'URIorCURIE',
                              'description': 'a URI or a CURIE',
                              'from_schema': 'https://github.com/airr-knowledge/ak-schema',
                              'name': 'uriorcurie',
                              'notes': ['If you are authoring schemas in LinkML '
                                        'YAML, the type is referenced with the '
                                        'lower case "uriorcurie".'],
                              'repr': 'str',
                              'uri': 'xsd:anyURI'}}} )

class InvestigationTypeOntology(str):
    pass


class BiologicalSexOntology(str):
    pass


class RaceOntology(str, Enum):
    American_Indian_or_Alaska_Native = "American Indian or Alaska Native"
    Asian = "Asian"
    Black_or_African_American = "Black or African American"
    Native_Hawaiian_or_Other_Pacific_Islander = "Native Hawaiian or Other Pacific Islander"
    White = "White"
    Other = "Other"
    raceCOLON_not_specified = "race: not specified"
    raceCOLON_other = "race: other"
    raceCOLON_unknown = "race: unknown"
    African_American = "African American"
    Asian_or_Pacific_Islander = "Asian or Pacific Islander"
    Black = "Black"
    Brazilian = "Brazilian"
    Chinese = "Chinese"
    GermanSOLIDUSEast_Indian = "German/East Indian"
    Hispanic_or_Latino = "Hispanic or Latino"
    Hispanic = "Hispanic"
    Indian = "Indian"
    Indian__Irish__French__polish = "Indian- Irish- French- polish"
    Korean = "Korean"
    Middle_Eastern_European = "Middle Eastern European"
    Middle_Eastern = "Middle Eastern"
    Mixed_racial_group = "Mixed racial group"
    Mixed = "Mixed"
    NR = "NR"
    Native_American_or_Alaska_Native = "Native American or Alaska Native"
    Native = "Native"
    Unknown_racial_group = "Unknown racial group"
    White_Asian = "White, Asian"
    White_Asian_Black = "White, Asian, Black"
    White_Caucasian = "White, Caucasian"
    White_British = "White-British"


class EthnicityOntology(str, Enum):
    Hispanic_or_Latino = "Hispanic or Latino"
    Not_Hispanic_or_Latino = "Not Hispanic or Latino"
    Other = "Other"
    ethnicityCOLON_not_specified = "ethnicity: not specified"
    ethnicityCOLON_other = "ethnicity: other"
    African = "African"
    African_American = "African-American"
    Arab = "Arab"
    Arabigan = "Arabigan"
    Asian = "Asian"
    Black_or_Black_British___African = "Black or Black British - African"
    Black = "Black"
    Caucasian = "Caucasian"
    Declined = "Declined"
    Han = "Han"
    Hispanic = "Hispanic"
    Italian = "Italian"
    Latin = "Latin"
    NR = "NR"
    Non_Hispanic_or_Latino = "Non-Hispanic or Latino"
    Non_Hispanic = "Non-Hispanic"
    Other___Not_Stated = "Other - Not Stated"
    SE_Asian = "SE Asian"
    Unknown_Ethnicity = "Unknown Ethnicity"
    White = "White"


class GeolocationOntology(str, Enum):
    USCOLON_New_York = "US: New York"
    USCOLON_California = "US: California"
    USCOLON_Connecticut = "US: Connecticut"
    USCOLON_Georgia = "US: Georgia"
    USCOLON_Texas = "US: Texas"
    Canada = "Canada"
    Nicaragua = "Nicaragua"
    USCOLON_Maryland = "US: Maryland"
    USCOLON_Minnesota = "US: Minnesota"
    United_States_of_America = "United States of America"
    Uganda = "Uganda"
    China = "China"
    England = "England"
    India = "India"
    USCOLON_Massachusetts = "US: Massachusetts"
    USCOLON_Colorado = "US: Colorado"
    Gambia = "Gambia"
    Papua_New_Guinea = "Papua New Guinea"
    Metropolitan_France = "Metropolitan France"
    Sri_Lanka = "Sri Lanka"
    Switzerland = "Switzerland"
    USCOLON_Washington = "US: Washington"
    geographic_location = "geographic location"
    Colombia = "Colombia"
    USCOLON_Florida = "US: Florida"
    USCOLON_Kansas = "US: Kansas"


class StrainEnum(str, Enum):
    number_1D2beta = "1D2beta"
    BALBSOLIDUScByJ = "BALB/cByJ"
    BalbSOLIDUSc = "Balb/c"
    C57BLSOLIDUS6 = "C57BL/6"
    C57BLSOLIDUS6J = "C57BL/6J"
    JHD_SOLIDUS__MRLSOLIDUSMpJ_Faslp = "JHD-/- MRL/MpJ-Faslp"
    LDLRPLUS_SIGNSOLIDUSPLUS_SIGN = "LDLR+/+"
    LDLR_SOLIDUS_ = "LDLR-/-"
    pet_shop_mouse = "pet shop mouse"


class LifeEventProcessOntology(str):
    pass


class ExposureMaterialOntology(str):
    pass


class DiseaseOntology(str):
    pass


class DiseaseStageOntology(str, Enum):
    acute_disease_course = "acute disease course"
    post_disease_course = "post disease course"
    unknown_disease_course = "unknown disease course"
    chronic_disease_course = "chronic disease course"
    other_disease_course = "other disease course"


class AssayTypeOntology(str):
    pass


class MeasurementUnitOntology(str):
    pass


class CategoricalSpecificityEnum(str, Enum):
    Positive = "Positive"
    Negative = "Negative"
    Positive_Low = "Positive-Low"
    Positive_High = "Positive-High"
    Positive_Intermediate = "Positive-Intermediate"


class DataItemTypeEnum(str, Enum):
    sequence_reads = "sequence_reads"
    sequence_quality = "sequence_quality"
    sequence_forward_paired_reads = "sequence_forward_paired_reads"
    sequence_reverse_paired_reads = "sequence_reverse_paired_reads"
    sequence = "sequence"
    primer_sequence = "primer_sequence"
    forward_primer_sequence = "forward_primer_sequence"
    reverse_primer_sequence = "reverse_primer_sequence"
    barcode_sequence = "barcode_sequence"
    vdj_sequence_annotation = "vdj_sequence_annotation"
    quality_statistics = "quality_statistics"
    annotation_statistics = "annotation_statistics"
    assigned_clones = "assigned_clones"
    physiochemical_annotation = "physiochemical_annotation"
    gene_usage = "gene_usage"
    gene_combo_usage = "gene_combo_usage"
    length_distribution = "length_distribution"
    diversity_profile = "diversity_profile"
    mutational_profile = "mutational_profile"
    similarity_comparison = "similarity_comparison"
    study_arm_comparison = "study_arm_comparison"
    archive = "archive"
    compressed = "compressed"


class DataTransformationTypeEnum(str, Enum):
    merge_reads = "merge_reads"
    barcode_matching = "barcode_matching"
    primer_matching = "primer_matching"
    length_filter = "length_filter"
    quality_filter = "quality_filter"
    homopolymer_filter = "homopolymer_filter"
    collapse_unique_sequences = "collapse_unique_sequences"
    vdj_annotation = "vdj_annotation"
    clonal_assignment = "clonal_assignment"
    germline_allele_inference = "germline_allele_inference"
    gene_usage = "gene_usage"
    gene_combo_usage = "gene_combo_usage"
    length_distribution = "length_distribution"
    diversity = "diversity"
    observed_mutations = "observed_mutations"


class AKFileFormatEnum(str, Enum):
    tsv = "tsv"
    csv = "csv"
    json = "json"
    jsonl = "jsonl"
    airr_tsv = "airr_tsv"
    airr_json = "airr_json"
    airr_jsonl = "airr_jsonl"


class ChainSimilarityTypeEnum(str, Enum):
    exact_match = "exact_match"
    exact_aa_match = "exact_aa_match"
    cdr3_exact_match = "cdr3_exact_match"
    cdr3_exact_aa_match = "cdr3_exact_aa_match"
    cdr3_exact_aa_and_vj_match = "cdr3_exact_aa_and_vj_match"


class TimePointUnitOntology(str):
    pass


class DerivationEnum(str, Enum):
    DNA = "DNA"
    RNA = "RNA"


class ObservationTypeEnum(str, Enum):
    direct_sequencing = "direct_sequencing"
    inference_from_repertoire = "inference_from_repertoire"


class StrandEnum(str, Enum):
    PLUS_SIGN = "+"
    _ = "-"


class LocusEnum(str, Enum):
    IGH = "IGH"
    IGI = "IGI"
    IGK = "IGK"
    IGL = "IGL"
    TRA = "TRA"
    TRB = "TRB"
    TRG = "TRG"
    TRD = "TRD"


class SequenceTypeEnum(str, Enum):
    V = "V"
    D = "D"
    J = "J"
    C = "C"


class InferenceTypeEnum(str, Enum):
    genomic_and_rearranged = "genomic_and_rearranged"
    genomic_only = "genomic_only"
    rearranged_only = "rearranged_only"


class SpeciesOntology(str):
    pass


class SpeciesSubgroupTypeEnum(str, Enum):
    breed = "breed"
    strain = "strain"
    inbred = "inbred"
    outbred = "outbred"
    locational = "locational"


class StatusEnum(str, Enum):
    active = "active"
    draft = "draft"
    retired = "retired"
    withdrawn = "withdrawn"


class JCodonFrameEnum(str, Enum):
    number_1 = "1"
    number_2 = "2"
    number_3 = "3"


class CurationalTagsEnum(str, Enum):
    likely_truncated = "likely_truncated"
    likely_full_length = "likely_full_length"


class InferenceProcessEnum(str, Enum):
    genomic_sequencing = "genomic_sequencing"
    repertoire_sequencing = "repertoire_sequencing"


class MhcClassEnum(str, Enum):
    MHC_I = "MHC-I"
    MHC_II = "MHC-II"
    MHC_nonclassical = "MHC-nonclassical"


class GeneOntology(str):
    pass


class StudyTypeOntology(str):
    pass


class KeywordsStudyEnum(str, Enum):
    contains_ig = "contains_ig"
    contains_tr = "contains_tr"
    contains_paired_chain = "contains_paired_chain"
    contains_schema_rearrangement = "contains_schema_rearrangement"
    contains_schema_clone = "contains_schema_clone"
    contains_schema_cell = "contains_schema_cell"
    contains_schema_receptor = "contains_schema_receptor"


class SexEnum(str, Enum):
    male = "male"
    female = "female"
    pooled = "pooled"
    hermaphrodite = "hermaphrodite"
    intersex = "intersex"


class AgeUnitOntology(str):
    pass


class DiseaseDiagnosisOntology(str):
    pass


class TissueOntology(str):
    pass


class CollectionTimePointRelativeUnitOntology(str):
    pass


class CellSubsetOntology(str):
    pass


class CellSpeciesOntology(str):
    pass


class PcrTargetLocusEnum(str, Enum):
    IGH = "IGH"
    IGI = "IGI"
    IGK = "IGK"
    IGL = "IGL"
    TRA = "TRA"
    TRB = "TRB"
    TRD = "TRD"
    TRG = "TRG"


class TemplateClassEnum(str, Enum):
    DNA = "DNA"
    RNA = "RNA"


class TemplateAmountUnitOntology(str):
    pass


class LibraryGenerationMethodEnum(str, Enum):
    PCR = "PCR"
    RTLEFT_PARENTHESISRHPRIGHT_PARENTHESISPLUS_SIGNPCR = "RT(RHP)+PCR"
    RTLEFT_PARENTHESISoligo_dTRIGHT_PARENTHESISPLUS_SIGNPCR = "RT(oligo-dT)+PCR"
    RTLEFT_PARENTHESISoligo_dTRIGHT_PARENTHESISPLUS_SIGNTSPLUS_SIGNPCR = "RT(oligo-dT)+TS+PCR"
    RTLEFT_PARENTHESISoligo_dTRIGHT_PARENTHESISPLUS_SIGNTSLEFT_PARENTHESISUMIRIGHT_PARENTHESISPLUS_SIGNPCR = "RT(oligo-dT)+TS(UMI)+PCR"
    RTLEFT_PARENTHESISspecificRIGHT_PARENTHESISPLUS_SIGNPCR = "RT(specific)+PCR"
    RTLEFT_PARENTHESISspecificRIGHT_PARENTHESISPLUS_SIGNTSPLUS_SIGNPCR = "RT(specific)+TS+PCR"
    RTLEFT_PARENTHESISspecificRIGHT_PARENTHESISPLUS_SIGNTSLEFT_PARENTHESISUMIRIGHT_PARENTHESISPLUS_SIGNPCR = "RT(specific)+TS(UMI)+PCR"
    RTLEFT_PARENTHESISspecificPLUS_SIGNUMIRIGHT_PARENTHESISPLUS_SIGNPCR = "RT(specific+UMI)+PCR"
    RTLEFT_PARENTHESISspecificPLUS_SIGNUMIRIGHT_PARENTHESISPLUS_SIGNTSPLUS_SIGNPCR = "RT(specific+UMI)+TS+PCR"
    RTLEFT_PARENTHESISspecificRIGHT_PARENTHESISPLUS_SIGNTS = "RT(specific)+TS"
    other = "other"


class CompleteSequencesEnum(str, Enum):
    partial = "partial"
    complete = "complete"
    completePLUS_SIGNuntemplated = "complete+untemplated"
    mixed = "mixed"


class PhysicalLinkageEnum(str, Enum):
    none = "none"
    hetero_head_head = "hetero_head-head"
    hetero_tail_head = "hetero_tail-head"
    hetero_prelinked = "hetero_prelinked"


class FileTypeEnum(str, Enum):
    fasta = "fasta"
    fastq = "fastq"


class ReadDirectionEnum(str, Enum):
    forward = "forward"
    reverse = "reverse"
    mixed = "mixed"


class PairedReadDirectionEnum(str, Enum):
    forward = "forward"
    reverse = "reverse"
    mixed = "mixed"


class ExpressionStudyMethodEnum(str, Enum):
    flow_cytometry = "flow_cytometry"
    single_cell_transcriptome = "single-cell_transcriptome"


class ReceptorTypeEnum(str, Enum):
    Ig = "Ig"
    TCR = "TCR"


class ReceptorVariableDomain1LocusEnum(str, Enum):
    IGH = "IGH"
    TRB = "TRB"
    TRD = "TRD"


class ReceptorVariableDomain2LocusEnum(str, Enum):
    IGI = "IGI"
    IGK = "IGK"
    IGL = "IGL"
    TRA = "TRA"
    TRG = "TRG"


class LigandTypeEnum(str, Enum):
    MHCCOLONpeptide = "MHC:peptide"
    MHCCOLONnon_peptide = "MHC:non-peptide"
    protein = "protein"
    peptide = "peptide"
    non_peptidic = "non-peptidic"


class AntigenTypeEnum(str, Enum):
    protein = "protein"
    peptide = "peptide"
    non_peptidic = "non-peptidic"


class AntigenSourceSpeciesOntology(str):
    pass


class MhcGene1Ontology(str):
    pass


class MhcGene2Ontology(str):
    pass


class ReactivityMethodEnum(str, Enum):
    SPR = "SPR"
    ITC = "ITC"
    ELISA = "ELISA"
    cytometry = "cytometry"
    biological_activity = "biological_activity"


class ReactivityReadoutEnum(str, Enum):
    binding_strength = "binding_strength"
    cytokine_release = "cytokine_release"
    dissociation_constant_kd = "dissociation_constant_kd"
    on_rate = "on_rate"
    off_rate = "off_rate"
    pathogen_inhibition = "pathogen_inhibition"



class AKObject(ConfiguredBaseModel):
    """
    Anything uniquely identifiable in the AKC.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class ForeignObject(ConfiguredBaseModel):
    """
    An object held outside of the AK.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    source_uri: str = Field(default=..., description="""AKC reference to a foreign thing.""", json_schema_extra = { "linkml_meta": {'alias': 'source_uri',
         'domain_of': ['ForeignObject'],
         'slot_uri': 'schema:identifier'} })


class AIRRStandards(ConfiguredBaseModel):
    """
    An object directly converted from the AIRR schema.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    pass


class AIRRStandardsV1p5(ConfiguredBaseModel):
    """
    An object directly converted from AIRR schema version 1.5.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    pass


class AIRRStandardsV2p0(ConfiguredBaseModel):
    """
    An object directly converted from AIRR schema version 2.0.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    pass


class NamedThing(AKObject):
    """
    Name and description for AKC things.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class Process(NamedThing):
    """
    A generic process.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'BFO:0000015',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class PlanSpecification(NamedThing):
    """
    A plan with specified actions to meet some objectives.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class AIRRKnowledgeCommons(ConfiguredBaseModel):
    """
    A container for instances of multiple classes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema',
         'tree_root': True})

    investigations: Optional[dict[str, Investigation]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'investigations',
         'domain_of': ['AIRRKnowledgeCommons', 'Reference', 'Conclusion']} })
    references: Optional[dict[str, Reference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['AIRRKnowledgeCommons']} })
    study_arms: Optional[dict[str, StudyArm]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'study_arms', 'domain_of': ['AIRRKnowledgeCommons', 'StudyEvent']} })
    study_events: Optional[dict[str, StudyEvent]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'study_events', 'domain_of': ['AIRRKnowledgeCommons']} })
    participants: Optional[dict[str, Participant]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'participants',
         'domain_of': ['AIRRKnowledgeCommons', 'Investigation']} })
    life_events: Optional[dict[str, Union[LifeEvent,ImmuneExposure,SpecimenCollection]]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'life_events', 'domain_of': ['AIRRKnowledgeCommons']} })
    immune_exposures: Optional[dict[str, ImmuneExposure]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'immune_exposures', 'domain_of': ['AIRRKnowledgeCommons']} })
    assessments: Optional[dict[str, Assessment]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'assessments', 'domain_of': ['AIRRKnowledgeCommons']} })
    specimens: Optional[dict[str, Specimen]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'specimens', 'domain_of': ['AIRRKnowledgeCommons']} })
    specimen_collections: Optional[dict[str, SpecimenCollection]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'specimen_collections', 'domain_of': ['AIRRKnowledgeCommons']} })
    specimen_processings: Optional[dict[str, SpecimenProcessing]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'specimen_processings', 'domain_of': ['AIRRKnowledgeCommons']} })
    assays: Optional[dict[str, Union[Assay,AIRRSequencingAssay,TCellReceptorEpitopeBindingAssay,AntibodyAntigenBindingAssay]]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'assays', 'domain_of': ['AIRRKnowledgeCommons', 'Investigation']} })
    datasets: Optional[dict[str, AKDataSet]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'datasets', 'domain_of': ['AIRRKnowledgeCommons', 'Conclusion']} })
    sequence_data: Optional[dict[str, Union[SequenceData,AIRRSequencingData,RNATranscriptomeData]]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sequence_data', 'domain_of': ['AIRRKnowledgeCommons']} })
    conclusions: Optional[dict[str, Conclusion]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'conclusions', 'domain_of': ['AIRRKnowledgeCommons', 'Investigation']} })
    chains: Optional[dict[str, Chain]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'chains', 'domain_of': ['AIRRKnowledgeCommons']} })
    ab_tcell_receptors: Optional[dict[str, AlphaBetaTCR]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'ab_tcell_receptors', 'domain_of': ['AIRRKnowledgeCommons']} })
    gd_tcell_receptors: Optional[dict[str, GammaDeltaTCR]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'gd_tcell_receptors', 'domain_of': ['AIRRKnowledgeCommons']} })
    bcell_receptors: Optional[dict[str, BCellReceptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'bcell_receptors', 'domain_of': ['AIRRKnowledgeCommons']} })
    epitopes: Optional[dict[str, Union[Epitope,PeptidicEpitope]]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'epitopes', 'domain_of': ['AIRRKnowledgeCommons']} })


class Investigation(Process):
    """
    A scientific investigation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0000066',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    investigation_type: Optional[InvestigationTypeOntology] = Field(default=None, description="""Type of study design""", json_schema_extra = { "linkml_meta": {'alias': 'investigation_type', 'domain_of': ['Investigation']} })
    archival_id: Optional[str] = Field(default=None, description="""Identifier for external archival resource for the investigation, e.g., BioProject""", json_schema_extra = { "linkml_meta": {'alias': 'archival_id',
         'domain_of': ['Investigation'],
         'slot_uri': 'schema:identifier'} })
    inclusion_exclusion_criteria: Optional[str] = Field(default=None, description="""List of criteria for inclusion/exclusion for the study""", json_schema_extra = { "linkml_meta": {'alias': 'inclusion_exclusion_criteria',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Investigation', 'Study']} })
    release_date: Optional[datetime ] = Field(default=None, description="""Date of this release""", json_schema_extra = { "linkml_meta": {'alias': 'release_date',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Investigation', 'AlleleDescription', 'GermlineSet']} })
    update_date: Optional[datetime ] = Field(default=None, description="""Subsequence updates to the investigation or its data""", json_schema_extra = { "linkml_meta": {'alias': 'update_date', 'domain_of': ['Investigation']} })
    participants: Optional[list[str]] = Field(default=None, description="""The participants involved with the investigation""", json_schema_extra = { "linkml_meta": {'alias': 'participants',
         'domain_of': ['AIRRKnowledgeCommons', 'Investigation'],
         'slot_uri': 'RO:0000057'} })
    assays: Optional[list[str]] = Field(default=None, description="""The assays performed by the investigation""", json_schema_extra = { "linkml_meta": {'alias': 'assays', 'domain_of': ['AIRRKnowledgeCommons', 'Investigation']} })
    simulations: Optional[list[str]] = Field(default=None, description="""The simulations performed by the investigation""", json_schema_extra = { "linkml_meta": {'alias': 'simulations', 'domain_of': ['Investigation']} })
    documents: Optional[list[str]] = Field(default=None, description="""The documents produced by the investigation""", json_schema_extra = { "linkml_meta": {'alias': 'documents', 'domain_of': ['Investigation']} })
    conclusions: Optional[list[str]] = Field(default=None, description="""The conclusions from the investigation""", json_schema_extra = { "linkml_meta": {'alias': 'conclusions', 'domain_of': ['AIRRKnowledgeCommons', 'Investigation']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class Reference(ForeignObject):
    """
    A document about an investigation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'IAO:0000310',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    sources: Optional[list[str]] = Field(default=None, description="""The source URLs for a reference""", json_schema_extra = { "linkml_meta": {'alias': 'sources',
         'domain_of': ['Reference'],
         'slot_uri': 'schema:identifier'} })
    investigations: Optional[list[str]] = Field(default=None, description="""The investigations that a reference or conclusion are about""", json_schema_extra = { "linkml_meta": {'alias': 'investigations',
         'domain_of': ['AIRRKnowledgeCommons', 'Reference', 'Conclusion'],
         'slot_uri': 'IAO:0000136'} })
    title: Optional[str] = Field(default=None, description="""The title of a reference""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['Reference'], 'slot_uri': 'schema:name'} })
    authors: Optional[list[str]] = Field(default=None, description="""The authors of a reference""", json_schema_extra = { "linkml_meta": {'alias': 'authors', 'domain_of': ['Reference'], 'slot_uri': 'schema:author'} })
    journal: Optional[str] = Field(default=None, description="""The journal in which a reference was published""", json_schema_extra = { "linkml_meta": {'alias': 'journal', 'domain_of': ['Reference']} })
    issue: Optional[str] = Field(default=None, description="""The issue of the journal in which a reference was published""", json_schema_extra = { "linkml_meta": {'alias': 'issue', 'domain_of': ['Reference'], 'slot_uri': 'schema:issueNumber'} })
    month: Optional[str] = Field(default=None, description="""The month of the issue of the journal in which a reference was published""", json_schema_extra = { "linkml_meta": {'alias': 'month', 'domain_of': ['Reference']} })
    year: Optional[int] = Field(default=None, description="""The year of the issue of the journal in which a reference was published""", json_schema_extra = { "linkml_meta": {'alias': 'year', 'domain_of': ['Reference']} })
    pages: Optional[str] = Field(default=None, description="""The pages of the issue of the journal in which a reference was published""", json_schema_extra = { "linkml_meta": {'alias': 'pages', 'domain_of': ['Reference']} })
    source_uri: str = Field(default=..., description="""AKC reference to a foreign thing.""", json_schema_extra = { "linkml_meta": {'alias': 'source_uri',
         'domain_of': ['ForeignObject'],
         'slot_uri': 'schema:identifier'} })

    @field_validator('year')
    def pattern_year(cls, v):
        pattern=re.compile(r"19\d\d|20\d\d")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid year format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid year format: {v}"
            raise ValueError(err_msg)
        return v


class StudyArm(NamedThing):
    """
    A population of participants of an investigation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0000181',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    investigation: Optional[str] = Field(default=None, description="""An investigation in which the study arm participates""", json_schema_extra = { "linkml_meta": {'alias': 'investigation', 'domain_of': ['StudyArm'], 'slot_uri': 'RO:0000056'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class Participant(NamedThing):
    """
    A participant in an investigation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0100026',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema',
         'slot_usage': {'sex': {'name': 'sex', 'range': 'BiologicalSexOntology'}}})

    study_arm: Optional[str] = Field(default=None, description="""The study arm that a participant is a member of""", json_schema_extra = { "linkml_meta": {'alias': 'study_arm', 'domain_of': ['Participant'], 'slot_uri': 'RO:0002350'} })
    species: Optional[SpeciesOntology] = Field(default=None, description="""Binomial designation of subject's species""", json_schema_extra = { "linkml_meta": {'alias': 'species',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Participant',
                       'Chain',
                       'AlleleDescription',
                       'GermlineSet',
                       'Subject']} })
    sex: Optional[BiologicalSexOntology] = Field(default=None, description="""Biological sex of subject""", json_schema_extra = { "linkml_meta": {'alias': 'sex',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Participant', 'Subject']} })
    age: Optional[str] = Field(default=None, description="""The age of a participant relative to age_event""", json_schema_extra = { "linkml_meta": {'alias': 'age', 'domain_of': ['Participant']} })
    age_unit: Optional[AgeUnitOntology] = Field(default=None, description="""Unit of age range""", json_schema_extra = { "linkml_meta": {'alias': 'age_unit',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Participant', 'Subject']} })
    age_event: Optional[str] = Field(default=None, description="""Event in the study schedule to which `Age` refers. For NCBI BioSample this MUST be `sampling`. For other implementations submitters need to be aware that there is currently no mechanism to encode to potential delta between `Age event` and `Sample collection time`, hence the chosen events should be in temporal proximity.""", json_schema_extra = { "linkml_meta": {'alias': 'age_event',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Participant', 'Subject']} })
    race: Optional[str] = Field(default=None, description="""Racial group of subject (as defined by NIH)""", json_schema_extra = { "linkml_meta": {'alias': 'race',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Participant', 'Subject']} })
    ethnicity: Optional[str] = Field(default=None, description="""Ethnic group of subject (defined as cultural/language-based membership)""", json_schema_extra = { "linkml_meta": {'alias': 'ethnicity',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Participant', 'Subject']} })
    geolocation: Optional[GeolocationOntology] = Field(default=None, description="""The geolocation of a participant at birth""", json_schema_extra = { "linkml_meta": {'alias': 'geolocation',
         'domain_of': ['Participant', 'LifeEvent'],
         'slot_uri': 'RO:0001025'} })
    strain: Optional[StrainEnum] = Field(default=None, description="""The strain of the participant (non-human study participants)""", json_schema_extra = { "linkml_meta": {'alias': 'strain', 'domain_of': ['Participant']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class StudyEvent(Process):
    """
    An event that is part of the study design of an investigation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'BFO:0000015',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    study_arms: Optional[list[str]] = Field(default=None, description="""The study arms that are relevant for a study event""", json_schema_extra = { "linkml_meta": {'alias': 'study_arms', 'domain_of': ['AIRRKnowledgeCommons', 'StudyEvent']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class LifeEvent(Process):
    """
    An event in which a study participant participates.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    type: Literal["LifeEvent"] = Field(default="LifeEvent", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['LifeEvent', 'Assay', 'AKDataItem', 'TCellReceptor', 'Epitope']} })
    participant: Optional[str] = Field(default=None, description="""The participant of a life event""", json_schema_extra = { "linkml_meta": {'alias': 'participant', 'domain_of': ['LifeEvent'], 'slot_uri': 'RO:0000057'} })
    study_event: Optional[str] = Field(default=None, description="""The study event corresponding to a life event""", json_schema_extra = { "linkml_meta": {'alias': 'study_event', 'domain_of': ['LifeEvent']} })
    life_event_type: Optional[LifeEventProcessOntology] = Field(default=None, description="""The specific type of a life event""", json_schema_extra = { "linkml_meta": {'alias': 'life_event_type', 'domain_of': ['LifeEvent'], 'slot_uri': 'rdf:type'} })
    geolocation: Optional[GeolocationOntology] = Field(default=None, description="""The geolocation of a participant at birth""", json_schema_extra = { "linkml_meta": {'alias': 'geolocation',
         'domain_of': ['Participant', 'LifeEvent'],
         'slot_uri': 'RO:0001025'} })
    t0_event: Optional[str] = Field(default=None, description="""The T0 event used to specify the time of this life event""", json_schema_extra = { "linkml_meta": {'alias': 't0_event', 'domain_of': ['LifeEvent']} })
    start: Optional[Decimal] = Field(default=None, description="""The start time of this life event, relative to the T0 event""", json_schema_extra = { "linkml_meta": {'alias': 'start', 'domain_of': ['LifeEvent']} })
    duration: Optional[Decimal] = Field(default=None, description="""The duration of this life event""", json_schema_extra = { "linkml_meta": {'alias': 'duration', 'domain_of': ['LifeEvent']} })
    time_unit: Optional[str] = Field(default=None, description="""The time unit used to measure the start and duration of this life event""", json_schema_extra = { "linkml_meta": {'alias': 'time_unit', 'domain_of': ['LifeEvent']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class ImmuneExposure(LifeEvent):
    """
    An event involving the immune system of a study participant.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    exposure_material: Optional[ExposureMaterialOntology] = Field(default=None, description="""The material relevant to an immune exposure""", json_schema_extra = { "linkml_meta": {'alias': 'exposure_material',
         'domain_of': ['ImmuneExposure'],
         'slot_uri': 'RO:0000057'} })
    disease: Optional[DiseaseOntology] = Field(default=None, description="""The disease relevant to an immune exposure""", json_schema_extra = { "linkml_meta": {'alias': 'disease', 'domain_of': ['ImmuneExposure']} })
    disease_stage: Optional[str] = Field(default=None, description="""Stage of disease at current intervention""", json_schema_extra = { "linkml_meta": {'alias': 'disease_stage',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['ImmuneExposure', 'Diagnosis']} })
    disease_severity: Optional[str] = Field(default=None, description="""The severity of the disease relevant to an immune exposure""", json_schema_extra = { "linkml_meta": {'alias': 'disease_severity', 'domain_of': ['ImmuneExposure']} })
    type: Literal["ImmuneExposure"] = Field(default="ImmuneExposure", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['LifeEvent', 'Assay', 'AKDataItem', 'TCellReceptor', 'Epitope']} })
    participant: Optional[str] = Field(default=None, description="""The participant of a life event""", json_schema_extra = { "linkml_meta": {'alias': 'participant', 'domain_of': ['LifeEvent'], 'slot_uri': 'RO:0000057'} })
    study_event: Optional[str] = Field(default=None, description="""The study event corresponding to a life event""", json_schema_extra = { "linkml_meta": {'alias': 'study_event', 'domain_of': ['LifeEvent']} })
    life_event_type: Optional[LifeEventProcessOntology] = Field(default=None, description="""The specific type of a life event""", json_schema_extra = { "linkml_meta": {'alias': 'life_event_type', 'domain_of': ['LifeEvent'], 'slot_uri': 'rdf:type'} })
    geolocation: Optional[GeolocationOntology] = Field(default=None, description="""The geolocation of a participant at birth""", json_schema_extra = { "linkml_meta": {'alias': 'geolocation',
         'domain_of': ['Participant', 'LifeEvent'],
         'slot_uri': 'RO:0001025'} })
    t0_event: Optional[str] = Field(default=None, description="""The T0 event used to specify the time of this life event""", json_schema_extra = { "linkml_meta": {'alias': 't0_event', 'domain_of': ['LifeEvent']} })
    start: Optional[Decimal] = Field(default=None, description="""The start time of this life event, relative to the T0 event""", json_schema_extra = { "linkml_meta": {'alias': 'start', 'domain_of': ['LifeEvent']} })
    duration: Optional[Decimal] = Field(default=None, description="""The duration of this life event""", json_schema_extra = { "linkml_meta": {'alias': 'duration', 'domain_of': ['LifeEvent']} })
    time_unit: Optional[str] = Field(default=None, description="""The time unit used to measure the start and duration of this life event""", json_schema_extra = { "linkml_meta": {'alias': 'time_unit', 'domain_of': ['LifeEvent']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class Specimen(NamedThing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0100051',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    life_event: Optional[str] = Field(default=None, description="""The life event corresponding to an immune exposure""", json_schema_extra = { "linkml_meta": {'alias': 'life_event', 'domain_of': ['Assessment', 'Specimen']} })
    tissue: Optional[TissueOntology] = Field(default=None, description="""The actual tissue sampled, e.g. lymph node, liver, peripheral blood""", json_schema_extra = { "linkml_meta": {'alias': 'tissue',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Specimen', 'Sample', 'SampleProcessing']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class SpecimenCollection(LifeEvent):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0000659',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    specimen: Optional[str] = Field(default=None, description="""The specimen that was input for an assay""", json_schema_extra = { "linkml_meta": {'alias': 'specimen',
         'domain_of': ['SpecimenCollection', 'SpecimenProcessing', 'Assay'],
         'slot_uri': 'OBI:0000293'} })
    type: Literal["SpecimenCollection"] = Field(default="SpecimenCollection", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['LifeEvent', 'Assay', 'AKDataItem', 'TCellReceptor', 'Epitope']} })
    participant: Optional[str] = Field(default=None, description="""The participant of a life event""", json_schema_extra = { "linkml_meta": {'alias': 'participant', 'domain_of': ['LifeEvent'], 'slot_uri': 'RO:0000057'} })
    study_event: Optional[str] = Field(default=None, description="""The study event corresponding to a life event""", json_schema_extra = { "linkml_meta": {'alias': 'study_event', 'domain_of': ['LifeEvent']} })
    life_event_type: Optional[LifeEventProcessOntology] = Field(default=None, description="""The specific type of a life event""", json_schema_extra = { "linkml_meta": {'alias': 'life_event_type', 'domain_of': ['LifeEvent'], 'slot_uri': 'rdf:type'} })
    geolocation: Optional[GeolocationOntology] = Field(default=None, description="""The geolocation of a participant at birth""", json_schema_extra = { "linkml_meta": {'alias': 'geolocation',
         'domain_of': ['Participant', 'LifeEvent'],
         'slot_uri': 'RO:0001025'} })
    t0_event: Optional[str] = Field(default=None, description="""The T0 event used to specify the time of this life event""", json_schema_extra = { "linkml_meta": {'alias': 't0_event', 'domain_of': ['LifeEvent']} })
    start: Optional[Decimal] = Field(default=None, description="""The start time of this life event, relative to the T0 event""", json_schema_extra = { "linkml_meta": {'alias': 'start', 'domain_of': ['LifeEvent']} })
    duration: Optional[Decimal] = Field(default=None, description="""The duration of this life event""", json_schema_extra = { "linkml_meta": {'alias': 'duration', 'domain_of': ['LifeEvent']} })
    time_unit: Optional[str] = Field(default=None, description="""The time unit used to measure the start and duration of this life event""", json_schema_extra = { "linkml_meta": {'alias': 'time_unit', 'domain_of': ['LifeEvent']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class SpecimenProcessing(Process):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0000094',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    specimen: Optional[str] = Field(default=None, description="""The specimen that was input for an assay""", json_schema_extra = { "linkml_meta": {'alias': 'specimen',
         'domain_of': ['SpecimenCollection', 'SpecimenProcessing', 'Assay'],
         'slot_uri': 'OBI:0000293'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class CellIsolationProcessing(SpecimenProcessing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:00000512',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    tissue_processing: Optional[str] = Field(default=None, description="""Enzymatic digestion and/or physical methods used to isolate cells from sample""", json_schema_extra = { "linkml_meta": {'alias': 'tissue_processing',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_subset: Optional[CellSubsetOntology] = Field(default=None, description="""Commonly-used designation of isolated cell population""", json_schema_extra = { "linkml_meta": {'alias': 'cell_subset',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_phenotype: Optional[str] = Field(default=None, description="""List of cellular markers and their expression levels used to isolate the cell population""", json_schema_extra = { "linkml_meta": {'alias': 'cell_phenotype',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_species: Optional[CellSpeciesOntology] = Field(default=None, description="""Binomial designation of the species from which the analyzed cells originate. Typically, this value should be identical to `species`, in which case it SHOULD NOT be set explicitly. However, there are valid experimental setups in which the two might differ, e.g., chimeric animal models. If set, this key will overwrite the `species` information for all lower layers of the schema.""", json_schema_extra = { "linkml_meta": {'alias': 'cell_species',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    single_cell: Optional[bool] = Field(default=None, description="""TRUE if single cells were isolated into separate compartments""", json_schema_extra = { "linkml_meta": {'alias': 'single_cell',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_number: Optional[int] = Field(default=None, description="""Total number of cells that went into the experiment""", json_schema_extra = { "linkml_meta": {'alias': 'cell_number',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cells_per_reaction: Optional[int] = Field(default=None, description="""Number of cells for each biological replicate""", json_schema_extra = { "linkml_meta": {'alias': 'cells_per_reaction',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_storage: Optional[bool] = Field(default=None, description="""TRUE if cells were cryo-preserved between isolation and further processing""", json_schema_extra = { "linkml_meta": {'alias': 'cell_storage',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_quality: Optional[str] = Field(default=None, description="""Relative amount of viable cells after preparation and (if applicable) thawing""", json_schema_extra = { "linkml_meta": {'alias': 'cell_quality',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_isolation: Optional[str] = Field(default=None, description="""Description of the procedure used for marker-based isolation or enrich cells""", json_schema_extra = { "linkml_meta": {'alias': 'cell_isolation',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_processing_protocol: Optional[str] = Field(default=None, description="""Description of the methods applied to the sample including cell preparation/ isolation/enrichment and nucleic acid extraction. This should closely mirror the Materials and methods section in the manuscript.""", json_schema_extra = { "linkml_meta": {'alias': 'cell_processing_protocol',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    specimen: Optional[str] = Field(default=None, description="""The specimen that was input for an assay""", json_schema_extra = { "linkml_meta": {'alias': 'specimen',
         'domain_of': ['SpecimenCollection', 'SpecimenProcessing', 'Assay'],
         'slot_uri': 'OBI:0000293'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class Assay(Process):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0000070',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    specimen: Optional[str] = Field(default=None, description="""The specimen that was input for an assay""", json_schema_extra = { "linkml_meta": {'alias': 'specimen',
         'domain_of': ['SpecimenCollection', 'SpecimenProcessing', 'Assay'],
         'slot_uri': 'OBI:0000293'} })
    specimen_processing: Optional[list[str]] = Field(default=None, description="""A series of zero or more specimen processing steps that precede an assay""", json_schema_extra = { "linkml_meta": {'alias': 'specimen_processing',
         'domain_of': ['Assay'],
         'slot_uri': 'BFO:0000051'} })
    type: Literal["Assay"] = Field(default="Assay", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['LifeEvent', 'Assay', 'AKDataItem', 'TCellReceptor', 'Epitope']} })
    assay_type: Optional[AssayTypeOntology] = Field(default=None, description="""The specific type of an assay""", json_schema_extra = { "linkml_meta": {'alias': 'assay_type', 'domain_of': ['Assay'], 'slot_uri': 'rdf:type'} })
    has_specified_output: Optional[str] = Field(default=None, description="""output data item""", json_schema_extra = { "linkml_meta": {'alias': 'has_specified_output', 'domain_of': ['Assay', 'InputOutputDataMap']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class AntibodyAntigenBindingAssay(Assay):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0003127',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    specimen: Optional[str] = Field(default=None, description="""The specimen that was input for an assay""", json_schema_extra = { "linkml_meta": {'alias': 'specimen',
         'domain_of': ['SpecimenCollection', 'SpecimenProcessing', 'Assay'],
         'slot_uri': 'OBI:0000293'} })
    specimen_processing: Optional[list[str]] = Field(default=None, description="""A series of zero or more specimen processing steps that precede an assay""", json_schema_extra = { "linkml_meta": {'alias': 'specimen_processing',
         'domain_of': ['Assay'],
         'slot_uri': 'BFO:0000051'} })
    type: Literal["AntibodyAntigenBindingAssay"] = Field(default="AntibodyAntigenBindingAssay", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['LifeEvent', 'Assay', 'AKDataItem', 'TCellReceptor', 'Epitope']} })
    assay_type: Optional[AssayTypeOntology] = Field(default=None, description="""The specific type of an assay""", json_schema_extra = { "linkml_meta": {'alias': 'assay_type', 'domain_of': ['Assay'], 'slot_uri': 'rdf:type'} })
    has_specified_output: Optional[str] = Field(default=None, description="""output data item""", json_schema_extra = { "linkml_meta": {'alias': 'has_specified_output', 'domain_of': ['Assay', 'InputOutputDataMap']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class DataItem(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'IAO:0000027',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    pass


class MeasurementDatum(DataItem):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'IAO:0000032',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    measurement_value: Optional[Decimal] = Field(default=None, description="""The measurement result value""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_value', 'domain_of': ['MeasurementDatum']} })
    measurement_unit: Optional[MeasurementUnitOntology] = Field(default=None, description="""The measurement result value unit""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_unit', 'domain_of': ['MeasurementDatum']} })


class Assessment(MeasurementDatum, Process):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0002441',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema',
         'mixins': ['MeasurementDatum']})

    life_event: Optional[str] = Field(default=None, description="""The life event corresponding to an immune exposure""", json_schema_extra = { "linkml_meta": {'alias': 'life_event', 'domain_of': ['Assessment', 'Specimen']} })
    assessment_type: Optional[str] = Field(default=None, description="""The specific type of an assessment""", json_schema_extra = { "linkml_meta": {'alias': 'assessment_type',
         'domain_of': ['Assessment'],
         'slot_uri': 'rdf:type'} })
    target_entity_type: Optional[str] = Field(default=None, description="""The type of the entity being measured""", json_schema_extra = { "linkml_meta": {'alias': 'target_entity_type', 'domain_of': ['Assessment']} })
    measurement_value: Optional[Decimal] = Field(default=None, description="""The measurement result value""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_value', 'domain_of': ['MeasurementDatum']} })
    measurement_unit: Optional[MeasurementUnitOntology] = Field(default=None, description="""The measurement result value unit""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_unit', 'domain_of': ['MeasurementDatum']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class MeasurementCategory(DataItem):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'OBI:0001930',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    measurement_category: Optional[str] = Field(default=None, description="""The measurement result category""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_category', 'domain_of': ['MeasurementCategory']} })


class TCellReceptorEpitopeSpecificityMeasurement(MeasurementCategory):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://github.com/airr-knowledge/ak-schema',
         'slot_usage': {'measurement_category': {'name': 'measurement_category',
                                                 'range': 'CategoricalSpecificityEnum'}}})

    measurement_category: Optional[CategoricalSpecificityEnum] = Field(default=None, description="""The measurement result category""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_category', 'domain_of': ['MeasurementCategory']} })


class TCellReceptorEpitopeBindingAssay(TCellReceptorEpitopeSpecificityMeasurement, Assay):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:1110037',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema',
         'mixins': ['TCellReceptorEpitopeSpecificityMeasurement']})

    epitope: Optional[str] = Field(default=None, description="""The epitope being measured""", json_schema_extra = { "linkml_meta": {'alias': 'epitope',
         'domain_of': ['TCellReceptorEpitopeBindingAssay', 'TCRpMHCComplex']} })
    tcell_receptors: Optional[list[str]] = Field(default=None, description="""The T cell receptors being measured""", json_schema_extra = { "linkml_meta": {'alias': 'tcell_receptors',
         'domain_of': ['AIRRSequencingAssay', 'TCellReceptorEpitopeBindingAssay']} })
    specimen: Optional[str] = Field(default=None, description="""The specimen that was input for an assay""", json_schema_extra = { "linkml_meta": {'alias': 'specimen',
         'domain_of': ['SpecimenCollection', 'SpecimenProcessing', 'Assay'],
         'slot_uri': 'OBI:0000293'} })
    specimen_processing: Optional[list[str]] = Field(default=None, description="""A series of zero or more specimen processing steps that precede an assay""", json_schema_extra = { "linkml_meta": {'alias': 'specimen_processing',
         'domain_of': ['Assay'],
         'slot_uri': 'BFO:0000051'} })
    type: Literal["TCellReceptorEpitopeBindingAssay"] = Field(default="TCellReceptorEpitopeBindingAssay", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['LifeEvent', 'Assay', 'AKDataItem', 'TCellReceptor', 'Epitope']} })
    assay_type: Optional[AssayTypeOntology] = Field(default=None, description="""The specific type of an assay""", json_schema_extra = { "linkml_meta": {'alias': 'assay_type', 'domain_of': ['Assay'], 'slot_uri': 'rdf:type'} })
    has_specified_output: Optional[str] = Field(default=None, description="""output data item""", json_schema_extra = { "linkml_meta": {'alias': 'has_specified_output', 'domain_of': ['Assay', 'InputOutputDataMap']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })
    measurement_category: Optional[CategoricalSpecificityEnum] = Field(default=None, description="""The measurement result category""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_category', 'domain_of': ['MeasurementCategory']} })


class DataSet(DataItem):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'IAO:0000100',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    data_items: Optional[list[str]] = Field(default=None, description="""set of data items""", json_schema_extra = { "linkml_meta": {'alias': 'data_items', 'domain_of': ['DataSet']} })


class AKDataItem(AKObject):
    """
    data item with an akc_id
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    type: Literal["AKDataItem"] = Field(default="AKDataItem", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['LifeEvent', 'Assay', 'AKDataItem', 'TCellReceptor', 'Epitope']} })
    data_item_types: Optional[list[DataItemTypeEnum]] = Field(default=None, description="""semantic types of the data""", json_schema_extra = { "linkml_meta": {'alias': 'data_item_types', 'domain_of': ['AKDataItem']} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class AKDataSet(AKDataItem, DataSet):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'IAO:0000100',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema',
         'mixins': ['DataSet']})

    data_items: Optional[list[str]] = Field(default=None, description="""set of data items""", json_schema_extra = { "linkml_meta": {'alias': 'data_items', 'domain_of': ['DataSet']} })
    type: Literal["AKDataSet"] = Field(default="AKDataSet", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['LifeEvent', 'Assay', 'AKDataItem', 'TCellReceptor', 'Epitope']} })
    data_item_types: Optional[list[DataItemTypeEnum]] = Field(default=None, description="""semantic types of the data""", json_schema_extra = { "linkml_meta": {'alias': 'data_item_types', 'domain_of': ['AKDataItem']} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class SequenceData(AKDataItem):
    """
    sequence data items are given an akc_id
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0000973',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    type: Literal["SequenceData"] = Field(default="SequenceData", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['LifeEvent', 'Assay', 'AKDataItem', 'TCellReceptor', 'Epitope']} })
    data_item_types: Optional[list[DataItemTypeEnum]] = Field(default=None, description="""semantic types of the data""", json_schema_extra = { "linkml_meta": {'alias': 'data_item_types', 'domain_of': ['AKDataItem']} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class RNATranscriptomeData(SequenceData):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    type: Literal["RNATranscriptomeData"] = Field(default="RNATranscriptomeData", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['LifeEvent', 'Assay', 'AKDataItem', 'TCellReceptor', 'Epitope']} })
    data_item_types: Optional[list[DataItemTypeEnum]] = Field(default=None, description="""semantic types of the data""", json_schema_extra = { "linkml_meta": {'alias': 'data_item_types', 'domain_of': ['AKDataItem']} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class DataTransformation(Process):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0200000',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    was_generated_by: Optional[list[InputOutputDataMap]] = Field(default=None, description="""direct provenance link of one entity (input) to another (output) for a data transformation""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by', 'domain_of': ['DataTransformation']} })
    data_transformation_types: Optional[list[DataItemTypeEnum]] = Field(default=None, description="""semantic types of the data transformation""", json_schema_extra = { "linkml_meta": {'alias': 'data_transformation_types', 'domain_of': ['DataTransformation']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class InputOutputDataMap(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    data_transformation: Optional[str] = Field(default=None, description="""a process that transforms input data into output data""", json_schema_extra = { "linkml_meta": {'alias': 'data_transformation', 'domain_of': ['InputOutputDataMap']} })
    has_specified_input: Optional[str] = Field(default=None, description="""input data item""", json_schema_extra = { "linkml_meta": {'alias': 'has_specified_input', 'domain_of': ['InputOutputDataMap']} })
    has_specified_output: Optional[str] = Field(default=None, description="""output data item""", json_schema_extra = { "linkml_meta": {'alias': 'has_specified_output', 'domain_of': ['Assay', 'InputOutputDataMap']} })


class Conclusion(NamedThing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0001909',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    investigations: Optional[list[str]] = Field(default=None, description="""The investigations that a reference or conclusion are about""", json_schema_extra = { "linkml_meta": {'alias': 'investigations',
         'domain_of': ['AIRRKnowledgeCommons', 'Reference', 'Conclusion'],
         'slot_uri': 'IAO:0000136'} })
    datasets: Optional[list[str]] = Field(default=None, description="""The datasets that support a conclusion""", json_schema_extra = { "linkml_meta": {'alias': 'datasets', 'domain_of': ['AIRRKnowledgeCommons', 'Conclusion']} })
    result: Optional[str] = Field(default=None, description="""The content of the conclusion""", json_schema_extra = { "linkml_meta": {'alias': 'result', 'domain_of': ['Conclusion']} })
    data_location_type: Optional[str] = Field(default=None, description="""The type of location where data was found, e.g. figure, table""", json_schema_extra = { "linkml_meta": {'alias': 'data_location_type', 'domain_of': ['Conclusion']} })
    data_location_value: Optional[str] = Field(default=None, description="""An identifier for the location of the data, e.g. figure 2""", json_schema_extra = { "linkml_meta": {'alias': 'data_location_value', 'domain_of': ['Conclusion']} })
    organism: Optional[SpeciesOntology] = Field(default=None, description="""The type of organism that the conclusion is about""", json_schema_extra = { "linkml_meta": {'alias': 'organism', 'domain_of': ['Conclusion'], 'slot_uri': 'IAO:0000136'} })
    experiment_type: Optional[str] = Field(default=None, description="""The type of experiment that supports the conclusion""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_type', 'domain_of': ['Conclusion']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class ImmuneSystem(NamedThing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'UBERON:0002405',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class Chain(AKObject):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    species: Optional[SpeciesOntology] = Field(default=None, description="""Binomial designation of subject's species""", json_schema_extra = { "linkml_meta": {'alias': 'species',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Participant',
                       'Chain',
                       'AlleleDescription',
                       'GermlineSet',
                       'Subject']} })
    aa_hash: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'aa_hash', 'domain_of': ['Chain']} })
    junction_aa_vj_allele_hash: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'junction_aa_vj_allele_hash', 'domain_of': ['Chain']} })
    junction_aa_vj_gene_hash: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'junction_aa_vj_gene_hash', 'domain_of': ['Chain']} })
    complete_vdj: Optional[bool] = Field(default=None, description="""Complete VDJ flag.""", json_schema_extra = { "linkml_meta": {'alias': 'complete_vdj', 'domain_of': ['Chain', 'Rearrangement']} })
    sequence: Optional[str] = Field(default=None, description="""Nucleotide sequence.""", json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'domain_of': ['Chain',
                       'RearrangedSequence',
                       'UnrearrangedSequence',
                       'AlleleDescription',
                       'UndocumentedAllele',
                       'Rearrangement']} })
    sequence_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the query nucleotide sequence.""", json_schema_extra = { "linkml_meta": {'alias': 'sequence_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'PeptidicEpitope', 'Rearrangement']} })
    locus: Optional[LocusEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'locus',
         'domain_of': ['Chain',
                       'AlleleDescription',
                       'GermlineSet',
                       'Genotype',
                       'Rearrangement']} })
    v_call: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'v_call',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement', 'Clone']} })
    d_call: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'd_call',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement', 'Clone']} })
    j_call: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'j_call',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement', 'Clone']} })
    c_call: Optional[str] = Field(default=None, description="""Constant region gene with allele. If referring to a known reference sequence in a database the relevant gene/allele nomenclature should be followed (e.g., IGHG1*01 if using IMGT/GENE-DB).""", json_schema_extra = { "linkml_meta": {'alias': 'c_call',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement']} })
    junction_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the junction.""", json_schema_extra = { "linkml_meta": {'alias': 'junction_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement', 'Clone', 'Node']} })
    cdr1_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the cdr1 field.""", json_schema_extra = { "linkml_meta": {'alias': 'cdr1_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement']} })
    cdr2_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the cdr2 field.""", json_schema_extra = { "linkml_meta": {'alias': 'cdr2_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement']} })
    cdr3_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the cdr3 field.""", json_schema_extra = { "linkml_meta": {'alias': 'cdr3_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement']} })
    cdr1_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cdr1_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'SequenceDelineationV', 'Rearrangement']} })
    cdr1_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cdr1_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'SequenceDelineationV', 'Rearrangement']} })
    cdr2_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cdr2_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'SequenceDelineationV', 'Rearrangement']} })
    cdr2_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cdr2_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'SequenceDelineationV', 'Rearrangement']} })
    cdr3_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cdr3_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'SequenceDelineationV', 'Rearrangement']} })
    cdr3_end: Optional[int] = Field(default=None, description="""CDR3 end position in the query sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'cdr3_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement']} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class ImmuneReceptor(AKObject):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class TCellReceptor(ImmuneReceptor):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'GO:0042101',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    type: Literal["TCellReceptor"] = Field(default="TCellReceptor", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['LifeEvent', 'Assay', 'AKDataItem', 'TCellReceptor', 'Epitope']} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class AlphaBetaTCR(TCellReceptor):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'GO:0042105',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    tra_chain: Optional[str] = Field(default=None, description="""T cell receptor alpha chain""", json_schema_extra = { "linkml_meta": {'alias': 'tra_chain', 'domain_of': ['AlphaBetaTCR']} })
    trb_chain: Optional[str] = Field(default=None, description="""T cell receptor beta chain""", json_schema_extra = { "linkml_meta": {'alias': 'trb_chain', 'domain_of': ['AlphaBetaTCR']} })
    type: Literal["AlphaBetaTCR"] = Field(default="AlphaBetaTCR", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['LifeEvent', 'Assay', 'AKDataItem', 'TCellReceptor', 'Epitope']} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class GammaDeltaTCR(TCellReceptor):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'GO:0042106',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    trg_chain: Optional[str] = Field(default=None, description="""T cell receptor gamma chain""", json_schema_extra = { "linkml_meta": {'alias': 'trg_chain', 'domain_of': ['GammaDeltaTCR']} })
    trd_chain: Optional[str] = Field(default=None, description="""T cell receptor delta chain""", json_schema_extra = { "linkml_meta": {'alias': 'trd_chain', 'domain_of': ['GammaDeltaTCR']} })
    type: Literal["GammaDeltaTCR"] = Field(default="GammaDeltaTCR", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['LifeEvent', 'Assay', 'AKDataItem', 'TCellReceptor', 'Epitope']} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class BCellReceptor(ImmuneReceptor):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    igh_chain: Optional[str] = Field(default=None, description="""IG heavy chain""", json_schema_extra = { "linkml_meta": {'alias': 'igh_chain', 'domain_of': ['BCellReceptor']} })
    igk_chain: Optional[str] = Field(default=None, description="""IG kappa light chain""", json_schema_extra = { "linkml_meta": {'alias': 'igk_chain', 'domain_of': ['BCellReceptor']} })
    igl_chain: Optional[str] = Field(default=None, description="""IG lambda light chain""", json_schema_extra = { "linkml_meta": {'alias': 'igl_chain', 'domain_of': ['BCellReceptor']} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class Antigen(NamedThing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:1110034',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    source_protein: Optional[str] = Field(default=None, description="""The protein that this epitope comes from""", json_schema_extra = { "linkml_meta": {'alias': 'source_protein', 'domain_of': ['Antigen', 'PeptidicEpitope']} })
    source_organism: Optional[str] = Field(default=None, description="""The organism that the source protein comes from""", json_schema_extra = { "linkml_meta": {'alias': 'source_organism', 'domain_of': ['Antigen', 'PeptidicEpitope']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class Epitope(NamedThing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    type: Literal["Epitope"] = Field(default="Epitope", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['LifeEvent', 'Assay', 'AKDataItem', 'TCellReceptor', 'Epitope']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class PeptidicEpitope(Epitope):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    sequence_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the query nucleotide sequence.""", json_schema_extra = { "linkml_meta": {'alias': 'sequence_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'PeptidicEpitope', 'Rearrangement']} })
    source_protein: Optional[str] = Field(default=None, description="""The protein that this epitope comes from""", json_schema_extra = { "linkml_meta": {'alias': 'source_protein', 'domain_of': ['Antigen', 'PeptidicEpitope']} })
    source_organism: Optional[str] = Field(default=None, description="""The organism that the source protein comes from""", json_schema_extra = { "linkml_meta": {'alias': 'source_organism', 'domain_of': ['Antigen', 'PeptidicEpitope']} })
    type: Literal["PeptidicEpitope"] = Field(default="PeptidicEpitope", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['LifeEvent', 'Assay', 'AKDataItem', 'TCellReceptor', 'Epitope']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class AntibodyAntigenComplex(NamedThing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0003119',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    antibody: Optional[str] = Field(default=None, description="""B cell receptor, immunoglobulin antibody""", json_schema_extra = { "linkml_meta": {'alias': 'antibody', 'domain_of': ['AntibodyAntigenComplex']} })
    antigen: Optional[str] = Field(default=None, description="""A material entity with antigen role""", json_schema_extra = { "linkml_meta": {'alias': 'antigen',
         'domain_of': ['AntibodyAntigenComplex', 'ReceptorReactivity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class TCRpMHCComplex(NamedThing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0003119',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    tcell_receptor: Optional[str] = Field(default=None, description="""T cell receptor""", json_schema_extra = { "linkml_meta": {'alias': 'tcell_receptor', 'domain_of': ['TCRpMHCComplex']} })
    epitope: Optional[str] = Field(default=None, description="""The epitope being measured""", json_schema_extra = { "linkml_meta": {'alias': 'epitope',
         'domain_of': ['TCellReceptorEpitopeBindingAssay', 'TCRpMHCComplex']} })
    mhc: Optional[MHCAllele] = Field(default=None, description="""Major histocompatibility complex""", json_schema_extra = { "linkml_meta": {'alias': 'mhc', 'domain_of': ['TCRpMHCComplex']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class Model(NamedThing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'EXO:0000072',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class ConceptualModel(Model):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'EXO:0000073',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class CommunicativeModel(Model):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class ModelSpecification(PlanSpecification):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class ModelingFramework(NamedThing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'SBO:0000004',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class Simulation(Process):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'APOLLO_SV:00000070',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class SimilarityCalculation(AKObject):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0200113',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    chain_domain: Optional[str] = Field(default=None, description="""Immune receptor chain element in binary relation domain""", json_schema_extra = { "linkml_meta": {'alias': 'chain_domain', 'domain_of': ['SimilarityCalculation']} })
    chain_codomain: Optional[str] = Field(default=None, description="""Immune receptor chain element in binary relation codomain""", json_schema_extra = { "linkml_meta": {'alias': 'chain_codomain', 'domain_of': ['SimilarityCalculation']} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class ChainSimilarity(SimilarityCalculation):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    chain_similarity_type: Optional[ChainSimilarityTypeEnum] = Field(default=None, description="""Type of similarity calculation between two immune receptor chains""", json_schema_extra = { "linkml_meta": {'alias': 'chain_similarity_type',
         'domain_of': ['ChainSimilarity'],
         'slot_uri': 'rdf:type'} })
    chain_domain: Optional[str] = Field(default=None, description="""Immune receptor chain element in binary relation domain""", json_schema_extra = { "linkml_meta": {'alias': 'chain_domain', 'domain_of': ['SimilarityCalculation']} })
    chain_codomain: Optional[str] = Field(default=None, description="""Immune receptor chain element in binary relation codomain""", json_schema_extra = { "linkml_meta": {'alias': 'chain_codomain', 'domain_of': ['SimilarityCalculation']} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class TimePoint(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    time_point_label: Optional[str] = Field(default=None, description="""Informative label for the time point""", json_schema_extra = { "linkml_meta": {'alias': 'time_point_label',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['TimePoint']} })
    time_point_value: Optional[float] = Field(default=None, description="""Value of the time point""", json_schema_extra = { "linkml_meta": {'alias': 'time_point_value',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['TimePoint']} })
    time_point_unit: Optional[TimePointUnitOntology] = Field(default=None, description="""Unit of the time point""", json_schema_extra = { "linkml_meta": {'alias': 'time_point_unit',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['TimePoint']} })


class Acknowledgement(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    acknowledgement_id: Optional[str] = Field(default=None, description="""unique identifier of this Acknowledgement within the file""", json_schema_extra = { "linkml_meta": {'alias': 'acknowledgement_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Acknowledgement']} })
    individual_full_name: Optional[str] = Field(default=None, description="""Full name of individual""", json_schema_extra = { "linkml_meta": {'alias': 'individual_full_name',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Acknowledgement']} })
    institution_name: Optional[str] = Field(default=None, description="""Individual's department and institution name""", json_schema_extra = { "linkml_meta": {'alias': 'institution_name',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Acknowledgement']} })
    orcid_id: Optional[str] = Field(default=None, description="""Individual's ORCID identifier""", json_schema_extra = { "linkml_meta": {'alias': 'orcid_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Acknowledgement']} })


class RearrangedSequence(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    sequence_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sequence_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RearrangedSequence',
                       'UnrearrangedSequence',
                       'Alignment',
                       'Rearrangement',
                       'Node']} })
    sequence: Optional[str] = Field(default=None, description="""Nucleotide sequence.""", json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'domain_of': ['Chain',
                       'RearrangedSequence',
                       'UnrearrangedSequence',
                       'AlleleDescription',
                       'UndocumentedAllele',
                       'Rearrangement']} })
    derivation: Optional[DerivationEnum] = Field(default=None, description="""The class of nucleic acid that was used as primary starting material""", json_schema_extra = { "linkml_meta": {'alias': 'derivation',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RearrangedSequence']} })
    observation_type: Optional[ObservationTypeEnum] = Field(default=None, description="""The type of observation from which this sequence was drawn, such as direct sequencing or  inference from repertoire sequencing data.""", json_schema_extra = { "linkml_meta": {'alias': 'observation_type',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['RearrangedSequence'],
         'slot_uri': 'rdf:type'} })
    curation: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'curation',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RearrangedSequence',
                       'UnrearrangedSequence',
                       'AlleleDescription',
                       'GermlineSet']} })
    repository_name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'repository_name',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RearrangedSequence', 'UnrearrangedSequence']} })
    repository_ref: Optional[str] = Field(default=None, description="""Queryable id or accession number of the sequence published by the repository""", json_schema_extra = { "linkml_meta": {'alias': 'repository_ref',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RearrangedSequence', 'UnrearrangedSequence']} })
    deposited_version: Optional[str] = Field(default=None, description="""Version number of the sequence within the repository""", json_schema_extra = { "linkml_meta": {'alias': 'deposited_version',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RearrangedSequence']} })
    sequence_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sequence_start', 'domain_of': ['RearrangedSequence', 'Alignment']} })
    sequence_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sequence_end', 'domain_of': ['RearrangedSequence', 'Alignment']} })


class UnrearrangedSequence(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    sequence_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sequence_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RearrangedSequence',
                       'UnrearrangedSequence',
                       'Alignment',
                       'Rearrangement',
                       'Node']} })
    sequence: Optional[str] = Field(default=None, description="""Nucleotide sequence.""", json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'domain_of': ['Chain',
                       'RearrangedSequence',
                       'UnrearrangedSequence',
                       'AlleleDescription',
                       'UndocumentedAllele',
                       'Rearrangement']} })
    curation: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'curation',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RearrangedSequence',
                       'UnrearrangedSequence',
                       'AlleleDescription',
                       'GermlineSet']} })
    repository_name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'repository_name',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RearrangedSequence', 'UnrearrangedSequence']} })
    repository_ref: Optional[str] = Field(default=None, description="""Queryable id or accession number of the sequence published by the repository""", json_schema_extra = { "linkml_meta": {'alias': 'repository_ref',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RearrangedSequence', 'UnrearrangedSequence']} })
    patch_no: Optional[str] = Field(default=None, description="""Genome assembly patch number in which this gene was determined""", json_schema_extra = { "linkml_meta": {'alias': 'patch_no',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['UnrearrangedSequence']} })
    gff_seqid: Optional[str] = Field(default=None, description="""Sequence (from the assembly) of a window including the gene and preferably also the promoter region.""", json_schema_extra = { "linkml_meta": {'alias': 'gff_seqid',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['UnrearrangedSequence']} })
    gff_start: Optional[int] = Field(default=None, description="""Genomic co-ordinates of the start of the sequence of interest described in this record in  Ensemble GFF version 3.""", json_schema_extra = { "linkml_meta": {'alias': 'gff_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['UnrearrangedSequence']} })
    gff_end: Optional[int] = Field(default=None, description="""Genomic co-ordinates of the end of the sequence of interest described in this record in  Ensemble GFF version 3.""", json_schema_extra = { "linkml_meta": {'alias': 'gff_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['UnrearrangedSequence']} })
    strand: Optional[StrandEnum] = Field(default=None, description="""sense (+ or -)""", json_schema_extra = { "linkml_meta": {'alias': 'strand',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['UnrearrangedSequence']} })


class SequenceDelineationV(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    sequence_delineation_id: Optional[str] = Field(default=None, description="""Unique identifier of this SequenceDelineationV within the file. Typically, generated by the  repository hosting the record.""", json_schema_extra = { "linkml_meta": {'alias': 'sequence_delineation_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequenceDelineationV']} })
    delineation_scheme: Optional[str] = Field(default=None, description="""Name of the delineation scheme""", json_schema_extra = { "linkml_meta": {'alias': 'delineation_scheme',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequenceDelineationV']} })
    unaligned_sequence: Optional[str] = Field(default=None, description="""entire V-sequence covered by this delineation""", json_schema_extra = { "linkml_meta": {'alias': 'unaligned_sequence',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequenceDelineationV']} })
    aligned_sequence: Optional[str] = Field(default=None, description="""Aligned sequence if this delineation provides an alignment. An aligned sequence should always be  provided for IMGT delineations.""", json_schema_extra = { "linkml_meta": {'alias': 'aligned_sequence',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequenceDelineationV']} })
    fwr1_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'fwr1_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequenceDelineationV', 'Rearrangement']} })
    fwr1_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'fwr1_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequenceDelineationV', 'Rearrangement']} })
    cdr1_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cdr1_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'SequenceDelineationV', 'Rearrangement']} })
    cdr1_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cdr1_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'SequenceDelineationV', 'Rearrangement']} })
    fwr2_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'fwr2_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequenceDelineationV', 'Rearrangement']} })
    fwr2_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'fwr2_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequenceDelineationV', 'Rearrangement']} })
    cdr2_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cdr2_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'SequenceDelineationV', 'Rearrangement']} })
    cdr2_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cdr2_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'SequenceDelineationV', 'Rearrangement']} })
    fwr3_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'fwr3_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequenceDelineationV', 'Rearrangement']} })
    fwr3_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'fwr3_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequenceDelineationV', 'Rearrangement']} })
    cdr3_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cdr3_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'SequenceDelineationV', 'Rearrangement']} })
    alignment_labels: Optional[list[str]] = Field(default=None, description="""One string for each codon in the aligned_sequence indicating the label of that codon according to  the numbering of the delineation scheme if it provides one.""", json_schema_extra = { "linkml_meta": {'alias': 'alignment_labels',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequenceDelineationV']} })


class AlleleDescription(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    allele_description_id: Optional[str] = Field(default=None, description="""Unique identifier of this AlleleDescription within the file. Typically, generated by the  repository hosting the record.""", json_schema_extra = { "linkml_meta": {'alias': 'allele_description_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    allele_description_ref: Optional[str] = Field(default=None, description="""Unique reference to the allele description, in standardized form (Repo:Label:Version)""", json_schema_extra = { "linkml_meta": {'alias': 'allele_description_ref',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    maintainer: Optional[str] = Field(default=None, description="""Maintainer of this sequence record""", json_schema_extra = { "linkml_meta": {'alias': 'maintainer',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    acknowledgements: Optional[list[Acknowledgement]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'acknowledgements',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription', 'GermlineSet']} })
    lab_address: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'lab_address',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription', 'GermlineSet', 'Study']} })
    release_version: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'release_version',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription', 'GermlineSet']} })
    release_date: Optional[datetime ] = Field(default=None, description="""Date of this release""", json_schema_extra = { "linkml_meta": {'alias': 'release_date',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Investigation', 'AlleleDescription', 'GermlineSet']} })
    release_description: Optional[str] = Field(default=None, description="""Brief descriptive notes of the reason for this release and the changes embodied""", json_schema_extra = { "linkml_meta": {'alias': 'release_description',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription', 'GermlineSet']} })
    label: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'label',
         'domain_of': ['AlleleDescription', 'DocumentedAllele', 'DeletedGene']} })
    sequence: Optional[str] = Field(default=None, description="""Nucleotide sequence.""", json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'domain_of': ['Chain',
                       'RearrangedSequence',
                       'UnrearrangedSequence',
                       'AlleleDescription',
                       'UndocumentedAllele',
                       'Rearrangement']} })
    coding_sequence: Optional[str] = Field(default=None, description="""Nucleotide sequence of the core coding region, such as the coding region of a D-, J- or C- gene  or the coding region of a V-gene excluding the leader.""", json_schema_extra = { "linkml_meta": {'alias': 'coding_sequence',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names for this sequence""", json_schema_extra = { "linkml_meta": {'alias': 'aliases',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    locus: Optional[LocusEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'locus',
         'domain_of': ['Chain',
                       'AlleleDescription',
                       'GermlineSet',
                       'Genotype',
                       'Rearrangement']} })
    chromosome: Optional[int] = Field(default=None, description="""chromosome on which the gene is located""", json_schema_extra = { "linkml_meta": {'alias': 'chromosome',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    sequence_type: Optional[SequenceTypeEnum] = Field(default=None, description="""Sequence type (V, D, J, C)""", json_schema_extra = { "linkml_meta": {'alias': 'sequence_type',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['AlleleDescription'],
         'slot_uri': 'rdf:type'} })
    functional: Optional[bool] = Field(default=None, description="""True if the gene is functional, false if it is a pseudogene""", json_schema_extra = { "linkml_meta": {'alias': 'functional',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    inference_type: Optional[InferenceTypeEnum] = Field(default=None, description="""Type of inference(s) from which this gene sequence was inferred""", json_schema_extra = { "linkml_meta": {'alias': 'inference_type',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription'],
         'slot_uri': 'rdf:type'} })
    species: Optional[SpeciesOntology] = Field(default=None, description="""Binomial designation of subject's species""", json_schema_extra = { "linkml_meta": {'alias': 'species',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Participant',
                       'Chain',
                       'AlleleDescription',
                       'GermlineSet',
                       'Subject']} })
    species_subgroup: Optional[str] = Field(default=None, description="""Race, strain or other species subgroup to which this subject belongs""", json_schema_extra = { "linkml_meta": {'alias': 'species_subgroup',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription', 'GermlineSet']} })
    species_subgroup_type: Optional[SpeciesSubgroupTypeEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'species_subgroup_type',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription', 'GermlineSet'],
         'slot_uri': 'rdf:type'} })
    status: Optional[StatusEnum] = Field(default=None, description="""Status of record, assumed active if the field is not present""", json_schema_extra = { "linkml_meta": {'alias': 'status',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    subgroup_designation: Optional[str] = Field(default=None, description="""Identifier of the gene subgroup or clade, as (and if) defined""", json_schema_extra = { "linkml_meta": {'alias': 'subgroup_designation',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    gene_designation: Optional[str] = Field(default=None, description="""Gene number or other identifier, as (and if) defined""", json_schema_extra = { "linkml_meta": {'alias': 'gene_designation',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    allele_designation: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'allele_designation',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription', 'MHCAllele']} })
    allele_similarity_cluster_designation: Optional[str] = Field(default=None, description="""ID of the similarity cluster used in this germline set, if designated""", json_schema_extra = { "linkml_meta": {'alias': 'allele_similarity_cluster_designation',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    allele_similarity_cluster_member_id: Optional[str] = Field(default=None, description="""Membership ID of the allele within the similarity cluster, if a cluster is designated""", json_schema_extra = { "linkml_meta": {'alias': 'allele_similarity_cluster_member_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    j_codon_frame: Optional[JCodonFrameEnum] = Field(default=None, description="""Codon position of the first nucleotide in the 'coding_sequence' field. Mandatory for J genes.  Not used for V or D genes. '1' means the sequence is in-frame, '2' means that the first bp is  missing from the first codon, and '3' means that the first 2 bp are missing.""", json_schema_extra = { "linkml_meta": {'alias': 'j_codon_frame',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    gene_start: Optional[int] = Field(default=None, description="""Co-ordinate in the sequence field of the first nucleotide in the coding_sequence field.""", json_schema_extra = { "linkml_meta": {'alias': 'gene_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    gene_end: Optional[int] = Field(default=None, description="""Co-ordinate in the sequence field of the last gene-coding nucleotide in the coding_sequence field.""", json_schema_extra = { "linkml_meta": {'alias': 'gene_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    utr_5_prime_start: Optional[int] = Field(default=None, description="""Start co-ordinate in the sequence field of the 5 prime UTR (V-genes only).""", json_schema_extra = { "linkml_meta": {'alias': 'utr_5_prime_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    utr_5_prime_end: Optional[int] = Field(default=None, description="""End co-ordinate in the sequence field of the 5 prime UTR (V-genes only).""", json_schema_extra = { "linkml_meta": {'alias': 'utr_5_prime_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    leader_1_start: Optional[int] = Field(default=None, description="""Start co-ordinate in the sequence field of L-PART1 (V-genes only).""", json_schema_extra = { "linkml_meta": {'alias': 'leader_1_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    leader_1_end: Optional[int] = Field(default=None, description="""End co-ordinate in the sequence field of L-PART1 (V-genes only).""", json_schema_extra = { "linkml_meta": {'alias': 'leader_1_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    leader_2_start: Optional[int] = Field(default=None, description="""Start co-ordinate in the sequence field of L-PART2 (V-genes only).""", json_schema_extra = { "linkml_meta": {'alias': 'leader_2_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    leader_2_end: Optional[int] = Field(default=None, description="""End co-ordinate in the sequence field of L-PART2 (V-genes only).""", json_schema_extra = { "linkml_meta": {'alias': 'leader_2_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    v_rs_start: Optional[int] = Field(default=None, description="""Start co-ordinate in the sequence field of the V recombination site (V-genes only).""", json_schema_extra = { "linkml_meta": {'alias': 'v_rs_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    v_rs_end: Optional[int] = Field(default=None, description="""End co-ordinate in the sequence field of the V recombination site (V-genes only).""", json_schema_extra = { "linkml_meta": {'alias': 'v_rs_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    d_rs_3_prime_start: Optional[int] = Field(default=None, description="""Start co-ordinate in the sequence field of the 3 prime D recombination site (D-genes only).""", json_schema_extra = { "linkml_meta": {'alias': 'd_rs_3_prime_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    d_rs_3_prime_end: Optional[int] = Field(default=None, description="""End co-ordinate in the sequence field of the 3 prime D recombination site (D-genes only).""", json_schema_extra = { "linkml_meta": {'alias': 'd_rs_3_prime_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    d_rs_5_prime_start: Optional[int] = Field(default=None, description="""Start co-ordinate in the sequence field of the 5 prime D recombination site (D-genes only).""", json_schema_extra = { "linkml_meta": {'alias': 'd_rs_5_prime_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    d_rs_5_prime_end: Optional[int] = Field(default=None, description="""End co-ordinate in the sequence field of 5 the prime D recombination site (D-genes only).""", json_schema_extra = { "linkml_meta": {'alias': 'd_rs_5_prime_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    j_cdr3_end: Optional[int] = Field(default=None, description="""In the case of a J-gene, the co-ordinate in the sequence field of the first nucelotide of the  conserved PHE or TRP (IMGT codon position 118).""", json_schema_extra = { "linkml_meta": {'alias': 'j_cdr3_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    j_rs_start: Optional[int] = Field(default=None, description="""Start co-ordinate in the sequence field of J recombination site (J-genes only).""", json_schema_extra = { "linkml_meta": {'alias': 'j_rs_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    j_rs_end: Optional[int] = Field(default=None, description="""End co-ordinate in the sequence field of J recombination site (J-genes only).""", json_schema_extra = { "linkml_meta": {'alias': 'j_rs_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    j_donor_splice: Optional[int] = Field(default=None, description="""Co-ordinate in the sequence field of the final 3' nucleotide of the J-REGION (J-genes only).""", json_schema_extra = { "linkml_meta": {'alias': 'j_donor_splice',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    v_gene_delineations: Optional[list[SequenceDelineationV]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'v_gene_delineations',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    unrearranged_support: Optional[list[UnrearrangedSequence]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'unrearranged_support',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    rearranged_support: Optional[list[RearrangedSequence]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'rearranged_support',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    paralogs: Optional[list[str]] = Field(default=None, description="""Gene symbols of any paralogs""", json_schema_extra = { "linkml_meta": {'alias': 'paralogs',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })
    curation: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'curation',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RearrangedSequence',
                       'UnrearrangedSequence',
                       'AlleleDescription',
                       'GermlineSet']} })
    curational_tags: Optional[list[CurationalTagsEnum]] = Field(default=None, description="""Controlled-vocabulary tags applied to this description""", json_schema_extra = { "linkml_meta": {'alias': 'curational_tags',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription']} })


class GermlineSet(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    germline_set_id: Optional[str] = Field(default=None, description="""Unique identifier of the GermlineSet within this file. Typically, generated by the  repository hosting the record.""", json_schema_extra = { "linkml_meta": {'alias': 'germline_set_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['GermlineSet']} })
    author: Optional[str] = Field(default=None, description="""Corresponding author""", json_schema_extra = { "linkml_meta": {'alias': 'author',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['GermlineSet']} })
    lab_name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'lab_name',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['GermlineSet', 'Study']} })
    lab_address: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'lab_address',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription', 'GermlineSet', 'Study']} })
    acknowledgements: Optional[list[Acknowledgement]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'acknowledgements',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription', 'GermlineSet']} })
    release_version: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'release_version',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription', 'GermlineSet']} })
    release_description: Optional[str] = Field(default=None, description="""Brief descriptive notes of the reason for this release and the changes embodied""", json_schema_extra = { "linkml_meta": {'alias': 'release_description',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription', 'GermlineSet']} })
    release_date: Optional[datetime ] = Field(default=None, description="""Date of this release""", json_schema_extra = { "linkml_meta": {'alias': 'release_date',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Investigation', 'AlleleDescription', 'GermlineSet']} })
    germline_set_name: Optional[str] = Field(default=None, description="""descriptive name of this germline set""", json_schema_extra = { "linkml_meta": {'alias': 'germline_set_name',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['GermlineSet']} })
    germline_set_ref: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'germline_set_ref',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['GermlineSet',
                       'DocumentedAllele',
                       'DeletedGene',
                       'DataProcessing']} })
    pub_ids: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'pub_ids',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['GermlineSet', 'Study']} })
    species: Optional[SpeciesOntology] = Field(default=None, description="""Binomial designation of subject's species""", json_schema_extra = { "linkml_meta": {'alias': 'species',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Participant',
                       'Chain',
                       'AlleleDescription',
                       'GermlineSet',
                       'Subject']} })
    species_subgroup: Optional[str] = Field(default=None, description="""Race, strain or other species subgroup to which this subject belongs""", json_schema_extra = { "linkml_meta": {'alias': 'species_subgroup',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription', 'GermlineSet']} })
    species_subgroup_type: Optional[SpeciesSubgroupTypeEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'species_subgroup_type',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription', 'GermlineSet'],
         'slot_uri': 'rdf:type'} })
    locus: Optional[LocusEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'locus',
         'domain_of': ['Chain',
                       'AlleleDescription',
                       'GermlineSet',
                       'Genotype',
                       'Rearrangement']} })
    allele_descriptions: Optional[list[AlleleDescription]] = Field(default=None, description="""list of allele_descriptions in the germline set""", json_schema_extra = { "linkml_meta": {'alias': 'allele_descriptions',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['GermlineSet']} })
    curation: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'curation',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RearrangedSequence',
                       'UnrearrangedSequence',
                       'AlleleDescription',
                       'GermlineSet']} })


class GenotypeSet(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    receptor_genotype_set_id: Optional[str] = Field(default=None, description="""A unique identifier for this Receptor Genotype Set, typically generated by the repository  hosting the schema, for example from the underlying ID of the database record.""", json_schema_extra = { "linkml_meta": {'alias': 'receptor_genotype_set_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['GenotypeSet']} })
    genotype_class_list: Optional[list[Genotype]] = Field(default=None, description="""List of Genotypes included in this Receptor Genotype Set.""", json_schema_extra = { "linkml_meta": {'alias': 'genotype_class_list',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['GenotypeSet']} })


class Genotype(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    receptor_genotype_id: Optional[str] = Field(default=None, description="""A unique identifier within the file for this Receptor Genotype, typically generated by the  repository hosting the schema, for example from the underlying ID of the database record.""", json_schema_extra = { "linkml_meta": {'alias': 'receptor_genotype_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Genotype']} })
    locus: Optional[LocusEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'locus',
         'domain_of': ['Chain',
                       'AlleleDescription',
                       'GermlineSet',
                       'Genotype',
                       'Rearrangement']} })
    documented_alleles: Optional[list[DocumentedAllele]] = Field(default=None, description="""List of alleles documented in reference set(s)""", json_schema_extra = { "linkml_meta": {'alias': 'documented_alleles',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Genotype']} })
    undocumented_alleles: Optional[list[UndocumentedAllele]] = Field(default=None, description="""List of alleles inferred to be present and not documented in an identified GermlineSet""", json_schema_extra = { "linkml_meta": {'alias': 'undocumented_alleles',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Genotype']} })
    deleted_genes: Optional[list[DeletedGene]] = Field(default=None, description="""Array of genes identified as being deleted in this genotype""", json_schema_extra = { "linkml_meta": {'alias': 'deleted_genes',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Genotype']} })
    inference_process: Optional[InferenceProcessEnum] = Field(default=None, description="""Information on how the genotype was acquired. Controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'alias': 'inference_process',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Genotype']} })


class DocumentedAllele(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    label: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'label',
         'domain_of': ['AlleleDescription', 'DocumentedAllele', 'DeletedGene']} })
    germline_set_ref: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'germline_set_ref',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['GermlineSet',
                       'DocumentedAllele',
                       'DeletedGene',
                       'DataProcessing']} })
    phasing: Optional[int] = Field(default=None, description="""Chromosomal phasing indicator. Alleles with the same value are inferred to be located on the  same chromosome.""", json_schema_extra = { "linkml_meta": {'alias': 'phasing',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DocumentedAllele', 'UndocumentedAllele', 'DeletedGene']} })


class UndocumentedAllele(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    allele_name: Optional[str] = Field(default=None, description="""Allele name as allocated by the inference pipeline""", json_schema_extra = { "linkml_meta": {'alias': 'allele_name',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['UndocumentedAllele']} })
    sequence: Optional[str] = Field(default=None, description="""Nucleotide sequence.""", json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'domain_of': ['Chain',
                       'RearrangedSequence',
                       'UnrearrangedSequence',
                       'AlleleDescription',
                       'UndocumentedAllele',
                       'Rearrangement']} })
    phasing: Optional[int] = Field(default=None, description="""Chromosomal phasing indicator. Alleles with the same value are inferred to be located on the  same chromosome.""", json_schema_extra = { "linkml_meta": {'alias': 'phasing',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DocumentedAllele', 'UndocumentedAllele', 'DeletedGene']} })


class DeletedGene(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    label: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'label',
         'domain_of': ['AlleleDescription', 'DocumentedAllele', 'DeletedGene']} })
    germline_set_ref: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'germline_set_ref',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['GermlineSet',
                       'DocumentedAllele',
                       'DeletedGene',
                       'DataProcessing']} })
    phasing: Optional[int] = Field(default=None, description="""Chromosomal phasing indicator. Alleles with the same value are inferred to be located on the  same chromosome.""", json_schema_extra = { "linkml_meta": {'alias': 'phasing',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DocumentedAllele', 'UndocumentedAllele', 'DeletedGene']} })


class MHCGenotypeSet(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    mhc_genotype_set_id: Optional[str] = Field(default=None, description="""A unique identifier for this MHCGenotypeSet""", json_schema_extra = { "linkml_meta": {'alias': 'mhc_genotype_set_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['MHCGenotypeSet']} })
    mhc_genotype_list: Optional[list[MHCGenotype]] = Field(default=None, description="""List of MHCGenotypes included in this set""", json_schema_extra = { "linkml_meta": {'alias': 'mhc_genotype_list',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['MHCGenotypeSet']} })


class MHCGenotype(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    mhc_genotype_id: Optional[str] = Field(default=None, description="""A unique identifier for this MHCGenotype, assumed to be unique in the context of the study""", json_schema_extra = { "linkml_meta": {'alias': 'mhc_genotype_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['MHCGenotype']} })
    mhc_class: Optional[MhcClassEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'mhc_class', 'domain_of': ['MHCGenotype', 'ReceptorReactivity']} })
    mhc_alleles: Optional[list[MHCAllele]] = Field(default=None, description="""List of MHC alleles of the indicated mhc_class identified in an individual""", json_schema_extra = { "linkml_meta": {'alias': 'mhc_alleles',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['MHCGenotype']} })
    mhc_genotyping_method: Optional[str] = Field(default=None, description="""Information on how the genotype was determined. The content of this field should come from a list of recommended terms provided in the AIRR Schema documentation.""", json_schema_extra = { "linkml_meta": {'alias': 'mhc_genotyping_method',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['MHCGenotype']} })


class MHCAllele(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    allele_designation: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'allele_designation',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription', 'MHCAllele']} })
    gene: Optional[GeneOntology] = Field(default=None, description="""The MHC gene to which the described allele belongs""", json_schema_extra = { "linkml_meta": {'alias': 'gene',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['MHCAllele']} })
    reference_set_ref: Optional[str] = Field(default=None, description="""Repository and list from which it was taken (issuer/name/version)""", json_schema_extra = { "linkml_meta": {'alias': 'reference_set_ref',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['MHCAllele']} })


class SubjectGenotype(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    receptor_genotype_set: Optional[GenotypeSet] = Field(default=None, description="""Immune receptor genotype set for this subject.""", json_schema_extra = { "linkml_meta": {'alias': 'receptor_genotype_set',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SubjectGenotype']} })
    mhc_genotype_set: Optional[MHCGenotypeSet] = Field(default=None, description="""MHC genotype set for this subject.""", json_schema_extra = { "linkml_meta": {'alias': 'mhc_genotype_set',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SubjectGenotype']} })


class Study(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    study_id: Optional[str] = Field(default=None, description="""Unique ID assigned by study registry such as one of the International Nucleotide Sequence Database Collaboration (INSDC) repositories.""", json_schema_extra = { "linkml_meta": {'alias': 'study_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Study']} })
    study_title: Optional[str] = Field(default=None, description="""Descriptive study title""", json_schema_extra = { "linkml_meta": {'alias': 'study_title',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Study']} })
    study_type: Optional[StudyTypeOntology] = Field(default=None, description="""Type of study design""", json_schema_extra = { "linkml_meta": {'alias': 'study_type',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Study'],
         'slot_uri': 'rdf:type'} })
    study_description: Optional[str] = Field(default=None, description="""Generic study description""", json_schema_extra = { "linkml_meta": {'alias': 'study_description',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Study']} })
    inclusion_exclusion_criteria: Optional[str] = Field(default=None, description="""List of criteria for inclusion/exclusion for the study""", json_schema_extra = { "linkml_meta": {'alias': 'inclusion_exclusion_criteria',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Investigation', 'Study']} })
    grants: Optional[str] = Field(default=None, description="""Funding agencies and grant numbers""", json_schema_extra = { "linkml_meta": {'alias': 'grants',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Study']} })
    study_contact: Optional[str] = Field(default=None, description="""Full contact information of the contact persons for this study This should include an e-mail address and a persistent identifier such as an ORCID ID.""", json_schema_extra = { "linkml_meta": {'alias': 'study_contact',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Study']} })
    collected_by: Optional[str] = Field(default=None, description="""Full contact information of the data collector, i.e. the person who is legally responsible for data collection and release. This should include an e-mail address and a persistent identifier such as an ORCID ID.""", json_schema_extra = { "linkml_meta": {'alias': 'collected_by',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Study']} })
    lab_name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'lab_name',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['GermlineSet', 'Study']} })
    lab_address: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'lab_address',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['AlleleDescription', 'GermlineSet', 'Study']} })
    submitted_by: Optional[str] = Field(default=None, description="""Full contact information of the data depositor, i.e., the person submitting the data to a repository. This should include an e-mail address and a persistent identifier such as an ORCID ID. This is supposed to be a short-lived and technical role until the submission is relased.""", json_schema_extra = { "linkml_meta": {'alias': 'submitted_by',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Study']} })
    pub_ids: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'pub_ids',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['GermlineSet', 'Study']} })
    keywords_study: Optional[list[KeywordsStudyEnum]] = Field(default=None, description="""Keywords describing properties of one or more data sets in a study. \"contains_schema\" keywords indicate that the study contains data objects from the AIRR Schema of that type (Rearrangement, Clone, Cell, Receptor) while the other keywords indicate that the study design considers the type of data indicated (e.g. it is possible to have a study that \"contains_paired_chain\" but does not \"contains_schema_cell\").""", json_schema_extra = { "linkml_meta": {'alias': 'keywords_study',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Study']} })
    adc_publish_date: Optional[datetime ] = Field(default=None, description="""Date the study was first published in the AIRR Data Commons.""", json_schema_extra = { "linkml_meta": {'alias': 'adc_publish_date',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Study']} })
    adc_update_date: Optional[datetime ] = Field(default=None, description="""Date the study data was updated in the AIRR Data Commons.""", json_schema_extra = { "linkml_meta": {'alias': 'adc_update_date',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Study']} })


class Subject(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    subject_id: Optional[str] = Field(default=None, description="""Subject ID assigned by submitter, unique within study. If possible, a persistent subject ID linked to an INSDC or similar repository study should be used.""", json_schema_extra = { "linkml_meta": {'alias': 'subject_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Subject']} })
    synthetic: Optional[bool] = Field(default=None, description="""TRUE for libraries in which the diversity has been synthetically generated (e.g. phage display)""", json_schema_extra = { "linkml_meta": {'alias': 'synthetic',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Subject']} })
    species: Optional[SpeciesOntology] = Field(default=None, description="""Binomial designation of subject's species""", json_schema_extra = { "linkml_meta": {'alias': 'species',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Participant',
                       'Chain',
                       'AlleleDescription',
                       'GermlineSet',
                       'Subject']} })
    sex: Optional[SexEnum] = Field(default=None, description="""Biological sex of subject""", json_schema_extra = { "linkml_meta": {'alias': 'sex',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Participant', 'Subject']} })
    age_min: Optional[float] = Field(default=None, description="""Specific age or lower boundary of age range.""", json_schema_extra = { "linkml_meta": {'alias': 'age_min',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Subject']} })
    age_max: Optional[float] = Field(default=None, description="""Upper boundary of age range or equal to age_min for specific age. This field should only be null if age_min is null.""", json_schema_extra = { "linkml_meta": {'alias': 'age_max',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Subject']} })
    age_unit: Optional[AgeUnitOntology] = Field(default=None, description="""Unit of age range""", json_schema_extra = { "linkml_meta": {'alias': 'age_unit',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Participant', 'Subject']} })
    age_event: Optional[str] = Field(default=None, description="""Event in the study schedule to which `Age` refers. For NCBI BioSample this MUST be `sampling`. For other implementations submitters need to be aware that there is currently no mechanism to encode to potential delta between `Age event` and `Sample collection time`, hence the chosen events should be in temporal proximity.""", json_schema_extra = { "linkml_meta": {'alias': 'age_event',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Participant', 'Subject']} })
    ancestry_population: Optional[str] = Field(default=None, description="""Broad geographic origin of ancestry (continent)""", json_schema_extra = { "linkml_meta": {'alias': 'ancestry_population',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Subject']} })
    ethnicity: Optional[str] = Field(default=None, description="""Ethnic group of subject (defined as cultural/language-based membership)""", json_schema_extra = { "linkml_meta": {'alias': 'ethnicity',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Participant', 'Subject']} })
    race: Optional[str] = Field(default=None, description="""Racial group of subject (as defined by NIH)""", json_schema_extra = { "linkml_meta": {'alias': 'race',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Participant', 'Subject']} })
    strain_name: Optional[str] = Field(default=None, description="""Non-human designation of the strain or breed of animal used""", json_schema_extra = { "linkml_meta": {'alias': 'strain_name',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Subject']} })
    linked_subjects: Optional[str] = Field(default=None, description="""Subject ID to which `Relation type` refers""", json_schema_extra = { "linkml_meta": {'alias': 'linked_subjects',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Subject']} })
    link_type: Optional[str] = Field(default=None, description="""Relation between subject and `linked_subjects`, can be genetic or environmental (e.g.exposure)""", json_schema_extra = { "linkml_meta": {'alias': 'link_type',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Subject'],
         'slot_uri': 'rdf:type'} })
    diagnosis: Optional[list[Diagnosis]] = Field(default=None, description="""Diagnosis information for subject""", json_schema_extra = { "linkml_meta": {'alias': 'diagnosis',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Subject']} })
    genotype: Optional[SubjectGenotype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'genotype',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Subject']} })


class Diagnosis(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    study_group_description: Optional[str] = Field(default=None, description="""Designation of study arm to which the subject is assigned to""", json_schema_extra = { "linkml_meta": {'alias': 'study_group_description',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Diagnosis']} })
    disease_diagnosis: Optional[DiseaseDiagnosisOntology] = Field(default=None, description="""Diagnosis of subject""", json_schema_extra = { "linkml_meta": {'alias': 'disease_diagnosis',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Diagnosis']} })
    disease_length: Optional[str] = Field(default=None, description="""Time duration between initial diagnosis and current intervention""", json_schema_extra = { "linkml_meta": {'alias': 'disease_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Diagnosis']} })
    disease_stage: Optional[str] = Field(default=None, description="""Stage of disease at current intervention""", json_schema_extra = { "linkml_meta": {'alias': 'disease_stage',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['ImmuneExposure', 'Diagnosis']} })
    prior_therapies: Optional[str] = Field(default=None, description="""List of all relevant previous therapies applied to subject for treatment of `Diagnosis`""", json_schema_extra = { "linkml_meta": {'alias': 'prior_therapies',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Diagnosis']} })
    immunogen: Optional[str] = Field(default=None, description="""Antigen, vaccine or drug applied to subject at this intervention""", json_schema_extra = { "linkml_meta": {'alias': 'immunogen',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Diagnosis']} })
    intervention: Optional[str] = Field(default=None, description="""Description of intervention""", json_schema_extra = { "linkml_meta": {'alias': 'intervention',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Diagnosis']} })
    medical_history: Optional[str] = Field(default=None, description="""Medical history of subject that is relevant to assess the course of disease and/or treatment""", json_schema_extra = { "linkml_meta": {'alias': 'medical_history',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Diagnosis']} })


class Sample(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    sample_id: Optional[str] = Field(default=None, description="""Sample ID assigned by submitter, unique within study. If possible, a persistent sample ID linked to INSDC or similar repository study should be used.""", json_schema_extra = { "linkml_meta": {'alias': 'sample_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Sample', 'SampleProcessing']} })
    sample_type: Optional[str] = Field(default=None, description="""The way the sample was obtained, e.g. fine-needle aspirate, organ harvest, peripheral venous puncture""", json_schema_extra = { "linkml_meta": {'alias': 'sample_type',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Sample', 'SampleProcessing'],
         'slot_uri': 'rdf:type'} })
    tissue: Optional[TissueOntology] = Field(default=None, description="""The actual tissue sampled, e.g. lymph node, liver, peripheral blood""", json_schema_extra = { "linkml_meta": {'alias': 'tissue',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Specimen', 'Sample', 'SampleProcessing']} })
    anatomic_site: Optional[str] = Field(default=None, description="""The anatomic location of the tissue, e.g. Inguinal, femur""", json_schema_extra = { "linkml_meta": {'alias': 'anatomic_site',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Sample', 'SampleProcessing']} })
    disease_state_sample: Optional[str] = Field(default=None, description="""Histopathologic evaluation of the sample""", json_schema_extra = { "linkml_meta": {'alias': 'disease_state_sample',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Sample', 'SampleProcessing']} })
    collection_time_point_relative: Optional[float] = Field(default=None, description="""Time point at which sample was taken, relative to `Collection time event`""", json_schema_extra = { "linkml_meta": {'alias': 'collection_time_point_relative',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Sample', 'SampleProcessing']} })
    collection_time_point_relative_unit: Optional[CollectionTimePointRelativeUnitOntology] = Field(default=None, description="""Unit of Sample collection time""", json_schema_extra = { "linkml_meta": {'alias': 'collection_time_point_relative_unit',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Sample', 'SampleProcessing']} })
    collection_time_point_reference: Optional[str] = Field(default=None, description="""Event in the study schedule to which `Sample collection time` relates to""", json_schema_extra = { "linkml_meta": {'alias': 'collection_time_point_reference',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Sample', 'SampleProcessing']} })
    biomaterial_provider: Optional[str] = Field(default=None, description="""Name and address of the entity providing the sample""", json_schema_extra = { "linkml_meta": {'alias': 'biomaterial_provider',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Sample', 'SampleProcessing']} })


class CellProcessing(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    tissue_processing: Optional[str] = Field(default=None, description="""Enzymatic digestion and/or physical methods used to isolate cells from sample""", json_schema_extra = { "linkml_meta": {'alias': 'tissue_processing',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_subset: Optional[CellSubsetOntology] = Field(default=None, description="""Commonly-used designation of isolated cell population""", json_schema_extra = { "linkml_meta": {'alias': 'cell_subset',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_phenotype: Optional[str] = Field(default=None, description="""List of cellular markers and their expression levels used to isolate the cell population""", json_schema_extra = { "linkml_meta": {'alias': 'cell_phenotype',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_species: Optional[CellSpeciesOntology] = Field(default=None, description="""Binomial designation of the species from which the analyzed cells originate. Typically, this value should be identical to `species`, in which case it SHOULD NOT be set explicitly. However, there are valid experimental setups in which the two might differ, e.g., chimeric animal models. If set, this key will overwrite the `species` information for all lower layers of the schema.""", json_schema_extra = { "linkml_meta": {'alias': 'cell_species',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    single_cell: Optional[bool] = Field(default=None, description="""TRUE if single cells were isolated into separate compartments""", json_schema_extra = { "linkml_meta": {'alias': 'single_cell',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_number: Optional[int] = Field(default=None, description="""Total number of cells that went into the experiment""", json_schema_extra = { "linkml_meta": {'alias': 'cell_number',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cells_per_reaction: Optional[int] = Field(default=None, description="""Number of cells for each biological replicate""", json_schema_extra = { "linkml_meta": {'alias': 'cells_per_reaction',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_storage: Optional[bool] = Field(default=None, description="""TRUE if cells were cryo-preserved between isolation and further processing""", json_schema_extra = { "linkml_meta": {'alias': 'cell_storage',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_quality: Optional[str] = Field(default=None, description="""Relative amount of viable cells after preparation and (if applicable) thawing""", json_schema_extra = { "linkml_meta": {'alias': 'cell_quality',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_isolation: Optional[str] = Field(default=None, description="""Description of the procedure used for marker-based isolation or enrich cells""", json_schema_extra = { "linkml_meta": {'alias': 'cell_isolation',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_processing_protocol: Optional[str] = Field(default=None, description="""Description of the methods applied to the sample including cell preparation/ isolation/enrichment and nucleic acid extraction. This should closely mirror the Materials and methods section in the manuscript.""", json_schema_extra = { "linkml_meta": {'alias': 'cell_processing_protocol',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })


class PCRTarget(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    pcr_target_locus: Optional[PcrTargetLocusEnum] = Field(default=None, description="""Designation of the target locus. Note that this field uses a controlled vocubulary that is meant to provide a generic classification of the locus, not necessarily the correct designation according to a specific nomenclature.""", json_schema_extra = { "linkml_meta": {'alias': 'pcr_target_locus',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['PCRTarget']} })
    forward_pcr_primer_target_location: Optional[str] = Field(default=None, description="""Position of the most distal nucleotide templated by the forward primer or primer mix""", json_schema_extra = { "linkml_meta": {'alias': 'forward_pcr_primer_target_location',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['PCRTarget']} })
    reverse_pcr_primer_target_location: Optional[str] = Field(default=None, description="""Position of the most proximal nucleotide templated by the reverse primer or primer mix""", json_schema_extra = { "linkml_meta": {'alias': 'reverse_pcr_primer_target_location',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['PCRTarget']} })


class NucleicAcidProcessing(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    template_class: Optional[TemplateClassEnum] = Field(default=None, description="""The class of nucleic acid that was used as primary starting material for the following procedures""", json_schema_extra = { "linkml_meta": {'alias': 'template_class',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    template_quality: Optional[str] = Field(default=None, description="""Description and results of the quality control performed on the template material""", json_schema_extra = { "linkml_meta": {'alias': 'template_quality',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    template_amount: Optional[float] = Field(default=None, description="""Amount of template that went into the process""", json_schema_extra = { "linkml_meta": {'alias': 'template_amount',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    template_amount_unit: Optional[TemplateAmountUnitOntology] = Field(default=None, description="""Unit of template amount""", json_schema_extra = { "linkml_meta": {'alias': 'template_amount_unit',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    library_generation_method: Optional[LibraryGenerationMethodEnum] = Field(default=None, description="""Generic type of library generation""", json_schema_extra = { "linkml_meta": {'alias': 'library_generation_method',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    library_generation_protocol: Optional[str] = Field(default=None, description="""Description of processes applied to substrate to obtain a library that is ready for sequencing""", json_schema_extra = { "linkml_meta": {'alias': 'library_generation_protocol',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    library_generation_kit_version: Optional[str] = Field(default=None, description="""When using a library generation protocol from a commercial provider, provide the protocol version number""", json_schema_extra = { "linkml_meta": {'alias': 'library_generation_kit_version',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    pcr_target: Optional[list[PCRTarget]] = Field(default=None, description="""If a PCR step was performed that specifically targets the IG/TR loci, the target and primer locations need to be provided here. This field holds an array of PCRTarget objects, so that multiplex PCR setups amplifying multiple loci at the same time can be annotated using one record per locus. PCR setups not targeting any specific locus must not annotate this field but select the appropriate library_generation_method instead.""", json_schema_extra = { "linkml_meta": {'alias': 'pcr_target',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    complete_sequences: Optional[CompleteSequencesEnum] = Field(default=None, description="""To be considered `complete`, the procedure used for library construction MUST generate sequences that 1) include the first V gene codon that encodes the mature polypeptide chain (i.e. after the leader sequence) and 2) include the last complete codon of the J gene (i.e. 1 bp 5' of the J->C splice site) and 3) provide sequence information for all positions between 1) and 2). To be considered `complete & untemplated`, the sections of the sequences defined in points 1) to 3) of the previous sentence MUST be untemplated, i.e. MUST NOT overlap with the primers used in library preparation. `mixed` should only be used if the procedure used for library construction will likely produce multiple categories of sequences in the given experiment. It SHOULD NOT be used as a replacement of a NULL value.""", json_schema_extra = { "linkml_meta": {'alias': 'complete_sequences',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    physical_linkage: Optional[PhysicalLinkageEnum] = Field(default=None, description="""In case an experimental setup is used that physically links nucleic acids derived from distinct `Rearrangements` before library preparation, this field describes the mode of that linkage. All `hetero_*` terms indicate that in case of paired-read sequencing, the two reads should be expected to map to distinct IG/TR loci. `*_head-head` refers to techniques that link the 5' ends of transcripts in a single-cell context. `*_tail-head` refers to techniques that link the 3' end of one transcript to the 5' end of another one in a single-cell context. This term does not provide any information whether a continuous reading-frame between the two is generated. `*_prelinked` refers to constructs in which the linkage was already present on the DNA level (e.g. scFv).""", json_schema_extra = { "linkml_meta": {'alias': 'physical_linkage',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })


class LibraryPreparationProcessing(NucleicAcidProcessing, SpecimenProcessing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:00000711',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema',
         'mixins': ['NucleicAcidProcessing']})

    template_class: Optional[TemplateClassEnum] = Field(default=None, description="""The class of nucleic acid that was used as primary starting material for the following procedures""", json_schema_extra = { "linkml_meta": {'alias': 'template_class',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    template_quality: Optional[str] = Field(default=None, description="""Description and results of the quality control performed on the template material""", json_schema_extra = { "linkml_meta": {'alias': 'template_quality',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    template_amount: Optional[float] = Field(default=None, description="""Amount of template that went into the process""", json_schema_extra = { "linkml_meta": {'alias': 'template_amount',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    template_amount_unit: Optional[TemplateAmountUnitOntology] = Field(default=None, description="""Unit of template amount""", json_schema_extra = { "linkml_meta": {'alias': 'template_amount_unit',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    library_generation_method: Optional[LibraryGenerationMethodEnum] = Field(default=None, description="""Generic type of library generation""", json_schema_extra = { "linkml_meta": {'alias': 'library_generation_method',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    library_generation_protocol: Optional[str] = Field(default=None, description="""Description of processes applied to substrate to obtain a library that is ready for sequencing""", json_schema_extra = { "linkml_meta": {'alias': 'library_generation_protocol',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    library_generation_kit_version: Optional[str] = Field(default=None, description="""When using a library generation protocol from a commercial provider, provide the protocol version number""", json_schema_extra = { "linkml_meta": {'alias': 'library_generation_kit_version',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    pcr_target: Optional[list[PCRTarget]] = Field(default=None, description="""If a PCR step was performed that specifically targets the IG/TR loci, the target and primer locations need to be provided here. This field holds an array of PCRTarget objects, so that multiplex PCR setups amplifying multiple loci at the same time can be annotated using one record per locus. PCR setups not targeting any specific locus must not annotate this field but select the appropriate library_generation_method instead.""", json_schema_extra = { "linkml_meta": {'alias': 'pcr_target',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    complete_sequences: Optional[CompleteSequencesEnum] = Field(default=None, description="""To be considered `complete`, the procedure used for library construction MUST generate sequences that 1) include the first V gene codon that encodes the mature polypeptide chain (i.e. after the leader sequence) and 2) include the last complete codon of the J gene (i.e. 1 bp 5' of the J->C splice site) and 3) provide sequence information for all positions between 1) and 2). To be considered `complete & untemplated`, the sections of the sequences defined in points 1) to 3) of the previous sentence MUST be untemplated, i.e. MUST NOT overlap with the primers used in library preparation. `mixed` should only be used if the procedure used for library construction will likely produce multiple categories of sequences in the given experiment. It SHOULD NOT be used as a replacement of a NULL value.""", json_schema_extra = { "linkml_meta": {'alias': 'complete_sequences',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    physical_linkage: Optional[PhysicalLinkageEnum] = Field(default=None, description="""In case an experimental setup is used that physically links nucleic acids derived from distinct `Rearrangements` before library preparation, this field describes the mode of that linkage. All `hetero_*` terms indicate that in case of paired-read sequencing, the two reads should be expected to map to distinct IG/TR loci. `*_head-head` refers to techniques that link the 5' ends of transcripts in a single-cell context. `*_tail-head` refers to techniques that link the 3' end of one transcript to the 5' end of another one in a single-cell context. This term does not provide any information whether a continuous reading-frame between the two is generated. `*_prelinked` refers to constructs in which the linkage was already present on the DNA level (e.g. scFv).""", json_schema_extra = { "linkml_meta": {'alias': 'physical_linkage',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    specimen: Optional[str] = Field(default=None, description="""The specimen that was input for an assay""", json_schema_extra = { "linkml_meta": {'alias': 'specimen',
         'domain_of': ['SpecimenCollection', 'SpecimenProcessing', 'Assay'],
         'slot_uri': 'OBI:0000293'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class SequencingRun(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    sequencing_run_id: Optional[str] = Field(default=None, description="""ID of sequencing run assigned by the sequencing facility""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_run_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    total_reads_passing_qc_filter: Optional[int] = Field(default=None, description="""Number of usable reads for analysis""", json_schema_extra = { "linkml_meta": {'alias': 'total_reads_passing_qc_filter',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    sequencing_platform: Optional[str] = Field(default=None, description="""Designation of sequencing instrument used""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_platform',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    sequencing_facility: Optional[str] = Field(default=None, description="""Name and address of sequencing facility""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_facility',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    sequencing_run_date: Optional[datetime ] = Field(default=None, description="""Date of sequencing run""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_run_date',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    sequencing_kit: Optional[str] = Field(default=None, description="""Name, manufacturer, order and lot numbers of sequencing kit""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_kit',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    sequencing_files: Optional[SequencingData] = Field(default=None, description="""Set of sequencing files produced by the sequencing run""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_files',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })


class AIRRSequencingAssay(SequencingRun, Assay):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0600047',
         'from_schema': 'https://github.com/airr-knowledge/ak-schema',
         'mixins': ['SequencingRun'],
         'slot_usage': {'sequencing_files': {'name': 'sequencing_files',
                                             'range': 'AIRRSequencingData'}}})

    repertoire_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'repertoire_id',
         'domain_of': ['AIRRSequencingAssay',
                       'Repertoire',
                       'RepertoireFilter',
                       'Rearrangement',
                       'Clone',
                       'Cell',
                       'CellExpression']} })
    tcell_receptors: Optional[list[str]] = Field(default=None, description="""The T cell receptors being measured""", json_schema_extra = { "linkml_meta": {'alias': 'tcell_receptors',
         'domain_of': ['AIRRSequencingAssay', 'TCellReceptorEpitopeBindingAssay']} })
    tcell_chains: Optional[list[str]] = Field(default=None, description="""The T cell receptor chains being measured""", json_schema_extra = { "linkml_meta": {'alias': 'tcell_chains', 'domain_of': ['AIRRSequencingAssay']} })
    sequencing_run_id: Optional[str] = Field(default=None, description="""ID of sequencing run assigned by the sequencing facility""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_run_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    total_reads_passing_qc_filter: Optional[int] = Field(default=None, description="""Number of usable reads for analysis""", json_schema_extra = { "linkml_meta": {'alias': 'total_reads_passing_qc_filter',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    sequencing_platform: Optional[str] = Field(default=None, description="""Designation of sequencing instrument used""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_platform',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    sequencing_facility: Optional[str] = Field(default=None, description="""Name and address of sequencing facility""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_facility',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    sequencing_run_date: Optional[datetime ] = Field(default=None, description="""Date of sequencing run""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_run_date',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    sequencing_kit: Optional[str] = Field(default=None, description="""Name, manufacturer, order and lot numbers of sequencing kit""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_kit',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    sequencing_files: Optional[str] = Field(default=None, description="""Set of sequencing files produced by the sequencing run""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_files',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    specimen: Optional[str] = Field(default=None, description="""The specimen that was input for an assay""", json_schema_extra = { "linkml_meta": {'alias': 'specimen',
         'domain_of': ['SpecimenCollection', 'SpecimenProcessing', 'Assay'],
         'slot_uri': 'OBI:0000293'} })
    specimen_processing: Optional[list[str]] = Field(default=None, description="""A series of zero or more specimen processing steps that precede an assay""", json_schema_extra = { "linkml_meta": {'alias': 'specimen_processing',
         'domain_of': ['Assay'],
         'slot_uri': 'BFO:0000051'} })
    type: Literal["AIRRSequencingAssay"] = Field(default="AIRRSequencingAssay", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['LifeEvent', 'Assay', 'AKDataItem', 'TCellReceptor', 'Epitope']} })
    assay_type: Optional[AssayTypeOntology] = Field(default=None, description="""The specific type of an assay""", json_schema_extra = { "linkml_meta": {'alias': 'assay_type', 'domain_of': ['Assay'], 'slot_uri': 'rdf:type'} })
    has_specified_output: Optional[str] = Field(default=None, description="""output data item""", json_schema_extra = { "linkml_meta": {'alias': 'has_specified_output', 'domain_of': ['Assay', 'InputOutputDataMap']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class SequencingData(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    sequencing_data_id: Optional[str] = Field(default=None, description="""Persistent identifier of raw data stored in an archive (e.g. INSDC run ID). Data archive should  be identified in the CURIE prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_data_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })
    file_type: Optional[FileTypeEnum] = Field(default=None, description="""File format for the raw reads or sequences""", json_schema_extra = { "linkml_meta": {'alias': 'file_type',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData'],
         'slot_uri': 'rdf:type'} })
    filename: Optional[str] = Field(default=None, description="""File name for the raw reads or sequences. The first file in paired-read sequencing.""", json_schema_extra = { "linkml_meta": {'alias': 'filename',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })
    read_direction: Optional[ReadDirectionEnum] = Field(default=None, description="""Read direction for the raw reads or sequences. The first file in paired-read sequencing.""", json_schema_extra = { "linkml_meta": {'alias': 'read_direction',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })
    read_length: Optional[int] = Field(default=None, description="""Read length in bases for the first file in paired-read sequencing""", json_schema_extra = { "linkml_meta": {'alias': 'read_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })
    paired_filename: Optional[str] = Field(default=None, description="""File name for the second file in paired-read sequencing""", json_schema_extra = { "linkml_meta": {'alias': 'paired_filename',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })
    paired_read_direction: Optional[PairedReadDirectionEnum] = Field(default=None, description="""Read direction for the second file in paired-read sequencing""", json_schema_extra = { "linkml_meta": {'alias': 'paired_read_direction',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })
    paired_read_length: Optional[int] = Field(default=None, description="""Read length in bases for the second file in paired-read sequencing""", json_schema_extra = { "linkml_meta": {'alias': 'paired_read_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })
    index_filename: Optional[str] = Field(default=None, description="""File name for the index file""", json_schema_extra = { "linkml_meta": {'alias': 'index_filename',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })
    index_length: Optional[int] = Field(default=None, description="""Read length in bases for the index file""", json_schema_extra = { "linkml_meta": {'alias': 'index_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })


class AIRRSequencingData(SequencingData, SequenceData):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema',
         'mixins': ['SequencingData']})

    sequencing_data_id: Optional[str] = Field(default=None, description="""Persistent identifier of raw data stored in an archive (e.g. INSDC run ID). Data archive should  be identified in the CURIE prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_data_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })
    file_type: Optional[FileTypeEnum] = Field(default=None, description="""File format for the raw reads or sequences""", json_schema_extra = { "linkml_meta": {'alias': 'file_type',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData'],
         'slot_uri': 'rdf:type'} })
    filename: Optional[str] = Field(default=None, description="""File name for the raw reads or sequences. The first file in paired-read sequencing.""", json_schema_extra = { "linkml_meta": {'alias': 'filename',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })
    read_direction: Optional[ReadDirectionEnum] = Field(default=None, description="""Read direction for the raw reads or sequences. The first file in paired-read sequencing.""", json_schema_extra = { "linkml_meta": {'alias': 'read_direction',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })
    read_length: Optional[int] = Field(default=None, description="""Read length in bases for the first file in paired-read sequencing""", json_schema_extra = { "linkml_meta": {'alias': 'read_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })
    paired_filename: Optional[str] = Field(default=None, description="""File name for the second file in paired-read sequencing""", json_schema_extra = { "linkml_meta": {'alias': 'paired_filename',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })
    paired_read_direction: Optional[PairedReadDirectionEnum] = Field(default=None, description="""Read direction for the second file in paired-read sequencing""", json_schema_extra = { "linkml_meta": {'alias': 'paired_read_direction',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })
    paired_read_length: Optional[int] = Field(default=None, description="""Read length in bases for the second file in paired-read sequencing""", json_schema_extra = { "linkml_meta": {'alias': 'paired_read_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })
    index_filename: Optional[str] = Field(default=None, description="""File name for the index file""", json_schema_extra = { "linkml_meta": {'alias': 'index_filename',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })
    index_length: Optional[int] = Field(default=None, description="""Read length in bases for the index file""", json_schema_extra = { "linkml_meta": {'alias': 'index_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingData']} })
    type: Literal["AIRRSequencingData"] = Field(default="AIRRSequencingData", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['LifeEvent', 'Assay', 'AKDataItem', 'TCellReceptor', 'Epitope']} })
    data_item_types: Optional[list[DataItemTypeEnum]] = Field(default=None, description="""semantic types of the data""", json_schema_extra = { "linkml_meta": {'alias': 'data_item_types', 'domain_of': ['AKDataItem']} })
    akc_id: str = Field(default=..., description="""A unique identifier for a thing in the AKC.""", json_schema_extra = { "linkml_meta": {'alias': 'akc_id', 'domain_of': ['AKObject'], 'slot_uri': 'schema:identifier'} })


class DataProcessing(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    data_processing_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'data_processing_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DataProcessing',
                       'Alignment',
                       'Rearrangement',
                       'Clone',
                       'Cell',
                       'CellExpression']} })
    primary_annotation: Optional[bool] = Field(default=None, description="""If true, indicates this is the primary or default data processing for the repertoire and its rearrangements. If false, indicates this is a secondary or additional data processing.""", json_schema_extra = { "linkml_meta": {'alias': 'primary_annotation',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['DataProcessing']} })
    software_versions: Optional[str] = Field(default=None, description="""Version number and / or date, include company pipelines""", json_schema_extra = { "linkml_meta": {'alias': 'software_versions',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DataProcessing']} })
    paired_reads_assembly: Optional[str] = Field(default=None, description="""How paired end reads were assembled into a single receptor sequence""", json_schema_extra = { "linkml_meta": {'alias': 'paired_reads_assembly',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DataProcessing']} })
    quality_thresholds: Optional[str] = Field(default=None, description="""How/if sequences were removed from (4) based on base quality scores""", json_schema_extra = { "linkml_meta": {'alias': 'quality_thresholds',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DataProcessing']} })
    primer_match_cutoffs: Optional[str] = Field(default=None, description="""How primers were identified in the sequences, were they removed/masked/etc?""", json_schema_extra = { "linkml_meta": {'alias': 'primer_match_cutoffs',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DataProcessing']} })
    collapsing_method: Optional[str] = Field(default=None, description="""The method used for combining multiple sequences from (4) into a single sequence in (5)""", json_schema_extra = { "linkml_meta": {'alias': 'collapsing_method',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DataProcessing']} })
    data_processing_protocols: Optional[str] = Field(default=None, description="""General description of how QC is performed""", json_schema_extra = { "linkml_meta": {'alias': 'data_processing_protocols',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DataProcessing']} })
    data_processing_files: Optional[list[str]] = Field(default=None, description="""Array of file names for data produced by this data processing.""", json_schema_extra = { "linkml_meta": {'alias': 'data_processing_files',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DataProcessing']} })
    germline_database: Optional[str] = Field(default=None, description="""Source of germline V(D)J genes with version number or date accessed.""", json_schema_extra = { "linkml_meta": {'alias': 'germline_database',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DataProcessing']} })
    germline_set_ref: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'germline_set_ref',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['GermlineSet',
                       'DocumentedAllele',
                       'DeletedGene',
                       'DataProcessing']} })
    analysis_provenance_id: Optional[str] = Field(default=None, description="""Identifier for machine-readable PROV model of analysis provenance""", json_schema_extra = { "linkml_meta": {'alias': 'analysis_provenance_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DataProcessing']} })


class Repertoire(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    repertoire_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'repertoire_id',
         'domain_of': ['AIRRSequencingAssay',
                       'Repertoire',
                       'RepertoireFilter',
                       'Rearrangement',
                       'Clone',
                       'Cell',
                       'CellExpression']} })
    repertoire_name: Optional[str] = Field(default=None, description="""Short generic display name for the repertoire""", json_schema_extra = { "linkml_meta": {'alias': 'repertoire_name',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Repertoire']} })
    repertoire_description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'repertoire_description',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Repertoire', 'RepertoireFilter']} })
    study: Optional[Study] = Field(default=None, description="""Study object""", json_schema_extra = { "linkml_meta": {'alias': 'study',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Repertoire']} })
    subject: Optional[Subject] = Field(default=None, description="""Subject object""", json_schema_extra = { "linkml_meta": {'alias': 'subject',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Repertoire']} })
    sample: Optional[list[SampleProcessing]] = Field(default=None, description="""List of Sample Processing objects""", json_schema_extra = { "linkml_meta": {'alias': 'sample',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Repertoire']} })
    data_processing: Optional[list[DataProcessing]] = Field(default=None, description="""List of Data Processing objects""", json_schema_extra = { "linkml_meta": {'alias': 'data_processing',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Repertoire']} })


class RepertoireFilter(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    repertoire_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'repertoire_id',
         'domain_of': ['AIRRSequencingAssay',
                       'Repertoire',
                       'RepertoireFilter',
                       'Rearrangement',
                       'Clone',
                       'Cell',
                       'CellExpression']} })
    repertoire_description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'repertoire_description',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Repertoire', 'RepertoireFilter']} })
    time_point: Optional[TimePoint] = Field(default=None, description="""Time point designation for this repertoire within the group""", json_schema_extra = { "linkml_meta": {'alias': 'time_point',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RepertoireFilter']} })


class RepertoireGroup(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    repertoire_group_id: Optional[str] = Field(default=None, description="""Identifier for this repertoire collection""", json_schema_extra = { "linkml_meta": {'alias': 'repertoire_group_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RepertoireGroup']} })
    repertoire_group_name: Optional[str] = Field(default=None, description="""Short display name for this repertoire collection""", json_schema_extra = { "linkml_meta": {'alias': 'repertoire_group_name',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RepertoireGroup']} })
    repertoire_group_description: Optional[str] = Field(default=None, description="""Repertoire collection description""", json_schema_extra = { "linkml_meta": {'alias': 'repertoire_group_description',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RepertoireGroup']} })
    repertoires: Optional[list[RepertoireFilter]] = Field(default=None, description="""List of repertoires in this collection with an associated description and time point designation""", json_schema_extra = { "linkml_meta": {'alias': 'repertoires',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RepertoireGroup']} })


class Alignment(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    sequence_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sequence_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RearrangedSequence',
                       'UnrearrangedSequence',
                       'Alignment',
                       'Rearrangement',
                       'Node']} })
    segment: Optional[str] = Field(default=None, description="""The segment for this alignment. One of V, D, J or C.""", json_schema_extra = { "linkml_meta": {'alias': 'segment',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Alignment']} })
    rev_comp: Optional[bool] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'rev_comp',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Alignment', 'Rearrangement']} })
    call: Optional[str] = Field(default=None, description="""Gene assignment with allele.""", json_schema_extra = { "linkml_meta": {'alias': 'call',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Alignment']} })
    score: Optional[float] = Field(default=None, description="""Alignment score.""", json_schema_extra = { "linkml_meta": {'alias': 'score',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Alignment']} })
    identity: Optional[float] = Field(default=None, description="""Alignment fractional identity.""", json_schema_extra = { "linkml_meta": {'alias': 'identity',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Alignment']} })
    support: Optional[float] = Field(default=None, description="""Alignment E-value, p-value, likelihood, probability or other similar measure of support for the gene assignment as defined by the alignment tool.""", json_schema_extra = { "linkml_meta": {'alias': 'support',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Alignment']} })
    cigar: Optional[str] = Field(default=None, description="""Alignment CIGAR string.""", json_schema_extra = { "linkml_meta": {'alias': 'cigar',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Alignment']} })
    sequence_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sequence_start', 'domain_of': ['RearrangedSequence', 'Alignment']} })
    sequence_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sequence_end', 'domain_of': ['RearrangedSequence', 'Alignment']} })
    germline_start: Optional[int] = Field(default=None, description="""Alignment start position in the reference sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'germline_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Alignment']} })
    germline_end: Optional[int] = Field(default=None, description="""Alignment end position in the reference sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'germline_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Alignment']} })
    rank: Optional[int] = Field(default=None, description="""Alignment rank.""", json_schema_extra = { "linkml_meta": {'alias': 'rank',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Alignment']} })
    data_processing_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'data_processing_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DataProcessing',
                       'Alignment',
                       'Rearrangement',
                       'Clone',
                       'Cell',
                       'CellExpression']} })


class Rearrangement(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    sequence_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sequence_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RearrangedSequence',
                       'UnrearrangedSequence',
                       'Alignment',
                       'Rearrangement',
                       'Node']} })
    sequence: Optional[str] = Field(default=None, description="""Nucleotide sequence.""", json_schema_extra = { "linkml_meta": {'alias': 'sequence',
         'domain_of': ['Chain',
                       'RearrangedSequence',
                       'UnrearrangedSequence',
                       'AlleleDescription',
                       'UndocumentedAllele',
                       'Rearrangement']} })
    quality: Optional[str] = Field(default=None, description="""The Sanger/Phred quality scores for assessment of sequence quality. Phred quality scores from 0 to 93 are encoded using ASCII 33 to 126 (Used by Illumina from v1.8.)""", json_schema_extra = { "linkml_meta": {'alias': 'quality',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    sequence_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the query nucleotide sequence.""", json_schema_extra = { "linkml_meta": {'alias': 'sequence_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'PeptidicEpitope', 'Rearrangement']} })
    rev_comp: Optional[bool] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'rev_comp',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Alignment', 'Rearrangement']} })
    productive: Optional[bool] = Field(default=None, description="""True if the V(D)J sequence is predicted to be productive.""", json_schema_extra = { "linkml_meta": {'alias': 'productive',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    vj_in_frame: Optional[bool] = Field(default=None, description="""True if the V and J gene alignments are in-frame.""", json_schema_extra = { "linkml_meta": {'alias': 'vj_in_frame',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    stop_codon: Optional[bool] = Field(default=None, description="""True if the aligned sequence contains a stop codon.""", json_schema_extra = { "linkml_meta": {'alias': 'stop_codon',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    complete_vdj: Optional[bool] = Field(default=None, description="""Complete VDJ flag.""", json_schema_extra = { "linkml_meta": {'alias': 'complete_vdj', 'domain_of': ['Chain', 'Rearrangement']} })
    locus: Optional[LocusEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'locus',
         'domain_of': ['Chain',
                       'AlleleDescription',
                       'GermlineSet',
                       'Genotype',
                       'Rearrangement']} })
    v_call: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'v_call',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement', 'Clone']} })
    d_call: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'd_call',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement', 'Clone']} })
    d2_call: Optional[str] = Field(default=None, description="""Second D gene with allele. If referring to a known reference sequence in a database the relevant gene/allele nomenclature should be followed (e.g., IGHD3-10*01 if using IMGT/GENE-DB).""", json_schema_extra = { "linkml_meta": {'alias': 'd2_call',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    j_call: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'j_call',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement', 'Clone']} })
    c_call: Optional[str] = Field(default=None, description="""Constant region gene with allele. If referring to a known reference sequence in a database the relevant gene/allele nomenclature should be followed (e.g., IGHG1*01 if using IMGT/GENE-DB).""", json_schema_extra = { "linkml_meta": {'alias': 'c_call',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement']} })
    sequence_alignment: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sequence_alignment',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Node']} })
    quality_alignment: Optional[str] = Field(default=None, description="""Sanger/Phred quality scores for assessment of sequence_alignment quality. Phred quality scores from 0 to 93 are encoded using ASCII 33 to 126 (Used by Illumina from v1.8.)""", json_schema_extra = { "linkml_meta": {'alias': 'quality_alignment',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    sequence_alignment_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the aligned query sequence.""", json_schema_extra = { "linkml_meta": {'alias': 'sequence_alignment_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    germline_alignment: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'germline_alignment',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    germline_alignment_aa: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'germline_alignment_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    junction: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'junction',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone', 'Node']} })
    junction_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the junction.""", json_schema_extra = { "linkml_meta": {'alias': 'junction_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement', 'Clone', 'Node']} })
    np1: Optional[str] = Field(default=None, description="""Nucleotide sequence of the combined N/P region between the V gene and first D gene alignment or between the V gene and J gene alignments.""", json_schema_extra = { "linkml_meta": {'alias': 'np1',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    np1_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the np1 field.""", json_schema_extra = { "linkml_meta": {'alias': 'np1_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    np2: Optional[str] = Field(default=None, description="""Nucleotide sequence of the combined N/P region between either the first D gene and J gene alignments or the first D gene and second D gene alignments.""", json_schema_extra = { "linkml_meta": {'alias': 'np2',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    np2_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the np2 field.""", json_schema_extra = { "linkml_meta": {'alias': 'np2_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    np3: Optional[str] = Field(default=None, description="""Nucleotide sequence of the combined N/P region between the second D gene and J gene alignments.""", json_schema_extra = { "linkml_meta": {'alias': 'np3',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    np3_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the np3 field.""", json_schema_extra = { "linkml_meta": {'alias': 'np3_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    cdr1: Optional[str] = Field(default=None, description="""Nucleotide sequence of the aligned CDR1 region.""", json_schema_extra = { "linkml_meta": {'alias': 'cdr1',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    cdr1_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the cdr1 field.""", json_schema_extra = { "linkml_meta": {'alias': 'cdr1_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement']} })
    cdr2: Optional[str] = Field(default=None, description="""Nucleotide sequence of the aligned CDR2 region.""", json_schema_extra = { "linkml_meta": {'alias': 'cdr2',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    cdr2_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the cdr2 field.""", json_schema_extra = { "linkml_meta": {'alias': 'cdr2_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement']} })
    cdr3: Optional[str] = Field(default=None, description="""Nucleotide sequence of the aligned CDR3 region.""", json_schema_extra = { "linkml_meta": {'alias': 'cdr3',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    cdr3_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the cdr3 field.""", json_schema_extra = { "linkml_meta": {'alias': 'cdr3_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement']} })
    fwr1: Optional[str] = Field(default=None, description="""Nucleotide sequence of the aligned FWR1 region.""", json_schema_extra = { "linkml_meta": {'alias': 'fwr1',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    fwr1_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the fwr1 field.""", json_schema_extra = { "linkml_meta": {'alias': 'fwr1_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    fwr2: Optional[str] = Field(default=None, description="""Nucleotide sequence of the aligned FWR2 region.""", json_schema_extra = { "linkml_meta": {'alias': 'fwr2',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    fwr2_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the fwr2 field.""", json_schema_extra = { "linkml_meta": {'alias': 'fwr2_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    fwr3: Optional[str] = Field(default=None, description="""Nucleotide sequence of the aligned FWR3 region.""", json_schema_extra = { "linkml_meta": {'alias': 'fwr3',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    fwr3_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the fwr3 field.""", json_schema_extra = { "linkml_meta": {'alias': 'fwr3_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    fwr4: Optional[str] = Field(default=None, description="""Nucleotide sequence of the aligned FWR4 region.""", json_schema_extra = { "linkml_meta": {'alias': 'fwr4',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    fwr4_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the fwr4 field.""", json_schema_extra = { "linkml_meta": {'alias': 'fwr4_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    v_score: Optional[float] = Field(default=None, description="""Alignment score for the V gene.""", json_schema_extra = { "linkml_meta": {'alias': 'v_score',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    v_identity: Optional[float] = Field(default=None, description="""Fractional identity for the V gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'v_identity',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    v_support: Optional[float] = Field(default=None, description="""V gene alignment E-value, p-value, likelihood, probability or other similar measure of support for the V gene assignment as defined by the alignment tool.""", json_schema_extra = { "linkml_meta": {'alias': 'v_support',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    v_cigar: Optional[str] = Field(default=None, description="""CIGAR string for the V gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'v_cigar',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d_score: Optional[float] = Field(default=None, description="""Alignment score for the first or only D gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'd_score',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d_identity: Optional[float] = Field(default=None, description="""Fractional identity for the first or only D gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'd_identity',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d_support: Optional[float] = Field(default=None, description="""D gene alignment E-value, p-value, likelihood, probability or other similar measure of support for the first or only D gene as defined by the alignment tool.""", json_schema_extra = { "linkml_meta": {'alias': 'd_support',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d_cigar: Optional[str] = Field(default=None, description="""CIGAR string for the first or only D gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'd_cigar',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d2_score: Optional[float] = Field(default=None, description="""Alignment score for the second D gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'd2_score',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d2_identity: Optional[float] = Field(default=None, description="""Fractional identity for the second D gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'd2_identity',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d2_support: Optional[float] = Field(default=None, description="""D gene alignment E-value, p-value, likelihood, probability or other similar measure of support for the second D gene as defined by the alignment tool.""", json_schema_extra = { "linkml_meta": {'alias': 'd2_support',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d2_cigar: Optional[str] = Field(default=None, description="""CIGAR string for the second D gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'd2_cigar',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    j_score: Optional[float] = Field(default=None, description="""Alignment score for the J gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'j_score',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    j_identity: Optional[float] = Field(default=None, description="""Fractional identity for the J gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'j_identity',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    j_support: Optional[float] = Field(default=None, description="""J gene alignment E-value, p-value, likelihood, probability or other similar measure of support for the J gene assignment as defined by the alignment tool.""", json_schema_extra = { "linkml_meta": {'alias': 'j_support',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    j_cigar: Optional[str] = Field(default=None, description="""CIGAR string for the J gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'j_cigar',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    c_score: Optional[float] = Field(default=None, description="""Alignment score for the C gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'c_score',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    c_identity: Optional[float] = Field(default=None, description="""Fractional identity for the C gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'c_identity',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    c_support: Optional[float] = Field(default=None, description="""C gene alignment E-value, p-value, likelihood, probability or other similar measure of support for the C gene assignment as defined by the alignment tool.""", json_schema_extra = { "linkml_meta": {'alias': 'c_support',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    c_cigar: Optional[str] = Field(default=None, description="""CIGAR string for the C gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'c_cigar',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    v_sequence_start: Optional[int] = Field(default=None, description="""Start position of the V gene in the query sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'v_sequence_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    v_sequence_end: Optional[int] = Field(default=None, description="""End position of the V gene in the query sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'v_sequence_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    v_germline_start: Optional[int] = Field(default=None, description="""Alignment start position in the V gene reference sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'v_germline_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    v_germline_end: Optional[int] = Field(default=None, description="""Alignment end position in the V gene reference sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'v_germline_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    v_alignment_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'v_alignment_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    v_alignment_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'v_alignment_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    d_sequence_start: Optional[int] = Field(default=None, description="""Start position of the first or only D gene in the query sequence. (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'd_sequence_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d_sequence_end: Optional[int] = Field(default=None, description="""End position of the first or only D gene in the query sequence. (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'd_sequence_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d_germline_start: Optional[int] = Field(default=None, description="""Alignment start position in the D gene reference sequence for the first or only D gene (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'd_germline_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d_germline_end: Optional[int] = Field(default=None, description="""Alignment end position in the D gene reference sequence for the first or only D gene (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'd_germline_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d_alignment_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'd_alignment_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    d_alignment_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'd_alignment_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    d2_sequence_start: Optional[int] = Field(default=None, description="""Start position of the second D gene in the query sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'd2_sequence_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d2_sequence_end: Optional[int] = Field(default=None, description="""End position of the second D gene in the query sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'd2_sequence_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d2_germline_start: Optional[int] = Field(default=None, description="""Alignment start position in the second D gene reference sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'd2_germline_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d2_germline_end: Optional[int] = Field(default=None, description="""Alignment end position in the second D gene reference sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'd2_germline_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d2_alignment_start: Optional[int] = Field(default=None, description="""Start position of the second D gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'd2_alignment_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d2_alignment_end: Optional[int] = Field(default=None, description="""End position of the second D gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'd2_alignment_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    j_sequence_start: Optional[int] = Field(default=None, description="""Start position of the J gene in the query sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'j_sequence_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    j_sequence_end: Optional[int] = Field(default=None, description="""End position of the J gene in the query sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'j_sequence_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    j_germline_start: Optional[int] = Field(default=None, description="""Alignment start position in the J gene reference sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'j_germline_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    j_germline_end: Optional[int] = Field(default=None, description="""Alignment end position in the J gene reference sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'j_germline_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    j_alignment_start: Optional[int] = Field(default=None, description="""Start position of the J gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'j_alignment_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    j_alignment_end: Optional[int] = Field(default=None, description="""End position of the J gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'j_alignment_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    c_sequence_start: Optional[int] = Field(default=None, description="""Start position of the C gene in the query sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'c_sequence_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    c_sequence_end: Optional[int] = Field(default=None, description="""End position of the C gene in the query sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'c_sequence_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    c_germline_start: Optional[int] = Field(default=None, description="""Alignment start position in the C gene reference sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'c_germline_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    c_germline_end: Optional[int] = Field(default=None, description="""Alignment end position in the C gene reference sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'c_germline_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    c_alignment_start: Optional[int] = Field(default=None, description="""Start position of the C gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'c_alignment_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    c_alignment_end: Optional[int] = Field(default=None, description="""End position of the C gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'c_alignment_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    cdr1_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cdr1_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'SequenceDelineationV', 'Rearrangement']} })
    cdr1_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cdr1_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'SequenceDelineationV', 'Rearrangement']} })
    cdr2_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cdr2_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'SequenceDelineationV', 'Rearrangement']} })
    cdr2_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cdr2_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'SequenceDelineationV', 'Rearrangement']} })
    cdr3_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cdr3_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'SequenceDelineationV', 'Rearrangement']} })
    cdr3_end: Optional[int] = Field(default=None, description="""CDR3 end position in the query sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'cdr3_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement']} })
    fwr1_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'fwr1_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequenceDelineationV', 'Rearrangement']} })
    fwr1_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'fwr1_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequenceDelineationV', 'Rearrangement']} })
    fwr2_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'fwr2_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequenceDelineationV', 'Rearrangement']} })
    fwr2_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'fwr2_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequenceDelineationV', 'Rearrangement']} })
    fwr3_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'fwr3_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequenceDelineationV', 'Rearrangement']} })
    fwr3_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'fwr3_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequenceDelineationV', 'Rearrangement']} })
    fwr4_start: Optional[int] = Field(default=None, description="""FWR4 start position in the query sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'fwr4_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    fwr4_end: Optional[int] = Field(default=None, description="""FWR4 end position in the query sequence (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'fwr4_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    v_sequence_alignment: Optional[str] = Field(default=None, description="""Aligned portion of query sequence assigned to the V gene, including any indel corrections or numbering spacers.""", json_schema_extra = { "linkml_meta": {'alias': 'v_sequence_alignment',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    v_sequence_alignment_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the v_sequence_alignment field.""", json_schema_extra = { "linkml_meta": {'alias': 'v_sequence_alignment_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d_sequence_alignment: Optional[str] = Field(default=None, description="""Aligned portion of query sequence assigned to the first or only D gene, including any indel corrections or numbering spacers.""", json_schema_extra = { "linkml_meta": {'alias': 'd_sequence_alignment',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d_sequence_alignment_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the d_sequence_alignment field.""", json_schema_extra = { "linkml_meta": {'alias': 'd_sequence_alignment_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d2_sequence_alignment: Optional[str] = Field(default=None, description="""Aligned portion of query sequence assigned to the second D gene, including any indel corrections or numbering spacers.""", json_schema_extra = { "linkml_meta": {'alias': 'd2_sequence_alignment',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d2_sequence_alignment_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the d2_sequence_alignment field.""", json_schema_extra = { "linkml_meta": {'alias': 'd2_sequence_alignment_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    j_sequence_alignment: Optional[str] = Field(default=None, description="""Aligned portion of query sequence assigned to the J gene, including any indel corrections or numbering spacers.""", json_schema_extra = { "linkml_meta": {'alias': 'j_sequence_alignment',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    j_sequence_alignment_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the j_sequence_alignment field.""", json_schema_extra = { "linkml_meta": {'alias': 'j_sequence_alignment_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    c_sequence_alignment: Optional[str] = Field(default=None, description="""Aligned portion of query sequence assigned to the constant region, including any indel corrections or numbering spacers.""", json_schema_extra = { "linkml_meta": {'alias': 'c_sequence_alignment',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    c_sequence_alignment_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the c_sequence_alignment field.""", json_schema_extra = { "linkml_meta": {'alias': 'c_sequence_alignment_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    v_germline_alignment: Optional[str] = Field(default=None, description="""Aligned V gene germline sequence spanning the same region as the v_sequence_alignment field and including the same set of corrections and spacers (if any).""", json_schema_extra = { "linkml_meta": {'alias': 'v_germline_alignment',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    v_germline_alignment_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the v_germline_alignment field.""", json_schema_extra = { "linkml_meta": {'alias': 'v_germline_alignment_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d_germline_alignment: Optional[str] = Field(default=None, description="""Aligned D gene germline sequence spanning the same region as the d_sequence_alignment field and including the same set of corrections and spacers (if any).""", json_schema_extra = { "linkml_meta": {'alias': 'd_germline_alignment',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d_germline_alignment_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the d_germline_alignment field.""", json_schema_extra = { "linkml_meta": {'alias': 'd_germline_alignment_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d2_germline_alignment: Optional[str] = Field(default=None, description="""Aligned D gene germline sequence spanning the same region as the d2_sequence_alignment field and including the same set of corrections and spacers (if any).""", json_schema_extra = { "linkml_meta": {'alias': 'd2_germline_alignment',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d2_germline_alignment_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the d2_germline_alignment field.""", json_schema_extra = { "linkml_meta": {'alias': 'd2_germline_alignment_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    j_germline_alignment: Optional[str] = Field(default=None, description="""Aligned J gene germline sequence spanning the same region as the j_sequence_alignment field and including the same set of corrections and spacers (if any).""", json_schema_extra = { "linkml_meta": {'alias': 'j_germline_alignment',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    j_germline_alignment_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the j_germline_alignment field.""", json_schema_extra = { "linkml_meta": {'alias': 'j_germline_alignment_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    c_germline_alignment: Optional[str] = Field(default=None, description="""Aligned constant region germline sequence spanning the same region as the c_sequence_alignment field and including the same set of corrections and spacers (if any).""", json_schema_extra = { "linkml_meta": {'alias': 'c_germline_alignment',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    c_germline_alignment_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the c_germline_aligment field.""", json_schema_extra = { "linkml_meta": {'alias': 'c_germline_alignment_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    junction_length: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'junction_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    junction_aa_length: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'junction_aa_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    np1_length: Optional[int] = Field(default=None, description="""Number of nucleotides between the V gene and first D gene alignments or between the V gene and J gene alignments.""", json_schema_extra = { "linkml_meta": {'alias': 'np1_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    np2_length: Optional[int] = Field(default=None, description="""Number of nucleotides between either the first D gene and J gene alignments or the first D gene and second D gene alignments.""", json_schema_extra = { "linkml_meta": {'alias': 'np2_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    np3_length: Optional[int] = Field(default=None, description="""Number of nucleotides between the second D gene and J gene alignments.""", json_schema_extra = { "linkml_meta": {'alias': 'np3_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    n1_length: Optional[int] = Field(default=None, description="""Number of untemplated nucleotides 5' of the first or only D gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'n1_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    n2_length: Optional[int] = Field(default=None, description="""Number of untemplated nucleotides 3' of the first or only D gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'n2_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    n3_length: Optional[int] = Field(default=None, description="""Number of untemplated nucleotides 3' of the second D gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'n3_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    p3v_length: Optional[int] = Field(default=None, description="""Number of palindromic nucleotides 3' of the V gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'p3v_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    p5d_length: Optional[int] = Field(default=None, description="""Number of palindromic nucleotides 5' of the first or only D gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'p5d_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    p3d_length: Optional[int] = Field(default=None, description="""Number of palindromic nucleotides 3' of the first or only D gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'p3d_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    p5d2_length: Optional[int] = Field(default=None, description="""Number of palindromic nucleotides 5' of the second D gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'p5d2_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    p3d2_length: Optional[int] = Field(default=None, description="""Number of palindromic nucleotides 3' of the second D gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'p3d2_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    p5j_length: Optional[int] = Field(default=None, description="""Number of palindromic nucleotides 5' of the J gene alignment.""", json_schema_extra = { "linkml_meta": {'alias': 'p5j_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    v_frameshift: Optional[bool] = Field(default=None, description="""True if the V gene in the query nucleotide sequence contains a translational frameshift relative to the frame of the V gene reference sequence.""", json_schema_extra = { "linkml_meta": {'alias': 'v_frameshift',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    j_frameshift: Optional[bool] = Field(default=None, description="""True if the J gene in the query nucleotide sequence contains a translational frameshift relative to the frame of the J gene reference sequence.""", json_schema_extra = { "linkml_meta": {'alias': 'j_frameshift',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d_frame: Optional[int] = Field(default=None, description="""Numerical reading frame (1, 2, 3) of the first or only D gene in the query nucleotide sequence, where frame 1 is relative to the first codon of D gene reference sequence.""", json_schema_extra = { "linkml_meta": {'alias': 'd_frame',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    d2_frame: Optional[int] = Field(default=None, description="""Numerical reading frame (1, 2, 3) of the second D gene in the query nucleotide sequence, where frame 1 is relative to the first codon of D gene reference sequence.""", json_schema_extra = { "linkml_meta": {'alias': 'd2_frame',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    consensus_count: Optional[int] = Field(default=None, description="""Number of reads contributing to the UMI consensus or contig assembly for this sequence. For example, the sum of the number of reads for all UMIs that contribute to the query sequence.""", json_schema_extra = { "linkml_meta": {'alias': 'consensus_count',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    duplicate_count: Optional[int] = Field(default=None, description="""Copy number or number of duplicate observations for the query sequence. For example, the number of identical reads observed for this sequence.""", json_schema_extra = { "linkml_meta": {'alias': 'duplicate_count',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement']} })
    umi_count: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'umi_count',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    cell_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cell_id', 'domain_of': ['Rearrangement', 'Cell', 'CellExpression']} })
    clone_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'clone_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone', 'Tree']} })
    repertoire_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'repertoire_id',
         'domain_of': ['AIRRSequencingAssay',
                       'Repertoire',
                       'RepertoireFilter',
                       'Rearrangement',
                       'Clone',
                       'Cell',
                       'CellExpression']} })
    sample_processing_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sample_processing_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'SampleProcessing']} })
    data_processing_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'data_processing_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DataProcessing',
                       'Alignment',
                       'Rearrangement',
                       'Clone',
                       'Cell',
                       'CellExpression']} })


class Clone(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    clone_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'clone_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone', 'Tree']} })
    repertoire_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'repertoire_id',
         'domain_of': ['AIRRSequencingAssay',
                       'Repertoire',
                       'RepertoireFilter',
                       'Rearrangement',
                       'Clone',
                       'Cell',
                       'CellExpression']} })
    data_processing_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'data_processing_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DataProcessing',
                       'Alignment',
                       'Rearrangement',
                       'Clone',
                       'Cell',
                       'CellExpression']} })
    sequences: Optional[list[str]] = Field(default=None, description="""List sequence_id strings that act as keys to the Rearrangement records for members of the clone.""", json_schema_extra = { "linkml_meta": {'alias': 'sequences',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Clone']} })
    v_call: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'v_call',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement', 'Clone']} })
    d_call: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'd_call',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement', 'Clone']} })
    j_call: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'j_call',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement', 'Clone']} })
    junction: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'junction',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone', 'Node']} })
    junction_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the junction.""", json_schema_extra = { "linkml_meta": {'alias': 'junction_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement', 'Clone', 'Node']} })
    junction_length: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'junction_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    junction_aa_length: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'junction_aa_length',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    germline_alignment: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'germline_alignment',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    germline_alignment_aa: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'germline_alignment_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    v_alignment_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'v_alignment_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    v_alignment_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'v_alignment_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    d_alignment_start: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'd_alignment_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    d_alignment_end: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'd_alignment_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    j_alignment_start: Optional[int] = Field(default=None, description="""Start position of the J gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'j_alignment_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    j_alignment_end: Optional[int] = Field(default=None, description="""End position of the J gene alignment in both the sequence_alignment and germline_alignment fields (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'j_alignment_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    junction_start: Optional[int] = Field(default=None, description="""Junction region start position in the alignment (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'junction_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Clone']} })
    junction_end: Optional[int] = Field(default=None, description="""Junction region end position in the alignment (1-based closed interval).""", json_schema_extra = { "linkml_meta": {'alias': 'junction_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Clone']} })
    umi_count: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'umi_count',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone']} })
    clone_count: Optional[int] = Field(default=None, description="""Absolute count of the size (number of members) of this clone in the repertoire. This could simply be the number of sequences (Rearrangement records) observed in this clone, the number of distinct cell barcodes (unique cell_id values), or a more sophisticated calculation appropriate to the experimental protocol. Absolute count is provided versus a frequency so that downstream analysis tools can perform their own normalization.""", json_schema_extra = { "linkml_meta": {'alias': 'clone_count',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Clone']} })
    seed_id: Optional[str] = Field(default=None, description="""sequence_id of the seed sequence. Empty string (or null) if there is no seed sequence.""", json_schema_extra = { "linkml_meta": {'alias': 'seed_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Clone']} })


class Tree(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    tree_id: Optional[str] = Field(default=None, description="""Identifier for the tree.""", json_schema_extra = { "linkml_meta": {'alias': 'tree_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Tree']} })
    clone_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'clone_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone', 'Tree']} })
    newick: Optional[str] = Field(default=None, description="""Newick string of the tree edges.""", json_schema_extra = { "linkml_meta": {'alias': 'newick',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Tree']} })
    nodes: Optional[list[Node]] = Field(default=None, description="""Dictionary of nodes in the tree, keyed by sequence_id string""", json_schema_extra = { "linkml_meta": {'alias': 'nodes',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Tree']} })


class Node(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    sequence_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sequence_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['RearrangedSequence',
                       'UnrearrangedSequence',
                       'Alignment',
                       'Rearrangement',
                       'Node']} })
    sequence_alignment: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sequence_alignment',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Node']} })
    junction: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'junction',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'Clone', 'Node']} })
    junction_aa: Optional[str] = Field(default=None, description="""Amino acid translation of the junction.""", json_schema_extra = { "linkml_meta": {'alias': 'junction_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Chain', 'Rearrangement', 'Clone', 'Node']} })


class Cell(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    cell_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cell_id', 'domain_of': ['Rearrangement', 'Cell', 'CellExpression']} })
    rearrangements: Optional[list[str]] = Field(default=None, description="""Array of sequence identifiers defined for the Rearrangement object""", json_schema_extra = { "linkml_meta": {'alias': 'rearrangements',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Cell']} })
    receptors: Optional[list[str]] = Field(default=None, description="""Array of receptor identifiers defined for the Receptor object""", json_schema_extra = { "linkml_meta": {'alias': 'receptors',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Cell']} })
    repertoire_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'repertoire_id',
         'domain_of': ['AIRRSequencingAssay',
                       'Repertoire',
                       'RepertoireFilter',
                       'Rearrangement',
                       'Clone',
                       'Cell',
                       'CellExpression']} })
    data_processing_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'data_processing_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DataProcessing',
                       'Alignment',
                       'Rearrangement',
                       'Clone',
                       'Cell',
                       'CellExpression']} })
    expression_study_method: Optional[ExpressionStudyMethodEnum] = Field(default=None, description="""Keyword describing the methodology used to assess expression. This values for this field MUST  come from a controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'alias': 'expression_study_method',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Cell']} })
    expression_raw_doi: Optional[str] = Field(default=None, description="""DOI of raw data set containing the current event""", json_schema_extra = { "linkml_meta": {'alias': 'expression_raw_doi',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Cell']} })
    expression_index: Optional[str] = Field(default=None, description="""Index addressing the current event within the raw data set.""", json_schema_extra = { "linkml_meta": {'alias': 'expression_index',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Cell']} })
    virtual_pairing: Optional[bool] = Field(default=None, description="""boolean to indicate if pairing was inferred.""", json_schema_extra = { "linkml_meta": {'alias': 'virtual_pairing',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Cell']} })


class CellExpression(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    expression_id: Optional[str] = Field(default=None, description="""Identifier of this expression property measurement.""", json_schema_extra = { "linkml_meta": {'alias': 'expression_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['CellExpression']} })
    cell_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cell_id', 'domain_of': ['Rearrangement', 'Cell', 'CellExpression']} })
    repertoire_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'repertoire_id',
         'domain_of': ['AIRRSequencingAssay',
                       'Repertoire',
                       'RepertoireFilter',
                       'Rearrangement',
                       'Clone',
                       'Cell',
                       'CellExpression']} })
    data_processing_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'data_processing_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['DataProcessing',
                       'Alignment',
                       'Rearrangement',
                       'Clone',
                       'Cell',
                       'CellExpression']} })
    property_type: Optional[str] = Field(default=None, description="""Keyword describing the property type and detection method used to measure the property value. The following keywords are recommended, but custom property types are also valid: \"mrna_expression_by_read_count\", \"protein_expression_by_fluorescence_intensity\", \"antigen_bait_binding_by_fluorescence_intensity\", \"protein_expression_by_dna_barcode_count\" and \"antigen_bait_binding_by_dna_barcode_count\".""", json_schema_extra = { "linkml_meta": {'alias': 'property_type',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['CellExpression'],
         'slot_uri': 'rdf:type'} })
    property: Optional[str] = Field(default=None, description="""Name of the property observed, typically a gene or antibody identifier (and label) from a  canonical resource such as Ensembl (e.g. ENSG00000275747, IGHV3-79) or  Antibody Registry (ABREG:1236456, Purified anti-mouse/rat/human CD27 antibody).""", json_schema_extra = { "linkml_meta": {'alias': 'property',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellExpression']} })
    property_value: Optional[float] = Field(default=None, description="""Level at which the property was observed in the experiment (non-normalized).""", json_schema_extra = { "linkml_meta": {'alias': 'property_value',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellExpression']} })


class Receptor(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    receptor_id: Optional[str] = Field(default=None, description="""ID of the current Receptor object, unique within the local repository.""", json_schema_extra = { "linkml_meta": {'alias': 'receptor_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Receptor']} })
    receptor_hash: Optional[str] = Field(default=None, description="""The SHA256 hash of the receptor amino acid sequence, calculated on the concatenated ``receptor_variable_domain_*_aa`` sequences and represented as base16-encoded string.""", json_schema_extra = { "linkml_meta": {'alias': 'receptor_hash',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Receptor']} })
    receptor_type: Optional[ReceptorTypeEnum] = Field(default=None, description="""The top-level receptor type, either Immunoglobulin (Ig) or T Cell Receptor (TCR).""", json_schema_extra = { "linkml_meta": {'alias': 'receptor_type',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Receptor'],
         'slot_uri': 'rdf:type'} })
    receptor_variable_domain_1_aa: Optional[str] = Field(default=None, description="""Complete amino acid sequence of the mature variable domain of the Ig heavy, TCR beta or TCR delta chain. The mature variable domain is defined as encompassing all AA from and including first AA after the the signal peptide to and including the last AA that is completely encoded by the J gene.""", json_schema_extra = { "linkml_meta": {'alias': 'receptor_variable_domain_1_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Receptor']} })
    receptor_variable_domain_1_locus: Optional[ReceptorVariableDomain1LocusEnum] = Field(default=None, description="""Locus from which the variable domain in receptor_variable_domain_1_aa originates""", json_schema_extra = { "linkml_meta": {'alias': 'receptor_variable_domain_1_locus',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Receptor']} })
    receptor_variable_domain_2_aa: Optional[str] = Field(default=None, description="""Complete amino acid sequence of the mature variable domain of the Ig light, TCR alpha or TCR gamma chain. The mature variable domain is defined as encompassing all AA from and including first AA after the the signal peptide to and including the last AA that is completely encoded by the J gene.""", json_schema_extra = { "linkml_meta": {'alias': 'receptor_variable_domain_2_aa',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Receptor']} })
    receptor_variable_domain_2_locus: Optional[ReceptorVariableDomain2LocusEnum] = Field(default=None, description="""Locus from which the variable domain in receptor_variable_domain_2_aa originates""", json_schema_extra = { "linkml_meta": {'alias': 'receptor_variable_domain_2_locus',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['Receptor']} })
    receptor_ref: Optional[list[str]] = Field(default=None, description="""Array of receptor identifiers defined for the Receptor object""", json_schema_extra = { "linkml_meta": {'alias': 'receptor_ref',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Receptor']} })
    reactivity_measurements: Optional[list[ReceptorReactivity]] = Field(default=None, description="""Records of reactivity measurement""", json_schema_extra = { "linkml_meta": {'alias': 'reactivity_measurements',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Receptor']} })


class ReceptorReactivity(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    ligand_type: Optional[LigandTypeEnum] = Field(default=None, description="""Classification of ligand binding to receptor""", json_schema_extra = { "linkml_meta": {'alias': 'ligand_type',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['ReceptorReactivity'],
         'slot_uri': 'rdf:type'} })
    antigen_type: Optional[AntigenTypeEnum] = Field(default=None, description="""The type of antigen before processing by the immune system.""", json_schema_extra = { "linkml_meta": {'alias': 'antigen_type',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['ReceptorReactivity'],
         'slot_uri': 'rdf:type'} })
    antigen: Optional[str] = Field(default=None, description="""A material entity with antigen role""", json_schema_extra = { "linkml_meta": {'alias': 'antigen',
         'domain_of': ['AntibodyAntigenComplex', 'ReceptorReactivity']} })
    antigen_source_species: Optional[AntigenSourceSpeciesOntology] = Field(default=None, description="""The species from which the antigen was isolated""", json_schema_extra = { "linkml_meta": {'alias': 'antigen_source_species',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['ReceptorReactivity']} })
    peptide_start: Optional[int] = Field(default=None, description="""Start position of the peptide within the reference protein sequence""", json_schema_extra = { "linkml_meta": {'alias': 'peptide_start',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['ReceptorReactivity']} })
    peptide_end: Optional[int] = Field(default=None, description="""End position of the peptide within the reference protein sequence""", json_schema_extra = { "linkml_meta": {'alias': 'peptide_end',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['ReceptorReactivity']} })
    mhc_class: Optional[MhcClassEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'mhc_class', 'domain_of': ['MHCGenotype', 'ReceptorReactivity']} })
    mhc_gene_1: Optional[MhcGene1Ontology] = Field(default=None, description="""The MHC gene to which the mhc_allele_1 belongs""", json_schema_extra = { "linkml_meta": {'alias': 'mhc_gene_1',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['ReceptorReactivity']} })
    mhc_allele_1: Optional[str] = Field(default=None, description="""Allele designation of the MHC alpha chain""", json_schema_extra = { "linkml_meta": {'alias': 'mhc_allele_1',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['ReceptorReactivity']} })
    mhc_gene_2: Optional[MhcGene2Ontology] = Field(default=None, description="""The MHC gene to which the mhc_allele_2 belongs""", json_schema_extra = { "linkml_meta": {'alias': 'mhc_gene_2',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['ReceptorReactivity']} })
    mhc_allele_2: Optional[str] = Field(default=None, description="""Allele designation of the MHC class II beta chain or the invariant beta2-microglobin chain""", json_schema_extra = { "linkml_meta": {'alias': 'mhc_allele_2',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['ReceptorReactivity']} })
    reactivity_method: Optional[ReactivityMethodEnum] = Field(default=None, description="""The methodology used to assess expression (assay implemented in experiment)""", json_schema_extra = { "linkml_meta": {'alias': 'reactivity_method',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['ReceptorReactivity']} })
    reactivity_readout: Optional[ReactivityReadoutEnum] = Field(default=None, description="""Reactivity measurement read-out""", json_schema_extra = { "linkml_meta": {'alias': 'reactivity_readout',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['ReceptorReactivity']} })
    reactivity_value: Optional[float] = Field(default=None, description="""The absolute (processed) value of the measurement""", json_schema_extra = { "linkml_meta": {'alias': 'reactivity_value',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['ReceptorReactivity']} })
    reactivity_unit: Optional[str] = Field(default=None, description="""The unit of the measurement""", json_schema_extra = { "linkml_meta": {'alias': 'reactivity_unit',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['ReceptorReactivity']} })


class SampleProcessing(AIRRStandards):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://github.com/airr-knowledge/ak-schema'})

    sample_processing_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sample_processing_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Rearrangement', 'SampleProcessing']} })
    sample_id: Optional[str] = Field(default=None, description="""Sample ID assigned by submitter, unique within study. If possible, a persistent sample ID linked to INSDC or similar repository study should be used.""", json_schema_extra = { "linkml_meta": {'alias': 'sample_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Sample', 'SampleProcessing']} })
    sample_type: Optional[str] = Field(default=None, description="""The way the sample was obtained, e.g. fine-needle aspirate, organ harvest, peripheral venous puncture""", json_schema_extra = { "linkml_meta": {'alias': 'sample_type',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Sample', 'SampleProcessing'],
         'slot_uri': 'rdf:type'} })
    tissue: Optional[TissueOntology] = Field(default=None, description="""The actual tissue sampled, e.g. lymph node, liver, peripheral blood""", json_schema_extra = { "linkml_meta": {'alias': 'tissue',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Specimen', 'Sample', 'SampleProcessing']} })
    anatomic_site: Optional[str] = Field(default=None, description="""The anatomic location of the tissue, e.g. Inguinal, femur""", json_schema_extra = { "linkml_meta": {'alias': 'anatomic_site',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Sample', 'SampleProcessing']} })
    disease_state_sample: Optional[str] = Field(default=None, description="""Histopathologic evaluation of the sample""", json_schema_extra = { "linkml_meta": {'alias': 'disease_state_sample',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Sample', 'SampleProcessing']} })
    collection_time_point_relative: Optional[float] = Field(default=None, description="""Time point at which sample was taken, relative to `Collection time event`""", json_schema_extra = { "linkml_meta": {'alias': 'collection_time_point_relative',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Sample', 'SampleProcessing']} })
    collection_time_point_relative_unit: Optional[CollectionTimePointRelativeUnitOntology] = Field(default=None, description="""Unit of Sample collection time""", json_schema_extra = { "linkml_meta": {'alias': 'collection_time_point_relative_unit',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Sample', 'SampleProcessing']} })
    collection_time_point_reference: Optional[str] = Field(default=None, description="""Event in the study schedule to which `Sample collection time` relates to""", json_schema_extra = { "linkml_meta": {'alias': 'collection_time_point_reference',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Sample', 'SampleProcessing']} })
    biomaterial_provider: Optional[str] = Field(default=None, description="""Name and address of the entity providing the sample""", json_schema_extra = { "linkml_meta": {'alias': 'biomaterial_provider',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['Sample', 'SampleProcessing']} })
    tissue_processing: Optional[str] = Field(default=None, description="""Enzymatic digestion and/or physical methods used to isolate cells from sample""", json_schema_extra = { "linkml_meta": {'alias': 'tissue_processing',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_subset: Optional[CellSubsetOntology] = Field(default=None, description="""Commonly-used designation of isolated cell population""", json_schema_extra = { "linkml_meta": {'alias': 'cell_subset',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_phenotype: Optional[str] = Field(default=None, description="""List of cellular markers and their expression levels used to isolate the cell population""", json_schema_extra = { "linkml_meta": {'alias': 'cell_phenotype',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_species: Optional[CellSpeciesOntology] = Field(default=None, description="""Binomial designation of the species from which the analyzed cells originate. Typically, this value should be identical to `species`, in which case it SHOULD NOT be set explicitly. However, there are valid experimental setups in which the two might differ, e.g., chimeric animal models. If set, this key will overwrite the `species` information for all lower layers of the schema.""", json_schema_extra = { "linkml_meta": {'alias': 'cell_species',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    single_cell: Optional[bool] = Field(default=None, description="""TRUE if single cells were isolated into separate compartments""", json_schema_extra = { "linkml_meta": {'alias': 'single_cell',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_number: Optional[int] = Field(default=None, description="""Total number of cells that went into the experiment""", json_schema_extra = { "linkml_meta": {'alias': 'cell_number',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cells_per_reaction: Optional[int] = Field(default=None, description="""Number of cells for each biological replicate""", json_schema_extra = { "linkml_meta": {'alias': 'cells_per_reaction',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_storage: Optional[bool] = Field(default=None, description="""TRUE if cells were cryo-preserved between isolation and further processing""", json_schema_extra = { "linkml_meta": {'alias': 'cell_storage',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_quality: Optional[str] = Field(default=None, description="""Relative amount of viable cells after preparation and (if applicable) thawing""", json_schema_extra = { "linkml_meta": {'alias': 'cell_quality',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_isolation: Optional[str] = Field(default=None, description="""Description of the procedure used for marker-based isolation or enrich cells""", json_schema_extra = { "linkml_meta": {'alias': 'cell_isolation',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    cell_processing_protocol: Optional[str] = Field(default=None, description="""Description of the methods applied to the sample including cell preparation/ isolation/enrichment and nucleic acid extraction. This should closely mirror the Materials and methods section in the manuscript.""", json_schema_extra = { "linkml_meta": {'alias': 'cell_processing_protocol',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['CellIsolationProcessing', 'CellProcessing', 'SampleProcessing']} })
    template_class: Optional[TemplateClassEnum] = Field(default=None, description="""The class of nucleic acid that was used as primary starting material for the following procedures""", json_schema_extra = { "linkml_meta": {'alias': 'template_class',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    template_quality: Optional[str] = Field(default=None, description="""Description and results of the quality control performed on the template material""", json_schema_extra = { "linkml_meta": {'alias': 'template_quality',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    template_amount: Optional[float] = Field(default=None, description="""Amount of template that went into the process""", json_schema_extra = { "linkml_meta": {'alias': 'template_amount',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    template_amount_unit: Optional[TemplateAmountUnitOntology] = Field(default=None, description="""Unit of template amount""", json_schema_extra = { "linkml_meta": {'alias': 'template_amount_unit',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    library_generation_method: Optional[LibraryGenerationMethodEnum] = Field(default=None, description="""Generic type of library generation""", json_schema_extra = { "linkml_meta": {'alias': 'library_generation_method',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    library_generation_protocol: Optional[str] = Field(default=None, description="""Description of processes applied to substrate to obtain a library that is ready for sequencing""", json_schema_extra = { "linkml_meta": {'alias': 'library_generation_protocol',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    library_generation_kit_version: Optional[str] = Field(default=None, description="""When using a library generation protocol from a commercial provider, provide the protocol version number""", json_schema_extra = { "linkml_meta": {'alias': 'library_generation_kit_version',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    pcr_target: Optional[list[PCRTarget]] = Field(default=None, description="""If a PCR step was performed that specifically targets the IG/TR loci, the target and primer locations need to be provided here. This field holds an array of PCRTarget objects, so that multiplex PCR setups amplifying multiple loci at the same time can be annotated using one record per locus. PCR setups not targeting any specific locus must not annotate this field but select the appropriate library_generation_method instead.""", json_schema_extra = { "linkml_meta": {'alias': 'pcr_target',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    complete_sequences: Optional[CompleteSequencesEnum] = Field(default=None, description="""To be considered `complete`, the procedure used for library construction MUST generate sequences that 1) include the first V gene codon that encodes the mature polypeptide chain (i.e. after the leader sequence) and 2) include the last complete codon of the J gene (i.e. 1 bp 5' of the J->C splice site) and 3) provide sequence information for all positions between 1) and 2). To be considered `complete & untemplated`, the sections of the sequences defined in points 1) to 3) of the previous sentence MUST be untemplated, i.e. MUST NOT overlap with the primers used in library preparation. `mixed` should only be used if the procedure used for library construction will likely produce multiple categories of sequences in the given experiment. It SHOULD NOT be used as a replacement of a NULL value.""", json_schema_extra = { "linkml_meta": {'alias': 'complete_sequences',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    physical_linkage: Optional[PhysicalLinkageEnum] = Field(default=None, description="""In case an experimental setup is used that physically links nucleic acids derived from distinct `Rearrangements` before library preparation, this field describes the mode of that linkage. All `hetero_*` terms indicate that in case of paired-read sequencing, the two reads should be expected to map to distinct IG/TR loci. `*_head-head` refers to techniques that link the 5' ends of transcripts in a single-cell context. `*_tail-head` refers to techniques that link the 3' end of one transcript to the 5' end of another one in a single-cell context. This term does not provide any information whether a continuous reading-frame between the two is generated. `*_prelinked` refers to constructs in which the linkage was already present on the DNA level (e.g. scFv).""", json_schema_extra = { "linkml_meta": {'alias': 'physical_linkage',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['NucleicAcidProcessing', 'SampleProcessing']} })
    sequencing_run_id: Optional[str] = Field(default=None, description="""ID of sequencing run assigned by the sequencing facility""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_run_id',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    total_reads_passing_qc_filter: Optional[int] = Field(default=None, description="""Number of usable reads for analysis""", json_schema_extra = { "linkml_meta": {'alias': 'total_reads_passing_qc_filter',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    sequencing_platform: Optional[str] = Field(default=None, description="""Designation of sequencing instrument used""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_platform',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    sequencing_facility: Optional[str] = Field(default=None, description="""Name and address of sequencing facility""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_facility',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    sequencing_run_date: Optional[datetime ] = Field(default=None, description="""Date of sequencing run""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_run_date',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    sequencing_kit: Optional[str] = Field(default=None, description="""Name, manufacturer, order and lot numbers of sequencing kit""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_kit',
         'annotations': {'nullable': {'tag': 'nullable', 'value': True}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })
    sequencing_files: Optional[SequencingData] = Field(default=None, description="""Set of sequencing files produced by the sequencing run""", json_schema_extra = { "linkml_meta": {'alias': 'sequencing_files',
         'annotations': {'nullable': {'tag': 'nullable', 'value': False}},
         'domain_of': ['SequencingRun', 'SampleProcessing']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
AKObject.model_rebuild()
ForeignObject.model_rebuild()
AIRRStandards.model_rebuild()
AIRRStandardsV1p5.model_rebuild()
AIRRStandardsV2p0.model_rebuild()
NamedThing.model_rebuild()
Process.model_rebuild()
PlanSpecification.model_rebuild()
AIRRKnowledgeCommons.model_rebuild()
Investigation.model_rebuild()
Reference.model_rebuild()
StudyArm.model_rebuild()
Participant.model_rebuild()
StudyEvent.model_rebuild()
LifeEvent.model_rebuild()
ImmuneExposure.model_rebuild()
Specimen.model_rebuild()
SpecimenCollection.model_rebuild()
SpecimenProcessing.model_rebuild()
CellIsolationProcessing.model_rebuild()
Assay.model_rebuild()
AntibodyAntigenBindingAssay.model_rebuild()
DataItem.model_rebuild()
MeasurementDatum.model_rebuild()
Assessment.model_rebuild()
MeasurementCategory.model_rebuild()
TCellReceptorEpitopeSpecificityMeasurement.model_rebuild()
TCellReceptorEpitopeBindingAssay.model_rebuild()
DataSet.model_rebuild()
AKDataItem.model_rebuild()
AKDataSet.model_rebuild()
SequenceData.model_rebuild()
RNATranscriptomeData.model_rebuild()
DataTransformation.model_rebuild()
InputOutputDataMap.model_rebuild()
Conclusion.model_rebuild()
ImmuneSystem.model_rebuild()
Chain.model_rebuild()
ImmuneReceptor.model_rebuild()
TCellReceptor.model_rebuild()
AlphaBetaTCR.model_rebuild()
GammaDeltaTCR.model_rebuild()
BCellReceptor.model_rebuild()
Antigen.model_rebuild()
Epitope.model_rebuild()
PeptidicEpitope.model_rebuild()
AntibodyAntigenComplex.model_rebuild()
TCRpMHCComplex.model_rebuild()
Model.model_rebuild()
ConceptualModel.model_rebuild()
CommunicativeModel.model_rebuild()
ModelSpecification.model_rebuild()
ModelingFramework.model_rebuild()
Simulation.model_rebuild()
SimilarityCalculation.model_rebuild()
ChainSimilarity.model_rebuild()
TimePoint.model_rebuild()
Acknowledgement.model_rebuild()
RearrangedSequence.model_rebuild()
UnrearrangedSequence.model_rebuild()
SequenceDelineationV.model_rebuild()
AlleleDescription.model_rebuild()
GermlineSet.model_rebuild()
GenotypeSet.model_rebuild()
Genotype.model_rebuild()
DocumentedAllele.model_rebuild()
UndocumentedAllele.model_rebuild()
DeletedGene.model_rebuild()
MHCGenotypeSet.model_rebuild()
MHCGenotype.model_rebuild()
MHCAllele.model_rebuild()
SubjectGenotype.model_rebuild()
Study.model_rebuild()
Subject.model_rebuild()
Diagnosis.model_rebuild()
Sample.model_rebuild()
CellProcessing.model_rebuild()
PCRTarget.model_rebuild()
NucleicAcidProcessing.model_rebuild()
LibraryPreparationProcessing.model_rebuild()
SequencingRun.model_rebuild()
AIRRSequencingAssay.model_rebuild()
SequencingData.model_rebuild()
AIRRSequencingData.model_rebuild()
DataProcessing.model_rebuild()
Repertoire.model_rebuild()
RepertoireFilter.model_rebuild()
RepertoireGroup.model_rebuild()
Alignment.model_rebuild()
Rearrangement.model_rebuild()
Clone.model_rebuild()
Tree.model_rebuild()
Node.model_rebuild()
Cell.model_rebuild()
CellExpression.model_rebuild()
Receptor.model_rebuild()
ReceptorReactivity.model_rebuild()
SampleProcessing.model_rebuild()

