# Auto generated from ak_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-11-25T12:33:28
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
    template_class: Optional[str] = None
    template_quality: Optional[str] = None
    template_amount: Optional[str] = None
    template_amount_unit: Optional[str] = None
    library_generation_method: Optional[str] = None
    library_generation_protocol: Optional[str] = None
    library_generation_kit_version: Optional[str] = None
    pcr_target: Optional[Union[str, List[str]]] = empty_list()
    complete_sequences: Optional[str] = None
    physical_linkage: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.akc_id):
            self.MissingRequiredField("akc_id")
        if not isinstance(self.akc_id, ReceptorRepertoireSequencingAssayAkcId):
            self.akc_id = ReceptorRepertoireSequencingAssayAkcId(self.akc_id)

        if self.template_class is not None and not isinstance(self.template_class, str):
            self.template_class = str(self.template_class)

        if self.template_quality is not None and not isinstance(self.template_quality, str):
            self.template_quality = str(self.template_quality)

        if self.template_amount is not None and not isinstance(self.template_amount, str):
            self.template_amount = str(self.template_amount)

        if self.template_amount_unit is not None and not isinstance(self.template_amount_unit, str):
            self.template_amount_unit = str(self.template_amount_unit)

        if self.library_generation_method is not None and not isinstance(self.library_generation_method, str):
            self.library_generation_method = str(self.library_generation_method)

        if self.library_generation_protocol is not None and not isinstance(self.library_generation_protocol, str):
            self.library_generation_protocol = str(self.library_generation_protocol)

        if self.library_generation_kit_version is not None and not isinstance(self.library_generation_kit_version, str):
            self.library_generation_kit_version = str(self.library_generation_kit_version)

        if not isinstance(self.pcr_target, list):
            self.pcr_target = [self.pcr_target] if self.pcr_target is not None else []
        self.pcr_target = [v if isinstance(v, str) else str(v) for v in self.pcr_target]

        if self.complete_sequences is not None and not isinstance(self.complete_sequences, str):
            self.complete_sequences = str(self.complete_sequences)

        if self.physical_linkage is not None and not isinstance(self.physical_linkage, str):
            self.physical_linkage = str(self.physical_linkage)

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
class TimePoint(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["TimePoint"]
    class_class_curie: ClassVar[str] = "ak_schema:TimePoint"
    class_name: ClassVar[str] = "TimePoint"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.TimePoint

    TimePoint_label: Optional[str] = None
    TimePoint_value: Optional[float] = None
    TimePoint_unit: Optional[Union[str, "Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.TimePoint_label is not None and not isinstance(self.TimePoint_label, str):
            self.TimePoint_label = str(self.TimePoint_label)

        if self.TimePoint_value is not None and not isinstance(self.TimePoint_value, float):
            self.TimePoint_value = float(self.TimePoint_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Acknowledgement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Acknowledgement"]
    class_class_curie: ClassVar[str] = "ak_schema:Acknowledgement"
    class_name: ClassVar[str] = "Acknowledgement"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Acknowledgement

    Acknowledgement_acknowledgement_id: str = None
    Acknowledgement_name: str = None
    Acknowledgement_institution_name: str = None
    Acknowledgement_orcid_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Acknowledgement_acknowledgement_id):
            self.MissingRequiredField("Acknowledgement_acknowledgement_id")
        if not isinstance(self.Acknowledgement_acknowledgement_id, str):
            self.Acknowledgement_acknowledgement_id = str(self.Acknowledgement_acknowledgement_id)

        if self._is_empty(self.Acknowledgement_name):
            self.MissingRequiredField("Acknowledgement_name")
        if not isinstance(self.Acknowledgement_name, str):
            self.Acknowledgement_name = str(self.Acknowledgement_name)

        if self._is_empty(self.Acknowledgement_institution_name):
            self.MissingRequiredField("Acknowledgement_institution_name")
        if not isinstance(self.Acknowledgement_institution_name, str):
            self.Acknowledgement_institution_name = str(self.Acknowledgement_institution_name)

        if self.Acknowledgement_orcid_id is not None and not isinstance(self.Acknowledgement_orcid_id, str):
            self.Acknowledgement_orcid_id = str(self.Acknowledgement_orcid_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["RearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:RearrangedSequence"
    class_name: ClassVar[str] = "RearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.RearrangedSequence

    RearrangedSequence_sequence_id: str = None
    RearrangedSequence_sequence: str = None
    RearrangedSequence_derivation: Union[str, "Derivation"] = None
    RearrangedSequence_observation_type: Union[str, "ObservationType"] = None
    RearrangedSequence_repository_name: str = None
    RearrangedSequence_deposited_version: str = None
    RearrangedSequence_curation: Optional[str] = None
    RearrangedSequence_repository_ref: Optional[str] = None
    RearrangedSequence_sequence_start: Optional[int] = None
    RearrangedSequence_sequence_end: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.RearrangedSequence_sequence_id):
            self.MissingRequiredField("RearrangedSequence_sequence_id")
        if not isinstance(self.RearrangedSequence_sequence_id, str):
            self.RearrangedSequence_sequence_id = str(self.RearrangedSequence_sequence_id)

        if self._is_empty(self.RearrangedSequence_sequence):
            self.MissingRequiredField("RearrangedSequence_sequence")
        if not isinstance(self.RearrangedSequence_sequence, str):
            self.RearrangedSequence_sequence = str(self.RearrangedSequence_sequence)

        if self._is_empty(self.RearrangedSequence_derivation):
            self.MissingRequiredField("RearrangedSequence_derivation")
        if not isinstance(self.RearrangedSequence_derivation, Derivation):
            self.RearrangedSequence_derivation = Derivation(self.RearrangedSequence_derivation)

        if self._is_empty(self.RearrangedSequence_observation_type):
            self.MissingRequiredField("RearrangedSequence_observation_type")
        if not isinstance(self.RearrangedSequence_observation_type, ObservationType):
            self.RearrangedSequence_observation_type = ObservationType(self.RearrangedSequence_observation_type)

        if self._is_empty(self.RearrangedSequence_repository_name):
            self.MissingRequiredField("RearrangedSequence_repository_name")
        if not isinstance(self.RearrangedSequence_repository_name, str):
            self.RearrangedSequence_repository_name = str(self.RearrangedSequence_repository_name)

        if self._is_empty(self.RearrangedSequence_deposited_version):
            self.MissingRequiredField("RearrangedSequence_deposited_version")
        if not isinstance(self.RearrangedSequence_deposited_version, str):
            self.RearrangedSequence_deposited_version = str(self.RearrangedSequence_deposited_version)

        if self.RearrangedSequence_curation is not None and not isinstance(self.RearrangedSequence_curation, str):
            self.RearrangedSequence_curation = str(self.RearrangedSequence_curation)

        if self.RearrangedSequence_repository_ref is not None and not isinstance(self.RearrangedSequence_repository_ref, str):
            self.RearrangedSequence_repository_ref = str(self.RearrangedSequence_repository_ref)

        if self.RearrangedSequence_sequence_start is not None and not isinstance(self.RearrangedSequence_sequence_start, int):
            self.RearrangedSequence_sequence_start = int(self.RearrangedSequence_sequence_start)

        if self.RearrangedSequence_sequence_end is not None and not isinstance(self.RearrangedSequence_sequence_end, int):
            self.RearrangedSequence_sequence_end = int(self.RearrangedSequence_sequence_end)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UnrearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["UnrearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:UnrearrangedSequence"
    class_name: ClassVar[str] = "UnrearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.UnrearrangedSequence

    UnrearrangedSequence_sequence_id: str = None
    UnrearrangedSequence_sequence: str = None
    UnrearrangedSequence_repository_name: str = None
    UnrearrangedSequence_gff_seqid: str = None
    UnrearrangedSequence_gff_start: int = None
    UnrearrangedSequence_gff_end: int = None
    UnrearrangedSequence_strand: Union[str, "Strand"] = None
    UnrearrangedSequence_curation: Optional[str] = None
    UnrearrangedSequence_repository_ref: Optional[str] = None
    UnrearrangedSequence_patch_no: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.UnrearrangedSequence_sequence_id):
            self.MissingRequiredField("UnrearrangedSequence_sequence_id")
        if not isinstance(self.UnrearrangedSequence_sequence_id, str):
            self.UnrearrangedSequence_sequence_id = str(self.UnrearrangedSequence_sequence_id)

        if self._is_empty(self.UnrearrangedSequence_sequence):
            self.MissingRequiredField("UnrearrangedSequence_sequence")
        if not isinstance(self.UnrearrangedSequence_sequence, str):
            self.UnrearrangedSequence_sequence = str(self.UnrearrangedSequence_sequence)

        if self._is_empty(self.UnrearrangedSequence_repository_name):
            self.MissingRequiredField("UnrearrangedSequence_repository_name")
        if not isinstance(self.UnrearrangedSequence_repository_name, str):
            self.UnrearrangedSequence_repository_name = str(self.UnrearrangedSequence_repository_name)

        if self._is_empty(self.UnrearrangedSequence_gff_seqid):
            self.MissingRequiredField("UnrearrangedSequence_gff_seqid")
        if not isinstance(self.UnrearrangedSequence_gff_seqid, str):
            self.UnrearrangedSequence_gff_seqid = str(self.UnrearrangedSequence_gff_seqid)

        if self._is_empty(self.UnrearrangedSequence_gff_start):
            self.MissingRequiredField("UnrearrangedSequence_gff_start")
        if not isinstance(self.UnrearrangedSequence_gff_start, int):
            self.UnrearrangedSequence_gff_start = int(self.UnrearrangedSequence_gff_start)

        if self._is_empty(self.UnrearrangedSequence_gff_end):
            self.MissingRequiredField("UnrearrangedSequence_gff_end")
        if not isinstance(self.UnrearrangedSequence_gff_end, int):
            self.UnrearrangedSequence_gff_end = int(self.UnrearrangedSequence_gff_end)

        if self._is_empty(self.UnrearrangedSequence_strand):
            self.MissingRequiredField("UnrearrangedSequence_strand")
        if not isinstance(self.UnrearrangedSequence_strand, Strand):
            self.UnrearrangedSequence_strand = Strand(self.UnrearrangedSequence_strand)

        if self.UnrearrangedSequence_curation is not None and not isinstance(self.UnrearrangedSequence_curation, str):
            self.UnrearrangedSequence_curation = str(self.UnrearrangedSequence_curation)

        if self.UnrearrangedSequence_repository_ref is not None and not isinstance(self.UnrearrangedSequence_repository_ref, str):
            self.UnrearrangedSequence_repository_ref = str(self.UnrearrangedSequence_repository_ref)

        if self.UnrearrangedSequence_patch_no is not None and not isinstance(self.UnrearrangedSequence_patch_no, str):
            self.UnrearrangedSequence_patch_no = str(self.UnrearrangedSequence_patch_no)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SequenceDelineationV(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["SequenceDelineationV"]
    class_class_curie: ClassVar[str] = "ak_schema:SequenceDelineationV"
    class_name: ClassVar[str] = "SequenceDelineationV"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.SequenceDelineationV

    SequenceDelineationV_sequence_delineation_id: str = None
    SequenceDelineationV_delineation_scheme: str = None
    SequenceDelineationV_fwr1_start: int = None
    SequenceDelineationV_fwr1_end: int = None
    SequenceDelineationV_cdr1_start: int = None
    SequenceDelineationV_cdr1_end: int = None
    SequenceDelineationV_fwr2_start: int = None
    SequenceDelineationV_fwr2_end: int = None
    SequenceDelineationV_cdr2_start: int = None
    SequenceDelineationV_cdr2_end: int = None
    SequenceDelineationV_fwr3_start: int = None
    SequenceDelineationV_fwr3_end: int = None
    SequenceDelineationV_cdr3_start: int = None
    SequenceDelineationV_unaligned_sequence: Optional[str] = None
    SequenceDelineationV_aligned_sequence: Optional[str] = None
    SequenceDelineationV_alignment_labels: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.SequenceDelineationV_sequence_delineation_id):
            self.MissingRequiredField("SequenceDelineationV_sequence_delineation_id")
        if not isinstance(self.SequenceDelineationV_sequence_delineation_id, str):
            self.SequenceDelineationV_sequence_delineation_id = str(self.SequenceDelineationV_sequence_delineation_id)

        if self._is_empty(self.SequenceDelineationV_delineation_scheme):
            self.MissingRequiredField("SequenceDelineationV_delineation_scheme")
        if not isinstance(self.SequenceDelineationV_delineation_scheme, str):
            self.SequenceDelineationV_delineation_scheme = str(self.SequenceDelineationV_delineation_scheme)

        if self._is_empty(self.SequenceDelineationV_fwr1_start):
            self.MissingRequiredField("SequenceDelineationV_fwr1_start")
        if not isinstance(self.SequenceDelineationV_fwr1_start, int):
            self.SequenceDelineationV_fwr1_start = int(self.SequenceDelineationV_fwr1_start)

        if self._is_empty(self.SequenceDelineationV_fwr1_end):
            self.MissingRequiredField("SequenceDelineationV_fwr1_end")
        if not isinstance(self.SequenceDelineationV_fwr1_end, int):
            self.SequenceDelineationV_fwr1_end = int(self.SequenceDelineationV_fwr1_end)

        if self._is_empty(self.SequenceDelineationV_cdr1_start):
            self.MissingRequiredField("SequenceDelineationV_cdr1_start")
        if not isinstance(self.SequenceDelineationV_cdr1_start, int):
            self.SequenceDelineationV_cdr1_start = int(self.SequenceDelineationV_cdr1_start)

        if self._is_empty(self.SequenceDelineationV_cdr1_end):
            self.MissingRequiredField("SequenceDelineationV_cdr1_end")
        if not isinstance(self.SequenceDelineationV_cdr1_end, int):
            self.SequenceDelineationV_cdr1_end = int(self.SequenceDelineationV_cdr1_end)

        if self._is_empty(self.SequenceDelineationV_fwr2_start):
            self.MissingRequiredField("SequenceDelineationV_fwr2_start")
        if not isinstance(self.SequenceDelineationV_fwr2_start, int):
            self.SequenceDelineationV_fwr2_start = int(self.SequenceDelineationV_fwr2_start)

        if self._is_empty(self.SequenceDelineationV_fwr2_end):
            self.MissingRequiredField("SequenceDelineationV_fwr2_end")
        if not isinstance(self.SequenceDelineationV_fwr2_end, int):
            self.SequenceDelineationV_fwr2_end = int(self.SequenceDelineationV_fwr2_end)

        if self._is_empty(self.SequenceDelineationV_cdr2_start):
            self.MissingRequiredField("SequenceDelineationV_cdr2_start")
        if not isinstance(self.SequenceDelineationV_cdr2_start, int):
            self.SequenceDelineationV_cdr2_start = int(self.SequenceDelineationV_cdr2_start)

        if self._is_empty(self.SequenceDelineationV_cdr2_end):
            self.MissingRequiredField("SequenceDelineationV_cdr2_end")
        if not isinstance(self.SequenceDelineationV_cdr2_end, int):
            self.SequenceDelineationV_cdr2_end = int(self.SequenceDelineationV_cdr2_end)

        if self._is_empty(self.SequenceDelineationV_fwr3_start):
            self.MissingRequiredField("SequenceDelineationV_fwr3_start")
        if not isinstance(self.SequenceDelineationV_fwr3_start, int):
            self.SequenceDelineationV_fwr3_start = int(self.SequenceDelineationV_fwr3_start)

        if self._is_empty(self.SequenceDelineationV_fwr3_end):
            self.MissingRequiredField("SequenceDelineationV_fwr3_end")
        if not isinstance(self.SequenceDelineationV_fwr3_end, int):
            self.SequenceDelineationV_fwr3_end = int(self.SequenceDelineationV_fwr3_end)

        if self._is_empty(self.SequenceDelineationV_cdr3_start):
            self.MissingRequiredField("SequenceDelineationV_cdr3_start")
        if not isinstance(self.SequenceDelineationV_cdr3_start, int):
            self.SequenceDelineationV_cdr3_start = int(self.SequenceDelineationV_cdr3_start)

        if self.SequenceDelineationV_unaligned_sequence is not None and not isinstance(self.SequenceDelineationV_unaligned_sequence, str):
            self.SequenceDelineationV_unaligned_sequence = str(self.SequenceDelineationV_unaligned_sequence)

        if self.SequenceDelineationV_aligned_sequence is not None and not isinstance(self.SequenceDelineationV_aligned_sequence, str):
            self.SequenceDelineationV_aligned_sequence = str(self.SequenceDelineationV_aligned_sequence)

        if not isinstance(self.SequenceDelineationV_alignment_labels, list):
            self.SequenceDelineationV_alignment_labels = [self.SequenceDelineationV_alignment_labels] if self.SequenceDelineationV_alignment_labels is not None else []
        self.SequenceDelineationV_alignment_labels = [v if isinstance(v, str) else str(v) for v in self.SequenceDelineationV_alignment_labels]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AlleleDescription(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["AlleleDescription"]
    class_class_curie: ClassVar[str] = "ak_schema:AlleleDescription"
    class_name: ClassVar[str] = "AlleleDescription"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.AlleleDescription

    AlleleDescription_allele_description_id: str = None
    AlleleDescription_maintainer: str = None
    AlleleDescription_lab_address: str = None
    AlleleDescription_release_version: int = None
    AlleleDescription_release_date: str = None
    AlleleDescription_release_description: str = None
    AlleleDescription_sequence: str = None
    AlleleDescription_coding_sequence: str = None
    AlleleDescription_locus: Union[str, "Locus"] = None
    AlleleDescription_sequence_type: Union[str, "SequenceType"] = None
    AlleleDescription_functional: Union[bool, Bool] = None
    AlleleDescription_inference_type: Union[str, "InferenceType"] = None
    AlleleDescription_species: Union[str, "Species"] = None
    AlleleDescription_allele_description_ref: Optional[str] = None
    AlleleDescription_acknowledgements: Optional[Union[Union[dict, Acknowledgement], List[Union[dict, Acknowledgement]]]] = empty_list()
    AlleleDescription_label: Optional[str] = None
    AlleleDescription_aliases: Optional[Union[str, List[str]]] = empty_list()
    AlleleDescription_chromosome: Optional[int] = None
    AlleleDescription_species_subgroup: Optional[str] = None
    AlleleDescription_species_subgroup_type: Optional[Union[str, "SpeciesSubgroupType"]] = None
    AlleleDescription_status: Optional[Union[str, "Status"]] = None
    AlleleDescription_subgroup_designation: Optional[str] = None
    AlleleDescription_gene_designation: Optional[str] = None
    AlleleDescription_allele_designation: Optional[str] = None
    AlleleDescription_allele_similarity_cluster_designation: Optional[str] = None
    AlleleDescription_allele_similarity_cluster_member_id: Optional[str] = None
    AlleleDescription_j_codon_frame: Optional[Union[str, "JCodonFrame"]] = None
    AlleleDescription_gene_start: Optional[int] = None
    AlleleDescription_gene_end: Optional[int] = None
    AlleleDescription_utr_5_prime_start: Optional[int] = None
    AlleleDescription_utr_5_prime_end: Optional[int] = None
    AlleleDescription_leader_1_start: Optional[int] = None
    AlleleDescription_leader_1_end: Optional[int] = None
    AlleleDescription_leader_2_start: Optional[int] = None
    AlleleDescription_leader_2_end: Optional[int] = None
    AlleleDescription_v_rs_start: Optional[int] = None
    AlleleDescription_v_rs_end: Optional[int] = None
    AlleleDescription_d_rs_3_prime_start: Optional[int] = None
    AlleleDescription_d_rs_3_prime_end: Optional[int] = None
    AlleleDescription_d_rs_5_prime_start: Optional[int] = None
    AlleleDescription_d_rs_5_prime_end: Optional[int] = None
    AlleleDescription_j_cdr3_end: Optional[int] = None
    AlleleDescription_j_rs_start: Optional[int] = None
    AlleleDescription_j_rs_end: Optional[int] = None
    AlleleDescription_j_donor_splice: Optional[int] = None
    AlleleDescription_v_gene_delineations: Optional[Union[Union[dict, SequenceDelineationV], List[Union[dict, SequenceDelineationV]]]] = empty_list()
    AlleleDescription_unrearranged_support: Optional[Union[Union[dict, UnrearrangedSequence], List[Union[dict, UnrearrangedSequence]]]] = empty_list()
    AlleleDescription_rearranged_support: Optional[Union[Union[dict, RearrangedSequence], List[Union[dict, RearrangedSequence]]]] = empty_list()
    AlleleDescription_paralogs: Optional[Union[str, List[str]]] = empty_list()
    AlleleDescription_curation: Optional[str] = None
    AlleleDescription_curational_tags: Optional[Union[Union[str, "CurationalTags"], List[Union[str, "CurationalTags"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.AlleleDescription_allele_description_id):
            self.MissingRequiredField("AlleleDescription_allele_description_id")
        if not isinstance(self.AlleleDescription_allele_description_id, str):
            self.AlleleDescription_allele_description_id = str(self.AlleleDescription_allele_description_id)

        if self._is_empty(self.AlleleDescription_maintainer):
            self.MissingRequiredField("AlleleDescription_maintainer")
        if not isinstance(self.AlleleDescription_maintainer, str):
            self.AlleleDescription_maintainer = str(self.AlleleDescription_maintainer)

        if self._is_empty(self.AlleleDescription_lab_address):
            self.MissingRequiredField("AlleleDescription_lab_address")
        if not isinstance(self.AlleleDescription_lab_address, str):
            self.AlleleDescription_lab_address = str(self.AlleleDescription_lab_address)

        if self._is_empty(self.AlleleDescription_release_version):
            self.MissingRequiredField("AlleleDescription_release_version")
        if not isinstance(self.AlleleDescription_release_version, int):
            self.AlleleDescription_release_version = int(self.AlleleDescription_release_version)

        if self._is_empty(self.AlleleDescription_release_date):
            self.MissingRequiredField("AlleleDescription_release_date")
        if not isinstance(self.AlleleDescription_release_date, str):
            self.AlleleDescription_release_date = str(self.AlleleDescription_release_date)

        if self._is_empty(self.AlleleDescription_release_description):
            self.MissingRequiredField("AlleleDescription_release_description")
        if not isinstance(self.AlleleDescription_release_description, str):
            self.AlleleDescription_release_description = str(self.AlleleDescription_release_description)

        if self._is_empty(self.AlleleDescription_sequence):
            self.MissingRequiredField("AlleleDescription_sequence")
        if not isinstance(self.AlleleDescription_sequence, str):
            self.AlleleDescription_sequence = str(self.AlleleDescription_sequence)

        if self._is_empty(self.AlleleDescription_coding_sequence):
            self.MissingRequiredField("AlleleDescription_coding_sequence")
        if not isinstance(self.AlleleDescription_coding_sequence, str):
            self.AlleleDescription_coding_sequence = str(self.AlleleDescription_coding_sequence)

        if self._is_empty(self.AlleleDescription_locus):
            self.MissingRequiredField("AlleleDescription_locus")
        if not isinstance(self.AlleleDescription_locus, Locus):
            self.AlleleDescription_locus = Locus(self.AlleleDescription_locus)

        if self._is_empty(self.AlleleDescription_sequence_type):
            self.MissingRequiredField("AlleleDescription_sequence_type")
        if not isinstance(self.AlleleDescription_sequence_type, SequenceType):
            self.AlleleDescription_sequence_type = SequenceType(self.AlleleDescription_sequence_type)

        if self._is_empty(self.AlleleDescription_functional):
            self.MissingRequiredField("AlleleDescription_functional")
        if not isinstance(self.AlleleDescription_functional, Bool):
            self.AlleleDescription_functional = Bool(self.AlleleDescription_functional)

        if self._is_empty(self.AlleleDescription_inference_type):
            self.MissingRequiredField("AlleleDescription_inference_type")
        if not isinstance(self.AlleleDescription_inference_type, InferenceType):
            self.AlleleDescription_inference_type = InferenceType(self.AlleleDescription_inference_type)

        if self._is_empty(self.AlleleDescription_species):
            self.MissingRequiredField("AlleleDescription_species")
        if not isinstance(self.AlleleDescription_species, Species):
            self.AlleleDescription_species = Species(self.AlleleDescription_species)

        if self.AlleleDescription_allele_description_ref is not None and not isinstance(self.AlleleDescription_allele_description_ref, str):
            self.AlleleDescription_allele_description_ref = str(self.AlleleDescription_allele_description_ref)

        self._normalize_inlined_as_dict(slot_name="AlleleDescription_acknowledgements", slot_type=Acknowledgement, key_name="Acknowledgement_acknowledgement_id", keyed=False)

        if self.AlleleDescription_label is not None and not isinstance(self.AlleleDescription_label, str):
            self.AlleleDescription_label = str(self.AlleleDescription_label)

        if not isinstance(self.AlleleDescription_aliases, list):
            self.AlleleDescription_aliases = [self.AlleleDescription_aliases] if self.AlleleDescription_aliases is not None else []
        self.AlleleDescription_aliases = [v if isinstance(v, str) else str(v) for v in self.AlleleDescription_aliases]

        if self.AlleleDescription_chromosome is not None and not isinstance(self.AlleleDescription_chromosome, int):
            self.AlleleDescription_chromosome = int(self.AlleleDescription_chromosome)

        if self.AlleleDescription_species_subgroup is not None and not isinstance(self.AlleleDescription_species_subgroup, str):
            self.AlleleDescription_species_subgroup = str(self.AlleleDescription_species_subgroup)

        if self.AlleleDescription_species_subgroup_type is not None and not isinstance(self.AlleleDescription_species_subgroup_type, SpeciesSubgroupType):
            self.AlleleDescription_species_subgroup_type = SpeciesSubgroupType(self.AlleleDescription_species_subgroup_type)

        if self.AlleleDescription_status is not None and not isinstance(self.AlleleDescription_status, Status):
            self.AlleleDescription_status = Status(self.AlleleDescription_status)

        if self.AlleleDescription_subgroup_designation is not None and not isinstance(self.AlleleDescription_subgroup_designation, str):
            self.AlleleDescription_subgroup_designation = str(self.AlleleDescription_subgroup_designation)

        if self.AlleleDescription_gene_designation is not None and not isinstance(self.AlleleDescription_gene_designation, str):
            self.AlleleDescription_gene_designation = str(self.AlleleDescription_gene_designation)

        if self.AlleleDescription_allele_designation is not None and not isinstance(self.AlleleDescription_allele_designation, str):
            self.AlleleDescription_allele_designation = str(self.AlleleDescription_allele_designation)

        if self.AlleleDescription_allele_similarity_cluster_designation is not None and not isinstance(self.AlleleDescription_allele_similarity_cluster_designation, str):
            self.AlleleDescription_allele_similarity_cluster_designation = str(self.AlleleDescription_allele_similarity_cluster_designation)

        if self.AlleleDescription_allele_similarity_cluster_member_id is not None and not isinstance(self.AlleleDescription_allele_similarity_cluster_member_id, str):
            self.AlleleDescription_allele_similarity_cluster_member_id = str(self.AlleleDescription_allele_similarity_cluster_member_id)

        if self.AlleleDescription_j_codon_frame is not None and not isinstance(self.AlleleDescription_j_codon_frame, JCodonFrame):
            self.AlleleDescription_j_codon_frame = JCodonFrame(self.AlleleDescription_j_codon_frame)

        if self.AlleleDescription_gene_start is not None and not isinstance(self.AlleleDescription_gene_start, int):
            self.AlleleDescription_gene_start = int(self.AlleleDescription_gene_start)

        if self.AlleleDescription_gene_end is not None and not isinstance(self.AlleleDescription_gene_end, int):
            self.AlleleDescription_gene_end = int(self.AlleleDescription_gene_end)

        if self.AlleleDescription_utr_5_prime_start is not None and not isinstance(self.AlleleDescription_utr_5_prime_start, int):
            self.AlleleDescription_utr_5_prime_start = int(self.AlleleDescription_utr_5_prime_start)

        if self.AlleleDescription_utr_5_prime_end is not None and not isinstance(self.AlleleDescription_utr_5_prime_end, int):
            self.AlleleDescription_utr_5_prime_end = int(self.AlleleDescription_utr_5_prime_end)

        if self.AlleleDescription_leader_1_start is not None and not isinstance(self.AlleleDescription_leader_1_start, int):
            self.AlleleDescription_leader_1_start = int(self.AlleleDescription_leader_1_start)

        if self.AlleleDescription_leader_1_end is not None and not isinstance(self.AlleleDescription_leader_1_end, int):
            self.AlleleDescription_leader_1_end = int(self.AlleleDescription_leader_1_end)

        if self.AlleleDescription_leader_2_start is not None and not isinstance(self.AlleleDescription_leader_2_start, int):
            self.AlleleDescription_leader_2_start = int(self.AlleleDescription_leader_2_start)

        if self.AlleleDescription_leader_2_end is not None and not isinstance(self.AlleleDescription_leader_2_end, int):
            self.AlleleDescription_leader_2_end = int(self.AlleleDescription_leader_2_end)

        if self.AlleleDescription_v_rs_start is not None and not isinstance(self.AlleleDescription_v_rs_start, int):
            self.AlleleDescription_v_rs_start = int(self.AlleleDescription_v_rs_start)

        if self.AlleleDescription_v_rs_end is not None and not isinstance(self.AlleleDescription_v_rs_end, int):
            self.AlleleDescription_v_rs_end = int(self.AlleleDescription_v_rs_end)

        if self.AlleleDescription_d_rs_3_prime_start is not None and not isinstance(self.AlleleDescription_d_rs_3_prime_start, int):
            self.AlleleDescription_d_rs_3_prime_start = int(self.AlleleDescription_d_rs_3_prime_start)

        if self.AlleleDescription_d_rs_3_prime_end is not None and not isinstance(self.AlleleDescription_d_rs_3_prime_end, int):
            self.AlleleDescription_d_rs_3_prime_end = int(self.AlleleDescription_d_rs_3_prime_end)

        if self.AlleleDescription_d_rs_5_prime_start is not None and not isinstance(self.AlleleDescription_d_rs_5_prime_start, int):
            self.AlleleDescription_d_rs_5_prime_start = int(self.AlleleDescription_d_rs_5_prime_start)

        if self.AlleleDescription_d_rs_5_prime_end is not None and not isinstance(self.AlleleDescription_d_rs_5_prime_end, int):
            self.AlleleDescription_d_rs_5_prime_end = int(self.AlleleDescription_d_rs_5_prime_end)

        if self.AlleleDescription_j_cdr3_end is not None and not isinstance(self.AlleleDescription_j_cdr3_end, int):
            self.AlleleDescription_j_cdr3_end = int(self.AlleleDescription_j_cdr3_end)

        if self.AlleleDescription_j_rs_start is not None and not isinstance(self.AlleleDescription_j_rs_start, int):
            self.AlleleDescription_j_rs_start = int(self.AlleleDescription_j_rs_start)

        if self.AlleleDescription_j_rs_end is not None and not isinstance(self.AlleleDescription_j_rs_end, int):
            self.AlleleDescription_j_rs_end = int(self.AlleleDescription_j_rs_end)

        if self.AlleleDescription_j_donor_splice is not None and not isinstance(self.AlleleDescription_j_donor_splice, int):
            self.AlleleDescription_j_donor_splice = int(self.AlleleDescription_j_donor_splice)

        self._normalize_inlined_as_dict(slot_name="AlleleDescription_v_gene_delineations", slot_type=SequenceDelineationV, key_name="SequenceDelineationV_sequence_delineation_id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="AlleleDescription_unrearranged_support", slot_type=UnrearrangedSequence, key_name="UnrearrangedSequence_sequence_id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="AlleleDescription_rearranged_support", slot_type=RearrangedSequence, key_name="RearrangedSequence_sequence_id", keyed=False)

        if not isinstance(self.AlleleDescription_paralogs, list):
            self.AlleleDescription_paralogs = [self.AlleleDescription_paralogs] if self.AlleleDescription_paralogs is not None else []
        self.AlleleDescription_paralogs = [v if isinstance(v, str) else str(v) for v in self.AlleleDescription_paralogs]

        if self.AlleleDescription_curation is not None and not isinstance(self.AlleleDescription_curation, str):
            self.AlleleDescription_curation = str(self.AlleleDescription_curation)

        if not isinstance(self.AlleleDescription_curational_tags, list):
            self.AlleleDescription_curational_tags = [self.AlleleDescription_curational_tags] if self.AlleleDescription_curational_tags is not None else []
        self.AlleleDescription_curational_tags = [v if isinstance(v, CurationalTags) else CurationalTags(v) for v in self.AlleleDescription_curational_tags]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GermlineSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["GermlineSet"]
    class_class_curie: ClassVar[str] = "ak_schema:GermlineSet"
    class_name: ClassVar[str] = "GermlineSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.GermlineSet

    GermlineSet_germline_set_id: str = None
    GermlineSet_author: str = None
    GermlineSet_lab_name: str = None
    GermlineSet_lab_address: str = None
    GermlineSet_release_version: float = None
    GermlineSet_release_description: str = None
    GermlineSet_release_date: str = None
    GermlineSet_germline_set_name: str = None
    GermlineSet_germline_set_ref: str = None
    GermlineSet_species: Union[str, "Species"] = None
    GermlineSet_locus: Union[str, "Locus"] = None
    GermlineSet_allele_descriptions: Union[Union[dict, AlleleDescription], List[Union[dict, AlleleDescription]]] = None
    GermlineSet_acknowledgements: Optional[Union[Union[dict, Acknowledgement], List[Union[dict, Acknowledgement]]]] = empty_list()
    GermlineSet_pub_ids: Optional[str] = None
    GermlineSet_species_subgroup: Optional[str] = None
    GermlineSet_species_subgroup_type: Optional[Union[str, "SpeciesSubgroupType"]] = None
    GermlineSet_curation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.GermlineSet_germline_set_id):
            self.MissingRequiredField("GermlineSet_germline_set_id")
        if not isinstance(self.GermlineSet_germline_set_id, str):
            self.GermlineSet_germline_set_id = str(self.GermlineSet_germline_set_id)

        if self._is_empty(self.GermlineSet_author):
            self.MissingRequiredField("GermlineSet_author")
        if not isinstance(self.GermlineSet_author, str):
            self.GermlineSet_author = str(self.GermlineSet_author)

        if self._is_empty(self.GermlineSet_lab_name):
            self.MissingRequiredField("GermlineSet_lab_name")
        if not isinstance(self.GermlineSet_lab_name, str):
            self.GermlineSet_lab_name = str(self.GermlineSet_lab_name)

        if self._is_empty(self.GermlineSet_lab_address):
            self.MissingRequiredField("GermlineSet_lab_address")
        if not isinstance(self.GermlineSet_lab_address, str):
            self.GermlineSet_lab_address = str(self.GermlineSet_lab_address)

        if self._is_empty(self.GermlineSet_release_version):
            self.MissingRequiredField("GermlineSet_release_version")
        if not isinstance(self.GermlineSet_release_version, float):
            self.GermlineSet_release_version = float(self.GermlineSet_release_version)

        if self._is_empty(self.GermlineSet_release_description):
            self.MissingRequiredField("GermlineSet_release_description")
        if not isinstance(self.GermlineSet_release_description, str):
            self.GermlineSet_release_description = str(self.GermlineSet_release_description)

        if self._is_empty(self.GermlineSet_release_date):
            self.MissingRequiredField("GermlineSet_release_date")
        if not isinstance(self.GermlineSet_release_date, str):
            self.GermlineSet_release_date = str(self.GermlineSet_release_date)

        if self._is_empty(self.GermlineSet_germline_set_name):
            self.MissingRequiredField("GermlineSet_germline_set_name")
        if not isinstance(self.GermlineSet_germline_set_name, str):
            self.GermlineSet_germline_set_name = str(self.GermlineSet_germline_set_name)

        if self._is_empty(self.GermlineSet_germline_set_ref):
            self.MissingRequiredField("GermlineSet_germline_set_ref")
        if not isinstance(self.GermlineSet_germline_set_ref, str):
            self.GermlineSet_germline_set_ref = str(self.GermlineSet_germline_set_ref)

        if self._is_empty(self.GermlineSet_species):
            self.MissingRequiredField("GermlineSet_species")
        if not isinstance(self.GermlineSet_species, Species):
            self.GermlineSet_species = Species(self.GermlineSet_species)

        if self._is_empty(self.GermlineSet_locus):
            self.MissingRequiredField("GermlineSet_locus")
        if not isinstance(self.GermlineSet_locus, Locus):
            self.GermlineSet_locus = Locus(self.GermlineSet_locus)

        if self._is_empty(self.GermlineSet_allele_descriptions):
            self.MissingRequiredField("GermlineSet_allele_descriptions")
        self._normalize_inlined_as_dict(slot_name="GermlineSet_allele_descriptions", slot_type=AlleleDescription, key_name="AlleleDescription_allele_description_id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="GermlineSet_acknowledgements", slot_type=Acknowledgement, key_name="Acknowledgement_acknowledgement_id", keyed=False)

        if self.GermlineSet_pub_ids is not None and not isinstance(self.GermlineSet_pub_ids, str):
            self.GermlineSet_pub_ids = str(self.GermlineSet_pub_ids)

        if self.GermlineSet_species_subgroup is not None and not isinstance(self.GermlineSet_species_subgroup, str):
            self.GermlineSet_species_subgroup = str(self.GermlineSet_species_subgroup)

        if self.GermlineSet_species_subgroup_type is not None and not isinstance(self.GermlineSet_species_subgroup_type, SpeciesSubgroupType):
            self.GermlineSet_species_subgroup_type = SpeciesSubgroupType(self.GermlineSet_species_subgroup_type)

        if self.GermlineSet_curation is not None and not isinstance(self.GermlineSet_curation, str):
            self.GermlineSet_curation = str(self.GermlineSet_curation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["GenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:GenotypeSet"
    class_name: ClassVar[str] = "GenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.GenotypeSet

    GenotypeSet_receptor_genotype_set_id: str = None
    GenotypeSet_genotype_class_list: Optional[Union[Union[dict, "Genotype"], List[Union[dict, "Genotype"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.GenotypeSet_receptor_genotype_set_id):
            self.MissingRequiredField("GenotypeSet_receptor_genotype_set_id")
        if not isinstance(self.GenotypeSet_receptor_genotype_set_id, str):
            self.GenotypeSet_receptor_genotype_set_id = str(self.GenotypeSet_receptor_genotype_set_id)

        self._normalize_inlined_as_dict(slot_name="GenotypeSet_genotype_class_list", slot_type=Genotype, key_name="Genotype_receptor_genotype_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Genotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Genotype"]
    class_class_curie: ClassVar[str] = "ak_schema:Genotype"
    class_name: ClassVar[str] = "Genotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Genotype

    Genotype_receptor_genotype_id: str = None
    Genotype_locus: Union[str, "Locus"] = None
    Genotype_documented_alleles: Optional[Union[Union[dict, "DocumentedAllele"], List[Union[dict, "DocumentedAllele"]]]] = empty_list()
    Genotype_undocumented_alleles: Optional[Union[Union[dict, "UndocumentedAllele"], List[Union[dict, "UndocumentedAllele"]]]] = empty_list()
    Genotype_deleted_genes: Optional[Union[Union[dict, "DeletedGene"], List[Union[dict, "DeletedGene"]]]] = empty_list()
    Genotype_inference_process: Optional[Union[str, "InferenceProcess"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Genotype_receptor_genotype_id):
            self.MissingRequiredField("Genotype_receptor_genotype_id")
        if not isinstance(self.Genotype_receptor_genotype_id, str):
            self.Genotype_receptor_genotype_id = str(self.Genotype_receptor_genotype_id)

        if self._is_empty(self.Genotype_locus):
            self.MissingRequiredField("Genotype_locus")
        if not isinstance(self.Genotype_locus, Locus):
            self.Genotype_locus = Locus(self.Genotype_locus)

        self._normalize_inlined_as_dict(slot_name="Genotype_documented_alleles", slot_type=DocumentedAllele, key_name="DocumentedAllele_label", keyed=False)

        self._normalize_inlined_as_dict(slot_name="Genotype_undocumented_alleles", slot_type=UndocumentedAllele, key_name="UndocumentedAllele_allele_name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="Genotype_deleted_genes", slot_type=DeletedGene, key_name="DeletedGene_label", keyed=False)

        if self.Genotype_inference_process is not None and not isinstance(self.Genotype_inference_process, InferenceProcess):
            self.Genotype_inference_process = InferenceProcess(self.Genotype_inference_process)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["DocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:DocumentedAllele"
    class_name: ClassVar[str] = "DocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.DocumentedAllele

    DocumentedAllele_label: str = None
    DocumentedAllele_germline_set_ref: str = None
    DocumentedAllele_phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.DocumentedAllele_label):
            self.MissingRequiredField("DocumentedAllele_label")
        if not isinstance(self.DocumentedAllele_label, str):
            self.DocumentedAllele_label = str(self.DocumentedAllele_label)

        if self._is_empty(self.DocumentedAllele_germline_set_ref):
            self.MissingRequiredField("DocumentedAllele_germline_set_ref")
        if not isinstance(self.DocumentedAllele_germline_set_ref, str):
            self.DocumentedAllele_germline_set_ref = str(self.DocumentedAllele_germline_set_ref)

        if self.DocumentedAllele_phasing is not None and not isinstance(self.DocumentedAllele_phasing, int):
            self.DocumentedAllele_phasing = int(self.DocumentedAllele_phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UndocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["UndocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:UndocumentedAllele"
    class_name: ClassVar[str] = "UndocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.UndocumentedAllele

    UndocumentedAllele_allele_name: str = None
    UndocumentedAllele_sequence: str = None
    UndocumentedAllele_phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.UndocumentedAllele_allele_name):
            self.MissingRequiredField("UndocumentedAllele_allele_name")
        if not isinstance(self.UndocumentedAllele_allele_name, str):
            self.UndocumentedAllele_allele_name = str(self.UndocumentedAllele_allele_name)

        if self._is_empty(self.UndocumentedAllele_sequence):
            self.MissingRequiredField("UndocumentedAllele_sequence")
        if not isinstance(self.UndocumentedAllele_sequence, str):
            self.UndocumentedAllele_sequence = str(self.UndocumentedAllele_sequence)

        if self.UndocumentedAllele_phasing is not None and not isinstance(self.UndocumentedAllele_phasing, int):
            self.UndocumentedAllele_phasing = int(self.UndocumentedAllele_phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DeletedGene(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["DeletedGene"]
    class_class_curie: ClassVar[str] = "ak_schema:DeletedGene"
    class_name: ClassVar[str] = "DeletedGene"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.DeletedGene

    DeletedGene_label: str = None
    DeletedGene_germline_set_ref: str = None
    DeletedGene_phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.DeletedGene_label):
            self.MissingRequiredField("DeletedGene_label")
        if not isinstance(self.DeletedGene_label, str):
            self.DeletedGene_label = str(self.DeletedGene_label)

        if self._is_empty(self.DeletedGene_germline_set_ref):
            self.MissingRequiredField("DeletedGene_germline_set_ref")
        if not isinstance(self.DeletedGene_germline_set_ref, str):
            self.DeletedGene_germline_set_ref = str(self.DeletedGene_germline_set_ref)

        if self.DeletedGene_phasing is not None and not isinstance(self.DeletedGene_phasing, int):
            self.DeletedGene_phasing = int(self.DeletedGene_phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MHCGenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["MHCGenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:MHCGenotypeSet"
    class_name: ClassVar[str] = "MHCGenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.MHCGenotypeSet

    MHCGenotypeSet_mhc_genotype_set_id: str = None
    MHCGenotypeSet_mhc_genotype_list: Union[Union[dict, "MHCGenotype"], List[Union[dict, "MHCGenotype"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.MHCGenotypeSet_mhc_genotype_set_id):
            self.MissingRequiredField("MHCGenotypeSet_mhc_genotype_set_id")
        if not isinstance(self.MHCGenotypeSet_mhc_genotype_set_id, str):
            self.MHCGenotypeSet_mhc_genotype_set_id = str(self.MHCGenotypeSet_mhc_genotype_set_id)

        if self._is_empty(self.MHCGenotypeSet_mhc_genotype_list):
            self.MissingRequiredField("MHCGenotypeSet_mhc_genotype_list")
        self._normalize_inlined_as_dict(slot_name="MHCGenotypeSet_mhc_genotype_list", slot_type=MHCGenotype, key_name="MHCGenotype_mhc_genotype_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MHCGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["MHCGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:MHCGenotype"
    class_name: ClassVar[str] = "MHCGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.MHCGenotype

    MHCGenotype_mhc_genotype_id: str = None
    MHCGenotype_mhc_class: Union[str, "MhcClass"] = None
    MHCGenotype_mhc_alleles: Union[Union[dict, "MHCAllele"], List[Union[dict, "MHCAllele"]]] = None
    MHCGenotype_mhc_genotyping_method: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.MHCGenotype_mhc_genotype_id):
            self.MissingRequiredField("MHCGenotype_mhc_genotype_id")
        if not isinstance(self.MHCGenotype_mhc_genotype_id, str):
            self.MHCGenotype_mhc_genotype_id = str(self.MHCGenotype_mhc_genotype_id)

        if self._is_empty(self.MHCGenotype_mhc_class):
            self.MissingRequiredField("MHCGenotype_mhc_class")
        if not isinstance(self.MHCGenotype_mhc_class, MhcClass):
            self.MHCGenotype_mhc_class = MhcClass(self.MHCGenotype_mhc_class)

        if self._is_empty(self.MHCGenotype_mhc_alleles):
            self.MissingRequiredField("MHCGenotype_mhc_alleles")
        if not isinstance(self.MHCGenotype_mhc_alleles, list):
            self.MHCGenotype_mhc_alleles = [self.MHCGenotype_mhc_alleles] if self.MHCGenotype_mhc_alleles is not None else []
        self.MHCGenotype_mhc_alleles = [v if isinstance(v, MHCAllele) else MHCAllele(**as_dict(v)) for v in self.MHCGenotype_mhc_alleles]

        if self.MHCGenotype_mhc_genotyping_method is not None and not isinstance(self.MHCGenotype_mhc_genotyping_method, str):
            self.MHCGenotype_mhc_genotyping_method = str(self.MHCGenotype_mhc_genotyping_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MHCAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["MHCAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:MHCAllele"
    class_name: ClassVar[str] = "MHCAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.MHCAllele

    MHCAllele_allele_designation: Optional[str] = None
    MHCAllele_gene: Optional[Union[str, "Gene"]] = None
    MHCAllele_reference_set_ref: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.MHCAllele_allele_designation is not None and not isinstance(self.MHCAllele_allele_designation, str):
            self.MHCAllele_allele_designation = str(self.MHCAllele_allele_designation)

        if self.MHCAllele_reference_set_ref is not None and not isinstance(self.MHCAllele_reference_set_ref, str):
            self.MHCAllele_reference_set_ref = str(self.MHCAllele_reference_set_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubjectGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["SubjectGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:SubjectGenotype"
    class_name: ClassVar[str] = "SubjectGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.SubjectGenotype

    SubjectGenotype_receptor_genotype_set: Optional[Union[dict, GenotypeSet]] = None
    SubjectGenotype_mhc_genotype_set: Optional[Union[dict, MHCGenotypeSet]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.SubjectGenotype_receptor_genotype_set is not None and not isinstance(self.SubjectGenotype_receptor_genotype_set, GenotypeSet):
            self.SubjectGenotype_receptor_genotype_set = GenotypeSet(**as_dict(self.SubjectGenotype_receptor_genotype_set))

        if self.SubjectGenotype_mhc_genotype_set is not None and not isinstance(self.SubjectGenotype_mhc_genotype_set, MHCGenotypeSet):
            self.SubjectGenotype_mhc_genotype_set = MHCGenotypeSet(**as_dict(self.SubjectGenotype_mhc_genotype_set))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Study(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Study"]
    class_class_curie: ClassVar[str] = "ak_schema:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Study

    Study_study_id: str = None
    Study_study_title: str = None
    Study_study_type: Union[str, "StudyType"] = None
    Study_inclusion_exclusion_criteria: str = None
    Study_grants: str = None
    Study_collected_by: str = None
    Study_lab_name: str = None
    Study_lab_address: str = None
    Study_submitted_by: str = None
    Study_pub_ids: str = None
    Study_keywords_study: Union[Union[str, "KeywordsStudy"], List[Union[str, "KeywordsStudy"]]] = None
    Study_study_description: Optional[str] = None
    Study_study_contact: Optional[str] = None
    Study_adc_publish_date: Optional[str] = None
    Study_adc_update_date: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Study_study_id):
            self.MissingRequiredField("Study_study_id")
        if not isinstance(self.Study_study_id, str):
            self.Study_study_id = str(self.Study_study_id)

        if self._is_empty(self.Study_study_title):
            self.MissingRequiredField("Study_study_title")
        if not isinstance(self.Study_study_title, str):
            self.Study_study_title = str(self.Study_study_title)

        if self._is_empty(self.Study_inclusion_exclusion_criteria):
            self.MissingRequiredField("Study_inclusion_exclusion_criteria")
        if not isinstance(self.Study_inclusion_exclusion_criteria, str):
            self.Study_inclusion_exclusion_criteria = str(self.Study_inclusion_exclusion_criteria)

        if self._is_empty(self.Study_grants):
            self.MissingRequiredField("Study_grants")
        if not isinstance(self.Study_grants, str):
            self.Study_grants = str(self.Study_grants)

        if self._is_empty(self.Study_collected_by):
            self.MissingRequiredField("Study_collected_by")
        if not isinstance(self.Study_collected_by, str):
            self.Study_collected_by = str(self.Study_collected_by)

        if self._is_empty(self.Study_lab_name):
            self.MissingRequiredField("Study_lab_name")
        if not isinstance(self.Study_lab_name, str):
            self.Study_lab_name = str(self.Study_lab_name)

        if self._is_empty(self.Study_lab_address):
            self.MissingRequiredField("Study_lab_address")
        if not isinstance(self.Study_lab_address, str):
            self.Study_lab_address = str(self.Study_lab_address)

        if self._is_empty(self.Study_submitted_by):
            self.MissingRequiredField("Study_submitted_by")
        if not isinstance(self.Study_submitted_by, str):
            self.Study_submitted_by = str(self.Study_submitted_by)

        if self._is_empty(self.Study_pub_ids):
            self.MissingRequiredField("Study_pub_ids")
        if not isinstance(self.Study_pub_ids, str):
            self.Study_pub_ids = str(self.Study_pub_ids)

        if self._is_empty(self.Study_keywords_study):
            self.MissingRequiredField("Study_keywords_study")
        if not isinstance(self.Study_keywords_study, list):
            self.Study_keywords_study = [self.Study_keywords_study] if self.Study_keywords_study is not None else []
        self.Study_keywords_study = [v if isinstance(v, KeywordsStudy) else KeywordsStudy(v) for v in self.Study_keywords_study]

        if self.Study_study_description is not None and not isinstance(self.Study_study_description, str):
            self.Study_study_description = str(self.Study_study_description)

        if self.Study_study_contact is not None and not isinstance(self.Study_study_contact, str):
            self.Study_study_contact = str(self.Study_study_contact)

        if self.Study_adc_publish_date is not None and not isinstance(self.Study_adc_publish_date, str):
            self.Study_adc_publish_date = str(self.Study_adc_publish_date)

        if self.Study_adc_update_date is not None and not isinstance(self.Study_adc_update_date, str):
            self.Study_adc_update_date = str(self.Study_adc_update_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Subject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Subject"]
    class_class_curie: ClassVar[str] = "ak_schema:Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Subject

    Subject_subject_id: str = None
    Subject_synthetic: Union[bool, Bool] = None
    Subject_species: Union[str, "Species"] = None
    Subject_sex: Union[str, "Sex"] = None
    Subject_age_min: float = None
    Subject_age_max: float = None
    Subject_age_unit: Union[str, "AgeUnit"] = None
    Subject_age_event: str = None
    Subject_ancestry_population: str = None
    Subject_ethnicity: str = None
    Subject_race: str = None
    Subject_strain_name: str = None
    Subject_linked_subjects: str = None
    Subject_link_type: str = None
    Subject_diagnosis: Optional[Union[Union[dict, "Diagnosis"], List[Union[dict, "Diagnosis"]]]] = empty_list()
    Subject_genotype: Optional[Union[dict, SubjectGenotype]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Subject_subject_id):
            self.MissingRequiredField("Subject_subject_id")
        if not isinstance(self.Subject_subject_id, str):
            self.Subject_subject_id = str(self.Subject_subject_id)

        if self._is_empty(self.Subject_synthetic):
            self.MissingRequiredField("Subject_synthetic")
        if not isinstance(self.Subject_synthetic, Bool):
            self.Subject_synthetic = Bool(self.Subject_synthetic)

        if self._is_empty(self.Subject_species):
            self.MissingRequiredField("Subject_species")
        if not isinstance(self.Subject_species, Species):
            self.Subject_species = Species(self.Subject_species)

        if self._is_empty(self.Subject_sex):
            self.MissingRequiredField("Subject_sex")
        if not isinstance(self.Subject_sex, Sex):
            self.Subject_sex = Sex(self.Subject_sex)

        if self._is_empty(self.Subject_age_min):
            self.MissingRequiredField("Subject_age_min")
        if not isinstance(self.Subject_age_min, float):
            self.Subject_age_min = float(self.Subject_age_min)

        if self._is_empty(self.Subject_age_max):
            self.MissingRequiredField("Subject_age_max")
        if not isinstance(self.Subject_age_max, float):
            self.Subject_age_max = float(self.Subject_age_max)

        if self._is_empty(self.Subject_age_event):
            self.MissingRequiredField("Subject_age_event")
        if not isinstance(self.Subject_age_event, str):
            self.Subject_age_event = str(self.Subject_age_event)

        if self._is_empty(self.Subject_ancestry_population):
            self.MissingRequiredField("Subject_ancestry_population")
        if not isinstance(self.Subject_ancestry_population, str):
            self.Subject_ancestry_population = str(self.Subject_ancestry_population)

        if self._is_empty(self.Subject_ethnicity):
            self.MissingRequiredField("Subject_ethnicity")
        if not isinstance(self.Subject_ethnicity, str):
            self.Subject_ethnicity = str(self.Subject_ethnicity)

        if self._is_empty(self.Subject_race):
            self.MissingRequiredField("Subject_race")
        if not isinstance(self.Subject_race, str):
            self.Subject_race = str(self.Subject_race)

        if self._is_empty(self.Subject_strain_name):
            self.MissingRequiredField("Subject_strain_name")
        if not isinstance(self.Subject_strain_name, str):
            self.Subject_strain_name = str(self.Subject_strain_name)

        if self._is_empty(self.Subject_linked_subjects):
            self.MissingRequiredField("Subject_linked_subjects")
        if not isinstance(self.Subject_linked_subjects, str):
            self.Subject_linked_subjects = str(self.Subject_linked_subjects)

        if self._is_empty(self.Subject_link_type):
            self.MissingRequiredField("Subject_link_type")
        if not isinstance(self.Subject_link_type, str):
            self.Subject_link_type = str(self.Subject_link_type)

        self._normalize_inlined_as_dict(slot_name="Subject_diagnosis", slot_type=Diagnosis, key_name="Diagnosis_study_group_description", keyed=False)

        if self.Subject_genotype is not None and not isinstance(self.Subject_genotype, SubjectGenotype):
            self.Subject_genotype = SubjectGenotype(**as_dict(self.Subject_genotype))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Diagnosis(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Diagnosis"]
    class_class_curie: ClassVar[str] = "ak_schema:Diagnosis"
    class_name: ClassVar[str] = "Diagnosis"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Diagnosis

    Diagnosis_study_group_description: str = None
    Diagnosis_disease_diagnosis: Union[str, "DiseaseDiagnosis"] = None
    Diagnosis_disease_length: str = None
    Diagnosis_disease_stage: str = None
    Diagnosis_prior_therapies: str = None
    Diagnosis_immunogen: str = None
    Diagnosis_intervention: str = None
    Diagnosis_medical_history: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Diagnosis_study_group_description):
            self.MissingRequiredField("Diagnosis_study_group_description")
        if not isinstance(self.Diagnosis_study_group_description, str):
            self.Diagnosis_study_group_description = str(self.Diagnosis_study_group_description)

        if self._is_empty(self.Diagnosis_disease_length):
            self.MissingRequiredField("Diagnosis_disease_length")
        if not isinstance(self.Diagnosis_disease_length, str):
            self.Diagnosis_disease_length = str(self.Diagnosis_disease_length)

        if self._is_empty(self.Diagnosis_disease_stage):
            self.MissingRequiredField("Diagnosis_disease_stage")
        if not isinstance(self.Diagnosis_disease_stage, str):
            self.Diagnosis_disease_stage = str(self.Diagnosis_disease_stage)

        if self._is_empty(self.Diagnosis_prior_therapies):
            self.MissingRequiredField("Diagnosis_prior_therapies")
        if not isinstance(self.Diagnosis_prior_therapies, str):
            self.Diagnosis_prior_therapies = str(self.Diagnosis_prior_therapies)

        if self._is_empty(self.Diagnosis_immunogen):
            self.MissingRequiredField("Diagnosis_immunogen")
        if not isinstance(self.Diagnosis_immunogen, str):
            self.Diagnosis_immunogen = str(self.Diagnosis_immunogen)

        if self._is_empty(self.Diagnosis_intervention):
            self.MissingRequiredField("Diagnosis_intervention")
        if not isinstance(self.Diagnosis_intervention, str):
            self.Diagnosis_intervention = str(self.Diagnosis_intervention)

        if self._is_empty(self.Diagnosis_medical_history):
            self.MissingRequiredField("Diagnosis_medical_history")
        if not isinstance(self.Diagnosis_medical_history, str):
            self.Diagnosis_medical_history = str(self.Diagnosis_medical_history)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Sample"]
    class_class_curie: ClassVar[str] = "ak_schema:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Sample

    Sample_sample_id: str = None
    Sample_sample_type: str = None
    Sample_tissue: Union[str, TissueAkcId] = None
    Sample_anatomic_site: str = None
    Sample_disease_state_sample: str = None
    Sample_collection_time_point_relative: float = None
    Sample_collection_time_point_relative_unit: Union[str, "CollectionTimePointRelativeUnit"] = None
    Sample_collection_time_point_reference: str = None
    Sample_biomaterial_provider: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Sample_sample_id):
            self.MissingRequiredField("Sample_sample_id")
        if not isinstance(self.Sample_sample_id, str):
            self.Sample_sample_id = str(self.Sample_sample_id)

        if self._is_empty(self.Sample_sample_type):
            self.MissingRequiredField("Sample_sample_type")
        if not isinstance(self.Sample_sample_type, str):
            self.Sample_sample_type = str(self.Sample_sample_type)

        if self._is_empty(self.Sample_tissue):
            self.MissingRequiredField("Sample_tissue")
        if not isinstance(self.Sample_tissue, TissueAkcId):
            self.Sample_tissue = TissueAkcId(self.Sample_tissue)

        if self._is_empty(self.Sample_anatomic_site):
            self.MissingRequiredField("Sample_anatomic_site")
        if not isinstance(self.Sample_anatomic_site, str):
            self.Sample_anatomic_site = str(self.Sample_anatomic_site)

        if self._is_empty(self.Sample_disease_state_sample):
            self.MissingRequiredField("Sample_disease_state_sample")
        if not isinstance(self.Sample_disease_state_sample, str):
            self.Sample_disease_state_sample = str(self.Sample_disease_state_sample)

        if self._is_empty(self.Sample_collection_time_point_relative):
            self.MissingRequiredField("Sample_collection_time_point_relative")
        if not isinstance(self.Sample_collection_time_point_relative, float):
            self.Sample_collection_time_point_relative = float(self.Sample_collection_time_point_relative)

        if self._is_empty(self.Sample_collection_time_point_reference):
            self.MissingRequiredField("Sample_collection_time_point_reference")
        if not isinstance(self.Sample_collection_time_point_reference, str):
            self.Sample_collection_time_point_reference = str(self.Sample_collection_time_point_reference)

        if self._is_empty(self.Sample_biomaterial_provider):
            self.MissingRequiredField("Sample_biomaterial_provider")
        if not isinstance(self.Sample_biomaterial_provider, str):
            self.Sample_biomaterial_provider = str(self.Sample_biomaterial_provider)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["CellProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:CellProcessing"
    class_name: ClassVar[str] = "CellProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.CellProcessing

    CellProcessing_tissue_processing: str = None
    CellProcessing_cell_subset: Union[str, "CellSubset"] = None
    CellProcessing_cell_phenotype: str = None
    CellProcessing_single_cell: Union[bool, Bool] = None
    CellProcessing_cell_number: int = None
    CellProcessing_cells_per_reaction: int = None
    CellProcessing_cell_storage: Union[bool, Bool] = None
    CellProcessing_cell_quality: str = None
    CellProcessing_cell_isolation: str = None
    CellProcessing_cell_processing_protocol: str = None
    CellProcessing_cell_species: Optional[Union[str, "CellSpecies"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.CellProcessing_tissue_processing):
            self.MissingRequiredField("CellProcessing_tissue_processing")
        if not isinstance(self.CellProcessing_tissue_processing, str):
            self.CellProcessing_tissue_processing = str(self.CellProcessing_tissue_processing)

        if self._is_empty(self.CellProcessing_cell_phenotype):
            self.MissingRequiredField("CellProcessing_cell_phenotype")
        if not isinstance(self.CellProcessing_cell_phenotype, str):
            self.CellProcessing_cell_phenotype = str(self.CellProcessing_cell_phenotype)

        if self._is_empty(self.CellProcessing_single_cell):
            self.MissingRequiredField("CellProcessing_single_cell")
        if not isinstance(self.CellProcessing_single_cell, Bool):
            self.CellProcessing_single_cell = Bool(self.CellProcessing_single_cell)

        if self._is_empty(self.CellProcessing_cell_number):
            self.MissingRequiredField("CellProcessing_cell_number")
        if not isinstance(self.CellProcessing_cell_number, int):
            self.CellProcessing_cell_number = int(self.CellProcessing_cell_number)

        if self._is_empty(self.CellProcessing_cells_per_reaction):
            self.MissingRequiredField("CellProcessing_cells_per_reaction")
        if not isinstance(self.CellProcessing_cells_per_reaction, int):
            self.CellProcessing_cells_per_reaction = int(self.CellProcessing_cells_per_reaction)

        if self._is_empty(self.CellProcessing_cell_storage):
            self.MissingRequiredField("CellProcessing_cell_storage")
        if not isinstance(self.CellProcessing_cell_storage, Bool):
            self.CellProcessing_cell_storage = Bool(self.CellProcessing_cell_storage)

        if self._is_empty(self.CellProcessing_cell_quality):
            self.MissingRequiredField("CellProcessing_cell_quality")
        if not isinstance(self.CellProcessing_cell_quality, str):
            self.CellProcessing_cell_quality = str(self.CellProcessing_cell_quality)

        if self._is_empty(self.CellProcessing_cell_isolation):
            self.MissingRequiredField("CellProcessing_cell_isolation")
        if not isinstance(self.CellProcessing_cell_isolation, str):
            self.CellProcessing_cell_isolation = str(self.CellProcessing_cell_isolation)

        if self._is_empty(self.CellProcessing_cell_processing_protocol):
            self.MissingRequiredField("CellProcessing_cell_processing_protocol")
        if not isinstance(self.CellProcessing_cell_processing_protocol, str):
            self.CellProcessing_cell_processing_protocol = str(self.CellProcessing_cell_processing_protocol)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PCRTarget(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["PCRTarget"]
    class_class_curie: ClassVar[str] = "ak_schema:PCRTarget"
    class_name: ClassVar[str] = "PCRTarget"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.PCRTarget

    PCRTarget_pcr_target_locus: Union[str, "PcrTargetLocus"] = None
    PCRTarget_forward_pcr_primer_target_location: str = None
    PCRTarget_reverse_pcr_primer_target_location: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.PCRTarget_pcr_target_locus):
            self.MissingRequiredField("PCRTarget_pcr_target_locus")
        if not isinstance(self.PCRTarget_pcr_target_locus, PcrTargetLocus):
            self.PCRTarget_pcr_target_locus = PcrTargetLocus(self.PCRTarget_pcr_target_locus)

        if self._is_empty(self.PCRTarget_forward_pcr_primer_target_location):
            self.MissingRequiredField("PCRTarget_forward_pcr_primer_target_location")
        if not isinstance(self.PCRTarget_forward_pcr_primer_target_location, str):
            self.PCRTarget_forward_pcr_primer_target_location = str(self.PCRTarget_forward_pcr_primer_target_location)

        if self._is_empty(self.PCRTarget_reverse_pcr_primer_target_location):
            self.MissingRequiredField("PCRTarget_reverse_pcr_primer_target_location")
        if not isinstance(self.PCRTarget_reverse_pcr_primer_target_location, str):
            self.PCRTarget_reverse_pcr_primer_target_location = str(self.PCRTarget_reverse_pcr_primer_target_location)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NucleicAcidProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["NucleicAcidProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:NucleicAcidProcessing"
    class_name: ClassVar[str] = "NucleicAcidProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.NucleicAcidProcessing

    NucleicAcidProcessing_template_class: Union[str, "TemplateClass"] = None
    NucleicAcidProcessing_template_quality: str = None
    NucleicAcidProcessing_template_amount: float = None
    NucleicAcidProcessing_template_amount_unit: Union[str, "TemplateAmountUnit"] = None
    NucleicAcidProcessing_library_generation_method: Union[str, "LibraryGenerationMethod"] = None
    NucleicAcidProcessing_library_generation_protocol: str = None
    NucleicAcidProcessing_library_generation_kit_version: str = None
    NucleicAcidProcessing_complete_sequences: Union[str, "CompleteSequences"] = None
    NucleicAcidProcessing_physical_linkage: Union[str, "PhysicalLinkage"] = None
    NucleicAcidProcessing_pcr_target: Optional[Union[Union[dict, PCRTarget], List[Union[dict, PCRTarget]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.NucleicAcidProcessing_template_class):
            self.MissingRequiredField("NucleicAcidProcessing_template_class")
        if not isinstance(self.NucleicAcidProcessing_template_class, TemplateClass):
            self.NucleicAcidProcessing_template_class = TemplateClass(self.NucleicAcidProcessing_template_class)

        if self._is_empty(self.NucleicAcidProcessing_template_quality):
            self.MissingRequiredField("NucleicAcidProcessing_template_quality")
        if not isinstance(self.NucleicAcidProcessing_template_quality, str):
            self.NucleicAcidProcessing_template_quality = str(self.NucleicAcidProcessing_template_quality)

        if self._is_empty(self.NucleicAcidProcessing_template_amount):
            self.MissingRequiredField("NucleicAcidProcessing_template_amount")
        if not isinstance(self.NucleicAcidProcessing_template_amount, float):
            self.NucleicAcidProcessing_template_amount = float(self.NucleicAcidProcessing_template_amount)

        if self._is_empty(self.NucleicAcidProcessing_library_generation_method):
            self.MissingRequiredField("NucleicAcidProcessing_library_generation_method")
        if not isinstance(self.NucleicAcidProcessing_library_generation_method, LibraryGenerationMethod):
            self.NucleicAcidProcessing_library_generation_method = LibraryGenerationMethod(self.NucleicAcidProcessing_library_generation_method)

        if self._is_empty(self.NucleicAcidProcessing_library_generation_protocol):
            self.MissingRequiredField("NucleicAcidProcessing_library_generation_protocol")
        if not isinstance(self.NucleicAcidProcessing_library_generation_protocol, str):
            self.NucleicAcidProcessing_library_generation_protocol = str(self.NucleicAcidProcessing_library_generation_protocol)

        if self._is_empty(self.NucleicAcidProcessing_library_generation_kit_version):
            self.MissingRequiredField("NucleicAcidProcessing_library_generation_kit_version")
        if not isinstance(self.NucleicAcidProcessing_library_generation_kit_version, str):
            self.NucleicAcidProcessing_library_generation_kit_version = str(self.NucleicAcidProcessing_library_generation_kit_version)

        if self._is_empty(self.NucleicAcidProcessing_complete_sequences):
            self.MissingRequiredField("NucleicAcidProcessing_complete_sequences")
        if not isinstance(self.NucleicAcidProcessing_complete_sequences, CompleteSequences):
            self.NucleicAcidProcessing_complete_sequences = CompleteSequences(self.NucleicAcidProcessing_complete_sequences)

        if self._is_empty(self.NucleicAcidProcessing_physical_linkage):
            self.MissingRequiredField("NucleicAcidProcessing_physical_linkage")
        if not isinstance(self.NucleicAcidProcessing_physical_linkage, PhysicalLinkage):
            self.NucleicAcidProcessing_physical_linkage = PhysicalLinkage(self.NucleicAcidProcessing_physical_linkage)

        self._normalize_inlined_as_dict(slot_name="NucleicAcidProcessing_pcr_target", slot_type=PCRTarget, key_name="PCRTarget_pcr_target_locus", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SequencingRun(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["SequencingRun"]
    class_class_curie: ClassVar[str] = "ak_schema:SequencingRun"
    class_name: ClassVar[str] = "SequencingRun"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.SequencingRun

    SequencingRun_sequencing_run_id: str = None
    SequencingRun_total_reads_passing_qc_filter: int = None
    SequencingRun_sequencing_platform: str = None
    SequencingRun_sequencing_facility: str = None
    SequencingRun_sequencing_run_date: str = None
    SequencingRun_sequencing_kit: str = None
    SequencingRun_sequencing_files: Optional[Union[dict, "SequencingData"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.SequencingRun_sequencing_run_id):
            self.MissingRequiredField("SequencingRun_sequencing_run_id")
        if not isinstance(self.SequencingRun_sequencing_run_id, str):
            self.SequencingRun_sequencing_run_id = str(self.SequencingRun_sequencing_run_id)

        if self._is_empty(self.SequencingRun_total_reads_passing_qc_filter):
            self.MissingRequiredField("SequencingRun_total_reads_passing_qc_filter")
        if not isinstance(self.SequencingRun_total_reads_passing_qc_filter, int):
            self.SequencingRun_total_reads_passing_qc_filter = int(self.SequencingRun_total_reads_passing_qc_filter)

        if self._is_empty(self.SequencingRun_sequencing_platform):
            self.MissingRequiredField("SequencingRun_sequencing_platform")
        if not isinstance(self.SequencingRun_sequencing_platform, str):
            self.SequencingRun_sequencing_platform = str(self.SequencingRun_sequencing_platform)

        if self._is_empty(self.SequencingRun_sequencing_facility):
            self.MissingRequiredField("SequencingRun_sequencing_facility")
        if not isinstance(self.SequencingRun_sequencing_facility, str):
            self.SequencingRun_sequencing_facility = str(self.SequencingRun_sequencing_facility)

        if self._is_empty(self.SequencingRun_sequencing_run_date):
            self.MissingRequiredField("SequencingRun_sequencing_run_date")
        if not isinstance(self.SequencingRun_sequencing_run_date, str):
            self.SequencingRun_sequencing_run_date = str(self.SequencingRun_sequencing_run_date)

        if self._is_empty(self.SequencingRun_sequencing_kit):
            self.MissingRequiredField("SequencingRun_sequencing_kit")
        if not isinstance(self.SequencingRun_sequencing_kit, str):
            self.SequencingRun_sequencing_kit = str(self.SequencingRun_sequencing_kit)

        if self.SequencingRun_sequencing_files is not None and not isinstance(self.SequencingRun_sequencing_files, SequencingData):
            self.SequencingRun_sequencing_files = SequencingData(**as_dict(self.SequencingRun_sequencing_files))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SequencingData(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["SequencingData"]
    class_class_curie: ClassVar[str] = "ak_schema:SequencingData"
    class_name: ClassVar[str] = "SequencingData"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.SequencingData

    SequencingData_sequencing_data_id: str = None
    SequencingData_file_type: Union[str, "FileType"] = None
    SequencingData_filename: str = None
    SequencingData_read_direction: Union[str, "ReadDirection"] = None
    SequencingData_read_length: int = None
    SequencingData_paired_filename: str = None
    SequencingData_paired_read_direction: Union[str, "PairedReadDirection"] = None
    SequencingData_paired_read_length: int = None
    SequencingData_index_filename: Optional[str] = None
    SequencingData_index_length: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.SequencingData_sequencing_data_id):
            self.MissingRequiredField("SequencingData_sequencing_data_id")
        if not isinstance(self.SequencingData_sequencing_data_id, str):
            self.SequencingData_sequencing_data_id = str(self.SequencingData_sequencing_data_id)

        if self._is_empty(self.SequencingData_file_type):
            self.MissingRequiredField("SequencingData_file_type")
        if not isinstance(self.SequencingData_file_type, FileType):
            self.SequencingData_file_type = FileType(self.SequencingData_file_type)

        if self._is_empty(self.SequencingData_filename):
            self.MissingRequiredField("SequencingData_filename")
        if not isinstance(self.SequencingData_filename, str):
            self.SequencingData_filename = str(self.SequencingData_filename)

        if self._is_empty(self.SequencingData_read_direction):
            self.MissingRequiredField("SequencingData_read_direction")
        if not isinstance(self.SequencingData_read_direction, ReadDirection):
            self.SequencingData_read_direction = ReadDirection(self.SequencingData_read_direction)

        if self._is_empty(self.SequencingData_read_length):
            self.MissingRequiredField("SequencingData_read_length")
        if not isinstance(self.SequencingData_read_length, int):
            self.SequencingData_read_length = int(self.SequencingData_read_length)

        if self._is_empty(self.SequencingData_paired_filename):
            self.MissingRequiredField("SequencingData_paired_filename")
        if not isinstance(self.SequencingData_paired_filename, str):
            self.SequencingData_paired_filename = str(self.SequencingData_paired_filename)

        if self._is_empty(self.SequencingData_paired_read_direction):
            self.MissingRequiredField("SequencingData_paired_read_direction")
        if not isinstance(self.SequencingData_paired_read_direction, PairedReadDirection):
            self.SequencingData_paired_read_direction = PairedReadDirection(self.SequencingData_paired_read_direction)

        if self._is_empty(self.SequencingData_paired_read_length):
            self.MissingRequiredField("SequencingData_paired_read_length")
        if not isinstance(self.SequencingData_paired_read_length, int):
            self.SequencingData_paired_read_length = int(self.SequencingData_paired_read_length)

        if self.SequencingData_index_filename is not None and not isinstance(self.SequencingData_index_filename, str):
            self.SequencingData_index_filename = str(self.SequencingData_index_filename)

        if self.SequencingData_index_length is not None and not isinstance(self.SequencingData_index_length, int):
            self.SequencingData_index_length = int(self.SequencingData_index_length)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["DataProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:DataProcessing"
    class_name: ClassVar[str] = "DataProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.DataProcessing

    DataProcessing_software_versions: str = None
    DataProcessing_paired_reads_assembly: str = None
    DataProcessing_quality_thresholds: str = None
    DataProcessing_primer_match_cutoffs: str = None
    DataProcessing_collapsing_method: str = None
    DataProcessing_data_processing_protocols: str = None
    DataProcessing_germline_database: str = None
    DataProcessing_data_processing_id: Optional[str] = None
    DataProcessing_primary_annotation: Optional[Union[bool, Bool]] = None
    DataProcessing_data_processing_files: Optional[Union[str, List[str]]] = empty_list()
    DataProcessing_germline_set_ref: Optional[str] = None
    DataProcessing_analysis_provenance_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.DataProcessing_software_versions):
            self.MissingRequiredField("DataProcessing_software_versions")
        if not isinstance(self.DataProcessing_software_versions, str):
            self.DataProcessing_software_versions = str(self.DataProcessing_software_versions)

        if self._is_empty(self.DataProcessing_paired_reads_assembly):
            self.MissingRequiredField("DataProcessing_paired_reads_assembly")
        if not isinstance(self.DataProcessing_paired_reads_assembly, str):
            self.DataProcessing_paired_reads_assembly = str(self.DataProcessing_paired_reads_assembly)

        if self._is_empty(self.DataProcessing_quality_thresholds):
            self.MissingRequiredField("DataProcessing_quality_thresholds")
        if not isinstance(self.DataProcessing_quality_thresholds, str):
            self.DataProcessing_quality_thresholds = str(self.DataProcessing_quality_thresholds)

        if self._is_empty(self.DataProcessing_primer_match_cutoffs):
            self.MissingRequiredField("DataProcessing_primer_match_cutoffs")
        if not isinstance(self.DataProcessing_primer_match_cutoffs, str):
            self.DataProcessing_primer_match_cutoffs = str(self.DataProcessing_primer_match_cutoffs)

        if self._is_empty(self.DataProcessing_collapsing_method):
            self.MissingRequiredField("DataProcessing_collapsing_method")
        if not isinstance(self.DataProcessing_collapsing_method, str):
            self.DataProcessing_collapsing_method = str(self.DataProcessing_collapsing_method)

        if self._is_empty(self.DataProcessing_data_processing_protocols):
            self.MissingRequiredField("DataProcessing_data_processing_protocols")
        if not isinstance(self.DataProcessing_data_processing_protocols, str):
            self.DataProcessing_data_processing_protocols = str(self.DataProcessing_data_processing_protocols)

        if self._is_empty(self.DataProcessing_germline_database):
            self.MissingRequiredField("DataProcessing_germline_database")
        if not isinstance(self.DataProcessing_germline_database, str):
            self.DataProcessing_germline_database = str(self.DataProcessing_germline_database)

        if self.DataProcessing_data_processing_id is not None and not isinstance(self.DataProcessing_data_processing_id, str):
            self.DataProcessing_data_processing_id = str(self.DataProcessing_data_processing_id)

        if self.DataProcessing_primary_annotation is not None and not isinstance(self.DataProcessing_primary_annotation, Bool):
            self.DataProcessing_primary_annotation = Bool(self.DataProcessing_primary_annotation)

        if not isinstance(self.DataProcessing_data_processing_files, list):
            self.DataProcessing_data_processing_files = [self.DataProcessing_data_processing_files] if self.DataProcessing_data_processing_files is not None else []
        self.DataProcessing_data_processing_files = [v if isinstance(v, str) else str(v) for v in self.DataProcessing_data_processing_files]

        if self.DataProcessing_germline_set_ref is not None and not isinstance(self.DataProcessing_germline_set_ref, str):
            self.DataProcessing_germline_set_ref = str(self.DataProcessing_germline_set_ref)

        if self.DataProcessing_analysis_provenance_id is not None and not isinstance(self.DataProcessing_analysis_provenance_id, str):
            self.DataProcessing_analysis_provenance_id = str(self.DataProcessing_analysis_provenance_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Repertoire(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Repertoire"]
    class_class_curie: ClassVar[str] = "ak_schema:Repertoire"
    class_name: ClassVar[str] = "Repertoire"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Repertoire

    Repertoire_study: Union[dict, Study] = None
    Repertoire_subject: Union[dict, Subject] = None
    Repertoire_sample: Union[Union[dict, "SampleProcessing"], List[Union[dict, "SampleProcessing"]]] = None
    Repertoire_data_processing: Union[Union[dict, DataProcessing], List[Union[dict, DataProcessing]]] = None
    Repertoire_repertoire_id: Optional[str] = None
    Repertoire_repertoire_name: Optional[str] = None
    Repertoire_repertoire_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Repertoire_study):
            self.MissingRequiredField("Repertoire_study")
        if not isinstance(self.Repertoire_study, Study):
            self.Repertoire_study = Study(**as_dict(self.Repertoire_study))

        if self._is_empty(self.Repertoire_subject):
            self.MissingRequiredField("Repertoire_subject")
        if not isinstance(self.Repertoire_subject, Subject):
            self.Repertoire_subject = Subject(**as_dict(self.Repertoire_subject))

        if self._is_empty(self.Repertoire_sample):
            self.MissingRequiredField("Repertoire_sample")
        self._normalize_inlined_as_dict(slot_name="Repertoire_sample", slot_type=SampleProcessing, key_name="Sample_sample_id", keyed=False)

        if self._is_empty(self.Repertoire_data_processing):
            self.MissingRequiredField("Repertoire_data_processing")
        self._normalize_inlined_as_dict(slot_name="Repertoire_data_processing", slot_type=DataProcessing, key_name="DataProcessing_software_versions", keyed=False)

        if self.Repertoire_repertoire_id is not None and not isinstance(self.Repertoire_repertoire_id, str):
            self.Repertoire_repertoire_id = str(self.Repertoire_repertoire_id)

        if self.Repertoire_repertoire_name is not None and not isinstance(self.Repertoire_repertoire_name, str):
            self.Repertoire_repertoire_name = str(self.Repertoire_repertoire_name)

        if self.Repertoire_repertoire_description is not None and not isinstance(self.Repertoire_repertoire_description, str):
            self.Repertoire_repertoire_description = str(self.Repertoire_repertoire_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RepertoireGroup(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["RepertoireGroup"]
    class_class_curie: ClassVar[str] = "ak_schema:RepertoireGroup"
    class_name: ClassVar[str] = "RepertoireGroup"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.RepertoireGroup

    RepertoireGroup_repertoire_group_id: str = None
    RepertoireGroup_repertoires: Union[str, List[str]] = None
    RepertoireGroup_repertoire_group_name: Optional[str] = None
    RepertoireGroup_repertoire_group_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.RepertoireGroup_repertoire_group_id):
            self.MissingRequiredField("RepertoireGroup_repertoire_group_id")
        if not isinstance(self.RepertoireGroup_repertoire_group_id, str):
            self.RepertoireGroup_repertoire_group_id = str(self.RepertoireGroup_repertoire_group_id)

        if self._is_empty(self.RepertoireGroup_repertoires):
            self.MissingRequiredField("RepertoireGroup_repertoires")
        if not isinstance(self.RepertoireGroup_repertoires, list):
            self.RepertoireGroup_repertoires = [self.RepertoireGroup_repertoires] if self.RepertoireGroup_repertoires is not None else []
        self.RepertoireGroup_repertoires = [v if isinstance(v, str) else str(v) for v in self.RepertoireGroup_repertoires]

        if self.RepertoireGroup_repertoire_group_name is not None and not isinstance(self.RepertoireGroup_repertoire_group_name, str):
            self.RepertoireGroup_repertoire_group_name = str(self.RepertoireGroup_repertoire_group_name)

        if self.RepertoireGroup_repertoire_group_description is not None and not isinstance(self.RepertoireGroup_repertoire_group_description, str):
            self.RepertoireGroup_repertoire_group_description = str(self.RepertoireGroup_repertoire_group_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Alignment(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Alignment"]
    class_class_curie: ClassVar[str] = "ak_schema:Alignment"
    class_name: ClassVar[str] = "Alignment"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Alignment

    Alignment_sequence_id: str = None
    Alignment_segment: str = None
    Alignment_call: str = None
    Alignment_score: float = None
    Alignment_cigar: str = None
    Alignment_rev_comp: Optional[Union[bool, Bool]] = None
    Alignment_identity: Optional[float] = None
    Alignment_support: Optional[float] = None
    Alignment_sequence_start: Optional[int] = None
    Alignment_sequence_end: Optional[int] = None
    Alignment_germline_start: Optional[int] = None
    Alignment_germline_end: Optional[int] = None
    Alignment_rank: Optional[int] = None
    Alignment_data_processing_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Alignment_sequence_id):
            self.MissingRequiredField("Alignment_sequence_id")
        if not isinstance(self.Alignment_sequence_id, str):
            self.Alignment_sequence_id = str(self.Alignment_sequence_id)

        if self._is_empty(self.Alignment_segment):
            self.MissingRequiredField("Alignment_segment")
        if not isinstance(self.Alignment_segment, str):
            self.Alignment_segment = str(self.Alignment_segment)

        if self._is_empty(self.Alignment_call):
            self.MissingRequiredField("Alignment_call")
        if not isinstance(self.Alignment_call, str):
            self.Alignment_call = str(self.Alignment_call)

        if self._is_empty(self.Alignment_score):
            self.MissingRequiredField("Alignment_score")
        if not isinstance(self.Alignment_score, float):
            self.Alignment_score = float(self.Alignment_score)

        if self._is_empty(self.Alignment_cigar):
            self.MissingRequiredField("Alignment_cigar")
        if not isinstance(self.Alignment_cigar, str):
            self.Alignment_cigar = str(self.Alignment_cigar)

        if self.Alignment_rev_comp is not None and not isinstance(self.Alignment_rev_comp, Bool):
            self.Alignment_rev_comp = Bool(self.Alignment_rev_comp)

        if self.Alignment_identity is not None and not isinstance(self.Alignment_identity, float):
            self.Alignment_identity = float(self.Alignment_identity)

        if self.Alignment_support is not None and not isinstance(self.Alignment_support, float):
            self.Alignment_support = float(self.Alignment_support)

        if self.Alignment_sequence_start is not None and not isinstance(self.Alignment_sequence_start, int):
            self.Alignment_sequence_start = int(self.Alignment_sequence_start)

        if self.Alignment_sequence_end is not None and not isinstance(self.Alignment_sequence_end, int):
            self.Alignment_sequence_end = int(self.Alignment_sequence_end)

        if self.Alignment_germline_start is not None and not isinstance(self.Alignment_germline_start, int):
            self.Alignment_germline_start = int(self.Alignment_germline_start)

        if self.Alignment_germline_end is not None and not isinstance(self.Alignment_germline_end, int):
            self.Alignment_germline_end = int(self.Alignment_germline_end)

        if self.Alignment_rank is not None and not isinstance(self.Alignment_rank, int):
            self.Alignment_rank = int(self.Alignment_rank)

        if self.Alignment_data_processing_id is not None and not isinstance(self.Alignment_data_processing_id, str):
            self.Alignment_data_processing_id = str(self.Alignment_data_processing_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rearrangement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Rearrangement"]
    class_class_curie: ClassVar[str] = "ak_schema:Rearrangement"
    class_name: ClassVar[str] = "Rearrangement"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Rearrangement

    Rearrangement_sequence_id: str = None
    Rearrangement_sequence: str = None
    Rearrangement_rev_comp: Union[bool, Bool] = None
    Rearrangement_productive: Union[bool, Bool] = None
    Rearrangement_v_call: str = None
    Rearrangement_d_call: str = None
    Rearrangement_j_call: str = None
    Rearrangement_sequence_alignment: str = None
    Rearrangement_germline_alignment: str = None
    Rearrangement_junction: str = None
    Rearrangement_junction_aa: str = None
    Rearrangement_v_cigar: str = None
    Rearrangement_d_cigar: str = None
    Rearrangement_j_cigar: str = None
    Rearrangement_quality: Optional[str] = None
    Rearrangement_sequence_aa: Optional[str] = None
    Rearrangement_vj_in_frame: Optional[Union[bool, Bool]] = None
    Rearrangement_stop_codon: Optional[Union[bool, Bool]] = None
    Rearrangement_complete_vdj: Optional[Union[bool, Bool]] = None
    Rearrangement_locus: Optional[Union[str, "Locus"]] = None
    Rearrangement_d2_call: Optional[str] = None
    Rearrangement_c_call: Optional[str] = None
    Rearrangement_quality_alignment: Optional[str] = None
    Rearrangement_sequence_alignment_aa: Optional[str] = None
    Rearrangement_germline_alignment_aa: Optional[str] = None
    Rearrangement_np1: Optional[str] = None
    Rearrangement_np1_aa: Optional[str] = None
    Rearrangement_np2: Optional[str] = None
    Rearrangement_np2_aa: Optional[str] = None
    Rearrangement_np3: Optional[str] = None
    Rearrangement_np3_aa: Optional[str] = None
    Rearrangement_cdr1: Optional[str] = None
    Rearrangement_cdr1_aa: Optional[str] = None
    Rearrangement_cdr2: Optional[str] = None
    Rearrangement_cdr2_aa: Optional[str] = None
    Rearrangement_cdr3: Optional[str] = None
    Rearrangement_cdr3_aa: Optional[str] = None
    Rearrangement_fwr1: Optional[str] = None
    Rearrangement_fwr1_aa: Optional[str] = None
    Rearrangement_fwr2: Optional[str] = None
    Rearrangement_fwr2_aa: Optional[str] = None
    Rearrangement_fwr3: Optional[str] = None
    Rearrangement_fwr3_aa: Optional[str] = None
    Rearrangement_fwr4: Optional[str] = None
    Rearrangement_fwr4_aa: Optional[str] = None
    Rearrangement_v_score: Optional[float] = None
    Rearrangement_v_identity: Optional[float] = None
    Rearrangement_v_support: Optional[float] = None
    Rearrangement_d_score: Optional[float] = None
    Rearrangement_d_identity: Optional[float] = None
    Rearrangement_d_support: Optional[float] = None
    Rearrangement_d2_score: Optional[float] = None
    Rearrangement_d2_identity: Optional[float] = None
    Rearrangement_d2_support: Optional[float] = None
    Rearrangement_d2_cigar: Optional[str] = None
    Rearrangement_j_score: Optional[float] = None
    Rearrangement_j_identity: Optional[float] = None
    Rearrangement_j_support: Optional[float] = None
    Rearrangement_c_score: Optional[float] = None
    Rearrangement_c_identity: Optional[float] = None
    Rearrangement_c_support: Optional[float] = None
    Rearrangement_c_cigar: Optional[str] = None
    Rearrangement_v_sequence_start: Optional[int] = None
    Rearrangement_v_sequence_end: Optional[int] = None
    Rearrangement_v_germline_start: Optional[int] = None
    Rearrangement_v_germline_end: Optional[int] = None
    Rearrangement_v_alignment_start: Optional[int] = None
    Rearrangement_v_alignment_end: Optional[int] = None
    Rearrangement_d_sequence_start: Optional[int] = None
    Rearrangement_d_sequence_end: Optional[int] = None
    Rearrangement_d_germline_start: Optional[int] = None
    Rearrangement_d_germline_end: Optional[int] = None
    Rearrangement_d_alignment_start: Optional[int] = None
    Rearrangement_d_alignment_end: Optional[int] = None
    Rearrangement_d2_sequence_start: Optional[int] = None
    Rearrangement_d2_sequence_end: Optional[int] = None
    Rearrangement_d2_germline_start: Optional[int] = None
    Rearrangement_d2_germline_end: Optional[int] = None
    Rearrangement_d2_alignment_start: Optional[int] = None
    Rearrangement_d2_alignment_end: Optional[int] = None
    Rearrangement_j_sequence_start: Optional[int] = None
    Rearrangement_j_sequence_end: Optional[int] = None
    Rearrangement_j_germline_start: Optional[int] = None
    Rearrangement_j_germline_end: Optional[int] = None
    Rearrangement_j_alignment_start: Optional[int] = None
    Rearrangement_j_alignment_end: Optional[int] = None
    Rearrangement_c_sequence_start: Optional[int] = None
    Rearrangement_c_sequence_end: Optional[int] = None
    Rearrangement_c_germline_start: Optional[int] = None
    Rearrangement_c_germline_end: Optional[int] = None
    Rearrangement_c_alignment_start: Optional[int] = None
    Rearrangement_c_alignment_end: Optional[int] = None
    Rearrangement_cdr1_start: Optional[int] = None
    Rearrangement_cdr1_end: Optional[int] = None
    Rearrangement_cdr2_start: Optional[int] = None
    Rearrangement_cdr2_end: Optional[int] = None
    Rearrangement_cdr3_start: Optional[int] = None
    Rearrangement_cdr3_end: Optional[int] = None
    Rearrangement_fwr1_start: Optional[int] = None
    Rearrangement_fwr1_end: Optional[int] = None
    Rearrangement_fwr2_start: Optional[int] = None
    Rearrangement_fwr2_end: Optional[int] = None
    Rearrangement_fwr3_start: Optional[int] = None
    Rearrangement_fwr3_end: Optional[int] = None
    Rearrangement_fwr4_start: Optional[int] = None
    Rearrangement_fwr4_end: Optional[int] = None
    Rearrangement_v_sequence_alignment: Optional[str] = None
    Rearrangement_v_sequence_alignment_aa: Optional[str] = None
    Rearrangement_d_sequence_alignment: Optional[str] = None
    Rearrangement_d_sequence_alignment_aa: Optional[str] = None
    Rearrangement_d2_sequence_alignment: Optional[str] = None
    Rearrangement_d2_sequence_alignment_aa: Optional[str] = None
    Rearrangement_j_sequence_alignment: Optional[str] = None
    Rearrangement_j_sequence_alignment_aa: Optional[str] = None
    Rearrangement_c_sequence_alignment: Optional[str] = None
    Rearrangement_c_sequence_alignment_aa: Optional[str] = None
    Rearrangement_v_germline_alignment: Optional[str] = None
    Rearrangement_v_germline_alignment_aa: Optional[str] = None
    Rearrangement_d_germline_alignment: Optional[str] = None
    Rearrangement_d_germline_alignment_aa: Optional[str] = None
    Rearrangement_d2_germline_alignment: Optional[str] = None
    Rearrangement_d2_germline_alignment_aa: Optional[str] = None
    Rearrangement_j_germline_alignment: Optional[str] = None
    Rearrangement_j_germline_alignment_aa: Optional[str] = None
    Rearrangement_c_germline_alignment: Optional[str] = None
    Rearrangement_c_germline_alignment_aa: Optional[str] = None
    Rearrangement_junction_length: Optional[int] = None
    Rearrangement_junction_aa_length: Optional[int] = None
    Rearrangement_np1_length: Optional[int] = None
    Rearrangement_np2_length: Optional[int] = None
    Rearrangement_np3_length: Optional[int] = None
    Rearrangement_n1_length: Optional[int] = None
    Rearrangement_n2_length: Optional[int] = None
    Rearrangement_n3_length: Optional[int] = None
    Rearrangement_p3v_length: Optional[int] = None
    Rearrangement_p5d_length: Optional[int] = None
    Rearrangement_p3d_length: Optional[int] = None
    Rearrangement_p5d2_length: Optional[int] = None
    Rearrangement_p3d2_length: Optional[int] = None
    Rearrangement_p5j_length: Optional[int] = None
    Rearrangement_v_frameshift: Optional[Union[bool, Bool]] = None
    Rearrangement_j_frameshift: Optional[Union[bool, Bool]] = None
    Rearrangement_d_frame: Optional[int] = None
    Rearrangement_d2_frame: Optional[int] = None
    Rearrangement_consensus_count: Optional[int] = None
    Rearrangement_duplicate_count: Optional[int] = None
    Rearrangement_umi_count: Optional[int] = None
    Rearrangement_cell_id: Optional[str] = None
    Rearrangement_clone_id: Optional[str] = None
    Rearrangement_repertoire_id: Optional[str] = None
    Rearrangement_sample_processing_id: Optional[str] = None
    Rearrangement_data_processing_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Rearrangement_sequence_id):
            self.MissingRequiredField("Rearrangement_sequence_id")
        if not isinstance(self.Rearrangement_sequence_id, str):
            self.Rearrangement_sequence_id = str(self.Rearrangement_sequence_id)

        if self._is_empty(self.Rearrangement_sequence):
            self.MissingRequiredField("Rearrangement_sequence")
        if not isinstance(self.Rearrangement_sequence, str):
            self.Rearrangement_sequence = str(self.Rearrangement_sequence)

        if self._is_empty(self.Rearrangement_rev_comp):
            self.MissingRequiredField("Rearrangement_rev_comp")
        if not isinstance(self.Rearrangement_rev_comp, Bool):
            self.Rearrangement_rev_comp = Bool(self.Rearrangement_rev_comp)

        if self._is_empty(self.Rearrangement_productive):
            self.MissingRequiredField("Rearrangement_productive")
        if not isinstance(self.Rearrangement_productive, Bool):
            self.Rearrangement_productive = Bool(self.Rearrangement_productive)

        if self._is_empty(self.Rearrangement_v_call):
            self.MissingRequiredField("Rearrangement_v_call")
        if not isinstance(self.Rearrangement_v_call, str):
            self.Rearrangement_v_call = str(self.Rearrangement_v_call)

        if self._is_empty(self.Rearrangement_d_call):
            self.MissingRequiredField("Rearrangement_d_call")
        if not isinstance(self.Rearrangement_d_call, str):
            self.Rearrangement_d_call = str(self.Rearrangement_d_call)

        if self._is_empty(self.Rearrangement_j_call):
            self.MissingRequiredField("Rearrangement_j_call")
        if not isinstance(self.Rearrangement_j_call, str):
            self.Rearrangement_j_call = str(self.Rearrangement_j_call)

        if self._is_empty(self.Rearrangement_sequence_alignment):
            self.MissingRequiredField("Rearrangement_sequence_alignment")
        if not isinstance(self.Rearrangement_sequence_alignment, str):
            self.Rearrangement_sequence_alignment = str(self.Rearrangement_sequence_alignment)

        if self._is_empty(self.Rearrangement_germline_alignment):
            self.MissingRequiredField("Rearrangement_germline_alignment")
        if not isinstance(self.Rearrangement_germline_alignment, str):
            self.Rearrangement_germline_alignment = str(self.Rearrangement_germline_alignment)

        if self._is_empty(self.Rearrangement_junction):
            self.MissingRequiredField("Rearrangement_junction")
        if not isinstance(self.Rearrangement_junction, str):
            self.Rearrangement_junction = str(self.Rearrangement_junction)

        if self._is_empty(self.Rearrangement_junction_aa):
            self.MissingRequiredField("Rearrangement_junction_aa")
        if not isinstance(self.Rearrangement_junction_aa, str):
            self.Rearrangement_junction_aa = str(self.Rearrangement_junction_aa)

        if self._is_empty(self.Rearrangement_v_cigar):
            self.MissingRequiredField("Rearrangement_v_cigar")
        if not isinstance(self.Rearrangement_v_cigar, str):
            self.Rearrangement_v_cigar = str(self.Rearrangement_v_cigar)

        if self._is_empty(self.Rearrangement_d_cigar):
            self.MissingRequiredField("Rearrangement_d_cigar")
        if not isinstance(self.Rearrangement_d_cigar, str):
            self.Rearrangement_d_cigar = str(self.Rearrangement_d_cigar)

        if self._is_empty(self.Rearrangement_j_cigar):
            self.MissingRequiredField("Rearrangement_j_cigar")
        if not isinstance(self.Rearrangement_j_cigar, str):
            self.Rearrangement_j_cigar = str(self.Rearrangement_j_cigar)

        if self.Rearrangement_quality is not None and not isinstance(self.Rearrangement_quality, str):
            self.Rearrangement_quality = str(self.Rearrangement_quality)

        if self.Rearrangement_sequence_aa is not None and not isinstance(self.Rearrangement_sequence_aa, str):
            self.Rearrangement_sequence_aa = str(self.Rearrangement_sequence_aa)

        if self.Rearrangement_vj_in_frame is not None and not isinstance(self.Rearrangement_vj_in_frame, Bool):
            self.Rearrangement_vj_in_frame = Bool(self.Rearrangement_vj_in_frame)

        if self.Rearrangement_stop_codon is not None and not isinstance(self.Rearrangement_stop_codon, Bool):
            self.Rearrangement_stop_codon = Bool(self.Rearrangement_stop_codon)

        if self.Rearrangement_complete_vdj is not None and not isinstance(self.Rearrangement_complete_vdj, Bool):
            self.Rearrangement_complete_vdj = Bool(self.Rearrangement_complete_vdj)

        if self.Rearrangement_locus is not None and not isinstance(self.Rearrangement_locus, Locus):
            self.Rearrangement_locus = Locus(self.Rearrangement_locus)

        if self.Rearrangement_d2_call is not None and not isinstance(self.Rearrangement_d2_call, str):
            self.Rearrangement_d2_call = str(self.Rearrangement_d2_call)

        if self.Rearrangement_c_call is not None and not isinstance(self.Rearrangement_c_call, str):
            self.Rearrangement_c_call = str(self.Rearrangement_c_call)

        if self.Rearrangement_quality_alignment is not None and not isinstance(self.Rearrangement_quality_alignment, str):
            self.Rearrangement_quality_alignment = str(self.Rearrangement_quality_alignment)

        if self.Rearrangement_sequence_alignment_aa is not None and not isinstance(self.Rearrangement_sequence_alignment_aa, str):
            self.Rearrangement_sequence_alignment_aa = str(self.Rearrangement_sequence_alignment_aa)

        if self.Rearrangement_germline_alignment_aa is not None and not isinstance(self.Rearrangement_germline_alignment_aa, str):
            self.Rearrangement_germline_alignment_aa = str(self.Rearrangement_germline_alignment_aa)

        if self.Rearrangement_np1 is not None and not isinstance(self.Rearrangement_np1, str):
            self.Rearrangement_np1 = str(self.Rearrangement_np1)

        if self.Rearrangement_np1_aa is not None and not isinstance(self.Rearrangement_np1_aa, str):
            self.Rearrangement_np1_aa = str(self.Rearrangement_np1_aa)

        if self.Rearrangement_np2 is not None and not isinstance(self.Rearrangement_np2, str):
            self.Rearrangement_np2 = str(self.Rearrangement_np2)

        if self.Rearrangement_np2_aa is not None and not isinstance(self.Rearrangement_np2_aa, str):
            self.Rearrangement_np2_aa = str(self.Rearrangement_np2_aa)

        if self.Rearrangement_np3 is not None and not isinstance(self.Rearrangement_np3, str):
            self.Rearrangement_np3 = str(self.Rearrangement_np3)

        if self.Rearrangement_np3_aa is not None and not isinstance(self.Rearrangement_np3_aa, str):
            self.Rearrangement_np3_aa = str(self.Rearrangement_np3_aa)

        if self.Rearrangement_cdr1 is not None and not isinstance(self.Rearrangement_cdr1, str):
            self.Rearrangement_cdr1 = str(self.Rearrangement_cdr1)

        if self.Rearrangement_cdr1_aa is not None and not isinstance(self.Rearrangement_cdr1_aa, str):
            self.Rearrangement_cdr1_aa = str(self.Rearrangement_cdr1_aa)

        if self.Rearrangement_cdr2 is not None and not isinstance(self.Rearrangement_cdr2, str):
            self.Rearrangement_cdr2 = str(self.Rearrangement_cdr2)

        if self.Rearrangement_cdr2_aa is not None and not isinstance(self.Rearrangement_cdr2_aa, str):
            self.Rearrangement_cdr2_aa = str(self.Rearrangement_cdr2_aa)

        if self.Rearrangement_cdr3 is not None and not isinstance(self.Rearrangement_cdr3, str):
            self.Rearrangement_cdr3 = str(self.Rearrangement_cdr3)

        if self.Rearrangement_cdr3_aa is not None and not isinstance(self.Rearrangement_cdr3_aa, str):
            self.Rearrangement_cdr3_aa = str(self.Rearrangement_cdr3_aa)

        if self.Rearrangement_fwr1 is not None and not isinstance(self.Rearrangement_fwr1, str):
            self.Rearrangement_fwr1 = str(self.Rearrangement_fwr1)

        if self.Rearrangement_fwr1_aa is not None and not isinstance(self.Rearrangement_fwr1_aa, str):
            self.Rearrangement_fwr1_aa = str(self.Rearrangement_fwr1_aa)

        if self.Rearrangement_fwr2 is not None and not isinstance(self.Rearrangement_fwr2, str):
            self.Rearrangement_fwr2 = str(self.Rearrangement_fwr2)

        if self.Rearrangement_fwr2_aa is not None and not isinstance(self.Rearrangement_fwr2_aa, str):
            self.Rearrangement_fwr2_aa = str(self.Rearrangement_fwr2_aa)

        if self.Rearrangement_fwr3 is not None and not isinstance(self.Rearrangement_fwr3, str):
            self.Rearrangement_fwr3 = str(self.Rearrangement_fwr3)

        if self.Rearrangement_fwr3_aa is not None and not isinstance(self.Rearrangement_fwr3_aa, str):
            self.Rearrangement_fwr3_aa = str(self.Rearrangement_fwr3_aa)

        if self.Rearrangement_fwr4 is not None and not isinstance(self.Rearrangement_fwr4, str):
            self.Rearrangement_fwr4 = str(self.Rearrangement_fwr4)

        if self.Rearrangement_fwr4_aa is not None and not isinstance(self.Rearrangement_fwr4_aa, str):
            self.Rearrangement_fwr4_aa = str(self.Rearrangement_fwr4_aa)

        if self.Rearrangement_v_score is not None and not isinstance(self.Rearrangement_v_score, float):
            self.Rearrangement_v_score = float(self.Rearrangement_v_score)

        if self.Rearrangement_v_identity is not None and not isinstance(self.Rearrangement_v_identity, float):
            self.Rearrangement_v_identity = float(self.Rearrangement_v_identity)

        if self.Rearrangement_v_support is not None and not isinstance(self.Rearrangement_v_support, float):
            self.Rearrangement_v_support = float(self.Rearrangement_v_support)

        if self.Rearrangement_d_score is not None and not isinstance(self.Rearrangement_d_score, float):
            self.Rearrangement_d_score = float(self.Rearrangement_d_score)

        if self.Rearrangement_d_identity is not None and not isinstance(self.Rearrangement_d_identity, float):
            self.Rearrangement_d_identity = float(self.Rearrangement_d_identity)

        if self.Rearrangement_d_support is not None and not isinstance(self.Rearrangement_d_support, float):
            self.Rearrangement_d_support = float(self.Rearrangement_d_support)

        if self.Rearrangement_d2_score is not None and not isinstance(self.Rearrangement_d2_score, float):
            self.Rearrangement_d2_score = float(self.Rearrangement_d2_score)

        if self.Rearrangement_d2_identity is not None and not isinstance(self.Rearrangement_d2_identity, float):
            self.Rearrangement_d2_identity = float(self.Rearrangement_d2_identity)

        if self.Rearrangement_d2_support is not None and not isinstance(self.Rearrangement_d2_support, float):
            self.Rearrangement_d2_support = float(self.Rearrangement_d2_support)

        if self.Rearrangement_d2_cigar is not None and not isinstance(self.Rearrangement_d2_cigar, str):
            self.Rearrangement_d2_cigar = str(self.Rearrangement_d2_cigar)

        if self.Rearrangement_j_score is not None and not isinstance(self.Rearrangement_j_score, float):
            self.Rearrangement_j_score = float(self.Rearrangement_j_score)

        if self.Rearrangement_j_identity is not None and not isinstance(self.Rearrangement_j_identity, float):
            self.Rearrangement_j_identity = float(self.Rearrangement_j_identity)

        if self.Rearrangement_j_support is not None and not isinstance(self.Rearrangement_j_support, float):
            self.Rearrangement_j_support = float(self.Rearrangement_j_support)

        if self.Rearrangement_c_score is not None and not isinstance(self.Rearrangement_c_score, float):
            self.Rearrangement_c_score = float(self.Rearrangement_c_score)

        if self.Rearrangement_c_identity is not None and not isinstance(self.Rearrangement_c_identity, float):
            self.Rearrangement_c_identity = float(self.Rearrangement_c_identity)

        if self.Rearrangement_c_support is not None and not isinstance(self.Rearrangement_c_support, float):
            self.Rearrangement_c_support = float(self.Rearrangement_c_support)

        if self.Rearrangement_c_cigar is not None and not isinstance(self.Rearrangement_c_cigar, str):
            self.Rearrangement_c_cigar = str(self.Rearrangement_c_cigar)

        if self.Rearrangement_v_sequence_start is not None and not isinstance(self.Rearrangement_v_sequence_start, int):
            self.Rearrangement_v_sequence_start = int(self.Rearrangement_v_sequence_start)

        if self.Rearrangement_v_sequence_end is not None and not isinstance(self.Rearrangement_v_sequence_end, int):
            self.Rearrangement_v_sequence_end = int(self.Rearrangement_v_sequence_end)

        if self.Rearrangement_v_germline_start is not None and not isinstance(self.Rearrangement_v_germline_start, int):
            self.Rearrangement_v_germline_start = int(self.Rearrangement_v_germline_start)

        if self.Rearrangement_v_germline_end is not None and not isinstance(self.Rearrangement_v_germline_end, int):
            self.Rearrangement_v_germline_end = int(self.Rearrangement_v_germline_end)

        if self.Rearrangement_v_alignment_start is not None and not isinstance(self.Rearrangement_v_alignment_start, int):
            self.Rearrangement_v_alignment_start = int(self.Rearrangement_v_alignment_start)

        if self.Rearrangement_v_alignment_end is not None and not isinstance(self.Rearrangement_v_alignment_end, int):
            self.Rearrangement_v_alignment_end = int(self.Rearrangement_v_alignment_end)

        if self.Rearrangement_d_sequence_start is not None and not isinstance(self.Rearrangement_d_sequence_start, int):
            self.Rearrangement_d_sequence_start = int(self.Rearrangement_d_sequence_start)

        if self.Rearrangement_d_sequence_end is not None and not isinstance(self.Rearrangement_d_sequence_end, int):
            self.Rearrangement_d_sequence_end = int(self.Rearrangement_d_sequence_end)

        if self.Rearrangement_d_germline_start is not None and not isinstance(self.Rearrangement_d_germline_start, int):
            self.Rearrangement_d_germline_start = int(self.Rearrangement_d_germline_start)

        if self.Rearrangement_d_germline_end is not None and not isinstance(self.Rearrangement_d_germline_end, int):
            self.Rearrangement_d_germline_end = int(self.Rearrangement_d_germline_end)

        if self.Rearrangement_d_alignment_start is not None and not isinstance(self.Rearrangement_d_alignment_start, int):
            self.Rearrangement_d_alignment_start = int(self.Rearrangement_d_alignment_start)

        if self.Rearrangement_d_alignment_end is not None and not isinstance(self.Rearrangement_d_alignment_end, int):
            self.Rearrangement_d_alignment_end = int(self.Rearrangement_d_alignment_end)

        if self.Rearrangement_d2_sequence_start is not None and not isinstance(self.Rearrangement_d2_sequence_start, int):
            self.Rearrangement_d2_sequence_start = int(self.Rearrangement_d2_sequence_start)

        if self.Rearrangement_d2_sequence_end is not None and not isinstance(self.Rearrangement_d2_sequence_end, int):
            self.Rearrangement_d2_sequence_end = int(self.Rearrangement_d2_sequence_end)

        if self.Rearrangement_d2_germline_start is not None and not isinstance(self.Rearrangement_d2_germline_start, int):
            self.Rearrangement_d2_germline_start = int(self.Rearrangement_d2_germline_start)

        if self.Rearrangement_d2_germline_end is not None and not isinstance(self.Rearrangement_d2_germline_end, int):
            self.Rearrangement_d2_germline_end = int(self.Rearrangement_d2_germline_end)

        if self.Rearrangement_d2_alignment_start is not None and not isinstance(self.Rearrangement_d2_alignment_start, int):
            self.Rearrangement_d2_alignment_start = int(self.Rearrangement_d2_alignment_start)

        if self.Rearrangement_d2_alignment_end is not None and not isinstance(self.Rearrangement_d2_alignment_end, int):
            self.Rearrangement_d2_alignment_end = int(self.Rearrangement_d2_alignment_end)

        if self.Rearrangement_j_sequence_start is not None and not isinstance(self.Rearrangement_j_sequence_start, int):
            self.Rearrangement_j_sequence_start = int(self.Rearrangement_j_sequence_start)

        if self.Rearrangement_j_sequence_end is not None and not isinstance(self.Rearrangement_j_sequence_end, int):
            self.Rearrangement_j_sequence_end = int(self.Rearrangement_j_sequence_end)

        if self.Rearrangement_j_germline_start is not None and not isinstance(self.Rearrangement_j_germline_start, int):
            self.Rearrangement_j_germline_start = int(self.Rearrangement_j_germline_start)

        if self.Rearrangement_j_germline_end is not None and not isinstance(self.Rearrangement_j_germline_end, int):
            self.Rearrangement_j_germline_end = int(self.Rearrangement_j_germline_end)

        if self.Rearrangement_j_alignment_start is not None and not isinstance(self.Rearrangement_j_alignment_start, int):
            self.Rearrangement_j_alignment_start = int(self.Rearrangement_j_alignment_start)

        if self.Rearrangement_j_alignment_end is not None and not isinstance(self.Rearrangement_j_alignment_end, int):
            self.Rearrangement_j_alignment_end = int(self.Rearrangement_j_alignment_end)

        if self.Rearrangement_c_sequence_start is not None and not isinstance(self.Rearrangement_c_sequence_start, int):
            self.Rearrangement_c_sequence_start = int(self.Rearrangement_c_sequence_start)

        if self.Rearrangement_c_sequence_end is not None and not isinstance(self.Rearrangement_c_sequence_end, int):
            self.Rearrangement_c_sequence_end = int(self.Rearrangement_c_sequence_end)

        if self.Rearrangement_c_germline_start is not None and not isinstance(self.Rearrangement_c_germline_start, int):
            self.Rearrangement_c_germline_start = int(self.Rearrangement_c_germline_start)

        if self.Rearrangement_c_germline_end is not None and not isinstance(self.Rearrangement_c_germline_end, int):
            self.Rearrangement_c_germline_end = int(self.Rearrangement_c_germline_end)

        if self.Rearrangement_c_alignment_start is not None and not isinstance(self.Rearrangement_c_alignment_start, int):
            self.Rearrangement_c_alignment_start = int(self.Rearrangement_c_alignment_start)

        if self.Rearrangement_c_alignment_end is not None and not isinstance(self.Rearrangement_c_alignment_end, int):
            self.Rearrangement_c_alignment_end = int(self.Rearrangement_c_alignment_end)

        if self.Rearrangement_cdr1_start is not None and not isinstance(self.Rearrangement_cdr1_start, int):
            self.Rearrangement_cdr1_start = int(self.Rearrangement_cdr1_start)

        if self.Rearrangement_cdr1_end is not None and not isinstance(self.Rearrangement_cdr1_end, int):
            self.Rearrangement_cdr1_end = int(self.Rearrangement_cdr1_end)

        if self.Rearrangement_cdr2_start is not None and not isinstance(self.Rearrangement_cdr2_start, int):
            self.Rearrangement_cdr2_start = int(self.Rearrangement_cdr2_start)

        if self.Rearrangement_cdr2_end is not None and not isinstance(self.Rearrangement_cdr2_end, int):
            self.Rearrangement_cdr2_end = int(self.Rearrangement_cdr2_end)

        if self.Rearrangement_cdr3_start is not None and not isinstance(self.Rearrangement_cdr3_start, int):
            self.Rearrangement_cdr3_start = int(self.Rearrangement_cdr3_start)

        if self.Rearrangement_cdr3_end is not None and not isinstance(self.Rearrangement_cdr3_end, int):
            self.Rearrangement_cdr3_end = int(self.Rearrangement_cdr3_end)

        if self.Rearrangement_fwr1_start is not None and not isinstance(self.Rearrangement_fwr1_start, int):
            self.Rearrangement_fwr1_start = int(self.Rearrangement_fwr1_start)

        if self.Rearrangement_fwr1_end is not None and not isinstance(self.Rearrangement_fwr1_end, int):
            self.Rearrangement_fwr1_end = int(self.Rearrangement_fwr1_end)

        if self.Rearrangement_fwr2_start is not None and not isinstance(self.Rearrangement_fwr2_start, int):
            self.Rearrangement_fwr2_start = int(self.Rearrangement_fwr2_start)

        if self.Rearrangement_fwr2_end is not None and not isinstance(self.Rearrangement_fwr2_end, int):
            self.Rearrangement_fwr2_end = int(self.Rearrangement_fwr2_end)

        if self.Rearrangement_fwr3_start is not None and not isinstance(self.Rearrangement_fwr3_start, int):
            self.Rearrangement_fwr3_start = int(self.Rearrangement_fwr3_start)

        if self.Rearrangement_fwr3_end is not None and not isinstance(self.Rearrangement_fwr3_end, int):
            self.Rearrangement_fwr3_end = int(self.Rearrangement_fwr3_end)

        if self.Rearrangement_fwr4_start is not None and not isinstance(self.Rearrangement_fwr4_start, int):
            self.Rearrangement_fwr4_start = int(self.Rearrangement_fwr4_start)

        if self.Rearrangement_fwr4_end is not None and not isinstance(self.Rearrangement_fwr4_end, int):
            self.Rearrangement_fwr4_end = int(self.Rearrangement_fwr4_end)

        if self.Rearrangement_v_sequence_alignment is not None and not isinstance(self.Rearrangement_v_sequence_alignment, str):
            self.Rearrangement_v_sequence_alignment = str(self.Rearrangement_v_sequence_alignment)

        if self.Rearrangement_v_sequence_alignment_aa is not None and not isinstance(self.Rearrangement_v_sequence_alignment_aa, str):
            self.Rearrangement_v_sequence_alignment_aa = str(self.Rearrangement_v_sequence_alignment_aa)

        if self.Rearrangement_d_sequence_alignment is not None and not isinstance(self.Rearrangement_d_sequence_alignment, str):
            self.Rearrangement_d_sequence_alignment = str(self.Rearrangement_d_sequence_alignment)

        if self.Rearrangement_d_sequence_alignment_aa is not None and not isinstance(self.Rearrangement_d_sequence_alignment_aa, str):
            self.Rearrangement_d_sequence_alignment_aa = str(self.Rearrangement_d_sequence_alignment_aa)

        if self.Rearrangement_d2_sequence_alignment is not None and not isinstance(self.Rearrangement_d2_sequence_alignment, str):
            self.Rearrangement_d2_sequence_alignment = str(self.Rearrangement_d2_sequence_alignment)

        if self.Rearrangement_d2_sequence_alignment_aa is not None and not isinstance(self.Rearrangement_d2_sequence_alignment_aa, str):
            self.Rearrangement_d2_sequence_alignment_aa = str(self.Rearrangement_d2_sequence_alignment_aa)

        if self.Rearrangement_j_sequence_alignment is not None and not isinstance(self.Rearrangement_j_sequence_alignment, str):
            self.Rearrangement_j_sequence_alignment = str(self.Rearrangement_j_sequence_alignment)

        if self.Rearrangement_j_sequence_alignment_aa is not None and not isinstance(self.Rearrangement_j_sequence_alignment_aa, str):
            self.Rearrangement_j_sequence_alignment_aa = str(self.Rearrangement_j_sequence_alignment_aa)

        if self.Rearrangement_c_sequence_alignment is not None and not isinstance(self.Rearrangement_c_sequence_alignment, str):
            self.Rearrangement_c_sequence_alignment = str(self.Rearrangement_c_sequence_alignment)

        if self.Rearrangement_c_sequence_alignment_aa is not None and not isinstance(self.Rearrangement_c_sequence_alignment_aa, str):
            self.Rearrangement_c_sequence_alignment_aa = str(self.Rearrangement_c_sequence_alignment_aa)

        if self.Rearrangement_v_germline_alignment is not None and not isinstance(self.Rearrangement_v_germline_alignment, str):
            self.Rearrangement_v_germline_alignment = str(self.Rearrangement_v_germline_alignment)

        if self.Rearrangement_v_germline_alignment_aa is not None and not isinstance(self.Rearrangement_v_germline_alignment_aa, str):
            self.Rearrangement_v_germline_alignment_aa = str(self.Rearrangement_v_germline_alignment_aa)

        if self.Rearrangement_d_germline_alignment is not None and not isinstance(self.Rearrangement_d_germline_alignment, str):
            self.Rearrangement_d_germline_alignment = str(self.Rearrangement_d_germline_alignment)

        if self.Rearrangement_d_germline_alignment_aa is not None and not isinstance(self.Rearrangement_d_germline_alignment_aa, str):
            self.Rearrangement_d_germline_alignment_aa = str(self.Rearrangement_d_germline_alignment_aa)

        if self.Rearrangement_d2_germline_alignment is not None and not isinstance(self.Rearrangement_d2_germline_alignment, str):
            self.Rearrangement_d2_germline_alignment = str(self.Rearrangement_d2_germline_alignment)

        if self.Rearrangement_d2_germline_alignment_aa is not None and not isinstance(self.Rearrangement_d2_germline_alignment_aa, str):
            self.Rearrangement_d2_germline_alignment_aa = str(self.Rearrangement_d2_germline_alignment_aa)

        if self.Rearrangement_j_germline_alignment is not None and not isinstance(self.Rearrangement_j_germline_alignment, str):
            self.Rearrangement_j_germline_alignment = str(self.Rearrangement_j_germline_alignment)

        if self.Rearrangement_j_germline_alignment_aa is not None and not isinstance(self.Rearrangement_j_germline_alignment_aa, str):
            self.Rearrangement_j_germline_alignment_aa = str(self.Rearrangement_j_germline_alignment_aa)

        if self.Rearrangement_c_germline_alignment is not None and not isinstance(self.Rearrangement_c_germline_alignment, str):
            self.Rearrangement_c_germline_alignment = str(self.Rearrangement_c_germline_alignment)

        if self.Rearrangement_c_germline_alignment_aa is not None and not isinstance(self.Rearrangement_c_germline_alignment_aa, str):
            self.Rearrangement_c_germline_alignment_aa = str(self.Rearrangement_c_germline_alignment_aa)

        if self.Rearrangement_junction_length is not None and not isinstance(self.Rearrangement_junction_length, int):
            self.Rearrangement_junction_length = int(self.Rearrangement_junction_length)

        if self.Rearrangement_junction_aa_length is not None and not isinstance(self.Rearrangement_junction_aa_length, int):
            self.Rearrangement_junction_aa_length = int(self.Rearrangement_junction_aa_length)

        if self.Rearrangement_np1_length is not None and not isinstance(self.Rearrangement_np1_length, int):
            self.Rearrangement_np1_length = int(self.Rearrangement_np1_length)

        if self.Rearrangement_np2_length is not None and not isinstance(self.Rearrangement_np2_length, int):
            self.Rearrangement_np2_length = int(self.Rearrangement_np2_length)

        if self.Rearrangement_np3_length is not None and not isinstance(self.Rearrangement_np3_length, int):
            self.Rearrangement_np3_length = int(self.Rearrangement_np3_length)

        if self.Rearrangement_n1_length is not None and not isinstance(self.Rearrangement_n1_length, int):
            self.Rearrangement_n1_length = int(self.Rearrangement_n1_length)

        if self.Rearrangement_n2_length is not None and not isinstance(self.Rearrangement_n2_length, int):
            self.Rearrangement_n2_length = int(self.Rearrangement_n2_length)

        if self.Rearrangement_n3_length is not None and not isinstance(self.Rearrangement_n3_length, int):
            self.Rearrangement_n3_length = int(self.Rearrangement_n3_length)

        if self.Rearrangement_p3v_length is not None and not isinstance(self.Rearrangement_p3v_length, int):
            self.Rearrangement_p3v_length = int(self.Rearrangement_p3v_length)

        if self.Rearrangement_p5d_length is not None and not isinstance(self.Rearrangement_p5d_length, int):
            self.Rearrangement_p5d_length = int(self.Rearrangement_p5d_length)

        if self.Rearrangement_p3d_length is not None and not isinstance(self.Rearrangement_p3d_length, int):
            self.Rearrangement_p3d_length = int(self.Rearrangement_p3d_length)

        if self.Rearrangement_p5d2_length is not None and not isinstance(self.Rearrangement_p5d2_length, int):
            self.Rearrangement_p5d2_length = int(self.Rearrangement_p5d2_length)

        if self.Rearrangement_p3d2_length is not None and not isinstance(self.Rearrangement_p3d2_length, int):
            self.Rearrangement_p3d2_length = int(self.Rearrangement_p3d2_length)

        if self.Rearrangement_p5j_length is not None and not isinstance(self.Rearrangement_p5j_length, int):
            self.Rearrangement_p5j_length = int(self.Rearrangement_p5j_length)

        if self.Rearrangement_v_frameshift is not None and not isinstance(self.Rearrangement_v_frameshift, Bool):
            self.Rearrangement_v_frameshift = Bool(self.Rearrangement_v_frameshift)

        if self.Rearrangement_j_frameshift is not None and not isinstance(self.Rearrangement_j_frameshift, Bool):
            self.Rearrangement_j_frameshift = Bool(self.Rearrangement_j_frameshift)

        if self.Rearrangement_d_frame is not None and not isinstance(self.Rearrangement_d_frame, int):
            self.Rearrangement_d_frame = int(self.Rearrangement_d_frame)

        if self.Rearrangement_d2_frame is not None and not isinstance(self.Rearrangement_d2_frame, int):
            self.Rearrangement_d2_frame = int(self.Rearrangement_d2_frame)

        if self.Rearrangement_consensus_count is not None and not isinstance(self.Rearrangement_consensus_count, int):
            self.Rearrangement_consensus_count = int(self.Rearrangement_consensus_count)

        if self.Rearrangement_duplicate_count is not None and not isinstance(self.Rearrangement_duplicate_count, int):
            self.Rearrangement_duplicate_count = int(self.Rearrangement_duplicate_count)

        if self.Rearrangement_umi_count is not None and not isinstance(self.Rearrangement_umi_count, int):
            self.Rearrangement_umi_count = int(self.Rearrangement_umi_count)

        if self.Rearrangement_cell_id is not None and not isinstance(self.Rearrangement_cell_id, str):
            self.Rearrangement_cell_id = str(self.Rearrangement_cell_id)

        if self.Rearrangement_clone_id is not None and not isinstance(self.Rearrangement_clone_id, str):
            self.Rearrangement_clone_id = str(self.Rearrangement_clone_id)

        if self.Rearrangement_repertoire_id is not None and not isinstance(self.Rearrangement_repertoire_id, str):
            self.Rearrangement_repertoire_id = str(self.Rearrangement_repertoire_id)

        if self.Rearrangement_sample_processing_id is not None and not isinstance(self.Rearrangement_sample_processing_id, str):
            self.Rearrangement_sample_processing_id = str(self.Rearrangement_sample_processing_id)

        if self.Rearrangement_data_processing_id is not None and not isinstance(self.Rearrangement_data_processing_id, str):
            self.Rearrangement_data_processing_id = str(self.Rearrangement_data_processing_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Clone(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Clone"]
    class_class_curie: ClassVar[str] = "ak_schema:Clone"
    class_name: ClassVar[str] = "Clone"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Clone

    Clone_clone_id: str = None
    Clone_germline_alignment: str = None
    Clone_repertoire_id: Optional[str] = None
    Clone_data_processing_id: Optional[str] = None
    Clone_sequences: Optional[Union[str, List[str]]] = empty_list()
    Clone_v_call: Optional[str] = None
    Clone_d_call: Optional[str] = None
    Clone_j_call: Optional[str] = None
    Clone_junction: Optional[str] = None
    Clone_junction_aa: Optional[str] = None
    Clone_junction_length: Optional[int] = None
    Clone_junction_aa_length: Optional[int] = None
    Clone_germline_alignment_aa: Optional[str] = None
    Clone_v_alignment_start: Optional[int] = None
    Clone_v_alignment_end: Optional[int] = None
    Clone_d_alignment_start: Optional[int] = None
    Clone_d_alignment_end: Optional[int] = None
    Clone_j_alignment_start: Optional[int] = None
    Clone_j_alignment_end: Optional[int] = None
    Clone_junction_start: Optional[int] = None
    Clone_junction_end: Optional[int] = None
    Clone_umi_count: Optional[int] = None
    Clone_clone_count: Optional[int] = None
    Clone_seed_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Clone_clone_id):
            self.MissingRequiredField("Clone_clone_id")
        if not isinstance(self.Clone_clone_id, str):
            self.Clone_clone_id = str(self.Clone_clone_id)

        if self._is_empty(self.Clone_germline_alignment):
            self.MissingRequiredField("Clone_germline_alignment")
        if not isinstance(self.Clone_germline_alignment, str):
            self.Clone_germline_alignment = str(self.Clone_germline_alignment)

        if self.Clone_repertoire_id is not None and not isinstance(self.Clone_repertoire_id, str):
            self.Clone_repertoire_id = str(self.Clone_repertoire_id)

        if self.Clone_data_processing_id is not None and not isinstance(self.Clone_data_processing_id, str):
            self.Clone_data_processing_id = str(self.Clone_data_processing_id)

        if not isinstance(self.Clone_sequences, list):
            self.Clone_sequences = [self.Clone_sequences] if self.Clone_sequences is not None else []
        self.Clone_sequences = [v if isinstance(v, str) else str(v) for v in self.Clone_sequences]

        if self.Clone_v_call is not None and not isinstance(self.Clone_v_call, str):
            self.Clone_v_call = str(self.Clone_v_call)

        if self.Clone_d_call is not None and not isinstance(self.Clone_d_call, str):
            self.Clone_d_call = str(self.Clone_d_call)

        if self.Clone_j_call is not None and not isinstance(self.Clone_j_call, str):
            self.Clone_j_call = str(self.Clone_j_call)

        if self.Clone_junction is not None and not isinstance(self.Clone_junction, str):
            self.Clone_junction = str(self.Clone_junction)

        if self.Clone_junction_aa is not None and not isinstance(self.Clone_junction_aa, str):
            self.Clone_junction_aa = str(self.Clone_junction_aa)

        if self.Clone_junction_length is not None and not isinstance(self.Clone_junction_length, int):
            self.Clone_junction_length = int(self.Clone_junction_length)

        if self.Clone_junction_aa_length is not None and not isinstance(self.Clone_junction_aa_length, int):
            self.Clone_junction_aa_length = int(self.Clone_junction_aa_length)

        if self.Clone_germline_alignment_aa is not None and not isinstance(self.Clone_germline_alignment_aa, str):
            self.Clone_germline_alignment_aa = str(self.Clone_germline_alignment_aa)

        if self.Clone_v_alignment_start is not None and not isinstance(self.Clone_v_alignment_start, int):
            self.Clone_v_alignment_start = int(self.Clone_v_alignment_start)

        if self.Clone_v_alignment_end is not None and not isinstance(self.Clone_v_alignment_end, int):
            self.Clone_v_alignment_end = int(self.Clone_v_alignment_end)

        if self.Clone_d_alignment_start is not None and not isinstance(self.Clone_d_alignment_start, int):
            self.Clone_d_alignment_start = int(self.Clone_d_alignment_start)

        if self.Clone_d_alignment_end is not None and not isinstance(self.Clone_d_alignment_end, int):
            self.Clone_d_alignment_end = int(self.Clone_d_alignment_end)

        if self.Clone_j_alignment_start is not None and not isinstance(self.Clone_j_alignment_start, int):
            self.Clone_j_alignment_start = int(self.Clone_j_alignment_start)

        if self.Clone_j_alignment_end is not None and not isinstance(self.Clone_j_alignment_end, int):
            self.Clone_j_alignment_end = int(self.Clone_j_alignment_end)

        if self.Clone_junction_start is not None and not isinstance(self.Clone_junction_start, int):
            self.Clone_junction_start = int(self.Clone_junction_start)

        if self.Clone_junction_end is not None and not isinstance(self.Clone_junction_end, int):
            self.Clone_junction_end = int(self.Clone_junction_end)

        if self.Clone_umi_count is not None and not isinstance(self.Clone_umi_count, int):
            self.Clone_umi_count = int(self.Clone_umi_count)

        if self.Clone_clone_count is not None and not isinstance(self.Clone_clone_count, int):
            self.Clone_clone_count = int(self.Clone_clone_count)

        if self.Clone_seed_id is not None and not isinstance(self.Clone_seed_id, str):
            self.Clone_seed_id = str(self.Clone_seed_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tree(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Tree"]
    class_class_curie: ClassVar[str] = "ak_schema:Tree"
    class_name: ClassVar[str] = "Tree"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Tree

    Tree_tree_id: str = None
    Tree_clone_id: str = None
    Tree_newick: str = None
    Tree_nodes: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Tree_tree_id):
            self.MissingRequiredField("Tree_tree_id")
        if not isinstance(self.Tree_tree_id, str):
            self.Tree_tree_id = str(self.Tree_tree_id)

        if self._is_empty(self.Tree_clone_id):
            self.MissingRequiredField("Tree_clone_id")
        if not isinstance(self.Tree_clone_id, str):
            self.Tree_clone_id = str(self.Tree_clone_id)

        if self._is_empty(self.Tree_newick):
            self.MissingRequiredField("Tree_newick")
        if not isinstance(self.Tree_newick, str):
            self.Tree_newick = str(self.Tree_newick)

        if self.Tree_nodes is not None and not isinstance(self.Tree_nodes, str):
            self.Tree_nodes = str(self.Tree_nodes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Node(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Node"]
    class_class_curie: ClassVar[str] = "ak_schema:Node"
    class_name: ClassVar[str] = "Node"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Node

    Node_sequence_id: str = None
    Node_sequence_alignment: Optional[str] = None
    Node_junction: Optional[str] = None
    Node_junction_aa: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Node_sequence_id):
            self.MissingRequiredField("Node_sequence_id")
        if not isinstance(self.Node_sequence_id, str):
            self.Node_sequence_id = str(self.Node_sequence_id)

        if self.Node_sequence_alignment is not None and not isinstance(self.Node_sequence_alignment, str):
            self.Node_sequence_alignment = str(self.Node_sequence_alignment)

        if self.Node_junction is not None and not isinstance(self.Node_junction, str):
            self.Node_junction = str(self.Node_junction)

        if self.Node_junction_aa is not None and not isinstance(self.Node_junction_aa, str):
            self.Node_junction_aa = str(self.Node_junction_aa)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["CellExpression"]
    class_class_curie: ClassVar[str] = "ak_schema:CellExpression"
    class_name: ClassVar[str] = "CellExpression"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.CellExpression

    CellExpression_expression_id: str = None
    CellExpression_cell_id: str = None
    CellExpression_repertoire_id: str = None
    CellExpression_data_processing_id: str = None
    CellExpression_property_type: str = None
    CellExpression_property: Union[str, "Property"] = None
    CellExpression_value: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.CellExpression_expression_id):
            self.MissingRequiredField("CellExpression_expression_id")
        if not isinstance(self.CellExpression_expression_id, str):
            self.CellExpression_expression_id = str(self.CellExpression_expression_id)

        if self._is_empty(self.CellExpression_cell_id):
            self.MissingRequiredField("CellExpression_cell_id")
        if not isinstance(self.CellExpression_cell_id, str):
            self.CellExpression_cell_id = str(self.CellExpression_cell_id)

        if self._is_empty(self.CellExpression_repertoire_id):
            self.MissingRequiredField("CellExpression_repertoire_id")
        if not isinstance(self.CellExpression_repertoire_id, str):
            self.CellExpression_repertoire_id = str(self.CellExpression_repertoire_id)

        if self._is_empty(self.CellExpression_data_processing_id):
            self.MissingRequiredField("CellExpression_data_processing_id")
        if not isinstance(self.CellExpression_data_processing_id, str):
            self.CellExpression_data_processing_id = str(self.CellExpression_data_processing_id)

        if self._is_empty(self.CellExpression_property_type):
            self.MissingRequiredField("CellExpression_property_type")
        if not isinstance(self.CellExpression_property_type, str):
            self.CellExpression_property_type = str(self.CellExpression_property_type)

        if self._is_empty(self.CellExpression_value):
            self.MissingRequiredField("CellExpression_value")
        if not isinstance(self.CellExpression_value, float):
            self.CellExpression_value = float(self.CellExpression_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Receptor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["Receptor"]
    class_class_curie: ClassVar[str] = "ak_schema:Receptor"
    class_name: ClassVar[str] = "Receptor"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.Receptor

    Receptor_receptor_id: str = None
    Receptor_receptor_hash: str = None
    Receptor_receptor_type: Union[str, "ReceptorType"] = None
    Receptor_receptor_variable_domain_1_aa: str = None
    Receptor_receptor_variable_domain_1_locus: Union[str, "ReceptorVariableDomain1Locus"] = None
    Receptor_receptor_variable_domain_2_aa: str = None
    Receptor_receptor_variable_domain_2_locus: Union[str, "ReceptorVariableDomain2Locus"] = None
    Receptor_receptor_ref: Optional[Union[str, List[str]]] = empty_list()
    Receptor_reactivity_measurements: Optional[Union[Union[dict, "ReceptorReactivity"], List[Union[dict, "ReceptorReactivity"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Receptor_receptor_id):
            self.MissingRequiredField("Receptor_receptor_id")
        if not isinstance(self.Receptor_receptor_id, str):
            self.Receptor_receptor_id = str(self.Receptor_receptor_id)

        if self._is_empty(self.Receptor_receptor_hash):
            self.MissingRequiredField("Receptor_receptor_hash")
        if not isinstance(self.Receptor_receptor_hash, str):
            self.Receptor_receptor_hash = str(self.Receptor_receptor_hash)

        if self._is_empty(self.Receptor_receptor_type):
            self.MissingRequiredField("Receptor_receptor_type")
        if not isinstance(self.Receptor_receptor_type, ReceptorType):
            self.Receptor_receptor_type = ReceptorType(self.Receptor_receptor_type)

        if self._is_empty(self.Receptor_receptor_variable_domain_1_aa):
            self.MissingRequiredField("Receptor_receptor_variable_domain_1_aa")
        if not isinstance(self.Receptor_receptor_variable_domain_1_aa, str):
            self.Receptor_receptor_variable_domain_1_aa = str(self.Receptor_receptor_variable_domain_1_aa)

        if self._is_empty(self.Receptor_receptor_variable_domain_1_locus):
            self.MissingRequiredField("Receptor_receptor_variable_domain_1_locus")
        if not isinstance(self.Receptor_receptor_variable_domain_1_locus, ReceptorVariableDomain1Locus):
            self.Receptor_receptor_variable_domain_1_locus = ReceptorVariableDomain1Locus(self.Receptor_receptor_variable_domain_1_locus)

        if self._is_empty(self.Receptor_receptor_variable_domain_2_aa):
            self.MissingRequiredField("Receptor_receptor_variable_domain_2_aa")
        if not isinstance(self.Receptor_receptor_variable_domain_2_aa, str):
            self.Receptor_receptor_variable_domain_2_aa = str(self.Receptor_receptor_variable_domain_2_aa)

        if self._is_empty(self.Receptor_receptor_variable_domain_2_locus):
            self.MissingRequiredField("Receptor_receptor_variable_domain_2_locus")
        if not isinstance(self.Receptor_receptor_variable_domain_2_locus, ReceptorVariableDomain2Locus):
            self.Receptor_receptor_variable_domain_2_locus = ReceptorVariableDomain2Locus(self.Receptor_receptor_variable_domain_2_locus)

        if not isinstance(self.Receptor_receptor_ref, list):
            self.Receptor_receptor_ref = [self.Receptor_receptor_ref] if self.Receptor_receptor_ref is not None else []
        self.Receptor_receptor_ref = [v if isinstance(v, str) else str(v) for v in self.Receptor_receptor_ref]

        self._normalize_inlined_as_dict(slot_name="Receptor_reactivity_measurements", slot_type=ReceptorReactivity, key_name="ReceptorReactivity_ligand_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReceptorReactivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["ReceptorReactivity"]
    class_class_curie: ClassVar[str] = "ak_schema:ReceptorReactivity"
    class_name: ClassVar[str] = "ReceptorReactivity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.ReceptorReactivity

    ReceptorReactivity_ligand_type: Union[str, "LigandType"] = None
    ReceptorReactivity_antigen_type: Union[str, "AntigenType"] = None
    ReceptorReactivity_antigen: Union[str, "Antigen"] = None
    ReceptorReactivity_reactivity_method: Union[str, "ReactivityMethod"] = None
    ReceptorReactivity_reactivity_readout: Union[str, "ReactivityReadout"] = None
    ReceptorReactivity_reactivity_value: float = None
    ReceptorReactivity_reactivity_unit: str = None
    ReceptorReactivity_antigen_source_species: Optional[Union[str, "AntigenSourceSpecies"]] = None
    ReceptorReactivity_peptide_start: Optional[int] = None
    ReceptorReactivity_peptide_end: Optional[int] = None
    ReceptorReactivity_mhc_class: Optional[Union[str, "MhcClass"]] = None
    ReceptorReactivity_mhc_gene_1: Optional[Union[str, "MhcGene1"]] = None
    ReceptorReactivity_mhc_allele_1: Optional[str] = None
    ReceptorReactivity_mhc_gene_2: Optional[Union[str, "MhcGene2"]] = None
    ReceptorReactivity_mhc_allele_2: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ReceptorReactivity_ligand_type):
            self.MissingRequiredField("ReceptorReactivity_ligand_type")
        if not isinstance(self.ReceptorReactivity_ligand_type, LigandType):
            self.ReceptorReactivity_ligand_type = LigandType(self.ReceptorReactivity_ligand_type)

        if self._is_empty(self.ReceptorReactivity_antigen_type):
            self.MissingRequiredField("ReceptorReactivity_antigen_type")
        if not isinstance(self.ReceptorReactivity_antigen_type, AntigenType):
            self.ReceptorReactivity_antigen_type = AntigenType(self.ReceptorReactivity_antigen_type)

        if self._is_empty(self.ReceptorReactivity_reactivity_method):
            self.MissingRequiredField("ReceptorReactivity_reactivity_method")
        if not isinstance(self.ReceptorReactivity_reactivity_method, ReactivityMethod):
            self.ReceptorReactivity_reactivity_method = ReactivityMethod(self.ReceptorReactivity_reactivity_method)

        if self._is_empty(self.ReceptorReactivity_reactivity_readout):
            self.MissingRequiredField("ReceptorReactivity_reactivity_readout")
        if not isinstance(self.ReceptorReactivity_reactivity_readout, ReactivityReadout):
            self.ReceptorReactivity_reactivity_readout = ReactivityReadout(self.ReceptorReactivity_reactivity_readout)

        if self._is_empty(self.ReceptorReactivity_reactivity_value):
            self.MissingRequiredField("ReceptorReactivity_reactivity_value")
        if not isinstance(self.ReceptorReactivity_reactivity_value, float):
            self.ReceptorReactivity_reactivity_value = float(self.ReceptorReactivity_reactivity_value)

        if self._is_empty(self.ReceptorReactivity_reactivity_unit):
            self.MissingRequiredField("ReceptorReactivity_reactivity_unit")
        if not isinstance(self.ReceptorReactivity_reactivity_unit, str):
            self.ReceptorReactivity_reactivity_unit = str(self.ReceptorReactivity_reactivity_unit)

        if self.ReceptorReactivity_peptide_start is not None and not isinstance(self.ReceptorReactivity_peptide_start, int):
            self.ReceptorReactivity_peptide_start = int(self.ReceptorReactivity_peptide_start)

        if self.ReceptorReactivity_peptide_end is not None and not isinstance(self.ReceptorReactivity_peptide_end, int):
            self.ReceptorReactivity_peptide_end = int(self.ReceptorReactivity_peptide_end)

        if self.ReceptorReactivity_mhc_class is not None and not isinstance(self.ReceptorReactivity_mhc_class, MhcClass):
            self.ReceptorReactivity_mhc_class = MhcClass(self.ReceptorReactivity_mhc_class)

        if self.ReceptorReactivity_mhc_allele_1 is not None and not isinstance(self.ReceptorReactivity_mhc_allele_1, str):
            self.ReceptorReactivity_mhc_allele_1 = str(self.ReceptorReactivity_mhc_allele_1)

        if self.ReceptorReactivity_mhc_allele_2 is not None and not isinstance(self.ReceptorReactivity_mhc_allele_2, str):
            self.ReceptorReactivity_mhc_allele_2 = str(self.ReceptorReactivity_mhc_allele_2)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SampleProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["SampleProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:SampleProcessing"
    class_name: ClassVar[str] = "SampleProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.SampleProcessing

    Sample_sample_id: str = None
    Sample_sample_type: str = None
    Sample_tissue: Union[str, TissueAkcId] = None
    Sample_anatomic_site: str = None
    Sample_disease_state_sample: str = None
    Sample_collection_time_point_relative: float = None
    Sample_collection_time_point_relative_unit: Union[str, "CollectionTimePointRelativeUnit"] = None
    Sample_collection_time_point_reference: str = None
    Sample_biomaterial_provider: str = None
    CellProcessing_tissue_processing: str = None
    CellProcessing_cell_subset: Union[str, "CellSubset"] = None
    CellProcessing_cell_phenotype: str = None
    CellProcessing_single_cell: Union[bool, Bool] = None
    CellProcessing_cell_number: int = None
    CellProcessing_cells_per_reaction: int = None
    CellProcessing_cell_storage: Union[bool, Bool] = None
    CellProcessing_cell_quality: str = None
    CellProcessing_cell_isolation: str = None
    CellProcessing_cell_processing_protocol: str = None
    NucleicAcidProcessing_template_class: Union[str, "TemplateClass"] = None
    NucleicAcidProcessing_template_quality: str = None
    NucleicAcidProcessing_template_amount: float = None
    NucleicAcidProcessing_template_amount_unit: Union[str, "TemplateAmountUnit"] = None
    NucleicAcidProcessing_library_generation_method: Union[str, "LibraryGenerationMethod"] = None
    NucleicAcidProcessing_library_generation_protocol: str = None
    NucleicAcidProcessing_library_generation_kit_version: str = None
    NucleicAcidProcessing_complete_sequences: Union[str, "CompleteSequences"] = None
    NucleicAcidProcessing_physical_linkage: Union[str, "PhysicalLinkage"] = None
    SequencingRun_sequencing_run_id: str = None
    SequencingRun_total_reads_passing_qc_filter: int = None
    SequencingRun_sequencing_platform: str = None
    SequencingRun_sequencing_facility: str = None
    SequencingRun_sequencing_run_date: str = None
    SequencingRun_sequencing_kit: str = None
    SampleProcessing_sample_processing_id: Optional[str] = None
    CellProcessing_cell_species: Optional[Union[str, "CellSpecies"]] = None
    NucleicAcidProcessing_pcr_target: Optional[Union[Union[dict, PCRTarget], List[Union[dict, PCRTarget]]]] = empty_list()
    SequencingRun_sequencing_files: Optional[Union[dict, SequencingData]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Sample_sample_id):
            self.MissingRequiredField("Sample_sample_id")
        if not isinstance(self.Sample_sample_id, str):
            self.Sample_sample_id = str(self.Sample_sample_id)

        if self._is_empty(self.Sample_sample_type):
            self.MissingRequiredField("Sample_sample_type")
        if not isinstance(self.Sample_sample_type, str):
            self.Sample_sample_type = str(self.Sample_sample_type)

        if self._is_empty(self.Sample_tissue):
            self.MissingRequiredField("Sample_tissue")
        if not isinstance(self.Sample_tissue, TissueAkcId):
            self.Sample_tissue = TissueAkcId(self.Sample_tissue)

        if self._is_empty(self.Sample_anatomic_site):
            self.MissingRequiredField("Sample_anatomic_site")
        if not isinstance(self.Sample_anatomic_site, str):
            self.Sample_anatomic_site = str(self.Sample_anatomic_site)

        if self._is_empty(self.Sample_disease_state_sample):
            self.MissingRequiredField("Sample_disease_state_sample")
        if not isinstance(self.Sample_disease_state_sample, str):
            self.Sample_disease_state_sample = str(self.Sample_disease_state_sample)

        if self._is_empty(self.Sample_collection_time_point_relative):
            self.MissingRequiredField("Sample_collection_time_point_relative")
        if not isinstance(self.Sample_collection_time_point_relative, float):
            self.Sample_collection_time_point_relative = float(self.Sample_collection_time_point_relative)

        if self._is_empty(self.Sample_collection_time_point_reference):
            self.MissingRequiredField("Sample_collection_time_point_reference")
        if not isinstance(self.Sample_collection_time_point_reference, str):
            self.Sample_collection_time_point_reference = str(self.Sample_collection_time_point_reference)

        if self._is_empty(self.Sample_biomaterial_provider):
            self.MissingRequiredField("Sample_biomaterial_provider")
        if not isinstance(self.Sample_biomaterial_provider, str):
            self.Sample_biomaterial_provider = str(self.Sample_biomaterial_provider)

        if self._is_empty(self.CellProcessing_tissue_processing):
            self.MissingRequiredField("CellProcessing_tissue_processing")
        if not isinstance(self.CellProcessing_tissue_processing, str):
            self.CellProcessing_tissue_processing = str(self.CellProcessing_tissue_processing)

        if self._is_empty(self.CellProcessing_cell_phenotype):
            self.MissingRequiredField("CellProcessing_cell_phenotype")
        if not isinstance(self.CellProcessing_cell_phenotype, str):
            self.CellProcessing_cell_phenotype = str(self.CellProcessing_cell_phenotype)

        if self._is_empty(self.CellProcessing_single_cell):
            self.MissingRequiredField("CellProcessing_single_cell")
        if not isinstance(self.CellProcessing_single_cell, Bool):
            self.CellProcessing_single_cell = Bool(self.CellProcessing_single_cell)

        if self._is_empty(self.CellProcessing_cell_number):
            self.MissingRequiredField("CellProcessing_cell_number")
        if not isinstance(self.CellProcessing_cell_number, int):
            self.CellProcessing_cell_number = int(self.CellProcessing_cell_number)

        if self._is_empty(self.CellProcessing_cells_per_reaction):
            self.MissingRequiredField("CellProcessing_cells_per_reaction")
        if not isinstance(self.CellProcessing_cells_per_reaction, int):
            self.CellProcessing_cells_per_reaction = int(self.CellProcessing_cells_per_reaction)

        if self._is_empty(self.CellProcessing_cell_storage):
            self.MissingRequiredField("CellProcessing_cell_storage")
        if not isinstance(self.CellProcessing_cell_storage, Bool):
            self.CellProcessing_cell_storage = Bool(self.CellProcessing_cell_storage)

        if self._is_empty(self.CellProcessing_cell_quality):
            self.MissingRequiredField("CellProcessing_cell_quality")
        if not isinstance(self.CellProcessing_cell_quality, str):
            self.CellProcessing_cell_quality = str(self.CellProcessing_cell_quality)

        if self._is_empty(self.CellProcessing_cell_isolation):
            self.MissingRequiredField("CellProcessing_cell_isolation")
        if not isinstance(self.CellProcessing_cell_isolation, str):
            self.CellProcessing_cell_isolation = str(self.CellProcessing_cell_isolation)

        if self._is_empty(self.CellProcessing_cell_processing_protocol):
            self.MissingRequiredField("CellProcessing_cell_processing_protocol")
        if not isinstance(self.CellProcessing_cell_processing_protocol, str):
            self.CellProcessing_cell_processing_protocol = str(self.CellProcessing_cell_processing_protocol)

        if self._is_empty(self.NucleicAcidProcessing_template_class):
            self.MissingRequiredField("NucleicAcidProcessing_template_class")
        if not isinstance(self.NucleicAcidProcessing_template_class, TemplateClass):
            self.NucleicAcidProcessing_template_class = TemplateClass(self.NucleicAcidProcessing_template_class)

        if self._is_empty(self.NucleicAcidProcessing_template_quality):
            self.MissingRequiredField("NucleicAcidProcessing_template_quality")
        if not isinstance(self.NucleicAcidProcessing_template_quality, str):
            self.NucleicAcidProcessing_template_quality = str(self.NucleicAcidProcessing_template_quality)

        if self._is_empty(self.NucleicAcidProcessing_template_amount):
            self.MissingRequiredField("NucleicAcidProcessing_template_amount")
        if not isinstance(self.NucleicAcidProcessing_template_amount, float):
            self.NucleicAcidProcessing_template_amount = float(self.NucleicAcidProcessing_template_amount)

        if self._is_empty(self.NucleicAcidProcessing_library_generation_method):
            self.MissingRequiredField("NucleicAcidProcessing_library_generation_method")
        if not isinstance(self.NucleicAcidProcessing_library_generation_method, LibraryGenerationMethod):
            self.NucleicAcidProcessing_library_generation_method = LibraryGenerationMethod(self.NucleicAcidProcessing_library_generation_method)

        if self._is_empty(self.NucleicAcidProcessing_library_generation_protocol):
            self.MissingRequiredField("NucleicAcidProcessing_library_generation_protocol")
        if not isinstance(self.NucleicAcidProcessing_library_generation_protocol, str):
            self.NucleicAcidProcessing_library_generation_protocol = str(self.NucleicAcidProcessing_library_generation_protocol)

        if self._is_empty(self.NucleicAcidProcessing_library_generation_kit_version):
            self.MissingRequiredField("NucleicAcidProcessing_library_generation_kit_version")
        if not isinstance(self.NucleicAcidProcessing_library_generation_kit_version, str):
            self.NucleicAcidProcessing_library_generation_kit_version = str(self.NucleicAcidProcessing_library_generation_kit_version)

        if self._is_empty(self.NucleicAcidProcessing_complete_sequences):
            self.MissingRequiredField("NucleicAcidProcessing_complete_sequences")
        if not isinstance(self.NucleicAcidProcessing_complete_sequences, CompleteSequences):
            self.NucleicAcidProcessing_complete_sequences = CompleteSequences(self.NucleicAcidProcessing_complete_sequences)

        if self._is_empty(self.NucleicAcidProcessing_physical_linkage):
            self.MissingRequiredField("NucleicAcidProcessing_physical_linkage")
        if not isinstance(self.NucleicAcidProcessing_physical_linkage, PhysicalLinkage):
            self.NucleicAcidProcessing_physical_linkage = PhysicalLinkage(self.NucleicAcidProcessing_physical_linkage)

        if self._is_empty(self.SequencingRun_sequencing_run_id):
            self.MissingRequiredField("SequencingRun_sequencing_run_id")
        if not isinstance(self.SequencingRun_sequencing_run_id, str):
            self.SequencingRun_sequencing_run_id = str(self.SequencingRun_sequencing_run_id)

        if self._is_empty(self.SequencingRun_total_reads_passing_qc_filter):
            self.MissingRequiredField("SequencingRun_total_reads_passing_qc_filter")
        if not isinstance(self.SequencingRun_total_reads_passing_qc_filter, int):
            self.SequencingRun_total_reads_passing_qc_filter = int(self.SequencingRun_total_reads_passing_qc_filter)

        if self._is_empty(self.SequencingRun_sequencing_platform):
            self.MissingRequiredField("SequencingRun_sequencing_platform")
        if not isinstance(self.SequencingRun_sequencing_platform, str):
            self.SequencingRun_sequencing_platform = str(self.SequencingRun_sequencing_platform)

        if self._is_empty(self.SequencingRun_sequencing_facility):
            self.MissingRequiredField("SequencingRun_sequencing_facility")
        if not isinstance(self.SequencingRun_sequencing_facility, str):
            self.SequencingRun_sequencing_facility = str(self.SequencingRun_sequencing_facility)

        if self._is_empty(self.SequencingRun_sequencing_run_date):
            self.MissingRequiredField("SequencingRun_sequencing_run_date")
        if not isinstance(self.SequencingRun_sequencing_run_date, str):
            self.SequencingRun_sequencing_run_date = str(self.SequencingRun_sequencing_run_date)

        if self._is_empty(self.SequencingRun_sequencing_kit):
            self.MissingRequiredField("SequencingRun_sequencing_kit")
        if not isinstance(self.SequencingRun_sequencing_kit, str):
            self.SequencingRun_sequencing_kit = str(self.SequencingRun_sequencing_kit)

        if self.SampleProcessing_sample_processing_id is not None and not isinstance(self.SampleProcessing_sample_processing_id, str):
            self.SampleProcessing_sample_processing_id = str(self.SampleProcessing_sample_processing_id)

        self._normalize_inlined_as_dict(slot_name="NucleicAcidProcessing_pcr_target", slot_type=PCRTarget, key_name="PCRTarget_pcr_target_locus", keyed=False)

        if self.SequencingRun_sequencing_files is not None and not isinstance(self.SequencingRun_sequencing_files, SequencingData):
            self.SequencingRun_sequencing_files = SequencingData(**as_dict(self.SequencingRun_sequencing_files))

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

class Unit(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="Unit",
    )

class Derivation(EnumDefinitionImpl):

    DNA = PermissibleValue(text="DNA")
    RNA = PermissibleValue(text="RNA")
    null = PermissibleValue(text="null")

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

    null = PermissibleValue(text="null")

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
    TRD = PermissibleValue(text="TRD")
    TRG = PermissibleValue(text="TRG")
    null = PermissibleValue(text="null")

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
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="InferenceType",
    )

class SpeciesSubgroupType(EnumDefinitionImpl):

    breed = PermissibleValue(text="breed")
    strain = PermissibleValue(text="strain")
    inbred = PermissibleValue(text="inbred")
    outbred = PermissibleValue(text="outbred")
    locational = PermissibleValue(text="locational")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="SpeciesSubgroupType",
    )

class Status(EnumDefinitionImpl):

    active = PermissibleValue(text="active")
    draft = PermissibleValue(text="draft")
    retired = PermissibleValue(text="retired")
    withdrawn = PermissibleValue(text="withdrawn")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="Status",
    )

class JCodonFrame(EnumDefinitionImpl):

    null = PermissibleValue(text="null")

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
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="InferenceProcess",
    )

class MhcClass(EnumDefinitionImpl):

    null = PermissibleValue(text="null")

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
    null = PermissibleValue(text="null")

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
    null = PermissibleValue(text="null")

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
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="FileType",
    )

class ReadDirection(EnumDefinitionImpl):

    forward = PermissibleValue(text="forward")
    reverse = PermissibleValue(text="reverse")
    mixed = PermissibleValue(text="mixed")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="ReadDirection",
    )

class PairedReadDirection(EnumDefinitionImpl):

    forward = PermissibleValue(text="forward")
    reverse = PermissibleValue(text="reverse")
    mixed = PermissibleValue(text="mixed")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="PairedReadDirection",
    )

class ExpressionStudyMethod(EnumDefinitionImpl):

    flow_cytometry = PermissibleValue(text="flow_cytometry")
    null = PermissibleValue(text="null")

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

slots.specimen_processing = Slot(uri=BFO['0000051'], name="specimen_processing", curie=BFO.curie('0000051'),
                   model_uri=AK_SCHEMA.specimen_processing, domain=None, range=Optional[Union[Union[str, SpecimenProcessingAkcId], List[Union[str, SpecimenProcessingAkcId]]]])

slots.assay_type = Slot(uri=RDF.type, name="assay_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.assay_type, domain=None, range=Optional[str])

slots.target_entity_type = Slot(uri=AK_SCHEMA.target_entity_type, name="target_entity_type", curie=AK_SCHEMA.curie('target_entity_type'),
                   model_uri=AK_SCHEMA.target_entity_type, domain=None, range=Optional[str])

slots.template_class = Slot(uri=AK_SCHEMA.template_class, name="template_class", curie=AK_SCHEMA.curie('template_class'),
                   model_uri=AK_SCHEMA.template_class, domain=None, range=Optional[str])

slots.template_quality = Slot(uri=AK_SCHEMA.template_quality, name="template_quality", curie=AK_SCHEMA.curie('template_quality'),
                   model_uri=AK_SCHEMA.template_quality, domain=None, range=Optional[str])

slots.template_amount = Slot(uri=AK_SCHEMA.template_amount, name="template_amount", curie=AK_SCHEMA.curie('template_amount'),
                   model_uri=AK_SCHEMA.template_amount, domain=None, range=Optional[str])

slots.template_amount_unit = Slot(uri=AK_SCHEMA.template_amount_unit, name="template_amount_unit", curie=AK_SCHEMA.curie('template_amount_unit'),
                   model_uri=AK_SCHEMA.template_amount_unit, domain=None, range=Optional[str])

slots.library_generation_method = Slot(uri=AK_SCHEMA.library_generation_method, name="library_generation_method", curie=AK_SCHEMA.curie('library_generation_method'),
                   model_uri=AK_SCHEMA.library_generation_method, domain=None, range=Optional[str])

slots.library_generation_protocol = Slot(uri=AK_SCHEMA.library_generation_protocol, name="library_generation_protocol", curie=AK_SCHEMA.curie('library_generation_protocol'),
                   model_uri=AK_SCHEMA.library_generation_protocol, domain=None, range=Optional[str])

slots.library_generation_kit_version = Slot(uri=AK_SCHEMA.library_generation_kit_version, name="library_generation_kit_version", curie=AK_SCHEMA.curie('library_generation_kit_version'),
                   model_uri=AK_SCHEMA.library_generation_kit_version, domain=None, range=Optional[str])

slots.pcr_target = Slot(uri=AK_SCHEMA.pcr_target, name="pcr_target", curie=AK_SCHEMA.curie('pcr_target'),
                   model_uri=AK_SCHEMA.pcr_target, domain=None, range=Optional[Union[str, List[str]]])

slots.complete_sequences = Slot(uri=AK_SCHEMA.complete_sequences, name="complete_sequences", curie=AK_SCHEMA.curie('complete_sequences'),
                   model_uri=AK_SCHEMA.complete_sequences, domain=None, range=Optional[str])

slots.physical_linkage = Slot(uri=AK_SCHEMA.physical_linkage, name="physical_linkage", curie=AK_SCHEMA.curie('physical_linkage'),
                   model_uri=AK_SCHEMA.physical_linkage, domain=None, range=Optional[str])

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

slots.TimePoint_label = Slot(uri=AK_SCHEMA.TimePoint_label, name="TimePoint_label", curie=AK_SCHEMA.curie('TimePoint_label'),
                   model_uri=AK_SCHEMA.TimePoint_label, domain=None, range=Optional[str])

slots.TimePoint_value = Slot(uri=AK_SCHEMA.TimePoint_value, name="TimePoint_value", curie=AK_SCHEMA.curie('TimePoint_value'),
                   model_uri=AK_SCHEMA.TimePoint_value, domain=None, range=Optional[float])

slots.TimePoint_unit = Slot(uri=AK_SCHEMA.TimePoint_unit, name="TimePoint_unit", curie=AK_SCHEMA.curie('TimePoint_unit'),
                   model_uri=AK_SCHEMA.TimePoint_unit, domain=None, range=Optional[Union[str, "Unit"]])

slots.Acknowledgement_acknowledgement_id = Slot(uri=AK_SCHEMA.Acknowledgement_acknowledgement_id, name="Acknowledgement_acknowledgement_id", curie=AK_SCHEMA.curie('Acknowledgement_acknowledgement_id'),
                   model_uri=AK_SCHEMA.Acknowledgement_acknowledgement_id, domain=None, range=str)

slots.Acknowledgement_name = Slot(uri=AK_SCHEMA.Acknowledgement_name, name="Acknowledgement_name", curie=AK_SCHEMA.curie('Acknowledgement_name'),
                   model_uri=AK_SCHEMA.Acknowledgement_name, domain=None, range=str)

slots.Acknowledgement_institution_name = Slot(uri=AK_SCHEMA.Acknowledgement_institution_name, name="Acknowledgement_institution_name", curie=AK_SCHEMA.curie('Acknowledgement_institution_name'),
                   model_uri=AK_SCHEMA.Acknowledgement_institution_name, domain=None, range=str)

slots.Acknowledgement_orcid_id = Slot(uri=AK_SCHEMA.Acknowledgement_orcid_id, name="Acknowledgement_orcid_id", curie=AK_SCHEMA.curie('Acknowledgement_orcid_id'),
                   model_uri=AK_SCHEMA.Acknowledgement_orcid_id, domain=None, range=Optional[str])

slots.RearrangedSequence_sequence_id = Slot(uri=AK_SCHEMA.RearrangedSequence_sequence_id, name="RearrangedSequence_sequence_id", curie=AK_SCHEMA.curie('RearrangedSequence_sequence_id'),
                   model_uri=AK_SCHEMA.RearrangedSequence_sequence_id, domain=None, range=str)

slots.RearrangedSequence_sequence = Slot(uri=AK_SCHEMA.RearrangedSequence_sequence, name="RearrangedSequence_sequence", curie=AK_SCHEMA.curie('RearrangedSequence_sequence'),
                   model_uri=AK_SCHEMA.RearrangedSequence_sequence, domain=None, range=str)

slots.RearrangedSequence_derivation = Slot(uri=AK_SCHEMA.RearrangedSequence_derivation, name="RearrangedSequence_derivation", curie=AK_SCHEMA.curie('RearrangedSequence_derivation'),
                   model_uri=AK_SCHEMA.RearrangedSequence_derivation, domain=None, range=Union[str, "Derivation"])

slots.RearrangedSequence_observation_type = Slot(uri=AK_SCHEMA.RearrangedSequence_observation_type, name="RearrangedSequence_observation_type", curie=AK_SCHEMA.curie('RearrangedSequence_observation_type'),
                   model_uri=AK_SCHEMA.RearrangedSequence_observation_type, domain=None, range=Union[str, "ObservationType"])

slots.RearrangedSequence_curation = Slot(uri=AK_SCHEMA.RearrangedSequence_curation, name="RearrangedSequence_curation", curie=AK_SCHEMA.curie('RearrangedSequence_curation'),
                   model_uri=AK_SCHEMA.RearrangedSequence_curation, domain=None, range=Optional[str])

slots.RearrangedSequence_repository_name = Slot(uri=AK_SCHEMA.RearrangedSequence_repository_name, name="RearrangedSequence_repository_name", curie=AK_SCHEMA.curie('RearrangedSequence_repository_name'),
                   model_uri=AK_SCHEMA.RearrangedSequence_repository_name, domain=None, range=str)

slots.RearrangedSequence_repository_ref = Slot(uri=AK_SCHEMA.RearrangedSequence_repository_ref, name="RearrangedSequence_repository_ref", curie=AK_SCHEMA.curie('RearrangedSequence_repository_ref'),
                   model_uri=AK_SCHEMA.RearrangedSequence_repository_ref, domain=None, range=Optional[str])

slots.RearrangedSequence_deposited_version = Slot(uri=AK_SCHEMA.RearrangedSequence_deposited_version, name="RearrangedSequence_deposited_version", curie=AK_SCHEMA.curie('RearrangedSequence_deposited_version'),
                   model_uri=AK_SCHEMA.RearrangedSequence_deposited_version, domain=None, range=str)

slots.RearrangedSequence_sequence_start = Slot(uri=AK_SCHEMA.RearrangedSequence_sequence_start, name="RearrangedSequence_sequence_start", curie=AK_SCHEMA.curie('RearrangedSequence_sequence_start'),
                   model_uri=AK_SCHEMA.RearrangedSequence_sequence_start, domain=None, range=Optional[int])

slots.RearrangedSequence_sequence_end = Slot(uri=AK_SCHEMA.RearrangedSequence_sequence_end, name="RearrangedSequence_sequence_end", curie=AK_SCHEMA.curie('RearrangedSequence_sequence_end'),
                   model_uri=AK_SCHEMA.RearrangedSequence_sequence_end, domain=None, range=Optional[int])

slots.UnrearrangedSequence_sequence_id = Slot(uri=AK_SCHEMA.UnrearrangedSequence_sequence_id, name="UnrearrangedSequence_sequence_id", curie=AK_SCHEMA.curie('UnrearrangedSequence_sequence_id'),
                   model_uri=AK_SCHEMA.UnrearrangedSequence_sequence_id, domain=None, range=str)

slots.UnrearrangedSequence_sequence = Slot(uri=AK_SCHEMA.UnrearrangedSequence_sequence, name="UnrearrangedSequence_sequence", curie=AK_SCHEMA.curie('UnrearrangedSequence_sequence'),
                   model_uri=AK_SCHEMA.UnrearrangedSequence_sequence, domain=None, range=str)

slots.UnrearrangedSequence_curation = Slot(uri=AK_SCHEMA.UnrearrangedSequence_curation, name="UnrearrangedSequence_curation", curie=AK_SCHEMA.curie('UnrearrangedSequence_curation'),
                   model_uri=AK_SCHEMA.UnrearrangedSequence_curation, domain=None, range=Optional[str])

slots.UnrearrangedSequence_repository_name = Slot(uri=AK_SCHEMA.UnrearrangedSequence_repository_name, name="UnrearrangedSequence_repository_name", curie=AK_SCHEMA.curie('UnrearrangedSequence_repository_name'),
                   model_uri=AK_SCHEMA.UnrearrangedSequence_repository_name, domain=None, range=str)

slots.UnrearrangedSequence_repository_ref = Slot(uri=AK_SCHEMA.UnrearrangedSequence_repository_ref, name="UnrearrangedSequence_repository_ref", curie=AK_SCHEMA.curie('UnrearrangedSequence_repository_ref'),
                   model_uri=AK_SCHEMA.UnrearrangedSequence_repository_ref, domain=None, range=Optional[str])

slots.UnrearrangedSequence_patch_no = Slot(uri=AK_SCHEMA.UnrearrangedSequence_patch_no, name="UnrearrangedSequence_patch_no", curie=AK_SCHEMA.curie('UnrearrangedSequence_patch_no'),
                   model_uri=AK_SCHEMA.UnrearrangedSequence_patch_no, domain=None, range=Optional[str])

slots.UnrearrangedSequence_gff_seqid = Slot(uri=AK_SCHEMA.UnrearrangedSequence_gff_seqid, name="UnrearrangedSequence_gff_seqid", curie=AK_SCHEMA.curie('UnrearrangedSequence_gff_seqid'),
                   model_uri=AK_SCHEMA.UnrearrangedSequence_gff_seqid, domain=None, range=str)

slots.UnrearrangedSequence_gff_start = Slot(uri=AK_SCHEMA.UnrearrangedSequence_gff_start, name="UnrearrangedSequence_gff_start", curie=AK_SCHEMA.curie('UnrearrangedSequence_gff_start'),
                   model_uri=AK_SCHEMA.UnrearrangedSequence_gff_start, domain=None, range=int)

slots.UnrearrangedSequence_gff_end = Slot(uri=AK_SCHEMA.UnrearrangedSequence_gff_end, name="UnrearrangedSequence_gff_end", curie=AK_SCHEMA.curie('UnrearrangedSequence_gff_end'),
                   model_uri=AK_SCHEMA.UnrearrangedSequence_gff_end, domain=None, range=int)

slots.UnrearrangedSequence_strand = Slot(uri=AK_SCHEMA.UnrearrangedSequence_strand, name="UnrearrangedSequence_strand", curie=AK_SCHEMA.curie('UnrearrangedSequence_strand'),
                   model_uri=AK_SCHEMA.UnrearrangedSequence_strand, domain=None, range=Union[str, "Strand"])

slots.SequenceDelineationV_sequence_delineation_id = Slot(uri=AK_SCHEMA.SequenceDelineationV_sequence_delineation_id, name="SequenceDelineationV_sequence_delineation_id", curie=AK_SCHEMA.curie('SequenceDelineationV_sequence_delineation_id'),
                   model_uri=AK_SCHEMA.SequenceDelineationV_sequence_delineation_id, domain=None, range=str)

slots.SequenceDelineationV_delineation_scheme = Slot(uri=AK_SCHEMA.SequenceDelineationV_delineation_scheme, name="SequenceDelineationV_delineation_scheme", curie=AK_SCHEMA.curie('SequenceDelineationV_delineation_scheme'),
                   model_uri=AK_SCHEMA.SequenceDelineationV_delineation_scheme, domain=None, range=str)

slots.SequenceDelineationV_unaligned_sequence = Slot(uri=AK_SCHEMA.SequenceDelineationV_unaligned_sequence, name="SequenceDelineationV_unaligned_sequence", curie=AK_SCHEMA.curie('SequenceDelineationV_unaligned_sequence'),
                   model_uri=AK_SCHEMA.SequenceDelineationV_unaligned_sequence, domain=None, range=Optional[str])

slots.SequenceDelineationV_aligned_sequence = Slot(uri=AK_SCHEMA.SequenceDelineationV_aligned_sequence, name="SequenceDelineationV_aligned_sequence", curie=AK_SCHEMA.curie('SequenceDelineationV_aligned_sequence'),
                   model_uri=AK_SCHEMA.SequenceDelineationV_aligned_sequence, domain=None, range=Optional[str])

slots.SequenceDelineationV_fwr1_start = Slot(uri=AK_SCHEMA.SequenceDelineationV_fwr1_start, name="SequenceDelineationV_fwr1_start", curie=AK_SCHEMA.curie('SequenceDelineationV_fwr1_start'),
                   model_uri=AK_SCHEMA.SequenceDelineationV_fwr1_start, domain=None, range=int)

slots.SequenceDelineationV_fwr1_end = Slot(uri=AK_SCHEMA.SequenceDelineationV_fwr1_end, name="SequenceDelineationV_fwr1_end", curie=AK_SCHEMA.curie('SequenceDelineationV_fwr1_end'),
                   model_uri=AK_SCHEMA.SequenceDelineationV_fwr1_end, domain=None, range=int)

slots.SequenceDelineationV_cdr1_start = Slot(uri=AK_SCHEMA.SequenceDelineationV_cdr1_start, name="SequenceDelineationV_cdr1_start", curie=AK_SCHEMA.curie('SequenceDelineationV_cdr1_start'),
                   model_uri=AK_SCHEMA.SequenceDelineationV_cdr1_start, domain=None, range=int)

slots.SequenceDelineationV_cdr1_end = Slot(uri=AK_SCHEMA.SequenceDelineationV_cdr1_end, name="SequenceDelineationV_cdr1_end", curie=AK_SCHEMA.curie('SequenceDelineationV_cdr1_end'),
                   model_uri=AK_SCHEMA.SequenceDelineationV_cdr1_end, domain=None, range=int)

slots.SequenceDelineationV_fwr2_start = Slot(uri=AK_SCHEMA.SequenceDelineationV_fwr2_start, name="SequenceDelineationV_fwr2_start", curie=AK_SCHEMA.curie('SequenceDelineationV_fwr2_start'),
                   model_uri=AK_SCHEMA.SequenceDelineationV_fwr2_start, domain=None, range=int)

slots.SequenceDelineationV_fwr2_end = Slot(uri=AK_SCHEMA.SequenceDelineationV_fwr2_end, name="SequenceDelineationV_fwr2_end", curie=AK_SCHEMA.curie('SequenceDelineationV_fwr2_end'),
                   model_uri=AK_SCHEMA.SequenceDelineationV_fwr2_end, domain=None, range=int)

slots.SequenceDelineationV_cdr2_start = Slot(uri=AK_SCHEMA.SequenceDelineationV_cdr2_start, name="SequenceDelineationV_cdr2_start", curie=AK_SCHEMA.curie('SequenceDelineationV_cdr2_start'),
                   model_uri=AK_SCHEMA.SequenceDelineationV_cdr2_start, domain=None, range=int)

slots.SequenceDelineationV_cdr2_end = Slot(uri=AK_SCHEMA.SequenceDelineationV_cdr2_end, name="SequenceDelineationV_cdr2_end", curie=AK_SCHEMA.curie('SequenceDelineationV_cdr2_end'),
                   model_uri=AK_SCHEMA.SequenceDelineationV_cdr2_end, domain=None, range=int)

slots.SequenceDelineationV_fwr3_start = Slot(uri=AK_SCHEMA.SequenceDelineationV_fwr3_start, name="SequenceDelineationV_fwr3_start", curie=AK_SCHEMA.curie('SequenceDelineationV_fwr3_start'),
                   model_uri=AK_SCHEMA.SequenceDelineationV_fwr3_start, domain=None, range=int)

slots.SequenceDelineationV_fwr3_end = Slot(uri=AK_SCHEMA.SequenceDelineationV_fwr3_end, name="SequenceDelineationV_fwr3_end", curie=AK_SCHEMA.curie('SequenceDelineationV_fwr3_end'),
                   model_uri=AK_SCHEMA.SequenceDelineationV_fwr3_end, domain=None, range=int)

slots.SequenceDelineationV_cdr3_start = Slot(uri=AK_SCHEMA.SequenceDelineationV_cdr3_start, name="SequenceDelineationV_cdr3_start", curie=AK_SCHEMA.curie('SequenceDelineationV_cdr3_start'),
                   model_uri=AK_SCHEMA.SequenceDelineationV_cdr3_start, domain=None, range=int)

slots.SequenceDelineationV_alignment_labels = Slot(uri=AK_SCHEMA.SequenceDelineationV_alignment_labels, name="SequenceDelineationV_alignment_labels", curie=AK_SCHEMA.curie('SequenceDelineationV_alignment_labels'),
                   model_uri=AK_SCHEMA.SequenceDelineationV_alignment_labels, domain=None, range=Optional[Union[str, List[str]]])

slots.AlleleDescription_allele_description_id = Slot(uri=AK_SCHEMA.AlleleDescription_allele_description_id, name="AlleleDescription_allele_description_id", curie=AK_SCHEMA.curie('AlleleDescription_allele_description_id'),
                   model_uri=AK_SCHEMA.AlleleDescription_allele_description_id, domain=None, range=str)

slots.AlleleDescription_allele_description_ref = Slot(uri=AK_SCHEMA.AlleleDescription_allele_description_ref, name="AlleleDescription_allele_description_ref", curie=AK_SCHEMA.curie('AlleleDescription_allele_description_ref'),
                   model_uri=AK_SCHEMA.AlleleDescription_allele_description_ref, domain=None, range=Optional[str])

slots.AlleleDescription_maintainer = Slot(uri=AK_SCHEMA.AlleleDescription_maintainer, name="AlleleDescription_maintainer", curie=AK_SCHEMA.curie('AlleleDescription_maintainer'),
                   model_uri=AK_SCHEMA.AlleleDescription_maintainer, domain=None, range=str)

slots.AlleleDescription_acknowledgements = Slot(uri=AK_SCHEMA.AlleleDescription_acknowledgements, name="AlleleDescription_acknowledgements", curie=AK_SCHEMA.curie('AlleleDescription_acknowledgements'),
                   model_uri=AK_SCHEMA.AlleleDescription_acknowledgements, domain=None, range=Optional[Union[Union[dict, Acknowledgement], List[Union[dict, Acknowledgement]]]])

slots.AlleleDescription_lab_address = Slot(uri=AK_SCHEMA.AlleleDescription_lab_address, name="AlleleDescription_lab_address", curie=AK_SCHEMA.curie('AlleleDescription_lab_address'),
                   model_uri=AK_SCHEMA.AlleleDescription_lab_address, domain=None, range=str)

slots.AlleleDescription_release_version = Slot(uri=AK_SCHEMA.AlleleDescription_release_version, name="AlleleDescription_release_version", curie=AK_SCHEMA.curie('AlleleDescription_release_version'),
                   model_uri=AK_SCHEMA.AlleleDescription_release_version, domain=None, range=int)

slots.AlleleDescription_release_date = Slot(uri=AK_SCHEMA.AlleleDescription_release_date, name="AlleleDescription_release_date", curie=AK_SCHEMA.curie('AlleleDescription_release_date'),
                   model_uri=AK_SCHEMA.AlleleDescription_release_date, domain=None, range=str)

slots.AlleleDescription_release_description = Slot(uri=AK_SCHEMA.AlleleDescription_release_description, name="AlleleDescription_release_description", curie=AK_SCHEMA.curie('AlleleDescription_release_description'),
                   model_uri=AK_SCHEMA.AlleleDescription_release_description, domain=None, range=str)

slots.AlleleDescription_label = Slot(uri=AK_SCHEMA.AlleleDescription_label, name="AlleleDescription_label", curie=AK_SCHEMA.curie('AlleleDescription_label'),
                   model_uri=AK_SCHEMA.AlleleDescription_label, domain=None, range=Optional[str])

slots.AlleleDescription_sequence = Slot(uri=AK_SCHEMA.AlleleDescription_sequence, name="AlleleDescription_sequence", curie=AK_SCHEMA.curie('AlleleDescription_sequence'),
                   model_uri=AK_SCHEMA.AlleleDescription_sequence, domain=None, range=str)

slots.AlleleDescription_coding_sequence = Slot(uri=AK_SCHEMA.AlleleDescription_coding_sequence, name="AlleleDescription_coding_sequence", curie=AK_SCHEMA.curie('AlleleDescription_coding_sequence'),
                   model_uri=AK_SCHEMA.AlleleDescription_coding_sequence, domain=None, range=str)

slots.AlleleDescription_aliases = Slot(uri=AK_SCHEMA.AlleleDescription_aliases, name="AlleleDescription_aliases", curie=AK_SCHEMA.curie('AlleleDescription_aliases'),
                   model_uri=AK_SCHEMA.AlleleDescription_aliases, domain=None, range=Optional[Union[str, List[str]]])

slots.AlleleDescription_locus = Slot(uri=AK_SCHEMA.AlleleDescription_locus, name="AlleleDescription_locus", curie=AK_SCHEMA.curie('AlleleDescription_locus'),
                   model_uri=AK_SCHEMA.AlleleDescription_locus, domain=None, range=Union[str, "Locus"])

slots.AlleleDescription_chromosome = Slot(uri=AK_SCHEMA.AlleleDescription_chromosome, name="AlleleDescription_chromosome", curie=AK_SCHEMA.curie('AlleleDescription_chromosome'),
                   model_uri=AK_SCHEMA.AlleleDescription_chromosome, domain=None, range=Optional[int])

slots.AlleleDescription_sequence_type = Slot(uri=AK_SCHEMA.AlleleDescription_sequence_type, name="AlleleDescription_sequence_type", curie=AK_SCHEMA.curie('AlleleDescription_sequence_type'),
                   model_uri=AK_SCHEMA.AlleleDescription_sequence_type, domain=None, range=Union[str, "SequenceType"])

slots.AlleleDescription_functional = Slot(uri=AK_SCHEMA.AlleleDescription_functional, name="AlleleDescription_functional", curie=AK_SCHEMA.curie('AlleleDescription_functional'),
                   model_uri=AK_SCHEMA.AlleleDescription_functional, domain=None, range=Union[bool, Bool])

slots.AlleleDescription_inference_type = Slot(uri=AK_SCHEMA.AlleleDescription_inference_type, name="AlleleDescription_inference_type", curie=AK_SCHEMA.curie('AlleleDescription_inference_type'),
                   model_uri=AK_SCHEMA.AlleleDescription_inference_type, domain=None, range=Union[str, "InferenceType"])

slots.AlleleDescription_species = Slot(uri=AK_SCHEMA.AlleleDescription_species, name="AlleleDescription_species", curie=AK_SCHEMA.curie('AlleleDescription_species'),
                   model_uri=AK_SCHEMA.AlleleDescription_species, domain=None, range=Union[str, "Species"])

slots.AlleleDescription_species_subgroup = Slot(uri=AK_SCHEMA.AlleleDescription_species_subgroup, name="AlleleDescription_species_subgroup", curie=AK_SCHEMA.curie('AlleleDescription_species_subgroup'),
                   model_uri=AK_SCHEMA.AlleleDescription_species_subgroup, domain=None, range=Optional[str])

slots.AlleleDescription_species_subgroup_type = Slot(uri=AK_SCHEMA.AlleleDescription_species_subgroup_type, name="AlleleDescription_species_subgroup_type", curie=AK_SCHEMA.curie('AlleleDescription_species_subgroup_type'),
                   model_uri=AK_SCHEMA.AlleleDescription_species_subgroup_type, domain=None, range=Optional[Union[str, "SpeciesSubgroupType"]])

slots.AlleleDescription_status = Slot(uri=AK_SCHEMA.AlleleDescription_status, name="AlleleDescription_status", curie=AK_SCHEMA.curie('AlleleDescription_status'),
                   model_uri=AK_SCHEMA.AlleleDescription_status, domain=None, range=Optional[Union[str, "Status"]])

slots.AlleleDescription_subgroup_designation = Slot(uri=AK_SCHEMA.AlleleDescription_subgroup_designation, name="AlleleDescription_subgroup_designation", curie=AK_SCHEMA.curie('AlleleDescription_subgroup_designation'),
                   model_uri=AK_SCHEMA.AlleleDescription_subgroup_designation, domain=None, range=Optional[str])

slots.AlleleDescription_gene_designation = Slot(uri=AK_SCHEMA.AlleleDescription_gene_designation, name="AlleleDescription_gene_designation", curie=AK_SCHEMA.curie('AlleleDescription_gene_designation'),
                   model_uri=AK_SCHEMA.AlleleDescription_gene_designation, domain=None, range=Optional[str])

slots.AlleleDescription_allele_designation = Slot(uri=AK_SCHEMA.AlleleDescription_allele_designation, name="AlleleDescription_allele_designation", curie=AK_SCHEMA.curie('AlleleDescription_allele_designation'),
                   model_uri=AK_SCHEMA.AlleleDescription_allele_designation, domain=None, range=Optional[str])

slots.AlleleDescription_allele_similarity_cluster_designation = Slot(uri=AK_SCHEMA.AlleleDescription_allele_similarity_cluster_designation, name="AlleleDescription_allele_similarity_cluster_designation", curie=AK_SCHEMA.curie('AlleleDescription_allele_similarity_cluster_designation'),
                   model_uri=AK_SCHEMA.AlleleDescription_allele_similarity_cluster_designation, domain=None, range=Optional[str])

slots.AlleleDescription_allele_similarity_cluster_member_id = Slot(uri=AK_SCHEMA.AlleleDescription_allele_similarity_cluster_member_id, name="AlleleDescription_allele_similarity_cluster_member_id", curie=AK_SCHEMA.curie('AlleleDescription_allele_similarity_cluster_member_id'),
                   model_uri=AK_SCHEMA.AlleleDescription_allele_similarity_cluster_member_id, domain=None, range=Optional[str])

slots.AlleleDescription_j_codon_frame = Slot(uri=AK_SCHEMA.AlleleDescription_j_codon_frame, name="AlleleDescription_j_codon_frame", curie=AK_SCHEMA.curie('AlleleDescription_j_codon_frame'),
                   model_uri=AK_SCHEMA.AlleleDescription_j_codon_frame, domain=None, range=Optional[Union[str, "JCodonFrame"]])

slots.AlleleDescription_gene_start = Slot(uri=AK_SCHEMA.AlleleDescription_gene_start, name="AlleleDescription_gene_start", curie=AK_SCHEMA.curie('AlleleDescription_gene_start'),
                   model_uri=AK_SCHEMA.AlleleDescription_gene_start, domain=None, range=Optional[int])

slots.AlleleDescription_gene_end = Slot(uri=AK_SCHEMA.AlleleDescription_gene_end, name="AlleleDescription_gene_end", curie=AK_SCHEMA.curie('AlleleDescription_gene_end'),
                   model_uri=AK_SCHEMA.AlleleDescription_gene_end, domain=None, range=Optional[int])

slots.AlleleDescription_utr_5_prime_start = Slot(uri=AK_SCHEMA.AlleleDescription_utr_5_prime_start, name="AlleleDescription_utr_5_prime_start", curie=AK_SCHEMA.curie('AlleleDescription_utr_5_prime_start'),
                   model_uri=AK_SCHEMA.AlleleDescription_utr_5_prime_start, domain=None, range=Optional[int])

slots.AlleleDescription_utr_5_prime_end = Slot(uri=AK_SCHEMA.AlleleDescription_utr_5_prime_end, name="AlleleDescription_utr_5_prime_end", curie=AK_SCHEMA.curie('AlleleDescription_utr_5_prime_end'),
                   model_uri=AK_SCHEMA.AlleleDescription_utr_5_prime_end, domain=None, range=Optional[int])

slots.AlleleDescription_leader_1_start = Slot(uri=AK_SCHEMA.AlleleDescription_leader_1_start, name="AlleleDescription_leader_1_start", curie=AK_SCHEMA.curie('AlleleDescription_leader_1_start'),
                   model_uri=AK_SCHEMA.AlleleDescription_leader_1_start, domain=None, range=Optional[int])

slots.AlleleDescription_leader_1_end = Slot(uri=AK_SCHEMA.AlleleDescription_leader_1_end, name="AlleleDescription_leader_1_end", curie=AK_SCHEMA.curie('AlleleDescription_leader_1_end'),
                   model_uri=AK_SCHEMA.AlleleDescription_leader_1_end, domain=None, range=Optional[int])

slots.AlleleDescription_leader_2_start = Slot(uri=AK_SCHEMA.AlleleDescription_leader_2_start, name="AlleleDescription_leader_2_start", curie=AK_SCHEMA.curie('AlleleDescription_leader_2_start'),
                   model_uri=AK_SCHEMA.AlleleDescription_leader_2_start, domain=None, range=Optional[int])

slots.AlleleDescription_leader_2_end = Slot(uri=AK_SCHEMA.AlleleDescription_leader_2_end, name="AlleleDescription_leader_2_end", curie=AK_SCHEMA.curie('AlleleDescription_leader_2_end'),
                   model_uri=AK_SCHEMA.AlleleDescription_leader_2_end, domain=None, range=Optional[int])

slots.AlleleDescription_v_rs_start = Slot(uri=AK_SCHEMA.AlleleDescription_v_rs_start, name="AlleleDescription_v_rs_start", curie=AK_SCHEMA.curie('AlleleDescription_v_rs_start'),
                   model_uri=AK_SCHEMA.AlleleDescription_v_rs_start, domain=None, range=Optional[int])

slots.AlleleDescription_v_rs_end = Slot(uri=AK_SCHEMA.AlleleDescription_v_rs_end, name="AlleleDescription_v_rs_end", curie=AK_SCHEMA.curie('AlleleDescription_v_rs_end'),
                   model_uri=AK_SCHEMA.AlleleDescription_v_rs_end, domain=None, range=Optional[int])

slots.AlleleDescription_d_rs_3_prime_start = Slot(uri=AK_SCHEMA.AlleleDescription_d_rs_3_prime_start, name="AlleleDescription_d_rs_3_prime_start", curie=AK_SCHEMA.curie('AlleleDescription_d_rs_3_prime_start'),
                   model_uri=AK_SCHEMA.AlleleDescription_d_rs_3_prime_start, domain=None, range=Optional[int])

slots.AlleleDescription_d_rs_3_prime_end = Slot(uri=AK_SCHEMA.AlleleDescription_d_rs_3_prime_end, name="AlleleDescription_d_rs_3_prime_end", curie=AK_SCHEMA.curie('AlleleDescription_d_rs_3_prime_end'),
                   model_uri=AK_SCHEMA.AlleleDescription_d_rs_3_prime_end, domain=None, range=Optional[int])

slots.AlleleDescription_d_rs_5_prime_start = Slot(uri=AK_SCHEMA.AlleleDescription_d_rs_5_prime_start, name="AlleleDescription_d_rs_5_prime_start", curie=AK_SCHEMA.curie('AlleleDescription_d_rs_5_prime_start'),
                   model_uri=AK_SCHEMA.AlleleDescription_d_rs_5_prime_start, domain=None, range=Optional[int])

slots.AlleleDescription_d_rs_5_prime_end = Slot(uri=AK_SCHEMA.AlleleDescription_d_rs_5_prime_end, name="AlleleDescription_d_rs_5_prime_end", curie=AK_SCHEMA.curie('AlleleDescription_d_rs_5_prime_end'),
                   model_uri=AK_SCHEMA.AlleleDescription_d_rs_5_prime_end, domain=None, range=Optional[int])

slots.AlleleDescription_j_cdr3_end = Slot(uri=AK_SCHEMA.AlleleDescription_j_cdr3_end, name="AlleleDescription_j_cdr3_end", curie=AK_SCHEMA.curie('AlleleDescription_j_cdr3_end'),
                   model_uri=AK_SCHEMA.AlleleDescription_j_cdr3_end, domain=None, range=Optional[int])

slots.AlleleDescription_j_rs_start = Slot(uri=AK_SCHEMA.AlleleDescription_j_rs_start, name="AlleleDescription_j_rs_start", curie=AK_SCHEMA.curie('AlleleDescription_j_rs_start'),
                   model_uri=AK_SCHEMA.AlleleDescription_j_rs_start, domain=None, range=Optional[int])

slots.AlleleDescription_j_rs_end = Slot(uri=AK_SCHEMA.AlleleDescription_j_rs_end, name="AlleleDescription_j_rs_end", curie=AK_SCHEMA.curie('AlleleDescription_j_rs_end'),
                   model_uri=AK_SCHEMA.AlleleDescription_j_rs_end, domain=None, range=Optional[int])

slots.AlleleDescription_j_donor_splice = Slot(uri=AK_SCHEMA.AlleleDescription_j_donor_splice, name="AlleleDescription_j_donor_splice", curie=AK_SCHEMA.curie('AlleleDescription_j_donor_splice'),
                   model_uri=AK_SCHEMA.AlleleDescription_j_donor_splice, domain=None, range=Optional[int])

slots.AlleleDescription_v_gene_delineations = Slot(uri=AK_SCHEMA.AlleleDescription_v_gene_delineations, name="AlleleDescription_v_gene_delineations", curie=AK_SCHEMA.curie('AlleleDescription_v_gene_delineations'),
                   model_uri=AK_SCHEMA.AlleleDescription_v_gene_delineations, domain=None, range=Optional[Union[Union[dict, SequenceDelineationV], List[Union[dict, SequenceDelineationV]]]])

slots.AlleleDescription_unrearranged_support = Slot(uri=AK_SCHEMA.AlleleDescription_unrearranged_support, name="AlleleDescription_unrearranged_support", curie=AK_SCHEMA.curie('AlleleDescription_unrearranged_support'),
                   model_uri=AK_SCHEMA.AlleleDescription_unrearranged_support, domain=None, range=Optional[Union[Union[dict, UnrearrangedSequence], List[Union[dict, UnrearrangedSequence]]]])

slots.AlleleDescription_rearranged_support = Slot(uri=AK_SCHEMA.AlleleDescription_rearranged_support, name="AlleleDescription_rearranged_support", curie=AK_SCHEMA.curie('AlleleDescription_rearranged_support'),
                   model_uri=AK_SCHEMA.AlleleDescription_rearranged_support, domain=None, range=Optional[Union[Union[dict, RearrangedSequence], List[Union[dict, RearrangedSequence]]]])

slots.AlleleDescription_paralogs = Slot(uri=AK_SCHEMA.AlleleDescription_paralogs, name="AlleleDescription_paralogs", curie=AK_SCHEMA.curie('AlleleDescription_paralogs'),
                   model_uri=AK_SCHEMA.AlleleDescription_paralogs, domain=None, range=Optional[Union[str, List[str]]])

slots.AlleleDescription_curation = Slot(uri=AK_SCHEMA.AlleleDescription_curation, name="AlleleDescription_curation", curie=AK_SCHEMA.curie('AlleleDescription_curation'),
                   model_uri=AK_SCHEMA.AlleleDescription_curation, domain=None, range=Optional[str])

slots.AlleleDescription_curational_tags = Slot(uri=AK_SCHEMA.AlleleDescription_curational_tags, name="AlleleDescription_curational_tags", curie=AK_SCHEMA.curie('AlleleDescription_curational_tags'),
                   model_uri=AK_SCHEMA.AlleleDescription_curational_tags, domain=None, range=Optional[Union[Union[str, "CurationalTags"], List[Union[str, "CurationalTags"]]]])

slots.GermlineSet_germline_set_id = Slot(uri=AK_SCHEMA.GermlineSet_germline_set_id, name="GermlineSet_germline_set_id", curie=AK_SCHEMA.curie('GermlineSet_germline_set_id'),
                   model_uri=AK_SCHEMA.GermlineSet_germline_set_id, domain=None, range=str)

slots.GermlineSet_author = Slot(uri=AK_SCHEMA.GermlineSet_author, name="GermlineSet_author", curie=AK_SCHEMA.curie('GermlineSet_author'),
                   model_uri=AK_SCHEMA.GermlineSet_author, domain=None, range=str)

slots.GermlineSet_lab_name = Slot(uri=AK_SCHEMA.GermlineSet_lab_name, name="GermlineSet_lab_name", curie=AK_SCHEMA.curie('GermlineSet_lab_name'),
                   model_uri=AK_SCHEMA.GermlineSet_lab_name, domain=None, range=str)

slots.GermlineSet_lab_address = Slot(uri=AK_SCHEMA.GermlineSet_lab_address, name="GermlineSet_lab_address", curie=AK_SCHEMA.curie('GermlineSet_lab_address'),
                   model_uri=AK_SCHEMA.GermlineSet_lab_address, domain=None, range=str)

slots.GermlineSet_acknowledgements = Slot(uri=AK_SCHEMA.GermlineSet_acknowledgements, name="GermlineSet_acknowledgements", curie=AK_SCHEMA.curie('GermlineSet_acknowledgements'),
                   model_uri=AK_SCHEMA.GermlineSet_acknowledgements, domain=None, range=Optional[Union[Union[dict, Acknowledgement], List[Union[dict, Acknowledgement]]]])

slots.GermlineSet_release_version = Slot(uri=AK_SCHEMA.GermlineSet_release_version, name="GermlineSet_release_version", curie=AK_SCHEMA.curie('GermlineSet_release_version'),
                   model_uri=AK_SCHEMA.GermlineSet_release_version, domain=None, range=float)

slots.GermlineSet_release_description = Slot(uri=AK_SCHEMA.GermlineSet_release_description, name="GermlineSet_release_description", curie=AK_SCHEMA.curie('GermlineSet_release_description'),
                   model_uri=AK_SCHEMA.GermlineSet_release_description, domain=None, range=str)

slots.GermlineSet_release_date = Slot(uri=AK_SCHEMA.GermlineSet_release_date, name="GermlineSet_release_date", curie=AK_SCHEMA.curie('GermlineSet_release_date'),
                   model_uri=AK_SCHEMA.GermlineSet_release_date, domain=None, range=str)

slots.GermlineSet_germline_set_name = Slot(uri=AK_SCHEMA.GermlineSet_germline_set_name, name="GermlineSet_germline_set_name", curie=AK_SCHEMA.curie('GermlineSet_germline_set_name'),
                   model_uri=AK_SCHEMA.GermlineSet_germline_set_name, domain=None, range=str)

slots.GermlineSet_germline_set_ref = Slot(uri=AK_SCHEMA.GermlineSet_germline_set_ref, name="GermlineSet_germline_set_ref", curie=AK_SCHEMA.curie('GermlineSet_germline_set_ref'),
                   model_uri=AK_SCHEMA.GermlineSet_germline_set_ref, domain=None, range=str)

slots.GermlineSet_pub_ids = Slot(uri=AK_SCHEMA.GermlineSet_pub_ids, name="GermlineSet_pub_ids", curie=AK_SCHEMA.curie('GermlineSet_pub_ids'),
                   model_uri=AK_SCHEMA.GermlineSet_pub_ids, domain=None, range=Optional[str])

slots.GermlineSet_species = Slot(uri=AK_SCHEMA.GermlineSet_species, name="GermlineSet_species", curie=AK_SCHEMA.curie('GermlineSet_species'),
                   model_uri=AK_SCHEMA.GermlineSet_species, domain=None, range=Union[str, "Species"])

slots.GermlineSet_species_subgroup = Slot(uri=AK_SCHEMA.GermlineSet_species_subgroup, name="GermlineSet_species_subgroup", curie=AK_SCHEMA.curie('GermlineSet_species_subgroup'),
                   model_uri=AK_SCHEMA.GermlineSet_species_subgroup, domain=None, range=Optional[str])

slots.GermlineSet_species_subgroup_type = Slot(uri=AK_SCHEMA.GermlineSet_species_subgroup_type, name="GermlineSet_species_subgroup_type", curie=AK_SCHEMA.curie('GermlineSet_species_subgroup_type'),
                   model_uri=AK_SCHEMA.GermlineSet_species_subgroup_type, domain=None, range=Optional[Union[str, "SpeciesSubgroupType"]])

slots.GermlineSet_locus = Slot(uri=AK_SCHEMA.GermlineSet_locus, name="GermlineSet_locus", curie=AK_SCHEMA.curie('GermlineSet_locus'),
                   model_uri=AK_SCHEMA.GermlineSet_locus, domain=None, range=Union[str, "Locus"])

slots.GermlineSet_allele_descriptions = Slot(uri=AK_SCHEMA.GermlineSet_allele_descriptions, name="GermlineSet_allele_descriptions", curie=AK_SCHEMA.curie('GermlineSet_allele_descriptions'),
                   model_uri=AK_SCHEMA.GermlineSet_allele_descriptions, domain=None, range=Union[Union[dict, AlleleDescription], List[Union[dict, AlleleDescription]]])

slots.GermlineSet_curation = Slot(uri=AK_SCHEMA.GermlineSet_curation, name="GermlineSet_curation", curie=AK_SCHEMA.curie('GermlineSet_curation'),
                   model_uri=AK_SCHEMA.GermlineSet_curation, domain=None, range=Optional[str])

slots.GenotypeSet_receptor_genotype_set_id = Slot(uri=AK_SCHEMA.GenotypeSet_receptor_genotype_set_id, name="GenotypeSet_receptor_genotype_set_id", curie=AK_SCHEMA.curie('GenotypeSet_receptor_genotype_set_id'),
                   model_uri=AK_SCHEMA.GenotypeSet_receptor_genotype_set_id, domain=None, range=str)

slots.GenotypeSet_genotype_class_list = Slot(uri=AK_SCHEMA.GenotypeSet_genotype_class_list, name="GenotypeSet_genotype_class_list", curie=AK_SCHEMA.curie('GenotypeSet_genotype_class_list'),
                   model_uri=AK_SCHEMA.GenotypeSet_genotype_class_list, domain=None, range=Optional[Union[Union[dict, Genotype], List[Union[dict, Genotype]]]])

slots.Genotype_receptor_genotype_id = Slot(uri=AK_SCHEMA.Genotype_receptor_genotype_id, name="Genotype_receptor_genotype_id", curie=AK_SCHEMA.curie('Genotype_receptor_genotype_id'),
                   model_uri=AK_SCHEMA.Genotype_receptor_genotype_id, domain=None, range=str)

slots.Genotype_locus = Slot(uri=AK_SCHEMA.Genotype_locus, name="Genotype_locus", curie=AK_SCHEMA.curie('Genotype_locus'),
                   model_uri=AK_SCHEMA.Genotype_locus, domain=None, range=Union[str, "Locus"])

slots.Genotype_documented_alleles = Slot(uri=AK_SCHEMA.Genotype_documented_alleles, name="Genotype_documented_alleles", curie=AK_SCHEMA.curie('Genotype_documented_alleles'),
                   model_uri=AK_SCHEMA.Genotype_documented_alleles, domain=None, range=Optional[Union[Union[dict, DocumentedAllele], List[Union[dict, DocumentedAllele]]]])

slots.Genotype_undocumented_alleles = Slot(uri=AK_SCHEMA.Genotype_undocumented_alleles, name="Genotype_undocumented_alleles", curie=AK_SCHEMA.curie('Genotype_undocumented_alleles'),
                   model_uri=AK_SCHEMA.Genotype_undocumented_alleles, domain=None, range=Optional[Union[Union[dict, UndocumentedAllele], List[Union[dict, UndocumentedAllele]]]])

slots.Genotype_deleted_genes = Slot(uri=AK_SCHEMA.Genotype_deleted_genes, name="Genotype_deleted_genes", curie=AK_SCHEMA.curie('Genotype_deleted_genes'),
                   model_uri=AK_SCHEMA.Genotype_deleted_genes, domain=None, range=Optional[Union[Union[dict, DeletedGene], List[Union[dict, DeletedGene]]]])

slots.Genotype_inference_process = Slot(uri=AK_SCHEMA.Genotype_inference_process, name="Genotype_inference_process", curie=AK_SCHEMA.curie('Genotype_inference_process'),
                   model_uri=AK_SCHEMA.Genotype_inference_process, domain=None, range=Optional[Union[str, "InferenceProcess"]])

slots.DocumentedAllele_label = Slot(uri=AK_SCHEMA.DocumentedAllele_label, name="DocumentedAllele_label", curie=AK_SCHEMA.curie('DocumentedAllele_label'),
                   model_uri=AK_SCHEMA.DocumentedAllele_label, domain=None, range=str)

slots.DocumentedAllele_germline_set_ref = Slot(uri=AK_SCHEMA.DocumentedAllele_germline_set_ref, name="DocumentedAllele_germline_set_ref", curie=AK_SCHEMA.curie('DocumentedAllele_germline_set_ref'),
                   model_uri=AK_SCHEMA.DocumentedAllele_germline_set_ref, domain=None, range=str)

slots.DocumentedAllele_phasing = Slot(uri=AK_SCHEMA.DocumentedAllele_phasing, name="DocumentedAllele_phasing", curie=AK_SCHEMA.curie('DocumentedAllele_phasing'),
                   model_uri=AK_SCHEMA.DocumentedAllele_phasing, domain=None, range=Optional[int])

slots.UndocumentedAllele_allele_name = Slot(uri=AK_SCHEMA.UndocumentedAllele_allele_name, name="UndocumentedAllele_allele_name", curie=AK_SCHEMA.curie('UndocumentedAllele_allele_name'),
                   model_uri=AK_SCHEMA.UndocumentedAllele_allele_name, domain=None, range=str)

slots.UndocumentedAllele_sequence = Slot(uri=AK_SCHEMA.UndocumentedAllele_sequence, name="UndocumentedAllele_sequence", curie=AK_SCHEMA.curie('UndocumentedAllele_sequence'),
                   model_uri=AK_SCHEMA.UndocumentedAllele_sequence, domain=None, range=str)

slots.UndocumentedAllele_phasing = Slot(uri=AK_SCHEMA.UndocumentedAllele_phasing, name="UndocumentedAllele_phasing", curie=AK_SCHEMA.curie('UndocumentedAllele_phasing'),
                   model_uri=AK_SCHEMA.UndocumentedAllele_phasing, domain=None, range=Optional[int])

slots.DeletedGene_label = Slot(uri=AK_SCHEMA.DeletedGene_label, name="DeletedGene_label", curie=AK_SCHEMA.curie('DeletedGene_label'),
                   model_uri=AK_SCHEMA.DeletedGene_label, domain=None, range=str)

slots.DeletedGene_germline_set_ref = Slot(uri=AK_SCHEMA.DeletedGene_germline_set_ref, name="DeletedGene_germline_set_ref", curie=AK_SCHEMA.curie('DeletedGene_germline_set_ref'),
                   model_uri=AK_SCHEMA.DeletedGene_germline_set_ref, domain=None, range=str)

slots.DeletedGene_phasing = Slot(uri=AK_SCHEMA.DeletedGene_phasing, name="DeletedGene_phasing", curie=AK_SCHEMA.curie('DeletedGene_phasing'),
                   model_uri=AK_SCHEMA.DeletedGene_phasing, domain=None, range=Optional[int])

slots.MHCGenotypeSet_mhc_genotype_set_id = Slot(uri=AK_SCHEMA.MHCGenotypeSet_mhc_genotype_set_id, name="MHCGenotypeSet_mhc_genotype_set_id", curie=AK_SCHEMA.curie('MHCGenotypeSet_mhc_genotype_set_id'),
                   model_uri=AK_SCHEMA.MHCGenotypeSet_mhc_genotype_set_id, domain=None, range=str)

slots.MHCGenotypeSet_mhc_genotype_list = Slot(uri=AK_SCHEMA.MHCGenotypeSet_mhc_genotype_list, name="MHCGenotypeSet_mhc_genotype_list", curie=AK_SCHEMA.curie('MHCGenotypeSet_mhc_genotype_list'),
                   model_uri=AK_SCHEMA.MHCGenotypeSet_mhc_genotype_list, domain=None, range=Union[Union[dict, MHCGenotype], List[Union[dict, MHCGenotype]]])

slots.MHCGenotype_mhc_genotype_id = Slot(uri=AK_SCHEMA.MHCGenotype_mhc_genotype_id, name="MHCGenotype_mhc_genotype_id", curie=AK_SCHEMA.curie('MHCGenotype_mhc_genotype_id'),
                   model_uri=AK_SCHEMA.MHCGenotype_mhc_genotype_id, domain=None, range=str)

slots.MHCGenotype_mhc_class = Slot(uri=AK_SCHEMA.MHCGenotype_mhc_class, name="MHCGenotype_mhc_class", curie=AK_SCHEMA.curie('MHCGenotype_mhc_class'),
                   model_uri=AK_SCHEMA.MHCGenotype_mhc_class, domain=None, range=Union[str, "MhcClass"])

slots.MHCGenotype_mhc_alleles = Slot(uri=AK_SCHEMA.MHCGenotype_mhc_alleles, name="MHCGenotype_mhc_alleles", curie=AK_SCHEMA.curie('MHCGenotype_mhc_alleles'),
                   model_uri=AK_SCHEMA.MHCGenotype_mhc_alleles, domain=None, range=Union[Union[dict, MHCAllele], List[Union[dict, MHCAllele]]])

slots.MHCGenotype_mhc_genotyping_method = Slot(uri=AK_SCHEMA.MHCGenotype_mhc_genotyping_method, name="MHCGenotype_mhc_genotyping_method", curie=AK_SCHEMA.curie('MHCGenotype_mhc_genotyping_method'),
                   model_uri=AK_SCHEMA.MHCGenotype_mhc_genotyping_method, domain=None, range=Optional[str])

slots.MHCAllele_allele_designation = Slot(uri=AK_SCHEMA.MHCAllele_allele_designation, name="MHCAllele_allele_designation", curie=AK_SCHEMA.curie('MHCAllele_allele_designation'),
                   model_uri=AK_SCHEMA.MHCAllele_allele_designation, domain=None, range=Optional[str])

slots.MHCAllele_gene = Slot(uri=AK_SCHEMA.MHCAllele_gene, name="MHCAllele_gene", curie=AK_SCHEMA.curie('MHCAllele_gene'),
                   model_uri=AK_SCHEMA.MHCAllele_gene, domain=None, range=Optional[Union[str, "Gene"]])

slots.MHCAllele_reference_set_ref = Slot(uri=AK_SCHEMA.MHCAllele_reference_set_ref, name="MHCAllele_reference_set_ref", curie=AK_SCHEMA.curie('MHCAllele_reference_set_ref'),
                   model_uri=AK_SCHEMA.MHCAllele_reference_set_ref, domain=None, range=Optional[str])

slots.SubjectGenotype_receptor_genotype_set = Slot(uri=AK_SCHEMA.SubjectGenotype_receptor_genotype_set, name="SubjectGenotype_receptor_genotype_set", curie=AK_SCHEMA.curie('SubjectGenotype_receptor_genotype_set'),
                   model_uri=AK_SCHEMA.SubjectGenotype_receptor_genotype_set, domain=None, range=Optional[Union[dict, GenotypeSet]])

slots.SubjectGenotype_mhc_genotype_set = Slot(uri=AK_SCHEMA.SubjectGenotype_mhc_genotype_set, name="SubjectGenotype_mhc_genotype_set", curie=AK_SCHEMA.curie('SubjectGenotype_mhc_genotype_set'),
                   model_uri=AK_SCHEMA.SubjectGenotype_mhc_genotype_set, domain=None, range=Optional[Union[dict, MHCGenotypeSet]])

slots.Study_study_id = Slot(uri=AK_SCHEMA.Study_study_id, name="Study_study_id", curie=AK_SCHEMA.curie('Study_study_id'),
                   model_uri=AK_SCHEMA.Study_study_id, domain=None, range=str)

slots.Study_study_title = Slot(uri=AK_SCHEMA.Study_study_title, name="Study_study_title", curie=AK_SCHEMA.curie('Study_study_title'),
                   model_uri=AK_SCHEMA.Study_study_title, domain=None, range=str)

slots.Study_study_type = Slot(uri=AK_SCHEMA.Study_study_type, name="Study_study_type", curie=AK_SCHEMA.curie('Study_study_type'),
                   model_uri=AK_SCHEMA.Study_study_type, domain=None, range=Union[str, "StudyType"])

slots.Study_study_description = Slot(uri=AK_SCHEMA.Study_study_description, name="Study_study_description", curie=AK_SCHEMA.curie('Study_study_description'),
                   model_uri=AK_SCHEMA.Study_study_description, domain=None, range=Optional[str])

slots.Study_inclusion_exclusion_criteria = Slot(uri=AK_SCHEMA.Study_inclusion_exclusion_criteria, name="Study_inclusion_exclusion_criteria", curie=AK_SCHEMA.curie('Study_inclusion_exclusion_criteria'),
                   model_uri=AK_SCHEMA.Study_inclusion_exclusion_criteria, domain=None, range=str)

slots.Study_grants = Slot(uri=AK_SCHEMA.Study_grants, name="Study_grants", curie=AK_SCHEMA.curie('Study_grants'),
                   model_uri=AK_SCHEMA.Study_grants, domain=None, range=str)

slots.Study_study_contact = Slot(uri=AK_SCHEMA.Study_study_contact, name="Study_study_contact", curie=AK_SCHEMA.curie('Study_study_contact'),
                   model_uri=AK_SCHEMA.Study_study_contact, domain=None, range=Optional[str])

slots.Study_collected_by = Slot(uri=AK_SCHEMA.Study_collected_by, name="Study_collected_by", curie=AK_SCHEMA.curie('Study_collected_by'),
                   model_uri=AK_SCHEMA.Study_collected_by, domain=None, range=str)

slots.Study_lab_name = Slot(uri=AK_SCHEMA.Study_lab_name, name="Study_lab_name", curie=AK_SCHEMA.curie('Study_lab_name'),
                   model_uri=AK_SCHEMA.Study_lab_name, domain=None, range=str)

slots.Study_lab_address = Slot(uri=AK_SCHEMA.Study_lab_address, name="Study_lab_address", curie=AK_SCHEMA.curie('Study_lab_address'),
                   model_uri=AK_SCHEMA.Study_lab_address, domain=None, range=str)

slots.Study_submitted_by = Slot(uri=AK_SCHEMA.Study_submitted_by, name="Study_submitted_by", curie=AK_SCHEMA.curie('Study_submitted_by'),
                   model_uri=AK_SCHEMA.Study_submitted_by, domain=None, range=str)

slots.Study_pub_ids = Slot(uri=AK_SCHEMA.Study_pub_ids, name="Study_pub_ids", curie=AK_SCHEMA.curie('Study_pub_ids'),
                   model_uri=AK_SCHEMA.Study_pub_ids, domain=None, range=str)

slots.Study_keywords_study = Slot(uri=AK_SCHEMA.Study_keywords_study, name="Study_keywords_study", curie=AK_SCHEMA.curie('Study_keywords_study'),
                   model_uri=AK_SCHEMA.Study_keywords_study, domain=None, range=Union[Union[str, "KeywordsStudy"], List[Union[str, "KeywordsStudy"]]])

slots.Study_adc_publish_date = Slot(uri=AK_SCHEMA.Study_adc_publish_date, name="Study_adc_publish_date", curie=AK_SCHEMA.curie('Study_adc_publish_date'),
                   model_uri=AK_SCHEMA.Study_adc_publish_date, domain=None, range=Optional[str])

slots.Study_adc_update_date = Slot(uri=AK_SCHEMA.Study_adc_update_date, name="Study_adc_update_date", curie=AK_SCHEMA.curie('Study_adc_update_date'),
                   model_uri=AK_SCHEMA.Study_adc_update_date, domain=None, range=Optional[str])

slots.Subject_subject_id = Slot(uri=AK_SCHEMA.Subject_subject_id, name="Subject_subject_id", curie=AK_SCHEMA.curie('Subject_subject_id'),
                   model_uri=AK_SCHEMA.Subject_subject_id, domain=None, range=str)

slots.Subject_synthetic = Slot(uri=AK_SCHEMA.Subject_synthetic, name="Subject_synthetic", curie=AK_SCHEMA.curie('Subject_synthetic'),
                   model_uri=AK_SCHEMA.Subject_synthetic, domain=None, range=Union[bool, Bool])

slots.Subject_species = Slot(uri=AK_SCHEMA.Subject_species, name="Subject_species", curie=AK_SCHEMA.curie('Subject_species'),
                   model_uri=AK_SCHEMA.Subject_species, domain=None, range=Union[str, "Species"])

slots.Subject_sex = Slot(uri=AK_SCHEMA.Subject_sex, name="Subject_sex", curie=AK_SCHEMA.curie('Subject_sex'),
                   model_uri=AK_SCHEMA.Subject_sex, domain=None, range=Union[str, "Sex"])

slots.Subject_age_min = Slot(uri=AK_SCHEMA.Subject_age_min, name="Subject_age_min", curie=AK_SCHEMA.curie('Subject_age_min'),
                   model_uri=AK_SCHEMA.Subject_age_min, domain=None, range=float)

slots.Subject_age_max = Slot(uri=AK_SCHEMA.Subject_age_max, name="Subject_age_max", curie=AK_SCHEMA.curie('Subject_age_max'),
                   model_uri=AK_SCHEMA.Subject_age_max, domain=None, range=float)

slots.Subject_age_unit = Slot(uri=AK_SCHEMA.Subject_age_unit, name="Subject_age_unit", curie=AK_SCHEMA.curie('Subject_age_unit'),
                   model_uri=AK_SCHEMA.Subject_age_unit, domain=None, range=Union[str, "AgeUnit"])

slots.Subject_age_event = Slot(uri=AK_SCHEMA.Subject_age_event, name="Subject_age_event", curie=AK_SCHEMA.curie('Subject_age_event'),
                   model_uri=AK_SCHEMA.Subject_age_event, domain=None, range=str)

slots.Subject_ancestry_population = Slot(uri=AK_SCHEMA.Subject_ancestry_population, name="Subject_ancestry_population", curie=AK_SCHEMA.curie('Subject_ancestry_population'),
                   model_uri=AK_SCHEMA.Subject_ancestry_population, domain=None, range=str)

slots.Subject_ethnicity = Slot(uri=AK_SCHEMA.Subject_ethnicity, name="Subject_ethnicity", curie=AK_SCHEMA.curie('Subject_ethnicity'),
                   model_uri=AK_SCHEMA.Subject_ethnicity, domain=None, range=str)

slots.Subject_race = Slot(uri=AK_SCHEMA.Subject_race, name="Subject_race", curie=AK_SCHEMA.curie('Subject_race'),
                   model_uri=AK_SCHEMA.Subject_race, domain=None, range=str)

slots.Subject_strain_name = Slot(uri=AK_SCHEMA.Subject_strain_name, name="Subject_strain_name", curie=AK_SCHEMA.curie('Subject_strain_name'),
                   model_uri=AK_SCHEMA.Subject_strain_name, domain=None, range=str)

slots.Subject_linked_subjects = Slot(uri=AK_SCHEMA.Subject_linked_subjects, name="Subject_linked_subjects", curie=AK_SCHEMA.curie('Subject_linked_subjects'),
                   model_uri=AK_SCHEMA.Subject_linked_subjects, domain=None, range=str)

slots.Subject_link_type = Slot(uri=AK_SCHEMA.Subject_link_type, name="Subject_link_type", curie=AK_SCHEMA.curie('Subject_link_type'),
                   model_uri=AK_SCHEMA.Subject_link_type, domain=None, range=str)

slots.Subject_diagnosis = Slot(uri=AK_SCHEMA.Subject_diagnosis, name="Subject_diagnosis", curie=AK_SCHEMA.curie('Subject_diagnosis'),
                   model_uri=AK_SCHEMA.Subject_diagnosis, domain=None, range=Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]])

slots.Subject_genotype = Slot(uri=AK_SCHEMA.Subject_genotype, name="Subject_genotype", curie=AK_SCHEMA.curie('Subject_genotype'),
                   model_uri=AK_SCHEMA.Subject_genotype, domain=None, range=Optional[Union[dict, SubjectGenotype]])

slots.Diagnosis_study_group_description = Slot(uri=AK_SCHEMA.Diagnosis_study_group_description, name="Diagnosis_study_group_description", curie=AK_SCHEMA.curie('Diagnosis_study_group_description'),
                   model_uri=AK_SCHEMA.Diagnosis_study_group_description, domain=None, range=str)

slots.Diagnosis_disease_diagnosis = Slot(uri=AK_SCHEMA.Diagnosis_disease_diagnosis, name="Diagnosis_disease_diagnosis", curie=AK_SCHEMA.curie('Diagnosis_disease_diagnosis'),
                   model_uri=AK_SCHEMA.Diagnosis_disease_diagnosis, domain=None, range=Union[str, "DiseaseDiagnosis"])

slots.Diagnosis_disease_length = Slot(uri=AK_SCHEMA.Diagnosis_disease_length, name="Diagnosis_disease_length", curie=AK_SCHEMA.curie('Diagnosis_disease_length'),
                   model_uri=AK_SCHEMA.Diagnosis_disease_length, domain=None, range=str)

slots.Diagnosis_disease_stage = Slot(uri=AK_SCHEMA.Diagnosis_disease_stage, name="Diagnosis_disease_stage", curie=AK_SCHEMA.curie('Diagnosis_disease_stage'),
                   model_uri=AK_SCHEMA.Diagnosis_disease_stage, domain=None, range=str)

slots.Diagnosis_prior_therapies = Slot(uri=AK_SCHEMA.Diagnosis_prior_therapies, name="Diagnosis_prior_therapies", curie=AK_SCHEMA.curie('Diagnosis_prior_therapies'),
                   model_uri=AK_SCHEMA.Diagnosis_prior_therapies, domain=None, range=str)

slots.Diagnosis_immunogen = Slot(uri=AK_SCHEMA.Diagnosis_immunogen, name="Diagnosis_immunogen", curie=AK_SCHEMA.curie('Diagnosis_immunogen'),
                   model_uri=AK_SCHEMA.Diagnosis_immunogen, domain=None, range=str)

slots.Diagnosis_intervention = Slot(uri=AK_SCHEMA.Diagnosis_intervention, name="Diagnosis_intervention", curie=AK_SCHEMA.curie('Diagnosis_intervention'),
                   model_uri=AK_SCHEMA.Diagnosis_intervention, domain=None, range=str)

slots.Diagnosis_medical_history = Slot(uri=AK_SCHEMA.Diagnosis_medical_history, name="Diagnosis_medical_history", curie=AK_SCHEMA.curie('Diagnosis_medical_history'),
                   model_uri=AK_SCHEMA.Diagnosis_medical_history, domain=None, range=str)

slots.Sample_sample_id = Slot(uri=AK_SCHEMA.Sample_sample_id, name="Sample_sample_id", curie=AK_SCHEMA.curie('Sample_sample_id'),
                   model_uri=AK_SCHEMA.Sample_sample_id, domain=None, range=str)

slots.Sample_sample_type = Slot(uri=AK_SCHEMA.Sample_sample_type, name="Sample_sample_type", curie=AK_SCHEMA.curie('Sample_sample_type'),
                   model_uri=AK_SCHEMA.Sample_sample_type, domain=None, range=str)

slots.Sample_tissue = Slot(uri=AK_SCHEMA.Sample_tissue, name="Sample_tissue", curie=AK_SCHEMA.curie('Sample_tissue'),
                   model_uri=AK_SCHEMA.Sample_tissue, domain=None, range=Union[str, TissueAkcId])

slots.Sample_anatomic_site = Slot(uri=AK_SCHEMA.Sample_anatomic_site, name="Sample_anatomic_site", curie=AK_SCHEMA.curie('Sample_anatomic_site'),
                   model_uri=AK_SCHEMA.Sample_anatomic_site, domain=None, range=str)

slots.Sample_disease_state_sample = Slot(uri=AK_SCHEMA.Sample_disease_state_sample, name="Sample_disease_state_sample", curie=AK_SCHEMA.curie('Sample_disease_state_sample'),
                   model_uri=AK_SCHEMA.Sample_disease_state_sample, domain=None, range=str)

slots.Sample_collection_time_point_relative = Slot(uri=AK_SCHEMA.Sample_collection_time_point_relative, name="Sample_collection_time_point_relative", curie=AK_SCHEMA.curie('Sample_collection_time_point_relative'),
                   model_uri=AK_SCHEMA.Sample_collection_time_point_relative, domain=None, range=float)

slots.Sample_collection_time_point_relative_unit = Slot(uri=AK_SCHEMA.Sample_collection_time_point_relative_unit, name="Sample_collection_time_point_relative_unit", curie=AK_SCHEMA.curie('Sample_collection_time_point_relative_unit'),
                   model_uri=AK_SCHEMA.Sample_collection_time_point_relative_unit, domain=None, range=Union[str, "CollectionTimePointRelativeUnit"])

slots.Sample_collection_time_point_reference = Slot(uri=AK_SCHEMA.Sample_collection_time_point_reference, name="Sample_collection_time_point_reference", curie=AK_SCHEMA.curie('Sample_collection_time_point_reference'),
                   model_uri=AK_SCHEMA.Sample_collection_time_point_reference, domain=None, range=str)

slots.Sample_biomaterial_provider = Slot(uri=AK_SCHEMA.Sample_biomaterial_provider, name="Sample_biomaterial_provider", curie=AK_SCHEMA.curie('Sample_biomaterial_provider'),
                   model_uri=AK_SCHEMA.Sample_biomaterial_provider, domain=None, range=str)

slots.CellProcessing_tissue_processing = Slot(uri=AK_SCHEMA.CellProcessing_tissue_processing, name="CellProcessing_tissue_processing", curie=AK_SCHEMA.curie('CellProcessing_tissue_processing'),
                   model_uri=AK_SCHEMA.CellProcessing_tissue_processing, domain=None, range=str)

slots.CellProcessing_cell_subset = Slot(uri=AK_SCHEMA.CellProcessing_cell_subset, name="CellProcessing_cell_subset", curie=AK_SCHEMA.curie('CellProcessing_cell_subset'),
                   model_uri=AK_SCHEMA.CellProcessing_cell_subset, domain=None, range=Union[str, "CellSubset"])

slots.CellProcessing_cell_phenotype = Slot(uri=AK_SCHEMA.CellProcessing_cell_phenotype, name="CellProcessing_cell_phenotype", curie=AK_SCHEMA.curie('CellProcessing_cell_phenotype'),
                   model_uri=AK_SCHEMA.CellProcessing_cell_phenotype, domain=None, range=str)

slots.CellProcessing_cell_species = Slot(uri=AK_SCHEMA.CellProcessing_cell_species, name="CellProcessing_cell_species", curie=AK_SCHEMA.curie('CellProcessing_cell_species'),
                   model_uri=AK_SCHEMA.CellProcessing_cell_species, domain=None, range=Optional[Union[str, "CellSpecies"]])

slots.CellProcessing_single_cell = Slot(uri=AK_SCHEMA.CellProcessing_single_cell, name="CellProcessing_single_cell", curie=AK_SCHEMA.curie('CellProcessing_single_cell'),
                   model_uri=AK_SCHEMA.CellProcessing_single_cell, domain=None, range=Union[bool, Bool])

slots.CellProcessing_cell_number = Slot(uri=AK_SCHEMA.CellProcessing_cell_number, name="CellProcessing_cell_number", curie=AK_SCHEMA.curie('CellProcessing_cell_number'),
                   model_uri=AK_SCHEMA.CellProcessing_cell_number, domain=None, range=int)

slots.CellProcessing_cells_per_reaction = Slot(uri=AK_SCHEMA.CellProcessing_cells_per_reaction, name="CellProcessing_cells_per_reaction", curie=AK_SCHEMA.curie('CellProcessing_cells_per_reaction'),
                   model_uri=AK_SCHEMA.CellProcessing_cells_per_reaction, domain=None, range=int)

slots.CellProcessing_cell_storage = Slot(uri=AK_SCHEMA.CellProcessing_cell_storage, name="CellProcessing_cell_storage", curie=AK_SCHEMA.curie('CellProcessing_cell_storage'),
                   model_uri=AK_SCHEMA.CellProcessing_cell_storage, domain=None, range=Union[bool, Bool])

slots.CellProcessing_cell_quality = Slot(uri=AK_SCHEMA.CellProcessing_cell_quality, name="CellProcessing_cell_quality", curie=AK_SCHEMA.curie('CellProcessing_cell_quality'),
                   model_uri=AK_SCHEMA.CellProcessing_cell_quality, domain=None, range=str)

slots.CellProcessing_cell_isolation = Slot(uri=AK_SCHEMA.CellProcessing_cell_isolation, name="CellProcessing_cell_isolation", curie=AK_SCHEMA.curie('CellProcessing_cell_isolation'),
                   model_uri=AK_SCHEMA.CellProcessing_cell_isolation, domain=None, range=str)

slots.CellProcessing_cell_processing_protocol = Slot(uri=AK_SCHEMA.CellProcessing_cell_processing_protocol, name="CellProcessing_cell_processing_protocol", curie=AK_SCHEMA.curie('CellProcessing_cell_processing_protocol'),
                   model_uri=AK_SCHEMA.CellProcessing_cell_processing_protocol, domain=None, range=str)

slots.PCRTarget_pcr_target_locus = Slot(uri=AK_SCHEMA.PCRTarget_pcr_target_locus, name="PCRTarget_pcr_target_locus", curie=AK_SCHEMA.curie('PCRTarget_pcr_target_locus'),
                   model_uri=AK_SCHEMA.PCRTarget_pcr_target_locus, domain=None, range=Union[str, "PcrTargetLocus"])

slots.PCRTarget_forward_pcr_primer_target_location = Slot(uri=AK_SCHEMA.PCRTarget_forward_pcr_primer_target_location, name="PCRTarget_forward_pcr_primer_target_location", curie=AK_SCHEMA.curie('PCRTarget_forward_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.PCRTarget_forward_pcr_primer_target_location, domain=None, range=str)

slots.PCRTarget_reverse_pcr_primer_target_location = Slot(uri=AK_SCHEMA.PCRTarget_reverse_pcr_primer_target_location, name="PCRTarget_reverse_pcr_primer_target_location", curie=AK_SCHEMA.curie('PCRTarget_reverse_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.PCRTarget_reverse_pcr_primer_target_location, domain=None, range=str)

slots.NucleicAcidProcessing_template_class = Slot(uri=AK_SCHEMA.NucleicAcidProcessing_template_class, name="NucleicAcidProcessing_template_class", curie=AK_SCHEMA.curie('NucleicAcidProcessing_template_class'),
                   model_uri=AK_SCHEMA.NucleicAcidProcessing_template_class, domain=None, range=Union[str, "TemplateClass"])

slots.NucleicAcidProcessing_template_quality = Slot(uri=AK_SCHEMA.NucleicAcidProcessing_template_quality, name="NucleicAcidProcessing_template_quality", curie=AK_SCHEMA.curie('NucleicAcidProcessing_template_quality'),
                   model_uri=AK_SCHEMA.NucleicAcidProcessing_template_quality, domain=None, range=str)

slots.NucleicAcidProcessing_template_amount = Slot(uri=AK_SCHEMA.NucleicAcidProcessing_template_amount, name="NucleicAcidProcessing_template_amount", curie=AK_SCHEMA.curie('NucleicAcidProcessing_template_amount'),
                   model_uri=AK_SCHEMA.NucleicAcidProcessing_template_amount, domain=None, range=float)

slots.NucleicAcidProcessing_template_amount_unit = Slot(uri=AK_SCHEMA.NucleicAcidProcessing_template_amount_unit, name="NucleicAcidProcessing_template_amount_unit", curie=AK_SCHEMA.curie('NucleicAcidProcessing_template_amount_unit'),
                   model_uri=AK_SCHEMA.NucleicAcidProcessing_template_amount_unit, domain=None, range=Union[str, "TemplateAmountUnit"])

slots.NucleicAcidProcessing_library_generation_method = Slot(uri=AK_SCHEMA.NucleicAcidProcessing_library_generation_method, name="NucleicAcidProcessing_library_generation_method", curie=AK_SCHEMA.curie('NucleicAcidProcessing_library_generation_method'),
                   model_uri=AK_SCHEMA.NucleicAcidProcessing_library_generation_method, domain=None, range=Union[str, "LibraryGenerationMethod"])

slots.NucleicAcidProcessing_library_generation_protocol = Slot(uri=AK_SCHEMA.NucleicAcidProcessing_library_generation_protocol, name="NucleicAcidProcessing_library_generation_protocol", curie=AK_SCHEMA.curie('NucleicAcidProcessing_library_generation_protocol'),
                   model_uri=AK_SCHEMA.NucleicAcidProcessing_library_generation_protocol, domain=None, range=str)

slots.NucleicAcidProcessing_library_generation_kit_version = Slot(uri=AK_SCHEMA.NucleicAcidProcessing_library_generation_kit_version, name="NucleicAcidProcessing_library_generation_kit_version", curie=AK_SCHEMA.curie('NucleicAcidProcessing_library_generation_kit_version'),
                   model_uri=AK_SCHEMA.NucleicAcidProcessing_library_generation_kit_version, domain=None, range=str)

slots.NucleicAcidProcessing_pcr_target = Slot(uri=AK_SCHEMA.NucleicAcidProcessing_pcr_target, name="NucleicAcidProcessing_pcr_target", curie=AK_SCHEMA.curie('NucleicAcidProcessing_pcr_target'),
                   model_uri=AK_SCHEMA.NucleicAcidProcessing_pcr_target, domain=None, range=Optional[Union[Union[dict, PCRTarget], List[Union[dict, PCRTarget]]]])

slots.NucleicAcidProcessing_complete_sequences = Slot(uri=AK_SCHEMA.NucleicAcidProcessing_complete_sequences, name="NucleicAcidProcessing_complete_sequences", curie=AK_SCHEMA.curie('NucleicAcidProcessing_complete_sequences'),
                   model_uri=AK_SCHEMA.NucleicAcidProcessing_complete_sequences, domain=None, range=Union[str, "CompleteSequences"])

slots.NucleicAcidProcessing_physical_linkage = Slot(uri=AK_SCHEMA.NucleicAcidProcessing_physical_linkage, name="NucleicAcidProcessing_physical_linkage", curie=AK_SCHEMA.curie('NucleicAcidProcessing_physical_linkage'),
                   model_uri=AK_SCHEMA.NucleicAcidProcessing_physical_linkage, domain=None, range=Union[str, "PhysicalLinkage"])

slots.SequencingRun_sequencing_run_id = Slot(uri=AK_SCHEMA.SequencingRun_sequencing_run_id, name="SequencingRun_sequencing_run_id", curie=AK_SCHEMA.curie('SequencingRun_sequencing_run_id'),
                   model_uri=AK_SCHEMA.SequencingRun_sequencing_run_id, domain=None, range=str)

slots.SequencingRun_total_reads_passing_qc_filter = Slot(uri=AK_SCHEMA.SequencingRun_total_reads_passing_qc_filter, name="SequencingRun_total_reads_passing_qc_filter", curie=AK_SCHEMA.curie('SequencingRun_total_reads_passing_qc_filter'),
                   model_uri=AK_SCHEMA.SequencingRun_total_reads_passing_qc_filter, domain=None, range=int)

slots.SequencingRun_sequencing_platform = Slot(uri=AK_SCHEMA.SequencingRun_sequencing_platform, name="SequencingRun_sequencing_platform", curie=AK_SCHEMA.curie('SequencingRun_sequencing_platform'),
                   model_uri=AK_SCHEMA.SequencingRun_sequencing_platform, domain=None, range=str)

slots.SequencingRun_sequencing_facility = Slot(uri=AK_SCHEMA.SequencingRun_sequencing_facility, name="SequencingRun_sequencing_facility", curie=AK_SCHEMA.curie('SequencingRun_sequencing_facility'),
                   model_uri=AK_SCHEMA.SequencingRun_sequencing_facility, domain=None, range=str)

slots.SequencingRun_sequencing_run_date = Slot(uri=AK_SCHEMA.SequencingRun_sequencing_run_date, name="SequencingRun_sequencing_run_date", curie=AK_SCHEMA.curie('SequencingRun_sequencing_run_date'),
                   model_uri=AK_SCHEMA.SequencingRun_sequencing_run_date, domain=None, range=str)

slots.SequencingRun_sequencing_kit = Slot(uri=AK_SCHEMA.SequencingRun_sequencing_kit, name="SequencingRun_sequencing_kit", curie=AK_SCHEMA.curie('SequencingRun_sequencing_kit'),
                   model_uri=AK_SCHEMA.SequencingRun_sequencing_kit, domain=None, range=str)

slots.SequencingRun_sequencing_files = Slot(uri=AK_SCHEMA.SequencingRun_sequencing_files, name="SequencingRun_sequencing_files", curie=AK_SCHEMA.curie('SequencingRun_sequencing_files'),
                   model_uri=AK_SCHEMA.SequencingRun_sequencing_files, domain=None, range=Optional[Union[dict, SequencingData]])

slots.SequencingData_sequencing_data_id = Slot(uri=AK_SCHEMA.SequencingData_sequencing_data_id, name="SequencingData_sequencing_data_id", curie=AK_SCHEMA.curie('SequencingData_sequencing_data_id'),
                   model_uri=AK_SCHEMA.SequencingData_sequencing_data_id, domain=None, range=str)

slots.SequencingData_file_type = Slot(uri=AK_SCHEMA.SequencingData_file_type, name="SequencingData_file_type", curie=AK_SCHEMA.curie('SequencingData_file_type'),
                   model_uri=AK_SCHEMA.SequencingData_file_type, domain=None, range=Union[str, "FileType"])

slots.SequencingData_filename = Slot(uri=AK_SCHEMA.SequencingData_filename, name="SequencingData_filename", curie=AK_SCHEMA.curie('SequencingData_filename'),
                   model_uri=AK_SCHEMA.SequencingData_filename, domain=None, range=str)

slots.SequencingData_read_direction = Slot(uri=AK_SCHEMA.SequencingData_read_direction, name="SequencingData_read_direction", curie=AK_SCHEMA.curie('SequencingData_read_direction'),
                   model_uri=AK_SCHEMA.SequencingData_read_direction, domain=None, range=Union[str, "ReadDirection"])

slots.SequencingData_read_length = Slot(uri=AK_SCHEMA.SequencingData_read_length, name="SequencingData_read_length", curie=AK_SCHEMA.curie('SequencingData_read_length'),
                   model_uri=AK_SCHEMA.SequencingData_read_length, domain=None, range=int)

slots.SequencingData_paired_filename = Slot(uri=AK_SCHEMA.SequencingData_paired_filename, name="SequencingData_paired_filename", curie=AK_SCHEMA.curie('SequencingData_paired_filename'),
                   model_uri=AK_SCHEMA.SequencingData_paired_filename, domain=None, range=str)

slots.SequencingData_paired_read_direction = Slot(uri=AK_SCHEMA.SequencingData_paired_read_direction, name="SequencingData_paired_read_direction", curie=AK_SCHEMA.curie('SequencingData_paired_read_direction'),
                   model_uri=AK_SCHEMA.SequencingData_paired_read_direction, domain=None, range=Union[str, "PairedReadDirection"])

slots.SequencingData_paired_read_length = Slot(uri=AK_SCHEMA.SequencingData_paired_read_length, name="SequencingData_paired_read_length", curie=AK_SCHEMA.curie('SequencingData_paired_read_length'),
                   model_uri=AK_SCHEMA.SequencingData_paired_read_length, domain=None, range=int)

slots.SequencingData_index_filename = Slot(uri=AK_SCHEMA.SequencingData_index_filename, name="SequencingData_index_filename", curie=AK_SCHEMA.curie('SequencingData_index_filename'),
                   model_uri=AK_SCHEMA.SequencingData_index_filename, domain=None, range=Optional[str])

slots.SequencingData_index_length = Slot(uri=AK_SCHEMA.SequencingData_index_length, name="SequencingData_index_length", curie=AK_SCHEMA.curie('SequencingData_index_length'),
                   model_uri=AK_SCHEMA.SequencingData_index_length, domain=None, range=Optional[int])

slots.DataProcessing_data_processing_id = Slot(uri=AK_SCHEMA.DataProcessing_data_processing_id, name="DataProcessing_data_processing_id", curie=AK_SCHEMA.curie('DataProcessing_data_processing_id'),
                   model_uri=AK_SCHEMA.DataProcessing_data_processing_id, domain=None, range=Optional[str])

slots.DataProcessing_primary_annotation = Slot(uri=AK_SCHEMA.DataProcessing_primary_annotation, name="DataProcessing_primary_annotation", curie=AK_SCHEMA.curie('DataProcessing_primary_annotation'),
                   model_uri=AK_SCHEMA.DataProcessing_primary_annotation, domain=None, range=Optional[Union[bool, Bool]])

slots.DataProcessing_software_versions = Slot(uri=AK_SCHEMA.DataProcessing_software_versions, name="DataProcessing_software_versions", curie=AK_SCHEMA.curie('DataProcessing_software_versions'),
                   model_uri=AK_SCHEMA.DataProcessing_software_versions, domain=None, range=str)

slots.DataProcessing_paired_reads_assembly = Slot(uri=AK_SCHEMA.DataProcessing_paired_reads_assembly, name="DataProcessing_paired_reads_assembly", curie=AK_SCHEMA.curie('DataProcessing_paired_reads_assembly'),
                   model_uri=AK_SCHEMA.DataProcessing_paired_reads_assembly, domain=None, range=str)

slots.DataProcessing_quality_thresholds = Slot(uri=AK_SCHEMA.DataProcessing_quality_thresholds, name="DataProcessing_quality_thresholds", curie=AK_SCHEMA.curie('DataProcessing_quality_thresholds'),
                   model_uri=AK_SCHEMA.DataProcessing_quality_thresholds, domain=None, range=str)

slots.DataProcessing_primer_match_cutoffs = Slot(uri=AK_SCHEMA.DataProcessing_primer_match_cutoffs, name="DataProcessing_primer_match_cutoffs", curie=AK_SCHEMA.curie('DataProcessing_primer_match_cutoffs'),
                   model_uri=AK_SCHEMA.DataProcessing_primer_match_cutoffs, domain=None, range=str)

slots.DataProcessing_collapsing_method = Slot(uri=AK_SCHEMA.DataProcessing_collapsing_method, name="DataProcessing_collapsing_method", curie=AK_SCHEMA.curie('DataProcessing_collapsing_method'),
                   model_uri=AK_SCHEMA.DataProcessing_collapsing_method, domain=None, range=str)

slots.DataProcessing_data_processing_protocols = Slot(uri=AK_SCHEMA.DataProcessing_data_processing_protocols, name="DataProcessing_data_processing_protocols", curie=AK_SCHEMA.curie('DataProcessing_data_processing_protocols'),
                   model_uri=AK_SCHEMA.DataProcessing_data_processing_protocols, domain=None, range=str)

slots.DataProcessing_data_processing_files = Slot(uri=AK_SCHEMA.DataProcessing_data_processing_files, name="DataProcessing_data_processing_files", curie=AK_SCHEMA.curie('DataProcessing_data_processing_files'),
                   model_uri=AK_SCHEMA.DataProcessing_data_processing_files, domain=None, range=Optional[Union[str, List[str]]])

slots.DataProcessing_germline_database = Slot(uri=AK_SCHEMA.DataProcessing_germline_database, name="DataProcessing_germline_database", curie=AK_SCHEMA.curie('DataProcessing_germline_database'),
                   model_uri=AK_SCHEMA.DataProcessing_germline_database, domain=None, range=str)

slots.DataProcessing_germline_set_ref = Slot(uri=AK_SCHEMA.DataProcessing_germline_set_ref, name="DataProcessing_germline_set_ref", curie=AK_SCHEMA.curie('DataProcessing_germline_set_ref'),
                   model_uri=AK_SCHEMA.DataProcessing_germline_set_ref, domain=None, range=Optional[str])

slots.DataProcessing_analysis_provenance_id = Slot(uri=AK_SCHEMA.DataProcessing_analysis_provenance_id, name="DataProcessing_analysis_provenance_id", curie=AK_SCHEMA.curie('DataProcessing_analysis_provenance_id'),
                   model_uri=AK_SCHEMA.DataProcessing_analysis_provenance_id, domain=None, range=Optional[str])

slots.Repertoire_repertoire_id = Slot(uri=AK_SCHEMA.Repertoire_repertoire_id, name="Repertoire_repertoire_id", curie=AK_SCHEMA.curie('Repertoire_repertoire_id'),
                   model_uri=AK_SCHEMA.Repertoire_repertoire_id, domain=None, range=Optional[str])

slots.Repertoire_repertoire_name = Slot(uri=AK_SCHEMA.Repertoire_repertoire_name, name="Repertoire_repertoire_name", curie=AK_SCHEMA.curie('Repertoire_repertoire_name'),
                   model_uri=AK_SCHEMA.Repertoire_repertoire_name, domain=None, range=Optional[str])

slots.Repertoire_repertoire_description = Slot(uri=AK_SCHEMA.Repertoire_repertoire_description, name="Repertoire_repertoire_description", curie=AK_SCHEMA.curie('Repertoire_repertoire_description'),
                   model_uri=AK_SCHEMA.Repertoire_repertoire_description, domain=None, range=Optional[str])

slots.Repertoire_study = Slot(uri=AK_SCHEMA.Repertoire_study, name="Repertoire_study", curie=AK_SCHEMA.curie('Repertoire_study'),
                   model_uri=AK_SCHEMA.Repertoire_study, domain=None, range=Union[dict, Study])

slots.Repertoire_subject = Slot(uri=AK_SCHEMA.Repertoire_subject, name="Repertoire_subject", curie=AK_SCHEMA.curie('Repertoire_subject'),
                   model_uri=AK_SCHEMA.Repertoire_subject, domain=None, range=Union[dict, Subject])

slots.Repertoire_sample = Slot(uri=AK_SCHEMA.Repertoire_sample, name="Repertoire_sample", curie=AK_SCHEMA.curie('Repertoire_sample'),
                   model_uri=AK_SCHEMA.Repertoire_sample, domain=None, range=Union[Union[dict, SampleProcessing], List[Union[dict, SampleProcessing]]])

slots.Repertoire_data_processing = Slot(uri=AK_SCHEMA.Repertoire_data_processing, name="Repertoire_data_processing", curie=AK_SCHEMA.curie('Repertoire_data_processing'),
                   model_uri=AK_SCHEMA.Repertoire_data_processing, domain=None, range=Union[Union[dict, DataProcessing], List[Union[dict, DataProcessing]]])

slots.RepertoireGroup_repertoire_group_id = Slot(uri=AK_SCHEMA.RepertoireGroup_repertoire_group_id, name="RepertoireGroup_repertoire_group_id", curie=AK_SCHEMA.curie('RepertoireGroup_repertoire_group_id'),
                   model_uri=AK_SCHEMA.RepertoireGroup_repertoire_group_id, domain=None, range=str)

slots.RepertoireGroup_repertoire_group_name = Slot(uri=AK_SCHEMA.RepertoireGroup_repertoire_group_name, name="RepertoireGroup_repertoire_group_name", curie=AK_SCHEMA.curie('RepertoireGroup_repertoire_group_name'),
                   model_uri=AK_SCHEMA.RepertoireGroup_repertoire_group_name, domain=None, range=Optional[str])

slots.RepertoireGroup_repertoire_group_description = Slot(uri=AK_SCHEMA.RepertoireGroup_repertoire_group_description, name="RepertoireGroup_repertoire_group_description", curie=AK_SCHEMA.curie('RepertoireGroup_repertoire_group_description'),
                   model_uri=AK_SCHEMA.RepertoireGroup_repertoire_group_description, domain=None, range=Optional[str])

slots.RepertoireGroup_repertoires = Slot(uri=AK_SCHEMA.RepertoireGroup_repertoires, name="RepertoireGroup_repertoires", curie=AK_SCHEMA.curie('RepertoireGroup_repertoires'),
                   model_uri=AK_SCHEMA.RepertoireGroup_repertoires, domain=None, range=Union[str, List[str]])

slots.Alignment_sequence_id = Slot(uri=AK_SCHEMA.Alignment_sequence_id, name="Alignment_sequence_id", curie=AK_SCHEMA.curie('Alignment_sequence_id'),
                   model_uri=AK_SCHEMA.Alignment_sequence_id, domain=None, range=str)

slots.Alignment_segment = Slot(uri=AK_SCHEMA.Alignment_segment, name="Alignment_segment", curie=AK_SCHEMA.curie('Alignment_segment'),
                   model_uri=AK_SCHEMA.Alignment_segment, domain=None, range=str)

slots.Alignment_rev_comp = Slot(uri=AK_SCHEMA.Alignment_rev_comp, name="Alignment_rev_comp", curie=AK_SCHEMA.curie('Alignment_rev_comp'),
                   model_uri=AK_SCHEMA.Alignment_rev_comp, domain=None, range=Optional[Union[bool, Bool]])

slots.Alignment_call = Slot(uri=AK_SCHEMA.Alignment_call, name="Alignment_call", curie=AK_SCHEMA.curie('Alignment_call'),
                   model_uri=AK_SCHEMA.Alignment_call, domain=None, range=str)

slots.Alignment_score = Slot(uri=AK_SCHEMA.Alignment_score, name="Alignment_score", curie=AK_SCHEMA.curie('Alignment_score'),
                   model_uri=AK_SCHEMA.Alignment_score, domain=None, range=float)

slots.Alignment_identity = Slot(uri=AK_SCHEMA.Alignment_identity, name="Alignment_identity", curie=AK_SCHEMA.curie('Alignment_identity'),
                   model_uri=AK_SCHEMA.Alignment_identity, domain=None, range=Optional[float])

slots.Alignment_support = Slot(uri=AK_SCHEMA.Alignment_support, name="Alignment_support", curie=AK_SCHEMA.curie('Alignment_support'),
                   model_uri=AK_SCHEMA.Alignment_support, domain=None, range=Optional[float])

slots.Alignment_cigar = Slot(uri=AK_SCHEMA.Alignment_cigar, name="Alignment_cigar", curie=AK_SCHEMA.curie('Alignment_cigar'),
                   model_uri=AK_SCHEMA.Alignment_cigar, domain=None, range=str)

slots.Alignment_sequence_start = Slot(uri=AK_SCHEMA.Alignment_sequence_start, name="Alignment_sequence_start", curie=AK_SCHEMA.curie('Alignment_sequence_start'),
                   model_uri=AK_SCHEMA.Alignment_sequence_start, domain=None, range=Optional[int])

slots.Alignment_sequence_end = Slot(uri=AK_SCHEMA.Alignment_sequence_end, name="Alignment_sequence_end", curie=AK_SCHEMA.curie('Alignment_sequence_end'),
                   model_uri=AK_SCHEMA.Alignment_sequence_end, domain=None, range=Optional[int])

slots.Alignment_germline_start = Slot(uri=AK_SCHEMA.Alignment_germline_start, name="Alignment_germline_start", curie=AK_SCHEMA.curie('Alignment_germline_start'),
                   model_uri=AK_SCHEMA.Alignment_germline_start, domain=None, range=Optional[int])

slots.Alignment_germline_end = Slot(uri=AK_SCHEMA.Alignment_germline_end, name="Alignment_germline_end", curie=AK_SCHEMA.curie('Alignment_germline_end'),
                   model_uri=AK_SCHEMA.Alignment_germline_end, domain=None, range=Optional[int])

slots.Alignment_rank = Slot(uri=AK_SCHEMA.Alignment_rank, name="Alignment_rank", curie=AK_SCHEMA.curie('Alignment_rank'),
                   model_uri=AK_SCHEMA.Alignment_rank, domain=None, range=Optional[int])

slots.Alignment_data_processing_id = Slot(uri=AK_SCHEMA.Alignment_data_processing_id, name="Alignment_data_processing_id", curie=AK_SCHEMA.curie('Alignment_data_processing_id'),
                   model_uri=AK_SCHEMA.Alignment_data_processing_id, domain=None, range=Optional[str])

slots.Rearrangement_sequence_id = Slot(uri=AK_SCHEMA.Rearrangement_sequence_id, name="Rearrangement_sequence_id", curie=AK_SCHEMA.curie('Rearrangement_sequence_id'),
                   model_uri=AK_SCHEMA.Rearrangement_sequence_id, domain=None, range=str)

slots.Rearrangement_sequence = Slot(uri=AK_SCHEMA.Rearrangement_sequence, name="Rearrangement_sequence", curie=AK_SCHEMA.curie('Rearrangement_sequence'),
                   model_uri=AK_SCHEMA.Rearrangement_sequence, domain=None, range=str)

slots.Rearrangement_quality = Slot(uri=AK_SCHEMA.Rearrangement_quality, name="Rearrangement_quality", curie=AK_SCHEMA.curie('Rearrangement_quality'),
                   model_uri=AK_SCHEMA.Rearrangement_quality, domain=None, range=Optional[str])

slots.Rearrangement_sequence_aa = Slot(uri=AK_SCHEMA.Rearrangement_sequence_aa, name="Rearrangement_sequence_aa", curie=AK_SCHEMA.curie('Rearrangement_sequence_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_sequence_aa, domain=None, range=Optional[str])

slots.Rearrangement_rev_comp = Slot(uri=AK_SCHEMA.Rearrangement_rev_comp, name="Rearrangement_rev_comp", curie=AK_SCHEMA.curie('Rearrangement_rev_comp'),
                   model_uri=AK_SCHEMA.Rearrangement_rev_comp, domain=None, range=Union[bool, Bool])

slots.Rearrangement_productive = Slot(uri=AK_SCHEMA.Rearrangement_productive, name="Rearrangement_productive", curie=AK_SCHEMA.curie('Rearrangement_productive'),
                   model_uri=AK_SCHEMA.Rearrangement_productive, domain=None, range=Union[bool, Bool])

slots.Rearrangement_vj_in_frame = Slot(uri=AK_SCHEMA.Rearrangement_vj_in_frame, name="Rearrangement_vj_in_frame", curie=AK_SCHEMA.curie('Rearrangement_vj_in_frame'),
                   model_uri=AK_SCHEMA.Rearrangement_vj_in_frame, domain=None, range=Optional[Union[bool, Bool]])

slots.Rearrangement_stop_codon = Slot(uri=AK_SCHEMA.Rearrangement_stop_codon, name="Rearrangement_stop_codon", curie=AK_SCHEMA.curie('Rearrangement_stop_codon'),
                   model_uri=AK_SCHEMA.Rearrangement_stop_codon, domain=None, range=Optional[Union[bool, Bool]])

slots.Rearrangement_complete_vdj = Slot(uri=AK_SCHEMA.Rearrangement_complete_vdj, name="Rearrangement_complete_vdj", curie=AK_SCHEMA.curie('Rearrangement_complete_vdj'),
                   model_uri=AK_SCHEMA.Rearrangement_complete_vdj, domain=None, range=Optional[Union[bool, Bool]])

slots.Rearrangement_locus = Slot(uri=AK_SCHEMA.Rearrangement_locus, name="Rearrangement_locus", curie=AK_SCHEMA.curie('Rearrangement_locus'),
                   model_uri=AK_SCHEMA.Rearrangement_locus, domain=None, range=Optional[Union[str, "Locus"]])

slots.Rearrangement_v_call = Slot(uri=AK_SCHEMA.Rearrangement_v_call, name="Rearrangement_v_call", curie=AK_SCHEMA.curie('Rearrangement_v_call'),
                   model_uri=AK_SCHEMA.Rearrangement_v_call, domain=None, range=str)

slots.Rearrangement_d_call = Slot(uri=AK_SCHEMA.Rearrangement_d_call, name="Rearrangement_d_call", curie=AK_SCHEMA.curie('Rearrangement_d_call'),
                   model_uri=AK_SCHEMA.Rearrangement_d_call, domain=None, range=str)

slots.Rearrangement_d2_call = Slot(uri=AK_SCHEMA.Rearrangement_d2_call, name="Rearrangement_d2_call", curie=AK_SCHEMA.curie('Rearrangement_d2_call'),
                   model_uri=AK_SCHEMA.Rearrangement_d2_call, domain=None, range=Optional[str])

slots.Rearrangement_j_call = Slot(uri=AK_SCHEMA.Rearrangement_j_call, name="Rearrangement_j_call", curie=AK_SCHEMA.curie('Rearrangement_j_call'),
                   model_uri=AK_SCHEMA.Rearrangement_j_call, domain=None, range=str)

slots.Rearrangement_c_call = Slot(uri=AK_SCHEMA.Rearrangement_c_call, name="Rearrangement_c_call", curie=AK_SCHEMA.curie('Rearrangement_c_call'),
                   model_uri=AK_SCHEMA.Rearrangement_c_call, domain=None, range=Optional[str])

slots.Rearrangement_sequence_alignment = Slot(uri=AK_SCHEMA.Rearrangement_sequence_alignment, name="Rearrangement_sequence_alignment", curie=AK_SCHEMA.curie('Rearrangement_sequence_alignment'),
                   model_uri=AK_SCHEMA.Rearrangement_sequence_alignment, domain=None, range=str)

slots.Rearrangement_quality_alignment = Slot(uri=AK_SCHEMA.Rearrangement_quality_alignment, name="Rearrangement_quality_alignment", curie=AK_SCHEMA.curie('Rearrangement_quality_alignment'),
                   model_uri=AK_SCHEMA.Rearrangement_quality_alignment, domain=None, range=Optional[str])

slots.Rearrangement_sequence_alignment_aa = Slot(uri=AK_SCHEMA.Rearrangement_sequence_alignment_aa, name="Rearrangement_sequence_alignment_aa", curie=AK_SCHEMA.curie('Rearrangement_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_sequence_alignment_aa, domain=None, range=Optional[str])

slots.Rearrangement_germline_alignment = Slot(uri=AK_SCHEMA.Rearrangement_germline_alignment, name="Rearrangement_germline_alignment", curie=AK_SCHEMA.curie('Rearrangement_germline_alignment'),
                   model_uri=AK_SCHEMA.Rearrangement_germline_alignment, domain=None, range=str)

slots.Rearrangement_germline_alignment_aa = Slot(uri=AK_SCHEMA.Rearrangement_germline_alignment_aa, name="Rearrangement_germline_alignment_aa", curie=AK_SCHEMA.curie('Rearrangement_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_germline_alignment_aa, domain=None, range=Optional[str])

slots.Rearrangement_junction = Slot(uri=AK_SCHEMA.Rearrangement_junction, name="Rearrangement_junction", curie=AK_SCHEMA.curie('Rearrangement_junction'),
                   model_uri=AK_SCHEMA.Rearrangement_junction, domain=None, range=str)

slots.Rearrangement_junction_aa = Slot(uri=AK_SCHEMA.Rearrangement_junction_aa, name="Rearrangement_junction_aa", curie=AK_SCHEMA.curie('Rearrangement_junction_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_junction_aa, domain=None, range=str)

slots.Rearrangement_np1 = Slot(uri=AK_SCHEMA.Rearrangement_np1, name="Rearrangement_np1", curie=AK_SCHEMA.curie('Rearrangement_np1'),
                   model_uri=AK_SCHEMA.Rearrangement_np1, domain=None, range=Optional[str])

slots.Rearrangement_np1_aa = Slot(uri=AK_SCHEMA.Rearrangement_np1_aa, name="Rearrangement_np1_aa", curie=AK_SCHEMA.curie('Rearrangement_np1_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_np1_aa, domain=None, range=Optional[str])

slots.Rearrangement_np2 = Slot(uri=AK_SCHEMA.Rearrangement_np2, name="Rearrangement_np2", curie=AK_SCHEMA.curie('Rearrangement_np2'),
                   model_uri=AK_SCHEMA.Rearrangement_np2, domain=None, range=Optional[str])

slots.Rearrangement_np2_aa = Slot(uri=AK_SCHEMA.Rearrangement_np2_aa, name="Rearrangement_np2_aa", curie=AK_SCHEMA.curie('Rearrangement_np2_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_np2_aa, domain=None, range=Optional[str])

slots.Rearrangement_np3 = Slot(uri=AK_SCHEMA.Rearrangement_np3, name="Rearrangement_np3", curie=AK_SCHEMA.curie('Rearrangement_np3'),
                   model_uri=AK_SCHEMA.Rearrangement_np3, domain=None, range=Optional[str])

slots.Rearrangement_np3_aa = Slot(uri=AK_SCHEMA.Rearrangement_np3_aa, name="Rearrangement_np3_aa", curie=AK_SCHEMA.curie('Rearrangement_np3_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_np3_aa, domain=None, range=Optional[str])

slots.Rearrangement_cdr1 = Slot(uri=AK_SCHEMA.Rearrangement_cdr1, name="Rearrangement_cdr1", curie=AK_SCHEMA.curie('Rearrangement_cdr1'),
                   model_uri=AK_SCHEMA.Rearrangement_cdr1, domain=None, range=Optional[str])

slots.Rearrangement_cdr1_aa = Slot(uri=AK_SCHEMA.Rearrangement_cdr1_aa, name="Rearrangement_cdr1_aa", curie=AK_SCHEMA.curie('Rearrangement_cdr1_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_cdr1_aa, domain=None, range=Optional[str])

slots.Rearrangement_cdr2 = Slot(uri=AK_SCHEMA.Rearrangement_cdr2, name="Rearrangement_cdr2", curie=AK_SCHEMA.curie('Rearrangement_cdr2'),
                   model_uri=AK_SCHEMA.Rearrangement_cdr2, domain=None, range=Optional[str])

slots.Rearrangement_cdr2_aa = Slot(uri=AK_SCHEMA.Rearrangement_cdr2_aa, name="Rearrangement_cdr2_aa", curie=AK_SCHEMA.curie('Rearrangement_cdr2_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_cdr2_aa, domain=None, range=Optional[str])

slots.Rearrangement_cdr3 = Slot(uri=AK_SCHEMA.Rearrangement_cdr3, name="Rearrangement_cdr3", curie=AK_SCHEMA.curie('Rearrangement_cdr3'),
                   model_uri=AK_SCHEMA.Rearrangement_cdr3, domain=None, range=Optional[str])

slots.Rearrangement_cdr3_aa = Slot(uri=AK_SCHEMA.Rearrangement_cdr3_aa, name="Rearrangement_cdr3_aa", curie=AK_SCHEMA.curie('Rearrangement_cdr3_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_cdr3_aa, domain=None, range=Optional[str])

slots.Rearrangement_fwr1 = Slot(uri=AK_SCHEMA.Rearrangement_fwr1, name="Rearrangement_fwr1", curie=AK_SCHEMA.curie('Rearrangement_fwr1'),
                   model_uri=AK_SCHEMA.Rearrangement_fwr1, domain=None, range=Optional[str])

slots.Rearrangement_fwr1_aa = Slot(uri=AK_SCHEMA.Rearrangement_fwr1_aa, name="Rearrangement_fwr1_aa", curie=AK_SCHEMA.curie('Rearrangement_fwr1_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_fwr1_aa, domain=None, range=Optional[str])

slots.Rearrangement_fwr2 = Slot(uri=AK_SCHEMA.Rearrangement_fwr2, name="Rearrangement_fwr2", curie=AK_SCHEMA.curie('Rearrangement_fwr2'),
                   model_uri=AK_SCHEMA.Rearrangement_fwr2, domain=None, range=Optional[str])

slots.Rearrangement_fwr2_aa = Slot(uri=AK_SCHEMA.Rearrangement_fwr2_aa, name="Rearrangement_fwr2_aa", curie=AK_SCHEMA.curie('Rearrangement_fwr2_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_fwr2_aa, domain=None, range=Optional[str])

slots.Rearrangement_fwr3 = Slot(uri=AK_SCHEMA.Rearrangement_fwr3, name="Rearrangement_fwr3", curie=AK_SCHEMA.curie('Rearrangement_fwr3'),
                   model_uri=AK_SCHEMA.Rearrangement_fwr3, domain=None, range=Optional[str])

slots.Rearrangement_fwr3_aa = Slot(uri=AK_SCHEMA.Rearrangement_fwr3_aa, name="Rearrangement_fwr3_aa", curie=AK_SCHEMA.curie('Rearrangement_fwr3_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_fwr3_aa, domain=None, range=Optional[str])

slots.Rearrangement_fwr4 = Slot(uri=AK_SCHEMA.Rearrangement_fwr4, name="Rearrangement_fwr4", curie=AK_SCHEMA.curie('Rearrangement_fwr4'),
                   model_uri=AK_SCHEMA.Rearrangement_fwr4, domain=None, range=Optional[str])

slots.Rearrangement_fwr4_aa = Slot(uri=AK_SCHEMA.Rearrangement_fwr4_aa, name="Rearrangement_fwr4_aa", curie=AK_SCHEMA.curie('Rearrangement_fwr4_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_fwr4_aa, domain=None, range=Optional[str])

slots.Rearrangement_v_score = Slot(uri=AK_SCHEMA.Rearrangement_v_score, name="Rearrangement_v_score", curie=AK_SCHEMA.curie('Rearrangement_v_score'),
                   model_uri=AK_SCHEMA.Rearrangement_v_score, domain=None, range=Optional[float])

slots.Rearrangement_v_identity = Slot(uri=AK_SCHEMA.Rearrangement_v_identity, name="Rearrangement_v_identity", curie=AK_SCHEMA.curie('Rearrangement_v_identity'),
                   model_uri=AK_SCHEMA.Rearrangement_v_identity, domain=None, range=Optional[float])

slots.Rearrangement_v_support = Slot(uri=AK_SCHEMA.Rearrangement_v_support, name="Rearrangement_v_support", curie=AK_SCHEMA.curie('Rearrangement_v_support'),
                   model_uri=AK_SCHEMA.Rearrangement_v_support, domain=None, range=Optional[float])

slots.Rearrangement_v_cigar = Slot(uri=AK_SCHEMA.Rearrangement_v_cigar, name="Rearrangement_v_cigar", curie=AK_SCHEMA.curie('Rearrangement_v_cigar'),
                   model_uri=AK_SCHEMA.Rearrangement_v_cigar, domain=None, range=str)

slots.Rearrangement_d_score = Slot(uri=AK_SCHEMA.Rearrangement_d_score, name="Rearrangement_d_score", curie=AK_SCHEMA.curie('Rearrangement_d_score'),
                   model_uri=AK_SCHEMA.Rearrangement_d_score, domain=None, range=Optional[float])

slots.Rearrangement_d_identity = Slot(uri=AK_SCHEMA.Rearrangement_d_identity, name="Rearrangement_d_identity", curie=AK_SCHEMA.curie('Rearrangement_d_identity'),
                   model_uri=AK_SCHEMA.Rearrangement_d_identity, domain=None, range=Optional[float])

slots.Rearrangement_d_support = Slot(uri=AK_SCHEMA.Rearrangement_d_support, name="Rearrangement_d_support", curie=AK_SCHEMA.curie('Rearrangement_d_support'),
                   model_uri=AK_SCHEMA.Rearrangement_d_support, domain=None, range=Optional[float])

slots.Rearrangement_d_cigar = Slot(uri=AK_SCHEMA.Rearrangement_d_cigar, name="Rearrangement_d_cigar", curie=AK_SCHEMA.curie('Rearrangement_d_cigar'),
                   model_uri=AK_SCHEMA.Rearrangement_d_cigar, domain=None, range=str)

slots.Rearrangement_d2_score = Slot(uri=AK_SCHEMA.Rearrangement_d2_score, name="Rearrangement_d2_score", curie=AK_SCHEMA.curie('Rearrangement_d2_score'),
                   model_uri=AK_SCHEMA.Rearrangement_d2_score, domain=None, range=Optional[float])

slots.Rearrangement_d2_identity = Slot(uri=AK_SCHEMA.Rearrangement_d2_identity, name="Rearrangement_d2_identity", curie=AK_SCHEMA.curie('Rearrangement_d2_identity'),
                   model_uri=AK_SCHEMA.Rearrangement_d2_identity, domain=None, range=Optional[float])

slots.Rearrangement_d2_support = Slot(uri=AK_SCHEMA.Rearrangement_d2_support, name="Rearrangement_d2_support", curie=AK_SCHEMA.curie('Rearrangement_d2_support'),
                   model_uri=AK_SCHEMA.Rearrangement_d2_support, domain=None, range=Optional[float])

slots.Rearrangement_d2_cigar = Slot(uri=AK_SCHEMA.Rearrangement_d2_cigar, name="Rearrangement_d2_cigar", curie=AK_SCHEMA.curie('Rearrangement_d2_cigar'),
                   model_uri=AK_SCHEMA.Rearrangement_d2_cigar, domain=None, range=Optional[str])

slots.Rearrangement_j_score = Slot(uri=AK_SCHEMA.Rearrangement_j_score, name="Rearrangement_j_score", curie=AK_SCHEMA.curie('Rearrangement_j_score'),
                   model_uri=AK_SCHEMA.Rearrangement_j_score, domain=None, range=Optional[float])

slots.Rearrangement_j_identity = Slot(uri=AK_SCHEMA.Rearrangement_j_identity, name="Rearrangement_j_identity", curie=AK_SCHEMA.curie('Rearrangement_j_identity'),
                   model_uri=AK_SCHEMA.Rearrangement_j_identity, domain=None, range=Optional[float])

slots.Rearrangement_j_support = Slot(uri=AK_SCHEMA.Rearrangement_j_support, name="Rearrangement_j_support", curie=AK_SCHEMA.curie('Rearrangement_j_support'),
                   model_uri=AK_SCHEMA.Rearrangement_j_support, domain=None, range=Optional[float])

slots.Rearrangement_j_cigar = Slot(uri=AK_SCHEMA.Rearrangement_j_cigar, name="Rearrangement_j_cigar", curie=AK_SCHEMA.curie('Rearrangement_j_cigar'),
                   model_uri=AK_SCHEMA.Rearrangement_j_cigar, domain=None, range=str)

slots.Rearrangement_c_score = Slot(uri=AK_SCHEMA.Rearrangement_c_score, name="Rearrangement_c_score", curie=AK_SCHEMA.curie('Rearrangement_c_score'),
                   model_uri=AK_SCHEMA.Rearrangement_c_score, domain=None, range=Optional[float])

slots.Rearrangement_c_identity = Slot(uri=AK_SCHEMA.Rearrangement_c_identity, name="Rearrangement_c_identity", curie=AK_SCHEMA.curie('Rearrangement_c_identity'),
                   model_uri=AK_SCHEMA.Rearrangement_c_identity, domain=None, range=Optional[float])

slots.Rearrangement_c_support = Slot(uri=AK_SCHEMA.Rearrangement_c_support, name="Rearrangement_c_support", curie=AK_SCHEMA.curie('Rearrangement_c_support'),
                   model_uri=AK_SCHEMA.Rearrangement_c_support, domain=None, range=Optional[float])

slots.Rearrangement_c_cigar = Slot(uri=AK_SCHEMA.Rearrangement_c_cigar, name="Rearrangement_c_cigar", curie=AK_SCHEMA.curie('Rearrangement_c_cigar'),
                   model_uri=AK_SCHEMA.Rearrangement_c_cigar, domain=None, range=Optional[str])

slots.Rearrangement_v_sequence_start = Slot(uri=AK_SCHEMA.Rearrangement_v_sequence_start, name="Rearrangement_v_sequence_start", curie=AK_SCHEMA.curie('Rearrangement_v_sequence_start'),
                   model_uri=AK_SCHEMA.Rearrangement_v_sequence_start, domain=None, range=Optional[int])

slots.Rearrangement_v_sequence_end = Slot(uri=AK_SCHEMA.Rearrangement_v_sequence_end, name="Rearrangement_v_sequence_end", curie=AK_SCHEMA.curie('Rearrangement_v_sequence_end'),
                   model_uri=AK_SCHEMA.Rearrangement_v_sequence_end, domain=None, range=Optional[int])

slots.Rearrangement_v_germline_start = Slot(uri=AK_SCHEMA.Rearrangement_v_germline_start, name="Rearrangement_v_germline_start", curie=AK_SCHEMA.curie('Rearrangement_v_germline_start'),
                   model_uri=AK_SCHEMA.Rearrangement_v_germline_start, domain=None, range=Optional[int])

slots.Rearrangement_v_germline_end = Slot(uri=AK_SCHEMA.Rearrangement_v_germline_end, name="Rearrangement_v_germline_end", curie=AK_SCHEMA.curie('Rearrangement_v_germline_end'),
                   model_uri=AK_SCHEMA.Rearrangement_v_germline_end, domain=None, range=Optional[int])

slots.Rearrangement_v_alignment_start = Slot(uri=AK_SCHEMA.Rearrangement_v_alignment_start, name="Rearrangement_v_alignment_start", curie=AK_SCHEMA.curie('Rearrangement_v_alignment_start'),
                   model_uri=AK_SCHEMA.Rearrangement_v_alignment_start, domain=None, range=Optional[int])

slots.Rearrangement_v_alignment_end = Slot(uri=AK_SCHEMA.Rearrangement_v_alignment_end, name="Rearrangement_v_alignment_end", curie=AK_SCHEMA.curie('Rearrangement_v_alignment_end'),
                   model_uri=AK_SCHEMA.Rearrangement_v_alignment_end, domain=None, range=Optional[int])

slots.Rearrangement_d_sequence_start = Slot(uri=AK_SCHEMA.Rearrangement_d_sequence_start, name="Rearrangement_d_sequence_start", curie=AK_SCHEMA.curie('Rearrangement_d_sequence_start'),
                   model_uri=AK_SCHEMA.Rearrangement_d_sequence_start, domain=None, range=Optional[int])

slots.Rearrangement_d_sequence_end = Slot(uri=AK_SCHEMA.Rearrangement_d_sequence_end, name="Rearrangement_d_sequence_end", curie=AK_SCHEMA.curie('Rearrangement_d_sequence_end'),
                   model_uri=AK_SCHEMA.Rearrangement_d_sequence_end, domain=None, range=Optional[int])

slots.Rearrangement_d_germline_start = Slot(uri=AK_SCHEMA.Rearrangement_d_germline_start, name="Rearrangement_d_germline_start", curie=AK_SCHEMA.curie('Rearrangement_d_germline_start'),
                   model_uri=AK_SCHEMA.Rearrangement_d_germline_start, domain=None, range=Optional[int])

slots.Rearrangement_d_germline_end = Slot(uri=AK_SCHEMA.Rearrangement_d_germline_end, name="Rearrangement_d_germline_end", curie=AK_SCHEMA.curie('Rearrangement_d_germline_end'),
                   model_uri=AK_SCHEMA.Rearrangement_d_germline_end, domain=None, range=Optional[int])

slots.Rearrangement_d_alignment_start = Slot(uri=AK_SCHEMA.Rearrangement_d_alignment_start, name="Rearrangement_d_alignment_start", curie=AK_SCHEMA.curie('Rearrangement_d_alignment_start'),
                   model_uri=AK_SCHEMA.Rearrangement_d_alignment_start, domain=None, range=Optional[int])

slots.Rearrangement_d_alignment_end = Slot(uri=AK_SCHEMA.Rearrangement_d_alignment_end, name="Rearrangement_d_alignment_end", curie=AK_SCHEMA.curie('Rearrangement_d_alignment_end'),
                   model_uri=AK_SCHEMA.Rearrangement_d_alignment_end, domain=None, range=Optional[int])

slots.Rearrangement_d2_sequence_start = Slot(uri=AK_SCHEMA.Rearrangement_d2_sequence_start, name="Rearrangement_d2_sequence_start", curie=AK_SCHEMA.curie('Rearrangement_d2_sequence_start'),
                   model_uri=AK_SCHEMA.Rearrangement_d2_sequence_start, domain=None, range=Optional[int])

slots.Rearrangement_d2_sequence_end = Slot(uri=AK_SCHEMA.Rearrangement_d2_sequence_end, name="Rearrangement_d2_sequence_end", curie=AK_SCHEMA.curie('Rearrangement_d2_sequence_end'),
                   model_uri=AK_SCHEMA.Rearrangement_d2_sequence_end, domain=None, range=Optional[int])

slots.Rearrangement_d2_germline_start = Slot(uri=AK_SCHEMA.Rearrangement_d2_germline_start, name="Rearrangement_d2_germline_start", curie=AK_SCHEMA.curie('Rearrangement_d2_germline_start'),
                   model_uri=AK_SCHEMA.Rearrangement_d2_germline_start, domain=None, range=Optional[int])

slots.Rearrangement_d2_germline_end = Slot(uri=AK_SCHEMA.Rearrangement_d2_germline_end, name="Rearrangement_d2_germline_end", curie=AK_SCHEMA.curie('Rearrangement_d2_germline_end'),
                   model_uri=AK_SCHEMA.Rearrangement_d2_germline_end, domain=None, range=Optional[int])

slots.Rearrangement_d2_alignment_start = Slot(uri=AK_SCHEMA.Rearrangement_d2_alignment_start, name="Rearrangement_d2_alignment_start", curie=AK_SCHEMA.curie('Rearrangement_d2_alignment_start'),
                   model_uri=AK_SCHEMA.Rearrangement_d2_alignment_start, domain=None, range=Optional[int])

slots.Rearrangement_d2_alignment_end = Slot(uri=AK_SCHEMA.Rearrangement_d2_alignment_end, name="Rearrangement_d2_alignment_end", curie=AK_SCHEMA.curie('Rearrangement_d2_alignment_end'),
                   model_uri=AK_SCHEMA.Rearrangement_d2_alignment_end, domain=None, range=Optional[int])

slots.Rearrangement_j_sequence_start = Slot(uri=AK_SCHEMA.Rearrangement_j_sequence_start, name="Rearrangement_j_sequence_start", curie=AK_SCHEMA.curie('Rearrangement_j_sequence_start'),
                   model_uri=AK_SCHEMA.Rearrangement_j_sequence_start, domain=None, range=Optional[int])

slots.Rearrangement_j_sequence_end = Slot(uri=AK_SCHEMA.Rearrangement_j_sequence_end, name="Rearrangement_j_sequence_end", curie=AK_SCHEMA.curie('Rearrangement_j_sequence_end'),
                   model_uri=AK_SCHEMA.Rearrangement_j_sequence_end, domain=None, range=Optional[int])

slots.Rearrangement_j_germline_start = Slot(uri=AK_SCHEMA.Rearrangement_j_germline_start, name="Rearrangement_j_germline_start", curie=AK_SCHEMA.curie('Rearrangement_j_germline_start'),
                   model_uri=AK_SCHEMA.Rearrangement_j_germline_start, domain=None, range=Optional[int])

slots.Rearrangement_j_germline_end = Slot(uri=AK_SCHEMA.Rearrangement_j_germline_end, name="Rearrangement_j_germline_end", curie=AK_SCHEMA.curie('Rearrangement_j_germline_end'),
                   model_uri=AK_SCHEMA.Rearrangement_j_germline_end, domain=None, range=Optional[int])

slots.Rearrangement_j_alignment_start = Slot(uri=AK_SCHEMA.Rearrangement_j_alignment_start, name="Rearrangement_j_alignment_start", curie=AK_SCHEMA.curie('Rearrangement_j_alignment_start'),
                   model_uri=AK_SCHEMA.Rearrangement_j_alignment_start, domain=None, range=Optional[int])

slots.Rearrangement_j_alignment_end = Slot(uri=AK_SCHEMA.Rearrangement_j_alignment_end, name="Rearrangement_j_alignment_end", curie=AK_SCHEMA.curie('Rearrangement_j_alignment_end'),
                   model_uri=AK_SCHEMA.Rearrangement_j_alignment_end, domain=None, range=Optional[int])

slots.Rearrangement_c_sequence_start = Slot(uri=AK_SCHEMA.Rearrangement_c_sequence_start, name="Rearrangement_c_sequence_start", curie=AK_SCHEMA.curie('Rearrangement_c_sequence_start'),
                   model_uri=AK_SCHEMA.Rearrangement_c_sequence_start, domain=None, range=Optional[int])

slots.Rearrangement_c_sequence_end = Slot(uri=AK_SCHEMA.Rearrangement_c_sequence_end, name="Rearrangement_c_sequence_end", curie=AK_SCHEMA.curie('Rearrangement_c_sequence_end'),
                   model_uri=AK_SCHEMA.Rearrangement_c_sequence_end, domain=None, range=Optional[int])

slots.Rearrangement_c_germline_start = Slot(uri=AK_SCHEMA.Rearrangement_c_germline_start, name="Rearrangement_c_germline_start", curie=AK_SCHEMA.curie('Rearrangement_c_germline_start'),
                   model_uri=AK_SCHEMA.Rearrangement_c_germline_start, domain=None, range=Optional[int])

slots.Rearrangement_c_germline_end = Slot(uri=AK_SCHEMA.Rearrangement_c_germline_end, name="Rearrangement_c_germline_end", curie=AK_SCHEMA.curie('Rearrangement_c_germline_end'),
                   model_uri=AK_SCHEMA.Rearrangement_c_germline_end, domain=None, range=Optional[int])

slots.Rearrangement_c_alignment_start = Slot(uri=AK_SCHEMA.Rearrangement_c_alignment_start, name="Rearrangement_c_alignment_start", curie=AK_SCHEMA.curie('Rearrangement_c_alignment_start'),
                   model_uri=AK_SCHEMA.Rearrangement_c_alignment_start, domain=None, range=Optional[int])

slots.Rearrangement_c_alignment_end = Slot(uri=AK_SCHEMA.Rearrangement_c_alignment_end, name="Rearrangement_c_alignment_end", curie=AK_SCHEMA.curie('Rearrangement_c_alignment_end'),
                   model_uri=AK_SCHEMA.Rearrangement_c_alignment_end, domain=None, range=Optional[int])

slots.Rearrangement_cdr1_start = Slot(uri=AK_SCHEMA.Rearrangement_cdr1_start, name="Rearrangement_cdr1_start", curie=AK_SCHEMA.curie('Rearrangement_cdr1_start'),
                   model_uri=AK_SCHEMA.Rearrangement_cdr1_start, domain=None, range=Optional[int])

slots.Rearrangement_cdr1_end = Slot(uri=AK_SCHEMA.Rearrangement_cdr1_end, name="Rearrangement_cdr1_end", curie=AK_SCHEMA.curie('Rearrangement_cdr1_end'),
                   model_uri=AK_SCHEMA.Rearrangement_cdr1_end, domain=None, range=Optional[int])

slots.Rearrangement_cdr2_start = Slot(uri=AK_SCHEMA.Rearrangement_cdr2_start, name="Rearrangement_cdr2_start", curie=AK_SCHEMA.curie('Rearrangement_cdr2_start'),
                   model_uri=AK_SCHEMA.Rearrangement_cdr2_start, domain=None, range=Optional[int])

slots.Rearrangement_cdr2_end = Slot(uri=AK_SCHEMA.Rearrangement_cdr2_end, name="Rearrangement_cdr2_end", curie=AK_SCHEMA.curie('Rearrangement_cdr2_end'),
                   model_uri=AK_SCHEMA.Rearrangement_cdr2_end, domain=None, range=Optional[int])

slots.Rearrangement_cdr3_start = Slot(uri=AK_SCHEMA.Rearrangement_cdr3_start, name="Rearrangement_cdr3_start", curie=AK_SCHEMA.curie('Rearrangement_cdr3_start'),
                   model_uri=AK_SCHEMA.Rearrangement_cdr3_start, domain=None, range=Optional[int])

slots.Rearrangement_cdr3_end = Slot(uri=AK_SCHEMA.Rearrangement_cdr3_end, name="Rearrangement_cdr3_end", curie=AK_SCHEMA.curie('Rearrangement_cdr3_end'),
                   model_uri=AK_SCHEMA.Rearrangement_cdr3_end, domain=None, range=Optional[int])

slots.Rearrangement_fwr1_start = Slot(uri=AK_SCHEMA.Rearrangement_fwr1_start, name="Rearrangement_fwr1_start", curie=AK_SCHEMA.curie('Rearrangement_fwr1_start'),
                   model_uri=AK_SCHEMA.Rearrangement_fwr1_start, domain=None, range=Optional[int])

slots.Rearrangement_fwr1_end = Slot(uri=AK_SCHEMA.Rearrangement_fwr1_end, name="Rearrangement_fwr1_end", curie=AK_SCHEMA.curie('Rearrangement_fwr1_end'),
                   model_uri=AK_SCHEMA.Rearrangement_fwr1_end, domain=None, range=Optional[int])

slots.Rearrangement_fwr2_start = Slot(uri=AK_SCHEMA.Rearrangement_fwr2_start, name="Rearrangement_fwr2_start", curie=AK_SCHEMA.curie('Rearrangement_fwr2_start'),
                   model_uri=AK_SCHEMA.Rearrangement_fwr2_start, domain=None, range=Optional[int])

slots.Rearrangement_fwr2_end = Slot(uri=AK_SCHEMA.Rearrangement_fwr2_end, name="Rearrangement_fwr2_end", curie=AK_SCHEMA.curie('Rearrangement_fwr2_end'),
                   model_uri=AK_SCHEMA.Rearrangement_fwr2_end, domain=None, range=Optional[int])

slots.Rearrangement_fwr3_start = Slot(uri=AK_SCHEMA.Rearrangement_fwr3_start, name="Rearrangement_fwr3_start", curie=AK_SCHEMA.curie('Rearrangement_fwr3_start'),
                   model_uri=AK_SCHEMA.Rearrangement_fwr3_start, domain=None, range=Optional[int])

slots.Rearrangement_fwr3_end = Slot(uri=AK_SCHEMA.Rearrangement_fwr3_end, name="Rearrangement_fwr3_end", curie=AK_SCHEMA.curie('Rearrangement_fwr3_end'),
                   model_uri=AK_SCHEMA.Rearrangement_fwr3_end, domain=None, range=Optional[int])

slots.Rearrangement_fwr4_start = Slot(uri=AK_SCHEMA.Rearrangement_fwr4_start, name="Rearrangement_fwr4_start", curie=AK_SCHEMA.curie('Rearrangement_fwr4_start'),
                   model_uri=AK_SCHEMA.Rearrangement_fwr4_start, domain=None, range=Optional[int])

slots.Rearrangement_fwr4_end = Slot(uri=AK_SCHEMA.Rearrangement_fwr4_end, name="Rearrangement_fwr4_end", curie=AK_SCHEMA.curie('Rearrangement_fwr4_end'),
                   model_uri=AK_SCHEMA.Rearrangement_fwr4_end, domain=None, range=Optional[int])

slots.Rearrangement_v_sequence_alignment = Slot(uri=AK_SCHEMA.Rearrangement_v_sequence_alignment, name="Rearrangement_v_sequence_alignment", curie=AK_SCHEMA.curie('Rearrangement_v_sequence_alignment'),
                   model_uri=AK_SCHEMA.Rearrangement_v_sequence_alignment, domain=None, range=Optional[str])

slots.Rearrangement_v_sequence_alignment_aa = Slot(uri=AK_SCHEMA.Rearrangement_v_sequence_alignment_aa, name="Rearrangement_v_sequence_alignment_aa", curie=AK_SCHEMA.curie('Rearrangement_v_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_v_sequence_alignment_aa, domain=None, range=Optional[str])

slots.Rearrangement_d_sequence_alignment = Slot(uri=AK_SCHEMA.Rearrangement_d_sequence_alignment, name="Rearrangement_d_sequence_alignment", curie=AK_SCHEMA.curie('Rearrangement_d_sequence_alignment'),
                   model_uri=AK_SCHEMA.Rearrangement_d_sequence_alignment, domain=None, range=Optional[str])

slots.Rearrangement_d_sequence_alignment_aa = Slot(uri=AK_SCHEMA.Rearrangement_d_sequence_alignment_aa, name="Rearrangement_d_sequence_alignment_aa", curie=AK_SCHEMA.curie('Rearrangement_d_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_d_sequence_alignment_aa, domain=None, range=Optional[str])

slots.Rearrangement_d2_sequence_alignment = Slot(uri=AK_SCHEMA.Rearrangement_d2_sequence_alignment, name="Rearrangement_d2_sequence_alignment", curie=AK_SCHEMA.curie('Rearrangement_d2_sequence_alignment'),
                   model_uri=AK_SCHEMA.Rearrangement_d2_sequence_alignment, domain=None, range=Optional[str])

slots.Rearrangement_d2_sequence_alignment_aa = Slot(uri=AK_SCHEMA.Rearrangement_d2_sequence_alignment_aa, name="Rearrangement_d2_sequence_alignment_aa", curie=AK_SCHEMA.curie('Rearrangement_d2_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_d2_sequence_alignment_aa, domain=None, range=Optional[str])

slots.Rearrangement_j_sequence_alignment = Slot(uri=AK_SCHEMA.Rearrangement_j_sequence_alignment, name="Rearrangement_j_sequence_alignment", curie=AK_SCHEMA.curie('Rearrangement_j_sequence_alignment'),
                   model_uri=AK_SCHEMA.Rearrangement_j_sequence_alignment, domain=None, range=Optional[str])

slots.Rearrangement_j_sequence_alignment_aa = Slot(uri=AK_SCHEMA.Rearrangement_j_sequence_alignment_aa, name="Rearrangement_j_sequence_alignment_aa", curie=AK_SCHEMA.curie('Rearrangement_j_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_j_sequence_alignment_aa, domain=None, range=Optional[str])

slots.Rearrangement_c_sequence_alignment = Slot(uri=AK_SCHEMA.Rearrangement_c_sequence_alignment, name="Rearrangement_c_sequence_alignment", curie=AK_SCHEMA.curie('Rearrangement_c_sequence_alignment'),
                   model_uri=AK_SCHEMA.Rearrangement_c_sequence_alignment, domain=None, range=Optional[str])

slots.Rearrangement_c_sequence_alignment_aa = Slot(uri=AK_SCHEMA.Rearrangement_c_sequence_alignment_aa, name="Rearrangement_c_sequence_alignment_aa", curie=AK_SCHEMA.curie('Rearrangement_c_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_c_sequence_alignment_aa, domain=None, range=Optional[str])

slots.Rearrangement_v_germline_alignment = Slot(uri=AK_SCHEMA.Rearrangement_v_germline_alignment, name="Rearrangement_v_germline_alignment", curie=AK_SCHEMA.curie('Rearrangement_v_germline_alignment'),
                   model_uri=AK_SCHEMA.Rearrangement_v_germline_alignment, domain=None, range=Optional[str])

slots.Rearrangement_v_germline_alignment_aa = Slot(uri=AK_SCHEMA.Rearrangement_v_germline_alignment_aa, name="Rearrangement_v_germline_alignment_aa", curie=AK_SCHEMA.curie('Rearrangement_v_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_v_germline_alignment_aa, domain=None, range=Optional[str])

slots.Rearrangement_d_germline_alignment = Slot(uri=AK_SCHEMA.Rearrangement_d_germline_alignment, name="Rearrangement_d_germline_alignment", curie=AK_SCHEMA.curie('Rearrangement_d_germline_alignment'),
                   model_uri=AK_SCHEMA.Rearrangement_d_germline_alignment, domain=None, range=Optional[str])

slots.Rearrangement_d_germline_alignment_aa = Slot(uri=AK_SCHEMA.Rearrangement_d_germline_alignment_aa, name="Rearrangement_d_germline_alignment_aa", curie=AK_SCHEMA.curie('Rearrangement_d_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_d_germline_alignment_aa, domain=None, range=Optional[str])

slots.Rearrangement_d2_germline_alignment = Slot(uri=AK_SCHEMA.Rearrangement_d2_germline_alignment, name="Rearrangement_d2_germline_alignment", curie=AK_SCHEMA.curie('Rearrangement_d2_germline_alignment'),
                   model_uri=AK_SCHEMA.Rearrangement_d2_germline_alignment, domain=None, range=Optional[str])

slots.Rearrangement_d2_germline_alignment_aa = Slot(uri=AK_SCHEMA.Rearrangement_d2_germline_alignment_aa, name="Rearrangement_d2_germline_alignment_aa", curie=AK_SCHEMA.curie('Rearrangement_d2_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_d2_germline_alignment_aa, domain=None, range=Optional[str])

slots.Rearrangement_j_germline_alignment = Slot(uri=AK_SCHEMA.Rearrangement_j_germline_alignment, name="Rearrangement_j_germline_alignment", curie=AK_SCHEMA.curie('Rearrangement_j_germline_alignment'),
                   model_uri=AK_SCHEMA.Rearrangement_j_germline_alignment, domain=None, range=Optional[str])

slots.Rearrangement_j_germline_alignment_aa = Slot(uri=AK_SCHEMA.Rearrangement_j_germline_alignment_aa, name="Rearrangement_j_germline_alignment_aa", curie=AK_SCHEMA.curie('Rearrangement_j_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_j_germline_alignment_aa, domain=None, range=Optional[str])

slots.Rearrangement_c_germline_alignment = Slot(uri=AK_SCHEMA.Rearrangement_c_germline_alignment, name="Rearrangement_c_germline_alignment", curie=AK_SCHEMA.curie('Rearrangement_c_germline_alignment'),
                   model_uri=AK_SCHEMA.Rearrangement_c_germline_alignment, domain=None, range=Optional[str])

slots.Rearrangement_c_germline_alignment_aa = Slot(uri=AK_SCHEMA.Rearrangement_c_germline_alignment_aa, name="Rearrangement_c_germline_alignment_aa", curie=AK_SCHEMA.curie('Rearrangement_c_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.Rearrangement_c_germline_alignment_aa, domain=None, range=Optional[str])

slots.Rearrangement_junction_length = Slot(uri=AK_SCHEMA.Rearrangement_junction_length, name="Rearrangement_junction_length", curie=AK_SCHEMA.curie('Rearrangement_junction_length'),
                   model_uri=AK_SCHEMA.Rearrangement_junction_length, domain=None, range=Optional[int])

slots.Rearrangement_junction_aa_length = Slot(uri=AK_SCHEMA.Rearrangement_junction_aa_length, name="Rearrangement_junction_aa_length", curie=AK_SCHEMA.curie('Rearrangement_junction_aa_length'),
                   model_uri=AK_SCHEMA.Rearrangement_junction_aa_length, domain=None, range=Optional[int])

slots.Rearrangement_np1_length = Slot(uri=AK_SCHEMA.Rearrangement_np1_length, name="Rearrangement_np1_length", curie=AK_SCHEMA.curie('Rearrangement_np1_length'),
                   model_uri=AK_SCHEMA.Rearrangement_np1_length, domain=None, range=Optional[int])

slots.Rearrangement_np2_length = Slot(uri=AK_SCHEMA.Rearrangement_np2_length, name="Rearrangement_np2_length", curie=AK_SCHEMA.curie('Rearrangement_np2_length'),
                   model_uri=AK_SCHEMA.Rearrangement_np2_length, domain=None, range=Optional[int])

slots.Rearrangement_np3_length = Slot(uri=AK_SCHEMA.Rearrangement_np3_length, name="Rearrangement_np3_length", curie=AK_SCHEMA.curie('Rearrangement_np3_length'),
                   model_uri=AK_SCHEMA.Rearrangement_np3_length, domain=None, range=Optional[int])

slots.Rearrangement_n1_length = Slot(uri=AK_SCHEMA.Rearrangement_n1_length, name="Rearrangement_n1_length", curie=AK_SCHEMA.curie('Rearrangement_n1_length'),
                   model_uri=AK_SCHEMA.Rearrangement_n1_length, domain=None, range=Optional[int])

slots.Rearrangement_n2_length = Slot(uri=AK_SCHEMA.Rearrangement_n2_length, name="Rearrangement_n2_length", curie=AK_SCHEMA.curie('Rearrangement_n2_length'),
                   model_uri=AK_SCHEMA.Rearrangement_n2_length, domain=None, range=Optional[int])

slots.Rearrangement_n3_length = Slot(uri=AK_SCHEMA.Rearrangement_n3_length, name="Rearrangement_n3_length", curie=AK_SCHEMA.curie('Rearrangement_n3_length'),
                   model_uri=AK_SCHEMA.Rearrangement_n3_length, domain=None, range=Optional[int])

slots.Rearrangement_p3v_length = Slot(uri=AK_SCHEMA.Rearrangement_p3v_length, name="Rearrangement_p3v_length", curie=AK_SCHEMA.curie('Rearrangement_p3v_length'),
                   model_uri=AK_SCHEMA.Rearrangement_p3v_length, domain=None, range=Optional[int])

slots.Rearrangement_p5d_length = Slot(uri=AK_SCHEMA.Rearrangement_p5d_length, name="Rearrangement_p5d_length", curie=AK_SCHEMA.curie('Rearrangement_p5d_length'),
                   model_uri=AK_SCHEMA.Rearrangement_p5d_length, domain=None, range=Optional[int])

slots.Rearrangement_p3d_length = Slot(uri=AK_SCHEMA.Rearrangement_p3d_length, name="Rearrangement_p3d_length", curie=AK_SCHEMA.curie('Rearrangement_p3d_length'),
                   model_uri=AK_SCHEMA.Rearrangement_p3d_length, domain=None, range=Optional[int])

slots.Rearrangement_p5d2_length = Slot(uri=AK_SCHEMA.Rearrangement_p5d2_length, name="Rearrangement_p5d2_length", curie=AK_SCHEMA.curie('Rearrangement_p5d2_length'),
                   model_uri=AK_SCHEMA.Rearrangement_p5d2_length, domain=None, range=Optional[int])

slots.Rearrangement_p3d2_length = Slot(uri=AK_SCHEMA.Rearrangement_p3d2_length, name="Rearrangement_p3d2_length", curie=AK_SCHEMA.curie('Rearrangement_p3d2_length'),
                   model_uri=AK_SCHEMA.Rearrangement_p3d2_length, domain=None, range=Optional[int])

slots.Rearrangement_p5j_length = Slot(uri=AK_SCHEMA.Rearrangement_p5j_length, name="Rearrangement_p5j_length", curie=AK_SCHEMA.curie('Rearrangement_p5j_length'),
                   model_uri=AK_SCHEMA.Rearrangement_p5j_length, domain=None, range=Optional[int])

slots.Rearrangement_v_frameshift = Slot(uri=AK_SCHEMA.Rearrangement_v_frameshift, name="Rearrangement_v_frameshift", curie=AK_SCHEMA.curie('Rearrangement_v_frameshift'),
                   model_uri=AK_SCHEMA.Rearrangement_v_frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.Rearrangement_j_frameshift = Slot(uri=AK_SCHEMA.Rearrangement_j_frameshift, name="Rearrangement_j_frameshift", curie=AK_SCHEMA.curie('Rearrangement_j_frameshift'),
                   model_uri=AK_SCHEMA.Rearrangement_j_frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.Rearrangement_d_frame = Slot(uri=AK_SCHEMA.Rearrangement_d_frame, name="Rearrangement_d_frame", curie=AK_SCHEMA.curie('Rearrangement_d_frame'),
                   model_uri=AK_SCHEMA.Rearrangement_d_frame, domain=None, range=Optional[int])

slots.Rearrangement_d2_frame = Slot(uri=AK_SCHEMA.Rearrangement_d2_frame, name="Rearrangement_d2_frame", curie=AK_SCHEMA.curie('Rearrangement_d2_frame'),
                   model_uri=AK_SCHEMA.Rearrangement_d2_frame, domain=None, range=Optional[int])

slots.Rearrangement_consensus_count = Slot(uri=AK_SCHEMA.Rearrangement_consensus_count, name="Rearrangement_consensus_count", curie=AK_SCHEMA.curie('Rearrangement_consensus_count'),
                   model_uri=AK_SCHEMA.Rearrangement_consensus_count, domain=None, range=Optional[int])

slots.Rearrangement_duplicate_count = Slot(uri=AK_SCHEMA.Rearrangement_duplicate_count, name="Rearrangement_duplicate_count", curie=AK_SCHEMA.curie('Rearrangement_duplicate_count'),
                   model_uri=AK_SCHEMA.Rearrangement_duplicate_count, domain=None, range=Optional[int])

slots.Rearrangement_umi_count = Slot(uri=AK_SCHEMA.Rearrangement_umi_count, name="Rearrangement_umi_count", curie=AK_SCHEMA.curie('Rearrangement_umi_count'),
                   model_uri=AK_SCHEMA.Rearrangement_umi_count, domain=None, range=Optional[int])

slots.Rearrangement_cell_id = Slot(uri=AK_SCHEMA.Rearrangement_cell_id, name="Rearrangement_cell_id", curie=AK_SCHEMA.curie('Rearrangement_cell_id'),
                   model_uri=AK_SCHEMA.Rearrangement_cell_id, domain=None, range=Optional[str])

slots.Rearrangement_clone_id = Slot(uri=AK_SCHEMA.Rearrangement_clone_id, name="Rearrangement_clone_id", curie=AK_SCHEMA.curie('Rearrangement_clone_id'),
                   model_uri=AK_SCHEMA.Rearrangement_clone_id, domain=None, range=Optional[str])

slots.Rearrangement_repertoire_id = Slot(uri=AK_SCHEMA.Rearrangement_repertoire_id, name="Rearrangement_repertoire_id", curie=AK_SCHEMA.curie('Rearrangement_repertoire_id'),
                   model_uri=AK_SCHEMA.Rearrangement_repertoire_id, domain=None, range=Optional[str])

slots.Rearrangement_sample_processing_id = Slot(uri=AK_SCHEMA.Rearrangement_sample_processing_id, name="Rearrangement_sample_processing_id", curie=AK_SCHEMA.curie('Rearrangement_sample_processing_id'),
                   model_uri=AK_SCHEMA.Rearrangement_sample_processing_id, domain=None, range=Optional[str])

slots.Rearrangement_data_processing_id = Slot(uri=AK_SCHEMA.Rearrangement_data_processing_id, name="Rearrangement_data_processing_id", curie=AK_SCHEMA.curie('Rearrangement_data_processing_id'),
                   model_uri=AK_SCHEMA.Rearrangement_data_processing_id, domain=None, range=Optional[str])

slots.Clone_clone_id = Slot(uri=AK_SCHEMA.Clone_clone_id, name="Clone_clone_id", curie=AK_SCHEMA.curie('Clone_clone_id'),
                   model_uri=AK_SCHEMA.Clone_clone_id, domain=None, range=str)

slots.Clone_repertoire_id = Slot(uri=AK_SCHEMA.Clone_repertoire_id, name="Clone_repertoire_id", curie=AK_SCHEMA.curie('Clone_repertoire_id'),
                   model_uri=AK_SCHEMA.Clone_repertoire_id, domain=None, range=Optional[str])

slots.Clone_data_processing_id = Slot(uri=AK_SCHEMA.Clone_data_processing_id, name="Clone_data_processing_id", curie=AK_SCHEMA.curie('Clone_data_processing_id'),
                   model_uri=AK_SCHEMA.Clone_data_processing_id, domain=None, range=Optional[str])

slots.Clone_sequences = Slot(uri=AK_SCHEMA.Clone_sequences, name="Clone_sequences", curie=AK_SCHEMA.curie('Clone_sequences'),
                   model_uri=AK_SCHEMA.Clone_sequences, domain=None, range=Optional[Union[str, List[str]]])

slots.Clone_v_call = Slot(uri=AK_SCHEMA.Clone_v_call, name="Clone_v_call", curie=AK_SCHEMA.curie('Clone_v_call'),
                   model_uri=AK_SCHEMA.Clone_v_call, domain=None, range=Optional[str])

slots.Clone_d_call = Slot(uri=AK_SCHEMA.Clone_d_call, name="Clone_d_call", curie=AK_SCHEMA.curie('Clone_d_call'),
                   model_uri=AK_SCHEMA.Clone_d_call, domain=None, range=Optional[str])

slots.Clone_j_call = Slot(uri=AK_SCHEMA.Clone_j_call, name="Clone_j_call", curie=AK_SCHEMA.curie('Clone_j_call'),
                   model_uri=AK_SCHEMA.Clone_j_call, domain=None, range=Optional[str])

slots.Clone_junction = Slot(uri=AK_SCHEMA.Clone_junction, name="Clone_junction", curie=AK_SCHEMA.curie('Clone_junction'),
                   model_uri=AK_SCHEMA.Clone_junction, domain=None, range=Optional[str])

slots.Clone_junction_aa = Slot(uri=AK_SCHEMA.Clone_junction_aa, name="Clone_junction_aa", curie=AK_SCHEMA.curie('Clone_junction_aa'),
                   model_uri=AK_SCHEMA.Clone_junction_aa, domain=None, range=Optional[str])

slots.Clone_junction_length = Slot(uri=AK_SCHEMA.Clone_junction_length, name="Clone_junction_length", curie=AK_SCHEMA.curie('Clone_junction_length'),
                   model_uri=AK_SCHEMA.Clone_junction_length, domain=None, range=Optional[int])

slots.Clone_junction_aa_length = Slot(uri=AK_SCHEMA.Clone_junction_aa_length, name="Clone_junction_aa_length", curie=AK_SCHEMA.curie('Clone_junction_aa_length'),
                   model_uri=AK_SCHEMA.Clone_junction_aa_length, domain=None, range=Optional[int])

slots.Clone_germline_alignment = Slot(uri=AK_SCHEMA.Clone_germline_alignment, name="Clone_germline_alignment", curie=AK_SCHEMA.curie('Clone_germline_alignment'),
                   model_uri=AK_SCHEMA.Clone_germline_alignment, domain=None, range=str)

slots.Clone_germline_alignment_aa = Slot(uri=AK_SCHEMA.Clone_germline_alignment_aa, name="Clone_germline_alignment_aa", curie=AK_SCHEMA.curie('Clone_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.Clone_germline_alignment_aa, domain=None, range=Optional[str])

slots.Clone_v_alignment_start = Slot(uri=AK_SCHEMA.Clone_v_alignment_start, name="Clone_v_alignment_start", curie=AK_SCHEMA.curie('Clone_v_alignment_start'),
                   model_uri=AK_SCHEMA.Clone_v_alignment_start, domain=None, range=Optional[int])

slots.Clone_v_alignment_end = Slot(uri=AK_SCHEMA.Clone_v_alignment_end, name="Clone_v_alignment_end", curie=AK_SCHEMA.curie('Clone_v_alignment_end'),
                   model_uri=AK_SCHEMA.Clone_v_alignment_end, domain=None, range=Optional[int])

slots.Clone_d_alignment_start = Slot(uri=AK_SCHEMA.Clone_d_alignment_start, name="Clone_d_alignment_start", curie=AK_SCHEMA.curie('Clone_d_alignment_start'),
                   model_uri=AK_SCHEMA.Clone_d_alignment_start, domain=None, range=Optional[int])

slots.Clone_d_alignment_end = Slot(uri=AK_SCHEMA.Clone_d_alignment_end, name="Clone_d_alignment_end", curie=AK_SCHEMA.curie('Clone_d_alignment_end'),
                   model_uri=AK_SCHEMA.Clone_d_alignment_end, domain=None, range=Optional[int])

slots.Clone_j_alignment_start = Slot(uri=AK_SCHEMA.Clone_j_alignment_start, name="Clone_j_alignment_start", curie=AK_SCHEMA.curie('Clone_j_alignment_start'),
                   model_uri=AK_SCHEMA.Clone_j_alignment_start, domain=None, range=Optional[int])

slots.Clone_j_alignment_end = Slot(uri=AK_SCHEMA.Clone_j_alignment_end, name="Clone_j_alignment_end", curie=AK_SCHEMA.curie('Clone_j_alignment_end'),
                   model_uri=AK_SCHEMA.Clone_j_alignment_end, domain=None, range=Optional[int])

slots.Clone_junction_start = Slot(uri=AK_SCHEMA.Clone_junction_start, name="Clone_junction_start", curie=AK_SCHEMA.curie('Clone_junction_start'),
                   model_uri=AK_SCHEMA.Clone_junction_start, domain=None, range=Optional[int])

slots.Clone_junction_end = Slot(uri=AK_SCHEMA.Clone_junction_end, name="Clone_junction_end", curie=AK_SCHEMA.curie('Clone_junction_end'),
                   model_uri=AK_SCHEMA.Clone_junction_end, domain=None, range=Optional[int])

slots.Clone_umi_count = Slot(uri=AK_SCHEMA.Clone_umi_count, name="Clone_umi_count", curie=AK_SCHEMA.curie('Clone_umi_count'),
                   model_uri=AK_SCHEMA.Clone_umi_count, domain=None, range=Optional[int])

slots.Clone_clone_count = Slot(uri=AK_SCHEMA.Clone_clone_count, name="Clone_clone_count", curie=AK_SCHEMA.curie('Clone_clone_count'),
                   model_uri=AK_SCHEMA.Clone_clone_count, domain=None, range=Optional[int])

slots.Clone_seed_id = Slot(uri=AK_SCHEMA.Clone_seed_id, name="Clone_seed_id", curie=AK_SCHEMA.curie('Clone_seed_id'),
                   model_uri=AK_SCHEMA.Clone_seed_id, domain=None, range=Optional[str])

slots.Tree_tree_id = Slot(uri=AK_SCHEMA.Tree_tree_id, name="Tree_tree_id", curie=AK_SCHEMA.curie('Tree_tree_id'),
                   model_uri=AK_SCHEMA.Tree_tree_id, domain=None, range=str)

slots.Tree_clone_id = Slot(uri=AK_SCHEMA.Tree_clone_id, name="Tree_clone_id", curie=AK_SCHEMA.curie('Tree_clone_id'),
                   model_uri=AK_SCHEMA.Tree_clone_id, domain=None, range=str)

slots.Tree_newick = Slot(uri=AK_SCHEMA.Tree_newick, name="Tree_newick", curie=AK_SCHEMA.curie('Tree_newick'),
                   model_uri=AK_SCHEMA.Tree_newick, domain=None, range=str)

slots.Tree_nodes = Slot(uri=AK_SCHEMA.Tree_nodes, name="Tree_nodes", curie=AK_SCHEMA.curie('Tree_nodes'),
                   model_uri=AK_SCHEMA.Tree_nodes, domain=None, range=Optional[str])

slots.Node_sequence_id = Slot(uri=AK_SCHEMA.Node_sequence_id, name="Node_sequence_id", curie=AK_SCHEMA.curie('Node_sequence_id'),
                   model_uri=AK_SCHEMA.Node_sequence_id, domain=None, range=str)

slots.Node_sequence_alignment = Slot(uri=AK_SCHEMA.Node_sequence_alignment, name="Node_sequence_alignment", curie=AK_SCHEMA.curie('Node_sequence_alignment'),
                   model_uri=AK_SCHEMA.Node_sequence_alignment, domain=None, range=Optional[str])

slots.Node_junction = Slot(uri=AK_SCHEMA.Node_junction, name="Node_junction", curie=AK_SCHEMA.curie('Node_junction'),
                   model_uri=AK_SCHEMA.Node_junction, domain=None, range=Optional[str])

slots.Node_junction_aa = Slot(uri=AK_SCHEMA.Node_junction_aa, name="Node_junction_aa", curie=AK_SCHEMA.curie('Node_junction_aa'),
                   model_uri=AK_SCHEMA.Node_junction_aa, domain=None, range=Optional[str])

slots.Cell_cell_id = Slot(uri=AK_SCHEMA.Cell_cell_id, name="Cell_cell_id", curie=AK_SCHEMA.curie('Cell_cell_id'),
                   model_uri=AK_SCHEMA.Cell_cell_id, domain=None, range=str)

slots.Cell_rearrangements = Slot(uri=AK_SCHEMA.Cell_rearrangements, name="Cell_rearrangements", curie=AK_SCHEMA.curie('Cell_rearrangements'),
                   model_uri=AK_SCHEMA.Cell_rearrangements, domain=None, range=Union[str, List[str]])

slots.Cell_receptors = Slot(uri=AK_SCHEMA.Cell_receptors, name="Cell_receptors", curie=AK_SCHEMA.curie('Cell_receptors'),
                   model_uri=AK_SCHEMA.Cell_receptors, domain=None, range=Optional[Union[str, List[str]]])

slots.Cell_repertoire_id = Slot(uri=AK_SCHEMA.Cell_repertoire_id, name="Cell_repertoire_id", curie=AK_SCHEMA.curie('Cell_repertoire_id'),
                   model_uri=AK_SCHEMA.Cell_repertoire_id, domain=None, range=str)

slots.Cell_data_processing_id = Slot(uri=AK_SCHEMA.Cell_data_processing_id, name="Cell_data_processing_id", curie=AK_SCHEMA.curie('Cell_data_processing_id'),
                   model_uri=AK_SCHEMA.Cell_data_processing_id, domain=None, range=Optional[str])

slots.Cell_expression_study_method = Slot(uri=AK_SCHEMA.Cell_expression_study_method, name="Cell_expression_study_method", curie=AK_SCHEMA.curie('Cell_expression_study_method'),
                   model_uri=AK_SCHEMA.Cell_expression_study_method, domain=None, range=Optional[Union[str, "ExpressionStudyMethod"]])

slots.Cell_expression_raw_doi = Slot(uri=AK_SCHEMA.Cell_expression_raw_doi, name="Cell_expression_raw_doi", curie=AK_SCHEMA.curie('Cell_expression_raw_doi'),
                   model_uri=AK_SCHEMA.Cell_expression_raw_doi, domain=None, range=Optional[str])

slots.Cell_expression_index = Slot(uri=AK_SCHEMA.Cell_expression_index, name="Cell_expression_index", curie=AK_SCHEMA.curie('Cell_expression_index'),
                   model_uri=AK_SCHEMA.Cell_expression_index, domain=None, range=Optional[str])

slots.Cell_virtual_pairing = Slot(uri=AK_SCHEMA.Cell_virtual_pairing, name="Cell_virtual_pairing", curie=AK_SCHEMA.curie('Cell_virtual_pairing'),
                   model_uri=AK_SCHEMA.Cell_virtual_pairing, domain=None, range=Union[bool, Bool])

slots.CellExpression_expression_id = Slot(uri=AK_SCHEMA.CellExpression_expression_id, name="CellExpression_expression_id", curie=AK_SCHEMA.curie('CellExpression_expression_id'),
                   model_uri=AK_SCHEMA.CellExpression_expression_id, domain=None, range=str)

slots.CellExpression_cell_id = Slot(uri=AK_SCHEMA.CellExpression_cell_id, name="CellExpression_cell_id", curie=AK_SCHEMA.curie('CellExpression_cell_id'),
                   model_uri=AK_SCHEMA.CellExpression_cell_id, domain=None, range=str)

slots.CellExpression_repertoire_id = Slot(uri=AK_SCHEMA.CellExpression_repertoire_id, name="CellExpression_repertoire_id", curie=AK_SCHEMA.curie('CellExpression_repertoire_id'),
                   model_uri=AK_SCHEMA.CellExpression_repertoire_id, domain=None, range=str)

slots.CellExpression_data_processing_id = Slot(uri=AK_SCHEMA.CellExpression_data_processing_id, name="CellExpression_data_processing_id", curie=AK_SCHEMA.curie('CellExpression_data_processing_id'),
                   model_uri=AK_SCHEMA.CellExpression_data_processing_id, domain=None, range=str)

slots.CellExpression_property_type = Slot(uri=AK_SCHEMA.CellExpression_property_type, name="CellExpression_property_type", curie=AK_SCHEMA.curie('CellExpression_property_type'),
                   model_uri=AK_SCHEMA.CellExpression_property_type, domain=None, range=str)

slots.CellExpression_property = Slot(uri=AK_SCHEMA.CellExpression_property, name="CellExpression_property", curie=AK_SCHEMA.curie('CellExpression_property'),
                   model_uri=AK_SCHEMA.CellExpression_property, domain=None, range=Union[str, "Property"])

slots.CellExpression_value = Slot(uri=AK_SCHEMA.CellExpression_value, name="CellExpression_value", curie=AK_SCHEMA.curie('CellExpression_value'),
                   model_uri=AK_SCHEMA.CellExpression_value, domain=None, range=float)

slots.Receptor_receptor_id = Slot(uri=AK_SCHEMA.Receptor_receptor_id, name="Receptor_receptor_id", curie=AK_SCHEMA.curie('Receptor_receptor_id'),
                   model_uri=AK_SCHEMA.Receptor_receptor_id, domain=None, range=str)

slots.Receptor_receptor_hash = Slot(uri=AK_SCHEMA.Receptor_receptor_hash, name="Receptor_receptor_hash", curie=AK_SCHEMA.curie('Receptor_receptor_hash'),
                   model_uri=AK_SCHEMA.Receptor_receptor_hash, domain=None, range=str)

slots.Receptor_receptor_type = Slot(uri=AK_SCHEMA.Receptor_receptor_type, name="Receptor_receptor_type", curie=AK_SCHEMA.curie('Receptor_receptor_type'),
                   model_uri=AK_SCHEMA.Receptor_receptor_type, domain=None, range=Union[str, "ReceptorType"])

slots.Receptor_receptor_variable_domain_1_aa = Slot(uri=AK_SCHEMA.Receptor_receptor_variable_domain_1_aa, name="Receptor_receptor_variable_domain_1_aa", curie=AK_SCHEMA.curie('Receptor_receptor_variable_domain_1_aa'),
                   model_uri=AK_SCHEMA.Receptor_receptor_variable_domain_1_aa, domain=None, range=str)

slots.Receptor_receptor_variable_domain_1_locus = Slot(uri=AK_SCHEMA.Receptor_receptor_variable_domain_1_locus, name="Receptor_receptor_variable_domain_1_locus", curie=AK_SCHEMA.curie('Receptor_receptor_variable_domain_1_locus'),
                   model_uri=AK_SCHEMA.Receptor_receptor_variable_domain_1_locus, domain=None, range=Union[str, "ReceptorVariableDomain1Locus"])

slots.Receptor_receptor_variable_domain_2_aa = Slot(uri=AK_SCHEMA.Receptor_receptor_variable_domain_2_aa, name="Receptor_receptor_variable_domain_2_aa", curie=AK_SCHEMA.curie('Receptor_receptor_variable_domain_2_aa'),
                   model_uri=AK_SCHEMA.Receptor_receptor_variable_domain_2_aa, domain=None, range=str)

slots.Receptor_receptor_variable_domain_2_locus = Slot(uri=AK_SCHEMA.Receptor_receptor_variable_domain_2_locus, name="Receptor_receptor_variable_domain_2_locus", curie=AK_SCHEMA.curie('Receptor_receptor_variable_domain_2_locus'),
                   model_uri=AK_SCHEMA.Receptor_receptor_variable_domain_2_locus, domain=None, range=Union[str, "ReceptorVariableDomain2Locus"])

slots.Receptor_receptor_ref = Slot(uri=AK_SCHEMA.Receptor_receptor_ref, name="Receptor_receptor_ref", curie=AK_SCHEMA.curie('Receptor_receptor_ref'),
                   model_uri=AK_SCHEMA.Receptor_receptor_ref, domain=None, range=Optional[Union[str, List[str]]])

slots.Receptor_reactivity_measurements = Slot(uri=AK_SCHEMA.Receptor_reactivity_measurements, name="Receptor_reactivity_measurements", curie=AK_SCHEMA.curie('Receptor_reactivity_measurements'),
                   model_uri=AK_SCHEMA.Receptor_reactivity_measurements, domain=None, range=Optional[Union[Union[dict, ReceptorReactivity], List[Union[dict, ReceptorReactivity]]]])

slots.ReceptorReactivity_ligand_type = Slot(uri=AK_SCHEMA.ReceptorReactivity_ligand_type, name="ReceptorReactivity_ligand_type", curie=AK_SCHEMA.curie('ReceptorReactivity_ligand_type'),
                   model_uri=AK_SCHEMA.ReceptorReactivity_ligand_type, domain=None, range=Union[str, "LigandType"])

slots.ReceptorReactivity_antigen_type = Slot(uri=AK_SCHEMA.ReceptorReactivity_antigen_type, name="ReceptorReactivity_antigen_type", curie=AK_SCHEMA.curie('ReceptorReactivity_antigen_type'),
                   model_uri=AK_SCHEMA.ReceptorReactivity_antigen_type, domain=None, range=Union[str, "AntigenType"])

slots.ReceptorReactivity_antigen = Slot(uri=AK_SCHEMA.ReceptorReactivity_antigen, name="ReceptorReactivity_antigen", curie=AK_SCHEMA.curie('ReceptorReactivity_antigen'),
                   model_uri=AK_SCHEMA.ReceptorReactivity_antigen, domain=None, range=Union[str, "Antigen"])

slots.ReceptorReactivity_antigen_source_species = Slot(uri=AK_SCHEMA.ReceptorReactivity_antigen_source_species, name="ReceptorReactivity_antigen_source_species", curie=AK_SCHEMA.curie('ReceptorReactivity_antigen_source_species'),
                   model_uri=AK_SCHEMA.ReceptorReactivity_antigen_source_species, domain=None, range=Optional[Union[str, "AntigenSourceSpecies"]])

slots.ReceptorReactivity_peptide_start = Slot(uri=AK_SCHEMA.ReceptorReactivity_peptide_start, name="ReceptorReactivity_peptide_start", curie=AK_SCHEMA.curie('ReceptorReactivity_peptide_start'),
                   model_uri=AK_SCHEMA.ReceptorReactivity_peptide_start, domain=None, range=Optional[int])

slots.ReceptorReactivity_peptide_end = Slot(uri=AK_SCHEMA.ReceptorReactivity_peptide_end, name="ReceptorReactivity_peptide_end", curie=AK_SCHEMA.curie('ReceptorReactivity_peptide_end'),
                   model_uri=AK_SCHEMA.ReceptorReactivity_peptide_end, domain=None, range=Optional[int])

slots.ReceptorReactivity_mhc_class = Slot(uri=AK_SCHEMA.ReceptorReactivity_mhc_class, name="ReceptorReactivity_mhc_class", curie=AK_SCHEMA.curie('ReceptorReactivity_mhc_class'),
                   model_uri=AK_SCHEMA.ReceptorReactivity_mhc_class, domain=None, range=Optional[Union[str, "MhcClass"]])

slots.ReceptorReactivity_mhc_gene_1 = Slot(uri=AK_SCHEMA.ReceptorReactivity_mhc_gene_1, name="ReceptorReactivity_mhc_gene_1", curie=AK_SCHEMA.curie('ReceptorReactivity_mhc_gene_1'),
                   model_uri=AK_SCHEMA.ReceptorReactivity_mhc_gene_1, domain=None, range=Optional[Union[str, "MhcGene1"]])

slots.ReceptorReactivity_mhc_allele_1 = Slot(uri=AK_SCHEMA.ReceptorReactivity_mhc_allele_1, name="ReceptorReactivity_mhc_allele_1", curie=AK_SCHEMA.curie('ReceptorReactivity_mhc_allele_1'),
                   model_uri=AK_SCHEMA.ReceptorReactivity_mhc_allele_1, domain=None, range=Optional[str])

slots.ReceptorReactivity_mhc_gene_2 = Slot(uri=AK_SCHEMA.ReceptorReactivity_mhc_gene_2, name="ReceptorReactivity_mhc_gene_2", curie=AK_SCHEMA.curie('ReceptorReactivity_mhc_gene_2'),
                   model_uri=AK_SCHEMA.ReceptorReactivity_mhc_gene_2, domain=None, range=Optional[Union[str, "MhcGene2"]])

slots.ReceptorReactivity_mhc_allele_2 = Slot(uri=AK_SCHEMA.ReceptorReactivity_mhc_allele_2, name="ReceptorReactivity_mhc_allele_2", curie=AK_SCHEMA.curie('ReceptorReactivity_mhc_allele_2'),
                   model_uri=AK_SCHEMA.ReceptorReactivity_mhc_allele_2, domain=None, range=Optional[str])

slots.ReceptorReactivity_reactivity_method = Slot(uri=AK_SCHEMA.ReceptorReactivity_reactivity_method, name="ReceptorReactivity_reactivity_method", curie=AK_SCHEMA.curie('ReceptorReactivity_reactivity_method'),
                   model_uri=AK_SCHEMA.ReceptorReactivity_reactivity_method, domain=None, range=Union[str, "ReactivityMethod"])

slots.ReceptorReactivity_reactivity_readout = Slot(uri=AK_SCHEMA.ReceptorReactivity_reactivity_readout, name="ReceptorReactivity_reactivity_readout", curie=AK_SCHEMA.curie('ReceptorReactivity_reactivity_readout'),
                   model_uri=AK_SCHEMA.ReceptorReactivity_reactivity_readout, domain=None, range=Union[str, "ReactivityReadout"])

slots.ReceptorReactivity_reactivity_value = Slot(uri=AK_SCHEMA.ReceptorReactivity_reactivity_value, name="ReceptorReactivity_reactivity_value", curie=AK_SCHEMA.curie('ReceptorReactivity_reactivity_value'),
                   model_uri=AK_SCHEMA.ReceptorReactivity_reactivity_value, domain=None, range=float)

slots.ReceptorReactivity_reactivity_unit = Slot(uri=AK_SCHEMA.ReceptorReactivity_reactivity_unit, name="ReceptorReactivity_reactivity_unit", curie=AK_SCHEMA.curie('ReceptorReactivity_reactivity_unit'),
                   model_uri=AK_SCHEMA.ReceptorReactivity_reactivity_unit, domain=None, range=str)

slots.SampleProcessing_sample_processing_id = Slot(uri=AK_SCHEMA.SampleProcessing_sample_processing_id, name="SampleProcessing_sample_processing_id", curie=AK_SCHEMA.curie('SampleProcessing_sample_processing_id'),
                   model_uri=AK_SCHEMA.SampleProcessing_sample_processing_id, domain=None, range=Optional[str])

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