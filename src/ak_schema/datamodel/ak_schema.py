# Auto generated from ak_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-12-05T14:08:28
# Schema: ak-schema
#
# id: https://github.com/airr-knowledge/ak-schema
# description: Common data model schema for the AIRR Knowledge Commons
# license: GNU GPL v3.0

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime, time
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.metamodelcore import Bool, Curie, Decimal, ElementIdentifier, NCName, NodeIdentifier, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
APOLLO_SV = CurieNamespace('APOLLO_SV', 'http://purl.obolibrary.org/obo/APOLLO_SV_')
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
DOID = CurieNamespace('DOID', 'http://purl.obolibrary.org/obo/DOID_')
EXO = CurieNamespace('EXO', 'http://purl.obolibrary.org/obo/EXO_')
GAZ = CurieNamespace('GAZ', 'http://purl.obolibrary.org/obo/GAZ_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
OGMS = CurieNamespace('OGMS', 'http://purl.obolibrary.org/obo/OGMS_')
OMRSE = CurieNamespace('OMRSE', 'http://purl.obolibrary.org/obo/OMRSE_')
ONTIE = CurieNamespace('ONTIE', 'https://ontology.iedb.org/ontology/ONTIE_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
SBO = CurieNamespace('SBO', 'http://purl.obolibrary.org/obo/SBO_')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
VO = CurieNamespace('VO', 'http://purl.obolibrary.org/obo/VO_')
AK_SCHEMA = CurieNamespace('ak_schema', 'https://github.com/airr-knowledge/ak-schema/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
DC = CurieNamespace('dc', 'http://purl.org/dc/elements/1.1/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
IEDB_ASSAY = CurieNamespace('iedb_assay', 'http://www.iedb.org/assay/')
IEDB_EPITOPE = CurieNamespace('iedb_epitope', 'http://www.iedb.org/epitope/')
IEDB_RECEPTOR = CurieNamespace('iedb_receptor', 'http://www.iedb.org/receptor/')
IEDB_REFERENCE = CurieNamespace('iedb_reference', 'http://www.iedb.org/reference/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = AK_SCHEMA


# Types
class String(str):
    """ A character string """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = AK_SCHEMA.String


class Integer(int):
    """ An integer """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "integer"
    type_model_uri = AK_SCHEMA.Integer


class Boolean(Bool):
    """ A binary (true or false) value """
    type_class_uri = XSD["boolean"]
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = AK_SCHEMA.Boolean


class Float(float):
    """ A real number that conforms to the xsd:float specification """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "float"
    type_model_uri = AK_SCHEMA.Float


class Double(float):
    """ A real number that conforms to the xsd:double specification """
    type_class_uri = XSD["double"]
    type_class_curie = "xsd:double"
    type_name = "double"
    type_model_uri = AK_SCHEMA.Double


class Decimal(Decimal):
    """ A real number with arbitrary precision that conforms to the xsd:decimal specification """
    type_class_uri = XSD["decimal"]
    type_class_curie = "xsd:decimal"
    type_name = "decimal"
    type_model_uri = AK_SCHEMA.Decimal


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD["time"]
    type_class_curie = "xsd:time"
    type_name = "time"
    type_model_uri = AK_SCHEMA.Time


class Date(XSDDate):
    """ a date (year, month and day) in an idealized calendar """
    type_class_uri = XSD["date"]
    type_class_curie = "xsd:date"
    type_name = "date"
    type_model_uri = AK_SCHEMA.Date


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    type_class_uri = XSD["dateTime"]
    type_class_curie = "xsd:dateTime"
    type_name = "datetime"
    type_model_uri = AK_SCHEMA.Datetime


class DateOrDatetime(str):
    """ Either a date or a datetime """
    type_class_uri = LINKML["DateOrDatetime"]
    type_class_curie = "linkml:DateOrDatetime"
    type_name = "date_or_datetime"
    type_model_uri = AK_SCHEMA.DateOrDatetime


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = AK_SCHEMA.Uriorcurie


class Curie(Curie):
    """ a compact URI """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "curie"
    type_model_uri = AK_SCHEMA.Curie


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = AK_SCHEMA.Uri


class Ncname(NCName):
    """ Prefix part of CURIE """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ncname"
    type_model_uri = AK_SCHEMA.Ncname


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    type_class_uri = SHEX["iri"]
    type_class_curie = "shex:iri"
    type_name = "objectidentifier"
    type_model_uri = AK_SCHEMA.Objectidentifier


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    type_class_uri = SHEX["nonLiteral"]
    type_class_curie = "shex:nonLiteral"
    type_name = "nodeidentifier"
    type_model_uri = AK_SCHEMA.Nodeidentifier


class Jsonpointer(str):
    """ A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "jsonpointer"
    type_model_uri = AK_SCHEMA.Jsonpointer


class Jsonpath(str):
    """ A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "jsonpath"
    type_model_uri = AK_SCHEMA.Jsonpath


class Sparqlpath(str):
    """ A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sparqlpath"
    type_model_uri = AK_SCHEMA.Sparqlpath


# Class references
class AKObjectAkcId(URIorCURIE):
    pass


class ForeignObjectSourceUri(URIorCURIE):
    pass


class NamedThingAkcId(AKObjectAkcId):
    pass


class PlannedProcessAkcId(NamedThingAkcId):
    pass


class PlanSpecificationAkcId(NamedThingAkcId):
    pass


class InvestigationAkcId(PlannedProcessAkcId):
    pass


class ReferenceSourceUri(ForeignObjectSourceUri):
    pass


class StudyArmAkcId(NamedThingAkcId):
    pass


class ParticipantAkcId(NamedThingAkcId):
    pass


class StudyEventAkcId(NamedThingAkcId):
    pass


class LifeEventAkcId(NamedThingAkcId):
    pass


class ImmuneExposureAkcId(NamedThingAkcId):
    pass


class SpecimenAkcId(NamedThingAkcId):
    pass


class SpecimenCollectionAkcId(PlannedProcessAkcId):
    pass


class SpecimenProcessingAkcId(PlannedProcessAkcId):
    pass


class CellIsolationProcessingAkcId(SpecimenProcessingAkcId):
    pass


class NucleicAcidProcessingAkcId(SpecimenProcessingAkcId):
    pass


class LibraryPreparationProcessingAkcId(SpecimenProcessingAkcId):
    pass


class AssayAkcId(PlannedProcessAkcId):
    pass


class ReceptorRepertoireSequencingAssayAkcId(AssayAkcId):
    pass


class TCellReceptorEpitopeBindingAssayAkcId(AssayAkcId):
    pass


class DatasetAkcId(NamedThingAkcId):
    pass


class ConclusionAkcId(NamedThingAkcId):
    pass


class AssessmentAkcId(PlannedProcessAkcId):
    pass


class CellAkcId(NamedThingAkcId):
    pass


class TissuePortionAkcId(NamedThingAkcId):
    pass


class ImmuneSystemAkcId(NamedThingAkcId):
    pass


class ChainAkcId(NamedThingAkcId):
    pass


class TCellReceptorAkcId(NamedThingAkcId):
    pass


class AlphaBetaTCRAkcId(TCellReceptorAkcId):
    pass


class GammaDeltaTCRAkcId(TCellReceptorAkcId):
    pass


class BCellReceptorAkcId(NamedThingAkcId):
    pass


class EpitopeAkcId(NamedThingAkcId):
    pass


class PeptidicEpitopeAkcId(EpitopeAkcId):
    pass


class ModelAkcId(NamedThingAkcId):
    pass


class ConceptualModelAkcId(ModelAkcId):
    pass


class CommunicativeModelAkcId(ModelAkcId):
    pass


class ModelSpecificationAkcId(PlanSpecificationAkcId):
    pass


class ModelingFrameworkAkcId(NamedThingAkcId):
    pass


class SimulationAkcId(PlannedProcessAkcId):
    pass


class SimilarityCalculationAkcId(AKObjectAkcId):
    pass


class ChainSimilarityAkcId(SimilarityCalculationAkcId):
    pass


@dataclass(repr=False)
class AKObject(YAMLRoot):
    """
    Anything uniquely identifiable in the AKC.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AKObject"]
    class_class_curie: ClassVar[str] = "ak_schema:AKObject"
    class_name: ClassVar[str] = "AKObject"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AKObject

    akc_id: Union[str, AKObjectAkcId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, AKObjectAkcId):
            self.akc_id = AKObjectAkcId(self.akc_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ForeignObject(YAMLRoot):
    """
    An object held outside of the AK.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["ForeignObject"]
    class_class_curie: ClassVar[str] = "ak_schema:ForeignObject"
    class_name: ClassVar[str] = "ForeignObject"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.ForeignObject

    source_uri: Union[str, ForeignObjectSourceUri] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.source_uri):
            self.MissingRequiredField("source_uri")
        if not isinstance(self.source_uri, ForeignObjectSourceUri):
            self.source_uri = ForeignObjectSourceUri(self.source_uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamedThing(AKObject):
    """
    Name and description for AKC things.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["NamedThing"]
    class_class_curie: ClassVar[str] = "ak_schema:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.NamedThing

    akc_id: Union[str, NamedThingAkcId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PlannedProcess(NamedThing):
    """
    A process to realize a plan.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["PlannedProcess"]
    class_class_curie: ClassVar[str] = "ak_schema:PlannedProcess"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.PlannedProcess

    akc_id: Union[str, PlannedProcessAkcId] = None

@dataclass(repr=False)
class PlanSpecification(NamedThing):
    """
    A plan with specified actions to meet some objectives.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["PlanSpecification"]
    class_class_curie: ClassVar[str] = "ak_schema:PlanSpecification"
    class_name: ClassVar[str] = "PlanSpecification"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.PlanSpecification

    akc_id: Union[str, PlanSpecificationAkcId] = None

@dataclass(repr=False)
class AIRRKnowledgeCommons(YAMLRoot):
    """
    A container for instances of multiple classes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AIRRKnowledgeCommons"]
    class_class_curie: ClassVar[str] = "ak_schema:AIRRKnowledgeCommons"
    class_name: ClassVar[str] = "AIRRKnowledgeCommons"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AIRRKnowledgeCommons

    investigations: Optional[Union[Dict[Union[str, InvestigationAkcId], Union[dict, "Investigation"]], List[Union[dict, "Investigation"]]]] = empty_dict()
    references: Optional[Union[Dict[Union[str, ReferenceSourceUri], Union[dict, "Reference"]], List[Union[dict, "Reference"]]]] = empty_dict()
    study_arms: Optional[Union[Dict[Union[str, StudyArmAkcId], Union[dict, "StudyArm"]], List[Union[dict, "StudyArm"]]]] = empty_dict()
    study_events: Optional[Union[Dict[Union[str, StudyEventAkcId], Union[dict, "StudyEvent"]], List[Union[dict, "StudyEvent"]]]] = empty_dict()
    participants: Optional[Union[Dict[Union[str, ParticipantAkcId], Union[dict, "Participant"]], List[Union[dict, "Participant"]]]] = empty_dict()
    life_events: Optional[Union[Dict[Union[str, LifeEventAkcId], Union[dict, "LifeEvent"]], List[Union[dict, "LifeEvent"]]]] = empty_dict()
    immune_exposures: Optional[Union[Dict[Union[str, ImmuneExposureAkcId], Union[dict, "ImmuneExposure"]], List[Union[dict, "ImmuneExposure"]]]] = empty_dict()
    assessments: Optional[Union[Dict[Union[str, AssessmentAkcId], Union[dict, "Assessment"]], List[Union[dict, "Assessment"]]]] = empty_dict()
    specimens: Optional[Union[Dict[Union[str, SpecimenAkcId], Union[dict, "Specimen"]], List[Union[dict, "Specimen"]]]] = empty_dict()
    specimen_collections: Optional[Union[Dict[Union[str, SpecimenCollectionAkcId], Union[dict, "SpecimenCollection"]], List[Union[dict, "SpecimenCollection"]]]] = empty_dict()
    specimen_processings: Optional[Union[Dict[Union[str, SpecimenProcessingAkcId], Union[dict, "SpecimenProcessing"]], List[Union[dict, "SpecimenProcessing"]]]] = empty_dict()
    assays: Optional[Union[Dict[Union[str, AssayAkcId], Union[dict, "Assay"]], List[Union[dict, "Assay"]]]] = empty_dict()
    datasets: Optional[Union[Dict[Union[str, DatasetAkcId], Union[dict, "Dataset"]], List[Union[dict, "Dataset"]]]] = empty_dict()
    conclusions: Optional[Union[Dict[Union[str, ConclusionAkcId], Union[dict, "Conclusion"]], List[Union[dict, "Conclusion"]]]] = empty_dict()
    chains: Optional[Union[Dict[Union[str, ChainAkcId], Union[dict, "Chain"]], List[Union[dict, "Chain"]]]] = empty_dict()
    tcell_receptors: Optional[Union[Dict[Union[str, TCellReceptorAkcId], Union[dict, "TCellReceptor"]], List[Union[dict, "TCellReceptor"]]]] = empty_dict()
    epitopes: Optional[Union[Dict[Union[str, EpitopeAkcId], Union[dict, "Epitope"]], List[Union[dict, "Epitope"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="investigations", slot_type=Investigation, key_name="akc_id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="references", slot_type=Reference, key_name="source_uri", keyed=True)

        self._normalize_inlined_as_dict(slot_name="study_arms", slot_type=StudyArm, key_name="akc_id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="study_events", slot_type=StudyEvent, key_name="akc_id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="participants", slot_type=Participant, key_name="akc_id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="life_events", slot_type=LifeEvent, key_name="akc_id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="immune_exposures", slot_type=ImmuneExposure, key_name="akc_id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="assessments", slot_type=Assessment, key_name="akc_id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="specimens", slot_type=Specimen, key_name="akc_id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="specimen_collections", slot_type=SpecimenCollection, key_name="akc_id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="specimen_processings", slot_type=SpecimenProcessing, key_name="akc_id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="assays", slot_type=Assay, key_name="akc_id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="datasets", slot_type=Dataset, key_name="akc_id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="conclusions", slot_type=Conclusion, key_name="akc_id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="chains", slot_type=Chain, key_name="akc_id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="tcell_receptors", slot_type=TCellReceptor, key_name="akc_id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="epitopes", slot_type=Epitope, key_name="akc_id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Investigation(PlannedProcess):
    """
    A scientific investigation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000066"]
    class_class_curie: ClassVar[str] = "OBI:0000066"
    class_name: ClassVar[str] = "Investigation"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Investigation

    akc_id: Union[str, InvestigationAkcId] = None
    study_type: Optional[Union[str, "StudyType"]] = None
    archival_id: Optional[Union[str, URIorCURIE]] = None
    inclusion_criteria: Optional[str] = None
    exclusion_criteria: Optional[str] = None
    release_date: Optional[Union[str, XSDDateTime]] = None
    update_date: Optional[Union[str, XSDDateTime]] = None
    participants: Optional[Union[Union[str, ParticipantAkcId], List[Union[str, ParticipantAkcId]]]] = empty_list()
    assays: Optional[Union[Union[str, AssayAkcId], List[Union[str, AssayAkcId]]]] = empty_list()
    simulations: Optional[Union[Union[str, SimulationAkcId], List[Union[str, SimulationAkcId]]]] = empty_list()
    documents: Optional[Union[Union[str, ReferenceSourceUri], List[Union[str, ReferenceSourceUri]]]] = empty_list()
    conclusions: Optional[Union[Union[str, ConclusionAkcId], List[Union[str, ConclusionAkcId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, InvestigationAkcId):
            self.akc_id = InvestigationAkcId(self.akc_id)

        if self.archival_id is not None and not isinstance(self.archival_id, URIorCURIE):
            self.archival_id = URIorCURIE(self.archival_id)

        if self.inclusion_criteria is not None and not isinstance(self.inclusion_criteria, str):
            self.inclusion_criteria = str(self.inclusion_criteria)

        if self.exclusion_criteria is not None and not isinstance(self.exclusion_criteria, str):
            self.exclusion_criteria = str(self.exclusion_criteria)

        if self.release_date is not None and not isinstance(self.release_date, XSDDateTime):
            self.release_date = XSDDateTime(self.release_date)

        if self.update_date is not None and not isinstance(self.update_date, XSDDateTime):
            self.update_date = XSDDateTime(self.update_date)

        if not isinstance(self.participants, list):
            self.participants = [self.participants] if self.participants is not None else []
        self.participants = [v if isinstance(v, ParticipantAkcId) else ParticipantAkcId(v) for v in self.participants]

        if not isinstance(self.assays, list):
            self.assays = [self.assays] if self.assays is not None else []
        self.assays = [v if isinstance(v, AssayAkcId) else AssayAkcId(v) for v in self.assays]

        if not isinstance(self.simulations, list):
            self.simulations = [self.simulations] if self.simulations is not None else []
        self.simulations = [v if isinstance(v, SimulationAkcId) else SimulationAkcId(v) for v in self.simulations]

        if not isinstance(self.documents, list):
            self.documents = [self.documents] if self.documents is not None else []
        self.documents = [v if isinstance(v, ReferenceSourceUri) else ReferenceSourceUri(v) for v in self.documents]

        if not isinstance(self.conclusions, list):
            self.conclusions = [self.conclusions] if self.conclusions is not None else []
        self.conclusions = [v if isinstance(v, ConclusionAkcId) else ConclusionAkcId(v) for v in self.conclusions]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reference(ForeignObject):
    """
    A document about an investigation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IAO["0000310"]
    class_class_curie: ClassVar[str] = "IAO:0000310"
    class_name: ClassVar[str] = "Reference"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Reference

    source_uri: Union[str, ReferenceSourceUri] = None
    sources: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    investigations: Optional[Union[Union[str, InvestigationAkcId], List[Union[str, InvestigationAkcId]]]] = empty_list()
    title: Optional[str] = None
    authors: Optional[Union[str, List[str]]] = empty_list()
    journal: Optional[str] = None
    issue: Optional[str] = None
    month: Optional[str] = None
    year: Optional[int] = None
    pages: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.source_uri):
            self.MissingRequiredField("source_uri")
        if not isinstance(self.source_uri, ReferenceSourceUri):
            self.source_uri = ReferenceSourceUri(self.source_uri)

        if not isinstance(self.sources, list):
            self.sources = [self.sources] if self.sources is not None else []
        self.sources = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.sources]

        if not isinstance(self.investigations, list):
            self.investigations = [self.investigations] if self.investigations is not None else []
        self.investigations = [v if isinstance(v, InvestigationAkcId) else InvestigationAkcId(v) for v in self.investigations]

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, str) else str(v) for v in self.authors]

        if self.journal is not None and not isinstance(self.journal, str):
            self.journal = str(self.journal)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if self.month is not None and not isinstance(self.month, str):
            self.month = str(self.month)

        if self.year is not None and not isinstance(self.year, int):
            self.year = int(self.year)

        if self.pages is not None and not isinstance(self.pages, str):
            self.pages = str(self.pages)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StudyArm(NamedThing):
    """
    A population of participants of an investigation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000181"]
    class_class_curie: ClassVar[str] = "OBI:0000181"
    class_name: ClassVar[str] = "StudyArm"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.StudyArm

    akc_id: Union[str, StudyArmAkcId] = None
    investigation: Optional[Union[str, InvestigationAkcId]] = None
    inclusion_criteria: Optional[str] = None
    exclusion_criteria: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, StudyArmAkcId):
            self.akc_id = StudyArmAkcId(self.akc_id)

        if self.investigation is not None and not isinstance(self.investigation, InvestigationAkcId):
            self.investigation = InvestigationAkcId(self.investigation)

        if self.inclusion_criteria is not None and not isinstance(self.inclusion_criteria, str):
            self.inclusion_criteria = str(self.inclusion_criteria)

        if self.exclusion_criteria is not None and not isinstance(self.exclusion_criteria, str):
            self.exclusion_criteria = str(self.exclusion_criteria)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Participant(NamedThing):
    """
    A participant in an investigation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0100026"]
    class_class_curie: ClassVar[str] = "OBI:0100026"
    class_name: ClassVar[str] = "Participant"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Participant

    akc_id: Union[str, ParticipantAkcId] = None
    study_arm: Optional[Union[str, StudyArmAkcId]] = None
    species: Optional[Union[str, "Species"]] = None
    biological_sex: Optional[Union[str, "BiologicalSex"]] = None
    phenotypic_sex: Optional[Union[str, "PhenotypicSex"]] = None
    age: Optional[str] = None
    age_unit: Optional[Union[str, "AgeUnit"]] = None
    age_event: Optional[Union[str, LifeEventAkcId]] = None
    race: Optional[Union[str, "Race"]] = None
    ethnicity: Optional[Union[str, "Ethnicity"]] = None
    geolocation: Optional[Union[str, "Geolocation"]] = None
    strain: Optional[Union[str, "Strain"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, ParticipantAkcId):
            self.akc_id = ParticipantAkcId(self.akc_id)

        if self.study_arm is not None and not isinstance(self.study_arm, StudyArmAkcId):
            self.study_arm = StudyArmAkcId(self.study_arm)

        if self.species is not None and not isinstance(self.species, Species):
            self.species = Species(self.species)

        if self.biological_sex is not None and not isinstance(self.biological_sex, BiologicalSex):
            self.biological_sex = BiologicalSex(self.biological_sex)

        if self.phenotypic_sex is not None and not isinstance(self.phenotypic_sex, PhenotypicSex):
            self.phenotypic_sex = PhenotypicSex(self.phenotypic_sex)

        if self.age is not None and not isinstance(self.age, str):
            self.age = str(self.age)

        if self.age_event is not None and not isinstance(self.age_event, LifeEventAkcId):
            self.age_event = LifeEventAkcId(self.age_event)

        if self.race is not None and not isinstance(self.race, Race):
            self.race = Race(self.race)

        if self.ethnicity is not None and not isinstance(self.ethnicity, Ethnicity):
            self.ethnicity = Ethnicity(self.ethnicity)

        if self.geolocation is not None and not isinstance(self.geolocation, Geolocation):
            self.geolocation = Geolocation(self.geolocation)

        if self.strain is not None and not isinstance(self.strain, Strain):
            self.strain = Strain(self.strain)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StudyEvent(NamedThing):
    """
    An event that is part of the study design of an investigation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BFO["0000015"]
    class_class_curie: ClassVar[str] = "BFO:0000015"
    class_name: ClassVar[str] = "StudyEvent"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.StudyEvent

    akc_id: Union[str, StudyEventAkcId] = None
    study_arms: Optional[Union[Union[str, StudyArmAkcId], List[Union[str, StudyArmAkcId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, StudyEventAkcId):
            self.akc_id = StudyEventAkcId(self.akc_id)

        if not isinstance(self.study_arms, list):
            self.study_arms = [self.study_arms] if self.study_arms is not None else []
        self.study_arms = [v if isinstance(v, StudyArmAkcId) else StudyArmAkcId(v) for v in self.study_arms]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LifeEvent(NamedThing):
    """
    An event in which a study participant participates.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BFO["0000015"]
    class_class_curie: ClassVar[str] = "BFO:0000015"
    class_name: ClassVar[str] = "LifeEvent"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.LifeEvent

    akc_id: Union[str, LifeEventAkcId] = None
    participant: Optional[Union[str, ParticipantAkcId]] = None
    study_event: Optional[Union[str, StudyEventAkcId]] = None
    life_event_type: Optional[Union[str, "LifeEventProcess"]] = None
    geolocation: Optional[Union[str, "Geolocation"]] = None
    t0_event: Optional[str] = None
    t0_event_type: Optional[str] = None
    start: Optional[Decimal] = None
    duration: Optional[Decimal] = None
    time_unit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, LifeEventAkcId):
            self.akc_id = LifeEventAkcId(self.akc_id)

        if self.participant is not None and not isinstance(self.participant, ParticipantAkcId):
            self.participant = ParticipantAkcId(self.participant)

        if self.study_event is not None and not isinstance(self.study_event, StudyEventAkcId):
            self.study_event = StudyEventAkcId(self.study_event)

        if self.life_event_type is not None and not isinstance(self.life_event_type, LifeEventProcess):
            self.life_event_type = LifeEventProcess(self.life_event_type)

        if self.geolocation is not None and not isinstance(self.geolocation, Geolocation):
            self.geolocation = Geolocation(self.geolocation)

        if self.t0_event is not None and not isinstance(self.t0_event, str):
            self.t0_event = str(self.t0_event)

        if self.t0_event_type is not None and not isinstance(self.t0_event_type, str):
            self.t0_event_type = str(self.t0_event_type)

        if self.start is not None and not isinstance(self.start, Decimal):
            self.start = Decimal(self.start)

        if self.duration is not None and not isinstance(self.duration, Decimal):
            self.duration = Decimal(self.duration)

        if self.time_unit is not None and not isinstance(self.time_unit, str):
            self.time_unit = str(self.time_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImmuneExposure(NamedThing):
    """
    An event involving the immune system of a study participant.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BFO["0000015"]
    class_class_curie: ClassVar[str] = "BFO:0000015"
    class_name: ClassVar[str] = "ImmuneExposure"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.ImmuneExposure

    akc_id: Union[str, ImmuneExposureAkcId] = None
    life_event: Optional[Union[str, LifeEventAkcId]] = None
    exposure_material: Optional[Union[str, "ExposureMaterial"]] = None
    disease: Optional[Union[str, "Disease"]] = None
    disease_stage: Optional[Union[str, "DiseaseStage"]] = None
    disease_severity: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, ImmuneExposureAkcId):
            self.akc_id = ImmuneExposureAkcId(self.akc_id)

        if self.life_event is not None and not isinstance(self.life_event, LifeEventAkcId):
            self.life_event = LifeEventAkcId(self.life_event)

        if self.exposure_material is not None and not isinstance(self.exposure_material, ExposureMaterial):
            self.exposure_material = ExposureMaterial(self.exposure_material)

        if self.disease is not None and not isinstance(self.disease, Disease):
            self.disease = Disease(self.disease)

        if self.disease_stage is not None and not isinstance(self.disease_stage, DiseaseStage):
            self.disease_stage = DiseaseStage(self.disease_stage)

        if self.disease_severity is not None and not isinstance(self.disease_severity, str):
            self.disease_severity = str(self.disease_severity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Specimen(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0100051"]
    class_class_curie: ClassVar[str] = "OBI:0100051"
    class_name: ClassVar[str] = "Specimen"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Specimen

    akc_id: Union[str, SpecimenAkcId] = None
    life_event: Optional[Union[str, LifeEventAkcId]] = None
    specimen_type: Optional[str] = None
    tissue: Optional[Union[str, "Tissue"]] = None
    process: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, SpecimenAkcId):
            self.akc_id = SpecimenAkcId(self.akc_id)

        if self.life_event is not None and not isinstance(self.life_event, LifeEventAkcId):
            self.life_event = LifeEventAkcId(self.life_event)

        if self.specimen_type is not None and not isinstance(self.specimen_type, str):
            self.specimen_type = str(self.specimen_type)

        if self.process is not None and not isinstance(self.process, str):
            self.process = str(self.process)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecimenCollection(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000659"]
    class_class_curie: ClassVar[str] = "OBI:0000659"
    class_name: ClassVar[str] = "SpecimenCollection"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.SpecimenCollection

    akc_id: Union[str, SpecimenCollectionAkcId] = None
    specimen: Optional[Union[str, SpecimenAkcId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, SpecimenCollectionAkcId):
            self.akc_id = SpecimenCollectionAkcId(self.akc_id)

        if self.specimen is not None and not isinstance(self.specimen, SpecimenAkcId):
            self.specimen = SpecimenAkcId(self.specimen)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecimenProcessing(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000094"]
    class_class_curie: ClassVar[str] = "OBI:0000094"
    class_name: ClassVar[str] = "SpecimenProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.SpecimenProcessing

    akc_id: Union[str, SpecimenProcessingAkcId] = None
    specimen: Optional[Union[str, SpecimenAkcId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, SpecimenProcessingAkcId):
            self.akc_id = SpecimenProcessingAkcId(self.akc_id)

        if self.specimen is not None and not isinstance(self.specimen, SpecimenAkcId):
            self.specimen = SpecimenAkcId(self.specimen)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellIsolationProcessing(SpecimenProcessing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["00000512"]
    class_class_curie: ClassVar[str] = "OBI:00000512"
    class_name: ClassVar[str] = "CellIsolationProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.CellIsolationProcessing

    akc_id: Union[str, CellIsolationProcessingAkcId] = None
    tissue_processing: Optional[str] = None
    cell_subset: Optional[Union[str, "CellSubset"]] = None
    cell_phenotype: Optional[str] = None
    cell_species: Optional[Union[str, "CellSpecies"]] = None
    single_cell: Optional[Union[bool, Bool]] = None
    cell_number: Optional[int] = None
    cells_per_reaction: Optional[int] = None
    cell_storage: Optional[Union[bool, Bool]] = None
    cell_quality: Optional[str] = None
    cell_isolation: Optional[str] = None
    cell_processing_protocol: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, CellIsolationProcessingAkcId):
            self.akc_id = CellIsolationProcessingAkcId(self.akc_id)

        if self.tissue_processing is not None and not isinstance(self.tissue_processing, str):
            self.tissue_processing = str(self.tissue_processing)

        if self.cell_phenotype is not None and not isinstance(self.cell_phenotype, str):
            self.cell_phenotype = str(self.cell_phenotype)

        if self.single_cell is not None and not isinstance(self.single_cell, Bool):
            self.single_cell = Bool(self.single_cell)

        if self.cell_number is not None and not isinstance(self.cell_number, int):
            self.cell_number = int(self.cell_number)

        if self.cells_per_reaction is not None and not isinstance(self.cells_per_reaction, int):
            self.cells_per_reaction = int(self.cells_per_reaction)

        if self.cell_storage is not None and not isinstance(self.cell_storage, Bool):
            self.cell_storage = Bool(self.cell_storage)

        if self.cell_quality is not None and not isinstance(self.cell_quality, str):
            self.cell_quality = str(self.cell_quality)

        if self.cell_isolation is not None and not isinstance(self.cell_isolation, str):
            self.cell_isolation = str(self.cell_isolation)

        if self.cell_processing_protocol is not None and not isinstance(self.cell_processing_protocol, str):
            self.cell_processing_protocol = str(self.cell_processing_protocol)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NucleicAcidProcessing(SpecimenProcessing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["00001902"]
    class_class_curie: ClassVar[str] = "OBI:00001902"
    class_name: ClassVar[str] = "NucleicAcidProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.NucleicAcidProcessing

    akc_id: Union[str, NucleicAcidProcessingAkcId] = None
    template_class: Optional[Union[str, "TemplateClass"]] = None
    template_quality: Optional[str] = None
    template_amount: Optional[float] = None
    template_amount_unit: Optional[Union[str, "TemplateAmountUnit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, NucleicAcidProcessingAkcId):
            self.akc_id = NucleicAcidProcessingAkcId(self.akc_id)

        if self.template_class is not None and not isinstance(self.template_class, TemplateClass):
            self.template_class = TemplateClass(self.template_class)

        if self.template_quality is not None and not isinstance(self.template_quality, str):
            self.template_quality = str(self.template_quality)

        if self.template_amount is not None and not isinstance(self.template_amount, float):
            self.template_amount = float(self.template_amount)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LibraryPreparationProcessing(SpecimenProcessing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["00000711"]
    class_class_curie: ClassVar[str] = "OBI:00000711"
    class_name: ClassVar[str] = "LibraryPreparationProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.LibraryPreparationProcessing

    akc_id: Union[str, LibraryPreparationProcessingAkcId] = None
    library_generation_method: Optional[Union[str, "LibraryGenerationMethod"]] = None
    library_generation_protocol: Optional[str] = None
    library_generation_kit_version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, LibraryPreparationProcessingAkcId):
            self.akc_id = LibraryPreparationProcessingAkcId(self.akc_id)

        if self.library_generation_method is not None and not isinstance(self.library_generation_method, LibraryGenerationMethod):
            self.library_generation_method = LibraryGenerationMethod(self.library_generation_method)

        if self.library_generation_protocol is not None and not isinstance(self.library_generation_protocol, str):
            self.library_generation_protocol = str(self.library_generation_protocol)

        if self.library_generation_kit_version is not None and not isinstance(self.library_generation_kit_version, str):
            self.library_generation_kit_version = str(self.library_generation_kit_version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Assay(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000070"]
    class_class_curie: ClassVar[str] = "OBI:0000070"
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Assay

    akc_id: Union[str, AssayAkcId] = None
    specimen: Optional[Union[str, SpecimenAkcId]] = None
    specimen_processing: Optional[Union[Union[str, SpecimenProcessingAkcId], List[Union[str, SpecimenProcessingAkcId]]]] = empty_list()
    type: Optional[str] = None
    assay_type: Optional[str] = None
    target_entity_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, AssayAkcId):
            self.akc_id = AssayAkcId(self.akc_id)

        if self.specimen is not None and not isinstance(self.specimen, SpecimenAkcId):
            self.specimen = SpecimenAkcId(self.specimen)

        if not isinstance(self.specimen_processing, list):
            self.specimen_processing = [self.specimen_processing] if self.specimen_processing is not None else []
        self.specimen_processing = [v if isinstance(v, SpecimenProcessingAkcId) else SpecimenProcessingAkcId(v) for v in self.specimen_processing]

        self.type = str(self.class_name)

        if self.assay_type is not None and not isinstance(self.assay_type, str):
            self.assay_type = str(self.assay_type)

        if self.target_entity_type is not None and not isinstance(self.target_entity_type, str):
            self.target_entity_type = str(self.target_entity_type)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class ReceptorRepertoireSequencingAssay(Assay):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0600047"]
    class_class_curie: ClassVar[str] = "OBI:0600047"
    class_name: ClassVar[str] = "ReceptorRepertoireSequencingAssay"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.ReceptorRepertoireSequencingAssay

    akc_id: Union[str, ReceptorRepertoireSequencingAssayAkcId] = None
    pcr_target: Optional[Union[Union[dict, "PCRTarget"], List[Union[dict, "PCRTarget"]]]] = empty_list()
    complete_sequences: Optional[Union[str, "CompleteSequences"]] = None
    physical_linkage: Optional[Union[str, "PhysicalLinkage"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, ReceptorRepertoireSequencingAssayAkcId):
            self.akc_id = ReceptorRepertoireSequencingAssayAkcId(self.akc_id)

        if not isinstance(self.pcr_target, list):
            self.pcr_target = [self.pcr_target] if self.pcr_target is not None else []
        self.pcr_target = [v if isinstance(v, PCRTarget) else PCRTarget(**as_dict(v)) for v in self.pcr_target]

        if self.complete_sequences is not None and not isinstance(self.complete_sequences, CompleteSequences):
            self.complete_sequences = CompleteSequences(self.complete_sequences)

        if self.physical_linkage is not None and not isinstance(self.physical_linkage, PhysicalLinkage):
            self.physical_linkage = PhysicalLinkage(self.physical_linkage)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class TCellReceptorEpitopeBindingAssay(Assay):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["1110037"]
    class_class_curie: ClassVar[str] = "OBI:1110037"
    class_name: ClassVar[str] = "TCellReceptorEpitopeBindingAssay"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.TCellReceptorEpitopeBindingAssay

    akc_id: Union[str, TCellReceptorEpitopeBindingAssayAkcId] = None
    epitope: Optional[Union[str, EpitopeAkcId]] = None
    tcell_receptors: Optional[Union[Union[str, TCellReceptorAkcId], List[Union[str, TCellReceptorAkcId]]]] = empty_list()
    value: Optional[str] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, TCellReceptorEpitopeBindingAssayAkcId):
            self.akc_id = TCellReceptorEpitopeBindingAssayAkcId(self.akc_id)

        if self.epitope is not None and not isinstance(self.epitope, EpitopeAkcId):
            self.epitope = EpitopeAkcId(self.epitope)

        if not isinstance(self.tcell_receptors, list):
            self.tcell_receptors = [self.tcell_receptors] if self.tcell_receptors is not None else []
        self.tcell_receptors = [v if isinstance(v, TCellReceptorAkcId) else TCellReceptorAkcId(v) for v in self.tcell_receptors]

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Dataset(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IAO["0000100"]
    class_class_curie: ClassVar[str] = "IAO:0000100"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Dataset

    akc_id: Union[str, DatasetAkcId] = None
    assessments: Optional[Union[Union[str, AssessmentAkcId], List[Union[str, AssessmentAkcId]]]] = empty_list()
    assays: Optional[Union[Union[str, AssayAkcId], List[Union[str, AssayAkcId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, DatasetAkcId):
            self.akc_id = DatasetAkcId(self.akc_id)

        if not isinstance(self.assessments, list):
            self.assessments = [self.assessments] if self.assessments is not None else []
        self.assessments = [v if isinstance(v, AssessmentAkcId) else AssessmentAkcId(v) for v in self.assessments]

        if not isinstance(self.assays, list):
            self.assays = [self.assays] if self.assays is not None else []
        self.assays = [v if isinstance(v, AssayAkcId) else AssayAkcId(v) for v in self.assays]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Conclusion(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0001909"]
    class_class_curie: ClassVar[str] = "OBI:0001909"
    class_name: ClassVar[str] = "Conclusion"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Conclusion

    akc_id: Union[str, ConclusionAkcId] = None
    investigations: Optional[Union[Union[str, InvestigationAkcId], List[Union[str, InvestigationAkcId]]]] = empty_list()
    datasets: Optional[Union[Union[str, DatasetAkcId], List[Union[str, DatasetAkcId]]]] = empty_list()
    result: Optional[str] = None
    data_location_type: Optional[str] = None
    data_location_value: Optional[str] = None
    organism: Optional[Union[str, "Species"]] = None
    experiment_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, ConclusionAkcId):
            self.akc_id = ConclusionAkcId(self.akc_id)

        if not isinstance(self.investigations, list):
            self.investigations = [self.investigations] if self.investigations is not None else []
        self.investigations = [v if isinstance(v, InvestigationAkcId) else InvestigationAkcId(v) for v in self.investigations]

        if not isinstance(self.datasets, list):
            self.datasets = [self.datasets] if self.datasets is not None else []
        self.datasets = [v if isinstance(v, DatasetAkcId) else DatasetAkcId(v) for v in self.datasets]

        if self.result is not None and not isinstance(self.result, str):
            self.result = str(self.result)

        if self.data_location_type is not None and not isinstance(self.data_location_type, str):
            self.data_location_type = str(self.data_location_type)

        if self.data_location_value is not None and not isinstance(self.data_location_value, str):
            self.data_location_value = str(self.data_location_value)

        if self.organism is not None and not isinstance(self.organism, Species):
            self.organism = Species(self.organism)

        if self.experiment_type is not None and not isinstance(self.experiment_type, str):
            self.experiment_type = str(self.experiment_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Assessment(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0002441"]
    class_class_curie: ClassVar[str] = "OBI:0002441"
    class_name: ClassVar[str] = "Assessment"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Assessment

    akc_id: Union[str, AssessmentAkcId] = None
    life_event: Optional[Union[str, LifeEventAkcId]] = None
    assessment_type: Optional[str] = None
    target_entity_type: Optional[str] = None
    value: Optional[str] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, AssessmentAkcId):
            self.akc_id = AssessmentAkcId(self.akc_id)

        if self.life_event is not None and not isinstance(self.life_event, LifeEventAkcId):
            self.life_event = LifeEventAkcId(self.life_event)

        if self.assessment_type is not None and not isinstance(self.assessment_type, str):
            self.assessment_type = str(self.assessment_type)

        if self.target_entity_type is not None and not isinstance(self.target_entity_type, str):
            self.target_entity_type = str(self.target_entity_type)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Cell(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CL["0000000"]
    class_class_curie: ClassVar[str] = "CL:0000000"
    class_name: ClassVar[str] = "Cell"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Cell

    akc_id: Union[str, CellAkcId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, CellAkcId):
            self.akc_id = CellAkcId(self.akc_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TissuePortion(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UBERON["0000479"]
    class_class_curie: ClassVar[str] = "UBERON:0000479"
    class_name: ClassVar[str] = "TissuePortion"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.TissuePortion

    akc_id: Union[str, TissuePortionAkcId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, TissuePortionAkcId):
            self.akc_id = TissuePortionAkcId(self.akc_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImmuneSystem(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UBERON["0002405"]
    class_class_curie: ClassVar[str] = "UBERON:0002405"
    class_name: ClassVar[str] = "ImmuneSystem"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.ImmuneSystem

    akc_id: Union[str, ImmuneSystemAkcId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, ImmuneSystemAkcId):
            self.akc_id = ImmuneSystemAkcId(self.akc_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Chain(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Chain"]
    class_class_curie: ClassVar[str] = "ak_schema:Chain"
    class_name: ClassVar[str] = "Chain"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Chain

    akc_id: Union[str, ChainAkcId] = None
    sequence: Optional[str] = None
    sequence_aa: Optional[str] = None
    chain_type: Optional[Union[str, "ChainType"]] = None
    v_call: Optional[str] = None
    d_call: Optional[str] = None
    j_call: Optional[str] = None
    c_call: Optional[str] = None
    junction_aa: Optional[str] = None
    cdr1_aa: Optional[str] = None
    cdr2_aa: Optional[str] = None
    cdr3_aa: Optional[str] = None
    cdr1_start: Optional[int] = None
    cdr1_end: Optional[int] = None
    cdr2_start: Optional[int] = None
    cdr2_end: Optional[int] = None
    cdr3_start: Optional[int] = None
    cdr3_end: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, ChainAkcId):
            self.akc_id = ChainAkcId(self.akc_id)

        if self.sequence is not None and not isinstance(self.sequence, str):
            self.sequence = str(self.sequence)

        if self.sequence_aa is not None and not isinstance(self.sequence_aa, str):
            self.sequence_aa = str(self.sequence_aa)

        if self.chain_type is not None and not isinstance(self.chain_type, ChainType):
            self.chain_type = ChainType(self.chain_type)

        if self.v_call is not None and not isinstance(self.v_call, str):
            self.v_call = str(self.v_call)

        if self.d_call is not None and not isinstance(self.d_call, str):
            self.d_call = str(self.d_call)

        if self.j_call is not None and not isinstance(self.j_call, str):
            self.j_call = str(self.j_call)

        if self.c_call is not None and not isinstance(self.c_call, str):
            self.c_call = str(self.c_call)

        if self.junction_aa is not None and not isinstance(self.junction_aa, str):
            self.junction_aa = str(self.junction_aa)

        if self.cdr1_aa is not None and not isinstance(self.cdr1_aa, str):
            self.cdr1_aa = str(self.cdr1_aa)

        if self.cdr2_aa is not None and not isinstance(self.cdr2_aa, str):
            self.cdr2_aa = str(self.cdr2_aa)

        if self.cdr3_aa is not None and not isinstance(self.cdr3_aa, str):
            self.cdr3_aa = str(self.cdr3_aa)

        if self.cdr1_start is not None and not isinstance(self.cdr1_start, int):
            self.cdr1_start = int(self.cdr1_start)

        if self.cdr1_end is not None and not isinstance(self.cdr1_end, int):
            self.cdr1_end = int(self.cdr1_end)

        if self.cdr2_start is not None and not isinstance(self.cdr2_start, int):
            self.cdr2_start = int(self.cdr2_start)

        if self.cdr2_end is not None and not isinstance(self.cdr2_end, int):
            self.cdr2_end = int(self.cdr2_end)

        if self.cdr3_start is not None and not isinstance(self.cdr3_start, int):
            self.cdr3_start = int(self.cdr3_start)

        if self.cdr3_end is not None and not isinstance(self.cdr3_end, int):
            self.cdr3_end = int(self.cdr3_end)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TCellReceptor(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GO["0042101"]
    class_class_curie: ClassVar[str] = "GO:0042101"
    class_name: ClassVar[str] = "TCellReceptor"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.TCellReceptor

    akc_id: Union[str, TCellReceptorAkcId] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, TCellReceptorAkcId):
            self.akc_id = TCellReceptorAkcId(self.akc_id)

        self.type = str(self.class_name)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class AlphaBetaTCR(TCellReceptor):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GO["0042105"]
    class_class_curie: ClassVar[str] = "GO:0042105"
    class_name: ClassVar[str] = "AlphaBetaTCR"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AlphaBetaTCR

    akc_id: Union[str, AlphaBetaTCRAkcId] = None
    TRA_chain: Optional[Union[str, ChainAkcId]] = None
    TRB_chain: Optional[Union[str, ChainAkcId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, AlphaBetaTCRAkcId):
            self.akc_id = AlphaBetaTCRAkcId(self.akc_id)

        if self.TRA_chain is not None and not isinstance(self.TRA_chain, ChainAkcId):
            self.TRA_chain = ChainAkcId(self.TRA_chain)

        if self.TRB_chain is not None and not isinstance(self.TRB_chain, ChainAkcId):
            self.TRB_chain = ChainAkcId(self.TRB_chain)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class GammaDeltaTCR(TCellReceptor):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GO["0042106"]
    class_class_curie: ClassVar[str] = "GO:0042106"
    class_name: ClassVar[str] = "GammaDeltaTCR"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.GammaDeltaTCR

    akc_id: Union[str, GammaDeltaTCRAkcId] = None
    TRG_chain: Optional[Union[str, ChainAkcId]] = None
    TRD_chain: Optional[Union[str, ChainAkcId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, GammaDeltaTCRAkcId):
            self.akc_id = GammaDeltaTCRAkcId(self.akc_id)

        if self.TRG_chain is not None and not isinstance(self.TRG_chain, ChainAkcId):
            self.TRG_chain = ChainAkcId(self.TRG_chain)

        if self.TRD_chain is not None and not isinstance(self.TRD_chain, ChainAkcId):
            self.TRD_chain = ChainAkcId(self.TRD_chain)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class BCellReceptor(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["BCellReceptor"]
    class_class_curie: ClassVar[str] = "ak_schema:BCellReceptor"
    class_name: ClassVar[str] = "BCellReceptor"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.BCellReceptor

    akc_id: Union[str, BCellReceptorAkcId] = None
    IGH_chain: Optional[Union[str, ChainAkcId]] = None
    IGK_chain: Optional[Union[str, ChainAkcId]] = None
    IGL_chain: Optional[Union[str, ChainAkcId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, BCellReceptorAkcId):
            self.akc_id = BCellReceptorAkcId(self.akc_id)

        if self.IGH_chain is not None and not isinstance(self.IGH_chain, ChainAkcId):
            self.IGH_chain = ChainAkcId(self.IGH_chain)

        if self.IGK_chain is not None and not isinstance(self.IGK_chain, ChainAkcId):
            self.IGK_chain = ChainAkcId(self.IGK_chain)

        if self.IGL_chain is not None and not isinstance(self.IGL_chain, ChainAkcId):
            self.IGL_chain = ChainAkcId(self.IGL_chain)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Epitope(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Epitope"]
    class_class_curie: ClassVar[str] = "ak_schema:Epitope"
    class_name: ClassVar[str] = "Epitope"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Epitope

    akc_id: Union[str, EpitopeAkcId] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, EpitopeAkcId):
            self.akc_id = EpitopeAkcId(self.akc_id)

        self.type = str(self.class_name)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class PeptidicEpitope(Epitope):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["PeptidicEpitope"]
    class_class_curie: ClassVar[str] = "ak_schema:PeptidicEpitope"
    class_name: ClassVar[str] = "PeptidicEpitope"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.PeptidicEpitope

    akc_id: Union[str, PeptidicEpitopeAkcId] = None
    sequence_aa: Optional[str] = None
    source_protein: Optional[str] = None
    source_organism: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, PeptidicEpitopeAkcId):
            self.akc_id = PeptidicEpitopeAkcId(self.akc_id)

        if self.sequence_aa is not None and not isinstance(self.sequence_aa, str):
            self.sequence_aa = str(self.sequence_aa)

        if self.source_protein is not None and not isinstance(self.source_protein, str):
            self.source_protein = str(self.source_protein)

        if self.source_organism is not None and not isinstance(self.source_organism, str):
            self.source_organism = str(self.source_organism)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Model(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXO["0000072"]
    class_class_curie: ClassVar[str] = "EXO:0000072"
    class_name: ClassVar[str] = "Model"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Model

    akc_id: Union[str, ModelAkcId] = None

@dataclass(repr=False)
class ConceptualModel(Model):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXO["0000073"]
    class_class_curie: ClassVar[str] = "EXO:0000073"
    class_name: ClassVar[str] = "ConceptualModel"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.ConceptualModel

    akc_id: Union[str, ConceptualModelAkcId] = None

@dataclass(repr=False)
class CommunicativeModel(Model):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["CommunicativeModel"]
    class_class_curie: ClassVar[str] = "ak_schema:CommunicativeModel"
    class_name: ClassVar[str] = "CommunicativeModel"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.CommunicativeModel

    akc_id: Union[str, CommunicativeModelAkcId] = None

@dataclass(repr=False)
class ModelSpecification(PlanSpecification):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["ModelSpecification"]
    class_class_curie: ClassVar[str] = "ak_schema:ModelSpecification"
    class_name: ClassVar[str] = "ModelSpecification"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.ModelSpecification

    akc_id: Union[str, ModelSpecificationAkcId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, ModelSpecificationAkcId):
            self.akc_id = ModelSpecificationAkcId(self.akc_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelingFramework(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SBO["0000004"]
    class_class_curie: ClassVar[str] = "SBO:0000004"
    class_name: ClassVar[str] = "ModelingFramework"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.ModelingFramework

    akc_id: Union[str, ModelingFrameworkAkcId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, ModelingFrameworkAkcId):
            self.akc_id = ModelingFrameworkAkcId(self.akc_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Simulation(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = APOLLO_SV["00000070"]
    class_class_curie: ClassVar[str] = "APOLLO_SV:00000070"
    class_name: ClassVar[str] = "Simulation"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Simulation

    akc_id: Union[str, SimulationAkcId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, SimulationAkcId):
            self.akc_id = SimulationAkcId(self.akc_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SimilarityCalculation(AKObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0200113"]
    class_class_curie: ClassVar[str] = "OBI:0200113"
    class_name: ClassVar[str] = "SimilarityCalculation"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.SimilarityCalculation

    akc_id: Union[str, SimilarityCalculationAkcId] = None
    chain_domain: Optional[Union[str, ChainAkcId]] = None
    chain_codomain: Optional[Union[str, ChainAkcId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, SimilarityCalculationAkcId):
            self.akc_id = SimilarityCalculationAkcId(self.akc_id)

        if self.chain_domain is not None and not isinstance(self.chain_domain, ChainAkcId):
            self.chain_domain = ChainAkcId(self.chain_domain)

        if self.chain_codomain is not None and not isinstance(self.chain_codomain, ChainAkcId):
            self.chain_codomain = ChainAkcId(self.chain_codomain)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChainSimilarity(SimilarityCalculation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["ChainSimilarity"]
    class_class_curie: ClassVar[str] = "ak_schema:ChainSimilarity"
    class_name: ClassVar[str] = "ChainSimilarity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.ChainSimilarity

    akc_id: Union[str, ChainSimilarityAkcId] = None
    chain_similarity_type: Optional[Union[str, "ChainSimilarityType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, ChainSimilarityAkcId):
            self.akc_id = ChainSimilarityAkcId(self.akc_id)

        if self.chain_similarity_type is not None and not isinstance(self.chain_similarity_type, ChainSimilarityType):
            self.chain_similarity_type = ChainSimilarityType(self.chain_similarity_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TimePoint(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["TimePoint"]
    class_class_curie: ClassVar[str] = "ak_schema:TimePoint"
    class_name: ClassVar[str] = "TimePoint"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.TimePoint

    label: Optional[str] = None
    value: Optional[str] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Acknowledgement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Acknowledgement"]
    class_class_curie: ClassVar[str] = "ak_schema:Acknowledgement"
    class_name: ClassVar[str] = "Acknowledgement"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Acknowledgement

    acknowledgement_id: Optional[str] = None
    name: Optional[str] = None
    institution_name: Optional[str] = None
    orcid_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.acknowledgement_id is not None and not isinstance(self.acknowledgement_id, str):
            self.acknowledgement_id = str(self.acknowledgement_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.institution_name is not None and not isinstance(self.institution_name, str):
            self.institution_name = str(self.institution_name)

        if self.orcid_id is not None and not isinstance(self.orcid_id, str):
            self.orcid_id = str(self.orcid_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["RearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:RearrangedSequence"
    class_name: ClassVar[str] = "RearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.RearrangedSequence

    sequence_id: Optional[str] = None
    sequence: Optional[str] = None
    derivation: Optional[Union[str, "Derivation"]] = None
    observation_type: Optional[Union[str, "ObservationType"]] = None
    curation: Optional[str] = None
    repository_name: Optional[str] = None
    repository_ref: Optional[str] = None
    deposited_version: Optional[str] = None
    sequence_start: Optional[int] = None
    sequence_end: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sequence_id is not None and not isinstance(self.sequence_id, str):
            self.sequence_id = str(self.sequence_id)

        if self.sequence is not None and not isinstance(self.sequence, str):
            self.sequence = str(self.sequence)

        if self.derivation is not None and not isinstance(self.derivation, Derivation):
            self.derivation = Derivation(self.derivation)

        if self.observation_type is not None and not isinstance(self.observation_type, ObservationType):
            self.observation_type = ObservationType(self.observation_type)

        if self.curation is not None and not isinstance(self.curation, str):
            self.curation = str(self.curation)

        if self.repository_name is not None and not isinstance(self.repository_name, str):
            self.repository_name = str(self.repository_name)

        if self.repository_ref is not None and not isinstance(self.repository_ref, str):
            self.repository_ref = str(self.repository_ref)

        if self.deposited_version is not None and not isinstance(self.deposited_version, str):
            self.deposited_version = str(self.deposited_version)

        if self.sequence_start is not None and not isinstance(self.sequence_start, int):
            self.sequence_start = int(self.sequence_start)

        if self.sequence_end is not None and not isinstance(self.sequence_end, int):
            self.sequence_end = int(self.sequence_end)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UnrearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["UnrearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:UnrearrangedSequence"
    class_name: ClassVar[str] = "UnrearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.UnrearrangedSequence

    sequence_id: Optional[str] = None
    sequence: Optional[str] = None
    curation: Optional[str] = None
    repository_name: Optional[str] = None
    repository_ref: Optional[str] = None
    patch_no: Optional[str] = None
    gff_seqid: Optional[str] = None
    gff_start: Optional[int] = None
    gff_end: Optional[int] = None
    strand: Optional[Union[str, "Strand"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sequence_id is not None and not isinstance(self.sequence_id, str):
            self.sequence_id = str(self.sequence_id)

        if self.sequence is not None and not isinstance(self.sequence, str):
            self.sequence = str(self.sequence)

        if self.curation is not None and not isinstance(self.curation, str):
            self.curation = str(self.curation)

        if self.repository_name is not None and not isinstance(self.repository_name, str):
            self.repository_name = str(self.repository_name)

        if self.repository_ref is not None and not isinstance(self.repository_ref, str):
            self.repository_ref = str(self.repository_ref)

        if self.patch_no is not None and not isinstance(self.patch_no, str):
            self.patch_no = str(self.patch_no)

        if self.gff_seqid is not None and not isinstance(self.gff_seqid, str):
            self.gff_seqid = str(self.gff_seqid)

        if self.gff_start is not None and not isinstance(self.gff_start, int):
            self.gff_start = int(self.gff_start)

        if self.gff_end is not None and not isinstance(self.gff_end, int):
            self.gff_end = int(self.gff_end)

        if self.strand is not None and not isinstance(self.strand, Strand):
            self.strand = Strand(self.strand)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SequenceDelineationV(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["SequenceDelineationV"]
    class_class_curie: ClassVar[str] = "ak_schema:SequenceDelineationV"
    class_name: ClassVar[str] = "SequenceDelineationV"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.SequenceDelineationV

    sequence_delineation_id: Optional[str] = None
    delineation_scheme: Optional[str] = None
    unaligned_sequence: Optional[str] = None
    aligned_sequence: Optional[str] = None
    fwr1_start: Optional[int] = None
    fwr1_end: Optional[int] = None
    cdr1_start: Optional[int] = None
    cdr1_end: Optional[int] = None
    fwr2_start: Optional[int] = None
    fwr2_end: Optional[int] = None
    cdr2_start: Optional[int] = None
    cdr2_end: Optional[int] = None
    fwr3_start: Optional[int] = None
    fwr3_end: Optional[int] = None
    cdr3_start: Optional[int] = None
    alignment_labels: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sequence_delineation_id is not None and not isinstance(self.sequence_delineation_id, str):
            self.sequence_delineation_id = str(self.sequence_delineation_id)

        if self.delineation_scheme is not None and not isinstance(self.delineation_scheme, str):
            self.delineation_scheme = str(self.delineation_scheme)

        if self.unaligned_sequence is not None and not isinstance(self.unaligned_sequence, str):
            self.unaligned_sequence = str(self.unaligned_sequence)

        if self.aligned_sequence is not None and not isinstance(self.aligned_sequence, str):
            self.aligned_sequence = str(self.aligned_sequence)

        if self.fwr1_start is not None and not isinstance(self.fwr1_start, int):
            self.fwr1_start = int(self.fwr1_start)

        if self.fwr1_end is not None and not isinstance(self.fwr1_end, int):
            self.fwr1_end = int(self.fwr1_end)

        if self.cdr1_start is not None and not isinstance(self.cdr1_start, int):
            self.cdr1_start = int(self.cdr1_start)

        if self.cdr1_end is not None and not isinstance(self.cdr1_end, int):
            self.cdr1_end = int(self.cdr1_end)

        if self.fwr2_start is not None and not isinstance(self.fwr2_start, int):
            self.fwr2_start = int(self.fwr2_start)

        if self.fwr2_end is not None and not isinstance(self.fwr2_end, int):
            self.fwr2_end = int(self.fwr2_end)

        if self.cdr2_start is not None and not isinstance(self.cdr2_start, int):
            self.cdr2_start = int(self.cdr2_start)

        if self.cdr2_end is not None and not isinstance(self.cdr2_end, int):
            self.cdr2_end = int(self.cdr2_end)

        if self.fwr3_start is not None and not isinstance(self.fwr3_start, int):
            self.fwr3_start = int(self.fwr3_start)

        if self.fwr3_end is not None and not isinstance(self.fwr3_end, int):
            self.fwr3_end = int(self.fwr3_end)

        if self.cdr3_start is not None and not isinstance(self.cdr3_start, int):
            self.cdr3_start = int(self.cdr3_start)

        if not isinstance(self.alignment_labels, list):
            self.alignment_labels = [self.alignment_labels] if self.alignment_labels is not None else []
        self.alignment_labels = [v if isinstance(v, str) else str(v) for v in self.alignment_labels]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AlleleDescription(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AlleleDescription"]
    class_class_curie: ClassVar[str] = "ak_schema:AlleleDescription"
    class_name: ClassVar[str] = "AlleleDescription"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AlleleDescription

    allele_description_id: Optional[str] = None
    allele_description_ref: Optional[str] = None
    maintainer: Optional[str] = None
    acknowledgements: Optional[Union[Union[dict, Acknowledgement], List[Union[dict, Acknowledgement]]]] = empty_list()
    lab_address: Optional[str] = None
    release_version: Optional[str] = None
    release_date: Optional[Union[str, XSDDateTime]] = None
    release_description: Optional[str] = None
    label: Optional[str] = None
    sequence: Optional[str] = None
    coding_sequence: Optional[str] = None
    aliases: Optional[Union[str, List[str]]] = empty_list()
    locus: Optional[Union[str, "Locus"]] = None
    chromosome: Optional[int] = None
    sequence_type: Optional[Union[str, "SequenceType"]] = None
    functional: Optional[Union[bool, Bool]] = None
    inference_type: Optional[Union[str, "InferenceType"]] = None
    species: Optional[Union[str, "Species"]] = None
    species_subgroup: Optional[str] = None
    species_subgroup_type: Optional[Union[str, "SpeciesSubgroupType"]] = None
    status: Optional[Union[str, "Status"]] = None
    subgroup_designation: Optional[str] = None
    gene_designation: Optional[str] = None
    allele_designation: Optional[str] = None
    allele_similarity_cluster_designation: Optional[str] = None
    allele_similarity_cluster_member_id: Optional[str] = None
    j_codon_frame: Optional[Union[str, "JCodonFrame"]] = None
    gene_start: Optional[int] = None
    gene_end: Optional[int] = None
    utr_5_prime_start: Optional[int] = None
    utr_5_prime_end: Optional[int] = None
    leader_1_start: Optional[int] = None
    leader_1_end: Optional[int] = None
    leader_2_start: Optional[int] = None
    leader_2_end: Optional[int] = None
    v_rs_start: Optional[int] = None
    v_rs_end: Optional[int] = None
    d_rs_3_prime_start: Optional[int] = None
    d_rs_3_prime_end: Optional[int] = None
    d_rs_5_prime_start: Optional[int] = None
    d_rs_5_prime_end: Optional[int] = None
    j_cdr3_end: Optional[int] = None
    j_rs_start: Optional[int] = None
    j_rs_end: Optional[int] = None
    j_donor_splice: Optional[int] = None
    v_gene_delineations: Optional[Union[Union[dict, SequenceDelineationV], List[Union[dict, SequenceDelineationV]]]] = empty_list()
    unrearranged_support: Optional[Union[Union[dict, UnrearrangedSequence], List[Union[dict, UnrearrangedSequence]]]] = empty_list()
    rearranged_support: Optional[Union[Union[dict, RearrangedSequence], List[Union[dict, RearrangedSequence]]]] = empty_list()
    paralogs: Optional[Union[str, List[str]]] = empty_list()
    curation: Optional[str] = None
    curational_tags: Optional[Union[Union[str, "CurationalTags"], List[Union[str, "CurationalTags"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.allele_description_id is not None and not isinstance(self.allele_description_id, str):
            self.allele_description_id = str(self.allele_description_id)

        if self.allele_description_ref is not None and not isinstance(self.allele_description_ref, str):
            self.allele_description_ref = str(self.allele_description_ref)

        if self.maintainer is not None and not isinstance(self.maintainer, str):
            self.maintainer = str(self.maintainer)

        if not isinstance(self.acknowledgements, list):
            self.acknowledgements = [self.acknowledgements] if self.acknowledgements is not None else []
        self.acknowledgements = [v if isinstance(v, Acknowledgement) else Acknowledgement(**as_dict(v)) for v in self.acknowledgements]

        if self.lab_address is not None and not isinstance(self.lab_address, str):
            self.lab_address = str(self.lab_address)

        if self.release_version is not None and not isinstance(self.release_version, str):
            self.release_version = str(self.release_version)

        if self.release_date is not None and not isinstance(self.release_date, XSDDateTime):
            self.release_date = XSDDateTime(self.release_date)

        if self.release_description is not None and not isinstance(self.release_description, str):
            self.release_description = str(self.release_description)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.sequence is not None and not isinstance(self.sequence, str):
            self.sequence = str(self.sequence)

        if self.coding_sequence is not None and not isinstance(self.coding_sequence, str):
            self.coding_sequence = str(self.coding_sequence)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if self.locus is not None and not isinstance(self.locus, Locus):
            self.locus = Locus(self.locus)

        if self.chromosome is not None and not isinstance(self.chromosome, int):
            self.chromosome = int(self.chromosome)

        if self.sequence_type is not None and not isinstance(self.sequence_type, SequenceType):
            self.sequence_type = SequenceType(self.sequence_type)

        if self.functional is not None and not isinstance(self.functional, Bool):
            self.functional = Bool(self.functional)

        if self.inference_type is not None and not isinstance(self.inference_type, InferenceType):
            self.inference_type = InferenceType(self.inference_type)

        if self.species is not None and not isinstance(self.species, Species):
            self.species = Species(self.species)

        if self.species_subgroup is not None and not isinstance(self.species_subgroup, str):
            self.species_subgroup = str(self.species_subgroup)

        if self.species_subgroup_type is not None and not isinstance(self.species_subgroup_type, SpeciesSubgroupType):
            self.species_subgroup_type = SpeciesSubgroupType(self.species_subgroup_type)

        if self.status is not None and not isinstance(self.status, Status):
            self.status = Status(self.status)

        if self.subgroup_designation is not None and not isinstance(self.subgroup_designation, str):
            self.subgroup_designation = str(self.subgroup_designation)

        if self.gene_designation is not None and not isinstance(self.gene_designation, str):
            self.gene_designation = str(self.gene_designation)

        if self.allele_designation is not None and not isinstance(self.allele_designation, str):
            self.allele_designation = str(self.allele_designation)

        if self.allele_similarity_cluster_designation is not None and not isinstance(self.allele_similarity_cluster_designation, str):
            self.allele_similarity_cluster_designation = str(self.allele_similarity_cluster_designation)

        if self.allele_similarity_cluster_member_id is not None and not isinstance(self.allele_similarity_cluster_member_id, str):
            self.allele_similarity_cluster_member_id = str(self.allele_similarity_cluster_member_id)

        if self.j_codon_frame is not None and not isinstance(self.j_codon_frame, JCodonFrame):
            self.j_codon_frame = JCodonFrame(self.j_codon_frame)

        if self.gene_start is not None and not isinstance(self.gene_start, int):
            self.gene_start = int(self.gene_start)

        if self.gene_end is not None and not isinstance(self.gene_end, int):
            self.gene_end = int(self.gene_end)

        if self.utr_5_prime_start is not None and not isinstance(self.utr_5_prime_start, int):
            self.utr_5_prime_start = int(self.utr_5_prime_start)

        if self.utr_5_prime_end is not None and not isinstance(self.utr_5_prime_end, int):
            self.utr_5_prime_end = int(self.utr_5_prime_end)

        if self.leader_1_start is not None and not isinstance(self.leader_1_start, int):
            self.leader_1_start = int(self.leader_1_start)

        if self.leader_1_end is not None and not isinstance(self.leader_1_end, int):
            self.leader_1_end = int(self.leader_1_end)

        if self.leader_2_start is not None and not isinstance(self.leader_2_start, int):
            self.leader_2_start = int(self.leader_2_start)

        if self.leader_2_end is not None and not isinstance(self.leader_2_end, int):
            self.leader_2_end = int(self.leader_2_end)

        if self.v_rs_start is not None and not isinstance(self.v_rs_start, int):
            self.v_rs_start = int(self.v_rs_start)

        if self.v_rs_end is not None and not isinstance(self.v_rs_end, int):
            self.v_rs_end = int(self.v_rs_end)

        if self.d_rs_3_prime_start is not None and not isinstance(self.d_rs_3_prime_start, int):
            self.d_rs_3_prime_start = int(self.d_rs_3_prime_start)

        if self.d_rs_3_prime_end is not None and not isinstance(self.d_rs_3_prime_end, int):
            self.d_rs_3_prime_end = int(self.d_rs_3_prime_end)

        if self.d_rs_5_prime_start is not None and not isinstance(self.d_rs_5_prime_start, int):
            self.d_rs_5_prime_start = int(self.d_rs_5_prime_start)

        if self.d_rs_5_prime_end is not None and not isinstance(self.d_rs_5_prime_end, int):
            self.d_rs_5_prime_end = int(self.d_rs_5_prime_end)

        if self.j_cdr3_end is not None and not isinstance(self.j_cdr3_end, int):
            self.j_cdr3_end = int(self.j_cdr3_end)

        if self.j_rs_start is not None and not isinstance(self.j_rs_start, int):
            self.j_rs_start = int(self.j_rs_start)

        if self.j_rs_end is not None and not isinstance(self.j_rs_end, int):
            self.j_rs_end = int(self.j_rs_end)

        if self.j_donor_splice is not None and not isinstance(self.j_donor_splice, int):
            self.j_donor_splice = int(self.j_donor_splice)

        if not isinstance(self.v_gene_delineations, list):
            self.v_gene_delineations = [self.v_gene_delineations] if self.v_gene_delineations is not None else []
        self.v_gene_delineations = [v if isinstance(v, SequenceDelineationV) else SequenceDelineationV(**as_dict(v)) for v in self.v_gene_delineations]

        if not isinstance(self.unrearranged_support, list):
            self.unrearranged_support = [self.unrearranged_support] if self.unrearranged_support is not None else []
        self.unrearranged_support = [v if isinstance(v, UnrearrangedSequence) else UnrearrangedSequence(**as_dict(v)) for v in self.unrearranged_support]

        if not isinstance(self.rearranged_support, list):
            self.rearranged_support = [self.rearranged_support] if self.rearranged_support is not None else []
        self.rearranged_support = [v if isinstance(v, RearrangedSequence) else RearrangedSequence(**as_dict(v)) for v in self.rearranged_support]

        if not isinstance(self.paralogs, list):
            self.paralogs = [self.paralogs] if self.paralogs is not None else []
        self.paralogs = [v if isinstance(v, str) else str(v) for v in self.paralogs]

        if self.curation is not None and not isinstance(self.curation, str):
            self.curation = str(self.curation)

        if not isinstance(self.curational_tags, list):
            self.curational_tags = [self.curational_tags] if self.curational_tags is not None else []
        self.curational_tags = [v if isinstance(v, CurationalTags) else CurationalTags(v) for v in self.curational_tags]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GermlineSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["GermlineSet"]
    class_class_curie: ClassVar[str] = "ak_schema:GermlineSet"
    class_name: ClassVar[str] = "GermlineSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.GermlineSet

    germline_set_id: Optional[str] = None
    author: Optional[str] = None
    lab_name: Optional[str] = None
    lab_address: Optional[str] = None
    acknowledgements: Optional[Union[Union[dict, Acknowledgement], List[Union[dict, Acknowledgement]]]] = empty_list()
    release_version: Optional[str] = None
    release_description: Optional[str] = None
    release_date: Optional[Union[str, XSDDateTime]] = None
    germline_set_name: Optional[str] = None
    germline_set_ref: Optional[str] = None
    pub_ids: Optional[str] = None
    species: Optional[Union[str, "Species"]] = None
    species_subgroup: Optional[str] = None
    species_subgroup_type: Optional[Union[str, "SpeciesSubgroupType"]] = None
    locus: Optional[Union[str, "Locus"]] = None
    allele_descriptions: Optional[Union[Union[dict, AlleleDescription], List[Union[dict, AlleleDescription]]]] = empty_list()
    curation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.germline_set_id is not None and not isinstance(self.germline_set_id, str):
            self.germline_set_id = str(self.germline_set_id)

        if self.author is not None and not isinstance(self.author, str):
            self.author = str(self.author)

        if self.lab_name is not None and not isinstance(self.lab_name, str):
            self.lab_name = str(self.lab_name)

        if self.lab_address is not None and not isinstance(self.lab_address, str):
            self.lab_address = str(self.lab_address)

        if not isinstance(self.acknowledgements, list):
            self.acknowledgements = [self.acknowledgements] if self.acknowledgements is not None else []
        self.acknowledgements = [v if isinstance(v, Acknowledgement) else Acknowledgement(**as_dict(v)) for v in self.acknowledgements]

        if self.release_version is not None and not isinstance(self.release_version, str):
            self.release_version = str(self.release_version)

        if self.release_description is not None and not isinstance(self.release_description, str):
            self.release_description = str(self.release_description)

        if self.release_date is not None and not isinstance(self.release_date, XSDDateTime):
            self.release_date = XSDDateTime(self.release_date)

        if self.germline_set_name is not None and not isinstance(self.germline_set_name, str):
            self.germline_set_name = str(self.germline_set_name)

        if self.germline_set_ref is not None and not isinstance(self.germline_set_ref, str):
            self.germline_set_ref = str(self.germline_set_ref)

        if self.pub_ids is not None and not isinstance(self.pub_ids, str):
            self.pub_ids = str(self.pub_ids)

        if self.species is not None and not isinstance(self.species, Species):
            self.species = Species(self.species)

        if self.species_subgroup is not None and not isinstance(self.species_subgroup, str):
            self.species_subgroup = str(self.species_subgroup)

        if self.species_subgroup_type is not None and not isinstance(self.species_subgroup_type, SpeciesSubgroupType):
            self.species_subgroup_type = SpeciesSubgroupType(self.species_subgroup_type)

        if self.locus is not None and not isinstance(self.locus, Locus):
            self.locus = Locus(self.locus)

        if not isinstance(self.allele_descriptions, list):
            self.allele_descriptions = [self.allele_descriptions] if self.allele_descriptions is not None else []
        self.allele_descriptions = [v if isinstance(v, AlleleDescription) else AlleleDescription(**as_dict(v)) for v in self.allele_descriptions]

        if self.curation is not None and not isinstance(self.curation, str):
            self.curation = str(self.curation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["GenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:GenotypeSet"
    class_name: ClassVar[str] = "GenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.GenotypeSet

    receptor_genotype_set_id: Optional[str] = None
    genotype_class_list: Optional[Union[Union[dict, "Genotype"], List[Union[dict, "Genotype"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.receptor_genotype_set_id is not None and not isinstance(self.receptor_genotype_set_id, str):
            self.receptor_genotype_set_id = str(self.receptor_genotype_set_id)

        if not isinstance(self.genotype_class_list, list):
            self.genotype_class_list = [self.genotype_class_list] if self.genotype_class_list is not None else []
        self.genotype_class_list = [v if isinstance(v, Genotype) else Genotype(**as_dict(v)) for v in self.genotype_class_list]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Genotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Genotype"]
    class_class_curie: ClassVar[str] = "ak_schema:Genotype"
    class_name: ClassVar[str] = "Genotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Genotype

    receptor_genotype_id: Optional[str] = None
    locus: Optional[Union[str, "Locus"]] = None
    documented_alleles: Optional[Union[Union[dict, "DocumentedAllele"], List[Union[dict, "DocumentedAllele"]]]] = empty_list()
    undocumented_alleles: Optional[Union[Union[dict, "UndocumentedAllele"], List[Union[dict, "UndocumentedAllele"]]]] = empty_list()
    deleted_genes: Optional[Union[Union[dict, "DeletedGene"], List[Union[dict, "DeletedGene"]]]] = empty_list()
    inference_process: Optional[Union[str, "InferenceProcess"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.receptor_genotype_id is not None and not isinstance(self.receptor_genotype_id, str):
            self.receptor_genotype_id = str(self.receptor_genotype_id)

        if self.locus is not None and not isinstance(self.locus, Locus):
            self.locus = Locus(self.locus)

        if not isinstance(self.documented_alleles, list):
            self.documented_alleles = [self.documented_alleles] if self.documented_alleles is not None else []
        self.documented_alleles = [v if isinstance(v, DocumentedAllele) else DocumentedAllele(**as_dict(v)) for v in self.documented_alleles]

        if not isinstance(self.undocumented_alleles, list):
            self.undocumented_alleles = [self.undocumented_alleles] if self.undocumented_alleles is not None else []
        self.undocumented_alleles = [v if isinstance(v, UndocumentedAllele) else UndocumentedAllele(**as_dict(v)) for v in self.undocumented_alleles]

        if not isinstance(self.deleted_genes, list):
            self.deleted_genes = [self.deleted_genes] if self.deleted_genes is not None else []
        self.deleted_genes = [v if isinstance(v, DeletedGene) else DeletedGene(**as_dict(v)) for v in self.deleted_genes]

        if self.inference_process is not None and not isinstance(self.inference_process, InferenceProcess):
            self.inference_process = InferenceProcess(self.inference_process)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["DocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:DocumentedAllele"
    class_name: ClassVar[str] = "DocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.DocumentedAllele

    label: Optional[str] = None
    germline_set_ref: Optional[str] = None
    phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.germline_set_ref is not None and not isinstance(self.germline_set_ref, str):
            self.germline_set_ref = str(self.germline_set_ref)

        if self.phasing is not None and not isinstance(self.phasing, int):
            self.phasing = int(self.phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UndocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["UndocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:UndocumentedAllele"
    class_name: ClassVar[str] = "UndocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.UndocumentedAllele

    allele_name: Optional[str] = None
    sequence: Optional[str] = None
    phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.allele_name is not None and not isinstance(self.allele_name, str):
            self.allele_name = str(self.allele_name)

        if self.sequence is not None and not isinstance(self.sequence, str):
            self.sequence = str(self.sequence)

        if self.phasing is not None and not isinstance(self.phasing, int):
            self.phasing = int(self.phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DeletedGene(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["DeletedGene"]
    class_class_curie: ClassVar[str] = "ak_schema:DeletedGene"
    class_name: ClassVar[str] = "DeletedGene"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.DeletedGene

    label: Optional[str] = None
    germline_set_ref: Optional[str] = None
    phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.germline_set_ref is not None and not isinstance(self.germline_set_ref, str):
            self.germline_set_ref = str(self.germline_set_ref)

        if self.phasing is not None and not isinstance(self.phasing, int):
            self.phasing = int(self.phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MHCGenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["MHCGenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:MHCGenotypeSet"
    class_name: ClassVar[str] = "MHCGenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.MHCGenotypeSet

    mhc_genotype_set_id: Optional[str] = None
    mhc_genotype_list: Optional[Union[Union[dict, "MHCGenotype"], List[Union[dict, "MHCGenotype"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.mhc_genotype_set_id is not None and not isinstance(self.mhc_genotype_set_id, str):
            self.mhc_genotype_set_id = str(self.mhc_genotype_set_id)

        if not isinstance(self.mhc_genotype_list, list):
            self.mhc_genotype_list = [self.mhc_genotype_list] if self.mhc_genotype_list is not None else []
        self.mhc_genotype_list = [v if isinstance(v, MHCGenotype) else MHCGenotype(**as_dict(v)) for v in self.mhc_genotype_list]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MHCGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["MHCGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:MHCGenotype"
    class_name: ClassVar[str] = "MHCGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.MHCGenotype

    mhc_genotype_id: Optional[str] = None
    mhc_class: Optional[Union[str, "MhcClass"]] = None
    mhc_alleles: Optional[Union[Union[dict, "MHCAllele"], List[Union[dict, "MHCAllele"]]]] = empty_list()
    mhc_genotyping_method: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.mhc_genotype_id is not None and not isinstance(self.mhc_genotype_id, str):
            self.mhc_genotype_id = str(self.mhc_genotype_id)

        if self.mhc_class is not None and not isinstance(self.mhc_class, MhcClass):
            self.mhc_class = MhcClass(self.mhc_class)

        if not isinstance(self.mhc_alleles, list):
            self.mhc_alleles = [self.mhc_alleles] if self.mhc_alleles is not None else []
        self.mhc_alleles = [v if isinstance(v, MHCAllele) else MHCAllele(**as_dict(v)) for v in self.mhc_alleles]

        if self.mhc_genotyping_method is not None and not isinstance(self.mhc_genotyping_method, str):
            self.mhc_genotyping_method = str(self.mhc_genotyping_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MHCAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["MHCAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:MHCAllele"
    class_name: ClassVar[str] = "MHCAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.MHCAllele

    allele_designation: Optional[str] = None
    gene: Optional[Union[str, "Gene"]] = None
    reference_set_ref: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.allele_designation is not None and not isinstance(self.allele_designation, str):
            self.allele_designation = str(self.allele_designation)

        if self.reference_set_ref is not None and not isinstance(self.reference_set_ref, str):
            self.reference_set_ref = str(self.reference_set_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubjectGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["SubjectGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:SubjectGenotype"
    class_name: ClassVar[str] = "SubjectGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.SubjectGenotype

    receptor_genotype_set: Optional[Union[dict, GenotypeSet]] = None
    mhc_genotype_set: Optional[Union[dict, MHCGenotypeSet]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.receptor_genotype_set is not None and not isinstance(self.receptor_genotype_set, GenotypeSet):
            self.receptor_genotype_set = GenotypeSet(**as_dict(self.receptor_genotype_set))

        if self.mhc_genotype_set is not None and not isinstance(self.mhc_genotype_set, MHCGenotypeSet):
            self.mhc_genotype_set = MHCGenotypeSet(**as_dict(self.mhc_genotype_set))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Study(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Study"]
    class_class_curie: ClassVar[str] = "ak_schema:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Study

    study_id: Optional[str] = None
    study_title: Optional[str] = None
    study_type: Optional[Union[str, "StudyType"]] = None
    study_description: Optional[str] = None
    inclusion_exclusion_criteria: Optional[str] = None
    grants: Optional[str] = None
    study_contact: Optional[str] = None
    collected_by: Optional[str] = None
    lab_name: Optional[str] = None
    lab_address: Optional[str] = None
    submitted_by: Optional[str] = None
    pub_ids: Optional[str] = None
    keywords_study: Optional[Union[Union[str, "KeywordsStudy"], List[Union[str, "KeywordsStudy"]]]] = empty_list()
    adc_publish_date: Optional[Union[str, XSDDateTime]] = None
    adc_update_date: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.study_id is not None and not isinstance(self.study_id, str):
            self.study_id = str(self.study_id)

        if self.study_title is not None and not isinstance(self.study_title, str):
            self.study_title = str(self.study_title)

        if self.study_description is not None and not isinstance(self.study_description, str):
            self.study_description = str(self.study_description)

        if self.inclusion_exclusion_criteria is not None and not isinstance(self.inclusion_exclusion_criteria, str):
            self.inclusion_exclusion_criteria = str(self.inclusion_exclusion_criteria)

        if self.grants is not None and not isinstance(self.grants, str):
            self.grants = str(self.grants)

        if self.study_contact is not None and not isinstance(self.study_contact, str):
            self.study_contact = str(self.study_contact)

        if self.collected_by is not None and not isinstance(self.collected_by, str):
            self.collected_by = str(self.collected_by)

        if self.lab_name is not None and not isinstance(self.lab_name, str):
            self.lab_name = str(self.lab_name)

        if self.lab_address is not None and not isinstance(self.lab_address, str):
            self.lab_address = str(self.lab_address)

        if self.submitted_by is not None and not isinstance(self.submitted_by, str):
            self.submitted_by = str(self.submitted_by)

        if self.pub_ids is not None and not isinstance(self.pub_ids, str):
            self.pub_ids = str(self.pub_ids)

        if not isinstance(self.keywords_study, list):
            self.keywords_study = [self.keywords_study] if self.keywords_study is not None else []
        self.keywords_study = [v if isinstance(v, KeywordsStudy) else KeywordsStudy(v) for v in self.keywords_study]

        if self.adc_publish_date is not None and not isinstance(self.adc_publish_date, XSDDateTime):
            self.adc_publish_date = XSDDateTime(self.adc_publish_date)

        if self.adc_update_date is not None and not isinstance(self.adc_update_date, XSDDateTime):
            self.adc_update_date = XSDDateTime(self.adc_update_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Subject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Subject"]
    class_class_curie: ClassVar[str] = "ak_schema:Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Subject

    subject_id: Optional[str] = None
    synthetic: Optional[Union[bool, Bool]] = None
    species: Optional[Union[str, "Species"]] = None
    sex: Optional[Union[str, "Sex"]] = None
    age_min: Optional[float] = None
    age_max: Optional[float] = None
    age_unit: Optional[Union[str, "AgeUnit"]] = None
    age_event: Optional[Union[str, LifeEventAkcId]] = None
    ancestry_population: Optional[str] = None
    ethnicity: Optional[Union[str, "Ethnicity"]] = None
    race: Optional[Union[str, "Race"]] = None
    strain_name: Optional[str] = None
    linked_subjects: Optional[str] = None
    link_type: Optional[str] = None
    diagnosis: Optional[Union[Union[dict, "Diagnosis"], List[Union[dict, "Diagnosis"]]]] = empty_list()
    genotype: Optional[Union[dict, SubjectGenotype]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject_id is not None and not isinstance(self.subject_id, str):
            self.subject_id = str(self.subject_id)

        if self.synthetic is not None and not isinstance(self.synthetic, Bool):
            self.synthetic = Bool(self.synthetic)

        if self.species is not None and not isinstance(self.species, Species):
            self.species = Species(self.species)

        if self.sex is not None and not isinstance(self.sex, Sex):
            self.sex = Sex(self.sex)

        if self.age_min is not None and not isinstance(self.age_min, float):
            self.age_min = float(self.age_min)

        if self.age_max is not None and not isinstance(self.age_max, float):
            self.age_max = float(self.age_max)

        if self.age_event is not None and not isinstance(self.age_event, LifeEventAkcId):
            self.age_event = LifeEventAkcId(self.age_event)

        if self.ancestry_population is not None and not isinstance(self.ancestry_population, str):
            self.ancestry_population = str(self.ancestry_population)

        if self.ethnicity is not None and not isinstance(self.ethnicity, Ethnicity):
            self.ethnicity = Ethnicity(self.ethnicity)

        if self.race is not None and not isinstance(self.race, Race):
            self.race = Race(self.race)

        if self.strain_name is not None and not isinstance(self.strain_name, str):
            self.strain_name = str(self.strain_name)

        if self.linked_subjects is not None and not isinstance(self.linked_subjects, str):
            self.linked_subjects = str(self.linked_subjects)

        if self.link_type is not None and not isinstance(self.link_type, str):
            self.link_type = str(self.link_type)

        if not isinstance(self.diagnosis, list):
            self.diagnosis = [self.diagnosis] if self.diagnosis is not None else []
        self.diagnosis = [v if isinstance(v, Diagnosis) else Diagnosis(**as_dict(v)) for v in self.diagnosis]

        if self.genotype is not None and not isinstance(self.genotype, SubjectGenotype):
            self.genotype = SubjectGenotype(**as_dict(self.genotype))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Diagnosis(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Diagnosis"]
    class_class_curie: ClassVar[str] = "ak_schema:Diagnosis"
    class_name: ClassVar[str] = "Diagnosis"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Diagnosis

    study_group_description: Optional[str] = None
    disease_diagnosis: Optional[Union[str, "DiseaseDiagnosis"]] = None
    disease_length: Optional[str] = None
    disease_stage: Optional[Union[str, "DiseaseStage"]] = None
    prior_therapies: Optional[str] = None
    immunogen: Optional[str] = None
    intervention: Optional[str] = None
    medical_history: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.study_group_description is not None and not isinstance(self.study_group_description, str):
            self.study_group_description = str(self.study_group_description)

        if self.disease_length is not None and not isinstance(self.disease_length, str):
            self.disease_length = str(self.disease_length)

        if self.disease_stage is not None and not isinstance(self.disease_stage, DiseaseStage):
            self.disease_stage = DiseaseStage(self.disease_stage)

        if self.prior_therapies is not None and not isinstance(self.prior_therapies, str):
            self.prior_therapies = str(self.prior_therapies)

        if self.immunogen is not None and not isinstance(self.immunogen, str):
            self.immunogen = str(self.immunogen)

        if self.intervention is not None and not isinstance(self.intervention, str):
            self.intervention = str(self.intervention)

        if self.medical_history is not None and not isinstance(self.medical_history, str):
            self.medical_history = str(self.medical_history)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Sample"]
    class_class_curie: ClassVar[str] = "ak_schema:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Sample

    sample_id: Optional[str] = None
    sample_type: Optional[str] = None
    tissue: Optional[Union[str, "Tissue"]] = None
    anatomic_site: Optional[str] = None
    disease_state_sample: Optional[str] = None
    collection_time_point_relative: Optional[float] = None
    collection_time_point_relative_unit: Optional[Union[str, "CollectionTimePointRelativeUnit"]] = None
    collection_time_point_reference: Optional[str] = None
    biomaterial_provider: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sample_id is not None and not isinstance(self.sample_id, str):
            self.sample_id = str(self.sample_id)

        if self.sample_type is not None and not isinstance(self.sample_type, str):
            self.sample_type = str(self.sample_type)

        if self.anatomic_site is not None and not isinstance(self.anatomic_site, str):
            self.anatomic_site = str(self.anatomic_site)

        if self.disease_state_sample is not None and not isinstance(self.disease_state_sample, str):
            self.disease_state_sample = str(self.disease_state_sample)

        if self.collection_time_point_relative is not None and not isinstance(self.collection_time_point_relative, float):
            self.collection_time_point_relative = float(self.collection_time_point_relative)

        if self.collection_time_point_reference is not None and not isinstance(self.collection_time_point_reference, str):
            self.collection_time_point_reference = str(self.collection_time_point_reference)

        if self.biomaterial_provider is not None and not isinstance(self.biomaterial_provider, str):
            self.biomaterial_provider = str(self.biomaterial_provider)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["CellProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:CellProcessing"
    class_name: ClassVar[str] = "CellProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.CellProcessing

    tissue_processing: Optional[str] = None
    cell_subset: Optional[Union[str, "CellSubset"]] = None
    cell_phenotype: Optional[str] = None
    cell_species: Optional[Union[str, "CellSpecies"]] = None
    single_cell: Optional[Union[bool, Bool]] = None
    cell_number: Optional[int] = None
    cells_per_reaction: Optional[int] = None
    cell_storage: Optional[Union[bool, Bool]] = None
    cell_quality: Optional[str] = None
    cell_isolation: Optional[str] = None
    cell_processing_protocol: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.tissue_processing is not None and not isinstance(self.tissue_processing, str):
            self.tissue_processing = str(self.tissue_processing)

        if self.cell_phenotype is not None and not isinstance(self.cell_phenotype, str):
            self.cell_phenotype = str(self.cell_phenotype)

        if self.single_cell is not None and not isinstance(self.single_cell, Bool):
            self.single_cell = Bool(self.single_cell)

        if self.cell_number is not None and not isinstance(self.cell_number, int):
            self.cell_number = int(self.cell_number)

        if self.cells_per_reaction is not None and not isinstance(self.cells_per_reaction, int):
            self.cells_per_reaction = int(self.cells_per_reaction)

        if self.cell_storage is not None and not isinstance(self.cell_storage, Bool):
            self.cell_storage = Bool(self.cell_storage)

        if self.cell_quality is not None and not isinstance(self.cell_quality, str):
            self.cell_quality = str(self.cell_quality)

        if self.cell_isolation is not None and not isinstance(self.cell_isolation, str):
            self.cell_isolation = str(self.cell_isolation)

        if self.cell_processing_protocol is not None and not isinstance(self.cell_processing_protocol, str):
            self.cell_processing_protocol = str(self.cell_processing_protocol)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PCRTarget(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["PCRTarget"]
    class_class_curie: ClassVar[str] = "ak_schema:PCRTarget"
    class_name: ClassVar[str] = "PCRTarget"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.PCRTarget

    pcr_target_locus: Optional[Union[str, "PcrTargetLocus"]] = None
    forward_pcr_primer_target_location: Optional[str] = None
    reverse_pcr_primer_target_location: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.pcr_target_locus is not None and not isinstance(self.pcr_target_locus, PcrTargetLocus):
            self.pcr_target_locus = PcrTargetLocus(self.pcr_target_locus)

        if self.forward_pcr_primer_target_location is not None and not isinstance(self.forward_pcr_primer_target_location, str):
            self.forward_pcr_primer_target_location = str(self.forward_pcr_primer_target_location)

        if self.reverse_pcr_primer_target_location is not None and not isinstance(self.reverse_pcr_primer_target_location, str):
            self.reverse_pcr_primer_target_location = str(self.reverse_pcr_primer_target_location)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SequencingRun(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["SequencingRun"]
    class_class_curie: ClassVar[str] = "ak_schema:SequencingRun"
    class_name: ClassVar[str] = "SequencingRun"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.SequencingRun

    sequencing_run_id: Optional[str] = None
    total_reads_passing_qc_filter: Optional[int] = None
    sequencing_platform: Optional[str] = None
    sequencing_facility: Optional[str] = None
    sequencing_run_date: Optional[Union[str, XSDDateTime]] = None
    sequencing_kit: Optional[str] = None
    sequencing_files: Optional[Union[dict, "SequencingData"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sequencing_run_id is not None and not isinstance(self.sequencing_run_id, str):
            self.sequencing_run_id = str(self.sequencing_run_id)

        if self.total_reads_passing_qc_filter is not None and not isinstance(self.total_reads_passing_qc_filter, int):
            self.total_reads_passing_qc_filter = int(self.total_reads_passing_qc_filter)

        if self.sequencing_platform is not None and not isinstance(self.sequencing_platform, str):
            self.sequencing_platform = str(self.sequencing_platform)

        if self.sequencing_facility is not None and not isinstance(self.sequencing_facility, str):
            self.sequencing_facility = str(self.sequencing_facility)

        if self.sequencing_run_date is not None and not isinstance(self.sequencing_run_date, XSDDateTime):
            self.sequencing_run_date = XSDDateTime(self.sequencing_run_date)

        if self.sequencing_kit is not None and not isinstance(self.sequencing_kit, str):
            self.sequencing_kit = str(self.sequencing_kit)

        if self.sequencing_files is not None and not isinstance(self.sequencing_files, SequencingData):
            self.sequencing_files = SequencingData(**as_dict(self.sequencing_files))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SequencingData(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["SequencingData"]
    class_class_curie: ClassVar[str] = "ak_schema:SequencingData"
    class_name: ClassVar[str] = "SequencingData"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.SequencingData

    sequencing_data_id: Optional[str] = None
    file_type: Optional[Union[str, "FileType"]] = None
    filename: Optional[str] = None
    read_direction: Optional[Union[str, "ReadDirection"]] = None
    read_length: Optional[int] = None
    paired_filename: Optional[str] = None
    paired_read_direction: Optional[Union[str, "PairedReadDirection"]] = None
    paired_read_length: Optional[int] = None
    index_filename: Optional[str] = None
    index_length: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sequencing_data_id is not None and not isinstance(self.sequencing_data_id, str):
            self.sequencing_data_id = str(self.sequencing_data_id)

        if self.file_type is not None and not isinstance(self.file_type, FileType):
            self.file_type = FileType(self.file_type)

        if self.filename is not None and not isinstance(self.filename, str):
            self.filename = str(self.filename)

        if self.read_direction is not None and not isinstance(self.read_direction, ReadDirection):
            self.read_direction = ReadDirection(self.read_direction)

        if self.read_length is not None and not isinstance(self.read_length, int):
            self.read_length = int(self.read_length)

        if self.paired_filename is not None and not isinstance(self.paired_filename, str):
            self.paired_filename = str(self.paired_filename)

        if self.paired_read_direction is not None and not isinstance(self.paired_read_direction, PairedReadDirection):
            self.paired_read_direction = PairedReadDirection(self.paired_read_direction)

        if self.paired_read_length is not None and not isinstance(self.paired_read_length, int):
            self.paired_read_length = int(self.paired_read_length)

        if self.index_filename is not None and not isinstance(self.index_filename, str):
            self.index_filename = str(self.index_filename)

        if self.index_length is not None and not isinstance(self.index_length, int):
            self.index_length = int(self.index_length)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["DataProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:DataProcessing"
    class_name: ClassVar[str] = "DataProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.DataProcessing

    data_processing_id: Optional[str] = None
    primary_annotation: Optional[Union[bool, Bool]] = None
    software_versions: Optional[str] = None
    paired_reads_assembly: Optional[str] = None
    quality_thresholds: Optional[str] = None
    primer_match_cutoffs: Optional[str] = None
    collapsing_method: Optional[str] = None
    data_processing_protocols: Optional[str] = None
    data_processing_files: Optional[Union[str, List[str]]] = empty_list()
    germline_database: Optional[str] = None
    germline_set_ref: Optional[str] = None
    analysis_provenance_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.data_processing_id is not None and not isinstance(self.data_processing_id, str):
            self.data_processing_id = str(self.data_processing_id)

        if self.primary_annotation is not None and not isinstance(self.primary_annotation, Bool):
            self.primary_annotation = Bool(self.primary_annotation)

        if self.software_versions is not None and not isinstance(self.software_versions, str):
            self.software_versions = str(self.software_versions)

        if self.paired_reads_assembly is not None and not isinstance(self.paired_reads_assembly, str):
            self.paired_reads_assembly = str(self.paired_reads_assembly)

        if self.quality_thresholds is not None and not isinstance(self.quality_thresholds, str):
            self.quality_thresholds = str(self.quality_thresholds)

        if self.primer_match_cutoffs is not None and not isinstance(self.primer_match_cutoffs, str):
            self.primer_match_cutoffs = str(self.primer_match_cutoffs)

        if self.collapsing_method is not None and not isinstance(self.collapsing_method, str):
            self.collapsing_method = str(self.collapsing_method)

        if self.data_processing_protocols is not None and not isinstance(self.data_processing_protocols, str):
            self.data_processing_protocols = str(self.data_processing_protocols)

        if not isinstance(self.data_processing_files, list):
            self.data_processing_files = [self.data_processing_files] if self.data_processing_files is not None else []
        self.data_processing_files = [v if isinstance(v, str) else str(v) for v in self.data_processing_files]

        if self.germline_database is not None and not isinstance(self.germline_database, str):
            self.germline_database = str(self.germline_database)

        if self.germline_set_ref is not None and not isinstance(self.germline_set_ref, str):
            self.germline_set_ref = str(self.germline_set_ref)

        if self.analysis_provenance_id is not None and not isinstance(self.analysis_provenance_id, str):
            self.analysis_provenance_id = str(self.analysis_provenance_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Repertoire(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Repertoire"]
    class_class_curie: ClassVar[str] = "ak_schema:Repertoire"
    class_name: ClassVar[str] = "Repertoire"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Repertoire

    repertoire_id: Optional[str] = None
    repertoire_name: Optional[str] = None
    repertoire_description: Optional[str] = None
    study: Optional[Union[dict, Study]] = None
    subject: Optional[Union[dict, Subject]] = None
    sample: Optional[Union[Union[dict, "SampleProcessing"], List[Union[dict, "SampleProcessing"]]]] = empty_list()
    data_processing: Optional[Union[Union[dict, DataProcessing], List[Union[dict, DataProcessing]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.repertoire_id is not None and not isinstance(self.repertoire_id, str):
            self.repertoire_id = str(self.repertoire_id)

        if self.repertoire_name is not None and not isinstance(self.repertoire_name, str):
            self.repertoire_name = str(self.repertoire_name)

        if self.repertoire_description is not None and not isinstance(self.repertoire_description, str):
            self.repertoire_description = str(self.repertoire_description)

        if self.study is not None and not isinstance(self.study, Study):
            self.study = Study(**as_dict(self.study))

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if not isinstance(self.sample, list):
            self.sample = [self.sample] if self.sample is not None else []
        self.sample = [v if isinstance(v, SampleProcessing) else SampleProcessing(**as_dict(v)) for v in self.sample]

        if not isinstance(self.data_processing, list):
            self.data_processing = [self.data_processing] if self.data_processing is not None else []
        self.data_processing = [v if isinstance(v, DataProcessing) else DataProcessing(**as_dict(v)) for v in self.data_processing]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RepertoireGroup(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["RepertoireGroup"]
    class_class_curie: ClassVar[str] = "ak_schema:RepertoireGroup"
    class_name: ClassVar[str] = "RepertoireGroup"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.RepertoireGroup

    repertoire_group_id: Optional[str] = None
    repertoire_group_name: Optional[str] = None
    repertoire_group_description: Optional[str] = None
    repertoires: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.repertoire_group_id is not None and not isinstance(self.repertoire_group_id, str):
            self.repertoire_group_id = str(self.repertoire_group_id)

        if self.repertoire_group_name is not None and not isinstance(self.repertoire_group_name, str):
            self.repertoire_group_name = str(self.repertoire_group_name)

        if self.repertoire_group_description is not None and not isinstance(self.repertoire_group_description, str):
            self.repertoire_group_description = str(self.repertoire_group_description)

        if not isinstance(self.repertoires, list):
            self.repertoires = [self.repertoires] if self.repertoires is not None else []
        self.repertoires = [v if isinstance(v, str) else str(v) for v in self.repertoires]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Alignment(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Alignment"]
    class_class_curie: ClassVar[str] = "ak_schema:Alignment"
    class_name: ClassVar[str] = "Alignment"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Alignment

    sequence_id: Optional[str] = None
    segment: Optional[str] = None
    rev_comp: Optional[Union[bool, Bool]] = None
    call: Optional[str] = None
    score: Optional[float] = None
    identity: Optional[float] = None
    support: Optional[float] = None
    cigar: Optional[str] = None
    sequence_start: Optional[int] = None
    sequence_end: Optional[int] = None
    germline_start: Optional[int] = None
    germline_end: Optional[int] = None
    rank: Optional[int] = None
    data_processing_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sequence_id is not None and not isinstance(self.sequence_id, str):
            self.sequence_id = str(self.sequence_id)

        if self.segment is not None and not isinstance(self.segment, str):
            self.segment = str(self.segment)

        if self.rev_comp is not None and not isinstance(self.rev_comp, Bool):
            self.rev_comp = Bool(self.rev_comp)

        if self.call is not None and not isinstance(self.call, str):
            self.call = str(self.call)

        if self.score is not None and not isinstance(self.score, float):
            self.score = float(self.score)

        if self.identity is not None and not isinstance(self.identity, float):
            self.identity = float(self.identity)

        if self.support is not None and not isinstance(self.support, float):
            self.support = float(self.support)

        if self.cigar is not None and not isinstance(self.cigar, str):
            self.cigar = str(self.cigar)

        if self.sequence_start is not None and not isinstance(self.sequence_start, int):
            self.sequence_start = int(self.sequence_start)

        if self.sequence_end is not None and not isinstance(self.sequence_end, int):
            self.sequence_end = int(self.sequence_end)

        if self.germline_start is not None and not isinstance(self.germline_start, int):
            self.germline_start = int(self.germline_start)

        if self.germline_end is not None and not isinstance(self.germline_end, int):
            self.germline_end = int(self.germline_end)

        if self.rank is not None and not isinstance(self.rank, int):
            self.rank = int(self.rank)

        if self.data_processing_id is not None and not isinstance(self.data_processing_id, str):
            self.data_processing_id = str(self.data_processing_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rearrangement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Rearrangement"]
    class_class_curie: ClassVar[str] = "ak_schema:Rearrangement"
    class_name: ClassVar[str] = "Rearrangement"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Rearrangement

    sequence_id: Optional[str] = None
    sequence: Optional[str] = None
    quality: Optional[str] = None
    sequence_aa: Optional[str] = None
    rev_comp: Optional[Union[bool, Bool]] = None
    productive: Optional[Union[bool, Bool]] = None
    vj_in_frame: Optional[Union[bool, Bool]] = None
    stop_codon: Optional[Union[bool, Bool]] = None
    complete_vdj: Optional[Union[bool, Bool]] = None
    locus: Optional[Union[str, "Locus"]] = None
    v_call: Optional[str] = None
    d_call: Optional[str] = None
    d2_call: Optional[str] = None
    j_call: Optional[str] = None
    c_call: Optional[str] = None
    sequence_alignment: Optional[str] = None
    quality_alignment: Optional[str] = None
    sequence_alignment_aa: Optional[str] = None
    germline_alignment: Optional[str] = None
    germline_alignment_aa: Optional[str] = None
    junction: Optional[str] = None
    junction_aa: Optional[str] = None
    np1: Optional[str] = None
    np1_aa: Optional[str] = None
    np2: Optional[str] = None
    np2_aa: Optional[str] = None
    np3: Optional[str] = None
    np3_aa: Optional[str] = None
    cdr1: Optional[str] = None
    cdr1_aa: Optional[str] = None
    cdr2: Optional[str] = None
    cdr2_aa: Optional[str] = None
    cdr3: Optional[str] = None
    cdr3_aa: Optional[str] = None
    fwr1: Optional[str] = None
    fwr1_aa: Optional[str] = None
    fwr2: Optional[str] = None
    fwr2_aa: Optional[str] = None
    fwr3: Optional[str] = None
    fwr3_aa: Optional[str] = None
    fwr4: Optional[str] = None
    fwr4_aa: Optional[str] = None
    v_score: Optional[float] = None
    v_identity: Optional[float] = None
    v_support: Optional[float] = None
    v_cigar: Optional[str] = None
    d_score: Optional[float] = None
    d_identity: Optional[float] = None
    d_support: Optional[float] = None
    d_cigar: Optional[str] = None
    d2_score: Optional[float] = None
    d2_identity: Optional[float] = None
    d2_support: Optional[float] = None
    d2_cigar: Optional[str] = None
    j_score: Optional[float] = None
    j_identity: Optional[float] = None
    j_support: Optional[float] = None
    j_cigar: Optional[str] = None
    c_score: Optional[float] = None
    c_identity: Optional[float] = None
    c_support: Optional[float] = None
    c_cigar: Optional[str] = None
    v_sequence_start: Optional[int] = None
    v_sequence_end: Optional[int] = None
    v_germline_start: Optional[int] = None
    v_germline_end: Optional[int] = None
    v_alignment_start: Optional[int] = None
    v_alignment_end: Optional[int] = None
    d_sequence_start: Optional[int] = None
    d_sequence_end: Optional[int] = None
    d_germline_start: Optional[int] = None
    d_germline_end: Optional[int] = None
    d_alignment_start: Optional[int] = None
    d_alignment_end: Optional[int] = None
    d2_sequence_start: Optional[int] = None
    d2_sequence_end: Optional[int] = None
    d2_germline_start: Optional[int] = None
    d2_germline_end: Optional[int] = None
    d2_alignment_start: Optional[int] = None
    d2_alignment_end: Optional[int] = None
    j_sequence_start: Optional[int] = None
    j_sequence_end: Optional[int] = None
    j_germline_start: Optional[int] = None
    j_germline_end: Optional[int] = None
    j_alignment_start: Optional[int] = None
    j_alignment_end: Optional[int] = None
    c_sequence_start: Optional[int] = None
    c_sequence_end: Optional[int] = None
    c_germline_start: Optional[int] = None
    c_germline_end: Optional[int] = None
    c_alignment_start: Optional[int] = None
    c_alignment_end: Optional[int] = None
    cdr1_start: Optional[int] = None
    cdr1_end: Optional[int] = None
    cdr2_start: Optional[int] = None
    cdr2_end: Optional[int] = None
    cdr3_start: Optional[int] = None
    cdr3_end: Optional[int] = None
    fwr1_start: Optional[int] = None
    fwr1_end: Optional[int] = None
    fwr2_start: Optional[int] = None
    fwr2_end: Optional[int] = None
    fwr3_start: Optional[int] = None
    fwr3_end: Optional[int] = None
    fwr4_start: Optional[int] = None
    fwr4_end: Optional[int] = None
    v_sequence_alignment: Optional[str] = None
    v_sequence_alignment_aa: Optional[str] = None
    d_sequence_alignment: Optional[str] = None
    d_sequence_alignment_aa: Optional[str] = None
    d2_sequence_alignment: Optional[str] = None
    d2_sequence_alignment_aa: Optional[str] = None
    j_sequence_alignment: Optional[str] = None
    j_sequence_alignment_aa: Optional[str] = None
    c_sequence_alignment: Optional[str] = None
    c_sequence_alignment_aa: Optional[str] = None
    v_germline_alignment: Optional[str] = None
    v_germline_alignment_aa: Optional[str] = None
    d_germline_alignment: Optional[str] = None
    d_germline_alignment_aa: Optional[str] = None
    d2_germline_alignment: Optional[str] = None
    d2_germline_alignment_aa: Optional[str] = None
    j_germline_alignment: Optional[str] = None
    j_germline_alignment_aa: Optional[str] = None
    c_germline_alignment: Optional[str] = None
    c_germline_alignment_aa: Optional[str] = None
    junction_length: Optional[int] = None
    junction_aa_length: Optional[int] = None
    np1_length: Optional[int] = None
    np2_length: Optional[int] = None
    np3_length: Optional[int] = None
    n1_length: Optional[int] = None
    n2_length: Optional[int] = None
    n3_length: Optional[int] = None
    p3v_length: Optional[int] = None
    p5d_length: Optional[int] = None
    p3d_length: Optional[int] = None
    p5d2_length: Optional[int] = None
    p3d2_length: Optional[int] = None
    p5j_length: Optional[int] = None
    v_frameshift: Optional[Union[bool, Bool]] = None
    j_frameshift: Optional[Union[bool, Bool]] = None
    d_frame: Optional[int] = None
    d2_frame: Optional[int] = None
    consensus_count: Optional[int] = None
    duplicate_count: Optional[int] = None
    umi_count: Optional[int] = None
    cell_id: Optional[str] = None
    clone_id: Optional[str] = None
    repertoire_id: Optional[str] = None
    sample_processing_id: Optional[str] = None
    data_processing_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sequence_id is not None and not isinstance(self.sequence_id, str):
            self.sequence_id = str(self.sequence_id)

        if self.sequence is not None and not isinstance(self.sequence, str):
            self.sequence = str(self.sequence)

        if self.quality is not None and not isinstance(self.quality, str):
            self.quality = str(self.quality)

        if self.sequence_aa is not None and not isinstance(self.sequence_aa, str):
            self.sequence_aa = str(self.sequence_aa)

        if self.rev_comp is not None and not isinstance(self.rev_comp, Bool):
            self.rev_comp = Bool(self.rev_comp)

        if self.productive is not None and not isinstance(self.productive, Bool):
            self.productive = Bool(self.productive)

        if self.vj_in_frame is not None and not isinstance(self.vj_in_frame, Bool):
            self.vj_in_frame = Bool(self.vj_in_frame)

        if self.stop_codon is not None and not isinstance(self.stop_codon, Bool):
            self.stop_codon = Bool(self.stop_codon)

        if self.complete_vdj is not None and not isinstance(self.complete_vdj, Bool):
            self.complete_vdj = Bool(self.complete_vdj)

        if self.locus is not None and not isinstance(self.locus, Locus):
            self.locus = Locus(self.locus)

        if self.v_call is not None and not isinstance(self.v_call, str):
            self.v_call = str(self.v_call)

        if self.d_call is not None and not isinstance(self.d_call, str):
            self.d_call = str(self.d_call)

        if self.d2_call is not None and not isinstance(self.d2_call, str):
            self.d2_call = str(self.d2_call)

        if self.j_call is not None and not isinstance(self.j_call, str):
            self.j_call = str(self.j_call)

        if self.c_call is not None and not isinstance(self.c_call, str):
            self.c_call = str(self.c_call)

        if self.sequence_alignment is not None and not isinstance(self.sequence_alignment, str):
            self.sequence_alignment = str(self.sequence_alignment)

        if self.quality_alignment is not None and not isinstance(self.quality_alignment, str):
            self.quality_alignment = str(self.quality_alignment)

        if self.sequence_alignment_aa is not None and not isinstance(self.sequence_alignment_aa, str):
            self.sequence_alignment_aa = str(self.sequence_alignment_aa)

        if self.germline_alignment is not None and not isinstance(self.germline_alignment, str):
            self.germline_alignment = str(self.germline_alignment)

        if self.germline_alignment_aa is not None and not isinstance(self.germline_alignment_aa, str):
            self.germline_alignment_aa = str(self.germline_alignment_aa)

        if self.junction is not None and not isinstance(self.junction, str):
            self.junction = str(self.junction)

        if self.junction_aa is not None and not isinstance(self.junction_aa, str):
            self.junction_aa = str(self.junction_aa)

        if self.np1 is not None and not isinstance(self.np1, str):
            self.np1 = str(self.np1)

        if self.np1_aa is not None and not isinstance(self.np1_aa, str):
            self.np1_aa = str(self.np1_aa)

        if self.np2 is not None and not isinstance(self.np2, str):
            self.np2 = str(self.np2)

        if self.np2_aa is not None and not isinstance(self.np2_aa, str):
            self.np2_aa = str(self.np2_aa)

        if self.np3 is not None and not isinstance(self.np3, str):
            self.np3 = str(self.np3)

        if self.np3_aa is not None and not isinstance(self.np3_aa, str):
            self.np3_aa = str(self.np3_aa)

        if self.cdr1 is not None and not isinstance(self.cdr1, str):
            self.cdr1 = str(self.cdr1)

        if self.cdr1_aa is not None and not isinstance(self.cdr1_aa, str):
            self.cdr1_aa = str(self.cdr1_aa)

        if self.cdr2 is not None and not isinstance(self.cdr2, str):
            self.cdr2 = str(self.cdr2)

        if self.cdr2_aa is not None and not isinstance(self.cdr2_aa, str):
            self.cdr2_aa = str(self.cdr2_aa)

        if self.cdr3 is not None and not isinstance(self.cdr3, str):
            self.cdr3 = str(self.cdr3)

        if self.cdr3_aa is not None and not isinstance(self.cdr3_aa, str):
            self.cdr3_aa = str(self.cdr3_aa)

        if self.fwr1 is not None and not isinstance(self.fwr1, str):
            self.fwr1 = str(self.fwr1)

        if self.fwr1_aa is not None and not isinstance(self.fwr1_aa, str):
            self.fwr1_aa = str(self.fwr1_aa)

        if self.fwr2 is not None and not isinstance(self.fwr2, str):
            self.fwr2 = str(self.fwr2)

        if self.fwr2_aa is not None and not isinstance(self.fwr2_aa, str):
            self.fwr2_aa = str(self.fwr2_aa)

        if self.fwr3 is not None and not isinstance(self.fwr3, str):
            self.fwr3 = str(self.fwr3)

        if self.fwr3_aa is not None and not isinstance(self.fwr3_aa, str):
            self.fwr3_aa = str(self.fwr3_aa)

        if self.fwr4 is not None and not isinstance(self.fwr4, str):
            self.fwr4 = str(self.fwr4)

        if self.fwr4_aa is not None and not isinstance(self.fwr4_aa, str):
            self.fwr4_aa = str(self.fwr4_aa)

        if self.v_score is not None and not isinstance(self.v_score, float):
            self.v_score = float(self.v_score)

        if self.v_identity is not None and not isinstance(self.v_identity, float):
            self.v_identity = float(self.v_identity)

        if self.v_support is not None and not isinstance(self.v_support, float):
            self.v_support = float(self.v_support)

        if self.v_cigar is not None and not isinstance(self.v_cigar, str):
            self.v_cigar = str(self.v_cigar)

        if self.d_score is not None and not isinstance(self.d_score, float):
            self.d_score = float(self.d_score)

        if self.d_identity is not None and not isinstance(self.d_identity, float):
            self.d_identity = float(self.d_identity)

        if self.d_support is not None and not isinstance(self.d_support, float):
            self.d_support = float(self.d_support)

        if self.d_cigar is not None and not isinstance(self.d_cigar, str):
            self.d_cigar = str(self.d_cigar)

        if self.d2_score is not None and not isinstance(self.d2_score, float):
            self.d2_score = float(self.d2_score)

        if self.d2_identity is not None and not isinstance(self.d2_identity, float):
            self.d2_identity = float(self.d2_identity)

        if self.d2_support is not None and not isinstance(self.d2_support, float):
            self.d2_support = float(self.d2_support)

        if self.d2_cigar is not None and not isinstance(self.d2_cigar, str):
            self.d2_cigar = str(self.d2_cigar)

        if self.j_score is not None and not isinstance(self.j_score, float):
            self.j_score = float(self.j_score)

        if self.j_identity is not None and not isinstance(self.j_identity, float):
            self.j_identity = float(self.j_identity)

        if self.j_support is not None and not isinstance(self.j_support, float):
            self.j_support = float(self.j_support)

        if self.j_cigar is not None and not isinstance(self.j_cigar, str):
            self.j_cigar = str(self.j_cigar)

        if self.c_score is not None and not isinstance(self.c_score, float):
            self.c_score = float(self.c_score)

        if self.c_identity is not None and not isinstance(self.c_identity, float):
            self.c_identity = float(self.c_identity)

        if self.c_support is not None and not isinstance(self.c_support, float):
            self.c_support = float(self.c_support)

        if self.c_cigar is not None and not isinstance(self.c_cigar, str):
            self.c_cigar = str(self.c_cigar)

        if self.v_sequence_start is not None and not isinstance(self.v_sequence_start, int):
            self.v_sequence_start = int(self.v_sequence_start)

        if self.v_sequence_end is not None and not isinstance(self.v_sequence_end, int):
            self.v_sequence_end = int(self.v_sequence_end)

        if self.v_germline_start is not None and not isinstance(self.v_germline_start, int):
            self.v_germline_start = int(self.v_germline_start)

        if self.v_germline_end is not None and not isinstance(self.v_germline_end, int):
            self.v_germline_end = int(self.v_germline_end)

        if self.v_alignment_start is not None and not isinstance(self.v_alignment_start, int):
            self.v_alignment_start = int(self.v_alignment_start)

        if self.v_alignment_end is not None and not isinstance(self.v_alignment_end, int):
            self.v_alignment_end = int(self.v_alignment_end)

        if self.d_sequence_start is not None and not isinstance(self.d_sequence_start, int):
            self.d_sequence_start = int(self.d_sequence_start)

        if self.d_sequence_end is not None and not isinstance(self.d_sequence_end, int):
            self.d_sequence_end = int(self.d_sequence_end)

        if self.d_germline_start is not None and not isinstance(self.d_germline_start, int):
            self.d_germline_start = int(self.d_germline_start)

        if self.d_germline_end is not None and not isinstance(self.d_germline_end, int):
            self.d_germline_end = int(self.d_germline_end)

        if self.d_alignment_start is not None and not isinstance(self.d_alignment_start, int):
            self.d_alignment_start = int(self.d_alignment_start)

        if self.d_alignment_end is not None and not isinstance(self.d_alignment_end, int):
            self.d_alignment_end = int(self.d_alignment_end)

        if self.d2_sequence_start is not None and not isinstance(self.d2_sequence_start, int):
            self.d2_sequence_start = int(self.d2_sequence_start)

        if self.d2_sequence_end is not None and not isinstance(self.d2_sequence_end, int):
            self.d2_sequence_end = int(self.d2_sequence_end)

        if self.d2_germline_start is not None and not isinstance(self.d2_germline_start, int):
            self.d2_germline_start = int(self.d2_germline_start)

        if self.d2_germline_end is not None and not isinstance(self.d2_germline_end, int):
            self.d2_germline_end = int(self.d2_germline_end)

        if self.d2_alignment_start is not None and not isinstance(self.d2_alignment_start, int):
            self.d2_alignment_start = int(self.d2_alignment_start)

        if self.d2_alignment_end is not None and not isinstance(self.d2_alignment_end, int):
            self.d2_alignment_end = int(self.d2_alignment_end)

        if self.j_sequence_start is not None and not isinstance(self.j_sequence_start, int):
            self.j_sequence_start = int(self.j_sequence_start)

        if self.j_sequence_end is not None and not isinstance(self.j_sequence_end, int):
            self.j_sequence_end = int(self.j_sequence_end)

        if self.j_germline_start is not None and not isinstance(self.j_germline_start, int):
            self.j_germline_start = int(self.j_germline_start)

        if self.j_germline_end is not None and not isinstance(self.j_germline_end, int):
            self.j_germline_end = int(self.j_germline_end)

        if self.j_alignment_start is not None and not isinstance(self.j_alignment_start, int):
            self.j_alignment_start = int(self.j_alignment_start)

        if self.j_alignment_end is not None and not isinstance(self.j_alignment_end, int):
            self.j_alignment_end = int(self.j_alignment_end)

        if self.c_sequence_start is not None and not isinstance(self.c_sequence_start, int):
            self.c_sequence_start = int(self.c_sequence_start)

        if self.c_sequence_end is not None and not isinstance(self.c_sequence_end, int):
            self.c_sequence_end = int(self.c_sequence_end)

        if self.c_germline_start is not None and not isinstance(self.c_germline_start, int):
            self.c_germline_start = int(self.c_germline_start)

        if self.c_germline_end is not None and not isinstance(self.c_germline_end, int):
            self.c_germline_end = int(self.c_germline_end)

        if self.c_alignment_start is not None and not isinstance(self.c_alignment_start, int):
            self.c_alignment_start = int(self.c_alignment_start)

        if self.c_alignment_end is not None and not isinstance(self.c_alignment_end, int):
            self.c_alignment_end = int(self.c_alignment_end)

        if self.cdr1_start is not None and not isinstance(self.cdr1_start, int):
            self.cdr1_start = int(self.cdr1_start)

        if self.cdr1_end is not None and not isinstance(self.cdr1_end, int):
            self.cdr1_end = int(self.cdr1_end)

        if self.cdr2_start is not None and not isinstance(self.cdr2_start, int):
            self.cdr2_start = int(self.cdr2_start)

        if self.cdr2_end is not None and not isinstance(self.cdr2_end, int):
            self.cdr2_end = int(self.cdr2_end)

        if self.cdr3_start is not None and not isinstance(self.cdr3_start, int):
            self.cdr3_start = int(self.cdr3_start)

        if self.cdr3_end is not None and not isinstance(self.cdr3_end, int):
            self.cdr3_end = int(self.cdr3_end)

        if self.fwr1_start is not None and not isinstance(self.fwr1_start, int):
            self.fwr1_start = int(self.fwr1_start)

        if self.fwr1_end is not None and not isinstance(self.fwr1_end, int):
            self.fwr1_end = int(self.fwr1_end)

        if self.fwr2_start is not None and not isinstance(self.fwr2_start, int):
            self.fwr2_start = int(self.fwr2_start)

        if self.fwr2_end is not None and not isinstance(self.fwr2_end, int):
            self.fwr2_end = int(self.fwr2_end)

        if self.fwr3_start is not None and not isinstance(self.fwr3_start, int):
            self.fwr3_start = int(self.fwr3_start)

        if self.fwr3_end is not None and not isinstance(self.fwr3_end, int):
            self.fwr3_end = int(self.fwr3_end)

        if self.fwr4_start is not None and not isinstance(self.fwr4_start, int):
            self.fwr4_start = int(self.fwr4_start)

        if self.fwr4_end is not None and not isinstance(self.fwr4_end, int):
            self.fwr4_end = int(self.fwr4_end)

        if self.v_sequence_alignment is not None and not isinstance(self.v_sequence_alignment, str):
            self.v_sequence_alignment = str(self.v_sequence_alignment)

        if self.v_sequence_alignment_aa is not None and not isinstance(self.v_sequence_alignment_aa, str):
            self.v_sequence_alignment_aa = str(self.v_sequence_alignment_aa)

        if self.d_sequence_alignment is not None and not isinstance(self.d_sequence_alignment, str):
            self.d_sequence_alignment = str(self.d_sequence_alignment)

        if self.d_sequence_alignment_aa is not None and not isinstance(self.d_sequence_alignment_aa, str):
            self.d_sequence_alignment_aa = str(self.d_sequence_alignment_aa)

        if self.d2_sequence_alignment is not None and not isinstance(self.d2_sequence_alignment, str):
            self.d2_sequence_alignment = str(self.d2_sequence_alignment)

        if self.d2_sequence_alignment_aa is not None and not isinstance(self.d2_sequence_alignment_aa, str):
            self.d2_sequence_alignment_aa = str(self.d2_sequence_alignment_aa)

        if self.j_sequence_alignment is not None and not isinstance(self.j_sequence_alignment, str):
            self.j_sequence_alignment = str(self.j_sequence_alignment)

        if self.j_sequence_alignment_aa is not None and not isinstance(self.j_sequence_alignment_aa, str):
            self.j_sequence_alignment_aa = str(self.j_sequence_alignment_aa)

        if self.c_sequence_alignment is not None and not isinstance(self.c_sequence_alignment, str):
            self.c_sequence_alignment = str(self.c_sequence_alignment)

        if self.c_sequence_alignment_aa is not None and not isinstance(self.c_sequence_alignment_aa, str):
            self.c_sequence_alignment_aa = str(self.c_sequence_alignment_aa)

        if self.v_germline_alignment is not None and not isinstance(self.v_germline_alignment, str):
            self.v_germline_alignment = str(self.v_germline_alignment)

        if self.v_germline_alignment_aa is not None and not isinstance(self.v_germline_alignment_aa, str):
            self.v_germline_alignment_aa = str(self.v_germline_alignment_aa)

        if self.d_germline_alignment is not None and not isinstance(self.d_germline_alignment, str):
            self.d_germline_alignment = str(self.d_germline_alignment)

        if self.d_germline_alignment_aa is not None and not isinstance(self.d_germline_alignment_aa, str):
            self.d_germline_alignment_aa = str(self.d_germline_alignment_aa)

        if self.d2_germline_alignment is not None and not isinstance(self.d2_germline_alignment, str):
            self.d2_germline_alignment = str(self.d2_germline_alignment)

        if self.d2_germline_alignment_aa is not None and not isinstance(self.d2_germline_alignment_aa, str):
            self.d2_germline_alignment_aa = str(self.d2_germline_alignment_aa)

        if self.j_germline_alignment is not None and not isinstance(self.j_germline_alignment, str):
            self.j_germline_alignment = str(self.j_germline_alignment)

        if self.j_germline_alignment_aa is not None and not isinstance(self.j_germline_alignment_aa, str):
            self.j_germline_alignment_aa = str(self.j_germline_alignment_aa)

        if self.c_germline_alignment is not None and not isinstance(self.c_germline_alignment, str):
            self.c_germline_alignment = str(self.c_germline_alignment)

        if self.c_germline_alignment_aa is not None and not isinstance(self.c_germline_alignment_aa, str):
            self.c_germline_alignment_aa = str(self.c_germline_alignment_aa)

        if self.junction_length is not None and not isinstance(self.junction_length, int):
            self.junction_length = int(self.junction_length)

        if self.junction_aa_length is not None and not isinstance(self.junction_aa_length, int):
            self.junction_aa_length = int(self.junction_aa_length)

        if self.np1_length is not None and not isinstance(self.np1_length, int):
            self.np1_length = int(self.np1_length)

        if self.np2_length is not None and not isinstance(self.np2_length, int):
            self.np2_length = int(self.np2_length)

        if self.np3_length is not None and not isinstance(self.np3_length, int):
            self.np3_length = int(self.np3_length)

        if self.n1_length is not None and not isinstance(self.n1_length, int):
            self.n1_length = int(self.n1_length)

        if self.n2_length is not None and not isinstance(self.n2_length, int):
            self.n2_length = int(self.n2_length)

        if self.n3_length is not None and not isinstance(self.n3_length, int):
            self.n3_length = int(self.n3_length)

        if self.p3v_length is not None and not isinstance(self.p3v_length, int):
            self.p3v_length = int(self.p3v_length)

        if self.p5d_length is not None and not isinstance(self.p5d_length, int):
            self.p5d_length = int(self.p5d_length)

        if self.p3d_length is not None and not isinstance(self.p3d_length, int):
            self.p3d_length = int(self.p3d_length)

        if self.p5d2_length is not None and not isinstance(self.p5d2_length, int):
            self.p5d2_length = int(self.p5d2_length)

        if self.p3d2_length is not None and not isinstance(self.p3d2_length, int):
            self.p3d2_length = int(self.p3d2_length)

        if self.p5j_length is not None and not isinstance(self.p5j_length, int):
            self.p5j_length = int(self.p5j_length)

        if self.v_frameshift is not None and not isinstance(self.v_frameshift, Bool):
            self.v_frameshift = Bool(self.v_frameshift)

        if self.j_frameshift is not None and not isinstance(self.j_frameshift, Bool):
            self.j_frameshift = Bool(self.j_frameshift)

        if self.d_frame is not None and not isinstance(self.d_frame, int):
            self.d_frame = int(self.d_frame)

        if self.d2_frame is not None and not isinstance(self.d2_frame, int):
            self.d2_frame = int(self.d2_frame)

        if self.consensus_count is not None and not isinstance(self.consensus_count, int):
            self.consensus_count = int(self.consensus_count)

        if self.duplicate_count is not None and not isinstance(self.duplicate_count, int):
            self.duplicate_count = int(self.duplicate_count)

        if self.umi_count is not None and not isinstance(self.umi_count, int):
            self.umi_count = int(self.umi_count)

        if self.cell_id is not None and not isinstance(self.cell_id, str):
            self.cell_id = str(self.cell_id)

        if self.clone_id is not None and not isinstance(self.clone_id, str):
            self.clone_id = str(self.clone_id)

        if self.repertoire_id is not None and not isinstance(self.repertoire_id, str):
            self.repertoire_id = str(self.repertoire_id)

        if self.sample_processing_id is not None and not isinstance(self.sample_processing_id, str):
            self.sample_processing_id = str(self.sample_processing_id)

        if self.data_processing_id is not None and not isinstance(self.data_processing_id, str):
            self.data_processing_id = str(self.data_processing_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Clone(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Clone"]
    class_class_curie: ClassVar[str] = "ak_schema:Clone"
    class_name: ClassVar[str] = "Clone"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Clone

    clone_id: Optional[str] = None
    repertoire_id: Optional[str] = None
    data_processing_id: Optional[str] = None
    sequences: Optional[Union[str, List[str]]] = empty_list()
    v_call: Optional[str] = None
    d_call: Optional[str] = None
    j_call: Optional[str] = None
    junction: Optional[str] = None
    junction_aa: Optional[str] = None
    junction_length: Optional[int] = None
    junction_aa_length: Optional[int] = None
    germline_alignment: Optional[str] = None
    germline_alignment_aa: Optional[str] = None
    v_alignment_start: Optional[int] = None
    v_alignment_end: Optional[int] = None
    d_alignment_start: Optional[int] = None
    d_alignment_end: Optional[int] = None
    j_alignment_start: Optional[int] = None
    j_alignment_end: Optional[int] = None
    junction_start: Optional[int] = None
    junction_end: Optional[int] = None
    umi_count: Optional[int] = None
    clone_count: Optional[int] = None
    seed_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.clone_id is not None and not isinstance(self.clone_id, str):
            self.clone_id = str(self.clone_id)

        if self.repertoire_id is not None and not isinstance(self.repertoire_id, str):
            self.repertoire_id = str(self.repertoire_id)

        if self.data_processing_id is not None and not isinstance(self.data_processing_id, str):
            self.data_processing_id = str(self.data_processing_id)

        if not isinstance(self.sequences, list):
            self.sequences = [self.sequences] if self.sequences is not None else []
        self.sequences = [v if isinstance(v, str) else str(v) for v in self.sequences]

        if self.v_call is not None and not isinstance(self.v_call, str):
            self.v_call = str(self.v_call)

        if self.d_call is not None and not isinstance(self.d_call, str):
            self.d_call = str(self.d_call)

        if self.j_call is not None and not isinstance(self.j_call, str):
            self.j_call = str(self.j_call)

        if self.junction is not None and not isinstance(self.junction, str):
            self.junction = str(self.junction)

        if self.junction_aa is not None and not isinstance(self.junction_aa, str):
            self.junction_aa = str(self.junction_aa)

        if self.junction_length is not None and not isinstance(self.junction_length, int):
            self.junction_length = int(self.junction_length)

        if self.junction_aa_length is not None and not isinstance(self.junction_aa_length, int):
            self.junction_aa_length = int(self.junction_aa_length)

        if self.germline_alignment is not None and not isinstance(self.germline_alignment, str):
            self.germline_alignment = str(self.germline_alignment)

        if self.germline_alignment_aa is not None and not isinstance(self.germline_alignment_aa, str):
            self.germline_alignment_aa = str(self.germline_alignment_aa)

        if self.v_alignment_start is not None and not isinstance(self.v_alignment_start, int):
            self.v_alignment_start = int(self.v_alignment_start)

        if self.v_alignment_end is not None and not isinstance(self.v_alignment_end, int):
            self.v_alignment_end = int(self.v_alignment_end)

        if self.d_alignment_start is not None and not isinstance(self.d_alignment_start, int):
            self.d_alignment_start = int(self.d_alignment_start)

        if self.d_alignment_end is not None and not isinstance(self.d_alignment_end, int):
            self.d_alignment_end = int(self.d_alignment_end)

        if self.j_alignment_start is not None and not isinstance(self.j_alignment_start, int):
            self.j_alignment_start = int(self.j_alignment_start)

        if self.j_alignment_end is not None and not isinstance(self.j_alignment_end, int):
            self.j_alignment_end = int(self.j_alignment_end)

        if self.junction_start is not None and not isinstance(self.junction_start, int):
            self.junction_start = int(self.junction_start)

        if self.junction_end is not None and not isinstance(self.junction_end, int):
            self.junction_end = int(self.junction_end)

        if self.umi_count is not None and not isinstance(self.umi_count, int):
            self.umi_count = int(self.umi_count)

        if self.clone_count is not None and not isinstance(self.clone_count, int):
            self.clone_count = int(self.clone_count)

        if self.seed_id is not None and not isinstance(self.seed_id, str):
            self.seed_id = str(self.seed_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tree(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Tree"]
    class_class_curie: ClassVar[str] = "ak_schema:Tree"
    class_name: ClassVar[str] = "Tree"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Tree

    tree_id: Optional[str] = None
    clone_id: Optional[str] = None
    newick: Optional[str] = None
    nodes: Optional[Union[Union[dict, "Node"], List[Union[dict, "Node"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.tree_id is not None and not isinstance(self.tree_id, str):
            self.tree_id = str(self.tree_id)

        if self.clone_id is not None and not isinstance(self.clone_id, str):
            self.clone_id = str(self.clone_id)

        if self.newick is not None and not isinstance(self.newick, str):
            self.newick = str(self.newick)

        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes] if self.nodes is not None else []
        self.nodes = [v if isinstance(v, Node) else Node(**as_dict(v)) for v in self.nodes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Node(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Node"]
    class_class_curie: ClassVar[str] = "ak_schema:Node"
    class_name: ClassVar[str] = "Node"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Node

    sequence_id: Optional[str] = None
    sequence_alignment: Optional[str] = None
    junction: Optional[str] = None
    junction_aa: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sequence_id is not None and not isinstance(self.sequence_id, str):
            self.sequence_id = str(self.sequence_id)

        if self.sequence_alignment is not None and not isinstance(self.sequence_alignment, str):
            self.sequence_alignment = str(self.sequence_alignment)

        if self.junction is not None and not isinstance(self.junction, str):
            self.junction = str(self.junction)

        if self.junction_aa is not None and not isinstance(self.junction_aa, str):
            self.junction_aa = str(self.junction_aa)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["CellExpression"]
    class_class_curie: ClassVar[str] = "ak_schema:CellExpression"
    class_name: ClassVar[str] = "CellExpression"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.CellExpression

    expression_id: Optional[str] = None
    cell_id: Optional[str] = None
    repertoire_id: Optional[str] = None
    data_processing_id: Optional[str] = None
    property_type: Optional[str] = None
    property: Optional[Union[str, "Property"]] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.expression_id is not None and not isinstance(self.expression_id, str):
            self.expression_id = str(self.expression_id)

        if self.cell_id is not None and not isinstance(self.cell_id, str):
            self.cell_id = str(self.cell_id)

        if self.repertoire_id is not None and not isinstance(self.repertoire_id, str):
            self.repertoire_id = str(self.repertoire_id)

        if self.data_processing_id is not None and not isinstance(self.data_processing_id, str):
            self.data_processing_id = str(self.data_processing_id)

        if self.property_type is not None and not isinstance(self.property_type, str):
            self.property_type = str(self.property_type)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Receptor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Receptor"]
    class_class_curie: ClassVar[str] = "ak_schema:Receptor"
    class_name: ClassVar[str] = "Receptor"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Receptor

    receptor_id: Optional[str] = None
    receptor_hash: Optional[str] = None
    receptor_type: Optional[Union[str, "ReceptorType"]] = None
    receptor_variable_domain_1_aa: Optional[str] = None
    receptor_variable_domain_1_locus: Optional[Union[str, "ReceptorVariableDomain1Locus"]] = None
    receptor_variable_domain_2_aa: Optional[str] = None
    receptor_variable_domain_2_locus: Optional[Union[str, "ReceptorVariableDomain2Locus"]] = None
    receptor_ref: Optional[Union[str, List[str]]] = empty_list()
    reactivity_measurements: Optional[Union[Union[dict, "ReceptorReactivity"], List[Union[dict, "ReceptorReactivity"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.receptor_id is not None and not isinstance(self.receptor_id, str):
            self.receptor_id = str(self.receptor_id)

        if self.receptor_hash is not None and not isinstance(self.receptor_hash, str):
            self.receptor_hash = str(self.receptor_hash)

        if self.receptor_type is not None and not isinstance(self.receptor_type, ReceptorType):
            self.receptor_type = ReceptorType(self.receptor_type)

        if self.receptor_variable_domain_1_aa is not None and not isinstance(self.receptor_variable_domain_1_aa, str):
            self.receptor_variable_domain_1_aa = str(self.receptor_variable_domain_1_aa)

        if self.receptor_variable_domain_1_locus is not None and not isinstance(self.receptor_variable_domain_1_locus, ReceptorVariableDomain1Locus):
            self.receptor_variable_domain_1_locus = ReceptorVariableDomain1Locus(self.receptor_variable_domain_1_locus)

        if self.receptor_variable_domain_2_aa is not None and not isinstance(self.receptor_variable_domain_2_aa, str):
            self.receptor_variable_domain_2_aa = str(self.receptor_variable_domain_2_aa)

        if self.receptor_variable_domain_2_locus is not None and not isinstance(self.receptor_variable_domain_2_locus, ReceptorVariableDomain2Locus):
            self.receptor_variable_domain_2_locus = ReceptorVariableDomain2Locus(self.receptor_variable_domain_2_locus)

        if not isinstance(self.receptor_ref, list):
            self.receptor_ref = [self.receptor_ref] if self.receptor_ref is not None else []
        self.receptor_ref = [v if isinstance(v, str) else str(v) for v in self.receptor_ref]

        if not isinstance(self.reactivity_measurements, list):
            self.reactivity_measurements = [self.reactivity_measurements] if self.reactivity_measurements is not None else []
        self.reactivity_measurements = [v if isinstance(v, ReceptorReactivity) else ReceptorReactivity(**as_dict(v)) for v in self.reactivity_measurements]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReceptorReactivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["ReceptorReactivity"]
    class_class_curie: ClassVar[str] = "ak_schema:ReceptorReactivity"
    class_name: ClassVar[str] = "ReceptorReactivity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.ReceptorReactivity

    ligand_type: Optional[Union[str, "LigandType"]] = None
    antigen_type: Optional[Union[str, "AntigenType"]] = None
    antigen: Optional[Union[str, "Antigen"]] = None
    antigen_source_species: Optional[Union[str, "AntigenSourceSpecies"]] = None
    peptide_start: Optional[int] = None
    peptide_end: Optional[int] = None
    mhc_class: Optional[Union[str, "MhcClass"]] = None
    mhc_gene_1: Optional[Union[str, "MhcGene1"]] = None
    mhc_allele_1: Optional[str] = None
    mhc_gene_2: Optional[Union[str, "MhcGene2"]] = None
    mhc_allele_2: Optional[str] = None
    reactivity_method: Optional[Union[str, "ReactivityMethod"]] = None
    reactivity_readout: Optional[Union[str, "ReactivityReadout"]] = None
    reactivity_value: Optional[float] = None
    reactivity_unit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ligand_type is not None and not isinstance(self.ligand_type, LigandType):
            self.ligand_type = LigandType(self.ligand_type)

        if self.antigen_type is not None and not isinstance(self.antigen_type, AntigenType):
            self.antigen_type = AntigenType(self.antigen_type)

        if self.peptide_start is not None and not isinstance(self.peptide_start, int):
            self.peptide_start = int(self.peptide_start)

        if self.peptide_end is not None and not isinstance(self.peptide_end, int):
            self.peptide_end = int(self.peptide_end)

        if self.mhc_class is not None and not isinstance(self.mhc_class, MhcClass):
            self.mhc_class = MhcClass(self.mhc_class)

        if self.mhc_allele_1 is not None and not isinstance(self.mhc_allele_1, str):
            self.mhc_allele_1 = str(self.mhc_allele_1)

        if self.mhc_allele_2 is not None and not isinstance(self.mhc_allele_2, str):
            self.mhc_allele_2 = str(self.mhc_allele_2)

        if self.reactivity_method is not None and not isinstance(self.reactivity_method, ReactivityMethod):
            self.reactivity_method = ReactivityMethod(self.reactivity_method)

        if self.reactivity_readout is not None and not isinstance(self.reactivity_readout, ReactivityReadout):
            self.reactivity_readout = ReactivityReadout(self.reactivity_readout)

        if self.reactivity_value is not None and not isinstance(self.reactivity_value, float):
            self.reactivity_value = float(self.reactivity_value)

        if self.reactivity_unit is not None and not isinstance(self.reactivity_unit, str):
            self.reactivity_unit = str(self.reactivity_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SampleProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["SampleProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:SampleProcessing"
    class_name: ClassVar[str] = "SampleProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.SampleProcessing

    sample_processing_id: Optional[str] = None
    sample_id: Optional[str] = None
    sample_type: Optional[str] = None
    tissue: Optional[Union[str, "Tissue"]] = None
    anatomic_site: Optional[str] = None
    disease_state_sample: Optional[str] = None
    collection_time_point_relative: Optional[float] = None
    collection_time_point_relative_unit: Optional[Union[str, "CollectionTimePointRelativeUnit"]] = None
    collection_time_point_reference: Optional[str] = None
    biomaterial_provider: Optional[str] = None
    tissue_processing: Optional[str] = None
    cell_subset: Optional[Union[str, "CellSubset"]] = None
    cell_phenotype: Optional[str] = None
    cell_species: Optional[Union[str, "CellSpecies"]] = None
    single_cell: Optional[Union[bool, Bool]] = None
    cell_number: Optional[int] = None
    cells_per_reaction: Optional[int] = None
    cell_storage: Optional[Union[bool, Bool]] = None
    cell_quality: Optional[str] = None
    cell_isolation: Optional[str] = None
    cell_processing_protocol: Optional[str] = None
    template_class: Optional[Union[str, "TemplateClass"]] = None
    template_quality: Optional[str] = None
    template_amount: Optional[float] = None
    template_amount_unit: Optional[Union[str, "TemplateAmountUnit"]] = None
    library_generation_method: Optional[Union[str, "LibraryGenerationMethod"]] = None
    library_generation_protocol: Optional[str] = None
    library_generation_kit_version: Optional[str] = None
    pcr_target: Optional[Union[Union[dict, PCRTarget], List[Union[dict, PCRTarget]]]] = empty_list()
    complete_sequences: Optional[Union[str, "CompleteSequences"]] = None
    physical_linkage: Optional[Union[str, "PhysicalLinkage"]] = None
    sequencing_run_id: Optional[str] = None
    total_reads_passing_qc_filter: Optional[int] = None
    sequencing_platform: Optional[str] = None
    sequencing_facility: Optional[str] = None
    sequencing_run_date: Optional[Union[str, XSDDateTime]] = None
    sequencing_kit: Optional[str] = None
    sequencing_files: Optional[Union[dict, SequencingData]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sample_processing_id is not None and not isinstance(self.sample_processing_id, str):
            self.sample_processing_id = str(self.sample_processing_id)

        if self.sample_id is not None and not isinstance(self.sample_id, str):
            self.sample_id = str(self.sample_id)

        if self.sample_type is not None and not isinstance(self.sample_type, str):
            self.sample_type = str(self.sample_type)

        if self.anatomic_site is not None and not isinstance(self.anatomic_site, str):
            self.anatomic_site = str(self.anatomic_site)

        if self.disease_state_sample is not None and not isinstance(self.disease_state_sample, str):
            self.disease_state_sample = str(self.disease_state_sample)

        if self.collection_time_point_relative is not None and not isinstance(self.collection_time_point_relative, float):
            self.collection_time_point_relative = float(self.collection_time_point_relative)

        if self.collection_time_point_reference is not None and not isinstance(self.collection_time_point_reference, str):
            self.collection_time_point_reference = str(self.collection_time_point_reference)

        if self.biomaterial_provider is not None and not isinstance(self.biomaterial_provider, str):
            self.biomaterial_provider = str(self.biomaterial_provider)

        if self.tissue_processing is not None and not isinstance(self.tissue_processing, str):
            self.tissue_processing = str(self.tissue_processing)

        if self.cell_phenotype is not None and not isinstance(self.cell_phenotype, str):
            self.cell_phenotype = str(self.cell_phenotype)

        if self.single_cell is not None and not isinstance(self.single_cell, Bool):
            self.single_cell = Bool(self.single_cell)

        if self.cell_number is not None and not isinstance(self.cell_number, int):
            self.cell_number = int(self.cell_number)

        if self.cells_per_reaction is not None and not isinstance(self.cells_per_reaction, int):
            self.cells_per_reaction = int(self.cells_per_reaction)

        if self.cell_storage is not None and not isinstance(self.cell_storage, Bool):
            self.cell_storage = Bool(self.cell_storage)

        if self.cell_quality is not None and not isinstance(self.cell_quality, str):
            self.cell_quality = str(self.cell_quality)

        if self.cell_isolation is not None and not isinstance(self.cell_isolation, str):
            self.cell_isolation = str(self.cell_isolation)

        if self.cell_processing_protocol is not None and not isinstance(self.cell_processing_protocol, str):
            self.cell_processing_protocol = str(self.cell_processing_protocol)

        if self.template_class is not None and not isinstance(self.template_class, TemplateClass):
            self.template_class = TemplateClass(self.template_class)

        if self.template_quality is not None and not isinstance(self.template_quality, str):
            self.template_quality = str(self.template_quality)

        if self.template_amount is not None and not isinstance(self.template_amount, float):
            self.template_amount = float(self.template_amount)

        if self.library_generation_method is not None and not isinstance(self.library_generation_method, LibraryGenerationMethod):
            self.library_generation_method = LibraryGenerationMethod(self.library_generation_method)

        if self.library_generation_protocol is not None and not isinstance(self.library_generation_protocol, str):
            self.library_generation_protocol = str(self.library_generation_protocol)

        if self.library_generation_kit_version is not None and not isinstance(self.library_generation_kit_version, str):
            self.library_generation_kit_version = str(self.library_generation_kit_version)

        if not isinstance(self.pcr_target, list):
            self.pcr_target = [self.pcr_target] if self.pcr_target is not None else []
        self.pcr_target = [v if isinstance(v, PCRTarget) else PCRTarget(**as_dict(v)) for v in self.pcr_target]

        if self.complete_sequences is not None and not isinstance(self.complete_sequences, CompleteSequences):
            self.complete_sequences = CompleteSequences(self.complete_sequences)

        if self.physical_linkage is not None and not isinstance(self.physical_linkage, PhysicalLinkage):
            self.physical_linkage = PhysicalLinkage(self.physical_linkage)

        if self.sequencing_run_id is not None and not isinstance(self.sequencing_run_id, str):
            self.sequencing_run_id = str(self.sequencing_run_id)

        if self.total_reads_passing_qc_filter is not None and not isinstance(self.total_reads_passing_qc_filter, int):
            self.total_reads_passing_qc_filter = int(self.total_reads_passing_qc_filter)

        if self.sequencing_platform is not None and not isinstance(self.sequencing_platform, str):
            self.sequencing_platform = str(self.sequencing_platform)

        if self.sequencing_facility is not None and not isinstance(self.sequencing_facility, str):
            self.sequencing_facility = str(self.sequencing_facility)

        if self.sequencing_run_date is not None and not isinstance(self.sequencing_run_date, XSDDateTime):
            self.sequencing_run_date = XSDDateTime(self.sequencing_run_date)

        if self.sequencing_kit is not None and not isinstance(self.sequencing_kit, str):
            self.sequencing_kit = str(self.sequencing_kit)

        if self.sequencing_files is not None and not isinstance(self.sequencing_files, SequencingData):
            self.sequencing_files = SequencingData(**as_dict(self.sequencing_files))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5TimePoint(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5TimePoint"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5TimePoint"
    class_name: ClassVar[str] = "V1p5TimePoint"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5TimePoint

    V1p5label: Optional[str] = None
    V1p5value: Optional[float] = None
    V1p5unit: Optional[Union[str, "V1p5Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5label is not None and not isinstance(self.V1p5label, str):
            self.V1p5label = str(self.V1p5label)

        if self.V1p5value is not None and not isinstance(self.V1p5value, float):
            self.V1p5value = float(self.V1p5value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Acknowledgement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Acknowledgement"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Acknowledgement"
    class_name: ClassVar[str] = "V1p5Acknowledgement"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Acknowledgement

    V1p5acknowledgement_id: Optional[str] = None
    V1p5name: Optional[str] = None
    V1p5institution_name: Optional[str] = None
    V1p5orcid_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5acknowledgement_id is not None and not isinstance(self.V1p5acknowledgement_id, str):
            self.V1p5acknowledgement_id = str(self.V1p5acknowledgement_id)

        if self.V1p5name is not None and not isinstance(self.V1p5name, str):
            self.V1p5name = str(self.V1p5name)

        if self.V1p5institution_name is not None and not isinstance(self.V1p5institution_name, str):
            self.V1p5institution_name = str(self.V1p5institution_name)

        if self.V1p5orcid_id is not None and not isinstance(self.V1p5orcid_id, str):
            self.V1p5orcid_id = str(self.V1p5orcid_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5RearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5RearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5RearrangedSequence"
    class_name: ClassVar[str] = "V1p5RearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5RearrangedSequence

    V1p5sequence_id: Optional[str] = None
    V1p5sequence: Optional[str] = None
    V1p5derivation: Optional[Union[str, "V1p5Derivation"]] = None
    V1p5observation_type: Optional[Union[str, "V1p5ObservationType"]] = None
    V1p5curation: Optional[str] = None
    V1p5repository_name: Optional[str] = None
    V1p5repository_ref: Optional[str] = None
    V1p5deposited_version: Optional[str] = None
    V1p5sequence_start: Optional[int] = None
    V1p5sequence_end: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5sequence_id is not None and not isinstance(self.V1p5sequence_id, str):
            self.V1p5sequence_id = str(self.V1p5sequence_id)

        if self.V1p5sequence is not None and not isinstance(self.V1p5sequence, str):
            self.V1p5sequence = str(self.V1p5sequence)

        if self.V1p5derivation is not None and not isinstance(self.V1p5derivation, V1p5Derivation):
            self.V1p5derivation = V1p5Derivation(self.V1p5derivation)

        if self.V1p5observation_type is not None and not isinstance(self.V1p5observation_type, V1p5ObservationType):
            self.V1p5observation_type = V1p5ObservationType(self.V1p5observation_type)

        if self.V1p5curation is not None and not isinstance(self.V1p5curation, str):
            self.V1p5curation = str(self.V1p5curation)

        if self.V1p5repository_name is not None and not isinstance(self.V1p5repository_name, str):
            self.V1p5repository_name = str(self.V1p5repository_name)

        if self.V1p5repository_ref is not None and not isinstance(self.V1p5repository_ref, str):
            self.V1p5repository_ref = str(self.V1p5repository_ref)

        if self.V1p5deposited_version is not None and not isinstance(self.V1p5deposited_version, str):
            self.V1p5deposited_version = str(self.V1p5deposited_version)

        if self.V1p5sequence_start is not None and not isinstance(self.V1p5sequence_start, int):
            self.V1p5sequence_start = int(self.V1p5sequence_start)

        if self.V1p5sequence_end is not None and not isinstance(self.V1p5sequence_end, int):
            self.V1p5sequence_end = int(self.V1p5sequence_end)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5UnrearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5UnrearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5UnrearrangedSequence"
    class_name: ClassVar[str] = "V1p5UnrearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5UnrearrangedSequence

    V1p5sequence_id: Optional[str] = None
    V1p5sequence: Optional[str] = None
    V1p5curation: Optional[str] = None
    V1p5repository_name: Optional[str] = None
    V1p5repository_ref: Optional[str] = None
    V1p5patch_no: Optional[str] = None
    V1p5gff_seqid: Optional[str] = None
    V1p5gff_start: Optional[int] = None
    V1p5gff_end: Optional[int] = None
    V1p5strand: Optional[Union[str, "V1p5Strand"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5sequence_id is not None and not isinstance(self.V1p5sequence_id, str):
            self.V1p5sequence_id = str(self.V1p5sequence_id)

        if self.V1p5sequence is not None and not isinstance(self.V1p5sequence, str):
            self.V1p5sequence = str(self.V1p5sequence)

        if self.V1p5curation is not None and not isinstance(self.V1p5curation, str):
            self.V1p5curation = str(self.V1p5curation)

        if self.V1p5repository_name is not None and not isinstance(self.V1p5repository_name, str):
            self.V1p5repository_name = str(self.V1p5repository_name)

        if self.V1p5repository_ref is not None and not isinstance(self.V1p5repository_ref, str):
            self.V1p5repository_ref = str(self.V1p5repository_ref)

        if self.V1p5patch_no is not None and not isinstance(self.V1p5patch_no, str):
            self.V1p5patch_no = str(self.V1p5patch_no)

        if self.V1p5gff_seqid is not None and not isinstance(self.V1p5gff_seqid, str):
            self.V1p5gff_seqid = str(self.V1p5gff_seqid)

        if self.V1p5gff_start is not None and not isinstance(self.V1p5gff_start, int):
            self.V1p5gff_start = int(self.V1p5gff_start)

        if self.V1p5gff_end is not None and not isinstance(self.V1p5gff_end, int):
            self.V1p5gff_end = int(self.V1p5gff_end)

        if self.V1p5strand is not None and not isinstance(self.V1p5strand, V1p5Strand):
            self.V1p5strand = V1p5Strand(self.V1p5strand)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5SequenceDelineationV(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5SequenceDelineationV"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5SequenceDelineationV"
    class_name: ClassVar[str] = "V1p5SequenceDelineationV"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5SequenceDelineationV

    V1p5sequence_delineation_id: Optional[str] = None
    V1p5delineation_scheme: Optional[str] = None
    V1p5unaligned_sequence: Optional[str] = None
    V1p5aligned_sequence: Optional[str] = None
    V1p5fwr1_start: Optional[int] = None
    V1p5fwr1_end: Optional[int] = None
    V1p5cdr1_start: Optional[int] = None
    V1p5cdr1_end: Optional[int] = None
    V1p5fwr2_start: Optional[int] = None
    V1p5fwr2_end: Optional[int] = None
    V1p5cdr2_start: Optional[int] = None
    V1p5cdr2_end: Optional[int] = None
    V1p5fwr3_start: Optional[int] = None
    V1p5fwr3_end: Optional[int] = None
    V1p5cdr3_start: Optional[int] = None
    V1p5alignment_labels: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5sequence_delineation_id is not None and not isinstance(self.V1p5sequence_delineation_id, str):
            self.V1p5sequence_delineation_id = str(self.V1p5sequence_delineation_id)

        if self.V1p5delineation_scheme is not None and not isinstance(self.V1p5delineation_scheme, str):
            self.V1p5delineation_scheme = str(self.V1p5delineation_scheme)

        if self.V1p5unaligned_sequence is not None and not isinstance(self.V1p5unaligned_sequence, str):
            self.V1p5unaligned_sequence = str(self.V1p5unaligned_sequence)

        if self.V1p5aligned_sequence is not None and not isinstance(self.V1p5aligned_sequence, str):
            self.V1p5aligned_sequence = str(self.V1p5aligned_sequence)

        if self.V1p5fwr1_start is not None and not isinstance(self.V1p5fwr1_start, int):
            self.V1p5fwr1_start = int(self.V1p5fwr1_start)

        if self.V1p5fwr1_end is not None and not isinstance(self.V1p5fwr1_end, int):
            self.V1p5fwr1_end = int(self.V1p5fwr1_end)

        if self.V1p5cdr1_start is not None and not isinstance(self.V1p5cdr1_start, int):
            self.V1p5cdr1_start = int(self.V1p5cdr1_start)

        if self.V1p5cdr1_end is not None and not isinstance(self.V1p5cdr1_end, int):
            self.V1p5cdr1_end = int(self.V1p5cdr1_end)

        if self.V1p5fwr2_start is not None and not isinstance(self.V1p5fwr2_start, int):
            self.V1p5fwr2_start = int(self.V1p5fwr2_start)

        if self.V1p5fwr2_end is not None and not isinstance(self.V1p5fwr2_end, int):
            self.V1p5fwr2_end = int(self.V1p5fwr2_end)

        if self.V1p5cdr2_start is not None and not isinstance(self.V1p5cdr2_start, int):
            self.V1p5cdr2_start = int(self.V1p5cdr2_start)

        if self.V1p5cdr2_end is not None and not isinstance(self.V1p5cdr2_end, int):
            self.V1p5cdr2_end = int(self.V1p5cdr2_end)

        if self.V1p5fwr3_start is not None and not isinstance(self.V1p5fwr3_start, int):
            self.V1p5fwr3_start = int(self.V1p5fwr3_start)

        if self.V1p5fwr3_end is not None and not isinstance(self.V1p5fwr3_end, int):
            self.V1p5fwr3_end = int(self.V1p5fwr3_end)

        if self.V1p5cdr3_start is not None and not isinstance(self.V1p5cdr3_start, int):
            self.V1p5cdr3_start = int(self.V1p5cdr3_start)

        if not isinstance(self.V1p5alignment_labels, list):
            self.V1p5alignment_labels = [self.V1p5alignment_labels] if self.V1p5alignment_labels is not None else []
        self.V1p5alignment_labels = [v if isinstance(v, str) else str(v) for v in self.V1p5alignment_labels]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5AlleleDescription(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5AlleleDescription"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5AlleleDescription"
    class_name: ClassVar[str] = "V1p5AlleleDescription"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5AlleleDescription

    V1p5allele_description_id: Optional[str] = None
    V1p5allele_description_ref: Optional[str] = None
    V1p5maintainer: Optional[str] = None
    V1p5acknowledgements: Optional[Union[Union[dict, V1p5Acknowledgement], List[Union[dict, V1p5Acknowledgement]]]] = empty_list()
    V1p5lab_address: Optional[str] = None
    V1p5release_version: Optional[str] = None
    V1p5release_date: Optional[Union[str, XSDDateTime]] = None
    V1p5release_description: Optional[str] = None
    V1p5label: Optional[str] = None
    V1p5sequence: Optional[str] = None
    V1p5coding_sequence: Optional[str] = None
    V1p5aliases: Optional[Union[str, List[str]]] = empty_list()
    V1p5locus: Optional[Union[str, "V1p5Locus"]] = None
    V1p5chromosome: Optional[int] = None
    V1p5sequence_type: Optional[Union[str, "V1p5SequenceType"]] = None
    V1p5functional: Optional[Union[bool, Bool]] = None
    V1p5inference_type: Optional[Union[str, "V1p5InferenceType"]] = None
    V1p5species: Optional[Union[str, "V1p5Species"]] = None
    V1p5species_subgroup: Optional[str] = None
    V1p5species_subgroup_type: Optional[Union[str, "V1p5SpeciesSubgroupType"]] = None
    V1p5status: Optional[Union[str, "V1p5Status"]] = None
    V1p5subgroup_designation: Optional[str] = None
    V1p5gene_designation: Optional[str] = None
    V1p5allele_designation: Optional[str] = None
    V1p5allele_similarity_cluster_designation: Optional[str] = None
    V1p5allele_similarity_cluster_member_id: Optional[str] = None
    V1p5j_codon_frame: Optional[Union[str, "V1p5JCodonFrame"]] = None
    V1p5gene_start: Optional[int] = None
    V1p5gene_end: Optional[int] = None
    V1p5utr_5_prime_start: Optional[int] = None
    V1p5utr_5_prime_end: Optional[int] = None
    V1p5leader_1_start: Optional[int] = None
    V1p5leader_1_end: Optional[int] = None
    V1p5leader_2_start: Optional[int] = None
    V1p5leader_2_end: Optional[int] = None
    V1p5v_rs_start: Optional[int] = None
    V1p5v_rs_end: Optional[int] = None
    V1p5d_rs_3_prime_start: Optional[int] = None
    V1p5d_rs_3_prime_end: Optional[int] = None
    V1p5d_rs_5_prime_start: Optional[int] = None
    V1p5d_rs_5_prime_end: Optional[int] = None
    V1p5j_cdr3_end: Optional[int] = None
    V1p5j_rs_start: Optional[int] = None
    V1p5j_rs_end: Optional[int] = None
    V1p5j_donor_splice: Optional[int] = None
    V1p5v_gene_delineations: Optional[Union[Union[dict, V1p5SequenceDelineationV], List[Union[dict, V1p5SequenceDelineationV]]]] = empty_list()
    V1p5unrearranged_support: Optional[Union[Union[dict, V1p5UnrearrangedSequence], List[Union[dict, V1p5UnrearrangedSequence]]]] = empty_list()
    V1p5rearranged_support: Optional[Union[Union[dict, V1p5RearrangedSequence], List[Union[dict, V1p5RearrangedSequence]]]] = empty_list()
    V1p5paralogs: Optional[Union[str, List[str]]] = empty_list()
    V1p5curation: Optional[str] = None
    V1p5curational_tags: Optional[Union[Union[str, "V1p5CurationalTags"], List[Union[str, "V1p5CurationalTags"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5allele_description_id is not None and not isinstance(self.V1p5allele_description_id, str):
            self.V1p5allele_description_id = str(self.V1p5allele_description_id)

        if self.V1p5allele_description_ref is not None and not isinstance(self.V1p5allele_description_ref, str):
            self.V1p5allele_description_ref = str(self.V1p5allele_description_ref)

        if self.V1p5maintainer is not None and not isinstance(self.V1p5maintainer, str):
            self.V1p5maintainer = str(self.V1p5maintainer)

        if not isinstance(self.V1p5acknowledgements, list):
            self.V1p5acknowledgements = [self.V1p5acknowledgements] if self.V1p5acknowledgements is not None else []
        self.V1p5acknowledgements = [v if isinstance(v, V1p5Acknowledgement) else V1p5Acknowledgement(**as_dict(v)) for v in self.V1p5acknowledgements]

        if self.V1p5lab_address is not None and not isinstance(self.V1p5lab_address, str):
            self.V1p5lab_address = str(self.V1p5lab_address)

        if self.V1p5release_version is not None and not isinstance(self.V1p5release_version, str):
            self.V1p5release_version = str(self.V1p5release_version)

        if self.V1p5release_date is not None and not isinstance(self.V1p5release_date, XSDDateTime):
            self.V1p5release_date = XSDDateTime(self.V1p5release_date)

        if self.V1p5release_description is not None and not isinstance(self.V1p5release_description, str):
            self.V1p5release_description = str(self.V1p5release_description)

        if self.V1p5label is not None and not isinstance(self.V1p5label, str):
            self.V1p5label = str(self.V1p5label)

        if self.V1p5sequence is not None and not isinstance(self.V1p5sequence, str):
            self.V1p5sequence = str(self.V1p5sequence)

        if self.V1p5coding_sequence is not None and not isinstance(self.V1p5coding_sequence, str):
            self.V1p5coding_sequence = str(self.V1p5coding_sequence)

        if not isinstance(self.V1p5aliases, list):
            self.V1p5aliases = [self.V1p5aliases] if self.V1p5aliases is not None else []
        self.V1p5aliases = [v if isinstance(v, str) else str(v) for v in self.V1p5aliases]

        if self.V1p5locus is not None and not isinstance(self.V1p5locus, V1p5Locus):
            self.V1p5locus = V1p5Locus(self.V1p5locus)

        if self.V1p5chromosome is not None and not isinstance(self.V1p5chromosome, int):
            self.V1p5chromosome = int(self.V1p5chromosome)

        if self.V1p5sequence_type is not None and not isinstance(self.V1p5sequence_type, V1p5SequenceType):
            self.V1p5sequence_type = V1p5SequenceType(self.V1p5sequence_type)

        if self.V1p5functional is not None and not isinstance(self.V1p5functional, Bool):
            self.V1p5functional = Bool(self.V1p5functional)

        if self.V1p5inference_type is not None and not isinstance(self.V1p5inference_type, V1p5InferenceType):
            self.V1p5inference_type = V1p5InferenceType(self.V1p5inference_type)

        if self.V1p5species_subgroup is not None and not isinstance(self.V1p5species_subgroup, str):
            self.V1p5species_subgroup = str(self.V1p5species_subgroup)

        if self.V1p5species_subgroup_type is not None and not isinstance(self.V1p5species_subgroup_type, V1p5SpeciesSubgroupType):
            self.V1p5species_subgroup_type = V1p5SpeciesSubgroupType(self.V1p5species_subgroup_type)

        if self.V1p5status is not None and not isinstance(self.V1p5status, V1p5Status):
            self.V1p5status = V1p5Status(self.V1p5status)

        if self.V1p5subgroup_designation is not None and not isinstance(self.V1p5subgroup_designation, str):
            self.V1p5subgroup_designation = str(self.V1p5subgroup_designation)

        if self.V1p5gene_designation is not None and not isinstance(self.V1p5gene_designation, str):
            self.V1p5gene_designation = str(self.V1p5gene_designation)

        if self.V1p5allele_designation is not None and not isinstance(self.V1p5allele_designation, str):
            self.V1p5allele_designation = str(self.V1p5allele_designation)

        if self.V1p5allele_similarity_cluster_designation is not None and not isinstance(self.V1p5allele_similarity_cluster_designation, str):
            self.V1p5allele_similarity_cluster_designation = str(self.V1p5allele_similarity_cluster_designation)

        if self.V1p5allele_similarity_cluster_member_id is not None and not isinstance(self.V1p5allele_similarity_cluster_member_id, str):
            self.V1p5allele_similarity_cluster_member_id = str(self.V1p5allele_similarity_cluster_member_id)

        if self.V1p5j_codon_frame is not None and not isinstance(self.V1p5j_codon_frame, V1p5JCodonFrame):
            self.V1p5j_codon_frame = V1p5JCodonFrame(self.V1p5j_codon_frame)

        if self.V1p5gene_start is not None and not isinstance(self.V1p5gene_start, int):
            self.V1p5gene_start = int(self.V1p5gene_start)

        if self.V1p5gene_end is not None and not isinstance(self.V1p5gene_end, int):
            self.V1p5gene_end = int(self.V1p5gene_end)

        if self.V1p5utr_5_prime_start is not None and not isinstance(self.V1p5utr_5_prime_start, int):
            self.V1p5utr_5_prime_start = int(self.V1p5utr_5_prime_start)

        if self.V1p5utr_5_prime_end is not None and not isinstance(self.V1p5utr_5_prime_end, int):
            self.V1p5utr_5_prime_end = int(self.V1p5utr_5_prime_end)

        if self.V1p5leader_1_start is not None and not isinstance(self.V1p5leader_1_start, int):
            self.V1p5leader_1_start = int(self.V1p5leader_1_start)

        if self.V1p5leader_1_end is not None and not isinstance(self.V1p5leader_1_end, int):
            self.V1p5leader_1_end = int(self.V1p5leader_1_end)

        if self.V1p5leader_2_start is not None and not isinstance(self.V1p5leader_2_start, int):
            self.V1p5leader_2_start = int(self.V1p5leader_2_start)

        if self.V1p5leader_2_end is not None and not isinstance(self.V1p5leader_2_end, int):
            self.V1p5leader_2_end = int(self.V1p5leader_2_end)

        if self.V1p5v_rs_start is not None and not isinstance(self.V1p5v_rs_start, int):
            self.V1p5v_rs_start = int(self.V1p5v_rs_start)

        if self.V1p5v_rs_end is not None and not isinstance(self.V1p5v_rs_end, int):
            self.V1p5v_rs_end = int(self.V1p5v_rs_end)

        if self.V1p5d_rs_3_prime_start is not None and not isinstance(self.V1p5d_rs_3_prime_start, int):
            self.V1p5d_rs_3_prime_start = int(self.V1p5d_rs_3_prime_start)

        if self.V1p5d_rs_3_prime_end is not None and not isinstance(self.V1p5d_rs_3_prime_end, int):
            self.V1p5d_rs_3_prime_end = int(self.V1p5d_rs_3_prime_end)

        if self.V1p5d_rs_5_prime_start is not None and not isinstance(self.V1p5d_rs_5_prime_start, int):
            self.V1p5d_rs_5_prime_start = int(self.V1p5d_rs_5_prime_start)

        if self.V1p5d_rs_5_prime_end is not None and not isinstance(self.V1p5d_rs_5_prime_end, int):
            self.V1p5d_rs_5_prime_end = int(self.V1p5d_rs_5_prime_end)

        if self.V1p5j_cdr3_end is not None and not isinstance(self.V1p5j_cdr3_end, int):
            self.V1p5j_cdr3_end = int(self.V1p5j_cdr3_end)

        if self.V1p5j_rs_start is not None and not isinstance(self.V1p5j_rs_start, int):
            self.V1p5j_rs_start = int(self.V1p5j_rs_start)

        if self.V1p5j_rs_end is not None and not isinstance(self.V1p5j_rs_end, int):
            self.V1p5j_rs_end = int(self.V1p5j_rs_end)

        if self.V1p5j_donor_splice is not None and not isinstance(self.V1p5j_donor_splice, int):
            self.V1p5j_donor_splice = int(self.V1p5j_donor_splice)

        if not isinstance(self.V1p5v_gene_delineations, list):
            self.V1p5v_gene_delineations = [self.V1p5v_gene_delineations] if self.V1p5v_gene_delineations is not None else []
        self.V1p5v_gene_delineations = [v if isinstance(v, V1p5SequenceDelineationV) else V1p5SequenceDelineationV(**as_dict(v)) for v in self.V1p5v_gene_delineations]

        if not isinstance(self.V1p5unrearranged_support, list):
            self.V1p5unrearranged_support = [self.V1p5unrearranged_support] if self.V1p5unrearranged_support is not None else []
        self.V1p5unrearranged_support = [v if isinstance(v, V1p5UnrearrangedSequence) else V1p5UnrearrangedSequence(**as_dict(v)) for v in self.V1p5unrearranged_support]

        if not isinstance(self.V1p5rearranged_support, list):
            self.V1p5rearranged_support = [self.V1p5rearranged_support] if self.V1p5rearranged_support is not None else []
        self.V1p5rearranged_support = [v if isinstance(v, V1p5RearrangedSequence) else V1p5RearrangedSequence(**as_dict(v)) for v in self.V1p5rearranged_support]

        if not isinstance(self.V1p5paralogs, list):
            self.V1p5paralogs = [self.V1p5paralogs] if self.V1p5paralogs is not None else []
        self.V1p5paralogs = [v if isinstance(v, str) else str(v) for v in self.V1p5paralogs]

        if self.V1p5curation is not None and not isinstance(self.V1p5curation, str):
            self.V1p5curation = str(self.V1p5curation)

        if not isinstance(self.V1p5curational_tags, list):
            self.V1p5curational_tags = [self.V1p5curational_tags] if self.V1p5curational_tags is not None else []
        self.V1p5curational_tags = [v if isinstance(v, V1p5CurationalTags) else V1p5CurationalTags(v) for v in self.V1p5curational_tags]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5GermlineSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5GermlineSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5GermlineSet"
    class_name: ClassVar[str] = "V1p5GermlineSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5GermlineSet

    V1p5germline_set_id: Optional[str] = None
    V1p5author: Optional[str] = None
    V1p5lab_name: Optional[str] = None
    V1p5lab_address: Optional[str] = None
    V1p5acknowledgements: Optional[Union[Union[dict, V1p5Acknowledgement], List[Union[dict, V1p5Acknowledgement]]]] = empty_list()
    V1p5release_version: Optional[str] = None
    V1p5release_description: Optional[str] = None
    V1p5release_date: Optional[Union[str, XSDDateTime]] = None
    V1p5germline_set_name: Optional[str] = None
    V1p5germline_set_ref: Optional[str] = None
    V1p5pub_ids: Optional[str] = None
    V1p5species: Optional[Union[str, "V1p5Species"]] = None
    V1p5species_subgroup: Optional[str] = None
    V1p5species_subgroup_type: Optional[Union[str, "V1p5SpeciesSubgroupType"]] = None
    V1p5locus: Optional[Union[str, "V1p5Locus"]] = None
    V1p5allele_descriptions: Optional[Union[Union[dict, V1p5AlleleDescription], List[Union[dict, V1p5AlleleDescription]]]] = empty_list()
    V1p5curation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5germline_set_id is not None and not isinstance(self.V1p5germline_set_id, str):
            self.V1p5germline_set_id = str(self.V1p5germline_set_id)

        if self.V1p5author is not None and not isinstance(self.V1p5author, str):
            self.V1p5author = str(self.V1p5author)

        if self.V1p5lab_name is not None and not isinstance(self.V1p5lab_name, str):
            self.V1p5lab_name = str(self.V1p5lab_name)

        if self.V1p5lab_address is not None and not isinstance(self.V1p5lab_address, str):
            self.V1p5lab_address = str(self.V1p5lab_address)

        if not isinstance(self.V1p5acknowledgements, list):
            self.V1p5acknowledgements = [self.V1p5acknowledgements] if self.V1p5acknowledgements is not None else []
        self.V1p5acknowledgements = [v if isinstance(v, V1p5Acknowledgement) else V1p5Acknowledgement(**as_dict(v)) for v in self.V1p5acknowledgements]

        if self.V1p5release_version is not None and not isinstance(self.V1p5release_version, str):
            self.V1p5release_version = str(self.V1p5release_version)

        if self.V1p5release_description is not None and not isinstance(self.V1p5release_description, str):
            self.V1p5release_description = str(self.V1p5release_description)

        if self.V1p5release_date is not None and not isinstance(self.V1p5release_date, XSDDateTime):
            self.V1p5release_date = XSDDateTime(self.V1p5release_date)

        if self.V1p5germline_set_name is not None and not isinstance(self.V1p5germline_set_name, str):
            self.V1p5germline_set_name = str(self.V1p5germline_set_name)

        if self.V1p5germline_set_ref is not None and not isinstance(self.V1p5germline_set_ref, str):
            self.V1p5germline_set_ref = str(self.V1p5germline_set_ref)

        if self.V1p5pub_ids is not None and not isinstance(self.V1p5pub_ids, str):
            self.V1p5pub_ids = str(self.V1p5pub_ids)

        if self.V1p5species_subgroup is not None and not isinstance(self.V1p5species_subgroup, str):
            self.V1p5species_subgroup = str(self.V1p5species_subgroup)

        if self.V1p5species_subgroup_type is not None and not isinstance(self.V1p5species_subgroup_type, V1p5SpeciesSubgroupType):
            self.V1p5species_subgroup_type = V1p5SpeciesSubgroupType(self.V1p5species_subgroup_type)

        if self.V1p5locus is not None and not isinstance(self.V1p5locus, V1p5Locus):
            self.V1p5locus = V1p5Locus(self.V1p5locus)

        if not isinstance(self.V1p5allele_descriptions, list):
            self.V1p5allele_descriptions = [self.V1p5allele_descriptions] if self.V1p5allele_descriptions is not None else []
        self.V1p5allele_descriptions = [v if isinstance(v, V1p5AlleleDescription) else V1p5AlleleDescription(**as_dict(v)) for v in self.V1p5allele_descriptions]

        if self.V1p5curation is not None and not isinstance(self.V1p5curation, str):
            self.V1p5curation = str(self.V1p5curation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5GenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5GenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5GenotypeSet"
    class_name: ClassVar[str] = "V1p5GenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5GenotypeSet

    V1p5receptor_genotype_set_id: Optional[str] = None
    V1p5genotype_class_list: Optional[Union[Union[dict, "V1p5Genotype"], List[Union[dict, "V1p5Genotype"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5receptor_genotype_set_id is not None and not isinstance(self.V1p5receptor_genotype_set_id, str):
            self.V1p5receptor_genotype_set_id = str(self.V1p5receptor_genotype_set_id)

        if not isinstance(self.V1p5genotype_class_list, list):
            self.V1p5genotype_class_list = [self.V1p5genotype_class_list] if self.V1p5genotype_class_list is not None else []
        self.V1p5genotype_class_list = [v if isinstance(v, V1p5Genotype) else V1p5Genotype(**as_dict(v)) for v in self.V1p5genotype_class_list]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Genotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Genotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Genotype"
    class_name: ClassVar[str] = "V1p5Genotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Genotype

    V1p5receptor_genotype_id: Optional[str] = None
    V1p5locus: Optional[Union[str, "V1p5Locus"]] = None
    V1p5documented_alleles: Optional[Union[Union[dict, "V1p5DocumentedAllele"], List[Union[dict, "V1p5DocumentedAllele"]]]] = empty_list()
    V1p5undocumented_alleles: Optional[Union[Union[dict, "V1p5UndocumentedAllele"], List[Union[dict, "V1p5UndocumentedAllele"]]]] = empty_list()
    V1p5deleted_genes: Optional[Union[Union[dict, "V1p5DeletedGene"], List[Union[dict, "V1p5DeletedGene"]]]] = empty_list()
    V1p5inference_process: Optional[Union[str, "V1p5InferenceProcess"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5receptor_genotype_id is not None and not isinstance(self.V1p5receptor_genotype_id, str):
            self.V1p5receptor_genotype_id = str(self.V1p5receptor_genotype_id)

        if self.V1p5locus is not None and not isinstance(self.V1p5locus, V1p5Locus):
            self.V1p5locus = V1p5Locus(self.V1p5locus)

        if not isinstance(self.V1p5documented_alleles, list):
            self.V1p5documented_alleles = [self.V1p5documented_alleles] if self.V1p5documented_alleles is not None else []
        self.V1p5documented_alleles = [v if isinstance(v, V1p5DocumentedAllele) else V1p5DocumentedAllele(**as_dict(v)) for v in self.V1p5documented_alleles]

        if not isinstance(self.V1p5undocumented_alleles, list):
            self.V1p5undocumented_alleles = [self.V1p5undocumented_alleles] if self.V1p5undocumented_alleles is not None else []
        self.V1p5undocumented_alleles = [v if isinstance(v, V1p5UndocumentedAllele) else V1p5UndocumentedAllele(**as_dict(v)) for v in self.V1p5undocumented_alleles]

        if not isinstance(self.V1p5deleted_genes, list):
            self.V1p5deleted_genes = [self.V1p5deleted_genes] if self.V1p5deleted_genes is not None else []
        self.V1p5deleted_genes = [v if isinstance(v, V1p5DeletedGene) else V1p5DeletedGene(**as_dict(v)) for v in self.V1p5deleted_genes]

        if self.V1p5inference_process is not None and not isinstance(self.V1p5inference_process, V1p5InferenceProcess):
            self.V1p5inference_process = V1p5InferenceProcess(self.V1p5inference_process)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5DocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5DocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5DocumentedAllele"
    class_name: ClassVar[str] = "V1p5DocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5DocumentedAllele

    V1p5label: Optional[str] = None
    V1p5germline_set_ref: Optional[str] = None
    V1p5phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5label is not None and not isinstance(self.V1p5label, str):
            self.V1p5label = str(self.V1p5label)

        if self.V1p5germline_set_ref is not None and not isinstance(self.V1p5germline_set_ref, str):
            self.V1p5germline_set_ref = str(self.V1p5germline_set_ref)

        if self.V1p5phasing is not None and not isinstance(self.V1p5phasing, int):
            self.V1p5phasing = int(self.V1p5phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5UndocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5UndocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5UndocumentedAllele"
    class_name: ClassVar[str] = "V1p5UndocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5UndocumentedAllele

    V1p5allele_name: Optional[str] = None
    V1p5sequence: Optional[str] = None
    V1p5phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5allele_name is not None and not isinstance(self.V1p5allele_name, str):
            self.V1p5allele_name = str(self.V1p5allele_name)

        if self.V1p5sequence is not None and not isinstance(self.V1p5sequence, str):
            self.V1p5sequence = str(self.V1p5sequence)

        if self.V1p5phasing is not None and not isinstance(self.V1p5phasing, int):
            self.V1p5phasing = int(self.V1p5phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5DeletedGene(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5DeletedGene"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5DeletedGene"
    class_name: ClassVar[str] = "V1p5DeletedGene"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5DeletedGene

    V1p5label: Optional[str] = None
    V1p5germline_set_ref: Optional[str] = None
    V1p5phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5label is not None and not isinstance(self.V1p5label, str):
            self.V1p5label = str(self.V1p5label)

        if self.V1p5germline_set_ref is not None and not isinstance(self.V1p5germline_set_ref, str):
            self.V1p5germline_set_ref = str(self.V1p5germline_set_ref)

        if self.V1p5phasing is not None and not isinstance(self.V1p5phasing, int):
            self.V1p5phasing = int(self.V1p5phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5MHCGenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5MHCGenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5MHCGenotypeSet"
    class_name: ClassVar[str] = "V1p5MHCGenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5MHCGenotypeSet

    V1p5mhc_genotype_set_id: Optional[str] = None
    V1p5mhc_genotype_list: Optional[Union[Union[dict, "V1p5MHCGenotype"], List[Union[dict, "V1p5MHCGenotype"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5mhc_genotype_set_id is not None and not isinstance(self.V1p5mhc_genotype_set_id, str):
            self.V1p5mhc_genotype_set_id = str(self.V1p5mhc_genotype_set_id)

        if not isinstance(self.V1p5mhc_genotype_list, list):
            self.V1p5mhc_genotype_list = [self.V1p5mhc_genotype_list] if self.V1p5mhc_genotype_list is not None else []
        self.V1p5mhc_genotype_list = [v if isinstance(v, V1p5MHCGenotype) else V1p5MHCGenotype(**as_dict(v)) for v in self.V1p5mhc_genotype_list]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5MHCGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5MHCGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5MHCGenotype"
    class_name: ClassVar[str] = "V1p5MHCGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5MHCGenotype

    V1p5mhc_genotype_id: Optional[str] = None
    V1p5mhc_class: Optional[Union[str, "V1p5MhcClass"]] = None
    V1p5mhc_alleles: Optional[Union[Union[dict, "V1p5MHCAllele"], List[Union[dict, "V1p5MHCAllele"]]]] = empty_list()
    V1p5mhc_genotyping_method: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5mhc_genotype_id is not None and not isinstance(self.V1p5mhc_genotype_id, str):
            self.V1p5mhc_genotype_id = str(self.V1p5mhc_genotype_id)

        if self.V1p5mhc_class is not None and not isinstance(self.V1p5mhc_class, V1p5MhcClass):
            self.V1p5mhc_class = V1p5MhcClass(self.V1p5mhc_class)

        if not isinstance(self.V1p5mhc_alleles, list):
            self.V1p5mhc_alleles = [self.V1p5mhc_alleles] if self.V1p5mhc_alleles is not None else []
        self.V1p5mhc_alleles = [v if isinstance(v, V1p5MHCAllele) else V1p5MHCAllele(**as_dict(v)) for v in self.V1p5mhc_alleles]

        if self.V1p5mhc_genotyping_method is not None and not isinstance(self.V1p5mhc_genotyping_method, str):
            self.V1p5mhc_genotyping_method = str(self.V1p5mhc_genotyping_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5MHCAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5MHCAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5MHCAllele"
    class_name: ClassVar[str] = "V1p5MHCAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5MHCAllele

    V1p5allele_designation: Optional[str] = None
    V1p5gene: Optional[Union[str, "V1p5Gene"]] = None
    V1p5reference_set_ref: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5allele_designation is not None and not isinstance(self.V1p5allele_designation, str):
            self.V1p5allele_designation = str(self.V1p5allele_designation)

        if self.V1p5reference_set_ref is not None and not isinstance(self.V1p5reference_set_ref, str):
            self.V1p5reference_set_ref = str(self.V1p5reference_set_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5SubjectGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5SubjectGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5SubjectGenotype"
    class_name: ClassVar[str] = "V1p5SubjectGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5SubjectGenotype

    V1p5receptor_genotype_set: Optional[Union[dict, V1p5GenotypeSet]] = None
    V1p5mhc_genotype_set: Optional[Union[dict, V1p5MHCGenotypeSet]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5receptor_genotype_set is not None and not isinstance(self.V1p5receptor_genotype_set, V1p5GenotypeSet):
            self.V1p5receptor_genotype_set = V1p5GenotypeSet(**as_dict(self.V1p5receptor_genotype_set))

        if self.V1p5mhc_genotype_set is not None and not isinstance(self.V1p5mhc_genotype_set, V1p5MHCGenotypeSet):
            self.V1p5mhc_genotype_set = V1p5MHCGenotypeSet(**as_dict(self.V1p5mhc_genotype_set))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Study(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Study"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Study"
    class_name: ClassVar[str] = "V1p5Study"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Study

    V1p5study_id: Optional[str] = None
    V1p5study_title: Optional[str] = None
    V1p5study_type: Optional[Union[str, "V1p5StudyType"]] = None
    V1p5study_description: Optional[str] = None
    V1p5inclusion_exclusion_criteria: Optional[str] = None
    V1p5grants: Optional[str] = None
    V1p5study_contact: Optional[str] = None
    V1p5collected_by: Optional[str] = None
    V1p5lab_name: Optional[str] = None
    V1p5lab_address: Optional[str] = None
    V1p5submitted_by: Optional[str] = None
    V1p5pub_ids: Optional[str] = None
    V1p5keywords_study: Optional[Union[Union[str, "V1p5KeywordsStudy"], List[Union[str, "V1p5KeywordsStudy"]]]] = empty_list()
    V1p5adc_publish_date: Optional[Union[str, XSDDateTime]] = None
    V1p5adc_update_date: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5study_id is not None and not isinstance(self.V1p5study_id, str):
            self.V1p5study_id = str(self.V1p5study_id)

        if self.V1p5study_title is not None and not isinstance(self.V1p5study_title, str):
            self.V1p5study_title = str(self.V1p5study_title)

        if self.V1p5study_description is not None and not isinstance(self.V1p5study_description, str):
            self.V1p5study_description = str(self.V1p5study_description)

        if self.V1p5inclusion_exclusion_criteria is not None and not isinstance(self.V1p5inclusion_exclusion_criteria, str):
            self.V1p5inclusion_exclusion_criteria = str(self.V1p5inclusion_exclusion_criteria)

        if self.V1p5grants is not None and not isinstance(self.V1p5grants, str):
            self.V1p5grants = str(self.V1p5grants)

        if self.V1p5study_contact is not None and not isinstance(self.V1p5study_contact, str):
            self.V1p5study_contact = str(self.V1p5study_contact)

        if self.V1p5collected_by is not None and not isinstance(self.V1p5collected_by, str):
            self.V1p5collected_by = str(self.V1p5collected_by)

        if self.V1p5lab_name is not None and not isinstance(self.V1p5lab_name, str):
            self.V1p5lab_name = str(self.V1p5lab_name)

        if self.V1p5lab_address is not None and not isinstance(self.V1p5lab_address, str):
            self.V1p5lab_address = str(self.V1p5lab_address)

        if self.V1p5submitted_by is not None and not isinstance(self.V1p5submitted_by, str):
            self.V1p5submitted_by = str(self.V1p5submitted_by)

        if self.V1p5pub_ids is not None and not isinstance(self.V1p5pub_ids, str):
            self.V1p5pub_ids = str(self.V1p5pub_ids)

        if not isinstance(self.V1p5keywords_study, list):
            self.V1p5keywords_study = [self.V1p5keywords_study] if self.V1p5keywords_study is not None else []
        self.V1p5keywords_study = [v if isinstance(v, V1p5KeywordsStudy) else V1p5KeywordsStudy(v) for v in self.V1p5keywords_study]

        if self.V1p5adc_publish_date is not None and not isinstance(self.V1p5adc_publish_date, XSDDateTime):
            self.V1p5adc_publish_date = XSDDateTime(self.V1p5adc_publish_date)

        if self.V1p5adc_update_date is not None and not isinstance(self.V1p5adc_update_date, XSDDateTime):
            self.V1p5adc_update_date = XSDDateTime(self.V1p5adc_update_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Subject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Subject"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Subject"
    class_name: ClassVar[str] = "V1p5Subject"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Subject

    V1p5subject_id: Optional[str] = None
    V1p5synthetic: Optional[Union[bool, Bool]] = None
    V1p5species: Optional[Union[str, "V1p5Species"]] = None
    V1p5sex: Optional[Union[str, "V1p5Sex"]] = None
    V1p5age_min: Optional[float] = None
    V1p5age_max: Optional[float] = None
    V1p5age_unit: Optional[Union[str, "V1p5AgeUnit"]] = None
    V1p5age_event: Optional[str] = None
    V1p5ancestry_population: Optional[str] = None
    V1p5ethnicity: Optional[str] = None
    V1p5race: Optional[str] = None
    V1p5strain_name: Optional[str] = None
    V1p5linked_subjects: Optional[str] = None
    V1p5link_type: Optional[str] = None
    V1p5diagnosis: Optional[Union[Union[dict, "V1p5Diagnosis"], List[Union[dict, "V1p5Diagnosis"]]]] = empty_list()
    V1p5genotype: Optional[Union[dict, V1p5SubjectGenotype]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5subject_id is not None and not isinstance(self.V1p5subject_id, str):
            self.V1p5subject_id = str(self.V1p5subject_id)

        if self.V1p5synthetic is not None and not isinstance(self.V1p5synthetic, Bool):
            self.V1p5synthetic = Bool(self.V1p5synthetic)

        if self.V1p5sex is not None and not isinstance(self.V1p5sex, V1p5Sex):
            self.V1p5sex = V1p5Sex(self.V1p5sex)

        if self.V1p5age_min is not None and not isinstance(self.V1p5age_min, float):
            self.V1p5age_min = float(self.V1p5age_min)

        if self.V1p5age_max is not None and not isinstance(self.V1p5age_max, float):
            self.V1p5age_max = float(self.V1p5age_max)

        if self.V1p5age_event is not None and not isinstance(self.V1p5age_event, str):
            self.V1p5age_event = str(self.V1p5age_event)

        if self.V1p5ancestry_population is not None and not isinstance(self.V1p5ancestry_population, str):
            self.V1p5ancestry_population = str(self.V1p5ancestry_population)

        if self.V1p5ethnicity is not None and not isinstance(self.V1p5ethnicity, str):
            self.V1p5ethnicity = str(self.V1p5ethnicity)

        if self.V1p5race is not None and not isinstance(self.V1p5race, str):
            self.V1p5race = str(self.V1p5race)

        if self.V1p5strain_name is not None and not isinstance(self.V1p5strain_name, str):
            self.V1p5strain_name = str(self.V1p5strain_name)

        if self.V1p5linked_subjects is not None and not isinstance(self.V1p5linked_subjects, str):
            self.V1p5linked_subjects = str(self.V1p5linked_subjects)

        if self.V1p5link_type is not None and not isinstance(self.V1p5link_type, str):
            self.V1p5link_type = str(self.V1p5link_type)

        if not isinstance(self.V1p5diagnosis, list):
            self.V1p5diagnosis = [self.V1p5diagnosis] if self.V1p5diagnosis is not None else []
        self.V1p5diagnosis = [v if isinstance(v, V1p5Diagnosis) else V1p5Diagnosis(**as_dict(v)) for v in self.V1p5diagnosis]

        if self.V1p5genotype is not None and not isinstance(self.V1p5genotype, V1p5SubjectGenotype):
            self.V1p5genotype = V1p5SubjectGenotype(**as_dict(self.V1p5genotype))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Diagnosis(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Diagnosis"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Diagnosis"
    class_name: ClassVar[str] = "V1p5Diagnosis"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Diagnosis

    V1p5study_group_description: Optional[str] = None
    V1p5disease_diagnosis: Optional[Union[str, "V1p5DiseaseDiagnosis"]] = None
    V1p5disease_length: Optional[str] = None
    V1p5disease_stage: Optional[str] = None
    V1p5prior_therapies: Optional[str] = None
    V1p5immunogen: Optional[str] = None
    V1p5intervention: Optional[str] = None
    V1p5medical_history: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5study_group_description is not None and not isinstance(self.V1p5study_group_description, str):
            self.V1p5study_group_description = str(self.V1p5study_group_description)

        if self.V1p5disease_length is not None and not isinstance(self.V1p5disease_length, str):
            self.V1p5disease_length = str(self.V1p5disease_length)

        if self.V1p5disease_stage is not None and not isinstance(self.V1p5disease_stage, str):
            self.V1p5disease_stage = str(self.V1p5disease_stage)

        if self.V1p5prior_therapies is not None and not isinstance(self.V1p5prior_therapies, str):
            self.V1p5prior_therapies = str(self.V1p5prior_therapies)

        if self.V1p5immunogen is not None and not isinstance(self.V1p5immunogen, str):
            self.V1p5immunogen = str(self.V1p5immunogen)

        if self.V1p5intervention is not None and not isinstance(self.V1p5intervention, str):
            self.V1p5intervention = str(self.V1p5intervention)

        if self.V1p5medical_history is not None and not isinstance(self.V1p5medical_history, str):
            self.V1p5medical_history = str(self.V1p5medical_history)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Sample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Sample"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Sample"
    class_name: ClassVar[str] = "V1p5Sample"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Sample

    V1p5sample_id: Optional[str] = None
    V1p5sample_type: Optional[str] = None
    V1p5tissue: Optional[Union[str, "V1p5Tissue"]] = None
    V1p5anatomic_site: Optional[str] = None
    V1p5disease_state_sample: Optional[str] = None
    V1p5collection_time_point_relative: Optional[float] = None
    V1p5collection_time_point_relative_unit: Optional[Union[str, "V1p5CollectionTimePointRelativeUnit"]] = None
    V1p5collection_time_point_reference: Optional[str] = None
    V1p5biomaterial_provider: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5sample_id is not None and not isinstance(self.V1p5sample_id, str):
            self.V1p5sample_id = str(self.V1p5sample_id)

        if self.V1p5sample_type is not None and not isinstance(self.V1p5sample_type, str):
            self.V1p5sample_type = str(self.V1p5sample_type)

        if self.V1p5anatomic_site is not None and not isinstance(self.V1p5anatomic_site, str):
            self.V1p5anatomic_site = str(self.V1p5anatomic_site)

        if self.V1p5disease_state_sample is not None and not isinstance(self.V1p5disease_state_sample, str):
            self.V1p5disease_state_sample = str(self.V1p5disease_state_sample)

        if self.V1p5collection_time_point_relative is not None and not isinstance(self.V1p5collection_time_point_relative, float):
            self.V1p5collection_time_point_relative = float(self.V1p5collection_time_point_relative)

        if self.V1p5collection_time_point_reference is not None and not isinstance(self.V1p5collection_time_point_reference, str):
            self.V1p5collection_time_point_reference = str(self.V1p5collection_time_point_reference)

        if self.V1p5biomaterial_provider is not None and not isinstance(self.V1p5biomaterial_provider, str):
            self.V1p5biomaterial_provider = str(self.V1p5biomaterial_provider)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5CellProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5CellProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5CellProcessing"
    class_name: ClassVar[str] = "V1p5CellProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5CellProcessing

    V1p5tissue_processing: Optional[str] = None
    V1p5cell_subset: Optional[Union[str, "V1p5CellSubset"]] = None
    V1p5cell_phenotype: Optional[str] = None
    V1p5cell_species: Optional[Union[str, "V1p5CellSpecies"]] = None
    V1p5single_cell: Optional[Union[bool, Bool]] = None
    V1p5cell_number: Optional[int] = None
    V1p5cells_per_reaction: Optional[int] = None
    V1p5cell_storage: Optional[Union[bool, Bool]] = None
    V1p5cell_quality: Optional[str] = None
    V1p5cell_isolation: Optional[str] = None
    V1p5cell_processing_protocol: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5tissue_processing is not None and not isinstance(self.V1p5tissue_processing, str):
            self.V1p5tissue_processing = str(self.V1p5tissue_processing)

        if self.V1p5cell_phenotype is not None and not isinstance(self.V1p5cell_phenotype, str):
            self.V1p5cell_phenotype = str(self.V1p5cell_phenotype)

        if self.V1p5single_cell is not None and not isinstance(self.V1p5single_cell, Bool):
            self.V1p5single_cell = Bool(self.V1p5single_cell)

        if self.V1p5cell_number is not None and not isinstance(self.V1p5cell_number, int):
            self.V1p5cell_number = int(self.V1p5cell_number)

        if self.V1p5cells_per_reaction is not None and not isinstance(self.V1p5cells_per_reaction, int):
            self.V1p5cells_per_reaction = int(self.V1p5cells_per_reaction)

        if self.V1p5cell_storage is not None and not isinstance(self.V1p5cell_storage, Bool):
            self.V1p5cell_storage = Bool(self.V1p5cell_storage)

        if self.V1p5cell_quality is not None and not isinstance(self.V1p5cell_quality, str):
            self.V1p5cell_quality = str(self.V1p5cell_quality)

        if self.V1p5cell_isolation is not None and not isinstance(self.V1p5cell_isolation, str):
            self.V1p5cell_isolation = str(self.V1p5cell_isolation)

        if self.V1p5cell_processing_protocol is not None and not isinstance(self.V1p5cell_processing_protocol, str):
            self.V1p5cell_processing_protocol = str(self.V1p5cell_processing_protocol)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5PCRTarget(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5PCRTarget"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5PCRTarget"
    class_name: ClassVar[str] = "V1p5PCRTarget"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5PCRTarget

    V1p5pcr_target_locus: Optional[Union[str, "V1p5PcrTargetLocus"]] = None
    V1p5forward_pcr_primer_target_location: Optional[str] = None
    V1p5reverse_pcr_primer_target_location: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5pcr_target_locus is not None and not isinstance(self.V1p5pcr_target_locus, V1p5PcrTargetLocus):
            self.V1p5pcr_target_locus = V1p5PcrTargetLocus(self.V1p5pcr_target_locus)

        if self.V1p5forward_pcr_primer_target_location is not None and not isinstance(self.V1p5forward_pcr_primer_target_location, str):
            self.V1p5forward_pcr_primer_target_location = str(self.V1p5forward_pcr_primer_target_location)

        if self.V1p5reverse_pcr_primer_target_location is not None and not isinstance(self.V1p5reverse_pcr_primer_target_location, str):
            self.V1p5reverse_pcr_primer_target_location = str(self.V1p5reverse_pcr_primer_target_location)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5NucleicAcidProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5NucleicAcidProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5NucleicAcidProcessing"
    class_name: ClassVar[str] = "V1p5NucleicAcidProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5NucleicAcidProcessing

    V1p5template_class: Optional[Union[str, "V1p5TemplateClass"]] = None
    V1p5template_quality: Optional[str] = None
    V1p5template_amount: Optional[float] = None
    V1p5template_amount_unit: Optional[Union[str, "V1p5TemplateAmountUnit"]] = None
    V1p5library_generation_method: Optional[Union[str, "V1p5LibraryGenerationMethod"]] = None
    V1p5library_generation_protocol: Optional[str] = None
    V1p5library_generation_kit_version: Optional[str] = None
    V1p5pcr_target: Optional[Union[Union[dict, V1p5PCRTarget], List[Union[dict, V1p5PCRTarget]]]] = empty_list()
    V1p5complete_sequences: Optional[Union[str, "V1p5CompleteSequences"]] = None
    V1p5physical_linkage: Optional[Union[str, "V1p5PhysicalLinkage"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5template_class is not None and not isinstance(self.V1p5template_class, V1p5TemplateClass):
            self.V1p5template_class = V1p5TemplateClass(self.V1p5template_class)

        if self.V1p5template_quality is not None and not isinstance(self.V1p5template_quality, str):
            self.V1p5template_quality = str(self.V1p5template_quality)

        if self.V1p5template_amount is not None and not isinstance(self.V1p5template_amount, float):
            self.V1p5template_amount = float(self.V1p5template_amount)

        if self.V1p5library_generation_method is not None and not isinstance(self.V1p5library_generation_method, V1p5LibraryGenerationMethod):
            self.V1p5library_generation_method = V1p5LibraryGenerationMethod(self.V1p5library_generation_method)

        if self.V1p5library_generation_protocol is not None and not isinstance(self.V1p5library_generation_protocol, str):
            self.V1p5library_generation_protocol = str(self.V1p5library_generation_protocol)

        if self.V1p5library_generation_kit_version is not None and not isinstance(self.V1p5library_generation_kit_version, str):
            self.V1p5library_generation_kit_version = str(self.V1p5library_generation_kit_version)

        if not isinstance(self.V1p5pcr_target, list):
            self.V1p5pcr_target = [self.V1p5pcr_target] if self.V1p5pcr_target is not None else []
        self.V1p5pcr_target = [v if isinstance(v, V1p5PCRTarget) else V1p5PCRTarget(**as_dict(v)) for v in self.V1p5pcr_target]

        if self.V1p5complete_sequences is not None and not isinstance(self.V1p5complete_sequences, V1p5CompleteSequences):
            self.V1p5complete_sequences = V1p5CompleteSequences(self.V1p5complete_sequences)

        if self.V1p5physical_linkage is not None and not isinstance(self.V1p5physical_linkage, V1p5PhysicalLinkage):
            self.V1p5physical_linkage = V1p5PhysicalLinkage(self.V1p5physical_linkage)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5SequencingRun(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5SequencingRun"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5SequencingRun"
    class_name: ClassVar[str] = "V1p5SequencingRun"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5SequencingRun

    V1p5sequencing_run_id: Optional[str] = None
    V1p5total_reads_passing_qc_filter: Optional[int] = None
    V1p5sequencing_platform: Optional[str] = None
    V1p5sequencing_facility: Optional[str] = None
    V1p5sequencing_run_date: Optional[Union[str, XSDDateTime]] = None
    V1p5sequencing_kit: Optional[str] = None
    V1p5sequencing_files: Optional[Union[dict, "V1p5SequencingData"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5sequencing_run_id is not None and not isinstance(self.V1p5sequencing_run_id, str):
            self.V1p5sequencing_run_id = str(self.V1p5sequencing_run_id)

        if self.V1p5total_reads_passing_qc_filter is not None and not isinstance(self.V1p5total_reads_passing_qc_filter, int):
            self.V1p5total_reads_passing_qc_filter = int(self.V1p5total_reads_passing_qc_filter)

        if self.V1p5sequencing_platform is not None and not isinstance(self.V1p5sequencing_platform, str):
            self.V1p5sequencing_platform = str(self.V1p5sequencing_platform)

        if self.V1p5sequencing_facility is not None and not isinstance(self.V1p5sequencing_facility, str):
            self.V1p5sequencing_facility = str(self.V1p5sequencing_facility)

        if self.V1p5sequencing_run_date is not None and not isinstance(self.V1p5sequencing_run_date, XSDDateTime):
            self.V1p5sequencing_run_date = XSDDateTime(self.V1p5sequencing_run_date)

        if self.V1p5sequencing_kit is not None and not isinstance(self.V1p5sequencing_kit, str):
            self.V1p5sequencing_kit = str(self.V1p5sequencing_kit)

        if self.V1p5sequencing_files is not None and not isinstance(self.V1p5sequencing_files, V1p5SequencingData):
            self.V1p5sequencing_files = V1p5SequencingData(**as_dict(self.V1p5sequencing_files))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5SequencingData(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5SequencingData"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5SequencingData"
    class_name: ClassVar[str] = "V1p5SequencingData"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5SequencingData

    V1p5sequencing_data_id: Optional[str] = None
    V1p5file_type: Optional[Union[str, "V1p5FileType"]] = None
    V1p5filename: Optional[str] = None
    V1p5read_direction: Optional[Union[str, "V1p5ReadDirection"]] = None
    V1p5read_length: Optional[int] = None
    V1p5paired_filename: Optional[str] = None
    V1p5paired_read_direction: Optional[Union[str, "V1p5PairedReadDirection"]] = None
    V1p5paired_read_length: Optional[int] = None
    V1p5index_filename: Optional[str] = None
    V1p5index_length: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5sequencing_data_id is not None and not isinstance(self.V1p5sequencing_data_id, str):
            self.V1p5sequencing_data_id = str(self.V1p5sequencing_data_id)

        if self.V1p5file_type is not None and not isinstance(self.V1p5file_type, V1p5FileType):
            self.V1p5file_type = V1p5FileType(self.V1p5file_type)

        if self.V1p5filename is not None and not isinstance(self.V1p5filename, str):
            self.V1p5filename = str(self.V1p5filename)

        if self.V1p5read_direction is not None and not isinstance(self.V1p5read_direction, V1p5ReadDirection):
            self.V1p5read_direction = V1p5ReadDirection(self.V1p5read_direction)

        if self.V1p5read_length is not None and not isinstance(self.V1p5read_length, int):
            self.V1p5read_length = int(self.V1p5read_length)

        if self.V1p5paired_filename is not None and not isinstance(self.V1p5paired_filename, str):
            self.V1p5paired_filename = str(self.V1p5paired_filename)

        if self.V1p5paired_read_direction is not None and not isinstance(self.V1p5paired_read_direction, V1p5PairedReadDirection):
            self.V1p5paired_read_direction = V1p5PairedReadDirection(self.V1p5paired_read_direction)

        if self.V1p5paired_read_length is not None and not isinstance(self.V1p5paired_read_length, int):
            self.V1p5paired_read_length = int(self.V1p5paired_read_length)

        if self.V1p5index_filename is not None and not isinstance(self.V1p5index_filename, str):
            self.V1p5index_filename = str(self.V1p5index_filename)

        if self.V1p5index_length is not None and not isinstance(self.V1p5index_length, int):
            self.V1p5index_length = int(self.V1p5index_length)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5DataProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5DataProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5DataProcessing"
    class_name: ClassVar[str] = "V1p5DataProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5DataProcessing

    V1p5data_processing_id: Optional[str] = None
    V1p5primary_annotation: Optional[Union[bool, Bool]] = None
    V1p5software_versions: Optional[str] = None
    V1p5paired_reads_assembly: Optional[str] = None
    V1p5quality_thresholds: Optional[str] = None
    V1p5primer_match_cutoffs: Optional[str] = None
    V1p5collapsing_method: Optional[str] = None
    V1p5data_processing_protocols: Optional[str] = None
    V1p5data_processing_files: Optional[Union[str, List[str]]] = empty_list()
    V1p5germline_database: Optional[str] = None
    V1p5germline_set_ref: Optional[str] = None
    V1p5analysis_provenance_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5data_processing_id is not None and not isinstance(self.V1p5data_processing_id, str):
            self.V1p5data_processing_id = str(self.V1p5data_processing_id)

        if self.V1p5primary_annotation is not None and not isinstance(self.V1p5primary_annotation, Bool):
            self.V1p5primary_annotation = Bool(self.V1p5primary_annotation)

        if self.V1p5software_versions is not None and not isinstance(self.V1p5software_versions, str):
            self.V1p5software_versions = str(self.V1p5software_versions)

        if self.V1p5paired_reads_assembly is not None and not isinstance(self.V1p5paired_reads_assembly, str):
            self.V1p5paired_reads_assembly = str(self.V1p5paired_reads_assembly)

        if self.V1p5quality_thresholds is not None and not isinstance(self.V1p5quality_thresholds, str):
            self.V1p5quality_thresholds = str(self.V1p5quality_thresholds)

        if self.V1p5primer_match_cutoffs is not None and not isinstance(self.V1p5primer_match_cutoffs, str):
            self.V1p5primer_match_cutoffs = str(self.V1p5primer_match_cutoffs)

        if self.V1p5collapsing_method is not None and not isinstance(self.V1p5collapsing_method, str):
            self.V1p5collapsing_method = str(self.V1p5collapsing_method)

        if self.V1p5data_processing_protocols is not None and not isinstance(self.V1p5data_processing_protocols, str):
            self.V1p5data_processing_protocols = str(self.V1p5data_processing_protocols)

        if not isinstance(self.V1p5data_processing_files, list):
            self.V1p5data_processing_files = [self.V1p5data_processing_files] if self.V1p5data_processing_files is not None else []
        self.V1p5data_processing_files = [v if isinstance(v, str) else str(v) for v in self.V1p5data_processing_files]

        if self.V1p5germline_database is not None and not isinstance(self.V1p5germline_database, str):
            self.V1p5germline_database = str(self.V1p5germline_database)

        if self.V1p5germline_set_ref is not None and not isinstance(self.V1p5germline_set_ref, str):
            self.V1p5germline_set_ref = str(self.V1p5germline_set_ref)

        if self.V1p5analysis_provenance_id is not None and not isinstance(self.V1p5analysis_provenance_id, str):
            self.V1p5analysis_provenance_id = str(self.V1p5analysis_provenance_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Repertoire(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Repertoire"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Repertoire"
    class_name: ClassVar[str] = "V1p5Repertoire"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Repertoire

    V1p5repertoire_id: Optional[str] = None
    V1p5repertoire_name: Optional[str] = None
    V1p5repertoire_description: Optional[str] = None
    V1p5study: Optional[Union[dict, V1p5Study]] = None
    V1p5subject: Optional[Union[dict, V1p5Subject]] = None
    V1p5sample: Optional[Union[Union[dict, "V1p5SampleProcessing"], List[Union[dict, "V1p5SampleProcessing"]]]] = empty_list()
    V1p5data_processing: Optional[Union[Union[dict, V1p5DataProcessing], List[Union[dict, V1p5DataProcessing]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5repertoire_id is not None and not isinstance(self.V1p5repertoire_id, str):
            self.V1p5repertoire_id = str(self.V1p5repertoire_id)

        if self.V1p5repertoire_name is not None and not isinstance(self.V1p5repertoire_name, str):
            self.V1p5repertoire_name = str(self.V1p5repertoire_name)

        if self.V1p5repertoire_description is not None and not isinstance(self.V1p5repertoire_description, str):
            self.V1p5repertoire_description = str(self.V1p5repertoire_description)

        if self.V1p5study is not None and not isinstance(self.V1p5study, V1p5Study):
            self.V1p5study = V1p5Study(**as_dict(self.V1p5study))

        if self.V1p5subject is not None and not isinstance(self.V1p5subject, V1p5Subject):
            self.V1p5subject = V1p5Subject(**as_dict(self.V1p5subject))

        if not isinstance(self.V1p5sample, list):
            self.V1p5sample = [self.V1p5sample] if self.V1p5sample is not None else []
        self.V1p5sample = [v if isinstance(v, V1p5SampleProcessing) else V1p5SampleProcessing(**as_dict(v)) for v in self.V1p5sample]

        if not isinstance(self.V1p5data_processing, list):
            self.V1p5data_processing = [self.V1p5data_processing] if self.V1p5data_processing is not None else []
        self.V1p5data_processing = [v if isinstance(v, V1p5DataProcessing) else V1p5DataProcessing(**as_dict(v)) for v in self.V1p5data_processing]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5RepertoireGroup(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5RepertoireGroup"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5RepertoireGroup"
    class_name: ClassVar[str] = "V1p5RepertoireGroup"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5RepertoireGroup

    V1p5repertoire_group_id: Optional[str] = None
    V1p5repertoire_group_name: Optional[str] = None
    V1p5repertoire_group_description: Optional[str] = None
    V1p5repertoires: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5repertoire_group_id is not None and not isinstance(self.V1p5repertoire_group_id, str):
            self.V1p5repertoire_group_id = str(self.V1p5repertoire_group_id)

        if self.V1p5repertoire_group_name is not None and not isinstance(self.V1p5repertoire_group_name, str):
            self.V1p5repertoire_group_name = str(self.V1p5repertoire_group_name)

        if self.V1p5repertoire_group_description is not None and not isinstance(self.V1p5repertoire_group_description, str):
            self.V1p5repertoire_group_description = str(self.V1p5repertoire_group_description)

        if not isinstance(self.V1p5repertoires, list):
            self.V1p5repertoires = [self.V1p5repertoires] if self.V1p5repertoires is not None else []
        self.V1p5repertoires = [v if isinstance(v, str) else str(v) for v in self.V1p5repertoires]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Alignment(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Alignment"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Alignment"
    class_name: ClassVar[str] = "V1p5Alignment"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Alignment

    V1p5sequence_id: Optional[str] = None
    V1p5segment: Optional[str] = None
    V1p5rev_comp: Optional[Union[bool, Bool]] = None
    V1p5call: Optional[str] = None
    V1p5score: Optional[float] = None
    V1p5identity: Optional[float] = None
    V1p5support: Optional[float] = None
    V1p5cigar: Optional[str] = None
    V1p5sequence_start: Optional[int] = None
    V1p5sequence_end: Optional[int] = None
    V1p5germline_start: Optional[int] = None
    V1p5germline_end: Optional[int] = None
    V1p5rank: Optional[int] = None
    V1p5data_processing_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5sequence_id is not None and not isinstance(self.V1p5sequence_id, str):
            self.V1p5sequence_id = str(self.V1p5sequence_id)

        if self.V1p5segment is not None and not isinstance(self.V1p5segment, str):
            self.V1p5segment = str(self.V1p5segment)

        if self.V1p5rev_comp is not None and not isinstance(self.V1p5rev_comp, Bool):
            self.V1p5rev_comp = Bool(self.V1p5rev_comp)

        if self.V1p5call is not None and not isinstance(self.V1p5call, str):
            self.V1p5call = str(self.V1p5call)

        if self.V1p5score is not None and not isinstance(self.V1p5score, float):
            self.V1p5score = float(self.V1p5score)

        if self.V1p5identity is not None and not isinstance(self.V1p5identity, float):
            self.V1p5identity = float(self.V1p5identity)

        if self.V1p5support is not None and not isinstance(self.V1p5support, float):
            self.V1p5support = float(self.V1p5support)

        if self.V1p5cigar is not None and not isinstance(self.V1p5cigar, str):
            self.V1p5cigar = str(self.V1p5cigar)

        if self.V1p5sequence_start is not None and not isinstance(self.V1p5sequence_start, int):
            self.V1p5sequence_start = int(self.V1p5sequence_start)

        if self.V1p5sequence_end is not None and not isinstance(self.V1p5sequence_end, int):
            self.V1p5sequence_end = int(self.V1p5sequence_end)

        if self.V1p5germline_start is not None and not isinstance(self.V1p5germline_start, int):
            self.V1p5germline_start = int(self.V1p5germline_start)

        if self.V1p5germline_end is not None and not isinstance(self.V1p5germline_end, int):
            self.V1p5germline_end = int(self.V1p5germline_end)

        if self.V1p5rank is not None and not isinstance(self.V1p5rank, int):
            self.V1p5rank = int(self.V1p5rank)

        if self.V1p5data_processing_id is not None and not isinstance(self.V1p5data_processing_id, str):
            self.V1p5data_processing_id = str(self.V1p5data_processing_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Rearrangement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Rearrangement"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Rearrangement"
    class_name: ClassVar[str] = "V1p5Rearrangement"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Rearrangement

    V1p5sequence_id: Optional[str] = None
    V1p5sequence: Optional[str] = None
    V1p5quality: Optional[str] = None
    V1p5sequence_aa: Optional[str] = None
    V1p5rev_comp: Optional[Union[bool, Bool]] = None
    V1p5productive: Optional[Union[bool, Bool]] = None
    V1p5vj_in_frame: Optional[Union[bool, Bool]] = None
    V1p5stop_codon: Optional[Union[bool, Bool]] = None
    V1p5complete_vdj: Optional[Union[bool, Bool]] = None
    V1p5locus: Optional[Union[str, "V1p5Locus"]] = None
    V1p5v_call: Optional[str] = None
    V1p5d_call: Optional[str] = None
    V1p5d2_call: Optional[str] = None
    V1p5j_call: Optional[str] = None
    V1p5c_call: Optional[str] = None
    V1p5sequence_alignment: Optional[str] = None
    V1p5quality_alignment: Optional[str] = None
    V1p5sequence_alignment_aa: Optional[str] = None
    V1p5germline_alignment: Optional[str] = None
    V1p5germline_alignment_aa: Optional[str] = None
    V1p5junction: Optional[str] = None
    V1p5junction_aa: Optional[str] = None
    V1p5np1: Optional[str] = None
    V1p5np1_aa: Optional[str] = None
    V1p5np2: Optional[str] = None
    V1p5np2_aa: Optional[str] = None
    V1p5np3: Optional[str] = None
    V1p5np3_aa: Optional[str] = None
    V1p5cdr1: Optional[str] = None
    V1p5cdr1_aa: Optional[str] = None
    V1p5cdr2: Optional[str] = None
    V1p5cdr2_aa: Optional[str] = None
    V1p5cdr3: Optional[str] = None
    V1p5cdr3_aa: Optional[str] = None
    V1p5fwr1: Optional[str] = None
    V1p5fwr1_aa: Optional[str] = None
    V1p5fwr2: Optional[str] = None
    V1p5fwr2_aa: Optional[str] = None
    V1p5fwr3: Optional[str] = None
    V1p5fwr3_aa: Optional[str] = None
    V1p5fwr4: Optional[str] = None
    V1p5fwr4_aa: Optional[str] = None
    V1p5v_score: Optional[float] = None
    V1p5v_identity: Optional[float] = None
    V1p5v_support: Optional[float] = None
    V1p5v_cigar: Optional[str] = None
    V1p5d_score: Optional[float] = None
    V1p5d_identity: Optional[float] = None
    V1p5d_support: Optional[float] = None
    V1p5d_cigar: Optional[str] = None
    V1p5d2_score: Optional[float] = None
    V1p5d2_identity: Optional[float] = None
    V1p5d2_support: Optional[float] = None
    V1p5d2_cigar: Optional[str] = None
    V1p5j_score: Optional[float] = None
    V1p5j_identity: Optional[float] = None
    V1p5j_support: Optional[float] = None
    V1p5j_cigar: Optional[str] = None
    V1p5c_score: Optional[float] = None
    V1p5c_identity: Optional[float] = None
    V1p5c_support: Optional[float] = None
    V1p5c_cigar: Optional[str] = None
    V1p5v_sequence_start: Optional[int] = None
    V1p5v_sequence_end: Optional[int] = None
    V1p5v_germline_start: Optional[int] = None
    V1p5v_germline_end: Optional[int] = None
    V1p5v_alignment_start: Optional[int] = None
    V1p5v_alignment_end: Optional[int] = None
    V1p5d_sequence_start: Optional[int] = None
    V1p5d_sequence_end: Optional[int] = None
    V1p5d_germline_start: Optional[int] = None
    V1p5d_germline_end: Optional[int] = None
    V1p5d_alignment_start: Optional[int] = None
    V1p5d_alignment_end: Optional[int] = None
    V1p5d2_sequence_start: Optional[int] = None
    V1p5d2_sequence_end: Optional[int] = None
    V1p5d2_germline_start: Optional[int] = None
    V1p5d2_germline_end: Optional[int] = None
    V1p5d2_alignment_start: Optional[int] = None
    V1p5d2_alignment_end: Optional[int] = None
    V1p5j_sequence_start: Optional[int] = None
    V1p5j_sequence_end: Optional[int] = None
    V1p5j_germline_start: Optional[int] = None
    V1p5j_germline_end: Optional[int] = None
    V1p5j_alignment_start: Optional[int] = None
    V1p5j_alignment_end: Optional[int] = None
    V1p5c_sequence_start: Optional[int] = None
    V1p5c_sequence_end: Optional[int] = None
    V1p5c_germline_start: Optional[int] = None
    V1p5c_germline_end: Optional[int] = None
    V1p5c_alignment_start: Optional[int] = None
    V1p5c_alignment_end: Optional[int] = None
    V1p5cdr1_start: Optional[int] = None
    V1p5cdr1_end: Optional[int] = None
    V1p5cdr2_start: Optional[int] = None
    V1p5cdr2_end: Optional[int] = None
    V1p5cdr3_start: Optional[int] = None
    V1p5cdr3_end: Optional[int] = None
    V1p5fwr1_start: Optional[int] = None
    V1p5fwr1_end: Optional[int] = None
    V1p5fwr2_start: Optional[int] = None
    V1p5fwr2_end: Optional[int] = None
    V1p5fwr3_start: Optional[int] = None
    V1p5fwr3_end: Optional[int] = None
    V1p5fwr4_start: Optional[int] = None
    V1p5fwr4_end: Optional[int] = None
    V1p5v_sequence_alignment: Optional[str] = None
    V1p5v_sequence_alignment_aa: Optional[str] = None
    V1p5d_sequence_alignment: Optional[str] = None
    V1p5d_sequence_alignment_aa: Optional[str] = None
    V1p5d2_sequence_alignment: Optional[str] = None
    V1p5d2_sequence_alignment_aa: Optional[str] = None
    V1p5j_sequence_alignment: Optional[str] = None
    V1p5j_sequence_alignment_aa: Optional[str] = None
    V1p5c_sequence_alignment: Optional[str] = None
    V1p5c_sequence_alignment_aa: Optional[str] = None
    V1p5v_germline_alignment: Optional[str] = None
    V1p5v_germline_alignment_aa: Optional[str] = None
    V1p5d_germline_alignment: Optional[str] = None
    V1p5d_germline_alignment_aa: Optional[str] = None
    V1p5d2_germline_alignment: Optional[str] = None
    V1p5d2_germline_alignment_aa: Optional[str] = None
    V1p5j_germline_alignment: Optional[str] = None
    V1p5j_germline_alignment_aa: Optional[str] = None
    V1p5c_germline_alignment: Optional[str] = None
    V1p5c_germline_alignment_aa: Optional[str] = None
    V1p5junction_length: Optional[int] = None
    V1p5junction_aa_length: Optional[int] = None
    V1p5np1_length: Optional[int] = None
    V1p5np2_length: Optional[int] = None
    V1p5np3_length: Optional[int] = None
    V1p5n1_length: Optional[int] = None
    V1p5n2_length: Optional[int] = None
    V1p5n3_length: Optional[int] = None
    V1p5p3v_length: Optional[int] = None
    V1p5p5d_length: Optional[int] = None
    V1p5p3d_length: Optional[int] = None
    V1p5p5d2_length: Optional[int] = None
    V1p5p3d2_length: Optional[int] = None
    V1p5p5j_length: Optional[int] = None
    V1p5v_frameshift: Optional[Union[bool, Bool]] = None
    V1p5j_frameshift: Optional[Union[bool, Bool]] = None
    V1p5d_frame: Optional[int] = None
    V1p5d2_frame: Optional[int] = None
    V1p5consensus_count: Optional[int] = None
    V1p5duplicate_count: Optional[int] = None
    V1p5umi_count: Optional[int] = None
    V1p5cell_id: Optional[str] = None
    V1p5clone_id: Optional[str] = None
    V1p5repertoire_id: Optional[str] = None
    V1p5sample_processing_id: Optional[str] = None
    V1p5data_processing_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5sequence_id is not None and not isinstance(self.V1p5sequence_id, str):
            self.V1p5sequence_id = str(self.V1p5sequence_id)

        if self.V1p5sequence is not None and not isinstance(self.V1p5sequence, str):
            self.V1p5sequence = str(self.V1p5sequence)

        if self.V1p5quality is not None and not isinstance(self.V1p5quality, str):
            self.V1p5quality = str(self.V1p5quality)

        if self.V1p5sequence_aa is not None and not isinstance(self.V1p5sequence_aa, str):
            self.V1p5sequence_aa = str(self.V1p5sequence_aa)

        if self.V1p5rev_comp is not None and not isinstance(self.V1p5rev_comp, Bool):
            self.V1p5rev_comp = Bool(self.V1p5rev_comp)

        if self.V1p5productive is not None and not isinstance(self.V1p5productive, Bool):
            self.V1p5productive = Bool(self.V1p5productive)

        if self.V1p5vj_in_frame is not None and not isinstance(self.V1p5vj_in_frame, Bool):
            self.V1p5vj_in_frame = Bool(self.V1p5vj_in_frame)

        if self.V1p5stop_codon is not None and not isinstance(self.V1p5stop_codon, Bool):
            self.V1p5stop_codon = Bool(self.V1p5stop_codon)

        if self.V1p5complete_vdj is not None and not isinstance(self.V1p5complete_vdj, Bool):
            self.V1p5complete_vdj = Bool(self.V1p5complete_vdj)

        if self.V1p5locus is not None and not isinstance(self.V1p5locus, V1p5Locus):
            self.V1p5locus = V1p5Locus(self.V1p5locus)

        if self.V1p5v_call is not None and not isinstance(self.V1p5v_call, str):
            self.V1p5v_call = str(self.V1p5v_call)

        if self.V1p5d_call is not None and not isinstance(self.V1p5d_call, str):
            self.V1p5d_call = str(self.V1p5d_call)

        if self.V1p5d2_call is not None and not isinstance(self.V1p5d2_call, str):
            self.V1p5d2_call = str(self.V1p5d2_call)

        if self.V1p5j_call is not None and not isinstance(self.V1p5j_call, str):
            self.V1p5j_call = str(self.V1p5j_call)

        if self.V1p5c_call is not None and not isinstance(self.V1p5c_call, str):
            self.V1p5c_call = str(self.V1p5c_call)

        if self.V1p5sequence_alignment is not None and not isinstance(self.V1p5sequence_alignment, str):
            self.V1p5sequence_alignment = str(self.V1p5sequence_alignment)

        if self.V1p5quality_alignment is not None and not isinstance(self.V1p5quality_alignment, str):
            self.V1p5quality_alignment = str(self.V1p5quality_alignment)

        if self.V1p5sequence_alignment_aa is not None and not isinstance(self.V1p5sequence_alignment_aa, str):
            self.V1p5sequence_alignment_aa = str(self.V1p5sequence_alignment_aa)

        if self.V1p5germline_alignment is not None and not isinstance(self.V1p5germline_alignment, str):
            self.V1p5germline_alignment = str(self.V1p5germline_alignment)

        if self.V1p5germline_alignment_aa is not None and not isinstance(self.V1p5germline_alignment_aa, str):
            self.V1p5germline_alignment_aa = str(self.V1p5germline_alignment_aa)

        if self.V1p5junction is not None and not isinstance(self.V1p5junction, str):
            self.V1p5junction = str(self.V1p5junction)

        if self.V1p5junction_aa is not None and not isinstance(self.V1p5junction_aa, str):
            self.V1p5junction_aa = str(self.V1p5junction_aa)

        if self.V1p5np1 is not None and not isinstance(self.V1p5np1, str):
            self.V1p5np1 = str(self.V1p5np1)

        if self.V1p5np1_aa is not None and not isinstance(self.V1p5np1_aa, str):
            self.V1p5np1_aa = str(self.V1p5np1_aa)

        if self.V1p5np2 is not None and not isinstance(self.V1p5np2, str):
            self.V1p5np2 = str(self.V1p5np2)

        if self.V1p5np2_aa is not None and not isinstance(self.V1p5np2_aa, str):
            self.V1p5np2_aa = str(self.V1p5np2_aa)

        if self.V1p5np3 is not None and not isinstance(self.V1p5np3, str):
            self.V1p5np3 = str(self.V1p5np3)

        if self.V1p5np3_aa is not None and not isinstance(self.V1p5np3_aa, str):
            self.V1p5np3_aa = str(self.V1p5np3_aa)

        if self.V1p5cdr1 is not None and not isinstance(self.V1p5cdr1, str):
            self.V1p5cdr1 = str(self.V1p5cdr1)

        if self.V1p5cdr1_aa is not None and not isinstance(self.V1p5cdr1_aa, str):
            self.V1p5cdr1_aa = str(self.V1p5cdr1_aa)

        if self.V1p5cdr2 is not None and not isinstance(self.V1p5cdr2, str):
            self.V1p5cdr2 = str(self.V1p5cdr2)

        if self.V1p5cdr2_aa is not None and not isinstance(self.V1p5cdr2_aa, str):
            self.V1p5cdr2_aa = str(self.V1p5cdr2_aa)

        if self.V1p5cdr3 is not None and not isinstance(self.V1p5cdr3, str):
            self.V1p5cdr3 = str(self.V1p5cdr3)

        if self.V1p5cdr3_aa is not None and not isinstance(self.V1p5cdr3_aa, str):
            self.V1p5cdr3_aa = str(self.V1p5cdr3_aa)

        if self.V1p5fwr1 is not None and not isinstance(self.V1p5fwr1, str):
            self.V1p5fwr1 = str(self.V1p5fwr1)

        if self.V1p5fwr1_aa is not None and not isinstance(self.V1p5fwr1_aa, str):
            self.V1p5fwr1_aa = str(self.V1p5fwr1_aa)

        if self.V1p5fwr2 is not None and not isinstance(self.V1p5fwr2, str):
            self.V1p5fwr2 = str(self.V1p5fwr2)

        if self.V1p5fwr2_aa is not None and not isinstance(self.V1p5fwr2_aa, str):
            self.V1p5fwr2_aa = str(self.V1p5fwr2_aa)

        if self.V1p5fwr3 is not None and not isinstance(self.V1p5fwr3, str):
            self.V1p5fwr3 = str(self.V1p5fwr3)

        if self.V1p5fwr3_aa is not None and not isinstance(self.V1p5fwr3_aa, str):
            self.V1p5fwr3_aa = str(self.V1p5fwr3_aa)

        if self.V1p5fwr4 is not None and not isinstance(self.V1p5fwr4, str):
            self.V1p5fwr4 = str(self.V1p5fwr4)

        if self.V1p5fwr4_aa is not None and not isinstance(self.V1p5fwr4_aa, str):
            self.V1p5fwr4_aa = str(self.V1p5fwr4_aa)

        if self.V1p5v_score is not None and not isinstance(self.V1p5v_score, float):
            self.V1p5v_score = float(self.V1p5v_score)

        if self.V1p5v_identity is not None and not isinstance(self.V1p5v_identity, float):
            self.V1p5v_identity = float(self.V1p5v_identity)

        if self.V1p5v_support is not None and not isinstance(self.V1p5v_support, float):
            self.V1p5v_support = float(self.V1p5v_support)

        if self.V1p5v_cigar is not None and not isinstance(self.V1p5v_cigar, str):
            self.V1p5v_cigar = str(self.V1p5v_cigar)

        if self.V1p5d_score is not None and not isinstance(self.V1p5d_score, float):
            self.V1p5d_score = float(self.V1p5d_score)

        if self.V1p5d_identity is not None and not isinstance(self.V1p5d_identity, float):
            self.V1p5d_identity = float(self.V1p5d_identity)

        if self.V1p5d_support is not None and not isinstance(self.V1p5d_support, float):
            self.V1p5d_support = float(self.V1p5d_support)

        if self.V1p5d_cigar is not None and not isinstance(self.V1p5d_cigar, str):
            self.V1p5d_cigar = str(self.V1p5d_cigar)

        if self.V1p5d2_score is not None and not isinstance(self.V1p5d2_score, float):
            self.V1p5d2_score = float(self.V1p5d2_score)

        if self.V1p5d2_identity is not None and not isinstance(self.V1p5d2_identity, float):
            self.V1p5d2_identity = float(self.V1p5d2_identity)

        if self.V1p5d2_support is not None and not isinstance(self.V1p5d2_support, float):
            self.V1p5d2_support = float(self.V1p5d2_support)

        if self.V1p5d2_cigar is not None and not isinstance(self.V1p5d2_cigar, str):
            self.V1p5d2_cigar = str(self.V1p5d2_cigar)

        if self.V1p5j_score is not None and not isinstance(self.V1p5j_score, float):
            self.V1p5j_score = float(self.V1p5j_score)

        if self.V1p5j_identity is not None and not isinstance(self.V1p5j_identity, float):
            self.V1p5j_identity = float(self.V1p5j_identity)

        if self.V1p5j_support is not None and not isinstance(self.V1p5j_support, float):
            self.V1p5j_support = float(self.V1p5j_support)

        if self.V1p5j_cigar is not None and not isinstance(self.V1p5j_cigar, str):
            self.V1p5j_cigar = str(self.V1p5j_cigar)

        if self.V1p5c_score is not None and not isinstance(self.V1p5c_score, float):
            self.V1p5c_score = float(self.V1p5c_score)

        if self.V1p5c_identity is not None and not isinstance(self.V1p5c_identity, float):
            self.V1p5c_identity = float(self.V1p5c_identity)

        if self.V1p5c_support is not None and not isinstance(self.V1p5c_support, float):
            self.V1p5c_support = float(self.V1p5c_support)

        if self.V1p5c_cigar is not None and not isinstance(self.V1p5c_cigar, str):
            self.V1p5c_cigar = str(self.V1p5c_cigar)

        if self.V1p5v_sequence_start is not None and not isinstance(self.V1p5v_sequence_start, int):
            self.V1p5v_sequence_start = int(self.V1p5v_sequence_start)

        if self.V1p5v_sequence_end is not None and not isinstance(self.V1p5v_sequence_end, int):
            self.V1p5v_sequence_end = int(self.V1p5v_sequence_end)

        if self.V1p5v_germline_start is not None and not isinstance(self.V1p5v_germline_start, int):
            self.V1p5v_germline_start = int(self.V1p5v_germline_start)

        if self.V1p5v_germline_end is not None and not isinstance(self.V1p5v_germline_end, int):
            self.V1p5v_germline_end = int(self.V1p5v_germline_end)

        if self.V1p5v_alignment_start is not None and not isinstance(self.V1p5v_alignment_start, int):
            self.V1p5v_alignment_start = int(self.V1p5v_alignment_start)

        if self.V1p5v_alignment_end is not None and not isinstance(self.V1p5v_alignment_end, int):
            self.V1p5v_alignment_end = int(self.V1p5v_alignment_end)

        if self.V1p5d_sequence_start is not None and not isinstance(self.V1p5d_sequence_start, int):
            self.V1p5d_sequence_start = int(self.V1p5d_sequence_start)

        if self.V1p5d_sequence_end is not None and not isinstance(self.V1p5d_sequence_end, int):
            self.V1p5d_sequence_end = int(self.V1p5d_sequence_end)

        if self.V1p5d_germline_start is not None and not isinstance(self.V1p5d_germline_start, int):
            self.V1p5d_germline_start = int(self.V1p5d_germline_start)

        if self.V1p5d_germline_end is not None and not isinstance(self.V1p5d_germline_end, int):
            self.V1p5d_germline_end = int(self.V1p5d_germline_end)

        if self.V1p5d_alignment_start is not None and not isinstance(self.V1p5d_alignment_start, int):
            self.V1p5d_alignment_start = int(self.V1p5d_alignment_start)

        if self.V1p5d_alignment_end is not None and not isinstance(self.V1p5d_alignment_end, int):
            self.V1p5d_alignment_end = int(self.V1p5d_alignment_end)

        if self.V1p5d2_sequence_start is not None and not isinstance(self.V1p5d2_sequence_start, int):
            self.V1p5d2_sequence_start = int(self.V1p5d2_sequence_start)

        if self.V1p5d2_sequence_end is not None and not isinstance(self.V1p5d2_sequence_end, int):
            self.V1p5d2_sequence_end = int(self.V1p5d2_sequence_end)

        if self.V1p5d2_germline_start is not None and not isinstance(self.V1p5d2_germline_start, int):
            self.V1p5d2_germline_start = int(self.V1p5d2_germline_start)

        if self.V1p5d2_germline_end is not None and not isinstance(self.V1p5d2_germline_end, int):
            self.V1p5d2_germline_end = int(self.V1p5d2_germline_end)

        if self.V1p5d2_alignment_start is not None and not isinstance(self.V1p5d2_alignment_start, int):
            self.V1p5d2_alignment_start = int(self.V1p5d2_alignment_start)

        if self.V1p5d2_alignment_end is not None and not isinstance(self.V1p5d2_alignment_end, int):
            self.V1p5d2_alignment_end = int(self.V1p5d2_alignment_end)

        if self.V1p5j_sequence_start is not None and not isinstance(self.V1p5j_sequence_start, int):
            self.V1p5j_sequence_start = int(self.V1p5j_sequence_start)

        if self.V1p5j_sequence_end is not None and not isinstance(self.V1p5j_sequence_end, int):
            self.V1p5j_sequence_end = int(self.V1p5j_sequence_end)

        if self.V1p5j_germline_start is not None and not isinstance(self.V1p5j_germline_start, int):
            self.V1p5j_germline_start = int(self.V1p5j_germline_start)

        if self.V1p5j_germline_end is not None and not isinstance(self.V1p5j_germline_end, int):
            self.V1p5j_germline_end = int(self.V1p5j_germline_end)

        if self.V1p5j_alignment_start is not None and not isinstance(self.V1p5j_alignment_start, int):
            self.V1p5j_alignment_start = int(self.V1p5j_alignment_start)

        if self.V1p5j_alignment_end is not None and not isinstance(self.V1p5j_alignment_end, int):
            self.V1p5j_alignment_end = int(self.V1p5j_alignment_end)

        if self.V1p5c_sequence_start is not None and not isinstance(self.V1p5c_sequence_start, int):
            self.V1p5c_sequence_start = int(self.V1p5c_sequence_start)

        if self.V1p5c_sequence_end is not None and not isinstance(self.V1p5c_sequence_end, int):
            self.V1p5c_sequence_end = int(self.V1p5c_sequence_end)

        if self.V1p5c_germline_start is not None and not isinstance(self.V1p5c_germline_start, int):
            self.V1p5c_germline_start = int(self.V1p5c_germline_start)

        if self.V1p5c_germline_end is not None and not isinstance(self.V1p5c_germline_end, int):
            self.V1p5c_germline_end = int(self.V1p5c_germline_end)

        if self.V1p5c_alignment_start is not None and not isinstance(self.V1p5c_alignment_start, int):
            self.V1p5c_alignment_start = int(self.V1p5c_alignment_start)

        if self.V1p5c_alignment_end is not None and not isinstance(self.V1p5c_alignment_end, int):
            self.V1p5c_alignment_end = int(self.V1p5c_alignment_end)

        if self.V1p5cdr1_start is not None and not isinstance(self.V1p5cdr1_start, int):
            self.V1p5cdr1_start = int(self.V1p5cdr1_start)

        if self.V1p5cdr1_end is not None and not isinstance(self.V1p5cdr1_end, int):
            self.V1p5cdr1_end = int(self.V1p5cdr1_end)

        if self.V1p5cdr2_start is not None and not isinstance(self.V1p5cdr2_start, int):
            self.V1p5cdr2_start = int(self.V1p5cdr2_start)

        if self.V1p5cdr2_end is not None and not isinstance(self.V1p5cdr2_end, int):
            self.V1p5cdr2_end = int(self.V1p5cdr2_end)

        if self.V1p5cdr3_start is not None and not isinstance(self.V1p5cdr3_start, int):
            self.V1p5cdr3_start = int(self.V1p5cdr3_start)

        if self.V1p5cdr3_end is not None and not isinstance(self.V1p5cdr3_end, int):
            self.V1p5cdr3_end = int(self.V1p5cdr3_end)

        if self.V1p5fwr1_start is not None and not isinstance(self.V1p5fwr1_start, int):
            self.V1p5fwr1_start = int(self.V1p5fwr1_start)

        if self.V1p5fwr1_end is not None and not isinstance(self.V1p5fwr1_end, int):
            self.V1p5fwr1_end = int(self.V1p5fwr1_end)

        if self.V1p5fwr2_start is not None and not isinstance(self.V1p5fwr2_start, int):
            self.V1p5fwr2_start = int(self.V1p5fwr2_start)

        if self.V1p5fwr2_end is not None and not isinstance(self.V1p5fwr2_end, int):
            self.V1p5fwr2_end = int(self.V1p5fwr2_end)

        if self.V1p5fwr3_start is not None and not isinstance(self.V1p5fwr3_start, int):
            self.V1p5fwr3_start = int(self.V1p5fwr3_start)

        if self.V1p5fwr3_end is not None and not isinstance(self.V1p5fwr3_end, int):
            self.V1p5fwr3_end = int(self.V1p5fwr3_end)

        if self.V1p5fwr4_start is not None and not isinstance(self.V1p5fwr4_start, int):
            self.V1p5fwr4_start = int(self.V1p5fwr4_start)

        if self.V1p5fwr4_end is not None and not isinstance(self.V1p5fwr4_end, int):
            self.V1p5fwr4_end = int(self.V1p5fwr4_end)

        if self.V1p5v_sequence_alignment is not None and not isinstance(self.V1p5v_sequence_alignment, str):
            self.V1p5v_sequence_alignment = str(self.V1p5v_sequence_alignment)

        if self.V1p5v_sequence_alignment_aa is not None and not isinstance(self.V1p5v_sequence_alignment_aa, str):
            self.V1p5v_sequence_alignment_aa = str(self.V1p5v_sequence_alignment_aa)

        if self.V1p5d_sequence_alignment is not None and not isinstance(self.V1p5d_sequence_alignment, str):
            self.V1p5d_sequence_alignment = str(self.V1p5d_sequence_alignment)

        if self.V1p5d_sequence_alignment_aa is not None and not isinstance(self.V1p5d_sequence_alignment_aa, str):
            self.V1p5d_sequence_alignment_aa = str(self.V1p5d_sequence_alignment_aa)

        if self.V1p5d2_sequence_alignment is not None and not isinstance(self.V1p5d2_sequence_alignment, str):
            self.V1p5d2_sequence_alignment = str(self.V1p5d2_sequence_alignment)

        if self.V1p5d2_sequence_alignment_aa is not None and not isinstance(self.V1p5d2_sequence_alignment_aa, str):
            self.V1p5d2_sequence_alignment_aa = str(self.V1p5d2_sequence_alignment_aa)

        if self.V1p5j_sequence_alignment is not None and not isinstance(self.V1p5j_sequence_alignment, str):
            self.V1p5j_sequence_alignment = str(self.V1p5j_sequence_alignment)

        if self.V1p5j_sequence_alignment_aa is not None and not isinstance(self.V1p5j_sequence_alignment_aa, str):
            self.V1p5j_sequence_alignment_aa = str(self.V1p5j_sequence_alignment_aa)

        if self.V1p5c_sequence_alignment is not None and not isinstance(self.V1p5c_sequence_alignment, str):
            self.V1p5c_sequence_alignment = str(self.V1p5c_sequence_alignment)

        if self.V1p5c_sequence_alignment_aa is not None and not isinstance(self.V1p5c_sequence_alignment_aa, str):
            self.V1p5c_sequence_alignment_aa = str(self.V1p5c_sequence_alignment_aa)

        if self.V1p5v_germline_alignment is not None and not isinstance(self.V1p5v_germline_alignment, str):
            self.V1p5v_germline_alignment = str(self.V1p5v_germline_alignment)

        if self.V1p5v_germline_alignment_aa is not None and not isinstance(self.V1p5v_germline_alignment_aa, str):
            self.V1p5v_germline_alignment_aa = str(self.V1p5v_germline_alignment_aa)

        if self.V1p5d_germline_alignment is not None and not isinstance(self.V1p5d_germline_alignment, str):
            self.V1p5d_germline_alignment = str(self.V1p5d_germline_alignment)

        if self.V1p5d_germline_alignment_aa is not None and not isinstance(self.V1p5d_germline_alignment_aa, str):
            self.V1p5d_germline_alignment_aa = str(self.V1p5d_germline_alignment_aa)

        if self.V1p5d2_germline_alignment is not None and not isinstance(self.V1p5d2_germline_alignment, str):
            self.V1p5d2_germline_alignment = str(self.V1p5d2_germline_alignment)

        if self.V1p5d2_germline_alignment_aa is not None and not isinstance(self.V1p5d2_germline_alignment_aa, str):
            self.V1p5d2_germline_alignment_aa = str(self.V1p5d2_germline_alignment_aa)

        if self.V1p5j_germline_alignment is not None and not isinstance(self.V1p5j_germline_alignment, str):
            self.V1p5j_germline_alignment = str(self.V1p5j_germline_alignment)

        if self.V1p5j_germline_alignment_aa is not None and not isinstance(self.V1p5j_germline_alignment_aa, str):
            self.V1p5j_germline_alignment_aa = str(self.V1p5j_germline_alignment_aa)

        if self.V1p5c_germline_alignment is not None and not isinstance(self.V1p5c_germline_alignment, str):
            self.V1p5c_germline_alignment = str(self.V1p5c_germline_alignment)

        if self.V1p5c_germline_alignment_aa is not None and not isinstance(self.V1p5c_germline_alignment_aa, str):
            self.V1p5c_germline_alignment_aa = str(self.V1p5c_germline_alignment_aa)

        if self.V1p5junction_length is not None and not isinstance(self.V1p5junction_length, int):
            self.V1p5junction_length = int(self.V1p5junction_length)

        if self.V1p5junction_aa_length is not None and not isinstance(self.V1p5junction_aa_length, int):
            self.V1p5junction_aa_length = int(self.V1p5junction_aa_length)

        if self.V1p5np1_length is not None and not isinstance(self.V1p5np1_length, int):
            self.V1p5np1_length = int(self.V1p5np1_length)

        if self.V1p5np2_length is not None and not isinstance(self.V1p5np2_length, int):
            self.V1p5np2_length = int(self.V1p5np2_length)

        if self.V1p5np3_length is not None and not isinstance(self.V1p5np3_length, int):
            self.V1p5np3_length = int(self.V1p5np3_length)

        if self.V1p5n1_length is not None and not isinstance(self.V1p5n1_length, int):
            self.V1p5n1_length = int(self.V1p5n1_length)

        if self.V1p5n2_length is not None and not isinstance(self.V1p5n2_length, int):
            self.V1p5n2_length = int(self.V1p5n2_length)

        if self.V1p5n3_length is not None and not isinstance(self.V1p5n3_length, int):
            self.V1p5n3_length = int(self.V1p5n3_length)

        if self.V1p5p3v_length is not None and not isinstance(self.V1p5p3v_length, int):
            self.V1p5p3v_length = int(self.V1p5p3v_length)

        if self.V1p5p5d_length is not None and not isinstance(self.V1p5p5d_length, int):
            self.V1p5p5d_length = int(self.V1p5p5d_length)

        if self.V1p5p3d_length is not None and not isinstance(self.V1p5p3d_length, int):
            self.V1p5p3d_length = int(self.V1p5p3d_length)

        if self.V1p5p5d2_length is not None and not isinstance(self.V1p5p5d2_length, int):
            self.V1p5p5d2_length = int(self.V1p5p5d2_length)

        if self.V1p5p3d2_length is not None and not isinstance(self.V1p5p3d2_length, int):
            self.V1p5p3d2_length = int(self.V1p5p3d2_length)

        if self.V1p5p5j_length is not None and not isinstance(self.V1p5p5j_length, int):
            self.V1p5p5j_length = int(self.V1p5p5j_length)

        if self.V1p5v_frameshift is not None and not isinstance(self.V1p5v_frameshift, Bool):
            self.V1p5v_frameshift = Bool(self.V1p5v_frameshift)

        if self.V1p5j_frameshift is not None and not isinstance(self.V1p5j_frameshift, Bool):
            self.V1p5j_frameshift = Bool(self.V1p5j_frameshift)

        if self.V1p5d_frame is not None and not isinstance(self.V1p5d_frame, int):
            self.V1p5d_frame = int(self.V1p5d_frame)

        if self.V1p5d2_frame is not None and not isinstance(self.V1p5d2_frame, int):
            self.V1p5d2_frame = int(self.V1p5d2_frame)

        if self.V1p5consensus_count is not None and not isinstance(self.V1p5consensus_count, int):
            self.V1p5consensus_count = int(self.V1p5consensus_count)

        if self.V1p5duplicate_count is not None and not isinstance(self.V1p5duplicate_count, int):
            self.V1p5duplicate_count = int(self.V1p5duplicate_count)

        if self.V1p5umi_count is not None and not isinstance(self.V1p5umi_count, int):
            self.V1p5umi_count = int(self.V1p5umi_count)

        if self.V1p5cell_id is not None and not isinstance(self.V1p5cell_id, str):
            self.V1p5cell_id = str(self.V1p5cell_id)

        if self.V1p5clone_id is not None and not isinstance(self.V1p5clone_id, str):
            self.V1p5clone_id = str(self.V1p5clone_id)

        if self.V1p5repertoire_id is not None and not isinstance(self.V1p5repertoire_id, str):
            self.V1p5repertoire_id = str(self.V1p5repertoire_id)

        if self.V1p5sample_processing_id is not None and not isinstance(self.V1p5sample_processing_id, str):
            self.V1p5sample_processing_id = str(self.V1p5sample_processing_id)

        if self.V1p5data_processing_id is not None and not isinstance(self.V1p5data_processing_id, str):
            self.V1p5data_processing_id = str(self.V1p5data_processing_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Clone(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Clone"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Clone"
    class_name: ClassVar[str] = "V1p5Clone"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Clone

    V1p5clone_id: Optional[str] = None
    V1p5repertoire_id: Optional[str] = None
    V1p5data_processing_id: Optional[str] = None
    V1p5sequences: Optional[Union[str, List[str]]] = empty_list()
    V1p5v_call: Optional[str] = None
    V1p5d_call: Optional[str] = None
    V1p5j_call: Optional[str] = None
    V1p5junction: Optional[str] = None
    V1p5junction_aa: Optional[str] = None
    V1p5junction_length: Optional[int] = None
    V1p5junction_aa_length: Optional[int] = None
    V1p5germline_alignment: Optional[str] = None
    V1p5germline_alignment_aa: Optional[str] = None
    V1p5v_alignment_start: Optional[int] = None
    V1p5v_alignment_end: Optional[int] = None
    V1p5d_alignment_start: Optional[int] = None
    V1p5d_alignment_end: Optional[int] = None
    V1p5j_alignment_start: Optional[int] = None
    V1p5j_alignment_end: Optional[int] = None
    V1p5junction_start: Optional[int] = None
    V1p5junction_end: Optional[int] = None
    V1p5umi_count: Optional[int] = None
    V1p5clone_count: Optional[int] = None
    V1p5seed_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5clone_id is not None and not isinstance(self.V1p5clone_id, str):
            self.V1p5clone_id = str(self.V1p5clone_id)

        if self.V1p5repertoire_id is not None and not isinstance(self.V1p5repertoire_id, str):
            self.V1p5repertoire_id = str(self.V1p5repertoire_id)

        if self.V1p5data_processing_id is not None and not isinstance(self.V1p5data_processing_id, str):
            self.V1p5data_processing_id = str(self.V1p5data_processing_id)

        if not isinstance(self.V1p5sequences, list):
            self.V1p5sequences = [self.V1p5sequences] if self.V1p5sequences is not None else []
        self.V1p5sequences = [v if isinstance(v, str) else str(v) for v in self.V1p5sequences]

        if self.V1p5v_call is not None and not isinstance(self.V1p5v_call, str):
            self.V1p5v_call = str(self.V1p5v_call)

        if self.V1p5d_call is not None and not isinstance(self.V1p5d_call, str):
            self.V1p5d_call = str(self.V1p5d_call)

        if self.V1p5j_call is not None and not isinstance(self.V1p5j_call, str):
            self.V1p5j_call = str(self.V1p5j_call)

        if self.V1p5junction is not None and not isinstance(self.V1p5junction, str):
            self.V1p5junction = str(self.V1p5junction)

        if self.V1p5junction_aa is not None and not isinstance(self.V1p5junction_aa, str):
            self.V1p5junction_aa = str(self.V1p5junction_aa)

        if self.V1p5junction_length is not None and not isinstance(self.V1p5junction_length, int):
            self.V1p5junction_length = int(self.V1p5junction_length)

        if self.V1p5junction_aa_length is not None and not isinstance(self.V1p5junction_aa_length, int):
            self.V1p5junction_aa_length = int(self.V1p5junction_aa_length)

        if self.V1p5germline_alignment is not None and not isinstance(self.V1p5germline_alignment, str):
            self.V1p5germline_alignment = str(self.V1p5germline_alignment)

        if self.V1p5germline_alignment_aa is not None and not isinstance(self.V1p5germline_alignment_aa, str):
            self.V1p5germline_alignment_aa = str(self.V1p5germline_alignment_aa)

        if self.V1p5v_alignment_start is not None and not isinstance(self.V1p5v_alignment_start, int):
            self.V1p5v_alignment_start = int(self.V1p5v_alignment_start)

        if self.V1p5v_alignment_end is not None and not isinstance(self.V1p5v_alignment_end, int):
            self.V1p5v_alignment_end = int(self.V1p5v_alignment_end)

        if self.V1p5d_alignment_start is not None and not isinstance(self.V1p5d_alignment_start, int):
            self.V1p5d_alignment_start = int(self.V1p5d_alignment_start)

        if self.V1p5d_alignment_end is not None and not isinstance(self.V1p5d_alignment_end, int):
            self.V1p5d_alignment_end = int(self.V1p5d_alignment_end)

        if self.V1p5j_alignment_start is not None and not isinstance(self.V1p5j_alignment_start, int):
            self.V1p5j_alignment_start = int(self.V1p5j_alignment_start)

        if self.V1p5j_alignment_end is not None and not isinstance(self.V1p5j_alignment_end, int):
            self.V1p5j_alignment_end = int(self.V1p5j_alignment_end)

        if self.V1p5junction_start is not None and not isinstance(self.V1p5junction_start, int):
            self.V1p5junction_start = int(self.V1p5junction_start)

        if self.V1p5junction_end is not None and not isinstance(self.V1p5junction_end, int):
            self.V1p5junction_end = int(self.V1p5junction_end)

        if self.V1p5umi_count is not None and not isinstance(self.V1p5umi_count, int):
            self.V1p5umi_count = int(self.V1p5umi_count)

        if self.V1p5clone_count is not None and not isinstance(self.V1p5clone_count, int):
            self.V1p5clone_count = int(self.V1p5clone_count)

        if self.V1p5seed_id is not None and not isinstance(self.V1p5seed_id, str):
            self.V1p5seed_id = str(self.V1p5seed_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Tree(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Tree"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Tree"
    class_name: ClassVar[str] = "V1p5Tree"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Tree

    V1p5tree_id: Optional[str] = None
    V1p5clone_id: Optional[str] = None
    V1p5newick: Optional[str] = None
    V1p5nodes: Optional[Union[Union[dict, "V1p5Node"], List[Union[dict, "V1p5Node"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5tree_id is not None and not isinstance(self.V1p5tree_id, str):
            self.V1p5tree_id = str(self.V1p5tree_id)

        if self.V1p5clone_id is not None and not isinstance(self.V1p5clone_id, str):
            self.V1p5clone_id = str(self.V1p5clone_id)

        if self.V1p5newick is not None and not isinstance(self.V1p5newick, str):
            self.V1p5newick = str(self.V1p5newick)

        if not isinstance(self.V1p5nodes, list):
            self.V1p5nodes = [self.V1p5nodes] if self.V1p5nodes is not None else []
        self.V1p5nodes = [v if isinstance(v, V1p5Node) else V1p5Node(**as_dict(v)) for v in self.V1p5nodes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Node(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Node"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Node"
    class_name: ClassVar[str] = "V1p5Node"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Node

    V1p5sequence_id: Optional[str] = None
    V1p5sequence_alignment: Optional[str] = None
    V1p5junction: Optional[str] = None
    V1p5junction_aa: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5sequence_id is not None and not isinstance(self.V1p5sequence_id, str):
            self.V1p5sequence_id = str(self.V1p5sequence_id)

        if self.V1p5sequence_alignment is not None and not isinstance(self.V1p5sequence_alignment, str):
            self.V1p5sequence_alignment = str(self.V1p5sequence_alignment)

        if self.V1p5junction is not None and not isinstance(self.V1p5junction, str):
            self.V1p5junction = str(self.V1p5junction)

        if self.V1p5junction_aa is not None and not isinstance(self.V1p5junction_aa, str):
            self.V1p5junction_aa = str(self.V1p5junction_aa)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Cell(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Cell"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Cell"
    class_name: ClassVar[str] = "V1p5Cell"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Cell

    V1p5cell_id: Optional[str] = None
    V1p5rearrangements: Optional[Union[str, List[str]]] = empty_list()
    V1p5receptors: Optional[Union[str, List[str]]] = empty_list()
    V1p5repertoire_id: Optional[str] = None
    V1p5data_processing_id: Optional[str] = None
    V1p5expression_study_method: Optional[Union[str, "V1p5ExpressionStudyMethod"]] = None
    V1p5expression_raw_doi: Optional[str] = None
    V1p5expression_index: Optional[str] = None
    V1p5virtual_pairing: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5cell_id is not None and not isinstance(self.V1p5cell_id, str):
            self.V1p5cell_id = str(self.V1p5cell_id)

        if not isinstance(self.V1p5rearrangements, list):
            self.V1p5rearrangements = [self.V1p5rearrangements] if self.V1p5rearrangements is not None else []
        self.V1p5rearrangements = [v if isinstance(v, str) else str(v) for v in self.V1p5rearrangements]

        if not isinstance(self.V1p5receptors, list):
            self.V1p5receptors = [self.V1p5receptors] if self.V1p5receptors is not None else []
        self.V1p5receptors = [v if isinstance(v, str) else str(v) for v in self.V1p5receptors]

        if self.V1p5repertoire_id is not None and not isinstance(self.V1p5repertoire_id, str):
            self.V1p5repertoire_id = str(self.V1p5repertoire_id)

        if self.V1p5data_processing_id is not None and not isinstance(self.V1p5data_processing_id, str):
            self.V1p5data_processing_id = str(self.V1p5data_processing_id)

        if self.V1p5expression_study_method is not None and not isinstance(self.V1p5expression_study_method, V1p5ExpressionStudyMethod):
            self.V1p5expression_study_method = V1p5ExpressionStudyMethod(self.V1p5expression_study_method)

        if self.V1p5expression_raw_doi is not None and not isinstance(self.V1p5expression_raw_doi, str):
            self.V1p5expression_raw_doi = str(self.V1p5expression_raw_doi)

        if self.V1p5expression_index is not None and not isinstance(self.V1p5expression_index, str):
            self.V1p5expression_index = str(self.V1p5expression_index)

        if self.V1p5virtual_pairing is not None and not isinstance(self.V1p5virtual_pairing, Bool):
            self.V1p5virtual_pairing = Bool(self.V1p5virtual_pairing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5CellExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5CellExpression"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5CellExpression"
    class_name: ClassVar[str] = "V1p5CellExpression"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5CellExpression

    V1p5expression_id: Optional[str] = None
    V1p5cell_id: Optional[str] = None
    V1p5repertoire_id: Optional[str] = None
    V1p5data_processing_id: Optional[str] = None
    V1p5property_type: Optional[str] = None
    V1p5property: Optional[Union[str, "V1p5Property"]] = None
    V1p5value: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5expression_id is not None and not isinstance(self.V1p5expression_id, str):
            self.V1p5expression_id = str(self.V1p5expression_id)

        if self.V1p5cell_id is not None and not isinstance(self.V1p5cell_id, str):
            self.V1p5cell_id = str(self.V1p5cell_id)

        if self.V1p5repertoire_id is not None and not isinstance(self.V1p5repertoire_id, str):
            self.V1p5repertoire_id = str(self.V1p5repertoire_id)

        if self.V1p5data_processing_id is not None and not isinstance(self.V1p5data_processing_id, str):
            self.V1p5data_processing_id = str(self.V1p5data_processing_id)

        if self.V1p5property_type is not None and not isinstance(self.V1p5property_type, str):
            self.V1p5property_type = str(self.V1p5property_type)

        if self.V1p5value is not None and not isinstance(self.V1p5value, float):
            self.V1p5value = float(self.V1p5value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Receptor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Receptor"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Receptor"
    class_name: ClassVar[str] = "V1p5Receptor"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Receptor

    V1p5receptor_id: Optional[str] = None
    V1p5receptor_hash: Optional[str] = None
    V1p5receptor_type: Optional[Union[str, "V1p5ReceptorType"]] = None
    V1p5receptor_variable_domain_1_aa: Optional[str] = None
    V1p5receptor_variable_domain_1_locus: Optional[Union[str, "V1p5ReceptorVariableDomain1Locus"]] = None
    V1p5receptor_variable_domain_2_aa: Optional[str] = None
    V1p5receptor_variable_domain_2_locus: Optional[Union[str, "V1p5ReceptorVariableDomain2Locus"]] = None
    V1p5receptor_ref: Optional[Union[str, List[str]]] = empty_list()
    V1p5reactivity_measurements: Optional[Union[Union[dict, "V1p5ReceptorReactivity"], List[Union[dict, "V1p5ReceptorReactivity"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5receptor_id is not None and not isinstance(self.V1p5receptor_id, str):
            self.V1p5receptor_id = str(self.V1p5receptor_id)

        if self.V1p5receptor_hash is not None and not isinstance(self.V1p5receptor_hash, str):
            self.V1p5receptor_hash = str(self.V1p5receptor_hash)

        if self.V1p5receptor_type is not None and not isinstance(self.V1p5receptor_type, V1p5ReceptorType):
            self.V1p5receptor_type = V1p5ReceptorType(self.V1p5receptor_type)

        if self.V1p5receptor_variable_domain_1_aa is not None and not isinstance(self.V1p5receptor_variable_domain_1_aa, str):
            self.V1p5receptor_variable_domain_1_aa = str(self.V1p5receptor_variable_domain_1_aa)

        if self.V1p5receptor_variable_domain_1_locus is not None and not isinstance(self.V1p5receptor_variable_domain_1_locus, V1p5ReceptorVariableDomain1Locus):
            self.V1p5receptor_variable_domain_1_locus = V1p5ReceptorVariableDomain1Locus(self.V1p5receptor_variable_domain_1_locus)

        if self.V1p5receptor_variable_domain_2_aa is not None and not isinstance(self.V1p5receptor_variable_domain_2_aa, str):
            self.V1p5receptor_variable_domain_2_aa = str(self.V1p5receptor_variable_domain_2_aa)

        if self.V1p5receptor_variable_domain_2_locus is not None and not isinstance(self.V1p5receptor_variable_domain_2_locus, V1p5ReceptorVariableDomain2Locus):
            self.V1p5receptor_variable_domain_2_locus = V1p5ReceptorVariableDomain2Locus(self.V1p5receptor_variable_domain_2_locus)

        if not isinstance(self.V1p5receptor_ref, list):
            self.V1p5receptor_ref = [self.V1p5receptor_ref] if self.V1p5receptor_ref is not None else []
        self.V1p5receptor_ref = [v if isinstance(v, str) else str(v) for v in self.V1p5receptor_ref]

        if not isinstance(self.V1p5reactivity_measurements, list):
            self.V1p5reactivity_measurements = [self.V1p5reactivity_measurements] if self.V1p5reactivity_measurements is not None else []
        self.V1p5reactivity_measurements = [v if isinstance(v, V1p5ReceptorReactivity) else V1p5ReceptorReactivity(**as_dict(v)) for v in self.V1p5reactivity_measurements]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5ReceptorReactivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5ReceptorReactivity"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5ReceptorReactivity"
    class_name: ClassVar[str] = "V1p5ReceptorReactivity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5ReceptorReactivity

    V1p5ligand_type: Optional[Union[str, "V1p5LigandType"]] = None
    V1p5antigen_type: Optional[Union[str, "V1p5AntigenType"]] = None
    V1p5antigen: Optional[Union[str, "V1p5Antigen"]] = None
    V1p5antigen_source_species: Optional[Union[str, "V1p5AntigenSourceSpecies"]] = None
    V1p5peptide_start: Optional[int] = None
    V1p5peptide_end: Optional[int] = None
    V1p5mhc_class: Optional[Union[str, "V1p5MhcClass"]] = None
    V1p5mhc_gene_1: Optional[Union[str, "V1p5MhcGene1"]] = None
    V1p5mhc_allele_1: Optional[str] = None
    V1p5mhc_gene_2: Optional[Union[str, "V1p5MhcGene2"]] = None
    V1p5mhc_allele_2: Optional[str] = None
    V1p5reactivity_method: Optional[Union[str, "V1p5ReactivityMethod"]] = None
    V1p5reactivity_readout: Optional[Union[str, "V1p5ReactivityReadout"]] = None
    V1p5reactivity_value: Optional[float] = None
    V1p5reactivity_unit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5ligand_type is not None and not isinstance(self.V1p5ligand_type, V1p5LigandType):
            self.V1p5ligand_type = V1p5LigandType(self.V1p5ligand_type)

        if self.V1p5antigen_type is not None and not isinstance(self.V1p5antigen_type, V1p5AntigenType):
            self.V1p5antigen_type = V1p5AntigenType(self.V1p5antigen_type)

        if self.V1p5peptide_start is not None and not isinstance(self.V1p5peptide_start, int):
            self.V1p5peptide_start = int(self.V1p5peptide_start)

        if self.V1p5peptide_end is not None and not isinstance(self.V1p5peptide_end, int):
            self.V1p5peptide_end = int(self.V1p5peptide_end)

        if self.V1p5mhc_class is not None and not isinstance(self.V1p5mhc_class, V1p5MhcClass):
            self.V1p5mhc_class = V1p5MhcClass(self.V1p5mhc_class)

        if self.V1p5mhc_allele_1 is not None and not isinstance(self.V1p5mhc_allele_1, str):
            self.V1p5mhc_allele_1 = str(self.V1p5mhc_allele_1)

        if self.V1p5mhc_allele_2 is not None and not isinstance(self.V1p5mhc_allele_2, str):
            self.V1p5mhc_allele_2 = str(self.V1p5mhc_allele_2)

        if self.V1p5reactivity_method is not None and not isinstance(self.V1p5reactivity_method, V1p5ReactivityMethod):
            self.V1p5reactivity_method = V1p5ReactivityMethod(self.V1p5reactivity_method)

        if self.V1p5reactivity_readout is not None and not isinstance(self.V1p5reactivity_readout, V1p5ReactivityReadout):
            self.V1p5reactivity_readout = V1p5ReactivityReadout(self.V1p5reactivity_readout)

        if self.V1p5reactivity_value is not None and not isinstance(self.V1p5reactivity_value, float):
            self.V1p5reactivity_value = float(self.V1p5reactivity_value)

        if self.V1p5reactivity_unit is not None and not isinstance(self.V1p5reactivity_unit, str):
            self.V1p5reactivity_unit = str(self.V1p5reactivity_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5SampleProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5SampleProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5SampleProcessing"
    class_name: ClassVar[str] = "V1p5SampleProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5SampleProcessing

    V1p5sample_processing_id: Optional[str] = None
    V1p5sample_id: Optional[str] = None
    V1p5sample_type: Optional[str] = None
    V1p5tissue: Optional[Union[str, "V1p5Tissue"]] = None
    V1p5anatomic_site: Optional[str] = None
    V1p5disease_state_sample: Optional[str] = None
    V1p5collection_time_point_relative: Optional[float] = None
    V1p5collection_time_point_relative_unit: Optional[Union[str, "V1p5CollectionTimePointRelativeUnit"]] = None
    V1p5collection_time_point_reference: Optional[str] = None
    V1p5biomaterial_provider: Optional[str] = None
    V1p5tissue_processing: Optional[str] = None
    V1p5cell_subset: Optional[Union[str, "V1p5CellSubset"]] = None
    V1p5cell_phenotype: Optional[str] = None
    V1p5cell_species: Optional[Union[str, "V1p5CellSpecies"]] = None
    V1p5single_cell: Optional[Union[bool, Bool]] = None
    V1p5cell_number: Optional[int] = None
    V1p5cells_per_reaction: Optional[int] = None
    V1p5cell_storage: Optional[Union[bool, Bool]] = None
    V1p5cell_quality: Optional[str] = None
    V1p5cell_isolation: Optional[str] = None
    V1p5cell_processing_protocol: Optional[str] = None
    V1p5template_class: Optional[Union[str, "V1p5TemplateClass"]] = None
    V1p5template_quality: Optional[str] = None
    V1p5template_amount: Optional[float] = None
    V1p5template_amount_unit: Optional[Union[str, "V1p5TemplateAmountUnit"]] = None
    V1p5library_generation_method: Optional[Union[str, "V1p5LibraryGenerationMethod"]] = None
    V1p5library_generation_protocol: Optional[str] = None
    V1p5library_generation_kit_version: Optional[str] = None
    V1p5pcr_target: Optional[Union[Union[dict, V1p5PCRTarget], List[Union[dict, V1p5PCRTarget]]]] = empty_list()
    V1p5complete_sequences: Optional[Union[str, "V1p5CompleteSequences"]] = None
    V1p5physical_linkage: Optional[Union[str, "V1p5PhysicalLinkage"]] = None
    V1p5sequencing_run_id: Optional[str] = None
    V1p5total_reads_passing_qc_filter: Optional[int] = None
    V1p5sequencing_platform: Optional[str] = None
    V1p5sequencing_facility: Optional[str] = None
    V1p5sequencing_run_date: Optional[Union[str, XSDDateTime]] = None
    V1p5sequencing_kit: Optional[str] = None
    V1p5sequencing_files: Optional[Union[dict, V1p5SequencingData]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5sample_processing_id is not None and not isinstance(self.V1p5sample_processing_id, str):
            self.V1p5sample_processing_id = str(self.V1p5sample_processing_id)

        if self.V1p5sample_id is not None and not isinstance(self.V1p5sample_id, str):
            self.V1p5sample_id = str(self.V1p5sample_id)

        if self.V1p5sample_type is not None and not isinstance(self.V1p5sample_type, str):
            self.V1p5sample_type = str(self.V1p5sample_type)

        if self.V1p5anatomic_site is not None and not isinstance(self.V1p5anatomic_site, str):
            self.V1p5anatomic_site = str(self.V1p5anatomic_site)

        if self.V1p5disease_state_sample is not None and not isinstance(self.V1p5disease_state_sample, str):
            self.V1p5disease_state_sample = str(self.V1p5disease_state_sample)

        if self.V1p5collection_time_point_relative is not None and not isinstance(self.V1p5collection_time_point_relative, float):
            self.V1p5collection_time_point_relative = float(self.V1p5collection_time_point_relative)

        if self.V1p5collection_time_point_reference is not None and not isinstance(self.V1p5collection_time_point_reference, str):
            self.V1p5collection_time_point_reference = str(self.V1p5collection_time_point_reference)

        if self.V1p5biomaterial_provider is not None and not isinstance(self.V1p5biomaterial_provider, str):
            self.V1p5biomaterial_provider = str(self.V1p5biomaterial_provider)

        if self.V1p5tissue_processing is not None and not isinstance(self.V1p5tissue_processing, str):
            self.V1p5tissue_processing = str(self.V1p5tissue_processing)

        if self.V1p5cell_phenotype is not None and not isinstance(self.V1p5cell_phenotype, str):
            self.V1p5cell_phenotype = str(self.V1p5cell_phenotype)

        if self.V1p5single_cell is not None and not isinstance(self.V1p5single_cell, Bool):
            self.V1p5single_cell = Bool(self.V1p5single_cell)

        if self.V1p5cell_number is not None and not isinstance(self.V1p5cell_number, int):
            self.V1p5cell_number = int(self.V1p5cell_number)

        if self.V1p5cells_per_reaction is not None and not isinstance(self.V1p5cells_per_reaction, int):
            self.V1p5cells_per_reaction = int(self.V1p5cells_per_reaction)

        if self.V1p5cell_storage is not None and not isinstance(self.V1p5cell_storage, Bool):
            self.V1p5cell_storage = Bool(self.V1p5cell_storage)

        if self.V1p5cell_quality is not None and not isinstance(self.V1p5cell_quality, str):
            self.V1p5cell_quality = str(self.V1p5cell_quality)

        if self.V1p5cell_isolation is not None and not isinstance(self.V1p5cell_isolation, str):
            self.V1p5cell_isolation = str(self.V1p5cell_isolation)

        if self.V1p5cell_processing_protocol is not None and not isinstance(self.V1p5cell_processing_protocol, str):
            self.V1p5cell_processing_protocol = str(self.V1p5cell_processing_protocol)

        if self.V1p5template_class is not None and not isinstance(self.V1p5template_class, V1p5TemplateClass):
            self.V1p5template_class = V1p5TemplateClass(self.V1p5template_class)

        if self.V1p5template_quality is not None and not isinstance(self.V1p5template_quality, str):
            self.V1p5template_quality = str(self.V1p5template_quality)

        if self.V1p5template_amount is not None and not isinstance(self.V1p5template_amount, float):
            self.V1p5template_amount = float(self.V1p5template_amount)

        if self.V1p5library_generation_method is not None and not isinstance(self.V1p5library_generation_method, V1p5LibraryGenerationMethod):
            self.V1p5library_generation_method = V1p5LibraryGenerationMethod(self.V1p5library_generation_method)

        if self.V1p5library_generation_protocol is not None and not isinstance(self.V1p5library_generation_protocol, str):
            self.V1p5library_generation_protocol = str(self.V1p5library_generation_protocol)

        if self.V1p5library_generation_kit_version is not None and not isinstance(self.V1p5library_generation_kit_version, str):
            self.V1p5library_generation_kit_version = str(self.V1p5library_generation_kit_version)

        if not isinstance(self.V1p5pcr_target, list):
            self.V1p5pcr_target = [self.V1p5pcr_target] if self.V1p5pcr_target is not None else []
        self.V1p5pcr_target = [v if isinstance(v, V1p5PCRTarget) else V1p5PCRTarget(**as_dict(v)) for v in self.V1p5pcr_target]

        if self.V1p5complete_sequences is not None and not isinstance(self.V1p5complete_sequences, V1p5CompleteSequences):
            self.V1p5complete_sequences = V1p5CompleteSequences(self.V1p5complete_sequences)

        if self.V1p5physical_linkage is not None and not isinstance(self.V1p5physical_linkage, V1p5PhysicalLinkage):
            self.V1p5physical_linkage = V1p5PhysicalLinkage(self.V1p5physical_linkage)

        if self.V1p5sequencing_run_id is not None and not isinstance(self.V1p5sequencing_run_id, str):
            self.V1p5sequencing_run_id = str(self.V1p5sequencing_run_id)

        if self.V1p5total_reads_passing_qc_filter is not None and not isinstance(self.V1p5total_reads_passing_qc_filter, int):
            self.V1p5total_reads_passing_qc_filter = int(self.V1p5total_reads_passing_qc_filter)

        if self.V1p5sequencing_platform is not None and not isinstance(self.V1p5sequencing_platform, str):
            self.V1p5sequencing_platform = str(self.V1p5sequencing_platform)

        if self.V1p5sequencing_facility is not None and not isinstance(self.V1p5sequencing_facility, str):
            self.V1p5sequencing_facility = str(self.V1p5sequencing_facility)

        if self.V1p5sequencing_run_date is not None and not isinstance(self.V1p5sequencing_run_date, XSDDateTime):
            self.V1p5sequencing_run_date = XSDDateTime(self.V1p5sequencing_run_date)

        if self.V1p5sequencing_kit is not None and not isinstance(self.V1p5sequencing_kit, str):
            self.V1p5sequencing_kit = str(self.V1p5sequencing_kit)

        if self.V1p5sequencing_files is not None and not isinstance(self.V1p5sequencing_files, V1p5SequencingData):
            self.V1p5sequencing_files = V1p5SequencingData(**as_dict(self.V1p5sequencing_files))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4TimePoint(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4TimePoint"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4TimePoint"
    class_name: ClassVar[str] = "V1p4TimePoint"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4TimePoint

    V1p4label: Optional[str] = None
    V1p4value: Optional[float] = None
    V1p4unit: Optional[Union[str, "V1p4Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4label is not None and not isinstance(self.V1p4label, str):
            self.V1p4label = str(self.V1p4label)

        if self.V1p4value is not None and not isinstance(self.V1p4value, float):
            self.V1p4value = float(self.V1p4value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4TimeInterval(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4TimeInterval"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4TimeInterval"
    class_name: ClassVar[str] = "V1p4TimeInterval"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4TimeInterval

    V1p4min: Optional[float] = None
    V1p4max: Optional[float] = None
    V1p4unit: Optional[Union[str, "V1p4Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4min is not None and not isinstance(self.V1p4min, float):
            self.V1p4min = float(self.V1p4min)

        if self.V1p4max is not None and not isinstance(self.V1p4max, float):
            self.V1p4max = float(self.V1p4max)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4PhysicalQuantity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4PhysicalQuantity"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4PhysicalQuantity"
    class_name: ClassVar[str] = "V1p4PhysicalQuantity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4PhysicalQuantity

    V1p4quantity: Optional[float] = None
    V1p4unit: Optional[Union[str, "V1p4Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4quantity is not None and not isinstance(self.V1p4quantity, float):
            self.V1p4quantity = float(self.V1p4quantity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4TimeQuantity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4TimeQuantity"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4TimeQuantity"
    class_name: ClassVar[str] = "V1p4TimeQuantity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4TimeQuantity

    V1p4quantity: Optional[float] = None
    V1p4unit: Optional[Union[str, "V1p4Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4quantity is not None and not isinstance(self.V1p4quantity, float):
            self.V1p4quantity = float(self.V1p4quantity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Contributor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Contributor"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Contributor"
    class_name: ClassVar[str] = "V1p4Contributor"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Contributor

    V1p4contributor_id: Optional[str] = None
    V1p4name: Optional[str] = None
    V1p4orcid_id: Optional[Union[str, "V1p4OrcidId"]] = None
    V1p4affiliation: Optional[Union[str, "V1p4Affiliation"]] = None
    V1p4affiliation_department: Optional[str] = None
    V1p4contributions: Optional[Union[Union[dict, "V1p4ContributorContribution"], List[Union[dict, "V1p4ContributorContribution"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4contributor_id is not None and not isinstance(self.V1p4contributor_id, str):
            self.V1p4contributor_id = str(self.V1p4contributor_id)

        if self.V1p4name is not None and not isinstance(self.V1p4name, str):
            self.V1p4name = str(self.V1p4name)

        if self.V1p4affiliation_department is not None and not isinstance(self.V1p4affiliation_department, str):
            self.V1p4affiliation_department = str(self.V1p4affiliation_department)

        if not isinstance(self.V1p4contributions, list):
            self.V1p4contributions = [self.V1p4contributions] if self.V1p4contributions is not None else []
        self.V1p4contributions = [v if isinstance(v, V1p4ContributorContribution) else V1p4ContributorContribution(**as_dict(v)) for v in self.V1p4contributions]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4ContributorContribution(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4ContributorContribution"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4ContributorContribution"
    class_name: ClassVar[str] = "V1p4ContributorContribution"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4ContributorContribution

    V1p4role: Optional[Union[str, "V1p4Role"]] = None
    V1p4degree: Optional[Union[str, "V1p4Degree"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4role is not None and not isinstance(self.V1p4role, V1p4Role):
            self.V1p4role = V1p4Role(self.V1p4role)

        if self.V1p4degree is not None and not isinstance(self.V1p4degree, V1p4Degree):
            self.V1p4degree = V1p4Degree(self.V1p4degree)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4RearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4RearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4RearrangedSequence"
    class_name: ClassVar[str] = "V1p4RearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4RearrangedSequence

    V1p4sequence_id: Optional[str] = None
    V1p4sequence: Optional[str] = None
    V1p4derivation: Optional[Union[str, "V1p4Derivation"]] = None
    V1p4observation_type: Optional[Union[str, "V1p4ObservationType"]] = None
    V1p4curation: Optional[str] = None
    V1p4repository_name: Optional[str] = None
    V1p4repository_ref: Optional[str] = None
    V1p4deposited_version: Optional[str] = None
    V1p4sequence_start: Optional[int] = None
    V1p4sequence_end: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4sequence_id is not None and not isinstance(self.V1p4sequence_id, str):
            self.V1p4sequence_id = str(self.V1p4sequence_id)

        if self.V1p4sequence is not None and not isinstance(self.V1p4sequence, str):
            self.V1p4sequence = str(self.V1p4sequence)

        if self.V1p4derivation is not None and not isinstance(self.V1p4derivation, V1p4Derivation):
            self.V1p4derivation = V1p4Derivation(self.V1p4derivation)

        if self.V1p4observation_type is not None and not isinstance(self.V1p4observation_type, V1p4ObservationType):
            self.V1p4observation_type = V1p4ObservationType(self.V1p4observation_type)

        if self.V1p4curation is not None and not isinstance(self.V1p4curation, str):
            self.V1p4curation = str(self.V1p4curation)

        if self.V1p4repository_name is not None and not isinstance(self.V1p4repository_name, str):
            self.V1p4repository_name = str(self.V1p4repository_name)

        if self.V1p4repository_ref is not None and not isinstance(self.V1p4repository_ref, str):
            self.V1p4repository_ref = str(self.V1p4repository_ref)

        if self.V1p4deposited_version is not None and not isinstance(self.V1p4deposited_version, str):
            self.V1p4deposited_version = str(self.V1p4deposited_version)

        if self.V1p4sequence_start is not None and not isinstance(self.V1p4sequence_start, int):
            self.V1p4sequence_start = int(self.V1p4sequence_start)

        if self.V1p4sequence_end is not None and not isinstance(self.V1p4sequence_end, int):
            self.V1p4sequence_end = int(self.V1p4sequence_end)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4UnrearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4UnrearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4UnrearrangedSequence"
    class_name: ClassVar[str] = "V1p4UnrearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4UnrearrangedSequence

    V1p4sequence_id: Optional[str] = None
    V1p4sequence: Optional[str] = None
    V1p4curation: Optional[str] = None
    V1p4repository_name: Optional[str] = None
    V1p4repository_ref: Optional[str] = None
    V1p4patch_no: Optional[str] = None
    V1p4gff_seqid: Optional[str] = None
    V1p4gff_start: Optional[int] = None
    V1p4gff_end: Optional[int] = None
    V1p4strand: Optional[Union[str, "V1p4Strand"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4sequence_id is not None and not isinstance(self.V1p4sequence_id, str):
            self.V1p4sequence_id = str(self.V1p4sequence_id)

        if self.V1p4sequence is not None and not isinstance(self.V1p4sequence, str):
            self.V1p4sequence = str(self.V1p4sequence)

        if self.V1p4curation is not None and not isinstance(self.V1p4curation, str):
            self.V1p4curation = str(self.V1p4curation)

        if self.V1p4repository_name is not None and not isinstance(self.V1p4repository_name, str):
            self.V1p4repository_name = str(self.V1p4repository_name)

        if self.V1p4repository_ref is not None and not isinstance(self.V1p4repository_ref, str):
            self.V1p4repository_ref = str(self.V1p4repository_ref)

        if self.V1p4patch_no is not None and not isinstance(self.V1p4patch_no, str):
            self.V1p4patch_no = str(self.V1p4patch_no)

        if self.V1p4gff_seqid is not None and not isinstance(self.V1p4gff_seqid, str):
            self.V1p4gff_seqid = str(self.V1p4gff_seqid)

        if self.V1p4gff_start is not None and not isinstance(self.V1p4gff_start, int):
            self.V1p4gff_start = int(self.V1p4gff_start)

        if self.V1p4gff_end is not None and not isinstance(self.V1p4gff_end, int):
            self.V1p4gff_end = int(self.V1p4gff_end)

        if self.V1p4strand is not None and not isinstance(self.V1p4strand, V1p4Strand):
            self.V1p4strand = V1p4Strand(self.V1p4strand)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SequenceDelineationV(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SequenceDelineationV"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SequenceDelineationV"
    class_name: ClassVar[str] = "V1p4SequenceDelineationV"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SequenceDelineationV

    V1p4sequence_delineation_id: Optional[str] = None
    V1p4delineation_scheme: Optional[str] = None
    V1p4unaligned_sequence: Optional[str] = None
    V1p4aligned_sequence: Optional[str] = None
    V1p4fwr1_start: Optional[int] = None
    V1p4fwr1_end: Optional[int] = None
    V1p4cdr1_start: Optional[int] = None
    V1p4cdr1_end: Optional[int] = None
    V1p4fwr2_start: Optional[int] = None
    V1p4fwr2_end: Optional[int] = None
    V1p4cdr2_start: Optional[int] = None
    V1p4cdr2_end: Optional[int] = None
    V1p4fwr3_start: Optional[int] = None
    V1p4fwr3_end: Optional[int] = None
    V1p4cdr3_start: Optional[int] = None
    V1p4alignment_labels: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4sequence_delineation_id is not None and not isinstance(self.V1p4sequence_delineation_id, str):
            self.V1p4sequence_delineation_id = str(self.V1p4sequence_delineation_id)

        if self.V1p4delineation_scheme is not None and not isinstance(self.V1p4delineation_scheme, str):
            self.V1p4delineation_scheme = str(self.V1p4delineation_scheme)

        if self.V1p4unaligned_sequence is not None and not isinstance(self.V1p4unaligned_sequence, str):
            self.V1p4unaligned_sequence = str(self.V1p4unaligned_sequence)

        if self.V1p4aligned_sequence is not None and not isinstance(self.V1p4aligned_sequence, str):
            self.V1p4aligned_sequence = str(self.V1p4aligned_sequence)

        if self.V1p4fwr1_start is not None and not isinstance(self.V1p4fwr1_start, int):
            self.V1p4fwr1_start = int(self.V1p4fwr1_start)

        if self.V1p4fwr1_end is not None and not isinstance(self.V1p4fwr1_end, int):
            self.V1p4fwr1_end = int(self.V1p4fwr1_end)

        if self.V1p4cdr1_start is not None and not isinstance(self.V1p4cdr1_start, int):
            self.V1p4cdr1_start = int(self.V1p4cdr1_start)

        if self.V1p4cdr1_end is not None and not isinstance(self.V1p4cdr1_end, int):
            self.V1p4cdr1_end = int(self.V1p4cdr1_end)

        if self.V1p4fwr2_start is not None and not isinstance(self.V1p4fwr2_start, int):
            self.V1p4fwr2_start = int(self.V1p4fwr2_start)

        if self.V1p4fwr2_end is not None and not isinstance(self.V1p4fwr2_end, int):
            self.V1p4fwr2_end = int(self.V1p4fwr2_end)

        if self.V1p4cdr2_start is not None and not isinstance(self.V1p4cdr2_start, int):
            self.V1p4cdr2_start = int(self.V1p4cdr2_start)

        if self.V1p4cdr2_end is not None and not isinstance(self.V1p4cdr2_end, int):
            self.V1p4cdr2_end = int(self.V1p4cdr2_end)

        if self.V1p4fwr3_start is not None and not isinstance(self.V1p4fwr3_start, int):
            self.V1p4fwr3_start = int(self.V1p4fwr3_start)

        if self.V1p4fwr3_end is not None and not isinstance(self.V1p4fwr3_end, int):
            self.V1p4fwr3_end = int(self.V1p4fwr3_end)

        if self.V1p4cdr3_start is not None and not isinstance(self.V1p4cdr3_start, int):
            self.V1p4cdr3_start = int(self.V1p4cdr3_start)

        if not isinstance(self.V1p4alignment_labels, list):
            self.V1p4alignment_labels = [self.V1p4alignment_labels] if self.V1p4alignment_labels is not None else []
        self.V1p4alignment_labels = [v if isinstance(v, str) else str(v) for v in self.V1p4alignment_labels]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4AlleleDescription(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4AlleleDescription"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4AlleleDescription"
    class_name: ClassVar[str] = "V1p4AlleleDescription"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4AlleleDescription

    V1p4allele_description_id: Optional[str] = None
    V1p4allele_description_ref: Optional[str] = None
    V1p4acknowledgements: Optional[Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]]] = empty_list()
    V1p4release_version: Optional[str] = None
    V1p4release_date: Optional[Union[str, XSDDateTime]] = None
    V1p4release_description: Optional[str] = None
    V1p4label: Optional[str] = None
    V1p4sequence: Optional[str] = None
    V1p4coding_sequence: Optional[str] = None
    V1p4aliases: Optional[Union[str, List[str]]] = empty_list()
    V1p4locus: Optional[Union[str, "V1p4Locus"]] = None
    V1p4chromosome: Optional[int] = None
    V1p4sequence_type: Optional[Union[str, "V1p4SequenceType"]] = None
    V1p4functional: Optional[Union[bool, Bool]] = None
    V1p4inference_type: Optional[Union[str, "V1p4InferenceType"]] = None
    V1p4species: Optional[Union[str, "V1p4Species"]] = None
    V1p4species_subgroup: Optional[str] = None
    V1p4species_subgroup_type: Optional[Union[str, "V1p4SpeciesSubgroupType"]] = None
    V1p4status: Optional[Union[str, "V1p4Status"]] = None
    V1p4subgroup_designation: Optional[str] = None
    V1p4gene_designation: Optional[str] = None
    V1p4allele_designation: Optional[str] = None
    V1p4allele_similarity_cluster_designation: Optional[str] = None
    V1p4allele_similarity_cluster_member_id: Optional[str] = None
    V1p4j_codon_frame: Optional[Union[str, "V1p4JCodonFrame"]] = None
    V1p4gene_start: Optional[int] = None
    V1p4gene_end: Optional[int] = None
    V1p4utr_5_prime_start: Optional[int] = None
    V1p4utr_5_prime_end: Optional[int] = None
    V1p4leader_1_start: Optional[int] = None
    V1p4leader_1_end: Optional[int] = None
    V1p4leader_2_start: Optional[int] = None
    V1p4leader_2_end: Optional[int] = None
    V1p4v_rs_start: Optional[int] = None
    V1p4v_rs_end: Optional[int] = None
    V1p4d_rs_3_prime_start: Optional[int] = None
    V1p4d_rs_3_prime_end: Optional[int] = None
    V1p4d_rs_5_prime_start: Optional[int] = None
    V1p4d_rs_5_prime_end: Optional[int] = None
    V1p4j_cdr3_end: Optional[int] = None
    V1p4j_rs_start: Optional[int] = None
    V1p4j_rs_end: Optional[int] = None
    V1p4j_donor_splice: Optional[int] = None
    V1p4v_gene_delineations: Optional[Union[Union[dict, V1p4SequenceDelineationV], List[Union[dict, V1p4SequenceDelineationV]]]] = empty_list()
    V1p4unrearranged_support: Optional[Union[Union[dict, V1p4UnrearrangedSequence], List[Union[dict, V1p4UnrearrangedSequence]]]] = empty_list()
    V1p4rearranged_support: Optional[Union[Union[dict, V1p4RearrangedSequence], List[Union[dict, V1p4RearrangedSequence]]]] = empty_list()
    V1p4paralogs: Optional[Union[str, List[str]]] = empty_list()
    V1p4curation: Optional[str] = None
    V1p4curational_tags: Optional[Union[Union[str, "V1p4CurationalTags"], List[Union[str, "V1p4CurationalTags"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4allele_description_id is not None and not isinstance(self.V1p4allele_description_id, str):
            self.V1p4allele_description_id = str(self.V1p4allele_description_id)

        if self.V1p4allele_description_ref is not None and not isinstance(self.V1p4allele_description_ref, str):
            self.V1p4allele_description_ref = str(self.V1p4allele_description_ref)

        if not isinstance(self.V1p4acknowledgements, list):
            self.V1p4acknowledgements = [self.V1p4acknowledgements] if self.V1p4acknowledgements is not None else []
        self.V1p4acknowledgements = [v if isinstance(v, V1p4Contributor) else V1p4Contributor(**as_dict(v)) for v in self.V1p4acknowledgements]

        if self.V1p4release_version is not None and not isinstance(self.V1p4release_version, str):
            self.V1p4release_version = str(self.V1p4release_version)

        if self.V1p4release_date is not None and not isinstance(self.V1p4release_date, XSDDateTime):
            self.V1p4release_date = XSDDateTime(self.V1p4release_date)

        if self.V1p4release_description is not None and not isinstance(self.V1p4release_description, str):
            self.V1p4release_description = str(self.V1p4release_description)

        if self.V1p4label is not None and not isinstance(self.V1p4label, str):
            self.V1p4label = str(self.V1p4label)

        if self.V1p4sequence is not None and not isinstance(self.V1p4sequence, str):
            self.V1p4sequence = str(self.V1p4sequence)

        if self.V1p4coding_sequence is not None and not isinstance(self.V1p4coding_sequence, str):
            self.V1p4coding_sequence = str(self.V1p4coding_sequence)

        if not isinstance(self.V1p4aliases, list):
            self.V1p4aliases = [self.V1p4aliases] if self.V1p4aliases is not None else []
        self.V1p4aliases = [v if isinstance(v, str) else str(v) for v in self.V1p4aliases]

        if self.V1p4locus is not None and not isinstance(self.V1p4locus, V1p4Locus):
            self.V1p4locus = V1p4Locus(self.V1p4locus)

        if self.V1p4chromosome is not None and not isinstance(self.V1p4chromosome, int):
            self.V1p4chromosome = int(self.V1p4chromosome)

        if self.V1p4sequence_type is not None and not isinstance(self.V1p4sequence_type, V1p4SequenceType):
            self.V1p4sequence_type = V1p4SequenceType(self.V1p4sequence_type)

        if self.V1p4functional is not None and not isinstance(self.V1p4functional, Bool):
            self.V1p4functional = Bool(self.V1p4functional)

        if self.V1p4inference_type is not None and not isinstance(self.V1p4inference_type, V1p4InferenceType):
            self.V1p4inference_type = V1p4InferenceType(self.V1p4inference_type)

        if self.V1p4species_subgroup is not None and not isinstance(self.V1p4species_subgroup, str):
            self.V1p4species_subgroup = str(self.V1p4species_subgroup)

        if self.V1p4species_subgroup_type is not None and not isinstance(self.V1p4species_subgroup_type, V1p4SpeciesSubgroupType):
            self.V1p4species_subgroup_type = V1p4SpeciesSubgroupType(self.V1p4species_subgroup_type)

        if self.V1p4status is not None and not isinstance(self.V1p4status, V1p4Status):
            self.V1p4status = V1p4Status(self.V1p4status)

        if self.V1p4subgroup_designation is not None and not isinstance(self.V1p4subgroup_designation, str):
            self.V1p4subgroup_designation = str(self.V1p4subgroup_designation)

        if self.V1p4gene_designation is not None and not isinstance(self.V1p4gene_designation, str):
            self.V1p4gene_designation = str(self.V1p4gene_designation)

        if self.V1p4allele_designation is not None and not isinstance(self.V1p4allele_designation, str):
            self.V1p4allele_designation = str(self.V1p4allele_designation)

        if self.V1p4allele_similarity_cluster_designation is not None and not isinstance(self.V1p4allele_similarity_cluster_designation, str):
            self.V1p4allele_similarity_cluster_designation = str(self.V1p4allele_similarity_cluster_designation)

        if self.V1p4allele_similarity_cluster_member_id is not None and not isinstance(self.V1p4allele_similarity_cluster_member_id, str):
            self.V1p4allele_similarity_cluster_member_id = str(self.V1p4allele_similarity_cluster_member_id)

        if self.V1p4j_codon_frame is not None and not isinstance(self.V1p4j_codon_frame, V1p4JCodonFrame):
            self.V1p4j_codon_frame = V1p4JCodonFrame(self.V1p4j_codon_frame)

        if self.V1p4gene_start is not None and not isinstance(self.V1p4gene_start, int):
            self.V1p4gene_start = int(self.V1p4gene_start)

        if self.V1p4gene_end is not None and not isinstance(self.V1p4gene_end, int):
            self.V1p4gene_end = int(self.V1p4gene_end)

        if self.V1p4utr_5_prime_start is not None and not isinstance(self.V1p4utr_5_prime_start, int):
            self.V1p4utr_5_prime_start = int(self.V1p4utr_5_prime_start)

        if self.V1p4utr_5_prime_end is not None and not isinstance(self.V1p4utr_5_prime_end, int):
            self.V1p4utr_5_prime_end = int(self.V1p4utr_5_prime_end)

        if self.V1p4leader_1_start is not None and not isinstance(self.V1p4leader_1_start, int):
            self.V1p4leader_1_start = int(self.V1p4leader_1_start)

        if self.V1p4leader_1_end is not None and not isinstance(self.V1p4leader_1_end, int):
            self.V1p4leader_1_end = int(self.V1p4leader_1_end)

        if self.V1p4leader_2_start is not None and not isinstance(self.V1p4leader_2_start, int):
            self.V1p4leader_2_start = int(self.V1p4leader_2_start)

        if self.V1p4leader_2_end is not None and not isinstance(self.V1p4leader_2_end, int):
            self.V1p4leader_2_end = int(self.V1p4leader_2_end)

        if self.V1p4v_rs_start is not None and not isinstance(self.V1p4v_rs_start, int):
            self.V1p4v_rs_start = int(self.V1p4v_rs_start)

        if self.V1p4v_rs_end is not None and not isinstance(self.V1p4v_rs_end, int):
            self.V1p4v_rs_end = int(self.V1p4v_rs_end)

        if self.V1p4d_rs_3_prime_start is not None and not isinstance(self.V1p4d_rs_3_prime_start, int):
            self.V1p4d_rs_3_prime_start = int(self.V1p4d_rs_3_prime_start)

        if self.V1p4d_rs_3_prime_end is not None and not isinstance(self.V1p4d_rs_3_prime_end, int):
            self.V1p4d_rs_3_prime_end = int(self.V1p4d_rs_3_prime_end)

        if self.V1p4d_rs_5_prime_start is not None and not isinstance(self.V1p4d_rs_5_prime_start, int):
            self.V1p4d_rs_5_prime_start = int(self.V1p4d_rs_5_prime_start)

        if self.V1p4d_rs_5_prime_end is not None and not isinstance(self.V1p4d_rs_5_prime_end, int):
            self.V1p4d_rs_5_prime_end = int(self.V1p4d_rs_5_prime_end)

        if self.V1p4j_cdr3_end is not None and not isinstance(self.V1p4j_cdr3_end, int):
            self.V1p4j_cdr3_end = int(self.V1p4j_cdr3_end)

        if self.V1p4j_rs_start is not None and not isinstance(self.V1p4j_rs_start, int):
            self.V1p4j_rs_start = int(self.V1p4j_rs_start)

        if self.V1p4j_rs_end is not None and not isinstance(self.V1p4j_rs_end, int):
            self.V1p4j_rs_end = int(self.V1p4j_rs_end)

        if self.V1p4j_donor_splice is not None and not isinstance(self.V1p4j_donor_splice, int):
            self.V1p4j_donor_splice = int(self.V1p4j_donor_splice)

        if not isinstance(self.V1p4v_gene_delineations, list):
            self.V1p4v_gene_delineations = [self.V1p4v_gene_delineations] if self.V1p4v_gene_delineations is not None else []
        self.V1p4v_gene_delineations = [v if isinstance(v, V1p4SequenceDelineationV) else V1p4SequenceDelineationV(**as_dict(v)) for v in self.V1p4v_gene_delineations]

        if not isinstance(self.V1p4unrearranged_support, list):
            self.V1p4unrearranged_support = [self.V1p4unrearranged_support] if self.V1p4unrearranged_support is not None else []
        self.V1p4unrearranged_support = [v if isinstance(v, V1p4UnrearrangedSequence) else V1p4UnrearrangedSequence(**as_dict(v)) for v in self.V1p4unrearranged_support]

        if not isinstance(self.V1p4rearranged_support, list):
            self.V1p4rearranged_support = [self.V1p4rearranged_support] if self.V1p4rearranged_support is not None else []
        self.V1p4rearranged_support = [v if isinstance(v, V1p4RearrangedSequence) else V1p4RearrangedSequence(**as_dict(v)) for v in self.V1p4rearranged_support]

        if not isinstance(self.V1p4paralogs, list):
            self.V1p4paralogs = [self.V1p4paralogs] if self.V1p4paralogs is not None else []
        self.V1p4paralogs = [v if isinstance(v, str) else str(v) for v in self.V1p4paralogs]

        if self.V1p4curation is not None and not isinstance(self.V1p4curation, str):
            self.V1p4curation = str(self.V1p4curation)

        if not isinstance(self.V1p4curational_tags, list):
            self.V1p4curational_tags = [self.V1p4curational_tags] if self.V1p4curational_tags is not None else []
        self.V1p4curational_tags = [v if isinstance(v, V1p4CurationalTags) else V1p4CurationalTags(v) for v in self.V1p4curational_tags]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4GermlineSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4GermlineSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4GermlineSet"
    class_name: ClassVar[str] = "V1p4GermlineSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4GermlineSet

    V1p4germline_set_id: Optional[str] = None
    V1p4acknowledgements: Optional[Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]]] = empty_list()
    V1p4release_version: Optional[str] = None
    V1p4release_description: Optional[str] = None
    V1p4release_date: Optional[Union[str, XSDDateTime]] = None
    V1p4germline_set_name: Optional[str] = None
    V1p4germline_set_ref: Optional[str] = None
    V1p4pub_ids: Optional[Union[str, List[str]]] = empty_list()
    V1p4species: Optional[Union[str, "V1p4Species"]] = None
    V1p4species_subgroup: Optional[str] = None
    V1p4species_subgroup_type: Optional[Union[str, "V1p4SpeciesSubgroupType"]] = None
    V1p4locus: Optional[Union[str, "V1p4Locus"]] = None
    V1p4allele_descriptions: Optional[Union[Union[dict, V1p4AlleleDescription], List[Union[dict, V1p4AlleleDescription]]]] = empty_list()
    V1p4curation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4germline_set_id is not None and not isinstance(self.V1p4germline_set_id, str):
            self.V1p4germline_set_id = str(self.V1p4germline_set_id)

        if not isinstance(self.V1p4acknowledgements, list):
            self.V1p4acknowledgements = [self.V1p4acknowledgements] if self.V1p4acknowledgements is not None else []
        self.V1p4acknowledgements = [v if isinstance(v, V1p4Contributor) else V1p4Contributor(**as_dict(v)) for v in self.V1p4acknowledgements]

        if self.V1p4release_version is not None and not isinstance(self.V1p4release_version, str):
            self.V1p4release_version = str(self.V1p4release_version)

        if self.V1p4release_description is not None and not isinstance(self.V1p4release_description, str):
            self.V1p4release_description = str(self.V1p4release_description)

        if self.V1p4release_date is not None and not isinstance(self.V1p4release_date, XSDDateTime):
            self.V1p4release_date = XSDDateTime(self.V1p4release_date)

        if self.V1p4germline_set_name is not None and not isinstance(self.V1p4germline_set_name, str):
            self.V1p4germline_set_name = str(self.V1p4germline_set_name)

        if self.V1p4germline_set_ref is not None and not isinstance(self.V1p4germline_set_ref, str):
            self.V1p4germline_set_ref = str(self.V1p4germline_set_ref)

        if not isinstance(self.V1p4pub_ids, list):
            self.V1p4pub_ids = [self.V1p4pub_ids] if self.V1p4pub_ids is not None else []
        self.V1p4pub_ids = [v if isinstance(v, str) else str(v) for v in self.V1p4pub_ids]

        if self.V1p4species_subgroup is not None and not isinstance(self.V1p4species_subgroup, str):
            self.V1p4species_subgroup = str(self.V1p4species_subgroup)

        if self.V1p4species_subgroup_type is not None and not isinstance(self.V1p4species_subgroup_type, V1p4SpeciesSubgroupType):
            self.V1p4species_subgroup_type = V1p4SpeciesSubgroupType(self.V1p4species_subgroup_type)

        if self.V1p4locus is not None and not isinstance(self.V1p4locus, V1p4Locus):
            self.V1p4locus = V1p4Locus(self.V1p4locus)

        if not isinstance(self.V1p4allele_descriptions, list):
            self.V1p4allele_descriptions = [self.V1p4allele_descriptions] if self.V1p4allele_descriptions is not None else []
        self.V1p4allele_descriptions = [v if isinstance(v, V1p4AlleleDescription) else V1p4AlleleDescription(**as_dict(v)) for v in self.V1p4allele_descriptions]

        if self.V1p4curation is not None and not isinstance(self.V1p4curation, str):
            self.V1p4curation = str(self.V1p4curation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4GenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4GenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4GenotypeSet"
    class_name: ClassVar[str] = "V1p4GenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4GenotypeSet

    V1p4receptor_genotype_set_id: Optional[str] = None
    V1p4genotype_class_list: Optional[Union[Union[dict, "V1p4Genotype"], List[Union[dict, "V1p4Genotype"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4receptor_genotype_set_id is not None and not isinstance(self.V1p4receptor_genotype_set_id, str):
            self.V1p4receptor_genotype_set_id = str(self.V1p4receptor_genotype_set_id)

        if not isinstance(self.V1p4genotype_class_list, list):
            self.V1p4genotype_class_list = [self.V1p4genotype_class_list] if self.V1p4genotype_class_list is not None else []
        self.V1p4genotype_class_list = [v if isinstance(v, V1p4Genotype) else V1p4Genotype(**as_dict(v)) for v in self.V1p4genotype_class_list]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Genotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Genotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Genotype"
    class_name: ClassVar[str] = "V1p4Genotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Genotype

    V1p4receptor_genotype_id: Optional[str] = None
    V1p4locus: Optional[Union[str, "V1p4Locus"]] = None
    V1p4documented_alleles: Optional[Union[Union[dict, "V1p4DocumentedAllele"], List[Union[dict, "V1p4DocumentedAllele"]]]] = empty_list()
    V1p4undocumented_alleles: Optional[Union[Union[dict, "V1p4UndocumentedAllele"], List[Union[dict, "V1p4UndocumentedAllele"]]]] = empty_list()
    V1p4deleted_genes: Optional[Union[Union[dict, "V1p4DeletedGene"], List[Union[dict, "V1p4DeletedGene"]]]] = empty_list()
    V1p4inference_process: Optional[Union[str, "V1p4InferenceProcess"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4receptor_genotype_id is not None and not isinstance(self.V1p4receptor_genotype_id, str):
            self.V1p4receptor_genotype_id = str(self.V1p4receptor_genotype_id)

        if self.V1p4locus is not None and not isinstance(self.V1p4locus, V1p4Locus):
            self.V1p4locus = V1p4Locus(self.V1p4locus)

        if not isinstance(self.V1p4documented_alleles, list):
            self.V1p4documented_alleles = [self.V1p4documented_alleles] if self.V1p4documented_alleles is not None else []
        self.V1p4documented_alleles = [v if isinstance(v, V1p4DocumentedAllele) else V1p4DocumentedAllele(**as_dict(v)) for v in self.V1p4documented_alleles]

        if not isinstance(self.V1p4undocumented_alleles, list):
            self.V1p4undocumented_alleles = [self.V1p4undocumented_alleles] if self.V1p4undocumented_alleles is not None else []
        self.V1p4undocumented_alleles = [v if isinstance(v, V1p4UndocumentedAllele) else V1p4UndocumentedAllele(**as_dict(v)) for v in self.V1p4undocumented_alleles]

        if not isinstance(self.V1p4deleted_genes, list):
            self.V1p4deleted_genes = [self.V1p4deleted_genes] if self.V1p4deleted_genes is not None else []
        self.V1p4deleted_genes = [v if isinstance(v, V1p4DeletedGene) else V1p4DeletedGene(**as_dict(v)) for v in self.V1p4deleted_genes]

        if self.V1p4inference_process is not None and not isinstance(self.V1p4inference_process, V1p4InferenceProcess):
            self.V1p4inference_process = V1p4InferenceProcess(self.V1p4inference_process)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4DocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4DocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4DocumentedAllele"
    class_name: ClassVar[str] = "V1p4DocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4DocumentedAllele

    V1p4label: Optional[str] = None
    V1p4germline_set_ref: Optional[str] = None
    V1p4phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4label is not None and not isinstance(self.V1p4label, str):
            self.V1p4label = str(self.V1p4label)

        if self.V1p4germline_set_ref is not None and not isinstance(self.V1p4germline_set_ref, str):
            self.V1p4germline_set_ref = str(self.V1p4germline_set_ref)

        if self.V1p4phasing is not None and not isinstance(self.V1p4phasing, int):
            self.V1p4phasing = int(self.V1p4phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4UndocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4UndocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4UndocumentedAllele"
    class_name: ClassVar[str] = "V1p4UndocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4UndocumentedAllele

    V1p4allele_name: Optional[str] = None
    V1p4sequence: Optional[str] = None
    V1p4phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4allele_name is not None and not isinstance(self.V1p4allele_name, str):
            self.V1p4allele_name = str(self.V1p4allele_name)

        if self.V1p4sequence is not None and not isinstance(self.V1p4sequence, str):
            self.V1p4sequence = str(self.V1p4sequence)

        if self.V1p4phasing is not None and not isinstance(self.V1p4phasing, int):
            self.V1p4phasing = int(self.V1p4phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4DeletedGene(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4DeletedGene"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4DeletedGene"
    class_name: ClassVar[str] = "V1p4DeletedGene"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4DeletedGene

    V1p4label: Optional[str] = None
    V1p4germline_set_ref: Optional[str] = None
    V1p4phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4label is not None and not isinstance(self.V1p4label, str):
            self.V1p4label = str(self.V1p4label)

        if self.V1p4germline_set_ref is not None and not isinstance(self.V1p4germline_set_ref, str):
            self.V1p4germline_set_ref = str(self.V1p4germline_set_ref)

        if self.V1p4phasing is not None and not isinstance(self.V1p4phasing, int):
            self.V1p4phasing = int(self.V1p4phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4MHCGenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4MHCGenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4MHCGenotypeSet"
    class_name: ClassVar[str] = "V1p4MHCGenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4MHCGenotypeSet

    V1p4mhc_genotype_set_id: Optional[str] = None
    V1p4mhc_genotype_list: Optional[Union[Union[dict, "V1p4MHCGenotype"], List[Union[dict, "V1p4MHCGenotype"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4mhc_genotype_set_id is not None and not isinstance(self.V1p4mhc_genotype_set_id, str):
            self.V1p4mhc_genotype_set_id = str(self.V1p4mhc_genotype_set_id)

        if not isinstance(self.V1p4mhc_genotype_list, list):
            self.V1p4mhc_genotype_list = [self.V1p4mhc_genotype_list] if self.V1p4mhc_genotype_list is not None else []
        self.V1p4mhc_genotype_list = [v if isinstance(v, V1p4MHCGenotype) else V1p4MHCGenotype(**as_dict(v)) for v in self.V1p4mhc_genotype_list]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4MHCGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4MHCGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4MHCGenotype"
    class_name: ClassVar[str] = "V1p4MHCGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4MHCGenotype

    V1p4mhc_genotype_id: Optional[str] = None
    V1p4mhc_class: Optional[Union[str, "V1p4MhcClass"]] = None
    V1p4mhc_alleles: Optional[Union[Union[dict, "V1p4MHCAllele"], List[Union[dict, "V1p4MHCAllele"]]]] = empty_list()
    V1p4mhc_genotyping_method: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4mhc_genotype_id is not None and not isinstance(self.V1p4mhc_genotype_id, str):
            self.V1p4mhc_genotype_id = str(self.V1p4mhc_genotype_id)

        if self.V1p4mhc_class is not None and not isinstance(self.V1p4mhc_class, V1p4MhcClass):
            self.V1p4mhc_class = V1p4MhcClass(self.V1p4mhc_class)

        if not isinstance(self.V1p4mhc_alleles, list):
            self.V1p4mhc_alleles = [self.V1p4mhc_alleles] if self.V1p4mhc_alleles is not None else []
        self.V1p4mhc_alleles = [v if isinstance(v, V1p4MHCAllele) else V1p4MHCAllele(**as_dict(v)) for v in self.V1p4mhc_alleles]

        if self.V1p4mhc_genotyping_method is not None and not isinstance(self.V1p4mhc_genotyping_method, str):
            self.V1p4mhc_genotyping_method = str(self.V1p4mhc_genotyping_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4MHCAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4MHCAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4MHCAllele"
    class_name: ClassVar[str] = "V1p4MHCAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4MHCAllele

    V1p4allele_designation: Optional[str] = None
    V1p4gene: Optional[Union[str, "V1p4Gene"]] = None
    V1p4reference_set_ref: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4allele_designation is not None and not isinstance(self.V1p4allele_designation, str):
            self.V1p4allele_designation = str(self.V1p4allele_designation)

        if self.V1p4reference_set_ref is not None and not isinstance(self.V1p4reference_set_ref, str):
            self.V1p4reference_set_ref = str(self.V1p4reference_set_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SubjectGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SubjectGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SubjectGenotype"
    class_name: ClassVar[str] = "V1p4SubjectGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SubjectGenotype

    V1p4receptor_genotype_set: Optional[Union[dict, V1p4GenotypeSet]] = None
    V1p4mhc_genotype_set: Optional[Union[dict, V1p4MHCGenotypeSet]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4receptor_genotype_set is not None and not isinstance(self.V1p4receptor_genotype_set, V1p4GenotypeSet):
            self.V1p4receptor_genotype_set = V1p4GenotypeSet(**as_dict(self.V1p4receptor_genotype_set))

        if self.V1p4mhc_genotype_set is not None and not isinstance(self.V1p4mhc_genotype_set, V1p4MHCGenotypeSet):
            self.V1p4mhc_genotype_set = V1p4MHCGenotypeSet(**as_dict(self.V1p4mhc_genotype_set))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Study(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Study"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Study"
    class_name: ClassVar[str] = "V1p4Study"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Study

    V1p4study_id: Optional[str] = None
    V1p4study_title: Optional[str] = None
    V1p4study_type: Optional[Union[str, "V1p4StudyType"]] = None
    V1p4study_description: Optional[str] = None
    V1p4inclusion_exclusion_criteria: Optional[str] = None
    V1p4grants: Optional[str] = None
    V1p4contributors: Optional[Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]]] = empty_list()
    V1p4pub_ids: Optional[Union[str, List[str]]] = empty_list()
    V1p4keywords_study: Optional[Union[Union[str, "V1p4KeywordsStudy"], List[Union[str, "V1p4KeywordsStudy"]]]] = empty_list()
    V1p4adc_publish_date: Optional[Union[str, XSDDateTime]] = None
    V1p4adc_update_date: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4study_id is not None and not isinstance(self.V1p4study_id, str):
            self.V1p4study_id = str(self.V1p4study_id)

        if self.V1p4study_title is not None and not isinstance(self.V1p4study_title, str):
            self.V1p4study_title = str(self.V1p4study_title)

        if self.V1p4study_description is not None and not isinstance(self.V1p4study_description, str):
            self.V1p4study_description = str(self.V1p4study_description)

        if self.V1p4inclusion_exclusion_criteria is not None and not isinstance(self.V1p4inclusion_exclusion_criteria, str):
            self.V1p4inclusion_exclusion_criteria = str(self.V1p4inclusion_exclusion_criteria)

        if self.V1p4grants is not None and not isinstance(self.V1p4grants, str):
            self.V1p4grants = str(self.V1p4grants)

        if not isinstance(self.V1p4contributors, list):
            self.V1p4contributors = [self.V1p4contributors] if self.V1p4contributors is not None else []
        self.V1p4contributors = [v if isinstance(v, V1p4Contributor) else V1p4Contributor(**as_dict(v)) for v in self.V1p4contributors]

        if not isinstance(self.V1p4pub_ids, list):
            self.V1p4pub_ids = [self.V1p4pub_ids] if self.V1p4pub_ids is not None else []
        self.V1p4pub_ids = [v if isinstance(v, str) else str(v) for v in self.V1p4pub_ids]

        if not isinstance(self.V1p4keywords_study, list):
            self.V1p4keywords_study = [self.V1p4keywords_study] if self.V1p4keywords_study is not None else []
        self.V1p4keywords_study = [v if isinstance(v, V1p4KeywordsStudy) else V1p4KeywordsStudy(v) for v in self.V1p4keywords_study]

        if self.V1p4adc_publish_date is not None and not isinstance(self.V1p4adc_publish_date, XSDDateTime):
            self.V1p4adc_publish_date = XSDDateTime(self.V1p4adc_publish_date)

        if self.V1p4adc_update_date is not None and not isinstance(self.V1p4adc_update_date, XSDDateTime):
            self.V1p4adc_update_date = XSDDateTime(self.V1p4adc_update_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Subject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Subject"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Subject"
    class_name: ClassVar[str] = "V1p4Subject"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Subject

    V1p4subject_id: Optional[str] = None
    V1p4synthetic: Optional[Union[bool, Bool]] = None
    V1p4species: Optional[Union[str, "V1p4Species"]] = None
    V1p4sex: Optional[Union[str, "V1p4Sex"]] = None
    V1p4age: Optional[Union[dict, V1p4TimeInterval]] = None
    V1p4age_event: Optional[str] = None
    V1p4ancestry_population: Optional[Union[str, "V1p4AncestryPopulation"]] = None
    V1p4location_birth: Optional[Union[str, "V1p4LocationBirth"]] = None
    V1p4ethnicity: Optional[str] = None
    V1p4race: Optional[str] = None
    V1p4strain_name: Optional[str] = None
    V1p4linked_subjects: Optional[str] = None
    V1p4link_type: Optional[str] = None
    V1p4diagnosis: Optional[Union[Union[dict, "V1p4Diagnosis"], List[Union[dict, "V1p4Diagnosis"]]]] = empty_list()
    V1p4genotype: Optional[Union[dict, V1p4SubjectGenotype]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4subject_id is not None and not isinstance(self.V1p4subject_id, str):
            self.V1p4subject_id = str(self.V1p4subject_id)

        if self.V1p4synthetic is not None and not isinstance(self.V1p4synthetic, Bool):
            self.V1p4synthetic = Bool(self.V1p4synthetic)

        if self.V1p4sex is not None and not isinstance(self.V1p4sex, V1p4Sex):
            self.V1p4sex = V1p4Sex(self.V1p4sex)

        if self.V1p4age is not None and not isinstance(self.V1p4age, V1p4TimeInterval):
            self.V1p4age = V1p4TimeInterval(**as_dict(self.V1p4age))

        if self.V1p4age_event is not None and not isinstance(self.V1p4age_event, str):
            self.V1p4age_event = str(self.V1p4age_event)

        if self.V1p4ethnicity is not None and not isinstance(self.V1p4ethnicity, str):
            self.V1p4ethnicity = str(self.V1p4ethnicity)

        if self.V1p4race is not None and not isinstance(self.V1p4race, str):
            self.V1p4race = str(self.V1p4race)

        if self.V1p4strain_name is not None and not isinstance(self.V1p4strain_name, str):
            self.V1p4strain_name = str(self.V1p4strain_name)

        if self.V1p4linked_subjects is not None and not isinstance(self.V1p4linked_subjects, str):
            self.V1p4linked_subjects = str(self.V1p4linked_subjects)

        if self.V1p4link_type is not None and not isinstance(self.V1p4link_type, str):
            self.V1p4link_type = str(self.V1p4link_type)

        if not isinstance(self.V1p4diagnosis, list):
            self.V1p4diagnosis = [self.V1p4diagnosis] if self.V1p4diagnosis is not None else []
        self.V1p4diagnosis = [v if isinstance(v, V1p4Diagnosis) else V1p4Diagnosis(**as_dict(v)) for v in self.V1p4diagnosis]

        if self.V1p4genotype is not None and not isinstance(self.V1p4genotype, V1p4SubjectGenotype):
            self.V1p4genotype = V1p4SubjectGenotype(**as_dict(self.V1p4genotype))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Diagnosis(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Diagnosis"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Diagnosis"
    class_name: ClassVar[str] = "V1p4Diagnosis"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Diagnosis

    V1p4study_group_description: Optional[str] = None
    V1p4diagnosis_timepoint: Optional[Union[dict, V1p4TimePoint]] = None
    V1p4disease_diagnosis: Optional[Union[str, "V1p4DiseaseDiagnosis"]] = None
    V1p4disease_length: Optional[Union[dict, V1p4TimeQuantity]] = None
    V1p4disease_stage: Optional[str] = None
    V1p4prior_therapies: Optional[str] = None
    V1p4immunogen: Optional[str] = None
    V1p4intervention: Optional[str] = None
    V1p4medical_history: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4study_group_description is not None and not isinstance(self.V1p4study_group_description, str):
            self.V1p4study_group_description = str(self.V1p4study_group_description)

        if self.V1p4diagnosis_timepoint is not None and not isinstance(self.V1p4diagnosis_timepoint, V1p4TimePoint):
            self.V1p4diagnosis_timepoint = V1p4TimePoint(**as_dict(self.V1p4diagnosis_timepoint))

        if self.V1p4disease_length is not None and not isinstance(self.V1p4disease_length, V1p4TimeQuantity):
            self.V1p4disease_length = V1p4TimeQuantity(**as_dict(self.V1p4disease_length))

        if self.V1p4disease_stage is not None and not isinstance(self.V1p4disease_stage, str):
            self.V1p4disease_stage = str(self.V1p4disease_stage)

        if self.V1p4prior_therapies is not None and not isinstance(self.V1p4prior_therapies, str):
            self.V1p4prior_therapies = str(self.V1p4prior_therapies)

        if self.V1p4immunogen is not None and not isinstance(self.V1p4immunogen, str):
            self.V1p4immunogen = str(self.V1p4immunogen)

        if self.V1p4intervention is not None and not isinstance(self.V1p4intervention, str):
            self.V1p4intervention = str(self.V1p4intervention)

        if self.V1p4medical_history is not None and not isinstance(self.V1p4medical_history, str):
            self.V1p4medical_history = str(self.V1p4medical_history)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Sample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Sample"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Sample"
    class_name: ClassVar[str] = "V1p4Sample"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Sample

    V1p4sample_id: Optional[str] = None
    V1p4sample_type: Optional[str] = None
    V1p4tissue: Optional[Union[str, "V1p4Tissue"]] = None
    V1p4anatomic_site: Optional[str] = None
    V1p4disease_state_sample: Optional[str] = None
    V1p4collection_time_point_relative: Optional[Union[dict, V1p4TimePoint]] = None
    V1p4collection_location: Optional[Union[str, "V1p4CollectionLocation"]] = None
    V1p4biomaterial_provider: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4sample_id is not None and not isinstance(self.V1p4sample_id, str):
            self.V1p4sample_id = str(self.V1p4sample_id)

        if self.V1p4sample_type is not None and not isinstance(self.V1p4sample_type, str):
            self.V1p4sample_type = str(self.V1p4sample_type)

        if self.V1p4anatomic_site is not None and not isinstance(self.V1p4anatomic_site, str):
            self.V1p4anatomic_site = str(self.V1p4anatomic_site)

        if self.V1p4disease_state_sample is not None and not isinstance(self.V1p4disease_state_sample, str):
            self.V1p4disease_state_sample = str(self.V1p4disease_state_sample)

        if self.V1p4collection_time_point_relative is not None and not isinstance(self.V1p4collection_time_point_relative, V1p4TimePoint):
            self.V1p4collection_time_point_relative = V1p4TimePoint(**as_dict(self.V1p4collection_time_point_relative))

        if self.V1p4biomaterial_provider is not None and not isinstance(self.V1p4biomaterial_provider, str):
            self.V1p4biomaterial_provider = str(self.V1p4biomaterial_provider)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4CellProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4CellProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4CellProcessing"
    class_name: ClassVar[str] = "V1p4CellProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4CellProcessing

    V1p4tissue_processing: Optional[str] = None
    V1p4cell_subset: Optional[Union[str, "V1p4CellSubset"]] = None
    V1p4cell_phenotype: Optional[str] = None
    V1p4cell_label: Optional[str] = None
    V1p4cell_species: Optional[Union[str, "V1p4CellSpecies"]] = None
    V1p4single_cell: Optional[Union[bool, Bool]] = None
    V1p4cell_number: Optional[int] = None
    V1p4cells_per_reaction: Optional[int] = None
    V1p4cell_storage: Optional[Union[bool, Bool]] = None
    V1p4cell_quality: Optional[str] = None
    V1p4cell_isolation: Optional[str] = None
    V1p4cell_processing_protocol: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4tissue_processing is not None and not isinstance(self.V1p4tissue_processing, str):
            self.V1p4tissue_processing = str(self.V1p4tissue_processing)

        if self.V1p4cell_phenotype is not None and not isinstance(self.V1p4cell_phenotype, str):
            self.V1p4cell_phenotype = str(self.V1p4cell_phenotype)

        if self.V1p4cell_label is not None and not isinstance(self.V1p4cell_label, str):
            self.V1p4cell_label = str(self.V1p4cell_label)

        if self.V1p4single_cell is not None and not isinstance(self.V1p4single_cell, Bool):
            self.V1p4single_cell = Bool(self.V1p4single_cell)

        if self.V1p4cell_number is not None and not isinstance(self.V1p4cell_number, int):
            self.V1p4cell_number = int(self.V1p4cell_number)

        if self.V1p4cells_per_reaction is not None and not isinstance(self.V1p4cells_per_reaction, int):
            self.V1p4cells_per_reaction = int(self.V1p4cells_per_reaction)

        if self.V1p4cell_storage is not None and not isinstance(self.V1p4cell_storage, Bool):
            self.V1p4cell_storage = Bool(self.V1p4cell_storage)

        if self.V1p4cell_quality is not None and not isinstance(self.V1p4cell_quality, str):
            self.V1p4cell_quality = str(self.V1p4cell_quality)

        if self.V1p4cell_isolation is not None and not isinstance(self.V1p4cell_isolation, str):
            self.V1p4cell_isolation = str(self.V1p4cell_isolation)

        if self.V1p4cell_processing_protocol is not None and not isinstance(self.V1p4cell_processing_protocol, str):
            self.V1p4cell_processing_protocol = str(self.V1p4cell_processing_protocol)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4PCRTarget(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4PCRTarget"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4PCRTarget"
    class_name: ClassVar[str] = "V1p4PCRTarget"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4PCRTarget

    V1p4pcr_target_locus: Optional[Union[str, "V1p4PcrTargetLocus"]] = None
    V1p4forward_pcr_primer_target_location: Optional[str] = None
    V1p4reverse_pcr_primer_target_location: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4pcr_target_locus is not None and not isinstance(self.V1p4pcr_target_locus, V1p4PcrTargetLocus):
            self.V1p4pcr_target_locus = V1p4PcrTargetLocus(self.V1p4pcr_target_locus)

        if self.V1p4forward_pcr_primer_target_location is not None and not isinstance(self.V1p4forward_pcr_primer_target_location, str):
            self.V1p4forward_pcr_primer_target_location = str(self.V1p4forward_pcr_primer_target_location)

        if self.V1p4reverse_pcr_primer_target_location is not None and not isinstance(self.V1p4reverse_pcr_primer_target_location, str):
            self.V1p4reverse_pcr_primer_target_location = str(self.V1p4reverse_pcr_primer_target_location)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4NucleicAcidProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4NucleicAcidProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4NucleicAcidProcessing"
    class_name: ClassVar[str] = "V1p4NucleicAcidProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4NucleicAcidProcessing

    V1p4template_class: Optional[Union[str, "V1p4TemplateClass"]] = None
    V1p4template_quality: Optional[str] = None
    V1p4template_amount: Optional[Union[dict, V1p4PhysicalQuantity]] = None
    V1p4library_generation_method: Optional[Union[str, "V1p4LibraryGenerationMethod"]] = None
    V1p4library_generation_protocol: Optional[str] = None
    V1p4library_generation_kit_version: Optional[str] = None
    V1p4pcr_target: Optional[Union[Union[dict, V1p4PCRTarget], List[Union[dict, V1p4PCRTarget]]]] = empty_list()
    V1p4complete_sequences: Optional[Union[str, "V1p4CompleteSequences"]] = None
    V1p4physical_linkage: Optional[Union[str, "V1p4PhysicalLinkage"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4template_class is not None and not isinstance(self.V1p4template_class, V1p4TemplateClass):
            self.V1p4template_class = V1p4TemplateClass(self.V1p4template_class)

        if self.V1p4template_quality is not None and not isinstance(self.V1p4template_quality, str):
            self.V1p4template_quality = str(self.V1p4template_quality)

        if self.V1p4template_amount is not None and not isinstance(self.V1p4template_amount, V1p4PhysicalQuantity):
            self.V1p4template_amount = V1p4PhysicalQuantity(**as_dict(self.V1p4template_amount))

        if self.V1p4library_generation_method is not None and not isinstance(self.V1p4library_generation_method, V1p4LibraryGenerationMethod):
            self.V1p4library_generation_method = V1p4LibraryGenerationMethod(self.V1p4library_generation_method)

        if self.V1p4library_generation_protocol is not None and not isinstance(self.V1p4library_generation_protocol, str):
            self.V1p4library_generation_protocol = str(self.V1p4library_generation_protocol)

        if self.V1p4library_generation_kit_version is not None and not isinstance(self.V1p4library_generation_kit_version, str):
            self.V1p4library_generation_kit_version = str(self.V1p4library_generation_kit_version)

        if not isinstance(self.V1p4pcr_target, list):
            self.V1p4pcr_target = [self.V1p4pcr_target] if self.V1p4pcr_target is not None else []
        self.V1p4pcr_target = [v if isinstance(v, V1p4PCRTarget) else V1p4PCRTarget(**as_dict(v)) for v in self.V1p4pcr_target]

        if self.V1p4complete_sequences is not None and not isinstance(self.V1p4complete_sequences, V1p4CompleteSequences):
            self.V1p4complete_sequences = V1p4CompleteSequences(self.V1p4complete_sequences)

        if self.V1p4physical_linkage is not None and not isinstance(self.V1p4physical_linkage, V1p4PhysicalLinkage):
            self.V1p4physical_linkage = V1p4PhysicalLinkage(self.V1p4physical_linkage)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SequencingRun(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SequencingRun"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SequencingRun"
    class_name: ClassVar[str] = "V1p4SequencingRun"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SequencingRun

    V1p4sequencing_run_id: Optional[str] = None
    V1p4total_reads_passing_qc_filter: Optional[int] = None
    V1p4sequencing_platform: Optional[str] = None
    V1p4sequencing_facility: Optional[str] = None
    V1p4sequencing_run_date: Optional[Union[str, XSDDateTime]] = None
    V1p4sequencing_kit: Optional[str] = None
    V1p4sequencing_files: Optional[Union[dict, "V1p4SequencingData"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4sequencing_run_id is not None and not isinstance(self.V1p4sequencing_run_id, str):
            self.V1p4sequencing_run_id = str(self.V1p4sequencing_run_id)

        if self.V1p4total_reads_passing_qc_filter is not None and not isinstance(self.V1p4total_reads_passing_qc_filter, int):
            self.V1p4total_reads_passing_qc_filter = int(self.V1p4total_reads_passing_qc_filter)

        if self.V1p4sequencing_platform is not None and not isinstance(self.V1p4sequencing_platform, str):
            self.V1p4sequencing_platform = str(self.V1p4sequencing_platform)

        if self.V1p4sequencing_facility is not None and not isinstance(self.V1p4sequencing_facility, str):
            self.V1p4sequencing_facility = str(self.V1p4sequencing_facility)

        if self.V1p4sequencing_run_date is not None and not isinstance(self.V1p4sequencing_run_date, XSDDateTime):
            self.V1p4sequencing_run_date = XSDDateTime(self.V1p4sequencing_run_date)

        if self.V1p4sequencing_kit is not None and not isinstance(self.V1p4sequencing_kit, str):
            self.V1p4sequencing_kit = str(self.V1p4sequencing_kit)

        if self.V1p4sequencing_files is not None and not isinstance(self.V1p4sequencing_files, V1p4SequencingData):
            self.V1p4sequencing_files = V1p4SequencingData(**as_dict(self.V1p4sequencing_files))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SequencingData(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SequencingData"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SequencingData"
    class_name: ClassVar[str] = "V1p4SequencingData"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SequencingData

    V1p4sequencing_data_id: Optional[str] = None
    V1p4file_type: Optional[Union[str, "V1p4FileType"]] = None
    V1p4filename: Optional[str] = None
    V1p4read_direction: Optional[Union[str, "V1p4ReadDirection"]] = None
    V1p4read_length: Optional[int] = None
    V1p4paired_filename: Optional[str] = None
    V1p4paired_read_direction: Optional[Union[str, "V1p4PairedReadDirection"]] = None
    V1p4paired_read_length: Optional[int] = None
    V1p4index_filename: Optional[str] = None
    V1p4index_length: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4sequencing_data_id is not None and not isinstance(self.V1p4sequencing_data_id, str):
            self.V1p4sequencing_data_id = str(self.V1p4sequencing_data_id)

        if self.V1p4file_type is not None and not isinstance(self.V1p4file_type, V1p4FileType):
            self.V1p4file_type = V1p4FileType(self.V1p4file_type)

        if self.V1p4filename is not None and not isinstance(self.V1p4filename, str):
            self.V1p4filename = str(self.V1p4filename)

        if self.V1p4read_direction is not None and not isinstance(self.V1p4read_direction, V1p4ReadDirection):
            self.V1p4read_direction = V1p4ReadDirection(self.V1p4read_direction)

        if self.V1p4read_length is not None and not isinstance(self.V1p4read_length, int):
            self.V1p4read_length = int(self.V1p4read_length)

        if self.V1p4paired_filename is not None and not isinstance(self.V1p4paired_filename, str):
            self.V1p4paired_filename = str(self.V1p4paired_filename)

        if self.V1p4paired_read_direction is not None and not isinstance(self.V1p4paired_read_direction, V1p4PairedReadDirection):
            self.V1p4paired_read_direction = V1p4PairedReadDirection(self.V1p4paired_read_direction)

        if self.V1p4paired_read_length is not None and not isinstance(self.V1p4paired_read_length, int):
            self.V1p4paired_read_length = int(self.V1p4paired_read_length)

        if self.V1p4index_filename is not None and not isinstance(self.V1p4index_filename, str):
            self.V1p4index_filename = str(self.V1p4index_filename)

        if self.V1p4index_length is not None and not isinstance(self.V1p4index_length, int):
            self.V1p4index_length = int(self.V1p4index_length)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4DataProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4DataProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4DataProcessing"
    class_name: ClassVar[str] = "V1p4DataProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4DataProcessing

    V1p4data_processing_id: Optional[str] = None
    V1p4primary_annotation: Optional[Union[bool, Bool]] = None
    V1p4software_versions: Optional[str] = None
    V1p4paired_reads_assembly: Optional[str] = None
    V1p4quality_thresholds: Optional[str] = None
    V1p4primer_match_cutoffs: Optional[str] = None
    V1p4collapsing_method: Optional[str] = None
    V1p4data_processing_protocols: Optional[str] = None
    V1p4data_processing_files: Optional[Union[str, List[str]]] = empty_list()
    V1p4germline_database: Optional[str] = None
    V1p4germline_set_ref: Optional[str] = None
    V1p4analysis_provenance_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4data_processing_id is not None and not isinstance(self.V1p4data_processing_id, str):
            self.V1p4data_processing_id = str(self.V1p4data_processing_id)

        if self.V1p4primary_annotation is not None and not isinstance(self.V1p4primary_annotation, Bool):
            self.V1p4primary_annotation = Bool(self.V1p4primary_annotation)

        if self.V1p4software_versions is not None and not isinstance(self.V1p4software_versions, str):
            self.V1p4software_versions = str(self.V1p4software_versions)

        if self.V1p4paired_reads_assembly is not None and not isinstance(self.V1p4paired_reads_assembly, str):
            self.V1p4paired_reads_assembly = str(self.V1p4paired_reads_assembly)

        if self.V1p4quality_thresholds is not None and not isinstance(self.V1p4quality_thresholds, str):
            self.V1p4quality_thresholds = str(self.V1p4quality_thresholds)

        if self.V1p4primer_match_cutoffs is not None and not isinstance(self.V1p4primer_match_cutoffs, str):
            self.V1p4primer_match_cutoffs = str(self.V1p4primer_match_cutoffs)

        if self.V1p4collapsing_method is not None and not isinstance(self.V1p4collapsing_method, str):
            self.V1p4collapsing_method = str(self.V1p4collapsing_method)

        if self.V1p4data_processing_protocols is not None and not isinstance(self.V1p4data_processing_protocols, str):
            self.V1p4data_processing_protocols = str(self.V1p4data_processing_protocols)

        if not isinstance(self.V1p4data_processing_files, list):
            self.V1p4data_processing_files = [self.V1p4data_processing_files] if self.V1p4data_processing_files is not None else []
        self.V1p4data_processing_files = [v if isinstance(v, str) else str(v) for v in self.V1p4data_processing_files]

        if self.V1p4germline_database is not None and not isinstance(self.V1p4germline_database, str):
            self.V1p4germline_database = str(self.V1p4germline_database)

        if self.V1p4germline_set_ref is not None and not isinstance(self.V1p4germline_set_ref, str):
            self.V1p4germline_set_ref = str(self.V1p4germline_set_ref)

        if self.V1p4analysis_provenance_id is not None and not isinstance(self.V1p4analysis_provenance_id, str):
            self.V1p4analysis_provenance_id = str(self.V1p4analysis_provenance_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Repertoire(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Repertoire"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Repertoire"
    class_name: ClassVar[str] = "V1p4Repertoire"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Repertoire

    V1p4repertoire_id: Optional[str] = None
    V1p4repertoire_name: Optional[str] = None
    V1p4repertoire_description: Optional[str] = None
    V1p4study: Optional[Union[dict, V1p4Study]] = None
    V1p4subject: Optional[Union[dict, V1p4Subject]] = None
    V1p4sample: Optional[Union[Union[dict, "V1p4SampleProcessing"], List[Union[dict, "V1p4SampleProcessing"]]]] = empty_list()
    V1p4data_processing: Optional[Union[Union[dict, V1p4DataProcessing], List[Union[dict, V1p4DataProcessing]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4repertoire_id is not None and not isinstance(self.V1p4repertoire_id, str):
            self.V1p4repertoire_id = str(self.V1p4repertoire_id)

        if self.V1p4repertoire_name is not None and not isinstance(self.V1p4repertoire_name, str):
            self.V1p4repertoire_name = str(self.V1p4repertoire_name)

        if self.V1p4repertoire_description is not None and not isinstance(self.V1p4repertoire_description, str):
            self.V1p4repertoire_description = str(self.V1p4repertoire_description)

        if self.V1p4study is not None and not isinstance(self.V1p4study, V1p4Study):
            self.V1p4study = V1p4Study(**as_dict(self.V1p4study))

        if self.V1p4subject is not None and not isinstance(self.V1p4subject, V1p4Subject):
            self.V1p4subject = V1p4Subject(**as_dict(self.V1p4subject))

        if not isinstance(self.V1p4sample, list):
            self.V1p4sample = [self.V1p4sample] if self.V1p4sample is not None else []
        self.V1p4sample = [v if isinstance(v, V1p4SampleProcessing) else V1p4SampleProcessing(**as_dict(v)) for v in self.V1p4sample]

        if not isinstance(self.V1p4data_processing, list):
            self.V1p4data_processing = [self.V1p4data_processing] if self.V1p4data_processing is not None else []
        self.V1p4data_processing = [v if isinstance(v, V1p4DataProcessing) else V1p4DataProcessing(**as_dict(v)) for v in self.V1p4data_processing]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4RepertoireGroup(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4RepertoireGroup"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4RepertoireGroup"
    class_name: ClassVar[str] = "V1p4RepertoireGroup"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4RepertoireGroup

    V1p4repertoire_group_id: Optional[str] = None
    V1p4repertoire_group_name: Optional[str] = None
    V1p4repertoire_group_description: Optional[str] = None
    V1p4repertoires: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4repertoire_group_id is not None and not isinstance(self.V1p4repertoire_group_id, str):
            self.V1p4repertoire_group_id = str(self.V1p4repertoire_group_id)

        if self.V1p4repertoire_group_name is not None and not isinstance(self.V1p4repertoire_group_name, str):
            self.V1p4repertoire_group_name = str(self.V1p4repertoire_group_name)

        if self.V1p4repertoire_group_description is not None and not isinstance(self.V1p4repertoire_group_description, str):
            self.V1p4repertoire_group_description = str(self.V1p4repertoire_group_description)

        if not isinstance(self.V1p4repertoires, list):
            self.V1p4repertoires = [self.V1p4repertoires] if self.V1p4repertoires is not None else []
        self.V1p4repertoires = [v if isinstance(v, str) else str(v) for v in self.V1p4repertoires]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Alignment(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Alignment"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Alignment"
    class_name: ClassVar[str] = "V1p4Alignment"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Alignment

    V1p4sequence_id: Optional[str] = None
    V1p4segment: Optional[str] = None
    V1p4rev_comp: Optional[Union[bool, Bool]] = None
    V1p4call: Optional[str] = None
    V1p4score: Optional[float] = None
    V1p4identity: Optional[float] = None
    V1p4support: Optional[float] = None
    V1p4cigar: Optional[str] = None
    V1p4sequence_start: Optional[int] = None
    V1p4sequence_end: Optional[int] = None
    V1p4germline_start: Optional[int] = None
    V1p4germline_end: Optional[int] = None
    V1p4rank: Optional[int] = None
    V1p4data_processing_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4sequence_id is not None and not isinstance(self.V1p4sequence_id, str):
            self.V1p4sequence_id = str(self.V1p4sequence_id)

        if self.V1p4segment is not None and not isinstance(self.V1p4segment, str):
            self.V1p4segment = str(self.V1p4segment)

        if self.V1p4rev_comp is not None and not isinstance(self.V1p4rev_comp, Bool):
            self.V1p4rev_comp = Bool(self.V1p4rev_comp)

        if self.V1p4call is not None and not isinstance(self.V1p4call, str):
            self.V1p4call = str(self.V1p4call)

        if self.V1p4score is not None and not isinstance(self.V1p4score, float):
            self.V1p4score = float(self.V1p4score)

        if self.V1p4identity is not None and not isinstance(self.V1p4identity, float):
            self.V1p4identity = float(self.V1p4identity)

        if self.V1p4support is not None and not isinstance(self.V1p4support, float):
            self.V1p4support = float(self.V1p4support)

        if self.V1p4cigar is not None and not isinstance(self.V1p4cigar, str):
            self.V1p4cigar = str(self.V1p4cigar)

        if self.V1p4sequence_start is not None and not isinstance(self.V1p4sequence_start, int):
            self.V1p4sequence_start = int(self.V1p4sequence_start)

        if self.V1p4sequence_end is not None and not isinstance(self.V1p4sequence_end, int):
            self.V1p4sequence_end = int(self.V1p4sequence_end)

        if self.V1p4germline_start is not None and not isinstance(self.V1p4germline_start, int):
            self.V1p4germline_start = int(self.V1p4germline_start)

        if self.V1p4germline_end is not None and not isinstance(self.V1p4germline_end, int):
            self.V1p4germline_end = int(self.V1p4germline_end)

        if self.V1p4rank is not None and not isinstance(self.V1p4rank, int):
            self.V1p4rank = int(self.V1p4rank)

        if self.V1p4data_processing_id is not None and not isinstance(self.V1p4data_processing_id, str):
            self.V1p4data_processing_id = str(self.V1p4data_processing_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Rearrangement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Rearrangement"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Rearrangement"
    class_name: ClassVar[str] = "V1p4Rearrangement"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Rearrangement

    V1p4sequence_id: Optional[str] = None
    V1p4sequence: Optional[str] = None
    V1p4quality: Optional[str] = None
    V1p4sequence_aa: Optional[str] = None
    V1p4rev_comp: Optional[Union[bool, Bool]] = None
    V1p4productive: Optional[Union[bool, Bool]] = None
    V1p4vj_in_frame: Optional[Union[bool, Bool]] = None
    V1p4stop_codon: Optional[Union[bool, Bool]] = None
    V1p4complete_vdj: Optional[Union[bool, Bool]] = None
    V1p4locus: Optional[Union[str, "V1p4Locus"]] = None
    V1p4locus_species: Optional[Union[str, "V1p4LocusSpecies"]] = None
    V1p4v_call: Optional[str] = None
    V1p4d_call: Optional[str] = None
    V1p4d2_call: Optional[str] = None
    V1p4j_call: Optional[str] = None
    V1p4c_call: Optional[str] = None
    V1p4sequence_alignment: Optional[str] = None
    V1p4quality_alignment: Optional[str] = None
    V1p4sequence_alignment_aa: Optional[str] = None
    V1p4germline_alignment: Optional[str] = None
    V1p4germline_alignment_aa: Optional[str] = None
    V1p4junction: Optional[str] = None
    V1p4junction_aa: Optional[str] = None
    V1p4np1: Optional[str] = None
    V1p4np1_aa: Optional[str] = None
    V1p4np2: Optional[str] = None
    V1p4np2_aa: Optional[str] = None
    V1p4np3: Optional[str] = None
    V1p4np3_aa: Optional[str] = None
    V1p4cdr1: Optional[str] = None
    V1p4cdr1_aa: Optional[str] = None
    V1p4cdr2: Optional[str] = None
    V1p4cdr2_aa: Optional[str] = None
    V1p4cdr3: Optional[str] = None
    V1p4cdr3_aa: Optional[str] = None
    V1p4fwr1: Optional[str] = None
    V1p4fwr1_aa: Optional[str] = None
    V1p4fwr2: Optional[str] = None
    V1p4fwr2_aa: Optional[str] = None
    V1p4fwr3: Optional[str] = None
    V1p4fwr3_aa: Optional[str] = None
    V1p4fwr4: Optional[str] = None
    V1p4fwr4_aa: Optional[str] = None
    V1p4v_score: Optional[float] = None
    V1p4v_identity: Optional[float] = None
    V1p4v_support: Optional[float] = None
    V1p4v_cigar: Optional[str] = None
    V1p4d_score: Optional[float] = None
    V1p4d_identity: Optional[float] = None
    V1p4d_support: Optional[float] = None
    V1p4d_cigar: Optional[str] = None
    V1p4d2_score: Optional[float] = None
    V1p4d2_identity: Optional[float] = None
    V1p4d2_support: Optional[float] = None
    V1p4d2_cigar: Optional[str] = None
    V1p4j_score: Optional[float] = None
    V1p4j_identity: Optional[float] = None
    V1p4j_support: Optional[float] = None
    V1p4j_cigar: Optional[str] = None
    V1p4c_score: Optional[float] = None
    V1p4c_identity: Optional[float] = None
    V1p4c_support: Optional[float] = None
    V1p4c_cigar: Optional[str] = None
    V1p4v_sequence_start: Optional[int] = None
    V1p4v_sequence_end: Optional[int] = None
    V1p4v_germline_start: Optional[int] = None
    V1p4v_germline_end: Optional[int] = None
    V1p4v_alignment_start: Optional[int] = None
    V1p4v_alignment_end: Optional[int] = None
    V1p4d_sequence_start: Optional[int] = None
    V1p4d_sequence_end: Optional[int] = None
    V1p4d_germline_start: Optional[int] = None
    V1p4d_germline_end: Optional[int] = None
    V1p4d_alignment_start: Optional[int] = None
    V1p4d_alignment_end: Optional[int] = None
    V1p4d2_sequence_start: Optional[int] = None
    V1p4d2_sequence_end: Optional[int] = None
    V1p4d2_germline_start: Optional[int] = None
    V1p4d2_germline_end: Optional[int] = None
    V1p4d2_alignment_start: Optional[int] = None
    V1p4d2_alignment_end: Optional[int] = None
    V1p4j_sequence_start: Optional[int] = None
    V1p4j_sequence_end: Optional[int] = None
    V1p4j_germline_start: Optional[int] = None
    V1p4j_germline_end: Optional[int] = None
    V1p4j_alignment_start: Optional[int] = None
    V1p4j_alignment_end: Optional[int] = None
    V1p4c_sequence_start: Optional[int] = None
    V1p4c_sequence_end: Optional[int] = None
    V1p4c_germline_start: Optional[int] = None
    V1p4c_germline_end: Optional[int] = None
    V1p4c_alignment_start: Optional[int] = None
    V1p4c_alignment_end: Optional[int] = None
    V1p4cdr1_start: Optional[int] = None
    V1p4cdr1_end: Optional[int] = None
    V1p4cdr2_start: Optional[int] = None
    V1p4cdr2_end: Optional[int] = None
    V1p4cdr3_start: Optional[int] = None
    V1p4cdr3_end: Optional[int] = None
    V1p4fwr1_start: Optional[int] = None
    V1p4fwr1_end: Optional[int] = None
    V1p4fwr2_start: Optional[int] = None
    V1p4fwr2_end: Optional[int] = None
    V1p4fwr3_start: Optional[int] = None
    V1p4fwr3_end: Optional[int] = None
    V1p4fwr4_start: Optional[int] = None
    V1p4fwr4_end: Optional[int] = None
    V1p4v_sequence_alignment: Optional[str] = None
    V1p4v_sequence_alignment_aa: Optional[str] = None
    V1p4d_sequence_alignment: Optional[str] = None
    V1p4d_sequence_alignment_aa: Optional[str] = None
    V1p4d2_sequence_alignment: Optional[str] = None
    V1p4d2_sequence_alignment_aa: Optional[str] = None
    V1p4j_sequence_alignment: Optional[str] = None
    V1p4j_sequence_alignment_aa: Optional[str] = None
    V1p4c_sequence_alignment: Optional[str] = None
    V1p4c_sequence_alignment_aa: Optional[str] = None
    V1p4v_germline_alignment: Optional[str] = None
    V1p4v_germline_alignment_aa: Optional[str] = None
    V1p4d_germline_alignment: Optional[str] = None
    V1p4d_germline_alignment_aa: Optional[str] = None
    V1p4d2_germline_alignment: Optional[str] = None
    V1p4d2_germline_alignment_aa: Optional[str] = None
    V1p4j_germline_alignment: Optional[str] = None
    V1p4j_germline_alignment_aa: Optional[str] = None
    V1p4c_germline_alignment: Optional[str] = None
    V1p4c_germline_alignment_aa: Optional[str] = None
    V1p4junction_length: Optional[int] = None
    V1p4junction_aa_length: Optional[int] = None
    V1p4np1_length: Optional[int] = None
    V1p4np2_length: Optional[int] = None
    V1p4np3_length: Optional[int] = None
    V1p4n1_length: Optional[int] = None
    V1p4n2_length: Optional[int] = None
    V1p4n3_length: Optional[int] = None
    V1p4p3v_length: Optional[int] = None
    V1p4p5d_length: Optional[int] = None
    V1p4p3d_length: Optional[int] = None
    V1p4p5d2_length: Optional[int] = None
    V1p4p3d2_length: Optional[int] = None
    V1p4p5j_length: Optional[int] = None
    V1p4v_frameshift: Optional[Union[bool, Bool]] = None
    V1p4j_frameshift: Optional[Union[bool, Bool]] = None
    V1p4d_frame: Optional[int] = None
    V1p4d2_frame: Optional[int] = None
    V1p4consensus_count: Optional[int] = None
    V1p4duplicate_count: Optional[int] = None
    V1p4umi_count: Optional[int] = None
    V1p4cell_id: Optional[str] = None
    V1p4clone_id: Optional[str] = None
    V1p4reactivity_id: Optional[str] = None
    V1p4reactivity_ref: Optional[str] = None
    V1p4repertoire_id: Optional[str] = None
    V1p4sample_processing_id: Optional[str] = None
    V1p4data_processing_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4sequence_id is not None and not isinstance(self.V1p4sequence_id, str):
            self.V1p4sequence_id = str(self.V1p4sequence_id)

        if self.V1p4sequence is not None and not isinstance(self.V1p4sequence, str):
            self.V1p4sequence = str(self.V1p4sequence)

        if self.V1p4quality is not None and not isinstance(self.V1p4quality, str):
            self.V1p4quality = str(self.V1p4quality)

        if self.V1p4sequence_aa is not None and not isinstance(self.V1p4sequence_aa, str):
            self.V1p4sequence_aa = str(self.V1p4sequence_aa)

        if self.V1p4rev_comp is not None and not isinstance(self.V1p4rev_comp, Bool):
            self.V1p4rev_comp = Bool(self.V1p4rev_comp)

        if self.V1p4productive is not None and not isinstance(self.V1p4productive, Bool):
            self.V1p4productive = Bool(self.V1p4productive)

        if self.V1p4vj_in_frame is not None and not isinstance(self.V1p4vj_in_frame, Bool):
            self.V1p4vj_in_frame = Bool(self.V1p4vj_in_frame)

        if self.V1p4stop_codon is not None and not isinstance(self.V1p4stop_codon, Bool):
            self.V1p4stop_codon = Bool(self.V1p4stop_codon)

        if self.V1p4complete_vdj is not None and not isinstance(self.V1p4complete_vdj, Bool):
            self.V1p4complete_vdj = Bool(self.V1p4complete_vdj)

        if self.V1p4locus is not None and not isinstance(self.V1p4locus, V1p4Locus):
            self.V1p4locus = V1p4Locus(self.V1p4locus)

        if self.V1p4v_call is not None and not isinstance(self.V1p4v_call, str):
            self.V1p4v_call = str(self.V1p4v_call)

        if self.V1p4d_call is not None and not isinstance(self.V1p4d_call, str):
            self.V1p4d_call = str(self.V1p4d_call)

        if self.V1p4d2_call is not None and not isinstance(self.V1p4d2_call, str):
            self.V1p4d2_call = str(self.V1p4d2_call)

        if self.V1p4j_call is not None and not isinstance(self.V1p4j_call, str):
            self.V1p4j_call = str(self.V1p4j_call)

        if self.V1p4c_call is not None and not isinstance(self.V1p4c_call, str):
            self.V1p4c_call = str(self.V1p4c_call)

        if self.V1p4sequence_alignment is not None and not isinstance(self.V1p4sequence_alignment, str):
            self.V1p4sequence_alignment = str(self.V1p4sequence_alignment)

        if self.V1p4quality_alignment is not None and not isinstance(self.V1p4quality_alignment, str):
            self.V1p4quality_alignment = str(self.V1p4quality_alignment)

        if self.V1p4sequence_alignment_aa is not None and not isinstance(self.V1p4sequence_alignment_aa, str):
            self.V1p4sequence_alignment_aa = str(self.V1p4sequence_alignment_aa)

        if self.V1p4germline_alignment is not None and not isinstance(self.V1p4germline_alignment, str):
            self.V1p4germline_alignment = str(self.V1p4germline_alignment)

        if self.V1p4germline_alignment_aa is not None and not isinstance(self.V1p4germline_alignment_aa, str):
            self.V1p4germline_alignment_aa = str(self.V1p4germline_alignment_aa)

        if self.V1p4junction is not None and not isinstance(self.V1p4junction, str):
            self.V1p4junction = str(self.V1p4junction)

        if self.V1p4junction_aa is not None and not isinstance(self.V1p4junction_aa, str):
            self.V1p4junction_aa = str(self.V1p4junction_aa)

        if self.V1p4np1 is not None and not isinstance(self.V1p4np1, str):
            self.V1p4np1 = str(self.V1p4np1)

        if self.V1p4np1_aa is not None and not isinstance(self.V1p4np1_aa, str):
            self.V1p4np1_aa = str(self.V1p4np1_aa)

        if self.V1p4np2 is not None and not isinstance(self.V1p4np2, str):
            self.V1p4np2 = str(self.V1p4np2)

        if self.V1p4np2_aa is not None and not isinstance(self.V1p4np2_aa, str):
            self.V1p4np2_aa = str(self.V1p4np2_aa)

        if self.V1p4np3 is not None and not isinstance(self.V1p4np3, str):
            self.V1p4np3 = str(self.V1p4np3)

        if self.V1p4np3_aa is not None and not isinstance(self.V1p4np3_aa, str):
            self.V1p4np3_aa = str(self.V1p4np3_aa)

        if self.V1p4cdr1 is not None and not isinstance(self.V1p4cdr1, str):
            self.V1p4cdr1 = str(self.V1p4cdr1)

        if self.V1p4cdr1_aa is not None and not isinstance(self.V1p4cdr1_aa, str):
            self.V1p4cdr1_aa = str(self.V1p4cdr1_aa)

        if self.V1p4cdr2 is not None and not isinstance(self.V1p4cdr2, str):
            self.V1p4cdr2 = str(self.V1p4cdr2)

        if self.V1p4cdr2_aa is not None and not isinstance(self.V1p4cdr2_aa, str):
            self.V1p4cdr2_aa = str(self.V1p4cdr2_aa)

        if self.V1p4cdr3 is not None and not isinstance(self.V1p4cdr3, str):
            self.V1p4cdr3 = str(self.V1p4cdr3)

        if self.V1p4cdr3_aa is not None and not isinstance(self.V1p4cdr3_aa, str):
            self.V1p4cdr3_aa = str(self.V1p4cdr3_aa)

        if self.V1p4fwr1 is not None and not isinstance(self.V1p4fwr1, str):
            self.V1p4fwr1 = str(self.V1p4fwr1)

        if self.V1p4fwr1_aa is not None and not isinstance(self.V1p4fwr1_aa, str):
            self.V1p4fwr1_aa = str(self.V1p4fwr1_aa)

        if self.V1p4fwr2 is not None and not isinstance(self.V1p4fwr2, str):
            self.V1p4fwr2 = str(self.V1p4fwr2)

        if self.V1p4fwr2_aa is not None and not isinstance(self.V1p4fwr2_aa, str):
            self.V1p4fwr2_aa = str(self.V1p4fwr2_aa)

        if self.V1p4fwr3 is not None and not isinstance(self.V1p4fwr3, str):
            self.V1p4fwr3 = str(self.V1p4fwr3)

        if self.V1p4fwr3_aa is not None and not isinstance(self.V1p4fwr3_aa, str):
            self.V1p4fwr3_aa = str(self.V1p4fwr3_aa)

        if self.V1p4fwr4 is not None and not isinstance(self.V1p4fwr4, str):
            self.V1p4fwr4 = str(self.V1p4fwr4)

        if self.V1p4fwr4_aa is not None and not isinstance(self.V1p4fwr4_aa, str):
            self.V1p4fwr4_aa = str(self.V1p4fwr4_aa)

        if self.V1p4v_score is not None and not isinstance(self.V1p4v_score, float):
            self.V1p4v_score = float(self.V1p4v_score)

        if self.V1p4v_identity is not None and not isinstance(self.V1p4v_identity, float):
            self.V1p4v_identity = float(self.V1p4v_identity)

        if self.V1p4v_support is not None and not isinstance(self.V1p4v_support, float):
            self.V1p4v_support = float(self.V1p4v_support)

        if self.V1p4v_cigar is not None and not isinstance(self.V1p4v_cigar, str):
            self.V1p4v_cigar = str(self.V1p4v_cigar)

        if self.V1p4d_score is not None and not isinstance(self.V1p4d_score, float):
            self.V1p4d_score = float(self.V1p4d_score)

        if self.V1p4d_identity is not None and not isinstance(self.V1p4d_identity, float):
            self.V1p4d_identity = float(self.V1p4d_identity)

        if self.V1p4d_support is not None and not isinstance(self.V1p4d_support, float):
            self.V1p4d_support = float(self.V1p4d_support)

        if self.V1p4d_cigar is not None and not isinstance(self.V1p4d_cigar, str):
            self.V1p4d_cigar = str(self.V1p4d_cigar)

        if self.V1p4d2_score is not None and not isinstance(self.V1p4d2_score, float):
            self.V1p4d2_score = float(self.V1p4d2_score)

        if self.V1p4d2_identity is not None and not isinstance(self.V1p4d2_identity, float):
            self.V1p4d2_identity = float(self.V1p4d2_identity)

        if self.V1p4d2_support is not None and not isinstance(self.V1p4d2_support, float):
            self.V1p4d2_support = float(self.V1p4d2_support)

        if self.V1p4d2_cigar is not None and not isinstance(self.V1p4d2_cigar, str):
            self.V1p4d2_cigar = str(self.V1p4d2_cigar)

        if self.V1p4j_score is not None and not isinstance(self.V1p4j_score, float):
            self.V1p4j_score = float(self.V1p4j_score)

        if self.V1p4j_identity is not None and not isinstance(self.V1p4j_identity, float):
            self.V1p4j_identity = float(self.V1p4j_identity)

        if self.V1p4j_support is not None and not isinstance(self.V1p4j_support, float):
            self.V1p4j_support = float(self.V1p4j_support)

        if self.V1p4j_cigar is not None and not isinstance(self.V1p4j_cigar, str):
            self.V1p4j_cigar = str(self.V1p4j_cigar)

        if self.V1p4c_score is not None and not isinstance(self.V1p4c_score, float):
            self.V1p4c_score = float(self.V1p4c_score)

        if self.V1p4c_identity is not None and not isinstance(self.V1p4c_identity, float):
            self.V1p4c_identity = float(self.V1p4c_identity)

        if self.V1p4c_support is not None and not isinstance(self.V1p4c_support, float):
            self.V1p4c_support = float(self.V1p4c_support)

        if self.V1p4c_cigar is not None and not isinstance(self.V1p4c_cigar, str):
            self.V1p4c_cigar = str(self.V1p4c_cigar)

        if self.V1p4v_sequence_start is not None and not isinstance(self.V1p4v_sequence_start, int):
            self.V1p4v_sequence_start = int(self.V1p4v_sequence_start)

        if self.V1p4v_sequence_end is not None and not isinstance(self.V1p4v_sequence_end, int):
            self.V1p4v_sequence_end = int(self.V1p4v_sequence_end)

        if self.V1p4v_germline_start is not None and not isinstance(self.V1p4v_germline_start, int):
            self.V1p4v_germline_start = int(self.V1p4v_germline_start)

        if self.V1p4v_germline_end is not None and not isinstance(self.V1p4v_germline_end, int):
            self.V1p4v_germline_end = int(self.V1p4v_germline_end)

        if self.V1p4v_alignment_start is not None and not isinstance(self.V1p4v_alignment_start, int):
            self.V1p4v_alignment_start = int(self.V1p4v_alignment_start)

        if self.V1p4v_alignment_end is not None and not isinstance(self.V1p4v_alignment_end, int):
            self.V1p4v_alignment_end = int(self.V1p4v_alignment_end)

        if self.V1p4d_sequence_start is not None and not isinstance(self.V1p4d_sequence_start, int):
            self.V1p4d_sequence_start = int(self.V1p4d_sequence_start)

        if self.V1p4d_sequence_end is not None and not isinstance(self.V1p4d_sequence_end, int):
            self.V1p4d_sequence_end = int(self.V1p4d_sequence_end)

        if self.V1p4d_germline_start is not None and not isinstance(self.V1p4d_germline_start, int):
            self.V1p4d_germline_start = int(self.V1p4d_germline_start)

        if self.V1p4d_germline_end is not None and not isinstance(self.V1p4d_germline_end, int):
            self.V1p4d_germline_end = int(self.V1p4d_germline_end)

        if self.V1p4d_alignment_start is not None and not isinstance(self.V1p4d_alignment_start, int):
            self.V1p4d_alignment_start = int(self.V1p4d_alignment_start)

        if self.V1p4d_alignment_end is not None and not isinstance(self.V1p4d_alignment_end, int):
            self.V1p4d_alignment_end = int(self.V1p4d_alignment_end)

        if self.V1p4d2_sequence_start is not None and not isinstance(self.V1p4d2_sequence_start, int):
            self.V1p4d2_sequence_start = int(self.V1p4d2_sequence_start)

        if self.V1p4d2_sequence_end is not None and not isinstance(self.V1p4d2_sequence_end, int):
            self.V1p4d2_sequence_end = int(self.V1p4d2_sequence_end)

        if self.V1p4d2_germline_start is not None and not isinstance(self.V1p4d2_germline_start, int):
            self.V1p4d2_germline_start = int(self.V1p4d2_germline_start)

        if self.V1p4d2_germline_end is not None and not isinstance(self.V1p4d2_germline_end, int):
            self.V1p4d2_germline_end = int(self.V1p4d2_germline_end)

        if self.V1p4d2_alignment_start is not None and not isinstance(self.V1p4d2_alignment_start, int):
            self.V1p4d2_alignment_start = int(self.V1p4d2_alignment_start)

        if self.V1p4d2_alignment_end is not None and not isinstance(self.V1p4d2_alignment_end, int):
            self.V1p4d2_alignment_end = int(self.V1p4d2_alignment_end)

        if self.V1p4j_sequence_start is not None and not isinstance(self.V1p4j_sequence_start, int):
            self.V1p4j_sequence_start = int(self.V1p4j_sequence_start)

        if self.V1p4j_sequence_end is not None and not isinstance(self.V1p4j_sequence_end, int):
            self.V1p4j_sequence_end = int(self.V1p4j_sequence_end)

        if self.V1p4j_germline_start is not None and not isinstance(self.V1p4j_germline_start, int):
            self.V1p4j_germline_start = int(self.V1p4j_germline_start)

        if self.V1p4j_germline_end is not None and not isinstance(self.V1p4j_germline_end, int):
            self.V1p4j_germline_end = int(self.V1p4j_germline_end)

        if self.V1p4j_alignment_start is not None and not isinstance(self.V1p4j_alignment_start, int):
            self.V1p4j_alignment_start = int(self.V1p4j_alignment_start)

        if self.V1p4j_alignment_end is not None and not isinstance(self.V1p4j_alignment_end, int):
            self.V1p4j_alignment_end = int(self.V1p4j_alignment_end)

        if self.V1p4c_sequence_start is not None and not isinstance(self.V1p4c_sequence_start, int):
            self.V1p4c_sequence_start = int(self.V1p4c_sequence_start)

        if self.V1p4c_sequence_end is not None and not isinstance(self.V1p4c_sequence_end, int):
            self.V1p4c_sequence_end = int(self.V1p4c_sequence_end)

        if self.V1p4c_germline_start is not None and not isinstance(self.V1p4c_germline_start, int):
            self.V1p4c_germline_start = int(self.V1p4c_germline_start)

        if self.V1p4c_germline_end is not None and not isinstance(self.V1p4c_germline_end, int):
            self.V1p4c_germline_end = int(self.V1p4c_germline_end)

        if self.V1p4c_alignment_start is not None and not isinstance(self.V1p4c_alignment_start, int):
            self.V1p4c_alignment_start = int(self.V1p4c_alignment_start)

        if self.V1p4c_alignment_end is not None and not isinstance(self.V1p4c_alignment_end, int):
            self.V1p4c_alignment_end = int(self.V1p4c_alignment_end)

        if self.V1p4cdr1_start is not None and not isinstance(self.V1p4cdr1_start, int):
            self.V1p4cdr1_start = int(self.V1p4cdr1_start)

        if self.V1p4cdr1_end is not None and not isinstance(self.V1p4cdr1_end, int):
            self.V1p4cdr1_end = int(self.V1p4cdr1_end)

        if self.V1p4cdr2_start is not None and not isinstance(self.V1p4cdr2_start, int):
            self.V1p4cdr2_start = int(self.V1p4cdr2_start)

        if self.V1p4cdr2_end is not None and not isinstance(self.V1p4cdr2_end, int):
            self.V1p4cdr2_end = int(self.V1p4cdr2_end)

        if self.V1p4cdr3_start is not None and not isinstance(self.V1p4cdr3_start, int):
            self.V1p4cdr3_start = int(self.V1p4cdr3_start)

        if self.V1p4cdr3_end is not None and not isinstance(self.V1p4cdr3_end, int):
            self.V1p4cdr3_end = int(self.V1p4cdr3_end)

        if self.V1p4fwr1_start is not None and not isinstance(self.V1p4fwr1_start, int):
            self.V1p4fwr1_start = int(self.V1p4fwr1_start)

        if self.V1p4fwr1_end is not None and not isinstance(self.V1p4fwr1_end, int):
            self.V1p4fwr1_end = int(self.V1p4fwr1_end)

        if self.V1p4fwr2_start is not None and not isinstance(self.V1p4fwr2_start, int):
            self.V1p4fwr2_start = int(self.V1p4fwr2_start)

        if self.V1p4fwr2_end is not None and not isinstance(self.V1p4fwr2_end, int):
            self.V1p4fwr2_end = int(self.V1p4fwr2_end)

        if self.V1p4fwr3_start is not None and not isinstance(self.V1p4fwr3_start, int):
            self.V1p4fwr3_start = int(self.V1p4fwr3_start)

        if self.V1p4fwr3_end is not None and not isinstance(self.V1p4fwr3_end, int):
            self.V1p4fwr3_end = int(self.V1p4fwr3_end)

        if self.V1p4fwr4_start is not None and not isinstance(self.V1p4fwr4_start, int):
            self.V1p4fwr4_start = int(self.V1p4fwr4_start)

        if self.V1p4fwr4_end is not None and not isinstance(self.V1p4fwr4_end, int):
            self.V1p4fwr4_end = int(self.V1p4fwr4_end)

        if self.V1p4v_sequence_alignment is not None and not isinstance(self.V1p4v_sequence_alignment, str):
            self.V1p4v_sequence_alignment = str(self.V1p4v_sequence_alignment)

        if self.V1p4v_sequence_alignment_aa is not None and not isinstance(self.V1p4v_sequence_alignment_aa, str):
            self.V1p4v_sequence_alignment_aa = str(self.V1p4v_sequence_alignment_aa)

        if self.V1p4d_sequence_alignment is not None and not isinstance(self.V1p4d_sequence_alignment, str):
            self.V1p4d_sequence_alignment = str(self.V1p4d_sequence_alignment)

        if self.V1p4d_sequence_alignment_aa is not None and not isinstance(self.V1p4d_sequence_alignment_aa, str):
            self.V1p4d_sequence_alignment_aa = str(self.V1p4d_sequence_alignment_aa)

        if self.V1p4d2_sequence_alignment is not None and not isinstance(self.V1p4d2_sequence_alignment, str):
            self.V1p4d2_sequence_alignment = str(self.V1p4d2_sequence_alignment)

        if self.V1p4d2_sequence_alignment_aa is not None and not isinstance(self.V1p4d2_sequence_alignment_aa, str):
            self.V1p4d2_sequence_alignment_aa = str(self.V1p4d2_sequence_alignment_aa)

        if self.V1p4j_sequence_alignment is not None and not isinstance(self.V1p4j_sequence_alignment, str):
            self.V1p4j_sequence_alignment = str(self.V1p4j_sequence_alignment)

        if self.V1p4j_sequence_alignment_aa is not None and not isinstance(self.V1p4j_sequence_alignment_aa, str):
            self.V1p4j_sequence_alignment_aa = str(self.V1p4j_sequence_alignment_aa)

        if self.V1p4c_sequence_alignment is not None and not isinstance(self.V1p4c_sequence_alignment, str):
            self.V1p4c_sequence_alignment = str(self.V1p4c_sequence_alignment)

        if self.V1p4c_sequence_alignment_aa is not None and not isinstance(self.V1p4c_sequence_alignment_aa, str):
            self.V1p4c_sequence_alignment_aa = str(self.V1p4c_sequence_alignment_aa)

        if self.V1p4v_germline_alignment is not None and not isinstance(self.V1p4v_germline_alignment, str):
            self.V1p4v_germline_alignment = str(self.V1p4v_germline_alignment)

        if self.V1p4v_germline_alignment_aa is not None and not isinstance(self.V1p4v_germline_alignment_aa, str):
            self.V1p4v_germline_alignment_aa = str(self.V1p4v_germline_alignment_aa)

        if self.V1p4d_germline_alignment is not None and not isinstance(self.V1p4d_germline_alignment, str):
            self.V1p4d_germline_alignment = str(self.V1p4d_germline_alignment)

        if self.V1p4d_germline_alignment_aa is not None and not isinstance(self.V1p4d_germline_alignment_aa, str):
            self.V1p4d_germline_alignment_aa = str(self.V1p4d_germline_alignment_aa)

        if self.V1p4d2_germline_alignment is not None and not isinstance(self.V1p4d2_germline_alignment, str):
            self.V1p4d2_germline_alignment = str(self.V1p4d2_germline_alignment)

        if self.V1p4d2_germline_alignment_aa is not None and not isinstance(self.V1p4d2_germline_alignment_aa, str):
            self.V1p4d2_germline_alignment_aa = str(self.V1p4d2_germline_alignment_aa)

        if self.V1p4j_germline_alignment is not None and not isinstance(self.V1p4j_germline_alignment, str):
            self.V1p4j_germline_alignment = str(self.V1p4j_germline_alignment)

        if self.V1p4j_germline_alignment_aa is not None and not isinstance(self.V1p4j_germline_alignment_aa, str):
            self.V1p4j_germline_alignment_aa = str(self.V1p4j_germline_alignment_aa)

        if self.V1p4c_germline_alignment is not None and not isinstance(self.V1p4c_germline_alignment, str):
            self.V1p4c_germline_alignment = str(self.V1p4c_germline_alignment)

        if self.V1p4c_germline_alignment_aa is not None and not isinstance(self.V1p4c_germline_alignment_aa, str):
            self.V1p4c_germline_alignment_aa = str(self.V1p4c_germline_alignment_aa)

        if self.V1p4junction_length is not None and not isinstance(self.V1p4junction_length, int):
            self.V1p4junction_length = int(self.V1p4junction_length)

        if self.V1p4junction_aa_length is not None and not isinstance(self.V1p4junction_aa_length, int):
            self.V1p4junction_aa_length = int(self.V1p4junction_aa_length)

        if self.V1p4np1_length is not None and not isinstance(self.V1p4np1_length, int):
            self.V1p4np1_length = int(self.V1p4np1_length)

        if self.V1p4np2_length is not None and not isinstance(self.V1p4np2_length, int):
            self.V1p4np2_length = int(self.V1p4np2_length)

        if self.V1p4np3_length is not None and not isinstance(self.V1p4np3_length, int):
            self.V1p4np3_length = int(self.V1p4np3_length)

        if self.V1p4n1_length is not None and not isinstance(self.V1p4n1_length, int):
            self.V1p4n1_length = int(self.V1p4n1_length)

        if self.V1p4n2_length is not None and not isinstance(self.V1p4n2_length, int):
            self.V1p4n2_length = int(self.V1p4n2_length)

        if self.V1p4n3_length is not None and not isinstance(self.V1p4n3_length, int):
            self.V1p4n3_length = int(self.V1p4n3_length)

        if self.V1p4p3v_length is not None and not isinstance(self.V1p4p3v_length, int):
            self.V1p4p3v_length = int(self.V1p4p3v_length)

        if self.V1p4p5d_length is not None and not isinstance(self.V1p4p5d_length, int):
            self.V1p4p5d_length = int(self.V1p4p5d_length)

        if self.V1p4p3d_length is not None and not isinstance(self.V1p4p3d_length, int):
            self.V1p4p3d_length = int(self.V1p4p3d_length)

        if self.V1p4p5d2_length is not None and not isinstance(self.V1p4p5d2_length, int):
            self.V1p4p5d2_length = int(self.V1p4p5d2_length)

        if self.V1p4p3d2_length is not None and not isinstance(self.V1p4p3d2_length, int):
            self.V1p4p3d2_length = int(self.V1p4p3d2_length)

        if self.V1p4p5j_length is not None and not isinstance(self.V1p4p5j_length, int):
            self.V1p4p5j_length = int(self.V1p4p5j_length)

        if self.V1p4v_frameshift is not None and not isinstance(self.V1p4v_frameshift, Bool):
            self.V1p4v_frameshift = Bool(self.V1p4v_frameshift)

        if self.V1p4j_frameshift is not None and not isinstance(self.V1p4j_frameshift, Bool):
            self.V1p4j_frameshift = Bool(self.V1p4j_frameshift)

        if self.V1p4d_frame is not None and not isinstance(self.V1p4d_frame, int):
            self.V1p4d_frame = int(self.V1p4d_frame)

        if self.V1p4d2_frame is not None and not isinstance(self.V1p4d2_frame, int):
            self.V1p4d2_frame = int(self.V1p4d2_frame)

        if self.V1p4consensus_count is not None and not isinstance(self.V1p4consensus_count, int):
            self.V1p4consensus_count = int(self.V1p4consensus_count)

        if self.V1p4duplicate_count is not None and not isinstance(self.V1p4duplicate_count, int):
            self.V1p4duplicate_count = int(self.V1p4duplicate_count)

        if self.V1p4umi_count is not None and not isinstance(self.V1p4umi_count, int):
            self.V1p4umi_count = int(self.V1p4umi_count)

        if self.V1p4cell_id is not None and not isinstance(self.V1p4cell_id, str):
            self.V1p4cell_id = str(self.V1p4cell_id)

        if self.V1p4clone_id is not None and not isinstance(self.V1p4clone_id, str):
            self.V1p4clone_id = str(self.V1p4clone_id)

        if self.V1p4reactivity_id is not None and not isinstance(self.V1p4reactivity_id, str):
            self.V1p4reactivity_id = str(self.V1p4reactivity_id)

        if self.V1p4reactivity_ref is not None and not isinstance(self.V1p4reactivity_ref, str):
            self.V1p4reactivity_ref = str(self.V1p4reactivity_ref)

        if self.V1p4repertoire_id is not None and not isinstance(self.V1p4repertoire_id, str):
            self.V1p4repertoire_id = str(self.V1p4repertoire_id)

        if self.V1p4sample_processing_id is not None and not isinstance(self.V1p4sample_processing_id, str):
            self.V1p4sample_processing_id = str(self.V1p4sample_processing_id)

        if self.V1p4data_processing_id is not None and not isinstance(self.V1p4data_processing_id, str):
            self.V1p4data_processing_id = str(self.V1p4data_processing_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Clone(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Clone"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Clone"
    class_name: ClassVar[str] = "V1p4Clone"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Clone

    V1p4clone_id: Optional[str] = None
    V1p4repertoire_id: Optional[str] = None
    V1p4data_processing_id: Optional[str] = None
    V1p4sequences: Optional[Union[str, List[str]]] = empty_list()
    V1p4v_call: Optional[str] = None
    V1p4d_call: Optional[str] = None
    V1p4j_call: Optional[str] = None
    V1p4junction: Optional[str] = None
    V1p4junction_aa: Optional[str] = None
    V1p4junction_length: Optional[int] = None
    V1p4junction_aa_length: Optional[int] = None
    V1p4germline_alignment: Optional[str] = None
    V1p4germline_alignment_aa: Optional[str] = None
    V1p4v_alignment_start: Optional[int] = None
    V1p4v_alignment_end: Optional[int] = None
    V1p4d_alignment_start: Optional[int] = None
    V1p4d_alignment_end: Optional[int] = None
    V1p4j_alignment_start: Optional[int] = None
    V1p4j_alignment_end: Optional[int] = None
    V1p4junction_start: Optional[int] = None
    V1p4junction_end: Optional[int] = None
    V1p4umi_count: Optional[int] = None
    V1p4clone_count: Optional[int] = None
    V1p4seed_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4clone_id is not None and not isinstance(self.V1p4clone_id, str):
            self.V1p4clone_id = str(self.V1p4clone_id)

        if self.V1p4repertoire_id is not None and not isinstance(self.V1p4repertoire_id, str):
            self.V1p4repertoire_id = str(self.V1p4repertoire_id)

        if self.V1p4data_processing_id is not None and not isinstance(self.V1p4data_processing_id, str):
            self.V1p4data_processing_id = str(self.V1p4data_processing_id)

        if not isinstance(self.V1p4sequences, list):
            self.V1p4sequences = [self.V1p4sequences] if self.V1p4sequences is not None else []
        self.V1p4sequences = [v if isinstance(v, str) else str(v) for v in self.V1p4sequences]

        if self.V1p4v_call is not None and not isinstance(self.V1p4v_call, str):
            self.V1p4v_call = str(self.V1p4v_call)

        if self.V1p4d_call is not None and not isinstance(self.V1p4d_call, str):
            self.V1p4d_call = str(self.V1p4d_call)

        if self.V1p4j_call is not None and not isinstance(self.V1p4j_call, str):
            self.V1p4j_call = str(self.V1p4j_call)

        if self.V1p4junction is not None and not isinstance(self.V1p4junction, str):
            self.V1p4junction = str(self.V1p4junction)

        if self.V1p4junction_aa is not None and not isinstance(self.V1p4junction_aa, str):
            self.V1p4junction_aa = str(self.V1p4junction_aa)

        if self.V1p4junction_length is not None and not isinstance(self.V1p4junction_length, int):
            self.V1p4junction_length = int(self.V1p4junction_length)

        if self.V1p4junction_aa_length is not None and not isinstance(self.V1p4junction_aa_length, int):
            self.V1p4junction_aa_length = int(self.V1p4junction_aa_length)

        if self.V1p4germline_alignment is not None and not isinstance(self.V1p4germline_alignment, str):
            self.V1p4germline_alignment = str(self.V1p4germline_alignment)

        if self.V1p4germline_alignment_aa is not None and not isinstance(self.V1p4germline_alignment_aa, str):
            self.V1p4germline_alignment_aa = str(self.V1p4germline_alignment_aa)

        if self.V1p4v_alignment_start is not None and not isinstance(self.V1p4v_alignment_start, int):
            self.V1p4v_alignment_start = int(self.V1p4v_alignment_start)

        if self.V1p4v_alignment_end is not None and not isinstance(self.V1p4v_alignment_end, int):
            self.V1p4v_alignment_end = int(self.V1p4v_alignment_end)

        if self.V1p4d_alignment_start is not None and not isinstance(self.V1p4d_alignment_start, int):
            self.V1p4d_alignment_start = int(self.V1p4d_alignment_start)

        if self.V1p4d_alignment_end is not None and not isinstance(self.V1p4d_alignment_end, int):
            self.V1p4d_alignment_end = int(self.V1p4d_alignment_end)

        if self.V1p4j_alignment_start is not None and not isinstance(self.V1p4j_alignment_start, int):
            self.V1p4j_alignment_start = int(self.V1p4j_alignment_start)

        if self.V1p4j_alignment_end is not None and not isinstance(self.V1p4j_alignment_end, int):
            self.V1p4j_alignment_end = int(self.V1p4j_alignment_end)

        if self.V1p4junction_start is not None and not isinstance(self.V1p4junction_start, int):
            self.V1p4junction_start = int(self.V1p4junction_start)

        if self.V1p4junction_end is not None and not isinstance(self.V1p4junction_end, int):
            self.V1p4junction_end = int(self.V1p4junction_end)

        if self.V1p4umi_count is not None and not isinstance(self.V1p4umi_count, int):
            self.V1p4umi_count = int(self.V1p4umi_count)

        if self.V1p4clone_count is not None and not isinstance(self.V1p4clone_count, int):
            self.V1p4clone_count = int(self.V1p4clone_count)

        if self.V1p4seed_id is not None and not isinstance(self.V1p4seed_id, str):
            self.V1p4seed_id = str(self.V1p4seed_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Tree(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Tree"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Tree"
    class_name: ClassVar[str] = "V1p4Tree"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Tree

    V1p4tree_id: Optional[str] = None
    V1p4clone_id: Optional[str] = None
    V1p4newick: Optional[str] = None
    V1p4nodes: Optional[Union[Union[dict, "V1p4Node"], List[Union[dict, "V1p4Node"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4tree_id is not None and not isinstance(self.V1p4tree_id, str):
            self.V1p4tree_id = str(self.V1p4tree_id)

        if self.V1p4clone_id is not None and not isinstance(self.V1p4clone_id, str):
            self.V1p4clone_id = str(self.V1p4clone_id)

        if self.V1p4newick is not None and not isinstance(self.V1p4newick, str):
            self.V1p4newick = str(self.V1p4newick)

        if not isinstance(self.V1p4nodes, list):
            self.V1p4nodes = [self.V1p4nodes] if self.V1p4nodes is not None else []
        self.V1p4nodes = [v if isinstance(v, V1p4Node) else V1p4Node(**as_dict(v)) for v in self.V1p4nodes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Node(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Node"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Node"
    class_name: ClassVar[str] = "V1p4Node"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Node

    V1p4sequence_id: Optional[str] = None
    V1p4sequence_alignment: Optional[str] = None
    V1p4junction: Optional[str] = None
    V1p4junction_aa: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4sequence_id is not None and not isinstance(self.V1p4sequence_id, str):
            self.V1p4sequence_id = str(self.V1p4sequence_id)

        if self.V1p4sequence_alignment is not None and not isinstance(self.V1p4sequence_alignment, str):
            self.V1p4sequence_alignment = str(self.V1p4sequence_alignment)

        if self.V1p4junction is not None and not isinstance(self.V1p4junction, str):
            self.V1p4junction = str(self.V1p4junction)

        if self.V1p4junction_aa is not None and not isinstance(self.V1p4junction_aa, str):
            self.V1p4junction_aa = str(self.V1p4junction_aa)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Cell(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Cell"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Cell"
    class_name: ClassVar[str] = "V1p4Cell"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Cell

    V1p4cell_id: Optional[str] = None
    V1p4repertoire_id: Optional[str] = None
    V1p4data_processing_id: Optional[str] = None
    V1p4receptors: Optional[Union[str, List[str]]] = empty_list()
    V1p4cell_subset: Optional[Union[str, "V1p4CellSubset"]] = None
    V1p4cell_phenotype: Optional[str] = None
    V1p4cell_label: Optional[str] = None
    V1p4virtual_pairing: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4cell_id is not None and not isinstance(self.V1p4cell_id, str):
            self.V1p4cell_id = str(self.V1p4cell_id)

        if self.V1p4repertoire_id is not None and not isinstance(self.V1p4repertoire_id, str):
            self.V1p4repertoire_id = str(self.V1p4repertoire_id)

        if self.V1p4data_processing_id is not None and not isinstance(self.V1p4data_processing_id, str):
            self.V1p4data_processing_id = str(self.V1p4data_processing_id)

        if not isinstance(self.V1p4receptors, list):
            self.V1p4receptors = [self.V1p4receptors] if self.V1p4receptors is not None else []
        self.V1p4receptors = [v if isinstance(v, str) else str(v) for v in self.V1p4receptors]

        if self.V1p4cell_phenotype is not None and not isinstance(self.V1p4cell_phenotype, str):
            self.V1p4cell_phenotype = str(self.V1p4cell_phenotype)

        if self.V1p4cell_label is not None and not isinstance(self.V1p4cell_label, str):
            self.V1p4cell_label = str(self.V1p4cell_label)

        if self.V1p4virtual_pairing is not None and not isinstance(self.V1p4virtual_pairing, Bool):
            self.V1p4virtual_pairing = Bool(self.V1p4virtual_pairing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Expression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Expression"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Expression"
    class_name: ClassVar[str] = "V1p4Expression"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Expression

    V1p4expression_id: Optional[str] = None
    V1p4cell_id: Optional[str] = None
    V1p4repertoire_id: Optional[str] = None
    V1p4data_processing_id: Optional[str] = None
    V1p4property_type: Optional[str] = None
    V1p4property: Optional[Union[str, "V1p4Property"]] = None
    V1p4value: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4expression_id is not None and not isinstance(self.V1p4expression_id, str):
            self.V1p4expression_id = str(self.V1p4expression_id)

        if self.V1p4cell_id is not None and not isinstance(self.V1p4cell_id, str):
            self.V1p4cell_id = str(self.V1p4cell_id)

        if self.V1p4repertoire_id is not None and not isinstance(self.V1p4repertoire_id, str):
            self.V1p4repertoire_id = str(self.V1p4repertoire_id)

        if self.V1p4data_processing_id is not None and not isinstance(self.V1p4data_processing_id, str):
            self.V1p4data_processing_id = str(self.V1p4data_processing_id)

        if self.V1p4property_type is not None and not isinstance(self.V1p4property_type, str):
            self.V1p4property_type = str(self.V1p4property_type)

        if self.V1p4value is not None and not isinstance(self.V1p4value, float):
            self.V1p4value = float(self.V1p4value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Receptor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Receptor"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Receptor"
    class_name: ClassVar[str] = "V1p4Receptor"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Receptor

    V1p4receptor_id: Optional[str] = None
    V1p4receptor_hash: Optional[str] = None
    V1p4receptor_type: Optional[Union[str, "V1p4ReceptorType"]] = None
    V1p4receptor_variable_domain_1_aa: Optional[str] = None
    V1p4receptor_variable_domain_1_locus: Optional[Union[str, "V1p4ReceptorVariableDomain1Locus"]] = None
    V1p4receptor_variable_domain_2_aa: Optional[str] = None
    V1p4receptor_variable_domain_2_locus: Optional[Union[str, "V1p4ReceptorVariableDomain2Locus"]] = None
    V1p4receptor_ref: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4receptor_id is not None and not isinstance(self.V1p4receptor_id, str):
            self.V1p4receptor_id = str(self.V1p4receptor_id)

        if self.V1p4receptor_hash is not None and not isinstance(self.V1p4receptor_hash, str):
            self.V1p4receptor_hash = str(self.V1p4receptor_hash)

        if self.V1p4receptor_type is not None and not isinstance(self.V1p4receptor_type, V1p4ReceptorType):
            self.V1p4receptor_type = V1p4ReceptorType(self.V1p4receptor_type)

        if self.V1p4receptor_variable_domain_1_aa is not None and not isinstance(self.V1p4receptor_variable_domain_1_aa, str):
            self.V1p4receptor_variable_domain_1_aa = str(self.V1p4receptor_variable_domain_1_aa)

        if self.V1p4receptor_variable_domain_1_locus is not None and not isinstance(self.V1p4receptor_variable_domain_1_locus, V1p4ReceptorVariableDomain1Locus):
            self.V1p4receptor_variable_domain_1_locus = V1p4ReceptorVariableDomain1Locus(self.V1p4receptor_variable_domain_1_locus)

        if self.V1p4receptor_variable_domain_2_aa is not None and not isinstance(self.V1p4receptor_variable_domain_2_aa, str):
            self.V1p4receptor_variable_domain_2_aa = str(self.V1p4receptor_variable_domain_2_aa)

        if self.V1p4receptor_variable_domain_2_locus is not None and not isinstance(self.V1p4receptor_variable_domain_2_locus, V1p4ReceptorVariableDomain2Locus):
            self.V1p4receptor_variable_domain_2_locus = V1p4ReceptorVariableDomain2Locus(self.V1p4receptor_variable_domain_2_locus)

        if not isinstance(self.V1p4receptor_ref, list):
            self.V1p4receptor_ref = [self.V1p4receptor_ref] if self.V1p4receptor_ref is not None else []
        self.V1p4receptor_ref = [v if isinstance(v, str) else str(v) for v in self.V1p4receptor_ref]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Reactivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Reactivity"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Reactivity"
    class_name: ClassVar[str] = "V1p4Reactivity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Reactivity

    V1p4reactivity_id: Optional[str] = None
    V1p4cell_id: Optional[str] = None
    V1p4repertoire_id: Optional[str] = None
    V1p4data_processing_id: Optional[str] = None
    V1p4ligand_type: Optional[Union[str, "V1p4LigandType"]] = None
    V1p4antigen_type: Optional[Union[str, "V1p4AntigenType"]] = None
    V1p4antigen: Optional[Union[str, "V1p4Antigen"]] = None
    V1p4antigen_source_species: Optional[Union[str, "V1p4AntigenSourceSpecies"]] = None
    V1p4peptide_start: Optional[int] = None
    V1p4peptide_end: Optional[int] = None
    V1p4peptide_sequence_aa: Optional[str] = None
    V1p4mhc_class: Optional[Union[str, "V1p4MhcClass"]] = None
    V1p4mhc_gene_1: Optional[Union[str, "V1p4MhcGene1"]] = None
    V1p4mhc_allele_1: Optional[str] = None
    V1p4mhc_gene_2: Optional[Union[str, "V1p4MhcGene2"]] = None
    V1p4mhc_allele_2: Optional[str] = None
    V1p4reactivity_method: Optional[str] = None
    V1p4reactivity_readout: Optional[str] = None
    V1p4reactivity_value: Optional[float] = None
    V1p4reactivity_unit: Optional[str] = None
    V1p4reactivity_ref: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4reactivity_id is not None and not isinstance(self.V1p4reactivity_id, str):
            self.V1p4reactivity_id = str(self.V1p4reactivity_id)

        if self.V1p4cell_id is not None and not isinstance(self.V1p4cell_id, str):
            self.V1p4cell_id = str(self.V1p4cell_id)

        if self.V1p4repertoire_id is not None and not isinstance(self.V1p4repertoire_id, str):
            self.V1p4repertoire_id = str(self.V1p4repertoire_id)

        if self.V1p4data_processing_id is not None and not isinstance(self.V1p4data_processing_id, str):
            self.V1p4data_processing_id = str(self.V1p4data_processing_id)

        if self.V1p4ligand_type is not None and not isinstance(self.V1p4ligand_type, V1p4LigandType):
            self.V1p4ligand_type = V1p4LigandType(self.V1p4ligand_type)

        if self.V1p4antigen_type is not None and not isinstance(self.V1p4antigen_type, V1p4AntigenType):
            self.V1p4antigen_type = V1p4AntigenType(self.V1p4antigen_type)

        if self.V1p4peptide_start is not None and not isinstance(self.V1p4peptide_start, int):
            self.V1p4peptide_start = int(self.V1p4peptide_start)

        if self.V1p4peptide_end is not None and not isinstance(self.V1p4peptide_end, int):
            self.V1p4peptide_end = int(self.V1p4peptide_end)

        if self.V1p4peptide_sequence_aa is not None and not isinstance(self.V1p4peptide_sequence_aa, str):
            self.V1p4peptide_sequence_aa = str(self.V1p4peptide_sequence_aa)

        if self.V1p4mhc_class is not None and not isinstance(self.V1p4mhc_class, V1p4MhcClass):
            self.V1p4mhc_class = V1p4MhcClass(self.V1p4mhc_class)

        if self.V1p4mhc_allele_1 is not None and not isinstance(self.V1p4mhc_allele_1, str):
            self.V1p4mhc_allele_1 = str(self.V1p4mhc_allele_1)

        if self.V1p4mhc_allele_2 is not None and not isinstance(self.V1p4mhc_allele_2, str):
            self.V1p4mhc_allele_2 = str(self.V1p4mhc_allele_2)

        if self.V1p4reactivity_method is not None and not isinstance(self.V1p4reactivity_method, str):
            self.V1p4reactivity_method = str(self.V1p4reactivity_method)

        if self.V1p4reactivity_readout is not None and not isinstance(self.V1p4reactivity_readout, str):
            self.V1p4reactivity_readout = str(self.V1p4reactivity_readout)

        if self.V1p4reactivity_value is not None and not isinstance(self.V1p4reactivity_value, float):
            self.V1p4reactivity_value = float(self.V1p4reactivity_value)

        if self.V1p4reactivity_unit is not None and not isinstance(self.V1p4reactivity_unit, str):
            self.V1p4reactivity_unit = str(self.V1p4reactivity_unit)

        if self.V1p4reactivity_ref is not None and not isinstance(self.V1p4reactivity_ref, str):
            self.V1p4reactivity_ref = str(self.V1p4reactivity_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SampleProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SampleProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SampleProcessing"
    class_name: ClassVar[str] = "V1p4SampleProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SampleProcessing

    V1p4sample_processing_id: Optional[str] = None
    V1p4sample_id: Optional[str] = None
    V1p4sample_type: Optional[str] = None
    V1p4tissue: Optional[Union[str, "V1p4Tissue"]] = None
    V1p4anatomic_site: Optional[str] = None
    V1p4disease_state_sample: Optional[str] = None
    V1p4collection_time_point_relative: Optional[Union[dict, V1p4TimePoint]] = None
    V1p4collection_location: Optional[Union[str, "V1p4CollectionLocation"]] = None
    V1p4biomaterial_provider: Optional[str] = None
    V1p4tissue_processing: Optional[str] = None
    V1p4cell_subset: Optional[Union[str, "V1p4CellSubset"]] = None
    V1p4cell_phenotype: Optional[str] = None
    V1p4cell_label: Optional[str] = None
    V1p4cell_species: Optional[Union[str, "V1p4CellSpecies"]] = None
    V1p4single_cell: Optional[Union[bool, Bool]] = None
    V1p4cell_number: Optional[int] = None
    V1p4cells_per_reaction: Optional[int] = None
    V1p4cell_storage: Optional[Union[bool, Bool]] = None
    V1p4cell_quality: Optional[str] = None
    V1p4cell_isolation: Optional[str] = None
    V1p4cell_processing_protocol: Optional[str] = None
    V1p4template_class: Optional[Union[str, "V1p4TemplateClass"]] = None
    V1p4template_quality: Optional[str] = None
    V1p4template_amount: Optional[Union[dict, V1p4PhysicalQuantity]] = None
    V1p4library_generation_method: Optional[Union[str, "V1p4LibraryGenerationMethod"]] = None
    V1p4library_generation_protocol: Optional[str] = None
    V1p4library_generation_kit_version: Optional[str] = None
    V1p4pcr_target: Optional[Union[Union[dict, V1p4PCRTarget], List[Union[dict, V1p4PCRTarget]]]] = empty_list()
    V1p4complete_sequences: Optional[Union[str, "V1p4CompleteSequences"]] = None
    V1p4physical_linkage: Optional[Union[str, "V1p4PhysicalLinkage"]] = None
    V1p4sequencing_run_id: Optional[str] = None
    V1p4total_reads_passing_qc_filter: Optional[int] = None
    V1p4sequencing_platform: Optional[str] = None
    V1p4sequencing_facility: Optional[str] = None
    V1p4sequencing_run_date: Optional[Union[str, XSDDateTime]] = None
    V1p4sequencing_kit: Optional[str] = None
    V1p4sequencing_files: Optional[Union[dict, V1p4SequencingData]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4sample_processing_id is not None and not isinstance(self.V1p4sample_processing_id, str):
            self.V1p4sample_processing_id = str(self.V1p4sample_processing_id)

        if self.V1p4sample_id is not None and not isinstance(self.V1p4sample_id, str):
            self.V1p4sample_id = str(self.V1p4sample_id)

        if self.V1p4sample_type is not None and not isinstance(self.V1p4sample_type, str):
            self.V1p4sample_type = str(self.V1p4sample_type)

        if self.V1p4anatomic_site is not None and not isinstance(self.V1p4anatomic_site, str):
            self.V1p4anatomic_site = str(self.V1p4anatomic_site)

        if self.V1p4disease_state_sample is not None and not isinstance(self.V1p4disease_state_sample, str):
            self.V1p4disease_state_sample = str(self.V1p4disease_state_sample)

        if self.V1p4collection_time_point_relative is not None and not isinstance(self.V1p4collection_time_point_relative, V1p4TimePoint):
            self.V1p4collection_time_point_relative = V1p4TimePoint(**as_dict(self.V1p4collection_time_point_relative))

        if self.V1p4biomaterial_provider is not None and not isinstance(self.V1p4biomaterial_provider, str):
            self.V1p4biomaterial_provider = str(self.V1p4biomaterial_provider)

        if self.V1p4tissue_processing is not None and not isinstance(self.V1p4tissue_processing, str):
            self.V1p4tissue_processing = str(self.V1p4tissue_processing)

        if self.V1p4cell_phenotype is not None and not isinstance(self.V1p4cell_phenotype, str):
            self.V1p4cell_phenotype = str(self.V1p4cell_phenotype)

        if self.V1p4cell_label is not None and not isinstance(self.V1p4cell_label, str):
            self.V1p4cell_label = str(self.V1p4cell_label)

        if self.V1p4single_cell is not None and not isinstance(self.V1p4single_cell, Bool):
            self.V1p4single_cell = Bool(self.V1p4single_cell)

        if self.V1p4cell_number is not None and not isinstance(self.V1p4cell_number, int):
            self.V1p4cell_number = int(self.V1p4cell_number)

        if self.V1p4cells_per_reaction is not None and not isinstance(self.V1p4cells_per_reaction, int):
            self.V1p4cells_per_reaction = int(self.V1p4cells_per_reaction)

        if self.V1p4cell_storage is not None and not isinstance(self.V1p4cell_storage, Bool):
            self.V1p4cell_storage = Bool(self.V1p4cell_storage)

        if self.V1p4cell_quality is not None and not isinstance(self.V1p4cell_quality, str):
            self.V1p4cell_quality = str(self.V1p4cell_quality)

        if self.V1p4cell_isolation is not None and not isinstance(self.V1p4cell_isolation, str):
            self.V1p4cell_isolation = str(self.V1p4cell_isolation)

        if self.V1p4cell_processing_protocol is not None and not isinstance(self.V1p4cell_processing_protocol, str):
            self.V1p4cell_processing_protocol = str(self.V1p4cell_processing_protocol)

        if self.V1p4template_class is not None and not isinstance(self.V1p4template_class, V1p4TemplateClass):
            self.V1p4template_class = V1p4TemplateClass(self.V1p4template_class)

        if self.V1p4template_quality is not None and not isinstance(self.V1p4template_quality, str):
            self.V1p4template_quality = str(self.V1p4template_quality)

        if self.V1p4template_amount is not None and not isinstance(self.V1p4template_amount, V1p4PhysicalQuantity):
            self.V1p4template_amount = V1p4PhysicalQuantity(**as_dict(self.V1p4template_amount))

        if self.V1p4library_generation_method is not None and not isinstance(self.V1p4library_generation_method, V1p4LibraryGenerationMethod):
            self.V1p4library_generation_method = V1p4LibraryGenerationMethod(self.V1p4library_generation_method)

        if self.V1p4library_generation_protocol is not None and not isinstance(self.V1p4library_generation_protocol, str):
            self.V1p4library_generation_protocol = str(self.V1p4library_generation_protocol)

        if self.V1p4library_generation_kit_version is not None and not isinstance(self.V1p4library_generation_kit_version, str):
            self.V1p4library_generation_kit_version = str(self.V1p4library_generation_kit_version)

        if not isinstance(self.V1p4pcr_target, list):
            self.V1p4pcr_target = [self.V1p4pcr_target] if self.V1p4pcr_target is not None else []
        self.V1p4pcr_target = [v if isinstance(v, V1p4PCRTarget) else V1p4PCRTarget(**as_dict(v)) for v in self.V1p4pcr_target]

        if self.V1p4complete_sequences is not None and not isinstance(self.V1p4complete_sequences, V1p4CompleteSequences):
            self.V1p4complete_sequences = V1p4CompleteSequences(self.V1p4complete_sequences)

        if self.V1p4physical_linkage is not None and not isinstance(self.V1p4physical_linkage, V1p4PhysicalLinkage):
            self.V1p4physical_linkage = V1p4PhysicalLinkage(self.V1p4physical_linkage)

        if self.V1p4sequencing_run_id is not None and not isinstance(self.V1p4sequencing_run_id, str):
            self.V1p4sequencing_run_id = str(self.V1p4sequencing_run_id)

        if self.V1p4total_reads_passing_qc_filter is not None and not isinstance(self.V1p4total_reads_passing_qc_filter, int):
            self.V1p4total_reads_passing_qc_filter = int(self.V1p4total_reads_passing_qc_filter)

        if self.V1p4sequencing_platform is not None and not isinstance(self.V1p4sequencing_platform, str):
            self.V1p4sequencing_platform = str(self.V1p4sequencing_platform)

        if self.V1p4sequencing_facility is not None and not isinstance(self.V1p4sequencing_facility, str):
            self.V1p4sequencing_facility = str(self.V1p4sequencing_facility)

        if self.V1p4sequencing_run_date is not None and not isinstance(self.V1p4sequencing_run_date, XSDDateTime):
            self.V1p4sequencing_run_date = XSDDateTime(self.V1p4sequencing_run_date)

        if self.V1p4sequencing_kit is not None and not isinstance(self.V1p4sequencing_kit, str):
            self.V1p4sequencing_kit = str(self.V1p4sequencing_kit)

        if self.V1p4sequencing_files is not None and not isinstance(self.V1p4sequencing_files, V1p4SequencingData):
            self.V1p4sequencing_files = V1p4SequencingData(**as_dict(self.V1p4sequencing_files))

        super().__post_init__(**kwargs)


# Enumerations
class Species(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="Species",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Homo sapiens (human)",
            PermissibleValue(
                text="Homo sapiens (human)",
                meaning=NCBITAXON["9606"]))
        setattr(cls, "Mus musculus (mouse)",
            PermissibleValue(
                text="Mus musculus (mouse)",
                meaning=NCBITAXON["10090"]))

class BiologicalSex(EnumDefinitionImpl):

    female = PermissibleValue(
        text="female",
        meaning=PATO["0020002"])
    male = PermissibleValue(
        text="male",
        meaning=PATO["0020001"])

    _defn = EnumDefinition(
        name="BiologicalSex",
    )

class PhenotypicSex(EnumDefinitionImpl):

    female = PermissibleValue(
        text="female",
        meaning=PATO["0000383"])
    male = PermissibleValue(
        text="male",
        meaning=PATO["0000384"])
    hermaphrodite = PermissibleValue(
        text="hermaphrodite",
        meaning=PATO["0001340"])
    intersex = PermissibleValue(text="intersex")
    pooled = PermissibleValue(text="pooled")

    _defn = EnumDefinition(
        name="PhenotypicSex",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not collected",
            PermissibleValue(text="not collected"))

class Race(EnumDefinitionImpl):

    Asian = PermissibleValue(
        text="Asian",
        meaning=OMRSE["00000216"])
    White = PermissibleValue(
        text="White",
        meaning=OMRSE["00000219"])
    Other = PermissibleValue(
        text="Other",
        meaning=OMRSE["00000214"])
    Black = PermissibleValue(text="Black")
    Brazilian = PermissibleValue(text="Brazilian")
    Chinese = PermissibleValue(text="Chinese")
    Hispanic = PermissibleValue(text="Hispanic")
    Indian = PermissibleValue(text="Indian")
    Korean = PermissibleValue(text="Korean")
    Mixed = PermissibleValue(text="Mixed")
    NR = PermissibleValue(text="NR")
    Native = PermissibleValue(text="Native")

    _defn = EnumDefinition(
        name="Race",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "American Indian or Alaska Native",
            PermissibleValue(
                text="American Indian or Alaska Native",
                meaning=OMRSE["00000215"]))
        setattr(cls, "Black or African American",
            PermissibleValue(
                text="Black or African American",
                meaning=OMRSE["00000217"]))
        setattr(cls, "Native Hawaiian or Other Pacific Islander",
            PermissibleValue(
                text="Native Hawaiian or Other Pacific Islander",
                meaning=OMRSE["00000218"]))
        setattr(cls, "African American",
            PermissibleValue(text="African American"))
        setattr(cls, "Asian or Pacific Islander",
            PermissibleValue(text="Asian or Pacific Islander"))
        setattr(cls, "German/East Indian",
            PermissibleValue(text="German/East Indian"))
        setattr(cls, "Hispanic or Latino",
            PermissibleValue(text="Hispanic or Latino"))
        setattr(cls, "Indian- Irish- French- polish",
            PermissibleValue(text="Indian- Irish- French- polish"))
        setattr(cls, "Middle Eastern European",
            PermissibleValue(text="Middle Eastern European"))
        setattr(cls, "Middle Eastern",
            PermissibleValue(text="Middle Eastern"))
        setattr(cls, "Mixed racial group",
            PermissibleValue(text="Mixed racial group"))
        setattr(cls, "Native American or Alaska Native",
            PermissibleValue(text="Native American or Alaska Native"))
        setattr(cls, "Unknown racial group",
            PermissibleValue(text="Unknown racial group"))
        setattr(cls, "White, Asian",
            PermissibleValue(text="White, Asian"))
        setattr(cls, "White, Asian, Black",
            PermissibleValue(text="White, Asian, Black"))
        setattr(cls, "White, Caucasian",
            PermissibleValue(text="White, Caucasian"))
        setattr(cls, "White-British",
            PermissibleValue(text="White-British"))

class Ethnicity(EnumDefinitionImpl):

    Other = PermissibleValue(
        text="Other",
        meaning=OMRSE["00000206"])
    African = PermissibleValue(text="African")
    Arab = PermissibleValue(text="Arab")
    Arabigan = PermissibleValue(text="Arabigan")
    Asian = PermissibleValue(text="Asian")
    Black = PermissibleValue(text="Black")
    Caucasian = PermissibleValue(text="Caucasian")
    Declined = PermissibleValue(text="Declined")
    Han = PermissibleValue(text="Han")
    Hispanic = PermissibleValue(text="Hispanic")
    Italian = PermissibleValue(text="Italian")
    Latin = PermissibleValue(text="Latin")
    NR = PermissibleValue(text="NR")
    White = PermissibleValue(text="White")

    _defn = EnumDefinition(
        name="Ethnicity",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Hispanic or Latino",
            PermissibleValue(
                text="Hispanic or Latino",
                meaning=OMRSE["00000207"]))
        setattr(cls, "Not Hispanic or Latino",
            PermissibleValue(
                text="Not Hispanic or Latino",
                meaning=OMRSE["00000208"]))
        setattr(cls, "African-American",
            PermissibleValue(text="African-American"))
        setattr(cls, "Black or Black British - African",
            PermissibleValue(text="Black or Black British - African"))
        setattr(cls, "Non-Hispanic or Latino",
            PermissibleValue(text="Non-Hispanic or Latino"))
        setattr(cls, "Non-Hispanic",
            PermissibleValue(text="Non-Hispanic"))
        setattr(cls, "Other - Not Stated",
            PermissibleValue(text="Other - Not Stated"))
        setattr(cls, "SE Asian",
            PermissibleValue(text="SE Asian"))
        setattr(cls, "Unknown Ethnicity",
            PermissibleValue(text="Unknown Ethnicity"))

class Geolocation(EnumDefinitionImpl):

    Canada = PermissibleValue(
        text="Canada",
        meaning=GAZ["00002560"])
    Nicaragua = PermissibleValue(
        text="Nicaragua",
        meaning=GAZ["00002978"])
    Uganda = PermissibleValue(
        text="Uganda",
        meaning=GAZ["00001102"])
    China = PermissibleValue(
        text="China",
        meaning=GAZ["00002845"])
    England = PermissibleValue(
        text="England",
        meaning=GAZ["00002641"])
    India = PermissibleValue(
        text="India",
        meaning=GAZ["00002839"])
    Gambia = PermissibleValue(
        text="Gambia",
        meaning=GAZ["00000907"])
    Switzerland = PermissibleValue(
        text="Switzerland",
        meaning=GAZ["00002941"])
    Colombia = PermissibleValue(
        text="Colombia",
        meaning=GAZ["00002929"])

    _defn = EnumDefinition(
        name="Geolocation",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "US: New York",
            PermissibleValue(
                text="US: New York",
                meaning=GAZ["00002514"]))
        setattr(cls, "US: California",
            PermissibleValue(
                text="US: California",
                meaning=GAZ["00002461"]))
        setattr(cls, "US: Connecticut",
            PermissibleValue(
                text="US: Connecticut",
                meaning=GAZ["00002591"]))
        setattr(cls, "US: Georgia",
            PermissibleValue(
                text="US: Georgia",
                meaning=GAZ["00002611"]))
        setattr(cls, "US: Texas",
            PermissibleValue(
                text="US: Texas",
                meaning=GAZ["00002580"]))
        setattr(cls, "US: Maryland",
            PermissibleValue(
                text="US: Maryland",
                meaning=GAZ["00002519"]))
        setattr(cls, "US: Minnesota",
            PermissibleValue(
                text="US: Minnesota",
                meaning=GAZ["00002539"]))
        setattr(cls, "United States of America",
            PermissibleValue(
                text="United States of America",
                meaning=GAZ["00002459"]))
        setattr(cls, "US: Massachusetts",
            PermissibleValue(
                text="US: Massachusetts",
                meaning=GAZ["00002537"]))
        setattr(cls, "US: Colorado",
            PermissibleValue(
                text="US: Colorado",
                meaning=GAZ["00006254"]))
        setattr(cls, "Papua New Guinea",
            PermissibleValue(
                text="Papua New Guinea",
                meaning=GAZ["00003922"]))
        setattr(cls, "Metropolitan France",
            PermissibleValue(
                text="Metropolitan France",
                meaning=GAZ["00003940"]))
        setattr(cls, "Sri Lanka",
            PermissibleValue(
                text="Sri Lanka",
                meaning=GAZ["00003924"]))
        setattr(cls, "US: Washington",
            PermissibleValue(
                text="US: Washington",
                meaning=GAZ["00002553"]))
        setattr(cls, "geographic location",
            PermissibleValue(
                text="geographic location",
                meaning=GAZ["00000448"]))
        setattr(cls, "US: Florida",
            PermissibleValue(
                text="US: Florida",
                meaning=GAZ["00002888"]))
        setattr(cls, "US: Kansas",
            PermissibleValue(
                text="US: Kansas",
                meaning=GAZ["00004435"]))

class Strain(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="Strain",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1D2beta",
            PermissibleValue(text="1D2beta"))
        setattr(cls, "BALB/cByJ",
            PermissibleValue(text="BALB/cByJ"))
        setattr(cls, "Balb/c",
            PermissibleValue(text="Balb/c"))
        setattr(cls, "C57BL/6",
            PermissibleValue(text="C57BL/6"))
        setattr(cls, "C57BL/6J",
            PermissibleValue(text="C57BL/6J"))
        setattr(cls, "JHD-/- MRL/MpJ-Faslp",
            PermissibleValue(text="JHD-/- MRL/MpJ-Faslp"))
        setattr(cls, "LDLR+/+",
            PermissibleValue(text="LDLR+/+"))
        setattr(cls, "LDLR-/-",
            PermissibleValue(text="LDLR-/-"))
        setattr(cls, "pet shop mouse",
            PermissibleValue(text="pet shop mouse"))

class LifeEventProcess(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="LifeEventProcess",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Documented exposure without evidence for disease",
            PermissibleValue(
                text="Documented exposure without evidence for disease",
                meaning=ONTIE["0003305"]))
        setattr(cls, "Environmental exposure to endemic/ubiquitous agent without evidence for disease",
            PermissibleValue(
                text="Environmental exposure to endemic/ubiquitous agent without evidence for disease",
                meaning=ONTIE["0003308"]))
        setattr(cls, "Exposure with existing immune reactivity without evidence for disease",
            PermissibleValue(
                text="Exposure with existing immune reactivity without evidence for disease",
                meaning=OBI["1110061"]))
        setattr(cls, "specimen collection",
            PermissibleValue(
                text="specimen collection",
                meaning=OBI["0000659"]))

class ExposureMaterial(EnumDefinitionImpl):

    Dryvax = PermissibleValue(
        text="Dryvax",
        meaning=VO["0000035"])

    _defn = EnumDefinition(
        name="ExposureMaterial",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Influenza A virus",
            PermissibleValue(
                text="Influenza A virus",
                meaning=NCBITAXON["11320"]))
        setattr(cls, "Mycobacterium tuberculosis",
            PermissibleValue(
                text="Mycobacterium tuberculosis",
                meaning=NCBITAXON["1773"]))
        setattr(cls, "Plasmodium falciparum",
            PermissibleValue(
                text="Plasmodium falciparum",
                meaning=NCBITAXON["5833"]))
        setattr(cls, "Human gammaherpesvirus 4",
            PermissibleValue(
                text="Human gammaherpesvirus 4",
                meaning=NCBITAXON["10376"]))
        setattr(cls, "Human betaherpesvirus 5",
            PermissibleValue(
                text="Human betaherpesvirus 5",
                meaning=NCBITAXON["10359"]))
        setattr(cls, "Diphtheria-Tetanus-Pertussis vaccine",
            PermissibleValue(
                text="Diphtheria-Tetanus-Pertussis vaccine",
                meaning=VO["0000738"]))

class Disease(EnumDefinitionImpl):

    healthy = PermissibleValue(
        text="healthy",
        meaning=ONTIE["000342"])

    _defn = EnumDefinition(
        name="Disease",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "COVID-19",
            PermissibleValue(
                text="COVID-19",
                meaning=DOID["0080600"]))
        setattr(cls, "Plasmodium falciparum malaria",
            PermissibleValue(
                text="Plasmodium falciparum malaria",
                meaning=DOID["14067"]))
        setattr(cls, "dengue hemorrhagic fever",
            PermissibleValue(
                text="dengue hemorrhagic fever",
                meaning=DOID["12206"]))

class DiseaseStage(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="DiseaseStage",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "acute disease course",
            PermissibleValue(
                text="acute disease course",
                meaning=OGMS["0000094"]))
        setattr(cls, "post disease course",
            PermissibleValue(
                text="post disease course",
                meaning=ONTIE["0003544"]))
        setattr(cls, "unknown disease course",
            PermissibleValue(
                text="unknown disease course",
                meaning=ONTIE["0003545"]))
        setattr(cls, "chronic disease course",
            PermissibleValue(
                text="chronic disease course",
                meaning=OGMS["0000064"]))
        setattr(cls, "other disease course",
            PermissibleValue(
                text="other disease course",
                meaning=ONTIE["0003547"]))

class ChainType(EnumDefinitionImpl):

    IGH = PermissibleValue(text="IGH")
    IGK = PermissibleValue(text="IGK")
    IGL = PermissibleValue(text="IGL")
    TRA = PermissibleValue(text="TRA")
    TRB = PermissibleValue(text="TRB")
    TRD = PermissibleValue(text="TRD")
    TRG = PermissibleValue(text="TRG")

    _defn = EnumDefinition(
        name="ChainType",
    )

class ChainSimilarityType(EnumDefinitionImpl):

    exact_match = PermissibleValue(text="exact_match")
    exact_aa_match = PermissibleValue(text="exact_aa_match")
    cdr3_exact_match = PermissibleValue(text="cdr3_exact_match")
    cdr3_exact_aa_match = PermissibleValue(text="cdr3_exact_aa_match")
    cdr3_exact_aa_and_vj_match = PermissibleValue(text="cdr3_exact_aa_and_vj_match")

    _defn = EnumDefinition(
        name="ChainSimilarityType",
    )

class Unit(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="Unit",
    )

class Derivation(EnumDefinitionImpl):

    DNA = PermissibleValue(text="DNA")
    RNA = PermissibleValue(text="RNA")

    _defn = EnumDefinition(
        name="Derivation",
    )

class ObservationType(EnumDefinitionImpl):

    direct_sequencing = PermissibleValue(text="direct_sequencing")
    inference_from_repertoire = PermissibleValue(text="inference_from_repertoire")

    _defn = EnumDefinition(
        name="ObservationType",
    )

class Strand(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="Strand",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "+",
            PermissibleValue(text="+"))
        setattr(cls, "-",
            PermissibleValue(text="-"))

class Locus(EnumDefinitionImpl):

    IGH = PermissibleValue(text="IGH")
    IGI = PermissibleValue(text="IGI")
    IGK = PermissibleValue(text="IGK")
    IGL = PermissibleValue(text="IGL")
    TRA = PermissibleValue(text="TRA")
    TRB = PermissibleValue(text="TRB")
    TRG = PermissibleValue(text="TRG")
    TRD = PermissibleValue(text="TRD")

    _defn = EnumDefinition(
        name="Locus",
    )

class SequenceType(EnumDefinitionImpl):

    V = PermissibleValue(text="V")
    D = PermissibleValue(text="D")
    J = PermissibleValue(text="J")
    C = PermissibleValue(text="C")

    _defn = EnumDefinition(
        name="SequenceType",
    )

class InferenceType(EnumDefinitionImpl):

    genomic_and_rearranged = PermissibleValue(text="genomic_and_rearranged")
    genomic_only = PermissibleValue(text="genomic_only")
    rearranged_only = PermissibleValue(text="rearranged_only")

    _defn = EnumDefinition(
        name="InferenceType",
    )

class SpeciesSubgroupType(EnumDefinitionImpl):

    breed = PermissibleValue(text="breed")
    strain = PermissibleValue(text="strain")
    inbred = PermissibleValue(text="inbred")
    outbred = PermissibleValue(text="outbred")
    locational = PermissibleValue(text="locational")

    _defn = EnumDefinition(
        name="SpeciesSubgroupType",
    )

class Status(EnumDefinitionImpl):

    active = PermissibleValue(text="active")
    draft = PermissibleValue(text="draft")
    retired = PermissibleValue(text="retired")
    withdrawn = PermissibleValue(text="withdrawn")

    _defn = EnumDefinition(
        name="Status",
    )

class JCodonFrame(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="JCodonFrame",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1",
            PermissibleValue(text="1"))
        setattr(cls, "2",
            PermissibleValue(text="2"))
        setattr(cls, "3",
            PermissibleValue(text="3"))

class CurationalTags(EnumDefinitionImpl):

    likely_truncated = PermissibleValue(text="likely_truncated")
    likely_full_length = PermissibleValue(text="likely_full_length")

    _defn = EnumDefinition(
        name="CurationalTags",
    )

class InferenceProcess(EnumDefinitionImpl):

    genomic_sequencing = PermissibleValue(text="genomic_sequencing")
    repertoire_sequencing = PermissibleValue(text="repertoire_sequencing")

    _defn = EnumDefinition(
        name="InferenceProcess",
    )

class MhcClass(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MhcClass",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "MHC-I",
            PermissibleValue(text="MHC-I"))
        setattr(cls, "MHC-II",
            PermissibleValue(text="MHC-II"))
        setattr(cls, "MHC-nonclassical",
            PermissibleValue(text="MHC-nonclassical"))

class Gene(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="Gene",
    )

class StudyType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="StudyType",
    )

class KeywordsStudy(EnumDefinitionImpl):

    contains_ig = PermissibleValue(text="contains_ig")
    contains_tr = PermissibleValue(text="contains_tr")
    contains_paired_chain = PermissibleValue(text="contains_paired_chain")
    contains_schema_rearrangement = PermissibleValue(text="contains_schema_rearrangement")
    contains_schema_clone = PermissibleValue(text="contains_schema_clone")
    contains_schema_cell = PermissibleValue(text="contains_schema_cell")
    contains_schema_receptor = PermissibleValue(text="contains_schema_receptor")

    _defn = EnumDefinition(
        name="KeywordsStudy",
    )

class Sex(EnumDefinitionImpl):

    male = PermissibleValue(text="male")
    female = PermissibleValue(text="female")
    pooled = PermissibleValue(text="pooled")
    hermaphrodite = PermissibleValue(text="hermaphrodite")
    intersex = PermissibleValue(text="intersex")

    _defn = EnumDefinition(
        name="Sex",
    )

class AgeUnit(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AgeUnit",
    )

class DiseaseDiagnosis(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="DiseaseDiagnosis",
    )

class Tissue(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="Tissue",
    )

class CollectionTimePointRelativeUnit(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CollectionTimePointRelativeUnit",
    )

class CellSubset(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CellSubset",
    )

class CellSpecies(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CellSpecies",
    )

class PcrTargetLocus(EnumDefinitionImpl):

    IGH = PermissibleValue(text="IGH")
    IGI = PermissibleValue(text="IGI")
    IGK = PermissibleValue(text="IGK")
    IGL = PermissibleValue(text="IGL")
    TRA = PermissibleValue(text="TRA")
    TRB = PermissibleValue(text="TRB")
    TRD = PermissibleValue(text="TRD")
    TRG = PermissibleValue(text="TRG")

    _defn = EnumDefinition(
        name="PcrTargetLocus",
    )

class TemplateClass(EnumDefinitionImpl):

    DNA = PermissibleValue(text="DNA")
    RNA = PermissibleValue(text="RNA")

    _defn = EnumDefinition(
        name="TemplateClass",
    )

class TemplateAmountUnit(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="TemplateAmountUnit",
    )

class LibraryGenerationMethod(EnumDefinitionImpl):

    PCR = PermissibleValue(text="PCR")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="LibraryGenerationMethod",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "RT(RHP)+PCR",
            PermissibleValue(text="RT(RHP)+PCR"))
        setattr(cls, "RT(oligo-dT)+PCR",
            PermissibleValue(text="RT(oligo-dT)+PCR"))
        setattr(cls, "RT(oligo-dT)+TS+PCR",
            PermissibleValue(text="RT(oligo-dT)+TS+PCR"))
        setattr(cls, "RT(oligo-dT)+TS(UMI)+PCR",
            PermissibleValue(text="RT(oligo-dT)+TS(UMI)+PCR"))
        setattr(cls, "RT(specific)+PCR",
            PermissibleValue(text="RT(specific)+PCR"))
        setattr(cls, "RT(specific)+TS+PCR",
            PermissibleValue(text="RT(specific)+TS+PCR"))
        setattr(cls, "RT(specific)+TS(UMI)+PCR",
            PermissibleValue(text="RT(specific)+TS(UMI)+PCR"))
        setattr(cls, "RT(specific+UMI)+PCR",
            PermissibleValue(text="RT(specific+UMI)+PCR"))
        setattr(cls, "RT(specific+UMI)+TS+PCR",
            PermissibleValue(text="RT(specific+UMI)+TS+PCR"))
        setattr(cls, "RT(specific)+TS",
            PermissibleValue(text="RT(specific)+TS"))

class CompleteSequences(EnumDefinitionImpl):

    partial = PermissibleValue(text="partial")
    complete = PermissibleValue(text="complete")
    mixed = PermissibleValue(text="mixed")

    _defn = EnumDefinition(
        name="CompleteSequences",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "complete+untemplated",
            PermissibleValue(text="complete+untemplated"))

class PhysicalLinkage(EnumDefinitionImpl):

    none = PermissibleValue(text="none")
    hetero_prelinked = PermissibleValue(text="hetero_prelinked")

    _defn = EnumDefinition(
        name="PhysicalLinkage",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "hetero_head-head",
            PermissibleValue(text="hetero_head-head"))
        setattr(cls, "hetero_tail-head",
            PermissibleValue(text="hetero_tail-head"))

class FileType(EnumDefinitionImpl):

    fasta = PermissibleValue(text="fasta")
    fastq = PermissibleValue(text="fastq")

    _defn = EnumDefinition(
        name="FileType",
    )

class ReadDirection(EnumDefinitionImpl):

    forward = PermissibleValue(text="forward")
    reverse = PermissibleValue(text="reverse")
    mixed = PermissibleValue(text="mixed")

    _defn = EnumDefinition(
        name="ReadDirection",
    )

class PairedReadDirection(EnumDefinitionImpl):

    forward = PermissibleValue(text="forward")
    reverse = PermissibleValue(text="reverse")
    mixed = PermissibleValue(text="mixed")

    _defn = EnumDefinition(
        name="PairedReadDirection",
    )

class ExpressionStudyMethod(EnumDefinitionImpl):

    flow_cytometry = PermissibleValue(text="flow_cytometry")

    _defn = EnumDefinition(
        name="ExpressionStudyMethod",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "single-cell_transcriptome",
            PermissibleValue(text="single-cell_transcriptome"))

class Property(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="Property",
    )

class ReceptorType(EnumDefinitionImpl):

    Ig = PermissibleValue(text="Ig")
    TCR = PermissibleValue(text="TCR")

    _defn = EnumDefinition(
        name="ReceptorType",
    )

class ReceptorVariableDomain1Locus(EnumDefinitionImpl):

    IGH = PermissibleValue(text="IGH")
    TRB = PermissibleValue(text="TRB")
    TRD = PermissibleValue(text="TRD")

    _defn = EnumDefinition(
        name="ReceptorVariableDomain1Locus",
    )

class ReceptorVariableDomain2Locus(EnumDefinitionImpl):

    IGI = PermissibleValue(text="IGI")
    IGK = PermissibleValue(text="IGK")
    IGL = PermissibleValue(text="IGL")
    TRA = PermissibleValue(text="TRA")
    TRG = PermissibleValue(text="TRG")

    _defn = EnumDefinition(
        name="ReceptorVariableDomain2Locus",
    )

class LigandType(EnumDefinitionImpl):

    protein = PermissibleValue(text="protein")
    peptide = PermissibleValue(text="peptide")

    _defn = EnumDefinition(
        name="LigandType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "MHC:peptide",
            PermissibleValue(text="MHC:peptide"))
        setattr(cls, "MHC:non-peptide",
            PermissibleValue(text="MHC:non-peptide"))
        setattr(cls, "non-peptidic",
            PermissibleValue(text="non-peptidic"))

class AntigenType(EnumDefinitionImpl):

    protein = PermissibleValue(text="protein")
    peptide = PermissibleValue(text="peptide")

    _defn = EnumDefinition(
        name="AntigenType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "non-peptidic",
            PermissibleValue(text="non-peptidic"))

class Antigen(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="Antigen",
    )

class AntigenSourceSpecies(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AntigenSourceSpecies",
    )

class MhcGene1(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MhcGene1",
    )

class MhcGene2(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MhcGene2",
    )

class ReactivityMethod(EnumDefinitionImpl):

    SPR = PermissibleValue(text="SPR")
    ITC = PermissibleValue(text="ITC")
    ELISA = PermissibleValue(text="ELISA")
    cytometry = PermissibleValue(text="cytometry")
    biological_activity = PermissibleValue(text="biological_activity")

    _defn = EnumDefinition(
        name="ReactivityMethod",
    )

class ReactivityReadout(EnumDefinitionImpl):

    binding_strength = PermissibleValue(text="binding_strength")
    cytokine_release = PermissibleValue(text="cytokine_release")
    dissociation_constant_kd = PermissibleValue(text="dissociation_constant_kd")
    on_rate = PermissibleValue(text="on_rate")
    off_rate = PermissibleValue(text="off_rate")
    pathogen_inhibition = PermissibleValue(text="pathogen_inhibition")

    _defn = EnumDefinition(
        name="ReactivityReadout",
    )

class V1p5Unit(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5Unit",
    )

class V1p5Derivation(EnumDefinitionImpl):

    DNA = PermissibleValue(text="DNA")
    RNA = PermissibleValue(text="RNA")

    _defn = EnumDefinition(
        name="V1p5Derivation",
    )

class V1p5ObservationType(EnumDefinitionImpl):

    direct_sequencing = PermissibleValue(text="direct_sequencing")
    inference_from_repertoire = PermissibleValue(text="inference_from_repertoire")

    _defn = EnumDefinition(
        name="V1p5ObservationType",
    )

class V1p5Strand(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5Strand",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "+",
            PermissibleValue(text="+"))
        setattr(cls, "-",
            PermissibleValue(text="-"))

class V1p5Locus(EnumDefinitionImpl):

    IGH = PermissibleValue(text="IGH")
    IGI = PermissibleValue(text="IGI")
    IGK = PermissibleValue(text="IGK")
    IGL = PermissibleValue(text="IGL")
    TRA = PermissibleValue(text="TRA")
    TRB = PermissibleValue(text="TRB")
    TRG = PermissibleValue(text="TRG")
    TRD = PermissibleValue(text="TRD")

    _defn = EnumDefinition(
        name="V1p5Locus",
    )

class V1p5SequenceType(EnumDefinitionImpl):

    V = PermissibleValue(text="V")
    D = PermissibleValue(text="D")
    J = PermissibleValue(text="J")
    C = PermissibleValue(text="C")

    _defn = EnumDefinition(
        name="V1p5SequenceType",
    )

class V1p5InferenceType(EnumDefinitionImpl):

    genomic_and_rearranged = PermissibleValue(text="genomic_and_rearranged")
    genomic_only = PermissibleValue(text="genomic_only")
    rearranged_only = PermissibleValue(text="rearranged_only")

    _defn = EnumDefinition(
        name="V1p5InferenceType",
    )

class V1p5Species(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5Species",
    )

class V1p5SpeciesSubgroupType(EnumDefinitionImpl):

    breed = PermissibleValue(text="breed")
    strain = PermissibleValue(text="strain")
    inbred = PermissibleValue(text="inbred")
    outbred = PermissibleValue(text="outbred")
    locational = PermissibleValue(text="locational")

    _defn = EnumDefinition(
        name="V1p5SpeciesSubgroupType",
    )

class V1p5Status(EnumDefinitionImpl):

    active = PermissibleValue(text="active")
    draft = PermissibleValue(text="draft")
    retired = PermissibleValue(text="retired")
    withdrawn = PermissibleValue(text="withdrawn")

    _defn = EnumDefinition(
        name="V1p5Status",
    )

class V1p5JCodonFrame(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5JCodonFrame",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1",
            PermissibleValue(text="1"))
        setattr(cls, "2",
            PermissibleValue(text="2"))
        setattr(cls, "3",
            PermissibleValue(text="3"))

class V1p5CurationalTags(EnumDefinitionImpl):

    likely_truncated = PermissibleValue(text="likely_truncated")
    likely_full_length = PermissibleValue(text="likely_full_length")

    _defn = EnumDefinition(
        name="V1p5CurationalTags",
    )

class V1p5InferenceProcess(EnumDefinitionImpl):

    genomic_sequencing = PermissibleValue(text="genomic_sequencing")
    repertoire_sequencing = PermissibleValue(text="repertoire_sequencing")

    _defn = EnumDefinition(
        name="V1p5InferenceProcess",
    )

class V1p5MhcClass(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5MhcClass",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "MHC-I",
            PermissibleValue(text="MHC-I"))
        setattr(cls, "MHC-II",
            PermissibleValue(text="MHC-II"))
        setattr(cls, "MHC-nonclassical",
            PermissibleValue(text="MHC-nonclassical"))

class V1p5Gene(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5Gene",
    )

class V1p5StudyType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5StudyType",
    )

class V1p5KeywordsStudy(EnumDefinitionImpl):

    contains_ig = PermissibleValue(text="contains_ig")
    contains_tr = PermissibleValue(text="contains_tr")
    contains_paired_chain = PermissibleValue(text="contains_paired_chain")
    contains_schema_rearrangement = PermissibleValue(text="contains_schema_rearrangement")
    contains_schema_clone = PermissibleValue(text="contains_schema_clone")
    contains_schema_cell = PermissibleValue(text="contains_schema_cell")
    contains_schema_receptor = PermissibleValue(text="contains_schema_receptor")

    _defn = EnumDefinition(
        name="V1p5KeywordsStudy",
    )

class V1p5Sex(EnumDefinitionImpl):

    male = PermissibleValue(text="male")
    female = PermissibleValue(text="female")
    pooled = PermissibleValue(text="pooled")
    hermaphrodite = PermissibleValue(text="hermaphrodite")
    intersex = PermissibleValue(text="intersex")

    _defn = EnumDefinition(
        name="V1p5Sex",
    )

class V1p5AgeUnit(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5AgeUnit",
    )

class V1p5DiseaseDiagnosis(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5DiseaseDiagnosis",
    )

class V1p5Tissue(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5Tissue",
    )

class V1p5CollectionTimePointRelativeUnit(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5CollectionTimePointRelativeUnit",
    )

class V1p5CellSubset(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5CellSubset",
    )

class V1p5CellSpecies(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5CellSpecies",
    )

class V1p5PcrTargetLocus(EnumDefinitionImpl):

    IGH = PermissibleValue(text="IGH")
    IGI = PermissibleValue(text="IGI")
    IGK = PermissibleValue(text="IGK")
    IGL = PermissibleValue(text="IGL")
    TRA = PermissibleValue(text="TRA")
    TRB = PermissibleValue(text="TRB")
    TRD = PermissibleValue(text="TRD")
    TRG = PermissibleValue(text="TRG")

    _defn = EnumDefinition(
        name="V1p5PcrTargetLocus",
    )

class V1p5TemplateClass(EnumDefinitionImpl):

    DNA = PermissibleValue(text="DNA")
    RNA = PermissibleValue(text="RNA")

    _defn = EnumDefinition(
        name="V1p5TemplateClass",
    )

class V1p5TemplateAmountUnit(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5TemplateAmountUnit",
    )

class V1p5LibraryGenerationMethod(EnumDefinitionImpl):

    PCR = PermissibleValue(text="PCR")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="V1p5LibraryGenerationMethod",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "RT(RHP)+PCR",
            PermissibleValue(text="RT(RHP)+PCR"))
        setattr(cls, "RT(oligo-dT)+PCR",
            PermissibleValue(text="RT(oligo-dT)+PCR"))
        setattr(cls, "RT(oligo-dT)+TS+PCR",
            PermissibleValue(text="RT(oligo-dT)+TS+PCR"))
        setattr(cls, "RT(oligo-dT)+TS(UMI)+PCR",
            PermissibleValue(text="RT(oligo-dT)+TS(UMI)+PCR"))
        setattr(cls, "RT(specific)+PCR",
            PermissibleValue(text="RT(specific)+PCR"))
        setattr(cls, "RT(specific)+TS+PCR",
            PermissibleValue(text="RT(specific)+TS+PCR"))
        setattr(cls, "RT(specific)+TS(UMI)+PCR",
            PermissibleValue(text="RT(specific)+TS(UMI)+PCR"))
        setattr(cls, "RT(specific+UMI)+PCR",
            PermissibleValue(text="RT(specific+UMI)+PCR"))
        setattr(cls, "RT(specific+UMI)+TS+PCR",
            PermissibleValue(text="RT(specific+UMI)+TS+PCR"))
        setattr(cls, "RT(specific)+TS",
            PermissibleValue(text="RT(specific)+TS"))

class V1p5CompleteSequences(EnumDefinitionImpl):

    partial = PermissibleValue(text="partial")
    complete = PermissibleValue(text="complete")
    mixed = PermissibleValue(text="mixed")

    _defn = EnumDefinition(
        name="V1p5CompleteSequences",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "complete+untemplated",
            PermissibleValue(text="complete+untemplated"))

class V1p5PhysicalLinkage(EnumDefinitionImpl):

    none = PermissibleValue(text="none")
    hetero_prelinked = PermissibleValue(text="hetero_prelinked")

    _defn = EnumDefinition(
        name="V1p5PhysicalLinkage",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "hetero_head-head",
            PermissibleValue(text="hetero_head-head"))
        setattr(cls, "hetero_tail-head",
            PermissibleValue(text="hetero_tail-head"))

class V1p5FileType(EnumDefinitionImpl):

    fasta = PermissibleValue(text="fasta")
    fastq = PermissibleValue(text="fastq")

    _defn = EnumDefinition(
        name="V1p5FileType",
    )

class V1p5ReadDirection(EnumDefinitionImpl):

    forward = PermissibleValue(text="forward")
    reverse = PermissibleValue(text="reverse")
    mixed = PermissibleValue(text="mixed")

    _defn = EnumDefinition(
        name="V1p5ReadDirection",
    )

class V1p5PairedReadDirection(EnumDefinitionImpl):

    forward = PermissibleValue(text="forward")
    reverse = PermissibleValue(text="reverse")
    mixed = PermissibleValue(text="mixed")

    _defn = EnumDefinition(
        name="V1p5PairedReadDirection",
    )

class V1p5ExpressionStudyMethod(EnumDefinitionImpl):

    flow_cytometry = PermissibleValue(text="flow_cytometry")

    _defn = EnumDefinition(
        name="V1p5ExpressionStudyMethod",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "single-cell_transcriptome",
            PermissibleValue(text="single-cell_transcriptome"))

class V1p5Property(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5Property",
    )

class V1p5ReceptorType(EnumDefinitionImpl):

    Ig = PermissibleValue(text="Ig")
    TCR = PermissibleValue(text="TCR")

    _defn = EnumDefinition(
        name="V1p5ReceptorType",
    )

class V1p5ReceptorVariableDomain1Locus(EnumDefinitionImpl):

    IGH = PermissibleValue(text="IGH")
    TRB = PermissibleValue(text="TRB")
    TRD = PermissibleValue(text="TRD")

    _defn = EnumDefinition(
        name="V1p5ReceptorVariableDomain1Locus",
    )

class V1p5ReceptorVariableDomain2Locus(EnumDefinitionImpl):

    IGI = PermissibleValue(text="IGI")
    IGK = PermissibleValue(text="IGK")
    IGL = PermissibleValue(text="IGL")
    TRA = PermissibleValue(text="TRA")
    TRG = PermissibleValue(text="TRG")

    _defn = EnumDefinition(
        name="V1p5ReceptorVariableDomain2Locus",
    )

class V1p5LigandType(EnumDefinitionImpl):

    protein = PermissibleValue(text="protein")
    peptide = PermissibleValue(text="peptide")

    _defn = EnumDefinition(
        name="V1p5LigandType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "MHC:peptide",
            PermissibleValue(text="MHC:peptide"))
        setattr(cls, "MHC:non-peptide",
            PermissibleValue(text="MHC:non-peptide"))
        setattr(cls, "non-peptidic",
            PermissibleValue(text="non-peptidic"))

class V1p5AntigenType(EnumDefinitionImpl):

    protein = PermissibleValue(text="protein")
    peptide = PermissibleValue(text="peptide")

    _defn = EnumDefinition(
        name="V1p5AntigenType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "non-peptidic",
            PermissibleValue(text="non-peptidic"))

class V1p5Antigen(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5Antigen",
    )

class V1p5AntigenSourceSpecies(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5AntigenSourceSpecies",
    )

class V1p5MhcGene1(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5MhcGene1",
    )

class V1p5MhcGene2(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5MhcGene2",
    )

class V1p5ReactivityMethod(EnumDefinitionImpl):

    SPR = PermissibleValue(text="SPR")
    ITC = PermissibleValue(text="ITC")
    ELISA = PermissibleValue(text="ELISA")
    cytometry = PermissibleValue(text="cytometry")
    biological_activity = PermissibleValue(text="biological_activity")

    _defn = EnumDefinition(
        name="V1p5ReactivityMethod",
    )

class V1p5ReactivityReadout(EnumDefinitionImpl):

    binding_strength = PermissibleValue(text="binding_strength")
    cytokine_release = PermissibleValue(text="cytokine_release")
    dissociation_constant_kd = PermissibleValue(text="dissociation_constant_kd")
    on_rate = PermissibleValue(text="on_rate")
    off_rate = PermissibleValue(text="off_rate")
    pathogen_inhibition = PermissibleValue(text="pathogen_inhibition")

    _defn = EnumDefinition(
        name="V1p5ReactivityReadout",
    )

class V1p4Unit(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4Unit",
    )

class V1p4OrcidId(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4OrcidId",
    )

class V1p4Affiliation(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4Affiliation",
    )

class V1p4Role(EnumDefinitionImpl):

    conceptualization = PermissibleValue(text="conceptualization")
    investigation = PermissibleValue(text="investigation")
    methodology = PermissibleValue(text="methodology")
    resources = PermissibleValue(text="resources")
    software = PermissibleValue(text="software")
    supervision = PermissibleValue(text="supervision")
    validation = PermissibleValue(text="validation")
    visualization = PermissibleValue(text="visualization")

    _defn = EnumDefinition(
        name="V1p4Role",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "data curation",
            PermissibleValue(text="data curation"))
        setattr(cls, "formal analysis",
            PermissibleValue(text="formal analysis"))
        setattr(cls, "funding acquisition",
            PermissibleValue(text="funding acquisition"))
        setattr(cls, "project administration",
            PermissibleValue(text="project administration"))
        setattr(cls, "writing - original draft",
            PermissibleValue(text="writing - original draft"))
        setattr(cls, "writing - review & editing",
            PermissibleValue(text="writing - review & editing"))

class V1p4Degree(EnumDefinitionImpl):

    lead = PermissibleValue(text="lead")
    equal = PermissibleValue(text="equal")
    supporting = PermissibleValue(text="supporting")

    _defn = EnumDefinition(
        name="V1p4Degree",
    )

class V1p4Derivation(EnumDefinitionImpl):

    DNA = PermissibleValue(text="DNA")
    RNA = PermissibleValue(text="RNA")

    _defn = EnumDefinition(
        name="V1p4Derivation",
    )

class V1p4ObservationType(EnumDefinitionImpl):

    direct_sequencing = PermissibleValue(text="direct_sequencing")
    inference_from_repertoire = PermissibleValue(text="inference_from_repertoire")

    _defn = EnumDefinition(
        name="V1p4ObservationType",
    )

class V1p4Strand(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4Strand",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "+",
            PermissibleValue(text="+"))
        setattr(cls, "-",
            PermissibleValue(text="-"))

class V1p4Locus(EnumDefinitionImpl):

    IGH = PermissibleValue(text="IGH")
    IGI = PermissibleValue(text="IGI")
    IGK = PermissibleValue(text="IGK")
    IGL = PermissibleValue(text="IGL")
    TRA = PermissibleValue(text="TRA")
    TRB = PermissibleValue(text="TRB")
    TRG = PermissibleValue(text="TRG")
    TRD = PermissibleValue(text="TRD")

    _defn = EnumDefinition(
        name="V1p4Locus",
    )

class V1p4SequenceType(EnumDefinitionImpl):

    V = PermissibleValue(text="V")
    D = PermissibleValue(text="D")
    J = PermissibleValue(text="J")
    C = PermissibleValue(text="C")

    _defn = EnumDefinition(
        name="V1p4SequenceType",
    )

class V1p4InferenceType(EnumDefinitionImpl):

    genomic_and_rearranged = PermissibleValue(text="genomic_and_rearranged")
    genomic_only = PermissibleValue(text="genomic_only")
    rearranged_only = PermissibleValue(text="rearranged_only")

    _defn = EnumDefinition(
        name="V1p4InferenceType",
    )

class V1p4Species(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4Species",
    )

class V1p4SpeciesSubgroupType(EnumDefinitionImpl):

    breed = PermissibleValue(text="breed")
    strain = PermissibleValue(text="strain")
    inbred = PermissibleValue(text="inbred")
    outbred = PermissibleValue(text="outbred")
    locational = PermissibleValue(text="locational")

    _defn = EnumDefinition(
        name="V1p4SpeciesSubgroupType",
    )

class V1p4Status(EnumDefinitionImpl):

    active = PermissibleValue(text="active")
    draft = PermissibleValue(text="draft")
    retired = PermissibleValue(text="retired")
    withdrawn = PermissibleValue(text="withdrawn")

    _defn = EnumDefinition(
        name="V1p4Status",
    )

class V1p4JCodonFrame(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4JCodonFrame",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1",
            PermissibleValue(text="1"))
        setattr(cls, "2",
            PermissibleValue(text="2"))
        setattr(cls, "3",
            PermissibleValue(text="3"))

class V1p4CurationalTags(EnumDefinitionImpl):

    likely_truncated = PermissibleValue(text="likely_truncated")
    likely_full_length = PermissibleValue(text="likely_full_length")

    _defn = EnumDefinition(
        name="V1p4CurationalTags",
    )

class V1p4InferenceProcess(EnumDefinitionImpl):

    genomic_sequencing = PermissibleValue(text="genomic_sequencing")
    repertoire_sequencing = PermissibleValue(text="repertoire_sequencing")

    _defn = EnumDefinition(
        name="V1p4InferenceProcess",
    )

class V1p4MhcClass(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4MhcClass",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "MHC-I",
            PermissibleValue(text="MHC-I"))
        setattr(cls, "MHC-II",
            PermissibleValue(text="MHC-II"))
        setattr(cls, "MHC-nonclassical",
            PermissibleValue(text="MHC-nonclassical"))

class V1p4Gene(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4Gene",
    )

class V1p4StudyType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4StudyType",
    )

class V1p4KeywordsStudy(EnumDefinitionImpl):

    contains_ig = PermissibleValue(text="contains_ig")
    contains_tr = PermissibleValue(text="contains_tr")
    contains_paired_chain = PermissibleValue(text="contains_paired_chain")
    contains_schema_rearrangement = PermissibleValue(text="contains_schema_rearrangement")
    contains_schema_clone = PermissibleValue(text="contains_schema_clone")
    contains_schema_cell = PermissibleValue(text="contains_schema_cell")
    contains_schema_receptor = PermissibleValue(text="contains_schema_receptor")
    contains_schema_cellexpression = PermissibleValue(text="contains_schema_cellexpression")
    contains_schema_receptorreactivity = PermissibleValue(text="contains_schema_receptorreactivity")

    _defn = EnumDefinition(
        name="V1p4KeywordsStudy",
    )

class V1p4Sex(EnumDefinitionImpl):

    male = PermissibleValue(text="male")
    female = PermissibleValue(text="female")
    pooled = PermissibleValue(text="pooled")
    hermaphrodite = PermissibleValue(text="hermaphrodite")
    intersex = PermissibleValue(text="intersex")

    _defn = EnumDefinition(
        name="V1p4Sex",
    )

class V1p4AncestryPopulation(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4AncestryPopulation",
    )

class V1p4LocationBirth(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4LocationBirth",
    )

class V1p4DiseaseDiagnosis(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4DiseaseDiagnosis",
    )

class V1p4Tissue(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4Tissue",
    )

class V1p4CollectionLocation(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4CollectionLocation",
    )

class V1p4CellSubset(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4CellSubset",
    )

class V1p4CellSpecies(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4CellSpecies",
    )

class V1p4PcrTargetLocus(EnumDefinitionImpl):

    IGH = PermissibleValue(text="IGH")
    IGI = PermissibleValue(text="IGI")
    IGK = PermissibleValue(text="IGK")
    IGL = PermissibleValue(text="IGL")
    TRA = PermissibleValue(text="TRA")
    TRB = PermissibleValue(text="TRB")
    TRD = PermissibleValue(text="TRD")
    TRG = PermissibleValue(text="TRG")

    _defn = EnumDefinition(
        name="V1p4PcrTargetLocus",
    )

class V1p4TemplateClass(EnumDefinitionImpl):

    DNA = PermissibleValue(text="DNA")
    RNA = PermissibleValue(text="RNA")

    _defn = EnumDefinition(
        name="V1p4TemplateClass",
    )

class V1p4LibraryGenerationMethod(EnumDefinitionImpl):

    PCR = PermissibleValue(text="PCR")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="V1p4LibraryGenerationMethod",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "RT(RHP)+PCR",
            PermissibleValue(text="RT(RHP)+PCR"))
        setattr(cls, "RT(oligo-dT)+PCR",
            PermissibleValue(text="RT(oligo-dT)+PCR"))
        setattr(cls, "RT(oligo-dT)+TS+PCR",
            PermissibleValue(text="RT(oligo-dT)+TS+PCR"))
        setattr(cls, "RT(oligo-dT)+TS(UMI)+PCR",
            PermissibleValue(text="RT(oligo-dT)+TS(UMI)+PCR"))
        setattr(cls, "RT(specific)+PCR",
            PermissibleValue(text="RT(specific)+PCR"))
        setattr(cls, "RT(specific)+TS+PCR",
            PermissibleValue(text="RT(specific)+TS+PCR"))
        setattr(cls, "RT(specific)+TS(UMI)+PCR",
            PermissibleValue(text="RT(specific)+TS(UMI)+PCR"))
        setattr(cls, "RT(specific+UMI)+PCR",
            PermissibleValue(text="RT(specific+UMI)+PCR"))
        setattr(cls, "RT(specific+UMI)+TS+PCR",
            PermissibleValue(text="RT(specific+UMI)+TS+PCR"))
        setattr(cls, "RT(specific)+TS",
            PermissibleValue(text="RT(specific)+TS"))

class V1p4CompleteSequences(EnumDefinitionImpl):

    partial = PermissibleValue(text="partial")
    complete = PermissibleValue(text="complete")
    mixed = PermissibleValue(text="mixed")

    _defn = EnumDefinition(
        name="V1p4CompleteSequences",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "complete+untemplated",
            PermissibleValue(text="complete+untemplated"))

class V1p4PhysicalLinkage(EnumDefinitionImpl):

    none = PermissibleValue(text="none")
    hetero_prelinked = PermissibleValue(text="hetero_prelinked")

    _defn = EnumDefinition(
        name="V1p4PhysicalLinkage",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "hetero_head-head",
            PermissibleValue(text="hetero_head-head"))
        setattr(cls, "hetero_tail-head",
            PermissibleValue(text="hetero_tail-head"))

class V1p4FileType(EnumDefinitionImpl):

    fasta = PermissibleValue(text="fasta")
    fastq = PermissibleValue(text="fastq")

    _defn = EnumDefinition(
        name="V1p4FileType",
    )

class V1p4ReadDirection(EnumDefinitionImpl):

    forward = PermissibleValue(text="forward")
    reverse = PermissibleValue(text="reverse")
    mixed = PermissibleValue(text="mixed")

    _defn = EnumDefinition(
        name="V1p4ReadDirection",
    )

class V1p4PairedReadDirection(EnumDefinitionImpl):

    forward = PermissibleValue(text="forward")
    reverse = PermissibleValue(text="reverse")
    mixed = PermissibleValue(text="mixed")

    _defn = EnumDefinition(
        name="V1p4PairedReadDirection",
    )

class V1p4LocusSpecies(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4LocusSpecies",
    )

class V1p4Property(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4Property",
    )

class V1p4ReceptorType(EnumDefinitionImpl):

    Ig = PermissibleValue(text="Ig")
    TCR = PermissibleValue(text="TCR")

    _defn = EnumDefinition(
        name="V1p4ReceptorType",
    )

class V1p4ReceptorVariableDomain1Locus(EnumDefinitionImpl):

    IGH = PermissibleValue(text="IGH")
    TRB = PermissibleValue(text="TRB")
    TRD = PermissibleValue(text="TRD")

    _defn = EnumDefinition(
        name="V1p4ReceptorVariableDomain1Locus",
    )

class V1p4ReceptorVariableDomain2Locus(EnumDefinitionImpl):

    IGI = PermissibleValue(text="IGI")
    IGK = PermissibleValue(text="IGK")
    IGL = PermissibleValue(text="IGL")
    TRA = PermissibleValue(text="TRA")
    TRG = PermissibleValue(text="TRG")

    _defn = EnumDefinition(
        name="V1p4ReceptorVariableDomain2Locus",
    )

class V1p4LigandType(EnumDefinitionImpl):

    protein = PermissibleValue(text="protein")
    peptide = PermissibleValue(text="peptide")

    _defn = EnumDefinition(
        name="V1p4LigandType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "MHC:peptide",
            PermissibleValue(text="MHC:peptide"))
        setattr(cls, "MHC:non-peptide",
            PermissibleValue(text="MHC:non-peptide"))
        setattr(cls, "non-peptidic",
            PermissibleValue(text="non-peptidic"))

class V1p4AntigenType(EnumDefinitionImpl):

    protein = PermissibleValue(text="protein")
    peptide = PermissibleValue(text="peptide")

    _defn = EnumDefinition(
        name="V1p4AntigenType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "non-peptidic",
            PermissibleValue(text="non-peptidic"))

class V1p4Antigen(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4Antigen",
    )

class V1p4AntigenSourceSpecies(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4AntigenSourceSpecies",
    )

class V1p4MhcGene1(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4MhcGene1",
    )

class V1p4MhcGene2(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p4MhcGene2",
    )

# Slots
class slots:
    pass

slots.akc_id = Slot(uri=SCHEMA.identifier, name="akc_id", curie=SCHEMA.curie('identifier'),
                   model_uri=AK_SCHEMA.akc_id, domain=None, range=URIRef)

slots.source_uri = Slot(uri=SCHEMA.identifier, name="source_uri", curie=SCHEMA.curie('identifier'),
                   model_uri=AK_SCHEMA.source_uri, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=AK_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=AK_SCHEMA.description, domain=None, range=Optional[str])

slots.archival_id = Slot(uri=SCHEMA.identifier, name="archival_id", curie=SCHEMA.curie('identifier'),
                   model_uri=AK_SCHEMA.archival_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.inclusion_criteria = Slot(uri=AK_SCHEMA.inclusion_criteria, name="inclusion_criteria", curie=AK_SCHEMA.curie('inclusion_criteria'),
                   model_uri=AK_SCHEMA.inclusion_criteria, domain=None, range=Optional[str])

slots.exclusion_criteria = Slot(uri=AK_SCHEMA.exclusion_criteria, name="exclusion_criteria", curie=AK_SCHEMA.curie('exclusion_criteria'),
                   model_uri=AK_SCHEMA.exclusion_criteria, domain=None, range=Optional[str])

slots.update_date = Slot(uri=AK_SCHEMA.update_date, name="update_date", curie=AK_SCHEMA.curie('update_date'),
                   model_uri=AK_SCHEMA.update_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.participants = Slot(uri=RO['0000057'], name="participants", curie=RO.curie('0000057'),
                   model_uri=AK_SCHEMA.participants, domain=None, range=Optional[Union[Union[str, ParticipantAkcId], List[Union[str, ParticipantAkcId]]]])

slots.assays = Slot(uri=AK_SCHEMA.assays, name="assays", curie=AK_SCHEMA.curie('assays'),
                   model_uri=AK_SCHEMA.assays, domain=None, range=Optional[Union[Union[str, AssayAkcId], List[Union[str, AssayAkcId]]]])

slots.simulations = Slot(uri=AK_SCHEMA.simulations, name="simulations", curie=AK_SCHEMA.curie('simulations'),
                   model_uri=AK_SCHEMA.simulations, domain=None, range=Optional[Union[Union[str, SimulationAkcId], List[Union[str, SimulationAkcId]]]])

slots.documents = Slot(uri=AK_SCHEMA.documents, name="documents", curie=AK_SCHEMA.curie('documents'),
                   model_uri=AK_SCHEMA.documents, domain=None, range=Optional[Union[Union[str, ReferenceSourceUri], List[Union[str, ReferenceSourceUri]]]])

slots.conclusions = Slot(uri=AK_SCHEMA.conclusions, name="conclusions", curie=AK_SCHEMA.curie('conclusions'),
                   model_uri=AK_SCHEMA.conclusions, domain=None, range=Optional[Union[Union[str, ConclusionAkcId], List[Union[str, ConclusionAkcId]]]])

slots.sources = Slot(uri=SCHEMA.identifier, name="sources", curie=SCHEMA.curie('identifier'),
                   model_uri=AK_SCHEMA.sources, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.investigations = Slot(uri=IAO['0000136'], name="investigations", curie=IAO.curie('0000136'),
                   model_uri=AK_SCHEMA.investigations, domain=None, range=Optional[Union[Union[str, InvestigationAkcId], List[Union[str, InvestigationAkcId]]]])

slots.title = Slot(uri=SCHEMA.name, name="title", curie=SCHEMA.curie('name'),
                   model_uri=AK_SCHEMA.title, domain=None, range=Optional[str])

slots.authors = Slot(uri=SCHEMA.author, name="authors", curie=SCHEMA.curie('author'),
                   model_uri=AK_SCHEMA.authors, domain=None, range=Optional[Union[str, List[str]]])

slots.journal = Slot(uri=AK_SCHEMA.journal, name="journal", curie=AK_SCHEMA.curie('journal'),
                   model_uri=AK_SCHEMA.journal, domain=None, range=Optional[str])

slots.issue = Slot(uri=SCHEMA.issueNumber, name="issue", curie=SCHEMA.curie('issueNumber'),
                   model_uri=AK_SCHEMA.issue, domain=None, range=Optional[str])

slots.month = Slot(uri=AK_SCHEMA.month, name="month", curie=AK_SCHEMA.curie('month'),
                   model_uri=AK_SCHEMA.month, domain=None, range=Optional[str])

slots.year = Slot(uri=AK_SCHEMA.year, name="year", curie=AK_SCHEMA.curie('year'),
                   model_uri=AK_SCHEMA.year, domain=None, range=Optional[int],
                   pattern=re.compile(r'19\d\d|20\d\d'))

slots.pages = Slot(uri=AK_SCHEMA.pages, name="pages", curie=AK_SCHEMA.curie('pages'),
                   model_uri=AK_SCHEMA.pages, domain=None, range=Optional[str])

slots.investigation = Slot(uri=RO['0000056'], name="investigation", curie=RO.curie('0000056'),
                   model_uri=AK_SCHEMA.investigation, domain=None, range=Optional[Union[str, InvestigationAkcId]])

slots.study_arm = Slot(uri=RO['0002350'], name="study_arm", curie=RO.curie('0002350'),
                   model_uri=AK_SCHEMA.study_arm, domain=None, range=Optional[Union[str, StudyArmAkcId]])

slots.species = Slot(uri=RDF.type, name="species", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.species, domain=None, range=Optional[Union[str, "Species"]])

slots.biological_sex = Slot(uri=RO['0000053'], name="biological_sex", curie=RO.curie('0000053'),
                   model_uri=AK_SCHEMA.biological_sex, domain=None, range=Optional[Union[str, "BiologicalSex"]])

slots.phenotypic_sex = Slot(uri=RO['0000053'], name="phenotypic_sex", curie=RO.curie('0000053'),
                   model_uri=AK_SCHEMA.phenotypic_sex, domain=None, range=Optional[Union[str, "PhenotypicSex"]])

slots.age = Slot(uri=AK_SCHEMA.age, name="age", curie=AK_SCHEMA.curie('age'),
                   model_uri=AK_SCHEMA.age, domain=None, range=Optional[str])

slots.age_event = Slot(uri=AK_SCHEMA.age_event, name="age_event", curie=AK_SCHEMA.curie('age_event'),
                   model_uri=AK_SCHEMA.age_event, domain=None, range=Optional[Union[str, LifeEventAkcId]])

slots.race = Slot(uri=AK_SCHEMA.race, name="race", curie=AK_SCHEMA.curie('race'),
                   model_uri=AK_SCHEMA.race, domain=None, range=Optional[Union[str, "Race"]])

slots.ethnicity = Slot(uri=AK_SCHEMA.ethnicity, name="ethnicity", curie=AK_SCHEMA.curie('ethnicity'),
                   model_uri=AK_SCHEMA.ethnicity, domain=None, range=Optional[Union[str, "Ethnicity"]])

slots.geolocation = Slot(uri=RO['0001025'], name="geolocation", curie=RO.curie('0001025'),
                   model_uri=AK_SCHEMA.geolocation, domain=None, range=Optional[Union[str, "Geolocation"]])

slots.strain = Slot(uri=AK_SCHEMA.strain, name="strain", curie=AK_SCHEMA.curie('strain'),
                   model_uri=AK_SCHEMA.strain, domain=None, range=Optional[Union[str, "Strain"]])

slots.study_arms = Slot(uri=AK_SCHEMA.study_arms, name="study_arms", curie=AK_SCHEMA.curie('study_arms'),
                   model_uri=AK_SCHEMA.study_arms, domain=None, range=Optional[Union[Union[str, StudyArmAkcId], List[Union[str, StudyArmAkcId]]]])

slots.participant = Slot(uri=RO['0000057'], name="participant", curie=RO.curie('0000057'),
                   model_uri=AK_SCHEMA.participant, domain=None, range=Optional[Union[str, ParticipantAkcId]])

slots.study_event = Slot(uri=AK_SCHEMA.study_event, name="study_event", curie=AK_SCHEMA.curie('study_event'),
                   model_uri=AK_SCHEMA.study_event, domain=None, range=Optional[Union[str, StudyEventAkcId]])

slots.life_event_type = Slot(uri=RDF.type, name="life_event_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.life_event_type, domain=None, range=Optional[Union[str, "LifeEventProcess"]])

slots.t0_event = Slot(uri=AK_SCHEMA.t0_event, name="t0_event", curie=AK_SCHEMA.curie('t0_event'),
                   model_uri=AK_SCHEMA.t0_event, domain=None, range=Optional[str])

slots.t0_event_type = Slot(uri=AK_SCHEMA.t0_event_type, name="t0_event_type", curie=AK_SCHEMA.curie('t0_event_type'),
                   model_uri=AK_SCHEMA.t0_event_type, domain=None, range=Optional[str])

slots.start = Slot(uri=AK_SCHEMA.start, name="start", curie=AK_SCHEMA.curie('start'),
                   model_uri=AK_SCHEMA.start, domain=None, range=Optional[Decimal])

slots.duration = Slot(uri=AK_SCHEMA.duration, name="duration", curie=AK_SCHEMA.curie('duration'),
                   model_uri=AK_SCHEMA.duration, domain=None, range=Optional[Decimal])

slots.time_unit = Slot(uri=AK_SCHEMA.time_unit, name="time_unit", curie=AK_SCHEMA.curie('time_unit'),
                   model_uri=AK_SCHEMA.time_unit, domain=None, range=Optional[str])

slots.life_event = Slot(uri=AK_SCHEMA.life_event, name="life_event", curie=AK_SCHEMA.curie('life_event'),
                   model_uri=AK_SCHEMA.life_event, domain=None, range=Optional[Union[str, LifeEventAkcId]])

slots.exposure_material = Slot(uri=RO['0000057'], name="exposure_material", curie=RO.curie('0000057'),
                   model_uri=AK_SCHEMA.exposure_material, domain=None, range=Optional[Union[str, "ExposureMaterial"]])

slots.disease = Slot(uri=AK_SCHEMA.disease, name="disease", curie=AK_SCHEMA.curie('disease'),
                   model_uri=AK_SCHEMA.disease, domain=None, range=Optional[Union[str, "Disease"]])

slots.disease_stage = Slot(uri=AK_SCHEMA.disease_stage, name="disease_stage", curie=AK_SCHEMA.curie('disease_stage'),
                   model_uri=AK_SCHEMA.disease_stage, domain=None, range=Optional[Union[str, "DiseaseStage"]])

slots.disease_severity = Slot(uri=AK_SCHEMA.disease_severity, name="disease_severity", curie=AK_SCHEMA.curie('disease_severity'),
                   model_uri=AK_SCHEMA.disease_severity, domain=None, range=Optional[str])

slots.type = Slot(uri=AK_SCHEMA.type, name="type", curie=AK_SCHEMA.curie('type'),
                   model_uri=AK_SCHEMA.type, domain=None, range=Optional[str])

slots.specimen_type = Slot(uri=RDF.type, name="specimen_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.specimen_type, domain=None, range=Optional[str])

slots.process = Slot(uri=AK_SCHEMA.process, name="process", curie=AK_SCHEMA.curie('process'),
                   model_uri=AK_SCHEMA.process, domain=None, range=Optional[str])

slots.specimen = Slot(uri=OBI['0000293'], name="specimen", curie=OBI.curie('0000293'),
                   model_uri=AK_SCHEMA.specimen, domain=None, range=Optional[Union[str, SpecimenAkcId]])

slots.specimen_processing = Slot(uri=BFO['0000051'], name="specimen_processing", curie=BFO.curie('0000051'),
                   model_uri=AK_SCHEMA.specimen_processing, domain=None, range=Optional[Union[Union[str, SpecimenProcessingAkcId], List[Union[str, SpecimenProcessingAkcId]]]])

slots.assay_type = Slot(uri=RDF.type, name="assay_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.assay_type, domain=None, range=Optional[str])

slots.target_entity_type = Slot(uri=AK_SCHEMA.target_entity_type, name="target_entity_type", curie=AK_SCHEMA.curie('target_entity_type'),
                   model_uri=AK_SCHEMA.target_entity_type, domain=None, range=Optional[str])

slots.epitope = Slot(uri=AK_SCHEMA.epitope, name="epitope", curie=AK_SCHEMA.curie('epitope'),
                   model_uri=AK_SCHEMA.epitope, domain=None, range=Optional[Union[str, EpitopeAkcId]])

slots.tcell_receptors = Slot(uri=AK_SCHEMA.tcell_receptors, name="tcell_receptors", curie=AK_SCHEMA.curie('tcell_receptors'),
                   model_uri=AK_SCHEMA.tcell_receptors, domain=None, range=Optional[Union[Union[str, TCellReceptorAkcId], List[Union[str, TCellReceptorAkcId]]]])

slots.value = Slot(uri=AK_SCHEMA.value, name="value", curie=AK_SCHEMA.curie('value'),
                   model_uri=AK_SCHEMA.value, domain=None, range=Optional[str])

slots.unit = Slot(uri=AK_SCHEMA.unit, name="unit", curie=AK_SCHEMA.curie('unit'),
                   model_uri=AK_SCHEMA.unit, domain=None, range=Optional[str])

slots.assessments = Slot(uri=IAO['0000136'], name="assessments", curie=IAO.curie('0000136'),
                   model_uri=AK_SCHEMA.assessments, domain=None, range=Optional[Union[Union[str, AssessmentAkcId], List[Union[str, AssessmentAkcId]]]])

slots.datasets = Slot(uri=AK_SCHEMA.datasets, name="datasets", curie=AK_SCHEMA.curie('datasets'),
                   model_uri=AK_SCHEMA.datasets, domain=None, range=Optional[Union[Union[str, DatasetAkcId], List[Union[str, DatasetAkcId]]]])

slots.result = Slot(uri=AK_SCHEMA.result, name="result", curie=AK_SCHEMA.curie('result'),
                   model_uri=AK_SCHEMA.result, domain=None, range=Optional[str])

slots.data_location_type = Slot(uri=AK_SCHEMA.data_location_type, name="data_location_type", curie=AK_SCHEMA.curie('data_location_type'),
                   model_uri=AK_SCHEMA.data_location_type, domain=None, range=Optional[str])

slots.data_location_value = Slot(uri=AK_SCHEMA.data_location_value, name="data_location_value", curie=AK_SCHEMA.curie('data_location_value'),
                   model_uri=AK_SCHEMA.data_location_value, domain=None, range=Optional[str])

slots.organism = Slot(uri=IAO['0000136'], name="organism", curie=IAO.curie('0000136'),
                   model_uri=AK_SCHEMA.organism, domain=None, range=Optional[Union[str, "Species"]])

slots.experiment_type = Slot(uri=AK_SCHEMA.experiment_type, name="experiment_type", curie=AK_SCHEMA.curie('experiment_type'),
                   model_uri=AK_SCHEMA.experiment_type, domain=None, range=Optional[str])

slots.assessment_type = Slot(uri=RDF.type, name="assessment_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.assessment_type, domain=None, range=Optional[str])

slots.chain_type = Slot(uri=AK_SCHEMA.chain_type, name="chain_type", curie=AK_SCHEMA.curie('chain_type'),
                   model_uri=AK_SCHEMA.chain_type, domain=None, range=Optional[Union[str, "ChainType"]])

slots.isotype = Slot(uri=AK_SCHEMA.isotype, name="isotype", curie=AK_SCHEMA.curie('isotype'),
                   model_uri=AK_SCHEMA.isotype, domain=None, range=Optional[str])

slots.IGH_chain = Slot(uri=AK_SCHEMA.IGH_chain, name="IGH_chain", curie=AK_SCHEMA.curie('IGH_chain'),
                   model_uri=AK_SCHEMA.IGH_chain, domain=None, range=Optional[Union[str, ChainAkcId]])

slots.IGL_chain = Slot(uri=AK_SCHEMA.IGL_chain, name="IGL_chain", curie=AK_SCHEMA.curie('IGL_chain'),
                   model_uri=AK_SCHEMA.IGL_chain, domain=None, range=Optional[Union[str, ChainAkcId]])

slots.IGK_chain = Slot(uri=AK_SCHEMA.IGK_chain, name="IGK_chain", curie=AK_SCHEMA.curie('IGK_chain'),
                   model_uri=AK_SCHEMA.IGK_chain, domain=None, range=Optional[Union[str, ChainAkcId]])

slots.TRA_chain = Slot(uri=AK_SCHEMA.TRA_chain, name="TRA_chain", curie=AK_SCHEMA.curie('TRA_chain'),
                   model_uri=AK_SCHEMA.TRA_chain, domain=None, range=Optional[Union[str, ChainAkcId]])

slots.TRB_chain = Slot(uri=AK_SCHEMA.TRB_chain, name="TRB_chain", curie=AK_SCHEMA.curie('TRB_chain'),
                   model_uri=AK_SCHEMA.TRB_chain, domain=None, range=Optional[Union[str, ChainAkcId]])

slots.TRD_chain = Slot(uri=AK_SCHEMA.TRD_chain, name="TRD_chain", curie=AK_SCHEMA.curie('TRD_chain'),
                   model_uri=AK_SCHEMA.TRD_chain, domain=None, range=Optional[Union[str, ChainAkcId]])

slots.TRG_chain = Slot(uri=AK_SCHEMA.TRG_chain, name="TRG_chain", curie=AK_SCHEMA.curie('TRG_chain'),
                   model_uri=AK_SCHEMA.TRG_chain, domain=None, range=Optional[Union[str, ChainAkcId]])

slots.source_protein = Slot(uri=AK_SCHEMA.source_protein, name="source_protein", curie=AK_SCHEMA.curie('source_protein'),
                   model_uri=AK_SCHEMA.source_protein, domain=None, range=Optional[str])

slots.source_organism = Slot(uri=AK_SCHEMA.source_organism, name="source_organism", curie=AK_SCHEMA.curie('source_organism'),
                   model_uri=AK_SCHEMA.source_organism, domain=None, range=Optional[str])

slots.chain_domain = Slot(uri=AK_SCHEMA.chain_domain, name="chain_domain", curie=AK_SCHEMA.curie('chain_domain'),
                   model_uri=AK_SCHEMA.chain_domain, domain=None, range=Optional[Union[str, ChainAkcId]])

slots.chain_codomain = Slot(uri=AK_SCHEMA.chain_codomain, name="chain_codomain", curie=AK_SCHEMA.curie('chain_codomain'),
                   model_uri=AK_SCHEMA.chain_codomain, domain=None, range=Optional[Union[str, ChainAkcId]])

slots.chain_similarity_type = Slot(uri=RDF.type, name="chain_similarity_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.chain_similarity_type, domain=None, range=Optional[Union[str, "ChainSimilarityType"]])

slots.label = Slot(uri=AK_SCHEMA.label, name="label", curie=AK_SCHEMA.curie('label'),
                   model_uri=AK_SCHEMA.label, domain=None, range=Optional[str])

slots.acknowledgement_id = Slot(uri=AK_SCHEMA.acknowledgement_id, name="acknowledgement_id", curie=AK_SCHEMA.curie('acknowledgement_id'),
                   model_uri=AK_SCHEMA.acknowledgement_id, domain=None, range=Optional[str])

slots.institution_name = Slot(uri=AK_SCHEMA.institution_name, name="institution_name", curie=AK_SCHEMA.curie('institution_name'),
                   model_uri=AK_SCHEMA.institution_name, domain=None, range=Optional[str])

slots.orcid_id = Slot(uri=AK_SCHEMA.orcid_id, name="orcid_id", curie=AK_SCHEMA.curie('orcid_id'),
                   model_uri=AK_SCHEMA.orcid_id, domain=None, range=Optional[str])

slots.sequence_id = Slot(uri=AK_SCHEMA.sequence_id, name="sequence_id", curie=AK_SCHEMA.curie('sequence_id'),
                   model_uri=AK_SCHEMA.sequence_id, domain=None, range=Optional[str])

slots.sequence = Slot(uri=AK_SCHEMA.sequence, name="sequence", curie=AK_SCHEMA.curie('sequence'),
                   model_uri=AK_SCHEMA.sequence, domain=None, range=Optional[str])

slots.derivation = Slot(uri=AK_SCHEMA.derivation, name="derivation", curie=AK_SCHEMA.curie('derivation'),
                   model_uri=AK_SCHEMA.derivation, domain=None, range=Optional[Union[str, "Derivation"]])

slots.observation_type = Slot(uri=RDF.type, name="observation_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.observation_type, domain=None, range=Optional[Union[str, "ObservationType"]])

slots.curation = Slot(uri=AK_SCHEMA.curation, name="curation", curie=AK_SCHEMA.curie('curation'),
                   model_uri=AK_SCHEMA.curation, domain=None, range=Optional[str])

slots.repository_name = Slot(uri=AK_SCHEMA.repository_name, name="repository_name", curie=AK_SCHEMA.curie('repository_name'),
                   model_uri=AK_SCHEMA.repository_name, domain=None, range=Optional[str])

slots.repository_ref = Slot(uri=AK_SCHEMA.repository_ref, name="repository_ref", curie=AK_SCHEMA.curie('repository_ref'),
                   model_uri=AK_SCHEMA.repository_ref, domain=None, range=Optional[str])

slots.deposited_version = Slot(uri=AK_SCHEMA.deposited_version, name="deposited_version", curie=AK_SCHEMA.curie('deposited_version'),
                   model_uri=AK_SCHEMA.deposited_version, domain=None, range=Optional[str])

slots.sequence_start = Slot(uri=AK_SCHEMA.sequence_start, name="sequence_start", curie=AK_SCHEMA.curie('sequence_start'),
                   model_uri=AK_SCHEMA.sequence_start, domain=None, range=Optional[int])

slots.sequence_end = Slot(uri=AK_SCHEMA.sequence_end, name="sequence_end", curie=AK_SCHEMA.curie('sequence_end'),
                   model_uri=AK_SCHEMA.sequence_end, domain=None, range=Optional[int])

slots.patch_no = Slot(uri=AK_SCHEMA.patch_no, name="patch_no", curie=AK_SCHEMA.curie('patch_no'),
                   model_uri=AK_SCHEMA.patch_no, domain=None, range=Optional[str])

slots.gff_seqid = Slot(uri=AK_SCHEMA.gff_seqid, name="gff_seqid", curie=AK_SCHEMA.curie('gff_seqid'),
                   model_uri=AK_SCHEMA.gff_seqid, domain=None, range=Optional[str])

slots.gff_start = Slot(uri=AK_SCHEMA.gff_start, name="gff_start", curie=AK_SCHEMA.curie('gff_start'),
                   model_uri=AK_SCHEMA.gff_start, domain=None, range=Optional[int])

slots.gff_end = Slot(uri=AK_SCHEMA.gff_end, name="gff_end", curie=AK_SCHEMA.curie('gff_end'),
                   model_uri=AK_SCHEMA.gff_end, domain=None, range=Optional[int])

slots.strand = Slot(uri=AK_SCHEMA.strand, name="strand", curie=AK_SCHEMA.curie('strand'),
                   model_uri=AK_SCHEMA.strand, domain=None, range=Optional[Union[str, "Strand"]])

slots.sequence_delineation_id = Slot(uri=AK_SCHEMA.sequence_delineation_id, name="sequence_delineation_id", curie=AK_SCHEMA.curie('sequence_delineation_id'),
                   model_uri=AK_SCHEMA.sequence_delineation_id, domain=None, range=Optional[str])

slots.delineation_scheme = Slot(uri=AK_SCHEMA.delineation_scheme, name="delineation_scheme", curie=AK_SCHEMA.curie('delineation_scheme'),
                   model_uri=AK_SCHEMA.delineation_scheme, domain=None, range=Optional[str])

slots.unaligned_sequence = Slot(uri=AK_SCHEMA.unaligned_sequence, name="unaligned_sequence", curie=AK_SCHEMA.curie('unaligned_sequence'),
                   model_uri=AK_SCHEMA.unaligned_sequence, domain=None, range=Optional[str])

slots.aligned_sequence = Slot(uri=AK_SCHEMA.aligned_sequence, name="aligned_sequence", curie=AK_SCHEMA.curie('aligned_sequence'),
                   model_uri=AK_SCHEMA.aligned_sequence, domain=None, range=Optional[str])

slots.fwr1_start = Slot(uri=AK_SCHEMA.fwr1_start, name="fwr1_start", curie=AK_SCHEMA.curie('fwr1_start'),
                   model_uri=AK_SCHEMA.fwr1_start, domain=None, range=Optional[int])

slots.fwr1_end = Slot(uri=AK_SCHEMA.fwr1_end, name="fwr1_end", curie=AK_SCHEMA.curie('fwr1_end'),
                   model_uri=AK_SCHEMA.fwr1_end, domain=None, range=Optional[int])

slots.cdr1_start = Slot(uri=AK_SCHEMA.cdr1_start, name="cdr1_start", curie=AK_SCHEMA.curie('cdr1_start'),
                   model_uri=AK_SCHEMA.cdr1_start, domain=None, range=Optional[int])

slots.cdr1_end = Slot(uri=AK_SCHEMA.cdr1_end, name="cdr1_end", curie=AK_SCHEMA.curie('cdr1_end'),
                   model_uri=AK_SCHEMA.cdr1_end, domain=None, range=Optional[int])

slots.fwr2_start = Slot(uri=AK_SCHEMA.fwr2_start, name="fwr2_start", curie=AK_SCHEMA.curie('fwr2_start'),
                   model_uri=AK_SCHEMA.fwr2_start, domain=None, range=Optional[int])

slots.fwr2_end = Slot(uri=AK_SCHEMA.fwr2_end, name="fwr2_end", curie=AK_SCHEMA.curie('fwr2_end'),
                   model_uri=AK_SCHEMA.fwr2_end, domain=None, range=Optional[int])

slots.cdr2_start = Slot(uri=AK_SCHEMA.cdr2_start, name="cdr2_start", curie=AK_SCHEMA.curie('cdr2_start'),
                   model_uri=AK_SCHEMA.cdr2_start, domain=None, range=Optional[int])

slots.cdr2_end = Slot(uri=AK_SCHEMA.cdr2_end, name="cdr2_end", curie=AK_SCHEMA.curie('cdr2_end'),
                   model_uri=AK_SCHEMA.cdr2_end, domain=None, range=Optional[int])

slots.fwr3_start = Slot(uri=AK_SCHEMA.fwr3_start, name="fwr3_start", curie=AK_SCHEMA.curie('fwr3_start'),
                   model_uri=AK_SCHEMA.fwr3_start, domain=None, range=Optional[int])

slots.fwr3_end = Slot(uri=AK_SCHEMA.fwr3_end, name="fwr3_end", curie=AK_SCHEMA.curie('fwr3_end'),
                   model_uri=AK_SCHEMA.fwr3_end, domain=None, range=Optional[int])

slots.cdr3_start = Slot(uri=AK_SCHEMA.cdr3_start, name="cdr3_start", curie=AK_SCHEMA.curie('cdr3_start'),
                   model_uri=AK_SCHEMA.cdr3_start, domain=None, range=Optional[int])

slots.alignment_labels = Slot(uri=AK_SCHEMA.alignment_labels, name="alignment_labels", curie=AK_SCHEMA.curie('alignment_labels'),
                   model_uri=AK_SCHEMA.alignment_labels, domain=None, range=Optional[Union[str, List[str]]])

slots.allele_description_id = Slot(uri=AK_SCHEMA.allele_description_id, name="allele_description_id", curie=AK_SCHEMA.curie('allele_description_id'),
                   model_uri=AK_SCHEMA.allele_description_id, domain=None, range=Optional[str])

slots.allele_description_ref = Slot(uri=AK_SCHEMA.allele_description_ref, name="allele_description_ref", curie=AK_SCHEMA.curie('allele_description_ref'),
                   model_uri=AK_SCHEMA.allele_description_ref, domain=None, range=Optional[str])

slots.maintainer = Slot(uri=AK_SCHEMA.maintainer, name="maintainer", curie=AK_SCHEMA.curie('maintainer'),
                   model_uri=AK_SCHEMA.maintainer, domain=None, range=Optional[str])

slots.acknowledgements = Slot(uri=AK_SCHEMA.acknowledgements, name="acknowledgements", curie=AK_SCHEMA.curie('acknowledgements'),
                   model_uri=AK_SCHEMA.acknowledgements, domain=None, range=Optional[Union[Union[dict, Acknowledgement], List[Union[dict, Acknowledgement]]]])

slots.lab_address = Slot(uri=AK_SCHEMA.lab_address, name="lab_address", curie=AK_SCHEMA.curie('lab_address'),
                   model_uri=AK_SCHEMA.lab_address, domain=None, range=Optional[str])

slots.release_version = Slot(uri=AK_SCHEMA.release_version, name="release_version", curie=AK_SCHEMA.curie('release_version'),
                   model_uri=AK_SCHEMA.release_version, domain=None, range=Optional[str])

slots.release_date = Slot(uri=AK_SCHEMA.release_date, name="release_date", curie=AK_SCHEMA.curie('release_date'),
                   model_uri=AK_SCHEMA.release_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.release_description = Slot(uri=AK_SCHEMA.release_description, name="release_description", curie=AK_SCHEMA.curie('release_description'),
                   model_uri=AK_SCHEMA.release_description, domain=None, range=Optional[str])

slots.coding_sequence = Slot(uri=AK_SCHEMA.coding_sequence, name="coding_sequence", curie=AK_SCHEMA.curie('coding_sequence'),
                   model_uri=AK_SCHEMA.coding_sequence, domain=None, range=Optional[str])

slots.aliases = Slot(uri=AK_SCHEMA.aliases, name="aliases", curie=AK_SCHEMA.curie('aliases'),
                   model_uri=AK_SCHEMA.aliases, domain=None, range=Optional[Union[str, List[str]]])

slots.locus = Slot(uri=AK_SCHEMA.locus, name="locus", curie=AK_SCHEMA.curie('locus'),
                   model_uri=AK_SCHEMA.locus, domain=None, range=Optional[Union[str, "Locus"]])

slots.chromosome = Slot(uri=AK_SCHEMA.chromosome, name="chromosome", curie=AK_SCHEMA.curie('chromosome'),
                   model_uri=AK_SCHEMA.chromosome, domain=None, range=Optional[int])

slots.sequence_type = Slot(uri=RDF.type, name="sequence_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.sequence_type, domain=None, range=Optional[Union[str, "SequenceType"]])

slots.functional = Slot(uri=AK_SCHEMA.functional, name="functional", curie=AK_SCHEMA.curie('functional'),
                   model_uri=AK_SCHEMA.functional, domain=None, range=Optional[Union[bool, Bool]])

slots.inference_type = Slot(uri=RDF.type, name="inference_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.inference_type, domain=None, range=Optional[Union[str, "InferenceType"]])

slots.species_subgroup = Slot(uri=AK_SCHEMA.species_subgroup, name="species_subgroup", curie=AK_SCHEMA.curie('species_subgroup'),
                   model_uri=AK_SCHEMA.species_subgroup, domain=None, range=Optional[str])

slots.species_subgroup_type = Slot(uri=RDF.type, name="species_subgroup_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.species_subgroup_type, domain=None, range=Optional[Union[str, "SpeciesSubgroupType"]])

slots.status = Slot(uri=AK_SCHEMA.status, name="status", curie=AK_SCHEMA.curie('status'),
                   model_uri=AK_SCHEMA.status, domain=None, range=Optional[Union[str, "Status"]])

slots.subgroup_designation = Slot(uri=AK_SCHEMA.subgroup_designation, name="subgroup_designation", curie=AK_SCHEMA.curie('subgroup_designation'),
                   model_uri=AK_SCHEMA.subgroup_designation, domain=None, range=Optional[str])

slots.gene_designation = Slot(uri=AK_SCHEMA.gene_designation, name="gene_designation", curie=AK_SCHEMA.curie('gene_designation'),
                   model_uri=AK_SCHEMA.gene_designation, domain=None, range=Optional[str])

slots.allele_designation = Slot(uri=AK_SCHEMA.allele_designation, name="allele_designation", curie=AK_SCHEMA.curie('allele_designation'),
                   model_uri=AK_SCHEMA.allele_designation, domain=None, range=Optional[str])

slots.allele_similarity_cluster_designation = Slot(uri=AK_SCHEMA.allele_similarity_cluster_designation, name="allele_similarity_cluster_designation", curie=AK_SCHEMA.curie('allele_similarity_cluster_designation'),
                   model_uri=AK_SCHEMA.allele_similarity_cluster_designation, domain=None, range=Optional[str])

slots.allele_similarity_cluster_member_id = Slot(uri=AK_SCHEMA.allele_similarity_cluster_member_id, name="allele_similarity_cluster_member_id", curie=AK_SCHEMA.curie('allele_similarity_cluster_member_id'),
                   model_uri=AK_SCHEMA.allele_similarity_cluster_member_id, domain=None, range=Optional[str])

slots.j_codon_frame = Slot(uri=AK_SCHEMA.j_codon_frame, name="j_codon_frame", curie=AK_SCHEMA.curie('j_codon_frame'),
                   model_uri=AK_SCHEMA.j_codon_frame, domain=None, range=Optional[Union[str, "JCodonFrame"]])

slots.gene_start = Slot(uri=AK_SCHEMA.gene_start, name="gene_start", curie=AK_SCHEMA.curie('gene_start'),
                   model_uri=AK_SCHEMA.gene_start, domain=None, range=Optional[int])

slots.gene_end = Slot(uri=AK_SCHEMA.gene_end, name="gene_end", curie=AK_SCHEMA.curie('gene_end'),
                   model_uri=AK_SCHEMA.gene_end, domain=None, range=Optional[int])

slots.utr_5_prime_start = Slot(uri=AK_SCHEMA.utr_5_prime_start, name="utr_5_prime_start", curie=AK_SCHEMA.curie('utr_5_prime_start'),
                   model_uri=AK_SCHEMA.utr_5_prime_start, domain=None, range=Optional[int])

slots.utr_5_prime_end = Slot(uri=AK_SCHEMA.utr_5_prime_end, name="utr_5_prime_end", curie=AK_SCHEMA.curie('utr_5_prime_end'),
                   model_uri=AK_SCHEMA.utr_5_prime_end, domain=None, range=Optional[int])

slots.leader_1_start = Slot(uri=AK_SCHEMA.leader_1_start, name="leader_1_start", curie=AK_SCHEMA.curie('leader_1_start'),
                   model_uri=AK_SCHEMA.leader_1_start, domain=None, range=Optional[int])

slots.leader_1_end = Slot(uri=AK_SCHEMA.leader_1_end, name="leader_1_end", curie=AK_SCHEMA.curie('leader_1_end'),
                   model_uri=AK_SCHEMA.leader_1_end, domain=None, range=Optional[int])

slots.leader_2_start = Slot(uri=AK_SCHEMA.leader_2_start, name="leader_2_start", curie=AK_SCHEMA.curie('leader_2_start'),
                   model_uri=AK_SCHEMA.leader_2_start, domain=None, range=Optional[int])

slots.leader_2_end = Slot(uri=AK_SCHEMA.leader_2_end, name="leader_2_end", curie=AK_SCHEMA.curie('leader_2_end'),
                   model_uri=AK_SCHEMA.leader_2_end, domain=None, range=Optional[int])

slots.v_rs_start = Slot(uri=AK_SCHEMA.v_rs_start, name="v_rs_start", curie=AK_SCHEMA.curie('v_rs_start'),
                   model_uri=AK_SCHEMA.v_rs_start, domain=None, range=Optional[int])

slots.v_rs_end = Slot(uri=AK_SCHEMA.v_rs_end, name="v_rs_end", curie=AK_SCHEMA.curie('v_rs_end'),
                   model_uri=AK_SCHEMA.v_rs_end, domain=None, range=Optional[int])

slots.d_rs_3_prime_start = Slot(uri=AK_SCHEMA.d_rs_3_prime_start, name="d_rs_3_prime_start", curie=AK_SCHEMA.curie('d_rs_3_prime_start'),
                   model_uri=AK_SCHEMA.d_rs_3_prime_start, domain=None, range=Optional[int])

slots.d_rs_3_prime_end = Slot(uri=AK_SCHEMA.d_rs_3_prime_end, name="d_rs_3_prime_end", curie=AK_SCHEMA.curie('d_rs_3_prime_end'),
                   model_uri=AK_SCHEMA.d_rs_3_prime_end, domain=None, range=Optional[int])

slots.d_rs_5_prime_start = Slot(uri=AK_SCHEMA.d_rs_5_prime_start, name="d_rs_5_prime_start", curie=AK_SCHEMA.curie('d_rs_5_prime_start'),
                   model_uri=AK_SCHEMA.d_rs_5_prime_start, domain=None, range=Optional[int])

slots.d_rs_5_prime_end = Slot(uri=AK_SCHEMA.d_rs_5_prime_end, name="d_rs_5_prime_end", curie=AK_SCHEMA.curie('d_rs_5_prime_end'),
                   model_uri=AK_SCHEMA.d_rs_5_prime_end, domain=None, range=Optional[int])

slots.j_cdr3_end = Slot(uri=AK_SCHEMA.j_cdr3_end, name="j_cdr3_end", curie=AK_SCHEMA.curie('j_cdr3_end'),
                   model_uri=AK_SCHEMA.j_cdr3_end, domain=None, range=Optional[int])

slots.j_rs_start = Slot(uri=AK_SCHEMA.j_rs_start, name="j_rs_start", curie=AK_SCHEMA.curie('j_rs_start'),
                   model_uri=AK_SCHEMA.j_rs_start, domain=None, range=Optional[int])

slots.j_rs_end = Slot(uri=AK_SCHEMA.j_rs_end, name="j_rs_end", curie=AK_SCHEMA.curie('j_rs_end'),
                   model_uri=AK_SCHEMA.j_rs_end, domain=None, range=Optional[int])

slots.j_donor_splice = Slot(uri=AK_SCHEMA.j_donor_splice, name="j_donor_splice", curie=AK_SCHEMA.curie('j_donor_splice'),
                   model_uri=AK_SCHEMA.j_donor_splice, domain=None, range=Optional[int])

slots.v_gene_delineations = Slot(uri=AK_SCHEMA.v_gene_delineations, name="v_gene_delineations", curie=AK_SCHEMA.curie('v_gene_delineations'),
                   model_uri=AK_SCHEMA.v_gene_delineations, domain=None, range=Optional[Union[Union[dict, SequenceDelineationV], List[Union[dict, SequenceDelineationV]]]])

slots.unrearranged_support = Slot(uri=AK_SCHEMA.unrearranged_support, name="unrearranged_support", curie=AK_SCHEMA.curie('unrearranged_support'),
                   model_uri=AK_SCHEMA.unrearranged_support, domain=None, range=Optional[Union[Union[dict, UnrearrangedSequence], List[Union[dict, UnrearrangedSequence]]]])

slots.rearranged_support = Slot(uri=AK_SCHEMA.rearranged_support, name="rearranged_support", curie=AK_SCHEMA.curie('rearranged_support'),
                   model_uri=AK_SCHEMA.rearranged_support, domain=None, range=Optional[Union[Union[dict, RearrangedSequence], List[Union[dict, RearrangedSequence]]]])

slots.paralogs = Slot(uri=AK_SCHEMA.paralogs, name="paralogs", curie=AK_SCHEMA.curie('paralogs'),
                   model_uri=AK_SCHEMA.paralogs, domain=None, range=Optional[Union[str, List[str]]])

slots.curational_tags = Slot(uri=AK_SCHEMA.curational_tags, name="curational_tags", curie=AK_SCHEMA.curie('curational_tags'),
                   model_uri=AK_SCHEMA.curational_tags, domain=None, range=Optional[Union[Union[str, "CurationalTags"], List[Union[str, "CurationalTags"]]]])

slots.germline_set_id = Slot(uri=AK_SCHEMA.germline_set_id, name="germline_set_id", curie=AK_SCHEMA.curie('germline_set_id'),
                   model_uri=AK_SCHEMA.germline_set_id, domain=None, range=Optional[str])

slots.author = Slot(uri=AK_SCHEMA.author, name="author", curie=AK_SCHEMA.curie('author'),
                   model_uri=AK_SCHEMA.author, domain=None, range=Optional[str])

slots.lab_name = Slot(uri=AK_SCHEMA.lab_name, name="lab_name", curie=AK_SCHEMA.curie('lab_name'),
                   model_uri=AK_SCHEMA.lab_name, domain=None, range=Optional[str])

slots.germline_set_name = Slot(uri=AK_SCHEMA.germline_set_name, name="germline_set_name", curie=AK_SCHEMA.curie('germline_set_name'),
                   model_uri=AK_SCHEMA.germline_set_name, domain=None, range=Optional[str])

slots.germline_set_ref = Slot(uri=AK_SCHEMA.germline_set_ref, name="germline_set_ref", curie=AK_SCHEMA.curie('germline_set_ref'),
                   model_uri=AK_SCHEMA.germline_set_ref, domain=None, range=Optional[str])

slots.pub_ids = Slot(uri=AK_SCHEMA.pub_ids, name="pub_ids", curie=AK_SCHEMA.curie('pub_ids'),
                   model_uri=AK_SCHEMA.pub_ids, domain=None, range=Optional[str])

slots.allele_descriptions = Slot(uri=AK_SCHEMA.allele_descriptions, name="allele_descriptions", curie=AK_SCHEMA.curie('allele_descriptions'),
                   model_uri=AK_SCHEMA.allele_descriptions, domain=None, range=Optional[Union[Union[dict, AlleleDescription], List[Union[dict, AlleleDescription]]]])

slots.receptor_genotype_set_id = Slot(uri=AK_SCHEMA.receptor_genotype_set_id, name="receptor_genotype_set_id", curie=AK_SCHEMA.curie('receptor_genotype_set_id'),
                   model_uri=AK_SCHEMA.receptor_genotype_set_id, domain=None, range=Optional[str])

slots.genotype_class_list = Slot(uri=AK_SCHEMA.genotype_class_list, name="genotype_class_list", curie=AK_SCHEMA.curie('genotype_class_list'),
                   model_uri=AK_SCHEMA.genotype_class_list, domain=None, range=Optional[Union[Union[dict, Genotype], List[Union[dict, Genotype]]]])

slots.receptor_genotype_id = Slot(uri=AK_SCHEMA.receptor_genotype_id, name="receptor_genotype_id", curie=AK_SCHEMA.curie('receptor_genotype_id'),
                   model_uri=AK_SCHEMA.receptor_genotype_id, domain=None, range=Optional[str])

slots.documented_alleles = Slot(uri=AK_SCHEMA.documented_alleles, name="documented_alleles", curie=AK_SCHEMA.curie('documented_alleles'),
                   model_uri=AK_SCHEMA.documented_alleles, domain=None, range=Optional[Union[Union[dict, DocumentedAllele], List[Union[dict, DocumentedAllele]]]])

slots.undocumented_alleles = Slot(uri=AK_SCHEMA.undocumented_alleles, name="undocumented_alleles", curie=AK_SCHEMA.curie('undocumented_alleles'),
                   model_uri=AK_SCHEMA.undocumented_alleles, domain=None, range=Optional[Union[Union[dict, UndocumentedAllele], List[Union[dict, UndocumentedAllele]]]])

slots.deleted_genes = Slot(uri=AK_SCHEMA.deleted_genes, name="deleted_genes", curie=AK_SCHEMA.curie('deleted_genes'),
                   model_uri=AK_SCHEMA.deleted_genes, domain=None, range=Optional[Union[Union[dict, DeletedGene], List[Union[dict, DeletedGene]]]])

slots.inference_process = Slot(uri=AK_SCHEMA.inference_process, name="inference_process", curie=AK_SCHEMA.curie('inference_process'),
                   model_uri=AK_SCHEMA.inference_process, domain=None, range=Optional[Union[str, "InferenceProcess"]])

slots.phasing = Slot(uri=AK_SCHEMA.phasing, name="phasing", curie=AK_SCHEMA.curie('phasing'),
                   model_uri=AK_SCHEMA.phasing, domain=None, range=Optional[int])

slots.allele_name = Slot(uri=AK_SCHEMA.allele_name, name="allele_name", curie=AK_SCHEMA.curie('allele_name'),
                   model_uri=AK_SCHEMA.allele_name, domain=None, range=Optional[str])

slots.mhc_genotype_set_id = Slot(uri=AK_SCHEMA.mhc_genotype_set_id, name="mhc_genotype_set_id", curie=AK_SCHEMA.curie('mhc_genotype_set_id'),
                   model_uri=AK_SCHEMA.mhc_genotype_set_id, domain=None, range=Optional[str])

slots.mhc_genotype_list = Slot(uri=AK_SCHEMA.mhc_genotype_list, name="mhc_genotype_list", curie=AK_SCHEMA.curie('mhc_genotype_list'),
                   model_uri=AK_SCHEMA.mhc_genotype_list, domain=None, range=Optional[Union[Union[dict, MHCGenotype], List[Union[dict, MHCGenotype]]]])

slots.mhc_genotype_id = Slot(uri=AK_SCHEMA.mhc_genotype_id, name="mhc_genotype_id", curie=AK_SCHEMA.curie('mhc_genotype_id'),
                   model_uri=AK_SCHEMA.mhc_genotype_id, domain=None, range=Optional[str])

slots.mhc_class = Slot(uri=AK_SCHEMA.mhc_class, name="mhc_class", curie=AK_SCHEMA.curie('mhc_class'),
                   model_uri=AK_SCHEMA.mhc_class, domain=None, range=Optional[Union[str, "MhcClass"]])

slots.mhc_alleles = Slot(uri=AK_SCHEMA.mhc_alleles, name="mhc_alleles", curie=AK_SCHEMA.curie('mhc_alleles'),
                   model_uri=AK_SCHEMA.mhc_alleles, domain=None, range=Optional[Union[Union[dict, MHCAllele], List[Union[dict, MHCAllele]]]])

slots.mhc_genotyping_method = Slot(uri=AK_SCHEMA.mhc_genotyping_method, name="mhc_genotyping_method", curie=AK_SCHEMA.curie('mhc_genotyping_method'),
                   model_uri=AK_SCHEMA.mhc_genotyping_method, domain=None, range=Optional[str])

slots.gene = Slot(uri=AK_SCHEMA.gene, name="gene", curie=AK_SCHEMA.curie('gene'),
                   model_uri=AK_SCHEMA.gene, domain=None, range=Optional[Union[str, "Gene"]])

slots.reference_set_ref = Slot(uri=AK_SCHEMA.reference_set_ref, name="reference_set_ref", curie=AK_SCHEMA.curie('reference_set_ref'),
                   model_uri=AK_SCHEMA.reference_set_ref, domain=None, range=Optional[str])

slots.receptor_genotype_set = Slot(uri=AK_SCHEMA.receptor_genotype_set, name="receptor_genotype_set", curie=AK_SCHEMA.curie('receptor_genotype_set'),
                   model_uri=AK_SCHEMA.receptor_genotype_set, domain=None, range=Optional[Union[dict, GenotypeSet]])

slots.mhc_genotype_set = Slot(uri=AK_SCHEMA.mhc_genotype_set, name="mhc_genotype_set", curie=AK_SCHEMA.curie('mhc_genotype_set'),
                   model_uri=AK_SCHEMA.mhc_genotype_set, domain=None, range=Optional[Union[dict, MHCGenotypeSet]])

slots.study_id = Slot(uri=AK_SCHEMA.study_id, name="study_id", curie=AK_SCHEMA.curie('study_id'),
                   model_uri=AK_SCHEMA.study_id, domain=None, range=Optional[str])

slots.study_title = Slot(uri=AK_SCHEMA.study_title, name="study_title", curie=AK_SCHEMA.curie('study_title'),
                   model_uri=AK_SCHEMA.study_title, domain=None, range=Optional[str])

slots.study_type = Slot(uri=RDF.type, name="study_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.study_type, domain=None, range=Optional[Union[str, "StudyType"]])

slots.study_description = Slot(uri=AK_SCHEMA.study_description, name="study_description", curie=AK_SCHEMA.curie('study_description'),
                   model_uri=AK_SCHEMA.study_description, domain=None, range=Optional[str])

slots.inclusion_exclusion_criteria = Slot(uri=AK_SCHEMA.inclusion_exclusion_criteria, name="inclusion_exclusion_criteria", curie=AK_SCHEMA.curie('inclusion_exclusion_criteria'),
                   model_uri=AK_SCHEMA.inclusion_exclusion_criteria, domain=None, range=Optional[str])

slots.grants = Slot(uri=AK_SCHEMA.grants, name="grants", curie=AK_SCHEMA.curie('grants'),
                   model_uri=AK_SCHEMA.grants, domain=None, range=Optional[str])

slots.study_contact = Slot(uri=AK_SCHEMA.study_contact, name="study_contact", curie=AK_SCHEMA.curie('study_contact'),
                   model_uri=AK_SCHEMA.study_contact, domain=None, range=Optional[str])

slots.collected_by = Slot(uri=AK_SCHEMA.collected_by, name="collected_by", curie=AK_SCHEMA.curie('collected_by'),
                   model_uri=AK_SCHEMA.collected_by, domain=None, range=Optional[str])

slots.submitted_by = Slot(uri=AK_SCHEMA.submitted_by, name="submitted_by", curie=AK_SCHEMA.curie('submitted_by'),
                   model_uri=AK_SCHEMA.submitted_by, domain=None, range=Optional[str])

slots.keywords_study = Slot(uri=AK_SCHEMA.keywords_study, name="keywords_study", curie=AK_SCHEMA.curie('keywords_study'),
                   model_uri=AK_SCHEMA.keywords_study, domain=None, range=Optional[Union[Union[str, "KeywordsStudy"], List[Union[str, "KeywordsStudy"]]]])

slots.adc_publish_date = Slot(uri=AK_SCHEMA.adc_publish_date, name="adc_publish_date", curie=AK_SCHEMA.curie('adc_publish_date'),
                   model_uri=AK_SCHEMA.adc_publish_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.adc_update_date = Slot(uri=AK_SCHEMA.adc_update_date, name="adc_update_date", curie=AK_SCHEMA.curie('adc_update_date'),
                   model_uri=AK_SCHEMA.adc_update_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.subject_id = Slot(uri=AK_SCHEMA.subject_id, name="subject_id", curie=AK_SCHEMA.curie('subject_id'),
                   model_uri=AK_SCHEMA.subject_id, domain=None, range=Optional[str])

slots.synthetic = Slot(uri=AK_SCHEMA.synthetic, name="synthetic", curie=AK_SCHEMA.curie('synthetic'),
                   model_uri=AK_SCHEMA.synthetic, domain=None, range=Optional[Union[bool, Bool]])

slots.sex = Slot(uri=AK_SCHEMA.sex, name="sex", curie=AK_SCHEMA.curie('sex'),
                   model_uri=AK_SCHEMA.sex, domain=None, range=Optional[Union[str, "Sex"]])

slots.age_min = Slot(uri=AK_SCHEMA.age_min, name="age_min", curie=AK_SCHEMA.curie('age_min'),
                   model_uri=AK_SCHEMA.age_min, domain=None, range=Optional[float])

slots.age_max = Slot(uri=AK_SCHEMA.age_max, name="age_max", curie=AK_SCHEMA.curie('age_max'),
                   model_uri=AK_SCHEMA.age_max, domain=None, range=Optional[float])

slots.age_unit = Slot(uri=AK_SCHEMA.age_unit, name="age_unit", curie=AK_SCHEMA.curie('age_unit'),
                   model_uri=AK_SCHEMA.age_unit, domain=None, range=Optional[Union[str, "AgeUnit"]])

slots.ancestry_population = Slot(uri=AK_SCHEMA.ancestry_population, name="ancestry_population", curie=AK_SCHEMA.curie('ancestry_population'),
                   model_uri=AK_SCHEMA.ancestry_population, domain=None, range=Optional[str])

slots.strain_name = Slot(uri=AK_SCHEMA.strain_name, name="strain_name", curie=AK_SCHEMA.curie('strain_name'),
                   model_uri=AK_SCHEMA.strain_name, domain=None, range=Optional[str])

slots.linked_subjects = Slot(uri=AK_SCHEMA.linked_subjects, name="linked_subjects", curie=AK_SCHEMA.curie('linked_subjects'),
                   model_uri=AK_SCHEMA.linked_subjects, domain=None, range=Optional[str])

slots.link_type = Slot(uri=RDF.type, name="link_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.link_type, domain=None, range=Optional[str])

slots.diagnosis = Slot(uri=AK_SCHEMA.diagnosis, name="diagnosis", curie=AK_SCHEMA.curie('diagnosis'),
                   model_uri=AK_SCHEMA.diagnosis, domain=None, range=Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]])

slots.genotype = Slot(uri=AK_SCHEMA.genotype, name="genotype", curie=AK_SCHEMA.curie('genotype'),
                   model_uri=AK_SCHEMA.genotype, domain=None, range=Optional[Union[dict, SubjectGenotype]])

slots.study_group_description = Slot(uri=AK_SCHEMA.study_group_description, name="study_group_description", curie=AK_SCHEMA.curie('study_group_description'),
                   model_uri=AK_SCHEMA.study_group_description, domain=None, range=Optional[str])

slots.disease_diagnosis = Slot(uri=AK_SCHEMA.disease_diagnosis, name="disease_diagnosis", curie=AK_SCHEMA.curie('disease_diagnosis'),
                   model_uri=AK_SCHEMA.disease_diagnosis, domain=None, range=Optional[Union[str, "DiseaseDiagnosis"]])

slots.disease_length = Slot(uri=AK_SCHEMA.disease_length, name="disease_length", curie=AK_SCHEMA.curie('disease_length'),
                   model_uri=AK_SCHEMA.disease_length, domain=None, range=Optional[str])

slots.prior_therapies = Slot(uri=AK_SCHEMA.prior_therapies, name="prior_therapies", curie=AK_SCHEMA.curie('prior_therapies'),
                   model_uri=AK_SCHEMA.prior_therapies, domain=None, range=Optional[str])

slots.immunogen = Slot(uri=AK_SCHEMA.immunogen, name="immunogen", curie=AK_SCHEMA.curie('immunogen'),
                   model_uri=AK_SCHEMA.immunogen, domain=None, range=Optional[str])

slots.intervention = Slot(uri=AK_SCHEMA.intervention, name="intervention", curie=AK_SCHEMA.curie('intervention'),
                   model_uri=AK_SCHEMA.intervention, domain=None, range=Optional[str])

slots.medical_history = Slot(uri=AK_SCHEMA.medical_history, name="medical_history", curie=AK_SCHEMA.curie('medical_history'),
                   model_uri=AK_SCHEMA.medical_history, domain=None, range=Optional[str])

slots.sample_id = Slot(uri=AK_SCHEMA.sample_id, name="sample_id", curie=AK_SCHEMA.curie('sample_id'),
                   model_uri=AK_SCHEMA.sample_id, domain=None, range=Optional[str])

slots.sample_type = Slot(uri=RDF.type, name="sample_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.sample_type, domain=None, range=Optional[str])

slots.tissue = Slot(uri=AK_SCHEMA.tissue, name="tissue", curie=AK_SCHEMA.curie('tissue'),
                   model_uri=AK_SCHEMA.tissue, domain=None, range=Optional[Union[str, "Tissue"]])

slots.anatomic_site = Slot(uri=AK_SCHEMA.anatomic_site, name="anatomic_site", curie=AK_SCHEMA.curie('anatomic_site'),
                   model_uri=AK_SCHEMA.anatomic_site, domain=None, range=Optional[str])

slots.disease_state_sample = Slot(uri=AK_SCHEMA.disease_state_sample, name="disease_state_sample", curie=AK_SCHEMA.curie('disease_state_sample'),
                   model_uri=AK_SCHEMA.disease_state_sample, domain=None, range=Optional[str])

slots.collection_time_point_relative = Slot(uri=AK_SCHEMA.collection_time_point_relative, name="collection_time_point_relative", curie=AK_SCHEMA.curie('collection_time_point_relative'),
                   model_uri=AK_SCHEMA.collection_time_point_relative, domain=None, range=Optional[float])

slots.collection_time_point_relative_unit = Slot(uri=AK_SCHEMA.collection_time_point_relative_unit, name="collection_time_point_relative_unit", curie=AK_SCHEMA.curie('collection_time_point_relative_unit'),
                   model_uri=AK_SCHEMA.collection_time_point_relative_unit, domain=None, range=Optional[Union[str, "CollectionTimePointRelativeUnit"]])

slots.collection_time_point_reference = Slot(uri=AK_SCHEMA.collection_time_point_reference, name="collection_time_point_reference", curie=AK_SCHEMA.curie('collection_time_point_reference'),
                   model_uri=AK_SCHEMA.collection_time_point_reference, domain=None, range=Optional[str])

slots.biomaterial_provider = Slot(uri=AK_SCHEMA.biomaterial_provider, name="biomaterial_provider", curie=AK_SCHEMA.curie('biomaterial_provider'),
                   model_uri=AK_SCHEMA.biomaterial_provider, domain=None, range=Optional[str])

slots.tissue_processing = Slot(uri=AK_SCHEMA.tissue_processing, name="tissue_processing", curie=AK_SCHEMA.curie('tissue_processing'),
                   model_uri=AK_SCHEMA.tissue_processing, domain=None, range=Optional[str])

slots.cell_subset = Slot(uri=AK_SCHEMA.cell_subset, name="cell_subset", curie=AK_SCHEMA.curie('cell_subset'),
                   model_uri=AK_SCHEMA.cell_subset, domain=None, range=Optional[Union[str, "CellSubset"]])

slots.cell_phenotype = Slot(uri=AK_SCHEMA.cell_phenotype, name="cell_phenotype", curie=AK_SCHEMA.curie('cell_phenotype'),
                   model_uri=AK_SCHEMA.cell_phenotype, domain=None, range=Optional[str])

slots.cell_species = Slot(uri=AK_SCHEMA.cell_species, name="cell_species", curie=AK_SCHEMA.curie('cell_species'),
                   model_uri=AK_SCHEMA.cell_species, domain=None, range=Optional[Union[str, "CellSpecies"]])

slots.single_cell = Slot(uri=AK_SCHEMA.single_cell, name="single_cell", curie=AK_SCHEMA.curie('single_cell'),
                   model_uri=AK_SCHEMA.single_cell, domain=None, range=Optional[Union[bool, Bool]])

slots.cell_number = Slot(uri=AK_SCHEMA.cell_number, name="cell_number", curie=AK_SCHEMA.curie('cell_number'),
                   model_uri=AK_SCHEMA.cell_number, domain=None, range=Optional[int])

slots.cells_per_reaction = Slot(uri=AK_SCHEMA.cells_per_reaction, name="cells_per_reaction", curie=AK_SCHEMA.curie('cells_per_reaction'),
                   model_uri=AK_SCHEMA.cells_per_reaction, domain=None, range=Optional[int])

slots.cell_storage = Slot(uri=AK_SCHEMA.cell_storage, name="cell_storage", curie=AK_SCHEMA.curie('cell_storage'),
                   model_uri=AK_SCHEMA.cell_storage, domain=None, range=Optional[Union[bool, Bool]])

slots.cell_quality = Slot(uri=AK_SCHEMA.cell_quality, name="cell_quality", curie=AK_SCHEMA.curie('cell_quality'),
                   model_uri=AK_SCHEMA.cell_quality, domain=None, range=Optional[str])

slots.cell_isolation = Slot(uri=AK_SCHEMA.cell_isolation, name="cell_isolation", curie=AK_SCHEMA.curie('cell_isolation'),
                   model_uri=AK_SCHEMA.cell_isolation, domain=None, range=Optional[str])

slots.cell_processing_protocol = Slot(uri=AK_SCHEMA.cell_processing_protocol, name="cell_processing_protocol", curie=AK_SCHEMA.curie('cell_processing_protocol'),
                   model_uri=AK_SCHEMA.cell_processing_protocol, domain=None, range=Optional[str])

slots.pcr_target_locus = Slot(uri=AK_SCHEMA.pcr_target_locus, name="pcr_target_locus", curie=AK_SCHEMA.curie('pcr_target_locus'),
                   model_uri=AK_SCHEMA.pcr_target_locus, domain=None, range=Optional[Union[str, "PcrTargetLocus"]])

slots.forward_pcr_primer_target_location = Slot(uri=AK_SCHEMA.forward_pcr_primer_target_location, name="forward_pcr_primer_target_location", curie=AK_SCHEMA.curie('forward_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.forward_pcr_primer_target_location, domain=None, range=Optional[str])

slots.reverse_pcr_primer_target_location = Slot(uri=AK_SCHEMA.reverse_pcr_primer_target_location, name="reverse_pcr_primer_target_location", curie=AK_SCHEMA.curie('reverse_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.reverse_pcr_primer_target_location, domain=None, range=Optional[str])

slots.template_class = Slot(uri=AK_SCHEMA.template_class, name="template_class", curie=AK_SCHEMA.curie('template_class'),
                   model_uri=AK_SCHEMA.template_class, domain=None, range=Optional[Union[str, "TemplateClass"]])

slots.template_quality = Slot(uri=AK_SCHEMA.template_quality, name="template_quality", curie=AK_SCHEMA.curie('template_quality'),
                   model_uri=AK_SCHEMA.template_quality, domain=None, range=Optional[str])

slots.template_amount = Slot(uri=AK_SCHEMA.template_amount, name="template_amount", curie=AK_SCHEMA.curie('template_amount'),
                   model_uri=AK_SCHEMA.template_amount, domain=None, range=Optional[float])

slots.template_amount_unit = Slot(uri=AK_SCHEMA.template_amount_unit, name="template_amount_unit", curie=AK_SCHEMA.curie('template_amount_unit'),
                   model_uri=AK_SCHEMA.template_amount_unit, domain=None, range=Optional[Union[str, "TemplateAmountUnit"]])

slots.library_generation_method = Slot(uri=AK_SCHEMA.library_generation_method, name="library_generation_method", curie=AK_SCHEMA.curie('library_generation_method'),
                   model_uri=AK_SCHEMA.library_generation_method, domain=None, range=Optional[Union[str, "LibraryGenerationMethod"]])

slots.library_generation_protocol = Slot(uri=AK_SCHEMA.library_generation_protocol, name="library_generation_protocol", curie=AK_SCHEMA.curie('library_generation_protocol'),
                   model_uri=AK_SCHEMA.library_generation_protocol, domain=None, range=Optional[str])

slots.library_generation_kit_version = Slot(uri=AK_SCHEMA.library_generation_kit_version, name="library_generation_kit_version", curie=AK_SCHEMA.curie('library_generation_kit_version'),
                   model_uri=AK_SCHEMA.library_generation_kit_version, domain=None, range=Optional[str])

slots.pcr_target = Slot(uri=AK_SCHEMA.pcr_target, name="pcr_target", curie=AK_SCHEMA.curie('pcr_target'),
                   model_uri=AK_SCHEMA.pcr_target, domain=None, range=Optional[Union[Union[dict, PCRTarget], List[Union[dict, PCRTarget]]]])

slots.complete_sequences = Slot(uri=AK_SCHEMA.complete_sequences, name="complete_sequences", curie=AK_SCHEMA.curie('complete_sequences'),
                   model_uri=AK_SCHEMA.complete_sequences, domain=None, range=Optional[Union[str, "CompleteSequences"]])

slots.physical_linkage = Slot(uri=AK_SCHEMA.physical_linkage, name="physical_linkage", curie=AK_SCHEMA.curie('physical_linkage'),
                   model_uri=AK_SCHEMA.physical_linkage, domain=None, range=Optional[Union[str, "PhysicalLinkage"]])

slots.sequencing_run_id = Slot(uri=AK_SCHEMA.sequencing_run_id, name="sequencing_run_id", curie=AK_SCHEMA.curie('sequencing_run_id'),
                   model_uri=AK_SCHEMA.sequencing_run_id, domain=None, range=Optional[str])

slots.total_reads_passing_qc_filter = Slot(uri=AK_SCHEMA.total_reads_passing_qc_filter, name="total_reads_passing_qc_filter", curie=AK_SCHEMA.curie('total_reads_passing_qc_filter'),
                   model_uri=AK_SCHEMA.total_reads_passing_qc_filter, domain=None, range=Optional[int])

slots.sequencing_platform = Slot(uri=AK_SCHEMA.sequencing_platform, name="sequencing_platform", curie=AK_SCHEMA.curie('sequencing_platform'),
                   model_uri=AK_SCHEMA.sequencing_platform, domain=None, range=Optional[str])

slots.sequencing_facility = Slot(uri=AK_SCHEMA.sequencing_facility, name="sequencing_facility", curie=AK_SCHEMA.curie('sequencing_facility'),
                   model_uri=AK_SCHEMA.sequencing_facility, domain=None, range=Optional[str])

slots.sequencing_run_date = Slot(uri=AK_SCHEMA.sequencing_run_date, name="sequencing_run_date", curie=AK_SCHEMA.curie('sequencing_run_date'),
                   model_uri=AK_SCHEMA.sequencing_run_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.sequencing_kit = Slot(uri=AK_SCHEMA.sequencing_kit, name="sequencing_kit", curie=AK_SCHEMA.curie('sequencing_kit'),
                   model_uri=AK_SCHEMA.sequencing_kit, domain=None, range=Optional[str])

slots.sequencing_files = Slot(uri=AK_SCHEMA.sequencing_files, name="sequencing_files", curie=AK_SCHEMA.curie('sequencing_files'),
                   model_uri=AK_SCHEMA.sequencing_files, domain=None, range=Optional[Union[dict, SequencingData]])

slots.sequencing_data_id = Slot(uri=AK_SCHEMA.sequencing_data_id, name="sequencing_data_id", curie=AK_SCHEMA.curie('sequencing_data_id'),
                   model_uri=AK_SCHEMA.sequencing_data_id, domain=None, range=Optional[str])

slots.file_type = Slot(uri=RDF.type, name="file_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.file_type, domain=None, range=Optional[Union[str, "FileType"]])

slots.filename = Slot(uri=AK_SCHEMA.filename, name="filename", curie=AK_SCHEMA.curie('filename'),
                   model_uri=AK_SCHEMA.filename, domain=None, range=Optional[str])

slots.read_direction = Slot(uri=AK_SCHEMA.read_direction, name="read_direction", curie=AK_SCHEMA.curie('read_direction'),
                   model_uri=AK_SCHEMA.read_direction, domain=None, range=Optional[Union[str, "ReadDirection"]])

slots.read_length = Slot(uri=AK_SCHEMA.read_length, name="read_length", curie=AK_SCHEMA.curie('read_length'),
                   model_uri=AK_SCHEMA.read_length, domain=None, range=Optional[int])

slots.paired_filename = Slot(uri=AK_SCHEMA.paired_filename, name="paired_filename", curie=AK_SCHEMA.curie('paired_filename'),
                   model_uri=AK_SCHEMA.paired_filename, domain=None, range=Optional[str])

slots.paired_read_direction = Slot(uri=AK_SCHEMA.paired_read_direction, name="paired_read_direction", curie=AK_SCHEMA.curie('paired_read_direction'),
                   model_uri=AK_SCHEMA.paired_read_direction, domain=None, range=Optional[Union[str, "PairedReadDirection"]])

slots.paired_read_length = Slot(uri=AK_SCHEMA.paired_read_length, name="paired_read_length", curie=AK_SCHEMA.curie('paired_read_length'),
                   model_uri=AK_SCHEMA.paired_read_length, domain=None, range=Optional[int])

slots.index_filename = Slot(uri=AK_SCHEMA.index_filename, name="index_filename", curie=AK_SCHEMA.curie('index_filename'),
                   model_uri=AK_SCHEMA.index_filename, domain=None, range=Optional[str])

slots.index_length = Slot(uri=AK_SCHEMA.index_length, name="index_length", curie=AK_SCHEMA.curie('index_length'),
                   model_uri=AK_SCHEMA.index_length, domain=None, range=Optional[int])

slots.data_processing_id = Slot(uri=AK_SCHEMA.data_processing_id, name="data_processing_id", curie=AK_SCHEMA.curie('data_processing_id'),
                   model_uri=AK_SCHEMA.data_processing_id, domain=None, range=Optional[str])

slots.primary_annotation = Slot(uri=AK_SCHEMA.primary_annotation, name="primary_annotation", curie=AK_SCHEMA.curie('primary_annotation'),
                   model_uri=AK_SCHEMA.primary_annotation, domain=None, range=Optional[Union[bool, Bool]])

slots.software_versions = Slot(uri=AK_SCHEMA.software_versions, name="software_versions", curie=AK_SCHEMA.curie('software_versions'),
                   model_uri=AK_SCHEMA.software_versions, domain=None, range=Optional[str])

slots.paired_reads_assembly = Slot(uri=AK_SCHEMA.paired_reads_assembly, name="paired_reads_assembly", curie=AK_SCHEMA.curie('paired_reads_assembly'),
                   model_uri=AK_SCHEMA.paired_reads_assembly, domain=None, range=Optional[str])

slots.quality_thresholds = Slot(uri=AK_SCHEMA.quality_thresholds, name="quality_thresholds", curie=AK_SCHEMA.curie('quality_thresholds'),
                   model_uri=AK_SCHEMA.quality_thresholds, domain=None, range=Optional[str])

slots.primer_match_cutoffs = Slot(uri=AK_SCHEMA.primer_match_cutoffs, name="primer_match_cutoffs", curie=AK_SCHEMA.curie('primer_match_cutoffs'),
                   model_uri=AK_SCHEMA.primer_match_cutoffs, domain=None, range=Optional[str])

slots.collapsing_method = Slot(uri=AK_SCHEMA.collapsing_method, name="collapsing_method", curie=AK_SCHEMA.curie('collapsing_method'),
                   model_uri=AK_SCHEMA.collapsing_method, domain=None, range=Optional[str])

slots.data_processing_protocols = Slot(uri=AK_SCHEMA.data_processing_protocols, name="data_processing_protocols", curie=AK_SCHEMA.curie('data_processing_protocols'),
                   model_uri=AK_SCHEMA.data_processing_protocols, domain=None, range=Optional[str])

slots.data_processing_files = Slot(uri=AK_SCHEMA.data_processing_files, name="data_processing_files", curie=AK_SCHEMA.curie('data_processing_files'),
                   model_uri=AK_SCHEMA.data_processing_files, domain=None, range=Optional[Union[str, List[str]]])

slots.germline_database = Slot(uri=AK_SCHEMA.germline_database, name="germline_database", curie=AK_SCHEMA.curie('germline_database'),
                   model_uri=AK_SCHEMA.germline_database, domain=None, range=Optional[str])

slots.analysis_provenance_id = Slot(uri=AK_SCHEMA.analysis_provenance_id, name="analysis_provenance_id", curie=AK_SCHEMA.curie('analysis_provenance_id'),
                   model_uri=AK_SCHEMA.analysis_provenance_id, domain=None, range=Optional[str])

slots.repertoire_id = Slot(uri=AK_SCHEMA.repertoire_id, name="repertoire_id", curie=AK_SCHEMA.curie('repertoire_id'),
                   model_uri=AK_SCHEMA.repertoire_id, domain=None, range=Optional[str])

slots.repertoire_name = Slot(uri=AK_SCHEMA.repertoire_name, name="repertoire_name", curie=AK_SCHEMA.curie('repertoire_name'),
                   model_uri=AK_SCHEMA.repertoire_name, domain=None, range=Optional[str])

slots.repertoire_description = Slot(uri=AK_SCHEMA.repertoire_description, name="repertoire_description", curie=AK_SCHEMA.curie('repertoire_description'),
                   model_uri=AK_SCHEMA.repertoire_description, domain=None, range=Optional[str])

slots.study = Slot(uri=AK_SCHEMA.study, name="study", curie=AK_SCHEMA.curie('study'),
                   model_uri=AK_SCHEMA.study, domain=None, range=Optional[Union[dict, Study]])

slots.subject = Slot(uri=AK_SCHEMA.subject, name="subject", curie=AK_SCHEMA.curie('subject'),
                   model_uri=AK_SCHEMA.subject, domain=None, range=Optional[Union[dict, Subject]])

slots.sample = Slot(uri=AK_SCHEMA.sample, name="sample", curie=AK_SCHEMA.curie('sample'),
                   model_uri=AK_SCHEMA.sample, domain=None, range=Optional[Union[Union[dict, SampleProcessing], List[Union[dict, SampleProcessing]]]])

slots.data_processing = Slot(uri=AK_SCHEMA.data_processing, name="data_processing", curie=AK_SCHEMA.curie('data_processing'),
                   model_uri=AK_SCHEMA.data_processing, domain=None, range=Optional[Union[Union[dict, DataProcessing], List[Union[dict, DataProcessing]]]])

slots.repertoire_group_id = Slot(uri=AK_SCHEMA.repertoire_group_id, name="repertoire_group_id", curie=AK_SCHEMA.curie('repertoire_group_id'),
                   model_uri=AK_SCHEMA.repertoire_group_id, domain=None, range=Optional[str])

slots.repertoire_group_name = Slot(uri=AK_SCHEMA.repertoire_group_name, name="repertoire_group_name", curie=AK_SCHEMA.curie('repertoire_group_name'),
                   model_uri=AK_SCHEMA.repertoire_group_name, domain=None, range=Optional[str])

slots.repertoire_group_description = Slot(uri=AK_SCHEMA.repertoire_group_description, name="repertoire_group_description", curie=AK_SCHEMA.curie('repertoire_group_description'),
                   model_uri=AK_SCHEMA.repertoire_group_description, domain=None, range=Optional[str])

slots.repertoires = Slot(uri=AK_SCHEMA.repertoires, name="repertoires", curie=AK_SCHEMA.curie('repertoires'),
                   model_uri=AK_SCHEMA.repertoires, domain=None, range=Optional[Union[str, List[str]]])

slots.segment = Slot(uri=AK_SCHEMA.segment, name="segment", curie=AK_SCHEMA.curie('segment'),
                   model_uri=AK_SCHEMA.segment, domain=None, range=Optional[str])

slots.rev_comp = Slot(uri=AK_SCHEMA.rev_comp, name="rev_comp", curie=AK_SCHEMA.curie('rev_comp'),
                   model_uri=AK_SCHEMA.rev_comp, domain=None, range=Optional[Union[bool, Bool]])

slots.call = Slot(uri=AK_SCHEMA.call, name="call", curie=AK_SCHEMA.curie('call'),
                   model_uri=AK_SCHEMA.call, domain=None, range=Optional[str])

slots.score = Slot(uri=AK_SCHEMA.score, name="score", curie=AK_SCHEMA.curie('score'),
                   model_uri=AK_SCHEMA.score, domain=None, range=Optional[float])

slots.identity = Slot(uri=AK_SCHEMA.identity, name="identity", curie=AK_SCHEMA.curie('identity'),
                   model_uri=AK_SCHEMA.identity, domain=None, range=Optional[float])

slots.support = Slot(uri=AK_SCHEMA.support, name="support", curie=AK_SCHEMA.curie('support'),
                   model_uri=AK_SCHEMA.support, domain=None, range=Optional[float])

slots.cigar = Slot(uri=AK_SCHEMA.cigar, name="cigar", curie=AK_SCHEMA.curie('cigar'),
                   model_uri=AK_SCHEMA.cigar, domain=None, range=Optional[str])

slots.germline_start = Slot(uri=AK_SCHEMA.germline_start, name="germline_start", curie=AK_SCHEMA.curie('germline_start'),
                   model_uri=AK_SCHEMA.germline_start, domain=None, range=Optional[int])

slots.germline_end = Slot(uri=AK_SCHEMA.germline_end, name="germline_end", curie=AK_SCHEMA.curie('germline_end'),
                   model_uri=AK_SCHEMA.germline_end, domain=None, range=Optional[int])

slots.rank = Slot(uri=AK_SCHEMA.rank, name="rank", curie=AK_SCHEMA.curie('rank'),
                   model_uri=AK_SCHEMA.rank, domain=None, range=Optional[int])

slots.quality = Slot(uri=AK_SCHEMA.quality, name="quality", curie=AK_SCHEMA.curie('quality'),
                   model_uri=AK_SCHEMA.quality, domain=None, range=Optional[str])

slots.sequence_aa = Slot(uri=AK_SCHEMA.sequence_aa, name="sequence_aa", curie=AK_SCHEMA.curie('sequence_aa'),
                   model_uri=AK_SCHEMA.sequence_aa, domain=None, range=Optional[str])

slots.productive = Slot(uri=AK_SCHEMA.productive, name="productive", curie=AK_SCHEMA.curie('productive'),
                   model_uri=AK_SCHEMA.productive, domain=None, range=Optional[Union[bool, Bool]])

slots.vj_in_frame = Slot(uri=AK_SCHEMA.vj_in_frame, name="vj_in_frame", curie=AK_SCHEMA.curie('vj_in_frame'),
                   model_uri=AK_SCHEMA.vj_in_frame, domain=None, range=Optional[Union[bool, Bool]])

slots.stop_codon = Slot(uri=AK_SCHEMA.stop_codon, name="stop_codon", curie=AK_SCHEMA.curie('stop_codon'),
                   model_uri=AK_SCHEMA.stop_codon, domain=None, range=Optional[Union[bool, Bool]])

slots.complete_vdj = Slot(uri=AK_SCHEMA.complete_vdj, name="complete_vdj", curie=AK_SCHEMA.curie('complete_vdj'),
                   model_uri=AK_SCHEMA.complete_vdj, domain=None, range=Optional[Union[bool, Bool]])

slots.v_call = Slot(uri=AK_SCHEMA.v_call, name="v_call", curie=AK_SCHEMA.curie('v_call'),
                   model_uri=AK_SCHEMA.v_call, domain=None, range=Optional[str])

slots.d_call = Slot(uri=AK_SCHEMA.d_call, name="d_call", curie=AK_SCHEMA.curie('d_call'),
                   model_uri=AK_SCHEMA.d_call, domain=None, range=Optional[str])

slots.d2_call = Slot(uri=AK_SCHEMA.d2_call, name="d2_call", curie=AK_SCHEMA.curie('d2_call'),
                   model_uri=AK_SCHEMA.d2_call, domain=None, range=Optional[str])

slots.j_call = Slot(uri=AK_SCHEMA.j_call, name="j_call", curie=AK_SCHEMA.curie('j_call'),
                   model_uri=AK_SCHEMA.j_call, domain=None, range=Optional[str])

slots.c_call = Slot(uri=AK_SCHEMA.c_call, name="c_call", curie=AK_SCHEMA.curie('c_call'),
                   model_uri=AK_SCHEMA.c_call, domain=None, range=Optional[str])

slots.sequence_alignment = Slot(uri=AK_SCHEMA.sequence_alignment, name="sequence_alignment", curie=AK_SCHEMA.curie('sequence_alignment'),
                   model_uri=AK_SCHEMA.sequence_alignment, domain=None, range=Optional[str])

slots.quality_alignment = Slot(uri=AK_SCHEMA.quality_alignment, name="quality_alignment", curie=AK_SCHEMA.curie('quality_alignment'),
                   model_uri=AK_SCHEMA.quality_alignment, domain=None, range=Optional[str])

slots.sequence_alignment_aa = Slot(uri=AK_SCHEMA.sequence_alignment_aa, name="sequence_alignment_aa", curie=AK_SCHEMA.curie('sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.sequence_alignment_aa, domain=None, range=Optional[str])

slots.germline_alignment = Slot(uri=AK_SCHEMA.germline_alignment, name="germline_alignment", curie=AK_SCHEMA.curie('germline_alignment'),
                   model_uri=AK_SCHEMA.germline_alignment, domain=None, range=Optional[str])

slots.germline_alignment_aa = Slot(uri=AK_SCHEMA.germline_alignment_aa, name="germline_alignment_aa", curie=AK_SCHEMA.curie('germline_alignment_aa'),
                   model_uri=AK_SCHEMA.germline_alignment_aa, domain=None, range=Optional[str])

slots.junction = Slot(uri=AK_SCHEMA.junction, name="junction", curie=AK_SCHEMA.curie('junction'),
                   model_uri=AK_SCHEMA.junction, domain=None, range=Optional[str])

slots.junction_aa = Slot(uri=AK_SCHEMA.junction_aa, name="junction_aa", curie=AK_SCHEMA.curie('junction_aa'),
                   model_uri=AK_SCHEMA.junction_aa, domain=None, range=Optional[str])

slots.np1 = Slot(uri=AK_SCHEMA.np1, name="np1", curie=AK_SCHEMA.curie('np1'),
                   model_uri=AK_SCHEMA.np1, domain=None, range=Optional[str])

slots.np1_aa = Slot(uri=AK_SCHEMA.np1_aa, name="np1_aa", curie=AK_SCHEMA.curie('np1_aa'),
                   model_uri=AK_SCHEMA.np1_aa, domain=None, range=Optional[str])

slots.np2 = Slot(uri=AK_SCHEMA.np2, name="np2", curie=AK_SCHEMA.curie('np2'),
                   model_uri=AK_SCHEMA.np2, domain=None, range=Optional[str])

slots.np2_aa = Slot(uri=AK_SCHEMA.np2_aa, name="np2_aa", curie=AK_SCHEMA.curie('np2_aa'),
                   model_uri=AK_SCHEMA.np2_aa, domain=None, range=Optional[str])

slots.np3 = Slot(uri=AK_SCHEMA.np3, name="np3", curie=AK_SCHEMA.curie('np3'),
                   model_uri=AK_SCHEMA.np3, domain=None, range=Optional[str])

slots.np3_aa = Slot(uri=AK_SCHEMA.np3_aa, name="np3_aa", curie=AK_SCHEMA.curie('np3_aa'),
                   model_uri=AK_SCHEMA.np3_aa, domain=None, range=Optional[str])

slots.cdr1 = Slot(uri=AK_SCHEMA.cdr1, name="cdr1", curie=AK_SCHEMA.curie('cdr1'),
                   model_uri=AK_SCHEMA.cdr1, domain=None, range=Optional[str])

slots.cdr1_aa = Slot(uri=AK_SCHEMA.cdr1_aa, name="cdr1_aa", curie=AK_SCHEMA.curie('cdr1_aa'),
                   model_uri=AK_SCHEMA.cdr1_aa, domain=None, range=Optional[str])

slots.cdr2 = Slot(uri=AK_SCHEMA.cdr2, name="cdr2", curie=AK_SCHEMA.curie('cdr2'),
                   model_uri=AK_SCHEMA.cdr2, domain=None, range=Optional[str])

slots.cdr2_aa = Slot(uri=AK_SCHEMA.cdr2_aa, name="cdr2_aa", curie=AK_SCHEMA.curie('cdr2_aa'),
                   model_uri=AK_SCHEMA.cdr2_aa, domain=None, range=Optional[str])

slots.cdr3 = Slot(uri=AK_SCHEMA.cdr3, name="cdr3", curie=AK_SCHEMA.curie('cdr3'),
                   model_uri=AK_SCHEMA.cdr3, domain=None, range=Optional[str])

slots.cdr3_aa = Slot(uri=AK_SCHEMA.cdr3_aa, name="cdr3_aa", curie=AK_SCHEMA.curie('cdr3_aa'),
                   model_uri=AK_SCHEMA.cdr3_aa, domain=None, range=Optional[str])

slots.fwr1 = Slot(uri=AK_SCHEMA.fwr1, name="fwr1", curie=AK_SCHEMA.curie('fwr1'),
                   model_uri=AK_SCHEMA.fwr1, domain=None, range=Optional[str])

slots.fwr1_aa = Slot(uri=AK_SCHEMA.fwr1_aa, name="fwr1_aa", curie=AK_SCHEMA.curie('fwr1_aa'),
                   model_uri=AK_SCHEMA.fwr1_aa, domain=None, range=Optional[str])

slots.fwr2 = Slot(uri=AK_SCHEMA.fwr2, name="fwr2", curie=AK_SCHEMA.curie('fwr2'),
                   model_uri=AK_SCHEMA.fwr2, domain=None, range=Optional[str])

slots.fwr2_aa = Slot(uri=AK_SCHEMA.fwr2_aa, name="fwr2_aa", curie=AK_SCHEMA.curie('fwr2_aa'),
                   model_uri=AK_SCHEMA.fwr2_aa, domain=None, range=Optional[str])

slots.fwr3 = Slot(uri=AK_SCHEMA.fwr3, name="fwr3", curie=AK_SCHEMA.curie('fwr3'),
                   model_uri=AK_SCHEMA.fwr3, domain=None, range=Optional[str])

slots.fwr3_aa = Slot(uri=AK_SCHEMA.fwr3_aa, name="fwr3_aa", curie=AK_SCHEMA.curie('fwr3_aa'),
                   model_uri=AK_SCHEMA.fwr3_aa, domain=None, range=Optional[str])

slots.fwr4 = Slot(uri=AK_SCHEMA.fwr4, name="fwr4", curie=AK_SCHEMA.curie('fwr4'),
                   model_uri=AK_SCHEMA.fwr4, domain=None, range=Optional[str])

slots.fwr4_aa = Slot(uri=AK_SCHEMA.fwr4_aa, name="fwr4_aa", curie=AK_SCHEMA.curie('fwr4_aa'),
                   model_uri=AK_SCHEMA.fwr4_aa, domain=None, range=Optional[str])

slots.v_score = Slot(uri=AK_SCHEMA.v_score, name="v_score", curie=AK_SCHEMA.curie('v_score'),
                   model_uri=AK_SCHEMA.v_score, domain=None, range=Optional[float])

slots.v_identity = Slot(uri=AK_SCHEMA.v_identity, name="v_identity", curie=AK_SCHEMA.curie('v_identity'),
                   model_uri=AK_SCHEMA.v_identity, domain=None, range=Optional[float])

slots.v_support = Slot(uri=AK_SCHEMA.v_support, name="v_support", curie=AK_SCHEMA.curie('v_support'),
                   model_uri=AK_SCHEMA.v_support, domain=None, range=Optional[float])

slots.v_cigar = Slot(uri=AK_SCHEMA.v_cigar, name="v_cigar", curie=AK_SCHEMA.curie('v_cigar'),
                   model_uri=AK_SCHEMA.v_cigar, domain=None, range=Optional[str])

slots.d_score = Slot(uri=AK_SCHEMA.d_score, name="d_score", curie=AK_SCHEMA.curie('d_score'),
                   model_uri=AK_SCHEMA.d_score, domain=None, range=Optional[float])

slots.d_identity = Slot(uri=AK_SCHEMA.d_identity, name="d_identity", curie=AK_SCHEMA.curie('d_identity'),
                   model_uri=AK_SCHEMA.d_identity, domain=None, range=Optional[float])

slots.d_support = Slot(uri=AK_SCHEMA.d_support, name="d_support", curie=AK_SCHEMA.curie('d_support'),
                   model_uri=AK_SCHEMA.d_support, domain=None, range=Optional[float])

slots.d_cigar = Slot(uri=AK_SCHEMA.d_cigar, name="d_cigar", curie=AK_SCHEMA.curie('d_cigar'),
                   model_uri=AK_SCHEMA.d_cigar, domain=None, range=Optional[str])

slots.d2_score = Slot(uri=AK_SCHEMA.d2_score, name="d2_score", curie=AK_SCHEMA.curie('d2_score'),
                   model_uri=AK_SCHEMA.d2_score, domain=None, range=Optional[float])

slots.d2_identity = Slot(uri=AK_SCHEMA.d2_identity, name="d2_identity", curie=AK_SCHEMA.curie('d2_identity'),
                   model_uri=AK_SCHEMA.d2_identity, domain=None, range=Optional[float])

slots.d2_support = Slot(uri=AK_SCHEMA.d2_support, name="d2_support", curie=AK_SCHEMA.curie('d2_support'),
                   model_uri=AK_SCHEMA.d2_support, domain=None, range=Optional[float])

slots.d2_cigar = Slot(uri=AK_SCHEMA.d2_cigar, name="d2_cigar", curie=AK_SCHEMA.curie('d2_cigar'),
                   model_uri=AK_SCHEMA.d2_cigar, domain=None, range=Optional[str])

slots.j_score = Slot(uri=AK_SCHEMA.j_score, name="j_score", curie=AK_SCHEMA.curie('j_score'),
                   model_uri=AK_SCHEMA.j_score, domain=None, range=Optional[float])

slots.j_identity = Slot(uri=AK_SCHEMA.j_identity, name="j_identity", curie=AK_SCHEMA.curie('j_identity'),
                   model_uri=AK_SCHEMA.j_identity, domain=None, range=Optional[float])

slots.j_support = Slot(uri=AK_SCHEMA.j_support, name="j_support", curie=AK_SCHEMA.curie('j_support'),
                   model_uri=AK_SCHEMA.j_support, domain=None, range=Optional[float])

slots.j_cigar = Slot(uri=AK_SCHEMA.j_cigar, name="j_cigar", curie=AK_SCHEMA.curie('j_cigar'),
                   model_uri=AK_SCHEMA.j_cigar, domain=None, range=Optional[str])

slots.c_score = Slot(uri=AK_SCHEMA.c_score, name="c_score", curie=AK_SCHEMA.curie('c_score'),
                   model_uri=AK_SCHEMA.c_score, domain=None, range=Optional[float])

slots.c_identity = Slot(uri=AK_SCHEMA.c_identity, name="c_identity", curie=AK_SCHEMA.curie('c_identity'),
                   model_uri=AK_SCHEMA.c_identity, domain=None, range=Optional[float])

slots.c_support = Slot(uri=AK_SCHEMA.c_support, name="c_support", curie=AK_SCHEMA.curie('c_support'),
                   model_uri=AK_SCHEMA.c_support, domain=None, range=Optional[float])

slots.c_cigar = Slot(uri=AK_SCHEMA.c_cigar, name="c_cigar", curie=AK_SCHEMA.curie('c_cigar'),
                   model_uri=AK_SCHEMA.c_cigar, domain=None, range=Optional[str])

slots.v_sequence_start = Slot(uri=AK_SCHEMA.v_sequence_start, name="v_sequence_start", curie=AK_SCHEMA.curie('v_sequence_start'),
                   model_uri=AK_SCHEMA.v_sequence_start, domain=None, range=Optional[int])

slots.v_sequence_end = Slot(uri=AK_SCHEMA.v_sequence_end, name="v_sequence_end", curie=AK_SCHEMA.curie('v_sequence_end'),
                   model_uri=AK_SCHEMA.v_sequence_end, domain=None, range=Optional[int])

slots.v_germline_start = Slot(uri=AK_SCHEMA.v_germline_start, name="v_germline_start", curie=AK_SCHEMA.curie('v_germline_start'),
                   model_uri=AK_SCHEMA.v_germline_start, domain=None, range=Optional[int])

slots.v_germline_end = Slot(uri=AK_SCHEMA.v_germline_end, name="v_germline_end", curie=AK_SCHEMA.curie('v_germline_end'),
                   model_uri=AK_SCHEMA.v_germline_end, domain=None, range=Optional[int])

slots.v_alignment_start = Slot(uri=AK_SCHEMA.v_alignment_start, name="v_alignment_start", curie=AK_SCHEMA.curie('v_alignment_start'),
                   model_uri=AK_SCHEMA.v_alignment_start, domain=None, range=Optional[int])

slots.v_alignment_end = Slot(uri=AK_SCHEMA.v_alignment_end, name="v_alignment_end", curie=AK_SCHEMA.curie('v_alignment_end'),
                   model_uri=AK_SCHEMA.v_alignment_end, domain=None, range=Optional[int])

slots.d_sequence_start = Slot(uri=AK_SCHEMA.d_sequence_start, name="d_sequence_start", curie=AK_SCHEMA.curie('d_sequence_start'),
                   model_uri=AK_SCHEMA.d_sequence_start, domain=None, range=Optional[int])

slots.d_sequence_end = Slot(uri=AK_SCHEMA.d_sequence_end, name="d_sequence_end", curie=AK_SCHEMA.curie('d_sequence_end'),
                   model_uri=AK_SCHEMA.d_sequence_end, domain=None, range=Optional[int])

slots.d_germline_start = Slot(uri=AK_SCHEMA.d_germline_start, name="d_germline_start", curie=AK_SCHEMA.curie('d_germline_start'),
                   model_uri=AK_SCHEMA.d_germline_start, domain=None, range=Optional[int])

slots.d_germline_end = Slot(uri=AK_SCHEMA.d_germline_end, name="d_germline_end", curie=AK_SCHEMA.curie('d_germline_end'),
                   model_uri=AK_SCHEMA.d_germline_end, domain=None, range=Optional[int])

slots.d_alignment_start = Slot(uri=AK_SCHEMA.d_alignment_start, name="d_alignment_start", curie=AK_SCHEMA.curie('d_alignment_start'),
                   model_uri=AK_SCHEMA.d_alignment_start, domain=None, range=Optional[int])

slots.d_alignment_end = Slot(uri=AK_SCHEMA.d_alignment_end, name="d_alignment_end", curie=AK_SCHEMA.curie('d_alignment_end'),
                   model_uri=AK_SCHEMA.d_alignment_end, domain=None, range=Optional[int])

slots.d2_sequence_start = Slot(uri=AK_SCHEMA.d2_sequence_start, name="d2_sequence_start", curie=AK_SCHEMA.curie('d2_sequence_start'),
                   model_uri=AK_SCHEMA.d2_sequence_start, domain=None, range=Optional[int])

slots.d2_sequence_end = Slot(uri=AK_SCHEMA.d2_sequence_end, name="d2_sequence_end", curie=AK_SCHEMA.curie('d2_sequence_end'),
                   model_uri=AK_SCHEMA.d2_sequence_end, domain=None, range=Optional[int])

slots.d2_germline_start = Slot(uri=AK_SCHEMA.d2_germline_start, name="d2_germline_start", curie=AK_SCHEMA.curie('d2_germline_start'),
                   model_uri=AK_SCHEMA.d2_germline_start, domain=None, range=Optional[int])

slots.d2_germline_end = Slot(uri=AK_SCHEMA.d2_germline_end, name="d2_germline_end", curie=AK_SCHEMA.curie('d2_germline_end'),
                   model_uri=AK_SCHEMA.d2_germline_end, domain=None, range=Optional[int])

slots.d2_alignment_start = Slot(uri=AK_SCHEMA.d2_alignment_start, name="d2_alignment_start", curie=AK_SCHEMA.curie('d2_alignment_start'),
                   model_uri=AK_SCHEMA.d2_alignment_start, domain=None, range=Optional[int])

slots.d2_alignment_end = Slot(uri=AK_SCHEMA.d2_alignment_end, name="d2_alignment_end", curie=AK_SCHEMA.curie('d2_alignment_end'),
                   model_uri=AK_SCHEMA.d2_alignment_end, domain=None, range=Optional[int])

slots.j_sequence_start = Slot(uri=AK_SCHEMA.j_sequence_start, name="j_sequence_start", curie=AK_SCHEMA.curie('j_sequence_start'),
                   model_uri=AK_SCHEMA.j_sequence_start, domain=None, range=Optional[int])

slots.j_sequence_end = Slot(uri=AK_SCHEMA.j_sequence_end, name="j_sequence_end", curie=AK_SCHEMA.curie('j_sequence_end'),
                   model_uri=AK_SCHEMA.j_sequence_end, domain=None, range=Optional[int])

slots.j_germline_start = Slot(uri=AK_SCHEMA.j_germline_start, name="j_germline_start", curie=AK_SCHEMA.curie('j_germline_start'),
                   model_uri=AK_SCHEMA.j_germline_start, domain=None, range=Optional[int])

slots.j_germline_end = Slot(uri=AK_SCHEMA.j_germline_end, name="j_germline_end", curie=AK_SCHEMA.curie('j_germline_end'),
                   model_uri=AK_SCHEMA.j_germline_end, domain=None, range=Optional[int])

slots.j_alignment_start = Slot(uri=AK_SCHEMA.j_alignment_start, name="j_alignment_start", curie=AK_SCHEMA.curie('j_alignment_start'),
                   model_uri=AK_SCHEMA.j_alignment_start, domain=None, range=Optional[int])

slots.j_alignment_end = Slot(uri=AK_SCHEMA.j_alignment_end, name="j_alignment_end", curie=AK_SCHEMA.curie('j_alignment_end'),
                   model_uri=AK_SCHEMA.j_alignment_end, domain=None, range=Optional[int])

slots.c_sequence_start = Slot(uri=AK_SCHEMA.c_sequence_start, name="c_sequence_start", curie=AK_SCHEMA.curie('c_sequence_start'),
                   model_uri=AK_SCHEMA.c_sequence_start, domain=None, range=Optional[int])

slots.c_sequence_end = Slot(uri=AK_SCHEMA.c_sequence_end, name="c_sequence_end", curie=AK_SCHEMA.curie('c_sequence_end'),
                   model_uri=AK_SCHEMA.c_sequence_end, domain=None, range=Optional[int])

slots.c_germline_start = Slot(uri=AK_SCHEMA.c_germline_start, name="c_germline_start", curie=AK_SCHEMA.curie('c_germline_start'),
                   model_uri=AK_SCHEMA.c_germline_start, domain=None, range=Optional[int])

slots.c_germline_end = Slot(uri=AK_SCHEMA.c_germline_end, name="c_germline_end", curie=AK_SCHEMA.curie('c_germline_end'),
                   model_uri=AK_SCHEMA.c_germline_end, domain=None, range=Optional[int])

slots.c_alignment_start = Slot(uri=AK_SCHEMA.c_alignment_start, name="c_alignment_start", curie=AK_SCHEMA.curie('c_alignment_start'),
                   model_uri=AK_SCHEMA.c_alignment_start, domain=None, range=Optional[int])

slots.c_alignment_end = Slot(uri=AK_SCHEMA.c_alignment_end, name="c_alignment_end", curie=AK_SCHEMA.curie('c_alignment_end'),
                   model_uri=AK_SCHEMA.c_alignment_end, domain=None, range=Optional[int])

slots.cdr3_end = Slot(uri=AK_SCHEMA.cdr3_end, name="cdr3_end", curie=AK_SCHEMA.curie('cdr3_end'),
                   model_uri=AK_SCHEMA.cdr3_end, domain=None, range=Optional[int])

slots.fwr4_start = Slot(uri=AK_SCHEMA.fwr4_start, name="fwr4_start", curie=AK_SCHEMA.curie('fwr4_start'),
                   model_uri=AK_SCHEMA.fwr4_start, domain=None, range=Optional[int])

slots.fwr4_end = Slot(uri=AK_SCHEMA.fwr4_end, name="fwr4_end", curie=AK_SCHEMA.curie('fwr4_end'),
                   model_uri=AK_SCHEMA.fwr4_end, domain=None, range=Optional[int])

slots.v_sequence_alignment = Slot(uri=AK_SCHEMA.v_sequence_alignment, name="v_sequence_alignment", curie=AK_SCHEMA.curie('v_sequence_alignment'),
                   model_uri=AK_SCHEMA.v_sequence_alignment, domain=None, range=Optional[str])

slots.v_sequence_alignment_aa = Slot(uri=AK_SCHEMA.v_sequence_alignment_aa, name="v_sequence_alignment_aa", curie=AK_SCHEMA.curie('v_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.v_sequence_alignment_aa, domain=None, range=Optional[str])

slots.d_sequence_alignment = Slot(uri=AK_SCHEMA.d_sequence_alignment, name="d_sequence_alignment", curie=AK_SCHEMA.curie('d_sequence_alignment'),
                   model_uri=AK_SCHEMA.d_sequence_alignment, domain=None, range=Optional[str])

slots.d_sequence_alignment_aa = Slot(uri=AK_SCHEMA.d_sequence_alignment_aa, name="d_sequence_alignment_aa", curie=AK_SCHEMA.curie('d_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.d_sequence_alignment_aa, domain=None, range=Optional[str])

slots.d2_sequence_alignment = Slot(uri=AK_SCHEMA.d2_sequence_alignment, name="d2_sequence_alignment", curie=AK_SCHEMA.curie('d2_sequence_alignment'),
                   model_uri=AK_SCHEMA.d2_sequence_alignment, domain=None, range=Optional[str])

slots.d2_sequence_alignment_aa = Slot(uri=AK_SCHEMA.d2_sequence_alignment_aa, name="d2_sequence_alignment_aa", curie=AK_SCHEMA.curie('d2_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.d2_sequence_alignment_aa, domain=None, range=Optional[str])

slots.j_sequence_alignment = Slot(uri=AK_SCHEMA.j_sequence_alignment, name="j_sequence_alignment", curie=AK_SCHEMA.curie('j_sequence_alignment'),
                   model_uri=AK_SCHEMA.j_sequence_alignment, domain=None, range=Optional[str])

slots.j_sequence_alignment_aa = Slot(uri=AK_SCHEMA.j_sequence_alignment_aa, name="j_sequence_alignment_aa", curie=AK_SCHEMA.curie('j_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.j_sequence_alignment_aa, domain=None, range=Optional[str])

slots.c_sequence_alignment = Slot(uri=AK_SCHEMA.c_sequence_alignment, name="c_sequence_alignment", curie=AK_SCHEMA.curie('c_sequence_alignment'),
                   model_uri=AK_SCHEMA.c_sequence_alignment, domain=None, range=Optional[str])

slots.c_sequence_alignment_aa = Slot(uri=AK_SCHEMA.c_sequence_alignment_aa, name="c_sequence_alignment_aa", curie=AK_SCHEMA.curie('c_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.c_sequence_alignment_aa, domain=None, range=Optional[str])

slots.v_germline_alignment = Slot(uri=AK_SCHEMA.v_germline_alignment, name="v_germline_alignment", curie=AK_SCHEMA.curie('v_germline_alignment'),
                   model_uri=AK_SCHEMA.v_germline_alignment, domain=None, range=Optional[str])

slots.v_germline_alignment_aa = Slot(uri=AK_SCHEMA.v_germline_alignment_aa, name="v_germline_alignment_aa", curie=AK_SCHEMA.curie('v_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.v_germline_alignment_aa, domain=None, range=Optional[str])

slots.d_germline_alignment = Slot(uri=AK_SCHEMA.d_germline_alignment, name="d_germline_alignment", curie=AK_SCHEMA.curie('d_germline_alignment'),
                   model_uri=AK_SCHEMA.d_germline_alignment, domain=None, range=Optional[str])

slots.d_germline_alignment_aa = Slot(uri=AK_SCHEMA.d_germline_alignment_aa, name="d_germline_alignment_aa", curie=AK_SCHEMA.curie('d_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.d_germline_alignment_aa, domain=None, range=Optional[str])

slots.d2_germline_alignment = Slot(uri=AK_SCHEMA.d2_germline_alignment, name="d2_germline_alignment", curie=AK_SCHEMA.curie('d2_germline_alignment'),
                   model_uri=AK_SCHEMA.d2_germline_alignment, domain=None, range=Optional[str])

slots.d2_germline_alignment_aa = Slot(uri=AK_SCHEMA.d2_germline_alignment_aa, name="d2_germline_alignment_aa", curie=AK_SCHEMA.curie('d2_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.d2_germline_alignment_aa, domain=None, range=Optional[str])

slots.j_germline_alignment = Slot(uri=AK_SCHEMA.j_germline_alignment, name="j_germline_alignment", curie=AK_SCHEMA.curie('j_germline_alignment'),
                   model_uri=AK_SCHEMA.j_germline_alignment, domain=None, range=Optional[str])

slots.j_germline_alignment_aa = Slot(uri=AK_SCHEMA.j_germline_alignment_aa, name="j_germline_alignment_aa", curie=AK_SCHEMA.curie('j_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.j_germline_alignment_aa, domain=None, range=Optional[str])

slots.c_germline_alignment = Slot(uri=AK_SCHEMA.c_germline_alignment, name="c_germline_alignment", curie=AK_SCHEMA.curie('c_germline_alignment'),
                   model_uri=AK_SCHEMA.c_germline_alignment, domain=None, range=Optional[str])

slots.c_germline_alignment_aa = Slot(uri=AK_SCHEMA.c_germline_alignment_aa, name="c_germline_alignment_aa", curie=AK_SCHEMA.curie('c_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.c_germline_alignment_aa, domain=None, range=Optional[str])

slots.junction_length = Slot(uri=AK_SCHEMA.junction_length, name="junction_length", curie=AK_SCHEMA.curie('junction_length'),
                   model_uri=AK_SCHEMA.junction_length, domain=None, range=Optional[int])

slots.junction_aa_length = Slot(uri=AK_SCHEMA.junction_aa_length, name="junction_aa_length", curie=AK_SCHEMA.curie('junction_aa_length'),
                   model_uri=AK_SCHEMA.junction_aa_length, domain=None, range=Optional[int])

slots.np1_length = Slot(uri=AK_SCHEMA.np1_length, name="np1_length", curie=AK_SCHEMA.curie('np1_length'),
                   model_uri=AK_SCHEMA.np1_length, domain=None, range=Optional[int])

slots.np2_length = Slot(uri=AK_SCHEMA.np2_length, name="np2_length", curie=AK_SCHEMA.curie('np2_length'),
                   model_uri=AK_SCHEMA.np2_length, domain=None, range=Optional[int])

slots.np3_length = Slot(uri=AK_SCHEMA.np3_length, name="np3_length", curie=AK_SCHEMA.curie('np3_length'),
                   model_uri=AK_SCHEMA.np3_length, domain=None, range=Optional[int])

slots.n1_length = Slot(uri=AK_SCHEMA.n1_length, name="n1_length", curie=AK_SCHEMA.curie('n1_length'),
                   model_uri=AK_SCHEMA.n1_length, domain=None, range=Optional[int])

slots.n2_length = Slot(uri=AK_SCHEMA.n2_length, name="n2_length", curie=AK_SCHEMA.curie('n2_length'),
                   model_uri=AK_SCHEMA.n2_length, domain=None, range=Optional[int])

slots.n3_length = Slot(uri=AK_SCHEMA.n3_length, name="n3_length", curie=AK_SCHEMA.curie('n3_length'),
                   model_uri=AK_SCHEMA.n3_length, domain=None, range=Optional[int])

slots.p3v_length = Slot(uri=AK_SCHEMA.p3v_length, name="p3v_length", curie=AK_SCHEMA.curie('p3v_length'),
                   model_uri=AK_SCHEMA.p3v_length, domain=None, range=Optional[int])

slots.p5d_length = Slot(uri=AK_SCHEMA.p5d_length, name="p5d_length", curie=AK_SCHEMA.curie('p5d_length'),
                   model_uri=AK_SCHEMA.p5d_length, domain=None, range=Optional[int])

slots.p3d_length = Slot(uri=AK_SCHEMA.p3d_length, name="p3d_length", curie=AK_SCHEMA.curie('p3d_length'),
                   model_uri=AK_SCHEMA.p3d_length, domain=None, range=Optional[int])

slots.p5d2_length = Slot(uri=AK_SCHEMA.p5d2_length, name="p5d2_length", curie=AK_SCHEMA.curie('p5d2_length'),
                   model_uri=AK_SCHEMA.p5d2_length, domain=None, range=Optional[int])

slots.p3d2_length = Slot(uri=AK_SCHEMA.p3d2_length, name="p3d2_length", curie=AK_SCHEMA.curie('p3d2_length'),
                   model_uri=AK_SCHEMA.p3d2_length, domain=None, range=Optional[int])

slots.p5j_length = Slot(uri=AK_SCHEMA.p5j_length, name="p5j_length", curie=AK_SCHEMA.curie('p5j_length'),
                   model_uri=AK_SCHEMA.p5j_length, domain=None, range=Optional[int])

slots.v_frameshift = Slot(uri=AK_SCHEMA.v_frameshift, name="v_frameshift", curie=AK_SCHEMA.curie('v_frameshift'),
                   model_uri=AK_SCHEMA.v_frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.j_frameshift = Slot(uri=AK_SCHEMA.j_frameshift, name="j_frameshift", curie=AK_SCHEMA.curie('j_frameshift'),
                   model_uri=AK_SCHEMA.j_frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.d_frame = Slot(uri=AK_SCHEMA.d_frame, name="d_frame", curie=AK_SCHEMA.curie('d_frame'),
                   model_uri=AK_SCHEMA.d_frame, domain=None, range=Optional[int])

slots.d2_frame = Slot(uri=AK_SCHEMA.d2_frame, name="d2_frame", curie=AK_SCHEMA.curie('d2_frame'),
                   model_uri=AK_SCHEMA.d2_frame, domain=None, range=Optional[int])

slots.consensus_count = Slot(uri=AK_SCHEMA.consensus_count, name="consensus_count", curie=AK_SCHEMA.curie('consensus_count'),
                   model_uri=AK_SCHEMA.consensus_count, domain=None, range=Optional[int])

slots.duplicate_count = Slot(uri=AK_SCHEMA.duplicate_count, name="duplicate_count", curie=AK_SCHEMA.curie('duplicate_count'),
                   model_uri=AK_SCHEMA.duplicate_count, domain=None, range=Optional[int])

slots.umi_count = Slot(uri=AK_SCHEMA.umi_count, name="umi_count", curie=AK_SCHEMA.curie('umi_count'),
                   model_uri=AK_SCHEMA.umi_count, domain=None, range=Optional[int])

slots.cell_id = Slot(uri=AK_SCHEMA.cell_id, name="cell_id", curie=AK_SCHEMA.curie('cell_id'),
                   model_uri=AK_SCHEMA.cell_id, domain=None, range=Optional[str])

slots.clone_id = Slot(uri=AK_SCHEMA.clone_id, name="clone_id", curie=AK_SCHEMA.curie('clone_id'),
                   model_uri=AK_SCHEMA.clone_id, domain=None, range=Optional[str])

slots.sample_processing_id = Slot(uri=AK_SCHEMA.sample_processing_id, name="sample_processing_id", curie=AK_SCHEMA.curie('sample_processing_id'),
                   model_uri=AK_SCHEMA.sample_processing_id, domain=None, range=Optional[str])

slots.sequences = Slot(uri=AK_SCHEMA.sequences, name="sequences", curie=AK_SCHEMA.curie('sequences'),
                   model_uri=AK_SCHEMA.sequences, domain=None, range=Optional[Union[str, List[str]]])

slots.junction_start = Slot(uri=AK_SCHEMA.junction_start, name="junction_start", curie=AK_SCHEMA.curie('junction_start'),
                   model_uri=AK_SCHEMA.junction_start, domain=None, range=Optional[int])

slots.junction_end = Slot(uri=AK_SCHEMA.junction_end, name="junction_end", curie=AK_SCHEMA.curie('junction_end'),
                   model_uri=AK_SCHEMA.junction_end, domain=None, range=Optional[int])

slots.clone_count = Slot(uri=AK_SCHEMA.clone_count, name="clone_count", curie=AK_SCHEMA.curie('clone_count'),
                   model_uri=AK_SCHEMA.clone_count, domain=None, range=Optional[int])

slots.seed_id = Slot(uri=AK_SCHEMA.seed_id, name="seed_id", curie=AK_SCHEMA.curie('seed_id'),
                   model_uri=AK_SCHEMA.seed_id, domain=None, range=Optional[str])

slots.tree_id = Slot(uri=AK_SCHEMA.tree_id, name="tree_id", curie=AK_SCHEMA.curie('tree_id'),
                   model_uri=AK_SCHEMA.tree_id, domain=None, range=Optional[str])

slots.newick = Slot(uri=AK_SCHEMA.newick, name="newick", curie=AK_SCHEMA.curie('newick'),
                   model_uri=AK_SCHEMA.newick, domain=None, range=Optional[str])

slots.nodes = Slot(uri=AK_SCHEMA.nodes, name="nodes", curie=AK_SCHEMA.curie('nodes'),
                   model_uri=AK_SCHEMA.nodes, domain=None, range=Optional[Union[Union[dict, Node], List[Union[dict, Node]]]])

slots.rearrangements = Slot(uri=AK_SCHEMA.rearrangements, name="rearrangements", curie=AK_SCHEMA.curie('rearrangements'),
                   model_uri=AK_SCHEMA.rearrangements, domain=None, range=Optional[Union[str, List[str]]])

slots.receptors = Slot(uri=AK_SCHEMA.receptors, name="receptors", curie=AK_SCHEMA.curie('receptors'),
                   model_uri=AK_SCHEMA.receptors, domain=None, range=Optional[Union[str, List[str]]])

slots.expression_study_method = Slot(uri=AK_SCHEMA.expression_study_method, name="expression_study_method", curie=AK_SCHEMA.curie('expression_study_method'),
                   model_uri=AK_SCHEMA.expression_study_method, domain=None, range=Optional[Union[str, "ExpressionStudyMethod"]])

slots.expression_raw_doi = Slot(uri=AK_SCHEMA.expression_raw_doi, name="expression_raw_doi", curie=AK_SCHEMA.curie('expression_raw_doi'),
                   model_uri=AK_SCHEMA.expression_raw_doi, domain=None, range=Optional[str])

slots.expression_index = Slot(uri=AK_SCHEMA.expression_index, name="expression_index", curie=AK_SCHEMA.curie('expression_index'),
                   model_uri=AK_SCHEMA.expression_index, domain=None, range=Optional[str])

slots.virtual_pairing = Slot(uri=AK_SCHEMA.virtual_pairing, name="virtual_pairing", curie=AK_SCHEMA.curie('virtual_pairing'),
                   model_uri=AK_SCHEMA.virtual_pairing, domain=None, range=Optional[Union[bool, Bool]])

slots.expression_id = Slot(uri=AK_SCHEMA.expression_id, name="expression_id", curie=AK_SCHEMA.curie('expression_id'),
                   model_uri=AK_SCHEMA.expression_id, domain=None, range=Optional[str])

slots.property_type = Slot(uri=RDF.type, name="property_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.property_type, domain=None, range=Optional[str])

slots.property = Slot(uri=AK_SCHEMA.property, name="property", curie=AK_SCHEMA.curie('property'),
                   model_uri=AK_SCHEMA.property, domain=None, range=Optional[Union[str, "Property"]])

slots.receptor_id = Slot(uri=AK_SCHEMA.receptor_id, name="receptor_id", curie=AK_SCHEMA.curie('receptor_id'),
                   model_uri=AK_SCHEMA.receptor_id, domain=None, range=Optional[str])

slots.receptor_hash = Slot(uri=AK_SCHEMA.receptor_hash, name="receptor_hash", curie=AK_SCHEMA.curie('receptor_hash'),
                   model_uri=AK_SCHEMA.receptor_hash, domain=None, range=Optional[str])

slots.receptor_type = Slot(uri=RDF.type, name="receptor_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.receptor_type, domain=None, range=Optional[Union[str, "ReceptorType"]])

slots.receptor_variable_domain_1_aa = Slot(uri=AK_SCHEMA.receptor_variable_domain_1_aa, name="receptor_variable_domain_1_aa", curie=AK_SCHEMA.curie('receptor_variable_domain_1_aa'),
                   model_uri=AK_SCHEMA.receptor_variable_domain_1_aa, domain=None, range=Optional[str])

slots.receptor_variable_domain_1_locus = Slot(uri=AK_SCHEMA.receptor_variable_domain_1_locus, name="receptor_variable_domain_1_locus", curie=AK_SCHEMA.curie('receptor_variable_domain_1_locus'),
                   model_uri=AK_SCHEMA.receptor_variable_domain_1_locus, domain=None, range=Optional[Union[str, "ReceptorVariableDomain1Locus"]])

slots.receptor_variable_domain_2_aa = Slot(uri=AK_SCHEMA.receptor_variable_domain_2_aa, name="receptor_variable_domain_2_aa", curie=AK_SCHEMA.curie('receptor_variable_domain_2_aa'),
                   model_uri=AK_SCHEMA.receptor_variable_domain_2_aa, domain=None, range=Optional[str])

slots.receptor_variable_domain_2_locus = Slot(uri=AK_SCHEMA.receptor_variable_domain_2_locus, name="receptor_variable_domain_2_locus", curie=AK_SCHEMA.curie('receptor_variable_domain_2_locus'),
                   model_uri=AK_SCHEMA.receptor_variable_domain_2_locus, domain=None, range=Optional[Union[str, "ReceptorVariableDomain2Locus"]])

slots.receptor_ref = Slot(uri=AK_SCHEMA.receptor_ref, name="receptor_ref", curie=AK_SCHEMA.curie('receptor_ref'),
                   model_uri=AK_SCHEMA.receptor_ref, domain=None, range=Optional[Union[str, List[str]]])

slots.reactivity_measurements = Slot(uri=AK_SCHEMA.reactivity_measurements, name="reactivity_measurements", curie=AK_SCHEMA.curie('reactivity_measurements'),
                   model_uri=AK_SCHEMA.reactivity_measurements, domain=None, range=Optional[Union[Union[dict, ReceptorReactivity], List[Union[dict, ReceptorReactivity]]]])

slots.ligand_type = Slot(uri=RDF.type, name="ligand_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.ligand_type, domain=None, range=Optional[Union[str, "LigandType"]])

slots.antigen_type = Slot(uri=RDF.type, name="antigen_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.antigen_type, domain=None, range=Optional[Union[str, "AntigenType"]])

slots.antigen = Slot(uri=AK_SCHEMA.antigen, name="antigen", curie=AK_SCHEMA.curie('antigen'),
                   model_uri=AK_SCHEMA.antigen, domain=None, range=Optional[Union[str, "Antigen"]])

slots.antigen_source_species = Slot(uri=AK_SCHEMA.antigen_source_species, name="antigen_source_species", curie=AK_SCHEMA.curie('antigen_source_species'),
                   model_uri=AK_SCHEMA.antigen_source_species, domain=None, range=Optional[Union[str, "AntigenSourceSpecies"]])

slots.peptide_start = Slot(uri=AK_SCHEMA.peptide_start, name="peptide_start", curie=AK_SCHEMA.curie('peptide_start'),
                   model_uri=AK_SCHEMA.peptide_start, domain=None, range=Optional[int])

slots.peptide_end = Slot(uri=AK_SCHEMA.peptide_end, name="peptide_end", curie=AK_SCHEMA.curie('peptide_end'),
                   model_uri=AK_SCHEMA.peptide_end, domain=None, range=Optional[int])

slots.mhc_gene_1 = Slot(uri=AK_SCHEMA.mhc_gene_1, name="mhc_gene_1", curie=AK_SCHEMA.curie('mhc_gene_1'),
                   model_uri=AK_SCHEMA.mhc_gene_1, domain=None, range=Optional[Union[str, "MhcGene1"]])

slots.mhc_allele_1 = Slot(uri=AK_SCHEMA.mhc_allele_1, name="mhc_allele_1", curie=AK_SCHEMA.curie('mhc_allele_1'),
                   model_uri=AK_SCHEMA.mhc_allele_1, domain=None, range=Optional[str])

slots.mhc_gene_2 = Slot(uri=AK_SCHEMA.mhc_gene_2, name="mhc_gene_2", curie=AK_SCHEMA.curie('mhc_gene_2'),
                   model_uri=AK_SCHEMA.mhc_gene_2, domain=None, range=Optional[Union[str, "MhcGene2"]])

slots.mhc_allele_2 = Slot(uri=AK_SCHEMA.mhc_allele_2, name="mhc_allele_2", curie=AK_SCHEMA.curie('mhc_allele_2'),
                   model_uri=AK_SCHEMA.mhc_allele_2, domain=None, range=Optional[str])

slots.reactivity_method = Slot(uri=AK_SCHEMA.reactivity_method, name="reactivity_method", curie=AK_SCHEMA.curie('reactivity_method'),
                   model_uri=AK_SCHEMA.reactivity_method, domain=None, range=Optional[Union[str, "ReactivityMethod"]])

slots.reactivity_readout = Slot(uri=AK_SCHEMA.reactivity_readout, name="reactivity_readout", curie=AK_SCHEMA.curie('reactivity_readout'),
                   model_uri=AK_SCHEMA.reactivity_readout, domain=None, range=Optional[Union[str, "ReactivityReadout"]])

slots.reactivity_value = Slot(uri=AK_SCHEMA.reactivity_value, name="reactivity_value", curie=AK_SCHEMA.curie('reactivity_value'),
                   model_uri=AK_SCHEMA.reactivity_value, domain=None, range=Optional[float])

slots.reactivity_unit = Slot(uri=AK_SCHEMA.reactivity_unit, name="reactivity_unit", curie=AK_SCHEMA.curie('reactivity_unit'),
                   model_uri=AK_SCHEMA.reactivity_unit, domain=None, range=Optional[str])

slots.V1p5label = Slot(uri=AK_SCHEMA.V1p5label, name="V1p5label", curie=AK_SCHEMA.curie('V1p5label'),
                   model_uri=AK_SCHEMA.V1p5label, domain=None, range=Optional[str])

slots.V1p5value = Slot(uri=AK_SCHEMA.V1p5value, name="V1p5value", curie=AK_SCHEMA.curie('V1p5value'),
                   model_uri=AK_SCHEMA.V1p5value, domain=None, range=Optional[float])

slots.V1p5unit = Slot(uri=AK_SCHEMA.V1p5unit, name="V1p5unit", curie=AK_SCHEMA.curie('V1p5unit'),
                   model_uri=AK_SCHEMA.V1p5unit, domain=None, range=Optional[Union[str, "V1p5Unit"]])

slots.V1p5acknowledgement_id = Slot(uri=AK_SCHEMA.V1p5acknowledgement_id, name="V1p5acknowledgement_id", curie=AK_SCHEMA.curie('V1p5acknowledgement_id'),
                   model_uri=AK_SCHEMA.V1p5acknowledgement_id, domain=None, range=Optional[str])

slots.V1p5name = Slot(uri=AK_SCHEMA.V1p5name, name="V1p5name", curie=AK_SCHEMA.curie('V1p5name'),
                   model_uri=AK_SCHEMA.V1p5name, domain=None, range=Optional[str])

slots.V1p5institution_name = Slot(uri=AK_SCHEMA.V1p5institution_name, name="V1p5institution_name", curie=AK_SCHEMA.curie('V1p5institution_name'),
                   model_uri=AK_SCHEMA.V1p5institution_name, domain=None, range=Optional[str])

slots.V1p5orcid_id = Slot(uri=AK_SCHEMA.V1p5orcid_id, name="V1p5orcid_id", curie=AK_SCHEMA.curie('V1p5orcid_id'),
                   model_uri=AK_SCHEMA.V1p5orcid_id, domain=None, range=Optional[str])

slots.V1p5sequence_id = Slot(uri=AK_SCHEMA.V1p5sequence_id, name="V1p5sequence_id", curie=AK_SCHEMA.curie('V1p5sequence_id'),
                   model_uri=AK_SCHEMA.V1p5sequence_id, domain=None, range=Optional[str])

slots.V1p5sequence = Slot(uri=AK_SCHEMA.V1p5sequence, name="V1p5sequence", curie=AK_SCHEMA.curie('V1p5sequence'),
                   model_uri=AK_SCHEMA.V1p5sequence, domain=None, range=Optional[str])

slots.V1p5derivation = Slot(uri=AK_SCHEMA.V1p5derivation, name="V1p5derivation", curie=AK_SCHEMA.curie('V1p5derivation'),
                   model_uri=AK_SCHEMA.V1p5derivation, domain=None, range=Optional[Union[str, "V1p5Derivation"]])

slots.V1p5observation_type = Slot(uri=RDF.type, name="V1p5observation_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p5observation_type, domain=None, range=Optional[Union[str, "V1p5ObservationType"]])

slots.V1p5curation = Slot(uri=AK_SCHEMA.V1p5curation, name="V1p5curation", curie=AK_SCHEMA.curie('V1p5curation'),
                   model_uri=AK_SCHEMA.V1p5curation, domain=None, range=Optional[str])

slots.V1p5repository_name = Slot(uri=AK_SCHEMA.V1p5repository_name, name="V1p5repository_name", curie=AK_SCHEMA.curie('V1p5repository_name'),
                   model_uri=AK_SCHEMA.V1p5repository_name, domain=None, range=Optional[str])

slots.V1p5repository_ref = Slot(uri=AK_SCHEMA.V1p5repository_ref, name="V1p5repository_ref", curie=AK_SCHEMA.curie('V1p5repository_ref'),
                   model_uri=AK_SCHEMA.V1p5repository_ref, domain=None, range=Optional[str])

slots.V1p5deposited_version = Slot(uri=AK_SCHEMA.V1p5deposited_version, name="V1p5deposited_version", curie=AK_SCHEMA.curie('V1p5deposited_version'),
                   model_uri=AK_SCHEMA.V1p5deposited_version, domain=None, range=Optional[str])

slots.V1p5sequence_start = Slot(uri=AK_SCHEMA.V1p5sequence_start, name="V1p5sequence_start", curie=AK_SCHEMA.curie('V1p5sequence_start'),
                   model_uri=AK_SCHEMA.V1p5sequence_start, domain=None, range=Optional[int])

slots.V1p5sequence_end = Slot(uri=AK_SCHEMA.V1p5sequence_end, name="V1p5sequence_end", curie=AK_SCHEMA.curie('V1p5sequence_end'),
                   model_uri=AK_SCHEMA.V1p5sequence_end, domain=None, range=Optional[int])

slots.V1p5patch_no = Slot(uri=AK_SCHEMA.V1p5patch_no, name="V1p5patch_no", curie=AK_SCHEMA.curie('V1p5patch_no'),
                   model_uri=AK_SCHEMA.V1p5patch_no, domain=None, range=Optional[str])

slots.V1p5gff_seqid = Slot(uri=AK_SCHEMA.V1p5gff_seqid, name="V1p5gff_seqid", curie=AK_SCHEMA.curie('V1p5gff_seqid'),
                   model_uri=AK_SCHEMA.V1p5gff_seqid, domain=None, range=Optional[str])

slots.V1p5gff_start = Slot(uri=AK_SCHEMA.V1p5gff_start, name="V1p5gff_start", curie=AK_SCHEMA.curie('V1p5gff_start'),
                   model_uri=AK_SCHEMA.V1p5gff_start, domain=None, range=Optional[int])

slots.V1p5gff_end = Slot(uri=AK_SCHEMA.V1p5gff_end, name="V1p5gff_end", curie=AK_SCHEMA.curie('V1p5gff_end'),
                   model_uri=AK_SCHEMA.V1p5gff_end, domain=None, range=Optional[int])

slots.V1p5strand = Slot(uri=AK_SCHEMA.V1p5strand, name="V1p5strand", curie=AK_SCHEMA.curie('V1p5strand'),
                   model_uri=AK_SCHEMA.V1p5strand, domain=None, range=Optional[Union[str, "V1p5Strand"]])

slots.V1p5sequence_delineation_id = Slot(uri=AK_SCHEMA.V1p5sequence_delineation_id, name="V1p5sequence_delineation_id", curie=AK_SCHEMA.curie('V1p5sequence_delineation_id'),
                   model_uri=AK_SCHEMA.V1p5sequence_delineation_id, domain=None, range=Optional[str])

slots.V1p5delineation_scheme = Slot(uri=AK_SCHEMA.V1p5delineation_scheme, name="V1p5delineation_scheme", curie=AK_SCHEMA.curie('V1p5delineation_scheme'),
                   model_uri=AK_SCHEMA.V1p5delineation_scheme, domain=None, range=Optional[str])

slots.V1p5unaligned_sequence = Slot(uri=AK_SCHEMA.V1p5unaligned_sequence, name="V1p5unaligned_sequence", curie=AK_SCHEMA.curie('V1p5unaligned_sequence'),
                   model_uri=AK_SCHEMA.V1p5unaligned_sequence, domain=None, range=Optional[str])

slots.V1p5aligned_sequence = Slot(uri=AK_SCHEMA.V1p5aligned_sequence, name="V1p5aligned_sequence", curie=AK_SCHEMA.curie('V1p5aligned_sequence'),
                   model_uri=AK_SCHEMA.V1p5aligned_sequence, domain=None, range=Optional[str])

slots.V1p5fwr1_start = Slot(uri=AK_SCHEMA.V1p5fwr1_start, name="V1p5fwr1_start", curie=AK_SCHEMA.curie('V1p5fwr1_start'),
                   model_uri=AK_SCHEMA.V1p5fwr1_start, domain=None, range=Optional[int])

slots.V1p5fwr1_end = Slot(uri=AK_SCHEMA.V1p5fwr1_end, name="V1p5fwr1_end", curie=AK_SCHEMA.curie('V1p5fwr1_end'),
                   model_uri=AK_SCHEMA.V1p5fwr1_end, domain=None, range=Optional[int])

slots.V1p5cdr1_start = Slot(uri=AK_SCHEMA.V1p5cdr1_start, name="V1p5cdr1_start", curie=AK_SCHEMA.curie('V1p5cdr1_start'),
                   model_uri=AK_SCHEMA.V1p5cdr1_start, domain=None, range=Optional[int])

slots.V1p5cdr1_end = Slot(uri=AK_SCHEMA.V1p5cdr1_end, name="V1p5cdr1_end", curie=AK_SCHEMA.curie('V1p5cdr1_end'),
                   model_uri=AK_SCHEMA.V1p5cdr1_end, domain=None, range=Optional[int])

slots.V1p5fwr2_start = Slot(uri=AK_SCHEMA.V1p5fwr2_start, name="V1p5fwr2_start", curie=AK_SCHEMA.curie('V1p5fwr2_start'),
                   model_uri=AK_SCHEMA.V1p5fwr2_start, domain=None, range=Optional[int])

slots.V1p5fwr2_end = Slot(uri=AK_SCHEMA.V1p5fwr2_end, name="V1p5fwr2_end", curie=AK_SCHEMA.curie('V1p5fwr2_end'),
                   model_uri=AK_SCHEMA.V1p5fwr2_end, domain=None, range=Optional[int])

slots.V1p5cdr2_start = Slot(uri=AK_SCHEMA.V1p5cdr2_start, name="V1p5cdr2_start", curie=AK_SCHEMA.curie('V1p5cdr2_start'),
                   model_uri=AK_SCHEMA.V1p5cdr2_start, domain=None, range=Optional[int])

slots.V1p5cdr2_end = Slot(uri=AK_SCHEMA.V1p5cdr2_end, name="V1p5cdr2_end", curie=AK_SCHEMA.curie('V1p5cdr2_end'),
                   model_uri=AK_SCHEMA.V1p5cdr2_end, domain=None, range=Optional[int])

slots.V1p5fwr3_start = Slot(uri=AK_SCHEMA.V1p5fwr3_start, name="V1p5fwr3_start", curie=AK_SCHEMA.curie('V1p5fwr3_start'),
                   model_uri=AK_SCHEMA.V1p5fwr3_start, domain=None, range=Optional[int])

slots.V1p5fwr3_end = Slot(uri=AK_SCHEMA.V1p5fwr3_end, name="V1p5fwr3_end", curie=AK_SCHEMA.curie('V1p5fwr3_end'),
                   model_uri=AK_SCHEMA.V1p5fwr3_end, domain=None, range=Optional[int])

slots.V1p5cdr3_start = Slot(uri=AK_SCHEMA.V1p5cdr3_start, name="V1p5cdr3_start", curie=AK_SCHEMA.curie('V1p5cdr3_start'),
                   model_uri=AK_SCHEMA.V1p5cdr3_start, domain=None, range=Optional[int])

slots.V1p5alignment_labels = Slot(uri=AK_SCHEMA.V1p5alignment_labels, name="V1p5alignment_labels", curie=AK_SCHEMA.curie('V1p5alignment_labels'),
                   model_uri=AK_SCHEMA.V1p5alignment_labels, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p5allele_description_id = Slot(uri=AK_SCHEMA.V1p5allele_description_id, name="V1p5allele_description_id", curie=AK_SCHEMA.curie('V1p5allele_description_id'),
                   model_uri=AK_SCHEMA.V1p5allele_description_id, domain=None, range=Optional[str])

slots.V1p5allele_description_ref = Slot(uri=AK_SCHEMA.V1p5allele_description_ref, name="V1p5allele_description_ref", curie=AK_SCHEMA.curie('V1p5allele_description_ref'),
                   model_uri=AK_SCHEMA.V1p5allele_description_ref, domain=None, range=Optional[str])

slots.V1p5maintainer = Slot(uri=AK_SCHEMA.V1p5maintainer, name="V1p5maintainer", curie=AK_SCHEMA.curie('V1p5maintainer'),
                   model_uri=AK_SCHEMA.V1p5maintainer, domain=None, range=Optional[str])

slots.V1p5acknowledgements = Slot(uri=AK_SCHEMA.V1p5acknowledgements, name="V1p5acknowledgements", curie=AK_SCHEMA.curie('V1p5acknowledgements'),
                   model_uri=AK_SCHEMA.V1p5acknowledgements, domain=None, range=Optional[Union[Union[dict, V1p5Acknowledgement], List[Union[dict, V1p5Acknowledgement]]]])

slots.V1p5lab_address = Slot(uri=AK_SCHEMA.V1p5lab_address, name="V1p5lab_address", curie=AK_SCHEMA.curie('V1p5lab_address'),
                   model_uri=AK_SCHEMA.V1p5lab_address, domain=None, range=Optional[str])

slots.V1p5release_version = Slot(uri=AK_SCHEMA.V1p5release_version, name="V1p5release_version", curie=AK_SCHEMA.curie('V1p5release_version'),
                   model_uri=AK_SCHEMA.V1p5release_version, domain=None, range=Optional[str])

slots.V1p5release_date = Slot(uri=AK_SCHEMA.V1p5release_date, name="V1p5release_date", curie=AK_SCHEMA.curie('V1p5release_date'),
                   model_uri=AK_SCHEMA.V1p5release_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.V1p5release_description = Slot(uri=AK_SCHEMA.V1p5release_description, name="V1p5release_description", curie=AK_SCHEMA.curie('V1p5release_description'),
                   model_uri=AK_SCHEMA.V1p5release_description, domain=None, range=Optional[str])

slots.V1p5coding_sequence = Slot(uri=AK_SCHEMA.V1p5coding_sequence, name="V1p5coding_sequence", curie=AK_SCHEMA.curie('V1p5coding_sequence'),
                   model_uri=AK_SCHEMA.V1p5coding_sequence, domain=None, range=Optional[str])

slots.V1p5aliases = Slot(uri=AK_SCHEMA.V1p5aliases, name="V1p5aliases", curie=AK_SCHEMA.curie('V1p5aliases'),
                   model_uri=AK_SCHEMA.V1p5aliases, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p5locus = Slot(uri=AK_SCHEMA.V1p5locus, name="V1p5locus", curie=AK_SCHEMA.curie('V1p5locus'),
                   model_uri=AK_SCHEMA.V1p5locus, domain=None, range=Optional[Union[str, "V1p5Locus"]])

slots.V1p5chromosome = Slot(uri=AK_SCHEMA.V1p5chromosome, name="V1p5chromosome", curie=AK_SCHEMA.curie('V1p5chromosome'),
                   model_uri=AK_SCHEMA.V1p5chromosome, domain=None, range=Optional[int])

slots.V1p5sequence_type = Slot(uri=RDF.type, name="V1p5sequence_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p5sequence_type, domain=None, range=Optional[Union[str, "V1p5SequenceType"]])

slots.V1p5functional = Slot(uri=AK_SCHEMA.V1p5functional, name="V1p5functional", curie=AK_SCHEMA.curie('V1p5functional'),
                   model_uri=AK_SCHEMA.V1p5functional, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5inference_type = Slot(uri=RDF.type, name="V1p5inference_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p5inference_type, domain=None, range=Optional[Union[str, "V1p5InferenceType"]])

slots.V1p5species = Slot(uri=AK_SCHEMA.V1p5species, name="V1p5species", curie=AK_SCHEMA.curie('V1p5species'),
                   model_uri=AK_SCHEMA.V1p5species, domain=None, range=Optional[Union[str, "V1p5Species"]])

slots.V1p5species_subgroup = Slot(uri=AK_SCHEMA.V1p5species_subgroup, name="V1p5species_subgroup", curie=AK_SCHEMA.curie('V1p5species_subgroup'),
                   model_uri=AK_SCHEMA.V1p5species_subgroup, domain=None, range=Optional[str])

slots.V1p5species_subgroup_type = Slot(uri=RDF.type, name="V1p5species_subgroup_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p5species_subgroup_type, domain=None, range=Optional[Union[str, "V1p5SpeciesSubgroupType"]])

slots.V1p5status = Slot(uri=AK_SCHEMA.V1p5status, name="V1p5status", curie=AK_SCHEMA.curie('V1p5status'),
                   model_uri=AK_SCHEMA.V1p5status, domain=None, range=Optional[Union[str, "V1p5Status"]])

slots.V1p5subgroup_designation = Slot(uri=AK_SCHEMA.V1p5subgroup_designation, name="V1p5subgroup_designation", curie=AK_SCHEMA.curie('V1p5subgroup_designation'),
                   model_uri=AK_SCHEMA.V1p5subgroup_designation, domain=None, range=Optional[str])

slots.V1p5gene_designation = Slot(uri=AK_SCHEMA.V1p5gene_designation, name="V1p5gene_designation", curie=AK_SCHEMA.curie('V1p5gene_designation'),
                   model_uri=AK_SCHEMA.V1p5gene_designation, domain=None, range=Optional[str])

slots.V1p5allele_designation = Slot(uri=AK_SCHEMA.V1p5allele_designation, name="V1p5allele_designation", curie=AK_SCHEMA.curie('V1p5allele_designation'),
                   model_uri=AK_SCHEMA.V1p5allele_designation, domain=None, range=Optional[str])

slots.V1p5allele_similarity_cluster_designation = Slot(uri=AK_SCHEMA.V1p5allele_similarity_cluster_designation, name="V1p5allele_similarity_cluster_designation", curie=AK_SCHEMA.curie('V1p5allele_similarity_cluster_designation'),
                   model_uri=AK_SCHEMA.V1p5allele_similarity_cluster_designation, domain=None, range=Optional[str])

slots.V1p5allele_similarity_cluster_member_id = Slot(uri=AK_SCHEMA.V1p5allele_similarity_cluster_member_id, name="V1p5allele_similarity_cluster_member_id", curie=AK_SCHEMA.curie('V1p5allele_similarity_cluster_member_id'),
                   model_uri=AK_SCHEMA.V1p5allele_similarity_cluster_member_id, domain=None, range=Optional[str])

slots.V1p5j_codon_frame = Slot(uri=AK_SCHEMA.V1p5j_codon_frame, name="V1p5j_codon_frame", curie=AK_SCHEMA.curie('V1p5j_codon_frame'),
                   model_uri=AK_SCHEMA.V1p5j_codon_frame, domain=None, range=Optional[Union[str, "V1p5JCodonFrame"]])

slots.V1p5gene_start = Slot(uri=AK_SCHEMA.V1p5gene_start, name="V1p5gene_start", curie=AK_SCHEMA.curie('V1p5gene_start'),
                   model_uri=AK_SCHEMA.V1p5gene_start, domain=None, range=Optional[int])

slots.V1p5gene_end = Slot(uri=AK_SCHEMA.V1p5gene_end, name="V1p5gene_end", curie=AK_SCHEMA.curie('V1p5gene_end'),
                   model_uri=AK_SCHEMA.V1p5gene_end, domain=None, range=Optional[int])

slots.V1p5utr_5_prime_start = Slot(uri=AK_SCHEMA.V1p5utr_5_prime_start, name="V1p5utr_5_prime_start", curie=AK_SCHEMA.curie('V1p5utr_5_prime_start'),
                   model_uri=AK_SCHEMA.V1p5utr_5_prime_start, domain=None, range=Optional[int])

slots.V1p5utr_5_prime_end = Slot(uri=AK_SCHEMA.V1p5utr_5_prime_end, name="V1p5utr_5_prime_end", curie=AK_SCHEMA.curie('V1p5utr_5_prime_end'),
                   model_uri=AK_SCHEMA.V1p5utr_5_prime_end, domain=None, range=Optional[int])

slots.V1p5leader_1_start = Slot(uri=AK_SCHEMA.V1p5leader_1_start, name="V1p5leader_1_start", curie=AK_SCHEMA.curie('V1p5leader_1_start'),
                   model_uri=AK_SCHEMA.V1p5leader_1_start, domain=None, range=Optional[int])

slots.V1p5leader_1_end = Slot(uri=AK_SCHEMA.V1p5leader_1_end, name="V1p5leader_1_end", curie=AK_SCHEMA.curie('V1p5leader_1_end'),
                   model_uri=AK_SCHEMA.V1p5leader_1_end, domain=None, range=Optional[int])

slots.V1p5leader_2_start = Slot(uri=AK_SCHEMA.V1p5leader_2_start, name="V1p5leader_2_start", curie=AK_SCHEMA.curie('V1p5leader_2_start'),
                   model_uri=AK_SCHEMA.V1p5leader_2_start, domain=None, range=Optional[int])

slots.V1p5leader_2_end = Slot(uri=AK_SCHEMA.V1p5leader_2_end, name="V1p5leader_2_end", curie=AK_SCHEMA.curie('V1p5leader_2_end'),
                   model_uri=AK_SCHEMA.V1p5leader_2_end, domain=None, range=Optional[int])

slots.V1p5v_rs_start = Slot(uri=AK_SCHEMA.V1p5v_rs_start, name="V1p5v_rs_start", curie=AK_SCHEMA.curie('V1p5v_rs_start'),
                   model_uri=AK_SCHEMA.V1p5v_rs_start, domain=None, range=Optional[int])

slots.V1p5v_rs_end = Slot(uri=AK_SCHEMA.V1p5v_rs_end, name="V1p5v_rs_end", curie=AK_SCHEMA.curie('V1p5v_rs_end'),
                   model_uri=AK_SCHEMA.V1p5v_rs_end, domain=None, range=Optional[int])

slots.V1p5d_rs_3_prime_start = Slot(uri=AK_SCHEMA.V1p5d_rs_3_prime_start, name="V1p5d_rs_3_prime_start", curie=AK_SCHEMA.curie('V1p5d_rs_3_prime_start'),
                   model_uri=AK_SCHEMA.V1p5d_rs_3_prime_start, domain=None, range=Optional[int])

slots.V1p5d_rs_3_prime_end = Slot(uri=AK_SCHEMA.V1p5d_rs_3_prime_end, name="V1p5d_rs_3_prime_end", curie=AK_SCHEMA.curie('V1p5d_rs_3_prime_end'),
                   model_uri=AK_SCHEMA.V1p5d_rs_3_prime_end, domain=None, range=Optional[int])

slots.V1p5d_rs_5_prime_start = Slot(uri=AK_SCHEMA.V1p5d_rs_5_prime_start, name="V1p5d_rs_5_prime_start", curie=AK_SCHEMA.curie('V1p5d_rs_5_prime_start'),
                   model_uri=AK_SCHEMA.V1p5d_rs_5_prime_start, domain=None, range=Optional[int])

slots.V1p5d_rs_5_prime_end = Slot(uri=AK_SCHEMA.V1p5d_rs_5_prime_end, name="V1p5d_rs_5_prime_end", curie=AK_SCHEMA.curie('V1p5d_rs_5_prime_end'),
                   model_uri=AK_SCHEMA.V1p5d_rs_5_prime_end, domain=None, range=Optional[int])

slots.V1p5j_cdr3_end = Slot(uri=AK_SCHEMA.V1p5j_cdr3_end, name="V1p5j_cdr3_end", curie=AK_SCHEMA.curie('V1p5j_cdr3_end'),
                   model_uri=AK_SCHEMA.V1p5j_cdr3_end, domain=None, range=Optional[int])

slots.V1p5j_rs_start = Slot(uri=AK_SCHEMA.V1p5j_rs_start, name="V1p5j_rs_start", curie=AK_SCHEMA.curie('V1p5j_rs_start'),
                   model_uri=AK_SCHEMA.V1p5j_rs_start, domain=None, range=Optional[int])

slots.V1p5j_rs_end = Slot(uri=AK_SCHEMA.V1p5j_rs_end, name="V1p5j_rs_end", curie=AK_SCHEMA.curie('V1p5j_rs_end'),
                   model_uri=AK_SCHEMA.V1p5j_rs_end, domain=None, range=Optional[int])

slots.V1p5j_donor_splice = Slot(uri=AK_SCHEMA.V1p5j_donor_splice, name="V1p5j_donor_splice", curie=AK_SCHEMA.curie('V1p5j_donor_splice'),
                   model_uri=AK_SCHEMA.V1p5j_donor_splice, domain=None, range=Optional[int])

slots.V1p5v_gene_delineations = Slot(uri=AK_SCHEMA.V1p5v_gene_delineations, name="V1p5v_gene_delineations", curie=AK_SCHEMA.curie('V1p5v_gene_delineations'),
                   model_uri=AK_SCHEMA.V1p5v_gene_delineations, domain=None, range=Optional[Union[Union[dict, V1p5SequenceDelineationV], List[Union[dict, V1p5SequenceDelineationV]]]])

slots.V1p5unrearranged_support = Slot(uri=AK_SCHEMA.V1p5unrearranged_support, name="V1p5unrearranged_support", curie=AK_SCHEMA.curie('V1p5unrearranged_support'),
                   model_uri=AK_SCHEMA.V1p5unrearranged_support, domain=None, range=Optional[Union[Union[dict, V1p5UnrearrangedSequence], List[Union[dict, V1p5UnrearrangedSequence]]]])

slots.V1p5rearranged_support = Slot(uri=AK_SCHEMA.V1p5rearranged_support, name="V1p5rearranged_support", curie=AK_SCHEMA.curie('V1p5rearranged_support'),
                   model_uri=AK_SCHEMA.V1p5rearranged_support, domain=None, range=Optional[Union[Union[dict, V1p5RearrangedSequence], List[Union[dict, V1p5RearrangedSequence]]]])

slots.V1p5paralogs = Slot(uri=AK_SCHEMA.V1p5paralogs, name="V1p5paralogs", curie=AK_SCHEMA.curie('V1p5paralogs'),
                   model_uri=AK_SCHEMA.V1p5paralogs, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p5curational_tags = Slot(uri=AK_SCHEMA.V1p5curational_tags, name="V1p5curational_tags", curie=AK_SCHEMA.curie('V1p5curational_tags'),
                   model_uri=AK_SCHEMA.V1p5curational_tags, domain=None, range=Optional[Union[Union[str, "V1p5CurationalTags"], List[Union[str, "V1p5CurationalTags"]]]])

slots.V1p5germline_set_id = Slot(uri=AK_SCHEMA.V1p5germline_set_id, name="V1p5germline_set_id", curie=AK_SCHEMA.curie('V1p5germline_set_id'),
                   model_uri=AK_SCHEMA.V1p5germline_set_id, domain=None, range=Optional[str])

slots.V1p5author = Slot(uri=AK_SCHEMA.V1p5author, name="V1p5author", curie=AK_SCHEMA.curie('V1p5author'),
                   model_uri=AK_SCHEMA.V1p5author, domain=None, range=Optional[str])

slots.V1p5lab_name = Slot(uri=AK_SCHEMA.V1p5lab_name, name="V1p5lab_name", curie=AK_SCHEMA.curie('V1p5lab_name'),
                   model_uri=AK_SCHEMA.V1p5lab_name, domain=None, range=Optional[str])

slots.V1p5germline_set_name = Slot(uri=AK_SCHEMA.V1p5germline_set_name, name="V1p5germline_set_name", curie=AK_SCHEMA.curie('V1p5germline_set_name'),
                   model_uri=AK_SCHEMA.V1p5germline_set_name, domain=None, range=Optional[str])

slots.V1p5germline_set_ref = Slot(uri=AK_SCHEMA.V1p5germline_set_ref, name="V1p5germline_set_ref", curie=AK_SCHEMA.curie('V1p5germline_set_ref'),
                   model_uri=AK_SCHEMA.V1p5germline_set_ref, domain=None, range=Optional[str])

slots.V1p5pub_ids = Slot(uri=AK_SCHEMA.V1p5pub_ids, name="V1p5pub_ids", curie=AK_SCHEMA.curie('V1p5pub_ids'),
                   model_uri=AK_SCHEMA.V1p5pub_ids, domain=None, range=Optional[str])

slots.V1p5allele_descriptions = Slot(uri=AK_SCHEMA.V1p5allele_descriptions, name="V1p5allele_descriptions", curie=AK_SCHEMA.curie('V1p5allele_descriptions'),
                   model_uri=AK_SCHEMA.V1p5allele_descriptions, domain=None, range=Optional[Union[Union[dict, V1p5AlleleDescription], List[Union[dict, V1p5AlleleDescription]]]])

slots.V1p5receptor_genotype_set_id = Slot(uri=AK_SCHEMA.V1p5receptor_genotype_set_id, name="V1p5receptor_genotype_set_id", curie=AK_SCHEMA.curie('V1p5receptor_genotype_set_id'),
                   model_uri=AK_SCHEMA.V1p5receptor_genotype_set_id, domain=None, range=Optional[str])

slots.V1p5genotype_class_list = Slot(uri=AK_SCHEMA.V1p5genotype_class_list, name="V1p5genotype_class_list", curie=AK_SCHEMA.curie('V1p5genotype_class_list'),
                   model_uri=AK_SCHEMA.V1p5genotype_class_list, domain=None, range=Optional[Union[Union[dict, V1p5Genotype], List[Union[dict, V1p5Genotype]]]])

slots.V1p5receptor_genotype_id = Slot(uri=AK_SCHEMA.V1p5receptor_genotype_id, name="V1p5receptor_genotype_id", curie=AK_SCHEMA.curie('V1p5receptor_genotype_id'),
                   model_uri=AK_SCHEMA.V1p5receptor_genotype_id, domain=None, range=Optional[str])

slots.V1p5documented_alleles = Slot(uri=AK_SCHEMA.V1p5documented_alleles, name="V1p5documented_alleles", curie=AK_SCHEMA.curie('V1p5documented_alleles'),
                   model_uri=AK_SCHEMA.V1p5documented_alleles, domain=None, range=Optional[Union[Union[dict, V1p5DocumentedAllele], List[Union[dict, V1p5DocumentedAllele]]]])

slots.V1p5undocumented_alleles = Slot(uri=AK_SCHEMA.V1p5undocumented_alleles, name="V1p5undocumented_alleles", curie=AK_SCHEMA.curie('V1p5undocumented_alleles'),
                   model_uri=AK_SCHEMA.V1p5undocumented_alleles, domain=None, range=Optional[Union[Union[dict, V1p5UndocumentedAllele], List[Union[dict, V1p5UndocumentedAllele]]]])

slots.V1p5deleted_genes = Slot(uri=AK_SCHEMA.V1p5deleted_genes, name="V1p5deleted_genes", curie=AK_SCHEMA.curie('V1p5deleted_genes'),
                   model_uri=AK_SCHEMA.V1p5deleted_genes, domain=None, range=Optional[Union[Union[dict, V1p5DeletedGene], List[Union[dict, V1p5DeletedGene]]]])

slots.V1p5inference_process = Slot(uri=AK_SCHEMA.V1p5inference_process, name="V1p5inference_process", curie=AK_SCHEMA.curie('V1p5inference_process'),
                   model_uri=AK_SCHEMA.V1p5inference_process, domain=None, range=Optional[Union[str, "V1p5InferenceProcess"]])

slots.V1p5phasing = Slot(uri=AK_SCHEMA.V1p5phasing, name="V1p5phasing", curie=AK_SCHEMA.curie('V1p5phasing'),
                   model_uri=AK_SCHEMA.V1p5phasing, domain=None, range=Optional[int])

slots.V1p5allele_name = Slot(uri=AK_SCHEMA.V1p5allele_name, name="V1p5allele_name", curie=AK_SCHEMA.curie('V1p5allele_name'),
                   model_uri=AK_SCHEMA.V1p5allele_name, domain=None, range=Optional[str])

slots.V1p5mhc_genotype_set_id = Slot(uri=AK_SCHEMA.V1p5mhc_genotype_set_id, name="V1p5mhc_genotype_set_id", curie=AK_SCHEMA.curie('V1p5mhc_genotype_set_id'),
                   model_uri=AK_SCHEMA.V1p5mhc_genotype_set_id, domain=None, range=Optional[str])

slots.V1p5mhc_genotype_list = Slot(uri=AK_SCHEMA.V1p5mhc_genotype_list, name="V1p5mhc_genotype_list", curie=AK_SCHEMA.curie('V1p5mhc_genotype_list'),
                   model_uri=AK_SCHEMA.V1p5mhc_genotype_list, domain=None, range=Optional[Union[Union[dict, V1p5MHCGenotype], List[Union[dict, V1p5MHCGenotype]]]])

slots.V1p5mhc_genotype_id = Slot(uri=AK_SCHEMA.V1p5mhc_genotype_id, name="V1p5mhc_genotype_id", curie=AK_SCHEMA.curie('V1p5mhc_genotype_id'),
                   model_uri=AK_SCHEMA.V1p5mhc_genotype_id, domain=None, range=Optional[str])

slots.V1p5mhc_class = Slot(uri=AK_SCHEMA.V1p5mhc_class, name="V1p5mhc_class", curie=AK_SCHEMA.curie('V1p5mhc_class'),
                   model_uri=AK_SCHEMA.V1p5mhc_class, domain=None, range=Optional[Union[str, "V1p5MhcClass"]])

slots.V1p5mhc_alleles = Slot(uri=AK_SCHEMA.V1p5mhc_alleles, name="V1p5mhc_alleles", curie=AK_SCHEMA.curie('V1p5mhc_alleles'),
                   model_uri=AK_SCHEMA.V1p5mhc_alleles, domain=None, range=Optional[Union[Union[dict, V1p5MHCAllele], List[Union[dict, V1p5MHCAllele]]]])

slots.V1p5mhc_genotyping_method = Slot(uri=AK_SCHEMA.V1p5mhc_genotyping_method, name="V1p5mhc_genotyping_method", curie=AK_SCHEMA.curie('V1p5mhc_genotyping_method'),
                   model_uri=AK_SCHEMA.V1p5mhc_genotyping_method, domain=None, range=Optional[str])

slots.V1p5gene = Slot(uri=AK_SCHEMA.V1p5gene, name="V1p5gene", curie=AK_SCHEMA.curie('V1p5gene'),
                   model_uri=AK_SCHEMA.V1p5gene, domain=None, range=Optional[Union[str, "V1p5Gene"]])

slots.V1p5reference_set_ref = Slot(uri=AK_SCHEMA.V1p5reference_set_ref, name="V1p5reference_set_ref", curie=AK_SCHEMA.curie('V1p5reference_set_ref'),
                   model_uri=AK_SCHEMA.V1p5reference_set_ref, domain=None, range=Optional[str])

slots.V1p5receptor_genotype_set = Slot(uri=AK_SCHEMA.V1p5receptor_genotype_set, name="V1p5receptor_genotype_set", curie=AK_SCHEMA.curie('V1p5receptor_genotype_set'),
                   model_uri=AK_SCHEMA.V1p5receptor_genotype_set, domain=None, range=Optional[Union[dict, V1p5GenotypeSet]])

slots.V1p5mhc_genotype_set = Slot(uri=AK_SCHEMA.V1p5mhc_genotype_set, name="V1p5mhc_genotype_set", curie=AK_SCHEMA.curie('V1p5mhc_genotype_set'),
                   model_uri=AK_SCHEMA.V1p5mhc_genotype_set, domain=None, range=Optional[Union[dict, V1p5MHCGenotypeSet]])

slots.V1p5study_id = Slot(uri=AK_SCHEMA.V1p5study_id, name="V1p5study_id", curie=AK_SCHEMA.curie('V1p5study_id'),
                   model_uri=AK_SCHEMA.V1p5study_id, domain=None, range=Optional[str])

slots.V1p5study_title = Slot(uri=AK_SCHEMA.V1p5study_title, name="V1p5study_title", curie=AK_SCHEMA.curie('V1p5study_title'),
                   model_uri=AK_SCHEMA.V1p5study_title, domain=None, range=Optional[str])

slots.V1p5study_type = Slot(uri=RDF.type, name="V1p5study_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p5study_type, domain=None, range=Optional[Union[str, "V1p5StudyType"]])

slots.V1p5study_description = Slot(uri=AK_SCHEMA.V1p5study_description, name="V1p5study_description", curie=AK_SCHEMA.curie('V1p5study_description'),
                   model_uri=AK_SCHEMA.V1p5study_description, domain=None, range=Optional[str])

slots.V1p5inclusion_exclusion_criteria = Slot(uri=AK_SCHEMA.V1p5inclusion_exclusion_criteria, name="V1p5inclusion_exclusion_criteria", curie=AK_SCHEMA.curie('V1p5inclusion_exclusion_criteria'),
                   model_uri=AK_SCHEMA.V1p5inclusion_exclusion_criteria, domain=None, range=Optional[str])

slots.V1p5grants = Slot(uri=AK_SCHEMA.V1p5grants, name="V1p5grants", curie=AK_SCHEMA.curie('V1p5grants'),
                   model_uri=AK_SCHEMA.V1p5grants, domain=None, range=Optional[str])

slots.V1p5study_contact = Slot(uri=AK_SCHEMA.V1p5study_contact, name="V1p5study_contact", curie=AK_SCHEMA.curie('V1p5study_contact'),
                   model_uri=AK_SCHEMA.V1p5study_contact, domain=None, range=Optional[str])

slots.V1p5collected_by = Slot(uri=AK_SCHEMA.V1p5collected_by, name="V1p5collected_by", curie=AK_SCHEMA.curie('V1p5collected_by'),
                   model_uri=AK_SCHEMA.V1p5collected_by, domain=None, range=Optional[str])

slots.V1p5submitted_by = Slot(uri=AK_SCHEMA.V1p5submitted_by, name="V1p5submitted_by", curie=AK_SCHEMA.curie('V1p5submitted_by'),
                   model_uri=AK_SCHEMA.V1p5submitted_by, domain=None, range=Optional[str])

slots.V1p5keywords_study = Slot(uri=AK_SCHEMA.V1p5keywords_study, name="V1p5keywords_study", curie=AK_SCHEMA.curie('V1p5keywords_study'),
                   model_uri=AK_SCHEMA.V1p5keywords_study, domain=None, range=Optional[Union[Union[str, "V1p5KeywordsStudy"], List[Union[str, "V1p5KeywordsStudy"]]]])

slots.V1p5adc_publish_date = Slot(uri=AK_SCHEMA.V1p5adc_publish_date, name="V1p5adc_publish_date", curie=AK_SCHEMA.curie('V1p5adc_publish_date'),
                   model_uri=AK_SCHEMA.V1p5adc_publish_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.V1p5adc_update_date = Slot(uri=AK_SCHEMA.V1p5adc_update_date, name="V1p5adc_update_date", curie=AK_SCHEMA.curie('V1p5adc_update_date'),
                   model_uri=AK_SCHEMA.V1p5adc_update_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.V1p5subject_id = Slot(uri=AK_SCHEMA.V1p5subject_id, name="V1p5subject_id", curie=AK_SCHEMA.curie('V1p5subject_id'),
                   model_uri=AK_SCHEMA.V1p5subject_id, domain=None, range=Optional[str])

slots.V1p5synthetic = Slot(uri=AK_SCHEMA.V1p5synthetic, name="V1p5synthetic", curie=AK_SCHEMA.curie('V1p5synthetic'),
                   model_uri=AK_SCHEMA.V1p5synthetic, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5sex = Slot(uri=AK_SCHEMA.V1p5sex, name="V1p5sex", curie=AK_SCHEMA.curie('V1p5sex'),
                   model_uri=AK_SCHEMA.V1p5sex, domain=None, range=Optional[Union[str, "V1p5Sex"]])

slots.V1p5age_min = Slot(uri=AK_SCHEMA.V1p5age_min, name="V1p5age_min", curie=AK_SCHEMA.curie('V1p5age_min'),
                   model_uri=AK_SCHEMA.V1p5age_min, domain=None, range=Optional[float])

slots.V1p5age_max = Slot(uri=AK_SCHEMA.V1p5age_max, name="V1p5age_max", curie=AK_SCHEMA.curie('V1p5age_max'),
                   model_uri=AK_SCHEMA.V1p5age_max, domain=None, range=Optional[float])

slots.V1p5age_unit = Slot(uri=AK_SCHEMA.V1p5age_unit, name="V1p5age_unit", curie=AK_SCHEMA.curie('V1p5age_unit'),
                   model_uri=AK_SCHEMA.V1p5age_unit, domain=None, range=Optional[Union[str, "V1p5AgeUnit"]])

slots.V1p5age_event = Slot(uri=AK_SCHEMA.V1p5age_event, name="V1p5age_event", curie=AK_SCHEMA.curie('V1p5age_event'),
                   model_uri=AK_SCHEMA.V1p5age_event, domain=None, range=Optional[str])

slots.V1p5ancestry_population = Slot(uri=AK_SCHEMA.V1p5ancestry_population, name="V1p5ancestry_population", curie=AK_SCHEMA.curie('V1p5ancestry_population'),
                   model_uri=AK_SCHEMA.V1p5ancestry_population, domain=None, range=Optional[str])

slots.V1p5ethnicity = Slot(uri=AK_SCHEMA.V1p5ethnicity, name="V1p5ethnicity", curie=AK_SCHEMA.curie('V1p5ethnicity'),
                   model_uri=AK_SCHEMA.V1p5ethnicity, domain=None, range=Optional[str])

slots.V1p5race = Slot(uri=AK_SCHEMA.V1p5race, name="V1p5race", curie=AK_SCHEMA.curie('V1p5race'),
                   model_uri=AK_SCHEMA.V1p5race, domain=None, range=Optional[str])

slots.V1p5strain_name = Slot(uri=AK_SCHEMA.V1p5strain_name, name="V1p5strain_name", curie=AK_SCHEMA.curie('V1p5strain_name'),
                   model_uri=AK_SCHEMA.V1p5strain_name, domain=None, range=Optional[str])

slots.V1p5linked_subjects = Slot(uri=AK_SCHEMA.V1p5linked_subjects, name="V1p5linked_subjects", curie=AK_SCHEMA.curie('V1p5linked_subjects'),
                   model_uri=AK_SCHEMA.V1p5linked_subjects, domain=None, range=Optional[str])

slots.V1p5link_type = Slot(uri=RDF.type, name="V1p5link_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p5link_type, domain=None, range=Optional[str])

slots.V1p5diagnosis = Slot(uri=AK_SCHEMA.V1p5diagnosis, name="V1p5diagnosis", curie=AK_SCHEMA.curie('V1p5diagnosis'),
                   model_uri=AK_SCHEMA.V1p5diagnosis, domain=None, range=Optional[Union[Union[dict, V1p5Diagnosis], List[Union[dict, V1p5Diagnosis]]]])

slots.V1p5genotype = Slot(uri=AK_SCHEMA.V1p5genotype, name="V1p5genotype", curie=AK_SCHEMA.curie('V1p5genotype'),
                   model_uri=AK_SCHEMA.V1p5genotype, domain=None, range=Optional[Union[dict, V1p5SubjectGenotype]])

slots.V1p5study_group_description = Slot(uri=AK_SCHEMA.V1p5study_group_description, name="V1p5study_group_description", curie=AK_SCHEMA.curie('V1p5study_group_description'),
                   model_uri=AK_SCHEMA.V1p5study_group_description, domain=None, range=Optional[str])

slots.V1p5disease_diagnosis = Slot(uri=AK_SCHEMA.V1p5disease_diagnosis, name="V1p5disease_diagnosis", curie=AK_SCHEMA.curie('V1p5disease_diagnosis'),
                   model_uri=AK_SCHEMA.V1p5disease_diagnosis, domain=None, range=Optional[Union[str, "V1p5DiseaseDiagnosis"]])

slots.V1p5disease_length = Slot(uri=AK_SCHEMA.V1p5disease_length, name="V1p5disease_length", curie=AK_SCHEMA.curie('V1p5disease_length'),
                   model_uri=AK_SCHEMA.V1p5disease_length, domain=None, range=Optional[str])

slots.V1p5disease_stage = Slot(uri=AK_SCHEMA.V1p5disease_stage, name="V1p5disease_stage", curie=AK_SCHEMA.curie('V1p5disease_stage'),
                   model_uri=AK_SCHEMA.V1p5disease_stage, domain=None, range=Optional[str])

slots.V1p5prior_therapies = Slot(uri=AK_SCHEMA.V1p5prior_therapies, name="V1p5prior_therapies", curie=AK_SCHEMA.curie('V1p5prior_therapies'),
                   model_uri=AK_SCHEMA.V1p5prior_therapies, domain=None, range=Optional[str])

slots.V1p5immunogen = Slot(uri=AK_SCHEMA.V1p5immunogen, name="V1p5immunogen", curie=AK_SCHEMA.curie('V1p5immunogen'),
                   model_uri=AK_SCHEMA.V1p5immunogen, domain=None, range=Optional[str])

slots.V1p5intervention = Slot(uri=AK_SCHEMA.V1p5intervention, name="V1p5intervention", curie=AK_SCHEMA.curie('V1p5intervention'),
                   model_uri=AK_SCHEMA.V1p5intervention, domain=None, range=Optional[str])

slots.V1p5medical_history = Slot(uri=AK_SCHEMA.V1p5medical_history, name="V1p5medical_history", curie=AK_SCHEMA.curie('V1p5medical_history'),
                   model_uri=AK_SCHEMA.V1p5medical_history, domain=None, range=Optional[str])

slots.V1p5sample_id = Slot(uri=AK_SCHEMA.V1p5sample_id, name="V1p5sample_id", curie=AK_SCHEMA.curie('V1p5sample_id'),
                   model_uri=AK_SCHEMA.V1p5sample_id, domain=None, range=Optional[str])

slots.V1p5sample_type = Slot(uri=RDF.type, name="V1p5sample_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p5sample_type, domain=None, range=Optional[str])

slots.V1p5tissue = Slot(uri=AK_SCHEMA.V1p5tissue, name="V1p5tissue", curie=AK_SCHEMA.curie('V1p5tissue'),
                   model_uri=AK_SCHEMA.V1p5tissue, domain=None, range=Optional[Union[str, "V1p5Tissue"]])

slots.V1p5anatomic_site = Slot(uri=AK_SCHEMA.V1p5anatomic_site, name="V1p5anatomic_site", curie=AK_SCHEMA.curie('V1p5anatomic_site'),
                   model_uri=AK_SCHEMA.V1p5anatomic_site, domain=None, range=Optional[str])

slots.V1p5disease_state_sample = Slot(uri=AK_SCHEMA.V1p5disease_state_sample, name="V1p5disease_state_sample", curie=AK_SCHEMA.curie('V1p5disease_state_sample'),
                   model_uri=AK_SCHEMA.V1p5disease_state_sample, domain=None, range=Optional[str])

slots.V1p5collection_time_point_relative = Slot(uri=AK_SCHEMA.V1p5collection_time_point_relative, name="V1p5collection_time_point_relative", curie=AK_SCHEMA.curie('V1p5collection_time_point_relative'),
                   model_uri=AK_SCHEMA.V1p5collection_time_point_relative, domain=None, range=Optional[float])

slots.V1p5collection_time_point_relative_unit = Slot(uri=AK_SCHEMA.V1p5collection_time_point_relative_unit, name="V1p5collection_time_point_relative_unit", curie=AK_SCHEMA.curie('V1p5collection_time_point_relative_unit'),
                   model_uri=AK_SCHEMA.V1p5collection_time_point_relative_unit, domain=None, range=Optional[Union[str, "V1p5CollectionTimePointRelativeUnit"]])

slots.V1p5collection_time_point_reference = Slot(uri=AK_SCHEMA.V1p5collection_time_point_reference, name="V1p5collection_time_point_reference", curie=AK_SCHEMA.curie('V1p5collection_time_point_reference'),
                   model_uri=AK_SCHEMA.V1p5collection_time_point_reference, domain=None, range=Optional[str])

slots.V1p5biomaterial_provider = Slot(uri=AK_SCHEMA.V1p5biomaterial_provider, name="V1p5biomaterial_provider", curie=AK_SCHEMA.curie('V1p5biomaterial_provider'),
                   model_uri=AK_SCHEMA.V1p5biomaterial_provider, domain=None, range=Optional[str])

slots.V1p5tissue_processing = Slot(uri=AK_SCHEMA.V1p5tissue_processing, name="V1p5tissue_processing", curie=AK_SCHEMA.curie('V1p5tissue_processing'),
                   model_uri=AK_SCHEMA.V1p5tissue_processing, domain=None, range=Optional[str])

slots.V1p5cell_subset = Slot(uri=AK_SCHEMA.V1p5cell_subset, name="V1p5cell_subset", curie=AK_SCHEMA.curie('V1p5cell_subset'),
                   model_uri=AK_SCHEMA.V1p5cell_subset, domain=None, range=Optional[Union[str, "V1p5CellSubset"]])

slots.V1p5cell_phenotype = Slot(uri=AK_SCHEMA.V1p5cell_phenotype, name="V1p5cell_phenotype", curie=AK_SCHEMA.curie('V1p5cell_phenotype'),
                   model_uri=AK_SCHEMA.V1p5cell_phenotype, domain=None, range=Optional[str])

slots.V1p5cell_species = Slot(uri=AK_SCHEMA.V1p5cell_species, name="V1p5cell_species", curie=AK_SCHEMA.curie('V1p5cell_species'),
                   model_uri=AK_SCHEMA.V1p5cell_species, domain=None, range=Optional[Union[str, "V1p5CellSpecies"]])

slots.V1p5single_cell = Slot(uri=AK_SCHEMA.V1p5single_cell, name="V1p5single_cell", curie=AK_SCHEMA.curie('V1p5single_cell'),
                   model_uri=AK_SCHEMA.V1p5single_cell, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5cell_number = Slot(uri=AK_SCHEMA.V1p5cell_number, name="V1p5cell_number", curie=AK_SCHEMA.curie('V1p5cell_number'),
                   model_uri=AK_SCHEMA.V1p5cell_number, domain=None, range=Optional[int])

slots.V1p5cells_per_reaction = Slot(uri=AK_SCHEMA.V1p5cells_per_reaction, name="V1p5cells_per_reaction", curie=AK_SCHEMA.curie('V1p5cells_per_reaction'),
                   model_uri=AK_SCHEMA.V1p5cells_per_reaction, domain=None, range=Optional[int])

slots.V1p5cell_storage = Slot(uri=AK_SCHEMA.V1p5cell_storage, name="V1p5cell_storage", curie=AK_SCHEMA.curie('V1p5cell_storage'),
                   model_uri=AK_SCHEMA.V1p5cell_storage, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5cell_quality = Slot(uri=AK_SCHEMA.V1p5cell_quality, name="V1p5cell_quality", curie=AK_SCHEMA.curie('V1p5cell_quality'),
                   model_uri=AK_SCHEMA.V1p5cell_quality, domain=None, range=Optional[str])

slots.V1p5cell_isolation = Slot(uri=AK_SCHEMA.V1p5cell_isolation, name="V1p5cell_isolation", curie=AK_SCHEMA.curie('V1p5cell_isolation'),
                   model_uri=AK_SCHEMA.V1p5cell_isolation, domain=None, range=Optional[str])

slots.V1p5cell_processing_protocol = Slot(uri=AK_SCHEMA.V1p5cell_processing_protocol, name="V1p5cell_processing_protocol", curie=AK_SCHEMA.curie('V1p5cell_processing_protocol'),
                   model_uri=AK_SCHEMA.V1p5cell_processing_protocol, domain=None, range=Optional[str])

slots.V1p5pcr_target_locus = Slot(uri=AK_SCHEMA.V1p5pcr_target_locus, name="V1p5pcr_target_locus", curie=AK_SCHEMA.curie('V1p5pcr_target_locus'),
                   model_uri=AK_SCHEMA.V1p5pcr_target_locus, domain=None, range=Optional[Union[str, "V1p5PcrTargetLocus"]])

slots.V1p5forward_pcr_primer_target_location = Slot(uri=AK_SCHEMA.V1p5forward_pcr_primer_target_location, name="V1p5forward_pcr_primer_target_location", curie=AK_SCHEMA.curie('V1p5forward_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.V1p5forward_pcr_primer_target_location, domain=None, range=Optional[str])

slots.V1p5reverse_pcr_primer_target_location = Slot(uri=AK_SCHEMA.V1p5reverse_pcr_primer_target_location, name="V1p5reverse_pcr_primer_target_location", curie=AK_SCHEMA.curie('V1p5reverse_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.V1p5reverse_pcr_primer_target_location, domain=None, range=Optional[str])

slots.V1p5template_class = Slot(uri=AK_SCHEMA.V1p5template_class, name="V1p5template_class", curie=AK_SCHEMA.curie('V1p5template_class'),
                   model_uri=AK_SCHEMA.V1p5template_class, domain=None, range=Optional[Union[str, "V1p5TemplateClass"]])

slots.V1p5template_quality = Slot(uri=AK_SCHEMA.V1p5template_quality, name="V1p5template_quality", curie=AK_SCHEMA.curie('V1p5template_quality'),
                   model_uri=AK_SCHEMA.V1p5template_quality, domain=None, range=Optional[str])

slots.V1p5template_amount = Slot(uri=AK_SCHEMA.V1p5template_amount, name="V1p5template_amount", curie=AK_SCHEMA.curie('V1p5template_amount'),
                   model_uri=AK_SCHEMA.V1p5template_amount, domain=None, range=Optional[float])

slots.V1p5template_amount_unit = Slot(uri=AK_SCHEMA.V1p5template_amount_unit, name="V1p5template_amount_unit", curie=AK_SCHEMA.curie('V1p5template_amount_unit'),
                   model_uri=AK_SCHEMA.V1p5template_amount_unit, domain=None, range=Optional[Union[str, "V1p5TemplateAmountUnit"]])

slots.V1p5library_generation_method = Slot(uri=AK_SCHEMA.V1p5library_generation_method, name="V1p5library_generation_method", curie=AK_SCHEMA.curie('V1p5library_generation_method'),
                   model_uri=AK_SCHEMA.V1p5library_generation_method, domain=None, range=Optional[Union[str, "V1p5LibraryGenerationMethod"]])

slots.V1p5library_generation_protocol = Slot(uri=AK_SCHEMA.V1p5library_generation_protocol, name="V1p5library_generation_protocol", curie=AK_SCHEMA.curie('V1p5library_generation_protocol'),
                   model_uri=AK_SCHEMA.V1p5library_generation_protocol, domain=None, range=Optional[str])

slots.V1p5library_generation_kit_version = Slot(uri=AK_SCHEMA.V1p5library_generation_kit_version, name="V1p5library_generation_kit_version", curie=AK_SCHEMA.curie('V1p5library_generation_kit_version'),
                   model_uri=AK_SCHEMA.V1p5library_generation_kit_version, domain=None, range=Optional[str])

slots.V1p5pcr_target = Slot(uri=AK_SCHEMA.V1p5pcr_target, name="V1p5pcr_target", curie=AK_SCHEMA.curie('V1p5pcr_target'),
                   model_uri=AK_SCHEMA.V1p5pcr_target, domain=None, range=Optional[Union[Union[dict, V1p5PCRTarget], List[Union[dict, V1p5PCRTarget]]]])

slots.V1p5complete_sequences = Slot(uri=AK_SCHEMA.V1p5complete_sequences, name="V1p5complete_sequences", curie=AK_SCHEMA.curie('V1p5complete_sequences'),
                   model_uri=AK_SCHEMA.V1p5complete_sequences, domain=None, range=Optional[Union[str, "V1p5CompleteSequences"]])

slots.V1p5physical_linkage = Slot(uri=AK_SCHEMA.V1p5physical_linkage, name="V1p5physical_linkage", curie=AK_SCHEMA.curie('V1p5physical_linkage'),
                   model_uri=AK_SCHEMA.V1p5physical_linkage, domain=None, range=Optional[Union[str, "V1p5PhysicalLinkage"]])

slots.V1p5sequencing_run_id = Slot(uri=AK_SCHEMA.V1p5sequencing_run_id, name="V1p5sequencing_run_id", curie=AK_SCHEMA.curie('V1p5sequencing_run_id'),
                   model_uri=AK_SCHEMA.V1p5sequencing_run_id, domain=None, range=Optional[str])

slots.V1p5total_reads_passing_qc_filter = Slot(uri=AK_SCHEMA.V1p5total_reads_passing_qc_filter, name="V1p5total_reads_passing_qc_filter", curie=AK_SCHEMA.curie('V1p5total_reads_passing_qc_filter'),
                   model_uri=AK_SCHEMA.V1p5total_reads_passing_qc_filter, domain=None, range=Optional[int])

slots.V1p5sequencing_platform = Slot(uri=AK_SCHEMA.V1p5sequencing_platform, name="V1p5sequencing_platform", curie=AK_SCHEMA.curie('V1p5sequencing_platform'),
                   model_uri=AK_SCHEMA.V1p5sequencing_platform, domain=None, range=Optional[str])

slots.V1p5sequencing_facility = Slot(uri=AK_SCHEMA.V1p5sequencing_facility, name="V1p5sequencing_facility", curie=AK_SCHEMA.curie('V1p5sequencing_facility'),
                   model_uri=AK_SCHEMA.V1p5sequencing_facility, domain=None, range=Optional[str])

slots.V1p5sequencing_run_date = Slot(uri=AK_SCHEMA.V1p5sequencing_run_date, name="V1p5sequencing_run_date", curie=AK_SCHEMA.curie('V1p5sequencing_run_date'),
                   model_uri=AK_SCHEMA.V1p5sequencing_run_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.V1p5sequencing_kit = Slot(uri=AK_SCHEMA.V1p5sequencing_kit, name="V1p5sequencing_kit", curie=AK_SCHEMA.curie('V1p5sequencing_kit'),
                   model_uri=AK_SCHEMA.V1p5sequencing_kit, domain=None, range=Optional[str])

slots.V1p5sequencing_files = Slot(uri=AK_SCHEMA.V1p5sequencing_files, name="V1p5sequencing_files", curie=AK_SCHEMA.curie('V1p5sequencing_files'),
                   model_uri=AK_SCHEMA.V1p5sequencing_files, domain=None, range=Optional[Union[dict, V1p5SequencingData]])

slots.V1p5sequencing_data_id = Slot(uri=AK_SCHEMA.V1p5sequencing_data_id, name="V1p5sequencing_data_id", curie=AK_SCHEMA.curie('V1p5sequencing_data_id'),
                   model_uri=AK_SCHEMA.V1p5sequencing_data_id, domain=None, range=Optional[str])

slots.V1p5file_type = Slot(uri=RDF.type, name="V1p5file_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p5file_type, domain=None, range=Optional[Union[str, "V1p5FileType"]])

slots.V1p5filename = Slot(uri=AK_SCHEMA.V1p5filename, name="V1p5filename", curie=AK_SCHEMA.curie('V1p5filename'),
                   model_uri=AK_SCHEMA.V1p5filename, domain=None, range=Optional[str])

slots.V1p5read_direction = Slot(uri=AK_SCHEMA.V1p5read_direction, name="V1p5read_direction", curie=AK_SCHEMA.curie('V1p5read_direction'),
                   model_uri=AK_SCHEMA.V1p5read_direction, domain=None, range=Optional[Union[str, "V1p5ReadDirection"]])

slots.V1p5read_length = Slot(uri=AK_SCHEMA.V1p5read_length, name="V1p5read_length", curie=AK_SCHEMA.curie('V1p5read_length'),
                   model_uri=AK_SCHEMA.V1p5read_length, domain=None, range=Optional[int])

slots.V1p5paired_filename = Slot(uri=AK_SCHEMA.V1p5paired_filename, name="V1p5paired_filename", curie=AK_SCHEMA.curie('V1p5paired_filename'),
                   model_uri=AK_SCHEMA.V1p5paired_filename, domain=None, range=Optional[str])

slots.V1p5paired_read_direction = Slot(uri=AK_SCHEMA.V1p5paired_read_direction, name="V1p5paired_read_direction", curie=AK_SCHEMA.curie('V1p5paired_read_direction'),
                   model_uri=AK_SCHEMA.V1p5paired_read_direction, domain=None, range=Optional[Union[str, "V1p5PairedReadDirection"]])

slots.V1p5paired_read_length = Slot(uri=AK_SCHEMA.V1p5paired_read_length, name="V1p5paired_read_length", curie=AK_SCHEMA.curie('V1p5paired_read_length'),
                   model_uri=AK_SCHEMA.V1p5paired_read_length, domain=None, range=Optional[int])

slots.V1p5index_filename = Slot(uri=AK_SCHEMA.V1p5index_filename, name="V1p5index_filename", curie=AK_SCHEMA.curie('V1p5index_filename'),
                   model_uri=AK_SCHEMA.V1p5index_filename, domain=None, range=Optional[str])

slots.V1p5index_length = Slot(uri=AK_SCHEMA.V1p5index_length, name="V1p5index_length", curie=AK_SCHEMA.curie('V1p5index_length'),
                   model_uri=AK_SCHEMA.V1p5index_length, domain=None, range=Optional[int])

slots.V1p5data_processing_id = Slot(uri=AK_SCHEMA.V1p5data_processing_id, name="V1p5data_processing_id", curie=AK_SCHEMA.curie('V1p5data_processing_id'),
                   model_uri=AK_SCHEMA.V1p5data_processing_id, domain=None, range=Optional[str])

slots.V1p5primary_annotation = Slot(uri=AK_SCHEMA.V1p5primary_annotation, name="V1p5primary_annotation", curie=AK_SCHEMA.curie('V1p5primary_annotation'),
                   model_uri=AK_SCHEMA.V1p5primary_annotation, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5software_versions = Slot(uri=AK_SCHEMA.V1p5software_versions, name="V1p5software_versions", curie=AK_SCHEMA.curie('V1p5software_versions'),
                   model_uri=AK_SCHEMA.V1p5software_versions, domain=None, range=Optional[str])

slots.V1p5paired_reads_assembly = Slot(uri=AK_SCHEMA.V1p5paired_reads_assembly, name="V1p5paired_reads_assembly", curie=AK_SCHEMA.curie('V1p5paired_reads_assembly'),
                   model_uri=AK_SCHEMA.V1p5paired_reads_assembly, domain=None, range=Optional[str])

slots.V1p5quality_thresholds = Slot(uri=AK_SCHEMA.V1p5quality_thresholds, name="V1p5quality_thresholds", curie=AK_SCHEMA.curie('V1p5quality_thresholds'),
                   model_uri=AK_SCHEMA.V1p5quality_thresholds, domain=None, range=Optional[str])

slots.V1p5primer_match_cutoffs = Slot(uri=AK_SCHEMA.V1p5primer_match_cutoffs, name="V1p5primer_match_cutoffs", curie=AK_SCHEMA.curie('V1p5primer_match_cutoffs'),
                   model_uri=AK_SCHEMA.V1p5primer_match_cutoffs, domain=None, range=Optional[str])

slots.V1p5collapsing_method = Slot(uri=AK_SCHEMA.V1p5collapsing_method, name="V1p5collapsing_method", curie=AK_SCHEMA.curie('V1p5collapsing_method'),
                   model_uri=AK_SCHEMA.V1p5collapsing_method, domain=None, range=Optional[str])

slots.V1p5data_processing_protocols = Slot(uri=AK_SCHEMA.V1p5data_processing_protocols, name="V1p5data_processing_protocols", curie=AK_SCHEMA.curie('V1p5data_processing_protocols'),
                   model_uri=AK_SCHEMA.V1p5data_processing_protocols, domain=None, range=Optional[str])

slots.V1p5data_processing_files = Slot(uri=AK_SCHEMA.V1p5data_processing_files, name="V1p5data_processing_files", curie=AK_SCHEMA.curie('V1p5data_processing_files'),
                   model_uri=AK_SCHEMA.V1p5data_processing_files, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p5germline_database = Slot(uri=AK_SCHEMA.V1p5germline_database, name="V1p5germline_database", curie=AK_SCHEMA.curie('V1p5germline_database'),
                   model_uri=AK_SCHEMA.V1p5germline_database, domain=None, range=Optional[str])

slots.V1p5analysis_provenance_id = Slot(uri=AK_SCHEMA.V1p5analysis_provenance_id, name="V1p5analysis_provenance_id", curie=AK_SCHEMA.curie('V1p5analysis_provenance_id'),
                   model_uri=AK_SCHEMA.V1p5analysis_provenance_id, domain=None, range=Optional[str])

slots.V1p5repertoire_id = Slot(uri=AK_SCHEMA.V1p5repertoire_id, name="V1p5repertoire_id", curie=AK_SCHEMA.curie('V1p5repertoire_id'),
                   model_uri=AK_SCHEMA.V1p5repertoire_id, domain=None, range=Optional[str])

slots.V1p5repertoire_name = Slot(uri=AK_SCHEMA.V1p5repertoire_name, name="V1p5repertoire_name", curie=AK_SCHEMA.curie('V1p5repertoire_name'),
                   model_uri=AK_SCHEMA.V1p5repertoire_name, domain=None, range=Optional[str])

slots.V1p5repertoire_description = Slot(uri=AK_SCHEMA.V1p5repertoire_description, name="V1p5repertoire_description", curie=AK_SCHEMA.curie('V1p5repertoire_description'),
                   model_uri=AK_SCHEMA.V1p5repertoire_description, domain=None, range=Optional[str])

slots.V1p5study = Slot(uri=AK_SCHEMA.V1p5study, name="V1p5study", curie=AK_SCHEMA.curie('V1p5study'),
                   model_uri=AK_SCHEMA.V1p5study, domain=None, range=Optional[Union[dict, V1p5Study]])

slots.V1p5subject = Slot(uri=AK_SCHEMA.V1p5subject, name="V1p5subject", curie=AK_SCHEMA.curie('V1p5subject'),
                   model_uri=AK_SCHEMA.V1p5subject, domain=None, range=Optional[Union[dict, V1p5Subject]])

slots.V1p5sample = Slot(uri=AK_SCHEMA.V1p5sample, name="V1p5sample", curie=AK_SCHEMA.curie('V1p5sample'),
                   model_uri=AK_SCHEMA.V1p5sample, domain=None, range=Optional[Union[Union[dict, V1p5SampleProcessing], List[Union[dict, V1p5SampleProcessing]]]])

slots.V1p5data_processing = Slot(uri=AK_SCHEMA.V1p5data_processing, name="V1p5data_processing", curie=AK_SCHEMA.curie('V1p5data_processing'),
                   model_uri=AK_SCHEMA.V1p5data_processing, domain=None, range=Optional[Union[Union[dict, V1p5DataProcessing], List[Union[dict, V1p5DataProcessing]]]])

slots.V1p5repertoire_group_id = Slot(uri=AK_SCHEMA.V1p5repertoire_group_id, name="V1p5repertoire_group_id", curie=AK_SCHEMA.curie('V1p5repertoire_group_id'),
                   model_uri=AK_SCHEMA.V1p5repertoire_group_id, domain=None, range=Optional[str])

slots.V1p5repertoire_group_name = Slot(uri=AK_SCHEMA.V1p5repertoire_group_name, name="V1p5repertoire_group_name", curie=AK_SCHEMA.curie('V1p5repertoire_group_name'),
                   model_uri=AK_SCHEMA.V1p5repertoire_group_name, domain=None, range=Optional[str])

slots.V1p5repertoire_group_description = Slot(uri=AK_SCHEMA.V1p5repertoire_group_description, name="V1p5repertoire_group_description", curie=AK_SCHEMA.curie('V1p5repertoire_group_description'),
                   model_uri=AK_SCHEMA.V1p5repertoire_group_description, domain=None, range=Optional[str])

slots.V1p5repertoires = Slot(uri=AK_SCHEMA.V1p5repertoires, name="V1p5repertoires", curie=AK_SCHEMA.curie('V1p5repertoires'),
                   model_uri=AK_SCHEMA.V1p5repertoires, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p5segment = Slot(uri=AK_SCHEMA.V1p5segment, name="V1p5segment", curie=AK_SCHEMA.curie('V1p5segment'),
                   model_uri=AK_SCHEMA.V1p5segment, domain=None, range=Optional[str])

slots.V1p5rev_comp = Slot(uri=AK_SCHEMA.V1p5rev_comp, name="V1p5rev_comp", curie=AK_SCHEMA.curie('V1p5rev_comp'),
                   model_uri=AK_SCHEMA.V1p5rev_comp, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5call = Slot(uri=AK_SCHEMA.V1p5call, name="V1p5call", curie=AK_SCHEMA.curie('V1p5call'),
                   model_uri=AK_SCHEMA.V1p5call, domain=None, range=Optional[str])

slots.V1p5score = Slot(uri=AK_SCHEMA.V1p5score, name="V1p5score", curie=AK_SCHEMA.curie('V1p5score'),
                   model_uri=AK_SCHEMA.V1p5score, domain=None, range=Optional[float])

slots.V1p5identity = Slot(uri=AK_SCHEMA.V1p5identity, name="V1p5identity", curie=AK_SCHEMA.curie('V1p5identity'),
                   model_uri=AK_SCHEMA.V1p5identity, domain=None, range=Optional[float])

slots.V1p5support = Slot(uri=AK_SCHEMA.V1p5support, name="V1p5support", curie=AK_SCHEMA.curie('V1p5support'),
                   model_uri=AK_SCHEMA.V1p5support, domain=None, range=Optional[float])

slots.V1p5cigar = Slot(uri=AK_SCHEMA.V1p5cigar, name="V1p5cigar", curie=AK_SCHEMA.curie('V1p5cigar'),
                   model_uri=AK_SCHEMA.V1p5cigar, domain=None, range=Optional[str])

slots.V1p5germline_start = Slot(uri=AK_SCHEMA.V1p5germline_start, name="V1p5germline_start", curie=AK_SCHEMA.curie('V1p5germline_start'),
                   model_uri=AK_SCHEMA.V1p5germline_start, domain=None, range=Optional[int])

slots.V1p5germline_end = Slot(uri=AK_SCHEMA.V1p5germline_end, name="V1p5germline_end", curie=AK_SCHEMA.curie('V1p5germline_end'),
                   model_uri=AK_SCHEMA.V1p5germline_end, domain=None, range=Optional[int])

slots.V1p5rank = Slot(uri=AK_SCHEMA.V1p5rank, name="V1p5rank", curie=AK_SCHEMA.curie('V1p5rank'),
                   model_uri=AK_SCHEMA.V1p5rank, domain=None, range=Optional[int])

slots.V1p5quality = Slot(uri=AK_SCHEMA.V1p5quality, name="V1p5quality", curie=AK_SCHEMA.curie('V1p5quality'),
                   model_uri=AK_SCHEMA.V1p5quality, domain=None, range=Optional[str])

slots.V1p5sequence_aa = Slot(uri=AK_SCHEMA.V1p5sequence_aa, name="V1p5sequence_aa", curie=AK_SCHEMA.curie('V1p5sequence_aa'),
                   model_uri=AK_SCHEMA.V1p5sequence_aa, domain=None, range=Optional[str])

slots.V1p5productive = Slot(uri=AK_SCHEMA.V1p5productive, name="V1p5productive", curie=AK_SCHEMA.curie('V1p5productive'),
                   model_uri=AK_SCHEMA.V1p5productive, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5vj_in_frame = Slot(uri=AK_SCHEMA.V1p5vj_in_frame, name="V1p5vj_in_frame", curie=AK_SCHEMA.curie('V1p5vj_in_frame'),
                   model_uri=AK_SCHEMA.V1p5vj_in_frame, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5stop_codon = Slot(uri=AK_SCHEMA.V1p5stop_codon, name="V1p5stop_codon", curie=AK_SCHEMA.curie('V1p5stop_codon'),
                   model_uri=AK_SCHEMA.V1p5stop_codon, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5complete_vdj = Slot(uri=AK_SCHEMA.V1p5complete_vdj, name="V1p5complete_vdj", curie=AK_SCHEMA.curie('V1p5complete_vdj'),
                   model_uri=AK_SCHEMA.V1p5complete_vdj, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5v_call = Slot(uri=AK_SCHEMA.V1p5v_call, name="V1p5v_call", curie=AK_SCHEMA.curie('V1p5v_call'),
                   model_uri=AK_SCHEMA.V1p5v_call, domain=None, range=Optional[str])

slots.V1p5d_call = Slot(uri=AK_SCHEMA.V1p5d_call, name="V1p5d_call", curie=AK_SCHEMA.curie('V1p5d_call'),
                   model_uri=AK_SCHEMA.V1p5d_call, domain=None, range=Optional[str])

slots.V1p5d2_call = Slot(uri=AK_SCHEMA.V1p5d2_call, name="V1p5d2_call", curie=AK_SCHEMA.curie('V1p5d2_call'),
                   model_uri=AK_SCHEMA.V1p5d2_call, domain=None, range=Optional[str])

slots.V1p5j_call = Slot(uri=AK_SCHEMA.V1p5j_call, name="V1p5j_call", curie=AK_SCHEMA.curie('V1p5j_call'),
                   model_uri=AK_SCHEMA.V1p5j_call, domain=None, range=Optional[str])

slots.V1p5c_call = Slot(uri=AK_SCHEMA.V1p5c_call, name="V1p5c_call", curie=AK_SCHEMA.curie('V1p5c_call'),
                   model_uri=AK_SCHEMA.V1p5c_call, domain=None, range=Optional[str])

slots.V1p5sequence_alignment = Slot(uri=AK_SCHEMA.V1p5sequence_alignment, name="V1p5sequence_alignment", curie=AK_SCHEMA.curie('V1p5sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p5sequence_alignment, domain=None, range=Optional[str])

slots.V1p5quality_alignment = Slot(uri=AK_SCHEMA.V1p5quality_alignment, name="V1p5quality_alignment", curie=AK_SCHEMA.curie('V1p5quality_alignment'),
                   model_uri=AK_SCHEMA.V1p5quality_alignment, domain=None, range=Optional[str])

slots.V1p5sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p5sequence_alignment_aa, name="V1p5sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p5sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p5germline_alignment = Slot(uri=AK_SCHEMA.V1p5germline_alignment, name="V1p5germline_alignment", curie=AK_SCHEMA.curie('V1p5germline_alignment'),
                   model_uri=AK_SCHEMA.V1p5germline_alignment, domain=None, range=Optional[str])

slots.V1p5germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p5germline_alignment_aa, name="V1p5germline_alignment_aa", curie=AK_SCHEMA.curie('V1p5germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p5junction = Slot(uri=AK_SCHEMA.V1p5junction, name="V1p5junction", curie=AK_SCHEMA.curie('V1p5junction'),
                   model_uri=AK_SCHEMA.V1p5junction, domain=None, range=Optional[str])

slots.V1p5junction_aa = Slot(uri=AK_SCHEMA.V1p5junction_aa, name="V1p5junction_aa", curie=AK_SCHEMA.curie('V1p5junction_aa'),
                   model_uri=AK_SCHEMA.V1p5junction_aa, domain=None, range=Optional[str])

slots.V1p5np1 = Slot(uri=AK_SCHEMA.V1p5np1, name="V1p5np1", curie=AK_SCHEMA.curie('V1p5np1'),
                   model_uri=AK_SCHEMA.V1p5np1, domain=None, range=Optional[str])

slots.V1p5np1_aa = Slot(uri=AK_SCHEMA.V1p5np1_aa, name="V1p5np1_aa", curie=AK_SCHEMA.curie('V1p5np1_aa'),
                   model_uri=AK_SCHEMA.V1p5np1_aa, domain=None, range=Optional[str])

slots.V1p5np2 = Slot(uri=AK_SCHEMA.V1p5np2, name="V1p5np2", curie=AK_SCHEMA.curie('V1p5np2'),
                   model_uri=AK_SCHEMA.V1p5np2, domain=None, range=Optional[str])

slots.V1p5np2_aa = Slot(uri=AK_SCHEMA.V1p5np2_aa, name="V1p5np2_aa", curie=AK_SCHEMA.curie('V1p5np2_aa'),
                   model_uri=AK_SCHEMA.V1p5np2_aa, domain=None, range=Optional[str])

slots.V1p5np3 = Slot(uri=AK_SCHEMA.V1p5np3, name="V1p5np3", curie=AK_SCHEMA.curie('V1p5np3'),
                   model_uri=AK_SCHEMA.V1p5np3, domain=None, range=Optional[str])

slots.V1p5np3_aa = Slot(uri=AK_SCHEMA.V1p5np3_aa, name="V1p5np3_aa", curie=AK_SCHEMA.curie('V1p5np3_aa'),
                   model_uri=AK_SCHEMA.V1p5np3_aa, domain=None, range=Optional[str])

slots.V1p5cdr1 = Slot(uri=AK_SCHEMA.V1p5cdr1, name="V1p5cdr1", curie=AK_SCHEMA.curie('V1p5cdr1'),
                   model_uri=AK_SCHEMA.V1p5cdr1, domain=None, range=Optional[str])

slots.V1p5cdr1_aa = Slot(uri=AK_SCHEMA.V1p5cdr1_aa, name="V1p5cdr1_aa", curie=AK_SCHEMA.curie('V1p5cdr1_aa'),
                   model_uri=AK_SCHEMA.V1p5cdr1_aa, domain=None, range=Optional[str])

slots.V1p5cdr2 = Slot(uri=AK_SCHEMA.V1p5cdr2, name="V1p5cdr2", curie=AK_SCHEMA.curie('V1p5cdr2'),
                   model_uri=AK_SCHEMA.V1p5cdr2, domain=None, range=Optional[str])

slots.V1p5cdr2_aa = Slot(uri=AK_SCHEMA.V1p5cdr2_aa, name="V1p5cdr2_aa", curie=AK_SCHEMA.curie('V1p5cdr2_aa'),
                   model_uri=AK_SCHEMA.V1p5cdr2_aa, domain=None, range=Optional[str])

slots.V1p5cdr3 = Slot(uri=AK_SCHEMA.V1p5cdr3, name="V1p5cdr3", curie=AK_SCHEMA.curie('V1p5cdr3'),
                   model_uri=AK_SCHEMA.V1p5cdr3, domain=None, range=Optional[str])

slots.V1p5cdr3_aa = Slot(uri=AK_SCHEMA.V1p5cdr3_aa, name="V1p5cdr3_aa", curie=AK_SCHEMA.curie('V1p5cdr3_aa'),
                   model_uri=AK_SCHEMA.V1p5cdr3_aa, domain=None, range=Optional[str])

slots.V1p5fwr1 = Slot(uri=AK_SCHEMA.V1p5fwr1, name="V1p5fwr1", curie=AK_SCHEMA.curie('V1p5fwr1'),
                   model_uri=AK_SCHEMA.V1p5fwr1, domain=None, range=Optional[str])

slots.V1p5fwr1_aa = Slot(uri=AK_SCHEMA.V1p5fwr1_aa, name="V1p5fwr1_aa", curie=AK_SCHEMA.curie('V1p5fwr1_aa'),
                   model_uri=AK_SCHEMA.V1p5fwr1_aa, domain=None, range=Optional[str])

slots.V1p5fwr2 = Slot(uri=AK_SCHEMA.V1p5fwr2, name="V1p5fwr2", curie=AK_SCHEMA.curie('V1p5fwr2'),
                   model_uri=AK_SCHEMA.V1p5fwr2, domain=None, range=Optional[str])

slots.V1p5fwr2_aa = Slot(uri=AK_SCHEMA.V1p5fwr2_aa, name="V1p5fwr2_aa", curie=AK_SCHEMA.curie('V1p5fwr2_aa'),
                   model_uri=AK_SCHEMA.V1p5fwr2_aa, domain=None, range=Optional[str])

slots.V1p5fwr3 = Slot(uri=AK_SCHEMA.V1p5fwr3, name="V1p5fwr3", curie=AK_SCHEMA.curie('V1p5fwr3'),
                   model_uri=AK_SCHEMA.V1p5fwr3, domain=None, range=Optional[str])

slots.V1p5fwr3_aa = Slot(uri=AK_SCHEMA.V1p5fwr3_aa, name="V1p5fwr3_aa", curie=AK_SCHEMA.curie('V1p5fwr3_aa'),
                   model_uri=AK_SCHEMA.V1p5fwr3_aa, domain=None, range=Optional[str])

slots.V1p5fwr4 = Slot(uri=AK_SCHEMA.V1p5fwr4, name="V1p5fwr4", curie=AK_SCHEMA.curie('V1p5fwr4'),
                   model_uri=AK_SCHEMA.V1p5fwr4, domain=None, range=Optional[str])

slots.V1p5fwr4_aa = Slot(uri=AK_SCHEMA.V1p5fwr4_aa, name="V1p5fwr4_aa", curie=AK_SCHEMA.curie('V1p5fwr4_aa'),
                   model_uri=AK_SCHEMA.V1p5fwr4_aa, domain=None, range=Optional[str])

slots.V1p5v_score = Slot(uri=AK_SCHEMA.V1p5v_score, name="V1p5v_score", curie=AK_SCHEMA.curie('V1p5v_score'),
                   model_uri=AK_SCHEMA.V1p5v_score, domain=None, range=Optional[float])

slots.V1p5v_identity = Slot(uri=AK_SCHEMA.V1p5v_identity, name="V1p5v_identity", curie=AK_SCHEMA.curie('V1p5v_identity'),
                   model_uri=AK_SCHEMA.V1p5v_identity, domain=None, range=Optional[float])

slots.V1p5v_support = Slot(uri=AK_SCHEMA.V1p5v_support, name="V1p5v_support", curie=AK_SCHEMA.curie('V1p5v_support'),
                   model_uri=AK_SCHEMA.V1p5v_support, domain=None, range=Optional[float])

slots.V1p5v_cigar = Slot(uri=AK_SCHEMA.V1p5v_cigar, name="V1p5v_cigar", curie=AK_SCHEMA.curie('V1p5v_cigar'),
                   model_uri=AK_SCHEMA.V1p5v_cigar, domain=None, range=Optional[str])

slots.V1p5d_score = Slot(uri=AK_SCHEMA.V1p5d_score, name="V1p5d_score", curie=AK_SCHEMA.curie('V1p5d_score'),
                   model_uri=AK_SCHEMA.V1p5d_score, domain=None, range=Optional[float])

slots.V1p5d_identity = Slot(uri=AK_SCHEMA.V1p5d_identity, name="V1p5d_identity", curie=AK_SCHEMA.curie('V1p5d_identity'),
                   model_uri=AK_SCHEMA.V1p5d_identity, domain=None, range=Optional[float])

slots.V1p5d_support = Slot(uri=AK_SCHEMA.V1p5d_support, name="V1p5d_support", curie=AK_SCHEMA.curie('V1p5d_support'),
                   model_uri=AK_SCHEMA.V1p5d_support, domain=None, range=Optional[float])

slots.V1p5d_cigar = Slot(uri=AK_SCHEMA.V1p5d_cigar, name="V1p5d_cigar", curie=AK_SCHEMA.curie('V1p5d_cigar'),
                   model_uri=AK_SCHEMA.V1p5d_cigar, domain=None, range=Optional[str])

slots.V1p5d2_score = Slot(uri=AK_SCHEMA.V1p5d2_score, name="V1p5d2_score", curie=AK_SCHEMA.curie('V1p5d2_score'),
                   model_uri=AK_SCHEMA.V1p5d2_score, domain=None, range=Optional[float])

slots.V1p5d2_identity = Slot(uri=AK_SCHEMA.V1p5d2_identity, name="V1p5d2_identity", curie=AK_SCHEMA.curie('V1p5d2_identity'),
                   model_uri=AK_SCHEMA.V1p5d2_identity, domain=None, range=Optional[float])

slots.V1p5d2_support = Slot(uri=AK_SCHEMA.V1p5d2_support, name="V1p5d2_support", curie=AK_SCHEMA.curie('V1p5d2_support'),
                   model_uri=AK_SCHEMA.V1p5d2_support, domain=None, range=Optional[float])

slots.V1p5d2_cigar = Slot(uri=AK_SCHEMA.V1p5d2_cigar, name="V1p5d2_cigar", curie=AK_SCHEMA.curie('V1p5d2_cigar'),
                   model_uri=AK_SCHEMA.V1p5d2_cigar, domain=None, range=Optional[str])

slots.V1p5j_score = Slot(uri=AK_SCHEMA.V1p5j_score, name="V1p5j_score", curie=AK_SCHEMA.curie('V1p5j_score'),
                   model_uri=AK_SCHEMA.V1p5j_score, domain=None, range=Optional[float])

slots.V1p5j_identity = Slot(uri=AK_SCHEMA.V1p5j_identity, name="V1p5j_identity", curie=AK_SCHEMA.curie('V1p5j_identity'),
                   model_uri=AK_SCHEMA.V1p5j_identity, domain=None, range=Optional[float])

slots.V1p5j_support = Slot(uri=AK_SCHEMA.V1p5j_support, name="V1p5j_support", curie=AK_SCHEMA.curie('V1p5j_support'),
                   model_uri=AK_SCHEMA.V1p5j_support, domain=None, range=Optional[float])

slots.V1p5j_cigar = Slot(uri=AK_SCHEMA.V1p5j_cigar, name="V1p5j_cigar", curie=AK_SCHEMA.curie('V1p5j_cigar'),
                   model_uri=AK_SCHEMA.V1p5j_cigar, domain=None, range=Optional[str])

slots.V1p5c_score = Slot(uri=AK_SCHEMA.V1p5c_score, name="V1p5c_score", curie=AK_SCHEMA.curie('V1p5c_score'),
                   model_uri=AK_SCHEMA.V1p5c_score, domain=None, range=Optional[float])

slots.V1p5c_identity = Slot(uri=AK_SCHEMA.V1p5c_identity, name="V1p5c_identity", curie=AK_SCHEMA.curie('V1p5c_identity'),
                   model_uri=AK_SCHEMA.V1p5c_identity, domain=None, range=Optional[float])

slots.V1p5c_support = Slot(uri=AK_SCHEMA.V1p5c_support, name="V1p5c_support", curie=AK_SCHEMA.curie('V1p5c_support'),
                   model_uri=AK_SCHEMA.V1p5c_support, domain=None, range=Optional[float])

slots.V1p5c_cigar = Slot(uri=AK_SCHEMA.V1p5c_cigar, name="V1p5c_cigar", curie=AK_SCHEMA.curie('V1p5c_cigar'),
                   model_uri=AK_SCHEMA.V1p5c_cigar, domain=None, range=Optional[str])

slots.V1p5v_sequence_start = Slot(uri=AK_SCHEMA.V1p5v_sequence_start, name="V1p5v_sequence_start", curie=AK_SCHEMA.curie('V1p5v_sequence_start'),
                   model_uri=AK_SCHEMA.V1p5v_sequence_start, domain=None, range=Optional[int])

slots.V1p5v_sequence_end = Slot(uri=AK_SCHEMA.V1p5v_sequence_end, name="V1p5v_sequence_end", curie=AK_SCHEMA.curie('V1p5v_sequence_end'),
                   model_uri=AK_SCHEMA.V1p5v_sequence_end, domain=None, range=Optional[int])

slots.V1p5v_germline_start = Slot(uri=AK_SCHEMA.V1p5v_germline_start, name="V1p5v_germline_start", curie=AK_SCHEMA.curie('V1p5v_germline_start'),
                   model_uri=AK_SCHEMA.V1p5v_germline_start, domain=None, range=Optional[int])

slots.V1p5v_germline_end = Slot(uri=AK_SCHEMA.V1p5v_germline_end, name="V1p5v_germline_end", curie=AK_SCHEMA.curie('V1p5v_germline_end'),
                   model_uri=AK_SCHEMA.V1p5v_germline_end, domain=None, range=Optional[int])

slots.V1p5v_alignment_start = Slot(uri=AK_SCHEMA.V1p5v_alignment_start, name="V1p5v_alignment_start", curie=AK_SCHEMA.curie('V1p5v_alignment_start'),
                   model_uri=AK_SCHEMA.V1p5v_alignment_start, domain=None, range=Optional[int])

slots.V1p5v_alignment_end = Slot(uri=AK_SCHEMA.V1p5v_alignment_end, name="V1p5v_alignment_end", curie=AK_SCHEMA.curie('V1p5v_alignment_end'),
                   model_uri=AK_SCHEMA.V1p5v_alignment_end, domain=None, range=Optional[int])

slots.V1p5d_sequence_start = Slot(uri=AK_SCHEMA.V1p5d_sequence_start, name="V1p5d_sequence_start", curie=AK_SCHEMA.curie('V1p5d_sequence_start'),
                   model_uri=AK_SCHEMA.V1p5d_sequence_start, domain=None, range=Optional[int])

slots.V1p5d_sequence_end = Slot(uri=AK_SCHEMA.V1p5d_sequence_end, name="V1p5d_sequence_end", curie=AK_SCHEMA.curie('V1p5d_sequence_end'),
                   model_uri=AK_SCHEMA.V1p5d_sequence_end, domain=None, range=Optional[int])

slots.V1p5d_germline_start = Slot(uri=AK_SCHEMA.V1p5d_germline_start, name="V1p5d_germline_start", curie=AK_SCHEMA.curie('V1p5d_germline_start'),
                   model_uri=AK_SCHEMA.V1p5d_germline_start, domain=None, range=Optional[int])

slots.V1p5d_germline_end = Slot(uri=AK_SCHEMA.V1p5d_germline_end, name="V1p5d_germline_end", curie=AK_SCHEMA.curie('V1p5d_germline_end'),
                   model_uri=AK_SCHEMA.V1p5d_germline_end, domain=None, range=Optional[int])

slots.V1p5d_alignment_start = Slot(uri=AK_SCHEMA.V1p5d_alignment_start, name="V1p5d_alignment_start", curie=AK_SCHEMA.curie('V1p5d_alignment_start'),
                   model_uri=AK_SCHEMA.V1p5d_alignment_start, domain=None, range=Optional[int])

slots.V1p5d_alignment_end = Slot(uri=AK_SCHEMA.V1p5d_alignment_end, name="V1p5d_alignment_end", curie=AK_SCHEMA.curie('V1p5d_alignment_end'),
                   model_uri=AK_SCHEMA.V1p5d_alignment_end, domain=None, range=Optional[int])

slots.V1p5d2_sequence_start = Slot(uri=AK_SCHEMA.V1p5d2_sequence_start, name="V1p5d2_sequence_start", curie=AK_SCHEMA.curie('V1p5d2_sequence_start'),
                   model_uri=AK_SCHEMA.V1p5d2_sequence_start, domain=None, range=Optional[int])

slots.V1p5d2_sequence_end = Slot(uri=AK_SCHEMA.V1p5d2_sequence_end, name="V1p5d2_sequence_end", curie=AK_SCHEMA.curie('V1p5d2_sequence_end'),
                   model_uri=AK_SCHEMA.V1p5d2_sequence_end, domain=None, range=Optional[int])

slots.V1p5d2_germline_start = Slot(uri=AK_SCHEMA.V1p5d2_germline_start, name="V1p5d2_germline_start", curie=AK_SCHEMA.curie('V1p5d2_germline_start'),
                   model_uri=AK_SCHEMA.V1p5d2_germline_start, domain=None, range=Optional[int])

slots.V1p5d2_germline_end = Slot(uri=AK_SCHEMA.V1p5d2_germline_end, name="V1p5d2_germline_end", curie=AK_SCHEMA.curie('V1p5d2_germline_end'),
                   model_uri=AK_SCHEMA.V1p5d2_germline_end, domain=None, range=Optional[int])

slots.V1p5d2_alignment_start = Slot(uri=AK_SCHEMA.V1p5d2_alignment_start, name="V1p5d2_alignment_start", curie=AK_SCHEMA.curie('V1p5d2_alignment_start'),
                   model_uri=AK_SCHEMA.V1p5d2_alignment_start, domain=None, range=Optional[int])

slots.V1p5d2_alignment_end = Slot(uri=AK_SCHEMA.V1p5d2_alignment_end, name="V1p5d2_alignment_end", curie=AK_SCHEMA.curie('V1p5d2_alignment_end'),
                   model_uri=AK_SCHEMA.V1p5d2_alignment_end, domain=None, range=Optional[int])

slots.V1p5j_sequence_start = Slot(uri=AK_SCHEMA.V1p5j_sequence_start, name="V1p5j_sequence_start", curie=AK_SCHEMA.curie('V1p5j_sequence_start'),
                   model_uri=AK_SCHEMA.V1p5j_sequence_start, domain=None, range=Optional[int])

slots.V1p5j_sequence_end = Slot(uri=AK_SCHEMA.V1p5j_sequence_end, name="V1p5j_sequence_end", curie=AK_SCHEMA.curie('V1p5j_sequence_end'),
                   model_uri=AK_SCHEMA.V1p5j_sequence_end, domain=None, range=Optional[int])

slots.V1p5j_germline_start = Slot(uri=AK_SCHEMA.V1p5j_germline_start, name="V1p5j_germline_start", curie=AK_SCHEMA.curie('V1p5j_germline_start'),
                   model_uri=AK_SCHEMA.V1p5j_germline_start, domain=None, range=Optional[int])

slots.V1p5j_germline_end = Slot(uri=AK_SCHEMA.V1p5j_germline_end, name="V1p5j_germline_end", curie=AK_SCHEMA.curie('V1p5j_germline_end'),
                   model_uri=AK_SCHEMA.V1p5j_germline_end, domain=None, range=Optional[int])

slots.V1p5j_alignment_start = Slot(uri=AK_SCHEMA.V1p5j_alignment_start, name="V1p5j_alignment_start", curie=AK_SCHEMA.curie('V1p5j_alignment_start'),
                   model_uri=AK_SCHEMA.V1p5j_alignment_start, domain=None, range=Optional[int])

slots.V1p5j_alignment_end = Slot(uri=AK_SCHEMA.V1p5j_alignment_end, name="V1p5j_alignment_end", curie=AK_SCHEMA.curie('V1p5j_alignment_end'),
                   model_uri=AK_SCHEMA.V1p5j_alignment_end, domain=None, range=Optional[int])

slots.V1p5c_sequence_start = Slot(uri=AK_SCHEMA.V1p5c_sequence_start, name="V1p5c_sequence_start", curie=AK_SCHEMA.curie('V1p5c_sequence_start'),
                   model_uri=AK_SCHEMA.V1p5c_sequence_start, domain=None, range=Optional[int])

slots.V1p5c_sequence_end = Slot(uri=AK_SCHEMA.V1p5c_sequence_end, name="V1p5c_sequence_end", curie=AK_SCHEMA.curie('V1p5c_sequence_end'),
                   model_uri=AK_SCHEMA.V1p5c_sequence_end, domain=None, range=Optional[int])

slots.V1p5c_germline_start = Slot(uri=AK_SCHEMA.V1p5c_germline_start, name="V1p5c_germline_start", curie=AK_SCHEMA.curie('V1p5c_germline_start'),
                   model_uri=AK_SCHEMA.V1p5c_germline_start, domain=None, range=Optional[int])

slots.V1p5c_germline_end = Slot(uri=AK_SCHEMA.V1p5c_germline_end, name="V1p5c_germline_end", curie=AK_SCHEMA.curie('V1p5c_germline_end'),
                   model_uri=AK_SCHEMA.V1p5c_germline_end, domain=None, range=Optional[int])

slots.V1p5c_alignment_start = Slot(uri=AK_SCHEMA.V1p5c_alignment_start, name="V1p5c_alignment_start", curie=AK_SCHEMA.curie('V1p5c_alignment_start'),
                   model_uri=AK_SCHEMA.V1p5c_alignment_start, domain=None, range=Optional[int])

slots.V1p5c_alignment_end = Slot(uri=AK_SCHEMA.V1p5c_alignment_end, name="V1p5c_alignment_end", curie=AK_SCHEMA.curie('V1p5c_alignment_end'),
                   model_uri=AK_SCHEMA.V1p5c_alignment_end, domain=None, range=Optional[int])

slots.V1p5cdr3_end = Slot(uri=AK_SCHEMA.V1p5cdr3_end, name="V1p5cdr3_end", curie=AK_SCHEMA.curie('V1p5cdr3_end'),
                   model_uri=AK_SCHEMA.V1p5cdr3_end, domain=None, range=Optional[int])

slots.V1p5fwr4_start = Slot(uri=AK_SCHEMA.V1p5fwr4_start, name="V1p5fwr4_start", curie=AK_SCHEMA.curie('V1p5fwr4_start'),
                   model_uri=AK_SCHEMA.V1p5fwr4_start, domain=None, range=Optional[int])

slots.V1p5fwr4_end = Slot(uri=AK_SCHEMA.V1p5fwr4_end, name="V1p5fwr4_end", curie=AK_SCHEMA.curie('V1p5fwr4_end'),
                   model_uri=AK_SCHEMA.V1p5fwr4_end, domain=None, range=Optional[int])

slots.V1p5v_sequence_alignment = Slot(uri=AK_SCHEMA.V1p5v_sequence_alignment, name="V1p5v_sequence_alignment", curie=AK_SCHEMA.curie('V1p5v_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p5v_sequence_alignment, domain=None, range=Optional[str])

slots.V1p5v_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p5v_sequence_alignment_aa, name="V1p5v_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p5v_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5v_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p5d_sequence_alignment = Slot(uri=AK_SCHEMA.V1p5d_sequence_alignment, name="V1p5d_sequence_alignment", curie=AK_SCHEMA.curie('V1p5d_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p5d_sequence_alignment, domain=None, range=Optional[str])

slots.V1p5d_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p5d_sequence_alignment_aa, name="V1p5d_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p5d_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5d_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p5d2_sequence_alignment = Slot(uri=AK_SCHEMA.V1p5d2_sequence_alignment, name="V1p5d2_sequence_alignment", curie=AK_SCHEMA.curie('V1p5d2_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p5d2_sequence_alignment, domain=None, range=Optional[str])

slots.V1p5d2_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p5d2_sequence_alignment_aa, name="V1p5d2_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p5d2_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5d2_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p5j_sequence_alignment = Slot(uri=AK_SCHEMA.V1p5j_sequence_alignment, name="V1p5j_sequence_alignment", curie=AK_SCHEMA.curie('V1p5j_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p5j_sequence_alignment, domain=None, range=Optional[str])

slots.V1p5j_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p5j_sequence_alignment_aa, name="V1p5j_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p5j_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5j_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p5c_sequence_alignment = Slot(uri=AK_SCHEMA.V1p5c_sequence_alignment, name="V1p5c_sequence_alignment", curie=AK_SCHEMA.curie('V1p5c_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p5c_sequence_alignment, domain=None, range=Optional[str])

slots.V1p5c_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p5c_sequence_alignment_aa, name="V1p5c_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p5c_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5c_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p5v_germline_alignment = Slot(uri=AK_SCHEMA.V1p5v_germline_alignment, name="V1p5v_germline_alignment", curie=AK_SCHEMA.curie('V1p5v_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p5v_germline_alignment, domain=None, range=Optional[str])

slots.V1p5v_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p5v_germline_alignment_aa, name="V1p5v_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p5v_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5v_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p5d_germline_alignment = Slot(uri=AK_SCHEMA.V1p5d_germline_alignment, name="V1p5d_germline_alignment", curie=AK_SCHEMA.curie('V1p5d_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p5d_germline_alignment, domain=None, range=Optional[str])

slots.V1p5d_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p5d_germline_alignment_aa, name="V1p5d_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p5d_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5d_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p5d2_germline_alignment = Slot(uri=AK_SCHEMA.V1p5d2_germline_alignment, name="V1p5d2_germline_alignment", curie=AK_SCHEMA.curie('V1p5d2_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p5d2_germline_alignment, domain=None, range=Optional[str])

slots.V1p5d2_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p5d2_germline_alignment_aa, name="V1p5d2_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p5d2_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5d2_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p5j_germline_alignment = Slot(uri=AK_SCHEMA.V1p5j_germline_alignment, name="V1p5j_germline_alignment", curie=AK_SCHEMA.curie('V1p5j_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p5j_germline_alignment, domain=None, range=Optional[str])

slots.V1p5j_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p5j_germline_alignment_aa, name="V1p5j_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p5j_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5j_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p5c_germline_alignment = Slot(uri=AK_SCHEMA.V1p5c_germline_alignment, name="V1p5c_germline_alignment", curie=AK_SCHEMA.curie('V1p5c_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p5c_germline_alignment, domain=None, range=Optional[str])

slots.V1p5c_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p5c_germline_alignment_aa, name="V1p5c_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p5c_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5c_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p5junction_length = Slot(uri=AK_SCHEMA.V1p5junction_length, name="V1p5junction_length", curie=AK_SCHEMA.curie('V1p5junction_length'),
                   model_uri=AK_SCHEMA.V1p5junction_length, domain=None, range=Optional[int])

slots.V1p5junction_aa_length = Slot(uri=AK_SCHEMA.V1p5junction_aa_length, name="V1p5junction_aa_length", curie=AK_SCHEMA.curie('V1p5junction_aa_length'),
                   model_uri=AK_SCHEMA.V1p5junction_aa_length, domain=None, range=Optional[int])

slots.V1p5np1_length = Slot(uri=AK_SCHEMA.V1p5np1_length, name="V1p5np1_length", curie=AK_SCHEMA.curie('V1p5np1_length'),
                   model_uri=AK_SCHEMA.V1p5np1_length, domain=None, range=Optional[int])

slots.V1p5np2_length = Slot(uri=AK_SCHEMA.V1p5np2_length, name="V1p5np2_length", curie=AK_SCHEMA.curie('V1p5np2_length'),
                   model_uri=AK_SCHEMA.V1p5np2_length, domain=None, range=Optional[int])

slots.V1p5np3_length = Slot(uri=AK_SCHEMA.V1p5np3_length, name="V1p5np3_length", curie=AK_SCHEMA.curie('V1p5np3_length'),
                   model_uri=AK_SCHEMA.V1p5np3_length, domain=None, range=Optional[int])

slots.V1p5n1_length = Slot(uri=AK_SCHEMA.V1p5n1_length, name="V1p5n1_length", curie=AK_SCHEMA.curie('V1p5n1_length'),
                   model_uri=AK_SCHEMA.V1p5n1_length, domain=None, range=Optional[int])

slots.V1p5n2_length = Slot(uri=AK_SCHEMA.V1p5n2_length, name="V1p5n2_length", curie=AK_SCHEMA.curie('V1p5n2_length'),
                   model_uri=AK_SCHEMA.V1p5n2_length, domain=None, range=Optional[int])

slots.V1p5n3_length = Slot(uri=AK_SCHEMA.V1p5n3_length, name="V1p5n3_length", curie=AK_SCHEMA.curie('V1p5n3_length'),
                   model_uri=AK_SCHEMA.V1p5n3_length, domain=None, range=Optional[int])

slots.V1p5p3v_length = Slot(uri=AK_SCHEMA.V1p5p3v_length, name="V1p5p3v_length", curie=AK_SCHEMA.curie('V1p5p3v_length'),
                   model_uri=AK_SCHEMA.V1p5p3v_length, domain=None, range=Optional[int])

slots.V1p5p5d_length = Slot(uri=AK_SCHEMA.V1p5p5d_length, name="V1p5p5d_length", curie=AK_SCHEMA.curie('V1p5p5d_length'),
                   model_uri=AK_SCHEMA.V1p5p5d_length, domain=None, range=Optional[int])

slots.V1p5p3d_length = Slot(uri=AK_SCHEMA.V1p5p3d_length, name="V1p5p3d_length", curie=AK_SCHEMA.curie('V1p5p3d_length'),
                   model_uri=AK_SCHEMA.V1p5p3d_length, domain=None, range=Optional[int])

slots.V1p5p5d2_length = Slot(uri=AK_SCHEMA.V1p5p5d2_length, name="V1p5p5d2_length", curie=AK_SCHEMA.curie('V1p5p5d2_length'),
                   model_uri=AK_SCHEMA.V1p5p5d2_length, domain=None, range=Optional[int])

slots.V1p5p3d2_length = Slot(uri=AK_SCHEMA.V1p5p3d2_length, name="V1p5p3d2_length", curie=AK_SCHEMA.curie('V1p5p3d2_length'),
                   model_uri=AK_SCHEMA.V1p5p3d2_length, domain=None, range=Optional[int])

slots.V1p5p5j_length = Slot(uri=AK_SCHEMA.V1p5p5j_length, name="V1p5p5j_length", curie=AK_SCHEMA.curie('V1p5p5j_length'),
                   model_uri=AK_SCHEMA.V1p5p5j_length, domain=None, range=Optional[int])

slots.V1p5v_frameshift = Slot(uri=AK_SCHEMA.V1p5v_frameshift, name="V1p5v_frameshift", curie=AK_SCHEMA.curie('V1p5v_frameshift'),
                   model_uri=AK_SCHEMA.V1p5v_frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5j_frameshift = Slot(uri=AK_SCHEMA.V1p5j_frameshift, name="V1p5j_frameshift", curie=AK_SCHEMA.curie('V1p5j_frameshift'),
                   model_uri=AK_SCHEMA.V1p5j_frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5d_frame = Slot(uri=AK_SCHEMA.V1p5d_frame, name="V1p5d_frame", curie=AK_SCHEMA.curie('V1p5d_frame'),
                   model_uri=AK_SCHEMA.V1p5d_frame, domain=None, range=Optional[int])

slots.V1p5d2_frame = Slot(uri=AK_SCHEMA.V1p5d2_frame, name="V1p5d2_frame", curie=AK_SCHEMA.curie('V1p5d2_frame'),
                   model_uri=AK_SCHEMA.V1p5d2_frame, domain=None, range=Optional[int])

slots.V1p5consensus_count = Slot(uri=AK_SCHEMA.V1p5consensus_count, name="V1p5consensus_count", curie=AK_SCHEMA.curie('V1p5consensus_count'),
                   model_uri=AK_SCHEMA.V1p5consensus_count, domain=None, range=Optional[int])

slots.V1p5duplicate_count = Slot(uri=AK_SCHEMA.V1p5duplicate_count, name="V1p5duplicate_count", curie=AK_SCHEMA.curie('V1p5duplicate_count'),
                   model_uri=AK_SCHEMA.V1p5duplicate_count, domain=None, range=Optional[int])

slots.V1p5umi_count = Slot(uri=AK_SCHEMA.V1p5umi_count, name="V1p5umi_count", curie=AK_SCHEMA.curie('V1p5umi_count'),
                   model_uri=AK_SCHEMA.V1p5umi_count, domain=None, range=Optional[int])

slots.V1p5cell_id = Slot(uri=AK_SCHEMA.V1p5cell_id, name="V1p5cell_id", curie=AK_SCHEMA.curie('V1p5cell_id'),
                   model_uri=AK_SCHEMA.V1p5cell_id, domain=None, range=Optional[str])

slots.V1p5clone_id = Slot(uri=AK_SCHEMA.V1p5clone_id, name="V1p5clone_id", curie=AK_SCHEMA.curie('V1p5clone_id'),
                   model_uri=AK_SCHEMA.V1p5clone_id, domain=None, range=Optional[str])

slots.V1p5sample_processing_id = Slot(uri=AK_SCHEMA.V1p5sample_processing_id, name="V1p5sample_processing_id", curie=AK_SCHEMA.curie('V1p5sample_processing_id'),
                   model_uri=AK_SCHEMA.V1p5sample_processing_id, domain=None, range=Optional[str])

slots.V1p5sequences = Slot(uri=AK_SCHEMA.V1p5sequences, name="V1p5sequences", curie=AK_SCHEMA.curie('V1p5sequences'),
                   model_uri=AK_SCHEMA.V1p5sequences, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p5junction_start = Slot(uri=AK_SCHEMA.V1p5junction_start, name="V1p5junction_start", curie=AK_SCHEMA.curie('V1p5junction_start'),
                   model_uri=AK_SCHEMA.V1p5junction_start, domain=None, range=Optional[int])

slots.V1p5junction_end = Slot(uri=AK_SCHEMA.V1p5junction_end, name="V1p5junction_end", curie=AK_SCHEMA.curie('V1p5junction_end'),
                   model_uri=AK_SCHEMA.V1p5junction_end, domain=None, range=Optional[int])

slots.V1p5clone_count = Slot(uri=AK_SCHEMA.V1p5clone_count, name="V1p5clone_count", curie=AK_SCHEMA.curie('V1p5clone_count'),
                   model_uri=AK_SCHEMA.V1p5clone_count, domain=None, range=Optional[int])

slots.V1p5seed_id = Slot(uri=AK_SCHEMA.V1p5seed_id, name="V1p5seed_id", curie=AK_SCHEMA.curie('V1p5seed_id'),
                   model_uri=AK_SCHEMA.V1p5seed_id, domain=None, range=Optional[str])

slots.V1p5tree_id = Slot(uri=AK_SCHEMA.V1p5tree_id, name="V1p5tree_id", curie=AK_SCHEMA.curie('V1p5tree_id'),
                   model_uri=AK_SCHEMA.V1p5tree_id, domain=None, range=Optional[str])

slots.V1p5newick = Slot(uri=AK_SCHEMA.V1p5newick, name="V1p5newick", curie=AK_SCHEMA.curie('V1p5newick'),
                   model_uri=AK_SCHEMA.V1p5newick, domain=None, range=Optional[str])

slots.V1p5nodes = Slot(uri=AK_SCHEMA.V1p5nodes, name="V1p5nodes", curie=AK_SCHEMA.curie('V1p5nodes'),
                   model_uri=AK_SCHEMA.V1p5nodes, domain=None, range=Optional[Union[Union[dict, V1p5Node], List[Union[dict, V1p5Node]]]])

slots.V1p5rearrangements = Slot(uri=AK_SCHEMA.V1p5rearrangements, name="V1p5rearrangements", curie=AK_SCHEMA.curie('V1p5rearrangements'),
                   model_uri=AK_SCHEMA.V1p5rearrangements, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p5receptors = Slot(uri=AK_SCHEMA.V1p5receptors, name="V1p5receptors", curie=AK_SCHEMA.curie('V1p5receptors'),
                   model_uri=AK_SCHEMA.V1p5receptors, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p5expression_study_method = Slot(uri=AK_SCHEMA.V1p5expression_study_method, name="V1p5expression_study_method", curie=AK_SCHEMA.curie('V1p5expression_study_method'),
                   model_uri=AK_SCHEMA.V1p5expression_study_method, domain=None, range=Optional[Union[str, "V1p5ExpressionStudyMethod"]])

slots.V1p5expression_raw_doi = Slot(uri=AK_SCHEMA.V1p5expression_raw_doi, name="V1p5expression_raw_doi", curie=AK_SCHEMA.curie('V1p5expression_raw_doi'),
                   model_uri=AK_SCHEMA.V1p5expression_raw_doi, domain=None, range=Optional[str])

slots.V1p5expression_index = Slot(uri=AK_SCHEMA.V1p5expression_index, name="V1p5expression_index", curie=AK_SCHEMA.curie('V1p5expression_index'),
                   model_uri=AK_SCHEMA.V1p5expression_index, domain=None, range=Optional[str])

slots.V1p5virtual_pairing = Slot(uri=AK_SCHEMA.V1p5virtual_pairing, name="V1p5virtual_pairing", curie=AK_SCHEMA.curie('V1p5virtual_pairing'),
                   model_uri=AK_SCHEMA.V1p5virtual_pairing, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5expression_id = Slot(uri=AK_SCHEMA.V1p5expression_id, name="V1p5expression_id", curie=AK_SCHEMA.curie('V1p5expression_id'),
                   model_uri=AK_SCHEMA.V1p5expression_id, domain=None, range=Optional[str])

slots.V1p5property_type = Slot(uri=RDF.type, name="V1p5property_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p5property_type, domain=None, range=Optional[str])

slots.V1p5property = Slot(uri=AK_SCHEMA.V1p5property, name="V1p5property", curie=AK_SCHEMA.curie('V1p5property'),
                   model_uri=AK_SCHEMA.V1p5property, domain=None, range=Optional[Union[str, "V1p5Property"]])

slots.V1p5receptor_id = Slot(uri=AK_SCHEMA.V1p5receptor_id, name="V1p5receptor_id", curie=AK_SCHEMA.curie('V1p5receptor_id'),
                   model_uri=AK_SCHEMA.V1p5receptor_id, domain=None, range=Optional[str])

slots.V1p5receptor_hash = Slot(uri=AK_SCHEMA.V1p5receptor_hash, name="V1p5receptor_hash", curie=AK_SCHEMA.curie('V1p5receptor_hash'),
                   model_uri=AK_SCHEMA.V1p5receptor_hash, domain=None, range=Optional[str])

slots.V1p5receptor_type = Slot(uri=RDF.type, name="V1p5receptor_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p5receptor_type, domain=None, range=Optional[Union[str, "V1p5ReceptorType"]])

slots.V1p5receptor_variable_domain_1_aa = Slot(uri=AK_SCHEMA.V1p5receptor_variable_domain_1_aa, name="V1p5receptor_variable_domain_1_aa", curie=AK_SCHEMA.curie('V1p5receptor_variable_domain_1_aa'),
                   model_uri=AK_SCHEMA.V1p5receptor_variable_domain_1_aa, domain=None, range=Optional[str])

slots.V1p5receptor_variable_domain_1_locus = Slot(uri=AK_SCHEMA.V1p5receptor_variable_domain_1_locus, name="V1p5receptor_variable_domain_1_locus", curie=AK_SCHEMA.curie('V1p5receptor_variable_domain_1_locus'),
                   model_uri=AK_SCHEMA.V1p5receptor_variable_domain_1_locus, domain=None, range=Optional[Union[str, "V1p5ReceptorVariableDomain1Locus"]])

slots.V1p5receptor_variable_domain_2_aa = Slot(uri=AK_SCHEMA.V1p5receptor_variable_domain_2_aa, name="V1p5receptor_variable_domain_2_aa", curie=AK_SCHEMA.curie('V1p5receptor_variable_domain_2_aa'),
                   model_uri=AK_SCHEMA.V1p5receptor_variable_domain_2_aa, domain=None, range=Optional[str])

slots.V1p5receptor_variable_domain_2_locus = Slot(uri=AK_SCHEMA.V1p5receptor_variable_domain_2_locus, name="V1p5receptor_variable_domain_2_locus", curie=AK_SCHEMA.curie('V1p5receptor_variable_domain_2_locus'),
                   model_uri=AK_SCHEMA.V1p5receptor_variable_domain_2_locus, domain=None, range=Optional[Union[str, "V1p5ReceptorVariableDomain2Locus"]])

slots.V1p5receptor_ref = Slot(uri=AK_SCHEMA.V1p5receptor_ref, name="V1p5receptor_ref", curie=AK_SCHEMA.curie('V1p5receptor_ref'),
                   model_uri=AK_SCHEMA.V1p5receptor_ref, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p5reactivity_measurements = Slot(uri=AK_SCHEMA.V1p5reactivity_measurements, name="V1p5reactivity_measurements", curie=AK_SCHEMA.curie('V1p5reactivity_measurements'),
                   model_uri=AK_SCHEMA.V1p5reactivity_measurements, domain=None, range=Optional[Union[Union[dict, V1p5ReceptorReactivity], List[Union[dict, V1p5ReceptorReactivity]]]])

slots.V1p5ligand_type = Slot(uri=RDF.type, name="V1p5ligand_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p5ligand_type, domain=None, range=Optional[Union[str, "V1p5LigandType"]])

slots.V1p5antigen_type = Slot(uri=RDF.type, name="V1p5antigen_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p5antigen_type, domain=None, range=Optional[Union[str, "V1p5AntigenType"]])

slots.V1p5antigen = Slot(uri=AK_SCHEMA.V1p5antigen, name="V1p5antigen", curie=AK_SCHEMA.curie('V1p5antigen'),
                   model_uri=AK_SCHEMA.V1p5antigen, domain=None, range=Optional[Union[str, "V1p5Antigen"]])

slots.V1p5antigen_source_species = Slot(uri=AK_SCHEMA.V1p5antigen_source_species, name="V1p5antigen_source_species", curie=AK_SCHEMA.curie('V1p5antigen_source_species'),
                   model_uri=AK_SCHEMA.V1p5antigen_source_species, domain=None, range=Optional[Union[str, "V1p5AntigenSourceSpecies"]])

slots.V1p5peptide_start = Slot(uri=AK_SCHEMA.V1p5peptide_start, name="V1p5peptide_start", curie=AK_SCHEMA.curie('V1p5peptide_start'),
                   model_uri=AK_SCHEMA.V1p5peptide_start, domain=None, range=Optional[int])

slots.V1p5peptide_end = Slot(uri=AK_SCHEMA.V1p5peptide_end, name="V1p5peptide_end", curie=AK_SCHEMA.curie('V1p5peptide_end'),
                   model_uri=AK_SCHEMA.V1p5peptide_end, domain=None, range=Optional[int])

slots.V1p5mhc_gene_1 = Slot(uri=AK_SCHEMA.V1p5mhc_gene_1, name="V1p5mhc_gene_1", curie=AK_SCHEMA.curie('V1p5mhc_gene_1'),
                   model_uri=AK_SCHEMA.V1p5mhc_gene_1, domain=None, range=Optional[Union[str, "V1p5MhcGene1"]])

slots.V1p5mhc_allele_1 = Slot(uri=AK_SCHEMA.V1p5mhc_allele_1, name="V1p5mhc_allele_1", curie=AK_SCHEMA.curie('V1p5mhc_allele_1'),
                   model_uri=AK_SCHEMA.V1p5mhc_allele_1, domain=None, range=Optional[str])

slots.V1p5mhc_gene_2 = Slot(uri=AK_SCHEMA.V1p5mhc_gene_2, name="V1p5mhc_gene_2", curie=AK_SCHEMA.curie('V1p5mhc_gene_2'),
                   model_uri=AK_SCHEMA.V1p5mhc_gene_2, domain=None, range=Optional[Union[str, "V1p5MhcGene2"]])

slots.V1p5mhc_allele_2 = Slot(uri=AK_SCHEMA.V1p5mhc_allele_2, name="V1p5mhc_allele_2", curie=AK_SCHEMA.curie('V1p5mhc_allele_2'),
                   model_uri=AK_SCHEMA.V1p5mhc_allele_2, domain=None, range=Optional[str])

slots.V1p5reactivity_method = Slot(uri=AK_SCHEMA.V1p5reactivity_method, name="V1p5reactivity_method", curie=AK_SCHEMA.curie('V1p5reactivity_method'),
                   model_uri=AK_SCHEMA.V1p5reactivity_method, domain=None, range=Optional[Union[str, "V1p5ReactivityMethod"]])

slots.V1p5reactivity_readout = Slot(uri=AK_SCHEMA.V1p5reactivity_readout, name="V1p5reactivity_readout", curie=AK_SCHEMA.curie('V1p5reactivity_readout'),
                   model_uri=AK_SCHEMA.V1p5reactivity_readout, domain=None, range=Optional[Union[str, "V1p5ReactivityReadout"]])

slots.V1p5reactivity_value = Slot(uri=AK_SCHEMA.V1p5reactivity_value, name="V1p5reactivity_value", curie=AK_SCHEMA.curie('V1p5reactivity_value'),
                   model_uri=AK_SCHEMA.V1p5reactivity_value, domain=None, range=Optional[float])

slots.V1p5reactivity_unit = Slot(uri=AK_SCHEMA.V1p5reactivity_unit, name="V1p5reactivity_unit", curie=AK_SCHEMA.curie('V1p5reactivity_unit'),
                   model_uri=AK_SCHEMA.V1p5reactivity_unit, domain=None, range=Optional[str])

slots.V1p4label = Slot(uri=AK_SCHEMA.V1p4label, name="V1p4label", curie=AK_SCHEMA.curie('V1p4label'),
                   model_uri=AK_SCHEMA.V1p4label, domain=None, range=Optional[str])

slots.V1p4value = Slot(uri=AK_SCHEMA.V1p4value, name="V1p4value", curie=AK_SCHEMA.curie('V1p4value'),
                   model_uri=AK_SCHEMA.V1p4value, domain=None, range=Optional[float])

slots.V1p4unit = Slot(uri=AK_SCHEMA.V1p4unit, name="V1p4unit", curie=AK_SCHEMA.curie('V1p4unit'),
                   model_uri=AK_SCHEMA.V1p4unit, domain=None, range=Optional[Union[str, "V1p4Unit"]])

slots.V1p4min = Slot(uri=AK_SCHEMA.V1p4min, name="V1p4min", curie=AK_SCHEMA.curie('V1p4min'),
                   model_uri=AK_SCHEMA.V1p4min, domain=None, range=Optional[float])

slots.V1p4max = Slot(uri=AK_SCHEMA.V1p4max, name="V1p4max", curie=AK_SCHEMA.curie('V1p4max'),
                   model_uri=AK_SCHEMA.V1p4max, domain=None, range=Optional[float])

slots.V1p4quantity = Slot(uri=AK_SCHEMA.V1p4quantity, name="V1p4quantity", curie=AK_SCHEMA.curie('V1p4quantity'),
                   model_uri=AK_SCHEMA.V1p4quantity, domain=None, range=Optional[float])

slots.V1p4contributor_id = Slot(uri=AK_SCHEMA.V1p4contributor_id, name="V1p4contributor_id", curie=AK_SCHEMA.curie('V1p4contributor_id'),
                   model_uri=AK_SCHEMA.V1p4contributor_id, domain=None, range=Optional[str])

slots.V1p4name = Slot(uri=AK_SCHEMA.V1p4name, name="V1p4name", curie=AK_SCHEMA.curie('V1p4name'),
                   model_uri=AK_SCHEMA.V1p4name, domain=None, range=Optional[str])

slots.V1p4orcid_id = Slot(uri=AK_SCHEMA.V1p4orcid_id, name="V1p4orcid_id", curie=AK_SCHEMA.curie('V1p4orcid_id'),
                   model_uri=AK_SCHEMA.V1p4orcid_id, domain=None, range=Optional[Union[str, "V1p4OrcidId"]])

slots.V1p4affiliation = Slot(uri=AK_SCHEMA.V1p4affiliation, name="V1p4affiliation", curie=AK_SCHEMA.curie('V1p4affiliation'),
                   model_uri=AK_SCHEMA.V1p4affiliation, domain=None, range=Optional[Union[str, "V1p4Affiliation"]])

slots.V1p4affiliation_department = Slot(uri=AK_SCHEMA.V1p4affiliation_department, name="V1p4affiliation_department", curie=AK_SCHEMA.curie('V1p4affiliation_department'),
                   model_uri=AK_SCHEMA.V1p4affiliation_department, domain=None, range=Optional[str])

slots.V1p4contributions = Slot(uri=AK_SCHEMA.V1p4contributions, name="V1p4contributions", curie=AK_SCHEMA.curie('V1p4contributions'),
                   model_uri=AK_SCHEMA.V1p4contributions, domain=None, range=Optional[Union[Union[dict, V1p4ContributorContribution], List[Union[dict, V1p4ContributorContribution]]]])

slots.V1p4role = Slot(uri=AK_SCHEMA.V1p4role, name="V1p4role", curie=AK_SCHEMA.curie('V1p4role'),
                   model_uri=AK_SCHEMA.V1p4role, domain=None, range=Optional[Union[str, "V1p4Role"]])

slots.V1p4degree = Slot(uri=AK_SCHEMA.V1p4degree, name="V1p4degree", curie=AK_SCHEMA.curie('V1p4degree'),
                   model_uri=AK_SCHEMA.V1p4degree, domain=None, range=Optional[Union[str, "V1p4Degree"]])

slots.V1p4sequence_id = Slot(uri=AK_SCHEMA.V1p4sequence_id, name="V1p4sequence_id", curie=AK_SCHEMA.curie('V1p4sequence_id'),
                   model_uri=AK_SCHEMA.V1p4sequence_id, domain=None, range=Optional[str])

slots.V1p4sequence = Slot(uri=AK_SCHEMA.V1p4sequence, name="V1p4sequence", curie=AK_SCHEMA.curie('V1p4sequence'),
                   model_uri=AK_SCHEMA.V1p4sequence, domain=None, range=Optional[str])

slots.V1p4derivation = Slot(uri=AK_SCHEMA.V1p4derivation, name="V1p4derivation", curie=AK_SCHEMA.curie('V1p4derivation'),
                   model_uri=AK_SCHEMA.V1p4derivation, domain=None, range=Optional[Union[str, "V1p4Derivation"]])

slots.V1p4observation_type = Slot(uri=RDF.type, name="V1p4observation_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p4observation_type, domain=None, range=Optional[Union[str, "V1p4ObservationType"]])

slots.V1p4curation = Slot(uri=AK_SCHEMA.V1p4curation, name="V1p4curation", curie=AK_SCHEMA.curie('V1p4curation'),
                   model_uri=AK_SCHEMA.V1p4curation, domain=None, range=Optional[str])

slots.V1p4repository_name = Slot(uri=AK_SCHEMA.V1p4repository_name, name="V1p4repository_name", curie=AK_SCHEMA.curie('V1p4repository_name'),
                   model_uri=AK_SCHEMA.V1p4repository_name, domain=None, range=Optional[str])

slots.V1p4repository_ref = Slot(uri=AK_SCHEMA.V1p4repository_ref, name="V1p4repository_ref", curie=AK_SCHEMA.curie('V1p4repository_ref'),
                   model_uri=AK_SCHEMA.V1p4repository_ref, domain=None, range=Optional[str])

slots.V1p4deposited_version = Slot(uri=AK_SCHEMA.V1p4deposited_version, name="V1p4deposited_version", curie=AK_SCHEMA.curie('V1p4deposited_version'),
                   model_uri=AK_SCHEMA.V1p4deposited_version, domain=None, range=Optional[str])

slots.V1p4sequence_start = Slot(uri=AK_SCHEMA.V1p4sequence_start, name="V1p4sequence_start", curie=AK_SCHEMA.curie('V1p4sequence_start'),
                   model_uri=AK_SCHEMA.V1p4sequence_start, domain=None, range=Optional[int])

slots.V1p4sequence_end = Slot(uri=AK_SCHEMA.V1p4sequence_end, name="V1p4sequence_end", curie=AK_SCHEMA.curie('V1p4sequence_end'),
                   model_uri=AK_SCHEMA.V1p4sequence_end, domain=None, range=Optional[int])

slots.V1p4patch_no = Slot(uri=AK_SCHEMA.V1p4patch_no, name="V1p4patch_no", curie=AK_SCHEMA.curie('V1p4patch_no'),
                   model_uri=AK_SCHEMA.V1p4patch_no, domain=None, range=Optional[str])

slots.V1p4gff_seqid = Slot(uri=AK_SCHEMA.V1p4gff_seqid, name="V1p4gff_seqid", curie=AK_SCHEMA.curie('V1p4gff_seqid'),
                   model_uri=AK_SCHEMA.V1p4gff_seqid, domain=None, range=Optional[str])

slots.V1p4gff_start = Slot(uri=AK_SCHEMA.V1p4gff_start, name="V1p4gff_start", curie=AK_SCHEMA.curie('V1p4gff_start'),
                   model_uri=AK_SCHEMA.V1p4gff_start, domain=None, range=Optional[int])

slots.V1p4gff_end = Slot(uri=AK_SCHEMA.V1p4gff_end, name="V1p4gff_end", curie=AK_SCHEMA.curie('V1p4gff_end'),
                   model_uri=AK_SCHEMA.V1p4gff_end, domain=None, range=Optional[int])

slots.V1p4strand = Slot(uri=AK_SCHEMA.V1p4strand, name="V1p4strand", curie=AK_SCHEMA.curie('V1p4strand'),
                   model_uri=AK_SCHEMA.V1p4strand, domain=None, range=Optional[Union[str, "V1p4Strand"]])

slots.V1p4sequence_delineation_id = Slot(uri=AK_SCHEMA.V1p4sequence_delineation_id, name="V1p4sequence_delineation_id", curie=AK_SCHEMA.curie('V1p4sequence_delineation_id'),
                   model_uri=AK_SCHEMA.V1p4sequence_delineation_id, domain=None, range=Optional[str])

slots.V1p4delineation_scheme = Slot(uri=AK_SCHEMA.V1p4delineation_scheme, name="V1p4delineation_scheme", curie=AK_SCHEMA.curie('V1p4delineation_scheme'),
                   model_uri=AK_SCHEMA.V1p4delineation_scheme, domain=None, range=Optional[str])

slots.V1p4unaligned_sequence = Slot(uri=AK_SCHEMA.V1p4unaligned_sequence, name="V1p4unaligned_sequence", curie=AK_SCHEMA.curie('V1p4unaligned_sequence'),
                   model_uri=AK_SCHEMA.V1p4unaligned_sequence, domain=None, range=Optional[str])

slots.V1p4aligned_sequence = Slot(uri=AK_SCHEMA.V1p4aligned_sequence, name="V1p4aligned_sequence", curie=AK_SCHEMA.curie('V1p4aligned_sequence'),
                   model_uri=AK_SCHEMA.V1p4aligned_sequence, domain=None, range=Optional[str])

slots.V1p4fwr1_start = Slot(uri=AK_SCHEMA.V1p4fwr1_start, name="V1p4fwr1_start", curie=AK_SCHEMA.curie('V1p4fwr1_start'),
                   model_uri=AK_SCHEMA.V1p4fwr1_start, domain=None, range=Optional[int])

slots.V1p4fwr1_end = Slot(uri=AK_SCHEMA.V1p4fwr1_end, name="V1p4fwr1_end", curie=AK_SCHEMA.curie('V1p4fwr1_end'),
                   model_uri=AK_SCHEMA.V1p4fwr1_end, domain=None, range=Optional[int])

slots.V1p4cdr1_start = Slot(uri=AK_SCHEMA.V1p4cdr1_start, name="V1p4cdr1_start", curie=AK_SCHEMA.curie('V1p4cdr1_start'),
                   model_uri=AK_SCHEMA.V1p4cdr1_start, domain=None, range=Optional[int])

slots.V1p4cdr1_end = Slot(uri=AK_SCHEMA.V1p4cdr1_end, name="V1p4cdr1_end", curie=AK_SCHEMA.curie('V1p4cdr1_end'),
                   model_uri=AK_SCHEMA.V1p4cdr1_end, domain=None, range=Optional[int])

slots.V1p4fwr2_start = Slot(uri=AK_SCHEMA.V1p4fwr2_start, name="V1p4fwr2_start", curie=AK_SCHEMA.curie('V1p4fwr2_start'),
                   model_uri=AK_SCHEMA.V1p4fwr2_start, domain=None, range=Optional[int])

slots.V1p4fwr2_end = Slot(uri=AK_SCHEMA.V1p4fwr2_end, name="V1p4fwr2_end", curie=AK_SCHEMA.curie('V1p4fwr2_end'),
                   model_uri=AK_SCHEMA.V1p4fwr2_end, domain=None, range=Optional[int])

slots.V1p4cdr2_start = Slot(uri=AK_SCHEMA.V1p4cdr2_start, name="V1p4cdr2_start", curie=AK_SCHEMA.curie('V1p4cdr2_start'),
                   model_uri=AK_SCHEMA.V1p4cdr2_start, domain=None, range=Optional[int])

slots.V1p4cdr2_end = Slot(uri=AK_SCHEMA.V1p4cdr2_end, name="V1p4cdr2_end", curie=AK_SCHEMA.curie('V1p4cdr2_end'),
                   model_uri=AK_SCHEMA.V1p4cdr2_end, domain=None, range=Optional[int])

slots.V1p4fwr3_start = Slot(uri=AK_SCHEMA.V1p4fwr3_start, name="V1p4fwr3_start", curie=AK_SCHEMA.curie('V1p4fwr3_start'),
                   model_uri=AK_SCHEMA.V1p4fwr3_start, domain=None, range=Optional[int])

slots.V1p4fwr3_end = Slot(uri=AK_SCHEMA.V1p4fwr3_end, name="V1p4fwr3_end", curie=AK_SCHEMA.curie('V1p4fwr3_end'),
                   model_uri=AK_SCHEMA.V1p4fwr3_end, domain=None, range=Optional[int])

slots.V1p4cdr3_start = Slot(uri=AK_SCHEMA.V1p4cdr3_start, name="V1p4cdr3_start", curie=AK_SCHEMA.curie('V1p4cdr3_start'),
                   model_uri=AK_SCHEMA.V1p4cdr3_start, domain=None, range=Optional[int])

slots.V1p4alignment_labels = Slot(uri=AK_SCHEMA.V1p4alignment_labels, name="V1p4alignment_labels", curie=AK_SCHEMA.curie('V1p4alignment_labels'),
                   model_uri=AK_SCHEMA.V1p4alignment_labels, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4allele_description_id = Slot(uri=AK_SCHEMA.V1p4allele_description_id, name="V1p4allele_description_id", curie=AK_SCHEMA.curie('V1p4allele_description_id'),
                   model_uri=AK_SCHEMA.V1p4allele_description_id, domain=None, range=Optional[str])

slots.V1p4allele_description_ref = Slot(uri=AK_SCHEMA.V1p4allele_description_ref, name="V1p4allele_description_ref", curie=AK_SCHEMA.curie('V1p4allele_description_ref'),
                   model_uri=AK_SCHEMA.V1p4allele_description_ref, domain=None, range=Optional[str])

slots.V1p4acknowledgements = Slot(uri=AK_SCHEMA.V1p4acknowledgements, name="V1p4acknowledgements", curie=AK_SCHEMA.curie('V1p4acknowledgements'),
                   model_uri=AK_SCHEMA.V1p4acknowledgements, domain=None, range=Optional[Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]]])

slots.V1p4release_version = Slot(uri=AK_SCHEMA.V1p4release_version, name="V1p4release_version", curie=AK_SCHEMA.curie('V1p4release_version'),
                   model_uri=AK_SCHEMA.V1p4release_version, domain=None, range=Optional[str])

slots.V1p4release_date = Slot(uri=AK_SCHEMA.V1p4release_date, name="V1p4release_date", curie=AK_SCHEMA.curie('V1p4release_date'),
                   model_uri=AK_SCHEMA.V1p4release_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.V1p4release_description = Slot(uri=AK_SCHEMA.V1p4release_description, name="V1p4release_description", curie=AK_SCHEMA.curie('V1p4release_description'),
                   model_uri=AK_SCHEMA.V1p4release_description, domain=None, range=Optional[str])

slots.V1p4coding_sequence = Slot(uri=AK_SCHEMA.V1p4coding_sequence, name="V1p4coding_sequence", curie=AK_SCHEMA.curie('V1p4coding_sequence'),
                   model_uri=AK_SCHEMA.V1p4coding_sequence, domain=None, range=Optional[str])

slots.V1p4aliases = Slot(uri=AK_SCHEMA.V1p4aliases, name="V1p4aliases", curie=AK_SCHEMA.curie('V1p4aliases'),
                   model_uri=AK_SCHEMA.V1p4aliases, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4locus = Slot(uri=AK_SCHEMA.V1p4locus, name="V1p4locus", curie=AK_SCHEMA.curie('V1p4locus'),
                   model_uri=AK_SCHEMA.V1p4locus, domain=None, range=Optional[Union[str, "V1p4Locus"]])

slots.V1p4chromosome = Slot(uri=AK_SCHEMA.V1p4chromosome, name="V1p4chromosome", curie=AK_SCHEMA.curie('V1p4chromosome'),
                   model_uri=AK_SCHEMA.V1p4chromosome, domain=None, range=Optional[int])

slots.V1p4sequence_type = Slot(uri=RDF.type, name="V1p4sequence_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p4sequence_type, domain=None, range=Optional[Union[str, "V1p4SequenceType"]])

slots.V1p4functional = Slot(uri=AK_SCHEMA.V1p4functional, name="V1p4functional", curie=AK_SCHEMA.curie('V1p4functional'),
                   model_uri=AK_SCHEMA.V1p4functional, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4inference_type = Slot(uri=RDF.type, name="V1p4inference_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p4inference_type, domain=None, range=Optional[Union[str, "V1p4InferenceType"]])

slots.V1p4species = Slot(uri=AK_SCHEMA.V1p4species, name="V1p4species", curie=AK_SCHEMA.curie('V1p4species'),
                   model_uri=AK_SCHEMA.V1p4species, domain=None, range=Optional[Union[str, "V1p4Species"]])

slots.V1p4species_subgroup = Slot(uri=AK_SCHEMA.V1p4species_subgroup, name="V1p4species_subgroup", curie=AK_SCHEMA.curie('V1p4species_subgroup'),
                   model_uri=AK_SCHEMA.V1p4species_subgroup, domain=None, range=Optional[str])

slots.V1p4species_subgroup_type = Slot(uri=RDF.type, name="V1p4species_subgroup_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p4species_subgroup_type, domain=None, range=Optional[Union[str, "V1p4SpeciesSubgroupType"]])

slots.V1p4status = Slot(uri=AK_SCHEMA.V1p4status, name="V1p4status", curie=AK_SCHEMA.curie('V1p4status'),
                   model_uri=AK_SCHEMA.V1p4status, domain=None, range=Optional[Union[str, "V1p4Status"]])

slots.V1p4subgroup_designation = Slot(uri=AK_SCHEMA.V1p4subgroup_designation, name="V1p4subgroup_designation", curie=AK_SCHEMA.curie('V1p4subgroup_designation'),
                   model_uri=AK_SCHEMA.V1p4subgroup_designation, domain=None, range=Optional[str])

slots.V1p4gene_designation = Slot(uri=AK_SCHEMA.V1p4gene_designation, name="V1p4gene_designation", curie=AK_SCHEMA.curie('V1p4gene_designation'),
                   model_uri=AK_SCHEMA.V1p4gene_designation, domain=None, range=Optional[str])

slots.V1p4allele_designation = Slot(uri=AK_SCHEMA.V1p4allele_designation, name="V1p4allele_designation", curie=AK_SCHEMA.curie('V1p4allele_designation'),
                   model_uri=AK_SCHEMA.V1p4allele_designation, domain=None, range=Optional[str])

slots.V1p4allele_similarity_cluster_designation = Slot(uri=AK_SCHEMA.V1p4allele_similarity_cluster_designation, name="V1p4allele_similarity_cluster_designation", curie=AK_SCHEMA.curie('V1p4allele_similarity_cluster_designation'),
                   model_uri=AK_SCHEMA.V1p4allele_similarity_cluster_designation, domain=None, range=Optional[str])

slots.V1p4allele_similarity_cluster_member_id = Slot(uri=AK_SCHEMA.V1p4allele_similarity_cluster_member_id, name="V1p4allele_similarity_cluster_member_id", curie=AK_SCHEMA.curie('V1p4allele_similarity_cluster_member_id'),
                   model_uri=AK_SCHEMA.V1p4allele_similarity_cluster_member_id, domain=None, range=Optional[str])

slots.V1p4j_codon_frame = Slot(uri=AK_SCHEMA.V1p4j_codon_frame, name="V1p4j_codon_frame", curie=AK_SCHEMA.curie('V1p4j_codon_frame'),
                   model_uri=AK_SCHEMA.V1p4j_codon_frame, domain=None, range=Optional[Union[str, "V1p4JCodonFrame"]])

slots.V1p4gene_start = Slot(uri=AK_SCHEMA.V1p4gene_start, name="V1p4gene_start", curie=AK_SCHEMA.curie('V1p4gene_start'),
                   model_uri=AK_SCHEMA.V1p4gene_start, domain=None, range=Optional[int])

slots.V1p4gene_end = Slot(uri=AK_SCHEMA.V1p4gene_end, name="V1p4gene_end", curie=AK_SCHEMA.curie('V1p4gene_end'),
                   model_uri=AK_SCHEMA.V1p4gene_end, domain=None, range=Optional[int])

slots.V1p4utr_5_prime_start = Slot(uri=AK_SCHEMA.V1p4utr_5_prime_start, name="V1p4utr_5_prime_start", curie=AK_SCHEMA.curie('V1p4utr_5_prime_start'),
                   model_uri=AK_SCHEMA.V1p4utr_5_prime_start, domain=None, range=Optional[int])

slots.V1p4utr_5_prime_end = Slot(uri=AK_SCHEMA.V1p4utr_5_prime_end, name="V1p4utr_5_prime_end", curie=AK_SCHEMA.curie('V1p4utr_5_prime_end'),
                   model_uri=AK_SCHEMA.V1p4utr_5_prime_end, domain=None, range=Optional[int])

slots.V1p4leader_1_start = Slot(uri=AK_SCHEMA.V1p4leader_1_start, name="V1p4leader_1_start", curie=AK_SCHEMA.curie('V1p4leader_1_start'),
                   model_uri=AK_SCHEMA.V1p4leader_1_start, domain=None, range=Optional[int])

slots.V1p4leader_1_end = Slot(uri=AK_SCHEMA.V1p4leader_1_end, name="V1p4leader_1_end", curie=AK_SCHEMA.curie('V1p4leader_1_end'),
                   model_uri=AK_SCHEMA.V1p4leader_1_end, domain=None, range=Optional[int])

slots.V1p4leader_2_start = Slot(uri=AK_SCHEMA.V1p4leader_2_start, name="V1p4leader_2_start", curie=AK_SCHEMA.curie('V1p4leader_2_start'),
                   model_uri=AK_SCHEMA.V1p4leader_2_start, domain=None, range=Optional[int])

slots.V1p4leader_2_end = Slot(uri=AK_SCHEMA.V1p4leader_2_end, name="V1p4leader_2_end", curie=AK_SCHEMA.curie('V1p4leader_2_end'),
                   model_uri=AK_SCHEMA.V1p4leader_2_end, domain=None, range=Optional[int])

slots.V1p4v_rs_start = Slot(uri=AK_SCHEMA.V1p4v_rs_start, name="V1p4v_rs_start", curie=AK_SCHEMA.curie('V1p4v_rs_start'),
                   model_uri=AK_SCHEMA.V1p4v_rs_start, domain=None, range=Optional[int])

slots.V1p4v_rs_end = Slot(uri=AK_SCHEMA.V1p4v_rs_end, name="V1p4v_rs_end", curie=AK_SCHEMA.curie('V1p4v_rs_end'),
                   model_uri=AK_SCHEMA.V1p4v_rs_end, domain=None, range=Optional[int])

slots.V1p4d_rs_3_prime_start = Slot(uri=AK_SCHEMA.V1p4d_rs_3_prime_start, name="V1p4d_rs_3_prime_start", curie=AK_SCHEMA.curie('V1p4d_rs_3_prime_start'),
                   model_uri=AK_SCHEMA.V1p4d_rs_3_prime_start, domain=None, range=Optional[int])

slots.V1p4d_rs_3_prime_end = Slot(uri=AK_SCHEMA.V1p4d_rs_3_prime_end, name="V1p4d_rs_3_prime_end", curie=AK_SCHEMA.curie('V1p4d_rs_3_prime_end'),
                   model_uri=AK_SCHEMA.V1p4d_rs_3_prime_end, domain=None, range=Optional[int])

slots.V1p4d_rs_5_prime_start = Slot(uri=AK_SCHEMA.V1p4d_rs_5_prime_start, name="V1p4d_rs_5_prime_start", curie=AK_SCHEMA.curie('V1p4d_rs_5_prime_start'),
                   model_uri=AK_SCHEMA.V1p4d_rs_5_prime_start, domain=None, range=Optional[int])

slots.V1p4d_rs_5_prime_end = Slot(uri=AK_SCHEMA.V1p4d_rs_5_prime_end, name="V1p4d_rs_5_prime_end", curie=AK_SCHEMA.curie('V1p4d_rs_5_prime_end'),
                   model_uri=AK_SCHEMA.V1p4d_rs_5_prime_end, domain=None, range=Optional[int])

slots.V1p4j_cdr3_end = Slot(uri=AK_SCHEMA.V1p4j_cdr3_end, name="V1p4j_cdr3_end", curie=AK_SCHEMA.curie('V1p4j_cdr3_end'),
                   model_uri=AK_SCHEMA.V1p4j_cdr3_end, domain=None, range=Optional[int])

slots.V1p4j_rs_start = Slot(uri=AK_SCHEMA.V1p4j_rs_start, name="V1p4j_rs_start", curie=AK_SCHEMA.curie('V1p4j_rs_start'),
                   model_uri=AK_SCHEMA.V1p4j_rs_start, domain=None, range=Optional[int])

slots.V1p4j_rs_end = Slot(uri=AK_SCHEMA.V1p4j_rs_end, name="V1p4j_rs_end", curie=AK_SCHEMA.curie('V1p4j_rs_end'),
                   model_uri=AK_SCHEMA.V1p4j_rs_end, domain=None, range=Optional[int])

slots.V1p4j_donor_splice = Slot(uri=AK_SCHEMA.V1p4j_donor_splice, name="V1p4j_donor_splice", curie=AK_SCHEMA.curie('V1p4j_donor_splice'),
                   model_uri=AK_SCHEMA.V1p4j_donor_splice, domain=None, range=Optional[int])

slots.V1p4v_gene_delineations = Slot(uri=AK_SCHEMA.V1p4v_gene_delineations, name="V1p4v_gene_delineations", curie=AK_SCHEMA.curie('V1p4v_gene_delineations'),
                   model_uri=AK_SCHEMA.V1p4v_gene_delineations, domain=None, range=Optional[Union[Union[dict, V1p4SequenceDelineationV], List[Union[dict, V1p4SequenceDelineationV]]]])

slots.V1p4unrearranged_support = Slot(uri=AK_SCHEMA.V1p4unrearranged_support, name="V1p4unrearranged_support", curie=AK_SCHEMA.curie('V1p4unrearranged_support'),
                   model_uri=AK_SCHEMA.V1p4unrearranged_support, domain=None, range=Optional[Union[Union[dict, V1p4UnrearrangedSequence], List[Union[dict, V1p4UnrearrangedSequence]]]])

slots.V1p4rearranged_support = Slot(uri=AK_SCHEMA.V1p4rearranged_support, name="V1p4rearranged_support", curie=AK_SCHEMA.curie('V1p4rearranged_support'),
                   model_uri=AK_SCHEMA.V1p4rearranged_support, domain=None, range=Optional[Union[Union[dict, V1p4RearrangedSequence], List[Union[dict, V1p4RearrangedSequence]]]])

slots.V1p4paralogs = Slot(uri=AK_SCHEMA.V1p4paralogs, name="V1p4paralogs", curie=AK_SCHEMA.curie('V1p4paralogs'),
                   model_uri=AK_SCHEMA.V1p4paralogs, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4curational_tags = Slot(uri=AK_SCHEMA.V1p4curational_tags, name="V1p4curational_tags", curie=AK_SCHEMA.curie('V1p4curational_tags'),
                   model_uri=AK_SCHEMA.V1p4curational_tags, domain=None, range=Optional[Union[Union[str, "V1p4CurationalTags"], List[Union[str, "V1p4CurationalTags"]]]])

slots.V1p4germline_set_id = Slot(uri=AK_SCHEMA.V1p4germline_set_id, name="V1p4germline_set_id", curie=AK_SCHEMA.curie('V1p4germline_set_id'),
                   model_uri=AK_SCHEMA.V1p4germline_set_id, domain=None, range=Optional[str])

slots.V1p4germline_set_name = Slot(uri=AK_SCHEMA.V1p4germline_set_name, name="V1p4germline_set_name", curie=AK_SCHEMA.curie('V1p4germline_set_name'),
                   model_uri=AK_SCHEMA.V1p4germline_set_name, domain=None, range=Optional[str])

slots.V1p4germline_set_ref = Slot(uri=AK_SCHEMA.V1p4germline_set_ref, name="V1p4germline_set_ref", curie=AK_SCHEMA.curie('V1p4germline_set_ref'),
                   model_uri=AK_SCHEMA.V1p4germline_set_ref, domain=None, range=Optional[str])

slots.V1p4pub_ids = Slot(uri=AK_SCHEMA.V1p4pub_ids, name="V1p4pub_ids", curie=AK_SCHEMA.curie('V1p4pub_ids'),
                   model_uri=AK_SCHEMA.V1p4pub_ids, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4allele_descriptions = Slot(uri=AK_SCHEMA.V1p4allele_descriptions, name="V1p4allele_descriptions", curie=AK_SCHEMA.curie('V1p4allele_descriptions'),
                   model_uri=AK_SCHEMA.V1p4allele_descriptions, domain=None, range=Optional[Union[Union[dict, V1p4AlleleDescription], List[Union[dict, V1p4AlleleDescription]]]])

slots.V1p4receptor_genotype_set_id = Slot(uri=AK_SCHEMA.V1p4receptor_genotype_set_id, name="V1p4receptor_genotype_set_id", curie=AK_SCHEMA.curie('V1p4receptor_genotype_set_id'),
                   model_uri=AK_SCHEMA.V1p4receptor_genotype_set_id, domain=None, range=Optional[str])

slots.V1p4genotype_class_list = Slot(uri=AK_SCHEMA.V1p4genotype_class_list, name="V1p4genotype_class_list", curie=AK_SCHEMA.curie('V1p4genotype_class_list'),
                   model_uri=AK_SCHEMA.V1p4genotype_class_list, domain=None, range=Optional[Union[Union[dict, V1p4Genotype], List[Union[dict, V1p4Genotype]]]])

slots.V1p4receptor_genotype_id = Slot(uri=AK_SCHEMA.V1p4receptor_genotype_id, name="V1p4receptor_genotype_id", curie=AK_SCHEMA.curie('V1p4receptor_genotype_id'),
                   model_uri=AK_SCHEMA.V1p4receptor_genotype_id, domain=None, range=Optional[str])

slots.V1p4documented_alleles = Slot(uri=AK_SCHEMA.V1p4documented_alleles, name="V1p4documented_alleles", curie=AK_SCHEMA.curie('V1p4documented_alleles'),
                   model_uri=AK_SCHEMA.V1p4documented_alleles, domain=None, range=Optional[Union[Union[dict, V1p4DocumentedAllele], List[Union[dict, V1p4DocumentedAllele]]]])

slots.V1p4undocumented_alleles = Slot(uri=AK_SCHEMA.V1p4undocumented_alleles, name="V1p4undocumented_alleles", curie=AK_SCHEMA.curie('V1p4undocumented_alleles'),
                   model_uri=AK_SCHEMA.V1p4undocumented_alleles, domain=None, range=Optional[Union[Union[dict, V1p4UndocumentedAllele], List[Union[dict, V1p4UndocumentedAllele]]]])

slots.V1p4deleted_genes = Slot(uri=AK_SCHEMA.V1p4deleted_genes, name="V1p4deleted_genes", curie=AK_SCHEMA.curie('V1p4deleted_genes'),
                   model_uri=AK_SCHEMA.V1p4deleted_genes, domain=None, range=Optional[Union[Union[dict, V1p4DeletedGene], List[Union[dict, V1p4DeletedGene]]]])

slots.V1p4inference_process = Slot(uri=AK_SCHEMA.V1p4inference_process, name="V1p4inference_process", curie=AK_SCHEMA.curie('V1p4inference_process'),
                   model_uri=AK_SCHEMA.V1p4inference_process, domain=None, range=Optional[Union[str, "V1p4InferenceProcess"]])

slots.V1p4phasing = Slot(uri=AK_SCHEMA.V1p4phasing, name="V1p4phasing", curie=AK_SCHEMA.curie('V1p4phasing'),
                   model_uri=AK_SCHEMA.V1p4phasing, domain=None, range=Optional[int])

slots.V1p4allele_name = Slot(uri=AK_SCHEMA.V1p4allele_name, name="V1p4allele_name", curie=AK_SCHEMA.curie('V1p4allele_name'),
                   model_uri=AK_SCHEMA.V1p4allele_name, domain=None, range=Optional[str])

slots.V1p4mhc_genotype_set_id = Slot(uri=AK_SCHEMA.V1p4mhc_genotype_set_id, name="V1p4mhc_genotype_set_id", curie=AK_SCHEMA.curie('V1p4mhc_genotype_set_id'),
                   model_uri=AK_SCHEMA.V1p4mhc_genotype_set_id, domain=None, range=Optional[str])

slots.V1p4mhc_genotype_list = Slot(uri=AK_SCHEMA.V1p4mhc_genotype_list, name="V1p4mhc_genotype_list", curie=AK_SCHEMA.curie('V1p4mhc_genotype_list'),
                   model_uri=AK_SCHEMA.V1p4mhc_genotype_list, domain=None, range=Optional[Union[Union[dict, V1p4MHCGenotype], List[Union[dict, V1p4MHCGenotype]]]])

slots.V1p4mhc_genotype_id = Slot(uri=AK_SCHEMA.V1p4mhc_genotype_id, name="V1p4mhc_genotype_id", curie=AK_SCHEMA.curie('V1p4mhc_genotype_id'),
                   model_uri=AK_SCHEMA.V1p4mhc_genotype_id, domain=None, range=Optional[str])

slots.V1p4mhc_class = Slot(uri=AK_SCHEMA.V1p4mhc_class, name="V1p4mhc_class", curie=AK_SCHEMA.curie('V1p4mhc_class'),
                   model_uri=AK_SCHEMA.V1p4mhc_class, domain=None, range=Optional[Union[str, "V1p4MhcClass"]])

slots.V1p4mhc_alleles = Slot(uri=AK_SCHEMA.V1p4mhc_alleles, name="V1p4mhc_alleles", curie=AK_SCHEMA.curie('V1p4mhc_alleles'),
                   model_uri=AK_SCHEMA.V1p4mhc_alleles, domain=None, range=Optional[Union[Union[dict, V1p4MHCAllele], List[Union[dict, V1p4MHCAllele]]]])

slots.V1p4mhc_genotyping_method = Slot(uri=AK_SCHEMA.V1p4mhc_genotyping_method, name="V1p4mhc_genotyping_method", curie=AK_SCHEMA.curie('V1p4mhc_genotyping_method'),
                   model_uri=AK_SCHEMA.V1p4mhc_genotyping_method, domain=None, range=Optional[str])

slots.V1p4gene = Slot(uri=AK_SCHEMA.V1p4gene, name="V1p4gene", curie=AK_SCHEMA.curie('V1p4gene'),
                   model_uri=AK_SCHEMA.V1p4gene, domain=None, range=Optional[Union[str, "V1p4Gene"]])

slots.V1p4reference_set_ref = Slot(uri=AK_SCHEMA.V1p4reference_set_ref, name="V1p4reference_set_ref", curie=AK_SCHEMA.curie('V1p4reference_set_ref'),
                   model_uri=AK_SCHEMA.V1p4reference_set_ref, domain=None, range=Optional[str])

slots.V1p4receptor_genotype_set = Slot(uri=AK_SCHEMA.V1p4receptor_genotype_set, name="V1p4receptor_genotype_set", curie=AK_SCHEMA.curie('V1p4receptor_genotype_set'),
                   model_uri=AK_SCHEMA.V1p4receptor_genotype_set, domain=None, range=Optional[Union[dict, V1p4GenotypeSet]])

slots.V1p4mhc_genotype_set = Slot(uri=AK_SCHEMA.V1p4mhc_genotype_set, name="V1p4mhc_genotype_set", curie=AK_SCHEMA.curie('V1p4mhc_genotype_set'),
                   model_uri=AK_SCHEMA.V1p4mhc_genotype_set, domain=None, range=Optional[Union[dict, V1p4MHCGenotypeSet]])

slots.V1p4study_id = Slot(uri=AK_SCHEMA.V1p4study_id, name="V1p4study_id", curie=AK_SCHEMA.curie('V1p4study_id'),
                   model_uri=AK_SCHEMA.V1p4study_id, domain=None, range=Optional[str])

slots.V1p4study_title = Slot(uri=AK_SCHEMA.V1p4study_title, name="V1p4study_title", curie=AK_SCHEMA.curie('V1p4study_title'),
                   model_uri=AK_SCHEMA.V1p4study_title, domain=None, range=Optional[str])

slots.V1p4study_type = Slot(uri=RDF.type, name="V1p4study_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p4study_type, domain=None, range=Optional[Union[str, "V1p4StudyType"]])

slots.V1p4study_description = Slot(uri=AK_SCHEMA.V1p4study_description, name="V1p4study_description", curie=AK_SCHEMA.curie('V1p4study_description'),
                   model_uri=AK_SCHEMA.V1p4study_description, domain=None, range=Optional[str])

slots.V1p4inclusion_exclusion_criteria = Slot(uri=AK_SCHEMA.V1p4inclusion_exclusion_criteria, name="V1p4inclusion_exclusion_criteria", curie=AK_SCHEMA.curie('V1p4inclusion_exclusion_criteria'),
                   model_uri=AK_SCHEMA.V1p4inclusion_exclusion_criteria, domain=None, range=Optional[str])

slots.V1p4grants = Slot(uri=AK_SCHEMA.V1p4grants, name="V1p4grants", curie=AK_SCHEMA.curie('V1p4grants'),
                   model_uri=AK_SCHEMA.V1p4grants, domain=None, range=Optional[str])

slots.V1p4contributors = Slot(uri=AK_SCHEMA.V1p4contributors, name="V1p4contributors", curie=AK_SCHEMA.curie('V1p4contributors'),
                   model_uri=AK_SCHEMA.V1p4contributors, domain=None, range=Optional[Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]]])

slots.V1p4keywords_study = Slot(uri=AK_SCHEMA.V1p4keywords_study, name="V1p4keywords_study", curie=AK_SCHEMA.curie('V1p4keywords_study'),
                   model_uri=AK_SCHEMA.V1p4keywords_study, domain=None, range=Optional[Union[Union[str, "V1p4KeywordsStudy"], List[Union[str, "V1p4KeywordsStudy"]]]])

slots.V1p4adc_publish_date = Slot(uri=AK_SCHEMA.V1p4adc_publish_date, name="V1p4adc_publish_date", curie=AK_SCHEMA.curie('V1p4adc_publish_date'),
                   model_uri=AK_SCHEMA.V1p4adc_publish_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.V1p4adc_update_date = Slot(uri=AK_SCHEMA.V1p4adc_update_date, name="V1p4adc_update_date", curie=AK_SCHEMA.curie('V1p4adc_update_date'),
                   model_uri=AK_SCHEMA.V1p4adc_update_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.V1p4subject_id = Slot(uri=AK_SCHEMA.V1p4subject_id, name="V1p4subject_id", curie=AK_SCHEMA.curie('V1p4subject_id'),
                   model_uri=AK_SCHEMA.V1p4subject_id, domain=None, range=Optional[str])

slots.V1p4synthetic = Slot(uri=AK_SCHEMA.V1p4synthetic, name="V1p4synthetic", curie=AK_SCHEMA.curie('V1p4synthetic'),
                   model_uri=AK_SCHEMA.V1p4synthetic, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4sex = Slot(uri=AK_SCHEMA.V1p4sex, name="V1p4sex", curie=AK_SCHEMA.curie('V1p4sex'),
                   model_uri=AK_SCHEMA.V1p4sex, domain=None, range=Optional[Union[str, "V1p4Sex"]])

slots.V1p4age = Slot(uri=AK_SCHEMA.V1p4age, name="V1p4age", curie=AK_SCHEMA.curie('V1p4age'),
                   model_uri=AK_SCHEMA.V1p4age, domain=None, range=Optional[Union[dict, V1p4TimeInterval]])

slots.V1p4age_event = Slot(uri=AK_SCHEMA.V1p4age_event, name="V1p4age_event", curie=AK_SCHEMA.curie('V1p4age_event'),
                   model_uri=AK_SCHEMA.V1p4age_event, domain=None, range=Optional[str])

slots.V1p4ancestry_population = Slot(uri=AK_SCHEMA.V1p4ancestry_population, name="V1p4ancestry_population", curie=AK_SCHEMA.curie('V1p4ancestry_population'),
                   model_uri=AK_SCHEMA.V1p4ancestry_population, domain=None, range=Optional[Union[str, "V1p4AncestryPopulation"]])

slots.V1p4location_birth = Slot(uri=AK_SCHEMA.V1p4location_birth, name="V1p4location_birth", curie=AK_SCHEMA.curie('V1p4location_birth'),
                   model_uri=AK_SCHEMA.V1p4location_birth, domain=None, range=Optional[Union[str, "V1p4LocationBirth"]])

slots.V1p4ethnicity = Slot(uri=AK_SCHEMA.V1p4ethnicity, name="V1p4ethnicity", curie=AK_SCHEMA.curie('V1p4ethnicity'),
                   model_uri=AK_SCHEMA.V1p4ethnicity, domain=None, range=Optional[str])

slots.V1p4race = Slot(uri=AK_SCHEMA.V1p4race, name="V1p4race", curie=AK_SCHEMA.curie('V1p4race'),
                   model_uri=AK_SCHEMA.V1p4race, domain=None, range=Optional[str])

slots.V1p4strain_name = Slot(uri=AK_SCHEMA.V1p4strain_name, name="V1p4strain_name", curie=AK_SCHEMA.curie('V1p4strain_name'),
                   model_uri=AK_SCHEMA.V1p4strain_name, domain=None, range=Optional[str])

slots.V1p4linked_subjects = Slot(uri=AK_SCHEMA.V1p4linked_subjects, name="V1p4linked_subjects", curie=AK_SCHEMA.curie('V1p4linked_subjects'),
                   model_uri=AK_SCHEMA.V1p4linked_subjects, domain=None, range=Optional[str])

slots.V1p4link_type = Slot(uri=RDF.type, name="V1p4link_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p4link_type, domain=None, range=Optional[str])

slots.V1p4diagnosis = Slot(uri=AK_SCHEMA.V1p4diagnosis, name="V1p4diagnosis", curie=AK_SCHEMA.curie('V1p4diagnosis'),
                   model_uri=AK_SCHEMA.V1p4diagnosis, domain=None, range=Optional[Union[Union[dict, V1p4Diagnosis], List[Union[dict, V1p4Diagnosis]]]])

slots.V1p4genotype = Slot(uri=AK_SCHEMA.V1p4genotype, name="V1p4genotype", curie=AK_SCHEMA.curie('V1p4genotype'),
                   model_uri=AK_SCHEMA.V1p4genotype, domain=None, range=Optional[Union[dict, V1p4SubjectGenotype]])

slots.V1p4study_group_description = Slot(uri=AK_SCHEMA.V1p4study_group_description, name="V1p4study_group_description", curie=AK_SCHEMA.curie('V1p4study_group_description'),
                   model_uri=AK_SCHEMA.V1p4study_group_description, domain=None, range=Optional[str])

slots.V1p4diagnosis_timepoint = Slot(uri=AK_SCHEMA.V1p4diagnosis_timepoint, name="V1p4diagnosis_timepoint", curie=AK_SCHEMA.curie('V1p4diagnosis_timepoint'),
                   model_uri=AK_SCHEMA.V1p4diagnosis_timepoint, domain=None, range=Optional[Union[dict, V1p4TimePoint]])

slots.V1p4disease_diagnosis = Slot(uri=AK_SCHEMA.V1p4disease_diagnosis, name="V1p4disease_diagnosis", curie=AK_SCHEMA.curie('V1p4disease_diagnosis'),
                   model_uri=AK_SCHEMA.V1p4disease_diagnosis, domain=None, range=Optional[Union[str, "V1p4DiseaseDiagnosis"]])

slots.V1p4disease_length = Slot(uri=AK_SCHEMA.V1p4disease_length, name="V1p4disease_length", curie=AK_SCHEMA.curie('V1p4disease_length'),
                   model_uri=AK_SCHEMA.V1p4disease_length, domain=None, range=Optional[Union[dict, V1p4TimeQuantity]])

slots.V1p4disease_stage = Slot(uri=AK_SCHEMA.V1p4disease_stage, name="V1p4disease_stage", curie=AK_SCHEMA.curie('V1p4disease_stage'),
                   model_uri=AK_SCHEMA.V1p4disease_stage, domain=None, range=Optional[str])

slots.V1p4prior_therapies = Slot(uri=AK_SCHEMA.V1p4prior_therapies, name="V1p4prior_therapies", curie=AK_SCHEMA.curie('V1p4prior_therapies'),
                   model_uri=AK_SCHEMA.V1p4prior_therapies, domain=None, range=Optional[str])

slots.V1p4immunogen = Slot(uri=AK_SCHEMA.V1p4immunogen, name="V1p4immunogen", curie=AK_SCHEMA.curie('V1p4immunogen'),
                   model_uri=AK_SCHEMA.V1p4immunogen, domain=None, range=Optional[str])

slots.V1p4intervention = Slot(uri=AK_SCHEMA.V1p4intervention, name="V1p4intervention", curie=AK_SCHEMA.curie('V1p4intervention'),
                   model_uri=AK_SCHEMA.V1p4intervention, domain=None, range=Optional[str])

slots.V1p4medical_history = Slot(uri=AK_SCHEMA.V1p4medical_history, name="V1p4medical_history", curie=AK_SCHEMA.curie('V1p4medical_history'),
                   model_uri=AK_SCHEMA.V1p4medical_history, domain=None, range=Optional[str])

slots.V1p4sample_id = Slot(uri=AK_SCHEMA.V1p4sample_id, name="V1p4sample_id", curie=AK_SCHEMA.curie('V1p4sample_id'),
                   model_uri=AK_SCHEMA.V1p4sample_id, domain=None, range=Optional[str])

slots.V1p4sample_type = Slot(uri=RDF.type, name="V1p4sample_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p4sample_type, domain=None, range=Optional[str])

slots.V1p4tissue = Slot(uri=AK_SCHEMA.V1p4tissue, name="V1p4tissue", curie=AK_SCHEMA.curie('V1p4tissue'),
                   model_uri=AK_SCHEMA.V1p4tissue, domain=None, range=Optional[Union[str, "V1p4Tissue"]])

slots.V1p4anatomic_site = Slot(uri=AK_SCHEMA.V1p4anatomic_site, name="V1p4anatomic_site", curie=AK_SCHEMA.curie('V1p4anatomic_site'),
                   model_uri=AK_SCHEMA.V1p4anatomic_site, domain=None, range=Optional[str])

slots.V1p4disease_state_sample = Slot(uri=AK_SCHEMA.V1p4disease_state_sample, name="V1p4disease_state_sample", curie=AK_SCHEMA.curie('V1p4disease_state_sample'),
                   model_uri=AK_SCHEMA.V1p4disease_state_sample, domain=None, range=Optional[str])

slots.V1p4collection_time_point_relative = Slot(uri=AK_SCHEMA.V1p4collection_time_point_relative, name="V1p4collection_time_point_relative", curie=AK_SCHEMA.curie('V1p4collection_time_point_relative'),
                   model_uri=AK_SCHEMA.V1p4collection_time_point_relative, domain=None, range=Optional[Union[dict, V1p4TimePoint]])

slots.V1p4collection_location = Slot(uri=AK_SCHEMA.V1p4collection_location, name="V1p4collection_location", curie=AK_SCHEMA.curie('V1p4collection_location'),
                   model_uri=AK_SCHEMA.V1p4collection_location, domain=None, range=Optional[Union[str, "V1p4CollectionLocation"]])

slots.V1p4biomaterial_provider = Slot(uri=AK_SCHEMA.V1p4biomaterial_provider, name="V1p4biomaterial_provider", curie=AK_SCHEMA.curie('V1p4biomaterial_provider'),
                   model_uri=AK_SCHEMA.V1p4biomaterial_provider, domain=None, range=Optional[str])

slots.V1p4tissue_processing = Slot(uri=AK_SCHEMA.V1p4tissue_processing, name="V1p4tissue_processing", curie=AK_SCHEMA.curie('V1p4tissue_processing'),
                   model_uri=AK_SCHEMA.V1p4tissue_processing, domain=None, range=Optional[str])

slots.V1p4cell_subset = Slot(uri=AK_SCHEMA.V1p4cell_subset, name="V1p4cell_subset", curie=AK_SCHEMA.curie('V1p4cell_subset'),
                   model_uri=AK_SCHEMA.V1p4cell_subset, domain=None, range=Optional[Union[str, "V1p4CellSubset"]])

slots.V1p4cell_phenotype = Slot(uri=AK_SCHEMA.V1p4cell_phenotype, name="V1p4cell_phenotype", curie=AK_SCHEMA.curie('V1p4cell_phenotype'),
                   model_uri=AK_SCHEMA.V1p4cell_phenotype, domain=None, range=Optional[str])

slots.V1p4cell_label = Slot(uri=AK_SCHEMA.V1p4cell_label, name="V1p4cell_label", curie=AK_SCHEMA.curie('V1p4cell_label'),
                   model_uri=AK_SCHEMA.V1p4cell_label, domain=None, range=Optional[str])

slots.V1p4cell_species = Slot(uri=AK_SCHEMA.V1p4cell_species, name="V1p4cell_species", curie=AK_SCHEMA.curie('V1p4cell_species'),
                   model_uri=AK_SCHEMA.V1p4cell_species, domain=None, range=Optional[Union[str, "V1p4CellSpecies"]])

slots.V1p4single_cell = Slot(uri=AK_SCHEMA.V1p4single_cell, name="V1p4single_cell", curie=AK_SCHEMA.curie('V1p4single_cell'),
                   model_uri=AK_SCHEMA.V1p4single_cell, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4cell_number = Slot(uri=AK_SCHEMA.V1p4cell_number, name="V1p4cell_number", curie=AK_SCHEMA.curie('V1p4cell_number'),
                   model_uri=AK_SCHEMA.V1p4cell_number, domain=None, range=Optional[int])

slots.V1p4cells_per_reaction = Slot(uri=AK_SCHEMA.V1p4cells_per_reaction, name="V1p4cells_per_reaction", curie=AK_SCHEMA.curie('V1p4cells_per_reaction'),
                   model_uri=AK_SCHEMA.V1p4cells_per_reaction, domain=None, range=Optional[int])

slots.V1p4cell_storage = Slot(uri=AK_SCHEMA.V1p4cell_storage, name="V1p4cell_storage", curie=AK_SCHEMA.curie('V1p4cell_storage'),
                   model_uri=AK_SCHEMA.V1p4cell_storage, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4cell_quality = Slot(uri=AK_SCHEMA.V1p4cell_quality, name="V1p4cell_quality", curie=AK_SCHEMA.curie('V1p4cell_quality'),
                   model_uri=AK_SCHEMA.V1p4cell_quality, domain=None, range=Optional[str])

slots.V1p4cell_isolation = Slot(uri=AK_SCHEMA.V1p4cell_isolation, name="V1p4cell_isolation", curie=AK_SCHEMA.curie('V1p4cell_isolation'),
                   model_uri=AK_SCHEMA.V1p4cell_isolation, domain=None, range=Optional[str])

slots.V1p4cell_processing_protocol = Slot(uri=AK_SCHEMA.V1p4cell_processing_protocol, name="V1p4cell_processing_protocol", curie=AK_SCHEMA.curie('V1p4cell_processing_protocol'),
                   model_uri=AK_SCHEMA.V1p4cell_processing_protocol, domain=None, range=Optional[str])

slots.V1p4pcr_target_locus = Slot(uri=AK_SCHEMA.V1p4pcr_target_locus, name="V1p4pcr_target_locus", curie=AK_SCHEMA.curie('V1p4pcr_target_locus'),
                   model_uri=AK_SCHEMA.V1p4pcr_target_locus, domain=None, range=Optional[Union[str, "V1p4PcrTargetLocus"]])

slots.V1p4forward_pcr_primer_target_location = Slot(uri=AK_SCHEMA.V1p4forward_pcr_primer_target_location, name="V1p4forward_pcr_primer_target_location", curie=AK_SCHEMA.curie('V1p4forward_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.V1p4forward_pcr_primer_target_location, domain=None, range=Optional[str])

slots.V1p4reverse_pcr_primer_target_location = Slot(uri=AK_SCHEMA.V1p4reverse_pcr_primer_target_location, name="V1p4reverse_pcr_primer_target_location", curie=AK_SCHEMA.curie('V1p4reverse_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.V1p4reverse_pcr_primer_target_location, domain=None, range=Optional[str])

slots.V1p4template_class = Slot(uri=AK_SCHEMA.V1p4template_class, name="V1p4template_class", curie=AK_SCHEMA.curie('V1p4template_class'),
                   model_uri=AK_SCHEMA.V1p4template_class, domain=None, range=Optional[Union[str, "V1p4TemplateClass"]])

slots.V1p4template_quality = Slot(uri=AK_SCHEMA.V1p4template_quality, name="V1p4template_quality", curie=AK_SCHEMA.curie('V1p4template_quality'),
                   model_uri=AK_SCHEMA.V1p4template_quality, domain=None, range=Optional[str])

slots.V1p4template_amount = Slot(uri=AK_SCHEMA.V1p4template_amount, name="V1p4template_amount", curie=AK_SCHEMA.curie('V1p4template_amount'),
                   model_uri=AK_SCHEMA.V1p4template_amount, domain=None, range=Optional[Union[dict, V1p4PhysicalQuantity]])

slots.V1p4library_generation_method = Slot(uri=AK_SCHEMA.V1p4library_generation_method, name="V1p4library_generation_method", curie=AK_SCHEMA.curie('V1p4library_generation_method'),
                   model_uri=AK_SCHEMA.V1p4library_generation_method, domain=None, range=Optional[Union[str, "V1p4LibraryGenerationMethod"]])

slots.V1p4library_generation_protocol = Slot(uri=AK_SCHEMA.V1p4library_generation_protocol, name="V1p4library_generation_protocol", curie=AK_SCHEMA.curie('V1p4library_generation_protocol'),
                   model_uri=AK_SCHEMA.V1p4library_generation_protocol, domain=None, range=Optional[str])

slots.V1p4library_generation_kit_version = Slot(uri=AK_SCHEMA.V1p4library_generation_kit_version, name="V1p4library_generation_kit_version", curie=AK_SCHEMA.curie('V1p4library_generation_kit_version'),
                   model_uri=AK_SCHEMA.V1p4library_generation_kit_version, domain=None, range=Optional[str])

slots.V1p4pcr_target = Slot(uri=AK_SCHEMA.V1p4pcr_target, name="V1p4pcr_target", curie=AK_SCHEMA.curie('V1p4pcr_target'),
                   model_uri=AK_SCHEMA.V1p4pcr_target, domain=None, range=Optional[Union[Union[dict, V1p4PCRTarget], List[Union[dict, V1p4PCRTarget]]]])

slots.V1p4complete_sequences = Slot(uri=AK_SCHEMA.V1p4complete_sequences, name="V1p4complete_sequences", curie=AK_SCHEMA.curie('V1p4complete_sequences'),
                   model_uri=AK_SCHEMA.V1p4complete_sequences, domain=None, range=Optional[Union[str, "V1p4CompleteSequences"]])

slots.V1p4physical_linkage = Slot(uri=AK_SCHEMA.V1p4physical_linkage, name="V1p4physical_linkage", curie=AK_SCHEMA.curie('V1p4physical_linkage'),
                   model_uri=AK_SCHEMA.V1p4physical_linkage, domain=None, range=Optional[Union[str, "V1p4PhysicalLinkage"]])

slots.V1p4sequencing_run_id = Slot(uri=AK_SCHEMA.V1p4sequencing_run_id, name="V1p4sequencing_run_id", curie=AK_SCHEMA.curie('V1p4sequencing_run_id'),
                   model_uri=AK_SCHEMA.V1p4sequencing_run_id, domain=None, range=Optional[str])

slots.V1p4total_reads_passing_qc_filter = Slot(uri=AK_SCHEMA.V1p4total_reads_passing_qc_filter, name="V1p4total_reads_passing_qc_filter", curie=AK_SCHEMA.curie('V1p4total_reads_passing_qc_filter'),
                   model_uri=AK_SCHEMA.V1p4total_reads_passing_qc_filter, domain=None, range=Optional[int])

slots.V1p4sequencing_platform = Slot(uri=AK_SCHEMA.V1p4sequencing_platform, name="V1p4sequencing_platform", curie=AK_SCHEMA.curie('V1p4sequencing_platform'),
                   model_uri=AK_SCHEMA.V1p4sequencing_platform, domain=None, range=Optional[str])

slots.V1p4sequencing_facility = Slot(uri=AK_SCHEMA.V1p4sequencing_facility, name="V1p4sequencing_facility", curie=AK_SCHEMA.curie('V1p4sequencing_facility'),
                   model_uri=AK_SCHEMA.V1p4sequencing_facility, domain=None, range=Optional[str])

slots.V1p4sequencing_run_date = Slot(uri=AK_SCHEMA.V1p4sequencing_run_date, name="V1p4sequencing_run_date", curie=AK_SCHEMA.curie('V1p4sequencing_run_date'),
                   model_uri=AK_SCHEMA.V1p4sequencing_run_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.V1p4sequencing_kit = Slot(uri=AK_SCHEMA.V1p4sequencing_kit, name="V1p4sequencing_kit", curie=AK_SCHEMA.curie('V1p4sequencing_kit'),
                   model_uri=AK_SCHEMA.V1p4sequencing_kit, domain=None, range=Optional[str])

slots.V1p4sequencing_files = Slot(uri=AK_SCHEMA.V1p4sequencing_files, name="V1p4sequencing_files", curie=AK_SCHEMA.curie('V1p4sequencing_files'),
                   model_uri=AK_SCHEMA.V1p4sequencing_files, domain=None, range=Optional[Union[dict, V1p4SequencingData]])

slots.V1p4sequencing_data_id = Slot(uri=AK_SCHEMA.V1p4sequencing_data_id, name="V1p4sequencing_data_id", curie=AK_SCHEMA.curie('V1p4sequencing_data_id'),
                   model_uri=AK_SCHEMA.V1p4sequencing_data_id, domain=None, range=Optional[str])

slots.V1p4file_type = Slot(uri=RDF.type, name="V1p4file_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p4file_type, domain=None, range=Optional[Union[str, "V1p4FileType"]])

slots.V1p4filename = Slot(uri=AK_SCHEMA.V1p4filename, name="V1p4filename", curie=AK_SCHEMA.curie('V1p4filename'),
                   model_uri=AK_SCHEMA.V1p4filename, domain=None, range=Optional[str])

slots.V1p4read_direction = Slot(uri=AK_SCHEMA.V1p4read_direction, name="V1p4read_direction", curie=AK_SCHEMA.curie('V1p4read_direction'),
                   model_uri=AK_SCHEMA.V1p4read_direction, domain=None, range=Optional[Union[str, "V1p4ReadDirection"]])

slots.V1p4read_length = Slot(uri=AK_SCHEMA.V1p4read_length, name="V1p4read_length", curie=AK_SCHEMA.curie('V1p4read_length'),
                   model_uri=AK_SCHEMA.V1p4read_length, domain=None, range=Optional[int])

slots.V1p4paired_filename = Slot(uri=AK_SCHEMA.V1p4paired_filename, name="V1p4paired_filename", curie=AK_SCHEMA.curie('V1p4paired_filename'),
                   model_uri=AK_SCHEMA.V1p4paired_filename, domain=None, range=Optional[str])

slots.V1p4paired_read_direction = Slot(uri=AK_SCHEMA.V1p4paired_read_direction, name="V1p4paired_read_direction", curie=AK_SCHEMA.curie('V1p4paired_read_direction'),
                   model_uri=AK_SCHEMA.V1p4paired_read_direction, domain=None, range=Optional[Union[str, "V1p4PairedReadDirection"]])

slots.V1p4paired_read_length = Slot(uri=AK_SCHEMA.V1p4paired_read_length, name="V1p4paired_read_length", curie=AK_SCHEMA.curie('V1p4paired_read_length'),
                   model_uri=AK_SCHEMA.V1p4paired_read_length, domain=None, range=Optional[int])

slots.V1p4index_filename = Slot(uri=AK_SCHEMA.V1p4index_filename, name="V1p4index_filename", curie=AK_SCHEMA.curie('V1p4index_filename'),
                   model_uri=AK_SCHEMA.V1p4index_filename, domain=None, range=Optional[str])

slots.V1p4index_length = Slot(uri=AK_SCHEMA.V1p4index_length, name="V1p4index_length", curie=AK_SCHEMA.curie('V1p4index_length'),
                   model_uri=AK_SCHEMA.V1p4index_length, domain=None, range=Optional[int])

slots.V1p4data_processing_id = Slot(uri=AK_SCHEMA.V1p4data_processing_id, name="V1p4data_processing_id", curie=AK_SCHEMA.curie('V1p4data_processing_id'),
                   model_uri=AK_SCHEMA.V1p4data_processing_id, domain=None, range=Optional[str])

slots.V1p4primary_annotation = Slot(uri=AK_SCHEMA.V1p4primary_annotation, name="V1p4primary_annotation", curie=AK_SCHEMA.curie('V1p4primary_annotation'),
                   model_uri=AK_SCHEMA.V1p4primary_annotation, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4software_versions = Slot(uri=AK_SCHEMA.V1p4software_versions, name="V1p4software_versions", curie=AK_SCHEMA.curie('V1p4software_versions'),
                   model_uri=AK_SCHEMA.V1p4software_versions, domain=None, range=Optional[str])

slots.V1p4paired_reads_assembly = Slot(uri=AK_SCHEMA.V1p4paired_reads_assembly, name="V1p4paired_reads_assembly", curie=AK_SCHEMA.curie('V1p4paired_reads_assembly'),
                   model_uri=AK_SCHEMA.V1p4paired_reads_assembly, domain=None, range=Optional[str])

slots.V1p4quality_thresholds = Slot(uri=AK_SCHEMA.V1p4quality_thresholds, name="V1p4quality_thresholds", curie=AK_SCHEMA.curie('V1p4quality_thresholds'),
                   model_uri=AK_SCHEMA.V1p4quality_thresholds, domain=None, range=Optional[str])

slots.V1p4primer_match_cutoffs = Slot(uri=AK_SCHEMA.V1p4primer_match_cutoffs, name="V1p4primer_match_cutoffs", curie=AK_SCHEMA.curie('V1p4primer_match_cutoffs'),
                   model_uri=AK_SCHEMA.V1p4primer_match_cutoffs, domain=None, range=Optional[str])

slots.V1p4collapsing_method = Slot(uri=AK_SCHEMA.V1p4collapsing_method, name="V1p4collapsing_method", curie=AK_SCHEMA.curie('V1p4collapsing_method'),
                   model_uri=AK_SCHEMA.V1p4collapsing_method, domain=None, range=Optional[str])

slots.V1p4data_processing_protocols = Slot(uri=AK_SCHEMA.V1p4data_processing_protocols, name="V1p4data_processing_protocols", curie=AK_SCHEMA.curie('V1p4data_processing_protocols'),
                   model_uri=AK_SCHEMA.V1p4data_processing_protocols, domain=None, range=Optional[str])

slots.V1p4data_processing_files = Slot(uri=AK_SCHEMA.V1p4data_processing_files, name="V1p4data_processing_files", curie=AK_SCHEMA.curie('V1p4data_processing_files'),
                   model_uri=AK_SCHEMA.V1p4data_processing_files, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4germline_database = Slot(uri=AK_SCHEMA.V1p4germline_database, name="V1p4germline_database", curie=AK_SCHEMA.curie('V1p4germline_database'),
                   model_uri=AK_SCHEMA.V1p4germline_database, domain=None, range=Optional[str])

slots.V1p4analysis_provenance_id = Slot(uri=AK_SCHEMA.V1p4analysis_provenance_id, name="V1p4analysis_provenance_id", curie=AK_SCHEMA.curie('V1p4analysis_provenance_id'),
                   model_uri=AK_SCHEMA.V1p4analysis_provenance_id, domain=None, range=Optional[str])

slots.V1p4repertoire_id = Slot(uri=AK_SCHEMA.V1p4repertoire_id, name="V1p4repertoire_id", curie=AK_SCHEMA.curie('V1p4repertoire_id'),
                   model_uri=AK_SCHEMA.V1p4repertoire_id, domain=None, range=Optional[str])

slots.V1p4repertoire_name = Slot(uri=AK_SCHEMA.V1p4repertoire_name, name="V1p4repertoire_name", curie=AK_SCHEMA.curie('V1p4repertoire_name'),
                   model_uri=AK_SCHEMA.V1p4repertoire_name, domain=None, range=Optional[str])

slots.V1p4repertoire_description = Slot(uri=AK_SCHEMA.V1p4repertoire_description, name="V1p4repertoire_description", curie=AK_SCHEMA.curie('V1p4repertoire_description'),
                   model_uri=AK_SCHEMA.V1p4repertoire_description, domain=None, range=Optional[str])

slots.V1p4study = Slot(uri=AK_SCHEMA.V1p4study, name="V1p4study", curie=AK_SCHEMA.curie('V1p4study'),
                   model_uri=AK_SCHEMA.V1p4study, domain=None, range=Optional[Union[dict, V1p4Study]])

slots.V1p4subject = Slot(uri=AK_SCHEMA.V1p4subject, name="V1p4subject", curie=AK_SCHEMA.curie('V1p4subject'),
                   model_uri=AK_SCHEMA.V1p4subject, domain=None, range=Optional[Union[dict, V1p4Subject]])

slots.V1p4sample = Slot(uri=AK_SCHEMA.V1p4sample, name="V1p4sample", curie=AK_SCHEMA.curie('V1p4sample'),
                   model_uri=AK_SCHEMA.V1p4sample, domain=None, range=Optional[Union[Union[dict, V1p4SampleProcessing], List[Union[dict, V1p4SampleProcessing]]]])

slots.V1p4data_processing = Slot(uri=AK_SCHEMA.V1p4data_processing, name="V1p4data_processing", curie=AK_SCHEMA.curie('V1p4data_processing'),
                   model_uri=AK_SCHEMA.V1p4data_processing, domain=None, range=Optional[Union[Union[dict, V1p4DataProcessing], List[Union[dict, V1p4DataProcessing]]]])

slots.V1p4repertoire_group_id = Slot(uri=AK_SCHEMA.V1p4repertoire_group_id, name="V1p4repertoire_group_id", curie=AK_SCHEMA.curie('V1p4repertoire_group_id'),
                   model_uri=AK_SCHEMA.V1p4repertoire_group_id, domain=None, range=Optional[str])

slots.V1p4repertoire_group_name = Slot(uri=AK_SCHEMA.V1p4repertoire_group_name, name="V1p4repertoire_group_name", curie=AK_SCHEMA.curie('V1p4repertoire_group_name'),
                   model_uri=AK_SCHEMA.V1p4repertoire_group_name, domain=None, range=Optional[str])

slots.V1p4repertoire_group_description = Slot(uri=AK_SCHEMA.V1p4repertoire_group_description, name="V1p4repertoire_group_description", curie=AK_SCHEMA.curie('V1p4repertoire_group_description'),
                   model_uri=AK_SCHEMA.V1p4repertoire_group_description, domain=None, range=Optional[str])

slots.V1p4repertoires = Slot(uri=AK_SCHEMA.V1p4repertoires, name="V1p4repertoires", curie=AK_SCHEMA.curie('V1p4repertoires'),
                   model_uri=AK_SCHEMA.V1p4repertoires, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4segment = Slot(uri=AK_SCHEMA.V1p4segment, name="V1p4segment", curie=AK_SCHEMA.curie('V1p4segment'),
                   model_uri=AK_SCHEMA.V1p4segment, domain=None, range=Optional[str])

slots.V1p4rev_comp = Slot(uri=AK_SCHEMA.V1p4rev_comp, name="V1p4rev_comp", curie=AK_SCHEMA.curie('V1p4rev_comp'),
                   model_uri=AK_SCHEMA.V1p4rev_comp, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4call = Slot(uri=AK_SCHEMA.V1p4call, name="V1p4call", curie=AK_SCHEMA.curie('V1p4call'),
                   model_uri=AK_SCHEMA.V1p4call, domain=None, range=Optional[str])

slots.V1p4score = Slot(uri=AK_SCHEMA.V1p4score, name="V1p4score", curie=AK_SCHEMA.curie('V1p4score'),
                   model_uri=AK_SCHEMA.V1p4score, domain=None, range=Optional[float])

slots.V1p4identity = Slot(uri=AK_SCHEMA.V1p4identity, name="V1p4identity", curie=AK_SCHEMA.curie('V1p4identity'),
                   model_uri=AK_SCHEMA.V1p4identity, domain=None, range=Optional[float])

slots.V1p4support = Slot(uri=AK_SCHEMA.V1p4support, name="V1p4support", curie=AK_SCHEMA.curie('V1p4support'),
                   model_uri=AK_SCHEMA.V1p4support, domain=None, range=Optional[float])

slots.V1p4cigar = Slot(uri=AK_SCHEMA.V1p4cigar, name="V1p4cigar", curie=AK_SCHEMA.curie('V1p4cigar'),
                   model_uri=AK_SCHEMA.V1p4cigar, domain=None, range=Optional[str])

slots.V1p4germline_start = Slot(uri=AK_SCHEMA.V1p4germline_start, name="V1p4germline_start", curie=AK_SCHEMA.curie('V1p4germline_start'),
                   model_uri=AK_SCHEMA.V1p4germline_start, domain=None, range=Optional[int])

slots.V1p4germline_end = Slot(uri=AK_SCHEMA.V1p4germline_end, name="V1p4germline_end", curie=AK_SCHEMA.curie('V1p4germline_end'),
                   model_uri=AK_SCHEMA.V1p4germline_end, domain=None, range=Optional[int])

slots.V1p4rank = Slot(uri=AK_SCHEMA.V1p4rank, name="V1p4rank", curie=AK_SCHEMA.curie('V1p4rank'),
                   model_uri=AK_SCHEMA.V1p4rank, domain=None, range=Optional[int])

slots.V1p4quality = Slot(uri=AK_SCHEMA.V1p4quality, name="V1p4quality", curie=AK_SCHEMA.curie('V1p4quality'),
                   model_uri=AK_SCHEMA.V1p4quality, domain=None, range=Optional[str])

slots.V1p4sequence_aa = Slot(uri=AK_SCHEMA.V1p4sequence_aa, name="V1p4sequence_aa", curie=AK_SCHEMA.curie('V1p4sequence_aa'),
                   model_uri=AK_SCHEMA.V1p4sequence_aa, domain=None, range=Optional[str])

slots.V1p4productive = Slot(uri=AK_SCHEMA.V1p4productive, name="V1p4productive", curie=AK_SCHEMA.curie('V1p4productive'),
                   model_uri=AK_SCHEMA.V1p4productive, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4vj_in_frame = Slot(uri=AK_SCHEMA.V1p4vj_in_frame, name="V1p4vj_in_frame", curie=AK_SCHEMA.curie('V1p4vj_in_frame'),
                   model_uri=AK_SCHEMA.V1p4vj_in_frame, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4stop_codon = Slot(uri=AK_SCHEMA.V1p4stop_codon, name="V1p4stop_codon", curie=AK_SCHEMA.curie('V1p4stop_codon'),
                   model_uri=AK_SCHEMA.V1p4stop_codon, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4complete_vdj = Slot(uri=AK_SCHEMA.V1p4complete_vdj, name="V1p4complete_vdj", curie=AK_SCHEMA.curie('V1p4complete_vdj'),
                   model_uri=AK_SCHEMA.V1p4complete_vdj, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4locus_species = Slot(uri=AK_SCHEMA.V1p4locus_species, name="V1p4locus_species", curie=AK_SCHEMA.curie('V1p4locus_species'),
                   model_uri=AK_SCHEMA.V1p4locus_species, domain=None, range=Optional[Union[str, "V1p4LocusSpecies"]])

slots.V1p4v_call = Slot(uri=AK_SCHEMA.V1p4v_call, name="V1p4v_call", curie=AK_SCHEMA.curie('V1p4v_call'),
                   model_uri=AK_SCHEMA.V1p4v_call, domain=None, range=Optional[str])

slots.V1p4d_call = Slot(uri=AK_SCHEMA.V1p4d_call, name="V1p4d_call", curie=AK_SCHEMA.curie('V1p4d_call'),
                   model_uri=AK_SCHEMA.V1p4d_call, domain=None, range=Optional[str])

slots.V1p4d2_call = Slot(uri=AK_SCHEMA.V1p4d2_call, name="V1p4d2_call", curie=AK_SCHEMA.curie('V1p4d2_call'),
                   model_uri=AK_SCHEMA.V1p4d2_call, domain=None, range=Optional[str])

slots.V1p4j_call = Slot(uri=AK_SCHEMA.V1p4j_call, name="V1p4j_call", curie=AK_SCHEMA.curie('V1p4j_call'),
                   model_uri=AK_SCHEMA.V1p4j_call, domain=None, range=Optional[str])

slots.V1p4c_call = Slot(uri=AK_SCHEMA.V1p4c_call, name="V1p4c_call", curie=AK_SCHEMA.curie('V1p4c_call'),
                   model_uri=AK_SCHEMA.V1p4c_call, domain=None, range=Optional[str])

slots.V1p4sequence_alignment = Slot(uri=AK_SCHEMA.V1p4sequence_alignment, name="V1p4sequence_alignment", curie=AK_SCHEMA.curie('V1p4sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p4sequence_alignment, domain=None, range=Optional[str])

slots.V1p4quality_alignment = Slot(uri=AK_SCHEMA.V1p4quality_alignment, name="V1p4quality_alignment", curie=AK_SCHEMA.curie('V1p4quality_alignment'),
                   model_uri=AK_SCHEMA.V1p4quality_alignment, domain=None, range=Optional[str])

slots.V1p4sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p4sequence_alignment_aa, name="V1p4sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p4sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p4germline_alignment = Slot(uri=AK_SCHEMA.V1p4germline_alignment, name="V1p4germline_alignment", curie=AK_SCHEMA.curie('V1p4germline_alignment'),
                   model_uri=AK_SCHEMA.V1p4germline_alignment, domain=None, range=Optional[str])

slots.V1p4germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p4germline_alignment_aa, name="V1p4germline_alignment_aa", curie=AK_SCHEMA.curie('V1p4germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p4junction = Slot(uri=AK_SCHEMA.V1p4junction, name="V1p4junction", curie=AK_SCHEMA.curie('V1p4junction'),
                   model_uri=AK_SCHEMA.V1p4junction, domain=None, range=Optional[str])

slots.V1p4junction_aa = Slot(uri=AK_SCHEMA.V1p4junction_aa, name="V1p4junction_aa", curie=AK_SCHEMA.curie('V1p4junction_aa'),
                   model_uri=AK_SCHEMA.V1p4junction_aa, domain=None, range=Optional[str])

slots.V1p4np1 = Slot(uri=AK_SCHEMA.V1p4np1, name="V1p4np1", curie=AK_SCHEMA.curie('V1p4np1'),
                   model_uri=AK_SCHEMA.V1p4np1, domain=None, range=Optional[str])

slots.V1p4np1_aa = Slot(uri=AK_SCHEMA.V1p4np1_aa, name="V1p4np1_aa", curie=AK_SCHEMA.curie('V1p4np1_aa'),
                   model_uri=AK_SCHEMA.V1p4np1_aa, domain=None, range=Optional[str])

slots.V1p4np2 = Slot(uri=AK_SCHEMA.V1p4np2, name="V1p4np2", curie=AK_SCHEMA.curie('V1p4np2'),
                   model_uri=AK_SCHEMA.V1p4np2, domain=None, range=Optional[str])

slots.V1p4np2_aa = Slot(uri=AK_SCHEMA.V1p4np2_aa, name="V1p4np2_aa", curie=AK_SCHEMA.curie('V1p4np2_aa'),
                   model_uri=AK_SCHEMA.V1p4np2_aa, domain=None, range=Optional[str])

slots.V1p4np3 = Slot(uri=AK_SCHEMA.V1p4np3, name="V1p4np3", curie=AK_SCHEMA.curie('V1p4np3'),
                   model_uri=AK_SCHEMA.V1p4np3, domain=None, range=Optional[str])

slots.V1p4np3_aa = Slot(uri=AK_SCHEMA.V1p4np3_aa, name="V1p4np3_aa", curie=AK_SCHEMA.curie('V1p4np3_aa'),
                   model_uri=AK_SCHEMA.V1p4np3_aa, domain=None, range=Optional[str])

slots.V1p4cdr1 = Slot(uri=AK_SCHEMA.V1p4cdr1, name="V1p4cdr1", curie=AK_SCHEMA.curie('V1p4cdr1'),
                   model_uri=AK_SCHEMA.V1p4cdr1, domain=None, range=Optional[str])

slots.V1p4cdr1_aa = Slot(uri=AK_SCHEMA.V1p4cdr1_aa, name="V1p4cdr1_aa", curie=AK_SCHEMA.curie('V1p4cdr1_aa'),
                   model_uri=AK_SCHEMA.V1p4cdr1_aa, domain=None, range=Optional[str])

slots.V1p4cdr2 = Slot(uri=AK_SCHEMA.V1p4cdr2, name="V1p4cdr2", curie=AK_SCHEMA.curie('V1p4cdr2'),
                   model_uri=AK_SCHEMA.V1p4cdr2, domain=None, range=Optional[str])

slots.V1p4cdr2_aa = Slot(uri=AK_SCHEMA.V1p4cdr2_aa, name="V1p4cdr2_aa", curie=AK_SCHEMA.curie('V1p4cdr2_aa'),
                   model_uri=AK_SCHEMA.V1p4cdr2_aa, domain=None, range=Optional[str])

slots.V1p4cdr3 = Slot(uri=AK_SCHEMA.V1p4cdr3, name="V1p4cdr3", curie=AK_SCHEMA.curie('V1p4cdr3'),
                   model_uri=AK_SCHEMA.V1p4cdr3, domain=None, range=Optional[str])

slots.V1p4cdr3_aa = Slot(uri=AK_SCHEMA.V1p4cdr3_aa, name="V1p4cdr3_aa", curie=AK_SCHEMA.curie('V1p4cdr3_aa'),
                   model_uri=AK_SCHEMA.V1p4cdr3_aa, domain=None, range=Optional[str])

slots.V1p4fwr1 = Slot(uri=AK_SCHEMA.V1p4fwr1, name="V1p4fwr1", curie=AK_SCHEMA.curie('V1p4fwr1'),
                   model_uri=AK_SCHEMA.V1p4fwr1, domain=None, range=Optional[str])

slots.V1p4fwr1_aa = Slot(uri=AK_SCHEMA.V1p4fwr1_aa, name="V1p4fwr1_aa", curie=AK_SCHEMA.curie('V1p4fwr1_aa'),
                   model_uri=AK_SCHEMA.V1p4fwr1_aa, domain=None, range=Optional[str])

slots.V1p4fwr2 = Slot(uri=AK_SCHEMA.V1p4fwr2, name="V1p4fwr2", curie=AK_SCHEMA.curie('V1p4fwr2'),
                   model_uri=AK_SCHEMA.V1p4fwr2, domain=None, range=Optional[str])

slots.V1p4fwr2_aa = Slot(uri=AK_SCHEMA.V1p4fwr2_aa, name="V1p4fwr2_aa", curie=AK_SCHEMA.curie('V1p4fwr2_aa'),
                   model_uri=AK_SCHEMA.V1p4fwr2_aa, domain=None, range=Optional[str])

slots.V1p4fwr3 = Slot(uri=AK_SCHEMA.V1p4fwr3, name="V1p4fwr3", curie=AK_SCHEMA.curie('V1p4fwr3'),
                   model_uri=AK_SCHEMA.V1p4fwr3, domain=None, range=Optional[str])

slots.V1p4fwr3_aa = Slot(uri=AK_SCHEMA.V1p4fwr3_aa, name="V1p4fwr3_aa", curie=AK_SCHEMA.curie('V1p4fwr3_aa'),
                   model_uri=AK_SCHEMA.V1p4fwr3_aa, domain=None, range=Optional[str])

slots.V1p4fwr4 = Slot(uri=AK_SCHEMA.V1p4fwr4, name="V1p4fwr4", curie=AK_SCHEMA.curie('V1p4fwr4'),
                   model_uri=AK_SCHEMA.V1p4fwr4, domain=None, range=Optional[str])

slots.V1p4fwr4_aa = Slot(uri=AK_SCHEMA.V1p4fwr4_aa, name="V1p4fwr4_aa", curie=AK_SCHEMA.curie('V1p4fwr4_aa'),
                   model_uri=AK_SCHEMA.V1p4fwr4_aa, domain=None, range=Optional[str])

slots.V1p4v_score = Slot(uri=AK_SCHEMA.V1p4v_score, name="V1p4v_score", curie=AK_SCHEMA.curie('V1p4v_score'),
                   model_uri=AK_SCHEMA.V1p4v_score, domain=None, range=Optional[float])

slots.V1p4v_identity = Slot(uri=AK_SCHEMA.V1p4v_identity, name="V1p4v_identity", curie=AK_SCHEMA.curie('V1p4v_identity'),
                   model_uri=AK_SCHEMA.V1p4v_identity, domain=None, range=Optional[float])

slots.V1p4v_support = Slot(uri=AK_SCHEMA.V1p4v_support, name="V1p4v_support", curie=AK_SCHEMA.curie('V1p4v_support'),
                   model_uri=AK_SCHEMA.V1p4v_support, domain=None, range=Optional[float])

slots.V1p4v_cigar = Slot(uri=AK_SCHEMA.V1p4v_cigar, name="V1p4v_cigar", curie=AK_SCHEMA.curie('V1p4v_cigar'),
                   model_uri=AK_SCHEMA.V1p4v_cigar, domain=None, range=Optional[str])

slots.V1p4d_score = Slot(uri=AK_SCHEMA.V1p4d_score, name="V1p4d_score", curie=AK_SCHEMA.curie('V1p4d_score'),
                   model_uri=AK_SCHEMA.V1p4d_score, domain=None, range=Optional[float])

slots.V1p4d_identity = Slot(uri=AK_SCHEMA.V1p4d_identity, name="V1p4d_identity", curie=AK_SCHEMA.curie('V1p4d_identity'),
                   model_uri=AK_SCHEMA.V1p4d_identity, domain=None, range=Optional[float])

slots.V1p4d_support = Slot(uri=AK_SCHEMA.V1p4d_support, name="V1p4d_support", curie=AK_SCHEMA.curie('V1p4d_support'),
                   model_uri=AK_SCHEMA.V1p4d_support, domain=None, range=Optional[float])

slots.V1p4d_cigar = Slot(uri=AK_SCHEMA.V1p4d_cigar, name="V1p4d_cigar", curie=AK_SCHEMA.curie('V1p4d_cigar'),
                   model_uri=AK_SCHEMA.V1p4d_cigar, domain=None, range=Optional[str])

slots.V1p4d2_score = Slot(uri=AK_SCHEMA.V1p4d2_score, name="V1p4d2_score", curie=AK_SCHEMA.curie('V1p4d2_score'),
                   model_uri=AK_SCHEMA.V1p4d2_score, domain=None, range=Optional[float])

slots.V1p4d2_identity = Slot(uri=AK_SCHEMA.V1p4d2_identity, name="V1p4d2_identity", curie=AK_SCHEMA.curie('V1p4d2_identity'),
                   model_uri=AK_SCHEMA.V1p4d2_identity, domain=None, range=Optional[float])

slots.V1p4d2_support = Slot(uri=AK_SCHEMA.V1p4d2_support, name="V1p4d2_support", curie=AK_SCHEMA.curie('V1p4d2_support'),
                   model_uri=AK_SCHEMA.V1p4d2_support, domain=None, range=Optional[float])

slots.V1p4d2_cigar = Slot(uri=AK_SCHEMA.V1p4d2_cigar, name="V1p4d2_cigar", curie=AK_SCHEMA.curie('V1p4d2_cigar'),
                   model_uri=AK_SCHEMA.V1p4d2_cigar, domain=None, range=Optional[str])

slots.V1p4j_score = Slot(uri=AK_SCHEMA.V1p4j_score, name="V1p4j_score", curie=AK_SCHEMA.curie('V1p4j_score'),
                   model_uri=AK_SCHEMA.V1p4j_score, domain=None, range=Optional[float])

slots.V1p4j_identity = Slot(uri=AK_SCHEMA.V1p4j_identity, name="V1p4j_identity", curie=AK_SCHEMA.curie('V1p4j_identity'),
                   model_uri=AK_SCHEMA.V1p4j_identity, domain=None, range=Optional[float])

slots.V1p4j_support = Slot(uri=AK_SCHEMA.V1p4j_support, name="V1p4j_support", curie=AK_SCHEMA.curie('V1p4j_support'),
                   model_uri=AK_SCHEMA.V1p4j_support, domain=None, range=Optional[float])

slots.V1p4j_cigar = Slot(uri=AK_SCHEMA.V1p4j_cigar, name="V1p4j_cigar", curie=AK_SCHEMA.curie('V1p4j_cigar'),
                   model_uri=AK_SCHEMA.V1p4j_cigar, domain=None, range=Optional[str])

slots.V1p4c_score = Slot(uri=AK_SCHEMA.V1p4c_score, name="V1p4c_score", curie=AK_SCHEMA.curie('V1p4c_score'),
                   model_uri=AK_SCHEMA.V1p4c_score, domain=None, range=Optional[float])

slots.V1p4c_identity = Slot(uri=AK_SCHEMA.V1p4c_identity, name="V1p4c_identity", curie=AK_SCHEMA.curie('V1p4c_identity'),
                   model_uri=AK_SCHEMA.V1p4c_identity, domain=None, range=Optional[float])

slots.V1p4c_support = Slot(uri=AK_SCHEMA.V1p4c_support, name="V1p4c_support", curie=AK_SCHEMA.curie('V1p4c_support'),
                   model_uri=AK_SCHEMA.V1p4c_support, domain=None, range=Optional[float])

slots.V1p4c_cigar = Slot(uri=AK_SCHEMA.V1p4c_cigar, name="V1p4c_cigar", curie=AK_SCHEMA.curie('V1p4c_cigar'),
                   model_uri=AK_SCHEMA.V1p4c_cigar, domain=None, range=Optional[str])

slots.V1p4v_sequence_start = Slot(uri=AK_SCHEMA.V1p4v_sequence_start, name="V1p4v_sequence_start", curie=AK_SCHEMA.curie('V1p4v_sequence_start'),
                   model_uri=AK_SCHEMA.V1p4v_sequence_start, domain=None, range=Optional[int])

slots.V1p4v_sequence_end = Slot(uri=AK_SCHEMA.V1p4v_sequence_end, name="V1p4v_sequence_end", curie=AK_SCHEMA.curie('V1p4v_sequence_end'),
                   model_uri=AK_SCHEMA.V1p4v_sequence_end, domain=None, range=Optional[int])

slots.V1p4v_germline_start = Slot(uri=AK_SCHEMA.V1p4v_germline_start, name="V1p4v_germline_start", curie=AK_SCHEMA.curie('V1p4v_germline_start'),
                   model_uri=AK_SCHEMA.V1p4v_germline_start, domain=None, range=Optional[int])

slots.V1p4v_germline_end = Slot(uri=AK_SCHEMA.V1p4v_germline_end, name="V1p4v_germline_end", curie=AK_SCHEMA.curie('V1p4v_germline_end'),
                   model_uri=AK_SCHEMA.V1p4v_germline_end, domain=None, range=Optional[int])

slots.V1p4v_alignment_start = Slot(uri=AK_SCHEMA.V1p4v_alignment_start, name="V1p4v_alignment_start", curie=AK_SCHEMA.curie('V1p4v_alignment_start'),
                   model_uri=AK_SCHEMA.V1p4v_alignment_start, domain=None, range=Optional[int])

slots.V1p4v_alignment_end = Slot(uri=AK_SCHEMA.V1p4v_alignment_end, name="V1p4v_alignment_end", curie=AK_SCHEMA.curie('V1p4v_alignment_end'),
                   model_uri=AK_SCHEMA.V1p4v_alignment_end, domain=None, range=Optional[int])

slots.V1p4d_sequence_start = Slot(uri=AK_SCHEMA.V1p4d_sequence_start, name="V1p4d_sequence_start", curie=AK_SCHEMA.curie('V1p4d_sequence_start'),
                   model_uri=AK_SCHEMA.V1p4d_sequence_start, domain=None, range=Optional[int])

slots.V1p4d_sequence_end = Slot(uri=AK_SCHEMA.V1p4d_sequence_end, name="V1p4d_sequence_end", curie=AK_SCHEMA.curie('V1p4d_sequence_end'),
                   model_uri=AK_SCHEMA.V1p4d_sequence_end, domain=None, range=Optional[int])

slots.V1p4d_germline_start = Slot(uri=AK_SCHEMA.V1p4d_germline_start, name="V1p4d_germline_start", curie=AK_SCHEMA.curie('V1p4d_germline_start'),
                   model_uri=AK_SCHEMA.V1p4d_germline_start, domain=None, range=Optional[int])

slots.V1p4d_germline_end = Slot(uri=AK_SCHEMA.V1p4d_germline_end, name="V1p4d_germline_end", curie=AK_SCHEMA.curie('V1p4d_germline_end'),
                   model_uri=AK_SCHEMA.V1p4d_germline_end, domain=None, range=Optional[int])

slots.V1p4d_alignment_start = Slot(uri=AK_SCHEMA.V1p4d_alignment_start, name="V1p4d_alignment_start", curie=AK_SCHEMA.curie('V1p4d_alignment_start'),
                   model_uri=AK_SCHEMA.V1p4d_alignment_start, domain=None, range=Optional[int])

slots.V1p4d_alignment_end = Slot(uri=AK_SCHEMA.V1p4d_alignment_end, name="V1p4d_alignment_end", curie=AK_SCHEMA.curie('V1p4d_alignment_end'),
                   model_uri=AK_SCHEMA.V1p4d_alignment_end, domain=None, range=Optional[int])

slots.V1p4d2_sequence_start = Slot(uri=AK_SCHEMA.V1p4d2_sequence_start, name="V1p4d2_sequence_start", curie=AK_SCHEMA.curie('V1p4d2_sequence_start'),
                   model_uri=AK_SCHEMA.V1p4d2_sequence_start, domain=None, range=Optional[int])

slots.V1p4d2_sequence_end = Slot(uri=AK_SCHEMA.V1p4d2_sequence_end, name="V1p4d2_sequence_end", curie=AK_SCHEMA.curie('V1p4d2_sequence_end'),
                   model_uri=AK_SCHEMA.V1p4d2_sequence_end, domain=None, range=Optional[int])

slots.V1p4d2_germline_start = Slot(uri=AK_SCHEMA.V1p4d2_germline_start, name="V1p4d2_germline_start", curie=AK_SCHEMA.curie('V1p4d2_germline_start'),
                   model_uri=AK_SCHEMA.V1p4d2_germline_start, domain=None, range=Optional[int])

slots.V1p4d2_germline_end = Slot(uri=AK_SCHEMA.V1p4d2_germline_end, name="V1p4d2_germline_end", curie=AK_SCHEMA.curie('V1p4d2_germline_end'),
                   model_uri=AK_SCHEMA.V1p4d2_germline_end, domain=None, range=Optional[int])

slots.V1p4d2_alignment_start = Slot(uri=AK_SCHEMA.V1p4d2_alignment_start, name="V1p4d2_alignment_start", curie=AK_SCHEMA.curie('V1p4d2_alignment_start'),
                   model_uri=AK_SCHEMA.V1p4d2_alignment_start, domain=None, range=Optional[int])

slots.V1p4d2_alignment_end = Slot(uri=AK_SCHEMA.V1p4d2_alignment_end, name="V1p4d2_alignment_end", curie=AK_SCHEMA.curie('V1p4d2_alignment_end'),
                   model_uri=AK_SCHEMA.V1p4d2_alignment_end, domain=None, range=Optional[int])

slots.V1p4j_sequence_start = Slot(uri=AK_SCHEMA.V1p4j_sequence_start, name="V1p4j_sequence_start", curie=AK_SCHEMA.curie('V1p4j_sequence_start'),
                   model_uri=AK_SCHEMA.V1p4j_sequence_start, domain=None, range=Optional[int])

slots.V1p4j_sequence_end = Slot(uri=AK_SCHEMA.V1p4j_sequence_end, name="V1p4j_sequence_end", curie=AK_SCHEMA.curie('V1p4j_sequence_end'),
                   model_uri=AK_SCHEMA.V1p4j_sequence_end, domain=None, range=Optional[int])

slots.V1p4j_germline_start = Slot(uri=AK_SCHEMA.V1p4j_germline_start, name="V1p4j_germline_start", curie=AK_SCHEMA.curie('V1p4j_germline_start'),
                   model_uri=AK_SCHEMA.V1p4j_germline_start, domain=None, range=Optional[int])

slots.V1p4j_germline_end = Slot(uri=AK_SCHEMA.V1p4j_germline_end, name="V1p4j_germline_end", curie=AK_SCHEMA.curie('V1p4j_germline_end'),
                   model_uri=AK_SCHEMA.V1p4j_germline_end, domain=None, range=Optional[int])

slots.V1p4j_alignment_start = Slot(uri=AK_SCHEMA.V1p4j_alignment_start, name="V1p4j_alignment_start", curie=AK_SCHEMA.curie('V1p4j_alignment_start'),
                   model_uri=AK_SCHEMA.V1p4j_alignment_start, domain=None, range=Optional[int])

slots.V1p4j_alignment_end = Slot(uri=AK_SCHEMA.V1p4j_alignment_end, name="V1p4j_alignment_end", curie=AK_SCHEMA.curie('V1p4j_alignment_end'),
                   model_uri=AK_SCHEMA.V1p4j_alignment_end, domain=None, range=Optional[int])

slots.V1p4c_sequence_start = Slot(uri=AK_SCHEMA.V1p4c_sequence_start, name="V1p4c_sequence_start", curie=AK_SCHEMA.curie('V1p4c_sequence_start'),
                   model_uri=AK_SCHEMA.V1p4c_sequence_start, domain=None, range=Optional[int])

slots.V1p4c_sequence_end = Slot(uri=AK_SCHEMA.V1p4c_sequence_end, name="V1p4c_sequence_end", curie=AK_SCHEMA.curie('V1p4c_sequence_end'),
                   model_uri=AK_SCHEMA.V1p4c_sequence_end, domain=None, range=Optional[int])

slots.V1p4c_germline_start = Slot(uri=AK_SCHEMA.V1p4c_germline_start, name="V1p4c_germline_start", curie=AK_SCHEMA.curie('V1p4c_germline_start'),
                   model_uri=AK_SCHEMA.V1p4c_germline_start, domain=None, range=Optional[int])

slots.V1p4c_germline_end = Slot(uri=AK_SCHEMA.V1p4c_germline_end, name="V1p4c_germline_end", curie=AK_SCHEMA.curie('V1p4c_germline_end'),
                   model_uri=AK_SCHEMA.V1p4c_germline_end, domain=None, range=Optional[int])

slots.V1p4c_alignment_start = Slot(uri=AK_SCHEMA.V1p4c_alignment_start, name="V1p4c_alignment_start", curie=AK_SCHEMA.curie('V1p4c_alignment_start'),
                   model_uri=AK_SCHEMA.V1p4c_alignment_start, domain=None, range=Optional[int])

slots.V1p4c_alignment_end = Slot(uri=AK_SCHEMA.V1p4c_alignment_end, name="V1p4c_alignment_end", curie=AK_SCHEMA.curie('V1p4c_alignment_end'),
                   model_uri=AK_SCHEMA.V1p4c_alignment_end, domain=None, range=Optional[int])

slots.V1p4cdr3_end = Slot(uri=AK_SCHEMA.V1p4cdr3_end, name="V1p4cdr3_end", curie=AK_SCHEMA.curie('V1p4cdr3_end'),
                   model_uri=AK_SCHEMA.V1p4cdr3_end, domain=None, range=Optional[int])

slots.V1p4fwr4_start = Slot(uri=AK_SCHEMA.V1p4fwr4_start, name="V1p4fwr4_start", curie=AK_SCHEMA.curie('V1p4fwr4_start'),
                   model_uri=AK_SCHEMA.V1p4fwr4_start, domain=None, range=Optional[int])

slots.V1p4fwr4_end = Slot(uri=AK_SCHEMA.V1p4fwr4_end, name="V1p4fwr4_end", curie=AK_SCHEMA.curie('V1p4fwr4_end'),
                   model_uri=AK_SCHEMA.V1p4fwr4_end, domain=None, range=Optional[int])

slots.V1p4v_sequence_alignment = Slot(uri=AK_SCHEMA.V1p4v_sequence_alignment, name="V1p4v_sequence_alignment", curie=AK_SCHEMA.curie('V1p4v_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p4v_sequence_alignment, domain=None, range=Optional[str])

slots.V1p4v_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p4v_sequence_alignment_aa, name="V1p4v_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p4v_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4v_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p4d_sequence_alignment = Slot(uri=AK_SCHEMA.V1p4d_sequence_alignment, name="V1p4d_sequence_alignment", curie=AK_SCHEMA.curie('V1p4d_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p4d_sequence_alignment, domain=None, range=Optional[str])

slots.V1p4d_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p4d_sequence_alignment_aa, name="V1p4d_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p4d_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4d_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p4d2_sequence_alignment = Slot(uri=AK_SCHEMA.V1p4d2_sequence_alignment, name="V1p4d2_sequence_alignment", curie=AK_SCHEMA.curie('V1p4d2_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p4d2_sequence_alignment, domain=None, range=Optional[str])

slots.V1p4d2_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p4d2_sequence_alignment_aa, name="V1p4d2_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p4d2_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4d2_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p4j_sequence_alignment = Slot(uri=AK_SCHEMA.V1p4j_sequence_alignment, name="V1p4j_sequence_alignment", curie=AK_SCHEMA.curie('V1p4j_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p4j_sequence_alignment, domain=None, range=Optional[str])

slots.V1p4j_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p4j_sequence_alignment_aa, name="V1p4j_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p4j_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4j_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p4c_sequence_alignment = Slot(uri=AK_SCHEMA.V1p4c_sequence_alignment, name="V1p4c_sequence_alignment", curie=AK_SCHEMA.curie('V1p4c_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p4c_sequence_alignment, domain=None, range=Optional[str])

slots.V1p4c_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p4c_sequence_alignment_aa, name="V1p4c_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p4c_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4c_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p4v_germline_alignment = Slot(uri=AK_SCHEMA.V1p4v_germline_alignment, name="V1p4v_germline_alignment", curie=AK_SCHEMA.curie('V1p4v_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p4v_germline_alignment, domain=None, range=Optional[str])

slots.V1p4v_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p4v_germline_alignment_aa, name="V1p4v_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p4v_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4v_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p4d_germline_alignment = Slot(uri=AK_SCHEMA.V1p4d_germline_alignment, name="V1p4d_germline_alignment", curie=AK_SCHEMA.curie('V1p4d_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p4d_germline_alignment, domain=None, range=Optional[str])

slots.V1p4d_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p4d_germline_alignment_aa, name="V1p4d_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p4d_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4d_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p4d2_germline_alignment = Slot(uri=AK_SCHEMA.V1p4d2_germline_alignment, name="V1p4d2_germline_alignment", curie=AK_SCHEMA.curie('V1p4d2_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p4d2_germline_alignment, domain=None, range=Optional[str])

slots.V1p4d2_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p4d2_germline_alignment_aa, name="V1p4d2_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p4d2_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4d2_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p4j_germline_alignment = Slot(uri=AK_SCHEMA.V1p4j_germline_alignment, name="V1p4j_germline_alignment", curie=AK_SCHEMA.curie('V1p4j_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p4j_germline_alignment, domain=None, range=Optional[str])

slots.V1p4j_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p4j_germline_alignment_aa, name="V1p4j_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p4j_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4j_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p4c_germline_alignment = Slot(uri=AK_SCHEMA.V1p4c_germline_alignment, name="V1p4c_germline_alignment", curie=AK_SCHEMA.curie('V1p4c_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p4c_germline_alignment, domain=None, range=Optional[str])

slots.V1p4c_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p4c_germline_alignment_aa, name="V1p4c_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p4c_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4c_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p4junction_length = Slot(uri=AK_SCHEMA.V1p4junction_length, name="V1p4junction_length", curie=AK_SCHEMA.curie('V1p4junction_length'),
                   model_uri=AK_SCHEMA.V1p4junction_length, domain=None, range=Optional[int])

slots.V1p4junction_aa_length = Slot(uri=AK_SCHEMA.V1p4junction_aa_length, name="V1p4junction_aa_length", curie=AK_SCHEMA.curie('V1p4junction_aa_length'),
                   model_uri=AK_SCHEMA.V1p4junction_aa_length, domain=None, range=Optional[int])

slots.V1p4np1_length = Slot(uri=AK_SCHEMA.V1p4np1_length, name="V1p4np1_length", curie=AK_SCHEMA.curie('V1p4np1_length'),
                   model_uri=AK_SCHEMA.V1p4np1_length, domain=None, range=Optional[int])

slots.V1p4np2_length = Slot(uri=AK_SCHEMA.V1p4np2_length, name="V1p4np2_length", curie=AK_SCHEMA.curie('V1p4np2_length'),
                   model_uri=AK_SCHEMA.V1p4np2_length, domain=None, range=Optional[int])

slots.V1p4np3_length = Slot(uri=AK_SCHEMA.V1p4np3_length, name="V1p4np3_length", curie=AK_SCHEMA.curie('V1p4np3_length'),
                   model_uri=AK_SCHEMA.V1p4np3_length, domain=None, range=Optional[int])

slots.V1p4n1_length = Slot(uri=AK_SCHEMA.V1p4n1_length, name="V1p4n1_length", curie=AK_SCHEMA.curie('V1p4n1_length'),
                   model_uri=AK_SCHEMA.V1p4n1_length, domain=None, range=Optional[int])

slots.V1p4n2_length = Slot(uri=AK_SCHEMA.V1p4n2_length, name="V1p4n2_length", curie=AK_SCHEMA.curie('V1p4n2_length'),
                   model_uri=AK_SCHEMA.V1p4n2_length, domain=None, range=Optional[int])

slots.V1p4n3_length = Slot(uri=AK_SCHEMA.V1p4n3_length, name="V1p4n3_length", curie=AK_SCHEMA.curie('V1p4n3_length'),
                   model_uri=AK_SCHEMA.V1p4n3_length, domain=None, range=Optional[int])

slots.V1p4p3v_length = Slot(uri=AK_SCHEMA.V1p4p3v_length, name="V1p4p3v_length", curie=AK_SCHEMA.curie('V1p4p3v_length'),
                   model_uri=AK_SCHEMA.V1p4p3v_length, domain=None, range=Optional[int])

slots.V1p4p5d_length = Slot(uri=AK_SCHEMA.V1p4p5d_length, name="V1p4p5d_length", curie=AK_SCHEMA.curie('V1p4p5d_length'),
                   model_uri=AK_SCHEMA.V1p4p5d_length, domain=None, range=Optional[int])

slots.V1p4p3d_length = Slot(uri=AK_SCHEMA.V1p4p3d_length, name="V1p4p3d_length", curie=AK_SCHEMA.curie('V1p4p3d_length'),
                   model_uri=AK_SCHEMA.V1p4p3d_length, domain=None, range=Optional[int])

slots.V1p4p5d2_length = Slot(uri=AK_SCHEMA.V1p4p5d2_length, name="V1p4p5d2_length", curie=AK_SCHEMA.curie('V1p4p5d2_length'),
                   model_uri=AK_SCHEMA.V1p4p5d2_length, domain=None, range=Optional[int])

slots.V1p4p3d2_length = Slot(uri=AK_SCHEMA.V1p4p3d2_length, name="V1p4p3d2_length", curie=AK_SCHEMA.curie('V1p4p3d2_length'),
                   model_uri=AK_SCHEMA.V1p4p3d2_length, domain=None, range=Optional[int])

slots.V1p4p5j_length = Slot(uri=AK_SCHEMA.V1p4p5j_length, name="V1p4p5j_length", curie=AK_SCHEMA.curie('V1p4p5j_length'),
                   model_uri=AK_SCHEMA.V1p4p5j_length, domain=None, range=Optional[int])

slots.V1p4v_frameshift = Slot(uri=AK_SCHEMA.V1p4v_frameshift, name="V1p4v_frameshift", curie=AK_SCHEMA.curie('V1p4v_frameshift'),
                   model_uri=AK_SCHEMA.V1p4v_frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4j_frameshift = Slot(uri=AK_SCHEMA.V1p4j_frameshift, name="V1p4j_frameshift", curie=AK_SCHEMA.curie('V1p4j_frameshift'),
                   model_uri=AK_SCHEMA.V1p4j_frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4d_frame = Slot(uri=AK_SCHEMA.V1p4d_frame, name="V1p4d_frame", curie=AK_SCHEMA.curie('V1p4d_frame'),
                   model_uri=AK_SCHEMA.V1p4d_frame, domain=None, range=Optional[int])

slots.V1p4d2_frame = Slot(uri=AK_SCHEMA.V1p4d2_frame, name="V1p4d2_frame", curie=AK_SCHEMA.curie('V1p4d2_frame'),
                   model_uri=AK_SCHEMA.V1p4d2_frame, domain=None, range=Optional[int])

slots.V1p4consensus_count = Slot(uri=AK_SCHEMA.V1p4consensus_count, name="V1p4consensus_count", curie=AK_SCHEMA.curie('V1p4consensus_count'),
                   model_uri=AK_SCHEMA.V1p4consensus_count, domain=None, range=Optional[int])

slots.V1p4duplicate_count = Slot(uri=AK_SCHEMA.V1p4duplicate_count, name="V1p4duplicate_count", curie=AK_SCHEMA.curie('V1p4duplicate_count'),
                   model_uri=AK_SCHEMA.V1p4duplicate_count, domain=None, range=Optional[int])

slots.V1p4umi_count = Slot(uri=AK_SCHEMA.V1p4umi_count, name="V1p4umi_count", curie=AK_SCHEMA.curie('V1p4umi_count'),
                   model_uri=AK_SCHEMA.V1p4umi_count, domain=None, range=Optional[int])

slots.V1p4cell_id = Slot(uri=AK_SCHEMA.V1p4cell_id, name="V1p4cell_id", curie=AK_SCHEMA.curie('V1p4cell_id'),
                   model_uri=AK_SCHEMA.V1p4cell_id, domain=None, range=Optional[str])

slots.V1p4clone_id = Slot(uri=AK_SCHEMA.V1p4clone_id, name="V1p4clone_id", curie=AK_SCHEMA.curie('V1p4clone_id'),
                   model_uri=AK_SCHEMA.V1p4clone_id, domain=None, range=Optional[str])

slots.V1p4reactivity_id = Slot(uri=AK_SCHEMA.V1p4reactivity_id, name="V1p4reactivity_id", curie=AK_SCHEMA.curie('V1p4reactivity_id'),
                   model_uri=AK_SCHEMA.V1p4reactivity_id, domain=None, range=Optional[str])

slots.V1p4reactivity_ref = Slot(uri=AK_SCHEMA.V1p4reactivity_ref, name="V1p4reactivity_ref", curie=AK_SCHEMA.curie('V1p4reactivity_ref'),
                   model_uri=AK_SCHEMA.V1p4reactivity_ref, domain=None, range=Optional[str])

slots.V1p4sample_processing_id = Slot(uri=AK_SCHEMA.V1p4sample_processing_id, name="V1p4sample_processing_id", curie=AK_SCHEMA.curie('V1p4sample_processing_id'),
                   model_uri=AK_SCHEMA.V1p4sample_processing_id, domain=None, range=Optional[str])

slots.V1p4sequences = Slot(uri=AK_SCHEMA.V1p4sequences, name="V1p4sequences", curie=AK_SCHEMA.curie('V1p4sequences'),
                   model_uri=AK_SCHEMA.V1p4sequences, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4junction_start = Slot(uri=AK_SCHEMA.V1p4junction_start, name="V1p4junction_start", curie=AK_SCHEMA.curie('V1p4junction_start'),
                   model_uri=AK_SCHEMA.V1p4junction_start, domain=None, range=Optional[int])

slots.V1p4junction_end = Slot(uri=AK_SCHEMA.V1p4junction_end, name="V1p4junction_end", curie=AK_SCHEMA.curie('V1p4junction_end'),
                   model_uri=AK_SCHEMA.V1p4junction_end, domain=None, range=Optional[int])

slots.V1p4clone_count = Slot(uri=AK_SCHEMA.V1p4clone_count, name="V1p4clone_count", curie=AK_SCHEMA.curie('V1p4clone_count'),
                   model_uri=AK_SCHEMA.V1p4clone_count, domain=None, range=Optional[int])

slots.V1p4seed_id = Slot(uri=AK_SCHEMA.V1p4seed_id, name="V1p4seed_id", curie=AK_SCHEMA.curie('V1p4seed_id'),
                   model_uri=AK_SCHEMA.V1p4seed_id, domain=None, range=Optional[str])

slots.V1p4tree_id = Slot(uri=AK_SCHEMA.V1p4tree_id, name="V1p4tree_id", curie=AK_SCHEMA.curie('V1p4tree_id'),
                   model_uri=AK_SCHEMA.V1p4tree_id, domain=None, range=Optional[str])

slots.V1p4newick = Slot(uri=AK_SCHEMA.V1p4newick, name="V1p4newick", curie=AK_SCHEMA.curie('V1p4newick'),
                   model_uri=AK_SCHEMA.V1p4newick, domain=None, range=Optional[str])

slots.V1p4nodes = Slot(uri=AK_SCHEMA.V1p4nodes, name="V1p4nodes", curie=AK_SCHEMA.curie('V1p4nodes'),
                   model_uri=AK_SCHEMA.V1p4nodes, domain=None, range=Optional[Union[Union[dict, V1p4Node], List[Union[dict, V1p4Node]]]])

slots.V1p4receptors = Slot(uri=AK_SCHEMA.V1p4receptors, name="V1p4receptors", curie=AK_SCHEMA.curie('V1p4receptors'),
                   model_uri=AK_SCHEMA.V1p4receptors, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4virtual_pairing = Slot(uri=AK_SCHEMA.V1p4virtual_pairing, name="V1p4virtual_pairing", curie=AK_SCHEMA.curie('V1p4virtual_pairing'),
                   model_uri=AK_SCHEMA.V1p4virtual_pairing, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4expression_id = Slot(uri=AK_SCHEMA.V1p4expression_id, name="V1p4expression_id", curie=AK_SCHEMA.curie('V1p4expression_id'),
                   model_uri=AK_SCHEMA.V1p4expression_id, domain=None, range=Optional[str])

slots.V1p4property_type = Slot(uri=RDF.type, name="V1p4property_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p4property_type, domain=None, range=Optional[str])

slots.V1p4property = Slot(uri=AK_SCHEMA.V1p4property, name="V1p4property", curie=AK_SCHEMA.curie('V1p4property'),
                   model_uri=AK_SCHEMA.V1p4property, domain=None, range=Optional[Union[str, "V1p4Property"]])

slots.V1p4receptor_id = Slot(uri=AK_SCHEMA.V1p4receptor_id, name="V1p4receptor_id", curie=AK_SCHEMA.curie('V1p4receptor_id'),
                   model_uri=AK_SCHEMA.V1p4receptor_id, domain=None, range=Optional[str])

slots.V1p4receptor_hash = Slot(uri=AK_SCHEMA.V1p4receptor_hash, name="V1p4receptor_hash", curie=AK_SCHEMA.curie('V1p4receptor_hash'),
                   model_uri=AK_SCHEMA.V1p4receptor_hash, domain=None, range=Optional[str])

slots.V1p4receptor_type = Slot(uri=RDF.type, name="V1p4receptor_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p4receptor_type, domain=None, range=Optional[Union[str, "V1p4ReceptorType"]])

slots.V1p4receptor_variable_domain_1_aa = Slot(uri=AK_SCHEMA.V1p4receptor_variable_domain_1_aa, name="V1p4receptor_variable_domain_1_aa", curie=AK_SCHEMA.curie('V1p4receptor_variable_domain_1_aa'),
                   model_uri=AK_SCHEMA.V1p4receptor_variable_domain_1_aa, domain=None, range=Optional[str])

slots.V1p4receptor_variable_domain_1_locus = Slot(uri=AK_SCHEMA.V1p4receptor_variable_domain_1_locus, name="V1p4receptor_variable_domain_1_locus", curie=AK_SCHEMA.curie('V1p4receptor_variable_domain_1_locus'),
                   model_uri=AK_SCHEMA.V1p4receptor_variable_domain_1_locus, domain=None, range=Optional[Union[str, "V1p4ReceptorVariableDomain1Locus"]])

slots.V1p4receptor_variable_domain_2_aa = Slot(uri=AK_SCHEMA.V1p4receptor_variable_domain_2_aa, name="V1p4receptor_variable_domain_2_aa", curie=AK_SCHEMA.curie('V1p4receptor_variable_domain_2_aa'),
                   model_uri=AK_SCHEMA.V1p4receptor_variable_domain_2_aa, domain=None, range=Optional[str])

slots.V1p4receptor_variable_domain_2_locus = Slot(uri=AK_SCHEMA.V1p4receptor_variable_domain_2_locus, name="V1p4receptor_variable_domain_2_locus", curie=AK_SCHEMA.curie('V1p4receptor_variable_domain_2_locus'),
                   model_uri=AK_SCHEMA.V1p4receptor_variable_domain_2_locus, domain=None, range=Optional[Union[str, "V1p4ReceptorVariableDomain2Locus"]])

slots.V1p4receptor_ref = Slot(uri=AK_SCHEMA.V1p4receptor_ref, name="V1p4receptor_ref", curie=AK_SCHEMA.curie('V1p4receptor_ref'),
                   model_uri=AK_SCHEMA.V1p4receptor_ref, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4ligand_type = Slot(uri=RDF.type, name="V1p4ligand_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p4ligand_type, domain=None, range=Optional[Union[str, "V1p4LigandType"]])

slots.V1p4antigen_type = Slot(uri=RDF.type, name="V1p4antigen_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.V1p4antigen_type, domain=None, range=Optional[Union[str, "V1p4AntigenType"]])

slots.V1p4antigen = Slot(uri=AK_SCHEMA.V1p4antigen, name="V1p4antigen", curie=AK_SCHEMA.curie('V1p4antigen'),
                   model_uri=AK_SCHEMA.V1p4antigen, domain=None, range=Optional[Union[str, "V1p4Antigen"]])

slots.V1p4antigen_source_species = Slot(uri=AK_SCHEMA.V1p4antigen_source_species, name="V1p4antigen_source_species", curie=AK_SCHEMA.curie('V1p4antigen_source_species'),
                   model_uri=AK_SCHEMA.V1p4antigen_source_species, domain=None, range=Optional[Union[str, "V1p4AntigenSourceSpecies"]])

slots.V1p4peptide_start = Slot(uri=AK_SCHEMA.V1p4peptide_start, name="V1p4peptide_start", curie=AK_SCHEMA.curie('V1p4peptide_start'),
                   model_uri=AK_SCHEMA.V1p4peptide_start, domain=None, range=Optional[int])

slots.V1p4peptide_end = Slot(uri=AK_SCHEMA.V1p4peptide_end, name="V1p4peptide_end", curie=AK_SCHEMA.curie('V1p4peptide_end'),
                   model_uri=AK_SCHEMA.V1p4peptide_end, domain=None, range=Optional[int])

slots.V1p4peptide_sequence_aa = Slot(uri=AK_SCHEMA.V1p4peptide_sequence_aa, name="V1p4peptide_sequence_aa", curie=AK_SCHEMA.curie('V1p4peptide_sequence_aa'),
                   model_uri=AK_SCHEMA.V1p4peptide_sequence_aa, domain=None, range=Optional[str])

slots.V1p4mhc_gene_1 = Slot(uri=AK_SCHEMA.V1p4mhc_gene_1, name="V1p4mhc_gene_1", curie=AK_SCHEMA.curie('V1p4mhc_gene_1'),
                   model_uri=AK_SCHEMA.V1p4mhc_gene_1, domain=None, range=Optional[Union[str, "V1p4MhcGene1"]])

slots.V1p4mhc_allele_1 = Slot(uri=AK_SCHEMA.V1p4mhc_allele_1, name="V1p4mhc_allele_1", curie=AK_SCHEMA.curie('V1p4mhc_allele_1'),
                   model_uri=AK_SCHEMA.V1p4mhc_allele_1, domain=None, range=Optional[str])

slots.V1p4mhc_gene_2 = Slot(uri=AK_SCHEMA.V1p4mhc_gene_2, name="V1p4mhc_gene_2", curie=AK_SCHEMA.curie('V1p4mhc_gene_2'),
                   model_uri=AK_SCHEMA.V1p4mhc_gene_2, domain=None, range=Optional[Union[str, "V1p4MhcGene2"]])

slots.V1p4mhc_allele_2 = Slot(uri=AK_SCHEMA.V1p4mhc_allele_2, name="V1p4mhc_allele_2", curie=AK_SCHEMA.curie('V1p4mhc_allele_2'),
                   model_uri=AK_SCHEMA.V1p4mhc_allele_2, domain=None, range=Optional[str])

slots.V1p4reactivity_method = Slot(uri=AK_SCHEMA.V1p4reactivity_method, name="V1p4reactivity_method", curie=AK_SCHEMA.curie('V1p4reactivity_method'),
                   model_uri=AK_SCHEMA.V1p4reactivity_method, domain=None, range=Optional[str])

slots.V1p4reactivity_readout = Slot(uri=AK_SCHEMA.V1p4reactivity_readout, name="V1p4reactivity_readout", curie=AK_SCHEMA.curie('V1p4reactivity_readout'),
                   model_uri=AK_SCHEMA.V1p4reactivity_readout, domain=None, range=Optional[str])

slots.V1p4reactivity_value = Slot(uri=AK_SCHEMA.V1p4reactivity_value, name="V1p4reactivity_value", curie=AK_SCHEMA.curie('V1p4reactivity_value'),
                   model_uri=AK_SCHEMA.V1p4reactivity_value, domain=None, range=Optional[float])

slots.V1p4reactivity_unit = Slot(uri=AK_SCHEMA.V1p4reactivity_unit, name="V1p4reactivity_unit", curie=AK_SCHEMA.curie('V1p4reactivity_unit'),
                   model_uri=AK_SCHEMA.V1p4reactivity_unit, domain=None, range=Optional[str])

slots.aIRRKnowledgeCommons__investigations = Slot(uri=AK_SCHEMA.investigations, name="aIRRKnowledgeCommons__investigations", curie=AK_SCHEMA.curie('investigations'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__investigations, domain=None, range=Optional[Union[Dict[Union[str, InvestigationAkcId], Union[dict, Investigation]], List[Union[dict, Investigation]]]])

slots.aIRRKnowledgeCommons__references = Slot(uri=AK_SCHEMA.references, name="aIRRKnowledgeCommons__references", curie=AK_SCHEMA.curie('references'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__references, domain=None, range=Optional[Union[Dict[Union[str, ReferenceSourceUri], Union[dict, Reference]], List[Union[dict, Reference]]]])

slots.aIRRKnowledgeCommons__study_arms = Slot(uri=AK_SCHEMA.study_arms, name="aIRRKnowledgeCommons__study_arms", curie=AK_SCHEMA.curie('study_arms'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__study_arms, domain=None, range=Optional[Union[Dict[Union[str, StudyArmAkcId], Union[dict, StudyArm]], List[Union[dict, StudyArm]]]])

slots.aIRRKnowledgeCommons__study_events = Slot(uri=AK_SCHEMA.study_events, name="aIRRKnowledgeCommons__study_events", curie=AK_SCHEMA.curie('study_events'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__study_events, domain=None, range=Optional[Union[Dict[Union[str, StudyEventAkcId], Union[dict, StudyEvent]], List[Union[dict, StudyEvent]]]])

slots.aIRRKnowledgeCommons__participants = Slot(uri=AK_SCHEMA.participants, name="aIRRKnowledgeCommons__participants", curie=AK_SCHEMA.curie('participants'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__participants, domain=None, range=Optional[Union[Dict[Union[str, ParticipantAkcId], Union[dict, Participant]], List[Union[dict, Participant]]]])

slots.aIRRKnowledgeCommons__life_events = Slot(uri=AK_SCHEMA.life_events, name="aIRRKnowledgeCommons__life_events", curie=AK_SCHEMA.curie('life_events'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__life_events, domain=None, range=Optional[Union[Dict[Union[str, LifeEventAkcId], Union[dict, LifeEvent]], List[Union[dict, LifeEvent]]]])

slots.aIRRKnowledgeCommons__immune_exposures = Slot(uri=AK_SCHEMA.immune_exposures, name="aIRRKnowledgeCommons__immune_exposures", curie=AK_SCHEMA.curie('immune_exposures'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__immune_exposures, domain=None, range=Optional[Union[Dict[Union[str, ImmuneExposureAkcId], Union[dict, ImmuneExposure]], List[Union[dict, ImmuneExposure]]]])

slots.aIRRKnowledgeCommons__assessments = Slot(uri=AK_SCHEMA.assessments, name="aIRRKnowledgeCommons__assessments", curie=AK_SCHEMA.curie('assessments'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__assessments, domain=None, range=Optional[Union[Dict[Union[str, AssessmentAkcId], Union[dict, Assessment]], List[Union[dict, Assessment]]]])

slots.aIRRKnowledgeCommons__specimens = Slot(uri=AK_SCHEMA.specimens, name="aIRRKnowledgeCommons__specimens", curie=AK_SCHEMA.curie('specimens'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__specimens, domain=None, range=Optional[Union[Dict[Union[str, SpecimenAkcId], Union[dict, Specimen]], List[Union[dict, Specimen]]]])

slots.aIRRKnowledgeCommons__specimen_collections = Slot(uri=AK_SCHEMA.specimen_collections, name="aIRRKnowledgeCommons__specimen_collections", curie=AK_SCHEMA.curie('specimen_collections'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__specimen_collections, domain=None, range=Optional[Union[Dict[Union[str, SpecimenCollectionAkcId], Union[dict, SpecimenCollection]], List[Union[dict, SpecimenCollection]]]])

slots.aIRRKnowledgeCommons__specimen_processings = Slot(uri=AK_SCHEMA.specimen_processings, name="aIRRKnowledgeCommons__specimen_processings", curie=AK_SCHEMA.curie('specimen_processings'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__specimen_processings, domain=None, range=Optional[Union[Dict[Union[str, SpecimenProcessingAkcId], Union[dict, SpecimenProcessing]], List[Union[dict, SpecimenProcessing]]]])

slots.aIRRKnowledgeCommons__assays = Slot(uri=AK_SCHEMA.assays, name="aIRRKnowledgeCommons__assays", curie=AK_SCHEMA.curie('assays'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__assays, domain=None, range=Optional[Union[Dict[Union[str, AssayAkcId], Union[dict, Assay]], List[Union[dict, Assay]]]])

slots.aIRRKnowledgeCommons__datasets = Slot(uri=AK_SCHEMA.datasets, name="aIRRKnowledgeCommons__datasets", curie=AK_SCHEMA.curie('datasets'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__datasets, domain=None, range=Optional[Union[Dict[Union[str, DatasetAkcId], Union[dict, Dataset]], List[Union[dict, Dataset]]]])

slots.aIRRKnowledgeCommons__conclusions = Slot(uri=AK_SCHEMA.conclusions, name="aIRRKnowledgeCommons__conclusions", curie=AK_SCHEMA.curie('conclusions'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__conclusions, domain=None, range=Optional[Union[Dict[Union[str, ConclusionAkcId], Union[dict, Conclusion]], List[Union[dict, Conclusion]]]])

slots.aIRRKnowledgeCommons__chains = Slot(uri=AK_SCHEMA.chains, name="aIRRKnowledgeCommons__chains", curie=AK_SCHEMA.curie('chains'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__chains, domain=None, range=Optional[Union[Dict[Union[str, ChainAkcId], Union[dict, Chain]], List[Union[dict, Chain]]]])

slots.aIRRKnowledgeCommons__tcell_receptors = Slot(uri=AK_SCHEMA.tcell_receptors, name="aIRRKnowledgeCommons__tcell_receptors", curie=AK_SCHEMA.curie('tcell_receptors'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__tcell_receptors, domain=None, range=Optional[Union[Dict[Union[str, TCellReceptorAkcId], Union[dict, TCellReceptor]], List[Union[dict, TCellReceptor]]]])

slots.aIRRKnowledgeCommons__epitopes = Slot(uri=AK_SCHEMA.epitopes, name="aIRRKnowledgeCommons__epitopes", curie=AK_SCHEMA.curie('epitopes'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__epitopes, domain=None, range=Optional[Union[Dict[Union[str, EpitopeAkcId], Union[dict, Epitope]], List[Union[dict, Epitope]]]])