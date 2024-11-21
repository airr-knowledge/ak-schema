# Auto generated from ak_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-11-21T14:37:48
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
class V1p4TimePoint(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4TimePoint"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4TimePoint"
    class_name: ClassVar[str] = "V1p4_TimePoint"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4TimePoint

    time_point__label: Optional[str] = None
    time_point__value: Optional[float] = None
    time_point__unit: Optional[Union[str, "V1p4Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.time_point__label is not None and not isinstance(self.time_point__label, str):
            self.time_point__label = str(self.time_point__label)

        if self.time_point__value is not None and not isinstance(self.time_point__value, float):
            self.time_point__value = float(self.time_point__value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4TimeInterval(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4TimeInterval"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4TimeInterval"
    class_name: ClassVar[str] = "V1p4_TimeInterval"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4TimeInterval

    time_interval__min: Optional[float] = None
    time_interval__max: Optional[float] = None
    time_interval__unit: Optional[Union[str, "V1p4Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.time_interval__min is not None and not isinstance(self.time_interval__min, float):
            self.time_interval__min = float(self.time_interval__min)

        if self.time_interval__max is not None and not isinstance(self.time_interval__max, float):
            self.time_interval__max = float(self.time_interval__max)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4PhysicalQuantity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4PhysicalQuantity"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4PhysicalQuantity"
    class_name: ClassVar[str] = "V1p4_PhysicalQuantity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4PhysicalQuantity

    physical_quantity__quantity: Optional[float] = None
    physical_quantity__unit: Optional[Union[str, "V1p4Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.physical_quantity__quantity is not None and not isinstance(self.physical_quantity__quantity, float):
            self.physical_quantity__quantity = float(self.physical_quantity__quantity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4TimeQuantity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4TimeQuantity"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4TimeQuantity"
    class_name: ClassVar[str] = "V1p4_TimeQuantity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4TimeQuantity

    time_quantity__quantity: Optional[float] = None
    time_quantity__unit: Optional[Union[str, "V1p4Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.time_quantity__quantity is not None and not isinstance(self.time_quantity__quantity, float):
            self.time_quantity__quantity = float(self.time_quantity__quantity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Contributor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Contributor"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Contributor"
    class_name: ClassVar[str] = "V1p4_Contributor"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Contributor

    contributor__contributor_id: str = None
    contributor__name: str = None
    contributor__orcid_id: Optional[Union[str, "V1p4OrcidId"]] = None
    contributor__affiliation: Optional[Union[str, "V1p4Affiliation"]] = None
    contributor__affiliation_department: Optional[str] = None
    contributor__contributions: Optional[Union[Union[dict, "V1p4ContributorContribution"], List[Union[dict, "V1p4ContributorContribution"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.contributor__contributor_id):
            self.MissingRequiredField("contributor__contributor_id")
        if not isinstance(self.contributor__contributor_id, str):
            self.contributor__contributor_id = str(self.contributor__contributor_id)

        if self._is_empty(self.contributor__name):
            self.MissingRequiredField("contributor__name")
        if not isinstance(self.contributor__name, str):
            self.contributor__name = str(self.contributor__name)

        if self.contributor__affiliation_department is not None and not isinstance(self.contributor__affiliation_department, str):
            self.contributor__affiliation_department = str(self.contributor__affiliation_department)

        self._normalize_inlined_as_dict(slot_name="contributor__contributions", slot_type=V1p4ContributorContribution, key_name="contributor_contribution__role", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4ContributorContribution(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4ContributorContribution"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4ContributorContribution"
    class_name: ClassVar[str] = "V1p4_ContributorContribution"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4ContributorContribution

    contributor_contribution__role: Union[str, "V1p4Role"] = None
    contributor_contribution__degree: Optional[Union[str, "V1p4Degree"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.contributor_contribution__role):
            self.MissingRequiredField("contributor_contribution__role")
        if not isinstance(self.contributor_contribution__role, V1p4Role):
            self.contributor_contribution__role = V1p4Role(self.contributor_contribution__role)

        if self.contributor_contribution__degree is not None and not isinstance(self.contributor_contribution__degree, V1p4Degree):
            self.contributor_contribution__degree = V1p4Degree(self.contributor_contribution__degree)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4RearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4RearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4RearrangedSequence"
    class_name: ClassVar[str] = "V1p4_RearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4RearrangedSequence

    rearranged_sequence__sequence_id: str = None
    rearranged_sequence__sequence: str = None
    rearranged_sequence__derivation: Union[str, "V1p4Derivation"] = None
    rearranged_sequence__observation_type: Union[str, "V1p4ObservationType"] = None
    rearranged_sequence__repository_name: str = None
    rearranged_sequence__deposited_version: str = None
    rearranged_sequence__curation: Optional[str] = None
    rearranged_sequence__repository_ref: Optional[str] = None
    rearranged_sequence__sequence_start: Optional[int] = None
    rearranged_sequence__sequence_end: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.rearranged_sequence__sequence_id):
            self.MissingRequiredField("rearranged_sequence__sequence_id")
        if not isinstance(self.rearranged_sequence__sequence_id, str):
            self.rearranged_sequence__sequence_id = str(self.rearranged_sequence__sequence_id)

        if self._is_empty(self.rearranged_sequence__sequence):
            self.MissingRequiredField("rearranged_sequence__sequence")
        if not isinstance(self.rearranged_sequence__sequence, str):
            self.rearranged_sequence__sequence = str(self.rearranged_sequence__sequence)

        if self._is_empty(self.rearranged_sequence__derivation):
            self.MissingRequiredField("rearranged_sequence__derivation")
        if not isinstance(self.rearranged_sequence__derivation, V1p4Derivation):
            self.rearranged_sequence__derivation = V1p4Derivation(self.rearranged_sequence__derivation)

        if self._is_empty(self.rearranged_sequence__observation_type):
            self.MissingRequiredField("rearranged_sequence__observation_type")
        if not isinstance(self.rearranged_sequence__observation_type, V1p4ObservationType):
            self.rearranged_sequence__observation_type = V1p4ObservationType(self.rearranged_sequence__observation_type)

        if self._is_empty(self.rearranged_sequence__repository_name):
            self.MissingRequiredField("rearranged_sequence__repository_name")
        if not isinstance(self.rearranged_sequence__repository_name, str):
            self.rearranged_sequence__repository_name = str(self.rearranged_sequence__repository_name)

        if self._is_empty(self.rearranged_sequence__deposited_version):
            self.MissingRequiredField("rearranged_sequence__deposited_version")
        if not isinstance(self.rearranged_sequence__deposited_version, str):
            self.rearranged_sequence__deposited_version = str(self.rearranged_sequence__deposited_version)

        if self.rearranged_sequence__curation is not None and not isinstance(self.rearranged_sequence__curation, str):
            self.rearranged_sequence__curation = str(self.rearranged_sequence__curation)

        if self.rearranged_sequence__repository_ref is not None and not isinstance(self.rearranged_sequence__repository_ref, str):
            self.rearranged_sequence__repository_ref = str(self.rearranged_sequence__repository_ref)

        if self.rearranged_sequence__sequence_start is not None and not isinstance(self.rearranged_sequence__sequence_start, int):
            self.rearranged_sequence__sequence_start = int(self.rearranged_sequence__sequence_start)

        if self.rearranged_sequence__sequence_end is not None and not isinstance(self.rearranged_sequence__sequence_end, int):
            self.rearranged_sequence__sequence_end = int(self.rearranged_sequence__sequence_end)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4UnrearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4UnrearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4UnrearrangedSequence"
    class_name: ClassVar[str] = "V1p4_UnrearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4UnrearrangedSequence

    unrearranged_sequence__sequence_id: str = None
    unrearranged_sequence__sequence: str = None
    unrearranged_sequence__repository_name: str = None
    unrearranged_sequence__gff_seqid: str = None
    unrearranged_sequence__gff_start: int = None
    unrearranged_sequence__gff_end: int = None
    unrearranged_sequence__strand: Union[str, "V1p4Strand"] = None
    unrearranged_sequence__curation: Optional[str] = None
    unrearranged_sequence__repository_ref: Optional[str] = None
    unrearranged_sequence__patch_no: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.unrearranged_sequence__sequence_id):
            self.MissingRequiredField("unrearranged_sequence__sequence_id")
        if not isinstance(self.unrearranged_sequence__sequence_id, str):
            self.unrearranged_sequence__sequence_id = str(self.unrearranged_sequence__sequence_id)

        if self._is_empty(self.unrearranged_sequence__sequence):
            self.MissingRequiredField("unrearranged_sequence__sequence")
        if not isinstance(self.unrearranged_sequence__sequence, str):
            self.unrearranged_sequence__sequence = str(self.unrearranged_sequence__sequence)

        if self._is_empty(self.unrearranged_sequence__repository_name):
            self.MissingRequiredField("unrearranged_sequence__repository_name")
        if not isinstance(self.unrearranged_sequence__repository_name, str):
            self.unrearranged_sequence__repository_name = str(self.unrearranged_sequence__repository_name)

        if self._is_empty(self.unrearranged_sequence__gff_seqid):
            self.MissingRequiredField("unrearranged_sequence__gff_seqid")
        if not isinstance(self.unrearranged_sequence__gff_seqid, str):
            self.unrearranged_sequence__gff_seqid = str(self.unrearranged_sequence__gff_seqid)

        if self._is_empty(self.unrearranged_sequence__gff_start):
            self.MissingRequiredField("unrearranged_sequence__gff_start")
        if not isinstance(self.unrearranged_sequence__gff_start, int):
            self.unrearranged_sequence__gff_start = int(self.unrearranged_sequence__gff_start)

        if self._is_empty(self.unrearranged_sequence__gff_end):
            self.MissingRequiredField("unrearranged_sequence__gff_end")
        if not isinstance(self.unrearranged_sequence__gff_end, int):
            self.unrearranged_sequence__gff_end = int(self.unrearranged_sequence__gff_end)

        if self._is_empty(self.unrearranged_sequence__strand):
            self.MissingRequiredField("unrearranged_sequence__strand")
        if not isinstance(self.unrearranged_sequence__strand, V1p4Strand):
            self.unrearranged_sequence__strand = V1p4Strand(self.unrearranged_sequence__strand)

        if self.unrearranged_sequence__curation is not None and not isinstance(self.unrearranged_sequence__curation, str):
            self.unrearranged_sequence__curation = str(self.unrearranged_sequence__curation)

        if self.unrearranged_sequence__repository_ref is not None and not isinstance(self.unrearranged_sequence__repository_ref, str):
            self.unrearranged_sequence__repository_ref = str(self.unrearranged_sequence__repository_ref)

        if self.unrearranged_sequence__patch_no is not None and not isinstance(self.unrearranged_sequence__patch_no, str):
            self.unrearranged_sequence__patch_no = str(self.unrearranged_sequence__patch_no)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SequenceDelineationV(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SequenceDelineationV"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SequenceDelineationV"
    class_name: ClassVar[str] = "V1p4_SequenceDelineationV"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SequenceDelineationV

    sequence_delineation_v__sequence_delineation_id: str = None
    sequence_delineation_v__delineation_scheme: str = None
    sequence_delineation_v__fwr1_start: int = None
    sequence_delineation_v__fwr1_end: int = None
    sequence_delineation_v__cdr1_start: int = None
    sequence_delineation_v__cdr1_end: int = None
    sequence_delineation_v__fwr2_start: int = None
    sequence_delineation_v__fwr2_end: int = None
    sequence_delineation_v__cdr2_start: int = None
    sequence_delineation_v__cdr2_end: int = None
    sequence_delineation_v__fwr3_start: int = None
    sequence_delineation_v__fwr3_end: int = None
    sequence_delineation_v__cdr3_start: int = None
    sequence_delineation_v__unaligned_sequence: Optional[str] = None
    sequence_delineation_v__aligned_sequence: Optional[str] = None
    sequence_delineation_v__alignment_labels: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sequence_delineation_v__sequence_delineation_id):
            self.MissingRequiredField("sequence_delineation_v__sequence_delineation_id")
        if not isinstance(self.sequence_delineation_v__sequence_delineation_id, str):
            self.sequence_delineation_v__sequence_delineation_id = str(self.sequence_delineation_v__sequence_delineation_id)

        if self._is_empty(self.sequence_delineation_v__delineation_scheme):
            self.MissingRequiredField("sequence_delineation_v__delineation_scheme")
        if not isinstance(self.sequence_delineation_v__delineation_scheme, str):
            self.sequence_delineation_v__delineation_scheme = str(self.sequence_delineation_v__delineation_scheme)

        if self._is_empty(self.sequence_delineation_v__fwr1_start):
            self.MissingRequiredField("sequence_delineation_v__fwr1_start")
        if not isinstance(self.sequence_delineation_v__fwr1_start, int):
            self.sequence_delineation_v__fwr1_start = int(self.sequence_delineation_v__fwr1_start)

        if self._is_empty(self.sequence_delineation_v__fwr1_end):
            self.MissingRequiredField("sequence_delineation_v__fwr1_end")
        if not isinstance(self.sequence_delineation_v__fwr1_end, int):
            self.sequence_delineation_v__fwr1_end = int(self.sequence_delineation_v__fwr1_end)

        if self._is_empty(self.sequence_delineation_v__cdr1_start):
            self.MissingRequiredField("sequence_delineation_v__cdr1_start")
        if not isinstance(self.sequence_delineation_v__cdr1_start, int):
            self.sequence_delineation_v__cdr1_start = int(self.sequence_delineation_v__cdr1_start)

        if self._is_empty(self.sequence_delineation_v__cdr1_end):
            self.MissingRequiredField("sequence_delineation_v__cdr1_end")
        if not isinstance(self.sequence_delineation_v__cdr1_end, int):
            self.sequence_delineation_v__cdr1_end = int(self.sequence_delineation_v__cdr1_end)

        if self._is_empty(self.sequence_delineation_v__fwr2_start):
            self.MissingRequiredField("sequence_delineation_v__fwr2_start")
        if not isinstance(self.sequence_delineation_v__fwr2_start, int):
            self.sequence_delineation_v__fwr2_start = int(self.sequence_delineation_v__fwr2_start)

        if self._is_empty(self.sequence_delineation_v__fwr2_end):
            self.MissingRequiredField("sequence_delineation_v__fwr2_end")
        if not isinstance(self.sequence_delineation_v__fwr2_end, int):
            self.sequence_delineation_v__fwr2_end = int(self.sequence_delineation_v__fwr2_end)

        if self._is_empty(self.sequence_delineation_v__cdr2_start):
            self.MissingRequiredField("sequence_delineation_v__cdr2_start")
        if not isinstance(self.sequence_delineation_v__cdr2_start, int):
            self.sequence_delineation_v__cdr2_start = int(self.sequence_delineation_v__cdr2_start)

        if self._is_empty(self.sequence_delineation_v__cdr2_end):
            self.MissingRequiredField("sequence_delineation_v__cdr2_end")
        if not isinstance(self.sequence_delineation_v__cdr2_end, int):
            self.sequence_delineation_v__cdr2_end = int(self.sequence_delineation_v__cdr2_end)

        if self._is_empty(self.sequence_delineation_v__fwr3_start):
            self.MissingRequiredField("sequence_delineation_v__fwr3_start")
        if not isinstance(self.sequence_delineation_v__fwr3_start, int):
            self.sequence_delineation_v__fwr3_start = int(self.sequence_delineation_v__fwr3_start)

        if self._is_empty(self.sequence_delineation_v__fwr3_end):
            self.MissingRequiredField("sequence_delineation_v__fwr3_end")
        if not isinstance(self.sequence_delineation_v__fwr3_end, int):
            self.sequence_delineation_v__fwr3_end = int(self.sequence_delineation_v__fwr3_end)

        if self._is_empty(self.sequence_delineation_v__cdr3_start):
            self.MissingRequiredField("sequence_delineation_v__cdr3_start")
        if not isinstance(self.sequence_delineation_v__cdr3_start, int):
            self.sequence_delineation_v__cdr3_start = int(self.sequence_delineation_v__cdr3_start)

        if self.sequence_delineation_v__unaligned_sequence is not None and not isinstance(self.sequence_delineation_v__unaligned_sequence, str):
            self.sequence_delineation_v__unaligned_sequence = str(self.sequence_delineation_v__unaligned_sequence)

        if self.sequence_delineation_v__aligned_sequence is not None and not isinstance(self.sequence_delineation_v__aligned_sequence, str):
            self.sequence_delineation_v__aligned_sequence = str(self.sequence_delineation_v__aligned_sequence)

        if not isinstance(self.sequence_delineation_v__alignment_labels, list):
            self.sequence_delineation_v__alignment_labels = [self.sequence_delineation_v__alignment_labels] if self.sequence_delineation_v__alignment_labels is not None else []
        self.sequence_delineation_v__alignment_labels = [v if isinstance(v, str) else str(v) for v in self.sequence_delineation_v__alignment_labels]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4AlleleDescription(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4AlleleDescription"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4AlleleDescription"
    class_name: ClassVar[str] = "V1p4_AlleleDescription"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4AlleleDescription

    allele_description__allele_description_id: str = None
    allele_description__acknowledgements: Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]] = None
    allele_description__release_version: int = None
    allele_description__release_date: str = None
    allele_description__release_description: str = None
    allele_description__sequence: str = None
    allele_description__coding_sequence: str = None
    allele_description__locus: Union[str, "V1p4Locus"] = None
    allele_description__sequence_type: Union[str, "V1p4SequenceType"] = None
    allele_description__functional: Union[bool, Bool] = None
    allele_description__inference_type: Union[str, "V1p4InferenceType"] = None
    allele_description__species: Union[str, "V1p4Species"] = None
    allele_description__allele_description_ref: Optional[str] = None
    allele_description__label: Optional[str] = None
    allele_description__aliases: Optional[Union[str, List[str]]] = empty_list()
    allele_description__chromosome: Optional[int] = None
    allele_description__species_subgroup: Optional[str] = None
    allele_description__species_subgroup_type: Optional[Union[str, "V1p4SpeciesSubgroupType"]] = None
    allele_description__status: Optional[Union[str, "V1p4Status"]] = None
    allele_description__subgroup_designation: Optional[str] = None
    allele_description__gene_designation: Optional[str] = None
    allele_description__allele_designation: Optional[str] = None
    allele_description__allele_similarity_cluster_designation: Optional[str] = None
    allele_description__allele_similarity_cluster_member_id: Optional[str] = None
    allele_description__j_codon_frame: Optional[Union[str, "V1p4JCodonFrame"]] = None
    allele_description__gene_start: Optional[int] = None
    allele_description__gene_end: Optional[int] = None
    allele_description__utr_5_prime_start: Optional[int] = None
    allele_description__utr_5_prime_end: Optional[int] = None
    allele_description__leader_1_start: Optional[int] = None
    allele_description__leader_1_end: Optional[int] = None
    allele_description__leader_2_start: Optional[int] = None
    allele_description__leader_2_end: Optional[int] = None
    allele_description__v_rs_start: Optional[int] = None
    allele_description__v_rs_end: Optional[int] = None
    allele_description__d_rs_3_prime_start: Optional[int] = None
    allele_description__d_rs_3_prime_end: Optional[int] = None
    allele_description__d_rs_5_prime_start: Optional[int] = None
    allele_description__d_rs_5_prime_end: Optional[int] = None
    allele_description__j_cdr3_end: Optional[int] = None
    allele_description__j_rs_start: Optional[int] = None
    allele_description__j_rs_end: Optional[int] = None
    allele_description__j_donor_splice: Optional[int] = None
    allele_description__v_gene_delineations: Optional[Union[Union[dict, V1p4SequenceDelineationV], List[Union[dict, V1p4SequenceDelineationV]]]] = empty_list()
    allele_description__unrearranged_support: Optional[Union[Union[dict, V1p4UnrearrangedSequence], List[Union[dict, V1p4UnrearrangedSequence]]]] = empty_list()
    allele_description__rearranged_support: Optional[Union[Union[dict, V1p4RearrangedSequence], List[Union[dict, V1p4RearrangedSequence]]]] = empty_list()
    allele_description__paralogs: Optional[Union[str, List[str]]] = empty_list()
    allele_description__curation: Optional[str] = None
    allele_description__curational_tags: Optional[Union[Union[str, "V1p4CurationalTags"], List[Union[str, "V1p4CurationalTags"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.allele_description__allele_description_id):
            self.MissingRequiredField("allele_description__allele_description_id")
        if not isinstance(self.allele_description__allele_description_id, str):
            self.allele_description__allele_description_id = str(self.allele_description__allele_description_id)

        if self._is_empty(self.allele_description__acknowledgements):
            self.MissingRequiredField("allele_description__acknowledgements")
        self._normalize_inlined_as_dict(slot_name="allele_description__acknowledgements", slot_type=V1p4Contributor, key_name="contributor__contributor_id", keyed=False)

        if self._is_empty(self.allele_description__release_version):
            self.MissingRequiredField("allele_description__release_version")
        if not isinstance(self.allele_description__release_version, int):
            self.allele_description__release_version = int(self.allele_description__release_version)

        if self._is_empty(self.allele_description__release_date):
            self.MissingRequiredField("allele_description__release_date")
        if not isinstance(self.allele_description__release_date, str):
            self.allele_description__release_date = str(self.allele_description__release_date)

        if self._is_empty(self.allele_description__release_description):
            self.MissingRequiredField("allele_description__release_description")
        if not isinstance(self.allele_description__release_description, str):
            self.allele_description__release_description = str(self.allele_description__release_description)

        if self._is_empty(self.allele_description__sequence):
            self.MissingRequiredField("allele_description__sequence")
        if not isinstance(self.allele_description__sequence, str):
            self.allele_description__sequence = str(self.allele_description__sequence)

        if self._is_empty(self.allele_description__coding_sequence):
            self.MissingRequiredField("allele_description__coding_sequence")
        if not isinstance(self.allele_description__coding_sequence, str):
            self.allele_description__coding_sequence = str(self.allele_description__coding_sequence)

        if self._is_empty(self.allele_description__locus):
            self.MissingRequiredField("allele_description__locus")
        if not isinstance(self.allele_description__locus, V1p4Locus):
            self.allele_description__locus = V1p4Locus(self.allele_description__locus)

        if self._is_empty(self.allele_description__sequence_type):
            self.MissingRequiredField("allele_description__sequence_type")
        if not isinstance(self.allele_description__sequence_type, V1p4SequenceType):
            self.allele_description__sequence_type = V1p4SequenceType(self.allele_description__sequence_type)

        if self._is_empty(self.allele_description__functional):
            self.MissingRequiredField("allele_description__functional")
        if not isinstance(self.allele_description__functional, Bool):
            self.allele_description__functional = Bool(self.allele_description__functional)

        if self._is_empty(self.allele_description__inference_type):
            self.MissingRequiredField("allele_description__inference_type")
        if not isinstance(self.allele_description__inference_type, V1p4InferenceType):
            self.allele_description__inference_type = V1p4InferenceType(self.allele_description__inference_type)

        if self.allele_description__allele_description_ref is not None and not isinstance(self.allele_description__allele_description_ref, str):
            self.allele_description__allele_description_ref = str(self.allele_description__allele_description_ref)

        if self.allele_description__label is not None and not isinstance(self.allele_description__label, str):
            self.allele_description__label = str(self.allele_description__label)

        if not isinstance(self.allele_description__aliases, list):
            self.allele_description__aliases = [self.allele_description__aliases] if self.allele_description__aliases is not None else []
        self.allele_description__aliases = [v if isinstance(v, str) else str(v) for v in self.allele_description__aliases]

        if self.allele_description__chromosome is not None and not isinstance(self.allele_description__chromosome, int):
            self.allele_description__chromosome = int(self.allele_description__chromosome)

        if self.allele_description__species_subgroup is not None and not isinstance(self.allele_description__species_subgroup, str):
            self.allele_description__species_subgroup = str(self.allele_description__species_subgroup)

        if self.allele_description__species_subgroup_type is not None and not isinstance(self.allele_description__species_subgroup_type, V1p4SpeciesSubgroupType):
            self.allele_description__species_subgroup_type = V1p4SpeciesSubgroupType(self.allele_description__species_subgroup_type)

        if self.allele_description__status is not None and not isinstance(self.allele_description__status, V1p4Status):
            self.allele_description__status = V1p4Status(self.allele_description__status)

        if self.allele_description__subgroup_designation is not None and not isinstance(self.allele_description__subgroup_designation, str):
            self.allele_description__subgroup_designation = str(self.allele_description__subgroup_designation)

        if self.allele_description__gene_designation is not None and not isinstance(self.allele_description__gene_designation, str):
            self.allele_description__gene_designation = str(self.allele_description__gene_designation)

        if self.allele_description__allele_designation is not None and not isinstance(self.allele_description__allele_designation, str):
            self.allele_description__allele_designation = str(self.allele_description__allele_designation)

        if self.allele_description__allele_similarity_cluster_designation is not None and not isinstance(self.allele_description__allele_similarity_cluster_designation, str):
            self.allele_description__allele_similarity_cluster_designation = str(self.allele_description__allele_similarity_cluster_designation)

        if self.allele_description__allele_similarity_cluster_member_id is not None and not isinstance(self.allele_description__allele_similarity_cluster_member_id, str):
            self.allele_description__allele_similarity_cluster_member_id = str(self.allele_description__allele_similarity_cluster_member_id)

        if self.allele_description__j_codon_frame is not None and not isinstance(self.allele_description__j_codon_frame, V1p4JCodonFrame):
            self.allele_description__j_codon_frame = V1p4JCodonFrame(self.allele_description__j_codon_frame)

        if self.allele_description__gene_start is not None and not isinstance(self.allele_description__gene_start, int):
            self.allele_description__gene_start = int(self.allele_description__gene_start)

        if self.allele_description__gene_end is not None and not isinstance(self.allele_description__gene_end, int):
            self.allele_description__gene_end = int(self.allele_description__gene_end)

        if self.allele_description__utr_5_prime_start is not None and not isinstance(self.allele_description__utr_5_prime_start, int):
            self.allele_description__utr_5_prime_start = int(self.allele_description__utr_5_prime_start)

        if self.allele_description__utr_5_prime_end is not None and not isinstance(self.allele_description__utr_5_prime_end, int):
            self.allele_description__utr_5_prime_end = int(self.allele_description__utr_5_prime_end)

        if self.allele_description__leader_1_start is not None and not isinstance(self.allele_description__leader_1_start, int):
            self.allele_description__leader_1_start = int(self.allele_description__leader_1_start)

        if self.allele_description__leader_1_end is not None and not isinstance(self.allele_description__leader_1_end, int):
            self.allele_description__leader_1_end = int(self.allele_description__leader_1_end)

        if self.allele_description__leader_2_start is not None and not isinstance(self.allele_description__leader_2_start, int):
            self.allele_description__leader_2_start = int(self.allele_description__leader_2_start)

        if self.allele_description__leader_2_end is not None and not isinstance(self.allele_description__leader_2_end, int):
            self.allele_description__leader_2_end = int(self.allele_description__leader_2_end)

        if self.allele_description__v_rs_start is not None and not isinstance(self.allele_description__v_rs_start, int):
            self.allele_description__v_rs_start = int(self.allele_description__v_rs_start)

        if self.allele_description__v_rs_end is not None and not isinstance(self.allele_description__v_rs_end, int):
            self.allele_description__v_rs_end = int(self.allele_description__v_rs_end)

        if self.allele_description__d_rs_3_prime_start is not None and not isinstance(self.allele_description__d_rs_3_prime_start, int):
            self.allele_description__d_rs_3_prime_start = int(self.allele_description__d_rs_3_prime_start)

        if self.allele_description__d_rs_3_prime_end is not None and not isinstance(self.allele_description__d_rs_3_prime_end, int):
            self.allele_description__d_rs_3_prime_end = int(self.allele_description__d_rs_3_prime_end)

        if self.allele_description__d_rs_5_prime_start is not None and not isinstance(self.allele_description__d_rs_5_prime_start, int):
            self.allele_description__d_rs_5_prime_start = int(self.allele_description__d_rs_5_prime_start)

        if self.allele_description__d_rs_5_prime_end is not None and not isinstance(self.allele_description__d_rs_5_prime_end, int):
            self.allele_description__d_rs_5_prime_end = int(self.allele_description__d_rs_5_prime_end)

        if self.allele_description__j_cdr3_end is not None and not isinstance(self.allele_description__j_cdr3_end, int):
            self.allele_description__j_cdr3_end = int(self.allele_description__j_cdr3_end)

        if self.allele_description__j_rs_start is not None and not isinstance(self.allele_description__j_rs_start, int):
            self.allele_description__j_rs_start = int(self.allele_description__j_rs_start)

        if self.allele_description__j_rs_end is not None and not isinstance(self.allele_description__j_rs_end, int):
            self.allele_description__j_rs_end = int(self.allele_description__j_rs_end)

        if self.allele_description__j_donor_splice is not None and not isinstance(self.allele_description__j_donor_splice, int):
            self.allele_description__j_donor_splice = int(self.allele_description__j_donor_splice)

        self._normalize_inlined_as_dict(slot_name="allele_description__v_gene_delineations", slot_type=V1p4SequenceDelineationV, key_name="sequence_delineation_v__sequence_delineation_id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_description__unrearranged_support", slot_type=V1p4UnrearrangedSequence, key_name="unrearranged_sequence__sequence_id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="allele_description__rearranged_support", slot_type=V1p4RearrangedSequence, key_name="rearranged_sequence__sequence_id", keyed=False)

        if not isinstance(self.allele_description__paralogs, list):
            self.allele_description__paralogs = [self.allele_description__paralogs] if self.allele_description__paralogs is not None else []
        self.allele_description__paralogs = [v if isinstance(v, str) else str(v) for v in self.allele_description__paralogs]

        if self.allele_description__curation is not None and not isinstance(self.allele_description__curation, str):
            self.allele_description__curation = str(self.allele_description__curation)

        if not isinstance(self.allele_description__curational_tags, list):
            self.allele_description__curational_tags = [self.allele_description__curational_tags] if self.allele_description__curational_tags is not None else []
        self.allele_description__curational_tags = [v if isinstance(v, V1p4CurationalTags) else V1p4CurationalTags(v) for v in self.allele_description__curational_tags]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4GermlineSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4GermlineSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4GermlineSet"
    class_name: ClassVar[str] = "V1p4_GermlineSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4GermlineSet

    germline_set__germline_set_id: str = None
    germline_set__acknowledgements: Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]] = None
    germline_set__release_version: float = None
    germline_set__release_description: str = None
    germline_set__release_date: str = None
    germline_set__germline_set_name: str = None
    germline_set__germline_set_ref: str = None
    germline_set__species: Union[str, "V1p4Species"] = None
    germline_set__locus: Union[str, "V1p4Locus"] = None
    germline_set__allele_descriptions: Union[Union[dict, V1p4AlleleDescription], List[Union[dict, V1p4AlleleDescription]]] = None
    germline_set__pub_ids: Optional[Union[str, List[str]]] = empty_list()
    germline_set__species_subgroup: Optional[str] = None
    germline_set__species_subgroup_type: Optional[Union[str, "V1p4SpeciesSubgroupType"]] = None
    germline_set__curation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.germline_set__germline_set_id):
            self.MissingRequiredField("germline_set__germline_set_id")
        if not isinstance(self.germline_set__germline_set_id, str):
            self.germline_set__germline_set_id = str(self.germline_set__germline_set_id)

        if self._is_empty(self.germline_set__acknowledgements):
            self.MissingRequiredField("germline_set__acknowledgements")
        self._normalize_inlined_as_dict(slot_name="germline_set__acknowledgements", slot_type=V1p4Contributor, key_name="contributor__contributor_id", keyed=False)

        if self._is_empty(self.germline_set__release_version):
            self.MissingRequiredField("germline_set__release_version")
        if not isinstance(self.germline_set__release_version, float):
            self.germline_set__release_version = float(self.germline_set__release_version)

        if self._is_empty(self.germline_set__release_description):
            self.MissingRequiredField("germline_set__release_description")
        if not isinstance(self.germline_set__release_description, str):
            self.germline_set__release_description = str(self.germline_set__release_description)

        if self._is_empty(self.germline_set__release_date):
            self.MissingRequiredField("germline_set__release_date")
        if not isinstance(self.germline_set__release_date, str):
            self.germline_set__release_date = str(self.germline_set__release_date)

        if self._is_empty(self.germline_set__germline_set_name):
            self.MissingRequiredField("germline_set__germline_set_name")
        if not isinstance(self.germline_set__germline_set_name, str):
            self.germline_set__germline_set_name = str(self.germline_set__germline_set_name)

        if self._is_empty(self.germline_set__germline_set_ref):
            self.MissingRequiredField("germline_set__germline_set_ref")
        if not isinstance(self.germline_set__germline_set_ref, str):
            self.germline_set__germline_set_ref = str(self.germline_set__germline_set_ref)

        if self._is_empty(self.germline_set__locus):
            self.MissingRequiredField("germline_set__locus")
        if not isinstance(self.germline_set__locus, V1p4Locus):
            self.germline_set__locus = V1p4Locus(self.germline_set__locus)

        if self._is_empty(self.germline_set__allele_descriptions):
            self.MissingRequiredField("germline_set__allele_descriptions")
        self._normalize_inlined_as_dict(slot_name="germline_set__allele_descriptions", slot_type=V1p4AlleleDescription, key_name="allele_description__allele_description_id", keyed=False)

        if not isinstance(self.germline_set__pub_ids, list):
            self.germline_set__pub_ids = [self.germline_set__pub_ids] if self.germline_set__pub_ids is not None else []
        self.germline_set__pub_ids = [v if isinstance(v, str) else str(v) for v in self.germline_set__pub_ids]

        if self.germline_set__species_subgroup is not None and not isinstance(self.germline_set__species_subgroup, str):
            self.germline_set__species_subgroup = str(self.germline_set__species_subgroup)

        if self.germline_set__species_subgroup_type is not None and not isinstance(self.germline_set__species_subgroup_type, V1p4SpeciesSubgroupType):
            self.germline_set__species_subgroup_type = V1p4SpeciesSubgroupType(self.germline_set__species_subgroup_type)

        if self.germline_set__curation is not None and not isinstance(self.germline_set__curation, str):
            self.germline_set__curation = str(self.germline_set__curation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4GenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4GenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4GenotypeSet"
    class_name: ClassVar[str] = "V1p4_GenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4GenotypeSet

    genotype_set__receptor_genotype_set_id: str = None
    genotype_set__genotype_class_list: Optional[Union[Union[dict, "V1p4Genotype"], List[Union[dict, "V1p4Genotype"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.genotype_set__receptor_genotype_set_id):
            self.MissingRequiredField("genotype_set__receptor_genotype_set_id")
        if not isinstance(self.genotype_set__receptor_genotype_set_id, str):
            self.genotype_set__receptor_genotype_set_id = str(self.genotype_set__receptor_genotype_set_id)

        self._normalize_inlined_as_dict(slot_name="genotype_set__genotype_class_list", slot_type=V1p4Genotype, key_name="genotype__receptor_genotype_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Genotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Genotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Genotype"
    class_name: ClassVar[str] = "V1p4_Genotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Genotype

    genotype__receptor_genotype_id: str = None
    genotype__locus: Union[str, "V1p4Locus"] = None
    genotype__documented_alleles: Optional[Union[Union[dict, "V1p4DocumentedAllele"], List[Union[dict, "V1p4DocumentedAllele"]]]] = empty_list()
    genotype__undocumented_alleles: Optional[Union[Union[dict, "V1p4UndocumentedAllele"], List[Union[dict, "V1p4UndocumentedAllele"]]]] = empty_list()
    genotype__deleted_genes: Optional[Union[Union[dict, "V1p4DeletedGene"], List[Union[dict, "V1p4DeletedGene"]]]] = empty_list()
    genotype__inference_process: Optional[Union[str, "V1p4InferenceProcess"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.genotype__receptor_genotype_id):
            self.MissingRequiredField("genotype__receptor_genotype_id")
        if not isinstance(self.genotype__receptor_genotype_id, str):
            self.genotype__receptor_genotype_id = str(self.genotype__receptor_genotype_id)

        if self._is_empty(self.genotype__locus):
            self.MissingRequiredField("genotype__locus")
        if not isinstance(self.genotype__locus, V1p4Locus):
            self.genotype__locus = V1p4Locus(self.genotype__locus)

        self._normalize_inlined_as_dict(slot_name="genotype__documented_alleles", slot_type=V1p4DocumentedAllele, key_name="documented_allele__label", keyed=False)

        self._normalize_inlined_as_dict(slot_name="genotype__undocumented_alleles", slot_type=V1p4UndocumentedAllele, key_name="undocumented_allele__allele_name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="genotype__deleted_genes", slot_type=V1p4DeletedGene, key_name="deleted_gene__label", keyed=False)

        if self.genotype__inference_process is not None and not isinstance(self.genotype__inference_process, V1p4InferenceProcess):
            self.genotype__inference_process = V1p4InferenceProcess(self.genotype__inference_process)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4DocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4DocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4DocumentedAllele"
    class_name: ClassVar[str] = "V1p4_DocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4DocumentedAllele

    documented_allele__label: str = None
    documented_allele__germline_set_ref: str = None
    documented_allele__phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.documented_allele__label):
            self.MissingRequiredField("documented_allele__label")
        if not isinstance(self.documented_allele__label, str):
            self.documented_allele__label = str(self.documented_allele__label)

        if self._is_empty(self.documented_allele__germline_set_ref):
            self.MissingRequiredField("documented_allele__germline_set_ref")
        if not isinstance(self.documented_allele__germline_set_ref, str):
            self.documented_allele__germline_set_ref = str(self.documented_allele__germline_set_ref)

        if self.documented_allele__phasing is not None and not isinstance(self.documented_allele__phasing, int):
            self.documented_allele__phasing = int(self.documented_allele__phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4UndocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4UndocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4UndocumentedAllele"
    class_name: ClassVar[str] = "V1p4_UndocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4UndocumentedAllele

    undocumented_allele__allele_name: str = None
    undocumented_allele__sequence: str = None
    undocumented_allele__phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.undocumented_allele__allele_name):
            self.MissingRequiredField("undocumented_allele__allele_name")
        if not isinstance(self.undocumented_allele__allele_name, str):
            self.undocumented_allele__allele_name = str(self.undocumented_allele__allele_name)

        if self._is_empty(self.undocumented_allele__sequence):
            self.MissingRequiredField("undocumented_allele__sequence")
        if not isinstance(self.undocumented_allele__sequence, str):
            self.undocumented_allele__sequence = str(self.undocumented_allele__sequence)

        if self.undocumented_allele__phasing is not None and not isinstance(self.undocumented_allele__phasing, int):
            self.undocumented_allele__phasing = int(self.undocumented_allele__phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4DeletedGene(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4DeletedGene"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4DeletedGene"
    class_name: ClassVar[str] = "V1p4_DeletedGene"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4DeletedGene

    deleted_gene__label: str = None
    deleted_gene__germline_set_ref: str = None
    deleted_gene__phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.deleted_gene__label):
            self.MissingRequiredField("deleted_gene__label")
        if not isinstance(self.deleted_gene__label, str):
            self.deleted_gene__label = str(self.deleted_gene__label)

        if self._is_empty(self.deleted_gene__germline_set_ref):
            self.MissingRequiredField("deleted_gene__germline_set_ref")
        if not isinstance(self.deleted_gene__germline_set_ref, str):
            self.deleted_gene__germline_set_ref = str(self.deleted_gene__germline_set_ref)

        if self.deleted_gene__phasing is not None and not isinstance(self.deleted_gene__phasing, int):
            self.deleted_gene__phasing = int(self.deleted_gene__phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4MHCGenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4MHCGenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4MHCGenotypeSet"
    class_name: ClassVar[str] = "V1p4_MHCGenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4MHCGenotypeSet

    m_h_c_genotype_set__mhc_genotype_set_id: str = None
    m_h_c_genotype_set__mhc_genotype_list: Union[Union[dict, "V1p4MHCGenotype"], List[Union[dict, "V1p4MHCGenotype"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.m_h_c_genotype_set__mhc_genotype_set_id):
            self.MissingRequiredField("m_h_c_genotype_set__mhc_genotype_set_id")
        if not isinstance(self.m_h_c_genotype_set__mhc_genotype_set_id, str):
            self.m_h_c_genotype_set__mhc_genotype_set_id = str(self.m_h_c_genotype_set__mhc_genotype_set_id)

        if self._is_empty(self.m_h_c_genotype_set__mhc_genotype_list):
            self.MissingRequiredField("m_h_c_genotype_set__mhc_genotype_list")
        self._normalize_inlined_as_dict(slot_name="m_h_c_genotype_set__mhc_genotype_list", slot_type=V1p4MHCGenotype, key_name="m_h_c_genotype__mhc_genotype_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4MHCGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4MHCGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4MHCGenotype"
    class_name: ClassVar[str] = "V1p4_MHCGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4MHCGenotype

    m_h_c_genotype__mhc_genotype_id: str = None
    m_h_c_genotype__mhc_class: Union[str, "V1p4MhcClass"] = None
    m_h_c_genotype__mhc_alleles: Union[Union[dict, "V1p4MHCAllele"], List[Union[dict, "V1p4MHCAllele"]]] = None
    m_h_c_genotype__mhc_genotyping_method: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.m_h_c_genotype__mhc_genotype_id):
            self.MissingRequiredField("m_h_c_genotype__mhc_genotype_id")
        if not isinstance(self.m_h_c_genotype__mhc_genotype_id, str):
            self.m_h_c_genotype__mhc_genotype_id = str(self.m_h_c_genotype__mhc_genotype_id)

        if self._is_empty(self.m_h_c_genotype__mhc_class):
            self.MissingRequiredField("m_h_c_genotype__mhc_class")
        if not isinstance(self.m_h_c_genotype__mhc_class, V1p4MhcClass):
            self.m_h_c_genotype__mhc_class = V1p4MhcClass(self.m_h_c_genotype__mhc_class)

        if self._is_empty(self.m_h_c_genotype__mhc_alleles):
            self.MissingRequiredField("m_h_c_genotype__mhc_alleles")
        if not isinstance(self.m_h_c_genotype__mhc_alleles, list):
            self.m_h_c_genotype__mhc_alleles = [self.m_h_c_genotype__mhc_alleles] if self.m_h_c_genotype__mhc_alleles is not None else []
        self.m_h_c_genotype__mhc_alleles = [v if isinstance(v, V1p4MHCAllele) else V1p4MHCAllele(**as_dict(v)) for v in self.m_h_c_genotype__mhc_alleles]

        if self.m_h_c_genotype__mhc_genotyping_method is not None and not isinstance(self.m_h_c_genotype__mhc_genotyping_method, str):
            self.m_h_c_genotype__mhc_genotyping_method = str(self.m_h_c_genotype__mhc_genotyping_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4MHCAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4MHCAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4MHCAllele"
    class_name: ClassVar[str] = "V1p4_MHCAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4MHCAllele

    m_h_c_allele__allele_designation: Optional[str] = None
    m_h_c_allele__gene: Optional[Union[str, "V1p4Gene"]] = None
    m_h_c_allele__reference_set_ref: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.m_h_c_allele__allele_designation is not None and not isinstance(self.m_h_c_allele__allele_designation, str):
            self.m_h_c_allele__allele_designation = str(self.m_h_c_allele__allele_designation)

        if self.m_h_c_allele__reference_set_ref is not None and not isinstance(self.m_h_c_allele__reference_set_ref, str):
            self.m_h_c_allele__reference_set_ref = str(self.m_h_c_allele__reference_set_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SubjectGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SubjectGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SubjectGenotype"
    class_name: ClassVar[str] = "V1p4_SubjectGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SubjectGenotype

    subject_genotype__receptor_genotype_set: Optional[Union[dict, V1p4GenotypeSet]] = None
    subject_genotype__mhc_genotype_set: Optional[Union[dict, V1p4MHCGenotypeSet]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject_genotype__receptor_genotype_set is not None and not isinstance(self.subject_genotype__receptor_genotype_set, V1p4GenotypeSet):
            self.subject_genotype__receptor_genotype_set = V1p4GenotypeSet(**as_dict(self.subject_genotype__receptor_genotype_set))

        if self.subject_genotype__mhc_genotype_set is not None and not isinstance(self.subject_genotype__mhc_genotype_set, V1p4MHCGenotypeSet):
            self.subject_genotype__mhc_genotype_set = V1p4MHCGenotypeSet(**as_dict(self.subject_genotype__mhc_genotype_set))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Study(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Study"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Study"
    class_name: ClassVar[str] = "V1p4_Study"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Study

    study__study_id: str = None
    study__study_title: str = None
    study__study_type: Union[str, "V1p4StudyType"] = None
    study__inclusion_exclusion_criteria: str = None
    study__grants: str = None
    study__contributors: Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]] = None
    study__pub_ids: Union[str, List[str]] = None
    study__keywords_study: Union[Union[str, "V1p4KeywordsStudy"], List[Union[str, "V1p4KeywordsStudy"]]] = None
    study__study_description: Optional[str] = None
    study__adc_publish_date: Optional[str] = None
    study__adc_update_date: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.study__study_id):
            self.MissingRequiredField("study__study_id")
        if not isinstance(self.study__study_id, str):
            self.study__study_id = str(self.study__study_id)

        if self._is_empty(self.study__study_title):
            self.MissingRequiredField("study__study_title")
        if not isinstance(self.study__study_title, str):
            self.study__study_title = str(self.study__study_title)

        if self._is_empty(self.study__inclusion_exclusion_criteria):
            self.MissingRequiredField("study__inclusion_exclusion_criteria")
        if not isinstance(self.study__inclusion_exclusion_criteria, str):
            self.study__inclusion_exclusion_criteria = str(self.study__inclusion_exclusion_criteria)

        if self._is_empty(self.study__grants):
            self.MissingRequiredField("study__grants")
        if not isinstance(self.study__grants, str):
            self.study__grants = str(self.study__grants)

        if self._is_empty(self.study__contributors):
            self.MissingRequiredField("study__contributors")
        self._normalize_inlined_as_dict(slot_name="study__contributors", slot_type=V1p4Contributor, key_name="contributor__contributor_id", keyed=False)

        if self._is_empty(self.study__pub_ids):
            self.MissingRequiredField("study__pub_ids")
        if not isinstance(self.study__pub_ids, list):
            self.study__pub_ids = [self.study__pub_ids] if self.study__pub_ids is not None else []
        self.study__pub_ids = [v if isinstance(v, str) else str(v) for v in self.study__pub_ids]

        if self._is_empty(self.study__keywords_study):
            self.MissingRequiredField("study__keywords_study")
        if not isinstance(self.study__keywords_study, list):
            self.study__keywords_study = [self.study__keywords_study] if self.study__keywords_study is not None else []
        self.study__keywords_study = [v if isinstance(v, V1p4KeywordsStudy) else V1p4KeywordsStudy(v) for v in self.study__keywords_study]

        if self.study__study_description is not None and not isinstance(self.study__study_description, str):
            self.study__study_description = str(self.study__study_description)

        if self.study__adc_publish_date is not None and not isinstance(self.study__adc_publish_date, str):
            self.study__adc_publish_date = str(self.study__adc_publish_date)

        if self.study__adc_update_date is not None and not isinstance(self.study__adc_update_date, str):
            self.study__adc_update_date = str(self.study__adc_update_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Subject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Subject"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Subject"
    class_name: ClassVar[str] = "V1p4_Subject"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Subject

    subject__subject_id: str = None
    subject__synthetic: Union[bool, Bool] = None
    subject__species: Union[str, "V1p4Species"] = None
    subject__sex: Union[str, "V1p4Sex"] = None
    subject__age: Union[dict, V1p4TimeInterval] = None
    subject__age_event: str = None
    subject__ancestry_population: Union[str, "V1p4AncestryPopulation"] = None
    subject__ethnicity: str = None
    subject__race: str = None
    subject__strain_name: str = None
    subject__linked_subjects: str = None
    subject__link_type: str = None
    subject__location_birth: Optional[Union[str, "V1p4LocationBirth"]] = None
    subject__diagnosis: Optional[Union[Union[dict, "V1p4Diagnosis"], List[Union[dict, "V1p4Diagnosis"]]]] = empty_list()
    subject__genotype: Optional[Union[dict, V1p4SubjectGenotype]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject__subject_id):
            self.MissingRequiredField("subject__subject_id")
        if not isinstance(self.subject__subject_id, str):
            self.subject__subject_id = str(self.subject__subject_id)

        if self._is_empty(self.subject__synthetic):
            self.MissingRequiredField("subject__synthetic")
        if not isinstance(self.subject__synthetic, Bool):
            self.subject__synthetic = Bool(self.subject__synthetic)

        if self._is_empty(self.subject__sex):
            self.MissingRequiredField("subject__sex")
        if not isinstance(self.subject__sex, V1p4Sex):
            self.subject__sex = V1p4Sex(self.subject__sex)

        if self._is_empty(self.subject__age):
            self.MissingRequiredField("subject__age")
        if not isinstance(self.subject__age, V1p4TimeInterval):
            self.subject__age = V1p4TimeInterval(**as_dict(self.subject__age))

        if self._is_empty(self.subject__age_event):
            self.MissingRequiredField("subject__age_event")
        if not isinstance(self.subject__age_event, str):
            self.subject__age_event = str(self.subject__age_event)

        if self._is_empty(self.subject__ethnicity):
            self.MissingRequiredField("subject__ethnicity")
        if not isinstance(self.subject__ethnicity, str):
            self.subject__ethnicity = str(self.subject__ethnicity)

        if self._is_empty(self.subject__race):
            self.MissingRequiredField("subject__race")
        if not isinstance(self.subject__race, str):
            self.subject__race = str(self.subject__race)

        if self._is_empty(self.subject__strain_name):
            self.MissingRequiredField("subject__strain_name")
        if not isinstance(self.subject__strain_name, str):
            self.subject__strain_name = str(self.subject__strain_name)

        if self._is_empty(self.subject__linked_subjects):
            self.MissingRequiredField("subject__linked_subjects")
        if not isinstance(self.subject__linked_subjects, str):
            self.subject__linked_subjects = str(self.subject__linked_subjects)

        if self._is_empty(self.subject__link_type):
            self.MissingRequiredField("subject__link_type")
        if not isinstance(self.subject__link_type, str):
            self.subject__link_type = str(self.subject__link_type)

        self._normalize_inlined_as_dict(slot_name="subject__diagnosis", slot_type=V1p4Diagnosis, key_name="diagnosis__study_group_description", keyed=False)

        if self.subject__genotype is not None and not isinstance(self.subject__genotype, V1p4SubjectGenotype):
            self.subject__genotype = V1p4SubjectGenotype(**as_dict(self.subject__genotype))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Diagnosis(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Diagnosis"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Diagnosis"
    class_name: ClassVar[str] = "V1p4_Diagnosis"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Diagnosis

    diagnosis__study_group_description: str = None
    diagnosis__disease_diagnosis: Union[str, "V1p4DiseaseDiagnosis"] = None
    diagnosis__disease_length: Union[dict, V1p4TimeQuantity] = None
    diagnosis__disease_stage: str = None
    diagnosis__prior_therapies: str = None
    diagnosis__immunogen: str = None
    diagnosis__intervention: str = None
    diagnosis__medical_history: str = None
    diagnosis__diagnosis_timepoint: Optional[Union[dict, V1p4TimePoint]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.diagnosis__study_group_description):
            self.MissingRequiredField("diagnosis__study_group_description")
        if not isinstance(self.diagnosis__study_group_description, str):
            self.diagnosis__study_group_description = str(self.diagnosis__study_group_description)

        if self._is_empty(self.diagnosis__disease_length):
            self.MissingRequiredField("diagnosis__disease_length")
        if not isinstance(self.diagnosis__disease_length, V1p4TimeQuantity):
            self.diagnosis__disease_length = V1p4TimeQuantity(**as_dict(self.diagnosis__disease_length))

        if self._is_empty(self.diagnosis__disease_stage):
            self.MissingRequiredField("diagnosis__disease_stage")
        if not isinstance(self.diagnosis__disease_stage, str):
            self.diagnosis__disease_stage = str(self.diagnosis__disease_stage)

        if self._is_empty(self.diagnosis__prior_therapies):
            self.MissingRequiredField("diagnosis__prior_therapies")
        if not isinstance(self.diagnosis__prior_therapies, str):
            self.diagnosis__prior_therapies = str(self.diagnosis__prior_therapies)

        if self._is_empty(self.diagnosis__immunogen):
            self.MissingRequiredField("diagnosis__immunogen")
        if not isinstance(self.diagnosis__immunogen, str):
            self.diagnosis__immunogen = str(self.diagnosis__immunogen)

        if self._is_empty(self.diagnosis__intervention):
            self.MissingRequiredField("diagnosis__intervention")
        if not isinstance(self.diagnosis__intervention, str):
            self.diagnosis__intervention = str(self.diagnosis__intervention)

        if self._is_empty(self.diagnosis__medical_history):
            self.MissingRequiredField("diagnosis__medical_history")
        if not isinstance(self.diagnosis__medical_history, str):
            self.diagnosis__medical_history = str(self.diagnosis__medical_history)

        if self.diagnosis__diagnosis_timepoint is not None and not isinstance(self.diagnosis__diagnosis_timepoint, V1p4TimePoint):
            self.diagnosis__diagnosis_timepoint = V1p4TimePoint(**as_dict(self.diagnosis__diagnosis_timepoint))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Sample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Sample"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Sample"
    class_name: ClassVar[str] = "V1p4_Sample"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Sample

    sample__sample_id: str = None
    sample__sample_type: str = None
    sample__tissue: Union[str, "V1p4Tissue"] = None
    sample__anatomic_site: str = None
    sample__disease_state_sample: str = None
    sample__collection_time_point_relative: Union[dict, V1p4TimePoint] = None
    sample__biomaterial_provider: str = None
    sample__collection_location: Optional[Union[str, "V1p4CollectionLocation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sample__sample_id):
            self.MissingRequiredField("sample__sample_id")
        if not isinstance(self.sample__sample_id, str):
            self.sample__sample_id = str(self.sample__sample_id)

        if self._is_empty(self.sample__sample_type):
            self.MissingRequiredField("sample__sample_type")
        if not isinstance(self.sample__sample_type, str):
            self.sample__sample_type = str(self.sample__sample_type)

        if self._is_empty(self.sample__anatomic_site):
            self.MissingRequiredField("sample__anatomic_site")
        if not isinstance(self.sample__anatomic_site, str):
            self.sample__anatomic_site = str(self.sample__anatomic_site)

        if self._is_empty(self.sample__disease_state_sample):
            self.MissingRequiredField("sample__disease_state_sample")
        if not isinstance(self.sample__disease_state_sample, str):
            self.sample__disease_state_sample = str(self.sample__disease_state_sample)

        if self._is_empty(self.sample__collection_time_point_relative):
            self.MissingRequiredField("sample__collection_time_point_relative")
        if not isinstance(self.sample__collection_time_point_relative, V1p4TimePoint):
            self.sample__collection_time_point_relative = V1p4TimePoint(**as_dict(self.sample__collection_time_point_relative))

        if self._is_empty(self.sample__biomaterial_provider):
            self.MissingRequiredField("sample__biomaterial_provider")
        if not isinstance(self.sample__biomaterial_provider, str):
            self.sample__biomaterial_provider = str(self.sample__biomaterial_provider)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4CellProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4CellProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4CellProcessing"
    class_name: ClassVar[str] = "V1p4_CellProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4CellProcessing

    cell_processing__tissue_processing: str = None
    cell_processing__cell_subset: Union[str, "V1p4CellSubset"] = None
    cell_processing__cell_phenotype: str = None
    cell_processing__single_cell: Union[bool, Bool] = None
    cell_processing__cell_number: int = None
    cell_processing__cells_per_reaction: int = None
    cell_processing__cell_storage: Union[bool, Bool] = None
    cell_processing__cell_quality: str = None
    cell_processing__cell_isolation: str = None
    cell_processing__cell_processing_protocol: str = None
    cell_processing__cell_label: Optional[str] = None
    cell_processing__cell_species: Optional[Union[str, "V1p4CellSpecies"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.cell_processing__tissue_processing):
            self.MissingRequiredField("cell_processing__tissue_processing")
        if not isinstance(self.cell_processing__tissue_processing, str):
            self.cell_processing__tissue_processing = str(self.cell_processing__tissue_processing)

        if self._is_empty(self.cell_processing__cell_phenotype):
            self.MissingRequiredField("cell_processing__cell_phenotype")
        if not isinstance(self.cell_processing__cell_phenotype, str):
            self.cell_processing__cell_phenotype = str(self.cell_processing__cell_phenotype)

        if self._is_empty(self.cell_processing__single_cell):
            self.MissingRequiredField("cell_processing__single_cell")
        if not isinstance(self.cell_processing__single_cell, Bool):
            self.cell_processing__single_cell = Bool(self.cell_processing__single_cell)

        if self._is_empty(self.cell_processing__cell_number):
            self.MissingRequiredField("cell_processing__cell_number")
        if not isinstance(self.cell_processing__cell_number, int):
            self.cell_processing__cell_number = int(self.cell_processing__cell_number)

        if self._is_empty(self.cell_processing__cells_per_reaction):
            self.MissingRequiredField("cell_processing__cells_per_reaction")
        if not isinstance(self.cell_processing__cells_per_reaction, int):
            self.cell_processing__cells_per_reaction = int(self.cell_processing__cells_per_reaction)

        if self._is_empty(self.cell_processing__cell_storage):
            self.MissingRequiredField("cell_processing__cell_storage")
        if not isinstance(self.cell_processing__cell_storage, Bool):
            self.cell_processing__cell_storage = Bool(self.cell_processing__cell_storage)

        if self._is_empty(self.cell_processing__cell_quality):
            self.MissingRequiredField("cell_processing__cell_quality")
        if not isinstance(self.cell_processing__cell_quality, str):
            self.cell_processing__cell_quality = str(self.cell_processing__cell_quality)

        if self._is_empty(self.cell_processing__cell_isolation):
            self.MissingRequiredField("cell_processing__cell_isolation")
        if not isinstance(self.cell_processing__cell_isolation, str):
            self.cell_processing__cell_isolation = str(self.cell_processing__cell_isolation)

        if self._is_empty(self.cell_processing__cell_processing_protocol):
            self.MissingRequiredField("cell_processing__cell_processing_protocol")
        if not isinstance(self.cell_processing__cell_processing_protocol, str):
            self.cell_processing__cell_processing_protocol = str(self.cell_processing__cell_processing_protocol)

        if self.cell_processing__cell_label is not None and not isinstance(self.cell_processing__cell_label, str):
            self.cell_processing__cell_label = str(self.cell_processing__cell_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4PCRTarget(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4PCRTarget"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4PCRTarget"
    class_name: ClassVar[str] = "V1p4_PCRTarget"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4PCRTarget

    p_c_r_target__pcr_target_locus: Union[str, "V1p4PcrTargetLocus"] = None
    p_c_r_target__forward_pcr_primer_target_location: str = None
    p_c_r_target__reverse_pcr_primer_target_location: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.p_c_r_target__pcr_target_locus):
            self.MissingRequiredField("p_c_r_target__pcr_target_locus")
        if not isinstance(self.p_c_r_target__pcr_target_locus, V1p4PcrTargetLocus):
            self.p_c_r_target__pcr_target_locus = V1p4PcrTargetLocus(self.p_c_r_target__pcr_target_locus)

        if self._is_empty(self.p_c_r_target__forward_pcr_primer_target_location):
            self.MissingRequiredField("p_c_r_target__forward_pcr_primer_target_location")
        if not isinstance(self.p_c_r_target__forward_pcr_primer_target_location, str):
            self.p_c_r_target__forward_pcr_primer_target_location = str(self.p_c_r_target__forward_pcr_primer_target_location)

        if self._is_empty(self.p_c_r_target__reverse_pcr_primer_target_location):
            self.MissingRequiredField("p_c_r_target__reverse_pcr_primer_target_location")
        if not isinstance(self.p_c_r_target__reverse_pcr_primer_target_location, str):
            self.p_c_r_target__reverse_pcr_primer_target_location = str(self.p_c_r_target__reverse_pcr_primer_target_location)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4NucleicAcidProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4NucleicAcidProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4NucleicAcidProcessing"
    class_name: ClassVar[str] = "V1p4_NucleicAcidProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4NucleicAcidProcessing

    nucleic_acid_processing__template_class: Union[str, "V1p4TemplateClass"] = None
    nucleic_acid_processing__template_quality: str = None
    nucleic_acid_processing__template_amount: Union[dict, V1p4PhysicalQuantity] = None
    nucleic_acid_processing__library_generation_method: Union[str, "V1p4LibraryGenerationMethod"] = None
    nucleic_acid_processing__library_generation_protocol: str = None
    nucleic_acid_processing__library_generation_kit_version: str = None
    nucleic_acid_processing__complete_sequences: Union[str, "V1p4CompleteSequences"] = None
    nucleic_acid_processing__physical_linkage: Union[str, "V1p4PhysicalLinkage"] = None
    nucleic_acid_processing__pcr_target: Optional[Union[Union[dict, V1p4PCRTarget], List[Union[dict, V1p4PCRTarget]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.nucleic_acid_processing__template_class):
            self.MissingRequiredField("nucleic_acid_processing__template_class")
        if not isinstance(self.nucleic_acid_processing__template_class, V1p4TemplateClass):
            self.nucleic_acid_processing__template_class = V1p4TemplateClass(self.nucleic_acid_processing__template_class)

        if self._is_empty(self.nucleic_acid_processing__template_quality):
            self.MissingRequiredField("nucleic_acid_processing__template_quality")
        if not isinstance(self.nucleic_acid_processing__template_quality, str):
            self.nucleic_acid_processing__template_quality = str(self.nucleic_acid_processing__template_quality)

        if self._is_empty(self.nucleic_acid_processing__template_amount):
            self.MissingRequiredField("nucleic_acid_processing__template_amount")
        if not isinstance(self.nucleic_acid_processing__template_amount, V1p4PhysicalQuantity):
            self.nucleic_acid_processing__template_amount = V1p4PhysicalQuantity(**as_dict(self.nucleic_acid_processing__template_amount))

        if self._is_empty(self.nucleic_acid_processing__library_generation_method):
            self.MissingRequiredField("nucleic_acid_processing__library_generation_method")
        if not isinstance(self.nucleic_acid_processing__library_generation_method, V1p4LibraryGenerationMethod):
            self.nucleic_acid_processing__library_generation_method = V1p4LibraryGenerationMethod(self.nucleic_acid_processing__library_generation_method)

        if self._is_empty(self.nucleic_acid_processing__library_generation_protocol):
            self.MissingRequiredField("nucleic_acid_processing__library_generation_protocol")
        if not isinstance(self.nucleic_acid_processing__library_generation_protocol, str):
            self.nucleic_acid_processing__library_generation_protocol = str(self.nucleic_acid_processing__library_generation_protocol)

        if self._is_empty(self.nucleic_acid_processing__library_generation_kit_version):
            self.MissingRequiredField("nucleic_acid_processing__library_generation_kit_version")
        if not isinstance(self.nucleic_acid_processing__library_generation_kit_version, str):
            self.nucleic_acid_processing__library_generation_kit_version = str(self.nucleic_acid_processing__library_generation_kit_version)

        if self._is_empty(self.nucleic_acid_processing__complete_sequences):
            self.MissingRequiredField("nucleic_acid_processing__complete_sequences")
        if not isinstance(self.nucleic_acid_processing__complete_sequences, V1p4CompleteSequences):
            self.nucleic_acid_processing__complete_sequences = V1p4CompleteSequences(self.nucleic_acid_processing__complete_sequences)

        if self._is_empty(self.nucleic_acid_processing__physical_linkage):
            self.MissingRequiredField("nucleic_acid_processing__physical_linkage")
        if not isinstance(self.nucleic_acid_processing__physical_linkage, V1p4PhysicalLinkage):
            self.nucleic_acid_processing__physical_linkage = V1p4PhysicalLinkage(self.nucleic_acid_processing__physical_linkage)

        self._normalize_inlined_as_dict(slot_name="nucleic_acid_processing__pcr_target", slot_type=V1p4PCRTarget, key_name="p_c_r_target__pcr_target_locus", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SequencingRun(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SequencingRun"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SequencingRun"
    class_name: ClassVar[str] = "V1p4_SequencingRun"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SequencingRun

    sequencing_run__sequencing_run_id: str = None
    sequencing_run__total_reads_passing_qc_filter: int = None
    sequencing_run__sequencing_platform: str = None
    sequencing_run__sequencing_facility: str = None
    sequencing_run__sequencing_run_date: str = None
    sequencing_run__sequencing_kit: str = None
    sequencing_run__sequencing_files: Optional[Union[dict, "V1p4SequencingData"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sequencing_run__sequencing_run_id):
            self.MissingRequiredField("sequencing_run__sequencing_run_id")
        if not isinstance(self.sequencing_run__sequencing_run_id, str):
            self.sequencing_run__sequencing_run_id = str(self.sequencing_run__sequencing_run_id)

        if self._is_empty(self.sequencing_run__total_reads_passing_qc_filter):
            self.MissingRequiredField("sequencing_run__total_reads_passing_qc_filter")
        if not isinstance(self.sequencing_run__total_reads_passing_qc_filter, int):
            self.sequencing_run__total_reads_passing_qc_filter = int(self.sequencing_run__total_reads_passing_qc_filter)

        if self._is_empty(self.sequencing_run__sequencing_platform):
            self.MissingRequiredField("sequencing_run__sequencing_platform")
        if not isinstance(self.sequencing_run__sequencing_platform, str):
            self.sequencing_run__sequencing_platform = str(self.sequencing_run__sequencing_platform)

        if self._is_empty(self.sequencing_run__sequencing_facility):
            self.MissingRequiredField("sequencing_run__sequencing_facility")
        if not isinstance(self.sequencing_run__sequencing_facility, str):
            self.sequencing_run__sequencing_facility = str(self.sequencing_run__sequencing_facility)

        if self._is_empty(self.sequencing_run__sequencing_run_date):
            self.MissingRequiredField("sequencing_run__sequencing_run_date")
        if not isinstance(self.sequencing_run__sequencing_run_date, str):
            self.sequencing_run__sequencing_run_date = str(self.sequencing_run__sequencing_run_date)

        if self._is_empty(self.sequencing_run__sequencing_kit):
            self.MissingRequiredField("sequencing_run__sequencing_kit")
        if not isinstance(self.sequencing_run__sequencing_kit, str):
            self.sequencing_run__sequencing_kit = str(self.sequencing_run__sequencing_kit)

        if self.sequencing_run__sequencing_files is not None and not isinstance(self.sequencing_run__sequencing_files, V1p4SequencingData):
            self.sequencing_run__sequencing_files = V1p4SequencingData(**as_dict(self.sequencing_run__sequencing_files))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SequencingData(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SequencingData"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SequencingData"
    class_name: ClassVar[str] = "V1p4_SequencingData"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SequencingData

    sequencing_data__sequencing_data_id: str = None
    sequencing_data__file_type: Union[str, "V1p4FileType"] = None
    sequencing_data__filename: str = None
    sequencing_data__read_direction: Union[str, "V1p4ReadDirection"] = None
    sequencing_data__read_length: int = None
    sequencing_data__paired_filename: str = None
    sequencing_data__paired_read_direction: Union[str, "V1p4PairedReadDirection"] = None
    sequencing_data__paired_read_length: int = None
    sequencing_data__index_filename: Optional[str] = None
    sequencing_data__index_length: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sequencing_data__sequencing_data_id):
            self.MissingRequiredField("sequencing_data__sequencing_data_id")
        if not isinstance(self.sequencing_data__sequencing_data_id, str):
            self.sequencing_data__sequencing_data_id = str(self.sequencing_data__sequencing_data_id)

        if self._is_empty(self.sequencing_data__file_type):
            self.MissingRequiredField("sequencing_data__file_type")
        if not isinstance(self.sequencing_data__file_type, V1p4FileType):
            self.sequencing_data__file_type = V1p4FileType(self.sequencing_data__file_type)

        if self._is_empty(self.sequencing_data__filename):
            self.MissingRequiredField("sequencing_data__filename")
        if not isinstance(self.sequencing_data__filename, str):
            self.sequencing_data__filename = str(self.sequencing_data__filename)

        if self._is_empty(self.sequencing_data__read_direction):
            self.MissingRequiredField("sequencing_data__read_direction")
        if not isinstance(self.sequencing_data__read_direction, V1p4ReadDirection):
            self.sequencing_data__read_direction = V1p4ReadDirection(self.sequencing_data__read_direction)

        if self._is_empty(self.sequencing_data__read_length):
            self.MissingRequiredField("sequencing_data__read_length")
        if not isinstance(self.sequencing_data__read_length, int):
            self.sequencing_data__read_length = int(self.sequencing_data__read_length)

        if self._is_empty(self.sequencing_data__paired_filename):
            self.MissingRequiredField("sequencing_data__paired_filename")
        if not isinstance(self.sequencing_data__paired_filename, str):
            self.sequencing_data__paired_filename = str(self.sequencing_data__paired_filename)

        if self._is_empty(self.sequencing_data__paired_read_direction):
            self.MissingRequiredField("sequencing_data__paired_read_direction")
        if not isinstance(self.sequencing_data__paired_read_direction, V1p4PairedReadDirection):
            self.sequencing_data__paired_read_direction = V1p4PairedReadDirection(self.sequencing_data__paired_read_direction)

        if self._is_empty(self.sequencing_data__paired_read_length):
            self.MissingRequiredField("sequencing_data__paired_read_length")
        if not isinstance(self.sequencing_data__paired_read_length, int):
            self.sequencing_data__paired_read_length = int(self.sequencing_data__paired_read_length)

        if self.sequencing_data__index_filename is not None and not isinstance(self.sequencing_data__index_filename, str):
            self.sequencing_data__index_filename = str(self.sequencing_data__index_filename)

        if self.sequencing_data__index_length is not None and not isinstance(self.sequencing_data__index_length, int):
            self.sequencing_data__index_length = int(self.sequencing_data__index_length)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4DataProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4DataProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4DataProcessing"
    class_name: ClassVar[str] = "V1p4_DataProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4DataProcessing

    data_processing__software_versions: str = None
    data_processing__paired_reads_assembly: str = None
    data_processing__quality_thresholds: str = None
    data_processing__primer_match_cutoffs: str = None
    data_processing__collapsing_method: str = None
    data_processing__data_processing_protocols: str = None
    data_processing__germline_database: str = None
    data_processing__data_processing_id: Optional[str] = None
    data_processing__primary_annotation: Optional[Union[bool, Bool]] = None
    data_processing__data_processing_files: Optional[Union[str, List[str]]] = empty_list()
    data_processing__germline_set_ref: Optional[str] = None
    data_processing__analysis_provenance_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.data_processing__software_versions):
            self.MissingRequiredField("data_processing__software_versions")
        if not isinstance(self.data_processing__software_versions, str):
            self.data_processing__software_versions = str(self.data_processing__software_versions)

        if self._is_empty(self.data_processing__paired_reads_assembly):
            self.MissingRequiredField("data_processing__paired_reads_assembly")
        if not isinstance(self.data_processing__paired_reads_assembly, str):
            self.data_processing__paired_reads_assembly = str(self.data_processing__paired_reads_assembly)

        if self._is_empty(self.data_processing__quality_thresholds):
            self.MissingRequiredField("data_processing__quality_thresholds")
        if not isinstance(self.data_processing__quality_thresholds, str):
            self.data_processing__quality_thresholds = str(self.data_processing__quality_thresholds)

        if self._is_empty(self.data_processing__primer_match_cutoffs):
            self.MissingRequiredField("data_processing__primer_match_cutoffs")
        if not isinstance(self.data_processing__primer_match_cutoffs, str):
            self.data_processing__primer_match_cutoffs = str(self.data_processing__primer_match_cutoffs)

        if self._is_empty(self.data_processing__collapsing_method):
            self.MissingRequiredField("data_processing__collapsing_method")
        if not isinstance(self.data_processing__collapsing_method, str):
            self.data_processing__collapsing_method = str(self.data_processing__collapsing_method)

        if self._is_empty(self.data_processing__data_processing_protocols):
            self.MissingRequiredField("data_processing__data_processing_protocols")
        if not isinstance(self.data_processing__data_processing_protocols, str):
            self.data_processing__data_processing_protocols = str(self.data_processing__data_processing_protocols)

        if self._is_empty(self.data_processing__germline_database):
            self.MissingRequiredField("data_processing__germline_database")
        if not isinstance(self.data_processing__germline_database, str):
            self.data_processing__germline_database = str(self.data_processing__germline_database)

        if self.data_processing__data_processing_id is not None and not isinstance(self.data_processing__data_processing_id, str):
            self.data_processing__data_processing_id = str(self.data_processing__data_processing_id)

        if self.data_processing__primary_annotation is not None and not isinstance(self.data_processing__primary_annotation, Bool):
            self.data_processing__primary_annotation = Bool(self.data_processing__primary_annotation)

        if not isinstance(self.data_processing__data_processing_files, list):
            self.data_processing__data_processing_files = [self.data_processing__data_processing_files] if self.data_processing__data_processing_files is not None else []
        self.data_processing__data_processing_files = [v if isinstance(v, str) else str(v) for v in self.data_processing__data_processing_files]

        if self.data_processing__germline_set_ref is not None and not isinstance(self.data_processing__germline_set_ref, str):
            self.data_processing__germline_set_ref = str(self.data_processing__germline_set_ref)

        if self.data_processing__analysis_provenance_id is not None and not isinstance(self.data_processing__analysis_provenance_id, str):
            self.data_processing__analysis_provenance_id = str(self.data_processing__analysis_provenance_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Repertoire(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Repertoire"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Repertoire"
    class_name: ClassVar[str] = "V1p4_Repertoire"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Repertoire

    repertoire__study: Union[dict, V1p4Study] = None
    repertoire__subject: Union[dict, V1p4Subject] = None
    repertoire__sample: Union[Union[dict, "V1p4SampleProcessing"], List[Union[dict, "V1p4SampleProcessing"]]] = None
    repertoire__data_processing: Union[Union[dict, V1p4DataProcessing], List[Union[dict, V1p4DataProcessing]]] = None
    repertoire__repertoire_id: Optional[str] = None
    repertoire__repertoire_name: Optional[str] = None
    repertoire__repertoire_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.repertoire__study):
            self.MissingRequiredField("repertoire__study")
        if not isinstance(self.repertoire__study, V1p4Study):
            self.repertoire__study = V1p4Study(**as_dict(self.repertoire__study))

        if self._is_empty(self.repertoire__subject):
            self.MissingRequiredField("repertoire__subject")
        if not isinstance(self.repertoire__subject, V1p4Subject):
            self.repertoire__subject = V1p4Subject(**as_dict(self.repertoire__subject))

        if self._is_empty(self.repertoire__sample):
            self.MissingRequiredField("repertoire__sample")
        self._normalize_inlined_as_dict(slot_name="repertoire__sample", slot_type=V1p4SampleProcessing, key_name="sample__sample_id", keyed=False)

        if self._is_empty(self.repertoire__data_processing):
            self.MissingRequiredField("repertoire__data_processing")
        self._normalize_inlined_as_dict(slot_name="repertoire__data_processing", slot_type=V1p4DataProcessing, key_name="data_processing__software_versions", keyed=False)

        if self.repertoire__repertoire_id is not None and not isinstance(self.repertoire__repertoire_id, str):
            self.repertoire__repertoire_id = str(self.repertoire__repertoire_id)

        if self.repertoire__repertoire_name is not None and not isinstance(self.repertoire__repertoire_name, str):
            self.repertoire__repertoire_name = str(self.repertoire__repertoire_name)

        if self.repertoire__repertoire_description is not None and not isinstance(self.repertoire__repertoire_description, str):
            self.repertoire__repertoire_description = str(self.repertoire__repertoire_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4RepertoireGroup(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4RepertoireGroup"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4RepertoireGroup"
    class_name: ClassVar[str] = "V1p4_RepertoireGroup"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4RepertoireGroup

    repertoire_group__repertoire_group_id: str = None
    repertoire_group__repertoires: Union[str, List[str]] = None
    repertoire_group__repertoire_group_name: Optional[str] = None
    repertoire_group__repertoire_group_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.repertoire_group__repertoire_group_id):
            self.MissingRequiredField("repertoire_group__repertoire_group_id")
        if not isinstance(self.repertoire_group__repertoire_group_id, str):
            self.repertoire_group__repertoire_group_id = str(self.repertoire_group__repertoire_group_id)

        if self._is_empty(self.repertoire_group__repertoires):
            self.MissingRequiredField("repertoire_group__repertoires")
        if not isinstance(self.repertoire_group__repertoires, list):
            self.repertoire_group__repertoires = [self.repertoire_group__repertoires] if self.repertoire_group__repertoires is not None else []
        self.repertoire_group__repertoires = [v if isinstance(v, str) else str(v) for v in self.repertoire_group__repertoires]

        if self.repertoire_group__repertoire_group_name is not None and not isinstance(self.repertoire_group__repertoire_group_name, str):
            self.repertoire_group__repertoire_group_name = str(self.repertoire_group__repertoire_group_name)

        if self.repertoire_group__repertoire_group_description is not None and not isinstance(self.repertoire_group__repertoire_group_description, str):
            self.repertoire_group__repertoire_group_description = str(self.repertoire_group__repertoire_group_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Alignment(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Alignment"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Alignment"
    class_name: ClassVar[str] = "V1p4_Alignment"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Alignment

    alignment__sequence_id: str = None
    alignment__segment: str = None
    alignment__call: str = None
    alignment__score: float = None
    alignment__cigar: str = None
    alignment__rev_comp: Optional[Union[bool, Bool]] = None
    alignment__identity: Optional[float] = None
    alignment__support: Optional[float] = None
    alignment__sequence_start: Optional[int] = None
    alignment__sequence_end: Optional[int] = None
    alignment__germline_start: Optional[int] = None
    alignment__germline_end: Optional[int] = None
    alignment__rank: Optional[int] = None
    alignment__data_processing_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.alignment__sequence_id):
            self.MissingRequiredField("alignment__sequence_id")
        if not isinstance(self.alignment__sequence_id, str):
            self.alignment__sequence_id = str(self.alignment__sequence_id)

        if self._is_empty(self.alignment__segment):
            self.MissingRequiredField("alignment__segment")
        if not isinstance(self.alignment__segment, str):
            self.alignment__segment = str(self.alignment__segment)

        if self._is_empty(self.alignment__call):
            self.MissingRequiredField("alignment__call")
        if not isinstance(self.alignment__call, str):
            self.alignment__call = str(self.alignment__call)

        if self._is_empty(self.alignment__score):
            self.MissingRequiredField("alignment__score")
        if not isinstance(self.alignment__score, float):
            self.alignment__score = float(self.alignment__score)

        if self._is_empty(self.alignment__cigar):
            self.MissingRequiredField("alignment__cigar")
        if not isinstance(self.alignment__cigar, str):
            self.alignment__cigar = str(self.alignment__cigar)

        if self.alignment__rev_comp is not None and not isinstance(self.alignment__rev_comp, Bool):
            self.alignment__rev_comp = Bool(self.alignment__rev_comp)

        if self.alignment__identity is not None and not isinstance(self.alignment__identity, float):
            self.alignment__identity = float(self.alignment__identity)

        if self.alignment__support is not None and not isinstance(self.alignment__support, float):
            self.alignment__support = float(self.alignment__support)

        if self.alignment__sequence_start is not None and not isinstance(self.alignment__sequence_start, int):
            self.alignment__sequence_start = int(self.alignment__sequence_start)

        if self.alignment__sequence_end is not None and not isinstance(self.alignment__sequence_end, int):
            self.alignment__sequence_end = int(self.alignment__sequence_end)

        if self.alignment__germline_start is not None and not isinstance(self.alignment__germline_start, int):
            self.alignment__germline_start = int(self.alignment__germline_start)

        if self.alignment__germline_end is not None and not isinstance(self.alignment__germline_end, int):
            self.alignment__germline_end = int(self.alignment__germline_end)

        if self.alignment__rank is not None and not isinstance(self.alignment__rank, int):
            self.alignment__rank = int(self.alignment__rank)

        if self.alignment__data_processing_id is not None and not isinstance(self.alignment__data_processing_id, str):
            self.alignment__data_processing_id = str(self.alignment__data_processing_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Rearrangement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Rearrangement"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Rearrangement"
    class_name: ClassVar[str] = "V1p4_Rearrangement"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Rearrangement

    rearrangement__sequence_id: str = None
    rearrangement__sequence: str = None
    rearrangement__rev_comp: Union[bool, Bool] = None
    rearrangement__productive: Union[bool, Bool] = None
    rearrangement__v_call: str = None
    rearrangement__d_call: str = None
    rearrangement__j_call: str = None
    rearrangement__sequence_alignment: str = None
    rearrangement__germline_alignment: str = None
    rearrangement__junction: str = None
    rearrangement__junction_aa: str = None
    rearrangement__v_cigar: str = None
    rearrangement__d_cigar: str = None
    rearrangement__j_cigar: str = None
    rearrangement__quality: Optional[str] = None
    rearrangement__sequence_aa: Optional[str] = None
    rearrangement__vj_in_frame: Optional[Union[bool, Bool]] = None
    rearrangement__stop_codon: Optional[Union[bool, Bool]] = None
    rearrangement__complete_vdj: Optional[Union[bool, Bool]] = None
    rearrangement__locus: Optional[Union[str, "V1p4Locus"]] = None
    rearrangement__locus_species: Optional[Union[str, "V1p4LocusSpecies"]] = None
    rearrangement__d2_call: Optional[str] = None
    rearrangement__c_call: Optional[str] = None
    rearrangement__quality_alignment: Optional[str] = None
    rearrangement__sequence_alignment_aa: Optional[str] = None
    rearrangement__germline_alignment_aa: Optional[str] = None
    rearrangement__np1: Optional[str] = None
    rearrangement__np1_aa: Optional[str] = None
    rearrangement__np2: Optional[str] = None
    rearrangement__np2_aa: Optional[str] = None
    rearrangement__np3: Optional[str] = None
    rearrangement__np3_aa: Optional[str] = None
    rearrangement__cdr1: Optional[str] = None
    rearrangement__cdr1_aa: Optional[str] = None
    rearrangement__cdr2: Optional[str] = None
    rearrangement__cdr2_aa: Optional[str] = None
    rearrangement__cdr3: Optional[str] = None
    rearrangement__cdr3_aa: Optional[str] = None
    rearrangement__fwr1: Optional[str] = None
    rearrangement__fwr1_aa: Optional[str] = None
    rearrangement__fwr2: Optional[str] = None
    rearrangement__fwr2_aa: Optional[str] = None
    rearrangement__fwr3: Optional[str] = None
    rearrangement__fwr3_aa: Optional[str] = None
    rearrangement__fwr4: Optional[str] = None
    rearrangement__fwr4_aa: Optional[str] = None
    rearrangement__v_score: Optional[float] = None
    rearrangement__v_identity: Optional[float] = None
    rearrangement__v_support: Optional[float] = None
    rearrangement__d_score: Optional[float] = None
    rearrangement__d_identity: Optional[float] = None
    rearrangement__d_support: Optional[float] = None
    rearrangement__d2_score: Optional[float] = None
    rearrangement__d2_identity: Optional[float] = None
    rearrangement__d2_support: Optional[float] = None
    rearrangement__d2_cigar: Optional[str] = None
    rearrangement__j_score: Optional[float] = None
    rearrangement__j_identity: Optional[float] = None
    rearrangement__j_support: Optional[float] = None
    rearrangement__c_score: Optional[float] = None
    rearrangement__c_identity: Optional[float] = None
    rearrangement__c_support: Optional[float] = None
    rearrangement__c_cigar: Optional[str] = None
    rearrangement__v_sequence_start: Optional[int] = None
    rearrangement__v_sequence_end: Optional[int] = None
    rearrangement__v_germline_start: Optional[int] = None
    rearrangement__v_germline_end: Optional[int] = None
    rearrangement__v_alignment_start: Optional[int] = None
    rearrangement__v_alignment_end: Optional[int] = None
    rearrangement__d_sequence_start: Optional[int] = None
    rearrangement__d_sequence_end: Optional[int] = None
    rearrangement__d_germline_start: Optional[int] = None
    rearrangement__d_germline_end: Optional[int] = None
    rearrangement__d_alignment_start: Optional[int] = None
    rearrangement__d_alignment_end: Optional[int] = None
    rearrangement__d2_sequence_start: Optional[int] = None
    rearrangement__d2_sequence_end: Optional[int] = None
    rearrangement__d2_germline_start: Optional[int] = None
    rearrangement__d2_germline_end: Optional[int] = None
    rearrangement__d2_alignment_start: Optional[int] = None
    rearrangement__d2_alignment_end: Optional[int] = None
    rearrangement__j_sequence_start: Optional[int] = None
    rearrangement__j_sequence_end: Optional[int] = None
    rearrangement__j_germline_start: Optional[int] = None
    rearrangement__j_germline_end: Optional[int] = None
    rearrangement__j_alignment_start: Optional[int] = None
    rearrangement__j_alignment_end: Optional[int] = None
    rearrangement__c_sequence_start: Optional[int] = None
    rearrangement__c_sequence_end: Optional[int] = None
    rearrangement__c_germline_start: Optional[int] = None
    rearrangement__c_germline_end: Optional[int] = None
    rearrangement__c_alignment_start: Optional[int] = None
    rearrangement__c_alignment_end: Optional[int] = None
    rearrangement__cdr1_start: Optional[int] = None
    rearrangement__cdr1_end: Optional[int] = None
    rearrangement__cdr2_start: Optional[int] = None
    rearrangement__cdr2_end: Optional[int] = None
    rearrangement__cdr3_start: Optional[int] = None
    rearrangement__cdr3_end: Optional[int] = None
    rearrangement__fwr1_start: Optional[int] = None
    rearrangement__fwr1_end: Optional[int] = None
    rearrangement__fwr2_start: Optional[int] = None
    rearrangement__fwr2_end: Optional[int] = None
    rearrangement__fwr3_start: Optional[int] = None
    rearrangement__fwr3_end: Optional[int] = None
    rearrangement__fwr4_start: Optional[int] = None
    rearrangement__fwr4_end: Optional[int] = None
    rearrangement__v_sequence_alignment: Optional[str] = None
    rearrangement__v_sequence_alignment_aa: Optional[str] = None
    rearrangement__d_sequence_alignment: Optional[str] = None
    rearrangement__d_sequence_alignment_aa: Optional[str] = None
    rearrangement__d2_sequence_alignment: Optional[str] = None
    rearrangement__d2_sequence_alignment_aa: Optional[str] = None
    rearrangement__j_sequence_alignment: Optional[str] = None
    rearrangement__j_sequence_alignment_aa: Optional[str] = None
    rearrangement__c_sequence_alignment: Optional[str] = None
    rearrangement__c_sequence_alignment_aa: Optional[str] = None
    rearrangement__v_germline_alignment: Optional[str] = None
    rearrangement__v_germline_alignment_aa: Optional[str] = None
    rearrangement__d_germline_alignment: Optional[str] = None
    rearrangement__d_germline_alignment_aa: Optional[str] = None
    rearrangement__d2_germline_alignment: Optional[str] = None
    rearrangement__d2_germline_alignment_aa: Optional[str] = None
    rearrangement__j_germline_alignment: Optional[str] = None
    rearrangement__j_germline_alignment_aa: Optional[str] = None
    rearrangement__c_germline_alignment: Optional[str] = None
    rearrangement__c_germline_alignment_aa: Optional[str] = None
    rearrangement__junction_length: Optional[int] = None
    rearrangement__junction_aa_length: Optional[int] = None
    rearrangement__np1_length: Optional[int] = None
    rearrangement__np2_length: Optional[int] = None
    rearrangement__np3_length: Optional[int] = None
    rearrangement__n1_length: Optional[int] = None
    rearrangement__n2_length: Optional[int] = None
    rearrangement__n3_length: Optional[int] = None
    rearrangement__p3v_length: Optional[int] = None
    rearrangement__p5d_length: Optional[int] = None
    rearrangement__p3d_length: Optional[int] = None
    rearrangement__p5d2_length: Optional[int] = None
    rearrangement__p3d2_length: Optional[int] = None
    rearrangement__p5j_length: Optional[int] = None
    rearrangement__v_frameshift: Optional[Union[bool, Bool]] = None
    rearrangement__j_frameshift: Optional[Union[bool, Bool]] = None
    rearrangement__d_frame: Optional[int] = None
    rearrangement__d2_frame: Optional[int] = None
    rearrangement__consensus_count: Optional[int] = None
    rearrangement__duplicate_count: Optional[int] = None
    rearrangement__umi_count: Optional[int] = None
    rearrangement__cell_id: Optional[str] = None
    rearrangement__clone_id: Optional[str] = None
    rearrangement__reactivity_id: Optional[str] = None
    rearrangement__reactivity_ref: Optional[str] = None
    rearrangement__repertoire_id: Optional[str] = None
    rearrangement__sample_processing_id: Optional[str] = None
    rearrangement__data_processing_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.rearrangement__sequence_id):
            self.MissingRequiredField("rearrangement__sequence_id")
        if not isinstance(self.rearrangement__sequence_id, str):
            self.rearrangement__sequence_id = str(self.rearrangement__sequence_id)

        if self._is_empty(self.rearrangement__sequence):
            self.MissingRequiredField("rearrangement__sequence")
        if not isinstance(self.rearrangement__sequence, str):
            self.rearrangement__sequence = str(self.rearrangement__sequence)

        if self._is_empty(self.rearrangement__rev_comp):
            self.MissingRequiredField("rearrangement__rev_comp")
        if not isinstance(self.rearrangement__rev_comp, Bool):
            self.rearrangement__rev_comp = Bool(self.rearrangement__rev_comp)

        if self._is_empty(self.rearrangement__productive):
            self.MissingRequiredField("rearrangement__productive")
        if not isinstance(self.rearrangement__productive, Bool):
            self.rearrangement__productive = Bool(self.rearrangement__productive)

        if self._is_empty(self.rearrangement__v_call):
            self.MissingRequiredField("rearrangement__v_call")
        if not isinstance(self.rearrangement__v_call, str):
            self.rearrangement__v_call = str(self.rearrangement__v_call)

        if self._is_empty(self.rearrangement__d_call):
            self.MissingRequiredField("rearrangement__d_call")
        if not isinstance(self.rearrangement__d_call, str):
            self.rearrangement__d_call = str(self.rearrangement__d_call)

        if self._is_empty(self.rearrangement__j_call):
            self.MissingRequiredField("rearrangement__j_call")
        if not isinstance(self.rearrangement__j_call, str):
            self.rearrangement__j_call = str(self.rearrangement__j_call)

        if self._is_empty(self.rearrangement__sequence_alignment):
            self.MissingRequiredField("rearrangement__sequence_alignment")
        if not isinstance(self.rearrangement__sequence_alignment, str):
            self.rearrangement__sequence_alignment = str(self.rearrangement__sequence_alignment)

        if self._is_empty(self.rearrangement__germline_alignment):
            self.MissingRequiredField("rearrangement__germline_alignment")
        if not isinstance(self.rearrangement__germline_alignment, str):
            self.rearrangement__germline_alignment = str(self.rearrangement__germline_alignment)

        if self._is_empty(self.rearrangement__junction):
            self.MissingRequiredField("rearrangement__junction")
        if not isinstance(self.rearrangement__junction, str):
            self.rearrangement__junction = str(self.rearrangement__junction)

        if self._is_empty(self.rearrangement__junction_aa):
            self.MissingRequiredField("rearrangement__junction_aa")
        if not isinstance(self.rearrangement__junction_aa, str):
            self.rearrangement__junction_aa = str(self.rearrangement__junction_aa)

        if self._is_empty(self.rearrangement__v_cigar):
            self.MissingRequiredField("rearrangement__v_cigar")
        if not isinstance(self.rearrangement__v_cigar, str):
            self.rearrangement__v_cigar = str(self.rearrangement__v_cigar)

        if self._is_empty(self.rearrangement__d_cigar):
            self.MissingRequiredField("rearrangement__d_cigar")
        if not isinstance(self.rearrangement__d_cigar, str):
            self.rearrangement__d_cigar = str(self.rearrangement__d_cigar)

        if self._is_empty(self.rearrangement__j_cigar):
            self.MissingRequiredField("rearrangement__j_cigar")
        if not isinstance(self.rearrangement__j_cigar, str):
            self.rearrangement__j_cigar = str(self.rearrangement__j_cigar)

        if self.rearrangement__quality is not None and not isinstance(self.rearrangement__quality, str):
            self.rearrangement__quality = str(self.rearrangement__quality)

        if self.rearrangement__sequence_aa is not None and not isinstance(self.rearrangement__sequence_aa, str):
            self.rearrangement__sequence_aa = str(self.rearrangement__sequence_aa)

        if self.rearrangement__vj_in_frame is not None and not isinstance(self.rearrangement__vj_in_frame, Bool):
            self.rearrangement__vj_in_frame = Bool(self.rearrangement__vj_in_frame)

        if self.rearrangement__stop_codon is not None and not isinstance(self.rearrangement__stop_codon, Bool):
            self.rearrangement__stop_codon = Bool(self.rearrangement__stop_codon)

        if self.rearrangement__complete_vdj is not None and not isinstance(self.rearrangement__complete_vdj, Bool):
            self.rearrangement__complete_vdj = Bool(self.rearrangement__complete_vdj)

        if self.rearrangement__locus is not None and not isinstance(self.rearrangement__locus, V1p4Locus):
            self.rearrangement__locus = V1p4Locus(self.rearrangement__locus)

        if self.rearrangement__d2_call is not None and not isinstance(self.rearrangement__d2_call, str):
            self.rearrangement__d2_call = str(self.rearrangement__d2_call)

        if self.rearrangement__c_call is not None and not isinstance(self.rearrangement__c_call, str):
            self.rearrangement__c_call = str(self.rearrangement__c_call)

        if self.rearrangement__quality_alignment is not None and not isinstance(self.rearrangement__quality_alignment, str):
            self.rearrangement__quality_alignment = str(self.rearrangement__quality_alignment)

        if self.rearrangement__sequence_alignment_aa is not None and not isinstance(self.rearrangement__sequence_alignment_aa, str):
            self.rearrangement__sequence_alignment_aa = str(self.rearrangement__sequence_alignment_aa)

        if self.rearrangement__germline_alignment_aa is not None and not isinstance(self.rearrangement__germline_alignment_aa, str):
            self.rearrangement__germline_alignment_aa = str(self.rearrangement__germline_alignment_aa)

        if self.rearrangement__np1 is not None and not isinstance(self.rearrangement__np1, str):
            self.rearrangement__np1 = str(self.rearrangement__np1)

        if self.rearrangement__np1_aa is not None and not isinstance(self.rearrangement__np1_aa, str):
            self.rearrangement__np1_aa = str(self.rearrangement__np1_aa)

        if self.rearrangement__np2 is not None and not isinstance(self.rearrangement__np2, str):
            self.rearrangement__np2 = str(self.rearrangement__np2)

        if self.rearrangement__np2_aa is not None and not isinstance(self.rearrangement__np2_aa, str):
            self.rearrangement__np2_aa = str(self.rearrangement__np2_aa)

        if self.rearrangement__np3 is not None and not isinstance(self.rearrangement__np3, str):
            self.rearrangement__np3 = str(self.rearrangement__np3)

        if self.rearrangement__np3_aa is not None and not isinstance(self.rearrangement__np3_aa, str):
            self.rearrangement__np3_aa = str(self.rearrangement__np3_aa)

        if self.rearrangement__cdr1 is not None and not isinstance(self.rearrangement__cdr1, str):
            self.rearrangement__cdr1 = str(self.rearrangement__cdr1)

        if self.rearrangement__cdr1_aa is not None and not isinstance(self.rearrangement__cdr1_aa, str):
            self.rearrangement__cdr1_aa = str(self.rearrangement__cdr1_aa)

        if self.rearrangement__cdr2 is not None and not isinstance(self.rearrangement__cdr2, str):
            self.rearrangement__cdr2 = str(self.rearrangement__cdr2)

        if self.rearrangement__cdr2_aa is not None and not isinstance(self.rearrangement__cdr2_aa, str):
            self.rearrangement__cdr2_aa = str(self.rearrangement__cdr2_aa)

        if self.rearrangement__cdr3 is not None and not isinstance(self.rearrangement__cdr3, str):
            self.rearrangement__cdr3 = str(self.rearrangement__cdr3)

        if self.rearrangement__cdr3_aa is not None and not isinstance(self.rearrangement__cdr3_aa, str):
            self.rearrangement__cdr3_aa = str(self.rearrangement__cdr3_aa)

        if self.rearrangement__fwr1 is not None and not isinstance(self.rearrangement__fwr1, str):
            self.rearrangement__fwr1 = str(self.rearrangement__fwr1)

        if self.rearrangement__fwr1_aa is not None and not isinstance(self.rearrangement__fwr1_aa, str):
            self.rearrangement__fwr1_aa = str(self.rearrangement__fwr1_aa)

        if self.rearrangement__fwr2 is not None and not isinstance(self.rearrangement__fwr2, str):
            self.rearrangement__fwr2 = str(self.rearrangement__fwr2)

        if self.rearrangement__fwr2_aa is not None and not isinstance(self.rearrangement__fwr2_aa, str):
            self.rearrangement__fwr2_aa = str(self.rearrangement__fwr2_aa)

        if self.rearrangement__fwr3 is not None and not isinstance(self.rearrangement__fwr3, str):
            self.rearrangement__fwr3 = str(self.rearrangement__fwr3)

        if self.rearrangement__fwr3_aa is not None and not isinstance(self.rearrangement__fwr3_aa, str):
            self.rearrangement__fwr3_aa = str(self.rearrangement__fwr3_aa)

        if self.rearrangement__fwr4 is not None and not isinstance(self.rearrangement__fwr4, str):
            self.rearrangement__fwr4 = str(self.rearrangement__fwr4)

        if self.rearrangement__fwr4_aa is not None and not isinstance(self.rearrangement__fwr4_aa, str):
            self.rearrangement__fwr4_aa = str(self.rearrangement__fwr4_aa)

        if self.rearrangement__v_score is not None and not isinstance(self.rearrangement__v_score, float):
            self.rearrangement__v_score = float(self.rearrangement__v_score)

        if self.rearrangement__v_identity is not None and not isinstance(self.rearrangement__v_identity, float):
            self.rearrangement__v_identity = float(self.rearrangement__v_identity)

        if self.rearrangement__v_support is not None and not isinstance(self.rearrangement__v_support, float):
            self.rearrangement__v_support = float(self.rearrangement__v_support)

        if self.rearrangement__d_score is not None and not isinstance(self.rearrangement__d_score, float):
            self.rearrangement__d_score = float(self.rearrangement__d_score)

        if self.rearrangement__d_identity is not None and not isinstance(self.rearrangement__d_identity, float):
            self.rearrangement__d_identity = float(self.rearrangement__d_identity)

        if self.rearrangement__d_support is not None and not isinstance(self.rearrangement__d_support, float):
            self.rearrangement__d_support = float(self.rearrangement__d_support)

        if self.rearrangement__d2_score is not None and not isinstance(self.rearrangement__d2_score, float):
            self.rearrangement__d2_score = float(self.rearrangement__d2_score)

        if self.rearrangement__d2_identity is not None and not isinstance(self.rearrangement__d2_identity, float):
            self.rearrangement__d2_identity = float(self.rearrangement__d2_identity)

        if self.rearrangement__d2_support is not None and not isinstance(self.rearrangement__d2_support, float):
            self.rearrangement__d2_support = float(self.rearrangement__d2_support)

        if self.rearrangement__d2_cigar is not None and not isinstance(self.rearrangement__d2_cigar, str):
            self.rearrangement__d2_cigar = str(self.rearrangement__d2_cigar)

        if self.rearrangement__j_score is not None and not isinstance(self.rearrangement__j_score, float):
            self.rearrangement__j_score = float(self.rearrangement__j_score)

        if self.rearrangement__j_identity is not None and not isinstance(self.rearrangement__j_identity, float):
            self.rearrangement__j_identity = float(self.rearrangement__j_identity)

        if self.rearrangement__j_support is not None and not isinstance(self.rearrangement__j_support, float):
            self.rearrangement__j_support = float(self.rearrangement__j_support)

        if self.rearrangement__c_score is not None and not isinstance(self.rearrangement__c_score, float):
            self.rearrangement__c_score = float(self.rearrangement__c_score)

        if self.rearrangement__c_identity is not None and not isinstance(self.rearrangement__c_identity, float):
            self.rearrangement__c_identity = float(self.rearrangement__c_identity)

        if self.rearrangement__c_support is not None and not isinstance(self.rearrangement__c_support, float):
            self.rearrangement__c_support = float(self.rearrangement__c_support)

        if self.rearrangement__c_cigar is not None and not isinstance(self.rearrangement__c_cigar, str):
            self.rearrangement__c_cigar = str(self.rearrangement__c_cigar)

        if self.rearrangement__v_sequence_start is not None and not isinstance(self.rearrangement__v_sequence_start, int):
            self.rearrangement__v_sequence_start = int(self.rearrangement__v_sequence_start)

        if self.rearrangement__v_sequence_end is not None and not isinstance(self.rearrangement__v_sequence_end, int):
            self.rearrangement__v_sequence_end = int(self.rearrangement__v_sequence_end)

        if self.rearrangement__v_germline_start is not None and not isinstance(self.rearrangement__v_germline_start, int):
            self.rearrangement__v_germline_start = int(self.rearrangement__v_germline_start)

        if self.rearrangement__v_germline_end is not None and not isinstance(self.rearrangement__v_germline_end, int):
            self.rearrangement__v_germline_end = int(self.rearrangement__v_germline_end)

        if self.rearrangement__v_alignment_start is not None and not isinstance(self.rearrangement__v_alignment_start, int):
            self.rearrangement__v_alignment_start = int(self.rearrangement__v_alignment_start)

        if self.rearrangement__v_alignment_end is not None and not isinstance(self.rearrangement__v_alignment_end, int):
            self.rearrangement__v_alignment_end = int(self.rearrangement__v_alignment_end)

        if self.rearrangement__d_sequence_start is not None and not isinstance(self.rearrangement__d_sequence_start, int):
            self.rearrangement__d_sequence_start = int(self.rearrangement__d_sequence_start)

        if self.rearrangement__d_sequence_end is not None and not isinstance(self.rearrangement__d_sequence_end, int):
            self.rearrangement__d_sequence_end = int(self.rearrangement__d_sequence_end)

        if self.rearrangement__d_germline_start is not None and not isinstance(self.rearrangement__d_germline_start, int):
            self.rearrangement__d_germline_start = int(self.rearrangement__d_germline_start)

        if self.rearrangement__d_germline_end is not None and not isinstance(self.rearrangement__d_germline_end, int):
            self.rearrangement__d_germline_end = int(self.rearrangement__d_germline_end)

        if self.rearrangement__d_alignment_start is not None and not isinstance(self.rearrangement__d_alignment_start, int):
            self.rearrangement__d_alignment_start = int(self.rearrangement__d_alignment_start)

        if self.rearrangement__d_alignment_end is not None and not isinstance(self.rearrangement__d_alignment_end, int):
            self.rearrangement__d_alignment_end = int(self.rearrangement__d_alignment_end)

        if self.rearrangement__d2_sequence_start is not None and not isinstance(self.rearrangement__d2_sequence_start, int):
            self.rearrangement__d2_sequence_start = int(self.rearrangement__d2_sequence_start)

        if self.rearrangement__d2_sequence_end is not None and not isinstance(self.rearrangement__d2_sequence_end, int):
            self.rearrangement__d2_sequence_end = int(self.rearrangement__d2_sequence_end)

        if self.rearrangement__d2_germline_start is not None and not isinstance(self.rearrangement__d2_germline_start, int):
            self.rearrangement__d2_germline_start = int(self.rearrangement__d2_germline_start)

        if self.rearrangement__d2_germline_end is not None and not isinstance(self.rearrangement__d2_germline_end, int):
            self.rearrangement__d2_germline_end = int(self.rearrangement__d2_germline_end)

        if self.rearrangement__d2_alignment_start is not None and not isinstance(self.rearrangement__d2_alignment_start, int):
            self.rearrangement__d2_alignment_start = int(self.rearrangement__d2_alignment_start)

        if self.rearrangement__d2_alignment_end is not None and not isinstance(self.rearrangement__d2_alignment_end, int):
            self.rearrangement__d2_alignment_end = int(self.rearrangement__d2_alignment_end)

        if self.rearrangement__j_sequence_start is not None and not isinstance(self.rearrangement__j_sequence_start, int):
            self.rearrangement__j_sequence_start = int(self.rearrangement__j_sequence_start)

        if self.rearrangement__j_sequence_end is not None and not isinstance(self.rearrangement__j_sequence_end, int):
            self.rearrangement__j_sequence_end = int(self.rearrangement__j_sequence_end)

        if self.rearrangement__j_germline_start is not None and not isinstance(self.rearrangement__j_germline_start, int):
            self.rearrangement__j_germline_start = int(self.rearrangement__j_germline_start)

        if self.rearrangement__j_germline_end is not None and not isinstance(self.rearrangement__j_germline_end, int):
            self.rearrangement__j_germline_end = int(self.rearrangement__j_germline_end)

        if self.rearrangement__j_alignment_start is not None and not isinstance(self.rearrangement__j_alignment_start, int):
            self.rearrangement__j_alignment_start = int(self.rearrangement__j_alignment_start)

        if self.rearrangement__j_alignment_end is not None and not isinstance(self.rearrangement__j_alignment_end, int):
            self.rearrangement__j_alignment_end = int(self.rearrangement__j_alignment_end)

        if self.rearrangement__c_sequence_start is not None and not isinstance(self.rearrangement__c_sequence_start, int):
            self.rearrangement__c_sequence_start = int(self.rearrangement__c_sequence_start)

        if self.rearrangement__c_sequence_end is not None and not isinstance(self.rearrangement__c_sequence_end, int):
            self.rearrangement__c_sequence_end = int(self.rearrangement__c_sequence_end)

        if self.rearrangement__c_germline_start is not None and not isinstance(self.rearrangement__c_germline_start, int):
            self.rearrangement__c_germline_start = int(self.rearrangement__c_germline_start)

        if self.rearrangement__c_germline_end is not None and not isinstance(self.rearrangement__c_germline_end, int):
            self.rearrangement__c_germline_end = int(self.rearrangement__c_germline_end)

        if self.rearrangement__c_alignment_start is not None and not isinstance(self.rearrangement__c_alignment_start, int):
            self.rearrangement__c_alignment_start = int(self.rearrangement__c_alignment_start)

        if self.rearrangement__c_alignment_end is not None and not isinstance(self.rearrangement__c_alignment_end, int):
            self.rearrangement__c_alignment_end = int(self.rearrangement__c_alignment_end)

        if self.rearrangement__cdr1_start is not None and not isinstance(self.rearrangement__cdr1_start, int):
            self.rearrangement__cdr1_start = int(self.rearrangement__cdr1_start)

        if self.rearrangement__cdr1_end is not None and not isinstance(self.rearrangement__cdr1_end, int):
            self.rearrangement__cdr1_end = int(self.rearrangement__cdr1_end)

        if self.rearrangement__cdr2_start is not None and not isinstance(self.rearrangement__cdr2_start, int):
            self.rearrangement__cdr2_start = int(self.rearrangement__cdr2_start)

        if self.rearrangement__cdr2_end is not None and not isinstance(self.rearrangement__cdr2_end, int):
            self.rearrangement__cdr2_end = int(self.rearrangement__cdr2_end)

        if self.rearrangement__cdr3_start is not None and not isinstance(self.rearrangement__cdr3_start, int):
            self.rearrangement__cdr3_start = int(self.rearrangement__cdr3_start)

        if self.rearrangement__cdr3_end is not None and not isinstance(self.rearrangement__cdr3_end, int):
            self.rearrangement__cdr3_end = int(self.rearrangement__cdr3_end)

        if self.rearrangement__fwr1_start is not None and not isinstance(self.rearrangement__fwr1_start, int):
            self.rearrangement__fwr1_start = int(self.rearrangement__fwr1_start)

        if self.rearrangement__fwr1_end is not None and not isinstance(self.rearrangement__fwr1_end, int):
            self.rearrangement__fwr1_end = int(self.rearrangement__fwr1_end)

        if self.rearrangement__fwr2_start is not None and not isinstance(self.rearrangement__fwr2_start, int):
            self.rearrangement__fwr2_start = int(self.rearrangement__fwr2_start)

        if self.rearrangement__fwr2_end is not None and not isinstance(self.rearrangement__fwr2_end, int):
            self.rearrangement__fwr2_end = int(self.rearrangement__fwr2_end)

        if self.rearrangement__fwr3_start is not None and not isinstance(self.rearrangement__fwr3_start, int):
            self.rearrangement__fwr3_start = int(self.rearrangement__fwr3_start)

        if self.rearrangement__fwr3_end is not None and not isinstance(self.rearrangement__fwr3_end, int):
            self.rearrangement__fwr3_end = int(self.rearrangement__fwr3_end)

        if self.rearrangement__fwr4_start is not None and not isinstance(self.rearrangement__fwr4_start, int):
            self.rearrangement__fwr4_start = int(self.rearrangement__fwr4_start)

        if self.rearrangement__fwr4_end is not None and not isinstance(self.rearrangement__fwr4_end, int):
            self.rearrangement__fwr4_end = int(self.rearrangement__fwr4_end)

        if self.rearrangement__v_sequence_alignment is not None and not isinstance(self.rearrangement__v_sequence_alignment, str):
            self.rearrangement__v_sequence_alignment = str(self.rearrangement__v_sequence_alignment)

        if self.rearrangement__v_sequence_alignment_aa is not None and not isinstance(self.rearrangement__v_sequence_alignment_aa, str):
            self.rearrangement__v_sequence_alignment_aa = str(self.rearrangement__v_sequence_alignment_aa)

        if self.rearrangement__d_sequence_alignment is not None and not isinstance(self.rearrangement__d_sequence_alignment, str):
            self.rearrangement__d_sequence_alignment = str(self.rearrangement__d_sequence_alignment)

        if self.rearrangement__d_sequence_alignment_aa is not None and not isinstance(self.rearrangement__d_sequence_alignment_aa, str):
            self.rearrangement__d_sequence_alignment_aa = str(self.rearrangement__d_sequence_alignment_aa)

        if self.rearrangement__d2_sequence_alignment is not None and not isinstance(self.rearrangement__d2_sequence_alignment, str):
            self.rearrangement__d2_sequence_alignment = str(self.rearrangement__d2_sequence_alignment)

        if self.rearrangement__d2_sequence_alignment_aa is not None and not isinstance(self.rearrangement__d2_sequence_alignment_aa, str):
            self.rearrangement__d2_sequence_alignment_aa = str(self.rearrangement__d2_sequence_alignment_aa)

        if self.rearrangement__j_sequence_alignment is not None and not isinstance(self.rearrangement__j_sequence_alignment, str):
            self.rearrangement__j_sequence_alignment = str(self.rearrangement__j_sequence_alignment)

        if self.rearrangement__j_sequence_alignment_aa is not None and not isinstance(self.rearrangement__j_sequence_alignment_aa, str):
            self.rearrangement__j_sequence_alignment_aa = str(self.rearrangement__j_sequence_alignment_aa)

        if self.rearrangement__c_sequence_alignment is not None and not isinstance(self.rearrangement__c_sequence_alignment, str):
            self.rearrangement__c_sequence_alignment = str(self.rearrangement__c_sequence_alignment)

        if self.rearrangement__c_sequence_alignment_aa is not None and not isinstance(self.rearrangement__c_sequence_alignment_aa, str):
            self.rearrangement__c_sequence_alignment_aa = str(self.rearrangement__c_sequence_alignment_aa)

        if self.rearrangement__v_germline_alignment is not None and not isinstance(self.rearrangement__v_germline_alignment, str):
            self.rearrangement__v_germline_alignment = str(self.rearrangement__v_germline_alignment)

        if self.rearrangement__v_germline_alignment_aa is not None and not isinstance(self.rearrangement__v_germline_alignment_aa, str):
            self.rearrangement__v_germline_alignment_aa = str(self.rearrangement__v_germline_alignment_aa)

        if self.rearrangement__d_germline_alignment is not None and not isinstance(self.rearrangement__d_germline_alignment, str):
            self.rearrangement__d_germline_alignment = str(self.rearrangement__d_germline_alignment)

        if self.rearrangement__d_germline_alignment_aa is not None and not isinstance(self.rearrangement__d_germline_alignment_aa, str):
            self.rearrangement__d_germline_alignment_aa = str(self.rearrangement__d_germline_alignment_aa)

        if self.rearrangement__d2_germline_alignment is not None and not isinstance(self.rearrangement__d2_germline_alignment, str):
            self.rearrangement__d2_germline_alignment = str(self.rearrangement__d2_germline_alignment)

        if self.rearrangement__d2_germline_alignment_aa is not None and not isinstance(self.rearrangement__d2_germline_alignment_aa, str):
            self.rearrangement__d2_germline_alignment_aa = str(self.rearrangement__d2_germline_alignment_aa)

        if self.rearrangement__j_germline_alignment is not None and not isinstance(self.rearrangement__j_germline_alignment, str):
            self.rearrangement__j_germline_alignment = str(self.rearrangement__j_germline_alignment)

        if self.rearrangement__j_germline_alignment_aa is not None and not isinstance(self.rearrangement__j_germline_alignment_aa, str):
            self.rearrangement__j_germline_alignment_aa = str(self.rearrangement__j_germline_alignment_aa)

        if self.rearrangement__c_germline_alignment is not None and not isinstance(self.rearrangement__c_germline_alignment, str):
            self.rearrangement__c_germline_alignment = str(self.rearrangement__c_germline_alignment)

        if self.rearrangement__c_germline_alignment_aa is not None and not isinstance(self.rearrangement__c_germline_alignment_aa, str):
            self.rearrangement__c_germline_alignment_aa = str(self.rearrangement__c_germline_alignment_aa)

        if self.rearrangement__junction_length is not None and not isinstance(self.rearrangement__junction_length, int):
            self.rearrangement__junction_length = int(self.rearrangement__junction_length)

        if self.rearrangement__junction_aa_length is not None and not isinstance(self.rearrangement__junction_aa_length, int):
            self.rearrangement__junction_aa_length = int(self.rearrangement__junction_aa_length)

        if self.rearrangement__np1_length is not None and not isinstance(self.rearrangement__np1_length, int):
            self.rearrangement__np1_length = int(self.rearrangement__np1_length)

        if self.rearrangement__np2_length is not None and not isinstance(self.rearrangement__np2_length, int):
            self.rearrangement__np2_length = int(self.rearrangement__np2_length)

        if self.rearrangement__np3_length is not None and not isinstance(self.rearrangement__np3_length, int):
            self.rearrangement__np3_length = int(self.rearrangement__np3_length)

        if self.rearrangement__n1_length is not None and not isinstance(self.rearrangement__n1_length, int):
            self.rearrangement__n1_length = int(self.rearrangement__n1_length)

        if self.rearrangement__n2_length is not None and not isinstance(self.rearrangement__n2_length, int):
            self.rearrangement__n2_length = int(self.rearrangement__n2_length)

        if self.rearrangement__n3_length is not None and not isinstance(self.rearrangement__n3_length, int):
            self.rearrangement__n3_length = int(self.rearrangement__n3_length)

        if self.rearrangement__p3v_length is not None and not isinstance(self.rearrangement__p3v_length, int):
            self.rearrangement__p3v_length = int(self.rearrangement__p3v_length)

        if self.rearrangement__p5d_length is not None and not isinstance(self.rearrangement__p5d_length, int):
            self.rearrangement__p5d_length = int(self.rearrangement__p5d_length)

        if self.rearrangement__p3d_length is not None and not isinstance(self.rearrangement__p3d_length, int):
            self.rearrangement__p3d_length = int(self.rearrangement__p3d_length)

        if self.rearrangement__p5d2_length is not None and not isinstance(self.rearrangement__p5d2_length, int):
            self.rearrangement__p5d2_length = int(self.rearrangement__p5d2_length)

        if self.rearrangement__p3d2_length is not None and not isinstance(self.rearrangement__p3d2_length, int):
            self.rearrangement__p3d2_length = int(self.rearrangement__p3d2_length)

        if self.rearrangement__p5j_length is not None and not isinstance(self.rearrangement__p5j_length, int):
            self.rearrangement__p5j_length = int(self.rearrangement__p5j_length)

        if self.rearrangement__v_frameshift is not None and not isinstance(self.rearrangement__v_frameshift, Bool):
            self.rearrangement__v_frameshift = Bool(self.rearrangement__v_frameshift)

        if self.rearrangement__j_frameshift is not None and not isinstance(self.rearrangement__j_frameshift, Bool):
            self.rearrangement__j_frameshift = Bool(self.rearrangement__j_frameshift)

        if self.rearrangement__d_frame is not None and not isinstance(self.rearrangement__d_frame, int):
            self.rearrangement__d_frame = int(self.rearrangement__d_frame)

        if self.rearrangement__d2_frame is not None and not isinstance(self.rearrangement__d2_frame, int):
            self.rearrangement__d2_frame = int(self.rearrangement__d2_frame)

        if self.rearrangement__consensus_count is not None and not isinstance(self.rearrangement__consensus_count, int):
            self.rearrangement__consensus_count = int(self.rearrangement__consensus_count)

        if self.rearrangement__duplicate_count is not None and not isinstance(self.rearrangement__duplicate_count, int):
            self.rearrangement__duplicate_count = int(self.rearrangement__duplicate_count)

        if self.rearrangement__umi_count is not None and not isinstance(self.rearrangement__umi_count, int):
            self.rearrangement__umi_count = int(self.rearrangement__umi_count)

        if self.rearrangement__cell_id is not None and not isinstance(self.rearrangement__cell_id, str):
            self.rearrangement__cell_id = str(self.rearrangement__cell_id)

        if self.rearrangement__clone_id is not None and not isinstance(self.rearrangement__clone_id, str):
            self.rearrangement__clone_id = str(self.rearrangement__clone_id)

        if self.rearrangement__reactivity_id is not None and not isinstance(self.rearrangement__reactivity_id, str):
            self.rearrangement__reactivity_id = str(self.rearrangement__reactivity_id)

        if self.rearrangement__reactivity_ref is not None and not isinstance(self.rearrangement__reactivity_ref, str):
            self.rearrangement__reactivity_ref = str(self.rearrangement__reactivity_ref)

        if self.rearrangement__repertoire_id is not None and not isinstance(self.rearrangement__repertoire_id, str):
            self.rearrangement__repertoire_id = str(self.rearrangement__repertoire_id)

        if self.rearrangement__sample_processing_id is not None and not isinstance(self.rearrangement__sample_processing_id, str):
            self.rearrangement__sample_processing_id = str(self.rearrangement__sample_processing_id)

        if self.rearrangement__data_processing_id is not None and not isinstance(self.rearrangement__data_processing_id, str):
            self.rearrangement__data_processing_id = str(self.rearrangement__data_processing_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Clone(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Clone"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Clone"
    class_name: ClassVar[str] = "V1p4_Clone"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Clone

    clone__clone_id: str = None
    clone__germline_alignment: str = None
    clone__repertoire_id: Optional[str] = None
    clone__data_processing_id: Optional[str] = None
    clone__sequences: Optional[Union[str, List[str]]] = empty_list()
    clone__v_call: Optional[str] = None
    clone__d_call: Optional[str] = None
    clone__j_call: Optional[str] = None
    clone__junction: Optional[str] = None
    clone__junction_aa: Optional[str] = None
    clone__junction_length: Optional[int] = None
    clone__junction_aa_length: Optional[int] = None
    clone__germline_alignment_aa: Optional[str] = None
    clone__v_alignment_start: Optional[int] = None
    clone__v_alignment_end: Optional[int] = None
    clone__d_alignment_start: Optional[int] = None
    clone__d_alignment_end: Optional[int] = None
    clone__j_alignment_start: Optional[int] = None
    clone__j_alignment_end: Optional[int] = None
    clone__junction_start: Optional[int] = None
    clone__junction_end: Optional[int] = None
    clone__umi_count: Optional[int] = None
    clone__clone_count: Optional[int] = None
    clone__seed_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.clone__clone_id):
            self.MissingRequiredField("clone__clone_id")
        if not isinstance(self.clone__clone_id, str):
            self.clone__clone_id = str(self.clone__clone_id)

        if self._is_empty(self.clone__germline_alignment):
            self.MissingRequiredField("clone__germline_alignment")
        if not isinstance(self.clone__germline_alignment, str):
            self.clone__germline_alignment = str(self.clone__germline_alignment)

        if self.clone__repertoire_id is not None and not isinstance(self.clone__repertoire_id, str):
            self.clone__repertoire_id = str(self.clone__repertoire_id)

        if self.clone__data_processing_id is not None and not isinstance(self.clone__data_processing_id, str):
            self.clone__data_processing_id = str(self.clone__data_processing_id)

        if not isinstance(self.clone__sequences, list):
            self.clone__sequences = [self.clone__sequences] if self.clone__sequences is not None else []
        self.clone__sequences = [v if isinstance(v, str) else str(v) for v in self.clone__sequences]

        if self.clone__v_call is not None and not isinstance(self.clone__v_call, str):
            self.clone__v_call = str(self.clone__v_call)

        if self.clone__d_call is not None and not isinstance(self.clone__d_call, str):
            self.clone__d_call = str(self.clone__d_call)

        if self.clone__j_call is not None and not isinstance(self.clone__j_call, str):
            self.clone__j_call = str(self.clone__j_call)

        if self.clone__junction is not None and not isinstance(self.clone__junction, str):
            self.clone__junction = str(self.clone__junction)

        if self.clone__junction_aa is not None and not isinstance(self.clone__junction_aa, str):
            self.clone__junction_aa = str(self.clone__junction_aa)

        if self.clone__junction_length is not None and not isinstance(self.clone__junction_length, int):
            self.clone__junction_length = int(self.clone__junction_length)

        if self.clone__junction_aa_length is not None and not isinstance(self.clone__junction_aa_length, int):
            self.clone__junction_aa_length = int(self.clone__junction_aa_length)

        if self.clone__germline_alignment_aa is not None and not isinstance(self.clone__germline_alignment_aa, str):
            self.clone__germline_alignment_aa = str(self.clone__germline_alignment_aa)

        if self.clone__v_alignment_start is not None and not isinstance(self.clone__v_alignment_start, int):
            self.clone__v_alignment_start = int(self.clone__v_alignment_start)

        if self.clone__v_alignment_end is not None and not isinstance(self.clone__v_alignment_end, int):
            self.clone__v_alignment_end = int(self.clone__v_alignment_end)

        if self.clone__d_alignment_start is not None and not isinstance(self.clone__d_alignment_start, int):
            self.clone__d_alignment_start = int(self.clone__d_alignment_start)

        if self.clone__d_alignment_end is not None and not isinstance(self.clone__d_alignment_end, int):
            self.clone__d_alignment_end = int(self.clone__d_alignment_end)

        if self.clone__j_alignment_start is not None and not isinstance(self.clone__j_alignment_start, int):
            self.clone__j_alignment_start = int(self.clone__j_alignment_start)

        if self.clone__j_alignment_end is not None and not isinstance(self.clone__j_alignment_end, int):
            self.clone__j_alignment_end = int(self.clone__j_alignment_end)

        if self.clone__junction_start is not None and not isinstance(self.clone__junction_start, int):
            self.clone__junction_start = int(self.clone__junction_start)

        if self.clone__junction_end is not None and not isinstance(self.clone__junction_end, int):
            self.clone__junction_end = int(self.clone__junction_end)

        if self.clone__umi_count is not None and not isinstance(self.clone__umi_count, int):
            self.clone__umi_count = int(self.clone__umi_count)

        if self.clone__clone_count is not None and not isinstance(self.clone__clone_count, int):
            self.clone__clone_count = int(self.clone__clone_count)

        if self.clone__seed_id is not None and not isinstance(self.clone__seed_id, str):
            self.clone__seed_id = str(self.clone__seed_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Tree(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Tree"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Tree"
    class_name: ClassVar[str] = "V1p4_Tree"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Tree

    tree__tree_id: str = None
    tree__clone_id: str = None
    tree__newick: str = None
    tree__nodes: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.tree__tree_id):
            self.MissingRequiredField("tree__tree_id")
        if not isinstance(self.tree__tree_id, str):
            self.tree__tree_id = str(self.tree__tree_id)

        if self._is_empty(self.tree__clone_id):
            self.MissingRequiredField("tree__clone_id")
        if not isinstance(self.tree__clone_id, str):
            self.tree__clone_id = str(self.tree__clone_id)

        if self._is_empty(self.tree__newick):
            self.MissingRequiredField("tree__newick")
        if not isinstance(self.tree__newick, str):
            self.tree__newick = str(self.tree__newick)

        if self.tree__nodes is not None and not isinstance(self.tree__nodes, str):
            self.tree__nodes = str(self.tree__nodes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Node(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Node"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Node"
    class_name: ClassVar[str] = "V1p4_Node"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Node

    node__sequence_id: str = None
    node__sequence_alignment: Optional[str] = None
    node__junction: Optional[str] = None
    node__junction_aa: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.node__sequence_id):
            self.MissingRequiredField("node__sequence_id")
        if not isinstance(self.node__sequence_id, str):
            self.node__sequence_id = str(self.node__sequence_id)

        if self.node__sequence_alignment is not None and not isinstance(self.node__sequence_alignment, str):
            self.node__sequence_alignment = str(self.node__sequence_alignment)

        if self.node__junction is not None and not isinstance(self.node__junction, str):
            self.node__junction = str(self.node__junction)

        if self.node__junction_aa is not None and not isinstance(self.node__junction_aa, str):
            self.node__junction_aa = str(self.node__junction_aa)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Cell(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Cell"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Cell"
    class_name: ClassVar[str] = "V1p4_Cell"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Cell

    cell__cell_id: str = None
    cell__repertoire_id: str = None
    cell__virtual_pairing: Union[bool, Bool] = None
    cell__data_processing_id: Optional[str] = None
    cell__receptors: Optional[Union[str, List[str]]] = empty_list()
    cell__cell_subset: Optional[Union[str, "V1p4CellSubset"]] = None
    cell__cell_phenotype: Optional[str] = None
    cell__cell_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.cell__cell_id):
            self.MissingRequiredField("cell__cell_id")
        if not isinstance(self.cell__cell_id, str):
            self.cell__cell_id = str(self.cell__cell_id)

        if self._is_empty(self.cell__repertoire_id):
            self.MissingRequiredField("cell__repertoire_id")
        if not isinstance(self.cell__repertoire_id, str):
            self.cell__repertoire_id = str(self.cell__repertoire_id)

        if self._is_empty(self.cell__virtual_pairing):
            self.MissingRequiredField("cell__virtual_pairing")
        if not isinstance(self.cell__virtual_pairing, Bool):
            self.cell__virtual_pairing = Bool(self.cell__virtual_pairing)

        if self.cell__data_processing_id is not None and not isinstance(self.cell__data_processing_id, str):
            self.cell__data_processing_id = str(self.cell__data_processing_id)

        if not isinstance(self.cell__receptors, list):
            self.cell__receptors = [self.cell__receptors] if self.cell__receptors is not None else []
        self.cell__receptors = [v if isinstance(v, str) else str(v) for v in self.cell__receptors]

        if self.cell__cell_phenotype is not None and not isinstance(self.cell__cell_phenotype, str):
            self.cell__cell_phenotype = str(self.cell__cell_phenotype)

        if self.cell__cell_label is not None and not isinstance(self.cell__cell_label, str):
            self.cell__cell_label = str(self.cell__cell_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Expression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Expression"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Expression"
    class_name: ClassVar[str] = "V1p4_Expression"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Expression

    expression__expression_id: str = None
    expression__cell_id: str = None
    expression__repertoire_id: str = None
    expression__data_processing_id: str = None
    expression__property_type: str = None
    expression__property: Union[str, "V1p4Property"] = None
    expression__value: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.expression__expression_id):
            self.MissingRequiredField("expression__expression_id")
        if not isinstance(self.expression__expression_id, str):
            self.expression__expression_id = str(self.expression__expression_id)

        if self._is_empty(self.expression__cell_id):
            self.MissingRequiredField("expression__cell_id")
        if not isinstance(self.expression__cell_id, str):
            self.expression__cell_id = str(self.expression__cell_id)

        if self._is_empty(self.expression__repertoire_id):
            self.MissingRequiredField("expression__repertoire_id")
        if not isinstance(self.expression__repertoire_id, str):
            self.expression__repertoire_id = str(self.expression__repertoire_id)

        if self._is_empty(self.expression__data_processing_id):
            self.MissingRequiredField("expression__data_processing_id")
        if not isinstance(self.expression__data_processing_id, str):
            self.expression__data_processing_id = str(self.expression__data_processing_id)

        if self._is_empty(self.expression__property_type):
            self.MissingRequiredField("expression__property_type")
        if not isinstance(self.expression__property_type, str):
            self.expression__property_type = str(self.expression__property_type)

        if self._is_empty(self.expression__value):
            self.MissingRequiredField("expression__value")
        if not isinstance(self.expression__value, float):
            self.expression__value = float(self.expression__value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Receptor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Receptor"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Receptor"
    class_name: ClassVar[str] = "V1p4_Receptor"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Receptor

    receptor__receptor_id: str = None
    receptor__receptor_hash: str = None
    receptor__receptor_type: Union[str, "V1p4ReceptorType"] = None
    receptor__receptor_variable_domain_1_aa: str = None
    receptor__receptor_variable_domain_1_locus: Union[str, "V1p4ReceptorVariableDomain1Locus"] = None
    receptor__receptor_variable_domain_2_aa: str = None
    receptor__receptor_variable_domain_2_locus: Union[str, "V1p4ReceptorVariableDomain2Locus"] = None
    receptor__receptor_ref: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.receptor__receptor_id):
            self.MissingRequiredField("receptor__receptor_id")
        if not isinstance(self.receptor__receptor_id, str):
            self.receptor__receptor_id = str(self.receptor__receptor_id)

        if self._is_empty(self.receptor__receptor_hash):
            self.MissingRequiredField("receptor__receptor_hash")
        if not isinstance(self.receptor__receptor_hash, str):
            self.receptor__receptor_hash = str(self.receptor__receptor_hash)

        if self._is_empty(self.receptor__receptor_type):
            self.MissingRequiredField("receptor__receptor_type")
        if not isinstance(self.receptor__receptor_type, V1p4ReceptorType):
            self.receptor__receptor_type = V1p4ReceptorType(self.receptor__receptor_type)

        if self._is_empty(self.receptor__receptor_variable_domain_1_aa):
            self.MissingRequiredField("receptor__receptor_variable_domain_1_aa")
        if not isinstance(self.receptor__receptor_variable_domain_1_aa, str):
            self.receptor__receptor_variable_domain_1_aa = str(self.receptor__receptor_variable_domain_1_aa)

        if self._is_empty(self.receptor__receptor_variable_domain_1_locus):
            self.MissingRequiredField("receptor__receptor_variable_domain_1_locus")
        if not isinstance(self.receptor__receptor_variable_domain_1_locus, V1p4ReceptorVariableDomain1Locus):
            self.receptor__receptor_variable_domain_1_locus = V1p4ReceptorVariableDomain1Locus(self.receptor__receptor_variable_domain_1_locus)

        if self._is_empty(self.receptor__receptor_variable_domain_2_aa):
            self.MissingRequiredField("receptor__receptor_variable_domain_2_aa")
        if not isinstance(self.receptor__receptor_variable_domain_2_aa, str):
            self.receptor__receptor_variable_domain_2_aa = str(self.receptor__receptor_variable_domain_2_aa)

        if self._is_empty(self.receptor__receptor_variable_domain_2_locus):
            self.MissingRequiredField("receptor__receptor_variable_domain_2_locus")
        if not isinstance(self.receptor__receptor_variable_domain_2_locus, V1p4ReceptorVariableDomain2Locus):
            self.receptor__receptor_variable_domain_2_locus = V1p4ReceptorVariableDomain2Locus(self.receptor__receptor_variable_domain_2_locus)

        if not isinstance(self.receptor__receptor_ref, list):
            self.receptor__receptor_ref = [self.receptor__receptor_ref] if self.receptor__receptor_ref is not None else []
        self.receptor__receptor_ref = [v if isinstance(v, str) else str(v) for v in self.receptor__receptor_ref]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Reactivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Reactivity"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Reactivity"
    class_name: ClassVar[str] = "V1p4_Reactivity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Reactivity

    reactivity__reactivity_id: str = None
    reactivity__cell_id: str = None
    reactivity__ligand_type: Union[str, "V1p4LigandType"] = None
    reactivity__antigen_type: Union[str, "V1p4AntigenType"] = None
    reactivity__antigen: Union[str, "V1p4Antigen"] = None
    reactivity__reactivity_method: str = None
    reactivity__reactivity_readout: str = None
    reactivity__reactivity_value: float = None
    reactivity__reactivity_unit: str = None
    reactivity__repertoire_id: Optional[str] = None
    reactivity__data_processing_id: Optional[str] = None
    reactivity__antigen_source_species: Optional[Union[str, "V1p4AntigenSourceSpecies"]] = None
    reactivity__peptide_start: Optional[int] = None
    reactivity__peptide_end: Optional[int] = None
    reactivity__peptide_sequence_aa: Optional[str] = None
    reactivity__mhc_class: Optional[Union[str, "V1p4MhcClass"]] = None
    reactivity__mhc_gene_1: Optional[Union[str, "V1p4MhcGene1"]] = None
    reactivity__mhc_allele_1: Optional[str] = None
    reactivity__mhc_gene_2: Optional[Union[str, "V1p4MhcGene2"]] = None
    reactivity__mhc_allele_2: Optional[str] = None
    reactivity__reactivity_ref: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.reactivity__reactivity_id):
            self.MissingRequiredField("reactivity__reactivity_id")
        if not isinstance(self.reactivity__reactivity_id, str):
            self.reactivity__reactivity_id = str(self.reactivity__reactivity_id)

        if self._is_empty(self.reactivity__cell_id):
            self.MissingRequiredField("reactivity__cell_id")
        if not isinstance(self.reactivity__cell_id, str):
            self.reactivity__cell_id = str(self.reactivity__cell_id)

        if self._is_empty(self.reactivity__ligand_type):
            self.MissingRequiredField("reactivity__ligand_type")
        if not isinstance(self.reactivity__ligand_type, V1p4LigandType):
            self.reactivity__ligand_type = V1p4LigandType(self.reactivity__ligand_type)

        if self._is_empty(self.reactivity__antigen_type):
            self.MissingRequiredField("reactivity__antigen_type")
        if not isinstance(self.reactivity__antigen_type, V1p4AntigenType):
            self.reactivity__antigen_type = V1p4AntigenType(self.reactivity__antigen_type)

        if self._is_empty(self.reactivity__reactivity_method):
            self.MissingRequiredField("reactivity__reactivity_method")
        if not isinstance(self.reactivity__reactivity_method, str):
            self.reactivity__reactivity_method = str(self.reactivity__reactivity_method)

        if self._is_empty(self.reactivity__reactivity_readout):
            self.MissingRequiredField("reactivity__reactivity_readout")
        if not isinstance(self.reactivity__reactivity_readout, str):
            self.reactivity__reactivity_readout = str(self.reactivity__reactivity_readout)

        if self._is_empty(self.reactivity__reactivity_value):
            self.MissingRequiredField("reactivity__reactivity_value")
        if not isinstance(self.reactivity__reactivity_value, float):
            self.reactivity__reactivity_value = float(self.reactivity__reactivity_value)

        if self._is_empty(self.reactivity__reactivity_unit):
            self.MissingRequiredField("reactivity__reactivity_unit")
        if not isinstance(self.reactivity__reactivity_unit, str):
            self.reactivity__reactivity_unit = str(self.reactivity__reactivity_unit)

        if self.reactivity__repertoire_id is not None and not isinstance(self.reactivity__repertoire_id, str):
            self.reactivity__repertoire_id = str(self.reactivity__repertoire_id)

        if self.reactivity__data_processing_id is not None and not isinstance(self.reactivity__data_processing_id, str):
            self.reactivity__data_processing_id = str(self.reactivity__data_processing_id)

        if self.reactivity__peptide_start is not None and not isinstance(self.reactivity__peptide_start, int):
            self.reactivity__peptide_start = int(self.reactivity__peptide_start)

        if self.reactivity__peptide_end is not None and not isinstance(self.reactivity__peptide_end, int):
            self.reactivity__peptide_end = int(self.reactivity__peptide_end)

        if self.reactivity__peptide_sequence_aa is not None and not isinstance(self.reactivity__peptide_sequence_aa, str):
            self.reactivity__peptide_sequence_aa = str(self.reactivity__peptide_sequence_aa)

        if self.reactivity__mhc_class is not None and not isinstance(self.reactivity__mhc_class, V1p4MhcClass):
            self.reactivity__mhc_class = V1p4MhcClass(self.reactivity__mhc_class)

        if self.reactivity__mhc_allele_1 is not None and not isinstance(self.reactivity__mhc_allele_1, str):
            self.reactivity__mhc_allele_1 = str(self.reactivity__mhc_allele_1)

        if self.reactivity__mhc_allele_2 is not None and not isinstance(self.reactivity__mhc_allele_2, str):
            self.reactivity__mhc_allele_2 = str(self.reactivity__mhc_allele_2)

        if not isinstance(self.reactivity__reactivity_ref, list):
            self.reactivity__reactivity_ref = [self.reactivity__reactivity_ref] if self.reactivity__reactivity_ref is not None else []
        self.reactivity__reactivity_ref = [v if isinstance(v, str) else str(v) for v in self.reactivity__reactivity_ref]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SampleProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SampleProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SampleProcessing"
    class_name: ClassVar[str] = "V1p4_SampleProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SampleProcessing

    sample__sample_id: str = None
    sample__sample_type: str = None
    sample__tissue: Union[str, "V1p4Tissue"] = None
    sample__anatomic_site: str = None
    sample__disease_state_sample: str = None
    sample__collection_time_point_relative: Union[dict, V1p4TimePoint] = None
    sample__biomaterial_provider: str = None
    cell_processing__tissue_processing: str = None
    cell_processing__cell_subset: Union[str, "V1p4CellSubset"] = None
    cell_processing__cell_phenotype: str = None
    cell_processing__single_cell: Union[bool, Bool] = None
    cell_processing__cell_number: int = None
    cell_processing__cells_per_reaction: int = None
    cell_processing__cell_storage: Union[bool, Bool] = None
    cell_processing__cell_quality: str = None
    cell_processing__cell_isolation: str = None
    cell_processing__cell_processing_protocol: str = None
    nucleic_acid_processing__template_class: Union[str, "V1p4TemplateClass"] = None
    nucleic_acid_processing__template_quality: str = None
    nucleic_acid_processing__template_amount: Union[dict, V1p4PhysicalQuantity] = None
    nucleic_acid_processing__library_generation_method: Union[str, "V1p4LibraryGenerationMethod"] = None
    nucleic_acid_processing__library_generation_protocol: str = None
    nucleic_acid_processing__library_generation_kit_version: str = None
    nucleic_acid_processing__complete_sequences: Union[str, "V1p4CompleteSequences"] = None
    nucleic_acid_processing__physical_linkage: Union[str, "V1p4PhysicalLinkage"] = None
    sequencing_run__sequencing_run_id: str = None
    sequencing_run__total_reads_passing_qc_filter: int = None
    sequencing_run__sequencing_platform: str = None
    sequencing_run__sequencing_facility: str = None
    sequencing_run__sequencing_run_date: str = None
    sequencing_run__sequencing_kit: str = None
    sample_processing__sample_processing_id: Optional[str] = None
    sample__collection_location: Optional[Union[str, "V1p4CollectionLocation"]] = None
    cell_processing__cell_label: Optional[str] = None
    cell_processing__cell_species: Optional[Union[str, "V1p4CellSpecies"]] = None
    nucleic_acid_processing__pcr_target: Optional[Union[Union[dict, V1p4PCRTarget], List[Union[dict, V1p4PCRTarget]]]] = empty_list()
    sequencing_run__sequencing_files: Optional[Union[dict, V1p4SequencingData]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sample__sample_id):
            self.MissingRequiredField("sample__sample_id")
        if not isinstance(self.sample__sample_id, str):
            self.sample__sample_id = str(self.sample__sample_id)

        if self._is_empty(self.sample__sample_type):
            self.MissingRequiredField("sample__sample_type")
        if not isinstance(self.sample__sample_type, str):
            self.sample__sample_type = str(self.sample__sample_type)

        if self._is_empty(self.sample__anatomic_site):
            self.MissingRequiredField("sample__anatomic_site")
        if not isinstance(self.sample__anatomic_site, str):
            self.sample__anatomic_site = str(self.sample__anatomic_site)

        if self._is_empty(self.sample__disease_state_sample):
            self.MissingRequiredField("sample__disease_state_sample")
        if not isinstance(self.sample__disease_state_sample, str):
            self.sample__disease_state_sample = str(self.sample__disease_state_sample)

        if self._is_empty(self.sample__collection_time_point_relative):
            self.MissingRequiredField("sample__collection_time_point_relative")
        if not isinstance(self.sample__collection_time_point_relative, V1p4TimePoint):
            self.sample__collection_time_point_relative = V1p4TimePoint(**as_dict(self.sample__collection_time_point_relative))

        if self._is_empty(self.sample__biomaterial_provider):
            self.MissingRequiredField("sample__biomaterial_provider")
        if not isinstance(self.sample__biomaterial_provider, str):
            self.sample__biomaterial_provider = str(self.sample__biomaterial_provider)

        if self._is_empty(self.cell_processing__tissue_processing):
            self.MissingRequiredField("cell_processing__tissue_processing")
        if not isinstance(self.cell_processing__tissue_processing, str):
            self.cell_processing__tissue_processing = str(self.cell_processing__tissue_processing)

        if self._is_empty(self.cell_processing__cell_phenotype):
            self.MissingRequiredField("cell_processing__cell_phenotype")
        if not isinstance(self.cell_processing__cell_phenotype, str):
            self.cell_processing__cell_phenotype = str(self.cell_processing__cell_phenotype)

        if self._is_empty(self.cell_processing__single_cell):
            self.MissingRequiredField("cell_processing__single_cell")
        if not isinstance(self.cell_processing__single_cell, Bool):
            self.cell_processing__single_cell = Bool(self.cell_processing__single_cell)

        if self._is_empty(self.cell_processing__cell_number):
            self.MissingRequiredField("cell_processing__cell_number")
        if not isinstance(self.cell_processing__cell_number, int):
            self.cell_processing__cell_number = int(self.cell_processing__cell_number)

        if self._is_empty(self.cell_processing__cells_per_reaction):
            self.MissingRequiredField("cell_processing__cells_per_reaction")
        if not isinstance(self.cell_processing__cells_per_reaction, int):
            self.cell_processing__cells_per_reaction = int(self.cell_processing__cells_per_reaction)

        if self._is_empty(self.cell_processing__cell_storage):
            self.MissingRequiredField("cell_processing__cell_storage")
        if not isinstance(self.cell_processing__cell_storage, Bool):
            self.cell_processing__cell_storage = Bool(self.cell_processing__cell_storage)

        if self._is_empty(self.cell_processing__cell_quality):
            self.MissingRequiredField("cell_processing__cell_quality")
        if not isinstance(self.cell_processing__cell_quality, str):
            self.cell_processing__cell_quality = str(self.cell_processing__cell_quality)

        if self._is_empty(self.cell_processing__cell_isolation):
            self.MissingRequiredField("cell_processing__cell_isolation")
        if not isinstance(self.cell_processing__cell_isolation, str):
            self.cell_processing__cell_isolation = str(self.cell_processing__cell_isolation)

        if self._is_empty(self.cell_processing__cell_processing_protocol):
            self.MissingRequiredField("cell_processing__cell_processing_protocol")
        if not isinstance(self.cell_processing__cell_processing_protocol, str):
            self.cell_processing__cell_processing_protocol = str(self.cell_processing__cell_processing_protocol)

        if self._is_empty(self.nucleic_acid_processing__template_class):
            self.MissingRequiredField("nucleic_acid_processing__template_class")
        if not isinstance(self.nucleic_acid_processing__template_class, V1p4TemplateClass):
            self.nucleic_acid_processing__template_class = V1p4TemplateClass(self.nucleic_acid_processing__template_class)

        if self._is_empty(self.nucleic_acid_processing__template_quality):
            self.MissingRequiredField("nucleic_acid_processing__template_quality")
        if not isinstance(self.nucleic_acid_processing__template_quality, str):
            self.nucleic_acid_processing__template_quality = str(self.nucleic_acid_processing__template_quality)

        if self._is_empty(self.nucleic_acid_processing__template_amount):
            self.MissingRequiredField("nucleic_acid_processing__template_amount")
        if not isinstance(self.nucleic_acid_processing__template_amount, V1p4PhysicalQuantity):
            self.nucleic_acid_processing__template_amount = V1p4PhysicalQuantity(**as_dict(self.nucleic_acid_processing__template_amount))

        if self._is_empty(self.nucleic_acid_processing__library_generation_method):
            self.MissingRequiredField("nucleic_acid_processing__library_generation_method")
        if not isinstance(self.nucleic_acid_processing__library_generation_method, V1p4LibraryGenerationMethod):
            self.nucleic_acid_processing__library_generation_method = V1p4LibraryGenerationMethod(self.nucleic_acid_processing__library_generation_method)

        if self._is_empty(self.nucleic_acid_processing__library_generation_protocol):
            self.MissingRequiredField("nucleic_acid_processing__library_generation_protocol")
        if not isinstance(self.nucleic_acid_processing__library_generation_protocol, str):
            self.nucleic_acid_processing__library_generation_protocol = str(self.nucleic_acid_processing__library_generation_protocol)

        if self._is_empty(self.nucleic_acid_processing__library_generation_kit_version):
            self.MissingRequiredField("nucleic_acid_processing__library_generation_kit_version")
        if not isinstance(self.nucleic_acid_processing__library_generation_kit_version, str):
            self.nucleic_acid_processing__library_generation_kit_version = str(self.nucleic_acid_processing__library_generation_kit_version)

        if self._is_empty(self.nucleic_acid_processing__complete_sequences):
            self.MissingRequiredField("nucleic_acid_processing__complete_sequences")
        if not isinstance(self.nucleic_acid_processing__complete_sequences, V1p4CompleteSequences):
            self.nucleic_acid_processing__complete_sequences = V1p4CompleteSequences(self.nucleic_acid_processing__complete_sequences)

        if self._is_empty(self.nucleic_acid_processing__physical_linkage):
            self.MissingRequiredField("nucleic_acid_processing__physical_linkage")
        if not isinstance(self.nucleic_acid_processing__physical_linkage, V1p4PhysicalLinkage):
            self.nucleic_acid_processing__physical_linkage = V1p4PhysicalLinkage(self.nucleic_acid_processing__physical_linkage)

        if self._is_empty(self.sequencing_run__sequencing_run_id):
            self.MissingRequiredField("sequencing_run__sequencing_run_id")
        if not isinstance(self.sequencing_run__sequencing_run_id, str):
            self.sequencing_run__sequencing_run_id = str(self.sequencing_run__sequencing_run_id)

        if self._is_empty(self.sequencing_run__total_reads_passing_qc_filter):
            self.MissingRequiredField("sequencing_run__total_reads_passing_qc_filter")
        if not isinstance(self.sequencing_run__total_reads_passing_qc_filter, int):
            self.sequencing_run__total_reads_passing_qc_filter = int(self.sequencing_run__total_reads_passing_qc_filter)

        if self._is_empty(self.sequencing_run__sequencing_platform):
            self.MissingRequiredField("sequencing_run__sequencing_platform")
        if not isinstance(self.sequencing_run__sequencing_platform, str):
            self.sequencing_run__sequencing_platform = str(self.sequencing_run__sequencing_platform)

        if self._is_empty(self.sequencing_run__sequencing_facility):
            self.MissingRequiredField("sequencing_run__sequencing_facility")
        if not isinstance(self.sequencing_run__sequencing_facility, str):
            self.sequencing_run__sequencing_facility = str(self.sequencing_run__sequencing_facility)

        if self._is_empty(self.sequencing_run__sequencing_run_date):
            self.MissingRequiredField("sequencing_run__sequencing_run_date")
        if not isinstance(self.sequencing_run__sequencing_run_date, str):
            self.sequencing_run__sequencing_run_date = str(self.sequencing_run__sequencing_run_date)

        if self._is_empty(self.sequencing_run__sequencing_kit):
            self.MissingRequiredField("sequencing_run__sequencing_kit")
        if not isinstance(self.sequencing_run__sequencing_kit, str):
            self.sequencing_run__sequencing_kit = str(self.sequencing_run__sequencing_kit)

        if self.sample_processing__sample_processing_id is not None and not isinstance(self.sample_processing__sample_processing_id, str):
            self.sample_processing__sample_processing_id = str(self.sample_processing__sample_processing_id)

        if self.cell_processing__cell_label is not None and not isinstance(self.cell_processing__cell_label, str):
            self.cell_processing__cell_label = str(self.cell_processing__cell_label)

        self._normalize_inlined_as_dict(slot_name="nucleic_acid_processing__pcr_target", slot_type=V1p4PCRTarget, key_name="p_c_r_target__pcr_target_locus", keyed=False)

        if self.sequencing_run__sequencing_files is not None and not isinstance(self.sequencing_run__sequencing_files, V1p4SequencingData):
            self.sequencing_run__sequencing_files = V1p4SequencingData(**as_dict(self.sequencing_run__sequencing_files))

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

slots.time_point__label = Slot(uri=AK_SCHEMA.time_point__label, name="time_point__label", curie=AK_SCHEMA.curie('time_point__label'),
                   model_uri=AK_SCHEMA.time_point__label, domain=None, range=Optional[str])

slots.time_point__value = Slot(uri=AK_SCHEMA.time_point__value, name="time_point__value", curie=AK_SCHEMA.curie('time_point__value'),
                   model_uri=AK_SCHEMA.time_point__value, domain=None, range=Optional[float])

slots.time_point__unit = Slot(uri=AK_SCHEMA.time_point__unit, name="time_point__unit", curie=AK_SCHEMA.curie('time_point__unit'),
                   model_uri=AK_SCHEMA.time_point__unit, domain=None, range=Optional[Union[str, "V1p4Unit"]])

slots.time_interval__min = Slot(uri=AK_SCHEMA.time_interval__min, name="time_interval__min", curie=AK_SCHEMA.curie('time_interval__min'),
                   model_uri=AK_SCHEMA.time_interval__min, domain=None, range=Optional[float])

slots.time_interval__max = Slot(uri=AK_SCHEMA.time_interval__max, name="time_interval__max", curie=AK_SCHEMA.curie('time_interval__max'),
                   model_uri=AK_SCHEMA.time_interval__max, domain=None, range=Optional[float])

slots.time_interval__unit = Slot(uri=AK_SCHEMA.time_interval__unit, name="time_interval__unit", curie=AK_SCHEMA.curie('time_interval__unit'),
                   model_uri=AK_SCHEMA.time_interval__unit, domain=None, range=Optional[Union[str, "V1p4Unit"]])

slots.physical_quantity__quantity = Slot(uri=AK_SCHEMA.physical_quantity__quantity, name="physical_quantity__quantity", curie=AK_SCHEMA.curie('physical_quantity__quantity'),
                   model_uri=AK_SCHEMA.physical_quantity__quantity, domain=None, range=Optional[float])

slots.physical_quantity__unit = Slot(uri=AK_SCHEMA.physical_quantity__unit, name="physical_quantity__unit", curie=AK_SCHEMA.curie('physical_quantity__unit'),
                   model_uri=AK_SCHEMA.physical_quantity__unit, domain=None, range=Optional[Union[str, "V1p4Unit"]])

slots.time_quantity__quantity = Slot(uri=AK_SCHEMA.time_quantity__quantity, name="time_quantity__quantity", curie=AK_SCHEMA.curie('time_quantity__quantity'),
                   model_uri=AK_SCHEMA.time_quantity__quantity, domain=None, range=Optional[float])

slots.time_quantity__unit = Slot(uri=AK_SCHEMA.time_quantity__unit, name="time_quantity__unit", curie=AK_SCHEMA.curie('time_quantity__unit'),
                   model_uri=AK_SCHEMA.time_quantity__unit, domain=None, range=Optional[Union[str, "V1p4Unit"]])

slots.contributor__contributor_id = Slot(uri=AK_SCHEMA.contributor__contributor_id, name="contributor__contributor_id", curie=AK_SCHEMA.curie('contributor__contributor_id'),
                   model_uri=AK_SCHEMA.contributor__contributor_id, domain=None, range=str)

slots.contributor__name = Slot(uri=AK_SCHEMA.contributor__name, name="contributor__name", curie=AK_SCHEMA.curie('contributor__name'),
                   model_uri=AK_SCHEMA.contributor__name, domain=None, range=str)

slots.contributor__orcid_id = Slot(uri=AK_SCHEMA.contributor__orcid_id, name="contributor__orcid_id", curie=AK_SCHEMA.curie('contributor__orcid_id'),
                   model_uri=AK_SCHEMA.contributor__orcid_id, domain=None, range=Optional[Union[str, "V1p4OrcidId"]])

slots.contributor__affiliation = Slot(uri=AK_SCHEMA.contributor__affiliation, name="contributor__affiliation", curie=AK_SCHEMA.curie('contributor__affiliation'),
                   model_uri=AK_SCHEMA.contributor__affiliation, domain=None, range=Optional[Union[str, "V1p4Affiliation"]])

slots.contributor__affiliation_department = Slot(uri=AK_SCHEMA.contributor__affiliation_department, name="contributor__affiliation_department", curie=AK_SCHEMA.curie('contributor__affiliation_department'),
                   model_uri=AK_SCHEMA.contributor__affiliation_department, domain=None, range=Optional[str])

slots.contributor__contributions = Slot(uri=AK_SCHEMA.contributor__contributions, name="contributor__contributions", curie=AK_SCHEMA.curie('contributor__contributions'),
                   model_uri=AK_SCHEMA.contributor__contributions, domain=None, range=Optional[Union[Union[dict, V1p4ContributorContribution], List[Union[dict, V1p4ContributorContribution]]]])

slots.contributor_contribution__role = Slot(uri=AK_SCHEMA.contributor_contribution__role, name="contributor_contribution__role", curie=AK_SCHEMA.curie('contributor_contribution__role'),
                   model_uri=AK_SCHEMA.contributor_contribution__role, domain=None, range=Union[str, "V1p4Role"])

slots.contributor_contribution__degree = Slot(uri=AK_SCHEMA.contributor_contribution__degree, name="contributor_contribution__degree", curie=AK_SCHEMA.curie('contributor_contribution__degree'),
                   model_uri=AK_SCHEMA.contributor_contribution__degree, domain=None, range=Optional[Union[str, "V1p4Degree"]])

slots.rearranged_sequence__sequence_id = Slot(uri=AK_SCHEMA.rearranged_sequence__sequence_id, name="rearranged_sequence__sequence_id", curie=AK_SCHEMA.curie('rearranged_sequence__sequence_id'),
                   model_uri=AK_SCHEMA.rearranged_sequence__sequence_id, domain=None, range=str)

slots.rearranged_sequence__sequence = Slot(uri=AK_SCHEMA.rearranged_sequence__sequence, name="rearranged_sequence__sequence", curie=AK_SCHEMA.curie('rearranged_sequence__sequence'),
                   model_uri=AK_SCHEMA.rearranged_sequence__sequence, domain=None, range=str)

slots.rearranged_sequence__derivation = Slot(uri=AK_SCHEMA.rearranged_sequence__derivation, name="rearranged_sequence__derivation", curie=AK_SCHEMA.curie('rearranged_sequence__derivation'),
                   model_uri=AK_SCHEMA.rearranged_sequence__derivation, domain=None, range=Union[str, "V1p4Derivation"])

slots.rearranged_sequence__observation_type = Slot(uri=AK_SCHEMA.rearranged_sequence__observation_type, name="rearranged_sequence__observation_type", curie=AK_SCHEMA.curie('rearranged_sequence__observation_type'),
                   model_uri=AK_SCHEMA.rearranged_sequence__observation_type, domain=None, range=Union[str, "V1p4ObservationType"])

slots.rearranged_sequence__curation = Slot(uri=AK_SCHEMA.rearranged_sequence__curation, name="rearranged_sequence__curation", curie=AK_SCHEMA.curie('rearranged_sequence__curation'),
                   model_uri=AK_SCHEMA.rearranged_sequence__curation, domain=None, range=Optional[str])

slots.rearranged_sequence__repository_name = Slot(uri=AK_SCHEMA.rearranged_sequence__repository_name, name="rearranged_sequence__repository_name", curie=AK_SCHEMA.curie('rearranged_sequence__repository_name'),
                   model_uri=AK_SCHEMA.rearranged_sequence__repository_name, domain=None, range=str)

slots.rearranged_sequence__repository_ref = Slot(uri=AK_SCHEMA.rearranged_sequence__repository_ref, name="rearranged_sequence__repository_ref", curie=AK_SCHEMA.curie('rearranged_sequence__repository_ref'),
                   model_uri=AK_SCHEMA.rearranged_sequence__repository_ref, domain=None, range=Optional[str])

slots.rearranged_sequence__deposited_version = Slot(uri=AK_SCHEMA.rearranged_sequence__deposited_version, name="rearranged_sequence__deposited_version", curie=AK_SCHEMA.curie('rearranged_sequence__deposited_version'),
                   model_uri=AK_SCHEMA.rearranged_sequence__deposited_version, domain=None, range=str)

slots.rearranged_sequence__sequence_start = Slot(uri=AK_SCHEMA.rearranged_sequence__sequence_start, name="rearranged_sequence__sequence_start", curie=AK_SCHEMA.curie('rearranged_sequence__sequence_start'),
                   model_uri=AK_SCHEMA.rearranged_sequence__sequence_start, domain=None, range=Optional[int])

slots.rearranged_sequence__sequence_end = Slot(uri=AK_SCHEMA.rearranged_sequence__sequence_end, name="rearranged_sequence__sequence_end", curie=AK_SCHEMA.curie('rearranged_sequence__sequence_end'),
                   model_uri=AK_SCHEMA.rearranged_sequence__sequence_end, domain=None, range=Optional[int])

slots.unrearranged_sequence__sequence_id = Slot(uri=AK_SCHEMA.unrearranged_sequence__sequence_id, name="unrearranged_sequence__sequence_id", curie=AK_SCHEMA.curie('unrearranged_sequence__sequence_id'),
                   model_uri=AK_SCHEMA.unrearranged_sequence__sequence_id, domain=None, range=str)

slots.unrearranged_sequence__sequence = Slot(uri=AK_SCHEMA.unrearranged_sequence__sequence, name="unrearranged_sequence__sequence", curie=AK_SCHEMA.curie('unrearranged_sequence__sequence'),
                   model_uri=AK_SCHEMA.unrearranged_sequence__sequence, domain=None, range=str)

slots.unrearranged_sequence__curation = Slot(uri=AK_SCHEMA.unrearranged_sequence__curation, name="unrearranged_sequence__curation", curie=AK_SCHEMA.curie('unrearranged_sequence__curation'),
                   model_uri=AK_SCHEMA.unrearranged_sequence__curation, domain=None, range=Optional[str])

slots.unrearranged_sequence__repository_name = Slot(uri=AK_SCHEMA.unrearranged_sequence__repository_name, name="unrearranged_sequence__repository_name", curie=AK_SCHEMA.curie('unrearranged_sequence__repository_name'),
                   model_uri=AK_SCHEMA.unrearranged_sequence__repository_name, domain=None, range=str)

slots.unrearranged_sequence__repository_ref = Slot(uri=AK_SCHEMA.unrearranged_sequence__repository_ref, name="unrearranged_sequence__repository_ref", curie=AK_SCHEMA.curie('unrearranged_sequence__repository_ref'),
                   model_uri=AK_SCHEMA.unrearranged_sequence__repository_ref, domain=None, range=Optional[str])

slots.unrearranged_sequence__patch_no = Slot(uri=AK_SCHEMA.unrearranged_sequence__patch_no, name="unrearranged_sequence__patch_no", curie=AK_SCHEMA.curie('unrearranged_sequence__patch_no'),
                   model_uri=AK_SCHEMA.unrearranged_sequence__patch_no, domain=None, range=Optional[str])

slots.unrearranged_sequence__gff_seqid = Slot(uri=AK_SCHEMA.unrearranged_sequence__gff_seqid, name="unrearranged_sequence__gff_seqid", curie=AK_SCHEMA.curie('unrearranged_sequence__gff_seqid'),
                   model_uri=AK_SCHEMA.unrearranged_sequence__gff_seqid, domain=None, range=str)

slots.unrearranged_sequence__gff_start = Slot(uri=AK_SCHEMA.unrearranged_sequence__gff_start, name="unrearranged_sequence__gff_start", curie=AK_SCHEMA.curie('unrearranged_sequence__gff_start'),
                   model_uri=AK_SCHEMA.unrearranged_sequence__gff_start, domain=None, range=int)

slots.unrearranged_sequence__gff_end = Slot(uri=AK_SCHEMA.unrearranged_sequence__gff_end, name="unrearranged_sequence__gff_end", curie=AK_SCHEMA.curie('unrearranged_sequence__gff_end'),
                   model_uri=AK_SCHEMA.unrearranged_sequence__gff_end, domain=None, range=int)

slots.unrearranged_sequence__strand = Slot(uri=AK_SCHEMA.unrearranged_sequence__strand, name="unrearranged_sequence__strand", curie=AK_SCHEMA.curie('unrearranged_sequence__strand'),
                   model_uri=AK_SCHEMA.unrearranged_sequence__strand, domain=None, range=Union[str, "V1p4Strand"])

slots.sequence_delineation_v__sequence_delineation_id = Slot(uri=AK_SCHEMA.sequence_delineation_v__sequence_delineation_id, name="sequence_delineation_v__sequence_delineation_id", curie=AK_SCHEMA.curie('sequence_delineation_v__sequence_delineation_id'),
                   model_uri=AK_SCHEMA.sequence_delineation_v__sequence_delineation_id, domain=None, range=str)

slots.sequence_delineation_v__delineation_scheme = Slot(uri=AK_SCHEMA.sequence_delineation_v__delineation_scheme, name="sequence_delineation_v__delineation_scheme", curie=AK_SCHEMA.curie('sequence_delineation_v__delineation_scheme'),
                   model_uri=AK_SCHEMA.sequence_delineation_v__delineation_scheme, domain=None, range=str)

slots.sequence_delineation_v__unaligned_sequence = Slot(uri=AK_SCHEMA.sequence_delineation_v__unaligned_sequence, name="sequence_delineation_v__unaligned_sequence", curie=AK_SCHEMA.curie('sequence_delineation_v__unaligned_sequence'),
                   model_uri=AK_SCHEMA.sequence_delineation_v__unaligned_sequence, domain=None, range=Optional[str])

slots.sequence_delineation_v__aligned_sequence = Slot(uri=AK_SCHEMA.sequence_delineation_v__aligned_sequence, name="sequence_delineation_v__aligned_sequence", curie=AK_SCHEMA.curie('sequence_delineation_v__aligned_sequence'),
                   model_uri=AK_SCHEMA.sequence_delineation_v__aligned_sequence, domain=None, range=Optional[str])

slots.sequence_delineation_v__fwr1_start = Slot(uri=AK_SCHEMA.sequence_delineation_v__fwr1_start, name="sequence_delineation_v__fwr1_start", curie=AK_SCHEMA.curie('sequence_delineation_v__fwr1_start'),
                   model_uri=AK_SCHEMA.sequence_delineation_v__fwr1_start, domain=None, range=int)

slots.sequence_delineation_v__fwr1_end = Slot(uri=AK_SCHEMA.sequence_delineation_v__fwr1_end, name="sequence_delineation_v__fwr1_end", curie=AK_SCHEMA.curie('sequence_delineation_v__fwr1_end'),
                   model_uri=AK_SCHEMA.sequence_delineation_v__fwr1_end, domain=None, range=int)

slots.sequence_delineation_v__cdr1_start = Slot(uri=AK_SCHEMA.sequence_delineation_v__cdr1_start, name="sequence_delineation_v__cdr1_start", curie=AK_SCHEMA.curie('sequence_delineation_v__cdr1_start'),
                   model_uri=AK_SCHEMA.sequence_delineation_v__cdr1_start, domain=None, range=int)

slots.sequence_delineation_v__cdr1_end = Slot(uri=AK_SCHEMA.sequence_delineation_v__cdr1_end, name="sequence_delineation_v__cdr1_end", curie=AK_SCHEMA.curie('sequence_delineation_v__cdr1_end'),
                   model_uri=AK_SCHEMA.sequence_delineation_v__cdr1_end, domain=None, range=int)

slots.sequence_delineation_v__fwr2_start = Slot(uri=AK_SCHEMA.sequence_delineation_v__fwr2_start, name="sequence_delineation_v__fwr2_start", curie=AK_SCHEMA.curie('sequence_delineation_v__fwr2_start'),
                   model_uri=AK_SCHEMA.sequence_delineation_v__fwr2_start, domain=None, range=int)

slots.sequence_delineation_v__fwr2_end = Slot(uri=AK_SCHEMA.sequence_delineation_v__fwr2_end, name="sequence_delineation_v__fwr2_end", curie=AK_SCHEMA.curie('sequence_delineation_v__fwr2_end'),
                   model_uri=AK_SCHEMA.sequence_delineation_v__fwr2_end, domain=None, range=int)

slots.sequence_delineation_v__cdr2_start = Slot(uri=AK_SCHEMA.sequence_delineation_v__cdr2_start, name="sequence_delineation_v__cdr2_start", curie=AK_SCHEMA.curie('sequence_delineation_v__cdr2_start'),
                   model_uri=AK_SCHEMA.sequence_delineation_v__cdr2_start, domain=None, range=int)

slots.sequence_delineation_v__cdr2_end = Slot(uri=AK_SCHEMA.sequence_delineation_v__cdr2_end, name="sequence_delineation_v__cdr2_end", curie=AK_SCHEMA.curie('sequence_delineation_v__cdr2_end'),
                   model_uri=AK_SCHEMA.sequence_delineation_v__cdr2_end, domain=None, range=int)

slots.sequence_delineation_v__fwr3_start = Slot(uri=AK_SCHEMA.sequence_delineation_v__fwr3_start, name="sequence_delineation_v__fwr3_start", curie=AK_SCHEMA.curie('sequence_delineation_v__fwr3_start'),
                   model_uri=AK_SCHEMA.sequence_delineation_v__fwr3_start, domain=None, range=int)

slots.sequence_delineation_v__fwr3_end = Slot(uri=AK_SCHEMA.sequence_delineation_v__fwr3_end, name="sequence_delineation_v__fwr3_end", curie=AK_SCHEMA.curie('sequence_delineation_v__fwr3_end'),
                   model_uri=AK_SCHEMA.sequence_delineation_v__fwr3_end, domain=None, range=int)

slots.sequence_delineation_v__cdr3_start = Slot(uri=AK_SCHEMA.sequence_delineation_v__cdr3_start, name="sequence_delineation_v__cdr3_start", curie=AK_SCHEMA.curie('sequence_delineation_v__cdr3_start'),
                   model_uri=AK_SCHEMA.sequence_delineation_v__cdr3_start, domain=None, range=int)

slots.sequence_delineation_v__alignment_labels = Slot(uri=AK_SCHEMA.sequence_delineation_v__alignment_labels, name="sequence_delineation_v__alignment_labels", curie=AK_SCHEMA.curie('sequence_delineation_v__alignment_labels'),
                   model_uri=AK_SCHEMA.sequence_delineation_v__alignment_labels, domain=None, range=Optional[Union[str, List[str]]])

slots.allele_description__allele_description_id = Slot(uri=AK_SCHEMA.allele_description__allele_description_id, name="allele_description__allele_description_id", curie=AK_SCHEMA.curie('allele_description__allele_description_id'),
                   model_uri=AK_SCHEMA.allele_description__allele_description_id, domain=None, range=str)

slots.allele_description__allele_description_ref = Slot(uri=AK_SCHEMA.allele_description__allele_description_ref, name="allele_description__allele_description_ref", curie=AK_SCHEMA.curie('allele_description__allele_description_ref'),
                   model_uri=AK_SCHEMA.allele_description__allele_description_ref, domain=None, range=Optional[str])

slots.allele_description__acknowledgements = Slot(uri=AK_SCHEMA.allele_description__acknowledgements, name="allele_description__acknowledgements", curie=AK_SCHEMA.curie('allele_description__acknowledgements'),
                   model_uri=AK_SCHEMA.allele_description__acknowledgements, domain=None, range=Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]])

slots.allele_description__release_version = Slot(uri=AK_SCHEMA.allele_description__release_version, name="allele_description__release_version", curie=AK_SCHEMA.curie('allele_description__release_version'),
                   model_uri=AK_SCHEMA.allele_description__release_version, domain=None, range=int)

slots.allele_description__release_date = Slot(uri=AK_SCHEMA.allele_description__release_date, name="allele_description__release_date", curie=AK_SCHEMA.curie('allele_description__release_date'),
                   model_uri=AK_SCHEMA.allele_description__release_date, domain=None, range=str)

slots.allele_description__release_description = Slot(uri=AK_SCHEMA.allele_description__release_description, name="allele_description__release_description", curie=AK_SCHEMA.curie('allele_description__release_description'),
                   model_uri=AK_SCHEMA.allele_description__release_description, domain=None, range=str)

slots.allele_description__label = Slot(uri=AK_SCHEMA.allele_description__label, name="allele_description__label", curie=AK_SCHEMA.curie('allele_description__label'),
                   model_uri=AK_SCHEMA.allele_description__label, domain=None, range=Optional[str])

slots.allele_description__sequence = Slot(uri=AK_SCHEMA.allele_description__sequence, name="allele_description__sequence", curie=AK_SCHEMA.curie('allele_description__sequence'),
                   model_uri=AK_SCHEMA.allele_description__sequence, domain=None, range=str)

slots.allele_description__coding_sequence = Slot(uri=AK_SCHEMA.allele_description__coding_sequence, name="allele_description__coding_sequence", curie=AK_SCHEMA.curie('allele_description__coding_sequence'),
                   model_uri=AK_SCHEMA.allele_description__coding_sequence, domain=None, range=str)

slots.allele_description__aliases = Slot(uri=AK_SCHEMA.allele_description__aliases, name="allele_description__aliases", curie=AK_SCHEMA.curie('allele_description__aliases'),
                   model_uri=AK_SCHEMA.allele_description__aliases, domain=None, range=Optional[Union[str, List[str]]])

slots.allele_description__locus = Slot(uri=AK_SCHEMA.allele_description__locus, name="allele_description__locus", curie=AK_SCHEMA.curie('allele_description__locus'),
                   model_uri=AK_SCHEMA.allele_description__locus, domain=None, range=Union[str, "V1p4Locus"])

slots.allele_description__chromosome = Slot(uri=AK_SCHEMA.allele_description__chromosome, name="allele_description__chromosome", curie=AK_SCHEMA.curie('allele_description__chromosome'),
                   model_uri=AK_SCHEMA.allele_description__chromosome, domain=None, range=Optional[int])

slots.allele_description__sequence_type = Slot(uri=AK_SCHEMA.allele_description__sequence_type, name="allele_description__sequence_type", curie=AK_SCHEMA.curie('allele_description__sequence_type'),
                   model_uri=AK_SCHEMA.allele_description__sequence_type, domain=None, range=Union[str, "V1p4SequenceType"])

slots.allele_description__functional = Slot(uri=AK_SCHEMA.allele_description__functional, name="allele_description__functional", curie=AK_SCHEMA.curie('allele_description__functional'),
                   model_uri=AK_SCHEMA.allele_description__functional, domain=None, range=Union[bool, Bool])

slots.allele_description__inference_type = Slot(uri=AK_SCHEMA.allele_description__inference_type, name="allele_description__inference_type", curie=AK_SCHEMA.curie('allele_description__inference_type'),
                   model_uri=AK_SCHEMA.allele_description__inference_type, domain=None, range=Union[str, "V1p4InferenceType"])

slots.allele_description__species = Slot(uri=AK_SCHEMA.allele_description__species, name="allele_description__species", curie=AK_SCHEMA.curie('allele_description__species'),
                   model_uri=AK_SCHEMA.allele_description__species, domain=None, range=Union[str, "V1p4Species"])

slots.allele_description__species_subgroup = Slot(uri=AK_SCHEMA.allele_description__species_subgroup, name="allele_description__species_subgroup", curie=AK_SCHEMA.curie('allele_description__species_subgroup'),
                   model_uri=AK_SCHEMA.allele_description__species_subgroup, domain=None, range=Optional[str])

slots.allele_description__species_subgroup_type = Slot(uri=AK_SCHEMA.allele_description__species_subgroup_type, name="allele_description__species_subgroup_type", curie=AK_SCHEMA.curie('allele_description__species_subgroup_type'),
                   model_uri=AK_SCHEMA.allele_description__species_subgroup_type, domain=None, range=Optional[Union[str, "V1p4SpeciesSubgroupType"]])

slots.allele_description__status = Slot(uri=AK_SCHEMA.allele_description__status, name="allele_description__status", curie=AK_SCHEMA.curie('allele_description__status'),
                   model_uri=AK_SCHEMA.allele_description__status, domain=None, range=Optional[Union[str, "V1p4Status"]])

slots.allele_description__subgroup_designation = Slot(uri=AK_SCHEMA.allele_description__subgroup_designation, name="allele_description__subgroup_designation", curie=AK_SCHEMA.curie('allele_description__subgroup_designation'),
                   model_uri=AK_SCHEMA.allele_description__subgroup_designation, domain=None, range=Optional[str])

slots.allele_description__gene_designation = Slot(uri=AK_SCHEMA.allele_description__gene_designation, name="allele_description__gene_designation", curie=AK_SCHEMA.curie('allele_description__gene_designation'),
                   model_uri=AK_SCHEMA.allele_description__gene_designation, domain=None, range=Optional[str])

slots.allele_description__allele_designation = Slot(uri=AK_SCHEMA.allele_description__allele_designation, name="allele_description__allele_designation", curie=AK_SCHEMA.curie('allele_description__allele_designation'),
                   model_uri=AK_SCHEMA.allele_description__allele_designation, domain=None, range=Optional[str])

slots.allele_description__allele_similarity_cluster_designation = Slot(uri=AK_SCHEMA.allele_description__allele_similarity_cluster_designation, name="allele_description__allele_similarity_cluster_designation", curie=AK_SCHEMA.curie('allele_description__allele_similarity_cluster_designation'),
                   model_uri=AK_SCHEMA.allele_description__allele_similarity_cluster_designation, domain=None, range=Optional[str])

slots.allele_description__allele_similarity_cluster_member_id = Slot(uri=AK_SCHEMA.allele_description__allele_similarity_cluster_member_id, name="allele_description__allele_similarity_cluster_member_id", curie=AK_SCHEMA.curie('allele_description__allele_similarity_cluster_member_id'),
                   model_uri=AK_SCHEMA.allele_description__allele_similarity_cluster_member_id, domain=None, range=Optional[str])

slots.allele_description__j_codon_frame = Slot(uri=AK_SCHEMA.allele_description__j_codon_frame, name="allele_description__j_codon_frame", curie=AK_SCHEMA.curie('allele_description__j_codon_frame'),
                   model_uri=AK_SCHEMA.allele_description__j_codon_frame, domain=None, range=Optional[Union[str, "V1p4JCodonFrame"]])

slots.allele_description__gene_start = Slot(uri=AK_SCHEMA.allele_description__gene_start, name="allele_description__gene_start", curie=AK_SCHEMA.curie('allele_description__gene_start'),
                   model_uri=AK_SCHEMA.allele_description__gene_start, domain=None, range=Optional[int])

slots.allele_description__gene_end = Slot(uri=AK_SCHEMA.allele_description__gene_end, name="allele_description__gene_end", curie=AK_SCHEMA.curie('allele_description__gene_end'),
                   model_uri=AK_SCHEMA.allele_description__gene_end, domain=None, range=Optional[int])

slots.allele_description__utr_5_prime_start = Slot(uri=AK_SCHEMA.allele_description__utr_5_prime_start, name="allele_description__utr_5_prime_start", curie=AK_SCHEMA.curie('allele_description__utr_5_prime_start'),
                   model_uri=AK_SCHEMA.allele_description__utr_5_prime_start, domain=None, range=Optional[int])

slots.allele_description__utr_5_prime_end = Slot(uri=AK_SCHEMA.allele_description__utr_5_prime_end, name="allele_description__utr_5_prime_end", curie=AK_SCHEMA.curie('allele_description__utr_5_prime_end'),
                   model_uri=AK_SCHEMA.allele_description__utr_5_prime_end, domain=None, range=Optional[int])

slots.allele_description__leader_1_start = Slot(uri=AK_SCHEMA.allele_description__leader_1_start, name="allele_description__leader_1_start", curie=AK_SCHEMA.curie('allele_description__leader_1_start'),
                   model_uri=AK_SCHEMA.allele_description__leader_1_start, domain=None, range=Optional[int])

slots.allele_description__leader_1_end = Slot(uri=AK_SCHEMA.allele_description__leader_1_end, name="allele_description__leader_1_end", curie=AK_SCHEMA.curie('allele_description__leader_1_end'),
                   model_uri=AK_SCHEMA.allele_description__leader_1_end, domain=None, range=Optional[int])

slots.allele_description__leader_2_start = Slot(uri=AK_SCHEMA.allele_description__leader_2_start, name="allele_description__leader_2_start", curie=AK_SCHEMA.curie('allele_description__leader_2_start'),
                   model_uri=AK_SCHEMA.allele_description__leader_2_start, domain=None, range=Optional[int])

slots.allele_description__leader_2_end = Slot(uri=AK_SCHEMA.allele_description__leader_2_end, name="allele_description__leader_2_end", curie=AK_SCHEMA.curie('allele_description__leader_2_end'),
                   model_uri=AK_SCHEMA.allele_description__leader_2_end, domain=None, range=Optional[int])

slots.allele_description__v_rs_start = Slot(uri=AK_SCHEMA.allele_description__v_rs_start, name="allele_description__v_rs_start", curie=AK_SCHEMA.curie('allele_description__v_rs_start'),
                   model_uri=AK_SCHEMA.allele_description__v_rs_start, domain=None, range=Optional[int])

slots.allele_description__v_rs_end = Slot(uri=AK_SCHEMA.allele_description__v_rs_end, name="allele_description__v_rs_end", curie=AK_SCHEMA.curie('allele_description__v_rs_end'),
                   model_uri=AK_SCHEMA.allele_description__v_rs_end, domain=None, range=Optional[int])

slots.allele_description__d_rs_3_prime_start = Slot(uri=AK_SCHEMA.allele_description__d_rs_3_prime_start, name="allele_description__d_rs_3_prime_start", curie=AK_SCHEMA.curie('allele_description__d_rs_3_prime_start'),
                   model_uri=AK_SCHEMA.allele_description__d_rs_3_prime_start, domain=None, range=Optional[int])

slots.allele_description__d_rs_3_prime_end = Slot(uri=AK_SCHEMA.allele_description__d_rs_3_prime_end, name="allele_description__d_rs_3_prime_end", curie=AK_SCHEMA.curie('allele_description__d_rs_3_prime_end'),
                   model_uri=AK_SCHEMA.allele_description__d_rs_3_prime_end, domain=None, range=Optional[int])

slots.allele_description__d_rs_5_prime_start = Slot(uri=AK_SCHEMA.allele_description__d_rs_5_prime_start, name="allele_description__d_rs_5_prime_start", curie=AK_SCHEMA.curie('allele_description__d_rs_5_prime_start'),
                   model_uri=AK_SCHEMA.allele_description__d_rs_5_prime_start, domain=None, range=Optional[int])

slots.allele_description__d_rs_5_prime_end = Slot(uri=AK_SCHEMA.allele_description__d_rs_5_prime_end, name="allele_description__d_rs_5_prime_end", curie=AK_SCHEMA.curie('allele_description__d_rs_5_prime_end'),
                   model_uri=AK_SCHEMA.allele_description__d_rs_5_prime_end, domain=None, range=Optional[int])

slots.allele_description__j_cdr3_end = Slot(uri=AK_SCHEMA.allele_description__j_cdr3_end, name="allele_description__j_cdr3_end", curie=AK_SCHEMA.curie('allele_description__j_cdr3_end'),
                   model_uri=AK_SCHEMA.allele_description__j_cdr3_end, domain=None, range=Optional[int])

slots.allele_description__j_rs_start = Slot(uri=AK_SCHEMA.allele_description__j_rs_start, name="allele_description__j_rs_start", curie=AK_SCHEMA.curie('allele_description__j_rs_start'),
                   model_uri=AK_SCHEMA.allele_description__j_rs_start, domain=None, range=Optional[int])

slots.allele_description__j_rs_end = Slot(uri=AK_SCHEMA.allele_description__j_rs_end, name="allele_description__j_rs_end", curie=AK_SCHEMA.curie('allele_description__j_rs_end'),
                   model_uri=AK_SCHEMA.allele_description__j_rs_end, domain=None, range=Optional[int])

slots.allele_description__j_donor_splice = Slot(uri=AK_SCHEMA.allele_description__j_donor_splice, name="allele_description__j_donor_splice", curie=AK_SCHEMA.curie('allele_description__j_donor_splice'),
                   model_uri=AK_SCHEMA.allele_description__j_donor_splice, domain=None, range=Optional[int])

slots.allele_description__v_gene_delineations = Slot(uri=AK_SCHEMA.allele_description__v_gene_delineations, name="allele_description__v_gene_delineations", curie=AK_SCHEMA.curie('allele_description__v_gene_delineations'),
                   model_uri=AK_SCHEMA.allele_description__v_gene_delineations, domain=None, range=Optional[Union[Union[dict, V1p4SequenceDelineationV], List[Union[dict, V1p4SequenceDelineationV]]]])

slots.allele_description__unrearranged_support = Slot(uri=AK_SCHEMA.allele_description__unrearranged_support, name="allele_description__unrearranged_support", curie=AK_SCHEMA.curie('allele_description__unrearranged_support'),
                   model_uri=AK_SCHEMA.allele_description__unrearranged_support, domain=None, range=Optional[Union[Union[dict, V1p4UnrearrangedSequence], List[Union[dict, V1p4UnrearrangedSequence]]]])

slots.allele_description__rearranged_support = Slot(uri=AK_SCHEMA.allele_description__rearranged_support, name="allele_description__rearranged_support", curie=AK_SCHEMA.curie('allele_description__rearranged_support'),
                   model_uri=AK_SCHEMA.allele_description__rearranged_support, domain=None, range=Optional[Union[Union[dict, V1p4RearrangedSequence], List[Union[dict, V1p4RearrangedSequence]]]])

slots.allele_description__paralogs = Slot(uri=AK_SCHEMA.allele_description__paralogs, name="allele_description__paralogs", curie=AK_SCHEMA.curie('allele_description__paralogs'),
                   model_uri=AK_SCHEMA.allele_description__paralogs, domain=None, range=Optional[Union[str, List[str]]])

slots.allele_description__curation = Slot(uri=AK_SCHEMA.allele_description__curation, name="allele_description__curation", curie=AK_SCHEMA.curie('allele_description__curation'),
                   model_uri=AK_SCHEMA.allele_description__curation, domain=None, range=Optional[str])

slots.allele_description__curational_tags = Slot(uri=AK_SCHEMA.allele_description__curational_tags, name="allele_description__curational_tags", curie=AK_SCHEMA.curie('allele_description__curational_tags'),
                   model_uri=AK_SCHEMA.allele_description__curational_tags, domain=None, range=Optional[Union[Union[str, "V1p4CurationalTags"], List[Union[str, "V1p4CurationalTags"]]]])

slots.germline_set__germline_set_id = Slot(uri=AK_SCHEMA.germline_set__germline_set_id, name="germline_set__germline_set_id", curie=AK_SCHEMA.curie('germline_set__germline_set_id'),
                   model_uri=AK_SCHEMA.germline_set__germline_set_id, domain=None, range=str)

slots.germline_set__acknowledgements = Slot(uri=AK_SCHEMA.germline_set__acknowledgements, name="germline_set__acknowledgements", curie=AK_SCHEMA.curie('germline_set__acknowledgements'),
                   model_uri=AK_SCHEMA.germline_set__acknowledgements, domain=None, range=Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]])

slots.germline_set__release_version = Slot(uri=AK_SCHEMA.germline_set__release_version, name="germline_set__release_version", curie=AK_SCHEMA.curie('germline_set__release_version'),
                   model_uri=AK_SCHEMA.germline_set__release_version, domain=None, range=float)

slots.germline_set__release_description = Slot(uri=AK_SCHEMA.germline_set__release_description, name="germline_set__release_description", curie=AK_SCHEMA.curie('germline_set__release_description'),
                   model_uri=AK_SCHEMA.germline_set__release_description, domain=None, range=str)

slots.germline_set__release_date = Slot(uri=AK_SCHEMA.germline_set__release_date, name="germline_set__release_date", curie=AK_SCHEMA.curie('germline_set__release_date'),
                   model_uri=AK_SCHEMA.germline_set__release_date, domain=None, range=str)

slots.germline_set__germline_set_name = Slot(uri=AK_SCHEMA.germline_set__germline_set_name, name="germline_set__germline_set_name", curie=AK_SCHEMA.curie('germline_set__germline_set_name'),
                   model_uri=AK_SCHEMA.germline_set__germline_set_name, domain=None, range=str)

slots.germline_set__germline_set_ref = Slot(uri=AK_SCHEMA.germline_set__germline_set_ref, name="germline_set__germline_set_ref", curie=AK_SCHEMA.curie('germline_set__germline_set_ref'),
                   model_uri=AK_SCHEMA.germline_set__germline_set_ref, domain=None, range=str)

slots.germline_set__pub_ids = Slot(uri=AK_SCHEMA.germline_set__pub_ids, name="germline_set__pub_ids", curie=AK_SCHEMA.curie('germline_set__pub_ids'),
                   model_uri=AK_SCHEMA.germline_set__pub_ids, domain=None, range=Optional[Union[str, List[str]]])

slots.germline_set__species = Slot(uri=AK_SCHEMA.germline_set__species, name="germline_set__species", curie=AK_SCHEMA.curie('germline_set__species'),
                   model_uri=AK_SCHEMA.germline_set__species, domain=None, range=Union[str, "V1p4Species"])

slots.germline_set__species_subgroup = Slot(uri=AK_SCHEMA.germline_set__species_subgroup, name="germline_set__species_subgroup", curie=AK_SCHEMA.curie('germline_set__species_subgroup'),
                   model_uri=AK_SCHEMA.germline_set__species_subgroup, domain=None, range=Optional[str])

slots.germline_set__species_subgroup_type = Slot(uri=AK_SCHEMA.germline_set__species_subgroup_type, name="germline_set__species_subgroup_type", curie=AK_SCHEMA.curie('germline_set__species_subgroup_type'),
                   model_uri=AK_SCHEMA.germline_set__species_subgroup_type, domain=None, range=Optional[Union[str, "V1p4SpeciesSubgroupType"]])

slots.germline_set__locus = Slot(uri=AK_SCHEMA.germline_set__locus, name="germline_set__locus", curie=AK_SCHEMA.curie('germline_set__locus'),
                   model_uri=AK_SCHEMA.germline_set__locus, domain=None, range=Union[str, "V1p4Locus"])

slots.germline_set__allele_descriptions = Slot(uri=AK_SCHEMA.germline_set__allele_descriptions, name="germline_set__allele_descriptions", curie=AK_SCHEMA.curie('germline_set__allele_descriptions'),
                   model_uri=AK_SCHEMA.germline_set__allele_descriptions, domain=None, range=Union[Union[dict, V1p4AlleleDescription], List[Union[dict, V1p4AlleleDescription]]])

slots.germline_set__curation = Slot(uri=AK_SCHEMA.germline_set__curation, name="germline_set__curation", curie=AK_SCHEMA.curie('germline_set__curation'),
                   model_uri=AK_SCHEMA.germline_set__curation, domain=None, range=Optional[str])

slots.genotype_set__receptor_genotype_set_id = Slot(uri=AK_SCHEMA.genotype_set__receptor_genotype_set_id, name="genotype_set__receptor_genotype_set_id", curie=AK_SCHEMA.curie('genotype_set__receptor_genotype_set_id'),
                   model_uri=AK_SCHEMA.genotype_set__receptor_genotype_set_id, domain=None, range=str)

slots.genotype_set__genotype_class_list = Slot(uri=AK_SCHEMA.genotype_set__genotype_class_list, name="genotype_set__genotype_class_list", curie=AK_SCHEMA.curie('genotype_set__genotype_class_list'),
                   model_uri=AK_SCHEMA.genotype_set__genotype_class_list, domain=None, range=Optional[Union[Union[dict, V1p4Genotype], List[Union[dict, V1p4Genotype]]]])

slots.genotype__receptor_genotype_id = Slot(uri=AK_SCHEMA.genotype__receptor_genotype_id, name="genotype__receptor_genotype_id", curie=AK_SCHEMA.curie('genotype__receptor_genotype_id'),
                   model_uri=AK_SCHEMA.genotype__receptor_genotype_id, domain=None, range=str)

slots.genotype__locus = Slot(uri=AK_SCHEMA.genotype__locus, name="genotype__locus", curie=AK_SCHEMA.curie('genotype__locus'),
                   model_uri=AK_SCHEMA.genotype__locus, domain=None, range=Union[str, "V1p4Locus"])

slots.genotype__documented_alleles = Slot(uri=AK_SCHEMA.genotype__documented_alleles, name="genotype__documented_alleles", curie=AK_SCHEMA.curie('genotype__documented_alleles'),
                   model_uri=AK_SCHEMA.genotype__documented_alleles, domain=None, range=Optional[Union[Union[dict, V1p4DocumentedAllele], List[Union[dict, V1p4DocumentedAllele]]]])

slots.genotype__undocumented_alleles = Slot(uri=AK_SCHEMA.genotype__undocumented_alleles, name="genotype__undocumented_alleles", curie=AK_SCHEMA.curie('genotype__undocumented_alleles'),
                   model_uri=AK_SCHEMA.genotype__undocumented_alleles, domain=None, range=Optional[Union[Union[dict, V1p4UndocumentedAllele], List[Union[dict, V1p4UndocumentedAllele]]]])

slots.genotype__deleted_genes = Slot(uri=AK_SCHEMA.genotype__deleted_genes, name="genotype__deleted_genes", curie=AK_SCHEMA.curie('genotype__deleted_genes'),
                   model_uri=AK_SCHEMA.genotype__deleted_genes, domain=None, range=Optional[Union[Union[dict, V1p4DeletedGene], List[Union[dict, V1p4DeletedGene]]]])

slots.genotype__inference_process = Slot(uri=AK_SCHEMA.genotype__inference_process, name="genotype__inference_process", curie=AK_SCHEMA.curie('genotype__inference_process'),
                   model_uri=AK_SCHEMA.genotype__inference_process, domain=None, range=Optional[Union[str, "V1p4InferenceProcess"]])

slots.documented_allele__label = Slot(uri=AK_SCHEMA.documented_allele__label, name="documented_allele__label", curie=AK_SCHEMA.curie('documented_allele__label'),
                   model_uri=AK_SCHEMA.documented_allele__label, domain=None, range=str)

slots.documented_allele__germline_set_ref = Slot(uri=AK_SCHEMA.documented_allele__germline_set_ref, name="documented_allele__germline_set_ref", curie=AK_SCHEMA.curie('documented_allele__germline_set_ref'),
                   model_uri=AK_SCHEMA.documented_allele__germline_set_ref, domain=None, range=str)

slots.documented_allele__phasing = Slot(uri=AK_SCHEMA.documented_allele__phasing, name="documented_allele__phasing", curie=AK_SCHEMA.curie('documented_allele__phasing'),
                   model_uri=AK_SCHEMA.documented_allele__phasing, domain=None, range=Optional[int])

slots.undocumented_allele__allele_name = Slot(uri=AK_SCHEMA.undocumented_allele__allele_name, name="undocumented_allele__allele_name", curie=AK_SCHEMA.curie('undocumented_allele__allele_name'),
                   model_uri=AK_SCHEMA.undocumented_allele__allele_name, domain=None, range=str)

slots.undocumented_allele__sequence = Slot(uri=AK_SCHEMA.undocumented_allele__sequence, name="undocumented_allele__sequence", curie=AK_SCHEMA.curie('undocumented_allele__sequence'),
                   model_uri=AK_SCHEMA.undocumented_allele__sequence, domain=None, range=str)

slots.undocumented_allele__phasing = Slot(uri=AK_SCHEMA.undocumented_allele__phasing, name="undocumented_allele__phasing", curie=AK_SCHEMA.curie('undocumented_allele__phasing'),
                   model_uri=AK_SCHEMA.undocumented_allele__phasing, domain=None, range=Optional[int])

slots.deleted_gene__label = Slot(uri=AK_SCHEMA.deleted_gene__label, name="deleted_gene__label", curie=AK_SCHEMA.curie('deleted_gene__label'),
                   model_uri=AK_SCHEMA.deleted_gene__label, domain=None, range=str)

slots.deleted_gene__germline_set_ref = Slot(uri=AK_SCHEMA.deleted_gene__germline_set_ref, name="deleted_gene__germline_set_ref", curie=AK_SCHEMA.curie('deleted_gene__germline_set_ref'),
                   model_uri=AK_SCHEMA.deleted_gene__germline_set_ref, domain=None, range=str)

slots.deleted_gene__phasing = Slot(uri=AK_SCHEMA.deleted_gene__phasing, name="deleted_gene__phasing", curie=AK_SCHEMA.curie('deleted_gene__phasing'),
                   model_uri=AK_SCHEMA.deleted_gene__phasing, domain=None, range=Optional[int])

slots.m_h_c_genotype_set__mhc_genotype_set_id = Slot(uri=AK_SCHEMA.m_h_c_genotype_set__mhc_genotype_set_id, name="m_h_c_genotype_set__mhc_genotype_set_id", curie=AK_SCHEMA.curie('m_h_c_genotype_set__mhc_genotype_set_id'),
                   model_uri=AK_SCHEMA.m_h_c_genotype_set__mhc_genotype_set_id, domain=None, range=str)

slots.m_h_c_genotype_set__mhc_genotype_list = Slot(uri=AK_SCHEMA.m_h_c_genotype_set__mhc_genotype_list, name="m_h_c_genotype_set__mhc_genotype_list", curie=AK_SCHEMA.curie('m_h_c_genotype_set__mhc_genotype_list'),
                   model_uri=AK_SCHEMA.m_h_c_genotype_set__mhc_genotype_list, domain=None, range=Union[Union[dict, V1p4MHCGenotype], List[Union[dict, V1p4MHCGenotype]]])

slots.m_h_c_genotype__mhc_genotype_id = Slot(uri=AK_SCHEMA.m_h_c_genotype__mhc_genotype_id, name="m_h_c_genotype__mhc_genotype_id", curie=AK_SCHEMA.curie('m_h_c_genotype__mhc_genotype_id'),
                   model_uri=AK_SCHEMA.m_h_c_genotype__mhc_genotype_id, domain=None, range=str)

slots.m_h_c_genotype__mhc_class = Slot(uri=AK_SCHEMA.m_h_c_genotype__mhc_class, name="m_h_c_genotype__mhc_class", curie=AK_SCHEMA.curie('m_h_c_genotype__mhc_class'),
                   model_uri=AK_SCHEMA.m_h_c_genotype__mhc_class, domain=None, range=Union[str, "V1p4MhcClass"])

slots.m_h_c_genotype__mhc_alleles = Slot(uri=AK_SCHEMA.m_h_c_genotype__mhc_alleles, name="m_h_c_genotype__mhc_alleles", curie=AK_SCHEMA.curie('m_h_c_genotype__mhc_alleles'),
                   model_uri=AK_SCHEMA.m_h_c_genotype__mhc_alleles, domain=None, range=Union[Union[dict, V1p4MHCAllele], List[Union[dict, V1p4MHCAllele]]])

slots.m_h_c_genotype__mhc_genotyping_method = Slot(uri=AK_SCHEMA.m_h_c_genotype__mhc_genotyping_method, name="m_h_c_genotype__mhc_genotyping_method", curie=AK_SCHEMA.curie('m_h_c_genotype__mhc_genotyping_method'),
                   model_uri=AK_SCHEMA.m_h_c_genotype__mhc_genotyping_method, domain=None, range=Optional[str])

slots.m_h_c_allele__allele_designation = Slot(uri=AK_SCHEMA.m_h_c_allele__allele_designation, name="m_h_c_allele__allele_designation", curie=AK_SCHEMA.curie('m_h_c_allele__allele_designation'),
                   model_uri=AK_SCHEMA.m_h_c_allele__allele_designation, domain=None, range=Optional[str])

slots.m_h_c_allele__gene = Slot(uri=AK_SCHEMA.m_h_c_allele__gene, name="m_h_c_allele__gene", curie=AK_SCHEMA.curie('m_h_c_allele__gene'),
                   model_uri=AK_SCHEMA.m_h_c_allele__gene, domain=None, range=Optional[Union[str, "V1p4Gene"]])

slots.m_h_c_allele__reference_set_ref = Slot(uri=AK_SCHEMA.m_h_c_allele__reference_set_ref, name="m_h_c_allele__reference_set_ref", curie=AK_SCHEMA.curie('m_h_c_allele__reference_set_ref'),
                   model_uri=AK_SCHEMA.m_h_c_allele__reference_set_ref, domain=None, range=Optional[str])

slots.subject_genotype__receptor_genotype_set = Slot(uri=AK_SCHEMA.subject_genotype__receptor_genotype_set, name="subject_genotype__receptor_genotype_set", curie=AK_SCHEMA.curie('subject_genotype__receptor_genotype_set'),
                   model_uri=AK_SCHEMA.subject_genotype__receptor_genotype_set, domain=None, range=Optional[Union[dict, V1p4GenotypeSet]])

slots.subject_genotype__mhc_genotype_set = Slot(uri=AK_SCHEMA.subject_genotype__mhc_genotype_set, name="subject_genotype__mhc_genotype_set", curie=AK_SCHEMA.curie('subject_genotype__mhc_genotype_set'),
                   model_uri=AK_SCHEMA.subject_genotype__mhc_genotype_set, domain=None, range=Optional[Union[dict, V1p4MHCGenotypeSet]])

slots.study__study_id = Slot(uri=AK_SCHEMA.study__study_id, name="study__study_id", curie=AK_SCHEMA.curie('study__study_id'),
                   model_uri=AK_SCHEMA.study__study_id, domain=None, range=str)

slots.study__study_title = Slot(uri=AK_SCHEMA.study__study_title, name="study__study_title", curie=AK_SCHEMA.curie('study__study_title'),
                   model_uri=AK_SCHEMA.study__study_title, domain=None, range=str)

slots.study__study_type = Slot(uri=AK_SCHEMA.study__study_type, name="study__study_type", curie=AK_SCHEMA.curie('study__study_type'),
                   model_uri=AK_SCHEMA.study__study_type, domain=None, range=Union[str, "V1p4StudyType"])

slots.study__study_description = Slot(uri=AK_SCHEMA.study__study_description, name="study__study_description", curie=AK_SCHEMA.curie('study__study_description'),
                   model_uri=AK_SCHEMA.study__study_description, domain=None, range=Optional[str])

slots.study__inclusion_exclusion_criteria = Slot(uri=AK_SCHEMA.study__inclusion_exclusion_criteria, name="study__inclusion_exclusion_criteria", curie=AK_SCHEMA.curie('study__inclusion_exclusion_criteria'),
                   model_uri=AK_SCHEMA.study__inclusion_exclusion_criteria, domain=None, range=str)

slots.study__grants = Slot(uri=AK_SCHEMA.study__grants, name="study__grants", curie=AK_SCHEMA.curie('study__grants'),
                   model_uri=AK_SCHEMA.study__grants, domain=None, range=str)

slots.study__contributors = Slot(uri=AK_SCHEMA.study__contributors, name="study__contributors", curie=AK_SCHEMA.curie('study__contributors'),
                   model_uri=AK_SCHEMA.study__contributors, domain=None, range=Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]])

slots.study__pub_ids = Slot(uri=AK_SCHEMA.study__pub_ids, name="study__pub_ids", curie=AK_SCHEMA.curie('study__pub_ids'),
                   model_uri=AK_SCHEMA.study__pub_ids, domain=None, range=Union[str, List[str]])

slots.study__keywords_study = Slot(uri=AK_SCHEMA.study__keywords_study, name="study__keywords_study", curie=AK_SCHEMA.curie('study__keywords_study'),
                   model_uri=AK_SCHEMA.study__keywords_study, domain=None, range=Union[Union[str, "V1p4KeywordsStudy"], List[Union[str, "V1p4KeywordsStudy"]]])

slots.study__adc_publish_date = Slot(uri=AK_SCHEMA.study__adc_publish_date, name="study__adc_publish_date", curie=AK_SCHEMA.curie('study__adc_publish_date'),
                   model_uri=AK_SCHEMA.study__adc_publish_date, domain=None, range=Optional[str])

slots.study__adc_update_date = Slot(uri=AK_SCHEMA.study__adc_update_date, name="study__adc_update_date", curie=AK_SCHEMA.curie('study__adc_update_date'),
                   model_uri=AK_SCHEMA.study__adc_update_date, domain=None, range=Optional[str])

slots.subject__subject_id = Slot(uri=AK_SCHEMA.subject__subject_id, name="subject__subject_id", curie=AK_SCHEMA.curie('subject__subject_id'),
                   model_uri=AK_SCHEMA.subject__subject_id, domain=None, range=str)

slots.subject__synthetic = Slot(uri=AK_SCHEMA.subject__synthetic, name="subject__synthetic", curie=AK_SCHEMA.curie('subject__synthetic'),
                   model_uri=AK_SCHEMA.subject__synthetic, domain=None, range=Union[bool, Bool])

slots.subject__species = Slot(uri=AK_SCHEMA.subject__species, name="subject__species", curie=AK_SCHEMA.curie('subject__species'),
                   model_uri=AK_SCHEMA.subject__species, domain=None, range=Union[str, "V1p4Species"])

slots.subject__sex = Slot(uri=AK_SCHEMA.subject__sex, name="subject__sex", curie=AK_SCHEMA.curie('subject__sex'),
                   model_uri=AK_SCHEMA.subject__sex, domain=None, range=Union[str, "V1p4Sex"])

slots.subject__age = Slot(uri=AK_SCHEMA.subject__age, name="subject__age", curie=AK_SCHEMA.curie('subject__age'),
                   model_uri=AK_SCHEMA.subject__age, domain=None, range=Union[dict, V1p4TimeInterval])

slots.subject__age_event = Slot(uri=AK_SCHEMA.subject__age_event, name="subject__age_event", curie=AK_SCHEMA.curie('subject__age_event'),
                   model_uri=AK_SCHEMA.subject__age_event, domain=None, range=str)

slots.subject__ancestry_population = Slot(uri=AK_SCHEMA.subject__ancestry_population, name="subject__ancestry_population", curie=AK_SCHEMA.curie('subject__ancestry_population'),
                   model_uri=AK_SCHEMA.subject__ancestry_population, domain=None, range=Union[str, "V1p4AncestryPopulation"])

slots.subject__location_birth = Slot(uri=AK_SCHEMA.subject__location_birth, name="subject__location_birth", curie=AK_SCHEMA.curie('subject__location_birth'),
                   model_uri=AK_SCHEMA.subject__location_birth, domain=None, range=Optional[Union[str, "V1p4LocationBirth"]])

slots.subject__ethnicity = Slot(uri=AK_SCHEMA.subject__ethnicity, name="subject__ethnicity", curie=AK_SCHEMA.curie('subject__ethnicity'),
                   model_uri=AK_SCHEMA.subject__ethnicity, domain=None, range=str)

slots.subject__race = Slot(uri=AK_SCHEMA.subject__race, name="subject__race", curie=AK_SCHEMA.curie('subject__race'),
                   model_uri=AK_SCHEMA.subject__race, domain=None, range=str)

slots.subject__strain_name = Slot(uri=AK_SCHEMA.subject__strain_name, name="subject__strain_name", curie=AK_SCHEMA.curie('subject__strain_name'),
                   model_uri=AK_SCHEMA.subject__strain_name, domain=None, range=str)

slots.subject__linked_subjects = Slot(uri=AK_SCHEMA.subject__linked_subjects, name="subject__linked_subjects", curie=AK_SCHEMA.curie('subject__linked_subjects'),
                   model_uri=AK_SCHEMA.subject__linked_subjects, domain=None, range=str)

slots.subject__link_type = Slot(uri=AK_SCHEMA.subject__link_type, name="subject__link_type", curie=AK_SCHEMA.curie('subject__link_type'),
                   model_uri=AK_SCHEMA.subject__link_type, domain=None, range=str)

slots.subject__diagnosis = Slot(uri=AK_SCHEMA.subject__diagnosis, name="subject__diagnosis", curie=AK_SCHEMA.curie('subject__diagnosis'),
                   model_uri=AK_SCHEMA.subject__diagnosis, domain=None, range=Optional[Union[Union[dict, V1p4Diagnosis], List[Union[dict, V1p4Diagnosis]]]])

slots.subject__genotype = Slot(uri=AK_SCHEMA.subject__genotype, name="subject__genotype", curie=AK_SCHEMA.curie('subject__genotype'),
                   model_uri=AK_SCHEMA.subject__genotype, domain=None, range=Optional[Union[dict, V1p4SubjectGenotype]])

slots.diagnosis__study_group_description = Slot(uri=AK_SCHEMA.diagnosis__study_group_description, name="diagnosis__study_group_description", curie=AK_SCHEMA.curie('diagnosis__study_group_description'),
                   model_uri=AK_SCHEMA.diagnosis__study_group_description, domain=None, range=str)

slots.diagnosis__diagnosis_timepoint = Slot(uri=AK_SCHEMA.diagnosis__diagnosis_timepoint, name="diagnosis__diagnosis_timepoint", curie=AK_SCHEMA.curie('diagnosis__diagnosis_timepoint'),
                   model_uri=AK_SCHEMA.diagnosis__diagnosis_timepoint, domain=None, range=Optional[Union[dict, V1p4TimePoint]])

slots.diagnosis__disease_diagnosis = Slot(uri=AK_SCHEMA.diagnosis__disease_diagnosis, name="diagnosis__disease_diagnosis", curie=AK_SCHEMA.curie('diagnosis__disease_diagnosis'),
                   model_uri=AK_SCHEMA.diagnosis__disease_diagnosis, domain=None, range=Union[str, "V1p4DiseaseDiagnosis"])

slots.diagnosis__disease_length = Slot(uri=AK_SCHEMA.diagnosis__disease_length, name="diagnosis__disease_length", curie=AK_SCHEMA.curie('diagnosis__disease_length'),
                   model_uri=AK_SCHEMA.diagnosis__disease_length, domain=None, range=Union[dict, V1p4TimeQuantity])

slots.diagnosis__disease_stage = Slot(uri=AK_SCHEMA.diagnosis__disease_stage, name="diagnosis__disease_stage", curie=AK_SCHEMA.curie('diagnosis__disease_stage'),
                   model_uri=AK_SCHEMA.diagnosis__disease_stage, domain=None, range=str)

slots.diagnosis__prior_therapies = Slot(uri=AK_SCHEMA.diagnosis__prior_therapies, name="diagnosis__prior_therapies", curie=AK_SCHEMA.curie('diagnosis__prior_therapies'),
                   model_uri=AK_SCHEMA.diagnosis__prior_therapies, domain=None, range=str)

slots.diagnosis__immunogen = Slot(uri=AK_SCHEMA.diagnosis__immunogen, name="diagnosis__immunogen", curie=AK_SCHEMA.curie('diagnosis__immunogen'),
                   model_uri=AK_SCHEMA.diagnosis__immunogen, domain=None, range=str)

slots.diagnosis__intervention = Slot(uri=AK_SCHEMA.diagnosis__intervention, name="diagnosis__intervention", curie=AK_SCHEMA.curie('diagnosis__intervention'),
                   model_uri=AK_SCHEMA.diagnosis__intervention, domain=None, range=str)

slots.diagnosis__medical_history = Slot(uri=AK_SCHEMA.diagnosis__medical_history, name="diagnosis__medical_history", curie=AK_SCHEMA.curie('diagnosis__medical_history'),
                   model_uri=AK_SCHEMA.diagnosis__medical_history, domain=None, range=str)

slots.sample__sample_id = Slot(uri=AK_SCHEMA.sample__sample_id, name="sample__sample_id", curie=AK_SCHEMA.curie('sample__sample_id'),
                   model_uri=AK_SCHEMA.sample__sample_id, domain=None, range=str)

slots.sample__sample_type = Slot(uri=AK_SCHEMA.sample__sample_type, name="sample__sample_type", curie=AK_SCHEMA.curie('sample__sample_type'),
                   model_uri=AK_SCHEMA.sample__sample_type, domain=None, range=str)

slots.sample__tissue = Slot(uri=AK_SCHEMA.sample__tissue, name="sample__tissue", curie=AK_SCHEMA.curie('sample__tissue'),
                   model_uri=AK_SCHEMA.sample__tissue, domain=None, range=Union[str, "V1p4Tissue"])

slots.sample__anatomic_site = Slot(uri=AK_SCHEMA.sample__anatomic_site, name="sample__anatomic_site", curie=AK_SCHEMA.curie('sample__anatomic_site'),
                   model_uri=AK_SCHEMA.sample__anatomic_site, domain=None, range=str)

slots.sample__disease_state_sample = Slot(uri=AK_SCHEMA.sample__disease_state_sample, name="sample__disease_state_sample", curie=AK_SCHEMA.curie('sample__disease_state_sample'),
                   model_uri=AK_SCHEMA.sample__disease_state_sample, domain=None, range=str)

slots.sample__collection_time_point_relative = Slot(uri=AK_SCHEMA.sample__collection_time_point_relative, name="sample__collection_time_point_relative", curie=AK_SCHEMA.curie('sample__collection_time_point_relative'),
                   model_uri=AK_SCHEMA.sample__collection_time_point_relative, domain=None, range=Union[dict, V1p4TimePoint])

slots.sample__collection_location = Slot(uri=AK_SCHEMA.sample__collection_location, name="sample__collection_location", curie=AK_SCHEMA.curie('sample__collection_location'),
                   model_uri=AK_SCHEMA.sample__collection_location, domain=None, range=Optional[Union[str, "V1p4CollectionLocation"]])

slots.sample__biomaterial_provider = Slot(uri=AK_SCHEMA.sample__biomaterial_provider, name="sample__biomaterial_provider", curie=AK_SCHEMA.curie('sample__biomaterial_provider'),
                   model_uri=AK_SCHEMA.sample__biomaterial_provider, domain=None, range=str)

slots.cell_processing__tissue_processing = Slot(uri=AK_SCHEMA.cell_processing__tissue_processing, name="cell_processing__tissue_processing", curie=AK_SCHEMA.curie('cell_processing__tissue_processing'),
                   model_uri=AK_SCHEMA.cell_processing__tissue_processing, domain=None, range=str)

slots.cell_processing__cell_subset = Slot(uri=AK_SCHEMA.cell_processing__cell_subset, name="cell_processing__cell_subset", curie=AK_SCHEMA.curie('cell_processing__cell_subset'),
                   model_uri=AK_SCHEMA.cell_processing__cell_subset, domain=None, range=Union[str, "V1p4CellSubset"])

slots.cell_processing__cell_phenotype = Slot(uri=AK_SCHEMA.cell_processing__cell_phenotype, name="cell_processing__cell_phenotype", curie=AK_SCHEMA.curie('cell_processing__cell_phenotype'),
                   model_uri=AK_SCHEMA.cell_processing__cell_phenotype, domain=None, range=str)

slots.cell_processing__cell_label = Slot(uri=AK_SCHEMA.cell_processing__cell_label, name="cell_processing__cell_label", curie=AK_SCHEMA.curie('cell_processing__cell_label'),
                   model_uri=AK_SCHEMA.cell_processing__cell_label, domain=None, range=Optional[str])

slots.cell_processing__cell_species = Slot(uri=AK_SCHEMA.cell_processing__cell_species, name="cell_processing__cell_species", curie=AK_SCHEMA.curie('cell_processing__cell_species'),
                   model_uri=AK_SCHEMA.cell_processing__cell_species, domain=None, range=Optional[Union[str, "V1p4CellSpecies"]])

slots.cell_processing__single_cell = Slot(uri=AK_SCHEMA.cell_processing__single_cell, name="cell_processing__single_cell", curie=AK_SCHEMA.curie('cell_processing__single_cell'),
                   model_uri=AK_SCHEMA.cell_processing__single_cell, domain=None, range=Union[bool, Bool])

slots.cell_processing__cell_number = Slot(uri=AK_SCHEMA.cell_processing__cell_number, name="cell_processing__cell_number", curie=AK_SCHEMA.curie('cell_processing__cell_number'),
                   model_uri=AK_SCHEMA.cell_processing__cell_number, domain=None, range=int)

slots.cell_processing__cells_per_reaction = Slot(uri=AK_SCHEMA.cell_processing__cells_per_reaction, name="cell_processing__cells_per_reaction", curie=AK_SCHEMA.curie('cell_processing__cells_per_reaction'),
                   model_uri=AK_SCHEMA.cell_processing__cells_per_reaction, domain=None, range=int)

slots.cell_processing__cell_storage = Slot(uri=AK_SCHEMA.cell_processing__cell_storage, name="cell_processing__cell_storage", curie=AK_SCHEMA.curie('cell_processing__cell_storage'),
                   model_uri=AK_SCHEMA.cell_processing__cell_storage, domain=None, range=Union[bool, Bool])

slots.cell_processing__cell_quality = Slot(uri=AK_SCHEMA.cell_processing__cell_quality, name="cell_processing__cell_quality", curie=AK_SCHEMA.curie('cell_processing__cell_quality'),
                   model_uri=AK_SCHEMA.cell_processing__cell_quality, domain=None, range=str)

slots.cell_processing__cell_isolation = Slot(uri=AK_SCHEMA.cell_processing__cell_isolation, name="cell_processing__cell_isolation", curie=AK_SCHEMA.curie('cell_processing__cell_isolation'),
                   model_uri=AK_SCHEMA.cell_processing__cell_isolation, domain=None, range=str)

slots.cell_processing__cell_processing_protocol = Slot(uri=AK_SCHEMA.cell_processing__cell_processing_protocol, name="cell_processing__cell_processing_protocol", curie=AK_SCHEMA.curie('cell_processing__cell_processing_protocol'),
                   model_uri=AK_SCHEMA.cell_processing__cell_processing_protocol, domain=None, range=str)

slots.p_c_r_target__pcr_target_locus = Slot(uri=AK_SCHEMA.p_c_r_target__pcr_target_locus, name="p_c_r_target__pcr_target_locus", curie=AK_SCHEMA.curie('p_c_r_target__pcr_target_locus'),
                   model_uri=AK_SCHEMA.p_c_r_target__pcr_target_locus, domain=None, range=Union[str, "V1p4PcrTargetLocus"])

slots.p_c_r_target__forward_pcr_primer_target_location = Slot(uri=AK_SCHEMA.p_c_r_target__forward_pcr_primer_target_location, name="p_c_r_target__forward_pcr_primer_target_location", curie=AK_SCHEMA.curie('p_c_r_target__forward_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.p_c_r_target__forward_pcr_primer_target_location, domain=None, range=str)

slots.p_c_r_target__reverse_pcr_primer_target_location = Slot(uri=AK_SCHEMA.p_c_r_target__reverse_pcr_primer_target_location, name="p_c_r_target__reverse_pcr_primer_target_location", curie=AK_SCHEMA.curie('p_c_r_target__reverse_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.p_c_r_target__reverse_pcr_primer_target_location, domain=None, range=str)

slots.nucleic_acid_processing__template_class = Slot(uri=AK_SCHEMA.nucleic_acid_processing__template_class, name="nucleic_acid_processing__template_class", curie=AK_SCHEMA.curie('nucleic_acid_processing__template_class'),
                   model_uri=AK_SCHEMA.nucleic_acid_processing__template_class, domain=None, range=Union[str, "V1p4TemplateClass"])

slots.nucleic_acid_processing__template_quality = Slot(uri=AK_SCHEMA.nucleic_acid_processing__template_quality, name="nucleic_acid_processing__template_quality", curie=AK_SCHEMA.curie('nucleic_acid_processing__template_quality'),
                   model_uri=AK_SCHEMA.nucleic_acid_processing__template_quality, domain=None, range=str)

slots.nucleic_acid_processing__template_amount = Slot(uri=AK_SCHEMA.nucleic_acid_processing__template_amount, name="nucleic_acid_processing__template_amount", curie=AK_SCHEMA.curie('nucleic_acid_processing__template_amount'),
                   model_uri=AK_SCHEMA.nucleic_acid_processing__template_amount, domain=None, range=Union[dict, V1p4PhysicalQuantity])

slots.nucleic_acid_processing__library_generation_method = Slot(uri=AK_SCHEMA.nucleic_acid_processing__library_generation_method, name="nucleic_acid_processing__library_generation_method", curie=AK_SCHEMA.curie('nucleic_acid_processing__library_generation_method'),
                   model_uri=AK_SCHEMA.nucleic_acid_processing__library_generation_method, domain=None, range=Union[str, "V1p4LibraryGenerationMethod"])

slots.nucleic_acid_processing__library_generation_protocol = Slot(uri=AK_SCHEMA.nucleic_acid_processing__library_generation_protocol, name="nucleic_acid_processing__library_generation_protocol", curie=AK_SCHEMA.curie('nucleic_acid_processing__library_generation_protocol'),
                   model_uri=AK_SCHEMA.nucleic_acid_processing__library_generation_protocol, domain=None, range=str)

slots.nucleic_acid_processing__library_generation_kit_version = Slot(uri=AK_SCHEMA.nucleic_acid_processing__library_generation_kit_version, name="nucleic_acid_processing__library_generation_kit_version", curie=AK_SCHEMA.curie('nucleic_acid_processing__library_generation_kit_version'),
                   model_uri=AK_SCHEMA.nucleic_acid_processing__library_generation_kit_version, domain=None, range=str)

slots.nucleic_acid_processing__pcr_target = Slot(uri=AK_SCHEMA.nucleic_acid_processing__pcr_target, name="nucleic_acid_processing__pcr_target", curie=AK_SCHEMA.curie('nucleic_acid_processing__pcr_target'),
                   model_uri=AK_SCHEMA.nucleic_acid_processing__pcr_target, domain=None, range=Optional[Union[Union[dict, V1p4PCRTarget], List[Union[dict, V1p4PCRTarget]]]])

slots.nucleic_acid_processing__complete_sequences = Slot(uri=AK_SCHEMA.nucleic_acid_processing__complete_sequences, name="nucleic_acid_processing__complete_sequences", curie=AK_SCHEMA.curie('nucleic_acid_processing__complete_sequences'),
                   model_uri=AK_SCHEMA.nucleic_acid_processing__complete_sequences, domain=None, range=Union[str, "V1p4CompleteSequences"])

slots.nucleic_acid_processing__physical_linkage = Slot(uri=AK_SCHEMA.nucleic_acid_processing__physical_linkage, name="nucleic_acid_processing__physical_linkage", curie=AK_SCHEMA.curie('nucleic_acid_processing__physical_linkage'),
                   model_uri=AK_SCHEMA.nucleic_acid_processing__physical_linkage, domain=None, range=Union[str, "V1p4PhysicalLinkage"])

slots.sequencing_run__sequencing_run_id = Slot(uri=AK_SCHEMA.sequencing_run__sequencing_run_id, name="sequencing_run__sequencing_run_id", curie=AK_SCHEMA.curie('sequencing_run__sequencing_run_id'),
                   model_uri=AK_SCHEMA.sequencing_run__sequencing_run_id, domain=None, range=str)

slots.sequencing_run__total_reads_passing_qc_filter = Slot(uri=AK_SCHEMA.sequencing_run__total_reads_passing_qc_filter, name="sequencing_run__total_reads_passing_qc_filter", curie=AK_SCHEMA.curie('sequencing_run__total_reads_passing_qc_filter'),
                   model_uri=AK_SCHEMA.sequencing_run__total_reads_passing_qc_filter, domain=None, range=int)

slots.sequencing_run__sequencing_platform = Slot(uri=AK_SCHEMA.sequencing_run__sequencing_platform, name="sequencing_run__sequencing_platform", curie=AK_SCHEMA.curie('sequencing_run__sequencing_platform'),
                   model_uri=AK_SCHEMA.sequencing_run__sequencing_platform, domain=None, range=str)

slots.sequencing_run__sequencing_facility = Slot(uri=AK_SCHEMA.sequencing_run__sequencing_facility, name="sequencing_run__sequencing_facility", curie=AK_SCHEMA.curie('sequencing_run__sequencing_facility'),
                   model_uri=AK_SCHEMA.sequencing_run__sequencing_facility, domain=None, range=str)

slots.sequencing_run__sequencing_run_date = Slot(uri=AK_SCHEMA.sequencing_run__sequencing_run_date, name="sequencing_run__sequencing_run_date", curie=AK_SCHEMA.curie('sequencing_run__sequencing_run_date'),
                   model_uri=AK_SCHEMA.sequencing_run__sequencing_run_date, domain=None, range=str)

slots.sequencing_run__sequencing_kit = Slot(uri=AK_SCHEMA.sequencing_run__sequencing_kit, name="sequencing_run__sequencing_kit", curie=AK_SCHEMA.curie('sequencing_run__sequencing_kit'),
                   model_uri=AK_SCHEMA.sequencing_run__sequencing_kit, domain=None, range=str)

slots.sequencing_run__sequencing_files = Slot(uri=AK_SCHEMA.sequencing_run__sequencing_files, name="sequencing_run__sequencing_files", curie=AK_SCHEMA.curie('sequencing_run__sequencing_files'),
                   model_uri=AK_SCHEMA.sequencing_run__sequencing_files, domain=None, range=Optional[Union[dict, V1p4SequencingData]])

slots.sequencing_data__sequencing_data_id = Slot(uri=AK_SCHEMA.sequencing_data__sequencing_data_id, name="sequencing_data__sequencing_data_id", curie=AK_SCHEMA.curie('sequencing_data__sequencing_data_id'),
                   model_uri=AK_SCHEMA.sequencing_data__sequencing_data_id, domain=None, range=str)

slots.sequencing_data__file_type = Slot(uri=AK_SCHEMA.sequencing_data__file_type, name="sequencing_data__file_type", curie=AK_SCHEMA.curie('sequencing_data__file_type'),
                   model_uri=AK_SCHEMA.sequencing_data__file_type, domain=None, range=Union[str, "V1p4FileType"])

slots.sequencing_data__filename = Slot(uri=AK_SCHEMA.sequencing_data__filename, name="sequencing_data__filename", curie=AK_SCHEMA.curie('sequencing_data__filename'),
                   model_uri=AK_SCHEMA.sequencing_data__filename, domain=None, range=str)

slots.sequencing_data__read_direction = Slot(uri=AK_SCHEMA.sequencing_data__read_direction, name="sequencing_data__read_direction", curie=AK_SCHEMA.curie('sequencing_data__read_direction'),
                   model_uri=AK_SCHEMA.sequencing_data__read_direction, domain=None, range=Union[str, "V1p4ReadDirection"])

slots.sequencing_data__read_length = Slot(uri=AK_SCHEMA.sequencing_data__read_length, name="sequencing_data__read_length", curie=AK_SCHEMA.curie('sequencing_data__read_length'),
                   model_uri=AK_SCHEMA.sequencing_data__read_length, domain=None, range=int)

slots.sequencing_data__paired_filename = Slot(uri=AK_SCHEMA.sequencing_data__paired_filename, name="sequencing_data__paired_filename", curie=AK_SCHEMA.curie('sequencing_data__paired_filename'),
                   model_uri=AK_SCHEMA.sequencing_data__paired_filename, domain=None, range=str)

slots.sequencing_data__paired_read_direction = Slot(uri=AK_SCHEMA.sequencing_data__paired_read_direction, name="sequencing_data__paired_read_direction", curie=AK_SCHEMA.curie('sequencing_data__paired_read_direction'),
                   model_uri=AK_SCHEMA.sequencing_data__paired_read_direction, domain=None, range=Union[str, "V1p4PairedReadDirection"])

slots.sequencing_data__paired_read_length = Slot(uri=AK_SCHEMA.sequencing_data__paired_read_length, name="sequencing_data__paired_read_length", curie=AK_SCHEMA.curie('sequencing_data__paired_read_length'),
                   model_uri=AK_SCHEMA.sequencing_data__paired_read_length, domain=None, range=int)

slots.sequencing_data__index_filename = Slot(uri=AK_SCHEMA.sequencing_data__index_filename, name="sequencing_data__index_filename", curie=AK_SCHEMA.curie('sequencing_data__index_filename'),
                   model_uri=AK_SCHEMA.sequencing_data__index_filename, domain=None, range=Optional[str])

slots.sequencing_data__index_length = Slot(uri=AK_SCHEMA.sequencing_data__index_length, name="sequencing_data__index_length", curie=AK_SCHEMA.curie('sequencing_data__index_length'),
                   model_uri=AK_SCHEMA.sequencing_data__index_length, domain=None, range=Optional[int])

slots.data_processing__data_processing_id = Slot(uri=AK_SCHEMA.data_processing__data_processing_id, name="data_processing__data_processing_id", curie=AK_SCHEMA.curie('data_processing__data_processing_id'),
                   model_uri=AK_SCHEMA.data_processing__data_processing_id, domain=None, range=Optional[str])

slots.data_processing__primary_annotation = Slot(uri=AK_SCHEMA.data_processing__primary_annotation, name="data_processing__primary_annotation", curie=AK_SCHEMA.curie('data_processing__primary_annotation'),
                   model_uri=AK_SCHEMA.data_processing__primary_annotation, domain=None, range=Optional[Union[bool, Bool]])

slots.data_processing__software_versions = Slot(uri=AK_SCHEMA.data_processing__software_versions, name="data_processing__software_versions", curie=AK_SCHEMA.curie('data_processing__software_versions'),
                   model_uri=AK_SCHEMA.data_processing__software_versions, domain=None, range=str)

slots.data_processing__paired_reads_assembly = Slot(uri=AK_SCHEMA.data_processing__paired_reads_assembly, name="data_processing__paired_reads_assembly", curie=AK_SCHEMA.curie('data_processing__paired_reads_assembly'),
                   model_uri=AK_SCHEMA.data_processing__paired_reads_assembly, domain=None, range=str)

slots.data_processing__quality_thresholds = Slot(uri=AK_SCHEMA.data_processing__quality_thresholds, name="data_processing__quality_thresholds", curie=AK_SCHEMA.curie('data_processing__quality_thresholds'),
                   model_uri=AK_SCHEMA.data_processing__quality_thresholds, domain=None, range=str)

slots.data_processing__primer_match_cutoffs = Slot(uri=AK_SCHEMA.data_processing__primer_match_cutoffs, name="data_processing__primer_match_cutoffs", curie=AK_SCHEMA.curie('data_processing__primer_match_cutoffs'),
                   model_uri=AK_SCHEMA.data_processing__primer_match_cutoffs, domain=None, range=str)

slots.data_processing__collapsing_method = Slot(uri=AK_SCHEMA.data_processing__collapsing_method, name="data_processing__collapsing_method", curie=AK_SCHEMA.curie('data_processing__collapsing_method'),
                   model_uri=AK_SCHEMA.data_processing__collapsing_method, domain=None, range=str)

slots.data_processing__data_processing_protocols = Slot(uri=AK_SCHEMA.data_processing__data_processing_protocols, name="data_processing__data_processing_protocols", curie=AK_SCHEMA.curie('data_processing__data_processing_protocols'),
                   model_uri=AK_SCHEMA.data_processing__data_processing_protocols, domain=None, range=str)

slots.data_processing__data_processing_files = Slot(uri=AK_SCHEMA.data_processing__data_processing_files, name="data_processing__data_processing_files", curie=AK_SCHEMA.curie('data_processing__data_processing_files'),
                   model_uri=AK_SCHEMA.data_processing__data_processing_files, domain=None, range=Optional[Union[str, List[str]]])

slots.data_processing__germline_database = Slot(uri=AK_SCHEMA.data_processing__germline_database, name="data_processing__germline_database", curie=AK_SCHEMA.curie('data_processing__germline_database'),
                   model_uri=AK_SCHEMA.data_processing__germline_database, domain=None, range=str)

slots.data_processing__germline_set_ref = Slot(uri=AK_SCHEMA.data_processing__germline_set_ref, name="data_processing__germline_set_ref", curie=AK_SCHEMA.curie('data_processing__germline_set_ref'),
                   model_uri=AK_SCHEMA.data_processing__germline_set_ref, domain=None, range=Optional[str])

slots.data_processing__analysis_provenance_id = Slot(uri=AK_SCHEMA.data_processing__analysis_provenance_id, name="data_processing__analysis_provenance_id", curie=AK_SCHEMA.curie('data_processing__analysis_provenance_id'),
                   model_uri=AK_SCHEMA.data_processing__analysis_provenance_id, domain=None, range=Optional[str])

slots.repertoire__repertoire_id = Slot(uri=AK_SCHEMA.repertoire__repertoire_id, name="repertoire__repertoire_id", curie=AK_SCHEMA.curie('repertoire__repertoire_id'),
                   model_uri=AK_SCHEMA.repertoire__repertoire_id, domain=None, range=Optional[str])

slots.repertoire__repertoire_name = Slot(uri=AK_SCHEMA.repertoire__repertoire_name, name="repertoire__repertoire_name", curie=AK_SCHEMA.curie('repertoire__repertoire_name'),
                   model_uri=AK_SCHEMA.repertoire__repertoire_name, domain=None, range=Optional[str])

slots.repertoire__repertoire_description = Slot(uri=AK_SCHEMA.repertoire__repertoire_description, name="repertoire__repertoire_description", curie=AK_SCHEMA.curie('repertoire__repertoire_description'),
                   model_uri=AK_SCHEMA.repertoire__repertoire_description, domain=None, range=Optional[str])

slots.repertoire__study = Slot(uri=AK_SCHEMA.repertoire__study, name="repertoire__study", curie=AK_SCHEMA.curie('repertoire__study'),
                   model_uri=AK_SCHEMA.repertoire__study, domain=None, range=Union[dict, V1p4Study])

slots.repertoire__subject = Slot(uri=AK_SCHEMA.repertoire__subject, name="repertoire__subject", curie=AK_SCHEMA.curie('repertoire__subject'),
                   model_uri=AK_SCHEMA.repertoire__subject, domain=None, range=Union[dict, V1p4Subject])

slots.repertoire__sample = Slot(uri=AK_SCHEMA.repertoire__sample, name="repertoire__sample", curie=AK_SCHEMA.curie('repertoire__sample'),
                   model_uri=AK_SCHEMA.repertoire__sample, domain=None, range=Union[Union[dict, V1p4SampleProcessing], List[Union[dict, V1p4SampleProcessing]]])

slots.repertoire__data_processing = Slot(uri=AK_SCHEMA.repertoire__data_processing, name="repertoire__data_processing", curie=AK_SCHEMA.curie('repertoire__data_processing'),
                   model_uri=AK_SCHEMA.repertoire__data_processing, domain=None, range=Union[Union[dict, V1p4DataProcessing], List[Union[dict, V1p4DataProcessing]]])

slots.repertoire_group__repertoire_group_id = Slot(uri=AK_SCHEMA.repertoire_group__repertoire_group_id, name="repertoire_group__repertoire_group_id", curie=AK_SCHEMA.curie('repertoire_group__repertoire_group_id'),
                   model_uri=AK_SCHEMA.repertoire_group__repertoire_group_id, domain=None, range=str)

slots.repertoire_group__repertoire_group_name = Slot(uri=AK_SCHEMA.repertoire_group__repertoire_group_name, name="repertoire_group__repertoire_group_name", curie=AK_SCHEMA.curie('repertoire_group__repertoire_group_name'),
                   model_uri=AK_SCHEMA.repertoire_group__repertoire_group_name, domain=None, range=Optional[str])

slots.repertoire_group__repertoire_group_description = Slot(uri=AK_SCHEMA.repertoire_group__repertoire_group_description, name="repertoire_group__repertoire_group_description", curie=AK_SCHEMA.curie('repertoire_group__repertoire_group_description'),
                   model_uri=AK_SCHEMA.repertoire_group__repertoire_group_description, domain=None, range=Optional[str])

slots.repertoire_group__repertoires = Slot(uri=AK_SCHEMA.repertoire_group__repertoires, name="repertoire_group__repertoires", curie=AK_SCHEMA.curie('repertoire_group__repertoires'),
                   model_uri=AK_SCHEMA.repertoire_group__repertoires, domain=None, range=Union[str, List[str]])

slots.alignment__sequence_id = Slot(uri=AK_SCHEMA.alignment__sequence_id, name="alignment__sequence_id", curie=AK_SCHEMA.curie('alignment__sequence_id'),
                   model_uri=AK_SCHEMA.alignment__sequence_id, domain=None, range=str)

slots.alignment__segment = Slot(uri=AK_SCHEMA.alignment__segment, name="alignment__segment", curie=AK_SCHEMA.curie('alignment__segment'),
                   model_uri=AK_SCHEMA.alignment__segment, domain=None, range=str)

slots.alignment__rev_comp = Slot(uri=AK_SCHEMA.alignment__rev_comp, name="alignment__rev_comp", curie=AK_SCHEMA.curie('alignment__rev_comp'),
                   model_uri=AK_SCHEMA.alignment__rev_comp, domain=None, range=Optional[Union[bool, Bool]])

slots.alignment__call = Slot(uri=AK_SCHEMA.alignment__call, name="alignment__call", curie=AK_SCHEMA.curie('alignment__call'),
                   model_uri=AK_SCHEMA.alignment__call, domain=None, range=str)

slots.alignment__score = Slot(uri=AK_SCHEMA.alignment__score, name="alignment__score", curie=AK_SCHEMA.curie('alignment__score'),
                   model_uri=AK_SCHEMA.alignment__score, domain=None, range=float)

slots.alignment__identity = Slot(uri=AK_SCHEMA.alignment__identity, name="alignment__identity", curie=AK_SCHEMA.curie('alignment__identity'),
                   model_uri=AK_SCHEMA.alignment__identity, domain=None, range=Optional[float])

slots.alignment__support = Slot(uri=AK_SCHEMA.alignment__support, name="alignment__support", curie=AK_SCHEMA.curie('alignment__support'),
                   model_uri=AK_SCHEMA.alignment__support, domain=None, range=Optional[float])

slots.alignment__cigar = Slot(uri=AK_SCHEMA.alignment__cigar, name="alignment__cigar", curie=AK_SCHEMA.curie('alignment__cigar'),
                   model_uri=AK_SCHEMA.alignment__cigar, domain=None, range=str)

slots.alignment__sequence_start = Slot(uri=AK_SCHEMA.alignment__sequence_start, name="alignment__sequence_start", curie=AK_SCHEMA.curie('alignment__sequence_start'),
                   model_uri=AK_SCHEMA.alignment__sequence_start, domain=None, range=Optional[int])

slots.alignment__sequence_end = Slot(uri=AK_SCHEMA.alignment__sequence_end, name="alignment__sequence_end", curie=AK_SCHEMA.curie('alignment__sequence_end'),
                   model_uri=AK_SCHEMA.alignment__sequence_end, domain=None, range=Optional[int])

slots.alignment__germline_start = Slot(uri=AK_SCHEMA.alignment__germline_start, name="alignment__germline_start", curie=AK_SCHEMA.curie('alignment__germline_start'),
                   model_uri=AK_SCHEMA.alignment__germline_start, domain=None, range=Optional[int])

slots.alignment__germline_end = Slot(uri=AK_SCHEMA.alignment__germline_end, name="alignment__germline_end", curie=AK_SCHEMA.curie('alignment__germline_end'),
                   model_uri=AK_SCHEMA.alignment__germline_end, domain=None, range=Optional[int])

slots.alignment__rank = Slot(uri=AK_SCHEMA.alignment__rank, name="alignment__rank", curie=AK_SCHEMA.curie('alignment__rank'),
                   model_uri=AK_SCHEMA.alignment__rank, domain=None, range=Optional[int])

slots.alignment__data_processing_id = Slot(uri=AK_SCHEMA.alignment__data_processing_id, name="alignment__data_processing_id", curie=AK_SCHEMA.curie('alignment__data_processing_id'),
                   model_uri=AK_SCHEMA.alignment__data_processing_id, domain=None, range=Optional[str])

slots.rearrangement__sequence_id = Slot(uri=AK_SCHEMA.rearrangement__sequence_id, name="rearrangement__sequence_id", curie=AK_SCHEMA.curie('rearrangement__sequence_id'),
                   model_uri=AK_SCHEMA.rearrangement__sequence_id, domain=None, range=str)

slots.rearrangement__sequence = Slot(uri=AK_SCHEMA.rearrangement__sequence, name="rearrangement__sequence", curie=AK_SCHEMA.curie('rearrangement__sequence'),
                   model_uri=AK_SCHEMA.rearrangement__sequence, domain=None, range=str)

slots.rearrangement__quality = Slot(uri=AK_SCHEMA.rearrangement__quality, name="rearrangement__quality", curie=AK_SCHEMA.curie('rearrangement__quality'),
                   model_uri=AK_SCHEMA.rearrangement__quality, domain=None, range=Optional[str])

slots.rearrangement__sequence_aa = Slot(uri=AK_SCHEMA.rearrangement__sequence_aa, name="rearrangement__sequence_aa", curie=AK_SCHEMA.curie('rearrangement__sequence_aa'),
                   model_uri=AK_SCHEMA.rearrangement__sequence_aa, domain=None, range=Optional[str])

slots.rearrangement__rev_comp = Slot(uri=AK_SCHEMA.rearrangement__rev_comp, name="rearrangement__rev_comp", curie=AK_SCHEMA.curie('rearrangement__rev_comp'),
                   model_uri=AK_SCHEMA.rearrangement__rev_comp, domain=None, range=Union[bool, Bool])

slots.rearrangement__productive = Slot(uri=AK_SCHEMA.rearrangement__productive, name="rearrangement__productive", curie=AK_SCHEMA.curie('rearrangement__productive'),
                   model_uri=AK_SCHEMA.rearrangement__productive, domain=None, range=Union[bool, Bool])

slots.rearrangement__vj_in_frame = Slot(uri=AK_SCHEMA.rearrangement__vj_in_frame, name="rearrangement__vj_in_frame", curie=AK_SCHEMA.curie('rearrangement__vj_in_frame'),
                   model_uri=AK_SCHEMA.rearrangement__vj_in_frame, domain=None, range=Optional[Union[bool, Bool]])

slots.rearrangement__stop_codon = Slot(uri=AK_SCHEMA.rearrangement__stop_codon, name="rearrangement__stop_codon", curie=AK_SCHEMA.curie('rearrangement__stop_codon'),
                   model_uri=AK_SCHEMA.rearrangement__stop_codon, domain=None, range=Optional[Union[bool, Bool]])

slots.rearrangement__complete_vdj = Slot(uri=AK_SCHEMA.rearrangement__complete_vdj, name="rearrangement__complete_vdj", curie=AK_SCHEMA.curie('rearrangement__complete_vdj'),
                   model_uri=AK_SCHEMA.rearrangement__complete_vdj, domain=None, range=Optional[Union[bool, Bool]])

slots.rearrangement__locus = Slot(uri=AK_SCHEMA.rearrangement__locus, name="rearrangement__locus", curie=AK_SCHEMA.curie('rearrangement__locus'),
                   model_uri=AK_SCHEMA.rearrangement__locus, domain=None, range=Optional[Union[str, "V1p4Locus"]])

slots.rearrangement__locus_species = Slot(uri=AK_SCHEMA.rearrangement__locus_species, name="rearrangement__locus_species", curie=AK_SCHEMA.curie('rearrangement__locus_species'),
                   model_uri=AK_SCHEMA.rearrangement__locus_species, domain=None, range=Optional[Union[str, "V1p4LocusSpecies"]])

slots.rearrangement__v_call = Slot(uri=AK_SCHEMA.rearrangement__v_call, name="rearrangement__v_call", curie=AK_SCHEMA.curie('rearrangement__v_call'),
                   model_uri=AK_SCHEMA.rearrangement__v_call, domain=None, range=str)

slots.rearrangement__d_call = Slot(uri=AK_SCHEMA.rearrangement__d_call, name="rearrangement__d_call", curie=AK_SCHEMA.curie('rearrangement__d_call'),
                   model_uri=AK_SCHEMA.rearrangement__d_call, domain=None, range=str)

slots.rearrangement__d2_call = Slot(uri=AK_SCHEMA.rearrangement__d2_call, name="rearrangement__d2_call", curie=AK_SCHEMA.curie('rearrangement__d2_call'),
                   model_uri=AK_SCHEMA.rearrangement__d2_call, domain=None, range=Optional[str])

slots.rearrangement__j_call = Slot(uri=AK_SCHEMA.rearrangement__j_call, name="rearrangement__j_call", curie=AK_SCHEMA.curie('rearrangement__j_call'),
                   model_uri=AK_SCHEMA.rearrangement__j_call, domain=None, range=str)

slots.rearrangement__c_call = Slot(uri=AK_SCHEMA.rearrangement__c_call, name="rearrangement__c_call", curie=AK_SCHEMA.curie('rearrangement__c_call'),
                   model_uri=AK_SCHEMA.rearrangement__c_call, domain=None, range=Optional[str])

slots.rearrangement__sequence_alignment = Slot(uri=AK_SCHEMA.rearrangement__sequence_alignment, name="rearrangement__sequence_alignment", curie=AK_SCHEMA.curie('rearrangement__sequence_alignment'),
                   model_uri=AK_SCHEMA.rearrangement__sequence_alignment, domain=None, range=str)

slots.rearrangement__quality_alignment = Slot(uri=AK_SCHEMA.rearrangement__quality_alignment, name="rearrangement__quality_alignment", curie=AK_SCHEMA.curie('rearrangement__quality_alignment'),
                   model_uri=AK_SCHEMA.rearrangement__quality_alignment, domain=None, range=Optional[str])

slots.rearrangement__sequence_alignment_aa = Slot(uri=AK_SCHEMA.rearrangement__sequence_alignment_aa, name="rearrangement__sequence_alignment_aa", curie=AK_SCHEMA.curie('rearrangement__sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangement__sequence_alignment_aa, domain=None, range=Optional[str])

slots.rearrangement__germline_alignment = Slot(uri=AK_SCHEMA.rearrangement__germline_alignment, name="rearrangement__germline_alignment", curie=AK_SCHEMA.curie('rearrangement__germline_alignment'),
                   model_uri=AK_SCHEMA.rearrangement__germline_alignment, domain=None, range=str)

slots.rearrangement__germline_alignment_aa = Slot(uri=AK_SCHEMA.rearrangement__germline_alignment_aa, name="rearrangement__germline_alignment_aa", curie=AK_SCHEMA.curie('rearrangement__germline_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangement__germline_alignment_aa, domain=None, range=Optional[str])

slots.rearrangement__junction = Slot(uri=AK_SCHEMA.rearrangement__junction, name="rearrangement__junction", curie=AK_SCHEMA.curie('rearrangement__junction'),
                   model_uri=AK_SCHEMA.rearrangement__junction, domain=None, range=str)

slots.rearrangement__junction_aa = Slot(uri=AK_SCHEMA.rearrangement__junction_aa, name="rearrangement__junction_aa", curie=AK_SCHEMA.curie('rearrangement__junction_aa'),
                   model_uri=AK_SCHEMA.rearrangement__junction_aa, domain=None, range=str)

slots.rearrangement__np1 = Slot(uri=AK_SCHEMA.rearrangement__np1, name="rearrangement__np1", curie=AK_SCHEMA.curie('rearrangement__np1'),
                   model_uri=AK_SCHEMA.rearrangement__np1, domain=None, range=Optional[str])

slots.rearrangement__np1_aa = Slot(uri=AK_SCHEMA.rearrangement__np1_aa, name="rearrangement__np1_aa", curie=AK_SCHEMA.curie('rearrangement__np1_aa'),
                   model_uri=AK_SCHEMA.rearrangement__np1_aa, domain=None, range=Optional[str])

slots.rearrangement__np2 = Slot(uri=AK_SCHEMA.rearrangement__np2, name="rearrangement__np2", curie=AK_SCHEMA.curie('rearrangement__np2'),
                   model_uri=AK_SCHEMA.rearrangement__np2, domain=None, range=Optional[str])

slots.rearrangement__np2_aa = Slot(uri=AK_SCHEMA.rearrangement__np2_aa, name="rearrangement__np2_aa", curie=AK_SCHEMA.curie('rearrangement__np2_aa'),
                   model_uri=AK_SCHEMA.rearrangement__np2_aa, domain=None, range=Optional[str])

slots.rearrangement__np3 = Slot(uri=AK_SCHEMA.rearrangement__np3, name="rearrangement__np3", curie=AK_SCHEMA.curie('rearrangement__np3'),
                   model_uri=AK_SCHEMA.rearrangement__np3, domain=None, range=Optional[str])

slots.rearrangement__np3_aa = Slot(uri=AK_SCHEMA.rearrangement__np3_aa, name="rearrangement__np3_aa", curie=AK_SCHEMA.curie('rearrangement__np3_aa'),
                   model_uri=AK_SCHEMA.rearrangement__np3_aa, domain=None, range=Optional[str])

slots.rearrangement__cdr1 = Slot(uri=AK_SCHEMA.rearrangement__cdr1, name="rearrangement__cdr1", curie=AK_SCHEMA.curie('rearrangement__cdr1'),
                   model_uri=AK_SCHEMA.rearrangement__cdr1, domain=None, range=Optional[str])

slots.rearrangement__cdr1_aa = Slot(uri=AK_SCHEMA.rearrangement__cdr1_aa, name="rearrangement__cdr1_aa", curie=AK_SCHEMA.curie('rearrangement__cdr1_aa'),
                   model_uri=AK_SCHEMA.rearrangement__cdr1_aa, domain=None, range=Optional[str])

slots.rearrangement__cdr2 = Slot(uri=AK_SCHEMA.rearrangement__cdr2, name="rearrangement__cdr2", curie=AK_SCHEMA.curie('rearrangement__cdr2'),
                   model_uri=AK_SCHEMA.rearrangement__cdr2, domain=None, range=Optional[str])

slots.rearrangement__cdr2_aa = Slot(uri=AK_SCHEMA.rearrangement__cdr2_aa, name="rearrangement__cdr2_aa", curie=AK_SCHEMA.curie('rearrangement__cdr2_aa'),
                   model_uri=AK_SCHEMA.rearrangement__cdr2_aa, domain=None, range=Optional[str])

slots.rearrangement__cdr3 = Slot(uri=AK_SCHEMA.rearrangement__cdr3, name="rearrangement__cdr3", curie=AK_SCHEMA.curie('rearrangement__cdr3'),
                   model_uri=AK_SCHEMA.rearrangement__cdr3, domain=None, range=Optional[str])

slots.rearrangement__cdr3_aa = Slot(uri=AK_SCHEMA.rearrangement__cdr3_aa, name="rearrangement__cdr3_aa", curie=AK_SCHEMA.curie('rearrangement__cdr3_aa'),
                   model_uri=AK_SCHEMA.rearrangement__cdr3_aa, domain=None, range=Optional[str])

slots.rearrangement__fwr1 = Slot(uri=AK_SCHEMA.rearrangement__fwr1, name="rearrangement__fwr1", curie=AK_SCHEMA.curie('rearrangement__fwr1'),
                   model_uri=AK_SCHEMA.rearrangement__fwr1, domain=None, range=Optional[str])

slots.rearrangement__fwr1_aa = Slot(uri=AK_SCHEMA.rearrangement__fwr1_aa, name="rearrangement__fwr1_aa", curie=AK_SCHEMA.curie('rearrangement__fwr1_aa'),
                   model_uri=AK_SCHEMA.rearrangement__fwr1_aa, domain=None, range=Optional[str])

slots.rearrangement__fwr2 = Slot(uri=AK_SCHEMA.rearrangement__fwr2, name="rearrangement__fwr2", curie=AK_SCHEMA.curie('rearrangement__fwr2'),
                   model_uri=AK_SCHEMA.rearrangement__fwr2, domain=None, range=Optional[str])

slots.rearrangement__fwr2_aa = Slot(uri=AK_SCHEMA.rearrangement__fwr2_aa, name="rearrangement__fwr2_aa", curie=AK_SCHEMA.curie('rearrangement__fwr2_aa'),
                   model_uri=AK_SCHEMA.rearrangement__fwr2_aa, domain=None, range=Optional[str])

slots.rearrangement__fwr3 = Slot(uri=AK_SCHEMA.rearrangement__fwr3, name="rearrangement__fwr3", curie=AK_SCHEMA.curie('rearrangement__fwr3'),
                   model_uri=AK_SCHEMA.rearrangement__fwr3, domain=None, range=Optional[str])

slots.rearrangement__fwr3_aa = Slot(uri=AK_SCHEMA.rearrangement__fwr3_aa, name="rearrangement__fwr3_aa", curie=AK_SCHEMA.curie('rearrangement__fwr3_aa'),
                   model_uri=AK_SCHEMA.rearrangement__fwr3_aa, domain=None, range=Optional[str])

slots.rearrangement__fwr4 = Slot(uri=AK_SCHEMA.rearrangement__fwr4, name="rearrangement__fwr4", curie=AK_SCHEMA.curie('rearrangement__fwr4'),
                   model_uri=AK_SCHEMA.rearrangement__fwr4, domain=None, range=Optional[str])

slots.rearrangement__fwr4_aa = Slot(uri=AK_SCHEMA.rearrangement__fwr4_aa, name="rearrangement__fwr4_aa", curie=AK_SCHEMA.curie('rearrangement__fwr4_aa'),
                   model_uri=AK_SCHEMA.rearrangement__fwr4_aa, domain=None, range=Optional[str])

slots.rearrangement__v_score = Slot(uri=AK_SCHEMA.rearrangement__v_score, name="rearrangement__v_score", curie=AK_SCHEMA.curie('rearrangement__v_score'),
                   model_uri=AK_SCHEMA.rearrangement__v_score, domain=None, range=Optional[float])

slots.rearrangement__v_identity = Slot(uri=AK_SCHEMA.rearrangement__v_identity, name="rearrangement__v_identity", curie=AK_SCHEMA.curie('rearrangement__v_identity'),
                   model_uri=AK_SCHEMA.rearrangement__v_identity, domain=None, range=Optional[float])

slots.rearrangement__v_support = Slot(uri=AK_SCHEMA.rearrangement__v_support, name="rearrangement__v_support", curie=AK_SCHEMA.curie('rearrangement__v_support'),
                   model_uri=AK_SCHEMA.rearrangement__v_support, domain=None, range=Optional[float])

slots.rearrangement__v_cigar = Slot(uri=AK_SCHEMA.rearrangement__v_cigar, name="rearrangement__v_cigar", curie=AK_SCHEMA.curie('rearrangement__v_cigar'),
                   model_uri=AK_SCHEMA.rearrangement__v_cigar, domain=None, range=str)

slots.rearrangement__d_score = Slot(uri=AK_SCHEMA.rearrangement__d_score, name="rearrangement__d_score", curie=AK_SCHEMA.curie('rearrangement__d_score'),
                   model_uri=AK_SCHEMA.rearrangement__d_score, domain=None, range=Optional[float])

slots.rearrangement__d_identity = Slot(uri=AK_SCHEMA.rearrangement__d_identity, name="rearrangement__d_identity", curie=AK_SCHEMA.curie('rearrangement__d_identity'),
                   model_uri=AK_SCHEMA.rearrangement__d_identity, domain=None, range=Optional[float])

slots.rearrangement__d_support = Slot(uri=AK_SCHEMA.rearrangement__d_support, name="rearrangement__d_support", curie=AK_SCHEMA.curie('rearrangement__d_support'),
                   model_uri=AK_SCHEMA.rearrangement__d_support, domain=None, range=Optional[float])

slots.rearrangement__d_cigar = Slot(uri=AK_SCHEMA.rearrangement__d_cigar, name="rearrangement__d_cigar", curie=AK_SCHEMA.curie('rearrangement__d_cigar'),
                   model_uri=AK_SCHEMA.rearrangement__d_cigar, domain=None, range=str)

slots.rearrangement__d2_score = Slot(uri=AK_SCHEMA.rearrangement__d2_score, name="rearrangement__d2_score", curie=AK_SCHEMA.curie('rearrangement__d2_score'),
                   model_uri=AK_SCHEMA.rearrangement__d2_score, domain=None, range=Optional[float])

slots.rearrangement__d2_identity = Slot(uri=AK_SCHEMA.rearrangement__d2_identity, name="rearrangement__d2_identity", curie=AK_SCHEMA.curie('rearrangement__d2_identity'),
                   model_uri=AK_SCHEMA.rearrangement__d2_identity, domain=None, range=Optional[float])

slots.rearrangement__d2_support = Slot(uri=AK_SCHEMA.rearrangement__d2_support, name="rearrangement__d2_support", curie=AK_SCHEMA.curie('rearrangement__d2_support'),
                   model_uri=AK_SCHEMA.rearrangement__d2_support, domain=None, range=Optional[float])

slots.rearrangement__d2_cigar = Slot(uri=AK_SCHEMA.rearrangement__d2_cigar, name="rearrangement__d2_cigar", curie=AK_SCHEMA.curie('rearrangement__d2_cigar'),
                   model_uri=AK_SCHEMA.rearrangement__d2_cigar, domain=None, range=Optional[str])

slots.rearrangement__j_score = Slot(uri=AK_SCHEMA.rearrangement__j_score, name="rearrangement__j_score", curie=AK_SCHEMA.curie('rearrangement__j_score'),
                   model_uri=AK_SCHEMA.rearrangement__j_score, domain=None, range=Optional[float])

slots.rearrangement__j_identity = Slot(uri=AK_SCHEMA.rearrangement__j_identity, name="rearrangement__j_identity", curie=AK_SCHEMA.curie('rearrangement__j_identity'),
                   model_uri=AK_SCHEMA.rearrangement__j_identity, domain=None, range=Optional[float])

slots.rearrangement__j_support = Slot(uri=AK_SCHEMA.rearrangement__j_support, name="rearrangement__j_support", curie=AK_SCHEMA.curie('rearrangement__j_support'),
                   model_uri=AK_SCHEMA.rearrangement__j_support, domain=None, range=Optional[float])

slots.rearrangement__j_cigar = Slot(uri=AK_SCHEMA.rearrangement__j_cigar, name="rearrangement__j_cigar", curie=AK_SCHEMA.curie('rearrangement__j_cigar'),
                   model_uri=AK_SCHEMA.rearrangement__j_cigar, domain=None, range=str)

slots.rearrangement__c_score = Slot(uri=AK_SCHEMA.rearrangement__c_score, name="rearrangement__c_score", curie=AK_SCHEMA.curie('rearrangement__c_score'),
                   model_uri=AK_SCHEMA.rearrangement__c_score, domain=None, range=Optional[float])

slots.rearrangement__c_identity = Slot(uri=AK_SCHEMA.rearrangement__c_identity, name="rearrangement__c_identity", curie=AK_SCHEMA.curie('rearrangement__c_identity'),
                   model_uri=AK_SCHEMA.rearrangement__c_identity, domain=None, range=Optional[float])

slots.rearrangement__c_support = Slot(uri=AK_SCHEMA.rearrangement__c_support, name="rearrangement__c_support", curie=AK_SCHEMA.curie('rearrangement__c_support'),
                   model_uri=AK_SCHEMA.rearrangement__c_support, domain=None, range=Optional[float])

slots.rearrangement__c_cigar = Slot(uri=AK_SCHEMA.rearrangement__c_cigar, name="rearrangement__c_cigar", curie=AK_SCHEMA.curie('rearrangement__c_cigar'),
                   model_uri=AK_SCHEMA.rearrangement__c_cigar, domain=None, range=Optional[str])

slots.rearrangement__v_sequence_start = Slot(uri=AK_SCHEMA.rearrangement__v_sequence_start, name="rearrangement__v_sequence_start", curie=AK_SCHEMA.curie('rearrangement__v_sequence_start'),
                   model_uri=AK_SCHEMA.rearrangement__v_sequence_start, domain=None, range=Optional[int])

slots.rearrangement__v_sequence_end = Slot(uri=AK_SCHEMA.rearrangement__v_sequence_end, name="rearrangement__v_sequence_end", curie=AK_SCHEMA.curie('rearrangement__v_sequence_end'),
                   model_uri=AK_SCHEMA.rearrangement__v_sequence_end, domain=None, range=Optional[int])

slots.rearrangement__v_germline_start = Slot(uri=AK_SCHEMA.rearrangement__v_germline_start, name="rearrangement__v_germline_start", curie=AK_SCHEMA.curie('rearrangement__v_germline_start'),
                   model_uri=AK_SCHEMA.rearrangement__v_germline_start, domain=None, range=Optional[int])

slots.rearrangement__v_germline_end = Slot(uri=AK_SCHEMA.rearrangement__v_germline_end, name="rearrangement__v_germline_end", curie=AK_SCHEMA.curie('rearrangement__v_germline_end'),
                   model_uri=AK_SCHEMA.rearrangement__v_germline_end, domain=None, range=Optional[int])

slots.rearrangement__v_alignment_start = Slot(uri=AK_SCHEMA.rearrangement__v_alignment_start, name="rearrangement__v_alignment_start", curie=AK_SCHEMA.curie('rearrangement__v_alignment_start'),
                   model_uri=AK_SCHEMA.rearrangement__v_alignment_start, domain=None, range=Optional[int])

slots.rearrangement__v_alignment_end = Slot(uri=AK_SCHEMA.rearrangement__v_alignment_end, name="rearrangement__v_alignment_end", curie=AK_SCHEMA.curie('rearrangement__v_alignment_end'),
                   model_uri=AK_SCHEMA.rearrangement__v_alignment_end, domain=None, range=Optional[int])

slots.rearrangement__d_sequence_start = Slot(uri=AK_SCHEMA.rearrangement__d_sequence_start, name="rearrangement__d_sequence_start", curie=AK_SCHEMA.curie('rearrangement__d_sequence_start'),
                   model_uri=AK_SCHEMA.rearrangement__d_sequence_start, domain=None, range=Optional[int])

slots.rearrangement__d_sequence_end = Slot(uri=AK_SCHEMA.rearrangement__d_sequence_end, name="rearrangement__d_sequence_end", curie=AK_SCHEMA.curie('rearrangement__d_sequence_end'),
                   model_uri=AK_SCHEMA.rearrangement__d_sequence_end, domain=None, range=Optional[int])

slots.rearrangement__d_germline_start = Slot(uri=AK_SCHEMA.rearrangement__d_germline_start, name="rearrangement__d_germline_start", curie=AK_SCHEMA.curie('rearrangement__d_germline_start'),
                   model_uri=AK_SCHEMA.rearrangement__d_germline_start, domain=None, range=Optional[int])

slots.rearrangement__d_germline_end = Slot(uri=AK_SCHEMA.rearrangement__d_germline_end, name="rearrangement__d_germline_end", curie=AK_SCHEMA.curie('rearrangement__d_germline_end'),
                   model_uri=AK_SCHEMA.rearrangement__d_germline_end, domain=None, range=Optional[int])

slots.rearrangement__d_alignment_start = Slot(uri=AK_SCHEMA.rearrangement__d_alignment_start, name="rearrangement__d_alignment_start", curie=AK_SCHEMA.curie('rearrangement__d_alignment_start'),
                   model_uri=AK_SCHEMA.rearrangement__d_alignment_start, domain=None, range=Optional[int])

slots.rearrangement__d_alignment_end = Slot(uri=AK_SCHEMA.rearrangement__d_alignment_end, name="rearrangement__d_alignment_end", curie=AK_SCHEMA.curie('rearrangement__d_alignment_end'),
                   model_uri=AK_SCHEMA.rearrangement__d_alignment_end, domain=None, range=Optional[int])

slots.rearrangement__d2_sequence_start = Slot(uri=AK_SCHEMA.rearrangement__d2_sequence_start, name="rearrangement__d2_sequence_start", curie=AK_SCHEMA.curie('rearrangement__d2_sequence_start'),
                   model_uri=AK_SCHEMA.rearrangement__d2_sequence_start, domain=None, range=Optional[int])

slots.rearrangement__d2_sequence_end = Slot(uri=AK_SCHEMA.rearrangement__d2_sequence_end, name="rearrangement__d2_sequence_end", curie=AK_SCHEMA.curie('rearrangement__d2_sequence_end'),
                   model_uri=AK_SCHEMA.rearrangement__d2_sequence_end, domain=None, range=Optional[int])

slots.rearrangement__d2_germline_start = Slot(uri=AK_SCHEMA.rearrangement__d2_germline_start, name="rearrangement__d2_germline_start", curie=AK_SCHEMA.curie('rearrangement__d2_germline_start'),
                   model_uri=AK_SCHEMA.rearrangement__d2_germline_start, domain=None, range=Optional[int])

slots.rearrangement__d2_germline_end = Slot(uri=AK_SCHEMA.rearrangement__d2_germline_end, name="rearrangement__d2_germline_end", curie=AK_SCHEMA.curie('rearrangement__d2_germline_end'),
                   model_uri=AK_SCHEMA.rearrangement__d2_germline_end, domain=None, range=Optional[int])

slots.rearrangement__d2_alignment_start = Slot(uri=AK_SCHEMA.rearrangement__d2_alignment_start, name="rearrangement__d2_alignment_start", curie=AK_SCHEMA.curie('rearrangement__d2_alignment_start'),
                   model_uri=AK_SCHEMA.rearrangement__d2_alignment_start, domain=None, range=Optional[int])

slots.rearrangement__d2_alignment_end = Slot(uri=AK_SCHEMA.rearrangement__d2_alignment_end, name="rearrangement__d2_alignment_end", curie=AK_SCHEMA.curie('rearrangement__d2_alignment_end'),
                   model_uri=AK_SCHEMA.rearrangement__d2_alignment_end, domain=None, range=Optional[int])

slots.rearrangement__j_sequence_start = Slot(uri=AK_SCHEMA.rearrangement__j_sequence_start, name="rearrangement__j_sequence_start", curie=AK_SCHEMA.curie('rearrangement__j_sequence_start'),
                   model_uri=AK_SCHEMA.rearrangement__j_sequence_start, domain=None, range=Optional[int])

slots.rearrangement__j_sequence_end = Slot(uri=AK_SCHEMA.rearrangement__j_sequence_end, name="rearrangement__j_sequence_end", curie=AK_SCHEMA.curie('rearrangement__j_sequence_end'),
                   model_uri=AK_SCHEMA.rearrangement__j_sequence_end, domain=None, range=Optional[int])

slots.rearrangement__j_germline_start = Slot(uri=AK_SCHEMA.rearrangement__j_germline_start, name="rearrangement__j_germline_start", curie=AK_SCHEMA.curie('rearrangement__j_germline_start'),
                   model_uri=AK_SCHEMA.rearrangement__j_germline_start, domain=None, range=Optional[int])

slots.rearrangement__j_germline_end = Slot(uri=AK_SCHEMA.rearrangement__j_germline_end, name="rearrangement__j_germline_end", curie=AK_SCHEMA.curie('rearrangement__j_germline_end'),
                   model_uri=AK_SCHEMA.rearrangement__j_germline_end, domain=None, range=Optional[int])

slots.rearrangement__j_alignment_start = Slot(uri=AK_SCHEMA.rearrangement__j_alignment_start, name="rearrangement__j_alignment_start", curie=AK_SCHEMA.curie('rearrangement__j_alignment_start'),
                   model_uri=AK_SCHEMA.rearrangement__j_alignment_start, domain=None, range=Optional[int])

slots.rearrangement__j_alignment_end = Slot(uri=AK_SCHEMA.rearrangement__j_alignment_end, name="rearrangement__j_alignment_end", curie=AK_SCHEMA.curie('rearrangement__j_alignment_end'),
                   model_uri=AK_SCHEMA.rearrangement__j_alignment_end, domain=None, range=Optional[int])

slots.rearrangement__c_sequence_start = Slot(uri=AK_SCHEMA.rearrangement__c_sequence_start, name="rearrangement__c_sequence_start", curie=AK_SCHEMA.curie('rearrangement__c_sequence_start'),
                   model_uri=AK_SCHEMA.rearrangement__c_sequence_start, domain=None, range=Optional[int])

slots.rearrangement__c_sequence_end = Slot(uri=AK_SCHEMA.rearrangement__c_sequence_end, name="rearrangement__c_sequence_end", curie=AK_SCHEMA.curie('rearrangement__c_sequence_end'),
                   model_uri=AK_SCHEMA.rearrangement__c_sequence_end, domain=None, range=Optional[int])

slots.rearrangement__c_germline_start = Slot(uri=AK_SCHEMA.rearrangement__c_germline_start, name="rearrangement__c_germline_start", curie=AK_SCHEMA.curie('rearrangement__c_germline_start'),
                   model_uri=AK_SCHEMA.rearrangement__c_germline_start, domain=None, range=Optional[int])

slots.rearrangement__c_germline_end = Slot(uri=AK_SCHEMA.rearrangement__c_germline_end, name="rearrangement__c_germline_end", curie=AK_SCHEMA.curie('rearrangement__c_germline_end'),
                   model_uri=AK_SCHEMA.rearrangement__c_germline_end, domain=None, range=Optional[int])

slots.rearrangement__c_alignment_start = Slot(uri=AK_SCHEMA.rearrangement__c_alignment_start, name="rearrangement__c_alignment_start", curie=AK_SCHEMA.curie('rearrangement__c_alignment_start'),
                   model_uri=AK_SCHEMA.rearrangement__c_alignment_start, domain=None, range=Optional[int])

slots.rearrangement__c_alignment_end = Slot(uri=AK_SCHEMA.rearrangement__c_alignment_end, name="rearrangement__c_alignment_end", curie=AK_SCHEMA.curie('rearrangement__c_alignment_end'),
                   model_uri=AK_SCHEMA.rearrangement__c_alignment_end, domain=None, range=Optional[int])

slots.rearrangement__cdr1_start = Slot(uri=AK_SCHEMA.rearrangement__cdr1_start, name="rearrangement__cdr1_start", curie=AK_SCHEMA.curie('rearrangement__cdr1_start'),
                   model_uri=AK_SCHEMA.rearrangement__cdr1_start, domain=None, range=Optional[int])

slots.rearrangement__cdr1_end = Slot(uri=AK_SCHEMA.rearrangement__cdr1_end, name="rearrangement__cdr1_end", curie=AK_SCHEMA.curie('rearrangement__cdr1_end'),
                   model_uri=AK_SCHEMA.rearrangement__cdr1_end, domain=None, range=Optional[int])

slots.rearrangement__cdr2_start = Slot(uri=AK_SCHEMA.rearrangement__cdr2_start, name="rearrangement__cdr2_start", curie=AK_SCHEMA.curie('rearrangement__cdr2_start'),
                   model_uri=AK_SCHEMA.rearrangement__cdr2_start, domain=None, range=Optional[int])

slots.rearrangement__cdr2_end = Slot(uri=AK_SCHEMA.rearrangement__cdr2_end, name="rearrangement__cdr2_end", curie=AK_SCHEMA.curie('rearrangement__cdr2_end'),
                   model_uri=AK_SCHEMA.rearrangement__cdr2_end, domain=None, range=Optional[int])

slots.rearrangement__cdr3_start = Slot(uri=AK_SCHEMA.rearrangement__cdr3_start, name="rearrangement__cdr3_start", curie=AK_SCHEMA.curie('rearrangement__cdr3_start'),
                   model_uri=AK_SCHEMA.rearrangement__cdr3_start, domain=None, range=Optional[int])

slots.rearrangement__cdr3_end = Slot(uri=AK_SCHEMA.rearrangement__cdr3_end, name="rearrangement__cdr3_end", curie=AK_SCHEMA.curie('rearrangement__cdr3_end'),
                   model_uri=AK_SCHEMA.rearrangement__cdr3_end, domain=None, range=Optional[int])

slots.rearrangement__fwr1_start = Slot(uri=AK_SCHEMA.rearrangement__fwr1_start, name="rearrangement__fwr1_start", curie=AK_SCHEMA.curie('rearrangement__fwr1_start'),
                   model_uri=AK_SCHEMA.rearrangement__fwr1_start, domain=None, range=Optional[int])

slots.rearrangement__fwr1_end = Slot(uri=AK_SCHEMA.rearrangement__fwr1_end, name="rearrangement__fwr1_end", curie=AK_SCHEMA.curie('rearrangement__fwr1_end'),
                   model_uri=AK_SCHEMA.rearrangement__fwr1_end, domain=None, range=Optional[int])

slots.rearrangement__fwr2_start = Slot(uri=AK_SCHEMA.rearrangement__fwr2_start, name="rearrangement__fwr2_start", curie=AK_SCHEMA.curie('rearrangement__fwr2_start'),
                   model_uri=AK_SCHEMA.rearrangement__fwr2_start, domain=None, range=Optional[int])

slots.rearrangement__fwr2_end = Slot(uri=AK_SCHEMA.rearrangement__fwr2_end, name="rearrangement__fwr2_end", curie=AK_SCHEMA.curie('rearrangement__fwr2_end'),
                   model_uri=AK_SCHEMA.rearrangement__fwr2_end, domain=None, range=Optional[int])

slots.rearrangement__fwr3_start = Slot(uri=AK_SCHEMA.rearrangement__fwr3_start, name="rearrangement__fwr3_start", curie=AK_SCHEMA.curie('rearrangement__fwr3_start'),
                   model_uri=AK_SCHEMA.rearrangement__fwr3_start, domain=None, range=Optional[int])

slots.rearrangement__fwr3_end = Slot(uri=AK_SCHEMA.rearrangement__fwr3_end, name="rearrangement__fwr3_end", curie=AK_SCHEMA.curie('rearrangement__fwr3_end'),
                   model_uri=AK_SCHEMA.rearrangement__fwr3_end, domain=None, range=Optional[int])

slots.rearrangement__fwr4_start = Slot(uri=AK_SCHEMA.rearrangement__fwr4_start, name="rearrangement__fwr4_start", curie=AK_SCHEMA.curie('rearrangement__fwr4_start'),
                   model_uri=AK_SCHEMA.rearrangement__fwr4_start, domain=None, range=Optional[int])

slots.rearrangement__fwr4_end = Slot(uri=AK_SCHEMA.rearrangement__fwr4_end, name="rearrangement__fwr4_end", curie=AK_SCHEMA.curie('rearrangement__fwr4_end'),
                   model_uri=AK_SCHEMA.rearrangement__fwr4_end, domain=None, range=Optional[int])

slots.rearrangement__v_sequence_alignment = Slot(uri=AK_SCHEMA.rearrangement__v_sequence_alignment, name="rearrangement__v_sequence_alignment", curie=AK_SCHEMA.curie('rearrangement__v_sequence_alignment'),
                   model_uri=AK_SCHEMA.rearrangement__v_sequence_alignment, domain=None, range=Optional[str])

slots.rearrangement__v_sequence_alignment_aa = Slot(uri=AK_SCHEMA.rearrangement__v_sequence_alignment_aa, name="rearrangement__v_sequence_alignment_aa", curie=AK_SCHEMA.curie('rearrangement__v_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangement__v_sequence_alignment_aa, domain=None, range=Optional[str])

slots.rearrangement__d_sequence_alignment = Slot(uri=AK_SCHEMA.rearrangement__d_sequence_alignment, name="rearrangement__d_sequence_alignment", curie=AK_SCHEMA.curie('rearrangement__d_sequence_alignment'),
                   model_uri=AK_SCHEMA.rearrangement__d_sequence_alignment, domain=None, range=Optional[str])

slots.rearrangement__d_sequence_alignment_aa = Slot(uri=AK_SCHEMA.rearrangement__d_sequence_alignment_aa, name="rearrangement__d_sequence_alignment_aa", curie=AK_SCHEMA.curie('rearrangement__d_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangement__d_sequence_alignment_aa, domain=None, range=Optional[str])

slots.rearrangement__d2_sequence_alignment = Slot(uri=AK_SCHEMA.rearrangement__d2_sequence_alignment, name="rearrangement__d2_sequence_alignment", curie=AK_SCHEMA.curie('rearrangement__d2_sequence_alignment'),
                   model_uri=AK_SCHEMA.rearrangement__d2_sequence_alignment, domain=None, range=Optional[str])

slots.rearrangement__d2_sequence_alignment_aa = Slot(uri=AK_SCHEMA.rearrangement__d2_sequence_alignment_aa, name="rearrangement__d2_sequence_alignment_aa", curie=AK_SCHEMA.curie('rearrangement__d2_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangement__d2_sequence_alignment_aa, domain=None, range=Optional[str])

slots.rearrangement__j_sequence_alignment = Slot(uri=AK_SCHEMA.rearrangement__j_sequence_alignment, name="rearrangement__j_sequence_alignment", curie=AK_SCHEMA.curie('rearrangement__j_sequence_alignment'),
                   model_uri=AK_SCHEMA.rearrangement__j_sequence_alignment, domain=None, range=Optional[str])

slots.rearrangement__j_sequence_alignment_aa = Slot(uri=AK_SCHEMA.rearrangement__j_sequence_alignment_aa, name="rearrangement__j_sequence_alignment_aa", curie=AK_SCHEMA.curie('rearrangement__j_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangement__j_sequence_alignment_aa, domain=None, range=Optional[str])

slots.rearrangement__c_sequence_alignment = Slot(uri=AK_SCHEMA.rearrangement__c_sequence_alignment, name="rearrangement__c_sequence_alignment", curie=AK_SCHEMA.curie('rearrangement__c_sequence_alignment'),
                   model_uri=AK_SCHEMA.rearrangement__c_sequence_alignment, domain=None, range=Optional[str])

slots.rearrangement__c_sequence_alignment_aa = Slot(uri=AK_SCHEMA.rearrangement__c_sequence_alignment_aa, name="rearrangement__c_sequence_alignment_aa", curie=AK_SCHEMA.curie('rearrangement__c_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangement__c_sequence_alignment_aa, domain=None, range=Optional[str])

slots.rearrangement__v_germline_alignment = Slot(uri=AK_SCHEMA.rearrangement__v_germline_alignment, name="rearrangement__v_germline_alignment", curie=AK_SCHEMA.curie('rearrangement__v_germline_alignment'),
                   model_uri=AK_SCHEMA.rearrangement__v_germline_alignment, domain=None, range=Optional[str])

slots.rearrangement__v_germline_alignment_aa = Slot(uri=AK_SCHEMA.rearrangement__v_germline_alignment_aa, name="rearrangement__v_germline_alignment_aa", curie=AK_SCHEMA.curie('rearrangement__v_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangement__v_germline_alignment_aa, domain=None, range=Optional[str])

slots.rearrangement__d_germline_alignment = Slot(uri=AK_SCHEMA.rearrangement__d_germline_alignment, name="rearrangement__d_germline_alignment", curie=AK_SCHEMA.curie('rearrangement__d_germline_alignment'),
                   model_uri=AK_SCHEMA.rearrangement__d_germline_alignment, domain=None, range=Optional[str])

slots.rearrangement__d_germline_alignment_aa = Slot(uri=AK_SCHEMA.rearrangement__d_germline_alignment_aa, name="rearrangement__d_germline_alignment_aa", curie=AK_SCHEMA.curie('rearrangement__d_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangement__d_germline_alignment_aa, domain=None, range=Optional[str])

slots.rearrangement__d2_germline_alignment = Slot(uri=AK_SCHEMA.rearrangement__d2_germline_alignment, name="rearrangement__d2_germline_alignment", curie=AK_SCHEMA.curie('rearrangement__d2_germline_alignment'),
                   model_uri=AK_SCHEMA.rearrangement__d2_germline_alignment, domain=None, range=Optional[str])

slots.rearrangement__d2_germline_alignment_aa = Slot(uri=AK_SCHEMA.rearrangement__d2_germline_alignment_aa, name="rearrangement__d2_germline_alignment_aa", curie=AK_SCHEMA.curie('rearrangement__d2_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangement__d2_germline_alignment_aa, domain=None, range=Optional[str])

slots.rearrangement__j_germline_alignment = Slot(uri=AK_SCHEMA.rearrangement__j_germline_alignment, name="rearrangement__j_germline_alignment", curie=AK_SCHEMA.curie('rearrangement__j_germline_alignment'),
                   model_uri=AK_SCHEMA.rearrangement__j_germline_alignment, domain=None, range=Optional[str])

slots.rearrangement__j_germline_alignment_aa = Slot(uri=AK_SCHEMA.rearrangement__j_germline_alignment_aa, name="rearrangement__j_germline_alignment_aa", curie=AK_SCHEMA.curie('rearrangement__j_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangement__j_germline_alignment_aa, domain=None, range=Optional[str])

slots.rearrangement__c_germline_alignment = Slot(uri=AK_SCHEMA.rearrangement__c_germline_alignment, name="rearrangement__c_germline_alignment", curie=AK_SCHEMA.curie('rearrangement__c_germline_alignment'),
                   model_uri=AK_SCHEMA.rearrangement__c_germline_alignment, domain=None, range=Optional[str])

slots.rearrangement__c_germline_alignment_aa = Slot(uri=AK_SCHEMA.rearrangement__c_germline_alignment_aa, name="rearrangement__c_germline_alignment_aa", curie=AK_SCHEMA.curie('rearrangement__c_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.rearrangement__c_germline_alignment_aa, domain=None, range=Optional[str])

slots.rearrangement__junction_length = Slot(uri=AK_SCHEMA.rearrangement__junction_length, name="rearrangement__junction_length", curie=AK_SCHEMA.curie('rearrangement__junction_length'),
                   model_uri=AK_SCHEMA.rearrangement__junction_length, domain=None, range=Optional[int])

slots.rearrangement__junction_aa_length = Slot(uri=AK_SCHEMA.rearrangement__junction_aa_length, name="rearrangement__junction_aa_length", curie=AK_SCHEMA.curie('rearrangement__junction_aa_length'),
                   model_uri=AK_SCHEMA.rearrangement__junction_aa_length, domain=None, range=Optional[int])

slots.rearrangement__np1_length = Slot(uri=AK_SCHEMA.rearrangement__np1_length, name="rearrangement__np1_length", curie=AK_SCHEMA.curie('rearrangement__np1_length'),
                   model_uri=AK_SCHEMA.rearrangement__np1_length, domain=None, range=Optional[int])

slots.rearrangement__np2_length = Slot(uri=AK_SCHEMA.rearrangement__np2_length, name="rearrangement__np2_length", curie=AK_SCHEMA.curie('rearrangement__np2_length'),
                   model_uri=AK_SCHEMA.rearrangement__np2_length, domain=None, range=Optional[int])

slots.rearrangement__np3_length = Slot(uri=AK_SCHEMA.rearrangement__np3_length, name="rearrangement__np3_length", curie=AK_SCHEMA.curie('rearrangement__np3_length'),
                   model_uri=AK_SCHEMA.rearrangement__np3_length, domain=None, range=Optional[int])

slots.rearrangement__n1_length = Slot(uri=AK_SCHEMA.rearrangement__n1_length, name="rearrangement__n1_length", curie=AK_SCHEMA.curie('rearrangement__n1_length'),
                   model_uri=AK_SCHEMA.rearrangement__n1_length, domain=None, range=Optional[int])

slots.rearrangement__n2_length = Slot(uri=AK_SCHEMA.rearrangement__n2_length, name="rearrangement__n2_length", curie=AK_SCHEMA.curie('rearrangement__n2_length'),
                   model_uri=AK_SCHEMA.rearrangement__n2_length, domain=None, range=Optional[int])

slots.rearrangement__n3_length = Slot(uri=AK_SCHEMA.rearrangement__n3_length, name="rearrangement__n3_length", curie=AK_SCHEMA.curie('rearrangement__n3_length'),
                   model_uri=AK_SCHEMA.rearrangement__n3_length, domain=None, range=Optional[int])

slots.rearrangement__p3v_length = Slot(uri=AK_SCHEMA.rearrangement__p3v_length, name="rearrangement__p3v_length", curie=AK_SCHEMA.curie('rearrangement__p3v_length'),
                   model_uri=AK_SCHEMA.rearrangement__p3v_length, domain=None, range=Optional[int])

slots.rearrangement__p5d_length = Slot(uri=AK_SCHEMA.rearrangement__p5d_length, name="rearrangement__p5d_length", curie=AK_SCHEMA.curie('rearrangement__p5d_length'),
                   model_uri=AK_SCHEMA.rearrangement__p5d_length, domain=None, range=Optional[int])

slots.rearrangement__p3d_length = Slot(uri=AK_SCHEMA.rearrangement__p3d_length, name="rearrangement__p3d_length", curie=AK_SCHEMA.curie('rearrangement__p3d_length'),
                   model_uri=AK_SCHEMA.rearrangement__p3d_length, domain=None, range=Optional[int])

slots.rearrangement__p5d2_length = Slot(uri=AK_SCHEMA.rearrangement__p5d2_length, name="rearrangement__p5d2_length", curie=AK_SCHEMA.curie('rearrangement__p5d2_length'),
                   model_uri=AK_SCHEMA.rearrangement__p5d2_length, domain=None, range=Optional[int])

slots.rearrangement__p3d2_length = Slot(uri=AK_SCHEMA.rearrangement__p3d2_length, name="rearrangement__p3d2_length", curie=AK_SCHEMA.curie('rearrangement__p3d2_length'),
                   model_uri=AK_SCHEMA.rearrangement__p3d2_length, domain=None, range=Optional[int])

slots.rearrangement__p5j_length = Slot(uri=AK_SCHEMA.rearrangement__p5j_length, name="rearrangement__p5j_length", curie=AK_SCHEMA.curie('rearrangement__p5j_length'),
                   model_uri=AK_SCHEMA.rearrangement__p5j_length, domain=None, range=Optional[int])

slots.rearrangement__v_frameshift = Slot(uri=AK_SCHEMA.rearrangement__v_frameshift, name="rearrangement__v_frameshift", curie=AK_SCHEMA.curie('rearrangement__v_frameshift'),
                   model_uri=AK_SCHEMA.rearrangement__v_frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.rearrangement__j_frameshift = Slot(uri=AK_SCHEMA.rearrangement__j_frameshift, name="rearrangement__j_frameshift", curie=AK_SCHEMA.curie('rearrangement__j_frameshift'),
                   model_uri=AK_SCHEMA.rearrangement__j_frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.rearrangement__d_frame = Slot(uri=AK_SCHEMA.rearrangement__d_frame, name="rearrangement__d_frame", curie=AK_SCHEMA.curie('rearrangement__d_frame'),
                   model_uri=AK_SCHEMA.rearrangement__d_frame, domain=None, range=Optional[int])

slots.rearrangement__d2_frame = Slot(uri=AK_SCHEMA.rearrangement__d2_frame, name="rearrangement__d2_frame", curie=AK_SCHEMA.curie('rearrangement__d2_frame'),
                   model_uri=AK_SCHEMA.rearrangement__d2_frame, domain=None, range=Optional[int])

slots.rearrangement__consensus_count = Slot(uri=AK_SCHEMA.rearrangement__consensus_count, name="rearrangement__consensus_count", curie=AK_SCHEMA.curie('rearrangement__consensus_count'),
                   model_uri=AK_SCHEMA.rearrangement__consensus_count, domain=None, range=Optional[int])

slots.rearrangement__duplicate_count = Slot(uri=AK_SCHEMA.rearrangement__duplicate_count, name="rearrangement__duplicate_count", curie=AK_SCHEMA.curie('rearrangement__duplicate_count'),
                   model_uri=AK_SCHEMA.rearrangement__duplicate_count, domain=None, range=Optional[int])

slots.rearrangement__umi_count = Slot(uri=AK_SCHEMA.rearrangement__umi_count, name="rearrangement__umi_count", curie=AK_SCHEMA.curie('rearrangement__umi_count'),
                   model_uri=AK_SCHEMA.rearrangement__umi_count, domain=None, range=Optional[int])

slots.rearrangement__cell_id = Slot(uri=AK_SCHEMA.rearrangement__cell_id, name="rearrangement__cell_id", curie=AK_SCHEMA.curie('rearrangement__cell_id'),
                   model_uri=AK_SCHEMA.rearrangement__cell_id, domain=None, range=Optional[str])

slots.rearrangement__clone_id = Slot(uri=AK_SCHEMA.rearrangement__clone_id, name="rearrangement__clone_id", curie=AK_SCHEMA.curie('rearrangement__clone_id'),
                   model_uri=AK_SCHEMA.rearrangement__clone_id, domain=None, range=Optional[str])

slots.rearrangement__reactivity_id = Slot(uri=AK_SCHEMA.rearrangement__reactivity_id, name="rearrangement__reactivity_id", curie=AK_SCHEMA.curie('rearrangement__reactivity_id'),
                   model_uri=AK_SCHEMA.rearrangement__reactivity_id, domain=None, range=Optional[str])

slots.rearrangement__reactivity_ref = Slot(uri=AK_SCHEMA.rearrangement__reactivity_ref, name="rearrangement__reactivity_ref", curie=AK_SCHEMA.curie('rearrangement__reactivity_ref'),
                   model_uri=AK_SCHEMA.rearrangement__reactivity_ref, domain=None, range=Optional[str])

slots.rearrangement__repertoire_id = Slot(uri=AK_SCHEMA.rearrangement__repertoire_id, name="rearrangement__repertoire_id", curie=AK_SCHEMA.curie('rearrangement__repertoire_id'),
                   model_uri=AK_SCHEMA.rearrangement__repertoire_id, domain=None, range=Optional[str])

slots.rearrangement__sample_processing_id = Slot(uri=AK_SCHEMA.rearrangement__sample_processing_id, name="rearrangement__sample_processing_id", curie=AK_SCHEMA.curie('rearrangement__sample_processing_id'),
                   model_uri=AK_SCHEMA.rearrangement__sample_processing_id, domain=None, range=Optional[str])

slots.rearrangement__data_processing_id = Slot(uri=AK_SCHEMA.rearrangement__data_processing_id, name="rearrangement__data_processing_id", curie=AK_SCHEMA.curie('rearrangement__data_processing_id'),
                   model_uri=AK_SCHEMA.rearrangement__data_processing_id, domain=None, range=Optional[str])

slots.clone__clone_id = Slot(uri=AK_SCHEMA.clone__clone_id, name="clone__clone_id", curie=AK_SCHEMA.curie('clone__clone_id'),
                   model_uri=AK_SCHEMA.clone__clone_id, domain=None, range=str)

slots.clone__repertoire_id = Slot(uri=AK_SCHEMA.clone__repertoire_id, name="clone__repertoire_id", curie=AK_SCHEMA.curie('clone__repertoire_id'),
                   model_uri=AK_SCHEMA.clone__repertoire_id, domain=None, range=Optional[str])

slots.clone__data_processing_id = Slot(uri=AK_SCHEMA.clone__data_processing_id, name="clone__data_processing_id", curie=AK_SCHEMA.curie('clone__data_processing_id'),
                   model_uri=AK_SCHEMA.clone__data_processing_id, domain=None, range=Optional[str])

slots.clone__sequences = Slot(uri=AK_SCHEMA.clone__sequences, name="clone__sequences", curie=AK_SCHEMA.curie('clone__sequences'),
                   model_uri=AK_SCHEMA.clone__sequences, domain=None, range=Optional[Union[str, List[str]]])

slots.clone__v_call = Slot(uri=AK_SCHEMA.clone__v_call, name="clone__v_call", curie=AK_SCHEMA.curie('clone__v_call'),
                   model_uri=AK_SCHEMA.clone__v_call, domain=None, range=Optional[str])

slots.clone__d_call = Slot(uri=AK_SCHEMA.clone__d_call, name="clone__d_call", curie=AK_SCHEMA.curie('clone__d_call'),
                   model_uri=AK_SCHEMA.clone__d_call, domain=None, range=Optional[str])

slots.clone__j_call = Slot(uri=AK_SCHEMA.clone__j_call, name="clone__j_call", curie=AK_SCHEMA.curie('clone__j_call'),
                   model_uri=AK_SCHEMA.clone__j_call, domain=None, range=Optional[str])

slots.clone__junction = Slot(uri=AK_SCHEMA.clone__junction, name="clone__junction", curie=AK_SCHEMA.curie('clone__junction'),
                   model_uri=AK_SCHEMA.clone__junction, domain=None, range=Optional[str])

slots.clone__junction_aa = Slot(uri=AK_SCHEMA.clone__junction_aa, name="clone__junction_aa", curie=AK_SCHEMA.curie('clone__junction_aa'),
                   model_uri=AK_SCHEMA.clone__junction_aa, domain=None, range=Optional[str])

slots.clone__junction_length = Slot(uri=AK_SCHEMA.clone__junction_length, name="clone__junction_length", curie=AK_SCHEMA.curie('clone__junction_length'),
                   model_uri=AK_SCHEMA.clone__junction_length, domain=None, range=Optional[int])

slots.clone__junction_aa_length = Slot(uri=AK_SCHEMA.clone__junction_aa_length, name="clone__junction_aa_length", curie=AK_SCHEMA.curie('clone__junction_aa_length'),
                   model_uri=AK_SCHEMA.clone__junction_aa_length, domain=None, range=Optional[int])

slots.clone__germline_alignment = Slot(uri=AK_SCHEMA.clone__germline_alignment, name="clone__germline_alignment", curie=AK_SCHEMA.curie('clone__germline_alignment'),
                   model_uri=AK_SCHEMA.clone__germline_alignment, domain=None, range=str)

slots.clone__germline_alignment_aa = Slot(uri=AK_SCHEMA.clone__germline_alignment_aa, name="clone__germline_alignment_aa", curie=AK_SCHEMA.curie('clone__germline_alignment_aa'),
                   model_uri=AK_SCHEMA.clone__germline_alignment_aa, domain=None, range=Optional[str])

slots.clone__v_alignment_start = Slot(uri=AK_SCHEMA.clone__v_alignment_start, name="clone__v_alignment_start", curie=AK_SCHEMA.curie('clone__v_alignment_start'),
                   model_uri=AK_SCHEMA.clone__v_alignment_start, domain=None, range=Optional[int])

slots.clone__v_alignment_end = Slot(uri=AK_SCHEMA.clone__v_alignment_end, name="clone__v_alignment_end", curie=AK_SCHEMA.curie('clone__v_alignment_end'),
                   model_uri=AK_SCHEMA.clone__v_alignment_end, domain=None, range=Optional[int])

slots.clone__d_alignment_start = Slot(uri=AK_SCHEMA.clone__d_alignment_start, name="clone__d_alignment_start", curie=AK_SCHEMA.curie('clone__d_alignment_start'),
                   model_uri=AK_SCHEMA.clone__d_alignment_start, domain=None, range=Optional[int])

slots.clone__d_alignment_end = Slot(uri=AK_SCHEMA.clone__d_alignment_end, name="clone__d_alignment_end", curie=AK_SCHEMA.curie('clone__d_alignment_end'),
                   model_uri=AK_SCHEMA.clone__d_alignment_end, domain=None, range=Optional[int])

slots.clone__j_alignment_start = Slot(uri=AK_SCHEMA.clone__j_alignment_start, name="clone__j_alignment_start", curie=AK_SCHEMA.curie('clone__j_alignment_start'),
                   model_uri=AK_SCHEMA.clone__j_alignment_start, domain=None, range=Optional[int])

slots.clone__j_alignment_end = Slot(uri=AK_SCHEMA.clone__j_alignment_end, name="clone__j_alignment_end", curie=AK_SCHEMA.curie('clone__j_alignment_end'),
                   model_uri=AK_SCHEMA.clone__j_alignment_end, domain=None, range=Optional[int])

slots.clone__junction_start = Slot(uri=AK_SCHEMA.clone__junction_start, name="clone__junction_start", curie=AK_SCHEMA.curie('clone__junction_start'),
                   model_uri=AK_SCHEMA.clone__junction_start, domain=None, range=Optional[int])

slots.clone__junction_end = Slot(uri=AK_SCHEMA.clone__junction_end, name="clone__junction_end", curie=AK_SCHEMA.curie('clone__junction_end'),
                   model_uri=AK_SCHEMA.clone__junction_end, domain=None, range=Optional[int])

slots.clone__umi_count = Slot(uri=AK_SCHEMA.clone__umi_count, name="clone__umi_count", curie=AK_SCHEMA.curie('clone__umi_count'),
                   model_uri=AK_SCHEMA.clone__umi_count, domain=None, range=Optional[int])

slots.clone__clone_count = Slot(uri=AK_SCHEMA.clone__clone_count, name="clone__clone_count", curie=AK_SCHEMA.curie('clone__clone_count'),
                   model_uri=AK_SCHEMA.clone__clone_count, domain=None, range=Optional[int])

slots.clone__seed_id = Slot(uri=AK_SCHEMA.clone__seed_id, name="clone__seed_id", curie=AK_SCHEMA.curie('clone__seed_id'),
                   model_uri=AK_SCHEMA.clone__seed_id, domain=None, range=Optional[str])

slots.tree__tree_id = Slot(uri=AK_SCHEMA.tree__tree_id, name="tree__tree_id", curie=AK_SCHEMA.curie('tree__tree_id'),
                   model_uri=AK_SCHEMA.tree__tree_id, domain=None, range=str)

slots.tree__clone_id = Slot(uri=AK_SCHEMA.tree__clone_id, name="tree__clone_id", curie=AK_SCHEMA.curie('tree__clone_id'),
                   model_uri=AK_SCHEMA.tree__clone_id, domain=None, range=str)

slots.tree__newick = Slot(uri=AK_SCHEMA.tree__newick, name="tree__newick", curie=AK_SCHEMA.curie('tree__newick'),
                   model_uri=AK_SCHEMA.tree__newick, domain=None, range=str)

slots.tree__nodes = Slot(uri=AK_SCHEMA.tree__nodes, name="tree__nodes", curie=AK_SCHEMA.curie('tree__nodes'),
                   model_uri=AK_SCHEMA.tree__nodes, domain=None, range=Optional[str])

slots.node__sequence_id = Slot(uri=AK_SCHEMA.node__sequence_id, name="node__sequence_id", curie=AK_SCHEMA.curie('node__sequence_id'),
                   model_uri=AK_SCHEMA.node__sequence_id, domain=None, range=str)

slots.node__sequence_alignment = Slot(uri=AK_SCHEMA.node__sequence_alignment, name="node__sequence_alignment", curie=AK_SCHEMA.curie('node__sequence_alignment'),
                   model_uri=AK_SCHEMA.node__sequence_alignment, domain=None, range=Optional[str])

slots.node__junction = Slot(uri=AK_SCHEMA.node__junction, name="node__junction", curie=AK_SCHEMA.curie('node__junction'),
                   model_uri=AK_SCHEMA.node__junction, domain=None, range=Optional[str])

slots.node__junction_aa = Slot(uri=AK_SCHEMA.node__junction_aa, name="node__junction_aa", curie=AK_SCHEMA.curie('node__junction_aa'),
                   model_uri=AK_SCHEMA.node__junction_aa, domain=None, range=Optional[str])

slots.cell__cell_id = Slot(uri=AK_SCHEMA.cell__cell_id, name="cell__cell_id", curie=AK_SCHEMA.curie('cell__cell_id'),
                   model_uri=AK_SCHEMA.cell__cell_id, domain=None, range=str)

slots.cell__repertoire_id = Slot(uri=AK_SCHEMA.cell__repertoire_id, name="cell__repertoire_id", curie=AK_SCHEMA.curie('cell__repertoire_id'),
                   model_uri=AK_SCHEMA.cell__repertoire_id, domain=None, range=str)

slots.cell__data_processing_id = Slot(uri=AK_SCHEMA.cell__data_processing_id, name="cell__data_processing_id", curie=AK_SCHEMA.curie('cell__data_processing_id'),
                   model_uri=AK_SCHEMA.cell__data_processing_id, domain=None, range=Optional[str])

slots.cell__receptors = Slot(uri=AK_SCHEMA.cell__receptors, name="cell__receptors", curie=AK_SCHEMA.curie('cell__receptors'),
                   model_uri=AK_SCHEMA.cell__receptors, domain=None, range=Optional[Union[str, List[str]]])

slots.cell__cell_subset = Slot(uri=AK_SCHEMA.cell__cell_subset, name="cell__cell_subset", curie=AK_SCHEMA.curie('cell__cell_subset'),
                   model_uri=AK_SCHEMA.cell__cell_subset, domain=None, range=Optional[Union[str, "V1p4CellSubset"]])

slots.cell__cell_phenotype = Slot(uri=AK_SCHEMA.cell__cell_phenotype, name="cell__cell_phenotype", curie=AK_SCHEMA.curie('cell__cell_phenotype'),
                   model_uri=AK_SCHEMA.cell__cell_phenotype, domain=None, range=Optional[str])

slots.cell__cell_label = Slot(uri=AK_SCHEMA.cell__cell_label, name="cell__cell_label", curie=AK_SCHEMA.curie('cell__cell_label'),
                   model_uri=AK_SCHEMA.cell__cell_label, domain=None, range=Optional[str])

slots.cell__virtual_pairing = Slot(uri=AK_SCHEMA.cell__virtual_pairing, name="cell__virtual_pairing", curie=AK_SCHEMA.curie('cell__virtual_pairing'),
                   model_uri=AK_SCHEMA.cell__virtual_pairing, domain=None, range=Union[bool, Bool])

slots.expression__expression_id = Slot(uri=AK_SCHEMA.expression__expression_id, name="expression__expression_id", curie=AK_SCHEMA.curie('expression__expression_id'),
                   model_uri=AK_SCHEMA.expression__expression_id, domain=None, range=str)

slots.expression__cell_id = Slot(uri=AK_SCHEMA.expression__cell_id, name="expression__cell_id", curie=AK_SCHEMA.curie('expression__cell_id'),
                   model_uri=AK_SCHEMA.expression__cell_id, domain=None, range=str)

slots.expression__repertoire_id = Slot(uri=AK_SCHEMA.expression__repertoire_id, name="expression__repertoire_id", curie=AK_SCHEMA.curie('expression__repertoire_id'),
                   model_uri=AK_SCHEMA.expression__repertoire_id, domain=None, range=str)

slots.expression__data_processing_id = Slot(uri=AK_SCHEMA.expression__data_processing_id, name="expression__data_processing_id", curie=AK_SCHEMA.curie('expression__data_processing_id'),
                   model_uri=AK_SCHEMA.expression__data_processing_id, domain=None, range=str)

slots.expression__property_type = Slot(uri=AK_SCHEMA.expression__property_type, name="expression__property_type", curie=AK_SCHEMA.curie('expression__property_type'),
                   model_uri=AK_SCHEMA.expression__property_type, domain=None, range=str)

slots.expression__property = Slot(uri=AK_SCHEMA.expression__property, name="expression__property", curie=AK_SCHEMA.curie('expression__property'),
                   model_uri=AK_SCHEMA.expression__property, domain=None, range=Union[str, "V1p4Property"])

slots.expression__value = Slot(uri=AK_SCHEMA.expression__value, name="expression__value", curie=AK_SCHEMA.curie('expression__value'),
                   model_uri=AK_SCHEMA.expression__value, domain=None, range=float)

slots.receptor__receptor_id = Slot(uri=AK_SCHEMA.receptor__receptor_id, name="receptor__receptor_id", curie=AK_SCHEMA.curie('receptor__receptor_id'),
                   model_uri=AK_SCHEMA.receptor__receptor_id, domain=None, range=str)

slots.receptor__receptor_hash = Slot(uri=AK_SCHEMA.receptor__receptor_hash, name="receptor__receptor_hash", curie=AK_SCHEMA.curie('receptor__receptor_hash'),
                   model_uri=AK_SCHEMA.receptor__receptor_hash, domain=None, range=str)

slots.receptor__receptor_type = Slot(uri=AK_SCHEMA.receptor__receptor_type, name="receptor__receptor_type", curie=AK_SCHEMA.curie('receptor__receptor_type'),
                   model_uri=AK_SCHEMA.receptor__receptor_type, domain=None, range=Union[str, "V1p4ReceptorType"])

slots.receptor__receptor_variable_domain_1_aa = Slot(uri=AK_SCHEMA.receptor__receptor_variable_domain_1_aa, name="receptor__receptor_variable_domain_1_aa", curie=AK_SCHEMA.curie('receptor__receptor_variable_domain_1_aa'),
                   model_uri=AK_SCHEMA.receptor__receptor_variable_domain_1_aa, domain=None, range=str)

slots.receptor__receptor_variable_domain_1_locus = Slot(uri=AK_SCHEMA.receptor__receptor_variable_domain_1_locus, name="receptor__receptor_variable_domain_1_locus", curie=AK_SCHEMA.curie('receptor__receptor_variable_domain_1_locus'),
                   model_uri=AK_SCHEMA.receptor__receptor_variable_domain_1_locus, domain=None, range=Union[str, "V1p4ReceptorVariableDomain1Locus"])

slots.receptor__receptor_variable_domain_2_aa = Slot(uri=AK_SCHEMA.receptor__receptor_variable_domain_2_aa, name="receptor__receptor_variable_domain_2_aa", curie=AK_SCHEMA.curie('receptor__receptor_variable_domain_2_aa'),
                   model_uri=AK_SCHEMA.receptor__receptor_variable_domain_2_aa, domain=None, range=str)

slots.receptor__receptor_variable_domain_2_locus = Slot(uri=AK_SCHEMA.receptor__receptor_variable_domain_2_locus, name="receptor__receptor_variable_domain_2_locus", curie=AK_SCHEMA.curie('receptor__receptor_variable_domain_2_locus'),
                   model_uri=AK_SCHEMA.receptor__receptor_variable_domain_2_locus, domain=None, range=Union[str, "V1p4ReceptorVariableDomain2Locus"])

slots.receptor__receptor_ref = Slot(uri=AK_SCHEMA.receptor__receptor_ref, name="receptor__receptor_ref", curie=AK_SCHEMA.curie('receptor__receptor_ref'),
                   model_uri=AK_SCHEMA.receptor__receptor_ref, domain=None, range=Optional[Union[str, List[str]]])

slots.reactivity__reactivity_id = Slot(uri=AK_SCHEMA.reactivity__reactivity_id, name="reactivity__reactivity_id", curie=AK_SCHEMA.curie('reactivity__reactivity_id'),
                   model_uri=AK_SCHEMA.reactivity__reactivity_id, domain=None, range=str)

slots.reactivity__cell_id = Slot(uri=AK_SCHEMA.reactivity__cell_id, name="reactivity__cell_id", curie=AK_SCHEMA.curie('reactivity__cell_id'),
                   model_uri=AK_SCHEMA.reactivity__cell_id, domain=None, range=str)

slots.reactivity__repertoire_id = Slot(uri=AK_SCHEMA.reactivity__repertoire_id, name="reactivity__repertoire_id", curie=AK_SCHEMA.curie('reactivity__repertoire_id'),
                   model_uri=AK_SCHEMA.reactivity__repertoire_id, domain=None, range=Optional[str])

slots.reactivity__data_processing_id = Slot(uri=AK_SCHEMA.reactivity__data_processing_id, name="reactivity__data_processing_id", curie=AK_SCHEMA.curie('reactivity__data_processing_id'),
                   model_uri=AK_SCHEMA.reactivity__data_processing_id, domain=None, range=Optional[str])

slots.reactivity__ligand_type = Slot(uri=AK_SCHEMA.reactivity__ligand_type, name="reactivity__ligand_type", curie=AK_SCHEMA.curie('reactivity__ligand_type'),
                   model_uri=AK_SCHEMA.reactivity__ligand_type, domain=None, range=Union[str, "V1p4LigandType"])

slots.reactivity__antigen_type = Slot(uri=AK_SCHEMA.reactivity__antigen_type, name="reactivity__antigen_type", curie=AK_SCHEMA.curie('reactivity__antigen_type'),
                   model_uri=AK_SCHEMA.reactivity__antigen_type, domain=None, range=Union[str, "V1p4AntigenType"])

slots.reactivity__antigen = Slot(uri=AK_SCHEMA.reactivity__antigen, name="reactivity__antigen", curie=AK_SCHEMA.curie('reactivity__antigen'),
                   model_uri=AK_SCHEMA.reactivity__antigen, domain=None, range=Union[str, "V1p4Antigen"])

slots.reactivity__antigen_source_species = Slot(uri=AK_SCHEMA.reactivity__antigen_source_species, name="reactivity__antigen_source_species", curie=AK_SCHEMA.curie('reactivity__antigen_source_species'),
                   model_uri=AK_SCHEMA.reactivity__antigen_source_species, domain=None, range=Optional[Union[str, "V1p4AntigenSourceSpecies"]])

slots.reactivity__peptide_start = Slot(uri=AK_SCHEMA.reactivity__peptide_start, name="reactivity__peptide_start", curie=AK_SCHEMA.curie('reactivity__peptide_start'),
                   model_uri=AK_SCHEMA.reactivity__peptide_start, domain=None, range=Optional[int])

slots.reactivity__peptide_end = Slot(uri=AK_SCHEMA.reactivity__peptide_end, name="reactivity__peptide_end", curie=AK_SCHEMA.curie('reactivity__peptide_end'),
                   model_uri=AK_SCHEMA.reactivity__peptide_end, domain=None, range=Optional[int])

slots.reactivity__peptide_sequence_aa = Slot(uri=AK_SCHEMA.reactivity__peptide_sequence_aa, name="reactivity__peptide_sequence_aa", curie=AK_SCHEMA.curie('reactivity__peptide_sequence_aa'),
                   model_uri=AK_SCHEMA.reactivity__peptide_sequence_aa, domain=None, range=Optional[str])

slots.reactivity__mhc_class = Slot(uri=AK_SCHEMA.reactivity__mhc_class, name="reactivity__mhc_class", curie=AK_SCHEMA.curie('reactivity__mhc_class'),
                   model_uri=AK_SCHEMA.reactivity__mhc_class, domain=None, range=Optional[Union[str, "V1p4MhcClass"]])

slots.reactivity__mhc_gene_1 = Slot(uri=AK_SCHEMA.reactivity__mhc_gene_1, name="reactivity__mhc_gene_1", curie=AK_SCHEMA.curie('reactivity__mhc_gene_1'),
                   model_uri=AK_SCHEMA.reactivity__mhc_gene_1, domain=None, range=Optional[Union[str, "V1p4MhcGene1"]])

slots.reactivity__mhc_allele_1 = Slot(uri=AK_SCHEMA.reactivity__mhc_allele_1, name="reactivity__mhc_allele_1", curie=AK_SCHEMA.curie('reactivity__mhc_allele_1'),
                   model_uri=AK_SCHEMA.reactivity__mhc_allele_1, domain=None, range=Optional[str])

slots.reactivity__mhc_gene_2 = Slot(uri=AK_SCHEMA.reactivity__mhc_gene_2, name="reactivity__mhc_gene_2", curie=AK_SCHEMA.curie('reactivity__mhc_gene_2'),
                   model_uri=AK_SCHEMA.reactivity__mhc_gene_2, domain=None, range=Optional[Union[str, "V1p4MhcGene2"]])

slots.reactivity__mhc_allele_2 = Slot(uri=AK_SCHEMA.reactivity__mhc_allele_2, name="reactivity__mhc_allele_2", curie=AK_SCHEMA.curie('reactivity__mhc_allele_2'),
                   model_uri=AK_SCHEMA.reactivity__mhc_allele_2, domain=None, range=Optional[str])

slots.reactivity__reactivity_method = Slot(uri=AK_SCHEMA.reactivity__reactivity_method, name="reactivity__reactivity_method", curie=AK_SCHEMA.curie('reactivity__reactivity_method'),
                   model_uri=AK_SCHEMA.reactivity__reactivity_method, domain=None, range=str)

slots.reactivity__reactivity_readout = Slot(uri=AK_SCHEMA.reactivity__reactivity_readout, name="reactivity__reactivity_readout", curie=AK_SCHEMA.curie('reactivity__reactivity_readout'),
                   model_uri=AK_SCHEMA.reactivity__reactivity_readout, domain=None, range=str)

slots.reactivity__reactivity_value = Slot(uri=AK_SCHEMA.reactivity__reactivity_value, name="reactivity__reactivity_value", curie=AK_SCHEMA.curie('reactivity__reactivity_value'),
                   model_uri=AK_SCHEMA.reactivity__reactivity_value, domain=None, range=float)

slots.reactivity__reactivity_unit = Slot(uri=AK_SCHEMA.reactivity__reactivity_unit, name="reactivity__reactivity_unit", curie=AK_SCHEMA.curie('reactivity__reactivity_unit'),
                   model_uri=AK_SCHEMA.reactivity__reactivity_unit, domain=None, range=str)

slots.reactivity__reactivity_ref = Slot(uri=AK_SCHEMA.reactivity__reactivity_ref, name="reactivity__reactivity_ref", curie=AK_SCHEMA.curie('reactivity__reactivity_ref'),
                   model_uri=AK_SCHEMA.reactivity__reactivity_ref, domain=None, range=Optional[Union[str, List[str]]])

slots.sample_processing__sample_processing_id = Slot(uri=AK_SCHEMA.sample_processing__sample_processing_id, name="sample_processing__sample_processing_id", curie=AK_SCHEMA.curie('sample_processing__sample_processing_id'),
                   model_uri=AK_SCHEMA.sample_processing__sample_processing_id, domain=None, range=Optional[str])

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