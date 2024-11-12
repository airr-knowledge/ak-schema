# Auto generated from ak_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-11-12T13:12:15
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


class AssayAkcId(NamedThingAkcId):
    pass


class TCellReceptorEpitopeBindingAssayAkcId(AssayAkcId):
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
    type: Optional[str] = None
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

        self.type = str(self.class_name)

        if self.assay_type is not None and not isinstance(self.assay_type, str):
            self.assay_type = str(self.assay_type)

        if self.target_entity_type is not None and not isinstance(self.target_entity_type, str):
            self.target_entity_type = str(self.target_entity_type)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

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
class TCellReceptorEpitopeBindingAssay(Assay):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["1110037"]
    class_class_curie: ClassVar[str] = "OBI:1110037"
    class_name: ClassVar[str] = "TCellReceptorEpitopeBindingAssay"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.TCellReceptorEpitopeBindingAssay

    akc_id: Union[str, TCellReceptorEpitopeBindingAssayAkcId] = None
    specimen: Optional[Union[str, SpecimenAkcId]] = None
    assay_type: Optional[str] = None
    epitope: Optional[Union[str, EpitopeAkcId]] = None
    tcell_receptors: Optional[Union[Union[str, TCellReceptorAkcId], List[Union[str, TCellReceptorAkcId]]]] = empty_list()
    value: Optional[str] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, TCellReceptorEpitopeBindingAssayAkcId):
            self.akc_id = TCellReceptorEpitopeBindingAssayAkcId(self.akc_id)

        if self.specimen is not None and not isinstance(self.specimen, SpecimenAkcId):
            self.specimen = SpecimenAkcId(self.specimen)

        if self.assay_type is not None and not isinstance(self.assay_type, str):
            self.assay_type = str(self.assay_type)

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
class V1p4TimePoint(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4TimePoint"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4TimePoint"
    class_name: ClassVar[str] = "V1p4_TimePoint"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4TimePoint

    time_pointlabel: Optional[str] = None
    time_pointvalue: Optional[float] = None
    time_pointunit: Optional[Union[str, "V1p4Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.time_pointlabel is not None and not isinstance(self.time_pointlabel, str):
            self.time_pointlabel = str(self.time_pointlabel)

        if self.time_pointvalue is not None and not isinstance(self.time_pointvalue, float):
            self.time_pointvalue = float(self.time_pointvalue)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4TimeInterval(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4TimeInterval"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4TimeInterval"
    class_name: ClassVar[str] = "V1p4_TimeInterval"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4TimeInterval

    time_intervalmin: Optional[float] = None
    time_intervalmax: Optional[float] = None
    time_intervalunit: Optional[Union[str, "V1p4Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.time_intervalmin is not None and not isinstance(self.time_intervalmin, float):
            self.time_intervalmin = float(self.time_intervalmin)

        if self.time_intervalmax is not None and not isinstance(self.time_intervalmax, float):
            self.time_intervalmax = float(self.time_intervalmax)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4PhysicalQuantity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4PhysicalQuantity"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4PhysicalQuantity"
    class_name: ClassVar[str] = "V1p4_PhysicalQuantity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4PhysicalQuantity

    physical_quantityquantity: Optional[float] = None
    physical_quantityunit: Optional[Union[str, "V1p4Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.physical_quantityquantity is not None and not isinstance(self.physical_quantityquantity, float):
            self.physical_quantityquantity = float(self.physical_quantityquantity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4TimeQuantity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4TimeQuantity"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4TimeQuantity"
    class_name: ClassVar[str] = "V1p4_TimeQuantity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4TimeQuantity

    time_quantityquantity: Optional[float] = None
    time_quantityunit: Optional[Union[str, "V1p4Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.time_quantityquantity is not None and not isinstance(self.time_quantityquantity, float):
            self.time_quantityquantity = float(self.time_quantityquantity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Contributor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Contributor"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Contributor"
    class_name: ClassVar[str] = "V1p4_Contributor"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Contributor

    contributorcontributor_id: str = None
    contributorname: str = None
    contributororcid_id: Optional[Union[str, "V1p4OrcidId"]] = None
    contributoraffiliation: Optional[Union[str, "V1p4Affiliation"]] = None
    contributoraffiliation_department: Optional[str] = None
    contributorcontributions: Optional[Union[Union[dict, "V1p4ContributorContribution"], List[Union[dict, "V1p4ContributorContribution"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.contributorcontributor_id):
            self.MissingRequiredField("contributorcontributor_id")
        if not isinstance(self.contributorcontributor_id, str):
            self.contributorcontributor_id = str(self.contributorcontributor_id)

        if self._is_empty(self.contributorname):
            self.MissingRequiredField("contributorname")
        if not isinstance(self.contributorname, str):
            self.contributorname = str(self.contributorname)

        if self.contributoraffiliation_department is not None and not isinstance(self.contributoraffiliation_department, str):
            self.contributoraffiliation_department = str(self.contributoraffiliation_department)

        self._normalize_inlined_as_dict(slot_name="contributorcontributions", slot_type=V1p4ContributorContribution, key_name="contributor_contributionrole", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4ContributorContribution(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4ContributorContribution"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4ContributorContribution"
    class_name: ClassVar[str] = "V1p4_ContributorContribution"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4ContributorContribution

    contributor_contributionrole: Union[str, "V1p4Role"] = None
    contributor_contributiondegree: Optional[Union[str, "V1p4Degree"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.contributor_contributionrole):
            self.MissingRequiredField("contributor_contributionrole")
        if not isinstance(self.contributor_contributionrole, V1p4Role):
            self.contributor_contributionrole = V1p4Role(self.contributor_contributionrole)

        if self.contributor_contributiondegree is not None and not isinstance(self.contributor_contributiondegree, V1p4Degree):
            self.contributor_contributiondegree = V1p4Degree(self.contributor_contributiondegree)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4RearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4RearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4RearrangedSequence"
    class_name: ClassVar[str] = "V1p4_RearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4RearrangedSequence

    rearranged_sequencesequence_id: str = None
    rearranged_sequencesequence: str = None
    rearranged_sequencederivation: Union[str, "V1p4Derivation"] = None
    rearranged_sequenceobservation_type: Union[str, "V1p4ObservationType"] = None
    rearranged_sequencerepository_name: str = None
    rearranged_sequencedeposited_version: str = None
    rearranged_sequencecuration: Optional[str] = None
    rearranged_sequencerepository_ref: Optional[str] = None
    rearranged_sequencesequence_start: Optional[int] = None
    rearranged_sequencesequence_end: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.rearranged_sequencesequence_id):
            self.MissingRequiredField("rearranged_sequencesequence_id")
        if not isinstance(self.rearranged_sequencesequence_id, str):
            self.rearranged_sequencesequence_id = str(self.rearranged_sequencesequence_id)

        if self._is_empty(self.rearranged_sequencesequence):
            self.MissingRequiredField("rearranged_sequencesequence")
        if not isinstance(self.rearranged_sequencesequence, str):
            self.rearranged_sequencesequence = str(self.rearranged_sequencesequence)

        if self._is_empty(self.rearranged_sequencederivation):
            self.MissingRequiredField("rearranged_sequencederivation")
        if not isinstance(self.rearranged_sequencederivation, V1p4Derivation):
            self.rearranged_sequencederivation = V1p4Derivation(self.rearranged_sequencederivation)

        if self._is_empty(self.rearranged_sequenceobservation_type):
            self.MissingRequiredField("rearranged_sequenceobservation_type")
        if not isinstance(self.rearranged_sequenceobservation_type, V1p4ObservationType):
            self.rearranged_sequenceobservation_type = V1p4ObservationType(self.rearranged_sequenceobservation_type)

        if self._is_empty(self.rearranged_sequencerepository_name):
            self.MissingRequiredField("rearranged_sequencerepository_name")
        if not isinstance(self.rearranged_sequencerepository_name, str):
            self.rearranged_sequencerepository_name = str(self.rearranged_sequencerepository_name)

        if self._is_empty(self.rearranged_sequencedeposited_version):
            self.MissingRequiredField("rearranged_sequencedeposited_version")
        if not isinstance(self.rearranged_sequencedeposited_version, str):
            self.rearranged_sequencedeposited_version = str(self.rearranged_sequencedeposited_version)

        if self.rearranged_sequencecuration is not None and not isinstance(self.rearranged_sequencecuration, str):
            self.rearranged_sequencecuration = str(self.rearranged_sequencecuration)

        if self.rearranged_sequencerepository_ref is not None and not isinstance(self.rearranged_sequencerepository_ref, str):
            self.rearranged_sequencerepository_ref = str(self.rearranged_sequencerepository_ref)

        if self.rearranged_sequencesequence_start is not None and not isinstance(self.rearranged_sequencesequence_start, int):
            self.rearranged_sequencesequence_start = int(self.rearranged_sequencesequence_start)

        if self.rearranged_sequencesequence_end is not None and not isinstance(self.rearranged_sequencesequence_end, int):
            self.rearranged_sequencesequence_end = int(self.rearranged_sequencesequence_end)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4UnrearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4UnrearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4UnrearrangedSequence"
    class_name: ClassVar[str] = "V1p4_UnrearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4UnrearrangedSequence

    unrearranged_sequencesequence_id: str = None
    unrearranged_sequencesequence: str = None
    unrearranged_sequencerepository_name: str = None
    unrearranged_sequencegff_seqid: str = None
    unrearranged_sequencegff_start: int = None
    unrearranged_sequencegff_end: int = None
    unrearranged_sequencestrand: Union[str, "V1p4Strand"] = None
    unrearranged_sequencecuration: Optional[str] = None
    unrearranged_sequencerepository_ref: Optional[str] = None
    unrearranged_sequencepatch_no: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.unrearranged_sequencesequence_id):
            self.MissingRequiredField("unrearranged_sequencesequence_id")
        if not isinstance(self.unrearranged_sequencesequence_id, str):
            self.unrearranged_sequencesequence_id = str(self.unrearranged_sequencesequence_id)

        if self._is_empty(self.unrearranged_sequencesequence):
            self.MissingRequiredField("unrearranged_sequencesequence")
        if not isinstance(self.unrearranged_sequencesequence, str):
            self.unrearranged_sequencesequence = str(self.unrearranged_sequencesequence)

        if self._is_empty(self.unrearranged_sequencerepository_name):
            self.MissingRequiredField("unrearranged_sequencerepository_name")
        if not isinstance(self.unrearranged_sequencerepository_name, str):
            self.unrearranged_sequencerepository_name = str(self.unrearranged_sequencerepository_name)

        if self._is_empty(self.unrearranged_sequencegff_seqid):
            self.MissingRequiredField("unrearranged_sequencegff_seqid")
        if not isinstance(self.unrearranged_sequencegff_seqid, str):
            self.unrearranged_sequencegff_seqid = str(self.unrearranged_sequencegff_seqid)

        if self._is_empty(self.unrearranged_sequencegff_start):
            self.MissingRequiredField("unrearranged_sequencegff_start")
        if not isinstance(self.unrearranged_sequencegff_start, int):
            self.unrearranged_sequencegff_start = int(self.unrearranged_sequencegff_start)

        if self._is_empty(self.unrearranged_sequencegff_end):
            self.MissingRequiredField("unrearranged_sequencegff_end")
        if not isinstance(self.unrearranged_sequencegff_end, int):
            self.unrearranged_sequencegff_end = int(self.unrearranged_sequencegff_end)

        if self._is_empty(self.unrearranged_sequencestrand):
            self.MissingRequiredField("unrearranged_sequencestrand")
        if not isinstance(self.unrearranged_sequencestrand, V1p4Strand):
            self.unrearranged_sequencestrand = V1p4Strand(self.unrearranged_sequencestrand)

        if self.unrearranged_sequencecuration is not None and not isinstance(self.unrearranged_sequencecuration, str):
            self.unrearranged_sequencecuration = str(self.unrearranged_sequencecuration)

        if self.unrearranged_sequencerepository_ref is not None and not isinstance(self.unrearranged_sequencerepository_ref, str):
            self.unrearranged_sequencerepository_ref = str(self.unrearranged_sequencerepository_ref)

        if self.unrearranged_sequencepatch_no is not None and not isinstance(self.unrearranged_sequencepatch_no, str):
            self.unrearranged_sequencepatch_no = str(self.unrearranged_sequencepatch_no)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SequenceDelineationV(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SequenceDelineationV"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SequenceDelineationV"
    class_name: ClassVar[str] = "V1p4_SequenceDelineationV"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SequenceDelineationV

    sequence_delineation_vsequence_delineation_id: str = None
    sequence_delineation_vdelineation_scheme: str = None
    sequence_delineation_vfwr1_start: int = None
    sequence_delineation_vfwr1_end: int = None
    sequence_delineation_vcdr1_start: int = None
    sequence_delineation_vcdr1_end: int = None
    sequence_delineation_vfwr2_start: int = None
    sequence_delineation_vfwr2_end: int = None
    sequence_delineation_vcdr2_start: int = None
    sequence_delineation_vcdr2_end: int = None
    sequence_delineation_vfwr3_start: int = None
    sequence_delineation_vfwr3_end: int = None
    sequence_delineation_vcdr3_start: int = None
    sequence_delineation_vunaligned_sequence: Optional[str] = None
    sequence_delineation_valigned_sequence: Optional[str] = None
    sequence_delineation_valignment_labels: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sequence_delineation_vsequence_delineation_id):
            self.MissingRequiredField("sequence_delineation_vsequence_delineation_id")
        if not isinstance(self.sequence_delineation_vsequence_delineation_id, str):
            self.sequence_delineation_vsequence_delineation_id = str(self.sequence_delineation_vsequence_delineation_id)

        if self._is_empty(self.sequence_delineation_vdelineation_scheme):
            self.MissingRequiredField("sequence_delineation_vdelineation_scheme")
        if not isinstance(self.sequence_delineation_vdelineation_scheme, str):
            self.sequence_delineation_vdelineation_scheme = str(self.sequence_delineation_vdelineation_scheme)

        if self._is_empty(self.sequence_delineation_vfwr1_start):
            self.MissingRequiredField("sequence_delineation_vfwr1_start")
        if not isinstance(self.sequence_delineation_vfwr1_start, int):
            self.sequence_delineation_vfwr1_start = int(self.sequence_delineation_vfwr1_start)

        if self._is_empty(self.sequence_delineation_vfwr1_end):
            self.MissingRequiredField("sequence_delineation_vfwr1_end")
        if not isinstance(self.sequence_delineation_vfwr1_end, int):
            self.sequence_delineation_vfwr1_end = int(self.sequence_delineation_vfwr1_end)

        if self._is_empty(self.sequence_delineation_vcdr1_start):
            self.MissingRequiredField("sequence_delineation_vcdr1_start")
        if not isinstance(self.sequence_delineation_vcdr1_start, int):
            self.sequence_delineation_vcdr1_start = int(self.sequence_delineation_vcdr1_start)

        if self._is_empty(self.sequence_delineation_vcdr1_end):
            self.MissingRequiredField("sequence_delineation_vcdr1_end")
        if not isinstance(self.sequence_delineation_vcdr1_end, int):
            self.sequence_delineation_vcdr1_end = int(self.sequence_delineation_vcdr1_end)

        if self._is_empty(self.sequence_delineation_vfwr2_start):
            self.MissingRequiredField("sequence_delineation_vfwr2_start")
        if not isinstance(self.sequence_delineation_vfwr2_start, int):
            self.sequence_delineation_vfwr2_start = int(self.sequence_delineation_vfwr2_start)

        if self._is_empty(self.sequence_delineation_vfwr2_end):
            self.MissingRequiredField("sequence_delineation_vfwr2_end")
        if not isinstance(self.sequence_delineation_vfwr2_end, int):
            self.sequence_delineation_vfwr2_end = int(self.sequence_delineation_vfwr2_end)

        if self._is_empty(self.sequence_delineation_vcdr2_start):
            self.MissingRequiredField("sequence_delineation_vcdr2_start")
        if not isinstance(self.sequence_delineation_vcdr2_start, int):
            self.sequence_delineation_vcdr2_start = int(self.sequence_delineation_vcdr2_start)

        if self._is_empty(self.sequence_delineation_vcdr2_end):
            self.MissingRequiredField("sequence_delineation_vcdr2_end")
        if not isinstance(self.sequence_delineation_vcdr2_end, int):
            self.sequence_delineation_vcdr2_end = int(self.sequence_delineation_vcdr2_end)

        if self._is_empty(self.sequence_delineation_vfwr3_start):
            self.MissingRequiredField("sequence_delineation_vfwr3_start")
        if not isinstance(self.sequence_delineation_vfwr3_start, int):
            self.sequence_delineation_vfwr3_start = int(self.sequence_delineation_vfwr3_start)

        if self._is_empty(self.sequence_delineation_vfwr3_end):
            self.MissingRequiredField("sequence_delineation_vfwr3_end")
        if not isinstance(self.sequence_delineation_vfwr3_end, int):
            self.sequence_delineation_vfwr3_end = int(self.sequence_delineation_vfwr3_end)

        if self._is_empty(self.sequence_delineation_vcdr3_start):
            self.MissingRequiredField("sequence_delineation_vcdr3_start")
        if not isinstance(self.sequence_delineation_vcdr3_start, int):
            self.sequence_delineation_vcdr3_start = int(self.sequence_delineation_vcdr3_start)

        if self.sequence_delineation_vunaligned_sequence is not None and not isinstance(self.sequence_delineation_vunaligned_sequence, str):
            self.sequence_delineation_vunaligned_sequence = str(self.sequence_delineation_vunaligned_sequence)

        if self.sequence_delineation_valigned_sequence is not None and not isinstance(self.sequence_delineation_valigned_sequence, str):
            self.sequence_delineation_valigned_sequence = str(self.sequence_delineation_valigned_sequence)

        if not isinstance(self.sequence_delineation_valignment_labels, list):
            self.sequence_delineation_valignment_labels = [self.sequence_delineation_valignment_labels] if self.sequence_delineation_valignment_labels is not None else []
        self.sequence_delineation_valignment_labels = [v if isinstance(v, str) else str(v) for v in self.sequence_delineation_valignment_labels]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4AlleleDescription(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4AlleleDescription"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4AlleleDescription"
    class_name: ClassVar[str] = "V1p4_AlleleDescription"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4AlleleDescription

    allele_descriptionallele_description_id: str = None
    allele_descriptionacknowledgements: Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]] = None
    allele_descriptionrelease_version: int = None
    allele_descriptionrelease_date: str = None
    allele_descriptionrelease_description: str = None
    allele_descriptionsequence: str = None
    allele_descriptioncoding_sequence: str = None
    allele_descriptionlocus: Union[str, "V1p4Locus"] = None
    allele_descriptionsequence_type: Union[str, "V1p4SequenceType"] = None
    allele_descriptionfunctional: Union[bool, Bool] = None
    allele_descriptioninference_type: Union[str, "V1p4InferenceType"] = None
    allele_descriptionspecies: Union[str, "V1p4Species"] = None
    allele_descriptionallele_description_ref: Optional[str] = None
    allele_descriptionlabel: Optional[str] = None
    allele_descriptionaliases: Optional[Union[str, List[str]]] = empty_list()
    allele_descriptionchromosome: Optional[int] = None
    allele_descriptionspecies_subgroup: Optional[str] = None
    allele_descriptionspecies_subgroup_type: Optional[Union[str, "V1p4SpeciesSubgroupType"]] = None
    allele_descriptionstatus: Optional[Union[str, "V1p4Status"]] = None
    allele_descriptionsubgroup_designation: Optional[str] = None
    allele_descriptiongene_designation: Optional[str] = None
    allele_descriptionallele_designation: Optional[str] = None
    allele_descriptionallele_similarity_cluster_designation: Optional[str] = None
    allele_descriptionallele_similarity_cluster_member_id: Optional[str] = None
    allele_descriptionj_codon_frame: Optional[Union[str, "V1p4JCodonFrame"]] = None
    allele_descriptiongene_start: Optional[int] = None
    allele_descriptiongene_end: Optional[int] = None
    allele_descriptionutr_5_prime_start: Optional[int] = None
    allele_descriptionutr_5_prime_end: Optional[int] = None
    allele_descriptionleader_1_start: Optional[int] = None
    allele_descriptionleader_1_end: Optional[int] = None
    allele_descriptionleader_2_start: Optional[int] = None
    allele_descriptionleader_2_end: Optional[int] = None
    allele_descriptionv_rs_start: Optional[int] = None
    allele_descriptionv_rs_end: Optional[int] = None
    allele_descriptiond_rs_3_prime_start: Optional[int] = None
    allele_descriptiond_rs_3_prime_end: Optional[int] = None
    allele_descriptiond_rs_5_prime_start: Optional[int] = None
    allele_descriptiond_rs_5_prime_end: Optional[int] = None
    allele_descriptionj_cdr3_end: Optional[int] = None
    allele_descriptionj_rs_start: Optional[int] = None
    allele_descriptionj_rs_end: Optional[int] = None
    allele_descriptionj_donor_splice: Optional[int] = None
    allele_descriptionv_gene_delineations: Optional[Union[Union[dict, V1p4SequenceDelineationV], List[Union[dict, V1p4SequenceDelineationV]]]] = empty_list()
    allele_descriptionunrearranged_support: Optional[Union[Union[dict, V1p4UnrearrangedSequence], List[Union[dict, V1p4UnrearrangedSequence]]]] = empty_list()
    allele_descriptionrearranged_support: Optional[Union[Union[dict, V1p4RearrangedSequence], List[Union[dict, V1p4RearrangedSequence]]]] = empty_list()
    allele_descriptionparalogs: Optional[Union[str, List[str]]] = empty_list()
    allele_descriptioncuration: Optional[str] = None
    allele_descriptioncurational_tags: Optional[Union[Union[str, "V1p4CurationalTags"], List[Union[str, "V1p4CurationalTags"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.allele_descriptionallele_description_id):
            self.MissingRequiredField("allele_descriptionallele_description_id")
        if not isinstance(self.allele_descriptionallele_description_id, str):
            self.allele_descriptionallele_description_id = str(self.allele_descriptionallele_description_id)

        if self._is_empty(self.allele_descriptionacknowledgements):
            self.MissingRequiredField("allele_descriptionacknowledgements")
        self._normalize_inlined_as_dict(slot_name="allele_descriptionacknowledgements", slot_type=V1p4Contributor, key_name="contributorcontributor_id", keyed=False)

        if self._is_empty(self.allele_descriptionrelease_version):
            self.MissingRequiredField("allele_descriptionrelease_version")
        if not isinstance(self.allele_descriptionrelease_version, int):
            self.allele_descriptionrelease_version = int(self.allele_descriptionrelease_version)

        if self._is_empty(self.allele_descriptionrelease_date):
            self.MissingRequiredField("allele_descriptionrelease_date")
        if not isinstance(self.allele_descriptionrelease_date, str):
            self.allele_descriptionrelease_date = str(self.allele_descriptionrelease_date)

        if self._is_empty(self.allele_descriptionrelease_description):
            self.MissingRequiredField("allele_descriptionrelease_description")
        if not isinstance(self.allele_descriptionrelease_description, str):
            self.allele_descriptionrelease_description = str(self.allele_descriptionrelease_description)

        if self._is_empty(self.allele_descriptionsequence):
            self.MissingRequiredField("allele_descriptionsequence")
        if not isinstance(self.allele_descriptionsequence, str):
            self.allele_descriptionsequence = str(self.allele_descriptionsequence)

        if self._is_empty(self.allele_descriptioncoding_sequence):
            self.MissingRequiredField("allele_descriptioncoding_sequence")
        if not isinstance(self.allele_descriptioncoding_sequence, str):
            self.allele_descriptioncoding_sequence = str(self.allele_descriptioncoding_sequence)

        if self._is_empty(self.allele_descriptionlocus):
            self.MissingRequiredField("allele_descriptionlocus")
        if not isinstance(self.allele_descriptionlocus, V1p4Locus):
            self.allele_descriptionlocus = V1p4Locus(self.allele_descriptionlocus)

        if self._is_empty(self.allele_descriptionsequence_type):
            self.MissingRequiredField("allele_descriptionsequence_type")
        if not isinstance(self.allele_descriptionsequence_type, V1p4SequenceType):
            self.allele_descriptionsequence_type = V1p4SequenceType(self.allele_descriptionsequence_type)

        if self._is_empty(self.allele_descriptionfunctional):
            self.MissingRequiredField("allele_descriptionfunctional")
        if not isinstance(self.allele_descriptionfunctional, Bool):
            self.allele_descriptionfunctional = Bool(self.allele_descriptionfunctional)

        if self._is_empty(self.allele_descriptioninference_type):
            self.MissingRequiredField("allele_descriptioninference_type")
        if not isinstance(self.allele_descriptioninference_type, V1p4InferenceType):
            self.allele_descriptioninference_type = V1p4InferenceType(self.allele_descriptioninference_type)

        if self.allele_descriptionallele_description_ref is not None and not isinstance(self.allele_descriptionallele_description_ref, str):
            self.allele_descriptionallele_description_ref = str(self.allele_descriptionallele_description_ref)

        if self.allele_descriptionlabel is not None and not isinstance(self.allele_descriptionlabel, str):
            self.allele_descriptionlabel = str(self.allele_descriptionlabel)

        if not isinstance(self.allele_descriptionaliases, list):
            self.allele_descriptionaliases = [self.allele_descriptionaliases] if self.allele_descriptionaliases is not None else []
        self.allele_descriptionaliases = [v if isinstance(v, str) else str(v) for v in self.allele_descriptionaliases]

        if self.allele_descriptionchromosome is not None and not isinstance(self.allele_descriptionchromosome, int):
            self.allele_descriptionchromosome = int(self.allele_descriptionchromosome)

        if self.allele_descriptionspecies_subgroup is not None and not isinstance(self.allele_descriptionspecies_subgroup, str):
            self.allele_descriptionspecies_subgroup = str(self.allele_descriptionspecies_subgroup)

        if self.allele_descriptionspecies_subgroup_type is not None and not isinstance(self.allele_descriptionspecies_subgroup_type, V1p4SpeciesSubgroupType):
            self.allele_descriptionspecies_subgroup_type = V1p4SpeciesSubgroupType(self.allele_descriptionspecies_subgroup_type)

        if self.allele_descriptionstatus is not None and not isinstance(self.allele_descriptionstatus, V1p4Status):
            self.allele_descriptionstatus = V1p4Status(self.allele_descriptionstatus)

        if self.allele_descriptionsubgroup_designation is not None and not isinstance(self.allele_descriptionsubgroup_designation, str):
            self.allele_descriptionsubgroup_designation = str(self.allele_descriptionsubgroup_designation)

        if self.allele_descriptiongene_designation is not None and not isinstance(self.allele_descriptiongene_designation, str):
            self.allele_descriptiongene_designation = str(self.allele_descriptiongene_designation)

        if self.allele_descriptionallele_designation is not None and not isinstance(self.allele_descriptionallele_designation, str):
            self.allele_descriptionallele_designation = str(self.allele_descriptionallele_designation)

        if self.allele_descriptionallele_similarity_cluster_designation is not None and not isinstance(self.allele_descriptionallele_similarity_cluster_designation, str):
            self.allele_descriptionallele_similarity_cluster_designation = str(self.allele_descriptionallele_similarity_cluster_designation)

        if self.allele_descriptionallele_similarity_cluster_member_id is not None and not isinstance(self.allele_descriptionallele_similarity_cluster_member_id, str):
            self.allele_descriptionallele_similarity_cluster_member_id = str(self.allele_descriptionallele_similarity_cluster_member_id)

        if self.allele_descriptionj_codon_frame is not None and not isinstance(self.allele_descriptionj_codon_frame, V1p4JCodonFrame):
            self.allele_descriptionj_codon_frame = V1p4JCodonFrame(self.allele_descriptionj_codon_frame)

        if self.allele_descriptiongene_start is not None and not isinstance(self.allele_descriptiongene_start, int):
            self.allele_descriptiongene_start = int(self.allele_descriptiongene_start)

        if self.allele_descriptiongene_end is not None and not isinstance(self.allele_descriptiongene_end, int):
            self.allele_descriptiongene_end = int(self.allele_descriptiongene_end)

        if self.allele_descriptionutr_5_prime_start is not None and not isinstance(self.allele_descriptionutr_5_prime_start, int):
            self.allele_descriptionutr_5_prime_start = int(self.allele_descriptionutr_5_prime_start)

        if self.allele_descriptionutr_5_prime_end is not None and not isinstance(self.allele_descriptionutr_5_prime_end, int):
            self.allele_descriptionutr_5_prime_end = int(self.allele_descriptionutr_5_prime_end)

        if self.allele_descriptionleader_1_start is not None and not isinstance(self.allele_descriptionleader_1_start, int):
            self.allele_descriptionleader_1_start = int(self.allele_descriptionleader_1_start)

        if self.allele_descriptionleader_1_end is not None and not isinstance(self.allele_descriptionleader_1_end, int):
            self.allele_descriptionleader_1_end = int(self.allele_descriptionleader_1_end)

        if self.allele_descriptionleader_2_start is not None and not isinstance(self.allele_descriptionleader_2_start, int):
            self.allele_descriptionleader_2_start = int(self.allele_descriptionleader_2_start)

        if self.allele_descriptionleader_2_end is not None and not isinstance(self.allele_descriptionleader_2_end, int):
            self.allele_descriptionleader_2_end = int(self.allele_descriptionleader_2_end)

        if self.allele_descriptionv_rs_start is not None and not isinstance(self.allele_descriptionv_rs_start, int):
            self.allele_descriptionv_rs_start = int(self.allele_descriptionv_rs_start)

        if self.allele_descriptionv_rs_end is not None and not isinstance(self.allele_descriptionv_rs_end, int):
            self.allele_descriptionv_rs_end = int(self.allele_descriptionv_rs_end)

        if self.allele_descriptiond_rs_3_prime_start is not None and not isinstance(self.allele_descriptiond_rs_3_prime_start, int):
            self.allele_descriptiond_rs_3_prime_start = int(self.allele_descriptiond_rs_3_prime_start)

        if self.allele_descriptiond_rs_3_prime_end is not None and not isinstance(self.allele_descriptiond_rs_3_prime_end, int):
            self.allele_descriptiond_rs_3_prime_end = int(self.allele_descriptiond_rs_3_prime_end)

        if self.allele_descriptiond_rs_5_prime_start is not None and not isinstance(self.allele_descriptiond_rs_5_prime_start, int):
            self.allele_descriptiond_rs_5_prime_start = int(self.allele_descriptiond_rs_5_prime_start)

        if self.allele_descriptiond_rs_5_prime_end is not None and not isinstance(self.allele_descriptiond_rs_5_prime_end, int):
            self.allele_descriptiond_rs_5_prime_end = int(self.allele_descriptiond_rs_5_prime_end)

        if self.allele_descriptionj_cdr3_end is not None and not isinstance(self.allele_descriptionj_cdr3_end, int):
            self.allele_descriptionj_cdr3_end = int(self.allele_descriptionj_cdr3_end)

        if self.allele_descriptionj_rs_start is not None and not isinstance(self.allele_descriptionj_rs_start, int):
            self.allele_descriptionj_rs_start = int(self.allele_descriptionj_rs_start)

        if self.allele_descriptionj_rs_end is not None and not isinstance(self.allele_descriptionj_rs_end, int):
            self.allele_descriptionj_rs_end = int(self.allele_descriptionj_rs_end)

        if self.allele_descriptionj_donor_splice is not None and not isinstance(self.allele_descriptionj_donor_splice, int):
            self.allele_descriptionj_donor_splice = int(self.allele_descriptionj_donor_splice)

        self._normalize_inlined_as_dict(slot_name="allele_descriptionv_gene_delineations", slot_type=V1p4SequenceDelineationV, key_name="sequence_delineation_vsequence_delineation_id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_descriptionunrearranged_support", slot_type=V1p4UnrearrangedSequence, key_name="unrearranged_sequencesequence_id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_descriptionrearranged_support", slot_type=V1p4RearrangedSequence, key_name="rearranged_sequencesequence_id", keyed=False)

        if not isinstance(self.allele_descriptionparalogs, list):
            self.allele_descriptionparalogs = [self.allele_descriptionparalogs] if self.allele_descriptionparalogs is not None else []
        self.allele_descriptionparalogs = [v if isinstance(v, str) else str(v) for v in self.allele_descriptionparalogs]

        if self.allele_descriptioncuration is not None and not isinstance(self.allele_descriptioncuration, str):
            self.allele_descriptioncuration = str(self.allele_descriptioncuration)

        if not isinstance(self.allele_descriptioncurational_tags, list):
            self.allele_descriptioncurational_tags = [self.allele_descriptioncurational_tags] if self.allele_descriptioncurational_tags is not None else []
        self.allele_descriptioncurational_tags = [v if isinstance(v, V1p4CurationalTags) else V1p4CurationalTags(v) for v in self.allele_descriptioncurational_tags]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4GermlineSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4GermlineSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4GermlineSet"
    class_name: ClassVar[str] = "V1p4_GermlineSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4GermlineSet

    germline_setgermline_set_id: str = None
    germline_setacknowledgements: Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]] = None
    germline_setrelease_version: float = None
    germline_setrelease_description: str = None
    germline_setrelease_date: str = None
    germline_setgermline_set_name: str = None
    germline_setgermline_set_ref: str = None
    germline_setspecies: Union[str, "V1p4Species"] = None
    germline_setlocus: Union[str, "V1p4Locus"] = None
    germline_setallele_descriptions: Union[Union[dict, V1p4AlleleDescription], List[Union[dict, V1p4AlleleDescription]]] = None
    germline_setpub_ids: Optional[Union[str, List[str]]] = empty_list()
    germline_setspecies_subgroup: Optional[str] = None
    germline_setspecies_subgroup_type: Optional[Union[str, "V1p4SpeciesSubgroupType"]] = None
    germline_setcuration: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.germline_setgermline_set_id):
            self.MissingRequiredField("germline_setgermline_set_id")
        if not isinstance(self.germline_setgermline_set_id, str):
            self.germline_setgermline_set_id = str(self.germline_setgermline_set_id)

        if self._is_empty(self.germline_setacknowledgements):
            self.MissingRequiredField("germline_setacknowledgements")
        self._normalize_inlined_as_dict(slot_name="germline_setacknowledgements", slot_type=V1p4Contributor, key_name="contributorcontributor_id", keyed=False)

        if self._is_empty(self.germline_setrelease_version):
            self.MissingRequiredField("germline_setrelease_version")
        if not isinstance(self.germline_setrelease_version, float):
            self.germline_setrelease_version = float(self.germline_setrelease_version)

        if self._is_empty(self.germline_setrelease_description):
            self.MissingRequiredField("germline_setrelease_description")
        if not isinstance(self.germline_setrelease_description, str):
            self.germline_setrelease_description = str(self.germline_setrelease_description)

        if self._is_empty(self.germline_setrelease_date):
            self.MissingRequiredField("germline_setrelease_date")
        if not isinstance(self.germline_setrelease_date, str):
            self.germline_setrelease_date = str(self.germline_setrelease_date)

        if self._is_empty(self.germline_setgermline_set_name):
            self.MissingRequiredField("germline_setgermline_set_name")
        if not isinstance(self.germline_setgermline_set_name, str):
            self.germline_setgermline_set_name = str(self.germline_setgermline_set_name)

        if self._is_empty(self.germline_setgermline_set_ref):
            self.MissingRequiredField("germline_setgermline_set_ref")
        if not isinstance(self.germline_setgermline_set_ref, str):
            self.germline_setgermline_set_ref = str(self.germline_setgermline_set_ref)

        if self._is_empty(self.germline_setlocus):
            self.MissingRequiredField("germline_setlocus")
        if not isinstance(self.germline_setlocus, V1p4Locus):
            self.germline_setlocus = V1p4Locus(self.germline_setlocus)

        if self._is_empty(self.germline_setallele_descriptions):
            self.MissingRequiredField("germline_setallele_descriptions")
        self._normalize_inlined_as_dict(slot_name="germline_setallele_descriptions", slot_type=V1p4AlleleDescription, key_name="allele_descriptionallele_description_id", keyed=False)

        if not isinstance(self.germline_setpub_ids, list):
            self.germline_setpub_ids = [self.germline_setpub_ids] if self.germline_setpub_ids is not None else []
        self.germline_setpub_ids = [v if isinstance(v, str) else str(v) for v in self.germline_setpub_ids]

        if self.germline_setspecies_subgroup is not None and not isinstance(self.germline_setspecies_subgroup, str):
            self.germline_setspecies_subgroup = str(self.germline_setspecies_subgroup)

        if self.germline_setspecies_subgroup_type is not None and not isinstance(self.germline_setspecies_subgroup_type, V1p4SpeciesSubgroupType):
            self.germline_setspecies_subgroup_type = V1p4SpeciesSubgroupType(self.germline_setspecies_subgroup_type)

        if self.germline_setcuration is not None and not isinstance(self.germline_setcuration, str):
            self.germline_setcuration = str(self.germline_setcuration)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4GenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4GenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4GenotypeSet"
    class_name: ClassVar[str] = "V1p4_GenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4GenotypeSet

    genotype_setreceptor_genotype_set_id: str = None
    genotype_setgenotype_class_list: Optional[Union[Union[dict, "V1p4Genotype"], List[Union[dict, "V1p4Genotype"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.genotype_setreceptor_genotype_set_id):
            self.MissingRequiredField("genotype_setreceptor_genotype_set_id")
        if not isinstance(self.genotype_setreceptor_genotype_set_id, str):
            self.genotype_setreceptor_genotype_set_id = str(self.genotype_setreceptor_genotype_set_id)

        self._normalize_inlined_as_dict(slot_name="genotype_setgenotype_class_list", slot_type=V1p4Genotype, key_name="genotypereceptor_genotype_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Genotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Genotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Genotype"
    class_name: ClassVar[str] = "V1p4_Genotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Genotype

    genotypereceptor_genotype_id: str = None
    genotypelocus: Union[str, "V1p4Locus"] = None
    genotypedocumented_alleles: Optional[Union[Union[dict, "V1p4DocumentedAllele"], List[Union[dict, "V1p4DocumentedAllele"]]]] = empty_list()
    genotypeundocumented_alleles: Optional[Union[Union[dict, "V1p4UndocumentedAllele"], List[Union[dict, "V1p4UndocumentedAllele"]]]] = empty_list()
    genotypedeleted_genes: Optional[Union[Union[dict, "V1p4DeletedGene"], List[Union[dict, "V1p4DeletedGene"]]]] = empty_list()
    genotypeinference_process: Optional[Union[str, "V1p4InferenceProcess"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.genotypereceptor_genotype_id):
            self.MissingRequiredField("genotypereceptor_genotype_id")
        if not isinstance(self.genotypereceptor_genotype_id, str):
            self.genotypereceptor_genotype_id = str(self.genotypereceptor_genotype_id)

        if self._is_empty(self.genotypelocus):
            self.MissingRequiredField("genotypelocus")
        if not isinstance(self.genotypelocus, V1p4Locus):
            self.genotypelocus = V1p4Locus(self.genotypelocus)

        self._normalize_inlined_as_dict(slot_name="genotypedocumented_alleles", slot_type=V1p4DocumentedAllele, key_name="documented_allelelabel", keyed=False)

        self._normalize_inlined_as_dict(slot_name="genotypeundocumented_alleles", slot_type=V1p4UndocumentedAllele, key_name="undocumented_alleleallele_name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="genotypedeleted_genes", slot_type=V1p4DeletedGene, key_name="deleted_genelabel", keyed=False)

        if self.genotypeinference_process is not None and not isinstance(self.genotypeinference_process, V1p4InferenceProcess):
            self.genotypeinference_process = V1p4InferenceProcess(self.genotypeinference_process)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4DocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4DocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4DocumentedAllele"
    class_name: ClassVar[str] = "V1p4_DocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4DocumentedAllele

    documented_allelelabel: str = None
    documented_allelegermline_set_ref: str = None
    documented_allelephasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.documented_allelelabel):
            self.MissingRequiredField("documented_allelelabel")
        if not isinstance(self.documented_allelelabel, str):
            self.documented_allelelabel = str(self.documented_allelelabel)

        if self._is_empty(self.documented_allelegermline_set_ref):
            self.MissingRequiredField("documented_allelegermline_set_ref")
        if not isinstance(self.documented_allelegermline_set_ref, str):
            self.documented_allelegermline_set_ref = str(self.documented_allelegermline_set_ref)

        if self.documented_allelephasing is not None and not isinstance(self.documented_allelephasing, int):
            self.documented_allelephasing = int(self.documented_allelephasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4UndocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4UndocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4UndocumentedAllele"
    class_name: ClassVar[str] = "V1p4_UndocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4UndocumentedAllele

    undocumented_alleleallele_name: str = None
    undocumented_allelesequence: str = None
    undocumented_allelephasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.undocumented_alleleallele_name):
            self.MissingRequiredField("undocumented_alleleallele_name")
        if not isinstance(self.undocumented_alleleallele_name, str):
            self.undocumented_alleleallele_name = str(self.undocumented_alleleallele_name)

        if self._is_empty(self.undocumented_allelesequence):
            self.MissingRequiredField("undocumented_allelesequence")
        if not isinstance(self.undocumented_allelesequence, str):
            self.undocumented_allelesequence = str(self.undocumented_allelesequence)

        if self.undocumented_allelephasing is not None and not isinstance(self.undocumented_allelephasing, int):
            self.undocumented_allelephasing = int(self.undocumented_allelephasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4DeletedGene(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4DeletedGene"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4DeletedGene"
    class_name: ClassVar[str] = "V1p4_DeletedGene"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4DeletedGene

    deleted_genelabel: str = None
    deleted_genegermline_set_ref: str = None
    deleted_genephasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.deleted_genelabel):
            self.MissingRequiredField("deleted_genelabel")
        if not isinstance(self.deleted_genelabel, str):
            self.deleted_genelabel = str(self.deleted_genelabel)

        if self._is_empty(self.deleted_genegermline_set_ref):
            self.MissingRequiredField("deleted_genegermline_set_ref")
        if not isinstance(self.deleted_genegermline_set_ref, str):
            self.deleted_genegermline_set_ref = str(self.deleted_genegermline_set_ref)

        if self.deleted_genephasing is not None and not isinstance(self.deleted_genephasing, int):
            self.deleted_genephasing = int(self.deleted_genephasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4MHCGenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4MHCGenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4MHCGenotypeSet"
    class_name: ClassVar[str] = "V1p4_MHCGenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4MHCGenotypeSet

    m_h_c_genotype_setmhc_genotype_set_id: str = None
    m_h_c_genotype_setmhc_genotype_list: Union[Union[dict, "V1p4MHCGenotype"], List[Union[dict, "V1p4MHCGenotype"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.m_h_c_genotype_setmhc_genotype_set_id):
            self.MissingRequiredField("m_h_c_genotype_setmhc_genotype_set_id")
        if not isinstance(self.m_h_c_genotype_setmhc_genotype_set_id, str):
            self.m_h_c_genotype_setmhc_genotype_set_id = str(self.m_h_c_genotype_setmhc_genotype_set_id)

        if self._is_empty(self.m_h_c_genotype_setmhc_genotype_list):
            self.MissingRequiredField("m_h_c_genotype_setmhc_genotype_list")
        self._normalize_inlined_as_dict(slot_name="m_h_c_genotype_setmhc_genotype_list", slot_type=V1p4MHCGenotype, key_name="m_h_c_genotypemhc_genotype_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4MHCGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4MHCGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4MHCGenotype"
    class_name: ClassVar[str] = "V1p4_MHCGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4MHCGenotype

    m_h_c_genotypemhc_genotype_id: str = None
    m_h_c_genotypemhc_class: Union[str, "V1p4MhcClass"] = None
    m_h_c_genotypemhc_alleles: Union[Union[dict, "V1p4MHCAllele"], List[Union[dict, "V1p4MHCAllele"]]] = None
    m_h_c_genotypemhc_genotyping_method: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.m_h_c_genotypemhc_genotype_id):
            self.MissingRequiredField("m_h_c_genotypemhc_genotype_id")
        if not isinstance(self.m_h_c_genotypemhc_genotype_id, str):
            self.m_h_c_genotypemhc_genotype_id = str(self.m_h_c_genotypemhc_genotype_id)

        if self._is_empty(self.m_h_c_genotypemhc_class):
            self.MissingRequiredField("m_h_c_genotypemhc_class")
        if not isinstance(self.m_h_c_genotypemhc_class, V1p4MhcClass):
            self.m_h_c_genotypemhc_class = V1p4MhcClass(self.m_h_c_genotypemhc_class)

        if self._is_empty(self.m_h_c_genotypemhc_alleles):
            self.MissingRequiredField("m_h_c_genotypemhc_alleles")
        if not isinstance(self.m_h_c_genotypemhc_alleles, list):
            self.m_h_c_genotypemhc_alleles = [self.m_h_c_genotypemhc_alleles] if self.m_h_c_genotypemhc_alleles is not None else []
        self.m_h_c_genotypemhc_alleles = [v if isinstance(v, V1p4MHCAllele) else V1p4MHCAllele(**as_dict(v)) for v in self.m_h_c_genotypemhc_alleles]

        if self.m_h_c_genotypemhc_genotyping_method is not None and not isinstance(self.m_h_c_genotypemhc_genotyping_method, str):
            self.m_h_c_genotypemhc_genotyping_method = str(self.m_h_c_genotypemhc_genotyping_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4MHCAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4MHCAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4MHCAllele"
    class_name: ClassVar[str] = "V1p4_MHCAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4MHCAllele

    m_h_c_alleleallele_designation: Optional[str] = None
    m_h_c_allelegene: Optional[Union[str, "V1p4Gene"]] = None
    m_h_c_allelereference_set_ref: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.m_h_c_alleleallele_designation is not None and not isinstance(self.m_h_c_alleleallele_designation, str):
            self.m_h_c_alleleallele_designation = str(self.m_h_c_alleleallele_designation)

        if self.m_h_c_allelereference_set_ref is not None and not isinstance(self.m_h_c_allelereference_set_ref, str):
            self.m_h_c_allelereference_set_ref = str(self.m_h_c_allelereference_set_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SubjectGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SubjectGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SubjectGenotype"
    class_name: ClassVar[str] = "V1p4_SubjectGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SubjectGenotype

    subject_genotypereceptor_genotype_set: Optional[Union[dict, V1p4GenotypeSet]] = None
    subject_genotypemhc_genotype_set: Optional[Union[dict, V1p4MHCGenotypeSet]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject_genotypereceptor_genotype_set is not None and not isinstance(self.subject_genotypereceptor_genotype_set, V1p4GenotypeSet):
            self.subject_genotypereceptor_genotype_set = V1p4GenotypeSet(**as_dict(self.subject_genotypereceptor_genotype_set))

        if self.subject_genotypemhc_genotype_set is not None and not isinstance(self.subject_genotypemhc_genotype_set, V1p4MHCGenotypeSet):
            self.subject_genotypemhc_genotype_set = V1p4MHCGenotypeSet(**as_dict(self.subject_genotypemhc_genotype_set))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Study(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Study"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Study"
    class_name: ClassVar[str] = "V1p4_Study"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Study

    studystudy_id: str = None
    studystudy_title: str = None
    studystudy_type: Union[str, "V1p4StudyType"] = None
    studyinclusion_exclusion_criteria: str = None
    studygrants: str = None
    studycontributors: Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]] = None
    studypub_ids: Union[str, List[str]] = None
    studykeywords_study: Union[Union[str, "V1p4KeywordsStudy"], List[Union[str, "V1p4KeywordsStudy"]]] = None
    studystudy_description: Optional[str] = None
    studyadc_publish_date: Optional[str] = None
    studyadc_update_date: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.studystudy_id):
            self.MissingRequiredField("studystudy_id")
        if not isinstance(self.studystudy_id, str):
            self.studystudy_id = str(self.studystudy_id)

        if self._is_empty(self.studystudy_title):
            self.MissingRequiredField("studystudy_title")
        if not isinstance(self.studystudy_title, str):
            self.studystudy_title = str(self.studystudy_title)

        if self._is_empty(self.studyinclusion_exclusion_criteria):
            self.MissingRequiredField("studyinclusion_exclusion_criteria")
        if not isinstance(self.studyinclusion_exclusion_criteria, str):
            self.studyinclusion_exclusion_criteria = str(self.studyinclusion_exclusion_criteria)

        if self._is_empty(self.studygrants):
            self.MissingRequiredField("studygrants")
        if not isinstance(self.studygrants, str):
            self.studygrants = str(self.studygrants)

        if self._is_empty(self.studycontributors):
            self.MissingRequiredField("studycontributors")
        self._normalize_inlined_as_dict(slot_name="studycontributors", slot_type=V1p4Contributor, key_name="contributorcontributor_id", keyed=False)

        if self._is_empty(self.studypub_ids):
            self.MissingRequiredField("studypub_ids")
        if not isinstance(self.studypub_ids, list):
            self.studypub_ids = [self.studypub_ids] if self.studypub_ids is not None else []
        self.studypub_ids = [v if isinstance(v, str) else str(v) for v in self.studypub_ids]

        if self._is_empty(self.studykeywords_study):
            self.MissingRequiredField("studykeywords_study")
        if not isinstance(self.studykeywords_study, list):
            self.studykeywords_study = [self.studykeywords_study] if self.studykeywords_study is not None else []
        self.studykeywords_study = [v if isinstance(v, V1p4KeywordsStudy) else V1p4KeywordsStudy(v) for v in self.studykeywords_study]

        if self.studystudy_description is not None and not isinstance(self.studystudy_description, str):
            self.studystudy_description = str(self.studystudy_description)

        if self.studyadc_publish_date is not None and not isinstance(self.studyadc_publish_date, str):
            self.studyadc_publish_date = str(self.studyadc_publish_date)

        if self.studyadc_update_date is not None and not isinstance(self.studyadc_update_date, str):
            self.studyadc_update_date = str(self.studyadc_update_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Subject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Subject"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Subject"
    class_name: ClassVar[str] = "V1p4_Subject"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Subject

    subjectsubject_id: str = None
    subjectsynthetic: Union[bool, Bool] = None
    subjectspecies: Union[str, "V1p4Species"] = None
    subjectsex: Union[str, "V1p4Sex"] = None
    subjectage: Union[dict, V1p4TimeInterval] = None
    subjectage_event: str = None
    subjectancestry_population: Union[str, "V1p4AncestryPopulation"] = None
    subjectethnicity: str = None
    subjectrace: str = None
    subjectstrain_name: str = None
    subjectlinked_subjects: str = None
    subjectlink_type: str = None
    subjectlocation_birth: Optional[Union[str, "V1p4LocationBirth"]] = None
    subjectdiagnosis: Optional[Union[Union[dict, "V1p4Diagnosis"], List[Union[dict, "V1p4Diagnosis"]]]] = empty_list()
    subjectgenotype: Optional[Union[dict, V1p4SubjectGenotype]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subjectsubject_id):
            self.MissingRequiredField("subjectsubject_id")
        if not isinstance(self.subjectsubject_id, str):
            self.subjectsubject_id = str(self.subjectsubject_id)

        if self._is_empty(self.subjectsynthetic):
            self.MissingRequiredField("subjectsynthetic")
        if not isinstance(self.subjectsynthetic, Bool):
            self.subjectsynthetic = Bool(self.subjectsynthetic)

        if self._is_empty(self.subjectsex):
            self.MissingRequiredField("subjectsex")
        if not isinstance(self.subjectsex, V1p4Sex):
            self.subjectsex = V1p4Sex(self.subjectsex)

        if self._is_empty(self.subjectage):
            self.MissingRequiredField("subjectage")
        if not isinstance(self.subjectage, V1p4TimeInterval):
            self.subjectage = V1p4TimeInterval(**as_dict(self.subjectage))

        if self._is_empty(self.subjectage_event):
            self.MissingRequiredField("subjectage_event")
        if not isinstance(self.subjectage_event, str):
            self.subjectage_event = str(self.subjectage_event)

        if self._is_empty(self.subjectethnicity):
            self.MissingRequiredField("subjectethnicity")
        if not isinstance(self.subjectethnicity, str):
            self.subjectethnicity = str(self.subjectethnicity)

        if self._is_empty(self.subjectrace):
            self.MissingRequiredField("subjectrace")
        if not isinstance(self.subjectrace, str):
            self.subjectrace = str(self.subjectrace)

        if self._is_empty(self.subjectstrain_name):
            self.MissingRequiredField("subjectstrain_name")
        if not isinstance(self.subjectstrain_name, str):
            self.subjectstrain_name = str(self.subjectstrain_name)

        if self._is_empty(self.subjectlinked_subjects):
            self.MissingRequiredField("subjectlinked_subjects")
        if not isinstance(self.subjectlinked_subjects, str):
            self.subjectlinked_subjects = str(self.subjectlinked_subjects)

        if self._is_empty(self.subjectlink_type):
            self.MissingRequiredField("subjectlink_type")
        if not isinstance(self.subjectlink_type, str):
            self.subjectlink_type = str(self.subjectlink_type)

        self._normalize_inlined_as_dict(slot_name="subjectdiagnosis", slot_type=V1p4Diagnosis, key_name="diagnosisstudy_group_description", keyed=False)

        if self.subjectgenotype is not None and not isinstance(self.subjectgenotype, V1p4SubjectGenotype):
            self.subjectgenotype = V1p4SubjectGenotype(**as_dict(self.subjectgenotype))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Diagnosis(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Diagnosis"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Diagnosis"
    class_name: ClassVar[str] = "V1p4_Diagnosis"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Diagnosis

    diagnosisstudy_group_description: str = None
    diagnosisdisease_diagnosis: Union[str, "V1p4DiseaseDiagnosis"] = None
    diagnosisdisease_length: Union[dict, V1p4TimeQuantity] = None
    diagnosisdisease_stage: str = None
    diagnosisprior_therapies: str = None
    diagnosisimmunogen: str = None
    diagnosisintervention: str = None
    diagnosismedical_history: str = None
    diagnosisdiagnosis_timepoint: Optional[Union[dict, V1p4TimePoint]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.diagnosisstudy_group_description):
            self.MissingRequiredField("diagnosisstudy_group_description")
        if not isinstance(self.diagnosisstudy_group_description, str):
            self.diagnosisstudy_group_description = str(self.diagnosisstudy_group_description)

        if self._is_empty(self.diagnosisdisease_length):
            self.MissingRequiredField("diagnosisdisease_length")
        if not isinstance(self.diagnosisdisease_length, V1p4TimeQuantity):
            self.diagnosisdisease_length = V1p4TimeQuantity(**as_dict(self.diagnosisdisease_length))

        if self._is_empty(self.diagnosisdisease_stage):
            self.MissingRequiredField("diagnosisdisease_stage")
        if not isinstance(self.diagnosisdisease_stage, str):
            self.diagnosisdisease_stage = str(self.diagnosisdisease_stage)

        if self._is_empty(self.diagnosisprior_therapies):
            self.MissingRequiredField("diagnosisprior_therapies")
        if not isinstance(self.diagnosisprior_therapies, str):
            self.diagnosisprior_therapies = str(self.diagnosisprior_therapies)

        if self._is_empty(self.diagnosisimmunogen):
            self.MissingRequiredField("diagnosisimmunogen")
        if not isinstance(self.diagnosisimmunogen, str):
            self.diagnosisimmunogen = str(self.diagnosisimmunogen)

        if self._is_empty(self.diagnosisintervention):
            self.MissingRequiredField("diagnosisintervention")
        if not isinstance(self.diagnosisintervention, str):
            self.diagnosisintervention = str(self.diagnosisintervention)

        if self._is_empty(self.diagnosismedical_history):
            self.MissingRequiredField("diagnosismedical_history")
        if not isinstance(self.diagnosismedical_history, str):
            self.diagnosismedical_history = str(self.diagnosismedical_history)

        if self.diagnosisdiagnosis_timepoint is not None and not isinstance(self.diagnosisdiagnosis_timepoint, V1p4TimePoint):
            self.diagnosisdiagnosis_timepoint = V1p4TimePoint(**as_dict(self.diagnosisdiagnosis_timepoint))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Sample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Sample"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Sample"
    class_name: ClassVar[str] = "V1p4_Sample"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Sample

    samplesample_id: str = None
    samplesample_type: str = None
    sampletissue: Union[str, "V1p4Tissue"] = None
    sampleanatomic_site: str = None
    sampledisease_state_sample: str = None
    samplecollection_time_point_relative: Union[dict, V1p4TimePoint] = None
    samplebiomaterial_provider: str = None
    samplecollection_location: Optional[Union[str, "V1p4CollectionLocation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.samplesample_id):
            self.MissingRequiredField("samplesample_id")
        if not isinstance(self.samplesample_id, str):
            self.samplesample_id = str(self.samplesample_id)

        if self._is_empty(self.samplesample_type):
            self.MissingRequiredField("samplesample_type")
        if not isinstance(self.samplesample_type, str):
            self.samplesample_type = str(self.samplesample_type)

        if self._is_empty(self.sampleanatomic_site):
            self.MissingRequiredField("sampleanatomic_site")
        if not isinstance(self.sampleanatomic_site, str):
            self.sampleanatomic_site = str(self.sampleanatomic_site)

        if self._is_empty(self.sampledisease_state_sample):
            self.MissingRequiredField("sampledisease_state_sample")
        if not isinstance(self.sampledisease_state_sample, str):
            self.sampledisease_state_sample = str(self.sampledisease_state_sample)

        if self._is_empty(self.samplecollection_time_point_relative):
            self.MissingRequiredField("samplecollection_time_point_relative")
        if not isinstance(self.samplecollection_time_point_relative, V1p4TimePoint):
            self.samplecollection_time_point_relative = V1p4TimePoint(**as_dict(self.samplecollection_time_point_relative))

        if self._is_empty(self.samplebiomaterial_provider):
            self.MissingRequiredField("samplebiomaterial_provider")
        if not isinstance(self.samplebiomaterial_provider, str):
            self.samplebiomaterial_provider = str(self.samplebiomaterial_provider)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4CellProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4CellProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4CellProcessing"
    class_name: ClassVar[str] = "V1p4_CellProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4CellProcessing

    cell_processingtissue_processing: str = None
    cell_processingcell_subset: Union[str, "V1p4CellSubset"] = None
    cell_processingcell_phenotype: str = None
    cell_processingsingle_cell: Union[bool, Bool] = None
    cell_processingcell_number: int = None
    cell_processingcells_per_reaction: int = None
    cell_processingcell_storage: Union[bool, Bool] = None
    cell_processingcell_quality: str = None
    cell_processingcell_isolation: str = None
    cell_processingcell_processing_protocol: str = None
    cell_processingcell_label: Optional[str] = None
    cell_processingcell_species: Optional[Union[str, "V1p4CellSpecies"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.cell_processingtissue_processing):
            self.MissingRequiredField("cell_processingtissue_processing")
        if not isinstance(self.cell_processingtissue_processing, str):
            self.cell_processingtissue_processing = str(self.cell_processingtissue_processing)

        if self._is_empty(self.cell_processingcell_phenotype):
            self.MissingRequiredField("cell_processingcell_phenotype")
        if not isinstance(self.cell_processingcell_phenotype, str):
            self.cell_processingcell_phenotype = str(self.cell_processingcell_phenotype)

        if self._is_empty(self.cell_processingsingle_cell):
            self.MissingRequiredField("cell_processingsingle_cell")
        if not isinstance(self.cell_processingsingle_cell, Bool):
            self.cell_processingsingle_cell = Bool(self.cell_processingsingle_cell)

        if self._is_empty(self.cell_processingcell_number):
            self.MissingRequiredField("cell_processingcell_number")
        if not isinstance(self.cell_processingcell_number, int):
            self.cell_processingcell_number = int(self.cell_processingcell_number)

        if self._is_empty(self.cell_processingcells_per_reaction):
            self.MissingRequiredField("cell_processingcells_per_reaction")
        if not isinstance(self.cell_processingcells_per_reaction, int):
            self.cell_processingcells_per_reaction = int(self.cell_processingcells_per_reaction)

        if self._is_empty(self.cell_processingcell_storage):
            self.MissingRequiredField("cell_processingcell_storage")
        if not isinstance(self.cell_processingcell_storage, Bool):
            self.cell_processingcell_storage = Bool(self.cell_processingcell_storage)

        if self._is_empty(self.cell_processingcell_quality):
            self.MissingRequiredField("cell_processingcell_quality")
        if not isinstance(self.cell_processingcell_quality, str):
            self.cell_processingcell_quality = str(self.cell_processingcell_quality)

        if self._is_empty(self.cell_processingcell_isolation):
            self.MissingRequiredField("cell_processingcell_isolation")
        if not isinstance(self.cell_processingcell_isolation, str):
            self.cell_processingcell_isolation = str(self.cell_processingcell_isolation)

        if self._is_empty(self.cell_processingcell_processing_protocol):
            self.MissingRequiredField("cell_processingcell_processing_protocol")
        if not isinstance(self.cell_processingcell_processing_protocol, str):
            self.cell_processingcell_processing_protocol = str(self.cell_processingcell_processing_protocol)

        if self.cell_processingcell_label is not None and not isinstance(self.cell_processingcell_label, str):
            self.cell_processingcell_label = str(self.cell_processingcell_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4PCRTarget(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4PCRTarget"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4PCRTarget"
    class_name: ClassVar[str] = "V1p4_PCRTarget"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4PCRTarget

    p_c_r_targetpcr_target_locus: Union[str, "V1p4PcrTargetLocus"] = None
    p_c_r_targetforward_pcr_primer_target_location: str = None
    p_c_r_targetreverse_pcr_primer_target_location: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.p_c_r_targetpcr_target_locus):
            self.MissingRequiredField("p_c_r_targetpcr_target_locus")
        if not isinstance(self.p_c_r_targetpcr_target_locus, V1p4PcrTargetLocus):
            self.p_c_r_targetpcr_target_locus = V1p4PcrTargetLocus(self.p_c_r_targetpcr_target_locus)

        if self._is_empty(self.p_c_r_targetforward_pcr_primer_target_location):
            self.MissingRequiredField("p_c_r_targetforward_pcr_primer_target_location")
        if not isinstance(self.p_c_r_targetforward_pcr_primer_target_location, str):
            self.p_c_r_targetforward_pcr_primer_target_location = str(self.p_c_r_targetforward_pcr_primer_target_location)

        if self._is_empty(self.p_c_r_targetreverse_pcr_primer_target_location):
            self.MissingRequiredField("p_c_r_targetreverse_pcr_primer_target_location")
        if not isinstance(self.p_c_r_targetreverse_pcr_primer_target_location, str):
            self.p_c_r_targetreverse_pcr_primer_target_location = str(self.p_c_r_targetreverse_pcr_primer_target_location)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4NucleicAcidProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4NucleicAcidProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4NucleicAcidProcessing"
    class_name: ClassVar[str] = "V1p4_NucleicAcidProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4NucleicAcidProcessing

    nucleic_acid_processingtemplate_class: Union[str, "V1p4TemplateClass"] = None
    nucleic_acid_processingtemplate_quality: str = None
    nucleic_acid_processingtemplate_amount: Union[dict, V1p4PhysicalQuantity] = None
    nucleic_acid_processinglibrary_generation_method: Union[str, "V1p4LibraryGenerationMethod"] = None
    nucleic_acid_processinglibrary_generation_protocol: str = None
    nucleic_acid_processinglibrary_generation_kit_version: str = None
    nucleic_acid_processingcomplete_sequences: Union[str, "V1p4CompleteSequences"] = None
    nucleic_acid_processingphysical_linkage: Union[str, "V1p4PhysicalLinkage"] = None
    nucleic_acid_processingpcr_target: Optional[Union[Union[dict, V1p4PCRTarget], List[Union[dict, V1p4PCRTarget]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.nucleic_acid_processingtemplate_class):
            self.MissingRequiredField("nucleic_acid_processingtemplate_class")
        if not isinstance(self.nucleic_acid_processingtemplate_class, V1p4TemplateClass):
            self.nucleic_acid_processingtemplate_class = V1p4TemplateClass(self.nucleic_acid_processingtemplate_class)

        if self._is_empty(self.nucleic_acid_processingtemplate_quality):
            self.MissingRequiredField("nucleic_acid_processingtemplate_quality")
        if not isinstance(self.nucleic_acid_processingtemplate_quality, str):
            self.nucleic_acid_processingtemplate_quality = str(self.nucleic_acid_processingtemplate_quality)

        if self._is_empty(self.nucleic_acid_processingtemplate_amount):
            self.MissingRequiredField("nucleic_acid_processingtemplate_amount")
        if not isinstance(self.nucleic_acid_processingtemplate_amount, V1p4PhysicalQuantity):
            self.nucleic_acid_processingtemplate_amount = V1p4PhysicalQuantity(**as_dict(self.nucleic_acid_processingtemplate_amount))

        if self._is_empty(self.nucleic_acid_processinglibrary_generation_method):
            self.MissingRequiredField("nucleic_acid_processinglibrary_generation_method")
        if not isinstance(self.nucleic_acid_processinglibrary_generation_method, V1p4LibraryGenerationMethod):
            self.nucleic_acid_processinglibrary_generation_method = V1p4LibraryGenerationMethod(self.nucleic_acid_processinglibrary_generation_method)

        if self._is_empty(self.nucleic_acid_processinglibrary_generation_protocol):
            self.MissingRequiredField("nucleic_acid_processinglibrary_generation_protocol")
        if not isinstance(self.nucleic_acid_processinglibrary_generation_protocol, str):
            self.nucleic_acid_processinglibrary_generation_protocol = str(self.nucleic_acid_processinglibrary_generation_protocol)

        if self._is_empty(self.nucleic_acid_processinglibrary_generation_kit_version):
            self.MissingRequiredField("nucleic_acid_processinglibrary_generation_kit_version")
        if not isinstance(self.nucleic_acid_processinglibrary_generation_kit_version, str):
            self.nucleic_acid_processinglibrary_generation_kit_version = str(self.nucleic_acid_processinglibrary_generation_kit_version)

        if self._is_empty(self.nucleic_acid_processingcomplete_sequences):
            self.MissingRequiredField("nucleic_acid_processingcomplete_sequences")
        if not isinstance(self.nucleic_acid_processingcomplete_sequences, V1p4CompleteSequences):
            self.nucleic_acid_processingcomplete_sequences = V1p4CompleteSequences(self.nucleic_acid_processingcomplete_sequences)

        if self._is_empty(self.nucleic_acid_processingphysical_linkage):
            self.MissingRequiredField("nucleic_acid_processingphysical_linkage")
        if not isinstance(self.nucleic_acid_processingphysical_linkage, V1p4PhysicalLinkage):
            self.nucleic_acid_processingphysical_linkage = V1p4PhysicalLinkage(self.nucleic_acid_processingphysical_linkage)

        self._normalize_inlined_as_dict(slot_name="nucleic_acid_processingpcr_target", slot_type=V1p4PCRTarget, key_name="p_c_r_targetpcr_target_locus", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SequencingRun(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SequencingRun"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SequencingRun"
    class_name: ClassVar[str] = "V1p4_SequencingRun"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SequencingRun

    sequencing_runsequencing_run_id: str = None
    sequencing_runtotal_reads_passing_qc_filter: int = None
    sequencing_runsequencing_platform: str = None
    sequencing_runsequencing_facility: str = None
    sequencing_runsequencing_run_date: str = None
    sequencing_runsequencing_kit: str = None
    sequencing_runsequencing_files: Optional[Union[dict, "V1p4SequencingData"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sequencing_runsequencing_run_id):
            self.MissingRequiredField("sequencing_runsequencing_run_id")
        if not isinstance(self.sequencing_runsequencing_run_id, str):
            self.sequencing_runsequencing_run_id = str(self.sequencing_runsequencing_run_id)

        if self._is_empty(self.sequencing_runtotal_reads_passing_qc_filter):
            self.MissingRequiredField("sequencing_runtotal_reads_passing_qc_filter")
        if not isinstance(self.sequencing_runtotal_reads_passing_qc_filter, int):
            self.sequencing_runtotal_reads_passing_qc_filter = int(self.sequencing_runtotal_reads_passing_qc_filter)

        if self._is_empty(self.sequencing_runsequencing_platform):
            self.MissingRequiredField("sequencing_runsequencing_platform")
        if not isinstance(self.sequencing_runsequencing_platform, str):
            self.sequencing_runsequencing_platform = str(self.sequencing_runsequencing_platform)

        if self._is_empty(self.sequencing_runsequencing_facility):
            self.MissingRequiredField("sequencing_runsequencing_facility")
        if not isinstance(self.sequencing_runsequencing_facility, str):
            self.sequencing_runsequencing_facility = str(self.sequencing_runsequencing_facility)

        if self._is_empty(self.sequencing_runsequencing_run_date):
            self.MissingRequiredField("sequencing_runsequencing_run_date")
        if not isinstance(self.sequencing_runsequencing_run_date, str):
            self.sequencing_runsequencing_run_date = str(self.sequencing_runsequencing_run_date)

        if self._is_empty(self.sequencing_runsequencing_kit):
            self.MissingRequiredField("sequencing_runsequencing_kit")
        if not isinstance(self.sequencing_runsequencing_kit, str):
            self.sequencing_runsequencing_kit = str(self.sequencing_runsequencing_kit)

        if self.sequencing_runsequencing_files is not None and not isinstance(self.sequencing_runsequencing_files, V1p4SequencingData):
            self.sequencing_runsequencing_files = V1p4SequencingData(**as_dict(self.sequencing_runsequencing_files))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SequencingData(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SequencingData"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SequencingData"
    class_name: ClassVar[str] = "V1p4_SequencingData"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SequencingData

    sequencing_datasequencing_data_id: str = None
    sequencing_datafile_type: Union[str, "V1p4FileType"] = None
    sequencing_datafilename: str = None
    sequencing_dataread_direction: Union[str, "V1p4ReadDirection"] = None
    sequencing_dataread_length: int = None
    sequencing_datapaired_filename: str = None
    sequencing_datapaired_read_direction: Union[str, "V1p4PairedReadDirection"] = None
    sequencing_datapaired_read_length: int = None
    sequencing_dataindex_filename: Optional[str] = None
    sequencing_dataindex_length: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sequencing_datasequencing_data_id):
            self.MissingRequiredField("sequencing_datasequencing_data_id")
        if not isinstance(self.sequencing_datasequencing_data_id, str):
            self.sequencing_datasequencing_data_id = str(self.sequencing_datasequencing_data_id)

        if self._is_empty(self.sequencing_datafile_type):
            self.MissingRequiredField("sequencing_datafile_type")
        if not isinstance(self.sequencing_datafile_type, V1p4FileType):
            self.sequencing_datafile_type = V1p4FileType(self.sequencing_datafile_type)

        if self._is_empty(self.sequencing_datafilename):
            self.MissingRequiredField("sequencing_datafilename")
        if not isinstance(self.sequencing_datafilename, str):
            self.sequencing_datafilename = str(self.sequencing_datafilename)

        if self._is_empty(self.sequencing_dataread_direction):
            self.MissingRequiredField("sequencing_dataread_direction")
        if not isinstance(self.sequencing_dataread_direction, V1p4ReadDirection):
            self.sequencing_dataread_direction = V1p4ReadDirection(self.sequencing_dataread_direction)

        if self._is_empty(self.sequencing_dataread_length):
            self.MissingRequiredField("sequencing_dataread_length")
        if not isinstance(self.sequencing_dataread_length, int):
            self.sequencing_dataread_length = int(self.sequencing_dataread_length)

        if self._is_empty(self.sequencing_datapaired_filename):
            self.MissingRequiredField("sequencing_datapaired_filename")
        if not isinstance(self.sequencing_datapaired_filename, str):
            self.sequencing_datapaired_filename = str(self.sequencing_datapaired_filename)

        if self._is_empty(self.sequencing_datapaired_read_direction):
            self.MissingRequiredField("sequencing_datapaired_read_direction")
        if not isinstance(self.sequencing_datapaired_read_direction, V1p4PairedReadDirection):
            self.sequencing_datapaired_read_direction = V1p4PairedReadDirection(self.sequencing_datapaired_read_direction)

        if self._is_empty(self.sequencing_datapaired_read_length):
            self.MissingRequiredField("sequencing_datapaired_read_length")
        if not isinstance(self.sequencing_datapaired_read_length, int):
            self.sequencing_datapaired_read_length = int(self.sequencing_datapaired_read_length)

        if self.sequencing_dataindex_filename is not None and not isinstance(self.sequencing_dataindex_filename, str):
            self.sequencing_dataindex_filename = str(self.sequencing_dataindex_filename)

        if self.sequencing_dataindex_length is not None and not isinstance(self.sequencing_dataindex_length, int):
            self.sequencing_dataindex_length = int(self.sequencing_dataindex_length)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4DataProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4DataProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4DataProcessing"
    class_name: ClassVar[str] = "V1p4_DataProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4DataProcessing

    data_processingsoftware_versions: str = None
    data_processingpaired_reads_assembly: str = None
    data_processingquality_thresholds: str = None
    data_processingprimer_match_cutoffs: str = None
    data_processingcollapsing_method: str = None
    data_processingdata_processing_protocols: str = None
    data_processinggermline_database: str = None
    data_processingdata_processing_id: Optional[str] = None
    data_processingprimary_annotation: Optional[Union[bool, Bool]] = None
    data_processingdata_processing_files: Optional[Union[str, List[str]]] = empty_list()
    data_processinggermline_set_ref: Optional[str] = None
    data_processinganalysis_provenance_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.data_processingsoftware_versions):
            self.MissingRequiredField("data_processingsoftware_versions")
        if not isinstance(self.data_processingsoftware_versions, str):
            self.data_processingsoftware_versions = str(self.data_processingsoftware_versions)

        if self._is_empty(self.data_processingpaired_reads_assembly):
            self.MissingRequiredField("data_processingpaired_reads_assembly")
        if not isinstance(self.data_processingpaired_reads_assembly, str):
            self.data_processingpaired_reads_assembly = str(self.data_processingpaired_reads_assembly)

        if self._is_empty(self.data_processingquality_thresholds):
            self.MissingRequiredField("data_processingquality_thresholds")
        if not isinstance(self.data_processingquality_thresholds, str):
            self.data_processingquality_thresholds = str(self.data_processingquality_thresholds)

        if self._is_empty(self.data_processingprimer_match_cutoffs):
            self.MissingRequiredField("data_processingprimer_match_cutoffs")
        if not isinstance(self.data_processingprimer_match_cutoffs, str):
            self.data_processingprimer_match_cutoffs = str(self.data_processingprimer_match_cutoffs)

        if self._is_empty(self.data_processingcollapsing_method):
            self.MissingRequiredField("data_processingcollapsing_method")
        if not isinstance(self.data_processingcollapsing_method, str):
            self.data_processingcollapsing_method = str(self.data_processingcollapsing_method)

        if self._is_empty(self.data_processingdata_processing_protocols):
            self.MissingRequiredField("data_processingdata_processing_protocols")
        if not isinstance(self.data_processingdata_processing_protocols, str):
            self.data_processingdata_processing_protocols = str(self.data_processingdata_processing_protocols)

        if self._is_empty(self.data_processinggermline_database):
            self.MissingRequiredField("data_processinggermline_database")
        if not isinstance(self.data_processinggermline_database, str):
            self.data_processinggermline_database = str(self.data_processinggermline_database)

        if self.data_processingdata_processing_id is not None and not isinstance(self.data_processingdata_processing_id, str):
            self.data_processingdata_processing_id = str(self.data_processingdata_processing_id)

        if self.data_processingprimary_annotation is not None and not isinstance(self.data_processingprimary_annotation, Bool):
            self.data_processingprimary_annotation = Bool(self.data_processingprimary_annotation)

        if not isinstance(self.data_processingdata_processing_files, list):
            self.data_processingdata_processing_files = [self.data_processingdata_processing_files] if self.data_processingdata_processing_files is not None else []
        self.data_processingdata_processing_files = [v if isinstance(v, str) else str(v) for v in self.data_processingdata_processing_files]

        if self.data_processinggermline_set_ref is not None and not isinstance(self.data_processinggermline_set_ref, str):
            self.data_processinggermline_set_ref = str(self.data_processinggermline_set_ref)

        if self.data_processinganalysis_provenance_id is not None and not isinstance(self.data_processinganalysis_provenance_id, str):
            self.data_processinganalysis_provenance_id = str(self.data_processinganalysis_provenance_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Repertoire(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Repertoire"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Repertoire"
    class_name: ClassVar[str] = "V1p4_Repertoire"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Repertoire

    repertoirestudy: Union[dict, V1p4Study] = None
    repertoiresubject: Union[dict, V1p4Subject] = None
    repertoiresample: Union[Union[dict, "V1p4SampleProcessing"], List[Union[dict, "V1p4SampleProcessing"]]] = None
    repertoiredata_processing: Union[Union[dict, V1p4DataProcessing], List[Union[dict, V1p4DataProcessing]]] = None
    repertoirerepertoire_id: Optional[str] = None
    repertoirerepertoire_name: Optional[str] = None
    repertoirerepertoire_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.repertoirestudy):
            self.MissingRequiredField("repertoirestudy")
        if not isinstance(self.repertoirestudy, V1p4Study):
            self.repertoirestudy = V1p4Study(**as_dict(self.repertoirestudy))

        if self._is_empty(self.repertoiresubject):
            self.MissingRequiredField("repertoiresubject")
        if not isinstance(self.repertoiresubject, V1p4Subject):
            self.repertoiresubject = V1p4Subject(**as_dict(self.repertoiresubject))

        if self._is_empty(self.repertoiresample):
            self.MissingRequiredField("repertoiresample")
        self._normalize_inlined_as_dict(slot_name="repertoiresample", slot_type=V1p4SampleProcessing, key_name="sequencing_runsequencing_run_id", keyed=False)

        if self._is_empty(self.repertoiredata_processing):
            self.MissingRequiredField("repertoiredata_processing")
        self._normalize_inlined_as_dict(slot_name="repertoiredata_processing", slot_type=V1p4DataProcessing, key_name="data_processingsoftware_versions", keyed=False)

        if self.repertoirerepertoire_id is not None and not isinstance(self.repertoirerepertoire_id, str):
            self.repertoirerepertoire_id = str(self.repertoirerepertoire_id)

        if self.repertoirerepertoire_name is not None and not isinstance(self.repertoirerepertoire_name, str):
            self.repertoirerepertoire_name = str(self.repertoirerepertoire_name)

        if self.repertoirerepertoire_description is not None and not isinstance(self.repertoirerepertoire_description, str):
            self.repertoirerepertoire_description = str(self.repertoirerepertoire_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4RepertoireGroup(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4RepertoireGroup"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4RepertoireGroup"
    class_name: ClassVar[str] = "V1p4_RepertoireGroup"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4RepertoireGroup

    repertoire_grouprepertoire_group_id: str = None
    repertoire_grouprepertoires: Union[str, List[str]] = None
    repertoire_grouprepertoire_group_name: Optional[str] = None
    repertoire_grouprepertoire_group_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.repertoire_grouprepertoire_group_id):
            self.MissingRequiredField("repertoire_grouprepertoire_group_id")
        if not isinstance(self.repertoire_grouprepertoire_group_id, str):
            self.repertoire_grouprepertoire_group_id = str(self.repertoire_grouprepertoire_group_id)

        if self._is_empty(self.repertoire_grouprepertoires):
            self.MissingRequiredField("repertoire_grouprepertoires")
        if not isinstance(self.repertoire_grouprepertoires, list):
            self.repertoire_grouprepertoires = [self.repertoire_grouprepertoires] if self.repertoire_grouprepertoires is not None else []
        self.repertoire_grouprepertoires = [v if isinstance(v, str) else str(v) for v in self.repertoire_grouprepertoires]

        if self.repertoire_grouprepertoire_group_name is not None and not isinstance(self.repertoire_grouprepertoire_group_name, str):
            self.repertoire_grouprepertoire_group_name = str(self.repertoire_grouprepertoire_group_name)

        if self.repertoire_grouprepertoire_group_description is not None and not isinstance(self.repertoire_grouprepertoire_group_description, str):
            self.repertoire_grouprepertoire_group_description = str(self.repertoire_grouprepertoire_group_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Alignment(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Alignment"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Alignment"
    class_name: ClassVar[str] = "V1p4_Alignment"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Alignment

    alignmentsequence_id: str = None
    alignmentsegment: str = None
    alignmentcall: str = None
    alignmentscore: float = None
    alignmentcigar: str = None
    alignmentrev_comp: Optional[Union[bool, Bool]] = None
    alignmentidentity: Optional[float] = None
    alignmentsupport: Optional[float] = None
    alignmentsequence_start: Optional[int] = None
    alignmentsequence_end: Optional[int] = None
    alignmentgermline_start: Optional[int] = None
    alignmentgermline_end: Optional[int] = None
    alignmentrank: Optional[int] = None
    alignmentdata_processing_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.alignmentsequence_id):
            self.MissingRequiredField("alignmentsequence_id")
        if not isinstance(self.alignmentsequence_id, str):
            self.alignmentsequence_id = str(self.alignmentsequence_id)

        if self._is_empty(self.alignmentsegment):
            self.MissingRequiredField("alignmentsegment")
        if not isinstance(self.alignmentsegment, str):
            self.alignmentsegment = str(self.alignmentsegment)

        if self._is_empty(self.alignmentcall):
            self.MissingRequiredField("alignmentcall")
        if not isinstance(self.alignmentcall, str):
            self.alignmentcall = str(self.alignmentcall)

        if self._is_empty(self.alignmentscore):
            self.MissingRequiredField("alignmentscore")
        if not isinstance(self.alignmentscore, float):
            self.alignmentscore = float(self.alignmentscore)

        if self._is_empty(self.alignmentcigar):
            self.MissingRequiredField("alignmentcigar")
        if not isinstance(self.alignmentcigar, str):
            self.alignmentcigar = str(self.alignmentcigar)

        if self.alignmentrev_comp is not None and not isinstance(self.alignmentrev_comp, Bool):
            self.alignmentrev_comp = Bool(self.alignmentrev_comp)

        if self.alignmentidentity is not None and not isinstance(self.alignmentidentity, float):
            self.alignmentidentity = float(self.alignmentidentity)

        if self.alignmentsupport is not None and not isinstance(self.alignmentsupport, float):
            self.alignmentsupport = float(self.alignmentsupport)

        if self.alignmentsequence_start is not None and not isinstance(self.alignmentsequence_start, int):
            self.alignmentsequence_start = int(self.alignmentsequence_start)

        if self.alignmentsequence_end is not None and not isinstance(self.alignmentsequence_end, int):
            self.alignmentsequence_end = int(self.alignmentsequence_end)

        if self.alignmentgermline_start is not None and not isinstance(self.alignmentgermline_start, int):
            self.alignmentgermline_start = int(self.alignmentgermline_start)

        if self.alignmentgermline_end is not None and not isinstance(self.alignmentgermline_end, int):
            self.alignmentgermline_end = int(self.alignmentgermline_end)

        if self.alignmentrank is not None and not isinstance(self.alignmentrank, int):
            self.alignmentrank = int(self.alignmentrank)

        if self.alignmentdata_processing_id is not None and not isinstance(self.alignmentdata_processing_id, str):
            self.alignmentdata_processing_id = str(self.alignmentdata_processing_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Rearrangement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Rearrangement"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Rearrangement"
    class_name: ClassVar[str] = "V1p4_Rearrangement"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Rearrangement

    rearrangementsequence_id: str = None
    rearrangementsequence: str = None
    rearrangementrev_comp: Union[bool, Bool] = None
    rearrangementproductive: Union[bool, Bool] = None
    rearrangementv_call: str = None
    rearrangementd_call: str = None
    rearrangementj_call: str = None
    rearrangementsequence_alignment: str = None
    rearrangementgermline_alignment: str = None
    rearrangementjunction: str = None
    rearrangementjunction_aa: str = None
    rearrangementv_cigar: str = None
    rearrangementd_cigar: str = None
    rearrangementj_cigar: str = None
    rearrangementquality: Optional[str] = None
    rearrangementsequence_aa: Optional[str] = None
    rearrangementvj_in_frame: Optional[Union[bool, Bool]] = None
    rearrangementstop_codon: Optional[Union[bool, Bool]] = None
    rearrangementcomplete_vdj: Optional[Union[bool, Bool]] = None
    rearrangementlocus: Optional[Union[str, "V1p4Locus"]] = None
    rearrangementlocus_species: Optional[Union[str, "V1p4LocusSpecies"]] = None
    rearrangementd2_call: Optional[str] = None
    rearrangementc_call: Optional[str] = None
    rearrangementquality_alignment: Optional[str] = None
    rearrangementsequence_alignment_aa: Optional[str] = None
    rearrangementgermline_alignment_aa: Optional[str] = None
    rearrangementnp1: Optional[str] = None
    rearrangementnp1_aa: Optional[str] = None
    rearrangementnp2: Optional[str] = None
    rearrangementnp2_aa: Optional[str] = None
    rearrangementnp3: Optional[str] = None
    rearrangementnp3_aa: Optional[str] = None
    rearrangementcdr1: Optional[str] = None
    rearrangementcdr1_aa: Optional[str] = None
    rearrangementcdr2: Optional[str] = None
    rearrangementcdr2_aa: Optional[str] = None
    rearrangementcdr3: Optional[str] = None
    rearrangementcdr3_aa: Optional[str] = None
    rearrangementfwr1: Optional[str] = None
    rearrangementfwr1_aa: Optional[str] = None
    rearrangementfwr2: Optional[str] = None
    rearrangementfwr2_aa: Optional[str] = None
    rearrangementfwr3: Optional[str] = None
    rearrangementfwr3_aa: Optional[str] = None
    rearrangementfwr4: Optional[str] = None
    rearrangementfwr4_aa: Optional[str] = None
    rearrangementv_score: Optional[float] = None
    rearrangementv_identity: Optional[float] = None
    rearrangementv_support: Optional[float] = None
    rearrangementd_score: Optional[float] = None
    rearrangementd_identity: Optional[float] = None
    rearrangementd_support: Optional[float] = None
    rearrangementd2_score: Optional[float] = None
    rearrangementd2_identity: Optional[float] = None
    rearrangementd2_support: Optional[float] = None
    rearrangementd2_cigar: Optional[str] = None
    rearrangementj_score: Optional[float] = None
    rearrangementj_identity: Optional[float] = None
    rearrangementj_support: Optional[float] = None
    rearrangementc_score: Optional[float] = None
    rearrangementc_identity: Optional[float] = None
    rearrangementc_support: Optional[float] = None
    rearrangementc_cigar: Optional[str] = None
    rearrangementv_sequence_start: Optional[int] = None
    rearrangementv_sequence_end: Optional[int] = None
    rearrangementv_germline_start: Optional[int] = None
    rearrangementv_germline_end: Optional[int] = None
    rearrangementv_alignment_start: Optional[int] = None
    rearrangementv_alignment_end: Optional[int] = None
    rearrangementd_sequence_start: Optional[int] = None
    rearrangementd_sequence_end: Optional[int] = None
    rearrangementd_germline_start: Optional[int] = None
    rearrangementd_germline_end: Optional[int] = None
    rearrangementd_alignment_start: Optional[int] = None
    rearrangementd_alignment_end: Optional[int] = None
    rearrangementd2_sequence_start: Optional[int] = None
    rearrangementd2_sequence_end: Optional[int] = None
    rearrangementd2_germline_start: Optional[int] = None
    rearrangementd2_germline_end: Optional[int] = None
    rearrangementd2_alignment_start: Optional[int] = None
    rearrangementd2_alignment_end: Optional[int] = None
    rearrangementj_sequence_start: Optional[int] = None
    rearrangementj_sequence_end: Optional[int] = None
    rearrangementj_germline_start: Optional[int] = None
    rearrangementj_germline_end: Optional[int] = None
    rearrangementj_alignment_start: Optional[int] = None
    rearrangementj_alignment_end: Optional[int] = None
    rearrangementc_sequence_start: Optional[int] = None
    rearrangementc_sequence_end: Optional[int] = None
    rearrangementc_germline_start: Optional[int] = None
    rearrangementc_germline_end: Optional[int] = None
    rearrangementc_alignment_start: Optional[int] = None
    rearrangementc_alignment_end: Optional[int] = None
    rearrangementcdr1_start: Optional[int] = None
    rearrangementcdr1_end: Optional[int] = None
    rearrangementcdr2_start: Optional[int] = None
    rearrangementcdr2_end: Optional[int] = None
    rearrangementcdr3_start: Optional[int] = None
    rearrangementcdr3_end: Optional[int] = None
    rearrangementfwr1_start: Optional[int] = None
    rearrangementfwr1_end: Optional[int] = None
    rearrangementfwr2_start: Optional[int] = None
    rearrangementfwr2_end: Optional[int] = None
    rearrangementfwr3_start: Optional[int] = None
    rearrangementfwr3_end: Optional[int] = None
    rearrangementfwr4_start: Optional[int] = None
    rearrangementfwr4_end: Optional[int] = None
    rearrangementv_sequence_alignment: Optional[str] = None
    rearrangementv_sequence_alignment_aa: Optional[str] = None
    rearrangementd_sequence_alignment: Optional[str] = None
    rearrangementd_sequence_alignment_aa: Optional[str] = None
    rearrangementd2_sequence_alignment: Optional[str] = None
    rearrangementd2_sequence_alignment_aa: Optional[str] = None
    rearrangementj_sequence_alignment: Optional[str] = None
    rearrangementj_sequence_alignment_aa: Optional[str] = None
    rearrangementc_sequence_alignment: Optional[str] = None
    rearrangementc_sequence_alignment_aa: Optional[str] = None
    rearrangementv_germline_alignment: Optional[str] = None
    rearrangementv_germline_alignment_aa: Optional[str] = None
    rearrangementd_germline_alignment: Optional[str] = None
    rearrangementd_germline_alignment_aa: Optional[str] = None
    rearrangementd2_germline_alignment: Optional[str] = None
    rearrangementd2_germline_alignment_aa: Optional[str] = None
    rearrangementj_germline_alignment: Optional[str] = None
    rearrangementj_germline_alignment_aa: Optional[str] = None
    rearrangementc_germline_alignment: Optional[str] = None
    rearrangementc_germline_alignment_aa: Optional[str] = None
    rearrangementjunction_length: Optional[int] = None
    rearrangementjunction_aa_length: Optional[int] = None
    rearrangementnp1_length: Optional[int] = None
    rearrangementnp2_length: Optional[int] = None
    rearrangementnp3_length: Optional[int] = None
    rearrangementn1_length: Optional[int] = None
    rearrangementn2_length: Optional[int] = None
    rearrangementn3_length: Optional[int] = None
    rearrangementp3v_length: Optional[int] = None
    rearrangementp5d_length: Optional[int] = None
    rearrangementp3d_length: Optional[int] = None
    rearrangementp5d2_length: Optional[int] = None
    rearrangementp3d2_length: Optional[int] = None
    rearrangementp5j_length: Optional[int] = None
    rearrangementv_frameshift: Optional[Union[bool, Bool]] = None
    rearrangementj_frameshift: Optional[Union[bool, Bool]] = None
    rearrangementd_frame: Optional[int] = None
    rearrangementd2_frame: Optional[int] = None
    rearrangementconsensus_count: Optional[int] = None
    rearrangementduplicate_count: Optional[int] = None
    rearrangementumi_count: Optional[int] = None
    rearrangementcell_id: Optional[str] = None
    rearrangementclone_id: Optional[str] = None
    rearrangementreactivity_id: Optional[str] = None
    rearrangementreactivity_ref: Optional[str] = None
    rearrangementrepertoire_id: Optional[str] = None
    rearrangementsample_processing_id: Optional[str] = None
    rearrangementdata_processing_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.rearrangementsequence_id):
            self.MissingRequiredField("rearrangementsequence_id")
        if not isinstance(self.rearrangementsequence_id, str):
            self.rearrangementsequence_id = str(self.rearrangementsequence_id)

        if self._is_empty(self.rearrangementsequence):
            self.MissingRequiredField("rearrangementsequence")
        if not isinstance(self.rearrangementsequence, str):
            self.rearrangementsequence = str(self.rearrangementsequence)

        if self._is_empty(self.rearrangementrev_comp):
            self.MissingRequiredField("rearrangementrev_comp")
        if not isinstance(self.rearrangementrev_comp, Bool):
            self.rearrangementrev_comp = Bool(self.rearrangementrev_comp)

        if self._is_empty(self.rearrangementproductive):
            self.MissingRequiredField("rearrangementproductive")
        if not isinstance(self.rearrangementproductive, Bool):
            self.rearrangementproductive = Bool(self.rearrangementproductive)

        if self._is_empty(self.rearrangementv_call):
            self.MissingRequiredField("rearrangementv_call")
        if not isinstance(self.rearrangementv_call, str):
            self.rearrangementv_call = str(self.rearrangementv_call)

        if self._is_empty(self.rearrangementd_call):
            self.MissingRequiredField("rearrangementd_call")
        if not isinstance(self.rearrangementd_call, str):
            self.rearrangementd_call = str(self.rearrangementd_call)

        if self._is_empty(self.rearrangementj_call):
            self.MissingRequiredField("rearrangementj_call")
        if not isinstance(self.rearrangementj_call, str):
            self.rearrangementj_call = str(self.rearrangementj_call)

        if self._is_empty(self.rearrangementsequence_alignment):
            self.MissingRequiredField("rearrangementsequence_alignment")
        if not isinstance(self.rearrangementsequence_alignment, str):
            self.rearrangementsequence_alignment = str(self.rearrangementsequence_alignment)

        if self._is_empty(self.rearrangementgermline_alignment):
            self.MissingRequiredField("rearrangementgermline_alignment")
        if not isinstance(self.rearrangementgermline_alignment, str):
            self.rearrangementgermline_alignment = str(self.rearrangementgermline_alignment)

        if self._is_empty(self.rearrangementjunction):
            self.MissingRequiredField("rearrangementjunction")
        if not isinstance(self.rearrangementjunction, str):
            self.rearrangementjunction = str(self.rearrangementjunction)

        if self._is_empty(self.rearrangementjunction_aa):
            self.MissingRequiredField("rearrangementjunction_aa")
        if not isinstance(self.rearrangementjunction_aa, str):
            self.rearrangementjunction_aa = str(self.rearrangementjunction_aa)

        if self._is_empty(self.rearrangementv_cigar):
            self.MissingRequiredField("rearrangementv_cigar")
        if not isinstance(self.rearrangementv_cigar, str):
            self.rearrangementv_cigar = str(self.rearrangementv_cigar)

        if self._is_empty(self.rearrangementd_cigar):
            self.MissingRequiredField("rearrangementd_cigar")
        if not isinstance(self.rearrangementd_cigar, str):
            self.rearrangementd_cigar = str(self.rearrangementd_cigar)

        if self._is_empty(self.rearrangementj_cigar):
            self.MissingRequiredField("rearrangementj_cigar")
        if not isinstance(self.rearrangementj_cigar, str):
            self.rearrangementj_cigar = str(self.rearrangementj_cigar)

        if self.rearrangementquality is not None and not isinstance(self.rearrangementquality, str):
            self.rearrangementquality = str(self.rearrangementquality)

        if self.rearrangementsequence_aa is not None and not isinstance(self.rearrangementsequence_aa, str):
            self.rearrangementsequence_aa = str(self.rearrangementsequence_aa)

        if self.rearrangementvj_in_frame is not None and not isinstance(self.rearrangementvj_in_frame, Bool):
            self.rearrangementvj_in_frame = Bool(self.rearrangementvj_in_frame)

        if self.rearrangementstop_codon is not None and not isinstance(self.rearrangementstop_codon, Bool):
            self.rearrangementstop_codon = Bool(self.rearrangementstop_codon)

        if self.rearrangementcomplete_vdj is not None and not isinstance(self.rearrangementcomplete_vdj, Bool):
            self.rearrangementcomplete_vdj = Bool(self.rearrangementcomplete_vdj)

        if self.rearrangementlocus is not None and not isinstance(self.rearrangementlocus, V1p4Locus):
            self.rearrangementlocus = V1p4Locus(self.rearrangementlocus)

        if self.rearrangementd2_call is not None and not isinstance(self.rearrangementd2_call, str):
            self.rearrangementd2_call = str(self.rearrangementd2_call)

        if self.rearrangementc_call is not None and not isinstance(self.rearrangementc_call, str):
            self.rearrangementc_call = str(self.rearrangementc_call)

        if self.rearrangementquality_alignment is not None and not isinstance(self.rearrangementquality_alignment, str):
            self.rearrangementquality_alignment = str(self.rearrangementquality_alignment)

        if self.rearrangementsequence_alignment_aa is not None and not isinstance(self.rearrangementsequence_alignment_aa, str):
            self.rearrangementsequence_alignment_aa = str(self.rearrangementsequence_alignment_aa)

        if self.rearrangementgermline_alignment_aa is not None and not isinstance(self.rearrangementgermline_alignment_aa, str):
            self.rearrangementgermline_alignment_aa = str(self.rearrangementgermline_alignment_aa)

        if self.rearrangementnp1 is not None and not isinstance(self.rearrangementnp1, str):
            self.rearrangementnp1 = str(self.rearrangementnp1)

        if self.rearrangementnp1_aa is not None and not isinstance(self.rearrangementnp1_aa, str):
            self.rearrangementnp1_aa = str(self.rearrangementnp1_aa)

        if self.rearrangementnp2 is not None and not isinstance(self.rearrangementnp2, str):
            self.rearrangementnp2 = str(self.rearrangementnp2)

        if self.rearrangementnp2_aa is not None and not isinstance(self.rearrangementnp2_aa, str):
            self.rearrangementnp2_aa = str(self.rearrangementnp2_aa)

        if self.rearrangementnp3 is not None and not isinstance(self.rearrangementnp3, str):
            self.rearrangementnp3 = str(self.rearrangementnp3)

        if self.rearrangementnp3_aa is not None and not isinstance(self.rearrangementnp3_aa, str):
            self.rearrangementnp3_aa = str(self.rearrangementnp3_aa)

        if self.rearrangementcdr1 is not None and not isinstance(self.rearrangementcdr1, str):
            self.rearrangementcdr1 = str(self.rearrangementcdr1)

        if self.rearrangementcdr1_aa is not None and not isinstance(self.rearrangementcdr1_aa, str):
            self.rearrangementcdr1_aa = str(self.rearrangementcdr1_aa)

        if self.rearrangementcdr2 is not None and not isinstance(self.rearrangementcdr2, str):
            self.rearrangementcdr2 = str(self.rearrangementcdr2)

        if self.rearrangementcdr2_aa is not None and not isinstance(self.rearrangementcdr2_aa, str):
            self.rearrangementcdr2_aa = str(self.rearrangementcdr2_aa)

        if self.rearrangementcdr3 is not None and not isinstance(self.rearrangementcdr3, str):
            self.rearrangementcdr3 = str(self.rearrangementcdr3)

        if self.rearrangementcdr3_aa is not None and not isinstance(self.rearrangementcdr3_aa, str):
            self.rearrangementcdr3_aa = str(self.rearrangementcdr3_aa)

        if self.rearrangementfwr1 is not None and not isinstance(self.rearrangementfwr1, str):
            self.rearrangementfwr1 = str(self.rearrangementfwr1)

        if self.rearrangementfwr1_aa is not None and not isinstance(self.rearrangementfwr1_aa, str):
            self.rearrangementfwr1_aa = str(self.rearrangementfwr1_aa)

        if self.rearrangementfwr2 is not None and not isinstance(self.rearrangementfwr2, str):
            self.rearrangementfwr2 = str(self.rearrangementfwr2)

        if self.rearrangementfwr2_aa is not None and not isinstance(self.rearrangementfwr2_aa, str):
            self.rearrangementfwr2_aa = str(self.rearrangementfwr2_aa)

        if self.rearrangementfwr3 is not None and not isinstance(self.rearrangementfwr3, str):
            self.rearrangementfwr3 = str(self.rearrangementfwr3)

        if self.rearrangementfwr3_aa is not None and not isinstance(self.rearrangementfwr3_aa, str):
            self.rearrangementfwr3_aa = str(self.rearrangementfwr3_aa)

        if self.rearrangementfwr4 is not None and not isinstance(self.rearrangementfwr4, str):
            self.rearrangementfwr4 = str(self.rearrangementfwr4)

        if self.rearrangementfwr4_aa is not None and not isinstance(self.rearrangementfwr4_aa, str):
            self.rearrangementfwr4_aa = str(self.rearrangementfwr4_aa)

        if self.rearrangementv_score is not None and not isinstance(self.rearrangementv_score, float):
            self.rearrangementv_score = float(self.rearrangementv_score)

        if self.rearrangementv_identity is not None and not isinstance(self.rearrangementv_identity, float):
            self.rearrangementv_identity = float(self.rearrangementv_identity)

        if self.rearrangementv_support is not None and not isinstance(self.rearrangementv_support, float):
            self.rearrangementv_support = float(self.rearrangementv_support)

        if self.rearrangementd_score is not None and not isinstance(self.rearrangementd_score, float):
            self.rearrangementd_score = float(self.rearrangementd_score)

        if self.rearrangementd_identity is not None and not isinstance(self.rearrangementd_identity, float):
            self.rearrangementd_identity = float(self.rearrangementd_identity)

        if self.rearrangementd_support is not None and not isinstance(self.rearrangementd_support, float):
            self.rearrangementd_support = float(self.rearrangementd_support)

        if self.rearrangementd2_score is not None and not isinstance(self.rearrangementd2_score, float):
            self.rearrangementd2_score = float(self.rearrangementd2_score)

        if self.rearrangementd2_identity is not None and not isinstance(self.rearrangementd2_identity, float):
            self.rearrangementd2_identity = float(self.rearrangementd2_identity)

        if self.rearrangementd2_support is not None and not isinstance(self.rearrangementd2_support, float):
            self.rearrangementd2_support = float(self.rearrangementd2_support)

        if self.rearrangementd2_cigar is not None and not isinstance(self.rearrangementd2_cigar, str):
            self.rearrangementd2_cigar = str(self.rearrangementd2_cigar)

        if self.rearrangementj_score is not None and not isinstance(self.rearrangementj_score, float):
            self.rearrangementj_score = float(self.rearrangementj_score)

        if self.rearrangementj_identity is not None and not isinstance(self.rearrangementj_identity, float):
            self.rearrangementj_identity = float(self.rearrangementj_identity)

        if self.rearrangementj_support is not None and not isinstance(self.rearrangementj_support, float):
            self.rearrangementj_support = float(self.rearrangementj_support)

        if self.rearrangementc_score is not None and not isinstance(self.rearrangementc_score, float):
            self.rearrangementc_score = float(self.rearrangementc_score)

        if self.rearrangementc_identity is not None and not isinstance(self.rearrangementc_identity, float):
            self.rearrangementc_identity = float(self.rearrangementc_identity)

        if self.rearrangementc_support is not None and not isinstance(self.rearrangementc_support, float):
            self.rearrangementc_support = float(self.rearrangementc_support)

        if self.rearrangementc_cigar is not None and not isinstance(self.rearrangementc_cigar, str):
            self.rearrangementc_cigar = str(self.rearrangementc_cigar)

        if self.rearrangementv_sequence_start is not None and not isinstance(self.rearrangementv_sequence_start, int):
            self.rearrangementv_sequence_start = int(self.rearrangementv_sequence_start)

        if self.rearrangementv_sequence_end is not None and not isinstance(self.rearrangementv_sequence_end, int):
            self.rearrangementv_sequence_end = int(self.rearrangementv_sequence_end)

        if self.rearrangementv_germline_start is not None and not isinstance(self.rearrangementv_germline_start, int):
            self.rearrangementv_germline_start = int(self.rearrangementv_germline_start)

        if self.rearrangementv_germline_end is not None and not isinstance(self.rearrangementv_germline_end, int):
            self.rearrangementv_germline_end = int(self.rearrangementv_germline_end)

        if self.rearrangementv_alignment_start is not None and not isinstance(self.rearrangementv_alignment_start, int):
            self.rearrangementv_alignment_start = int(self.rearrangementv_alignment_start)

        if self.rearrangementv_alignment_end is not None and not isinstance(self.rearrangementv_alignment_end, int):
            self.rearrangementv_alignment_end = int(self.rearrangementv_alignment_end)

        if self.rearrangementd_sequence_start is not None and not isinstance(self.rearrangementd_sequence_start, int):
            self.rearrangementd_sequence_start = int(self.rearrangementd_sequence_start)

        if self.rearrangementd_sequence_end is not None and not isinstance(self.rearrangementd_sequence_end, int):
            self.rearrangementd_sequence_end = int(self.rearrangementd_sequence_end)

        if self.rearrangementd_germline_start is not None and not isinstance(self.rearrangementd_germline_start, int):
            self.rearrangementd_germline_start = int(self.rearrangementd_germline_start)

        if self.rearrangementd_germline_end is not None and not isinstance(self.rearrangementd_germline_end, int):
            self.rearrangementd_germline_end = int(self.rearrangementd_germline_end)

        if self.rearrangementd_alignment_start is not None and not isinstance(self.rearrangementd_alignment_start, int):
            self.rearrangementd_alignment_start = int(self.rearrangementd_alignment_start)

        if self.rearrangementd_alignment_end is not None and not isinstance(self.rearrangementd_alignment_end, int):
            self.rearrangementd_alignment_end = int(self.rearrangementd_alignment_end)

        if self.rearrangementd2_sequence_start is not None and not isinstance(self.rearrangementd2_sequence_start, int):
            self.rearrangementd2_sequence_start = int(self.rearrangementd2_sequence_start)

        if self.rearrangementd2_sequence_end is not None and not isinstance(self.rearrangementd2_sequence_end, int):
            self.rearrangementd2_sequence_end = int(self.rearrangementd2_sequence_end)

        if self.rearrangementd2_germline_start is not None and not isinstance(self.rearrangementd2_germline_start, int):
            self.rearrangementd2_germline_start = int(self.rearrangementd2_germline_start)

        if self.rearrangementd2_germline_end is not None and not isinstance(self.rearrangementd2_germline_end, int):
            self.rearrangementd2_germline_end = int(self.rearrangementd2_germline_end)

        if self.rearrangementd2_alignment_start is not None and not isinstance(self.rearrangementd2_alignment_start, int):
            self.rearrangementd2_alignment_start = int(self.rearrangementd2_alignment_start)

        if self.rearrangementd2_alignment_end is not None and not isinstance(self.rearrangementd2_alignment_end, int):
            self.rearrangementd2_alignment_end = int(self.rearrangementd2_alignment_end)

        if self.rearrangementj_sequence_start is not None and not isinstance(self.rearrangementj_sequence_start, int):
            self.rearrangementj_sequence_start = int(self.rearrangementj_sequence_start)

        if self.rearrangementj_sequence_end is not None and not isinstance(self.rearrangementj_sequence_end, int):
            self.rearrangementj_sequence_end = int(self.rearrangementj_sequence_end)

        if self.rearrangementj_germline_start is not None and not isinstance(self.rearrangementj_germline_start, int):
            self.rearrangementj_germline_start = int(self.rearrangementj_germline_start)

        if self.rearrangementj_germline_end is not None and not isinstance(self.rearrangementj_germline_end, int):
            self.rearrangementj_germline_end = int(self.rearrangementj_germline_end)

        if self.rearrangementj_alignment_start is not None and not isinstance(self.rearrangementj_alignment_start, int):
            self.rearrangementj_alignment_start = int(self.rearrangementj_alignment_start)

        if self.rearrangementj_alignment_end is not None and not isinstance(self.rearrangementj_alignment_end, int):
            self.rearrangementj_alignment_end = int(self.rearrangementj_alignment_end)

        if self.rearrangementc_sequence_start is not None and not isinstance(self.rearrangementc_sequence_start, int):
            self.rearrangementc_sequence_start = int(self.rearrangementc_sequence_start)

        if self.rearrangementc_sequence_end is not None and not isinstance(self.rearrangementc_sequence_end, int):
            self.rearrangementc_sequence_end = int(self.rearrangementc_sequence_end)

        if self.rearrangementc_germline_start is not None and not isinstance(self.rearrangementc_germline_start, int):
            self.rearrangementc_germline_start = int(self.rearrangementc_germline_start)

        if self.rearrangementc_germline_end is not None and not isinstance(self.rearrangementc_germline_end, int):
            self.rearrangementc_germline_end = int(self.rearrangementc_germline_end)

        if self.rearrangementc_alignment_start is not None and not isinstance(self.rearrangementc_alignment_start, int):
            self.rearrangementc_alignment_start = int(self.rearrangementc_alignment_start)

        if self.rearrangementc_alignment_end is not None and not isinstance(self.rearrangementc_alignment_end, int):
            self.rearrangementc_alignment_end = int(self.rearrangementc_alignment_end)

        if self.rearrangementcdr1_start is not None and not isinstance(self.rearrangementcdr1_start, int):
            self.rearrangementcdr1_start = int(self.rearrangementcdr1_start)

        if self.rearrangementcdr1_end is not None and not isinstance(self.rearrangementcdr1_end, int):
            self.rearrangementcdr1_end = int(self.rearrangementcdr1_end)

        if self.rearrangementcdr2_start is not None and not isinstance(self.rearrangementcdr2_start, int):
            self.rearrangementcdr2_start = int(self.rearrangementcdr2_start)

        if self.rearrangementcdr2_end is not None and not isinstance(self.rearrangementcdr2_end, int):
            self.rearrangementcdr2_end = int(self.rearrangementcdr2_end)

        if self.rearrangementcdr3_start is not None and not isinstance(self.rearrangementcdr3_start, int):
            self.rearrangementcdr3_start = int(self.rearrangementcdr3_start)

        if self.rearrangementcdr3_end is not None and not isinstance(self.rearrangementcdr3_end, int):
            self.rearrangementcdr3_end = int(self.rearrangementcdr3_end)

        if self.rearrangementfwr1_start is not None and not isinstance(self.rearrangementfwr1_start, int):
            self.rearrangementfwr1_start = int(self.rearrangementfwr1_start)

        if self.rearrangementfwr1_end is not None and not isinstance(self.rearrangementfwr1_end, int):
            self.rearrangementfwr1_end = int(self.rearrangementfwr1_end)

        if self.rearrangementfwr2_start is not None and not isinstance(self.rearrangementfwr2_start, int):
            self.rearrangementfwr2_start = int(self.rearrangementfwr2_start)

        if self.rearrangementfwr2_end is not None and not isinstance(self.rearrangementfwr2_end, int):
            self.rearrangementfwr2_end = int(self.rearrangementfwr2_end)

        if self.rearrangementfwr3_start is not None and not isinstance(self.rearrangementfwr3_start, int):
            self.rearrangementfwr3_start = int(self.rearrangementfwr3_start)

        if self.rearrangementfwr3_end is not None and not isinstance(self.rearrangementfwr3_end, int):
            self.rearrangementfwr3_end = int(self.rearrangementfwr3_end)

        if self.rearrangementfwr4_start is not None and not isinstance(self.rearrangementfwr4_start, int):
            self.rearrangementfwr4_start = int(self.rearrangementfwr4_start)

        if self.rearrangementfwr4_end is not None and not isinstance(self.rearrangementfwr4_end, int):
            self.rearrangementfwr4_end = int(self.rearrangementfwr4_end)

        if self.rearrangementv_sequence_alignment is not None and not isinstance(self.rearrangementv_sequence_alignment, str):
            self.rearrangementv_sequence_alignment = str(self.rearrangementv_sequence_alignment)

        if self.rearrangementv_sequence_alignment_aa is not None and not isinstance(self.rearrangementv_sequence_alignment_aa, str):
            self.rearrangementv_sequence_alignment_aa = str(self.rearrangementv_sequence_alignment_aa)

        if self.rearrangementd_sequence_alignment is not None and not isinstance(self.rearrangementd_sequence_alignment, str):
            self.rearrangementd_sequence_alignment = str(self.rearrangementd_sequence_alignment)

        if self.rearrangementd_sequence_alignment_aa is not None and not isinstance(self.rearrangementd_sequence_alignment_aa, str):
            self.rearrangementd_sequence_alignment_aa = str(self.rearrangementd_sequence_alignment_aa)

        if self.rearrangementd2_sequence_alignment is not None and not isinstance(self.rearrangementd2_sequence_alignment, str):
            self.rearrangementd2_sequence_alignment = str(self.rearrangementd2_sequence_alignment)

        if self.rearrangementd2_sequence_alignment_aa is not None and not isinstance(self.rearrangementd2_sequence_alignment_aa, str):
            self.rearrangementd2_sequence_alignment_aa = str(self.rearrangementd2_sequence_alignment_aa)

        if self.rearrangementj_sequence_alignment is not None and not isinstance(self.rearrangementj_sequence_alignment, str):
            self.rearrangementj_sequence_alignment = str(self.rearrangementj_sequence_alignment)

        if self.rearrangementj_sequence_alignment_aa is not None and not isinstance(self.rearrangementj_sequence_alignment_aa, str):
            self.rearrangementj_sequence_alignment_aa = str(self.rearrangementj_sequence_alignment_aa)

        if self.rearrangementc_sequence_alignment is not None and not isinstance(self.rearrangementc_sequence_alignment, str):
            self.rearrangementc_sequence_alignment = str(self.rearrangementc_sequence_alignment)

        if self.rearrangementc_sequence_alignment_aa is not None and not isinstance(self.rearrangementc_sequence_alignment_aa, str):
            self.rearrangementc_sequence_alignment_aa = str(self.rearrangementc_sequence_alignment_aa)

        if self.rearrangementv_germline_alignment is not None and not isinstance(self.rearrangementv_germline_alignment, str):
            self.rearrangementv_germline_alignment = str(self.rearrangementv_germline_alignment)

        if self.rearrangementv_germline_alignment_aa is not None and not isinstance(self.rearrangementv_germline_alignment_aa, str):
            self.rearrangementv_germline_alignment_aa = str(self.rearrangementv_germline_alignment_aa)

        if self.rearrangementd_germline_alignment is not None and not isinstance(self.rearrangementd_germline_alignment, str):
            self.rearrangementd_germline_alignment = str(self.rearrangementd_germline_alignment)

        if self.rearrangementd_germline_alignment_aa is not None and not isinstance(self.rearrangementd_germline_alignment_aa, str):
            self.rearrangementd_germline_alignment_aa = str(self.rearrangementd_germline_alignment_aa)

        if self.rearrangementd2_germline_alignment is not None and not isinstance(self.rearrangementd2_germline_alignment, str):
            self.rearrangementd2_germline_alignment = str(self.rearrangementd2_germline_alignment)

        if self.rearrangementd2_germline_alignment_aa is not None and not isinstance(self.rearrangementd2_germline_alignment_aa, str):
            self.rearrangementd2_germline_alignment_aa = str(self.rearrangementd2_germline_alignment_aa)

        if self.rearrangementj_germline_alignment is not None and not isinstance(self.rearrangementj_germline_alignment, str):
            self.rearrangementj_germline_alignment = str(self.rearrangementj_germline_alignment)

        if self.rearrangementj_germline_alignment_aa is not None and not isinstance(self.rearrangementj_germline_alignment_aa, str):
            self.rearrangementj_germline_alignment_aa = str(self.rearrangementj_germline_alignment_aa)

        if self.rearrangementc_germline_alignment is not None and not isinstance(self.rearrangementc_germline_alignment, str):
            self.rearrangementc_germline_alignment = str(self.rearrangementc_germline_alignment)

        if self.rearrangementc_germline_alignment_aa is not None and not isinstance(self.rearrangementc_germline_alignment_aa, str):
            self.rearrangementc_germline_alignment_aa = str(self.rearrangementc_germline_alignment_aa)

        if self.rearrangementjunction_length is not None and not isinstance(self.rearrangementjunction_length, int):
            self.rearrangementjunction_length = int(self.rearrangementjunction_length)

        if self.rearrangementjunction_aa_length is not None and not isinstance(self.rearrangementjunction_aa_length, int):
            self.rearrangementjunction_aa_length = int(self.rearrangementjunction_aa_length)

        if self.rearrangementnp1_length is not None and not isinstance(self.rearrangementnp1_length, int):
            self.rearrangementnp1_length = int(self.rearrangementnp1_length)

        if self.rearrangementnp2_length is not None and not isinstance(self.rearrangementnp2_length, int):
            self.rearrangementnp2_length = int(self.rearrangementnp2_length)

        if self.rearrangementnp3_length is not None and not isinstance(self.rearrangementnp3_length, int):
            self.rearrangementnp3_length = int(self.rearrangementnp3_length)

        if self.rearrangementn1_length is not None and not isinstance(self.rearrangementn1_length, int):
            self.rearrangementn1_length = int(self.rearrangementn1_length)

        if self.rearrangementn2_length is not None and not isinstance(self.rearrangementn2_length, int):
            self.rearrangementn2_length = int(self.rearrangementn2_length)

        if self.rearrangementn3_length is not None and not isinstance(self.rearrangementn3_length, int):
            self.rearrangementn3_length = int(self.rearrangementn3_length)

        if self.rearrangementp3v_length is not None and not isinstance(self.rearrangementp3v_length, int):
            self.rearrangementp3v_length = int(self.rearrangementp3v_length)

        if self.rearrangementp5d_length is not None and not isinstance(self.rearrangementp5d_length, int):
            self.rearrangementp5d_length = int(self.rearrangementp5d_length)

        if self.rearrangementp3d_length is not None and not isinstance(self.rearrangementp3d_length, int):
            self.rearrangementp3d_length = int(self.rearrangementp3d_length)

        if self.rearrangementp5d2_length is not None and not isinstance(self.rearrangementp5d2_length, int):
            self.rearrangementp5d2_length = int(self.rearrangementp5d2_length)

        if self.rearrangementp3d2_length is not None and not isinstance(self.rearrangementp3d2_length, int):
            self.rearrangementp3d2_length = int(self.rearrangementp3d2_length)

        if self.rearrangementp5j_length is not None and not isinstance(self.rearrangementp5j_length, int):
            self.rearrangementp5j_length = int(self.rearrangementp5j_length)

        if self.rearrangementv_frameshift is not None and not isinstance(self.rearrangementv_frameshift, Bool):
            self.rearrangementv_frameshift = Bool(self.rearrangementv_frameshift)

        if self.rearrangementj_frameshift is not None and not isinstance(self.rearrangementj_frameshift, Bool):
            self.rearrangementj_frameshift = Bool(self.rearrangementj_frameshift)

        if self.rearrangementd_frame is not None and not isinstance(self.rearrangementd_frame, int):
            self.rearrangementd_frame = int(self.rearrangementd_frame)

        if self.rearrangementd2_frame is not None and not isinstance(self.rearrangementd2_frame, int):
            self.rearrangementd2_frame = int(self.rearrangementd2_frame)

        if self.rearrangementconsensus_count is not None and not isinstance(self.rearrangementconsensus_count, int):
            self.rearrangementconsensus_count = int(self.rearrangementconsensus_count)

        if self.rearrangementduplicate_count is not None and not isinstance(self.rearrangementduplicate_count, int):
            self.rearrangementduplicate_count = int(self.rearrangementduplicate_count)

        if self.rearrangementumi_count is not None and not isinstance(self.rearrangementumi_count, int):
            self.rearrangementumi_count = int(self.rearrangementumi_count)

        if self.rearrangementcell_id is not None and not isinstance(self.rearrangementcell_id, str):
            self.rearrangementcell_id = str(self.rearrangementcell_id)

        if self.rearrangementclone_id is not None and not isinstance(self.rearrangementclone_id, str):
            self.rearrangementclone_id = str(self.rearrangementclone_id)

        if self.rearrangementreactivity_id is not None and not isinstance(self.rearrangementreactivity_id, str):
            self.rearrangementreactivity_id = str(self.rearrangementreactivity_id)

        if self.rearrangementreactivity_ref is not None and not isinstance(self.rearrangementreactivity_ref, str):
            self.rearrangementreactivity_ref = str(self.rearrangementreactivity_ref)

        if self.rearrangementrepertoire_id is not None and not isinstance(self.rearrangementrepertoire_id, str):
            self.rearrangementrepertoire_id = str(self.rearrangementrepertoire_id)

        if self.rearrangementsample_processing_id is not None and not isinstance(self.rearrangementsample_processing_id, str):
            self.rearrangementsample_processing_id = str(self.rearrangementsample_processing_id)

        if self.rearrangementdata_processing_id is not None and not isinstance(self.rearrangementdata_processing_id, str):
            self.rearrangementdata_processing_id = str(self.rearrangementdata_processing_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Clone(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Clone"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Clone"
    class_name: ClassVar[str] = "V1p4_Clone"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Clone

    cloneclone_id: str = None
    clonegermline_alignment: str = None
    clonerepertoire_id: Optional[str] = None
    clonedata_processing_id: Optional[str] = None
    clonesequences: Optional[Union[str, List[str]]] = empty_list()
    clonev_call: Optional[str] = None
    cloned_call: Optional[str] = None
    clonej_call: Optional[str] = None
    clonejunction: Optional[str] = None
    clonejunction_aa: Optional[str] = None
    clonejunction_length: Optional[int] = None
    clonejunction_aa_length: Optional[int] = None
    clonegermline_alignment_aa: Optional[str] = None
    clonev_alignment_start: Optional[int] = None
    clonev_alignment_end: Optional[int] = None
    cloned_alignment_start: Optional[int] = None
    cloned_alignment_end: Optional[int] = None
    clonej_alignment_start: Optional[int] = None
    clonej_alignment_end: Optional[int] = None
    clonejunction_start: Optional[int] = None
    clonejunction_end: Optional[int] = None
    cloneumi_count: Optional[int] = None
    cloneclone_count: Optional[int] = None
    cloneseed_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.cloneclone_id):
            self.MissingRequiredField("cloneclone_id")
        if not isinstance(self.cloneclone_id, str):
            self.cloneclone_id = str(self.cloneclone_id)

        if self._is_empty(self.clonegermline_alignment):
            self.MissingRequiredField("clonegermline_alignment")
        if not isinstance(self.clonegermline_alignment, str):
            self.clonegermline_alignment = str(self.clonegermline_alignment)

        if self.clonerepertoire_id is not None and not isinstance(self.clonerepertoire_id, str):
            self.clonerepertoire_id = str(self.clonerepertoire_id)

        if self.clonedata_processing_id is not None and not isinstance(self.clonedata_processing_id, str):
            self.clonedata_processing_id = str(self.clonedata_processing_id)

        if not isinstance(self.clonesequences, list):
            self.clonesequences = [self.clonesequences] if self.clonesequences is not None else []
        self.clonesequences = [v if isinstance(v, str) else str(v) for v in self.clonesequences]

        if self.clonev_call is not None and not isinstance(self.clonev_call, str):
            self.clonev_call = str(self.clonev_call)

        if self.cloned_call is not None and not isinstance(self.cloned_call, str):
            self.cloned_call = str(self.cloned_call)

        if self.clonej_call is not None and not isinstance(self.clonej_call, str):
            self.clonej_call = str(self.clonej_call)

        if self.clonejunction is not None and not isinstance(self.clonejunction, str):
            self.clonejunction = str(self.clonejunction)

        if self.clonejunction_aa is not None and not isinstance(self.clonejunction_aa, str):
            self.clonejunction_aa = str(self.clonejunction_aa)

        if self.clonejunction_length is not None and not isinstance(self.clonejunction_length, int):
            self.clonejunction_length = int(self.clonejunction_length)

        if self.clonejunction_aa_length is not None and not isinstance(self.clonejunction_aa_length, int):
            self.clonejunction_aa_length = int(self.clonejunction_aa_length)

        if self.clonegermline_alignment_aa is not None and not isinstance(self.clonegermline_alignment_aa, str):
            self.clonegermline_alignment_aa = str(self.clonegermline_alignment_aa)

        if self.clonev_alignment_start is not None and not isinstance(self.clonev_alignment_start, int):
            self.clonev_alignment_start = int(self.clonev_alignment_start)

        if self.clonev_alignment_end is not None and not isinstance(self.clonev_alignment_end, int):
            self.clonev_alignment_end = int(self.clonev_alignment_end)

        if self.cloned_alignment_start is not None and not isinstance(self.cloned_alignment_start, int):
            self.cloned_alignment_start = int(self.cloned_alignment_start)

        if self.cloned_alignment_end is not None and not isinstance(self.cloned_alignment_end, int):
            self.cloned_alignment_end = int(self.cloned_alignment_end)

        if self.clonej_alignment_start is not None and not isinstance(self.clonej_alignment_start, int):
            self.clonej_alignment_start = int(self.clonej_alignment_start)

        if self.clonej_alignment_end is not None and not isinstance(self.clonej_alignment_end, int):
            self.clonej_alignment_end = int(self.clonej_alignment_end)

        if self.clonejunction_start is not None and not isinstance(self.clonejunction_start, int):
            self.clonejunction_start = int(self.clonejunction_start)

        if self.clonejunction_end is not None and not isinstance(self.clonejunction_end, int):
            self.clonejunction_end = int(self.clonejunction_end)

        if self.cloneumi_count is not None and not isinstance(self.cloneumi_count, int):
            self.cloneumi_count = int(self.cloneumi_count)

        if self.cloneclone_count is not None and not isinstance(self.cloneclone_count, int):
            self.cloneclone_count = int(self.cloneclone_count)

        if self.cloneseed_id is not None and not isinstance(self.cloneseed_id, str):
            self.cloneseed_id = str(self.cloneseed_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Tree(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Tree"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Tree"
    class_name: ClassVar[str] = "V1p4_Tree"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Tree

    treetree_id: str = None
    treeclone_id: str = None
    treenewick: str = None
    treenodes: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.treetree_id):
            self.MissingRequiredField("treetree_id")
        if not isinstance(self.treetree_id, str):
            self.treetree_id = str(self.treetree_id)

        if self._is_empty(self.treeclone_id):
            self.MissingRequiredField("treeclone_id")
        if not isinstance(self.treeclone_id, str):
            self.treeclone_id = str(self.treeclone_id)

        if self._is_empty(self.treenewick):
            self.MissingRequiredField("treenewick")
        if not isinstance(self.treenewick, str):
            self.treenewick = str(self.treenewick)

        if self.treenodes is not None and not isinstance(self.treenodes, str):
            self.treenodes = str(self.treenodes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Node(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Node"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Node"
    class_name: ClassVar[str] = "V1p4_Node"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Node

    nodesequence_id: str = None
    nodesequence_alignment: Optional[str] = None
    nodejunction: Optional[str] = None
    nodejunction_aa: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.nodesequence_id):
            self.MissingRequiredField("nodesequence_id")
        if not isinstance(self.nodesequence_id, str):
            self.nodesequence_id = str(self.nodesequence_id)

        if self.nodesequence_alignment is not None and not isinstance(self.nodesequence_alignment, str):
            self.nodesequence_alignment = str(self.nodesequence_alignment)

        if self.nodejunction is not None and not isinstance(self.nodejunction, str):
            self.nodejunction = str(self.nodejunction)

        if self.nodejunction_aa is not None and not isinstance(self.nodejunction_aa, str):
            self.nodejunction_aa = str(self.nodejunction_aa)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Cell(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Cell"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Cell"
    class_name: ClassVar[str] = "V1p4_Cell"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Cell

    cellcell_id: str = None
    cellrepertoire_id: str = None
    cellvirtual_pairing: Union[bool, Bool] = None
    celldata_processing_id: Optional[str] = None
    cellreceptors: Optional[Union[str, List[str]]] = empty_list()
    cellcell_subset: Optional[Union[str, "V1p4CellSubset"]] = None
    cellcell_phenotype: Optional[str] = None
    cellcell_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.cellcell_id):
            self.MissingRequiredField("cellcell_id")
        if not isinstance(self.cellcell_id, str):
            self.cellcell_id = str(self.cellcell_id)

        if self._is_empty(self.cellrepertoire_id):
            self.MissingRequiredField("cellrepertoire_id")
        if not isinstance(self.cellrepertoire_id, str):
            self.cellrepertoire_id = str(self.cellrepertoire_id)

        if self._is_empty(self.cellvirtual_pairing):
            self.MissingRequiredField("cellvirtual_pairing")
        if not isinstance(self.cellvirtual_pairing, Bool):
            self.cellvirtual_pairing = Bool(self.cellvirtual_pairing)

        if self.celldata_processing_id is not None and not isinstance(self.celldata_processing_id, str):
            self.celldata_processing_id = str(self.celldata_processing_id)

        if not isinstance(self.cellreceptors, list):
            self.cellreceptors = [self.cellreceptors] if self.cellreceptors is not None else []
        self.cellreceptors = [v if isinstance(v, str) else str(v) for v in self.cellreceptors]

        if self.cellcell_phenotype is not None and not isinstance(self.cellcell_phenotype, str):
            self.cellcell_phenotype = str(self.cellcell_phenotype)

        if self.cellcell_label is not None and not isinstance(self.cellcell_label, str):
            self.cellcell_label = str(self.cellcell_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Expression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Expression"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Expression"
    class_name: ClassVar[str] = "V1p4_Expression"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Expression

    expressionexpression_id: str = None
    expressioncell_id: str = None
    expressionrepertoire_id: str = None
    expressiondata_processing_id: str = None
    expressionproperty_type: str = None
    expressionproperty: Union[str, "V1p4Property"] = None
    expressionvalue: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.expressionexpression_id):
            self.MissingRequiredField("expressionexpression_id")
        if not isinstance(self.expressionexpression_id, str):
            self.expressionexpression_id = str(self.expressionexpression_id)

        if self._is_empty(self.expressioncell_id):
            self.MissingRequiredField("expressioncell_id")
        if not isinstance(self.expressioncell_id, str):
            self.expressioncell_id = str(self.expressioncell_id)

        if self._is_empty(self.expressionrepertoire_id):
            self.MissingRequiredField("expressionrepertoire_id")
        if not isinstance(self.expressionrepertoire_id, str):
            self.expressionrepertoire_id = str(self.expressionrepertoire_id)

        if self._is_empty(self.expressiondata_processing_id):
            self.MissingRequiredField("expressiondata_processing_id")
        if not isinstance(self.expressiondata_processing_id, str):
            self.expressiondata_processing_id = str(self.expressiondata_processing_id)

        if self._is_empty(self.expressionproperty_type):
            self.MissingRequiredField("expressionproperty_type")
        if not isinstance(self.expressionproperty_type, str):
            self.expressionproperty_type = str(self.expressionproperty_type)

        if self._is_empty(self.expressionvalue):
            self.MissingRequiredField("expressionvalue")
        if not isinstance(self.expressionvalue, float):
            self.expressionvalue = float(self.expressionvalue)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Receptor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Receptor"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Receptor"
    class_name: ClassVar[str] = "V1p4_Receptor"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Receptor

    receptorreceptor_id: str = None
    receptorreceptor_hash: str = None
    receptorreceptor_type: Union[str, "V1p4ReceptorType"] = None
    receptorreceptor_variable_domain_1_aa: str = None
    receptorreceptor_variable_domain_1_locus: Union[str, "V1p4ReceptorVariableDomain1Locus"] = None
    receptorreceptor_variable_domain_2_aa: str = None
    receptorreceptor_variable_domain_2_locus: Union[str, "V1p4ReceptorVariableDomain2Locus"] = None
    receptorreceptor_ref: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.receptorreceptor_id):
            self.MissingRequiredField("receptorreceptor_id")
        if not isinstance(self.receptorreceptor_id, str):
            self.receptorreceptor_id = str(self.receptorreceptor_id)

        if self._is_empty(self.receptorreceptor_hash):
            self.MissingRequiredField("receptorreceptor_hash")
        if not isinstance(self.receptorreceptor_hash, str):
            self.receptorreceptor_hash = str(self.receptorreceptor_hash)

        if self._is_empty(self.receptorreceptor_type):
            self.MissingRequiredField("receptorreceptor_type")
        if not isinstance(self.receptorreceptor_type, V1p4ReceptorType):
            self.receptorreceptor_type = V1p4ReceptorType(self.receptorreceptor_type)

        if self._is_empty(self.receptorreceptor_variable_domain_1_aa):
            self.MissingRequiredField("receptorreceptor_variable_domain_1_aa")
        if not isinstance(self.receptorreceptor_variable_domain_1_aa, str):
            self.receptorreceptor_variable_domain_1_aa = str(self.receptorreceptor_variable_domain_1_aa)

        if self._is_empty(self.receptorreceptor_variable_domain_1_locus):
            self.MissingRequiredField("receptorreceptor_variable_domain_1_locus")
        if not isinstance(self.receptorreceptor_variable_domain_1_locus, V1p4ReceptorVariableDomain1Locus):
            self.receptorreceptor_variable_domain_1_locus = V1p4ReceptorVariableDomain1Locus(self.receptorreceptor_variable_domain_1_locus)

        if self._is_empty(self.receptorreceptor_variable_domain_2_aa):
            self.MissingRequiredField("receptorreceptor_variable_domain_2_aa")
        if not isinstance(self.receptorreceptor_variable_domain_2_aa, str):
            self.receptorreceptor_variable_domain_2_aa = str(self.receptorreceptor_variable_domain_2_aa)

        if self._is_empty(self.receptorreceptor_variable_domain_2_locus):
            self.MissingRequiredField("receptorreceptor_variable_domain_2_locus")
        if not isinstance(self.receptorreceptor_variable_domain_2_locus, V1p4ReceptorVariableDomain2Locus):
            self.receptorreceptor_variable_domain_2_locus = V1p4ReceptorVariableDomain2Locus(self.receptorreceptor_variable_domain_2_locus)

        if not isinstance(self.receptorreceptor_ref, list):
            self.receptorreceptor_ref = [self.receptorreceptor_ref] if self.receptorreceptor_ref is not None else []
        self.receptorreceptor_ref = [v if isinstance(v, str) else str(v) for v in self.receptorreceptor_ref]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Reactivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Reactivity"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Reactivity"
    class_name: ClassVar[str] = "V1p4_Reactivity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Reactivity

    reactivityreactivity_id: str = None
    reactivitycell_id: str = None
    reactivityligand_type: Union[str, "V1p4LigandType"] = None
    reactivityantigen_type: Union[str, "V1p4AntigenType"] = None
    reactivityantigen: Union[str, "V1p4Antigen"] = None
    reactivityreactivity_method: str = None
    reactivityreactivity_readout: str = None
    reactivityreactivity_value: float = None
    reactivityreactivity_unit: str = None
    reactivityrepertoire_id: Optional[str] = None
    reactivitydata_processing_id: Optional[str] = None
    reactivityantigen_source_species: Optional[Union[str, "V1p4AntigenSourceSpecies"]] = None
    reactivitypeptide_start: Optional[int] = None
    reactivitypeptide_end: Optional[int] = None
    reactivitypeptide_sequence_aa: Optional[str] = None
    reactivitymhc_class: Optional[Union[str, "V1p4MhcClass"]] = None
    reactivitymhc_gene_1: Optional[Union[str, "V1p4MhcGene1"]] = None
    reactivitymhc_allele_1: Optional[str] = None
    reactivitymhc_gene_2: Optional[Union[str, "V1p4MhcGene2"]] = None
    reactivitymhc_allele_2: Optional[str] = None
    reactivityreactivity_ref: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.reactivityreactivity_id):
            self.MissingRequiredField("reactivityreactivity_id")
        if not isinstance(self.reactivityreactivity_id, str):
            self.reactivityreactivity_id = str(self.reactivityreactivity_id)

        if self._is_empty(self.reactivitycell_id):
            self.MissingRequiredField("reactivitycell_id")
        if not isinstance(self.reactivitycell_id, str):
            self.reactivitycell_id = str(self.reactivitycell_id)

        if self._is_empty(self.reactivityligand_type):
            self.MissingRequiredField("reactivityligand_type")
        if not isinstance(self.reactivityligand_type, V1p4LigandType):
            self.reactivityligand_type = V1p4LigandType(self.reactivityligand_type)

        if self._is_empty(self.reactivityantigen_type):
            self.MissingRequiredField("reactivityantigen_type")
        if not isinstance(self.reactivityantigen_type, V1p4AntigenType):
            self.reactivityantigen_type = V1p4AntigenType(self.reactivityantigen_type)

        if self._is_empty(self.reactivityreactivity_method):
            self.MissingRequiredField("reactivityreactivity_method")
        if not isinstance(self.reactivityreactivity_method, str):
            self.reactivityreactivity_method = str(self.reactivityreactivity_method)

        if self._is_empty(self.reactivityreactivity_readout):
            self.MissingRequiredField("reactivityreactivity_readout")
        if not isinstance(self.reactivityreactivity_readout, str):
            self.reactivityreactivity_readout = str(self.reactivityreactivity_readout)

        if self._is_empty(self.reactivityreactivity_value):
            self.MissingRequiredField("reactivityreactivity_value")
        if not isinstance(self.reactivityreactivity_value, float):
            self.reactivityreactivity_value = float(self.reactivityreactivity_value)

        if self._is_empty(self.reactivityreactivity_unit):
            self.MissingRequiredField("reactivityreactivity_unit")
        if not isinstance(self.reactivityreactivity_unit, str):
            self.reactivityreactivity_unit = str(self.reactivityreactivity_unit)

        if self.reactivityrepertoire_id is not None and not isinstance(self.reactivityrepertoire_id, str):
            self.reactivityrepertoire_id = str(self.reactivityrepertoire_id)

        if self.reactivitydata_processing_id is not None and not isinstance(self.reactivitydata_processing_id, str):
            self.reactivitydata_processing_id = str(self.reactivitydata_processing_id)

        if self.reactivitypeptide_start is not None and not isinstance(self.reactivitypeptide_start, int):
            self.reactivitypeptide_start = int(self.reactivitypeptide_start)

        if self.reactivitypeptide_end is not None and not isinstance(self.reactivitypeptide_end, int):
            self.reactivitypeptide_end = int(self.reactivitypeptide_end)

        if self.reactivitypeptide_sequence_aa is not None and not isinstance(self.reactivitypeptide_sequence_aa, str):
            self.reactivitypeptide_sequence_aa = str(self.reactivitypeptide_sequence_aa)

        if self.reactivitymhc_class is not None and not isinstance(self.reactivitymhc_class, V1p4MhcClass):
            self.reactivitymhc_class = V1p4MhcClass(self.reactivitymhc_class)

        if self.reactivitymhc_allele_1 is not None and not isinstance(self.reactivitymhc_allele_1, str):
            self.reactivitymhc_allele_1 = str(self.reactivitymhc_allele_1)

        if self.reactivitymhc_allele_2 is not None and not isinstance(self.reactivitymhc_allele_2, str):
            self.reactivitymhc_allele_2 = str(self.reactivitymhc_allele_2)

        if not isinstance(self.reactivityreactivity_ref, list):
            self.reactivityreactivity_ref = [self.reactivityreactivity_ref] if self.reactivityreactivity_ref is not None else []
        self.reactivityreactivity_ref = [v if isinstance(v, str) else str(v) for v in self.reactivityreactivity_ref]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SampleProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SampleProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SampleProcessing"
    class_name: ClassVar[str] = "V1p4_SampleProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SampleProcessing

    sequencing_runsequencing_run_id: str = None
    sequencing_runtotal_reads_passing_qc_filter: int = None
    sequencing_runsequencing_platform: str = None
    sequencing_runsequencing_facility: str = None
    sequencing_runsequencing_run_date: str = None
    sequencing_runsequencing_kit: str = None
    sequencing_runsequencing_files: Optional[Union[dict, V1p4SequencingData]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sequencing_runsequencing_run_id):
            self.MissingRequiredField("sequencing_runsequencing_run_id")
        if not isinstance(self.sequencing_runsequencing_run_id, str):
            self.sequencing_runsequencing_run_id = str(self.sequencing_runsequencing_run_id)

        if self._is_empty(self.sequencing_runtotal_reads_passing_qc_filter):
            self.MissingRequiredField("sequencing_runtotal_reads_passing_qc_filter")
        if not isinstance(self.sequencing_runtotal_reads_passing_qc_filter, int):
            self.sequencing_runtotal_reads_passing_qc_filter = int(self.sequencing_runtotal_reads_passing_qc_filter)

        if self._is_empty(self.sequencing_runsequencing_platform):
            self.MissingRequiredField("sequencing_runsequencing_platform")
        if not isinstance(self.sequencing_runsequencing_platform, str):
            self.sequencing_runsequencing_platform = str(self.sequencing_runsequencing_platform)

        if self._is_empty(self.sequencing_runsequencing_facility):
            self.MissingRequiredField("sequencing_runsequencing_facility")
        if not isinstance(self.sequencing_runsequencing_facility, str):
            self.sequencing_runsequencing_facility = str(self.sequencing_runsequencing_facility)

        if self._is_empty(self.sequencing_runsequencing_run_date):
            self.MissingRequiredField("sequencing_runsequencing_run_date")
        if not isinstance(self.sequencing_runsequencing_run_date, str):
            self.sequencing_runsequencing_run_date = str(self.sequencing_runsequencing_run_date)

        if self._is_empty(self.sequencing_runsequencing_kit):
            self.MissingRequiredField("sequencing_runsequencing_kit")
        if not isinstance(self.sequencing_runsequencing_kit, str):
            self.sequencing_runsequencing_kit = str(self.sequencing_runsequencing_kit)

        if self.sequencing_runsequencing_files is not None and not isinstance(self.sequencing_runsequencing_files, V1p4SequencingData):
            self.sequencing_runsequencing_files = V1p4SequencingData(**as_dict(self.sequencing_runsequencing_files))

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
    null = PermissibleValue(text="null")

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

    null = PermissibleValue(text="null")

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
    TRD = PermissibleValue(text="TRD")
    TRG = PermissibleValue(text="TRG")
    null = PermissibleValue(text="null")

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
    null = PermissibleValue(text="null")

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
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="V1p4SpeciesSubgroupType",
    )

class V1p4Status(EnumDefinitionImpl):

    active = PermissibleValue(text="active")
    draft = PermissibleValue(text="draft")
    retired = PermissibleValue(text="retired")
    withdrawn = PermissibleValue(text="withdrawn")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="V1p4Status",
    )

class V1p4JCodonFrame(EnumDefinitionImpl):

    null = PermissibleValue(text="null")

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
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="V1p4InferenceProcess",
    )

class V1p4MhcClass(EnumDefinitionImpl):

    null = PermissibleValue(text="null")

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
    null = PermissibleValue(text="null")

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
    null = PermissibleValue(text="null")

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
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="V1p4FileType",
    )

class V1p4ReadDirection(EnumDefinitionImpl):

    forward = PermissibleValue(text="forward")
    reverse = PermissibleValue(text="reverse")
    mixed = PermissibleValue(text="mixed")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="V1p4ReadDirection",
    )

class V1p4PairedReadDirection(EnumDefinitionImpl):

    forward = PermissibleValue(text="forward")
    reverse = PermissibleValue(text="reverse")
    mixed = PermissibleValue(text="mixed")
    null = PermissibleValue(text="null")

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

slots.type = Slot(uri=AK_SCHEMA.type, name="type", curie=AK_SCHEMA.curie('type'),
                   model_uri=AK_SCHEMA.type, domain=None, range=Optional[str])

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

slots.source_protein = Slot(uri=AK_SCHEMA.source_protein, name="source_protein", curie=AK_SCHEMA.curie('source_protein'),
                   model_uri=AK_SCHEMA.source_protein, domain=None, range=Optional[str])

slots.source_organism = Slot(uri=AK_SCHEMA.source_organism, name="source_organism", curie=AK_SCHEMA.curie('source_organism'),
                   model_uri=AK_SCHEMA.source_organism, domain=None, range=Optional[str])

slots.time_pointlabel = Slot(uri=AK_SCHEMA.time_pointlabel, name="time_pointlabel", curie=AK_SCHEMA.curie('time_pointlabel'),
                   model_uri=AK_SCHEMA.time_pointlabel, domain=None, range=Optional[str])

slots.time_pointvalue = Slot(uri=AK_SCHEMA.time_pointvalue, name="time_pointvalue", curie=AK_SCHEMA.curie('time_pointvalue'),
                   model_uri=AK_SCHEMA.time_pointvalue, domain=None, range=Optional[float])

slots.time_pointunit = Slot(uri=AK_SCHEMA.time_pointunit, name="time_pointunit", curie=AK_SCHEMA.curie('time_pointunit'),
                   model_uri=AK_SCHEMA.time_pointunit, domain=None, range=Optional[Union[str, "V1p4Unit"]])

slots.time_intervalmin = Slot(uri=AK_SCHEMA.time_intervalmin, name="time_intervalmin", curie=AK_SCHEMA.curie('time_intervalmin'),
                   model_uri=AK_SCHEMA.time_intervalmin, domain=None, range=Optional[float])

slots.time_intervalmax = Slot(uri=AK_SCHEMA.time_intervalmax, name="time_intervalmax", curie=AK_SCHEMA.curie('time_intervalmax'),
                   model_uri=AK_SCHEMA.time_intervalmax, domain=None, range=Optional[float])

slots.time_intervalunit = Slot(uri=AK_SCHEMA.time_intervalunit, name="time_intervalunit", curie=AK_SCHEMA.curie('time_intervalunit'),
                   model_uri=AK_SCHEMA.time_intervalunit, domain=None, range=Optional[Union[str, "V1p4Unit"]])

slots.physical_quantityquantity = Slot(uri=AK_SCHEMA.physical_quantityquantity, name="physical_quantityquantity", curie=AK_SCHEMA.curie('physical_quantityquantity'),
                   model_uri=AK_SCHEMA.physical_quantityquantity, domain=None, range=Optional[float])

slots.physical_quantityunit = Slot(uri=AK_SCHEMA.physical_quantityunit, name="physical_quantityunit", curie=AK_SCHEMA.curie('physical_quantityunit'),
                   model_uri=AK_SCHEMA.physical_quantityunit, domain=None, range=Optional[Union[str, "V1p4Unit"]])

slots.time_quantityquantity = Slot(uri=AK_SCHEMA.time_quantityquantity, name="time_quantityquantity", curie=AK_SCHEMA.curie('time_quantityquantity'),
                   model_uri=AK_SCHEMA.time_quantityquantity, domain=None, range=Optional[float])

slots.time_quantityunit = Slot(uri=AK_SCHEMA.time_quantityunit, name="time_quantityunit", curie=AK_SCHEMA.curie('time_quantityunit'),
                   model_uri=AK_SCHEMA.time_quantityunit, domain=None, range=Optional[Union[str, "V1p4Unit"]])

slots.contributorcontributor_id = Slot(uri=AK_SCHEMA.contributorcontributor_id, name="contributorcontributor_id", curie=AK_SCHEMA.curie('contributorcontributor_id'),
                   model_uri=AK_SCHEMA.contributorcontributor_id, domain=None, range=str)

slots.contributorname = Slot(uri=AK_SCHEMA.contributorname, name="contributorname", curie=AK_SCHEMA.curie('contributorname'),
                   model_uri=AK_SCHEMA.contributorname, domain=None, range=str)

slots.contributororcid_id = Slot(uri=AK_SCHEMA.contributororcid_id, name="contributororcid_id", curie=AK_SCHEMA.curie('contributororcid_id'),
                   model_uri=AK_SCHEMA.contributororcid_id, domain=None, range=Optional[Union[str, "V1p4OrcidId"]])

slots.contributoraffiliation = Slot(uri=AK_SCHEMA.contributoraffiliation, name="contributoraffiliation", curie=AK_SCHEMA.curie('contributoraffiliation'),
                   model_uri=AK_SCHEMA.contributoraffiliation, domain=None, range=Optional[Union[str, "V1p4Affiliation"]])

slots.contributoraffiliation_department = Slot(uri=AK_SCHEMA.contributoraffiliation_department, name="contributoraffiliation_department", curie=AK_SCHEMA.curie('contributoraffiliation_department'),
                   model_uri=AK_SCHEMA.contributoraffiliation_department, domain=None, range=Optional[str])

slots.contributorcontributions = Slot(uri=AK_SCHEMA.contributorcontributions, name="contributorcontributions", curie=AK_SCHEMA.curie('contributorcontributions'),
                   model_uri=AK_SCHEMA.contributorcontributions, domain=None, range=Optional[Union[Union[dict, V1p4ContributorContribution], List[Union[dict, V1p4ContributorContribution]]]])

slots.contributor_contributionrole = Slot(uri=AK_SCHEMA.contributor_contributionrole, name="contributor_contributionrole", curie=AK_SCHEMA.curie('contributor_contributionrole'),
                   model_uri=AK_SCHEMA.contributor_contributionrole, domain=None, range=Union[str, "V1p4Role"])

slots.contributor_contributiondegree = Slot(uri=AK_SCHEMA.contributor_contributiondegree, name="contributor_contributiondegree", curie=AK_SCHEMA.curie('contributor_contributiondegree'),
                   model_uri=AK_SCHEMA.contributor_contributiondegree, domain=None, range=Optional[Union[str, "V1p4Degree"]])

slots.rearranged_sequencesequence_id = Slot(uri=AK_SCHEMA.rearranged_sequencesequence_id, name="rearranged_sequencesequence_id", curie=AK_SCHEMA.curie('rearranged_sequencesequence_id'),
                   model_uri=AK_SCHEMA.rearranged_sequencesequence_id, domain=None, range=str)

slots.rearranged_sequencesequence = Slot(uri=AK_SCHEMA.rearranged_sequencesequence, name="rearranged_sequencesequence", curie=AK_SCHEMA.curie('rearranged_sequencesequence'),
                   model_uri=AK_SCHEMA.rearranged_sequencesequence, domain=None, range=str)

slots.rearranged_sequencederivation = Slot(uri=AK_SCHEMA.rearranged_sequencederivation, name="rearranged_sequencederivation", curie=AK_SCHEMA.curie('rearranged_sequencederivation'),
                   model_uri=AK_SCHEMA.rearranged_sequencederivation, domain=None, range=Union[str, "V1p4Derivation"])

slots.rearranged_sequenceobservation_type = Slot(uri=AK_SCHEMA.rearranged_sequenceobservation_type, name="rearranged_sequenceobservation_type", curie=AK_SCHEMA.curie('rearranged_sequenceobservation_type'),
                   model_uri=AK_SCHEMA.rearranged_sequenceobservation_type, domain=None, range=Union[str, "V1p4ObservationType"])

slots.rearranged_sequencecuration = Slot(uri=AK_SCHEMA.rearranged_sequencecuration, name="rearranged_sequencecuration", curie=AK_SCHEMA.curie('rearranged_sequencecuration'),
                   model_uri=AK_SCHEMA.rearranged_sequencecuration, domain=None, range=Optional[str])

slots.rearranged_sequencerepository_name = Slot(uri=AK_SCHEMA.rearranged_sequencerepository_name, name="rearranged_sequencerepository_name", curie=AK_SCHEMA.curie('rearranged_sequencerepository_name'),
                   model_uri=AK_SCHEMA.rearranged_sequencerepository_name, domain=None, range=str)

slots.rearranged_sequencerepository_ref = Slot(uri=AK_SCHEMA.rearranged_sequencerepository_ref, name="rearranged_sequencerepository_ref", curie=AK_SCHEMA.curie('rearranged_sequencerepository_ref'),
                   model_uri=AK_SCHEMA.rearranged_sequencerepository_ref, domain=None, range=Optional[str])

slots.rearranged_sequencedeposited_version = Slot(uri=AK_SCHEMA.rearranged_sequencedeposited_version, name="rearranged_sequencedeposited_version", curie=AK_SCHEMA.curie('rearranged_sequencedeposited_version'),
                   model_uri=AK_SCHEMA.rearranged_sequencedeposited_version, domain=None, range=str)

slots.rearranged_sequencesequence_start = Slot(uri=AK_SCHEMA.rearranged_sequencesequence_start, name="rearranged_sequencesequence_start", curie=AK_SCHEMA.curie('rearranged_sequencesequence_start'),
                   model_uri=AK_SCHEMA.rearranged_sequencesequence_start, domain=None, range=Optional[int])

slots.rearranged_sequencesequence_end = Slot(uri=AK_SCHEMA.rearranged_sequencesequence_end, name="rearranged_sequencesequence_end", curie=AK_SCHEMA.curie('rearranged_sequencesequence_end'),
                   model_uri=AK_SCHEMA.rearranged_sequencesequence_end, domain=None, range=Optional[int])

slots.unrearranged_sequencesequence_id = Slot(uri=AK_SCHEMA.unrearranged_sequencesequence_id, name="unrearranged_sequencesequence_id", curie=AK_SCHEMA.curie('unrearranged_sequencesequence_id'),
                   model_uri=AK_SCHEMA.unrearranged_sequencesequence_id, domain=None, range=str)

slots.unrearranged_sequencesequence = Slot(uri=AK_SCHEMA.unrearranged_sequencesequence, name="unrearranged_sequencesequence", curie=AK_SCHEMA.curie('unrearranged_sequencesequence'),
                   model_uri=AK_SCHEMA.unrearranged_sequencesequence, domain=None, range=str)

slots.unrearranged_sequencecuration = Slot(uri=AK_SCHEMA.unrearranged_sequencecuration, name="unrearranged_sequencecuration", curie=AK_SCHEMA.curie('unrearranged_sequencecuration'),
                   model_uri=AK_SCHEMA.unrearranged_sequencecuration, domain=None, range=Optional[str])

slots.unrearranged_sequencerepository_name = Slot(uri=AK_SCHEMA.unrearranged_sequencerepository_name, name="unrearranged_sequencerepository_name", curie=AK_SCHEMA.curie('unrearranged_sequencerepository_name'),
                   model_uri=AK_SCHEMA.unrearranged_sequencerepository_name, domain=None, range=str)

slots.unrearranged_sequencerepository_ref = Slot(uri=AK_SCHEMA.unrearranged_sequencerepository_ref, name="unrearranged_sequencerepository_ref", curie=AK_SCHEMA.curie('unrearranged_sequencerepository_ref'),
                   model_uri=AK_SCHEMA.unrearranged_sequencerepository_ref, domain=None, range=Optional[str])

slots.unrearranged_sequencepatch_no = Slot(uri=AK_SCHEMA.unrearranged_sequencepatch_no, name="unrearranged_sequencepatch_no", curie=AK_SCHEMA.curie('unrearranged_sequencepatch_no'),
                   model_uri=AK_SCHEMA.unrearranged_sequencepatch_no, domain=None, range=Optional[str])

slots.unrearranged_sequencegff_seqid = Slot(uri=AK_SCHEMA.unrearranged_sequencegff_seqid, name="unrearranged_sequencegff_seqid", curie=AK_SCHEMA.curie('unrearranged_sequencegff_seqid'),
                   model_uri=AK_SCHEMA.unrearranged_sequencegff_seqid, domain=None, range=str)

slots.unrearranged_sequencegff_start = Slot(uri=AK_SCHEMA.unrearranged_sequencegff_start, name="unrearranged_sequencegff_start", curie=AK_SCHEMA.curie('unrearranged_sequencegff_start'),
                   model_uri=AK_SCHEMA.unrearranged_sequencegff_start, domain=None, range=int)

slots.unrearranged_sequencegff_end = Slot(uri=AK_SCHEMA.unrearranged_sequencegff_end, name="unrearranged_sequencegff_end", curie=AK_SCHEMA.curie('unrearranged_sequencegff_end'),
                   model_uri=AK_SCHEMA.unrearranged_sequencegff_end, domain=None, range=int)

slots.unrearranged_sequencestrand = Slot(uri=AK_SCHEMA.unrearranged_sequencestrand, name="unrearranged_sequencestrand", curie=AK_SCHEMA.curie('unrearranged_sequencestrand'),
                   model_uri=AK_SCHEMA.unrearranged_sequencestrand, domain=None, range=Union[str, "V1p4Strand"])

slots.sequence_delineation_vsequence_delineation_id = Slot(uri=AK_SCHEMA.sequence_delineation_vsequence_delineation_id, name="sequence_delineation_vsequence_delineation_id", curie=AK_SCHEMA.curie('sequence_delineation_vsequence_delineation_id'),
                   model_uri=AK_SCHEMA.sequence_delineation_vsequence_delineation_id, domain=None, range=str)

slots.sequence_delineation_vdelineation_scheme = Slot(uri=AK_SCHEMA.sequence_delineation_vdelineation_scheme, name="sequence_delineation_vdelineation_scheme", curie=AK_SCHEMA.curie('sequence_delineation_vdelineation_scheme'),
                   model_uri=AK_SCHEMA.sequence_delineation_vdelineation_scheme, domain=None, range=str)

slots.sequence_delineation_vunaligned_sequence = Slot(uri=AK_SCHEMA.sequence_delineation_vunaligned_sequence, name="sequence_delineation_vunaligned_sequence", curie=AK_SCHEMA.curie('sequence_delineation_vunaligned_sequence'),
                   model_uri=AK_SCHEMA.sequence_delineation_vunaligned_sequence, domain=None, range=Optional[str])

slots.sequence_delineation_valigned_sequence = Slot(uri=AK_SCHEMA.sequence_delineation_valigned_sequence, name="sequence_delineation_valigned_sequence", curie=AK_SCHEMA.curie('sequence_delineation_valigned_sequence'),
                   model_uri=AK_SCHEMA.sequence_delineation_valigned_sequence, domain=None, range=Optional[str])

slots.sequence_delineation_vfwr1_start = Slot(uri=AK_SCHEMA.sequence_delineation_vfwr1_start, name="sequence_delineation_vfwr1_start", curie=AK_SCHEMA.curie('sequence_delineation_vfwr1_start'),
                   model_uri=AK_SCHEMA.sequence_delineation_vfwr1_start, domain=None, range=int)

slots.sequence_delineation_vfwr1_end = Slot(uri=AK_SCHEMA.sequence_delineation_vfwr1_end, name="sequence_delineation_vfwr1_end", curie=AK_SCHEMA.curie('sequence_delineation_vfwr1_end'),
                   model_uri=AK_SCHEMA.sequence_delineation_vfwr1_end, domain=None, range=int)

slots.sequence_delineation_vcdr1_start = Slot(uri=AK_SCHEMA.sequence_delineation_vcdr1_start, name="sequence_delineation_vcdr1_start", curie=AK_SCHEMA.curie('sequence_delineation_vcdr1_start'),
                   model_uri=AK_SCHEMA.sequence_delineation_vcdr1_start, domain=None, range=int)

slots.sequence_delineation_vcdr1_end = Slot(uri=AK_SCHEMA.sequence_delineation_vcdr1_end, name="sequence_delineation_vcdr1_end", curie=AK_SCHEMA.curie('sequence_delineation_vcdr1_end'),
                   model_uri=AK_SCHEMA.sequence_delineation_vcdr1_end, domain=None, range=int)

slots.sequence_delineation_vfwr2_start = Slot(uri=AK_SCHEMA.sequence_delineation_vfwr2_start, name="sequence_delineation_vfwr2_start", curie=AK_SCHEMA.curie('sequence_delineation_vfwr2_start'),
                   model_uri=AK_SCHEMA.sequence_delineation_vfwr2_start, domain=None, range=int)

slots.sequence_delineation_vfwr2_end = Slot(uri=AK_SCHEMA.sequence_delineation_vfwr2_end, name="sequence_delineation_vfwr2_end", curie=AK_SCHEMA.curie('sequence_delineation_vfwr2_end'),
                   model_uri=AK_SCHEMA.sequence_delineation_vfwr2_end, domain=None, range=int)

slots.sequence_delineation_vcdr2_start = Slot(uri=AK_SCHEMA.sequence_delineation_vcdr2_start, name="sequence_delineation_vcdr2_start", curie=AK_SCHEMA.curie('sequence_delineation_vcdr2_start'),
                   model_uri=AK_SCHEMA.sequence_delineation_vcdr2_start, domain=None, range=int)

slots.sequence_delineation_vcdr2_end = Slot(uri=AK_SCHEMA.sequence_delineation_vcdr2_end, name="sequence_delineation_vcdr2_end", curie=AK_SCHEMA.curie('sequence_delineation_vcdr2_end'),
                   model_uri=AK_SCHEMA.sequence_delineation_vcdr2_end, domain=None, range=int)

slots.sequence_delineation_vfwr3_start = Slot(uri=AK_SCHEMA.sequence_delineation_vfwr3_start, name="sequence_delineation_vfwr3_start", curie=AK_SCHEMA.curie('sequence_delineation_vfwr3_start'),
                   model_uri=AK_SCHEMA.sequence_delineation_vfwr3_start, domain=None, range=int)

slots.sequence_delineation_vfwr3_end = Slot(uri=AK_SCHEMA.sequence_delineation_vfwr3_end, name="sequence_delineation_vfwr3_end", curie=AK_SCHEMA.curie('sequence_delineation_vfwr3_end'),
                   model_uri=AK_SCHEMA.sequence_delineation_vfwr3_end, domain=None, range=int)

slots.sequence_delineation_vcdr3_start = Slot(uri=AK_SCHEMA.sequence_delineation_vcdr3_start, name="sequence_delineation_vcdr3_start", curie=AK_SCHEMA.curie('sequence_delineation_vcdr3_start'),
                   model_uri=AK_SCHEMA.sequence_delineation_vcdr3_start, domain=None, range=int)

slots.sequence_delineation_valignment_labels = Slot(uri=AK_SCHEMA.sequence_delineation_valignment_labels, name="sequence_delineation_valignment_labels", curie=AK_SCHEMA.curie('sequence_delineation_valignment_labels'),
                   model_uri=AK_SCHEMA.sequence_delineation_valignment_labels, domain=None, range=Optional[Union[str, List[str]]])

slots.allele_descriptionallele_description_id = Slot(uri=AK_SCHEMA.allele_descriptionallele_description_id, name="allele_descriptionallele_description_id", curie=AK_SCHEMA.curie('allele_descriptionallele_description_id'),
                   model_uri=AK_SCHEMA.allele_descriptionallele_description_id, domain=None, range=str)

slots.allele_descriptionallele_description_ref = Slot(uri=AK_SCHEMA.allele_descriptionallele_description_ref, name="allele_descriptionallele_description_ref", curie=AK_SCHEMA.curie('allele_descriptionallele_description_ref'),
                   model_uri=AK_SCHEMA.allele_descriptionallele_description_ref, domain=None, range=Optional[str])

slots.allele_descriptionacknowledgements = Slot(uri=AK_SCHEMA.allele_descriptionacknowledgements, name="allele_descriptionacknowledgements", curie=AK_SCHEMA.curie('allele_descriptionacknowledgements'),
                   model_uri=AK_SCHEMA.allele_descriptionacknowledgements, domain=None, range=Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]])

slots.allele_descriptionrelease_version = Slot(uri=AK_SCHEMA.allele_descriptionrelease_version, name="allele_descriptionrelease_version", curie=AK_SCHEMA.curie('allele_descriptionrelease_version'),
                   model_uri=AK_SCHEMA.allele_descriptionrelease_version, domain=None, range=int)

slots.allele_descriptionrelease_date = Slot(uri=AK_SCHEMA.allele_descriptionrelease_date, name="allele_descriptionrelease_date", curie=AK_SCHEMA.curie('allele_descriptionrelease_date'),
                   model_uri=AK_SCHEMA.allele_descriptionrelease_date, domain=None, range=str)

slots.allele_descriptionrelease_description = Slot(uri=AK_SCHEMA.allele_descriptionrelease_description, name="allele_descriptionrelease_description", curie=AK_SCHEMA.curie('allele_descriptionrelease_description'),
                   model_uri=AK_SCHEMA.allele_descriptionrelease_description, domain=None, range=str)

slots.allele_descriptionlabel = Slot(uri=AK_SCHEMA.allele_descriptionlabel, name="allele_descriptionlabel", curie=AK_SCHEMA.curie('allele_descriptionlabel'),
                   model_uri=AK_SCHEMA.allele_descriptionlabel, domain=None, range=Optional[str])

slots.allele_descriptionsequence = Slot(uri=AK_SCHEMA.allele_descriptionsequence, name="allele_descriptionsequence", curie=AK_SCHEMA.curie('allele_descriptionsequence'),
                   model_uri=AK_SCHEMA.allele_descriptionsequence, domain=None, range=str)

slots.allele_descriptioncoding_sequence = Slot(uri=AK_SCHEMA.allele_descriptioncoding_sequence, name="allele_descriptioncoding_sequence", curie=AK_SCHEMA.curie('allele_descriptioncoding_sequence'),
                   model_uri=AK_SCHEMA.allele_descriptioncoding_sequence, domain=None, range=str)

slots.allele_descriptionaliases = Slot(uri=AK_SCHEMA.allele_descriptionaliases, name="allele_descriptionaliases", curie=AK_SCHEMA.curie('allele_descriptionaliases'),
                   model_uri=AK_SCHEMA.allele_descriptionaliases, domain=None, range=Optional[Union[str, List[str]]])

slots.allele_descriptionlocus = Slot(uri=AK_SCHEMA.allele_descriptionlocus, name="allele_descriptionlocus", curie=AK_SCHEMA.curie('allele_descriptionlocus'),
                   model_uri=AK_SCHEMA.allele_descriptionlocus, domain=None, range=Union[str, "V1p4Locus"])

slots.allele_descriptionchromosome = Slot(uri=AK_SCHEMA.allele_descriptionchromosome, name="allele_descriptionchromosome", curie=AK_SCHEMA.curie('allele_descriptionchromosome'),
                   model_uri=AK_SCHEMA.allele_descriptionchromosome, domain=None, range=Optional[int])

slots.allele_descriptionsequence_type = Slot(uri=AK_SCHEMA.allele_descriptionsequence_type, name="allele_descriptionsequence_type", curie=AK_SCHEMA.curie('allele_descriptionsequence_type'),
                   model_uri=AK_SCHEMA.allele_descriptionsequence_type, domain=None, range=Union[str, "V1p4SequenceType"])

slots.allele_descriptionfunctional = Slot(uri=AK_SCHEMA.allele_descriptionfunctional, name="allele_descriptionfunctional", curie=AK_SCHEMA.curie('allele_descriptionfunctional'),
                   model_uri=AK_SCHEMA.allele_descriptionfunctional, domain=None, range=Union[bool, Bool])

slots.allele_descriptioninference_type = Slot(uri=AK_SCHEMA.allele_descriptioninference_type, name="allele_descriptioninference_type", curie=AK_SCHEMA.curie('allele_descriptioninference_type'),
                   model_uri=AK_SCHEMA.allele_descriptioninference_type, domain=None, range=Union[str, "V1p4InferenceType"])

slots.allele_descriptionspecies = Slot(uri=AK_SCHEMA.allele_descriptionspecies, name="allele_descriptionspecies", curie=AK_SCHEMA.curie('allele_descriptionspecies'),
                   model_uri=AK_SCHEMA.allele_descriptionspecies, domain=None, range=Union[str, "V1p4Species"])

slots.allele_descriptionspecies_subgroup = Slot(uri=AK_SCHEMA.allele_descriptionspecies_subgroup, name="allele_descriptionspecies_subgroup", curie=AK_SCHEMA.curie('allele_descriptionspecies_subgroup'),
                   model_uri=AK_SCHEMA.allele_descriptionspecies_subgroup, domain=None, range=Optional[str])

slots.allele_descriptionspecies_subgroup_type = Slot(uri=AK_SCHEMA.allele_descriptionspecies_subgroup_type, name="allele_descriptionspecies_subgroup_type", curie=AK_SCHEMA.curie('allele_descriptionspecies_subgroup_type'),
                   model_uri=AK_SCHEMA.allele_descriptionspecies_subgroup_type, domain=None, range=Optional[Union[str, "V1p4SpeciesSubgroupType"]])

slots.allele_descriptionstatus = Slot(uri=AK_SCHEMA.allele_descriptionstatus, name="allele_descriptionstatus", curie=AK_SCHEMA.curie('allele_descriptionstatus'),
                   model_uri=AK_SCHEMA.allele_descriptionstatus, domain=None, range=Optional[Union[str, "V1p4Status"]])

slots.allele_descriptionsubgroup_designation = Slot(uri=AK_SCHEMA.allele_descriptionsubgroup_designation, name="allele_descriptionsubgroup_designation", curie=AK_SCHEMA.curie('allele_descriptionsubgroup_designation'),
                   model_uri=AK_SCHEMA.allele_descriptionsubgroup_designation, domain=None, range=Optional[str])

slots.allele_descriptiongene_designation = Slot(uri=AK_SCHEMA.allele_descriptiongene_designation, name="allele_descriptiongene_designation", curie=AK_SCHEMA.curie('allele_descriptiongene_designation'),
                   model_uri=AK_SCHEMA.allele_descriptiongene_designation, domain=None, range=Optional[str])

slots.allele_descriptionallele_designation = Slot(uri=AK_SCHEMA.allele_descriptionallele_designation, name="allele_descriptionallele_designation", curie=AK_SCHEMA.curie('allele_descriptionallele_designation'),
                   model_uri=AK_SCHEMA.allele_descriptionallele_designation, domain=None, range=Optional[str])

slots.allele_descriptionallele_similarity_cluster_designation = Slot(uri=AK_SCHEMA.allele_descriptionallele_similarity_cluster_designation, name="allele_descriptionallele_similarity_cluster_designation", curie=AK_SCHEMA.curie('allele_descriptionallele_similarity_cluster_designation'),
                   model_uri=AK_SCHEMA.allele_descriptionallele_similarity_cluster_designation, domain=None, range=Optional[str])

slots.allele_descriptionallele_similarity_cluster_member_id = Slot(uri=AK_SCHEMA.allele_descriptionallele_similarity_cluster_member_id, name="allele_descriptionallele_similarity_cluster_member_id", curie=AK_SCHEMA.curie('allele_descriptionallele_similarity_cluster_member_id'),
                   model_uri=AK_SCHEMA.allele_descriptionallele_similarity_cluster_member_id, domain=None, range=Optional[str])

slots.allele_descriptionj_codon_frame = Slot(uri=AK_SCHEMA.allele_descriptionj_codon_frame, name="allele_descriptionj_codon_frame", curie=AK_SCHEMA.curie('allele_descriptionj_codon_frame'),
                   model_uri=AK_SCHEMA.allele_descriptionj_codon_frame, domain=None, range=Optional[Union[str, "V1p4JCodonFrame"]])

slots.allele_descriptiongene_start = Slot(uri=AK_SCHEMA.allele_descriptiongene_start, name="allele_descriptiongene_start", curie=AK_SCHEMA.curie('allele_descriptiongene_start'),
                   model_uri=AK_SCHEMA.allele_descriptiongene_start, domain=None, range=Optional[int])

slots.allele_descriptiongene_end = Slot(uri=AK_SCHEMA.allele_descriptiongene_end, name="allele_descriptiongene_end", curie=AK_SCHEMA.curie('allele_descriptiongene_end'),
                   model_uri=AK_SCHEMA.allele_descriptiongene_end, domain=None, range=Optional[int])

slots.allele_descriptionutr_5_prime_start = Slot(uri=AK_SCHEMA.allele_descriptionutr_5_prime_start, name="allele_descriptionutr_5_prime_start", curie=AK_SCHEMA.curie('allele_descriptionutr_5_prime_start'),
                   model_uri=AK_SCHEMA.allele_descriptionutr_5_prime_start, domain=None, range=Optional[int])

slots.allele_descriptionutr_5_prime_end = Slot(uri=AK_SCHEMA.allele_descriptionutr_5_prime_end, name="allele_descriptionutr_5_prime_end", curie=AK_SCHEMA.curie('allele_descriptionutr_5_prime_end'),
                   model_uri=AK_SCHEMA.allele_descriptionutr_5_prime_end, domain=None, range=Optional[int])

slots.allele_descriptionleader_1_start = Slot(uri=AK_SCHEMA.allele_descriptionleader_1_start, name="allele_descriptionleader_1_start", curie=AK_SCHEMA.curie('allele_descriptionleader_1_start'),
                   model_uri=AK_SCHEMA.allele_descriptionleader_1_start, domain=None, range=Optional[int])

slots.allele_descriptionleader_1_end = Slot(uri=AK_SCHEMA.allele_descriptionleader_1_end, name="allele_descriptionleader_1_end", curie=AK_SCHEMA.curie('allele_descriptionleader_1_end'),
                   model_uri=AK_SCHEMA.allele_descriptionleader_1_end, domain=None, range=Optional[int])

slots.allele_descriptionleader_2_start = Slot(uri=AK_SCHEMA.allele_descriptionleader_2_start, name="allele_descriptionleader_2_start", curie=AK_SCHEMA.curie('allele_descriptionleader_2_start'),
                   model_uri=AK_SCHEMA.allele_descriptionleader_2_start, domain=None, range=Optional[int])

slots.allele_descriptionleader_2_end = Slot(uri=AK_SCHEMA.allele_descriptionleader_2_end, name="allele_descriptionleader_2_end", curie=AK_SCHEMA.curie('allele_descriptionleader_2_end'),
                   model_uri=AK_SCHEMA.allele_descriptionleader_2_end, domain=None, range=Optional[int])

slots.allele_descriptionv_rs_start = Slot(uri=AK_SCHEMA.allele_descriptionv_rs_start, name="allele_descriptionv_rs_start", curie=AK_SCHEMA.curie('allele_descriptionv_rs_start'),
                   model_uri=AK_SCHEMA.allele_descriptionv_rs_start, domain=None, range=Optional[int])

slots.allele_descriptionv_rs_end = Slot(uri=AK_SCHEMA.allele_descriptionv_rs_end, name="allele_descriptionv_rs_end", curie=AK_SCHEMA.curie('allele_descriptionv_rs_end'),
                   model_uri=AK_SCHEMA.allele_descriptionv_rs_end, domain=None, range=Optional[int])

slots.allele_descriptiond_rs_3_prime_start = Slot(uri=AK_SCHEMA.allele_descriptiond_rs_3_prime_start, name="allele_descriptiond_rs_3_prime_start", curie=AK_SCHEMA.curie('allele_descriptiond_rs_3_prime_start'),
                   model_uri=AK_SCHEMA.allele_descriptiond_rs_3_prime_start, domain=None, range=Optional[int])

slots.allele_descriptiond_rs_3_prime_end = Slot(uri=AK_SCHEMA.allele_descriptiond_rs_3_prime_end, name="allele_descriptiond_rs_3_prime_end", curie=AK_SCHEMA.curie('allele_descriptiond_rs_3_prime_end'),
                   model_uri=AK_SCHEMA.allele_descriptiond_rs_3_prime_end, domain=None, range=Optional[int])

slots.allele_descriptiond_rs_5_prime_start = Slot(uri=AK_SCHEMA.allele_descriptiond_rs_5_prime_start, name="allele_descriptiond_rs_5_prime_start", curie=AK_SCHEMA.curie('allele_descriptiond_rs_5_prime_start'),
                   model_uri=AK_SCHEMA.allele_descriptiond_rs_5_prime_start, domain=None, range=Optional[int])

slots.allele_descriptiond_rs_5_prime_end = Slot(uri=AK_SCHEMA.allele_descriptiond_rs_5_prime_end, name="allele_descriptiond_rs_5_prime_end", curie=AK_SCHEMA.curie('allele_descriptiond_rs_5_prime_end'),
                   model_uri=AK_SCHEMA.allele_descriptiond_rs_5_prime_end, domain=None, range=Optional[int])

slots.allele_descriptionj_cdr3_end = Slot(uri=AK_SCHEMA.allele_descriptionj_cdr3_end, name="allele_descriptionj_cdr3_end", curie=AK_SCHEMA.curie('allele_descriptionj_cdr3_end'),
                   model_uri=AK_SCHEMA.allele_descriptionj_cdr3_end, domain=None, range=Optional[int])

slots.allele_descriptionj_rs_start = Slot(uri=AK_SCHEMA.allele_descriptionj_rs_start, name="allele_descriptionj_rs_start", curie=AK_SCHEMA.curie('allele_descriptionj_rs_start'),
                   model_uri=AK_SCHEMA.allele_descriptionj_rs_start, domain=None, range=Optional[int])

slots.allele_descriptionj_rs_end = Slot(uri=AK_SCHEMA.allele_descriptionj_rs_end, name="allele_descriptionj_rs_end", curie=AK_SCHEMA.curie('allele_descriptionj_rs_end'),
                   model_uri=AK_SCHEMA.allele_descriptionj_rs_end, domain=None, range=Optional[int])

slots.allele_descriptionj_donor_splice = Slot(uri=AK_SCHEMA.allele_descriptionj_donor_splice, name="allele_descriptionj_donor_splice", curie=AK_SCHEMA.curie('allele_descriptionj_donor_splice'),
                   model_uri=AK_SCHEMA.allele_descriptionj_donor_splice, domain=None, range=Optional[int])

slots.allele_descriptionv_gene_delineations = Slot(uri=AK_SCHEMA.allele_descriptionv_gene_delineations, name="allele_descriptionv_gene_delineations", curie=AK_SCHEMA.curie('allele_descriptionv_gene_delineations'),
                   model_uri=AK_SCHEMA.allele_descriptionv_gene_delineations, domain=None, range=Optional[Union[Union[dict, V1p4SequenceDelineationV], List[Union[dict, V1p4SequenceDelineationV]]]])

slots.allele_descriptionunrearranged_support = Slot(uri=AK_SCHEMA.allele_descriptionunrearranged_support, name="allele_descriptionunrearranged_support", curie=AK_SCHEMA.curie('allele_descriptionunrearranged_support'),
                   model_uri=AK_SCHEMA.allele_descriptionunrearranged_support, domain=None, range=Optional[Union[Union[dict, V1p4UnrearrangedSequence], List[Union[dict, V1p4UnrearrangedSequence]]]])

slots.allele_descriptionrearranged_support = Slot(uri=AK_SCHEMA.allele_descriptionrearranged_support, name="allele_descriptionrearranged_support", curie=AK_SCHEMA.curie('allele_descriptionrearranged_support'),
                   model_uri=AK_SCHEMA.allele_descriptionrearranged_support, domain=None, range=Optional[Union[Union[dict, V1p4RearrangedSequence], List[Union[dict, V1p4RearrangedSequence]]]])

slots.allele_descriptionparalogs = Slot(uri=AK_SCHEMA.allele_descriptionparalogs, name="allele_descriptionparalogs", curie=AK_SCHEMA.curie('allele_descriptionparalogs'),
                   model_uri=AK_SCHEMA.allele_descriptionparalogs, domain=None, range=Optional[Union[str, List[str]]])

slots.allele_descriptioncuration = Slot(uri=AK_SCHEMA.allele_descriptioncuration, name="allele_descriptioncuration", curie=AK_SCHEMA.curie('allele_descriptioncuration'),
                   model_uri=AK_SCHEMA.allele_descriptioncuration, domain=None, range=Optional[str])

slots.allele_descriptioncurational_tags = Slot(uri=AK_SCHEMA.allele_descriptioncurational_tags, name="allele_descriptioncurational_tags", curie=AK_SCHEMA.curie('allele_descriptioncurational_tags'),
                   model_uri=AK_SCHEMA.allele_descriptioncurational_tags, domain=None, range=Optional[Union[Union[str, "V1p4CurationalTags"], List[Union[str, "V1p4CurationalTags"]]]])

slots.germline_setgermline_set_id = Slot(uri=AK_SCHEMA.germline_setgermline_set_id, name="germline_setgermline_set_id", curie=AK_SCHEMA.curie('germline_setgermline_set_id'),
                   model_uri=AK_SCHEMA.germline_setgermline_set_id, domain=None, range=str)

slots.germline_setacknowledgements = Slot(uri=AK_SCHEMA.germline_setacknowledgements, name="germline_setacknowledgements", curie=AK_SCHEMA.curie('germline_setacknowledgements'),
                   model_uri=AK_SCHEMA.germline_setacknowledgements, domain=None, range=Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]])

slots.germline_setrelease_version = Slot(uri=AK_SCHEMA.germline_setrelease_version, name="germline_setrelease_version", curie=AK_SCHEMA.curie('germline_setrelease_version'),
                   model_uri=AK_SCHEMA.germline_setrelease_version, domain=None, range=float)

slots.germline_setrelease_description = Slot(uri=AK_SCHEMA.germline_setrelease_description, name="germline_setrelease_description", curie=AK_SCHEMA.curie('germline_setrelease_description'),
                   model_uri=AK_SCHEMA.germline_setrelease_description, domain=None, range=str)

slots.germline_setrelease_date = Slot(uri=AK_SCHEMA.germline_setrelease_date, name="germline_setrelease_date", curie=AK_SCHEMA.curie('germline_setrelease_date'),
                   model_uri=AK_SCHEMA.germline_setrelease_date, domain=None, range=str)

slots.germline_setgermline_set_name = Slot(uri=AK_SCHEMA.germline_setgermline_set_name, name="germline_setgermline_set_name", curie=AK_SCHEMA.curie('germline_setgermline_set_name'),
                   model_uri=AK_SCHEMA.germline_setgermline_set_name, domain=None, range=str)

slots.germline_setgermline_set_ref = Slot(uri=AK_SCHEMA.germline_setgermline_set_ref, name="germline_setgermline_set_ref", curie=AK_SCHEMA.curie('germline_setgermline_set_ref'),
                   model_uri=AK_SCHEMA.germline_setgermline_set_ref, domain=None, range=str)

slots.germline_setpub_ids = Slot(uri=AK_SCHEMA.germline_setpub_ids, name="germline_setpub_ids", curie=AK_SCHEMA.curie('germline_setpub_ids'),
                   model_uri=AK_SCHEMA.germline_setpub_ids, domain=None, range=Optional[Union[str, List[str]]])

slots.germline_setspecies = Slot(uri=AK_SCHEMA.germline_setspecies, name="germline_setspecies", curie=AK_SCHEMA.curie('germline_setspecies'),
                   model_uri=AK_SCHEMA.germline_setspecies, domain=None, range=Union[str, "V1p4Species"])

slots.germline_setspecies_subgroup = Slot(uri=AK_SCHEMA.germline_setspecies_subgroup, name="germline_setspecies_subgroup", curie=AK_SCHEMA.curie('germline_setspecies_subgroup'),
                   model_uri=AK_SCHEMA.germline_setspecies_subgroup, domain=None, range=Optional[str])

slots.germline_setspecies_subgroup_type = Slot(uri=AK_SCHEMA.germline_setspecies_subgroup_type, name="germline_setspecies_subgroup_type", curie=AK_SCHEMA.curie('germline_setspecies_subgroup_type'),
                   model_uri=AK_SCHEMA.germline_setspecies_subgroup_type, domain=None, range=Optional[Union[str, "V1p4SpeciesSubgroupType"]])

slots.germline_setlocus = Slot(uri=AK_SCHEMA.germline_setlocus, name="germline_setlocus", curie=AK_SCHEMA.curie('germline_setlocus'),
                   model_uri=AK_SCHEMA.germline_setlocus, domain=None, range=Union[str, "V1p4Locus"])

slots.germline_setallele_descriptions = Slot(uri=AK_SCHEMA.germline_setallele_descriptions, name="germline_setallele_descriptions", curie=AK_SCHEMA.curie('germline_setallele_descriptions'),
                   model_uri=AK_SCHEMA.germline_setallele_descriptions, domain=None, range=Union[Union[dict, V1p4AlleleDescription], List[Union[dict, V1p4AlleleDescription]]])

slots.germline_setcuration = Slot(uri=AK_SCHEMA.germline_setcuration, name="germline_setcuration", curie=AK_SCHEMA.curie('germline_setcuration'),
                   model_uri=AK_SCHEMA.germline_setcuration, domain=None, range=Optional[str])

slots.genotype_setreceptor_genotype_set_id = Slot(uri=AK_SCHEMA.genotype_setreceptor_genotype_set_id, name="genotype_setreceptor_genotype_set_id", curie=AK_SCHEMA.curie('genotype_setreceptor_genotype_set_id'),
                   model_uri=AK_SCHEMA.genotype_setreceptor_genotype_set_id, domain=None, range=str)

slots.genotype_setgenotype_class_list = Slot(uri=AK_SCHEMA.genotype_setgenotype_class_list, name="genotype_setgenotype_class_list", curie=AK_SCHEMA.curie('genotype_setgenotype_class_list'),
                   model_uri=AK_SCHEMA.genotype_setgenotype_class_list, domain=None, range=Optional[Union[Union[dict, V1p4Genotype], List[Union[dict, V1p4Genotype]]]])

slots.genotypereceptor_genotype_id = Slot(uri=AK_SCHEMA.genotypereceptor_genotype_id, name="genotypereceptor_genotype_id", curie=AK_SCHEMA.curie('genotypereceptor_genotype_id'),
                   model_uri=AK_SCHEMA.genotypereceptor_genotype_id, domain=None, range=str)

slots.genotypelocus = Slot(uri=AK_SCHEMA.genotypelocus, name="genotypelocus", curie=AK_SCHEMA.curie('genotypelocus'),
                   model_uri=AK_SCHEMA.genotypelocus, domain=None, range=Union[str, "V1p4Locus"])

slots.genotypedocumented_alleles = Slot(uri=AK_SCHEMA.genotypedocumented_alleles, name="genotypedocumented_alleles", curie=AK_SCHEMA.curie('genotypedocumented_alleles'),
                   model_uri=AK_SCHEMA.genotypedocumented_alleles, domain=None, range=Optional[Union[Union[dict, V1p4DocumentedAllele], List[Union[dict, V1p4DocumentedAllele]]]])

slots.genotypeundocumented_alleles = Slot(uri=AK_SCHEMA.genotypeundocumented_alleles, name="genotypeundocumented_alleles", curie=AK_SCHEMA.curie('genotypeundocumented_alleles'),
                   model_uri=AK_SCHEMA.genotypeundocumented_alleles, domain=None, range=Optional[Union[Union[dict, V1p4UndocumentedAllele], List[Union[dict, V1p4UndocumentedAllele]]]])

slots.genotypedeleted_genes = Slot(uri=AK_SCHEMA.genotypedeleted_genes, name="genotypedeleted_genes", curie=AK_SCHEMA.curie('genotypedeleted_genes'),
                   model_uri=AK_SCHEMA.genotypedeleted_genes, domain=None, range=Optional[Union[Union[dict, V1p4DeletedGene], List[Union[dict, V1p4DeletedGene]]]])

slots.genotypeinference_process = Slot(uri=AK_SCHEMA.genotypeinference_process, name="genotypeinference_process", curie=AK_SCHEMA.curie('genotypeinference_process'),
                   model_uri=AK_SCHEMA.genotypeinference_process, domain=None, range=Optional[Union[str, "V1p4InferenceProcess"]])

slots.documented_allelelabel = Slot(uri=AK_SCHEMA.documented_allelelabel, name="documented_allelelabel", curie=AK_SCHEMA.curie('documented_allelelabel'),
                   model_uri=AK_SCHEMA.documented_allelelabel, domain=None, range=str)

slots.documented_allelegermline_set_ref = Slot(uri=AK_SCHEMA.documented_allelegermline_set_ref, name="documented_allelegermline_set_ref", curie=AK_SCHEMA.curie('documented_allelegermline_set_ref'),
                   model_uri=AK_SCHEMA.documented_allelegermline_set_ref, domain=None, range=str)

slots.documented_allelephasing = Slot(uri=AK_SCHEMA.documented_allelephasing, name="documented_allelephasing", curie=AK_SCHEMA.curie('documented_allelephasing'),
                   model_uri=AK_SCHEMA.documented_allelephasing, domain=None, range=Optional[int])

slots.undocumented_alleleallele_name = Slot(uri=AK_SCHEMA.undocumented_alleleallele_name, name="undocumented_alleleallele_name", curie=AK_SCHEMA.curie('undocumented_alleleallele_name'),
                   model_uri=AK_SCHEMA.undocumented_alleleallele_name, domain=None, range=str)

slots.undocumented_allelesequence = Slot(uri=AK_SCHEMA.undocumented_allelesequence, name="undocumented_allelesequence", curie=AK_SCHEMA.curie('undocumented_allelesequence'),
                   model_uri=AK_SCHEMA.undocumented_allelesequence, domain=None, range=str)

slots.undocumented_allelephasing = Slot(uri=AK_SCHEMA.undocumented_allelephasing, name="undocumented_allelephasing", curie=AK_SCHEMA.curie('undocumented_allelephasing'),
                   model_uri=AK_SCHEMA.undocumented_allelephasing, domain=None, range=Optional[int])

slots.deleted_genelabel = Slot(uri=AK_SCHEMA.deleted_genelabel, name="deleted_genelabel", curie=AK_SCHEMA.curie('deleted_genelabel'),
                   model_uri=AK_SCHEMA.deleted_genelabel, domain=None, range=str)

slots.deleted_genegermline_set_ref = Slot(uri=AK_SCHEMA.deleted_genegermline_set_ref, name="deleted_genegermline_set_ref", curie=AK_SCHEMA.curie('deleted_genegermline_set_ref'),
                   model_uri=AK_SCHEMA.deleted_genegermline_set_ref, domain=None, range=str)

slots.deleted_genephasing = Slot(uri=AK_SCHEMA.deleted_genephasing, name="deleted_genephasing", curie=AK_SCHEMA.curie('deleted_genephasing'),
                   model_uri=AK_SCHEMA.deleted_genephasing, domain=None, range=Optional[int])

slots.m_h_c_genotype_setmhc_genotype_set_id = Slot(uri=AK_SCHEMA.m_h_c_genotype_setmhc_genotype_set_id, name="m_h_c_genotype_setmhc_genotype_set_id", curie=AK_SCHEMA.curie('m_h_c_genotype_setmhc_genotype_set_id'),
                   model_uri=AK_SCHEMA.m_h_c_genotype_setmhc_genotype_set_id, domain=None, range=str)

slots.m_h_c_genotype_setmhc_genotype_list = Slot(uri=AK_SCHEMA.m_h_c_genotype_setmhc_genotype_list, name="m_h_c_genotype_setmhc_genotype_list", curie=AK_SCHEMA.curie('m_h_c_genotype_setmhc_genotype_list'),
                   model_uri=AK_SCHEMA.m_h_c_genotype_setmhc_genotype_list, domain=None, range=Union[Union[dict, V1p4MHCGenotype], List[Union[dict, V1p4MHCGenotype]]])

slots.m_h_c_genotypemhc_genotype_id = Slot(uri=AK_SCHEMA.m_h_c_genotypemhc_genotype_id, name="m_h_c_genotypemhc_genotype_id", curie=AK_SCHEMA.curie('m_h_c_genotypemhc_genotype_id'),
                   model_uri=AK_SCHEMA.m_h_c_genotypemhc_genotype_id, domain=None, range=str)

slots.m_h_c_genotypemhc_class = Slot(uri=AK_SCHEMA.m_h_c_genotypemhc_class, name="m_h_c_genotypemhc_class", curie=AK_SCHEMA.curie('m_h_c_genotypemhc_class'),
                   model_uri=AK_SCHEMA.m_h_c_genotypemhc_class, domain=None, range=Union[str, "V1p4MhcClass"])

slots.m_h_c_genotypemhc_alleles = Slot(uri=AK_SCHEMA.m_h_c_genotypemhc_alleles, name="m_h_c_genotypemhc_alleles", curie=AK_SCHEMA.curie('m_h_c_genotypemhc_alleles'),
                   model_uri=AK_SCHEMA.m_h_c_genotypemhc_alleles, domain=None, range=Union[Union[dict, V1p4MHCAllele], List[Union[dict, V1p4MHCAllele]]])

slots.m_h_c_genotypemhc_genotyping_method = Slot(uri=AK_SCHEMA.m_h_c_genotypemhc_genotyping_method, name="m_h_c_genotypemhc_genotyping_method", curie=AK_SCHEMA.curie('m_h_c_genotypemhc_genotyping_method'),
                   model_uri=AK_SCHEMA.m_h_c_genotypemhc_genotyping_method, domain=None, range=Optional[str])

slots.m_h_c_alleleallele_designation = Slot(uri=AK_SCHEMA.m_h_c_alleleallele_designation, name="m_h_c_alleleallele_designation", curie=AK_SCHEMA.curie('m_h_c_alleleallele_designation'),
                   model_uri=AK_SCHEMA.m_h_c_alleleallele_designation, domain=None, range=Optional[str])

slots.m_h_c_allelegene = Slot(uri=AK_SCHEMA.m_h_c_allelegene, name="m_h_c_allelegene", curie=AK_SCHEMA.curie('m_h_c_allelegene'),
                   model_uri=AK_SCHEMA.m_h_c_allelegene, domain=None, range=Optional[Union[str, "V1p4Gene"]])

slots.m_h_c_allelereference_set_ref = Slot(uri=AK_SCHEMA.m_h_c_allelereference_set_ref, name="m_h_c_allelereference_set_ref", curie=AK_SCHEMA.curie('m_h_c_allelereference_set_ref'),
                   model_uri=AK_SCHEMA.m_h_c_allelereference_set_ref, domain=None, range=Optional[str])

slots.subject_genotypereceptor_genotype_set = Slot(uri=AK_SCHEMA.subject_genotypereceptor_genotype_set, name="subject_genotypereceptor_genotype_set", curie=AK_SCHEMA.curie('subject_genotypereceptor_genotype_set'),
                   model_uri=AK_SCHEMA.subject_genotypereceptor_genotype_set, domain=None, range=Optional[Union[dict, V1p4GenotypeSet]])

slots.subject_genotypemhc_genotype_set = Slot(uri=AK_SCHEMA.subject_genotypemhc_genotype_set, name="subject_genotypemhc_genotype_set", curie=AK_SCHEMA.curie('subject_genotypemhc_genotype_set'),
                   model_uri=AK_SCHEMA.subject_genotypemhc_genotype_set, domain=None, range=Optional[Union[dict, V1p4MHCGenotypeSet]])

slots.studystudy_id = Slot(uri=AK_SCHEMA.studystudy_id, name="studystudy_id", curie=AK_SCHEMA.curie('studystudy_id'),
                   model_uri=AK_SCHEMA.studystudy_id, domain=None, range=str)

slots.studystudy_title = Slot(uri=AK_SCHEMA.studystudy_title, name="studystudy_title", curie=AK_SCHEMA.curie('studystudy_title'),
                   model_uri=AK_SCHEMA.studystudy_title, domain=None, range=str)

slots.studystudy_type = Slot(uri=AK_SCHEMA.studystudy_type, name="studystudy_type", curie=AK_SCHEMA.curie('studystudy_type'),
                   model_uri=AK_SCHEMA.studystudy_type, domain=None, range=Union[str, "V1p4StudyType"])

slots.studystudy_description = Slot(uri=AK_SCHEMA.studystudy_description, name="studystudy_description", curie=AK_SCHEMA.curie('studystudy_description'),
                   model_uri=AK_SCHEMA.studystudy_description, domain=None, range=Optional[str])

slots.studyinclusion_exclusion_criteria = Slot(uri=AK_SCHEMA.studyinclusion_exclusion_criteria, name="studyinclusion_exclusion_criteria", curie=AK_SCHEMA.curie('studyinclusion_exclusion_criteria'),
                   model_uri=AK_SCHEMA.studyinclusion_exclusion_criteria, domain=None, range=str)

slots.studygrants = Slot(uri=AK_SCHEMA.studygrants, name="studygrants", curie=AK_SCHEMA.curie('studygrants'),
                   model_uri=AK_SCHEMA.studygrants, domain=None, range=str)

slots.studycontributors = Slot(uri=AK_SCHEMA.studycontributors, name="studycontributors", curie=AK_SCHEMA.curie('studycontributors'),
                   model_uri=AK_SCHEMA.studycontributors, domain=None, range=Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]])

slots.studypub_ids = Slot(uri=AK_SCHEMA.studypub_ids, name="studypub_ids", curie=AK_SCHEMA.curie('studypub_ids'),
                   model_uri=AK_SCHEMA.studypub_ids, domain=None, range=Union[str, List[str]])

slots.studykeywords_study = Slot(uri=AK_SCHEMA.studykeywords_study, name="studykeywords_study", curie=AK_SCHEMA.curie('studykeywords_study'),
                   model_uri=AK_SCHEMA.studykeywords_study, domain=None, range=Union[Union[str, "V1p4KeywordsStudy"], List[Union[str, "V1p4KeywordsStudy"]]])

slots.studyadc_publish_date = Slot(uri=AK_SCHEMA.studyadc_publish_date, name="studyadc_publish_date", curie=AK_SCHEMA.curie('studyadc_publish_date'),
                   model_uri=AK_SCHEMA.studyadc_publish_date, domain=None, range=Optional[str])

slots.studyadc_update_date = Slot(uri=AK_SCHEMA.studyadc_update_date, name="studyadc_update_date", curie=AK_SCHEMA.curie('studyadc_update_date'),
                   model_uri=AK_SCHEMA.studyadc_update_date, domain=None, range=Optional[str])

slots.subjectsubject_id = Slot(uri=AK_SCHEMA.subjectsubject_id, name="subjectsubject_id", curie=AK_SCHEMA.curie('subjectsubject_id'),
                   model_uri=AK_SCHEMA.subjectsubject_id, domain=None, range=str)

slots.subjectsynthetic = Slot(uri=AK_SCHEMA.subjectsynthetic, name="subjectsynthetic", curie=AK_SCHEMA.curie('subjectsynthetic'),
                   model_uri=AK_SCHEMA.subjectsynthetic, domain=None, range=Union[bool, Bool])

slots.subjectspecies = Slot(uri=AK_SCHEMA.subjectspecies, name="subjectspecies", curie=AK_SCHEMA.curie('subjectspecies'),
                   model_uri=AK_SCHEMA.subjectspecies, domain=None, range=Union[str, "V1p4Species"])

slots.subjectsex = Slot(uri=AK_SCHEMA.subjectsex, name="subjectsex", curie=AK_SCHEMA.curie('subjectsex'),
                   model_uri=AK_SCHEMA.subjectsex, domain=None, range=Union[str, "V1p4Sex"])

slots.subjectage = Slot(uri=AK_SCHEMA.subjectage, name="subjectage", curie=AK_SCHEMA.curie('subjectage'),
                   model_uri=AK_SCHEMA.subjectage, domain=None, range=Union[dict, V1p4TimeInterval])

slots.subjectage_event = Slot(uri=AK_SCHEMA.subjectage_event, name="subjectage_event", curie=AK_SCHEMA.curie('subjectage_event'),
                   model_uri=AK_SCHEMA.subjectage_event, domain=None, range=str)

slots.subjectancestry_population = Slot(uri=AK_SCHEMA.subjectancestry_population, name="subjectancestry_population", curie=AK_SCHEMA.curie('subjectancestry_population'),
                   model_uri=AK_SCHEMA.subjectancestry_population, domain=None, range=Union[str, "V1p4AncestryPopulation"])

slots.subjectlocation_birth = Slot(uri=AK_SCHEMA.subjectlocation_birth, name="subjectlocation_birth", curie=AK_SCHEMA.curie('subjectlocation_birth'),
                   model_uri=AK_SCHEMA.subjectlocation_birth, domain=None, range=Optional[Union[str, "V1p4LocationBirth"]])

slots.subjectethnicity = Slot(uri=AK_SCHEMA.subjectethnicity, name="subjectethnicity", curie=AK_SCHEMA.curie('subjectethnicity'),
                   model_uri=AK_SCHEMA.subjectethnicity, domain=None, range=str)

slots.subjectrace = Slot(uri=AK_SCHEMA.subjectrace, name="subjectrace", curie=AK_SCHEMA.curie('subjectrace'),
                   model_uri=AK_SCHEMA.subjectrace, domain=None, range=str)

slots.subjectstrain_name = Slot(uri=AK_SCHEMA.subjectstrain_name, name="subjectstrain_name", curie=AK_SCHEMA.curie('subjectstrain_name'),
                   model_uri=AK_SCHEMA.subjectstrain_name, domain=None, range=str)

slots.subjectlinked_subjects = Slot(uri=AK_SCHEMA.subjectlinked_subjects, name="subjectlinked_subjects", curie=AK_SCHEMA.curie('subjectlinked_subjects'),
                   model_uri=AK_SCHEMA.subjectlinked_subjects, domain=None, range=str)

slots.subjectlink_type = Slot(uri=AK_SCHEMA.subjectlink_type, name="subjectlink_type", curie=AK_SCHEMA.curie('subjectlink_type'),
                   model_uri=AK_SCHEMA.subjectlink_type, domain=None, range=str)

slots.subjectdiagnosis = Slot(uri=AK_SCHEMA.subjectdiagnosis, name="subjectdiagnosis", curie=AK_SCHEMA.curie('subjectdiagnosis'),
                   model_uri=AK_SCHEMA.subjectdiagnosis, domain=None, range=Optional[Union[Union[dict, V1p4Diagnosis], List[Union[dict, V1p4Diagnosis]]]])

slots.subjectgenotype = Slot(uri=AK_SCHEMA.subjectgenotype, name="subjectgenotype", curie=AK_SCHEMA.curie('subjectgenotype'),
                   model_uri=AK_SCHEMA.subjectgenotype, domain=None, range=Optional[Union[dict, V1p4SubjectGenotype]])

slots.diagnosisstudy_group_description = Slot(uri=AK_SCHEMA.diagnosisstudy_group_description, name="diagnosisstudy_group_description", curie=AK_SCHEMA.curie('diagnosisstudy_group_description'),
                   model_uri=AK_SCHEMA.diagnosisstudy_group_description, domain=None, range=str)

slots.diagnosisdiagnosis_timepoint = Slot(uri=AK_SCHEMA.diagnosisdiagnosis_timepoint, name="diagnosisdiagnosis_timepoint", curie=AK_SCHEMA.curie('diagnosisdiagnosis_timepoint'),
                   model_uri=AK_SCHEMA.diagnosisdiagnosis_timepoint, domain=None, range=Optional[Union[dict, V1p4TimePoint]])

slots.diagnosisdisease_diagnosis = Slot(uri=AK_SCHEMA.diagnosisdisease_diagnosis, name="diagnosisdisease_diagnosis", curie=AK_SCHEMA.curie('diagnosisdisease_diagnosis'),
                   model_uri=AK_SCHEMA.diagnosisdisease_diagnosis, domain=None, range=Union[str, "V1p4DiseaseDiagnosis"])

slots.diagnosisdisease_length = Slot(uri=AK_SCHEMA.diagnosisdisease_length, name="diagnosisdisease_length", curie=AK_SCHEMA.curie('diagnosisdisease_length'),
                   model_uri=AK_SCHEMA.diagnosisdisease_length, domain=None, range=Union[dict, V1p4TimeQuantity])

slots.diagnosisdisease_stage = Slot(uri=AK_SCHEMA.diagnosisdisease_stage, name="diagnosisdisease_stage", curie=AK_SCHEMA.curie('diagnosisdisease_stage'),
                   model_uri=AK_SCHEMA.diagnosisdisease_stage, domain=None, range=str)

slots.diagnosisprior_therapies = Slot(uri=AK_SCHEMA.diagnosisprior_therapies, name="diagnosisprior_therapies", curie=AK_SCHEMA.curie('diagnosisprior_therapies'),
                   model_uri=AK_SCHEMA.diagnosisprior_therapies, domain=None, range=str)

slots.diagnosisimmunogen = Slot(uri=AK_SCHEMA.diagnosisimmunogen, name="diagnosisimmunogen", curie=AK_SCHEMA.curie('diagnosisimmunogen'),
                   model_uri=AK_SCHEMA.diagnosisimmunogen, domain=None, range=str)

slots.diagnosisintervention = Slot(uri=AK_SCHEMA.diagnosisintervention, name="diagnosisintervention", curie=AK_SCHEMA.curie('diagnosisintervention'),
                   model_uri=AK_SCHEMA.diagnosisintervention, domain=None, range=str)

slots.diagnosismedical_history = Slot(uri=AK_SCHEMA.diagnosismedical_history, name="diagnosismedical_history", curie=AK_SCHEMA.curie('diagnosismedical_history'),
                   model_uri=AK_SCHEMA.diagnosismedical_history, domain=None, range=str)

slots.samplesample_id = Slot(uri=AK_SCHEMA.samplesample_id, name="samplesample_id", curie=AK_SCHEMA.curie('samplesample_id'),
                   model_uri=AK_SCHEMA.samplesample_id, domain=None, range=str)

slots.samplesample_type = Slot(uri=AK_SCHEMA.samplesample_type, name="samplesample_type", curie=AK_SCHEMA.curie('samplesample_type'),
                   model_uri=AK_SCHEMA.samplesample_type, domain=None, range=str)

slots.sampletissue = Slot(uri=AK_SCHEMA.sampletissue, name="sampletissue", curie=AK_SCHEMA.curie('sampletissue'),
                   model_uri=AK_SCHEMA.sampletissue, domain=None, range=Union[str, "V1p4Tissue"])

slots.sampleanatomic_site = Slot(uri=AK_SCHEMA.sampleanatomic_site, name="sampleanatomic_site", curie=AK_SCHEMA.curie('sampleanatomic_site'),
                   model_uri=AK_SCHEMA.sampleanatomic_site, domain=None, range=str)

slots.sampledisease_state_sample = Slot(uri=AK_SCHEMA.sampledisease_state_sample, name="sampledisease_state_sample", curie=AK_SCHEMA.curie('sampledisease_state_sample'),
                   model_uri=AK_SCHEMA.sampledisease_state_sample, domain=None, range=str)

slots.samplecollection_time_point_relative = Slot(uri=AK_SCHEMA.samplecollection_time_point_relative, name="samplecollection_time_point_relative", curie=AK_SCHEMA.curie('samplecollection_time_point_relative'),
                   model_uri=AK_SCHEMA.samplecollection_time_point_relative, domain=None, range=Union[dict, V1p4TimePoint])

slots.samplecollection_location = Slot(uri=AK_SCHEMA.samplecollection_location, name="samplecollection_location", curie=AK_SCHEMA.curie('samplecollection_location'),
                   model_uri=AK_SCHEMA.samplecollection_location, domain=None, range=Optional[Union[str, "V1p4CollectionLocation"]])

slots.samplebiomaterial_provider = Slot(uri=AK_SCHEMA.samplebiomaterial_provider, name="samplebiomaterial_provider", curie=AK_SCHEMA.curie('samplebiomaterial_provider'),
                   model_uri=AK_SCHEMA.samplebiomaterial_provider, domain=None, range=str)

slots.cell_processingtissue_processing = Slot(uri=AK_SCHEMA.cell_processingtissue_processing, name="cell_processingtissue_processing", curie=AK_SCHEMA.curie('cell_processingtissue_processing'),
                   model_uri=AK_SCHEMA.cell_processingtissue_processing, domain=None, range=str)

slots.cell_processingcell_subset = Slot(uri=AK_SCHEMA.cell_processingcell_subset, name="cell_processingcell_subset", curie=AK_SCHEMA.curie('cell_processingcell_subset'),
                   model_uri=AK_SCHEMA.cell_processingcell_subset, domain=None, range=Union[str, "V1p4CellSubset"])

slots.cell_processingcell_phenotype = Slot(uri=AK_SCHEMA.cell_processingcell_phenotype, name="cell_processingcell_phenotype", curie=AK_SCHEMA.curie('cell_processingcell_phenotype'),
                   model_uri=AK_SCHEMA.cell_processingcell_phenotype, domain=None, range=str)

slots.cell_processingcell_label = Slot(uri=AK_SCHEMA.cell_processingcell_label, name="cell_processingcell_label", curie=AK_SCHEMA.curie('cell_processingcell_label'),
                   model_uri=AK_SCHEMA.cell_processingcell_label, domain=None, range=Optional[str])

slots.cell_processingcell_species = Slot(uri=AK_SCHEMA.cell_processingcell_species, name="cell_processingcell_species", curie=AK_SCHEMA.curie('cell_processingcell_species'),
                   model_uri=AK_SCHEMA.cell_processingcell_species, domain=None, range=Optional[Union[str, "V1p4CellSpecies"]])

slots.cell_processingsingle_cell = Slot(uri=AK_SCHEMA.cell_processingsingle_cell, name="cell_processingsingle_cell", curie=AK_SCHEMA.curie('cell_processingsingle_cell'),
                   model_uri=AK_SCHEMA.cell_processingsingle_cell, domain=None, range=Union[bool, Bool])

slots.cell_processingcell_number = Slot(uri=AK_SCHEMA.cell_processingcell_number, name="cell_processingcell_number", curie=AK_SCHEMA.curie('cell_processingcell_number'),
                   model_uri=AK_SCHEMA.cell_processingcell_number, domain=None, range=int)

slots.cell_processingcells_per_reaction = Slot(uri=AK_SCHEMA.cell_processingcells_per_reaction, name="cell_processingcells_per_reaction", curie=AK_SCHEMA.curie('cell_processingcells_per_reaction'),
                   model_uri=AK_SCHEMA.cell_processingcells_per_reaction, domain=None, range=int)

slots.cell_processingcell_storage = Slot(uri=AK_SCHEMA.cell_processingcell_storage, name="cell_processingcell_storage", curie=AK_SCHEMA.curie('cell_processingcell_storage'),
                   model_uri=AK_SCHEMA.cell_processingcell_storage, domain=None, range=Union[bool, Bool])

slots.cell_processingcell_quality = Slot(uri=AK_SCHEMA.cell_processingcell_quality, name="cell_processingcell_quality", curie=AK_SCHEMA.curie('cell_processingcell_quality'),
                   model_uri=AK_SCHEMA.cell_processingcell_quality, domain=None, range=str)

slots.cell_processingcell_isolation = Slot(uri=AK_SCHEMA.cell_processingcell_isolation, name="cell_processingcell_isolation", curie=AK_SCHEMA.curie('cell_processingcell_isolation'),
                   model_uri=AK_SCHEMA.cell_processingcell_isolation, domain=None, range=str)

slots.cell_processingcell_processing_protocol = Slot(uri=AK_SCHEMA.cell_processingcell_processing_protocol, name="cell_processingcell_processing_protocol", curie=AK_SCHEMA.curie('cell_processingcell_processing_protocol'),
                   model_uri=AK_SCHEMA.cell_processingcell_processing_protocol, domain=None, range=str)

slots.p_c_r_targetpcr_target_locus = Slot(uri=AK_SCHEMA.p_c_r_targetpcr_target_locus, name="p_c_r_targetpcr_target_locus", curie=AK_SCHEMA.curie('p_c_r_targetpcr_target_locus'),
                   model_uri=AK_SCHEMA.p_c_r_targetpcr_target_locus, domain=None, range=Union[str, "V1p4PcrTargetLocus"])

slots.p_c_r_targetforward_pcr_primer_target_location = Slot(uri=AK_SCHEMA.p_c_r_targetforward_pcr_primer_target_location, name="p_c_r_targetforward_pcr_primer_target_location", curie=AK_SCHEMA.curie('p_c_r_targetforward_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.p_c_r_targetforward_pcr_primer_target_location, domain=None, range=str)

slots.p_c_r_targetreverse_pcr_primer_target_location = Slot(uri=AK_SCHEMA.p_c_r_targetreverse_pcr_primer_target_location, name="p_c_r_targetreverse_pcr_primer_target_location", curie=AK_SCHEMA.curie('p_c_r_targetreverse_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.p_c_r_targetreverse_pcr_primer_target_location, domain=None, range=str)

slots.nucleic_acid_processingtemplate_class = Slot(uri=AK_SCHEMA.nucleic_acid_processingtemplate_class, name="nucleic_acid_processingtemplate_class", curie=AK_SCHEMA.curie('nucleic_acid_processingtemplate_class'),
                   model_uri=AK_SCHEMA.nucleic_acid_processingtemplate_class, domain=None, range=Union[str, "V1p4TemplateClass"])

slots.nucleic_acid_processingtemplate_quality = Slot(uri=AK_SCHEMA.nucleic_acid_processingtemplate_quality, name="nucleic_acid_processingtemplate_quality", curie=AK_SCHEMA.curie('nucleic_acid_processingtemplate_quality'),
                   model_uri=AK_SCHEMA.nucleic_acid_processingtemplate_quality, domain=None, range=str)

slots.nucleic_acid_processingtemplate_amount = Slot(uri=AK_SCHEMA.nucleic_acid_processingtemplate_amount, name="nucleic_acid_processingtemplate_amount", curie=AK_SCHEMA.curie('nucleic_acid_processingtemplate_amount'),
                   model_uri=AK_SCHEMA.nucleic_acid_processingtemplate_amount, domain=None, range=Union[dict, V1p4PhysicalQuantity])

slots.nucleic_acid_processinglibrary_generation_method = Slot(uri=AK_SCHEMA.nucleic_acid_processinglibrary_generation_method, name="nucleic_acid_processinglibrary_generation_method", curie=AK_SCHEMA.curie('nucleic_acid_processinglibrary_generation_method'),
                   model_uri=AK_SCHEMA.nucleic_acid_processinglibrary_generation_method, domain=None, range=Union[str, "V1p4LibraryGenerationMethod"])

slots.nucleic_acid_processinglibrary_generation_protocol = Slot(uri=AK_SCHEMA.nucleic_acid_processinglibrary_generation_protocol, name="nucleic_acid_processinglibrary_generation_protocol", curie=AK_SCHEMA.curie('nucleic_acid_processinglibrary_generation_protocol'),
                   model_uri=AK_SCHEMA.nucleic_acid_processinglibrary_generation_protocol, domain=None, range=str)

slots.nucleic_acid_processinglibrary_generation_kit_version = Slot(uri=AK_SCHEMA.nucleic_acid_processinglibrary_generation_kit_version, name="nucleic_acid_processinglibrary_generation_kit_version", curie=AK_SCHEMA.curie('nucleic_acid_processinglibrary_generation_kit_version'),
                   model_uri=AK_SCHEMA.nucleic_acid_processinglibrary_generation_kit_version, domain=None, range=str)

slots.nucleic_acid_processingpcr_target = Slot(uri=AK_SCHEMA.nucleic_acid_processingpcr_target, name="nucleic_acid_processingpcr_target", curie=AK_SCHEMA.curie('nucleic_acid_processingpcr_target'),
                   model_uri=AK_SCHEMA.nucleic_acid_processingpcr_target, domain=None, range=Optional[Union[Union[dict, V1p4PCRTarget], List[Union[dict, V1p4PCRTarget]]]])

slots.nucleic_acid_processingcomplete_sequences = Slot(uri=AK_SCHEMA.nucleic_acid_processingcomplete_sequences, name="nucleic_acid_processingcomplete_sequences", curie=AK_SCHEMA.curie('nucleic_acid_processingcomplete_sequences'),
                   model_uri=AK_SCHEMA.nucleic_acid_processingcomplete_sequences, domain=None, range=Union[str, "V1p4CompleteSequences"])

slots.nucleic_acid_processingphysical_linkage = Slot(uri=AK_SCHEMA.nucleic_acid_processingphysical_linkage, name="nucleic_acid_processingphysical_linkage", curie=AK_SCHEMA.curie('nucleic_acid_processingphysical_linkage'),
                   model_uri=AK_SCHEMA.nucleic_acid_processingphysical_linkage, domain=None, range=Union[str, "V1p4PhysicalLinkage"])

slots.sequencing_runsequencing_run_id = Slot(uri=AK_SCHEMA.sequencing_runsequencing_run_id, name="sequencing_runsequencing_run_id", curie=AK_SCHEMA.curie('sequencing_runsequencing_run_id'),
                   model_uri=AK_SCHEMA.sequencing_runsequencing_run_id, domain=None, range=str)

slots.sequencing_runtotal_reads_passing_qc_filter = Slot(uri=AK_SCHEMA.sequencing_runtotal_reads_passing_qc_filter, name="sequencing_runtotal_reads_passing_qc_filter", curie=AK_SCHEMA.curie('sequencing_runtotal_reads_passing_qc_filter'),
                   model_uri=AK_SCHEMA.sequencing_runtotal_reads_passing_qc_filter, domain=None, range=int)

slots.sequencing_runsequencing_platform = Slot(uri=AK_SCHEMA.sequencing_runsequencing_platform, name="sequencing_runsequencing_platform", curie=AK_SCHEMA.curie('sequencing_runsequencing_platform'),
                   model_uri=AK_SCHEMA.sequencing_runsequencing_platform, domain=None, range=str)

slots.sequencing_runsequencing_facility = Slot(uri=AK_SCHEMA.sequencing_runsequencing_facility, name="sequencing_runsequencing_facility", curie=AK_SCHEMA.curie('sequencing_runsequencing_facility'),
                   model_uri=AK_SCHEMA.sequencing_runsequencing_facility, domain=None, range=str)

slots.sequencing_runsequencing_run_date = Slot(uri=AK_SCHEMA.sequencing_runsequencing_run_date, name="sequencing_runsequencing_run_date", curie=AK_SCHEMA.curie('sequencing_runsequencing_run_date'),
                   model_uri=AK_SCHEMA.sequencing_runsequencing_run_date, domain=None, range=str)

slots.sequencing_runsequencing_kit = Slot(uri=AK_SCHEMA.sequencing_runsequencing_kit, name="sequencing_runsequencing_kit", curie=AK_SCHEMA.curie('sequencing_runsequencing_kit'),
                   model_uri=AK_SCHEMA.sequencing_runsequencing_kit, domain=None, range=str)

slots.sequencing_runsequencing_files = Slot(uri=AK_SCHEMA.sequencing_runsequencing_files, name="sequencing_runsequencing_files", curie=AK_SCHEMA.curie('sequencing_runsequencing_files'),
                   model_uri=AK_SCHEMA.sequencing_runsequencing_files, domain=None, range=Optional[Union[dict, V1p4SequencingData]])

slots.sequencing_datasequencing_data_id = Slot(uri=AK_SCHEMA.sequencing_datasequencing_data_id, name="sequencing_datasequencing_data_id", curie=AK_SCHEMA.curie('sequencing_datasequencing_data_id'),
                   model_uri=AK_SCHEMA.sequencing_datasequencing_data_id, domain=None, range=str)

slots.sequencing_datafile_type = Slot(uri=AK_SCHEMA.sequencing_datafile_type, name="sequencing_datafile_type", curie=AK_SCHEMA.curie('sequencing_datafile_type'),
                   model_uri=AK_SCHEMA.sequencing_datafile_type, domain=None, range=Union[str, "V1p4FileType"])

slots.sequencing_datafilename = Slot(uri=AK_SCHEMA.sequencing_datafilename, name="sequencing_datafilename", curie=AK_SCHEMA.curie('sequencing_datafilename'),
                   model_uri=AK_SCHEMA.sequencing_datafilename, domain=None, range=str)

slots.sequencing_dataread_direction = Slot(uri=AK_SCHEMA.sequencing_dataread_direction, name="sequencing_dataread_direction", curie=AK_SCHEMA.curie('sequencing_dataread_direction'),
                   model_uri=AK_SCHEMA.sequencing_dataread_direction, domain=None, range=Union[str, "V1p4ReadDirection"])

slots.sequencing_dataread_length = Slot(uri=AK_SCHEMA.sequencing_dataread_length, name="sequencing_dataread_length", curie=AK_SCHEMA.curie('sequencing_dataread_length'),
                   model_uri=AK_SCHEMA.sequencing_dataread_length, domain=None, range=int)

slots.sequencing_datapaired_filename = Slot(uri=AK_SCHEMA.sequencing_datapaired_filename, name="sequencing_datapaired_filename", curie=AK_SCHEMA.curie('sequencing_datapaired_filename'),
                   model_uri=AK_SCHEMA.sequencing_datapaired_filename, domain=None, range=str)

slots.sequencing_datapaired_read_direction = Slot(uri=AK_SCHEMA.sequencing_datapaired_read_direction, name="sequencing_datapaired_read_direction", curie=AK_SCHEMA.curie('sequencing_datapaired_read_direction'),
                   model_uri=AK_SCHEMA.sequencing_datapaired_read_direction, domain=None, range=Union[str, "V1p4PairedReadDirection"])

slots.sequencing_datapaired_read_length = Slot(uri=AK_SCHEMA.sequencing_datapaired_read_length, name="sequencing_datapaired_read_length", curie=AK_SCHEMA.curie('sequencing_datapaired_read_length'),
                   model_uri=AK_SCHEMA.sequencing_datapaired_read_length, domain=None, range=int)

slots.sequencing_dataindex_filename = Slot(uri=AK_SCHEMA.sequencing_dataindex_filename, name="sequencing_dataindex_filename", curie=AK_SCHEMA.curie('sequencing_dataindex_filename'),
                   model_uri=AK_SCHEMA.sequencing_dataindex_filename, domain=None, range=Optional[str])

slots.sequencing_dataindex_length = Slot(uri=AK_SCHEMA.sequencing_dataindex_length, name="sequencing_dataindex_length", curie=AK_SCHEMA.curie('sequencing_dataindex_length'),
                   model_uri=AK_SCHEMA.sequencing_dataindex_length, domain=None, range=Optional[int])

slots.data_processingdata_processing_id = Slot(uri=AK_SCHEMA.data_processingdata_processing_id, name="data_processingdata_processing_id", curie=AK_SCHEMA.curie('data_processingdata_processing_id'),
                   model_uri=AK_SCHEMA.data_processingdata_processing_id, domain=None, range=Optional[str])

slots.data_processingprimary_annotation = Slot(uri=AK_SCHEMA.data_processingprimary_annotation, name="data_processingprimary_annotation", curie=AK_SCHEMA.curie('data_processingprimary_annotation'),
                   model_uri=AK_SCHEMA.data_processingprimary_annotation, domain=None, range=Optional[Union[bool, Bool]])

slots.data_processingsoftware_versions = Slot(uri=AK_SCHEMA.data_processingsoftware_versions, name="data_processingsoftware_versions", curie=AK_SCHEMA.curie('data_processingsoftware_versions'),
                   model_uri=AK_SCHEMA.data_processingsoftware_versions, domain=None, range=str)

slots.data_processingpaired_reads_assembly = Slot(uri=AK_SCHEMA.data_processingpaired_reads_assembly, name="data_processingpaired_reads_assembly", curie=AK_SCHEMA.curie('data_processingpaired_reads_assembly'),
                   model_uri=AK_SCHEMA.data_processingpaired_reads_assembly, domain=None, range=str)

slots.data_processingquality_thresholds = Slot(uri=AK_SCHEMA.data_processingquality_thresholds, name="data_processingquality_thresholds", curie=AK_SCHEMA.curie('data_processingquality_thresholds'),
                   model_uri=AK_SCHEMA.data_processingquality_thresholds, domain=None, range=str)

slots.data_processingprimer_match_cutoffs = Slot(uri=AK_SCHEMA.data_processingprimer_match_cutoffs, name="data_processingprimer_match_cutoffs", curie=AK_SCHEMA.curie('data_processingprimer_match_cutoffs'),
                   model_uri=AK_SCHEMA.data_processingprimer_match_cutoffs, domain=None, range=str)

slots.data_processingcollapsing_method = Slot(uri=AK_SCHEMA.data_processingcollapsing_method, name="data_processingcollapsing_method", curie=AK_SCHEMA.curie('data_processingcollapsing_method'),
                   model_uri=AK_SCHEMA.data_processingcollapsing_method, domain=None, range=str)

slots.data_processingdata_processing_protocols = Slot(uri=AK_SCHEMA.data_processingdata_processing_protocols, name="data_processingdata_processing_protocols", curie=AK_SCHEMA.curie('data_processingdata_processing_protocols'),
                   model_uri=AK_SCHEMA.data_processingdata_processing_protocols, domain=None, range=str)

slots.data_processingdata_processing_files = Slot(uri=AK_SCHEMA.data_processingdata_processing_files, name="data_processingdata_processing_files", curie=AK_SCHEMA.curie('data_processingdata_processing_files'),
                   model_uri=AK_SCHEMA.data_processingdata_processing_files, domain=None, range=Optional[Union[str, List[str]]])

slots.data_processinggermline_database = Slot(uri=AK_SCHEMA.data_processinggermline_database, name="data_processinggermline_database", curie=AK_SCHEMA.curie('data_processinggermline_database'),
                   model_uri=AK_SCHEMA.data_processinggermline_database, domain=None, range=str)

slots.data_processinggermline_set_ref = Slot(uri=AK_SCHEMA.data_processinggermline_set_ref, name="data_processinggermline_set_ref", curie=AK_SCHEMA.curie('data_processinggermline_set_ref'),
                   model_uri=AK_SCHEMA.data_processinggermline_set_ref, domain=None, range=Optional[str])

slots.data_processinganalysis_provenance_id = Slot(uri=AK_SCHEMA.data_processinganalysis_provenance_id, name="data_processinganalysis_provenance_id", curie=AK_SCHEMA.curie('data_processinganalysis_provenance_id'),
                   model_uri=AK_SCHEMA.data_processinganalysis_provenance_id, domain=None, range=Optional[str])

slots.repertoirerepertoire_id = Slot(uri=AK_SCHEMA.repertoirerepertoire_id, name="repertoirerepertoire_id", curie=AK_SCHEMA.curie('repertoirerepertoire_id'),
                   model_uri=AK_SCHEMA.repertoirerepertoire_id, domain=None, range=Optional[str])

slots.repertoirerepertoire_name = Slot(uri=AK_SCHEMA.repertoirerepertoire_name, name="repertoirerepertoire_name", curie=AK_SCHEMA.curie('repertoirerepertoire_name'),
                   model_uri=AK_SCHEMA.repertoirerepertoire_name, domain=None, range=Optional[str])

slots.repertoirerepertoire_description = Slot(uri=AK_SCHEMA.repertoirerepertoire_description, name="repertoirerepertoire_description", curie=AK_SCHEMA.curie('repertoirerepertoire_description'),
                   model_uri=AK_SCHEMA.repertoirerepertoire_description, domain=None, range=Optional[str])

slots.repertoirestudy = Slot(uri=AK_SCHEMA.repertoirestudy, name="repertoirestudy", curie=AK_SCHEMA.curie('repertoirestudy'),
                   model_uri=AK_SCHEMA.repertoirestudy, domain=None, range=Union[dict, V1p4Study])

slots.repertoiresubject = Slot(uri=AK_SCHEMA.repertoiresubject, name="repertoiresubject", curie=AK_SCHEMA.curie('repertoiresubject'),
                   model_uri=AK_SCHEMA.repertoiresubject, domain=None, range=Union[dict, V1p4Subject])

slots.repertoiresample = Slot(uri=AK_SCHEMA.repertoiresample, name="repertoiresample", curie=AK_SCHEMA.curie('repertoiresample'),
                   model_uri=AK_SCHEMA.repertoiresample, domain=None, range=Union[Union[dict, V1p4SampleProcessing], List[Union[dict, V1p4SampleProcessing]]])

slots.repertoiredata_processing = Slot(uri=AK_SCHEMA.repertoiredata_processing, name="repertoiredata_processing", curie=AK_SCHEMA.curie('repertoiredata_processing'),
                   model_uri=AK_SCHEMA.repertoiredata_processing, domain=None, range=Union[Union[dict, V1p4DataProcessing], List[Union[dict, V1p4DataProcessing]]])

slots.repertoire_grouprepertoire_group_id = Slot(uri=AK_SCHEMA.repertoire_grouprepertoire_group_id, name="repertoire_grouprepertoire_group_id", curie=AK_SCHEMA.curie('repertoire_grouprepertoire_group_id'),
                   model_uri=AK_SCHEMA.repertoire_grouprepertoire_group_id, domain=None, range=str)

slots.repertoire_grouprepertoire_group_name = Slot(uri=AK_SCHEMA.repertoire_grouprepertoire_group_name, name="repertoire_grouprepertoire_group_name", curie=AK_SCHEMA.curie('repertoire_grouprepertoire_group_name'),
                   model_uri=AK_SCHEMA.repertoire_grouprepertoire_group_name, domain=None, range=Optional[str])

slots.repertoire_grouprepertoire_group_description = Slot(uri=AK_SCHEMA.repertoire_grouprepertoire_group_description, name="repertoire_grouprepertoire_group_description", curie=AK_SCHEMA.curie('repertoire_grouprepertoire_group_description'),
                   model_uri=AK_SCHEMA.repertoire_grouprepertoire_group_description, domain=None, range=Optional[str])

slots.repertoire_grouprepertoires = Slot(uri=AK_SCHEMA.repertoire_grouprepertoires, name="repertoire_grouprepertoires", curie=AK_SCHEMA.curie('repertoire_grouprepertoires'),
                   model_uri=AK_SCHEMA.repertoire_grouprepertoires, domain=None, range=Union[str, List[str]])

slots.alignmentsequence_id = Slot(uri=AK_SCHEMA.alignmentsequence_id, name="alignmentsequence_id", curie=AK_SCHEMA.curie('alignmentsequence_id'),
                   model_uri=AK_SCHEMA.alignmentsequence_id, domain=None, range=str)

slots.alignmentsegment = Slot(uri=AK_SCHEMA.alignmentsegment, name="alignmentsegment", curie=AK_SCHEMA.curie('alignmentsegment'),
                   model_uri=AK_SCHEMA.alignmentsegment, domain=None, range=str)

slots.alignmentrev_comp = Slot(uri=AK_SCHEMA.alignmentrev_comp, name="alignmentrev_comp", curie=AK_SCHEMA.curie('alignmentrev_comp'),
                   model_uri=AK_SCHEMA.alignmentrev_comp, domain=None, range=Optional[Union[bool, Bool]])

slots.alignmentcall = Slot(uri=AK_SCHEMA.alignmentcall, name="alignmentcall", curie=AK_SCHEMA.curie('alignmentcall'),
                   model_uri=AK_SCHEMA.alignmentcall, domain=None, range=str)

slots.alignmentscore = Slot(uri=AK_SCHEMA.alignmentscore, name="alignmentscore", curie=AK_SCHEMA.curie('alignmentscore'),
                   model_uri=AK_SCHEMA.alignmentscore, domain=None, range=float)

slots.alignmentidentity = Slot(uri=AK_SCHEMA.alignmentidentity, name="alignmentidentity", curie=AK_SCHEMA.curie('alignmentidentity'),
                   model_uri=AK_SCHEMA.alignmentidentity, domain=None, range=Optional[float])

slots.alignmentsupport = Slot(uri=AK_SCHEMA.alignmentsupport, name="alignmentsupport", curie=AK_SCHEMA.curie('alignmentsupport'),
                   model_uri=AK_SCHEMA.alignmentsupport, domain=None, range=Optional[float])

slots.alignmentcigar = Slot(uri=AK_SCHEMA.alignmentcigar, name="alignmentcigar", curie=AK_SCHEMA.curie('alignmentcigar'),
                   model_uri=AK_SCHEMA.alignmentcigar, domain=None, range=str)

slots.alignmentsequence_start = Slot(uri=AK_SCHEMA.alignmentsequence_start, name="alignmentsequence_start", curie=AK_SCHEMA.curie('alignmentsequence_start'),
                   model_uri=AK_SCHEMA.alignmentsequence_start, domain=None, range=Optional[int])

slots.alignmentsequence_end = Slot(uri=AK_SCHEMA.alignmentsequence_end, name="alignmentsequence_end", curie=AK_SCHEMA.curie('alignmentsequence_end'),
                   model_uri=AK_SCHEMA.alignmentsequence_end, domain=None, range=Optional[int])

slots.alignmentgermline_start = Slot(uri=AK_SCHEMA.alignmentgermline_start, name="alignmentgermline_start", curie=AK_SCHEMA.curie('alignmentgermline_start'),
                   model_uri=AK_SCHEMA.alignmentgermline_start, domain=None, range=Optional[int])

slots.alignmentgermline_end = Slot(uri=AK_SCHEMA.alignmentgermline_end, name="alignmentgermline_end", curie=AK_SCHEMA.curie('alignmentgermline_end'),
                   model_uri=AK_SCHEMA.alignmentgermline_end, domain=None, range=Optional[int])

slots.alignmentrank = Slot(uri=AK_SCHEMA.alignmentrank, name="alignmentrank", curie=AK_SCHEMA.curie('alignmentrank'),
                   model_uri=AK_SCHEMA.alignmentrank, domain=None, range=Optional[int])

slots.alignmentdata_processing_id = Slot(uri=AK_SCHEMA.alignmentdata_processing_id, name="alignmentdata_processing_id", curie=AK_SCHEMA.curie('alignmentdata_processing_id'),
                   model_uri=AK_SCHEMA.alignmentdata_processing_id, domain=None, range=Optional[str])

slots.rearrangementsequence_id = Slot(uri=AK_SCHEMA.rearrangementsequence_id, name="rearrangementsequence_id", curie=AK_SCHEMA.curie('rearrangementsequence_id'),
                   model_uri=AK_SCHEMA.rearrangementsequence_id, domain=None, range=str)

slots.rearrangementsequence = Slot(uri=AK_SCHEMA.rearrangementsequence, name="rearrangementsequence", curie=AK_SCHEMA.curie('rearrangementsequence'),
                   model_uri=AK_SCHEMA.rearrangementsequence, domain=None, range=str)

slots.rearrangementquality = Slot(uri=AK_SCHEMA.rearrangementquality, name="rearrangementquality", curie=AK_SCHEMA.curie('rearrangementquality'),
                   model_uri=AK_SCHEMA.rearrangementquality, domain=None, range=Optional[str])

slots.rearrangementsequence_aa = Slot(uri=AK_SCHEMA.rearrangementsequence_aa, name="rearrangementsequence_aa", curie=AK_SCHEMA.curie('rearrangementsequence_aa'),
                   model_uri=AK_SCHEMA.rearrangementsequence_aa, domain=None, range=Optional[str])

slots.rearrangementrev_comp = Slot(uri=AK_SCHEMA.rearrangementrev_comp, name="rearrangementrev_comp", curie=AK_SCHEMA.curie('rearrangementrev_comp'),
                   model_uri=AK_SCHEMA.rearrangementrev_comp, domain=None, range=Union[bool, Bool])

slots.rearrangementproductive = Slot(uri=AK_SCHEMA.rearrangementproductive, name="rearrangementproductive", curie=AK_SCHEMA.curie('rearrangementproductive'),
                   model_uri=AK_SCHEMA.rearrangementproductive, domain=None, range=Union[bool, Bool])

slots.rearrangementvj_in_frame = Slot(uri=AK_SCHEMA.rearrangementvj_in_frame, name="rearrangementvj_in_frame", curie=AK_SCHEMA.curie('rearrangementvj_in_frame'),
                   model_uri=AK_SCHEMA.rearrangementvj_in_frame, domain=None, range=Optional[Union[bool, Bool]])

slots.rearrangementstop_codon = Slot(uri=AK_SCHEMA.rearrangementstop_codon, name="rearrangementstop_codon", curie=AK_SCHEMA.curie('rearrangementstop_codon'),
                   model_uri=AK_SCHEMA.rearrangementstop_codon, domain=None, range=Optional[Union[bool, Bool]])

slots.rearrangementcomplete_vdj = Slot(uri=AK_SCHEMA.rearrangementcomplete_vdj, name="rearrangementcomplete_vdj", curie=AK_SCHEMA.curie('rearrangementcomplete_vdj'),
                   model_uri=AK_SCHEMA.rearrangementcomplete_vdj, domain=None, range=Optional[Union[bool, Bool]])

slots.rearrangementlocus = Slot(uri=AK_SCHEMA.rearrangementlocus, name="rearrangementlocus", curie=AK_SCHEMA.curie('rearrangementlocus'),
                   model_uri=AK_SCHEMA.rearrangementlocus, domain=None, range=Optional[Union[str, "V1p4Locus"]])

slots.rearrangementlocus_species = Slot(uri=AK_SCHEMA.rearrangementlocus_species, name="rearrangementlocus_species", curie=AK_SCHEMA.curie('rearrangementlocus_species'),
                   model_uri=AK_SCHEMA.rearrangementlocus_species, domain=None, range=Optional[Union[str, "V1p4LocusSpecies"]])

slots.rearrangementv_call = Slot(uri=AK_SCHEMA.rearrangementv_call, name="rearrangementv_call", curie=AK_SCHEMA.curie('rearrangementv_call'),
                   model_uri=AK_SCHEMA.rearrangementv_call, domain=None, range=str)

slots.rearrangementd_call = Slot(uri=AK_SCHEMA.rearrangementd_call, name="rearrangementd_call", curie=AK_SCHEMA.curie('rearrangementd_call'),
                   model_uri=AK_SCHEMA.rearrangementd_call, domain=None, range=str)

slots.rearrangementd2_call = Slot(uri=AK_SCHEMA.rearrangementd2_call, name="rearrangementd2_call", curie=AK_SCHEMA.curie('rearrangementd2_call'),
                   model_uri=AK_SCHEMA.rearrangementd2_call, domain=None, range=Optional[str])

slots.rearrangementj_call = Slot(uri=AK_SCHEMA.rearrangementj_call, name="rearrangementj_call", curie=AK_SCHEMA.curie('rearrangementj_call'),
                   model_uri=AK_SCHEMA.rearrangementj_call, domain=None, range=str)

slots.rearrangementc_call = Slot(uri=AK_SCHEMA.rearrangementc_call, name="rearrangementc_call", curie=AK_SCHEMA.curie('rearrangementc_call'),
                   model_uri=AK_SCHEMA.rearrangementc_call, domain=None, range=Optional[str])

slots.rearrangementsequence_alignment = Slot(uri=AK_SCHEMA.rearrangementsequence_alignment, name="rearrangementsequence_alignment", curie=AK_SCHEMA.curie('rearrangementsequence_alignment'),
                   model_uri=AK_SCHEMA.rearrangementsequence_alignment, domain=None, range=str)

slots.rearrangementquality_alignment = Slot(uri=AK_SCHEMA.rearrangementquality_alignment, name="rearrangementquality_alignment", curie=AK_SCHEMA.curie('rearrangementquality_alignment'),
                   model_uri=AK_SCHEMA.rearrangementquality_alignment, domain=None, range=Optional[str])

slots.rearrangementsequence_alignment_aa = Slot(uri=AK_SCHEMA.rearrangementsequence_alignment_aa, name="rearrangementsequence_alignment_aa", curie=AK_SCHEMA.curie('rearrangementsequence_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangementsequence_alignment_aa, domain=None, range=Optional[str])

slots.rearrangementgermline_alignment = Slot(uri=AK_SCHEMA.rearrangementgermline_alignment, name="rearrangementgermline_alignment", curie=AK_SCHEMA.curie('rearrangementgermline_alignment'),
                   model_uri=AK_SCHEMA.rearrangementgermline_alignment, domain=None, range=str)

slots.rearrangementgermline_alignment_aa = Slot(uri=AK_SCHEMA.rearrangementgermline_alignment_aa, name="rearrangementgermline_alignment_aa", curie=AK_SCHEMA.curie('rearrangementgermline_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangementgermline_alignment_aa, domain=None, range=Optional[str])

slots.rearrangementjunction = Slot(uri=AK_SCHEMA.rearrangementjunction, name="rearrangementjunction", curie=AK_SCHEMA.curie('rearrangementjunction'),
                   model_uri=AK_SCHEMA.rearrangementjunction, domain=None, range=str)

slots.rearrangementjunction_aa = Slot(uri=AK_SCHEMA.rearrangementjunction_aa, name="rearrangementjunction_aa", curie=AK_SCHEMA.curie('rearrangementjunction_aa'),
                   model_uri=AK_SCHEMA.rearrangementjunction_aa, domain=None, range=str)

slots.rearrangementnp1 = Slot(uri=AK_SCHEMA.rearrangementnp1, name="rearrangementnp1", curie=AK_SCHEMA.curie('rearrangementnp1'),
                   model_uri=AK_SCHEMA.rearrangementnp1, domain=None, range=Optional[str])

slots.rearrangementnp1_aa = Slot(uri=AK_SCHEMA.rearrangementnp1_aa, name="rearrangementnp1_aa", curie=AK_SCHEMA.curie('rearrangementnp1_aa'),
                   model_uri=AK_SCHEMA.rearrangementnp1_aa, domain=None, range=Optional[str])

slots.rearrangementnp2 = Slot(uri=AK_SCHEMA.rearrangementnp2, name="rearrangementnp2", curie=AK_SCHEMA.curie('rearrangementnp2'),
                   model_uri=AK_SCHEMA.rearrangementnp2, domain=None, range=Optional[str])

slots.rearrangementnp2_aa = Slot(uri=AK_SCHEMA.rearrangementnp2_aa, name="rearrangementnp2_aa", curie=AK_SCHEMA.curie('rearrangementnp2_aa'),
                   model_uri=AK_SCHEMA.rearrangementnp2_aa, domain=None, range=Optional[str])

slots.rearrangementnp3 = Slot(uri=AK_SCHEMA.rearrangementnp3, name="rearrangementnp3", curie=AK_SCHEMA.curie('rearrangementnp3'),
                   model_uri=AK_SCHEMA.rearrangementnp3, domain=None, range=Optional[str])

slots.rearrangementnp3_aa = Slot(uri=AK_SCHEMA.rearrangementnp3_aa, name="rearrangementnp3_aa", curie=AK_SCHEMA.curie('rearrangementnp3_aa'),
                   model_uri=AK_SCHEMA.rearrangementnp3_aa, domain=None, range=Optional[str])

slots.rearrangementcdr1 = Slot(uri=AK_SCHEMA.rearrangementcdr1, name="rearrangementcdr1", curie=AK_SCHEMA.curie('rearrangementcdr1'),
                   model_uri=AK_SCHEMA.rearrangementcdr1, domain=None, range=Optional[str])

slots.rearrangementcdr1_aa = Slot(uri=AK_SCHEMA.rearrangementcdr1_aa, name="rearrangementcdr1_aa", curie=AK_SCHEMA.curie('rearrangementcdr1_aa'),
                   model_uri=AK_SCHEMA.rearrangementcdr1_aa, domain=None, range=Optional[str])

slots.rearrangementcdr2 = Slot(uri=AK_SCHEMA.rearrangementcdr2, name="rearrangementcdr2", curie=AK_SCHEMA.curie('rearrangementcdr2'),
                   model_uri=AK_SCHEMA.rearrangementcdr2, domain=None, range=Optional[str])

slots.rearrangementcdr2_aa = Slot(uri=AK_SCHEMA.rearrangementcdr2_aa, name="rearrangementcdr2_aa", curie=AK_SCHEMA.curie('rearrangementcdr2_aa'),
                   model_uri=AK_SCHEMA.rearrangementcdr2_aa, domain=None, range=Optional[str])

slots.rearrangementcdr3 = Slot(uri=AK_SCHEMA.rearrangementcdr3, name="rearrangementcdr3", curie=AK_SCHEMA.curie('rearrangementcdr3'),
                   model_uri=AK_SCHEMA.rearrangementcdr3, domain=None, range=Optional[str])

slots.rearrangementcdr3_aa = Slot(uri=AK_SCHEMA.rearrangementcdr3_aa, name="rearrangementcdr3_aa", curie=AK_SCHEMA.curie('rearrangementcdr3_aa'),
                   model_uri=AK_SCHEMA.rearrangementcdr3_aa, domain=None, range=Optional[str])

slots.rearrangementfwr1 = Slot(uri=AK_SCHEMA.rearrangementfwr1, name="rearrangementfwr1", curie=AK_SCHEMA.curie('rearrangementfwr1'),
                   model_uri=AK_SCHEMA.rearrangementfwr1, domain=None, range=Optional[str])

slots.rearrangementfwr1_aa = Slot(uri=AK_SCHEMA.rearrangementfwr1_aa, name="rearrangementfwr1_aa", curie=AK_SCHEMA.curie('rearrangementfwr1_aa'),
                   model_uri=AK_SCHEMA.rearrangementfwr1_aa, domain=None, range=Optional[str])

slots.rearrangementfwr2 = Slot(uri=AK_SCHEMA.rearrangementfwr2, name="rearrangementfwr2", curie=AK_SCHEMA.curie('rearrangementfwr2'),
                   model_uri=AK_SCHEMA.rearrangementfwr2, domain=None, range=Optional[str])

slots.rearrangementfwr2_aa = Slot(uri=AK_SCHEMA.rearrangementfwr2_aa, name="rearrangementfwr2_aa", curie=AK_SCHEMA.curie('rearrangementfwr2_aa'),
                   model_uri=AK_SCHEMA.rearrangementfwr2_aa, domain=None, range=Optional[str])

slots.rearrangementfwr3 = Slot(uri=AK_SCHEMA.rearrangementfwr3, name="rearrangementfwr3", curie=AK_SCHEMA.curie('rearrangementfwr3'),
                   model_uri=AK_SCHEMA.rearrangementfwr3, domain=None, range=Optional[str])

slots.rearrangementfwr3_aa = Slot(uri=AK_SCHEMA.rearrangementfwr3_aa, name="rearrangementfwr3_aa", curie=AK_SCHEMA.curie('rearrangementfwr3_aa'),
                   model_uri=AK_SCHEMA.rearrangementfwr3_aa, domain=None, range=Optional[str])

slots.rearrangementfwr4 = Slot(uri=AK_SCHEMA.rearrangementfwr4, name="rearrangementfwr4", curie=AK_SCHEMA.curie('rearrangementfwr4'),
                   model_uri=AK_SCHEMA.rearrangementfwr4, domain=None, range=Optional[str])

slots.rearrangementfwr4_aa = Slot(uri=AK_SCHEMA.rearrangementfwr4_aa, name="rearrangementfwr4_aa", curie=AK_SCHEMA.curie('rearrangementfwr4_aa'),
                   model_uri=AK_SCHEMA.rearrangementfwr4_aa, domain=None, range=Optional[str])

slots.rearrangementv_score = Slot(uri=AK_SCHEMA.rearrangementv_score, name="rearrangementv_score", curie=AK_SCHEMA.curie('rearrangementv_score'),
                   model_uri=AK_SCHEMA.rearrangementv_score, domain=None, range=Optional[float])

slots.rearrangementv_identity = Slot(uri=AK_SCHEMA.rearrangementv_identity, name="rearrangementv_identity", curie=AK_SCHEMA.curie('rearrangementv_identity'),
                   model_uri=AK_SCHEMA.rearrangementv_identity, domain=None, range=Optional[float])

slots.rearrangementv_support = Slot(uri=AK_SCHEMA.rearrangementv_support, name="rearrangementv_support", curie=AK_SCHEMA.curie('rearrangementv_support'),
                   model_uri=AK_SCHEMA.rearrangementv_support, domain=None, range=Optional[float])

slots.rearrangementv_cigar = Slot(uri=AK_SCHEMA.rearrangementv_cigar, name="rearrangementv_cigar", curie=AK_SCHEMA.curie('rearrangementv_cigar'),
                   model_uri=AK_SCHEMA.rearrangementv_cigar, domain=None, range=str)

slots.rearrangementd_score = Slot(uri=AK_SCHEMA.rearrangementd_score, name="rearrangementd_score", curie=AK_SCHEMA.curie('rearrangementd_score'),
                   model_uri=AK_SCHEMA.rearrangementd_score, domain=None, range=Optional[float])

slots.rearrangementd_identity = Slot(uri=AK_SCHEMA.rearrangementd_identity, name="rearrangementd_identity", curie=AK_SCHEMA.curie('rearrangementd_identity'),
                   model_uri=AK_SCHEMA.rearrangementd_identity, domain=None, range=Optional[float])

slots.rearrangementd_support = Slot(uri=AK_SCHEMA.rearrangementd_support, name="rearrangementd_support", curie=AK_SCHEMA.curie('rearrangementd_support'),
                   model_uri=AK_SCHEMA.rearrangementd_support, domain=None, range=Optional[float])

slots.rearrangementd_cigar = Slot(uri=AK_SCHEMA.rearrangementd_cigar, name="rearrangementd_cigar", curie=AK_SCHEMA.curie('rearrangementd_cigar'),
                   model_uri=AK_SCHEMA.rearrangementd_cigar, domain=None, range=str)

slots.rearrangementd2_score = Slot(uri=AK_SCHEMA.rearrangementd2_score, name="rearrangementd2_score", curie=AK_SCHEMA.curie('rearrangementd2_score'),
                   model_uri=AK_SCHEMA.rearrangementd2_score, domain=None, range=Optional[float])

slots.rearrangementd2_identity = Slot(uri=AK_SCHEMA.rearrangementd2_identity, name="rearrangementd2_identity", curie=AK_SCHEMA.curie('rearrangementd2_identity'),
                   model_uri=AK_SCHEMA.rearrangementd2_identity, domain=None, range=Optional[float])

slots.rearrangementd2_support = Slot(uri=AK_SCHEMA.rearrangementd2_support, name="rearrangementd2_support", curie=AK_SCHEMA.curie('rearrangementd2_support'),
                   model_uri=AK_SCHEMA.rearrangementd2_support, domain=None, range=Optional[float])

slots.rearrangementd2_cigar = Slot(uri=AK_SCHEMA.rearrangementd2_cigar, name="rearrangementd2_cigar", curie=AK_SCHEMA.curie('rearrangementd2_cigar'),
                   model_uri=AK_SCHEMA.rearrangementd2_cigar, domain=None, range=Optional[str])

slots.rearrangementj_score = Slot(uri=AK_SCHEMA.rearrangementj_score, name="rearrangementj_score", curie=AK_SCHEMA.curie('rearrangementj_score'),
                   model_uri=AK_SCHEMA.rearrangementj_score, domain=None, range=Optional[float])

slots.rearrangementj_identity = Slot(uri=AK_SCHEMA.rearrangementj_identity, name="rearrangementj_identity", curie=AK_SCHEMA.curie('rearrangementj_identity'),
                   model_uri=AK_SCHEMA.rearrangementj_identity, domain=None, range=Optional[float])

slots.rearrangementj_support = Slot(uri=AK_SCHEMA.rearrangementj_support, name="rearrangementj_support", curie=AK_SCHEMA.curie('rearrangementj_support'),
                   model_uri=AK_SCHEMA.rearrangementj_support, domain=None, range=Optional[float])

slots.rearrangementj_cigar = Slot(uri=AK_SCHEMA.rearrangementj_cigar, name="rearrangementj_cigar", curie=AK_SCHEMA.curie('rearrangementj_cigar'),
                   model_uri=AK_SCHEMA.rearrangementj_cigar, domain=None, range=str)

slots.rearrangementc_score = Slot(uri=AK_SCHEMA.rearrangementc_score, name="rearrangementc_score", curie=AK_SCHEMA.curie('rearrangementc_score'),
                   model_uri=AK_SCHEMA.rearrangementc_score, domain=None, range=Optional[float])

slots.rearrangementc_identity = Slot(uri=AK_SCHEMA.rearrangementc_identity, name="rearrangementc_identity", curie=AK_SCHEMA.curie('rearrangementc_identity'),
                   model_uri=AK_SCHEMA.rearrangementc_identity, domain=None, range=Optional[float])

slots.rearrangementc_support = Slot(uri=AK_SCHEMA.rearrangementc_support, name="rearrangementc_support", curie=AK_SCHEMA.curie('rearrangementc_support'),
                   model_uri=AK_SCHEMA.rearrangementc_support, domain=None, range=Optional[float])

slots.rearrangementc_cigar = Slot(uri=AK_SCHEMA.rearrangementc_cigar, name="rearrangementc_cigar", curie=AK_SCHEMA.curie('rearrangementc_cigar'),
                   model_uri=AK_SCHEMA.rearrangementc_cigar, domain=None, range=Optional[str])

slots.rearrangementv_sequence_start = Slot(uri=AK_SCHEMA.rearrangementv_sequence_start, name="rearrangementv_sequence_start", curie=AK_SCHEMA.curie('rearrangementv_sequence_start'),
                   model_uri=AK_SCHEMA.rearrangementv_sequence_start, domain=None, range=Optional[int])

slots.rearrangementv_sequence_end = Slot(uri=AK_SCHEMA.rearrangementv_sequence_end, name="rearrangementv_sequence_end", curie=AK_SCHEMA.curie('rearrangementv_sequence_end'),
                   model_uri=AK_SCHEMA.rearrangementv_sequence_end, domain=None, range=Optional[int])

slots.rearrangementv_germline_start = Slot(uri=AK_SCHEMA.rearrangementv_germline_start, name="rearrangementv_germline_start", curie=AK_SCHEMA.curie('rearrangementv_germline_start'),
                   model_uri=AK_SCHEMA.rearrangementv_germline_start, domain=None, range=Optional[int])

slots.rearrangementv_germline_end = Slot(uri=AK_SCHEMA.rearrangementv_germline_end, name="rearrangementv_germline_end", curie=AK_SCHEMA.curie('rearrangementv_germline_end'),
                   model_uri=AK_SCHEMA.rearrangementv_germline_end, domain=None, range=Optional[int])

slots.rearrangementv_alignment_start = Slot(uri=AK_SCHEMA.rearrangementv_alignment_start, name="rearrangementv_alignment_start", curie=AK_SCHEMA.curie('rearrangementv_alignment_start'),
                   model_uri=AK_SCHEMA.rearrangementv_alignment_start, domain=None, range=Optional[int])

slots.rearrangementv_alignment_end = Slot(uri=AK_SCHEMA.rearrangementv_alignment_end, name="rearrangementv_alignment_end", curie=AK_SCHEMA.curie('rearrangementv_alignment_end'),
                   model_uri=AK_SCHEMA.rearrangementv_alignment_end, domain=None, range=Optional[int])

slots.rearrangementd_sequence_start = Slot(uri=AK_SCHEMA.rearrangementd_sequence_start, name="rearrangementd_sequence_start", curie=AK_SCHEMA.curie('rearrangementd_sequence_start'),
                   model_uri=AK_SCHEMA.rearrangementd_sequence_start, domain=None, range=Optional[int])

slots.rearrangementd_sequence_end = Slot(uri=AK_SCHEMA.rearrangementd_sequence_end, name="rearrangementd_sequence_end", curie=AK_SCHEMA.curie('rearrangementd_sequence_end'),
                   model_uri=AK_SCHEMA.rearrangementd_sequence_end, domain=None, range=Optional[int])

slots.rearrangementd_germline_start = Slot(uri=AK_SCHEMA.rearrangementd_germline_start, name="rearrangementd_germline_start", curie=AK_SCHEMA.curie('rearrangementd_germline_start'),
                   model_uri=AK_SCHEMA.rearrangementd_germline_start, domain=None, range=Optional[int])

slots.rearrangementd_germline_end = Slot(uri=AK_SCHEMA.rearrangementd_germline_end, name="rearrangementd_germline_end", curie=AK_SCHEMA.curie('rearrangementd_germline_end'),
                   model_uri=AK_SCHEMA.rearrangementd_germline_end, domain=None, range=Optional[int])

slots.rearrangementd_alignment_start = Slot(uri=AK_SCHEMA.rearrangementd_alignment_start, name="rearrangementd_alignment_start", curie=AK_SCHEMA.curie('rearrangementd_alignment_start'),
                   model_uri=AK_SCHEMA.rearrangementd_alignment_start, domain=None, range=Optional[int])

slots.rearrangementd_alignment_end = Slot(uri=AK_SCHEMA.rearrangementd_alignment_end, name="rearrangementd_alignment_end", curie=AK_SCHEMA.curie('rearrangementd_alignment_end'),
                   model_uri=AK_SCHEMA.rearrangementd_alignment_end, domain=None, range=Optional[int])

slots.rearrangementd2_sequence_start = Slot(uri=AK_SCHEMA.rearrangementd2_sequence_start, name="rearrangementd2_sequence_start", curie=AK_SCHEMA.curie('rearrangementd2_sequence_start'),
                   model_uri=AK_SCHEMA.rearrangementd2_sequence_start, domain=None, range=Optional[int])

slots.rearrangementd2_sequence_end = Slot(uri=AK_SCHEMA.rearrangementd2_sequence_end, name="rearrangementd2_sequence_end", curie=AK_SCHEMA.curie('rearrangementd2_sequence_end'),
                   model_uri=AK_SCHEMA.rearrangementd2_sequence_end, domain=None, range=Optional[int])

slots.rearrangementd2_germline_start = Slot(uri=AK_SCHEMA.rearrangementd2_germline_start, name="rearrangementd2_germline_start", curie=AK_SCHEMA.curie('rearrangementd2_germline_start'),
                   model_uri=AK_SCHEMA.rearrangementd2_germline_start, domain=None, range=Optional[int])

slots.rearrangementd2_germline_end = Slot(uri=AK_SCHEMA.rearrangementd2_germline_end, name="rearrangementd2_germline_end", curie=AK_SCHEMA.curie('rearrangementd2_germline_end'),
                   model_uri=AK_SCHEMA.rearrangementd2_germline_end, domain=None, range=Optional[int])

slots.rearrangementd2_alignment_start = Slot(uri=AK_SCHEMA.rearrangementd2_alignment_start, name="rearrangementd2_alignment_start", curie=AK_SCHEMA.curie('rearrangementd2_alignment_start'),
                   model_uri=AK_SCHEMA.rearrangementd2_alignment_start, domain=None, range=Optional[int])

slots.rearrangementd2_alignment_end = Slot(uri=AK_SCHEMA.rearrangementd2_alignment_end, name="rearrangementd2_alignment_end", curie=AK_SCHEMA.curie('rearrangementd2_alignment_end'),
                   model_uri=AK_SCHEMA.rearrangementd2_alignment_end, domain=None, range=Optional[int])

slots.rearrangementj_sequence_start = Slot(uri=AK_SCHEMA.rearrangementj_sequence_start, name="rearrangementj_sequence_start", curie=AK_SCHEMA.curie('rearrangementj_sequence_start'),
                   model_uri=AK_SCHEMA.rearrangementj_sequence_start, domain=None, range=Optional[int])

slots.rearrangementj_sequence_end = Slot(uri=AK_SCHEMA.rearrangementj_sequence_end, name="rearrangementj_sequence_end", curie=AK_SCHEMA.curie('rearrangementj_sequence_end'),
                   model_uri=AK_SCHEMA.rearrangementj_sequence_end, domain=None, range=Optional[int])

slots.rearrangementj_germline_start = Slot(uri=AK_SCHEMA.rearrangementj_germline_start, name="rearrangementj_germline_start", curie=AK_SCHEMA.curie('rearrangementj_germline_start'),
                   model_uri=AK_SCHEMA.rearrangementj_germline_start, domain=None, range=Optional[int])

slots.rearrangementj_germline_end = Slot(uri=AK_SCHEMA.rearrangementj_germline_end, name="rearrangementj_germline_end", curie=AK_SCHEMA.curie('rearrangementj_germline_end'),
                   model_uri=AK_SCHEMA.rearrangementj_germline_end, domain=None, range=Optional[int])

slots.rearrangementj_alignment_start = Slot(uri=AK_SCHEMA.rearrangementj_alignment_start, name="rearrangementj_alignment_start", curie=AK_SCHEMA.curie('rearrangementj_alignment_start'),
                   model_uri=AK_SCHEMA.rearrangementj_alignment_start, domain=None, range=Optional[int])

slots.rearrangementj_alignment_end = Slot(uri=AK_SCHEMA.rearrangementj_alignment_end, name="rearrangementj_alignment_end", curie=AK_SCHEMA.curie('rearrangementj_alignment_end'),
                   model_uri=AK_SCHEMA.rearrangementj_alignment_end, domain=None, range=Optional[int])

slots.rearrangementc_sequence_start = Slot(uri=AK_SCHEMA.rearrangementc_sequence_start, name="rearrangementc_sequence_start", curie=AK_SCHEMA.curie('rearrangementc_sequence_start'),
                   model_uri=AK_SCHEMA.rearrangementc_sequence_start, domain=None, range=Optional[int])

slots.rearrangementc_sequence_end = Slot(uri=AK_SCHEMA.rearrangementc_sequence_end, name="rearrangementc_sequence_end", curie=AK_SCHEMA.curie('rearrangementc_sequence_end'),
                   model_uri=AK_SCHEMA.rearrangementc_sequence_end, domain=None, range=Optional[int])

slots.rearrangementc_germline_start = Slot(uri=AK_SCHEMA.rearrangementc_germline_start, name="rearrangementc_germline_start", curie=AK_SCHEMA.curie('rearrangementc_germline_start'),
                   model_uri=AK_SCHEMA.rearrangementc_germline_start, domain=None, range=Optional[int])

slots.rearrangementc_germline_end = Slot(uri=AK_SCHEMA.rearrangementc_germline_end, name="rearrangementc_germline_end", curie=AK_SCHEMA.curie('rearrangementc_germline_end'),
                   model_uri=AK_SCHEMA.rearrangementc_germline_end, domain=None, range=Optional[int])

slots.rearrangementc_alignment_start = Slot(uri=AK_SCHEMA.rearrangementc_alignment_start, name="rearrangementc_alignment_start", curie=AK_SCHEMA.curie('rearrangementc_alignment_start'),
                   model_uri=AK_SCHEMA.rearrangementc_alignment_start, domain=None, range=Optional[int])

slots.rearrangementc_alignment_end = Slot(uri=AK_SCHEMA.rearrangementc_alignment_end, name="rearrangementc_alignment_end", curie=AK_SCHEMA.curie('rearrangementc_alignment_end'),
                   model_uri=AK_SCHEMA.rearrangementc_alignment_end, domain=None, range=Optional[int])

slots.rearrangementcdr1_start = Slot(uri=AK_SCHEMA.rearrangementcdr1_start, name="rearrangementcdr1_start", curie=AK_SCHEMA.curie('rearrangementcdr1_start'),
                   model_uri=AK_SCHEMA.rearrangementcdr1_start, domain=None, range=Optional[int])

slots.rearrangementcdr1_end = Slot(uri=AK_SCHEMA.rearrangementcdr1_end, name="rearrangementcdr1_end", curie=AK_SCHEMA.curie('rearrangementcdr1_end'),
                   model_uri=AK_SCHEMA.rearrangementcdr1_end, domain=None, range=Optional[int])

slots.rearrangementcdr2_start = Slot(uri=AK_SCHEMA.rearrangementcdr2_start, name="rearrangementcdr2_start", curie=AK_SCHEMA.curie('rearrangementcdr2_start'),
                   model_uri=AK_SCHEMA.rearrangementcdr2_start, domain=None, range=Optional[int])

slots.rearrangementcdr2_end = Slot(uri=AK_SCHEMA.rearrangementcdr2_end, name="rearrangementcdr2_end", curie=AK_SCHEMA.curie('rearrangementcdr2_end'),
                   model_uri=AK_SCHEMA.rearrangementcdr2_end, domain=None, range=Optional[int])

slots.rearrangementcdr3_start = Slot(uri=AK_SCHEMA.rearrangementcdr3_start, name="rearrangementcdr3_start", curie=AK_SCHEMA.curie('rearrangementcdr3_start'),
                   model_uri=AK_SCHEMA.rearrangementcdr3_start, domain=None, range=Optional[int])

slots.rearrangementcdr3_end = Slot(uri=AK_SCHEMA.rearrangementcdr3_end, name="rearrangementcdr3_end", curie=AK_SCHEMA.curie('rearrangementcdr3_end'),
                   model_uri=AK_SCHEMA.rearrangementcdr3_end, domain=None, range=Optional[int])

slots.rearrangementfwr1_start = Slot(uri=AK_SCHEMA.rearrangementfwr1_start, name="rearrangementfwr1_start", curie=AK_SCHEMA.curie('rearrangementfwr1_start'),
                   model_uri=AK_SCHEMA.rearrangementfwr1_start, domain=None, range=Optional[int])

slots.rearrangementfwr1_end = Slot(uri=AK_SCHEMA.rearrangementfwr1_end, name="rearrangementfwr1_end", curie=AK_SCHEMA.curie('rearrangementfwr1_end'),
                   model_uri=AK_SCHEMA.rearrangementfwr1_end, domain=None, range=Optional[int])

slots.rearrangementfwr2_start = Slot(uri=AK_SCHEMA.rearrangementfwr2_start, name="rearrangementfwr2_start", curie=AK_SCHEMA.curie('rearrangementfwr2_start'),
                   model_uri=AK_SCHEMA.rearrangementfwr2_start, domain=None, range=Optional[int])

slots.rearrangementfwr2_end = Slot(uri=AK_SCHEMA.rearrangementfwr2_end, name="rearrangementfwr2_end", curie=AK_SCHEMA.curie('rearrangementfwr2_end'),
                   model_uri=AK_SCHEMA.rearrangementfwr2_end, domain=None, range=Optional[int])

slots.rearrangementfwr3_start = Slot(uri=AK_SCHEMA.rearrangementfwr3_start, name="rearrangementfwr3_start", curie=AK_SCHEMA.curie('rearrangementfwr3_start'),
                   model_uri=AK_SCHEMA.rearrangementfwr3_start, domain=None, range=Optional[int])

slots.rearrangementfwr3_end = Slot(uri=AK_SCHEMA.rearrangementfwr3_end, name="rearrangementfwr3_end", curie=AK_SCHEMA.curie('rearrangementfwr3_end'),
                   model_uri=AK_SCHEMA.rearrangementfwr3_end, domain=None, range=Optional[int])

slots.rearrangementfwr4_start = Slot(uri=AK_SCHEMA.rearrangementfwr4_start, name="rearrangementfwr4_start", curie=AK_SCHEMA.curie('rearrangementfwr4_start'),
                   model_uri=AK_SCHEMA.rearrangementfwr4_start, domain=None, range=Optional[int])

slots.rearrangementfwr4_end = Slot(uri=AK_SCHEMA.rearrangementfwr4_end, name="rearrangementfwr4_end", curie=AK_SCHEMA.curie('rearrangementfwr4_end'),
                   model_uri=AK_SCHEMA.rearrangementfwr4_end, domain=None, range=Optional[int])

slots.rearrangementv_sequence_alignment = Slot(uri=AK_SCHEMA.rearrangementv_sequence_alignment, name="rearrangementv_sequence_alignment", curie=AK_SCHEMA.curie('rearrangementv_sequence_alignment'),
                   model_uri=AK_SCHEMA.rearrangementv_sequence_alignment, domain=None, range=Optional[str])

slots.rearrangementv_sequence_alignment_aa = Slot(uri=AK_SCHEMA.rearrangementv_sequence_alignment_aa, name="rearrangementv_sequence_alignment_aa", curie=AK_SCHEMA.curie('rearrangementv_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangementv_sequence_alignment_aa, domain=None, range=Optional[str])

slots.rearrangementd_sequence_alignment = Slot(uri=AK_SCHEMA.rearrangementd_sequence_alignment, name="rearrangementd_sequence_alignment", curie=AK_SCHEMA.curie('rearrangementd_sequence_alignment'),
                   model_uri=AK_SCHEMA.rearrangementd_sequence_alignment, domain=None, range=Optional[str])

slots.rearrangementd_sequence_alignment_aa = Slot(uri=AK_SCHEMA.rearrangementd_sequence_alignment_aa, name="rearrangementd_sequence_alignment_aa", curie=AK_SCHEMA.curie('rearrangementd_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangementd_sequence_alignment_aa, domain=None, range=Optional[str])

slots.rearrangementd2_sequence_alignment = Slot(uri=AK_SCHEMA.rearrangementd2_sequence_alignment, name="rearrangementd2_sequence_alignment", curie=AK_SCHEMA.curie('rearrangementd2_sequence_alignment'),
                   model_uri=AK_SCHEMA.rearrangementd2_sequence_alignment, domain=None, range=Optional[str])

slots.rearrangementd2_sequence_alignment_aa = Slot(uri=AK_SCHEMA.rearrangementd2_sequence_alignment_aa, name="rearrangementd2_sequence_alignment_aa", curie=AK_SCHEMA.curie('rearrangementd2_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangementd2_sequence_alignment_aa, domain=None, range=Optional[str])

slots.rearrangementj_sequence_alignment = Slot(uri=AK_SCHEMA.rearrangementj_sequence_alignment, name="rearrangementj_sequence_alignment", curie=AK_SCHEMA.curie('rearrangementj_sequence_alignment'),
                   model_uri=AK_SCHEMA.rearrangementj_sequence_alignment, domain=None, range=Optional[str])

slots.rearrangementj_sequence_alignment_aa = Slot(uri=AK_SCHEMA.rearrangementj_sequence_alignment_aa, name="rearrangementj_sequence_alignment_aa", curie=AK_SCHEMA.curie('rearrangementj_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangementj_sequence_alignment_aa, domain=None, range=Optional[str])

slots.rearrangementc_sequence_alignment = Slot(uri=AK_SCHEMA.rearrangementc_sequence_alignment, name="rearrangementc_sequence_alignment", curie=AK_SCHEMA.curie('rearrangementc_sequence_alignment'),
                   model_uri=AK_SCHEMA.rearrangementc_sequence_alignment, domain=None, range=Optional[str])

slots.rearrangementc_sequence_alignment_aa = Slot(uri=AK_SCHEMA.rearrangementc_sequence_alignment_aa, name="rearrangementc_sequence_alignment_aa", curie=AK_SCHEMA.curie('rearrangementc_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangementc_sequence_alignment_aa, domain=None, range=Optional[str])

slots.rearrangementv_germline_alignment = Slot(uri=AK_SCHEMA.rearrangementv_germline_alignment, name="rearrangementv_germline_alignment", curie=AK_SCHEMA.curie('rearrangementv_germline_alignment'),
                   model_uri=AK_SCHEMA.rearrangementv_germline_alignment, domain=None, range=Optional[str])

slots.rearrangementv_germline_alignment_aa = Slot(uri=AK_SCHEMA.rearrangementv_germline_alignment_aa, name="rearrangementv_germline_alignment_aa", curie=AK_SCHEMA.curie('rearrangementv_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangementv_germline_alignment_aa, domain=None, range=Optional[str])

slots.rearrangementd_germline_alignment = Slot(uri=AK_SCHEMA.rearrangementd_germline_alignment, name="rearrangementd_germline_alignment", curie=AK_SCHEMA.curie('rearrangementd_germline_alignment'),
                   model_uri=AK_SCHEMA.rearrangementd_germline_alignment, domain=None, range=Optional[str])

slots.rearrangementd_germline_alignment_aa = Slot(uri=AK_SCHEMA.rearrangementd_germline_alignment_aa, name="rearrangementd_germline_alignment_aa", curie=AK_SCHEMA.curie('rearrangementd_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangementd_germline_alignment_aa, domain=None, range=Optional[str])

slots.rearrangementd2_germline_alignment = Slot(uri=AK_SCHEMA.rearrangementd2_germline_alignment, name="rearrangementd2_germline_alignment", curie=AK_SCHEMA.curie('rearrangementd2_germline_alignment'),
                   model_uri=AK_SCHEMA.rearrangementd2_germline_alignment, domain=None, range=Optional[str])

slots.rearrangementd2_germline_alignment_aa = Slot(uri=AK_SCHEMA.rearrangementd2_germline_alignment_aa, name="rearrangementd2_germline_alignment_aa", curie=AK_SCHEMA.curie('rearrangementd2_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangementd2_germline_alignment_aa, domain=None, range=Optional[str])

slots.rearrangementj_germline_alignment = Slot(uri=AK_SCHEMA.rearrangementj_germline_alignment, name="rearrangementj_germline_alignment", curie=AK_SCHEMA.curie('rearrangementj_germline_alignment'),
                   model_uri=AK_SCHEMA.rearrangementj_germline_alignment, domain=None, range=Optional[str])

slots.rearrangementj_germline_alignment_aa = Slot(uri=AK_SCHEMA.rearrangementj_germline_alignment_aa, name="rearrangementj_germline_alignment_aa", curie=AK_SCHEMA.curie('rearrangementj_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangementj_germline_alignment_aa, domain=None, range=Optional[str])

slots.rearrangementc_germline_alignment = Slot(uri=AK_SCHEMA.rearrangementc_germline_alignment, name="rearrangementc_germline_alignment", curie=AK_SCHEMA.curie('rearrangementc_germline_alignment'),
                   model_uri=AK_SCHEMA.rearrangementc_germline_alignment, domain=None, range=Optional[str])

slots.rearrangementc_germline_alignment_aa = Slot(uri=AK_SCHEMA.rearrangementc_germline_alignment_aa, name="rearrangementc_germline_alignment_aa", curie=AK_SCHEMA.curie('rearrangementc_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangementc_germline_alignment_aa, domain=None, range=Optional[str])

slots.rearrangementjunction_length = Slot(uri=AK_SCHEMA.rearrangementjunction_length, name="rearrangementjunction_length", curie=AK_SCHEMA.curie('rearrangementjunction_length'),
                   model_uri=AK_SCHEMA.rearrangementjunction_length, domain=None, range=Optional[int])

slots.rearrangementjunction_aa_length = Slot(uri=AK_SCHEMA.rearrangementjunction_aa_length, name="rearrangementjunction_aa_length", curie=AK_SCHEMA.curie('rearrangementjunction_aa_length'),
                   model_uri=AK_SCHEMA.rearrangementjunction_aa_length, domain=None, range=Optional[int])

slots.rearrangementnp1_length = Slot(uri=AK_SCHEMA.rearrangementnp1_length, name="rearrangementnp1_length", curie=AK_SCHEMA.curie('rearrangementnp1_length'),
                   model_uri=AK_SCHEMA.rearrangementnp1_length, domain=None, range=Optional[int])

slots.rearrangementnp2_length = Slot(uri=AK_SCHEMA.rearrangementnp2_length, name="rearrangementnp2_length", curie=AK_SCHEMA.curie('rearrangementnp2_length'),
                   model_uri=AK_SCHEMA.rearrangementnp2_length, domain=None, range=Optional[int])

slots.rearrangementnp3_length = Slot(uri=AK_SCHEMA.rearrangementnp3_length, name="rearrangementnp3_length", curie=AK_SCHEMA.curie('rearrangementnp3_length'),
                   model_uri=AK_SCHEMA.rearrangementnp3_length, domain=None, range=Optional[int])

slots.rearrangementn1_length = Slot(uri=AK_SCHEMA.rearrangementn1_length, name="rearrangementn1_length", curie=AK_SCHEMA.curie('rearrangementn1_length'),
                   model_uri=AK_SCHEMA.rearrangementn1_length, domain=None, range=Optional[int])

slots.rearrangementn2_length = Slot(uri=AK_SCHEMA.rearrangementn2_length, name="rearrangementn2_length", curie=AK_SCHEMA.curie('rearrangementn2_length'),
                   model_uri=AK_SCHEMA.rearrangementn2_length, domain=None, range=Optional[int])

slots.rearrangementn3_length = Slot(uri=AK_SCHEMA.rearrangementn3_length, name="rearrangementn3_length", curie=AK_SCHEMA.curie('rearrangementn3_length'),
                   model_uri=AK_SCHEMA.rearrangementn3_length, domain=None, range=Optional[int])

slots.rearrangementp3v_length = Slot(uri=AK_SCHEMA.rearrangementp3v_length, name="rearrangementp3v_length", curie=AK_SCHEMA.curie('rearrangementp3v_length'),
                   model_uri=AK_SCHEMA.rearrangementp3v_length, domain=None, range=Optional[int])

slots.rearrangementp5d_length = Slot(uri=AK_SCHEMA.rearrangementp5d_length, name="rearrangementp5d_length", curie=AK_SCHEMA.curie('rearrangementp5d_length'),
                   model_uri=AK_SCHEMA.rearrangementp5d_length, domain=None, range=Optional[int])

slots.rearrangementp3d_length = Slot(uri=AK_SCHEMA.rearrangementp3d_length, name="rearrangementp3d_length", curie=AK_SCHEMA.curie('rearrangementp3d_length'),
                   model_uri=AK_SCHEMA.rearrangementp3d_length, domain=None, range=Optional[int])

slots.rearrangementp5d2_length = Slot(uri=AK_SCHEMA.rearrangementp5d2_length, name="rearrangementp5d2_length", curie=AK_SCHEMA.curie('rearrangementp5d2_length'),
                   model_uri=AK_SCHEMA.rearrangementp5d2_length, domain=None, range=Optional[int])

slots.rearrangementp3d2_length = Slot(uri=AK_SCHEMA.rearrangementp3d2_length, name="rearrangementp3d2_length", curie=AK_SCHEMA.curie('rearrangementp3d2_length'),
                   model_uri=AK_SCHEMA.rearrangementp3d2_length, domain=None, range=Optional[int])

slots.rearrangementp5j_length = Slot(uri=AK_SCHEMA.rearrangementp5j_length, name="rearrangementp5j_length", curie=AK_SCHEMA.curie('rearrangementp5j_length'),
                   model_uri=AK_SCHEMA.rearrangementp5j_length, domain=None, range=Optional[int])

slots.rearrangementv_frameshift = Slot(uri=AK_SCHEMA.rearrangementv_frameshift, name="rearrangementv_frameshift", curie=AK_SCHEMA.curie('rearrangementv_frameshift'),
                   model_uri=AK_SCHEMA.rearrangementv_frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.rearrangementj_frameshift = Slot(uri=AK_SCHEMA.rearrangementj_frameshift, name="rearrangementj_frameshift", curie=AK_SCHEMA.curie('rearrangementj_frameshift'),
                   model_uri=AK_SCHEMA.rearrangementj_frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.rearrangementd_frame = Slot(uri=AK_SCHEMA.rearrangementd_frame, name="rearrangementd_frame", curie=AK_SCHEMA.curie('rearrangementd_frame'),
                   model_uri=AK_SCHEMA.rearrangementd_frame, domain=None, range=Optional[int])

slots.rearrangementd2_frame = Slot(uri=AK_SCHEMA.rearrangementd2_frame, name="rearrangementd2_frame", curie=AK_SCHEMA.curie('rearrangementd2_frame'),
                   model_uri=AK_SCHEMA.rearrangementd2_frame, domain=None, range=Optional[int])

slots.rearrangementconsensus_count = Slot(uri=AK_SCHEMA.rearrangementconsensus_count, name="rearrangementconsensus_count", curie=AK_SCHEMA.curie('rearrangementconsensus_count'),
                   model_uri=AK_SCHEMA.rearrangementconsensus_count, domain=None, range=Optional[int])

slots.rearrangementduplicate_count = Slot(uri=AK_SCHEMA.rearrangementduplicate_count, name="rearrangementduplicate_count", curie=AK_SCHEMA.curie('rearrangementduplicate_count'),
                   model_uri=AK_SCHEMA.rearrangementduplicate_count, domain=None, range=Optional[int])

slots.rearrangementumi_count = Slot(uri=AK_SCHEMA.rearrangementumi_count, name="rearrangementumi_count", curie=AK_SCHEMA.curie('rearrangementumi_count'),
                   model_uri=AK_SCHEMA.rearrangementumi_count, domain=None, range=Optional[int])

slots.rearrangementcell_id = Slot(uri=AK_SCHEMA.rearrangementcell_id, name="rearrangementcell_id", curie=AK_SCHEMA.curie('rearrangementcell_id'),
                   model_uri=AK_SCHEMA.rearrangementcell_id, domain=None, range=Optional[str])

slots.rearrangementclone_id = Slot(uri=AK_SCHEMA.rearrangementclone_id, name="rearrangementclone_id", curie=AK_SCHEMA.curie('rearrangementclone_id'),
                   model_uri=AK_SCHEMA.rearrangementclone_id, domain=None, range=Optional[str])

slots.rearrangementreactivity_id = Slot(uri=AK_SCHEMA.rearrangementreactivity_id, name="rearrangementreactivity_id", curie=AK_SCHEMA.curie('rearrangementreactivity_id'),
                   model_uri=AK_SCHEMA.rearrangementreactivity_id, domain=None, range=Optional[str])

slots.rearrangementreactivity_ref = Slot(uri=AK_SCHEMA.rearrangementreactivity_ref, name="rearrangementreactivity_ref", curie=AK_SCHEMA.curie('rearrangementreactivity_ref'),
                   model_uri=AK_SCHEMA.rearrangementreactivity_ref, domain=None, range=Optional[str])

slots.rearrangementrepertoire_id = Slot(uri=AK_SCHEMA.rearrangementrepertoire_id, name="rearrangementrepertoire_id", curie=AK_SCHEMA.curie('rearrangementrepertoire_id'),
                   model_uri=AK_SCHEMA.rearrangementrepertoire_id, domain=None, range=Optional[str])

slots.rearrangementsample_processing_id = Slot(uri=AK_SCHEMA.rearrangementsample_processing_id, name="rearrangementsample_processing_id", curie=AK_SCHEMA.curie('rearrangementsample_processing_id'),
                   model_uri=AK_SCHEMA.rearrangementsample_processing_id, domain=None, range=Optional[str])

slots.rearrangementdata_processing_id = Slot(uri=AK_SCHEMA.rearrangementdata_processing_id, name="rearrangementdata_processing_id", curie=AK_SCHEMA.curie('rearrangementdata_processing_id'),
                   model_uri=AK_SCHEMA.rearrangementdata_processing_id, domain=None, range=Optional[str])

slots.cloneclone_id = Slot(uri=AK_SCHEMA.cloneclone_id, name="cloneclone_id", curie=AK_SCHEMA.curie('cloneclone_id'),
                   model_uri=AK_SCHEMA.cloneclone_id, domain=None, range=str)

slots.clonerepertoire_id = Slot(uri=AK_SCHEMA.clonerepertoire_id, name="clonerepertoire_id", curie=AK_SCHEMA.curie('clonerepertoire_id'),
                   model_uri=AK_SCHEMA.clonerepertoire_id, domain=None, range=Optional[str])

slots.clonedata_processing_id = Slot(uri=AK_SCHEMA.clonedata_processing_id, name="clonedata_processing_id", curie=AK_SCHEMA.curie('clonedata_processing_id'),
                   model_uri=AK_SCHEMA.clonedata_processing_id, domain=None, range=Optional[str])

slots.clonesequences = Slot(uri=AK_SCHEMA.clonesequences, name="clonesequences", curie=AK_SCHEMA.curie('clonesequences'),
                   model_uri=AK_SCHEMA.clonesequences, domain=None, range=Optional[Union[str, List[str]]])

slots.clonev_call = Slot(uri=AK_SCHEMA.clonev_call, name="clonev_call", curie=AK_SCHEMA.curie('clonev_call'),
                   model_uri=AK_SCHEMA.clonev_call, domain=None, range=Optional[str])

slots.cloned_call = Slot(uri=AK_SCHEMA.cloned_call, name="cloned_call", curie=AK_SCHEMA.curie('cloned_call'),
                   model_uri=AK_SCHEMA.cloned_call, domain=None, range=Optional[str])

slots.clonej_call = Slot(uri=AK_SCHEMA.clonej_call, name="clonej_call", curie=AK_SCHEMA.curie('clonej_call'),
                   model_uri=AK_SCHEMA.clonej_call, domain=None, range=Optional[str])

slots.clonejunction = Slot(uri=AK_SCHEMA.clonejunction, name="clonejunction", curie=AK_SCHEMA.curie('clonejunction'),
                   model_uri=AK_SCHEMA.clonejunction, domain=None, range=Optional[str])

slots.clonejunction_aa = Slot(uri=AK_SCHEMA.clonejunction_aa, name="clonejunction_aa", curie=AK_SCHEMA.curie('clonejunction_aa'),
                   model_uri=AK_SCHEMA.clonejunction_aa, domain=None, range=Optional[str])

slots.clonejunction_length = Slot(uri=AK_SCHEMA.clonejunction_length, name="clonejunction_length", curie=AK_SCHEMA.curie('clonejunction_length'),
                   model_uri=AK_SCHEMA.clonejunction_length, domain=None, range=Optional[int])

slots.clonejunction_aa_length = Slot(uri=AK_SCHEMA.clonejunction_aa_length, name="clonejunction_aa_length", curie=AK_SCHEMA.curie('clonejunction_aa_length'),
                   model_uri=AK_SCHEMA.clonejunction_aa_length, domain=None, range=Optional[int])

slots.clonegermline_alignment = Slot(uri=AK_SCHEMA.clonegermline_alignment, name="clonegermline_alignment", curie=AK_SCHEMA.curie('clonegermline_alignment'),
                   model_uri=AK_SCHEMA.clonegermline_alignment, domain=None, range=str)

slots.clonegermline_alignment_aa = Slot(uri=AK_SCHEMA.clonegermline_alignment_aa, name="clonegermline_alignment_aa", curie=AK_SCHEMA.curie('clonegermline_alignment_aa'),
                   model_uri=AK_SCHEMA.clonegermline_alignment_aa, domain=None, range=Optional[str])

slots.clonev_alignment_start = Slot(uri=AK_SCHEMA.clonev_alignment_start, name="clonev_alignment_start", curie=AK_SCHEMA.curie('clonev_alignment_start'),
                   model_uri=AK_SCHEMA.clonev_alignment_start, domain=None, range=Optional[int])

slots.clonev_alignment_end = Slot(uri=AK_SCHEMA.clonev_alignment_end, name="clonev_alignment_end", curie=AK_SCHEMA.curie('clonev_alignment_end'),
                   model_uri=AK_SCHEMA.clonev_alignment_end, domain=None, range=Optional[int])

slots.cloned_alignment_start = Slot(uri=AK_SCHEMA.cloned_alignment_start, name="cloned_alignment_start", curie=AK_SCHEMA.curie('cloned_alignment_start'),
                   model_uri=AK_SCHEMA.cloned_alignment_start, domain=None, range=Optional[int])

slots.cloned_alignment_end = Slot(uri=AK_SCHEMA.cloned_alignment_end, name="cloned_alignment_end", curie=AK_SCHEMA.curie('cloned_alignment_end'),
                   model_uri=AK_SCHEMA.cloned_alignment_end, domain=None, range=Optional[int])

slots.clonej_alignment_start = Slot(uri=AK_SCHEMA.clonej_alignment_start, name="clonej_alignment_start", curie=AK_SCHEMA.curie('clonej_alignment_start'),
                   model_uri=AK_SCHEMA.clonej_alignment_start, domain=None, range=Optional[int])

slots.clonej_alignment_end = Slot(uri=AK_SCHEMA.clonej_alignment_end, name="clonej_alignment_end", curie=AK_SCHEMA.curie('clonej_alignment_end'),
                   model_uri=AK_SCHEMA.clonej_alignment_end, domain=None, range=Optional[int])

slots.clonejunction_start = Slot(uri=AK_SCHEMA.clonejunction_start, name="clonejunction_start", curie=AK_SCHEMA.curie('clonejunction_start'),
                   model_uri=AK_SCHEMA.clonejunction_start, domain=None, range=Optional[int])

slots.clonejunction_end = Slot(uri=AK_SCHEMA.clonejunction_end, name="clonejunction_end", curie=AK_SCHEMA.curie('clonejunction_end'),
                   model_uri=AK_SCHEMA.clonejunction_end, domain=None, range=Optional[int])

slots.cloneumi_count = Slot(uri=AK_SCHEMA.cloneumi_count, name="cloneumi_count", curie=AK_SCHEMA.curie('cloneumi_count'),
                   model_uri=AK_SCHEMA.cloneumi_count, domain=None, range=Optional[int])

slots.cloneclone_count = Slot(uri=AK_SCHEMA.cloneclone_count, name="cloneclone_count", curie=AK_SCHEMA.curie('cloneclone_count'),
                   model_uri=AK_SCHEMA.cloneclone_count, domain=None, range=Optional[int])

slots.cloneseed_id = Slot(uri=AK_SCHEMA.cloneseed_id, name="cloneseed_id", curie=AK_SCHEMA.curie('cloneseed_id'),
                   model_uri=AK_SCHEMA.cloneseed_id, domain=None, range=Optional[str])

slots.treetree_id = Slot(uri=AK_SCHEMA.treetree_id, name="treetree_id", curie=AK_SCHEMA.curie('treetree_id'),
                   model_uri=AK_SCHEMA.treetree_id, domain=None, range=str)

slots.treeclone_id = Slot(uri=AK_SCHEMA.treeclone_id, name="treeclone_id", curie=AK_SCHEMA.curie('treeclone_id'),
                   model_uri=AK_SCHEMA.treeclone_id, domain=None, range=str)

slots.treenewick = Slot(uri=AK_SCHEMA.treenewick, name="treenewick", curie=AK_SCHEMA.curie('treenewick'),
                   model_uri=AK_SCHEMA.treenewick, domain=None, range=str)

slots.treenodes = Slot(uri=AK_SCHEMA.treenodes, name="treenodes", curie=AK_SCHEMA.curie('treenodes'),
                   model_uri=AK_SCHEMA.treenodes, domain=None, range=Optional[str])

slots.nodesequence_id = Slot(uri=AK_SCHEMA.nodesequence_id, name="nodesequence_id", curie=AK_SCHEMA.curie('nodesequence_id'),
                   model_uri=AK_SCHEMA.nodesequence_id, domain=None, range=str)

slots.nodesequence_alignment = Slot(uri=AK_SCHEMA.nodesequence_alignment, name="nodesequence_alignment", curie=AK_SCHEMA.curie('nodesequence_alignment'),
                   model_uri=AK_SCHEMA.nodesequence_alignment, domain=None, range=Optional[str])

slots.nodejunction = Slot(uri=AK_SCHEMA.nodejunction, name="nodejunction", curie=AK_SCHEMA.curie('nodejunction'),
                   model_uri=AK_SCHEMA.nodejunction, domain=None, range=Optional[str])

slots.nodejunction_aa = Slot(uri=AK_SCHEMA.nodejunction_aa, name="nodejunction_aa", curie=AK_SCHEMA.curie('nodejunction_aa'),
                   model_uri=AK_SCHEMA.nodejunction_aa, domain=None, range=Optional[str])

slots.cellcell_id = Slot(uri=AK_SCHEMA.cellcell_id, name="cellcell_id", curie=AK_SCHEMA.curie('cellcell_id'),
                   model_uri=AK_SCHEMA.cellcell_id, domain=None, range=str)

slots.cellrepertoire_id = Slot(uri=AK_SCHEMA.cellrepertoire_id, name="cellrepertoire_id", curie=AK_SCHEMA.curie('cellrepertoire_id'),
                   model_uri=AK_SCHEMA.cellrepertoire_id, domain=None, range=str)

slots.celldata_processing_id = Slot(uri=AK_SCHEMA.celldata_processing_id, name="celldata_processing_id", curie=AK_SCHEMA.curie('celldata_processing_id'),
                   model_uri=AK_SCHEMA.celldata_processing_id, domain=None, range=Optional[str])

slots.cellreceptors = Slot(uri=AK_SCHEMA.cellreceptors, name="cellreceptors", curie=AK_SCHEMA.curie('cellreceptors'),
                   model_uri=AK_SCHEMA.cellreceptors, domain=None, range=Optional[Union[str, List[str]]])

slots.cellcell_subset = Slot(uri=AK_SCHEMA.cellcell_subset, name="cellcell_subset", curie=AK_SCHEMA.curie('cellcell_subset'),
                   model_uri=AK_SCHEMA.cellcell_subset, domain=None, range=Optional[Union[str, "V1p4CellSubset"]])

slots.cellcell_phenotype = Slot(uri=AK_SCHEMA.cellcell_phenotype, name="cellcell_phenotype", curie=AK_SCHEMA.curie('cellcell_phenotype'),
                   model_uri=AK_SCHEMA.cellcell_phenotype, domain=None, range=Optional[str])

slots.cellcell_label = Slot(uri=AK_SCHEMA.cellcell_label, name="cellcell_label", curie=AK_SCHEMA.curie('cellcell_label'),
                   model_uri=AK_SCHEMA.cellcell_label, domain=None, range=Optional[str])

slots.cellvirtual_pairing = Slot(uri=AK_SCHEMA.cellvirtual_pairing, name="cellvirtual_pairing", curie=AK_SCHEMA.curie('cellvirtual_pairing'),
                   model_uri=AK_SCHEMA.cellvirtual_pairing, domain=None, range=Union[bool, Bool])

slots.expressionexpression_id = Slot(uri=AK_SCHEMA.expressionexpression_id, name="expressionexpression_id", curie=AK_SCHEMA.curie('expressionexpression_id'),
                   model_uri=AK_SCHEMA.expressionexpression_id, domain=None, range=str)

slots.expressioncell_id = Slot(uri=AK_SCHEMA.expressioncell_id, name="expressioncell_id", curie=AK_SCHEMA.curie('expressioncell_id'),
                   model_uri=AK_SCHEMA.expressioncell_id, domain=None, range=str)

slots.expressionrepertoire_id = Slot(uri=AK_SCHEMA.expressionrepertoire_id, name="expressionrepertoire_id", curie=AK_SCHEMA.curie('expressionrepertoire_id'),
                   model_uri=AK_SCHEMA.expressionrepertoire_id, domain=None, range=str)

slots.expressiondata_processing_id = Slot(uri=AK_SCHEMA.expressiondata_processing_id, name="expressiondata_processing_id", curie=AK_SCHEMA.curie('expressiondata_processing_id'),
                   model_uri=AK_SCHEMA.expressiondata_processing_id, domain=None, range=str)

slots.expressionproperty_type = Slot(uri=AK_SCHEMA.expressionproperty_type, name="expressionproperty_type", curie=AK_SCHEMA.curie('expressionproperty_type'),
                   model_uri=AK_SCHEMA.expressionproperty_type, domain=None, range=str)

slots.expressionproperty = Slot(uri=AK_SCHEMA.expressionproperty, name="expressionproperty", curie=AK_SCHEMA.curie('expressionproperty'),
                   model_uri=AK_SCHEMA.expressionproperty, domain=None, range=Union[str, "V1p4Property"])

slots.expressionvalue = Slot(uri=AK_SCHEMA.expressionvalue, name="expressionvalue", curie=AK_SCHEMA.curie('expressionvalue'),
                   model_uri=AK_SCHEMA.expressionvalue, domain=None, range=float)

slots.receptorreceptor_id = Slot(uri=AK_SCHEMA.receptorreceptor_id, name="receptorreceptor_id", curie=AK_SCHEMA.curie('receptorreceptor_id'),
                   model_uri=AK_SCHEMA.receptorreceptor_id, domain=None, range=str)

slots.receptorreceptor_hash = Slot(uri=AK_SCHEMA.receptorreceptor_hash, name="receptorreceptor_hash", curie=AK_SCHEMA.curie('receptorreceptor_hash'),
                   model_uri=AK_SCHEMA.receptorreceptor_hash, domain=None, range=str)

slots.receptorreceptor_type = Slot(uri=AK_SCHEMA.receptorreceptor_type, name="receptorreceptor_type", curie=AK_SCHEMA.curie('receptorreceptor_type'),
                   model_uri=AK_SCHEMA.receptorreceptor_type, domain=None, range=Union[str, "V1p4ReceptorType"])

slots.receptorreceptor_variable_domain_1_aa = Slot(uri=AK_SCHEMA.receptorreceptor_variable_domain_1_aa, name="receptorreceptor_variable_domain_1_aa", curie=AK_SCHEMA.curie('receptorreceptor_variable_domain_1_aa'),
                   model_uri=AK_SCHEMA.receptorreceptor_variable_domain_1_aa, domain=None, range=str)

slots.receptorreceptor_variable_domain_1_locus = Slot(uri=AK_SCHEMA.receptorreceptor_variable_domain_1_locus, name="receptorreceptor_variable_domain_1_locus", curie=AK_SCHEMA.curie('receptorreceptor_variable_domain_1_locus'),
                   model_uri=AK_SCHEMA.receptorreceptor_variable_domain_1_locus, domain=None, range=Union[str, "V1p4ReceptorVariableDomain1Locus"])

slots.receptorreceptor_variable_domain_2_aa = Slot(uri=AK_SCHEMA.receptorreceptor_variable_domain_2_aa, name="receptorreceptor_variable_domain_2_aa", curie=AK_SCHEMA.curie('receptorreceptor_variable_domain_2_aa'),
                   model_uri=AK_SCHEMA.receptorreceptor_variable_domain_2_aa, domain=None, range=str)

slots.receptorreceptor_variable_domain_2_locus = Slot(uri=AK_SCHEMA.receptorreceptor_variable_domain_2_locus, name="receptorreceptor_variable_domain_2_locus", curie=AK_SCHEMA.curie('receptorreceptor_variable_domain_2_locus'),
                   model_uri=AK_SCHEMA.receptorreceptor_variable_domain_2_locus, domain=None, range=Union[str, "V1p4ReceptorVariableDomain2Locus"])

slots.receptorreceptor_ref = Slot(uri=AK_SCHEMA.receptorreceptor_ref, name="receptorreceptor_ref", curie=AK_SCHEMA.curie('receptorreceptor_ref'),
                   model_uri=AK_SCHEMA.receptorreceptor_ref, domain=None, range=Optional[Union[str, List[str]]])

slots.reactivityreactivity_id = Slot(uri=AK_SCHEMA.reactivityreactivity_id, name="reactivityreactivity_id", curie=AK_SCHEMA.curie('reactivityreactivity_id'),
                   model_uri=AK_SCHEMA.reactivityreactivity_id, domain=None, range=str)

slots.reactivitycell_id = Slot(uri=AK_SCHEMA.reactivitycell_id, name="reactivitycell_id", curie=AK_SCHEMA.curie('reactivitycell_id'),
                   model_uri=AK_SCHEMA.reactivitycell_id, domain=None, range=str)

slots.reactivityrepertoire_id = Slot(uri=AK_SCHEMA.reactivityrepertoire_id, name="reactivityrepertoire_id", curie=AK_SCHEMA.curie('reactivityrepertoire_id'),
                   model_uri=AK_SCHEMA.reactivityrepertoire_id, domain=None, range=Optional[str])

slots.reactivitydata_processing_id = Slot(uri=AK_SCHEMA.reactivitydata_processing_id, name="reactivitydata_processing_id", curie=AK_SCHEMA.curie('reactivitydata_processing_id'),
                   model_uri=AK_SCHEMA.reactivitydata_processing_id, domain=None, range=Optional[str])

slots.reactivityligand_type = Slot(uri=AK_SCHEMA.reactivityligand_type, name="reactivityligand_type", curie=AK_SCHEMA.curie('reactivityligand_type'),
                   model_uri=AK_SCHEMA.reactivityligand_type, domain=None, range=Union[str, "V1p4LigandType"])

slots.reactivityantigen_type = Slot(uri=AK_SCHEMA.reactivityantigen_type, name="reactivityantigen_type", curie=AK_SCHEMA.curie('reactivityantigen_type'),
                   model_uri=AK_SCHEMA.reactivityantigen_type, domain=None, range=Union[str, "V1p4AntigenType"])

slots.reactivityantigen = Slot(uri=AK_SCHEMA.reactivityantigen, name="reactivityantigen", curie=AK_SCHEMA.curie('reactivityantigen'),
                   model_uri=AK_SCHEMA.reactivityantigen, domain=None, range=Union[str, "V1p4Antigen"])

slots.reactivityantigen_source_species = Slot(uri=AK_SCHEMA.reactivityantigen_source_species, name="reactivityantigen_source_species", curie=AK_SCHEMA.curie('reactivityantigen_source_species'),
                   model_uri=AK_SCHEMA.reactivityantigen_source_species, domain=None, range=Optional[Union[str, "V1p4AntigenSourceSpecies"]])

slots.reactivitypeptide_start = Slot(uri=AK_SCHEMA.reactivitypeptide_start, name="reactivitypeptide_start", curie=AK_SCHEMA.curie('reactivitypeptide_start'),
                   model_uri=AK_SCHEMA.reactivitypeptide_start, domain=None, range=Optional[int])

slots.reactivitypeptide_end = Slot(uri=AK_SCHEMA.reactivitypeptide_end, name="reactivitypeptide_end", curie=AK_SCHEMA.curie('reactivitypeptide_end'),
                   model_uri=AK_SCHEMA.reactivitypeptide_end, domain=None, range=Optional[int])

slots.reactivitypeptide_sequence_aa = Slot(uri=AK_SCHEMA.reactivitypeptide_sequence_aa, name="reactivitypeptide_sequence_aa", curie=AK_SCHEMA.curie('reactivitypeptide_sequence_aa'),
                   model_uri=AK_SCHEMA.reactivitypeptide_sequence_aa, domain=None, range=Optional[str])

slots.reactivitymhc_class = Slot(uri=AK_SCHEMA.reactivitymhc_class, name="reactivitymhc_class", curie=AK_SCHEMA.curie('reactivitymhc_class'),
                   model_uri=AK_SCHEMA.reactivitymhc_class, domain=None, range=Optional[Union[str, "V1p4MhcClass"]])

slots.reactivitymhc_gene_1 = Slot(uri=AK_SCHEMA.reactivitymhc_gene_1, name="reactivitymhc_gene_1", curie=AK_SCHEMA.curie('reactivitymhc_gene_1'),
                   model_uri=AK_SCHEMA.reactivitymhc_gene_1, domain=None, range=Optional[Union[str, "V1p4MhcGene1"]])

slots.reactivitymhc_allele_1 = Slot(uri=AK_SCHEMA.reactivitymhc_allele_1, name="reactivitymhc_allele_1", curie=AK_SCHEMA.curie('reactivitymhc_allele_1'),
                   model_uri=AK_SCHEMA.reactivitymhc_allele_1, domain=None, range=Optional[str])

slots.reactivitymhc_gene_2 = Slot(uri=AK_SCHEMA.reactivitymhc_gene_2, name="reactivitymhc_gene_2", curie=AK_SCHEMA.curie('reactivitymhc_gene_2'),
                   model_uri=AK_SCHEMA.reactivitymhc_gene_2, domain=None, range=Optional[Union[str, "V1p4MhcGene2"]])

slots.reactivitymhc_allele_2 = Slot(uri=AK_SCHEMA.reactivitymhc_allele_2, name="reactivitymhc_allele_2", curie=AK_SCHEMA.curie('reactivitymhc_allele_2'),
                   model_uri=AK_SCHEMA.reactivitymhc_allele_2, domain=None, range=Optional[str])

slots.reactivityreactivity_method = Slot(uri=AK_SCHEMA.reactivityreactivity_method, name="reactivityreactivity_method", curie=AK_SCHEMA.curie('reactivityreactivity_method'),
                   model_uri=AK_SCHEMA.reactivityreactivity_method, domain=None, range=str)

slots.reactivityreactivity_readout = Slot(uri=AK_SCHEMA.reactivityreactivity_readout, name="reactivityreactivity_readout", curie=AK_SCHEMA.curie('reactivityreactivity_readout'),
                   model_uri=AK_SCHEMA.reactivityreactivity_readout, domain=None, range=str)

slots.reactivityreactivity_value = Slot(uri=AK_SCHEMA.reactivityreactivity_value, name="reactivityreactivity_value", curie=AK_SCHEMA.curie('reactivityreactivity_value'),
                   model_uri=AK_SCHEMA.reactivityreactivity_value, domain=None, range=float)

slots.reactivityreactivity_unit = Slot(uri=AK_SCHEMA.reactivityreactivity_unit, name="reactivityreactivity_unit", curie=AK_SCHEMA.curie('reactivityreactivity_unit'),
                   model_uri=AK_SCHEMA.reactivityreactivity_unit, domain=None, range=str)

slots.reactivityreactivity_ref = Slot(uri=AK_SCHEMA.reactivityreactivity_ref, name="reactivityreactivity_ref", curie=AK_SCHEMA.curie('reactivityreactivity_ref'),
                   model_uri=AK_SCHEMA.reactivityreactivity_ref, domain=None, range=Optional[Union[str, List[str]]])

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

slots.aIRRKnowledgeCommons__chains = Slot(uri=AK_SCHEMA.chains, name="aIRRKnowledgeCommons__chains", curie=AK_SCHEMA.curie('chains'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__chains, domain=None, range=Optional[Union[Dict[Union[str, ChainAkcId], Union[dict, Chain]], List[Union[dict, Chain]]]])

slots.aIRRKnowledgeCommons__tcell_receptors = Slot(uri=AK_SCHEMA.tcell_receptors, name="aIRRKnowledgeCommons__tcell_receptors", curie=AK_SCHEMA.curie('tcell_receptors'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__tcell_receptors, domain=None, range=Optional[Union[Dict[Union[str, TCellReceptorAkcId], Union[dict, TCellReceptor]], List[Union[dict, TCellReceptor]]]])

slots.aIRRKnowledgeCommons__epitopes = Slot(uri=AK_SCHEMA.epitopes, name="aIRRKnowledgeCommons__epitopes", curie=AK_SCHEMA.curie('epitopes'),
                   model_uri=AK_SCHEMA.aIRRKnowledgeCommons__epitopes, domain=None, range=Optional[Union[Dict[Union[str, EpitopeAkcId], Union[dict, Epitope]], List[Union[dict, Epitope]]]])