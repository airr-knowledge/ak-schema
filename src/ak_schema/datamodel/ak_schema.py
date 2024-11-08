# Auto generated from ak_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-11-08T12:30:35
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


class AssayAkcId(NamedThingAkcId):
    pass


class DatasetAkcId(NamedThingAkcId):
    pass


class ConclusionAkcId(NamedThingAkcId):
    pass


class AssessmentAkcId(NamedThingAkcId):
    pass


class CellAkcId(NamedThingAkcId):
    pass


class TissueAkcId(NamedThingAkcId):
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
    assays: Optional[Union[Dict[Union[str, AssayAkcId], Union[dict, "Assay"]], List[Union[dict, "Assay"]]]] = empty_dict()
    datasets: Optional[Union[Dict[Union[str, DatasetAkcId], Union[dict, "Dataset"]], List[Union[dict, "Dataset"]]]] = empty_dict()
    conclusions: Optional[Union[Dict[Union[str, ConclusionAkcId], Union[dict, "Conclusion"]], List[Union[dict, "Conclusion"]]]] = empty_dict()

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

        self._normalize_inlined_as_dict(slot_name="assays", slot_type=Assay, key_name="akc_id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="datasets", slot_type=Dataset, key_name="akc_id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="conclusions", slot_type=Conclusion, key_name="akc_id", keyed=True)

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
    age_unit: Optional[str] = None
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

        if self.age_unit is not None and not isinstance(self.age_unit, str):
            self.age_unit = str(self.age_unit)

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
    tissue: Optional[str] = None
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

        if self.tissue is not None and not isinstance(self.tissue, str):
            self.tissue = str(self.tissue)

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
class Assay(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000070"]
    class_class_curie: ClassVar[str] = "OBI:0000070"
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Assay

    akc_id: Union[str, AssayAkcId] = None
    specimen: Optional[Union[str, SpecimenAkcId]] = None
    assay_type: Optional[str] = None
    target_entity_type: Optional[str] = None
    value: Optional[str] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, AssayAkcId):
            self.akc_id = AssayAkcId(self.akc_id)

        if self.specimen is not None and not isinstance(self.specimen, SpecimenAkcId):
            self.specimen = SpecimenAkcId(self.specimen)

        if self.assay_type is not None and not isinstance(self.assay_type, str):
            self.assay_type = str(self.assay_type)

        if self.target_entity_type is not None and not isinstance(self.target_entity_type, str):
            self.target_entity_type = str(self.target_entity_type)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


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
class Assessment(NamedThing):
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
class Tissue(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UBERON["0000479"]
    class_class_curie: ClassVar[str] = "UBERON:0000479"
    class_name: ClassVar[str] = "Tissue"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Tissue

    akc_id: Union[str, TissueAkcId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, TissueAkcId):
            self.akc_id = TissueAkcId(self.akc_id)

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

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, TCellReceptorAkcId):
            self.akc_id = TCellReceptorAkcId(self.akc_id)

        super().__post_init__(**kwargs)


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
class AirrV15TimePoint(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15TimePoint"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15TimePoint"
    class_name: ClassVar[str] = "AirrV1_5_TimePoint"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15TimePoint

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
class AirrV15Acknowledgement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15Acknowledgement"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15Acknowledgement"
    class_name: ClassVar[str] = "AirrV1_5_Acknowledgement"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15Acknowledgement

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
class AirrV15RearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15RearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15RearrangedSequence"
    class_name: ClassVar[str] = "AirrV1_5_RearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15RearrangedSequence

    sequence_id: Optional[str] = None
    sequence: Optional[str] = None
    derivation: Optional[Union[str, "AirrV15Derivation"]] = None
    observation_type: Optional[Union[str, "AirrV15ObservationType"]] = None
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

        if self.derivation is not None and not isinstance(self.derivation, AirrV15Derivation):
            self.derivation = AirrV15Derivation(self.derivation)

        if self.observation_type is not None and not isinstance(self.observation_type, AirrV15ObservationType):
            self.observation_type = AirrV15ObservationType(self.observation_type)

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
class AirrV15UnrearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15UnrearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15UnrearrangedSequence"
    class_name: ClassVar[str] = "AirrV1_5_UnrearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15UnrearrangedSequence

    sequence_id: Optional[str] = None
    sequence: Optional[str] = None
    curation: Optional[str] = None
    repository_name: Optional[str] = None
    repository_ref: Optional[str] = None
    patch_no: Optional[str] = None
    gff_seqid: Optional[str] = None
    gff_start: Optional[int] = None
    gff_end: Optional[int] = None
    strand: Optional[Union[str, "AirrV15Strand"]] = None

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

        if self.strand is not None and not isinstance(self.strand, AirrV15Strand):
            self.strand = AirrV15Strand(self.strand)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15SequenceDelineationV(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15SequenceDelineationV"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15SequenceDelineationV"
    class_name: ClassVar[str] = "AirrV1_5_SequenceDelineationV"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15SequenceDelineationV

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
class AirrV15AlleleDescription(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15AlleleDescription"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15AlleleDescription"
    class_name: ClassVar[str] = "AirrV1_5_AlleleDescription"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15AlleleDescription

    allele_description_id: Optional[str] = None
    allele_description_ref: Optional[str] = None
    maintainer: Optional[str] = None
    acknowledgements: Optional[Union[Union[dict, AirrV15Acknowledgement], List[Union[dict, AirrV15Acknowledgement]]]] = empty_list()
    lab_address: Optional[str] = None
    release_version: Optional[float] = None
    release_date: Optional[Union[str, XSDDateTime]] = None
    release_description: Optional[str] = None
    label: Optional[str] = None
    sequence: Optional[str] = None
    coding_sequence: Optional[str] = None
    aliases: Optional[Union[str, List[str]]] = empty_list()
    locus: Optional[Union[str, "AirrV15Locus"]] = None
    chromosome: Optional[int] = None
    sequence_type: Optional[Union[str, "AirrV15SequenceType"]] = None
    functional: Optional[Union[bool, Bool]] = None
    inference_type: Optional[Union[str, "AirrV15InferenceType"]] = None
    species: Optional[Union[str, "Species"]] = None
    species_subgroup: Optional[str] = None
    species_subgroup_type: Optional[Union[str, "AirrV15SpeciesSubgroupType"]] = None
    status: Optional[Union[str, "AirrV15Status"]] = None
    subgroup_designation: Optional[str] = None
    gene_designation: Optional[str] = None
    allele_designation: Optional[str] = None
    allele_similarity_cluster_designation: Optional[str] = None
    allele_similarity_cluster_member_id: Optional[str] = None
    j_codon_frame: Optional[Union[str, "AirrV15JCodonFrame"]] = None
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
    v_gene_delineations: Optional[Union[Union[dict, AirrV15SequenceDelineationV], List[Union[dict, AirrV15SequenceDelineationV]]]] = empty_list()
    unrearranged_support: Optional[Union[Union[dict, AirrV15UnrearrangedSequence], List[Union[dict, AirrV15UnrearrangedSequence]]]] = empty_list()
    rearranged_support: Optional[Union[Union[dict, AirrV15RearrangedSequence], List[Union[dict, AirrV15RearrangedSequence]]]] = empty_list()
    paralogs: Optional[Union[str, List[str]]] = empty_list()
    curation: Optional[str] = None
    curational_tags: Optional[Union[Union[str, "AirrV15CurationalTags"], List[Union[str, "AirrV15CurationalTags"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.allele_description_id is not None and not isinstance(self.allele_description_id, str):
            self.allele_description_id = str(self.allele_description_id)

        if self.allele_description_ref is not None and not isinstance(self.allele_description_ref, str):
            self.allele_description_ref = str(self.allele_description_ref)

        if self.maintainer is not None and not isinstance(self.maintainer, str):
            self.maintainer = str(self.maintainer)

        if not isinstance(self.acknowledgements, list):
            self.acknowledgements = [self.acknowledgements] if self.acknowledgements is not None else []
        self.acknowledgements = [v if isinstance(v, AirrV15Acknowledgement) else AirrV15Acknowledgement(**as_dict(v)) for v in self.acknowledgements]

        if self.lab_address is not None and not isinstance(self.lab_address, str):
            self.lab_address = str(self.lab_address)

        if self.release_version is not None and not isinstance(self.release_version, float):
            self.release_version = float(self.release_version)

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

        if self.locus is not None and not isinstance(self.locus, AirrV15Locus):
            self.locus = AirrV15Locus(self.locus)

        if self.chromosome is not None and not isinstance(self.chromosome, int):
            self.chromosome = int(self.chromosome)

        if self.sequence_type is not None and not isinstance(self.sequence_type, AirrV15SequenceType):
            self.sequence_type = AirrV15SequenceType(self.sequence_type)

        if self.functional is not None and not isinstance(self.functional, Bool):
            self.functional = Bool(self.functional)

        if self.inference_type is not None and not isinstance(self.inference_type, AirrV15InferenceType):
            self.inference_type = AirrV15InferenceType(self.inference_type)

        if self.species is not None and not isinstance(self.species, Species):
            self.species = Species(self.species)

        if self.species_subgroup is not None and not isinstance(self.species_subgroup, str):
            self.species_subgroup = str(self.species_subgroup)

        if self.species_subgroup_type is not None and not isinstance(self.species_subgroup_type, AirrV15SpeciesSubgroupType):
            self.species_subgroup_type = AirrV15SpeciesSubgroupType(self.species_subgroup_type)

        if self.status is not None and not isinstance(self.status, AirrV15Status):
            self.status = AirrV15Status(self.status)

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

        if self.j_codon_frame is not None and not isinstance(self.j_codon_frame, AirrV15JCodonFrame):
            self.j_codon_frame = AirrV15JCodonFrame(self.j_codon_frame)

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
        self.v_gene_delineations = [v if isinstance(v, AirrV15SequenceDelineationV) else AirrV15SequenceDelineationV(**as_dict(v)) for v in self.v_gene_delineations]

        if not isinstance(self.unrearranged_support, list):
            self.unrearranged_support = [self.unrearranged_support] if self.unrearranged_support is not None else []
        self.unrearranged_support = [v if isinstance(v, AirrV15UnrearrangedSequence) else AirrV15UnrearrangedSequence(**as_dict(v)) for v in self.unrearranged_support]

        if not isinstance(self.rearranged_support, list):
            self.rearranged_support = [self.rearranged_support] if self.rearranged_support is not None else []
        self.rearranged_support = [v if isinstance(v, AirrV15RearrangedSequence) else AirrV15RearrangedSequence(**as_dict(v)) for v in self.rearranged_support]

        if not isinstance(self.paralogs, list):
            self.paralogs = [self.paralogs] if self.paralogs is not None else []
        self.paralogs = [v if isinstance(v, str) else str(v) for v in self.paralogs]

        if self.curation is not None and not isinstance(self.curation, str):
            self.curation = str(self.curation)

        if not isinstance(self.curational_tags, list):
            self.curational_tags = [self.curational_tags] if self.curational_tags is not None else []
        self.curational_tags = [v if isinstance(v, AirrV15CurationalTags) else AirrV15CurationalTags(v) for v in self.curational_tags]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15GermlineSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15GermlineSet"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15GermlineSet"
    class_name: ClassVar[str] = "AirrV1_5_GermlineSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15GermlineSet

    germline_set_id: Optional[str] = None
    author: Optional[str] = None
    lab_name: Optional[str] = None
    lab_address: Optional[str] = None
    acknowledgements: Optional[Union[Union[dict, AirrV15Acknowledgement], List[Union[dict, AirrV15Acknowledgement]]]] = empty_list()
    release_version: Optional[float] = None
    release_description: Optional[str] = None
    release_date: Optional[Union[str, XSDDateTime]] = None
    germline_set_name: Optional[str] = None
    germline_set_ref: Optional[str] = None
    pub_ids: Optional[str] = None
    species: Optional[Union[str, "Species"]] = None
    species_subgroup: Optional[str] = None
    species_subgroup_type: Optional[Union[str, "AirrV15SpeciesSubgroupType"]] = None
    locus: Optional[Union[str, "AirrV15Locus"]] = None
    allele_descriptions: Optional[Union[Union[dict, AirrV15AlleleDescription], List[Union[dict, AirrV15AlleleDescription]]]] = empty_list()
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
        self.acknowledgements = [v if isinstance(v, AirrV15Acknowledgement) else AirrV15Acknowledgement(**as_dict(v)) for v in self.acknowledgements]

        if self.release_version is not None and not isinstance(self.release_version, float):
            self.release_version = float(self.release_version)

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

        if self.species_subgroup_type is not None and not isinstance(self.species_subgroup_type, AirrV15SpeciesSubgroupType):
            self.species_subgroup_type = AirrV15SpeciesSubgroupType(self.species_subgroup_type)

        if self.locus is not None and not isinstance(self.locus, AirrV15Locus):
            self.locus = AirrV15Locus(self.locus)

        if not isinstance(self.allele_descriptions, list):
            self.allele_descriptions = [self.allele_descriptions] if self.allele_descriptions is not None else []
        self.allele_descriptions = [v if isinstance(v, AirrV15AlleleDescription) else AirrV15AlleleDescription(**as_dict(v)) for v in self.allele_descriptions]

        if self.curation is not None and not isinstance(self.curation, str):
            self.curation = str(self.curation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15GenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15GenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15GenotypeSet"
    class_name: ClassVar[str] = "AirrV1_5_GenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15GenotypeSet

    receptor_genotype_set_id: Optional[str] = None
    genotype_class_list: Optional[Union[Union[dict, "AirrV15Genotype"], List[Union[dict, "AirrV15Genotype"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.receptor_genotype_set_id is not None and not isinstance(self.receptor_genotype_set_id, str):
            self.receptor_genotype_set_id = str(self.receptor_genotype_set_id)

        if not isinstance(self.genotype_class_list, list):
            self.genotype_class_list = [self.genotype_class_list] if self.genotype_class_list is not None else []
        self.genotype_class_list = [v if isinstance(v, AirrV15Genotype) else AirrV15Genotype(**as_dict(v)) for v in self.genotype_class_list]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15Genotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15Genotype"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15Genotype"
    class_name: ClassVar[str] = "AirrV1_5_Genotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15Genotype

    receptor_genotype_id: Optional[str] = None
    locus: Optional[Union[str, "AirrV15Locus"]] = None
    documented_alleles: Optional[Union[Union[dict, "AirrV15DocumentedAllele"], List[Union[dict, "AirrV15DocumentedAllele"]]]] = empty_list()
    undocumented_alleles: Optional[Union[Union[dict, "AirrV15UndocumentedAllele"], List[Union[dict, "AirrV15UndocumentedAllele"]]]] = empty_list()
    deleted_genes: Optional[Union[Union[dict, "AirrV15DeletedGene"], List[Union[dict, "AirrV15DeletedGene"]]]] = empty_list()
    inference_process: Optional[Union[str, "AirrV15InferenceProcess"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.receptor_genotype_id is not None and not isinstance(self.receptor_genotype_id, str):
            self.receptor_genotype_id = str(self.receptor_genotype_id)

        if self.locus is not None and not isinstance(self.locus, AirrV15Locus):
            self.locus = AirrV15Locus(self.locus)

        if not isinstance(self.documented_alleles, list):
            self.documented_alleles = [self.documented_alleles] if self.documented_alleles is not None else []
        self.documented_alleles = [v if isinstance(v, AirrV15DocumentedAllele) else AirrV15DocumentedAllele(**as_dict(v)) for v in self.documented_alleles]

        if not isinstance(self.undocumented_alleles, list):
            self.undocumented_alleles = [self.undocumented_alleles] if self.undocumented_alleles is not None else []
        self.undocumented_alleles = [v if isinstance(v, AirrV15UndocumentedAllele) else AirrV15UndocumentedAllele(**as_dict(v)) for v in self.undocumented_alleles]

        if not isinstance(self.deleted_genes, list):
            self.deleted_genes = [self.deleted_genes] if self.deleted_genes is not None else []
        self.deleted_genes = [v if isinstance(v, AirrV15DeletedGene) else AirrV15DeletedGene(**as_dict(v)) for v in self.deleted_genes]

        if self.inference_process is not None and not isinstance(self.inference_process, AirrV15InferenceProcess):
            self.inference_process = AirrV15InferenceProcess(self.inference_process)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15DocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15DocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15DocumentedAllele"
    class_name: ClassVar[str] = "AirrV1_5_DocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15DocumentedAllele

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
class AirrV15UndocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15UndocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15UndocumentedAllele"
    class_name: ClassVar[str] = "AirrV1_5_UndocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15UndocumentedAllele

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
class AirrV15DeletedGene(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15DeletedGene"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15DeletedGene"
    class_name: ClassVar[str] = "AirrV1_5_DeletedGene"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15DeletedGene

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
class AirrV15MHCGenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15MHCGenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15MHCGenotypeSet"
    class_name: ClassVar[str] = "AirrV1_5_MHCGenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15MHCGenotypeSet

    mhc_genotype_set_id: Optional[str] = None
    mhc_genotype_list: Optional[Union[Union[dict, "AirrV15MHCGenotype"], List[Union[dict, "AirrV15MHCGenotype"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.mhc_genotype_set_id is not None and not isinstance(self.mhc_genotype_set_id, str):
            self.mhc_genotype_set_id = str(self.mhc_genotype_set_id)

        if not isinstance(self.mhc_genotype_list, list):
            self.mhc_genotype_list = [self.mhc_genotype_list] if self.mhc_genotype_list is not None else []
        self.mhc_genotype_list = [v if isinstance(v, AirrV15MHCGenotype) else AirrV15MHCGenotype(**as_dict(v)) for v in self.mhc_genotype_list]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15MHCGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15MHCGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15MHCGenotype"
    class_name: ClassVar[str] = "AirrV1_5_MHCGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15MHCGenotype

    mhc_genotype_id: Optional[str] = None
    mhc_class: Optional[Union[str, "AirrV15MhcClass"]] = None
    mhc_alleles: Optional[Union[Union[dict, "AirrV15MHCAllele"], List[Union[dict, "AirrV15MHCAllele"]]]] = empty_list()
    mhc_genotyping_method: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.mhc_genotype_id is not None and not isinstance(self.mhc_genotype_id, str):
            self.mhc_genotype_id = str(self.mhc_genotype_id)

        if self.mhc_class is not None and not isinstance(self.mhc_class, AirrV15MhcClass):
            self.mhc_class = AirrV15MhcClass(self.mhc_class)

        if not isinstance(self.mhc_alleles, list):
            self.mhc_alleles = [self.mhc_alleles] if self.mhc_alleles is not None else []
        self.mhc_alleles = [v if isinstance(v, AirrV15MHCAllele) else AirrV15MHCAllele(**as_dict(v)) for v in self.mhc_alleles]

        if self.mhc_genotyping_method is not None and not isinstance(self.mhc_genotyping_method, str):
            self.mhc_genotyping_method = str(self.mhc_genotyping_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15MHCAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15MHCAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15MHCAllele"
    class_name: ClassVar[str] = "AirrV1_5_MHCAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15MHCAllele

    allele_designation: Optional[str] = None
    gene: Optional[Union[str, "AirrV15Gene"]] = None
    reference_set_ref: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.allele_designation is not None and not isinstance(self.allele_designation, str):
            self.allele_designation = str(self.allele_designation)

        if self.reference_set_ref is not None and not isinstance(self.reference_set_ref, str):
            self.reference_set_ref = str(self.reference_set_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15SubjectGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15SubjectGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15SubjectGenotype"
    class_name: ClassVar[str] = "AirrV1_5_SubjectGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15SubjectGenotype

    receptor_genotype_set: Optional[Union[dict, AirrV15GenotypeSet]] = None
    mhc_genotype_set: Optional[Union[dict, AirrV15MHCGenotypeSet]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.receptor_genotype_set is not None and not isinstance(self.receptor_genotype_set, AirrV15GenotypeSet):
            self.receptor_genotype_set = AirrV15GenotypeSet(**as_dict(self.receptor_genotype_set))

        if self.mhc_genotype_set is not None and not isinstance(self.mhc_genotype_set, AirrV15MHCGenotypeSet):
            self.mhc_genotype_set = AirrV15MHCGenotypeSet(**as_dict(self.mhc_genotype_set))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15Study(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15Study"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15Study"
    class_name: ClassVar[str] = "AirrV1_5_Study"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15Study

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
    keywords_study: Optional[Union[Union[str, "AirrV15KeywordsStudy"], List[Union[str, "AirrV15KeywordsStudy"]]]] = empty_list()
    adc_publish_date: Optional[str] = None
    adc_update_date: Optional[str] = None

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
        self.keywords_study = [v if isinstance(v, AirrV15KeywordsStudy) else AirrV15KeywordsStudy(v) for v in self.keywords_study]

        if self.adc_publish_date is not None and not isinstance(self.adc_publish_date, str):
            self.adc_publish_date = str(self.adc_publish_date)

        if self.adc_update_date is not None and not isinstance(self.adc_update_date, str):
            self.adc_update_date = str(self.adc_update_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15Subject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15Subject"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15Subject"
    class_name: ClassVar[str] = "AirrV1_5_Subject"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15Subject

    subject_id: Optional[str] = None
    synthetic: Optional[Union[bool, Bool]] = None
    species: Optional[Union[str, "Species"]] = None
    sex: Optional[Union[str, "AirrV15Sex"]] = None
    age_min: Optional[float] = None
    age_max: Optional[float] = None
    age_unit: Optional[str] = None
    age_event: Optional[Union[str, LifeEventAkcId]] = None
    ancestry_population: Optional[str] = None
    ethnicity: Optional[Union[str, "Ethnicity"]] = None
    race: Optional[Union[str, "Race"]] = None
    strain_name: Optional[str] = None
    linked_subjects: Optional[str] = None
    link_type: Optional[str] = None
    diagnosis: Optional[Union[Union[dict, "AirrV15Diagnosis"], List[Union[dict, "AirrV15Diagnosis"]]]] = empty_list()
    genotype: Optional[Union[dict, AirrV15SubjectGenotype]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject_id is not None and not isinstance(self.subject_id, str):
            self.subject_id = str(self.subject_id)

        if self.synthetic is not None and not isinstance(self.synthetic, Bool):
            self.synthetic = Bool(self.synthetic)

        if self.species is not None and not isinstance(self.species, Species):
            self.species = Species(self.species)

        if self.sex is not None and not isinstance(self.sex, AirrV15Sex):
            self.sex = AirrV15Sex(self.sex)

        if self.age_min is not None and not isinstance(self.age_min, float):
            self.age_min = float(self.age_min)

        if self.age_max is not None and not isinstance(self.age_max, float):
            self.age_max = float(self.age_max)

        if self.age_unit is not None and not isinstance(self.age_unit, str):
            self.age_unit = str(self.age_unit)

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
        self.diagnosis = [v if isinstance(v, AirrV15Diagnosis) else AirrV15Diagnosis(**as_dict(v)) for v in self.diagnosis]

        if self.genotype is not None and not isinstance(self.genotype, AirrV15SubjectGenotype):
            self.genotype = AirrV15SubjectGenotype(**as_dict(self.genotype))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15Diagnosis(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15Diagnosis"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15Diagnosis"
    class_name: ClassVar[str] = "AirrV1_5_Diagnosis"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15Diagnosis

    study_group_description: Optional[str] = None
    disease_diagnosis: Optional[Union[str, "AirrV15DiseaseDiagnosis"]] = None
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
class AirrV15Sample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15Sample"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15Sample"
    class_name: ClassVar[str] = "AirrV1_5_Sample"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15Sample

    sample_id: Optional[str] = None
    sample_type: Optional[str] = None
    tissue: Optional[str] = None
    anatomic_site: Optional[str] = None
    disease_state_sample: Optional[str] = None
    collection_time_point_relative: Optional[float] = None
    collection_time_point_relative_unit: Optional[Union[str, "AirrV15CollectionTimePointRelativeUnit"]] = None
    collection_time_point_reference: Optional[str] = None
    biomaterial_provider: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sample_id is not None and not isinstance(self.sample_id, str):
            self.sample_id = str(self.sample_id)

        if self.sample_type is not None and not isinstance(self.sample_type, str):
            self.sample_type = str(self.sample_type)

        if self.tissue is not None and not isinstance(self.tissue, str):
            self.tissue = str(self.tissue)

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
class AirrV15CellProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15CellProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15CellProcessing"
    class_name: ClassVar[str] = "AirrV1_5_CellProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15CellProcessing

    tissue_processing: Optional[str] = None
    cell_subset: Optional[Union[str, "AirrV15CellSubset"]] = None
    cell_phenotype: Optional[str] = None
    cell_species: Optional[Union[str, "AirrV15CellSpecies"]] = None
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
class AirrV15PCRTarget(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15PCRTarget"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15PCRTarget"
    class_name: ClassVar[str] = "AirrV1_5_PCRTarget"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15PCRTarget

    pcr_target_locus: Optional[Union[str, "AirrV15PcrTargetLocus"]] = None
    forward_pcr_primer_target_location: Optional[str] = None
    reverse_pcr_primer_target_location: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.pcr_target_locus is not None and not isinstance(self.pcr_target_locus, AirrV15PcrTargetLocus):
            self.pcr_target_locus = AirrV15PcrTargetLocus(self.pcr_target_locus)

        if self.forward_pcr_primer_target_location is not None and not isinstance(self.forward_pcr_primer_target_location, str):
            self.forward_pcr_primer_target_location = str(self.forward_pcr_primer_target_location)

        if self.reverse_pcr_primer_target_location is not None and not isinstance(self.reverse_pcr_primer_target_location, str):
            self.reverse_pcr_primer_target_location = str(self.reverse_pcr_primer_target_location)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15NucleicAcidProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15NucleicAcidProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15NucleicAcidProcessing"
    class_name: ClassVar[str] = "AirrV1_5_NucleicAcidProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15NucleicAcidProcessing

    template_class: Optional[Union[str, "AirrV15TemplateClass"]] = None
    template_quality: Optional[str] = None
    template_amount: Optional[float] = None
    template_amount_unit: Optional[Union[str, "AirrV15TemplateAmountUnit"]] = None
    library_generation_method: Optional[Union[str, "AirrV15LibraryGenerationMethod"]] = None
    library_generation_protocol: Optional[str] = None
    library_generation_kit_version: Optional[str] = None
    pcr_target: Optional[Union[Union[dict, AirrV15PCRTarget], List[Union[dict, AirrV15PCRTarget]]]] = empty_list()
    complete_sequences: Optional[Union[str, "AirrV15CompleteSequences"]] = None
    physical_linkage: Optional[Union[str, "AirrV15PhysicalLinkage"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.template_class is not None and not isinstance(self.template_class, AirrV15TemplateClass):
            self.template_class = AirrV15TemplateClass(self.template_class)

        if self.template_quality is not None and not isinstance(self.template_quality, str):
            self.template_quality = str(self.template_quality)

        if self.template_amount is not None and not isinstance(self.template_amount, float):
            self.template_amount = float(self.template_amount)

        if self.library_generation_method is not None and not isinstance(self.library_generation_method, AirrV15LibraryGenerationMethod):
            self.library_generation_method = AirrV15LibraryGenerationMethod(self.library_generation_method)

        if self.library_generation_protocol is not None and not isinstance(self.library_generation_protocol, str):
            self.library_generation_protocol = str(self.library_generation_protocol)

        if self.library_generation_kit_version is not None and not isinstance(self.library_generation_kit_version, str):
            self.library_generation_kit_version = str(self.library_generation_kit_version)

        if not isinstance(self.pcr_target, list):
            self.pcr_target = [self.pcr_target] if self.pcr_target is not None else []
        self.pcr_target = [v if isinstance(v, AirrV15PCRTarget) else AirrV15PCRTarget(**as_dict(v)) for v in self.pcr_target]

        if self.complete_sequences is not None and not isinstance(self.complete_sequences, AirrV15CompleteSequences):
            self.complete_sequences = AirrV15CompleteSequences(self.complete_sequences)

        if self.physical_linkage is not None and not isinstance(self.physical_linkage, AirrV15PhysicalLinkage):
            self.physical_linkage = AirrV15PhysicalLinkage(self.physical_linkage)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15SequencingRun(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15SequencingRun"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15SequencingRun"
    class_name: ClassVar[str] = "AirrV1_5_SequencingRun"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15SequencingRun

    sequencing_run_id: Optional[str] = None
    total_reads_passing_qc_filter: Optional[int] = None
    sequencing_platform: Optional[str] = None
    sequencing_facility: Optional[str] = None
    sequencing_run_date: Optional[str] = None
    sequencing_kit: Optional[str] = None
    sequencing_files: Optional[Union[dict, "AirrV15SequencingData"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sequencing_run_id is not None and not isinstance(self.sequencing_run_id, str):
            self.sequencing_run_id = str(self.sequencing_run_id)

        if self.total_reads_passing_qc_filter is not None and not isinstance(self.total_reads_passing_qc_filter, int):
            self.total_reads_passing_qc_filter = int(self.total_reads_passing_qc_filter)

        if self.sequencing_platform is not None and not isinstance(self.sequencing_platform, str):
            self.sequencing_platform = str(self.sequencing_platform)

        if self.sequencing_facility is not None and not isinstance(self.sequencing_facility, str):
            self.sequencing_facility = str(self.sequencing_facility)

        if self.sequencing_run_date is not None and not isinstance(self.sequencing_run_date, str):
            self.sequencing_run_date = str(self.sequencing_run_date)

        if self.sequencing_kit is not None and not isinstance(self.sequencing_kit, str):
            self.sequencing_kit = str(self.sequencing_kit)

        if self.sequencing_files is not None and not isinstance(self.sequencing_files, AirrV15SequencingData):
            self.sequencing_files = AirrV15SequencingData(**as_dict(self.sequencing_files))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15SequencingData(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15SequencingData"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15SequencingData"
    class_name: ClassVar[str] = "AirrV1_5_SequencingData"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15SequencingData

    sequencing_data_id: Optional[str] = None
    file_type: Optional[Union[str, "AirrV15FileType"]] = None
    filename: Optional[str] = None
    read_direction: Optional[Union[str, "AirrV15ReadDirection"]] = None
    read_length: Optional[int] = None
    paired_filename: Optional[str] = None
    paired_read_direction: Optional[Union[str, "AirrV15PairedReadDirection"]] = None
    paired_read_length: Optional[int] = None
    index_filename: Optional[str] = None
    index_length: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sequencing_data_id is not None and not isinstance(self.sequencing_data_id, str):
            self.sequencing_data_id = str(self.sequencing_data_id)

        if self.file_type is not None and not isinstance(self.file_type, AirrV15FileType):
            self.file_type = AirrV15FileType(self.file_type)

        if self.filename is not None and not isinstance(self.filename, str):
            self.filename = str(self.filename)

        if self.read_direction is not None and not isinstance(self.read_direction, AirrV15ReadDirection):
            self.read_direction = AirrV15ReadDirection(self.read_direction)

        if self.read_length is not None and not isinstance(self.read_length, int):
            self.read_length = int(self.read_length)

        if self.paired_filename is not None and not isinstance(self.paired_filename, str):
            self.paired_filename = str(self.paired_filename)

        if self.paired_read_direction is not None and not isinstance(self.paired_read_direction, AirrV15PairedReadDirection):
            self.paired_read_direction = AirrV15PairedReadDirection(self.paired_read_direction)

        if self.paired_read_length is not None and not isinstance(self.paired_read_length, int):
            self.paired_read_length = int(self.paired_read_length)

        if self.index_filename is not None and not isinstance(self.index_filename, str):
            self.index_filename = str(self.index_filename)

        if self.index_length is not None and not isinstance(self.index_length, int):
            self.index_length = int(self.index_length)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15DataProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15DataProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15DataProcessing"
    class_name: ClassVar[str] = "AirrV1_5_DataProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15DataProcessing

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
class AirrV15Repertoire(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15Repertoire"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15Repertoire"
    class_name: ClassVar[str] = "AirrV1_5_Repertoire"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15Repertoire

    repertoire_id: Optional[str] = None
    repertoire_name: Optional[str] = None
    repertoire_description: Optional[str] = None
    study: Optional[Union[dict, AirrV15Study]] = None
    subject: Optional[Union[dict, AirrV15Subject]] = None
    sample: Optional[Union[Union[dict, "AirrV15SampleProcessing"], List[Union[dict, "AirrV15SampleProcessing"]]]] = empty_list()
    data_processing: Optional[Union[Union[dict, AirrV15DataProcessing], List[Union[dict, AirrV15DataProcessing]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.repertoire_id is not None and not isinstance(self.repertoire_id, str):
            self.repertoire_id = str(self.repertoire_id)

        if self.repertoire_name is not None and not isinstance(self.repertoire_name, str):
            self.repertoire_name = str(self.repertoire_name)

        if self.repertoire_description is not None and not isinstance(self.repertoire_description, str):
            self.repertoire_description = str(self.repertoire_description)

        if self.study is not None and not isinstance(self.study, AirrV15Study):
            self.study = AirrV15Study(**as_dict(self.study))

        if self.subject is not None and not isinstance(self.subject, AirrV15Subject):
            self.subject = AirrV15Subject(**as_dict(self.subject))

        if not isinstance(self.sample, list):
            self.sample = [self.sample] if self.sample is not None else []
        self.sample = [v if isinstance(v, AirrV15SampleProcessing) else AirrV15SampleProcessing(**as_dict(v)) for v in self.sample]

        if not isinstance(self.data_processing, list):
            self.data_processing = [self.data_processing] if self.data_processing is not None else []
        self.data_processing = [v if isinstance(v, AirrV15DataProcessing) else AirrV15DataProcessing(**as_dict(v)) for v in self.data_processing]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15RepertoireGroup(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15RepertoireGroup"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15RepertoireGroup"
    class_name: ClassVar[str] = "AirrV1_5_RepertoireGroup"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15RepertoireGroup

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
class AirrV15Alignment(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15Alignment"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15Alignment"
    class_name: ClassVar[str] = "AirrV1_5_Alignment"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15Alignment

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
class AirrV15Rearrangement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15Rearrangement"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15Rearrangement"
    class_name: ClassVar[str] = "AirrV1_5_Rearrangement"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15Rearrangement

    sequence_id: Optional[str] = None
    sequence: Optional[str] = None
    quality: Optional[str] = None
    sequence_aa: Optional[str] = None
    rev_comp: Optional[Union[bool, Bool]] = None
    productive: Optional[Union[bool, Bool]] = None
    vj_in_frame: Optional[Union[bool, Bool]] = None
    stop_codon: Optional[Union[bool, Bool]] = None
    complete_vdj: Optional[Union[bool, Bool]] = None
    locus: Optional[Union[str, "AirrV15Locus"]] = None
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

        if self.locus is not None and not isinstance(self.locus, AirrV15Locus):
            self.locus = AirrV15Locus(self.locus)

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
class AirrV15Clone(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15Clone"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15Clone"
    class_name: ClassVar[str] = "AirrV1_5_Clone"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15Clone

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
class AirrV15Tree(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15Tree"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15Tree"
    class_name: ClassVar[str] = "AirrV1_5_Tree"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15Tree

    tree_id: Optional[str] = None
    clone_id: Optional[str] = None
    newick: Optional[str] = None
    nodes: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.tree_id is not None and not isinstance(self.tree_id, str):
            self.tree_id = str(self.tree_id)

        if self.clone_id is not None and not isinstance(self.clone_id, str):
            self.clone_id = str(self.clone_id)

        if self.newick is not None and not isinstance(self.newick, str):
            self.newick = str(self.newick)

        if self.nodes is not None and not isinstance(self.nodes, str):
            self.nodes = str(self.nodes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15Node(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15Node"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15Node"
    class_name: ClassVar[str] = "AirrV1_5_Node"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15Node

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
class AirrV15Cell(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15Cell"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15Cell"
    class_name: ClassVar[str] = "AirrV1_5_Cell"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15Cell

    cell_id: Optional[str] = None
    rearrangements: Optional[Union[str, List[str]]] = empty_list()
    receptors: Optional[Union[str, List[str]]] = empty_list()
    repertoire_id: Optional[str] = None
    data_processing_id: Optional[str] = None
    expression_study_method: Optional[Union[str, "AirrV15ExpressionStudyMethod"]] = None
    expression_raw_doi: Optional[str] = None
    expression_index: Optional[str] = None
    virtual_pairing: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.cell_id is not None and not isinstance(self.cell_id, str):
            self.cell_id = str(self.cell_id)

        if not isinstance(self.rearrangements, list):
            self.rearrangements = [self.rearrangements] if self.rearrangements is not None else []
        self.rearrangements = [v if isinstance(v, str) else str(v) for v in self.rearrangements]

        if not isinstance(self.receptors, list):
            self.receptors = [self.receptors] if self.receptors is not None else []
        self.receptors = [v if isinstance(v, str) else str(v) for v in self.receptors]

        if self.repertoire_id is not None and not isinstance(self.repertoire_id, str):
            self.repertoire_id = str(self.repertoire_id)

        if self.data_processing_id is not None and not isinstance(self.data_processing_id, str):
            self.data_processing_id = str(self.data_processing_id)

        if self.expression_study_method is not None and not isinstance(self.expression_study_method, AirrV15ExpressionStudyMethod):
            self.expression_study_method = AirrV15ExpressionStudyMethod(self.expression_study_method)

        if self.expression_raw_doi is not None and not isinstance(self.expression_raw_doi, str):
            self.expression_raw_doi = str(self.expression_raw_doi)

        if self.expression_index is not None and not isinstance(self.expression_index, str):
            self.expression_index = str(self.expression_index)

        if self.virtual_pairing is not None and not isinstance(self.virtual_pairing, Bool):
            self.virtual_pairing = Bool(self.virtual_pairing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15CellExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15CellExpression"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15CellExpression"
    class_name: ClassVar[str] = "AirrV1_5_CellExpression"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15CellExpression

    expression_id: Optional[str] = None
    cell_id: Optional[str] = None
    repertoire_id: Optional[str] = None
    data_processing_id: Optional[str] = None
    property_type: Optional[str] = None
    property: Optional[Union[str, "AirrV15Property"]] = None
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
class AirrV15Receptor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15Receptor"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15Receptor"
    class_name: ClassVar[str] = "AirrV1_5_Receptor"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15Receptor

    receptor_id: Optional[str] = None
    receptor_hash: Optional[str] = None
    receptor_type: Optional[Union[str, "AirrV15ReceptorType"]] = None
    receptor_variable_domain_1_aa: Optional[str] = None
    receptor_variable_domain_1_locus: Optional[Union[str, "AirrV15ReceptorVariableDomain1Locus"]] = None
    receptor_variable_domain_2_aa: Optional[str] = None
    receptor_variable_domain_2_locus: Optional[Union[str, "AirrV15ReceptorVariableDomain2Locus"]] = None
    receptor_ref: Optional[Union[str, List[str]]] = empty_list()
    reactivity_measurements: Optional[Union[Union[dict, "AirrV15ReceptorReactivity"], List[Union[dict, "AirrV15ReceptorReactivity"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.receptor_id is not None and not isinstance(self.receptor_id, str):
            self.receptor_id = str(self.receptor_id)

        if self.receptor_hash is not None and not isinstance(self.receptor_hash, str):
            self.receptor_hash = str(self.receptor_hash)

        if self.receptor_type is not None and not isinstance(self.receptor_type, AirrV15ReceptorType):
            self.receptor_type = AirrV15ReceptorType(self.receptor_type)

        if self.receptor_variable_domain_1_aa is not None and not isinstance(self.receptor_variable_domain_1_aa, str):
            self.receptor_variable_domain_1_aa = str(self.receptor_variable_domain_1_aa)

        if self.receptor_variable_domain_1_locus is not None and not isinstance(self.receptor_variable_domain_1_locus, AirrV15ReceptorVariableDomain1Locus):
            self.receptor_variable_domain_1_locus = AirrV15ReceptorVariableDomain1Locus(self.receptor_variable_domain_1_locus)

        if self.receptor_variable_domain_2_aa is not None and not isinstance(self.receptor_variable_domain_2_aa, str):
            self.receptor_variable_domain_2_aa = str(self.receptor_variable_domain_2_aa)

        if self.receptor_variable_domain_2_locus is not None and not isinstance(self.receptor_variable_domain_2_locus, AirrV15ReceptorVariableDomain2Locus):
            self.receptor_variable_domain_2_locus = AirrV15ReceptorVariableDomain2Locus(self.receptor_variable_domain_2_locus)

        if not isinstance(self.receptor_ref, list):
            self.receptor_ref = [self.receptor_ref] if self.receptor_ref is not None else []
        self.receptor_ref = [v if isinstance(v, str) else str(v) for v in self.receptor_ref]

        if not isinstance(self.reactivity_measurements, list):
            self.reactivity_measurements = [self.reactivity_measurements] if self.reactivity_measurements is not None else []
        self.reactivity_measurements = [v if isinstance(v, AirrV15ReceptorReactivity) else AirrV15ReceptorReactivity(**as_dict(v)) for v in self.reactivity_measurements]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15ReceptorReactivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15ReceptorReactivity"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15ReceptorReactivity"
    class_name: ClassVar[str] = "AirrV1_5_ReceptorReactivity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15ReceptorReactivity

    ligand_type: Optional[Union[str, "AirrV15LigandType"]] = None
    antigen_type: Optional[Union[str, "AirrV15AntigenType"]] = None
    antigen: Optional[Union[str, "AirrV15Antigen"]] = None
    antigen_source_species: Optional[Union[str, "AirrV15AntigenSourceSpecies"]] = None
    peptide_start: Optional[int] = None
    peptide_end: Optional[int] = None
    mhc_class: Optional[Union[str, "AirrV15MhcClass"]] = None
    mhc_gene_1: Optional[Union[str, "AirrV15MhcGene1"]] = None
    mhc_allele_1: Optional[str] = None
    mhc_gene_2: Optional[Union[str, "AirrV15MhcGene2"]] = None
    mhc_allele_2: Optional[str] = None
    reactivity_method: Optional[Union[str, "AirrV15ReactivityMethod"]] = None
    reactivity_readout: Optional[Union[str, "AirrV15ReactivityReadout"]] = None
    reactivity_value: Optional[float] = None
    reactivity_unit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ligand_type is not None and not isinstance(self.ligand_type, AirrV15LigandType):
            self.ligand_type = AirrV15LigandType(self.ligand_type)

        if self.antigen_type is not None and not isinstance(self.antigen_type, AirrV15AntigenType):
            self.antigen_type = AirrV15AntigenType(self.antigen_type)

        if self.peptide_start is not None and not isinstance(self.peptide_start, int):
            self.peptide_start = int(self.peptide_start)

        if self.peptide_end is not None and not isinstance(self.peptide_end, int):
            self.peptide_end = int(self.peptide_end)

        if self.mhc_class is not None and not isinstance(self.mhc_class, AirrV15MhcClass):
            self.mhc_class = AirrV15MhcClass(self.mhc_class)

        if self.mhc_allele_1 is not None and not isinstance(self.mhc_allele_1, str):
            self.mhc_allele_1 = str(self.mhc_allele_1)

        if self.mhc_allele_2 is not None and not isinstance(self.mhc_allele_2, str):
            self.mhc_allele_2 = str(self.mhc_allele_2)

        if self.reactivity_method is not None and not isinstance(self.reactivity_method, AirrV15ReactivityMethod):
            self.reactivity_method = AirrV15ReactivityMethod(self.reactivity_method)

        if self.reactivity_readout is not None and not isinstance(self.reactivity_readout, AirrV15ReactivityReadout):
            self.reactivity_readout = AirrV15ReactivityReadout(self.reactivity_readout)

        if self.reactivity_value is not None and not isinstance(self.reactivity_value, float):
            self.reactivity_value = float(self.reactivity_value)

        if self.reactivity_unit is not None and not isinstance(self.reactivity_unit, str):
            self.reactivity_unit = str(self.reactivity_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirrV15SampleProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AirrV15SampleProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:AirrV15SampleProcessing"
    class_name: ClassVar[str] = "AirrV1_5_SampleProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AirrV15SampleProcessing

    sequencing_run_id: Optional[str] = None
    total_reads_passing_qc_filter: Optional[int] = None
    sequencing_platform: Optional[str] = None
    sequencing_facility: Optional[str] = None
    sequencing_run_date: Optional[str] = None
    sequencing_kit: Optional[str] = None
    sequencing_files: Optional[Union[dict, AirrV15SequencingData]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sequencing_run_id is not None and not isinstance(self.sequencing_run_id, str):
            self.sequencing_run_id = str(self.sequencing_run_id)

        if self.total_reads_passing_qc_filter is not None and not isinstance(self.total_reads_passing_qc_filter, int):
            self.total_reads_passing_qc_filter = int(self.total_reads_passing_qc_filter)

        if self.sequencing_platform is not None and not isinstance(self.sequencing_platform, str):
            self.sequencing_platform = str(self.sequencing_platform)

        if self.sequencing_facility is not None and not isinstance(self.sequencing_facility, str):
            self.sequencing_facility = str(self.sequencing_facility)

        if self.sequencing_run_date is not None and not isinstance(self.sequencing_run_date, str):
            self.sequencing_run_date = str(self.sequencing_run_date)

        if self.sequencing_kit is not None and not isinstance(self.sequencing_kit, str):
            self.sequencing_kit = str(self.sequencing_kit)

        if self.sequencing_files is not None and not isinstance(self.sequencing_files, AirrV15SequencingData):
            self.sequencing_files = AirrV15SequencingData(**as_dict(self.sequencing_files))

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


# Enumerations
class StudyType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="StudyType",
    )

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

class AirrV15Unit(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AirrV15Unit",
    )

class AirrV15Derivation(EnumDefinitionImpl):

    DNA = PermissibleValue(text="DNA")
    RNA = PermissibleValue(text="RNA")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="AirrV15Derivation",
    )

class AirrV15ObservationType(EnumDefinitionImpl):

    direct_sequencing = PermissibleValue(text="direct_sequencing")
    inference_from_repertoire = PermissibleValue(text="inference_from_repertoire")

    _defn = EnumDefinition(
        name="AirrV15ObservationType",
    )

class AirrV15Strand(EnumDefinitionImpl):

    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="AirrV15Strand",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "+",
            PermissibleValue(text="+"))
        setattr(cls, "-",
            PermissibleValue(text="-"))

class AirrV15Locus(EnumDefinitionImpl):

    IGH = PermissibleValue(text="IGH")
    IGI = PermissibleValue(text="IGI")
    IGK = PermissibleValue(text="IGK")
    IGL = PermissibleValue(text="IGL")
    TRA = PermissibleValue(text="TRA")
    TRB = PermissibleValue(text="TRB")
    TRD = PermissibleValue(text="TRD")
    TRG = PermissibleValue(text="TRG")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="AirrV15Locus",
    )

class AirrV15SequenceType(EnumDefinitionImpl):

    V = PermissibleValue(text="V")
    D = PermissibleValue(text="D")
    J = PermissibleValue(text="J")
    C = PermissibleValue(text="C")

    _defn = EnumDefinition(
        name="AirrV15SequenceType",
    )

class AirrV15InferenceType(EnumDefinitionImpl):

    genomic_and_rearranged = PermissibleValue(text="genomic_and_rearranged")
    genomic_only = PermissibleValue(text="genomic_only")
    rearranged_only = PermissibleValue(text="rearranged_only")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="AirrV15InferenceType",
    )

class AirrV15Species(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AirrV15Species",
    )

class AirrV15SpeciesSubgroupType(EnumDefinitionImpl):

    breed = PermissibleValue(text="breed")
    strain = PermissibleValue(text="strain")
    inbred = PermissibleValue(text="inbred")
    outbred = PermissibleValue(text="outbred")
    locational = PermissibleValue(text="locational")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="AirrV15SpeciesSubgroupType",
    )

class AirrV15Status(EnumDefinitionImpl):

    active = PermissibleValue(text="active")
    draft = PermissibleValue(text="draft")
    retired = PermissibleValue(text="retired")
    withdrawn = PermissibleValue(text="withdrawn")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="AirrV15Status",
    )

class AirrV15JCodonFrame(EnumDefinitionImpl):

    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="AirrV15JCodonFrame",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1",
            PermissibleValue(text="1"))
        setattr(cls, "2",
            PermissibleValue(text="2"))
        setattr(cls, "3",
            PermissibleValue(text="3"))

class AirrV15CurationalTags(EnumDefinitionImpl):

    likely_truncated = PermissibleValue(text="likely_truncated")
    likely_full_length = PermissibleValue(text="likely_full_length")

    _defn = EnumDefinition(
        name="AirrV15CurationalTags",
    )

class AirrV15InferenceProcess(EnumDefinitionImpl):

    genomic_sequencing = PermissibleValue(text="genomic_sequencing")
    repertoire_sequencing = PermissibleValue(text="repertoire_sequencing")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="AirrV15InferenceProcess",
    )

class AirrV15MhcClass(EnumDefinitionImpl):

    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="AirrV15MhcClass",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "MHC-I",
            PermissibleValue(text="MHC-I"))
        setattr(cls, "MHC-II",
            PermissibleValue(text="MHC-II"))
        setattr(cls, "MHC-nonclassical",
            PermissibleValue(text="MHC-nonclassical"))

class AirrV15Gene(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AirrV15Gene",
    )

class AirrV15StudyType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AirrV15StudyType",
    )

class AirrV15KeywordsStudy(EnumDefinitionImpl):

    contains_ig = PermissibleValue(text="contains_ig")
    contains_tr = PermissibleValue(text="contains_tr")
    contains_paired_chain = PermissibleValue(text="contains_paired_chain")
    contains_schema_rearrangement = PermissibleValue(text="contains_schema_rearrangement")
    contains_schema_clone = PermissibleValue(text="contains_schema_clone")
    contains_schema_cell = PermissibleValue(text="contains_schema_cell")
    contains_schema_receptor = PermissibleValue(text="contains_schema_receptor")

    _defn = EnumDefinition(
        name="AirrV15KeywordsStudy",
    )

class AirrV15Sex(EnumDefinitionImpl):

    male = PermissibleValue(text="male")
    female = PermissibleValue(text="female")
    pooled = PermissibleValue(text="pooled")
    hermaphrodite = PermissibleValue(text="hermaphrodite")
    intersex = PermissibleValue(text="intersex")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="AirrV15Sex",
    )

class AirrV15AgeUnit(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AirrV15AgeUnit",
    )

class AirrV15DiseaseDiagnosis(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AirrV15DiseaseDiagnosis",
    )

class AirrV15Tissue(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AirrV15Tissue",
    )

class AirrV15CollectionTimePointRelativeUnit(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AirrV15CollectionTimePointRelativeUnit",
    )

class AirrV15CellSubset(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AirrV15CellSubset",
    )

class AirrV15CellSpecies(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AirrV15CellSpecies",
    )

class AirrV15PcrTargetLocus(EnumDefinitionImpl):

    IGH = PermissibleValue(text="IGH")
    IGI = PermissibleValue(text="IGI")
    IGK = PermissibleValue(text="IGK")
    IGL = PermissibleValue(text="IGL")
    TRA = PermissibleValue(text="TRA")
    TRB = PermissibleValue(text="TRB")
    TRD = PermissibleValue(text="TRD")
    TRG = PermissibleValue(text="TRG")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="AirrV15PcrTargetLocus",
    )

class AirrV15TemplateClass(EnumDefinitionImpl):

    DNA = PermissibleValue(text="DNA")
    RNA = PermissibleValue(text="RNA")

    _defn = EnumDefinition(
        name="AirrV15TemplateClass",
    )

class AirrV15TemplateAmountUnit(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AirrV15TemplateAmountUnit",
    )

class AirrV15LibraryGenerationMethod(EnumDefinitionImpl):

    PCR = PermissibleValue(text="PCR")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="AirrV15LibraryGenerationMethod",
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

class AirrV15CompleteSequences(EnumDefinitionImpl):

    partial = PermissibleValue(text="partial")
    complete = PermissibleValue(text="complete")
    mixed = PermissibleValue(text="mixed")

    _defn = EnumDefinition(
        name="AirrV15CompleteSequences",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "complete+untemplated",
            PermissibleValue(text="complete+untemplated"))

class AirrV15PhysicalLinkage(EnumDefinitionImpl):

    none = PermissibleValue(text="none")
    hetero_prelinked = PermissibleValue(text="hetero_prelinked")

    _defn = EnumDefinition(
        name="AirrV15PhysicalLinkage",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "hetero_head-head",
            PermissibleValue(text="hetero_head-head"))
        setattr(cls, "hetero_tail-head",
            PermissibleValue(text="hetero_tail-head"))

class AirrV15FileType(EnumDefinitionImpl):

    fasta = PermissibleValue(text="fasta")
    fastq = PermissibleValue(text="fastq")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="AirrV15FileType",
    )

class AirrV15ReadDirection(EnumDefinitionImpl):

    forward = PermissibleValue(text="forward")
    reverse = PermissibleValue(text="reverse")
    mixed = PermissibleValue(text="mixed")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="AirrV15ReadDirection",
    )

class AirrV15PairedReadDirection(EnumDefinitionImpl):

    forward = PermissibleValue(text="forward")
    reverse = PermissibleValue(text="reverse")
    mixed = PermissibleValue(text="mixed")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="AirrV15PairedReadDirection",
    )

class AirrV15ExpressionStudyMethod(EnumDefinitionImpl):

    flow_cytometry = PermissibleValue(text="flow_cytometry")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="AirrV15ExpressionStudyMethod",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "single-cell_transcriptome",
            PermissibleValue(text="single-cell_transcriptome"))

class AirrV15Property(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AirrV15Property",
    )

class AirrV15ReceptorType(EnumDefinitionImpl):

    Ig = PermissibleValue(text="Ig")
    TCR = PermissibleValue(text="TCR")

    _defn = EnumDefinition(
        name="AirrV15ReceptorType",
    )

class AirrV15ReceptorVariableDomain1Locus(EnumDefinitionImpl):

    IGH = PermissibleValue(text="IGH")
    TRB = PermissibleValue(text="TRB")
    TRD = PermissibleValue(text="TRD")

    _defn = EnumDefinition(
        name="AirrV15ReceptorVariableDomain1Locus",
    )

class AirrV15ReceptorVariableDomain2Locus(EnumDefinitionImpl):

    IGI = PermissibleValue(text="IGI")
    IGK = PermissibleValue(text="IGK")
    IGL = PermissibleValue(text="IGL")
    TRA = PermissibleValue(text="TRA")
    TRG = PermissibleValue(text="TRG")

    _defn = EnumDefinition(
        name="AirrV15ReceptorVariableDomain2Locus",
    )

class AirrV15LigandType(EnumDefinitionImpl):

    protein = PermissibleValue(text="protein")
    peptide = PermissibleValue(text="peptide")

    _defn = EnumDefinition(
        name="AirrV15LigandType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "MHC:peptide",
            PermissibleValue(text="MHC:peptide"))
        setattr(cls, "MHC:non-peptide",
            PermissibleValue(text="MHC:non-peptide"))
        setattr(cls, "non-peptidic",
            PermissibleValue(text="non-peptidic"))

class AirrV15AntigenType(EnumDefinitionImpl):

    protein = PermissibleValue(text="protein")
    peptide = PermissibleValue(text="peptide")

    _defn = EnumDefinition(
        name="AirrV15AntigenType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "non-peptidic",
            PermissibleValue(text="non-peptidic"))

class AirrV15Antigen(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AirrV15Antigen",
    )

class AirrV15AntigenSourceSpecies(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AirrV15AntigenSourceSpecies",
    )

class AirrV15MhcGene1(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AirrV15MhcGene1",
    )

class AirrV15MhcGene2(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AirrV15MhcGene2",
    )

class AirrV15ReactivityMethod(EnumDefinitionImpl):

    SPR = PermissibleValue(text="SPR")
    ITC = PermissibleValue(text="ITC")
    ELISA = PermissibleValue(text="ELISA")
    cytometry = PermissibleValue(text="cytometry")
    biological_activity = PermissibleValue(text="biological_activity")

    _defn = EnumDefinition(
        name="AirrV15ReactivityMethod",
    )

class AirrV15ReactivityReadout(EnumDefinitionImpl):

    binding_strength = PermissibleValue(text="binding_strength")
    cytokine_release = PermissibleValue(text="cytokine_release")
    dissociation_constant_kd = PermissibleValue(text="dissociation_constant_kd")
    on_rate = PermissibleValue(text="on_rate")
    off_rate = PermissibleValue(text="off_rate")
    pathogen_inhibition = PermissibleValue(text="pathogen_inhibition")

    _defn = EnumDefinition(
        name="AirrV15ReactivityReadout",
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

slots.study_type = Slot(uri=RDF.type, name="study_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.study_type, domain=None, range=Optional[Union[str, "StudyType"]])

slots.inclusion_criteria = Slot(uri=AK_SCHEMA.inclusion_criteria, name="inclusion_criteria", curie=AK_SCHEMA.curie('inclusion_criteria'),
                   model_uri=AK_SCHEMA.inclusion_criteria, domain=None, range=Optional[str])

slots.exclusion_criteria = Slot(uri=AK_SCHEMA.exclusion_criteria, name="exclusion_criteria", curie=AK_SCHEMA.curie('exclusion_criteria'),
                   model_uri=AK_SCHEMA.exclusion_criteria, domain=None, range=Optional[str])

slots.release_date = Slot(uri=AK_SCHEMA.release_date, name="release_date", curie=AK_SCHEMA.curie('release_date'),
                   model_uri=AK_SCHEMA.release_date, domain=None, range=Optional[Union[str, XSDDateTime]])

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

slots.age_unit = Slot(uri=AK_SCHEMA.age_unit, name="age_unit", curie=AK_SCHEMA.curie('age_unit'),
                   model_uri=AK_SCHEMA.age_unit, domain=None, range=Optional[str])

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

slots.specimen_type = Slot(uri=RDF.type, name="specimen_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.specimen_type, domain=None, range=Optional[str])

slots.tissue = Slot(uri=AK_SCHEMA.tissue, name="tissue", curie=AK_SCHEMA.curie('tissue'),
                   model_uri=AK_SCHEMA.tissue, domain=None, range=Optional[str])

slots.process = Slot(uri=AK_SCHEMA.process, name="process", curie=AK_SCHEMA.curie('process'),
                   model_uri=AK_SCHEMA.process, domain=None, range=Optional[str])

slots.specimen = Slot(uri=OBI['0000293'], name="specimen", curie=OBI.curie('0000293'),
                   model_uri=AK_SCHEMA.specimen, domain=None, range=Optional[Union[str, SpecimenAkcId]])

slots.assay_type = Slot(uri=RDF.type, name="assay_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.assay_type, domain=None, range=Optional[str])

slots.target_entity_type = Slot(uri=AK_SCHEMA.target_entity_type, name="target_entity_type", curie=AK_SCHEMA.curie('target_entity_type'),
                   model_uri=AK_SCHEMA.target_entity_type, domain=None, range=Optional[str])

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

slots.sequence = Slot(uri=AK_SCHEMA.sequence, name="sequence", curie=AK_SCHEMA.curie('sequence'),
                   model_uri=AK_SCHEMA.sequence, domain=None, range=Optional[str])

slots.sequence_aa = Slot(uri=AK_SCHEMA.sequence_aa, name="sequence_aa", curie=AK_SCHEMA.curie('sequence_aa'),
                   model_uri=AK_SCHEMA.sequence_aa, domain=None, range=Optional[str])

slots.chain_type = Slot(uri=AK_SCHEMA.chain_type, name="chain_type", curie=AK_SCHEMA.curie('chain_type'),
                   model_uri=AK_SCHEMA.chain_type, domain=None, range=Optional[Union[str, "ChainType"]])

slots.v_call = Slot(uri=AK_SCHEMA.v_call, name="v_call", curie=AK_SCHEMA.curie('v_call'),
                   model_uri=AK_SCHEMA.v_call, domain=None, range=Optional[str])

slots.d_call = Slot(uri=AK_SCHEMA.d_call, name="d_call", curie=AK_SCHEMA.curie('d_call'),
                   model_uri=AK_SCHEMA.d_call, domain=None, range=Optional[str])

slots.j_call = Slot(uri=AK_SCHEMA.j_call, name="j_call", curie=AK_SCHEMA.curie('j_call'),
                   model_uri=AK_SCHEMA.j_call, domain=None, range=Optional[str])

slots.c_call = Slot(uri=AK_SCHEMA.c_call, name="c_call", curie=AK_SCHEMA.curie('c_call'),
                   model_uri=AK_SCHEMA.c_call, domain=None, range=Optional[str])

slots.junction_aa = Slot(uri=AK_SCHEMA.junction_aa, name="junction_aa", curie=AK_SCHEMA.curie('junction_aa'),
                   model_uri=AK_SCHEMA.junction_aa, domain=None, range=Optional[str])

slots.cdr1_aa = Slot(uri=AK_SCHEMA.cdr1_aa, name="cdr1_aa", curie=AK_SCHEMA.curie('cdr1_aa'),
                   model_uri=AK_SCHEMA.cdr1_aa, domain=None, range=Optional[str])

slots.cdr2_aa = Slot(uri=AK_SCHEMA.cdr2_aa, name="cdr2_aa", curie=AK_SCHEMA.curie('cdr2_aa'),
                   model_uri=AK_SCHEMA.cdr2_aa, domain=None, range=Optional[str])

slots.cdr3_aa = Slot(uri=AK_SCHEMA.cdr3_aa, name="cdr3_aa", curie=AK_SCHEMA.curie('cdr3_aa'),
                   model_uri=AK_SCHEMA.cdr3_aa, domain=None, range=Optional[str])

slots.cdr1_start = Slot(uri=AK_SCHEMA.cdr1_start, name="cdr1_start", curie=AK_SCHEMA.curie('cdr1_start'),
                   model_uri=AK_SCHEMA.cdr1_start, domain=None, range=Optional[int])

slots.cdr1_end = Slot(uri=AK_SCHEMA.cdr1_end, name="cdr1_end", curie=AK_SCHEMA.curie('cdr1_end'),
                   model_uri=AK_SCHEMA.cdr1_end, domain=None, range=Optional[int])

slots.cdr2_start = Slot(uri=AK_SCHEMA.cdr2_start, name="cdr2_start", curie=AK_SCHEMA.curie('cdr2_start'),
                   model_uri=AK_SCHEMA.cdr2_start, domain=None, range=Optional[int])

slots.cdr2_end = Slot(uri=AK_SCHEMA.cdr2_end, name="cdr2_end", curie=AK_SCHEMA.curie('cdr2_end'),
                   model_uri=AK_SCHEMA.cdr2_end, domain=None, range=Optional[int])

slots.cdr3_start = Slot(uri=AK_SCHEMA.cdr3_start, name="cdr3_start", curie=AK_SCHEMA.curie('cdr3_start'),
                   model_uri=AK_SCHEMA.cdr3_start, domain=None, range=Optional[int])

slots.cdr3_end = Slot(uri=AK_SCHEMA.cdr3_end, name="cdr3_end", curie=AK_SCHEMA.curie('cdr3_end'),
                   model_uri=AK_SCHEMA.cdr3_end, domain=None, range=Optional[int])

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

slots.derivation = Slot(uri=AK_SCHEMA.derivation, name="derivation", curie=AK_SCHEMA.curie('derivation'),
                   model_uri=AK_SCHEMA.derivation, domain=None, range=Optional[Union[str, "AirrV15Derivation"]])

slots.observation_type = Slot(uri=AK_SCHEMA.observation_type, name="observation_type", curie=AK_SCHEMA.curie('observation_type'),
                   model_uri=AK_SCHEMA.observation_type, domain=None, range=Optional[Union[str, "AirrV15ObservationType"]])

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
                   model_uri=AK_SCHEMA.strand, domain=None, range=Optional[Union[str, "AirrV15Strand"]])

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

slots.fwr2_start = Slot(uri=AK_SCHEMA.fwr2_start, name="fwr2_start", curie=AK_SCHEMA.curie('fwr2_start'),
                   model_uri=AK_SCHEMA.fwr2_start, domain=None, range=Optional[int])

slots.fwr2_end = Slot(uri=AK_SCHEMA.fwr2_end, name="fwr2_end", curie=AK_SCHEMA.curie('fwr2_end'),
                   model_uri=AK_SCHEMA.fwr2_end, domain=None, range=Optional[int])

slots.fwr3_start = Slot(uri=AK_SCHEMA.fwr3_start, name="fwr3_start", curie=AK_SCHEMA.curie('fwr3_start'),
                   model_uri=AK_SCHEMA.fwr3_start, domain=None, range=Optional[int])

slots.fwr3_end = Slot(uri=AK_SCHEMA.fwr3_end, name="fwr3_end", curie=AK_SCHEMA.curie('fwr3_end'),
                   model_uri=AK_SCHEMA.fwr3_end, domain=None, range=Optional[int])

slots.alignment_labels = Slot(uri=AK_SCHEMA.alignment_labels, name="alignment_labels", curie=AK_SCHEMA.curie('alignment_labels'),
                   model_uri=AK_SCHEMA.alignment_labels, domain=None, range=Optional[Union[str, List[str]]])

slots.allele_description_id = Slot(uri=AK_SCHEMA.allele_description_id, name="allele_description_id", curie=AK_SCHEMA.curie('allele_description_id'),
                   model_uri=AK_SCHEMA.allele_description_id, domain=None, range=Optional[str])

slots.allele_description_ref = Slot(uri=AK_SCHEMA.allele_description_ref, name="allele_description_ref", curie=AK_SCHEMA.curie('allele_description_ref'),
                   model_uri=AK_SCHEMA.allele_description_ref, domain=None, range=Optional[str])

slots.maintainer = Slot(uri=AK_SCHEMA.maintainer, name="maintainer", curie=AK_SCHEMA.curie('maintainer'),
                   model_uri=AK_SCHEMA.maintainer, domain=None, range=Optional[str])

slots.acknowledgements = Slot(uri=AK_SCHEMA.acknowledgements, name="acknowledgements", curie=AK_SCHEMA.curie('acknowledgements'),
                   model_uri=AK_SCHEMA.acknowledgements, domain=None, range=Optional[Union[Union[dict, AirrV15Acknowledgement], List[Union[dict, AirrV15Acknowledgement]]]])

slots.lab_address = Slot(uri=AK_SCHEMA.lab_address, name="lab_address", curie=AK_SCHEMA.curie('lab_address'),
                   model_uri=AK_SCHEMA.lab_address, domain=None, range=Optional[str])

slots.release_version = Slot(uri=AK_SCHEMA.release_version, name="release_version", curie=AK_SCHEMA.curie('release_version'),
                   model_uri=AK_SCHEMA.release_version, domain=None, range=Optional[float])

slots.release_description = Slot(uri=AK_SCHEMA.release_description, name="release_description", curie=AK_SCHEMA.curie('release_description'),
                   model_uri=AK_SCHEMA.release_description, domain=None, range=Optional[str])

slots.coding_sequence = Slot(uri=AK_SCHEMA.coding_sequence, name="coding_sequence", curie=AK_SCHEMA.curie('coding_sequence'),
                   model_uri=AK_SCHEMA.coding_sequence, domain=None, range=Optional[str])

slots.aliases = Slot(uri=AK_SCHEMA.aliases, name="aliases", curie=AK_SCHEMA.curie('aliases'),
                   model_uri=AK_SCHEMA.aliases, domain=None, range=Optional[Union[str, List[str]]])

slots.locus = Slot(uri=AK_SCHEMA.locus, name="locus", curie=AK_SCHEMA.curie('locus'),
                   model_uri=AK_SCHEMA.locus, domain=None, range=Optional[Union[str, "AirrV15Locus"]])

slots.chromosome = Slot(uri=AK_SCHEMA.chromosome, name="chromosome", curie=AK_SCHEMA.curie('chromosome'),
                   model_uri=AK_SCHEMA.chromosome, domain=None, range=Optional[int])

slots.sequence_type = Slot(uri=AK_SCHEMA.sequence_type, name="sequence_type", curie=AK_SCHEMA.curie('sequence_type'),
                   model_uri=AK_SCHEMA.sequence_type, domain=None, range=Optional[Union[str, "AirrV15SequenceType"]])

slots.functional = Slot(uri=AK_SCHEMA.functional, name="functional", curie=AK_SCHEMA.curie('functional'),
                   model_uri=AK_SCHEMA.functional, domain=None, range=Optional[Union[bool, Bool]])

slots.inference_type = Slot(uri=AK_SCHEMA.inference_type, name="inference_type", curie=AK_SCHEMA.curie('inference_type'),
                   model_uri=AK_SCHEMA.inference_type, domain=None, range=Optional[Union[str, "AirrV15InferenceType"]])

slots.species_subgroup = Slot(uri=AK_SCHEMA.species_subgroup, name="species_subgroup", curie=AK_SCHEMA.curie('species_subgroup'),
                   model_uri=AK_SCHEMA.species_subgroup, domain=None, range=Optional[str])

slots.species_subgroup_type = Slot(uri=AK_SCHEMA.species_subgroup_type, name="species_subgroup_type", curie=AK_SCHEMA.curie('species_subgroup_type'),
                   model_uri=AK_SCHEMA.species_subgroup_type, domain=None, range=Optional[Union[str, "AirrV15SpeciesSubgroupType"]])

slots.status = Slot(uri=AK_SCHEMA.status, name="status", curie=AK_SCHEMA.curie('status'),
                   model_uri=AK_SCHEMA.status, domain=None, range=Optional[Union[str, "AirrV15Status"]])

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
                   model_uri=AK_SCHEMA.j_codon_frame, domain=None, range=Optional[Union[str, "AirrV15JCodonFrame"]])

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
                   model_uri=AK_SCHEMA.v_gene_delineations, domain=None, range=Optional[Union[Union[dict, AirrV15SequenceDelineationV], List[Union[dict, AirrV15SequenceDelineationV]]]])

slots.unrearranged_support = Slot(uri=AK_SCHEMA.unrearranged_support, name="unrearranged_support", curie=AK_SCHEMA.curie('unrearranged_support'),
                   model_uri=AK_SCHEMA.unrearranged_support, domain=None, range=Optional[Union[Union[dict, AirrV15UnrearrangedSequence], List[Union[dict, AirrV15UnrearrangedSequence]]]])

slots.rearranged_support = Slot(uri=AK_SCHEMA.rearranged_support, name="rearranged_support", curie=AK_SCHEMA.curie('rearranged_support'),
                   model_uri=AK_SCHEMA.rearranged_support, domain=None, range=Optional[Union[Union[dict, AirrV15RearrangedSequence], List[Union[dict, AirrV15RearrangedSequence]]]])

slots.paralogs = Slot(uri=AK_SCHEMA.paralogs, name="paralogs", curie=AK_SCHEMA.curie('paralogs'),
                   model_uri=AK_SCHEMA.paralogs, domain=None, range=Optional[Union[str, List[str]]])

slots.curational_tags = Slot(uri=AK_SCHEMA.curational_tags, name="curational_tags", curie=AK_SCHEMA.curie('curational_tags'),
                   model_uri=AK_SCHEMA.curational_tags, domain=None, range=Optional[Union[Union[str, "AirrV15CurationalTags"], List[Union[str, "AirrV15CurationalTags"]]]])

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
                   model_uri=AK_SCHEMA.allele_descriptions, domain=None, range=Optional[Union[Union[dict, AirrV15AlleleDescription], List[Union[dict, AirrV15AlleleDescription]]]])

slots.receptor_genotype_set_id = Slot(uri=AK_SCHEMA.receptor_genotype_set_id, name="receptor_genotype_set_id", curie=AK_SCHEMA.curie('receptor_genotype_set_id'),
                   model_uri=AK_SCHEMA.receptor_genotype_set_id, domain=None, range=Optional[str])

slots.genotype_class_list = Slot(uri=AK_SCHEMA.genotype_class_list, name="genotype_class_list", curie=AK_SCHEMA.curie('genotype_class_list'),
                   model_uri=AK_SCHEMA.genotype_class_list, domain=None, range=Optional[Union[Union[dict, AirrV15Genotype], List[Union[dict, AirrV15Genotype]]]])

slots.receptor_genotype_id = Slot(uri=AK_SCHEMA.receptor_genotype_id, name="receptor_genotype_id", curie=AK_SCHEMA.curie('receptor_genotype_id'),
                   model_uri=AK_SCHEMA.receptor_genotype_id, domain=None, range=Optional[str])

slots.documented_alleles = Slot(uri=AK_SCHEMA.documented_alleles, name="documented_alleles", curie=AK_SCHEMA.curie('documented_alleles'),
                   model_uri=AK_SCHEMA.documented_alleles, domain=None, range=Optional[Union[Union[dict, AirrV15DocumentedAllele], List[Union[dict, AirrV15DocumentedAllele]]]])

slots.undocumented_alleles = Slot(uri=AK_SCHEMA.undocumented_alleles, name="undocumented_alleles", curie=AK_SCHEMA.curie('undocumented_alleles'),
                   model_uri=AK_SCHEMA.undocumented_alleles, domain=None, range=Optional[Union[Union[dict, AirrV15UndocumentedAllele], List[Union[dict, AirrV15UndocumentedAllele]]]])

slots.deleted_genes = Slot(uri=AK_SCHEMA.deleted_genes, name="deleted_genes", curie=AK_SCHEMA.curie('deleted_genes'),
                   model_uri=AK_SCHEMA.deleted_genes, domain=None, range=Optional[Union[Union[dict, AirrV15DeletedGene], List[Union[dict, AirrV15DeletedGene]]]])

slots.inference_process = Slot(uri=AK_SCHEMA.inference_process, name="inference_process", curie=AK_SCHEMA.curie('inference_process'),
                   model_uri=AK_SCHEMA.inference_process, domain=None, range=Optional[Union[str, "AirrV15InferenceProcess"]])

slots.phasing = Slot(uri=AK_SCHEMA.phasing, name="phasing", curie=AK_SCHEMA.curie('phasing'),
                   model_uri=AK_SCHEMA.phasing, domain=None, range=Optional[int])

slots.allele_name = Slot(uri=AK_SCHEMA.allele_name, name="allele_name", curie=AK_SCHEMA.curie('allele_name'),
                   model_uri=AK_SCHEMA.allele_name, domain=None, range=Optional[str])

slots.mhc_genotype_set_id = Slot(uri=AK_SCHEMA.mhc_genotype_set_id, name="mhc_genotype_set_id", curie=AK_SCHEMA.curie('mhc_genotype_set_id'),
                   model_uri=AK_SCHEMA.mhc_genotype_set_id, domain=None, range=Optional[str])

slots.mhc_genotype_list = Slot(uri=AK_SCHEMA.mhc_genotype_list, name="mhc_genotype_list", curie=AK_SCHEMA.curie('mhc_genotype_list'),
                   model_uri=AK_SCHEMA.mhc_genotype_list, domain=None, range=Optional[Union[Union[dict, AirrV15MHCGenotype], List[Union[dict, AirrV15MHCGenotype]]]])

slots.mhc_genotype_id = Slot(uri=AK_SCHEMA.mhc_genotype_id, name="mhc_genotype_id", curie=AK_SCHEMA.curie('mhc_genotype_id'),
                   model_uri=AK_SCHEMA.mhc_genotype_id, domain=None, range=Optional[str])

slots.mhc_class = Slot(uri=AK_SCHEMA.mhc_class, name="mhc_class", curie=AK_SCHEMA.curie('mhc_class'),
                   model_uri=AK_SCHEMA.mhc_class, domain=None, range=Optional[Union[str, "AirrV15MhcClass"]])

slots.mhc_alleles = Slot(uri=AK_SCHEMA.mhc_alleles, name="mhc_alleles", curie=AK_SCHEMA.curie('mhc_alleles'),
                   model_uri=AK_SCHEMA.mhc_alleles, domain=None, range=Optional[Union[Union[dict, AirrV15MHCAllele], List[Union[dict, AirrV15MHCAllele]]]])

slots.mhc_genotyping_method = Slot(uri=AK_SCHEMA.mhc_genotyping_method, name="mhc_genotyping_method", curie=AK_SCHEMA.curie('mhc_genotyping_method'),
                   model_uri=AK_SCHEMA.mhc_genotyping_method, domain=None, range=Optional[str])

slots.gene = Slot(uri=AK_SCHEMA.gene, name="gene", curie=AK_SCHEMA.curie('gene'),
                   model_uri=AK_SCHEMA.gene, domain=None, range=Optional[Union[str, "AirrV15Gene"]])

slots.reference_set_ref = Slot(uri=AK_SCHEMA.reference_set_ref, name="reference_set_ref", curie=AK_SCHEMA.curie('reference_set_ref'),
                   model_uri=AK_SCHEMA.reference_set_ref, domain=None, range=Optional[str])

slots.receptor_genotype_set = Slot(uri=AK_SCHEMA.receptor_genotype_set, name="receptor_genotype_set", curie=AK_SCHEMA.curie('receptor_genotype_set'),
                   model_uri=AK_SCHEMA.receptor_genotype_set, domain=None, range=Optional[Union[dict, AirrV15GenotypeSet]])

slots.mhc_genotype_set = Slot(uri=AK_SCHEMA.mhc_genotype_set, name="mhc_genotype_set", curie=AK_SCHEMA.curie('mhc_genotype_set'),
                   model_uri=AK_SCHEMA.mhc_genotype_set, domain=None, range=Optional[Union[dict, AirrV15MHCGenotypeSet]])

slots.study_id = Slot(uri=AK_SCHEMA.study_id, name="study_id", curie=AK_SCHEMA.curie('study_id'),
                   model_uri=AK_SCHEMA.study_id, domain=None, range=Optional[str])

slots.study_title = Slot(uri=AK_SCHEMA.study_title, name="study_title", curie=AK_SCHEMA.curie('study_title'),
                   model_uri=AK_SCHEMA.study_title, domain=None, range=Optional[str])

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
                   model_uri=AK_SCHEMA.keywords_study, domain=None, range=Optional[Union[Union[str, "AirrV15KeywordsStudy"], List[Union[str, "AirrV15KeywordsStudy"]]]])

slots.adc_publish_date = Slot(uri=AK_SCHEMA.adc_publish_date, name="adc_publish_date", curie=AK_SCHEMA.curie('adc_publish_date'),
                   model_uri=AK_SCHEMA.adc_publish_date, domain=None, range=Optional[str])

slots.adc_update_date = Slot(uri=AK_SCHEMA.adc_update_date, name="adc_update_date", curie=AK_SCHEMA.curie('adc_update_date'),
                   model_uri=AK_SCHEMA.adc_update_date, domain=None, range=Optional[str])

slots.subject_id = Slot(uri=AK_SCHEMA.subject_id, name="subject_id", curie=AK_SCHEMA.curie('subject_id'),
                   model_uri=AK_SCHEMA.subject_id, domain=None, range=Optional[str])

slots.synthetic = Slot(uri=AK_SCHEMA.synthetic, name="synthetic", curie=AK_SCHEMA.curie('synthetic'),
                   model_uri=AK_SCHEMA.synthetic, domain=None, range=Optional[Union[bool, Bool]])

slots.sex = Slot(uri=AK_SCHEMA.sex, name="sex", curie=AK_SCHEMA.curie('sex'),
                   model_uri=AK_SCHEMA.sex, domain=None, range=Optional[Union[str, "AirrV15Sex"]])

slots.age_min = Slot(uri=AK_SCHEMA.age_min, name="age_min", curie=AK_SCHEMA.curie('age_min'),
                   model_uri=AK_SCHEMA.age_min, domain=None, range=Optional[float])

slots.age_max = Slot(uri=AK_SCHEMA.age_max, name="age_max", curie=AK_SCHEMA.curie('age_max'),
                   model_uri=AK_SCHEMA.age_max, domain=None, range=Optional[float])

slots.ancestry_population = Slot(uri=AK_SCHEMA.ancestry_population, name="ancestry_population", curie=AK_SCHEMA.curie('ancestry_population'),
                   model_uri=AK_SCHEMA.ancestry_population, domain=None, range=Optional[str])

slots.strain_name = Slot(uri=AK_SCHEMA.strain_name, name="strain_name", curie=AK_SCHEMA.curie('strain_name'),
                   model_uri=AK_SCHEMA.strain_name, domain=None, range=Optional[str])

slots.linked_subjects = Slot(uri=AK_SCHEMA.linked_subjects, name="linked_subjects", curie=AK_SCHEMA.curie('linked_subjects'),
                   model_uri=AK_SCHEMA.linked_subjects, domain=None, range=Optional[str])

slots.link_type = Slot(uri=AK_SCHEMA.link_type, name="link_type", curie=AK_SCHEMA.curie('link_type'),
                   model_uri=AK_SCHEMA.link_type, domain=None, range=Optional[str])

slots.diagnosis = Slot(uri=AK_SCHEMA.diagnosis, name="diagnosis", curie=AK_SCHEMA.curie('diagnosis'),
                   model_uri=AK_SCHEMA.diagnosis, domain=None, range=Optional[Union[Union[dict, AirrV15Diagnosis], List[Union[dict, AirrV15Diagnosis]]]])

slots.genotype = Slot(uri=AK_SCHEMA.genotype, name="genotype", curie=AK_SCHEMA.curie('genotype'),
                   model_uri=AK_SCHEMA.genotype, domain=None, range=Optional[Union[dict, AirrV15SubjectGenotype]])

slots.study_group_description = Slot(uri=AK_SCHEMA.study_group_description, name="study_group_description", curie=AK_SCHEMA.curie('study_group_description'),
                   model_uri=AK_SCHEMA.study_group_description, domain=None, range=Optional[str])

slots.disease_diagnosis = Slot(uri=AK_SCHEMA.disease_diagnosis, name="disease_diagnosis", curie=AK_SCHEMA.curie('disease_diagnosis'),
                   model_uri=AK_SCHEMA.disease_diagnosis, domain=None, range=Optional[Union[str, "AirrV15DiseaseDiagnosis"]])

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

slots.sample_type = Slot(uri=AK_SCHEMA.sample_type, name="sample_type", curie=AK_SCHEMA.curie('sample_type'),
                   model_uri=AK_SCHEMA.sample_type, domain=None, range=Optional[str])

slots.anatomic_site = Slot(uri=AK_SCHEMA.anatomic_site, name="anatomic_site", curie=AK_SCHEMA.curie('anatomic_site'),
                   model_uri=AK_SCHEMA.anatomic_site, domain=None, range=Optional[str])

slots.disease_state_sample = Slot(uri=AK_SCHEMA.disease_state_sample, name="disease_state_sample", curie=AK_SCHEMA.curie('disease_state_sample'),
                   model_uri=AK_SCHEMA.disease_state_sample, domain=None, range=Optional[str])

slots.collection_time_point_relative = Slot(uri=AK_SCHEMA.collection_time_point_relative, name="collection_time_point_relative", curie=AK_SCHEMA.curie('collection_time_point_relative'),
                   model_uri=AK_SCHEMA.collection_time_point_relative, domain=None, range=Optional[float])

slots.collection_time_point_relative_unit = Slot(uri=AK_SCHEMA.collection_time_point_relative_unit, name="collection_time_point_relative_unit", curie=AK_SCHEMA.curie('collection_time_point_relative_unit'),
                   model_uri=AK_SCHEMA.collection_time_point_relative_unit, domain=None, range=Optional[Union[str, "AirrV15CollectionTimePointRelativeUnit"]])

slots.collection_time_point_reference = Slot(uri=AK_SCHEMA.collection_time_point_reference, name="collection_time_point_reference", curie=AK_SCHEMA.curie('collection_time_point_reference'),
                   model_uri=AK_SCHEMA.collection_time_point_reference, domain=None, range=Optional[str])

slots.biomaterial_provider = Slot(uri=AK_SCHEMA.biomaterial_provider, name="biomaterial_provider", curie=AK_SCHEMA.curie('biomaterial_provider'),
                   model_uri=AK_SCHEMA.biomaterial_provider, domain=None, range=Optional[str])

slots.tissue_processing = Slot(uri=AK_SCHEMA.tissue_processing, name="tissue_processing", curie=AK_SCHEMA.curie('tissue_processing'),
                   model_uri=AK_SCHEMA.tissue_processing, domain=None, range=Optional[str])

slots.cell_subset = Slot(uri=AK_SCHEMA.cell_subset, name="cell_subset", curie=AK_SCHEMA.curie('cell_subset'),
                   model_uri=AK_SCHEMA.cell_subset, domain=None, range=Optional[Union[str, "AirrV15CellSubset"]])

slots.cell_phenotype = Slot(uri=AK_SCHEMA.cell_phenotype, name="cell_phenotype", curie=AK_SCHEMA.curie('cell_phenotype'),
                   model_uri=AK_SCHEMA.cell_phenotype, domain=None, range=Optional[str])

slots.cell_species = Slot(uri=AK_SCHEMA.cell_species, name="cell_species", curie=AK_SCHEMA.curie('cell_species'),
                   model_uri=AK_SCHEMA.cell_species, domain=None, range=Optional[Union[str, "AirrV15CellSpecies"]])

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
                   model_uri=AK_SCHEMA.pcr_target_locus, domain=None, range=Optional[Union[str, "AirrV15PcrTargetLocus"]])

slots.forward_pcr_primer_target_location = Slot(uri=AK_SCHEMA.forward_pcr_primer_target_location, name="forward_pcr_primer_target_location", curie=AK_SCHEMA.curie('forward_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.forward_pcr_primer_target_location, domain=None, range=Optional[str])

slots.reverse_pcr_primer_target_location = Slot(uri=AK_SCHEMA.reverse_pcr_primer_target_location, name="reverse_pcr_primer_target_location", curie=AK_SCHEMA.curie('reverse_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.reverse_pcr_primer_target_location, domain=None, range=Optional[str])

slots.template_class = Slot(uri=AK_SCHEMA.template_class, name="template_class", curie=AK_SCHEMA.curie('template_class'),
                   model_uri=AK_SCHEMA.template_class, domain=None, range=Optional[Union[str, "AirrV15TemplateClass"]])

slots.template_quality = Slot(uri=AK_SCHEMA.template_quality, name="template_quality", curie=AK_SCHEMA.curie('template_quality'),
                   model_uri=AK_SCHEMA.template_quality, domain=None, range=Optional[str])

slots.template_amount = Slot(uri=AK_SCHEMA.template_amount, name="template_amount", curie=AK_SCHEMA.curie('template_amount'),
                   model_uri=AK_SCHEMA.template_amount, domain=None, range=Optional[float])

slots.template_amount_unit = Slot(uri=AK_SCHEMA.template_amount_unit, name="template_amount_unit", curie=AK_SCHEMA.curie('template_amount_unit'),
                   model_uri=AK_SCHEMA.template_amount_unit, domain=None, range=Optional[Union[str, "AirrV15TemplateAmountUnit"]])

slots.library_generation_method = Slot(uri=AK_SCHEMA.library_generation_method, name="library_generation_method", curie=AK_SCHEMA.curie('library_generation_method'),
                   model_uri=AK_SCHEMA.library_generation_method, domain=None, range=Optional[Union[str, "AirrV15LibraryGenerationMethod"]])

slots.library_generation_protocol = Slot(uri=AK_SCHEMA.library_generation_protocol, name="library_generation_protocol", curie=AK_SCHEMA.curie('library_generation_protocol'),
                   model_uri=AK_SCHEMA.library_generation_protocol, domain=None, range=Optional[str])

slots.library_generation_kit_version = Slot(uri=AK_SCHEMA.library_generation_kit_version, name="library_generation_kit_version", curie=AK_SCHEMA.curie('library_generation_kit_version'),
                   model_uri=AK_SCHEMA.library_generation_kit_version, domain=None, range=Optional[str])

slots.pcr_target = Slot(uri=AK_SCHEMA.pcr_target, name="pcr_target", curie=AK_SCHEMA.curie('pcr_target'),
                   model_uri=AK_SCHEMA.pcr_target, domain=None, range=Optional[Union[Union[dict, AirrV15PCRTarget], List[Union[dict, AirrV15PCRTarget]]]])

slots.complete_sequences = Slot(uri=AK_SCHEMA.complete_sequences, name="complete_sequences", curie=AK_SCHEMA.curie('complete_sequences'),
                   model_uri=AK_SCHEMA.complete_sequences, domain=None, range=Optional[Union[str, "AirrV15CompleteSequences"]])

slots.physical_linkage = Slot(uri=AK_SCHEMA.physical_linkage, name="physical_linkage", curie=AK_SCHEMA.curie('physical_linkage'),
                   model_uri=AK_SCHEMA.physical_linkage, domain=None, range=Optional[Union[str, "AirrV15PhysicalLinkage"]])

slots.sequencing_run_id = Slot(uri=AK_SCHEMA.sequencing_run_id, name="sequencing_run_id", curie=AK_SCHEMA.curie('sequencing_run_id'),
                   model_uri=AK_SCHEMA.sequencing_run_id, domain=None, range=Optional[str])

slots.total_reads_passing_qc_filter = Slot(uri=AK_SCHEMA.total_reads_passing_qc_filter, name="total_reads_passing_qc_filter", curie=AK_SCHEMA.curie('total_reads_passing_qc_filter'),
                   model_uri=AK_SCHEMA.total_reads_passing_qc_filter, domain=None, range=Optional[int])

slots.sequencing_platform = Slot(uri=AK_SCHEMA.sequencing_platform, name="sequencing_platform", curie=AK_SCHEMA.curie('sequencing_platform'),
                   model_uri=AK_SCHEMA.sequencing_platform, domain=None, range=Optional[str])

slots.sequencing_facility = Slot(uri=AK_SCHEMA.sequencing_facility, name="sequencing_facility", curie=AK_SCHEMA.curie('sequencing_facility'),
                   model_uri=AK_SCHEMA.sequencing_facility, domain=None, range=Optional[str])

slots.sequencing_run_date = Slot(uri=AK_SCHEMA.sequencing_run_date, name="sequencing_run_date", curie=AK_SCHEMA.curie('sequencing_run_date'),
                   model_uri=AK_SCHEMA.sequencing_run_date, domain=None, range=Optional[str])

slots.sequencing_kit = Slot(uri=AK_SCHEMA.sequencing_kit, name="sequencing_kit", curie=AK_SCHEMA.curie('sequencing_kit'),
                   model_uri=AK_SCHEMA.sequencing_kit, domain=None, range=Optional[str])

slots.sequencing_files = Slot(uri=AK_SCHEMA.sequencing_files, name="sequencing_files", curie=AK_SCHEMA.curie('sequencing_files'),
                   model_uri=AK_SCHEMA.sequencing_files, domain=None, range=Optional[Union[dict, AirrV15SequencingData]])

slots.sequencing_data_id = Slot(uri=AK_SCHEMA.sequencing_data_id, name="sequencing_data_id", curie=AK_SCHEMA.curie('sequencing_data_id'),
                   model_uri=AK_SCHEMA.sequencing_data_id, domain=None, range=Optional[str])

slots.file_type = Slot(uri=AK_SCHEMA.file_type, name="file_type", curie=AK_SCHEMA.curie('file_type'),
                   model_uri=AK_SCHEMA.file_type, domain=None, range=Optional[Union[str, "AirrV15FileType"]])

slots.filename = Slot(uri=AK_SCHEMA.filename, name="filename", curie=AK_SCHEMA.curie('filename'),
                   model_uri=AK_SCHEMA.filename, domain=None, range=Optional[str])

slots.read_direction = Slot(uri=AK_SCHEMA.read_direction, name="read_direction", curie=AK_SCHEMA.curie('read_direction'),
                   model_uri=AK_SCHEMA.read_direction, domain=None, range=Optional[Union[str, "AirrV15ReadDirection"]])

slots.read_length = Slot(uri=AK_SCHEMA.read_length, name="read_length", curie=AK_SCHEMA.curie('read_length'),
                   model_uri=AK_SCHEMA.read_length, domain=None, range=Optional[int])

slots.paired_filename = Slot(uri=AK_SCHEMA.paired_filename, name="paired_filename", curie=AK_SCHEMA.curie('paired_filename'),
                   model_uri=AK_SCHEMA.paired_filename, domain=None, range=Optional[str])

slots.paired_read_direction = Slot(uri=AK_SCHEMA.paired_read_direction, name="paired_read_direction", curie=AK_SCHEMA.curie('paired_read_direction'),
                   model_uri=AK_SCHEMA.paired_read_direction, domain=None, range=Optional[Union[str, "AirrV15PairedReadDirection"]])

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
                   model_uri=AK_SCHEMA.study, domain=None, range=Optional[Union[dict, AirrV15Study]])

slots.subject = Slot(uri=AK_SCHEMA.subject, name="subject", curie=AK_SCHEMA.curie('subject'),
                   model_uri=AK_SCHEMA.subject, domain=None, range=Optional[Union[dict, AirrV15Subject]])

slots.sample = Slot(uri=AK_SCHEMA.sample, name="sample", curie=AK_SCHEMA.curie('sample'),
                   model_uri=AK_SCHEMA.sample, domain=None, range=Optional[Union[Union[dict, AirrV15SampleProcessing], List[Union[dict, AirrV15SampleProcessing]]]])

slots.data_processing = Slot(uri=AK_SCHEMA.data_processing, name="data_processing", curie=AK_SCHEMA.curie('data_processing'),
                   model_uri=AK_SCHEMA.data_processing, domain=None, range=Optional[Union[Union[dict, AirrV15DataProcessing], List[Union[dict, AirrV15DataProcessing]]]])

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

slots.productive = Slot(uri=AK_SCHEMA.productive, name="productive", curie=AK_SCHEMA.curie('productive'),
                   model_uri=AK_SCHEMA.productive, domain=None, range=Optional[Union[bool, Bool]])

slots.vj_in_frame = Slot(uri=AK_SCHEMA.vj_in_frame, name="vj_in_frame", curie=AK_SCHEMA.curie('vj_in_frame'),
                   model_uri=AK_SCHEMA.vj_in_frame, domain=None, range=Optional[Union[bool, Bool]])

slots.stop_codon = Slot(uri=AK_SCHEMA.stop_codon, name="stop_codon", curie=AK_SCHEMA.curie('stop_codon'),
                   model_uri=AK_SCHEMA.stop_codon, domain=None, range=Optional[Union[bool, Bool]])

slots.complete_vdj = Slot(uri=AK_SCHEMA.complete_vdj, name="complete_vdj", curie=AK_SCHEMA.curie('complete_vdj'),
                   model_uri=AK_SCHEMA.complete_vdj, domain=None, range=Optional[Union[bool, Bool]])

slots.d2_call = Slot(uri=AK_SCHEMA.d2_call, name="d2_call", curie=AK_SCHEMA.curie('d2_call'),
                   model_uri=AK_SCHEMA.d2_call, domain=None, range=Optional[str])

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

slots.cdr2 = Slot(uri=AK_SCHEMA.cdr2, name="cdr2", curie=AK_SCHEMA.curie('cdr2'),
                   model_uri=AK_SCHEMA.cdr2, domain=None, range=Optional[str])

slots.cdr3 = Slot(uri=AK_SCHEMA.cdr3, name="cdr3", curie=AK_SCHEMA.curie('cdr3'),
                   model_uri=AK_SCHEMA.cdr3, domain=None, range=Optional[str])

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
                   model_uri=AK_SCHEMA.nodes, domain=None, range=Optional[str])

slots.rearrangements = Slot(uri=AK_SCHEMA.rearrangements, name="rearrangements", curie=AK_SCHEMA.curie('rearrangements'),
                   model_uri=AK_SCHEMA.rearrangements, domain=None, range=Optional[Union[str, List[str]]])

slots.receptors = Slot(uri=AK_SCHEMA.receptors, name="receptors", curie=AK_SCHEMA.curie('receptors'),
                   model_uri=AK_SCHEMA.receptors, domain=None, range=Optional[Union[str, List[str]]])

slots.expression_study_method = Slot(uri=AK_SCHEMA.expression_study_method, name="expression_study_method", curie=AK_SCHEMA.curie('expression_study_method'),
                   model_uri=AK_SCHEMA.expression_study_method, domain=None, range=Optional[Union[str, "AirrV15ExpressionStudyMethod"]])

slots.expression_raw_doi = Slot(uri=AK_SCHEMA.expression_raw_doi, name="expression_raw_doi", curie=AK_SCHEMA.curie('expression_raw_doi'),
                   model_uri=AK_SCHEMA.expression_raw_doi, domain=None, range=Optional[str])

slots.expression_index = Slot(uri=AK_SCHEMA.expression_index, name="expression_index", curie=AK_SCHEMA.curie('expression_index'),
                   model_uri=AK_SCHEMA.expression_index, domain=None, range=Optional[str])

slots.virtual_pairing = Slot(uri=AK_SCHEMA.virtual_pairing, name="virtual_pairing", curie=AK_SCHEMA.curie('virtual_pairing'),
                   model_uri=AK_SCHEMA.virtual_pairing, domain=None, range=Optional[Union[bool, Bool]])

slots.expression_id = Slot(uri=AK_SCHEMA.expression_id, name="expression_id", curie=AK_SCHEMA.curie('expression_id'),
                   model_uri=AK_SCHEMA.expression_id, domain=None, range=Optional[str])

slots.property_type = Slot(uri=AK_SCHEMA.property_type, name="property_type", curie=AK_SCHEMA.curie('property_type'),
                   model_uri=AK_SCHEMA.property_type, domain=None, range=Optional[str])

slots.property = Slot(uri=AK_SCHEMA.property, name="property", curie=AK_SCHEMA.curie('property'),
                   model_uri=AK_SCHEMA.property, domain=None, range=Optional[Union[str, "AirrV15Property"]])

slots.receptor_id = Slot(uri=AK_SCHEMA.receptor_id, name="receptor_id", curie=AK_SCHEMA.curie('receptor_id'),
                   model_uri=AK_SCHEMA.receptor_id, domain=None, range=Optional[str])

slots.receptor_hash = Slot(uri=AK_SCHEMA.receptor_hash, name="receptor_hash", curie=AK_SCHEMA.curie('receptor_hash'),
                   model_uri=AK_SCHEMA.receptor_hash, domain=None, range=Optional[str])

slots.receptor_type = Slot(uri=AK_SCHEMA.receptor_type, name="receptor_type", curie=AK_SCHEMA.curie('receptor_type'),
                   model_uri=AK_SCHEMA.receptor_type, domain=None, range=Optional[Union[str, "AirrV15ReceptorType"]])

slots.receptor_variable_domain_1_aa = Slot(uri=AK_SCHEMA.receptor_variable_domain_1_aa, name="receptor_variable_domain_1_aa", curie=AK_SCHEMA.curie('receptor_variable_domain_1_aa'),
                   model_uri=AK_SCHEMA.receptor_variable_domain_1_aa, domain=None, range=Optional[str])

slots.receptor_variable_domain_1_locus = Slot(uri=AK_SCHEMA.receptor_variable_domain_1_locus, name="receptor_variable_domain_1_locus", curie=AK_SCHEMA.curie('receptor_variable_domain_1_locus'),
                   model_uri=AK_SCHEMA.receptor_variable_domain_1_locus, domain=None, range=Optional[Union[str, "AirrV15ReceptorVariableDomain1Locus"]])

slots.receptor_variable_domain_2_aa = Slot(uri=AK_SCHEMA.receptor_variable_domain_2_aa, name="receptor_variable_domain_2_aa", curie=AK_SCHEMA.curie('receptor_variable_domain_2_aa'),
                   model_uri=AK_SCHEMA.receptor_variable_domain_2_aa, domain=None, range=Optional[str])

slots.receptor_variable_domain_2_locus = Slot(uri=AK_SCHEMA.receptor_variable_domain_2_locus, name="receptor_variable_domain_2_locus", curie=AK_SCHEMA.curie('receptor_variable_domain_2_locus'),
                   model_uri=AK_SCHEMA.receptor_variable_domain_2_locus, domain=None, range=Optional[Union[str, "AirrV15ReceptorVariableDomain2Locus"]])

slots.receptor_ref = Slot(uri=AK_SCHEMA.receptor_ref, name="receptor_ref", curie=AK_SCHEMA.curie('receptor_ref'),
                   model_uri=AK_SCHEMA.receptor_ref, domain=None, range=Optional[Union[str, List[str]]])

slots.reactivity_measurements = Slot(uri=AK_SCHEMA.reactivity_measurements, name="reactivity_measurements", curie=AK_SCHEMA.curie('reactivity_measurements'),
                   model_uri=AK_SCHEMA.reactivity_measurements, domain=None, range=Optional[Union[Union[dict, AirrV15ReceptorReactivity], List[Union[dict, AirrV15ReceptorReactivity]]]])

slots.ligand_type = Slot(uri=AK_SCHEMA.ligand_type, name="ligand_type", curie=AK_SCHEMA.curie('ligand_type'),
                   model_uri=AK_SCHEMA.ligand_type, domain=None, range=Optional[Union[str, "AirrV15LigandType"]])

slots.antigen_type = Slot(uri=AK_SCHEMA.antigen_type, name="antigen_type", curie=AK_SCHEMA.curie('antigen_type'),
                   model_uri=AK_SCHEMA.antigen_type, domain=None, range=Optional[Union[str, "AirrV15AntigenType"]])

slots.antigen = Slot(uri=AK_SCHEMA.antigen, name="antigen", curie=AK_SCHEMA.curie('antigen'),
                   model_uri=AK_SCHEMA.antigen, domain=None, range=Optional[Union[str, "AirrV15Antigen"]])

slots.antigen_source_species = Slot(uri=AK_SCHEMA.antigen_source_species, name="antigen_source_species", curie=AK_SCHEMA.curie('antigen_source_species'),
                   model_uri=AK_SCHEMA.antigen_source_species, domain=None, range=Optional[Union[str, "AirrV15AntigenSourceSpecies"]])

slots.peptide_start = Slot(uri=AK_SCHEMA.peptide_start, name="peptide_start", curie=AK_SCHEMA.curie('peptide_start'),
                   model_uri=AK_SCHEMA.peptide_start, domain=None, range=Optional[int])

slots.peptide_end = Slot(uri=AK_SCHEMA.peptide_end, name="peptide_end", curie=AK_SCHEMA.curie('peptide_end'),
                   model_uri=AK_SCHEMA.peptide_end, domain=None, range=Optional[int])

slots.mhc_gene_1 = Slot(uri=AK_SCHEMA.mhc_gene_1, name="mhc_gene_1", curie=AK_SCHEMA.curie('mhc_gene_1'),
                   model_uri=AK_SCHEMA.mhc_gene_1, domain=None, range=Optional[Union[str, "AirrV15MhcGene1"]])

slots.mhc_allele_1 = Slot(uri=AK_SCHEMA.mhc_allele_1, name="mhc_allele_1", curie=AK_SCHEMA.curie('mhc_allele_1'),
                   model_uri=AK_SCHEMA.mhc_allele_1, domain=None, range=Optional[str])

slots.mhc_gene_2 = Slot(uri=AK_SCHEMA.mhc_gene_2, name="mhc_gene_2", curie=AK_SCHEMA.curie('mhc_gene_2'),
                   model_uri=AK_SCHEMA.mhc_gene_2, domain=None, range=Optional[Union[str, "AirrV15MhcGene2"]])

slots.mhc_allele_2 = Slot(uri=AK_SCHEMA.mhc_allele_2, name="mhc_allele_2", curie=AK_SCHEMA.curie('mhc_allele_2'),
                   model_uri=AK_SCHEMA.mhc_allele_2, domain=None, range=Optional[str])

slots.reactivity_method = Slot(uri=AK_SCHEMA.reactivity_method, name="reactivity_method", curie=AK_SCHEMA.curie('reactivity_method'),
                   model_uri=AK_SCHEMA.reactivity_method, domain=None, range=Optional[Union[str, "AirrV15ReactivityMethod"]])

slots.reactivity_readout = Slot(uri=AK_SCHEMA.reactivity_readout, name="reactivity_readout", curie=AK_SCHEMA.curie('reactivity_readout'),
                   model_uri=AK_SCHEMA.reactivity_readout, domain=None, range=Optional[Union[str, "AirrV15ReactivityReadout"]])

slots.reactivity_value = Slot(uri=AK_SCHEMA.reactivity_value, name="reactivity_value", curie=AK_SCHEMA.curie('reactivity_value'),
                   model_uri=AK_SCHEMA.reactivity_value, domain=None, range=Optional[float])

slots.reactivity_unit = Slot(uri=AK_SCHEMA.reactivity_unit, name="reactivity_unit", curie=AK_SCHEMA.curie('reactivity_unit'),
                   model_uri=AK_SCHEMA.reactivity_unit, domain=None, range=Optional[str])

slots.chain_domain = Slot(uri=AK_SCHEMA.chain_domain, name="chain_domain", curie=AK_SCHEMA.curie('chain_domain'),
                   model_uri=AK_SCHEMA.chain_domain, domain=None, range=Optional[Union[str, ChainAkcId]])

slots.chain_codomain = Slot(uri=AK_SCHEMA.chain_codomain, name="chain_codomain", curie=AK_SCHEMA.curie('chain_codomain'),
                   model_uri=AK_SCHEMA.chain_codomain, domain=None, range=Optional[Union[str, ChainAkcId]])

slots.chain_similarity_type = Slot(uri=RDF.type, name="chain_similarity_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.chain_similarity_type, domain=None, range=Optional[Union[str, "ChainSimilarityType"]])

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

slots.aIRRKnowledgeCommons__assays = Slot(uri=AK_SCHEMA.assays, name="aIRRKnowledgeCommons__assays", curie=AK_SCHEMA.curie('assays'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__assays, domain=None, range=Optional[Union[Dict[Union[str, AssayAkcId], Union[dict, Assay]], List[Union[dict, Assay]]]])

slots.aIRRKnowledgeCommons__datasets = Slot(uri=AK_SCHEMA.datasets, name="aIRRKnowledgeCommons__datasets", curie=AK_SCHEMA.curie('datasets'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__datasets, domain=None, range=Optional[Union[Dict[Union[str, DatasetAkcId], Union[dict, Dataset]], List[Union[dict, Dataset]]]])

slots.aIRRKnowledgeCommons__conclusions = Slot(uri=AK_SCHEMA.conclusions, name="aIRRKnowledgeCommons__conclusions", curie=AK_SCHEMA.curie('conclusions'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__conclusions, domain=None, range=Optional[Union[Dict[Union[str, ConclusionAkcId], Union[dict, Conclusion]], List[Union[dict, Conclusion]]]])