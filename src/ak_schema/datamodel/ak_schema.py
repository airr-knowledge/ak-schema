# Auto generated from ak_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-11-26T14:07:23
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
class V1p5TimePoint(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5TimePoint"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5TimePoint"
    class_name: ClassVar[str] = "V1p5TimePoint"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5TimePoint

    V1p5TimePoint_label: Optional[str] = None
    V1p5TimePoint_value: Optional[float] = None
    V1p5TimePoint_unit: Optional[Union[str, "V1p5Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5TimePoint_label is not None and not isinstance(self.V1p5TimePoint_label, str):
            self.V1p5TimePoint_label = str(self.V1p5TimePoint_label)

        if self.V1p5TimePoint_value is not None and not isinstance(self.V1p5TimePoint_value, float):
            self.V1p5TimePoint_value = float(self.V1p5TimePoint_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Acknowledgement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Acknowledgement"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Acknowledgement"
    class_name: ClassVar[str] = "V1p5Acknowledgement"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Acknowledgement

    V1p5Acknowledgement_acknowledgement_id: str = None
    V1p5Acknowledgement_name: str = None
    V1p5Acknowledgement_institution_name: str = None
    V1p5Acknowledgement_orcid_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5Acknowledgement_acknowledgement_id):
            self.MissingRequiredField("V1p5Acknowledgement_acknowledgement_id")
        if not isinstance(self.V1p5Acknowledgement_acknowledgement_id, str):
            self.V1p5Acknowledgement_acknowledgement_id = str(self.V1p5Acknowledgement_acknowledgement_id)

        if self._is_empty(self.V1p5Acknowledgement_name):
            self.MissingRequiredField("V1p5Acknowledgement_name")
        if not isinstance(self.V1p5Acknowledgement_name, str):
            self.V1p5Acknowledgement_name = str(self.V1p5Acknowledgement_name)

        if self._is_empty(self.V1p5Acknowledgement_institution_name):
            self.MissingRequiredField("V1p5Acknowledgement_institution_name")
        if not isinstance(self.V1p5Acknowledgement_institution_name, str):
            self.V1p5Acknowledgement_institution_name = str(self.V1p5Acknowledgement_institution_name)

        if self.V1p5Acknowledgement_orcid_id is not None and not isinstance(self.V1p5Acknowledgement_orcid_id, str):
            self.V1p5Acknowledgement_orcid_id = str(self.V1p5Acknowledgement_orcid_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5RearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5RearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5RearrangedSequence"
    class_name: ClassVar[str] = "V1p5RearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5RearrangedSequence

    V1p5RearrangedSequence_sequence_id: str = None
    V1p5RearrangedSequence_sequence: str = None
    V1p5RearrangedSequence_derivation: Union[str, "V1p5Derivation"] = None
    V1p5RearrangedSequence_observation_type: Union[str, "V1p5ObservationType"] = None
    V1p5RearrangedSequence_repository_name: str = None
    V1p5RearrangedSequence_deposited_version: str = None
    V1p5RearrangedSequence_curation: Optional[str] = None
    V1p5RearrangedSequence_repository_ref: Optional[str] = None
    V1p5RearrangedSequence_sequence_start: Optional[int] = None
    V1p5RearrangedSequence_sequence_end: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5RearrangedSequence_sequence_id):
            self.MissingRequiredField("V1p5RearrangedSequence_sequence_id")
        if not isinstance(self.V1p5RearrangedSequence_sequence_id, str):
            self.V1p5RearrangedSequence_sequence_id = str(self.V1p5RearrangedSequence_sequence_id)

        if self._is_empty(self.V1p5RearrangedSequence_sequence):
            self.MissingRequiredField("V1p5RearrangedSequence_sequence")
        if not isinstance(self.V1p5RearrangedSequence_sequence, str):
            self.V1p5RearrangedSequence_sequence = str(self.V1p5RearrangedSequence_sequence)

        if self._is_empty(self.V1p5RearrangedSequence_derivation):
            self.MissingRequiredField("V1p5RearrangedSequence_derivation")
        if not isinstance(self.V1p5RearrangedSequence_derivation, V1p5Derivation):
            self.V1p5RearrangedSequence_derivation = V1p5Derivation(self.V1p5RearrangedSequence_derivation)

        if self._is_empty(self.V1p5RearrangedSequence_observation_type):
            self.MissingRequiredField("V1p5RearrangedSequence_observation_type")
        if not isinstance(self.V1p5RearrangedSequence_observation_type, V1p5ObservationType):
            self.V1p5RearrangedSequence_observation_type = V1p5ObservationType(self.V1p5RearrangedSequence_observation_type)

        if self._is_empty(self.V1p5RearrangedSequence_repository_name):
            self.MissingRequiredField("V1p5RearrangedSequence_repository_name")
        if not isinstance(self.V1p5RearrangedSequence_repository_name, str):
            self.V1p5RearrangedSequence_repository_name = str(self.V1p5RearrangedSequence_repository_name)

        if self._is_empty(self.V1p5RearrangedSequence_deposited_version):
            self.MissingRequiredField("V1p5RearrangedSequence_deposited_version")
        if not isinstance(self.V1p5RearrangedSequence_deposited_version, str):
            self.V1p5RearrangedSequence_deposited_version = str(self.V1p5RearrangedSequence_deposited_version)

        if self.V1p5RearrangedSequence_curation is not None and not isinstance(self.V1p5RearrangedSequence_curation, str):
            self.V1p5RearrangedSequence_curation = str(self.V1p5RearrangedSequence_curation)

        if self.V1p5RearrangedSequence_repository_ref is not None and not isinstance(self.V1p5RearrangedSequence_repository_ref, str):
            self.V1p5RearrangedSequence_repository_ref = str(self.V1p5RearrangedSequence_repository_ref)

        if self.V1p5RearrangedSequence_sequence_start is not None and not isinstance(self.V1p5RearrangedSequence_sequence_start, int):
            self.V1p5RearrangedSequence_sequence_start = int(self.V1p5RearrangedSequence_sequence_start)

        if self.V1p5RearrangedSequence_sequence_end is not None and not isinstance(self.V1p5RearrangedSequence_sequence_end, int):
            self.V1p5RearrangedSequence_sequence_end = int(self.V1p5RearrangedSequence_sequence_end)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5UnrearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5UnrearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5UnrearrangedSequence"
    class_name: ClassVar[str] = "V1p5UnrearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5UnrearrangedSequence

    V1p5UnrearrangedSequence_sequence_id: str = None
    V1p5UnrearrangedSequence_sequence: str = None
    V1p5UnrearrangedSequence_repository_name: str = None
    V1p5UnrearrangedSequence_gff_seqid: str = None
    V1p5UnrearrangedSequence_gff_start: int = None
    V1p5UnrearrangedSequence_gff_end: int = None
    V1p5UnrearrangedSequence_strand: Union[str, "V1p5Strand"] = None
    V1p5UnrearrangedSequence_curation: Optional[str] = None
    V1p5UnrearrangedSequence_repository_ref: Optional[str] = None
    V1p5UnrearrangedSequence_patch_no: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5UnrearrangedSequence_sequence_id):
            self.MissingRequiredField("V1p5UnrearrangedSequence_sequence_id")
        if not isinstance(self.V1p5UnrearrangedSequence_sequence_id, str):
            self.V1p5UnrearrangedSequence_sequence_id = str(self.V1p5UnrearrangedSequence_sequence_id)

        if self._is_empty(self.V1p5UnrearrangedSequence_sequence):
            self.MissingRequiredField("V1p5UnrearrangedSequence_sequence")
        if not isinstance(self.V1p5UnrearrangedSequence_sequence, str):
            self.V1p5UnrearrangedSequence_sequence = str(self.V1p5UnrearrangedSequence_sequence)

        if self._is_empty(self.V1p5UnrearrangedSequence_repository_name):
            self.MissingRequiredField("V1p5UnrearrangedSequence_repository_name")
        if not isinstance(self.V1p5UnrearrangedSequence_repository_name, str):
            self.V1p5UnrearrangedSequence_repository_name = str(self.V1p5UnrearrangedSequence_repository_name)

        if self._is_empty(self.V1p5UnrearrangedSequence_gff_seqid):
            self.MissingRequiredField("V1p5UnrearrangedSequence_gff_seqid")
        if not isinstance(self.V1p5UnrearrangedSequence_gff_seqid, str):
            self.V1p5UnrearrangedSequence_gff_seqid = str(self.V1p5UnrearrangedSequence_gff_seqid)

        if self._is_empty(self.V1p5UnrearrangedSequence_gff_start):
            self.MissingRequiredField("V1p5UnrearrangedSequence_gff_start")
        if not isinstance(self.V1p5UnrearrangedSequence_gff_start, int):
            self.V1p5UnrearrangedSequence_gff_start = int(self.V1p5UnrearrangedSequence_gff_start)

        if self._is_empty(self.V1p5UnrearrangedSequence_gff_end):
            self.MissingRequiredField("V1p5UnrearrangedSequence_gff_end")
        if not isinstance(self.V1p5UnrearrangedSequence_gff_end, int):
            self.V1p5UnrearrangedSequence_gff_end = int(self.V1p5UnrearrangedSequence_gff_end)

        if self._is_empty(self.V1p5UnrearrangedSequence_strand):
            self.MissingRequiredField("V1p5UnrearrangedSequence_strand")
        if not isinstance(self.V1p5UnrearrangedSequence_strand, V1p5Strand):
            self.V1p5UnrearrangedSequence_strand = V1p5Strand(self.V1p5UnrearrangedSequence_strand)

        if self.V1p5UnrearrangedSequence_curation is not None and not isinstance(self.V1p5UnrearrangedSequence_curation, str):
            self.V1p5UnrearrangedSequence_curation = str(self.V1p5UnrearrangedSequence_curation)

        if self.V1p5UnrearrangedSequence_repository_ref is not None and not isinstance(self.V1p5UnrearrangedSequence_repository_ref, str):
            self.V1p5UnrearrangedSequence_repository_ref = str(self.V1p5UnrearrangedSequence_repository_ref)

        if self.V1p5UnrearrangedSequence_patch_no is not None and not isinstance(self.V1p5UnrearrangedSequence_patch_no, str):
            self.V1p5UnrearrangedSequence_patch_no = str(self.V1p5UnrearrangedSequence_patch_no)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5SequenceDelineationV(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5SequenceDelineationV"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5SequenceDelineationV"
    class_name: ClassVar[str] = "V1p5SequenceDelineationV"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5SequenceDelineationV

    V1p5SequenceDelineationV_sequence_delineation_id: str = None
    V1p5SequenceDelineationV_delineation_scheme: str = None
    V1p5SequenceDelineationV_fwr1_start: int = None
    V1p5SequenceDelineationV_fwr1_end: int = None
    V1p5SequenceDelineationV_cdr1_start: int = None
    V1p5SequenceDelineationV_cdr1_end: int = None
    V1p5SequenceDelineationV_fwr2_start: int = None
    V1p5SequenceDelineationV_fwr2_end: int = None
    V1p5SequenceDelineationV_cdr2_start: int = None
    V1p5SequenceDelineationV_cdr2_end: int = None
    V1p5SequenceDelineationV_fwr3_start: int = None
    V1p5SequenceDelineationV_fwr3_end: int = None
    V1p5SequenceDelineationV_cdr3_start: int = None
    V1p5SequenceDelineationV_unaligned_sequence: Optional[str] = None
    V1p5SequenceDelineationV_aligned_sequence: Optional[str] = None
    V1p5SequenceDelineationV_alignment_labels: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5SequenceDelineationV_sequence_delineation_id):
            self.MissingRequiredField("V1p5SequenceDelineationV_sequence_delineation_id")
        if not isinstance(self.V1p5SequenceDelineationV_sequence_delineation_id, str):
            self.V1p5SequenceDelineationV_sequence_delineation_id = str(self.V1p5SequenceDelineationV_sequence_delineation_id)

        if self._is_empty(self.V1p5SequenceDelineationV_delineation_scheme):
            self.MissingRequiredField("V1p5SequenceDelineationV_delineation_scheme")
        if not isinstance(self.V1p5SequenceDelineationV_delineation_scheme, str):
            self.V1p5SequenceDelineationV_delineation_scheme = str(self.V1p5SequenceDelineationV_delineation_scheme)

        if self._is_empty(self.V1p5SequenceDelineationV_fwr1_start):
            self.MissingRequiredField("V1p5SequenceDelineationV_fwr1_start")
        if not isinstance(self.V1p5SequenceDelineationV_fwr1_start, int):
            self.V1p5SequenceDelineationV_fwr1_start = int(self.V1p5SequenceDelineationV_fwr1_start)

        if self._is_empty(self.V1p5SequenceDelineationV_fwr1_end):
            self.MissingRequiredField("V1p5SequenceDelineationV_fwr1_end")
        if not isinstance(self.V1p5SequenceDelineationV_fwr1_end, int):
            self.V1p5SequenceDelineationV_fwr1_end = int(self.V1p5SequenceDelineationV_fwr1_end)

        if self._is_empty(self.V1p5SequenceDelineationV_cdr1_start):
            self.MissingRequiredField("V1p5SequenceDelineationV_cdr1_start")
        if not isinstance(self.V1p5SequenceDelineationV_cdr1_start, int):
            self.V1p5SequenceDelineationV_cdr1_start = int(self.V1p5SequenceDelineationV_cdr1_start)

        if self._is_empty(self.V1p5SequenceDelineationV_cdr1_end):
            self.MissingRequiredField("V1p5SequenceDelineationV_cdr1_end")
        if not isinstance(self.V1p5SequenceDelineationV_cdr1_end, int):
            self.V1p5SequenceDelineationV_cdr1_end = int(self.V1p5SequenceDelineationV_cdr1_end)

        if self._is_empty(self.V1p5SequenceDelineationV_fwr2_start):
            self.MissingRequiredField("V1p5SequenceDelineationV_fwr2_start")
        if not isinstance(self.V1p5SequenceDelineationV_fwr2_start, int):
            self.V1p5SequenceDelineationV_fwr2_start = int(self.V1p5SequenceDelineationV_fwr2_start)

        if self._is_empty(self.V1p5SequenceDelineationV_fwr2_end):
            self.MissingRequiredField("V1p5SequenceDelineationV_fwr2_end")
        if not isinstance(self.V1p5SequenceDelineationV_fwr2_end, int):
            self.V1p5SequenceDelineationV_fwr2_end = int(self.V1p5SequenceDelineationV_fwr2_end)

        if self._is_empty(self.V1p5SequenceDelineationV_cdr2_start):
            self.MissingRequiredField("V1p5SequenceDelineationV_cdr2_start")
        if not isinstance(self.V1p5SequenceDelineationV_cdr2_start, int):
            self.V1p5SequenceDelineationV_cdr2_start = int(self.V1p5SequenceDelineationV_cdr2_start)

        if self._is_empty(self.V1p5SequenceDelineationV_cdr2_end):
            self.MissingRequiredField("V1p5SequenceDelineationV_cdr2_end")
        if not isinstance(self.V1p5SequenceDelineationV_cdr2_end, int):
            self.V1p5SequenceDelineationV_cdr2_end = int(self.V1p5SequenceDelineationV_cdr2_end)

        if self._is_empty(self.V1p5SequenceDelineationV_fwr3_start):
            self.MissingRequiredField("V1p5SequenceDelineationV_fwr3_start")
        if not isinstance(self.V1p5SequenceDelineationV_fwr3_start, int):
            self.V1p5SequenceDelineationV_fwr3_start = int(self.V1p5SequenceDelineationV_fwr3_start)

        if self._is_empty(self.V1p5SequenceDelineationV_fwr3_end):
            self.MissingRequiredField("V1p5SequenceDelineationV_fwr3_end")
        if not isinstance(self.V1p5SequenceDelineationV_fwr3_end, int):
            self.V1p5SequenceDelineationV_fwr3_end = int(self.V1p5SequenceDelineationV_fwr3_end)

        if self._is_empty(self.V1p5SequenceDelineationV_cdr3_start):
            self.MissingRequiredField("V1p5SequenceDelineationV_cdr3_start")
        if not isinstance(self.V1p5SequenceDelineationV_cdr3_start, int):
            self.V1p5SequenceDelineationV_cdr3_start = int(self.V1p5SequenceDelineationV_cdr3_start)

        if self.V1p5SequenceDelineationV_unaligned_sequence is not None and not isinstance(self.V1p5SequenceDelineationV_unaligned_sequence, str):
            self.V1p5SequenceDelineationV_unaligned_sequence = str(self.V1p5SequenceDelineationV_unaligned_sequence)

        if self.V1p5SequenceDelineationV_aligned_sequence is not None and not isinstance(self.V1p5SequenceDelineationV_aligned_sequence, str):
            self.V1p5SequenceDelineationV_aligned_sequence = str(self.V1p5SequenceDelineationV_aligned_sequence)

        if not isinstance(self.V1p5SequenceDelineationV_alignment_labels, list):
            self.V1p5SequenceDelineationV_alignment_labels = [self.V1p5SequenceDelineationV_alignment_labels] if self.V1p5SequenceDelineationV_alignment_labels is not None else []
        self.V1p5SequenceDelineationV_alignment_labels = [v if isinstance(v, str) else str(v) for v in self.V1p5SequenceDelineationV_alignment_labels]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5AlleleDescription(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5AlleleDescription"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5AlleleDescription"
    class_name: ClassVar[str] = "V1p5AlleleDescription"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5AlleleDescription

    V1p5AlleleDescription_allele_description_id: str = None
    V1p5AlleleDescription_maintainer: str = None
    V1p5AlleleDescription_lab_address: str = None
    V1p5AlleleDescription_release_version: int = None
    V1p5AlleleDescription_release_date: str = None
    V1p5AlleleDescription_release_description: str = None
    V1p5AlleleDescription_sequence: str = None
    V1p5AlleleDescription_coding_sequence: str = None
    V1p5AlleleDescription_locus: Union[str, "V1p5Locus"] = None
    V1p5AlleleDescription_sequence_type: Union[str, "V1p5SequenceType"] = None
    V1p5AlleleDescription_functional: Union[bool, Bool] = None
    V1p5AlleleDescription_inference_type: Union[str, "V1p5InferenceType"] = None
    V1p5AlleleDescription_species: Union[str, "V1p5Species"] = None
    V1p5AlleleDescription_allele_description_ref: Optional[str] = None
    V1p5AlleleDescription_acknowledgements: Optional[Union[Union[dict, V1p5Acknowledgement], List[Union[dict, V1p5Acknowledgement]]]] = empty_list()
    V1p5AlleleDescription_label: Optional[str] = None
    V1p5AlleleDescription_aliases: Optional[Union[str, List[str]]] = empty_list()
    V1p5AlleleDescription_chromosome: Optional[int] = None
    V1p5AlleleDescription_species_subgroup: Optional[str] = None
    V1p5AlleleDescription_species_subgroup_type: Optional[Union[str, "V1p5SpeciesSubgroupType"]] = None
    V1p5AlleleDescription_status: Optional[Union[str, "V1p5Status"]] = None
    V1p5AlleleDescription_subgroup_designation: Optional[str] = None
    V1p5AlleleDescription_gene_designation: Optional[str] = None
    V1p5AlleleDescription_allele_designation: Optional[str] = None
    V1p5AlleleDescription_allele_similarity_cluster_designation: Optional[str] = None
    V1p5AlleleDescription_allele_similarity_cluster_member_id: Optional[str] = None
    V1p5AlleleDescription_j_codon_frame: Optional[Union[str, "V1p5JCodonFrame"]] = None
    V1p5AlleleDescription_gene_start: Optional[int] = None
    V1p5AlleleDescription_gene_end: Optional[int] = None
    V1p5AlleleDescription_utr_5_prime_start: Optional[int] = None
    V1p5AlleleDescription_utr_5_prime_end: Optional[int] = None
    V1p5AlleleDescription_leader_1_start: Optional[int] = None
    V1p5AlleleDescription_leader_1_end: Optional[int] = None
    V1p5AlleleDescription_leader_2_start: Optional[int] = None
    V1p5AlleleDescription_leader_2_end: Optional[int] = None
    V1p5AlleleDescription_v_rs_start: Optional[int] = None
    V1p5AlleleDescription_v_rs_end: Optional[int] = None
    V1p5AlleleDescription_d_rs_3_prime_start: Optional[int] = None
    V1p5AlleleDescription_d_rs_3_prime_end: Optional[int] = None
    V1p5AlleleDescription_d_rs_5_prime_start: Optional[int] = None
    V1p5AlleleDescription_d_rs_5_prime_end: Optional[int] = None
    V1p5AlleleDescription_j_cdr3_end: Optional[int] = None
    V1p5AlleleDescription_j_rs_start: Optional[int] = None
    V1p5AlleleDescription_j_rs_end: Optional[int] = None
    V1p5AlleleDescription_j_donor_splice: Optional[int] = None
    V1p5AlleleDescription_v_gene_delineations: Optional[Union[Union[dict, V1p5SequenceDelineationV], List[Union[dict, V1p5SequenceDelineationV]]]] = empty_list()
    V1p5AlleleDescription_unrearranged_support: Optional[Union[Union[dict, V1p5UnrearrangedSequence], List[Union[dict, V1p5UnrearrangedSequence]]]] = empty_list()
    V1p5AlleleDescription_rearranged_support: Optional[Union[Union[dict, V1p5RearrangedSequence], List[Union[dict, V1p5RearrangedSequence]]]] = empty_list()
    V1p5AlleleDescription_paralogs: Optional[Union[str, List[str]]] = empty_list()
    V1p5AlleleDescription_curation: Optional[str] = None
    V1p5AlleleDescription_curational_tags: Optional[Union[Union[str, "V1p5CurationalTags"], List[Union[str, "V1p5CurationalTags"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5AlleleDescription_allele_description_id):
            self.MissingRequiredField("V1p5AlleleDescription_allele_description_id")
        if not isinstance(self.V1p5AlleleDescription_allele_description_id, str):
            self.V1p5AlleleDescription_allele_description_id = str(self.V1p5AlleleDescription_allele_description_id)

        if self._is_empty(self.V1p5AlleleDescription_maintainer):
            self.MissingRequiredField("V1p5AlleleDescription_maintainer")
        if not isinstance(self.V1p5AlleleDescription_maintainer, str):
            self.V1p5AlleleDescription_maintainer = str(self.V1p5AlleleDescription_maintainer)

        if self._is_empty(self.V1p5AlleleDescription_lab_address):
            self.MissingRequiredField("V1p5AlleleDescription_lab_address")
        if not isinstance(self.V1p5AlleleDescription_lab_address, str):
            self.V1p5AlleleDescription_lab_address = str(self.V1p5AlleleDescription_lab_address)

        if self._is_empty(self.V1p5AlleleDescription_release_version):
            self.MissingRequiredField("V1p5AlleleDescription_release_version")
        if not isinstance(self.V1p5AlleleDescription_release_version, int):
            self.V1p5AlleleDescription_release_version = int(self.V1p5AlleleDescription_release_version)

        if self._is_empty(self.V1p5AlleleDescription_release_date):
            self.MissingRequiredField("V1p5AlleleDescription_release_date")
        if not isinstance(self.V1p5AlleleDescription_release_date, str):
            self.V1p5AlleleDescription_release_date = str(self.V1p5AlleleDescription_release_date)

        if self._is_empty(self.V1p5AlleleDescription_release_description):
            self.MissingRequiredField("V1p5AlleleDescription_release_description")
        if not isinstance(self.V1p5AlleleDescription_release_description, str):
            self.V1p5AlleleDescription_release_description = str(self.V1p5AlleleDescription_release_description)

        if self._is_empty(self.V1p5AlleleDescription_sequence):
            self.MissingRequiredField("V1p5AlleleDescription_sequence")
        if not isinstance(self.V1p5AlleleDescription_sequence, str):
            self.V1p5AlleleDescription_sequence = str(self.V1p5AlleleDescription_sequence)

        if self._is_empty(self.V1p5AlleleDescription_coding_sequence):
            self.MissingRequiredField("V1p5AlleleDescription_coding_sequence")
        if not isinstance(self.V1p5AlleleDescription_coding_sequence, str):
            self.V1p5AlleleDescription_coding_sequence = str(self.V1p5AlleleDescription_coding_sequence)

        if self._is_empty(self.V1p5AlleleDescription_locus):
            self.MissingRequiredField("V1p5AlleleDescription_locus")
        if not isinstance(self.V1p5AlleleDescription_locus, V1p5Locus):
            self.V1p5AlleleDescription_locus = V1p5Locus(self.V1p5AlleleDescription_locus)

        if self._is_empty(self.V1p5AlleleDescription_sequence_type):
            self.MissingRequiredField("V1p5AlleleDescription_sequence_type")
        if not isinstance(self.V1p5AlleleDescription_sequence_type, V1p5SequenceType):
            self.V1p5AlleleDescription_sequence_type = V1p5SequenceType(self.V1p5AlleleDescription_sequence_type)

        if self._is_empty(self.V1p5AlleleDescription_functional):
            self.MissingRequiredField("V1p5AlleleDescription_functional")
        if not isinstance(self.V1p5AlleleDescription_functional, Bool):
            self.V1p5AlleleDescription_functional = Bool(self.V1p5AlleleDescription_functional)

        if self._is_empty(self.V1p5AlleleDescription_inference_type):
            self.MissingRequiredField("V1p5AlleleDescription_inference_type")
        if not isinstance(self.V1p5AlleleDescription_inference_type, V1p5InferenceType):
            self.V1p5AlleleDescription_inference_type = V1p5InferenceType(self.V1p5AlleleDescription_inference_type)

        if self.V1p5AlleleDescription_allele_description_ref is not None and not isinstance(self.V1p5AlleleDescription_allele_description_ref, str):
            self.V1p5AlleleDescription_allele_description_ref = str(self.V1p5AlleleDescription_allele_description_ref)

        self._normalize_inlined_as_dict(slot_name="V1p5AlleleDescription_acknowledgements", slot_type=V1p5Acknowledgement, key_name="V1p5Acknowledgement_acknowledgement_id", keyed=False)

        if self.V1p5AlleleDescription_label is not None and not isinstance(self.V1p5AlleleDescription_label, str):
            self.V1p5AlleleDescription_label = str(self.V1p5AlleleDescription_label)

        if not isinstance(self.V1p5AlleleDescription_aliases, list):
            self.V1p5AlleleDescription_aliases = [self.V1p5AlleleDescription_aliases] if self.V1p5AlleleDescription_aliases is not None else []
        self.V1p5AlleleDescription_aliases = [v if isinstance(v, str) else str(v) for v in self.V1p5AlleleDescription_aliases]

        if self.V1p5AlleleDescription_chromosome is not None and not isinstance(self.V1p5AlleleDescription_chromosome, int):
            self.V1p5AlleleDescription_chromosome = int(self.V1p5AlleleDescription_chromosome)

        if self.V1p5AlleleDescription_species_subgroup is not None and not isinstance(self.V1p5AlleleDescription_species_subgroup, str):
            self.V1p5AlleleDescription_species_subgroup = str(self.V1p5AlleleDescription_species_subgroup)

        if self.V1p5AlleleDescription_species_subgroup_type is not None and not isinstance(self.V1p5AlleleDescription_species_subgroup_type, V1p5SpeciesSubgroupType):
            self.V1p5AlleleDescription_species_subgroup_type = V1p5SpeciesSubgroupType(self.V1p5AlleleDescription_species_subgroup_type)

        if self.V1p5AlleleDescription_status is not None and not isinstance(self.V1p5AlleleDescription_status, V1p5Status):
            self.V1p5AlleleDescription_status = V1p5Status(self.V1p5AlleleDescription_status)

        if self.V1p5AlleleDescription_subgroup_designation is not None and not isinstance(self.V1p5AlleleDescription_subgroup_designation, str):
            self.V1p5AlleleDescription_subgroup_designation = str(self.V1p5AlleleDescription_subgroup_designation)

        if self.V1p5AlleleDescription_gene_designation is not None and not isinstance(self.V1p5AlleleDescription_gene_designation, str):
            self.V1p5AlleleDescription_gene_designation = str(self.V1p5AlleleDescription_gene_designation)

        if self.V1p5AlleleDescription_allele_designation is not None and not isinstance(self.V1p5AlleleDescription_allele_designation, str):
            self.V1p5AlleleDescription_allele_designation = str(self.V1p5AlleleDescription_allele_designation)

        if self.V1p5AlleleDescription_allele_similarity_cluster_designation is not None and not isinstance(self.V1p5AlleleDescription_allele_similarity_cluster_designation, str):
            self.V1p5AlleleDescription_allele_similarity_cluster_designation = str(self.V1p5AlleleDescription_allele_similarity_cluster_designation)

        if self.V1p5AlleleDescription_allele_similarity_cluster_member_id is not None and not isinstance(self.V1p5AlleleDescription_allele_similarity_cluster_member_id, str):
            self.V1p5AlleleDescription_allele_similarity_cluster_member_id = str(self.V1p5AlleleDescription_allele_similarity_cluster_member_id)

        if self.V1p5AlleleDescription_j_codon_frame is not None and not isinstance(self.V1p5AlleleDescription_j_codon_frame, V1p5JCodonFrame):
            self.V1p5AlleleDescription_j_codon_frame = V1p5JCodonFrame(self.V1p5AlleleDescription_j_codon_frame)

        if self.V1p5AlleleDescription_gene_start is not None and not isinstance(self.V1p5AlleleDescription_gene_start, int):
            self.V1p5AlleleDescription_gene_start = int(self.V1p5AlleleDescription_gene_start)

        if self.V1p5AlleleDescription_gene_end is not None and not isinstance(self.V1p5AlleleDescription_gene_end, int):
            self.V1p5AlleleDescription_gene_end = int(self.V1p5AlleleDescription_gene_end)

        if self.V1p5AlleleDescription_utr_5_prime_start is not None and not isinstance(self.V1p5AlleleDescription_utr_5_prime_start, int):
            self.V1p5AlleleDescription_utr_5_prime_start = int(self.V1p5AlleleDescription_utr_5_prime_start)

        if self.V1p5AlleleDescription_utr_5_prime_end is not None and not isinstance(self.V1p5AlleleDescription_utr_5_prime_end, int):
            self.V1p5AlleleDescription_utr_5_prime_end = int(self.V1p5AlleleDescription_utr_5_prime_end)

        if self.V1p5AlleleDescription_leader_1_start is not None and not isinstance(self.V1p5AlleleDescription_leader_1_start, int):
            self.V1p5AlleleDescription_leader_1_start = int(self.V1p5AlleleDescription_leader_1_start)

        if self.V1p5AlleleDescription_leader_1_end is not None and not isinstance(self.V1p5AlleleDescription_leader_1_end, int):
            self.V1p5AlleleDescription_leader_1_end = int(self.V1p5AlleleDescription_leader_1_end)

        if self.V1p5AlleleDescription_leader_2_start is not None and not isinstance(self.V1p5AlleleDescription_leader_2_start, int):
            self.V1p5AlleleDescription_leader_2_start = int(self.V1p5AlleleDescription_leader_2_start)

        if self.V1p5AlleleDescription_leader_2_end is not None and not isinstance(self.V1p5AlleleDescription_leader_2_end, int):
            self.V1p5AlleleDescription_leader_2_end = int(self.V1p5AlleleDescription_leader_2_end)

        if self.V1p5AlleleDescription_v_rs_start is not None and not isinstance(self.V1p5AlleleDescription_v_rs_start, int):
            self.V1p5AlleleDescription_v_rs_start = int(self.V1p5AlleleDescription_v_rs_start)

        if self.V1p5AlleleDescription_v_rs_end is not None and not isinstance(self.V1p5AlleleDescription_v_rs_end, int):
            self.V1p5AlleleDescription_v_rs_end = int(self.V1p5AlleleDescription_v_rs_end)

        if self.V1p5AlleleDescription_d_rs_3_prime_start is not None and not isinstance(self.V1p5AlleleDescription_d_rs_3_prime_start, int):
            self.V1p5AlleleDescription_d_rs_3_prime_start = int(self.V1p5AlleleDescription_d_rs_3_prime_start)

        if self.V1p5AlleleDescription_d_rs_3_prime_end is not None and not isinstance(self.V1p5AlleleDescription_d_rs_3_prime_end, int):
            self.V1p5AlleleDescription_d_rs_3_prime_end = int(self.V1p5AlleleDescription_d_rs_3_prime_end)

        if self.V1p5AlleleDescription_d_rs_5_prime_start is not None and not isinstance(self.V1p5AlleleDescription_d_rs_5_prime_start, int):
            self.V1p5AlleleDescription_d_rs_5_prime_start = int(self.V1p5AlleleDescription_d_rs_5_prime_start)

        if self.V1p5AlleleDescription_d_rs_5_prime_end is not None and not isinstance(self.V1p5AlleleDescription_d_rs_5_prime_end, int):
            self.V1p5AlleleDescription_d_rs_5_prime_end = int(self.V1p5AlleleDescription_d_rs_5_prime_end)

        if self.V1p5AlleleDescription_j_cdr3_end is not None and not isinstance(self.V1p5AlleleDescription_j_cdr3_end, int):
            self.V1p5AlleleDescription_j_cdr3_end = int(self.V1p5AlleleDescription_j_cdr3_end)

        if self.V1p5AlleleDescription_j_rs_start is not None and not isinstance(self.V1p5AlleleDescription_j_rs_start, int):
            self.V1p5AlleleDescription_j_rs_start = int(self.V1p5AlleleDescription_j_rs_start)

        if self.V1p5AlleleDescription_j_rs_end is not None and not isinstance(self.V1p5AlleleDescription_j_rs_end, int):
            self.V1p5AlleleDescription_j_rs_end = int(self.V1p5AlleleDescription_j_rs_end)

        if self.V1p5AlleleDescription_j_donor_splice is not None and not isinstance(self.V1p5AlleleDescription_j_donor_splice, int):
            self.V1p5AlleleDescription_j_donor_splice = int(self.V1p5AlleleDescription_j_donor_splice)

        self._normalize_inlined_as_dict(slot_name="V1p5AlleleDescription_v_gene_delineations", slot_type=V1p5SequenceDelineationV, key_name="V1p5SequenceDelineationV_sequence_delineation_id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="V1p5AlleleDescription_unrearranged_support", slot_type=V1p5UnrearrangedSequence, key_name="V1p5UnrearrangedSequence_sequence_id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="V1p5AlleleDescription_rearranged_support", slot_type=V1p5RearrangedSequence, key_name="V1p5RearrangedSequence_sequence_id", keyed=False)

        if not isinstance(self.V1p5AlleleDescription_paralogs, list):
            self.V1p5AlleleDescription_paralogs = [self.V1p5AlleleDescription_paralogs] if self.V1p5AlleleDescription_paralogs is not None else []
        self.V1p5AlleleDescription_paralogs = [v if isinstance(v, str) else str(v) for v in self.V1p5AlleleDescription_paralogs]

        if self.V1p5AlleleDescription_curation is not None and not isinstance(self.V1p5AlleleDescription_curation, str):
            self.V1p5AlleleDescription_curation = str(self.V1p5AlleleDescription_curation)

        if not isinstance(self.V1p5AlleleDescription_curational_tags, list):
            self.V1p5AlleleDescription_curational_tags = [self.V1p5AlleleDescription_curational_tags] if self.V1p5AlleleDescription_curational_tags is not None else []
        self.V1p5AlleleDescription_curational_tags = [v if isinstance(v, V1p5CurationalTags) else V1p5CurationalTags(v) for v in self.V1p5AlleleDescription_curational_tags]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5GermlineSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5GermlineSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5GermlineSet"
    class_name: ClassVar[str] = "V1p5GermlineSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5GermlineSet

    V1p5GermlineSet_germline_set_id: str = None
    V1p5GermlineSet_author: str = None
    V1p5GermlineSet_lab_name: str = None
    V1p5GermlineSet_lab_address: str = None
    V1p5GermlineSet_release_version: int = None
    V1p5GermlineSet_release_description: str = None
    V1p5GermlineSet_release_date: str = None
    V1p5GermlineSet_germline_set_name: str = None
    V1p5GermlineSet_germline_set_ref: str = None
    V1p5GermlineSet_species: Union[str, "V1p5Species"] = None
    V1p5GermlineSet_locus: Union[str, "V1p5Locus"] = None
    V1p5GermlineSet_allele_descriptions: Union[Union[dict, V1p5AlleleDescription], List[Union[dict, V1p5AlleleDescription]]] = None
    V1p5GermlineSet_acknowledgements: Optional[Union[Union[dict, V1p5Acknowledgement], List[Union[dict, V1p5Acknowledgement]]]] = empty_list()
    V1p5GermlineSet_pub_ids: Optional[str] = None
    V1p5GermlineSet_species_subgroup: Optional[str] = None
    V1p5GermlineSet_species_subgroup_type: Optional[Union[str, "V1p5SpeciesSubgroupType"]] = None
    V1p5GermlineSet_curation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5GermlineSet_germline_set_id):
            self.MissingRequiredField("V1p5GermlineSet_germline_set_id")
        if not isinstance(self.V1p5GermlineSet_germline_set_id, str):
            self.V1p5GermlineSet_germline_set_id = str(self.V1p5GermlineSet_germline_set_id)

        if self._is_empty(self.V1p5GermlineSet_author):
            self.MissingRequiredField("V1p5GermlineSet_author")
        if not isinstance(self.V1p5GermlineSet_author, str):
            self.V1p5GermlineSet_author = str(self.V1p5GermlineSet_author)

        if self._is_empty(self.V1p5GermlineSet_lab_name):
            self.MissingRequiredField("V1p5GermlineSet_lab_name")
        if not isinstance(self.V1p5GermlineSet_lab_name, str):
            self.V1p5GermlineSet_lab_name = str(self.V1p5GermlineSet_lab_name)

        if self._is_empty(self.V1p5GermlineSet_lab_address):
            self.MissingRequiredField("V1p5GermlineSet_lab_address")
        if not isinstance(self.V1p5GermlineSet_lab_address, str):
            self.V1p5GermlineSet_lab_address = str(self.V1p5GermlineSet_lab_address)

        if self._is_empty(self.V1p5GermlineSet_release_version):
            self.MissingRequiredField("V1p5GermlineSet_release_version")
        if not isinstance(self.V1p5GermlineSet_release_version, int):
            self.V1p5GermlineSet_release_version = int(self.V1p5GermlineSet_release_version)

        if self._is_empty(self.V1p5GermlineSet_release_description):
            self.MissingRequiredField("V1p5GermlineSet_release_description")
        if not isinstance(self.V1p5GermlineSet_release_description, str):
            self.V1p5GermlineSet_release_description = str(self.V1p5GermlineSet_release_description)

        if self._is_empty(self.V1p5GermlineSet_release_date):
            self.MissingRequiredField("V1p5GermlineSet_release_date")
        if not isinstance(self.V1p5GermlineSet_release_date, str):
            self.V1p5GermlineSet_release_date = str(self.V1p5GermlineSet_release_date)

        if self._is_empty(self.V1p5GermlineSet_germline_set_name):
            self.MissingRequiredField("V1p5GermlineSet_germline_set_name")
        if not isinstance(self.V1p5GermlineSet_germline_set_name, str):
            self.V1p5GermlineSet_germline_set_name = str(self.V1p5GermlineSet_germline_set_name)

        if self._is_empty(self.V1p5GermlineSet_germline_set_ref):
            self.MissingRequiredField("V1p5GermlineSet_germline_set_ref")
        if not isinstance(self.V1p5GermlineSet_germline_set_ref, str):
            self.V1p5GermlineSet_germline_set_ref = str(self.V1p5GermlineSet_germline_set_ref)

        if self._is_empty(self.V1p5GermlineSet_locus):
            self.MissingRequiredField("V1p5GermlineSet_locus")
        if not isinstance(self.V1p5GermlineSet_locus, V1p5Locus):
            self.V1p5GermlineSet_locus = V1p5Locus(self.V1p5GermlineSet_locus)

        if self._is_empty(self.V1p5GermlineSet_allele_descriptions):
            self.MissingRequiredField("V1p5GermlineSet_allele_descriptions")
        self._normalize_inlined_as_dict(slot_name="V1p5GermlineSet_allele_descriptions", slot_type=V1p5AlleleDescription, key_name="V1p5AlleleDescription_allele_description_id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="V1p5GermlineSet_acknowledgements", slot_type=V1p5Acknowledgement, key_name="V1p5Acknowledgement_acknowledgement_id", keyed=False)

        if self.V1p5GermlineSet_pub_ids is not None and not isinstance(self.V1p5GermlineSet_pub_ids, str):
            self.V1p5GermlineSet_pub_ids = str(self.V1p5GermlineSet_pub_ids)

        if self.V1p5GermlineSet_species_subgroup is not None and not isinstance(self.V1p5GermlineSet_species_subgroup, str):
            self.V1p5GermlineSet_species_subgroup = str(self.V1p5GermlineSet_species_subgroup)

        if self.V1p5GermlineSet_species_subgroup_type is not None and not isinstance(self.V1p5GermlineSet_species_subgroup_type, V1p5SpeciesSubgroupType):
            self.V1p5GermlineSet_species_subgroup_type = V1p5SpeciesSubgroupType(self.V1p5GermlineSet_species_subgroup_type)

        if self.V1p5GermlineSet_curation is not None and not isinstance(self.V1p5GermlineSet_curation, str):
            self.V1p5GermlineSet_curation = str(self.V1p5GermlineSet_curation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5GenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5GenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5GenotypeSet"
    class_name: ClassVar[str] = "V1p5GenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5GenotypeSet

    V1p5GenotypeSet_receptor_genotype_set_id: str = None
    V1p5GenotypeSet_genotype_class_list: Optional[Union[Union[dict, "V1p5Genotype"], List[Union[dict, "V1p5Genotype"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5GenotypeSet_receptor_genotype_set_id):
            self.MissingRequiredField("V1p5GenotypeSet_receptor_genotype_set_id")
        if not isinstance(self.V1p5GenotypeSet_receptor_genotype_set_id, str):
            self.V1p5GenotypeSet_receptor_genotype_set_id = str(self.V1p5GenotypeSet_receptor_genotype_set_id)

        self._normalize_inlined_as_dict(slot_name="V1p5GenotypeSet_genotype_class_list", slot_type=V1p5Genotype, key_name="V1p5Genotype_receptor_genotype_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Genotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Genotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Genotype"
    class_name: ClassVar[str] = "V1p5Genotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Genotype

    V1p5Genotype_receptor_genotype_id: str = None
    V1p5Genotype_locus: Union[str, "V1p5Locus"] = None
    V1p5Genotype_documented_alleles: Optional[Union[Union[dict, "V1p5DocumentedAllele"], List[Union[dict, "V1p5DocumentedAllele"]]]] = empty_list()
    V1p5Genotype_undocumented_alleles: Optional[Union[Union[dict, "V1p5UndocumentedAllele"], List[Union[dict, "V1p5UndocumentedAllele"]]]] = empty_list()
    V1p5Genotype_deleted_genes: Optional[Union[Union[dict, "V1p5DeletedGene"], List[Union[dict, "V1p5DeletedGene"]]]] = empty_list()
    V1p5Genotype_inference_process: Optional[Union[str, "V1p5InferenceProcess"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5Genotype_receptor_genotype_id):
            self.MissingRequiredField("V1p5Genotype_receptor_genotype_id")
        if not isinstance(self.V1p5Genotype_receptor_genotype_id, str):
            self.V1p5Genotype_receptor_genotype_id = str(self.V1p5Genotype_receptor_genotype_id)

        if self._is_empty(self.V1p5Genotype_locus):
            self.MissingRequiredField("V1p5Genotype_locus")
        if not isinstance(self.V1p5Genotype_locus, V1p5Locus):
            self.V1p5Genotype_locus = V1p5Locus(self.V1p5Genotype_locus)

        self._normalize_inlined_as_dict(slot_name="V1p5Genotype_documented_alleles", slot_type=V1p5DocumentedAllele, key_name="V1p5DocumentedAllele_label", keyed=False)

        self._normalize_inlined_as_dict(slot_name="V1p5Genotype_undocumented_alleles", slot_type=V1p5UndocumentedAllele, key_name="V1p5UndocumentedAllele_allele_name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="V1p5Genotype_deleted_genes", slot_type=V1p5DeletedGene, key_name="V1p5DeletedGene_label", keyed=False)

        if self.V1p5Genotype_inference_process is not None and not isinstance(self.V1p5Genotype_inference_process, V1p5InferenceProcess):
            self.V1p5Genotype_inference_process = V1p5InferenceProcess(self.V1p5Genotype_inference_process)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5DocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5DocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5DocumentedAllele"
    class_name: ClassVar[str] = "V1p5DocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5DocumentedAllele

    V1p5DocumentedAllele_label: str = None
    V1p5DocumentedAllele_germline_set_ref: str = None
    V1p5DocumentedAllele_phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5DocumentedAllele_label):
            self.MissingRequiredField("V1p5DocumentedAllele_label")
        if not isinstance(self.V1p5DocumentedAllele_label, str):
            self.V1p5DocumentedAllele_label = str(self.V1p5DocumentedAllele_label)

        if self._is_empty(self.V1p5DocumentedAllele_germline_set_ref):
            self.MissingRequiredField("V1p5DocumentedAllele_germline_set_ref")
        if not isinstance(self.V1p5DocumentedAllele_germline_set_ref, str):
            self.V1p5DocumentedAllele_germline_set_ref = str(self.V1p5DocumentedAllele_germline_set_ref)

        if self.V1p5DocumentedAllele_phasing is not None and not isinstance(self.V1p5DocumentedAllele_phasing, int):
            self.V1p5DocumentedAllele_phasing = int(self.V1p5DocumentedAllele_phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5UndocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5UndocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5UndocumentedAllele"
    class_name: ClassVar[str] = "V1p5UndocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5UndocumentedAllele

    V1p5UndocumentedAllele_allele_name: str = None
    V1p5UndocumentedAllele_sequence: str = None
    V1p5UndocumentedAllele_phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5UndocumentedAllele_allele_name):
            self.MissingRequiredField("V1p5UndocumentedAllele_allele_name")
        if not isinstance(self.V1p5UndocumentedAllele_allele_name, str):
            self.V1p5UndocumentedAllele_allele_name = str(self.V1p5UndocumentedAllele_allele_name)

        if self._is_empty(self.V1p5UndocumentedAllele_sequence):
            self.MissingRequiredField("V1p5UndocumentedAllele_sequence")
        if not isinstance(self.V1p5UndocumentedAllele_sequence, str):
            self.V1p5UndocumentedAllele_sequence = str(self.V1p5UndocumentedAllele_sequence)

        if self.V1p5UndocumentedAllele_phasing is not None and not isinstance(self.V1p5UndocumentedAllele_phasing, int):
            self.V1p5UndocumentedAllele_phasing = int(self.V1p5UndocumentedAllele_phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5DeletedGene(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5DeletedGene"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5DeletedGene"
    class_name: ClassVar[str] = "V1p5DeletedGene"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5DeletedGene

    V1p5DeletedGene_label: str = None
    V1p5DeletedGene_germline_set_ref: str = None
    V1p5DeletedGene_phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5DeletedGene_label):
            self.MissingRequiredField("V1p5DeletedGene_label")
        if not isinstance(self.V1p5DeletedGene_label, str):
            self.V1p5DeletedGene_label = str(self.V1p5DeletedGene_label)

        if self._is_empty(self.V1p5DeletedGene_germline_set_ref):
            self.MissingRequiredField("V1p5DeletedGene_germline_set_ref")
        if not isinstance(self.V1p5DeletedGene_germline_set_ref, str):
            self.V1p5DeletedGene_germline_set_ref = str(self.V1p5DeletedGene_germline_set_ref)

        if self.V1p5DeletedGene_phasing is not None and not isinstance(self.V1p5DeletedGene_phasing, int):
            self.V1p5DeletedGene_phasing = int(self.V1p5DeletedGene_phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5MHCGenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5MHCGenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5MHCGenotypeSet"
    class_name: ClassVar[str] = "V1p5MHCGenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5MHCGenotypeSet

    V1p5MHCGenotypeSet_mhc_genotype_set_id: str = None
    V1p5MHCGenotypeSet_mhc_genotype_list: Union[Union[dict, "V1p5MHCGenotype"], List[Union[dict, "V1p5MHCGenotype"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5MHCGenotypeSet_mhc_genotype_set_id):
            self.MissingRequiredField("V1p5MHCGenotypeSet_mhc_genotype_set_id")
        if not isinstance(self.V1p5MHCGenotypeSet_mhc_genotype_set_id, str):
            self.V1p5MHCGenotypeSet_mhc_genotype_set_id = str(self.V1p5MHCGenotypeSet_mhc_genotype_set_id)

        if self._is_empty(self.V1p5MHCGenotypeSet_mhc_genotype_list):
            self.MissingRequiredField("V1p5MHCGenotypeSet_mhc_genotype_list")
        self._normalize_inlined_as_dict(slot_name="V1p5MHCGenotypeSet_mhc_genotype_list", slot_type=V1p5MHCGenotype, key_name="V1p5MHCGenotype_mhc_genotype_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5MHCGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5MHCGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5MHCGenotype"
    class_name: ClassVar[str] = "V1p5MHCGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5MHCGenotype

    V1p5MHCGenotype_mhc_genotype_id: str = None
    V1p5MHCGenotype_mhc_class: Union[str, "V1p5MhcClass"] = None
    V1p5MHCGenotype_mhc_alleles: Union[Union[dict, "V1p5MHCAllele"], List[Union[dict, "V1p5MHCAllele"]]] = None
    V1p5MHCGenotype_mhc_genotyping_method: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5MHCGenotype_mhc_genotype_id):
            self.MissingRequiredField("V1p5MHCGenotype_mhc_genotype_id")
        if not isinstance(self.V1p5MHCGenotype_mhc_genotype_id, str):
            self.V1p5MHCGenotype_mhc_genotype_id = str(self.V1p5MHCGenotype_mhc_genotype_id)

        if self._is_empty(self.V1p5MHCGenotype_mhc_class):
            self.MissingRequiredField("V1p5MHCGenotype_mhc_class")
        if not isinstance(self.V1p5MHCGenotype_mhc_class, V1p5MhcClass):
            self.V1p5MHCGenotype_mhc_class = V1p5MhcClass(self.V1p5MHCGenotype_mhc_class)

        if self._is_empty(self.V1p5MHCGenotype_mhc_alleles):
            self.MissingRequiredField("V1p5MHCGenotype_mhc_alleles")
        if not isinstance(self.V1p5MHCGenotype_mhc_alleles, list):
            self.V1p5MHCGenotype_mhc_alleles = [self.V1p5MHCGenotype_mhc_alleles] if self.V1p5MHCGenotype_mhc_alleles is not None else []
        self.V1p5MHCGenotype_mhc_alleles = [v if isinstance(v, V1p5MHCAllele) else V1p5MHCAllele(**as_dict(v)) for v in self.V1p5MHCGenotype_mhc_alleles]

        if self.V1p5MHCGenotype_mhc_genotyping_method is not None and not isinstance(self.V1p5MHCGenotype_mhc_genotyping_method, str):
            self.V1p5MHCGenotype_mhc_genotyping_method = str(self.V1p5MHCGenotype_mhc_genotyping_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5MHCAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5MHCAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5MHCAllele"
    class_name: ClassVar[str] = "V1p5MHCAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5MHCAllele

    V1p5MHCAllele_allele_designation: Optional[str] = None
    V1p5MHCAllele_gene: Optional[Union[str, "V1p5Gene"]] = None
    V1p5MHCAllele_reference_set_ref: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5MHCAllele_allele_designation is not None and not isinstance(self.V1p5MHCAllele_allele_designation, str):
            self.V1p5MHCAllele_allele_designation = str(self.V1p5MHCAllele_allele_designation)

        if self.V1p5MHCAllele_reference_set_ref is not None and not isinstance(self.V1p5MHCAllele_reference_set_ref, str):
            self.V1p5MHCAllele_reference_set_ref = str(self.V1p5MHCAllele_reference_set_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5SubjectGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5SubjectGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5SubjectGenotype"
    class_name: ClassVar[str] = "V1p5SubjectGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5SubjectGenotype

    V1p5SubjectGenotype_receptor_genotype_set: Optional[Union[dict, V1p5GenotypeSet]] = None
    V1p5SubjectGenotype_mhc_genotype_set: Optional[Union[dict, V1p5MHCGenotypeSet]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5SubjectGenotype_receptor_genotype_set is not None and not isinstance(self.V1p5SubjectGenotype_receptor_genotype_set, V1p5GenotypeSet):
            self.V1p5SubjectGenotype_receptor_genotype_set = V1p5GenotypeSet(**as_dict(self.V1p5SubjectGenotype_receptor_genotype_set))

        if self.V1p5SubjectGenotype_mhc_genotype_set is not None and not isinstance(self.V1p5SubjectGenotype_mhc_genotype_set, V1p5MHCGenotypeSet):
            self.V1p5SubjectGenotype_mhc_genotype_set = V1p5MHCGenotypeSet(**as_dict(self.V1p5SubjectGenotype_mhc_genotype_set))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Study(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Study"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Study"
    class_name: ClassVar[str] = "V1p5Study"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Study

    V1p5Study_study_id: str = None
    V1p5Study_study_title: str = None
    V1p5Study_study_type: Union[str, "V1p5StudyType"] = None
    V1p5Study_inclusion_exclusion_criteria: str = None
    V1p5Study_grants: str = None
    V1p5Study_collected_by: str = None
    V1p5Study_lab_name: str = None
    V1p5Study_lab_address: str = None
    V1p5Study_submitted_by: str = None
    V1p5Study_pub_ids: str = None
    V1p5Study_keywords_study: Union[Union[str, "V1p5KeywordsStudy"], List[Union[str, "V1p5KeywordsStudy"]]] = None
    V1p5Study_study_description: Optional[str] = None
    V1p5Study_study_contact: Optional[str] = None
    V1p5Study_adc_publish_date: Optional[str] = None
    V1p5Study_adc_update_date: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5Study_study_id):
            self.MissingRequiredField("V1p5Study_study_id")
        if not isinstance(self.V1p5Study_study_id, str):
            self.V1p5Study_study_id = str(self.V1p5Study_study_id)

        if self._is_empty(self.V1p5Study_study_title):
            self.MissingRequiredField("V1p5Study_study_title")
        if not isinstance(self.V1p5Study_study_title, str):
            self.V1p5Study_study_title = str(self.V1p5Study_study_title)

        if self._is_empty(self.V1p5Study_inclusion_exclusion_criteria):
            self.MissingRequiredField("V1p5Study_inclusion_exclusion_criteria")
        if not isinstance(self.V1p5Study_inclusion_exclusion_criteria, str):
            self.V1p5Study_inclusion_exclusion_criteria = str(self.V1p5Study_inclusion_exclusion_criteria)

        if self._is_empty(self.V1p5Study_grants):
            self.MissingRequiredField("V1p5Study_grants")
        if not isinstance(self.V1p5Study_grants, str):
            self.V1p5Study_grants = str(self.V1p5Study_grants)

        if self._is_empty(self.V1p5Study_collected_by):
            self.MissingRequiredField("V1p5Study_collected_by")
        if not isinstance(self.V1p5Study_collected_by, str):
            self.V1p5Study_collected_by = str(self.V1p5Study_collected_by)

        if self._is_empty(self.V1p5Study_lab_name):
            self.MissingRequiredField("V1p5Study_lab_name")
        if not isinstance(self.V1p5Study_lab_name, str):
            self.V1p5Study_lab_name = str(self.V1p5Study_lab_name)

        if self._is_empty(self.V1p5Study_lab_address):
            self.MissingRequiredField("V1p5Study_lab_address")
        if not isinstance(self.V1p5Study_lab_address, str):
            self.V1p5Study_lab_address = str(self.V1p5Study_lab_address)

        if self._is_empty(self.V1p5Study_submitted_by):
            self.MissingRequiredField("V1p5Study_submitted_by")
        if not isinstance(self.V1p5Study_submitted_by, str):
            self.V1p5Study_submitted_by = str(self.V1p5Study_submitted_by)

        if self._is_empty(self.V1p5Study_pub_ids):
            self.MissingRequiredField("V1p5Study_pub_ids")
        if not isinstance(self.V1p5Study_pub_ids, str):
            self.V1p5Study_pub_ids = str(self.V1p5Study_pub_ids)

        if self._is_empty(self.V1p5Study_keywords_study):
            self.MissingRequiredField("V1p5Study_keywords_study")
        if not isinstance(self.V1p5Study_keywords_study, list):
            self.V1p5Study_keywords_study = [self.V1p5Study_keywords_study] if self.V1p5Study_keywords_study is not None else []
        self.V1p5Study_keywords_study = [v if isinstance(v, V1p5KeywordsStudy) else V1p5KeywordsStudy(v) for v in self.V1p5Study_keywords_study]

        if self.V1p5Study_study_description is not None and not isinstance(self.V1p5Study_study_description, str):
            self.V1p5Study_study_description = str(self.V1p5Study_study_description)

        if self.V1p5Study_study_contact is not None and not isinstance(self.V1p5Study_study_contact, str):
            self.V1p5Study_study_contact = str(self.V1p5Study_study_contact)

        if self.V1p5Study_adc_publish_date is not None and not isinstance(self.V1p5Study_adc_publish_date, str):
            self.V1p5Study_adc_publish_date = str(self.V1p5Study_adc_publish_date)

        if self.V1p5Study_adc_update_date is not None and not isinstance(self.V1p5Study_adc_update_date, str):
            self.V1p5Study_adc_update_date = str(self.V1p5Study_adc_update_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Subject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Subject"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Subject"
    class_name: ClassVar[str] = "V1p5Subject"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Subject

    V1p5Subject_subject_id: str = None
    V1p5Subject_synthetic: Union[bool, Bool] = None
    V1p5Subject_species: Union[str, "V1p5Species"] = None
    V1p5Subject_sex: Union[str, "V1p5Sex"] = None
    V1p5Subject_age_min: float = None
    V1p5Subject_age_max: float = None
    V1p5Subject_age_unit: Union[str, "V1p5AgeUnit"] = None
    V1p5Subject_age_event: str = None
    V1p5Subject_ancestry_population: str = None
    V1p5Subject_ethnicity: str = None
    V1p5Subject_race: str = None
    V1p5Subject_strain_name: str = None
    V1p5Subject_linked_subjects: str = None
    V1p5Subject_link_type: str = None
    V1p5Subject_diagnosis: Optional[Union[Union[dict, "V1p5Diagnosis"], List[Union[dict, "V1p5Diagnosis"]]]] = empty_list()
    V1p5Subject_genotype: Optional[Union[dict, V1p5SubjectGenotype]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5Subject_subject_id):
            self.MissingRequiredField("V1p5Subject_subject_id")
        if not isinstance(self.V1p5Subject_subject_id, str):
            self.V1p5Subject_subject_id = str(self.V1p5Subject_subject_id)

        if self._is_empty(self.V1p5Subject_synthetic):
            self.MissingRequiredField("V1p5Subject_synthetic")
        if not isinstance(self.V1p5Subject_synthetic, Bool):
            self.V1p5Subject_synthetic = Bool(self.V1p5Subject_synthetic)

        if self._is_empty(self.V1p5Subject_sex):
            self.MissingRequiredField("V1p5Subject_sex")
        if not isinstance(self.V1p5Subject_sex, V1p5Sex):
            self.V1p5Subject_sex = V1p5Sex(self.V1p5Subject_sex)

        if self._is_empty(self.V1p5Subject_age_min):
            self.MissingRequiredField("V1p5Subject_age_min")
        if not isinstance(self.V1p5Subject_age_min, float):
            self.V1p5Subject_age_min = float(self.V1p5Subject_age_min)

        if self._is_empty(self.V1p5Subject_age_max):
            self.MissingRequiredField("V1p5Subject_age_max")
        if not isinstance(self.V1p5Subject_age_max, float):
            self.V1p5Subject_age_max = float(self.V1p5Subject_age_max)

        if self._is_empty(self.V1p5Subject_age_event):
            self.MissingRequiredField("V1p5Subject_age_event")
        if not isinstance(self.V1p5Subject_age_event, str):
            self.V1p5Subject_age_event = str(self.V1p5Subject_age_event)

        if self._is_empty(self.V1p5Subject_ancestry_population):
            self.MissingRequiredField("V1p5Subject_ancestry_population")
        if not isinstance(self.V1p5Subject_ancestry_population, str):
            self.V1p5Subject_ancestry_population = str(self.V1p5Subject_ancestry_population)

        if self._is_empty(self.V1p5Subject_ethnicity):
            self.MissingRequiredField("V1p5Subject_ethnicity")
        if not isinstance(self.V1p5Subject_ethnicity, str):
            self.V1p5Subject_ethnicity = str(self.V1p5Subject_ethnicity)

        if self._is_empty(self.V1p5Subject_race):
            self.MissingRequiredField("V1p5Subject_race")
        if not isinstance(self.V1p5Subject_race, str):
            self.V1p5Subject_race = str(self.V1p5Subject_race)

        if self._is_empty(self.V1p5Subject_strain_name):
            self.MissingRequiredField("V1p5Subject_strain_name")
        if not isinstance(self.V1p5Subject_strain_name, str):
            self.V1p5Subject_strain_name = str(self.V1p5Subject_strain_name)

        if self._is_empty(self.V1p5Subject_linked_subjects):
            self.MissingRequiredField("V1p5Subject_linked_subjects")
        if not isinstance(self.V1p5Subject_linked_subjects, str):
            self.V1p5Subject_linked_subjects = str(self.V1p5Subject_linked_subjects)

        if self._is_empty(self.V1p5Subject_link_type):
            self.MissingRequiredField("V1p5Subject_link_type")
        if not isinstance(self.V1p5Subject_link_type, str):
            self.V1p5Subject_link_type = str(self.V1p5Subject_link_type)

        self._normalize_inlined_as_dict(slot_name="V1p5Subject_diagnosis", slot_type=V1p5Diagnosis, key_name="V1p5Diagnosis_study_group_description", keyed=False)

        if self.V1p5Subject_genotype is not None and not isinstance(self.V1p5Subject_genotype, V1p5SubjectGenotype):
            self.V1p5Subject_genotype = V1p5SubjectGenotype(**as_dict(self.V1p5Subject_genotype))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Diagnosis(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Diagnosis"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Diagnosis"
    class_name: ClassVar[str] = "V1p5Diagnosis"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Diagnosis

    V1p5Diagnosis_study_group_description: str = None
    V1p5Diagnosis_disease_diagnosis: Union[str, "V1p5DiseaseDiagnosis"] = None
    V1p5Diagnosis_disease_length: str = None
    V1p5Diagnosis_disease_stage: str = None
    V1p5Diagnosis_prior_therapies: str = None
    V1p5Diagnosis_immunogen: str = None
    V1p5Diagnosis_intervention: str = None
    V1p5Diagnosis_medical_history: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5Diagnosis_study_group_description):
            self.MissingRequiredField("V1p5Diagnosis_study_group_description")
        if not isinstance(self.V1p5Diagnosis_study_group_description, str):
            self.V1p5Diagnosis_study_group_description = str(self.V1p5Diagnosis_study_group_description)

        if self._is_empty(self.V1p5Diagnosis_disease_length):
            self.MissingRequiredField("V1p5Diagnosis_disease_length")
        if not isinstance(self.V1p5Diagnosis_disease_length, str):
            self.V1p5Diagnosis_disease_length = str(self.V1p5Diagnosis_disease_length)

        if self._is_empty(self.V1p5Diagnosis_disease_stage):
            self.MissingRequiredField("V1p5Diagnosis_disease_stage")
        if not isinstance(self.V1p5Diagnosis_disease_stage, str):
            self.V1p5Diagnosis_disease_stage = str(self.V1p5Diagnosis_disease_stage)

        if self._is_empty(self.V1p5Diagnosis_prior_therapies):
            self.MissingRequiredField("V1p5Diagnosis_prior_therapies")
        if not isinstance(self.V1p5Diagnosis_prior_therapies, str):
            self.V1p5Diagnosis_prior_therapies = str(self.V1p5Diagnosis_prior_therapies)

        if self._is_empty(self.V1p5Diagnosis_immunogen):
            self.MissingRequiredField("V1p5Diagnosis_immunogen")
        if not isinstance(self.V1p5Diagnosis_immunogen, str):
            self.V1p5Diagnosis_immunogen = str(self.V1p5Diagnosis_immunogen)

        if self._is_empty(self.V1p5Diagnosis_intervention):
            self.MissingRequiredField("V1p5Diagnosis_intervention")
        if not isinstance(self.V1p5Diagnosis_intervention, str):
            self.V1p5Diagnosis_intervention = str(self.V1p5Diagnosis_intervention)

        if self._is_empty(self.V1p5Diagnosis_medical_history):
            self.MissingRequiredField("V1p5Diagnosis_medical_history")
        if not isinstance(self.V1p5Diagnosis_medical_history, str):
            self.V1p5Diagnosis_medical_history = str(self.V1p5Diagnosis_medical_history)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Sample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Sample"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Sample"
    class_name: ClassVar[str] = "V1p5Sample"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Sample

    V1p5Sample_sample_id: str = None
    V1p5Sample_sample_type: str = None
    V1p5Sample_tissue: Union[str, "V1p5Tissue"] = None
    V1p5Sample_anatomic_site: str = None
    V1p5Sample_disease_state_sample: str = None
    V1p5Sample_collection_time_point_relative: float = None
    V1p5Sample_collection_time_point_relative_unit: Union[str, "V1p5CollectionTimePointRelativeUnit"] = None
    V1p5Sample_collection_time_point_reference: str = None
    V1p5Sample_biomaterial_provider: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5Sample_sample_id):
            self.MissingRequiredField("V1p5Sample_sample_id")
        if not isinstance(self.V1p5Sample_sample_id, str):
            self.V1p5Sample_sample_id = str(self.V1p5Sample_sample_id)

        if self._is_empty(self.V1p5Sample_sample_type):
            self.MissingRequiredField("V1p5Sample_sample_type")
        if not isinstance(self.V1p5Sample_sample_type, str):
            self.V1p5Sample_sample_type = str(self.V1p5Sample_sample_type)

        if self._is_empty(self.V1p5Sample_anatomic_site):
            self.MissingRequiredField("V1p5Sample_anatomic_site")
        if not isinstance(self.V1p5Sample_anatomic_site, str):
            self.V1p5Sample_anatomic_site = str(self.V1p5Sample_anatomic_site)

        if self._is_empty(self.V1p5Sample_disease_state_sample):
            self.MissingRequiredField("V1p5Sample_disease_state_sample")
        if not isinstance(self.V1p5Sample_disease_state_sample, str):
            self.V1p5Sample_disease_state_sample = str(self.V1p5Sample_disease_state_sample)

        if self._is_empty(self.V1p5Sample_collection_time_point_relative):
            self.MissingRequiredField("V1p5Sample_collection_time_point_relative")
        if not isinstance(self.V1p5Sample_collection_time_point_relative, float):
            self.V1p5Sample_collection_time_point_relative = float(self.V1p5Sample_collection_time_point_relative)

        if self._is_empty(self.V1p5Sample_collection_time_point_reference):
            self.MissingRequiredField("V1p5Sample_collection_time_point_reference")
        if not isinstance(self.V1p5Sample_collection_time_point_reference, str):
            self.V1p5Sample_collection_time_point_reference = str(self.V1p5Sample_collection_time_point_reference)

        if self._is_empty(self.V1p5Sample_biomaterial_provider):
            self.MissingRequiredField("V1p5Sample_biomaterial_provider")
        if not isinstance(self.V1p5Sample_biomaterial_provider, str):
            self.V1p5Sample_biomaterial_provider = str(self.V1p5Sample_biomaterial_provider)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5CellProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5CellProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5CellProcessing"
    class_name: ClassVar[str] = "V1p5CellProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5CellProcessing

    V1p5CellProcessing_tissue_processing: str = None
    V1p5CellProcessing_cell_subset: Union[str, "V1p5CellSubset"] = None
    V1p5CellProcessing_cell_phenotype: str = None
    V1p5CellProcessing_single_cell: Union[bool, Bool] = None
    V1p5CellProcessing_cell_number: int = None
    V1p5CellProcessing_cells_per_reaction: int = None
    V1p5CellProcessing_cell_storage: Union[bool, Bool] = None
    V1p5CellProcessing_cell_quality: str = None
    V1p5CellProcessing_cell_isolation: str = None
    V1p5CellProcessing_cell_processing_protocol: str = None
    V1p5CellProcessing_cell_species: Optional[Union[str, "V1p5CellSpecies"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5CellProcessing_tissue_processing):
            self.MissingRequiredField("V1p5CellProcessing_tissue_processing")
        if not isinstance(self.V1p5CellProcessing_tissue_processing, str):
            self.V1p5CellProcessing_tissue_processing = str(self.V1p5CellProcessing_tissue_processing)

        if self._is_empty(self.V1p5CellProcessing_cell_phenotype):
            self.MissingRequiredField("V1p5CellProcessing_cell_phenotype")
        if not isinstance(self.V1p5CellProcessing_cell_phenotype, str):
            self.V1p5CellProcessing_cell_phenotype = str(self.V1p5CellProcessing_cell_phenotype)

        if self._is_empty(self.V1p5CellProcessing_single_cell):
            self.MissingRequiredField("V1p5CellProcessing_single_cell")
        if not isinstance(self.V1p5CellProcessing_single_cell, Bool):
            self.V1p5CellProcessing_single_cell = Bool(self.V1p5CellProcessing_single_cell)

        if self._is_empty(self.V1p5CellProcessing_cell_number):
            self.MissingRequiredField("V1p5CellProcessing_cell_number")
        if not isinstance(self.V1p5CellProcessing_cell_number, int):
            self.V1p5CellProcessing_cell_number = int(self.V1p5CellProcessing_cell_number)

        if self._is_empty(self.V1p5CellProcessing_cells_per_reaction):
            self.MissingRequiredField("V1p5CellProcessing_cells_per_reaction")
        if not isinstance(self.V1p5CellProcessing_cells_per_reaction, int):
            self.V1p5CellProcessing_cells_per_reaction = int(self.V1p5CellProcessing_cells_per_reaction)

        if self._is_empty(self.V1p5CellProcessing_cell_storage):
            self.MissingRequiredField("V1p5CellProcessing_cell_storage")
        if not isinstance(self.V1p5CellProcessing_cell_storage, Bool):
            self.V1p5CellProcessing_cell_storage = Bool(self.V1p5CellProcessing_cell_storage)

        if self._is_empty(self.V1p5CellProcessing_cell_quality):
            self.MissingRequiredField("V1p5CellProcessing_cell_quality")
        if not isinstance(self.V1p5CellProcessing_cell_quality, str):
            self.V1p5CellProcessing_cell_quality = str(self.V1p5CellProcessing_cell_quality)

        if self._is_empty(self.V1p5CellProcessing_cell_isolation):
            self.MissingRequiredField("V1p5CellProcessing_cell_isolation")
        if not isinstance(self.V1p5CellProcessing_cell_isolation, str):
            self.V1p5CellProcessing_cell_isolation = str(self.V1p5CellProcessing_cell_isolation)

        if self._is_empty(self.V1p5CellProcessing_cell_processing_protocol):
            self.MissingRequiredField("V1p5CellProcessing_cell_processing_protocol")
        if not isinstance(self.V1p5CellProcessing_cell_processing_protocol, str):
            self.V1p5CellProcessing_cell_processing_protocol = str(self.V1p5CellProcessing_cell_processing_protocol)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5PCRTarget(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5PCRTarget"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5PCRTarget"
    class_name: ClassVar[str] = "V1p5PCRTarget"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5PCRTarget

    V1p5PCRTarget_pcr_target_locus: Union[str, "V1p5PcrTargetLocus"] = None
    V1p5PCRTarget_forward_pcr_primer_target_location: str = None
    V1p5PCRTarget_reverse_pcr_primer_target_location: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5PCRTarget_pcr_target_locus):
            self.MissingRequiredField("V1p5PCRTarget_pcr_target_locus")
        if not isinstance(self.V1p5PCRTarget_pcr_target_locus, V1p5PcrTargetLocus):
            self.V1p5PCRTarget_pcr_target_locus = V1p5PcrTargetLocus(self.V1p5PCRTarget_pcr_target_locus)

        if self._is_empty(self.V1p5PCRTarget_forward_pcr_primer_target_location):
            self.MissingRequiredField("V1p5PCRTarget_forward_pcr_primer_target_location")
        if not isinstance(self.V1p5PCRTarget_forward_pcr_primer_target_location, str):
            self.V1p5PCRTarget_forward_pcr_primer_target_location = str(self.V1p5PCRTarget_forward_pcr_primer_target_location)

        if self._is_empty(self.V1p5PCRTarget_reverse_pcr_primer_target_location):
            self.MissingRequiredField("V1p5PCRTarget_reverse_pcr_primer_target_location")
        if not isinstance(self.V1p5PCRTarget_reverse_pcr_primer_target_location, str):
            self.V1p5PCRTarget_reverse_pcr_primer_target_location = str(self.V1p5PCRTarget_reverse_pcr_primer_target_location)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5NucleicAcidProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5NucleicAcidProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5NucleicAcidProcessing"
    class_name: ClassVar[str] = "V1p5NucleicAcidProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5NucleicAcidProcessing

    V1p5NucleicAcidProcessing_template_class: Union[str, "V1p5TemplateClass"] = None
    V1p5NucleicAcidProcessing_template_quality: str = None
    V1p5NucleicAcidProcessing_template_amount: float = None
    V1p5NucleicAcidProcessing_template_amount_unit: Union[str, "V1p5TemplateAmountUnit"] = None
    V1p5NucleicAcidProcessing_library_generation_method: Union[str, "V1p5LibraryGenerationMethod"] = None
    V1p5NucleicAcidProcessing_library_generation_protocol: str = None
    V1p5NucleicAcidProcessing_library_generation_kit_version: str = None
    V1p5NucleicAcidProcessing_complete_sequences: Union[str, "V1p5CompleteSequences"] = None
    V1p5NucleicAcidProcessing_physical_linkage: Union[str, "V1p5PhysicalLinkage"] = None
    V1p5NucleicAcidProcessing_pcr_target: Optional[Union[Union[dict, V1p5PCRTarget], List[Union[dict, V1p5PCRTarget]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5NucleicAcidProcessing_template_class):
            self.MissingRequiredField("V1p5NucleicAcidProcessing_template_class")
        if not isinstance(self.V1p5NucleicAcidProcessing_template_class, V1p5TemplateClass):
            self.V1p5NucleicAcidProcessing_template_class = V1p5TemplateClass(self.V1p5NucleicAcidProcessing_template_class)

        if self._is_empty(self.V1p5NucleicAcidProcessing_template_quality):
            self.MissingRequiredField("V1p5NucleicAcidProcessing_template_quality")
        if not isinstance(self.V1p5NucleicAcidProcessing_template_quality, str):
            self.V1p5NucleicAcidProcessing_template_quality = str(self.V1p5NucleicAcidProcessing_template_quality)

        if self._is_empty(self.V1p5NucleicAcidProcessing_template_amount):
            self.MissingRequiredField("V1p5NucleicAcidProcessing_template_amount")
        if not isinstance(self.V1p5NucleicAcidProcessing_template_amount, float):
            self.V1p5NucleicAcidProcessing_template_amount = float(self.V1p5NucleicAcidProcessing_template_amount)

        if self._is_empty(self.V1p5NucleicAcidProcessing_library_generation_method):
            self.MissingRequiredField("V1p5NucleicAcidProcessing_library_generation_method")
        if not isinstance(self.V1p5NucleicAcidProcessing_library_generation_method, V1p5LibraryGenerationMethod):
            self.V1p5NucleicAcidProcessing_library_generation_method = V1p5LibraryGenerationMethod(self.V1p5NucleicAcidProcessing_library_generation_method)

        if self._is_empty(self.V1p5NucleicAcidProcessing_library_generation_protocol):
            self.MissingRequiredField("V1p5NucleicAcidProcessing_library_generation_protocol")
        if not isinstance(self.V1p5NucleicAcidProcessing_library_generation_protocol, str):
            self.V1p5NucleicAcidProcessing_library_generation_protocol = str(self.V1p5NucleicAcidProcessing_library_generation_protocol)

        if self._is_empty(self.V1p5NucleicAcidProcessing_library_generation_kit_version):
            self.MissingRequiredField("V1p5NucleicAcidProcessing_library_generation_kit_version")
        if not isinstance(self.V1p5NucleicAcidProcessing_library_generation_kit_version, str):
            self.V1p5NucleicAcidProcessing_library_generation_kit_version = str(self.V1p5NucleicAcidProcessing_library_generation_kit_version)

        if self._is_empty(self.V1p5NucleicAcidProcessing_complete_sequences):
            self.MissingRequiredField("V1p5NucleicAcidProcessing_complete_sequences")
        if not isinstance(self.V1p5NucleicAcidProcessing_complete_sequences, V1p5CompleteSequences):
            self.V1p5NucleicAcidProcessing_complete_sequences = V1p5CompleteSequences(self.V1p5NucleicAcidProcessing_complete_sequences)

        if self._is_empty(self.V1p5NucleicAcidProcessing_physical_linkage):
            self.MissingRequiredField("V1p5NucleicAcidProcessing_physical_linkage")
        if not isinstance(self.V1p5NucleicAcidProcessing_physical_linkage, V1p5PhysicalLinkage):
            self.V1p5NucleicAcidProcessing_physical_linkage = V1p5PhysicalLinkage(self.V1p5NucleicAcidProcessing_physical_linkage)

        self._normalize_inlined_as_dict(slot_name="V1p5NucleicAcidProcessing_pcr_target", slot_type=V1p5PCRTarget, key_name="V1p5PCRTarget_pcr_target_locus", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5SequencingRun(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5SequencingRun"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5SequencingRun"
    class_name: ClassVar[str] = "V1p5SequencingRun"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5SequencingRun

    V1p5SequencingRun_sequencing_run_id: str = None
    V1p5SequencingRun_total_reads_passing_qc_filter: int = None
    V1p5SequencingRun_sequencing_platform: str = None
    V1p5SequencingRun_sequencing_facility: str = None
    V1p5SequencingRun_sequencing_run_date: str = None
    V1p5SequencingRun_sequencing_kit: str = None
    V1p5SequencingRun_sequencing_files: Optional[Union[dict, "V1p5SequencingData"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5SequencingRun_sequencing_run_id):
            self.MissingRequiredField("V1p5SequencingRun_sequencing_run_id")
        if not isinstance(self.V1p5SequencingRun_sequencing_run_id, str):
            self.V1p5SequencingRun_sequencing_run_id = str(self.V1p5SequencingRun_sequencing_run_id)

        if self._is_empty(self.V1p5SequencingRun_total_reads_passing_qc_filter):
            self.MissingRequiredField("V1p5SequencingRun_total_reads_passing_qc_filter")
        if not isinstance(self.V1p5SequencingRun_total_reads_passing_qc_filter, int):
            self.V1p5SequencingRun_total_reads_passing_qc_filter = int(self.V1p5SequencingRun_total_reads_passing_qc_filter)

        if self._is_empty(self.V1p5SequencingRun_sequencing_platform):
            self.MissingRequiredField("V1p5SequencingRun_sequencing_platform")
        if not isinstance(self.V1p5SequencingRun_sequencing_platform, str):
            self.V1p5SequencingRun_sequencing_platform = str(self.V1p5SequencingRun_sequencing_platform)

        if self._is_empty(self.V1p5SequencingRun_sequencing_facility):
            self.MissingRequiredField("V1p5SequencingRun_sequencing_facility")
        if not isinstance(self.V1p5SequencingRun_sequencing_facility, str):
            self.V1p5SequencingRun_sequencing_facility = str(self.V1p5SequencingRun_sequencing_facility)

        if self._is_empty(self.V1p5SequencingRun_sequencing_run_date):
            self.MissingRequiredField("V1p5SequencingRun_sequencing_run_date")
        if not isinstance(self.V1p5SequencingRun_sequencing_run_date, str):
            self.V1p5SequencingRun_sequencing_run_date = str(self.V1p5SequencingRun_sequencing_run_date)

        if self._is_empty(self.V1p5SequencingRun_sequencing_kit):
            self.MissingRequiredField("V1p5SequencingRun_sequencing_kit")
        if not isinstance(self.V1p5SequencingRun_sequencing_kit, str):
            self.V1p5SequencingRun_sequencing_kit = str(self.V1p5SequencingRun_sequencing_kit)

        if self.V1p5SequencingRun_sequencing_files is not None and not isinstance(self.V1p5SequencingRun_sequencing_files, V1p5SequencingData):
            self.V1p5SequencingRun_sequencing_files = V1p5SequencingData(**as_dict(self.V1p5SequencingRun_sequencing_files))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5SequencingData(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5SequencingData"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5SequencingData"
    class_name: ClassVar[str] = "V1p5SequencingData"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5SequencingData

    V1p5SequencingData_sequencing_data_id: str = None
    V1p5SequencingData_file_type: Union[str, "V1p5FileType"] = None
    V1p5SequencingData_filename: str = None
    V1p5SequencingData_read_direction: Union[str, "V1p5ReadDirection"] = None
    V1p5SequencingData_read_length: int = None
    V1p5SequencingData_paired_filename: str = None
    V1p5SequencingData_paired_read_direction: Union[str, "V1p5PairedReadDirection"] = None
    V1p5SequencingData_paired_read_length: int = None
    V1p5SequencingData_index_filename: Optional[str] = None
    V1p5SequencingData_index_length: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5SequencingData_sequencing_data_id):
            self.MissingRequiredField("V1p5SequencingData_sequencing_data_id")
        if not isinstance(self.V1p5SequencingData_sequencing_data_id, str):
            self.V1p5SequencingData_sequencing_data_id = str(self.V1p5SequencingData_sequencing_data_id)

        if self._is_empty(self.V1p5SequencingData_file_type):
            self.MissingRequiredField("V1p5SequencingData_file_type")
        if not isinstance(self.V1p5SequencingData_file_type, V1p5FileType):
            self.V1p5SequencingData_file_type = V1p5FileType(self.V1p5SequencingData_file_type)

        if self._is_empty(self.V1p5SequencingData_filename):
            self.MissingRequiredField("V1p5SequencingData_filename")
        if not isinstance(self.V1p5SequencingData_filename, str):
            self.V1p5SequencingData_filename = str(self.V1p5SequencingData_filename)

        if self._is_empty(self.V1p5SequencingData_read_direction):
            self.MissingRequiredField("V1p5SequencingData_read_direction")
        if not isinstance(self.V1p5SequencingData_read_direction, V1p5ReadDirection):
            self.V1p5SequencingData_read_direction = V1p5ReadDirection(self.V1p5SequencingData_read_direction)

        if self._is_empty(self.V1p5SequencingData_read_length):
            self.MissingRequiredField("V1p5SequencingData_read_length")
        if not isinstance(self.V1p5SequencingData_read_length, int):
            self.V1p5SequencingData_read_length = int(self.V1p5SequencingData_read_length)

        if self._is_empty(self.V1p5SequencingData_paired_filename):
            self.MissingRequiredField("V1p5SequencingData_paired_filename")
        if not isinstance(self.V1p5SequencingData_paired_filename, str):
            self.V1p5SequencingData_paired_filename = str(self.V1p5SequencingData_paired_filename)

        if self._is_empty(self.V1p5SequencingData_paired_read_direction):
            self.MissingRequiredField("V1p5SequencingData_paired_read_direction")
        if not isinstance(self.V1p5SequencingData_paired_read_direction, V1p5PairedReadDirection):
            self.V1p5SequencingData_paired_read_direction = V1p5PairedReadDirection(self.V1p5SequencingData_paired_read_direction)

        if self._is_empty(self.V1p5SequencingData_paired_read_length):
            self.MissingRequiredField("V1p5SequencingData_paired_read_length")
        if not isinstance(self.V1p5SequencingData_paired_read_length, int):
            self.V1p5SequencingData_paired_read_length = int(self.V1p5SequencingData_paired_read_length)

        if self.V1p5SequencingData_index_filename is not None and not isinstance(self.V1p5SequencingData_index_filename, str):
            self.V1p5SequencingData_index_filename = str(self.V1p5SequencingData_index_filename)

        if self.V1p5SequencingData_index_length is not None and not isinstance(self.V1p5SequencingData_index_length, int):
            self.V1p5SequencingData_index_length = int(self.V1p5SequencingData_index_length)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5DataProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5DataProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5DataProcessing"
    class_name: ClassVar[str] = "V1p5DataProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5DataProcessing

    V1p5DataProcessing_software_versions: str = None
    V1p5DataProcessing_paired_reads_assembly: str = None
    V1p5DataProcessing_quality_thresholds: str = None
    V1p5DataProcessing_primer_match_cutoffs: str = None
    V1p5DataProcessing_collapsing_method: str = None
    V1p5DataProcessing_data_processing_protocols: str = None
    V1p5DataProcessing_germline_database: str = None
    V1p5DataProcessing_data_processing_id: Optional[str] = None
    V1p5DataProcessing_primary_annotation: Optional[Union[bool, Bool]] = None
    V1p5DataProcessing_data_processing_files: Optional[Union[str, List[str]]] = empty_list()
    V1p5DataProcessing_germline_set_ref: Optional[str] = None
    V1p5DataProcessing_analysis_provenance_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5DataProcessing_software_versions):
            self.MissingRequiredField("V1p5DataProcessing_software_versions")
        if not isinstance(self.V1p5DataProcessing_software_versions, str):
            self.V1p5DataProcessing_software_versions = str(self.V1p5DataProcessing_software_versions)

        if self._is_empty(self.V1p5DataProcessing_paired_reads_assembly):
            self.MissingRequiredField("V1p5DataProcessing_paired_reads_assembly")
        if not isinstance(self.V1p5DataProcessing_paired_reads_assembly, str):
            self.V1p5DataProcessing_paired_reads_assembly = str(self.V1p5DataProcessing_paired_reads_assembly)

        if self._is_empty(self.V1p5DataProcessing_quality_thresholds):
            self.MissingRequiredField("V1p5DataProcessing_quality_thresholds")
        if not isinstance(self.V1p5DataProcessing_quality_thresholds, str):
            self.V1p5DataProcessing_quality_thresholds = str(self.V1p5DataProcessing_quality_thresholds)

        if self._is_empty(self.V1p5DataProcessing_primer_match_cutoffs):
            self.MissingRequiredField("V1p5DataProcessing_primer_match_cutoffs")
        if not isinstance(self.V1p5DataProcessing_primer_match_cutoffs, str):
            self.V1p5DataProcessing_primer_match_cutoffs = str(self.V1p5DataProcessing_primer_match_cutoffs)

        if self._is_empty(self.V1p5DataProcessing_collapsing_method):
            self.MissingRequiredField("V1p5DataProcessing_collapsing_method")
        if not isinstance(self.V1p5DataProcessing_collapsing_method, str):
            self.V1p5DataProcessing_collapsing_method = str(self.V1p5DataProcessing_collapsing_method)

        if self._is_empty(self.V1p5DataProcessing_data_processing_protocols):
            self.MissingRequiredField("V1p5DataProcessing_data_processing_protocols")
        if not isinstance(self.V1p5DataProcessing_data_processing_protocols, str):
            self.V1p5DataProcessing_data_processing_protocols = str(self.V1p5DataProcessing_data_processing_protocols)

        if self._is_empty(self.V1p5DataProcessing_germline_database):
            self.MissingRequiredField("V1p5DataProcessing_germline_database")
        if not isinstance(self.V1p5DataProcessing_germline_database, str):
            self.V1p5DataProcessing_germline_database = str(self.V1p5DataProcessing_germline_database)

        if self.V1p5DataProcessing_data_processing_id is not None and not isinstance(self.V1p5DataProcessing_data_processing_id, str):
            self.V1p5DataProcessing_data_processing_id = str(self.V1p5DataProcessing_data_processing_id)

        if self.V1p5DataProcessing_primary_annotation is not None and not isinstance(self.V1p5DataProcessing_primary_annotation, Bool):
            self.V1p5DataProcessing_primary_annotation = Bool(self.V1p5DataProcessing_primary_annotation)

        if not isinstance(self.V1p5DataProcessing_data_processing_files, list):
            self.V1p5DataProcessing_data_processing_files = [self.V1p5DataProcessing_data_processing_files] if self.V1p5DataProcessing_data_processing_files is not None else []
        self.V1p5DataProcessing_data_processing_files = [v if isinstance(v, str) else str(v) for v in self.V1p5DataProcessing_data_processing_files]

        if self.V1p5DataProcessing_germline_set_ref is not None and not isinstance(self.V1p5DataProcessing_germline_set_ref, str):
            self.V1p5DataProcessing_germline_set_ref = str(self.V1p5DataProcessing_germline_set_ref)

        if self.V1p5DataProcessing_analysis_provenance_id is not None and not isinstance(self.V1p5DataProcessing_analysis_provenance_id, str):
            self.V1p5DataProcessing_analysis_provenance_id = str(self.V1p5DataProcessing_analysis_provenance_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Repertoire(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Repertoire"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Repertoire"
    class_name: ClassVar[str] = "V1p5Repertoire"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Repertoire

    V1p5Repertoire_study: Union[dict, V1p5Study] = None
    V1p5Repertoire_subject: Union[dict, V1p5Subject] = None
    V1p5Repertoire_sample: Union[Union[dict, "V1p5SampleProcessing"], List[Union[dict, "V1p5SampleProcessing"]]] = None
    V1p5Repertoire_data_processing: Union[Union[dict, V1p5DataProcessing], List[Union[dict, V1p5DataProcessing]]] = None
    V1p5Repertoire_repertoire_id: Optional[str] = None
    V1p5Repertoire_repertoire_name: Optional[str] = None
    V1p5Repertoire_repertoire_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5Repertoire_study):
            self.MissingRequiredField("V1p5Repertoire_study")
        if not isinstance(self.V1p5Repertoire_study, V1p5Study):
            self.V1p5Repertoire_study = V1p5Study(**as_dict(self.V1p5Repertoire_study))

        if self._is_empty(self.V1p5Repertoire_subject):
            self.MissingRequiredField("V1p5Repertoire_subject")
        if not isinstance(self.V1p5Repertoire_subject, V1p5Subject):
            self.V1p5Repertoire_subject = V1p5Subject(**as_dict(self.V1p5Repertoire_subject))

        if self._is_empty(self.V1p5Repertoire_sample):
            self.MissingRequiredField("V1p5Repertoire_sample")
        self._normalize_inlined_as_dict(slot_name="V1p5Repertoire_sample", slot_type=V1p5SampleProcessing, key_name="V1p5Sample_sample_id", keyed=False)

        if self._is_empty(self.V1p5Repertoire_data_processing):
            self.MissingRequiredField("V1p5Repertoire_data_processing")
        self._normalize_inlined_as_dict(slot_name="V1p5Repertoire_data_processing", slot_type=V1p5DataProcessing, key_name="V1p5DataProcessing_software_versions", keyed=False)

        if self.V1p5Repertoire_repertoire_id is not None and not isinstance(self.V1p5Repertoire_repertoire_id, str):
            self.V1p5Repertoire_repertoire_id = str(self.V1p5Repertoire_repertoire_id)

        if self.V1p5Repertoire_repertoire_name is not None and not isinstance(self.V1p5Repertoire_repertoire_name, str):
            self.V1p5Repertoire_repertoire_name = str(self.V1p5Repertoire_repertoire_name)

        if self.V1p5Repertoire_repertoire_description is not None and not isinstance(self.V1p5Repertoire_repertoire_description, str):
            self.V1p5Repertoire_repertoire_description = str(self.V1p5Repertoire_repertoire_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5RepertoireGroupDetail(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5RepertoireGroupDetail"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5RepertoireGroupDetail"
    class_name: ClassVar[str] = "V1p5RepertoireGroupDetail"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5RepertoireGroupDetail

    V1p5RepertoireGroupDetail_repertoire_id: Optional[str] = None
    V1p5RepertoireGroupDetail_repertoire_description: Optional[str] = None
    V1p5RepertoireGroupDetail_time_point: Optional[Union[dict, V1p5TimePoint]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p5RepertoireGroupDetail_repertoire_id is not None and not isinstance(self.V1p5RepertoireGroupDetail_repertoire_id, str):
            self.V1p5RepertoireGroupDetail_repertoire_id = str(self.V1p5RepertoireGroupDetail_repertoire_id)

        if self.V1p5RepertoireGroupDetail_repertoire_description is not None and not isinstance(self.V1p5RepertoireGroupDetail_repertoire_description, str):
            self.V1p5RepertoireGroupDetail_repertoire_description = str(self.V1p5RepertoireGroupDetail_repertoire_description)

        if self.V1p5RepertoireGroupDetail_time_point is not None and not isinstance(self.V1p5RepertoireGroupDetail_time_point, V1p5TimePoint):
            self.V1p5RepertoireGroupDetail_time_point = V1p5TimePoint(**as_dict(self.V1p5RepertoireGroupDetail_time_point))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5RepertoireGroup(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5RepertoireGroup"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5RepertoireGroup"
    class_name: ClassVar[str] = "V1p5RepertoireGroup"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5RepertoireGroup

    V1p5RepertoireGroup_repertoire_group_id: str = None
    V1p5RepertoireGroup_repertoires: Union[Union[dict, V1p5RepertoireGroupDetail], List[Union[dict, V1p5RepertoireGroupDetail]]] = None
    V1p5RepertoireGroup_repertoire_group_name: Optional[str] = None
    V1p5RepertoireGroup_repertoire_group_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5RepertoireGroup_repertoire_group_id):
            self.MissingRequiredField("V1p5RepertoireGroup_repertoire_group_id")
        if not isinstance(self.V1p5RepertoireGroup_repertoire_group_id, str):
            self.V1p5RepertoireGroup_repertoire_group_id = str(self.V1p5RepertoireGroup_repertoire_group_id)

        if self._is_empty(self.V1p5RepertoireGroup_repertoires):
            self.MissingRequiredField("V1p5RepertoireGroup_repertoires")
        if not isinstance(self.V1p5RepertoireGroup_repertoires, list):
            self.V1p5RepertoireGroup_repertoires = [self.V1p5RepertoireGroup_repertoires] if self.V1p5RepertoireGroup_repertoires is not None else []
        self.V1p5RepertoireGroup_repertoires = [v if isinstance(v, V1p5RepertoireGroupDetail) else V1p5RepertoireGroupDetail(**as_dict(v)) for v in self.V1p5RepertoireGroup_repertoires]

        if self.V1p5RepertoireGroup_repertoire_group_name is not None and not isinstance(self.V1p5RepertoireGroup_repertoire_group_name, str):
            self.V1p5RepertoireGroup_repertoire_group_name = str(self.V1p5RepertoireGroup_repertoire_group_name)

        if self.V1p5RepertoireGroup_repertoire_group_description is not None and not isinstance(self.V1p5RepertoireGroup_repertoire_group_description, str):
            self.V1p5RepertoireGroup_repertoire_group_description = str(self.V1p5RepertoireGroup_repertoire_group_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Alignment(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Alignment"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Alignment"
    class_name: ClassVar[str] = "V1p5Alignment"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Alignment

    V1p5Alignment_sequence_id: str = None
    V1p5Alignment_segment: str = None
    V1p5Alignment_call: str = None
    V1p5Alignment_score: float = None
    V1p5Alignment_cigar: str = None
    V1p5Alignment_rev_comp: Optional[Union[bool, Bool]] = None
    V1p5Alignment_identity: Optional[float] = None
    V1p5Alignment_support: Optional[float] = None
    V1p5Alignment_sequence_start: Optional[int] = None
    V1p5Alignment_sequence_end: Optional[int] = None
    V1p5Alignment_germline_start: Optional[int] = None
    V1p5Alignment_germline_end: Optional[int] = None
    V1p5Alignment_rank: Optional[int] = None
    V1p5Alignment_data_processing_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5Alignment_sequence_id):
            self.MissingRequiredField("V1p5Alignment_sequence_id")
        if not isinstance(self.V1p5Alignment_sequence_id, str):
            self.V1p5Alignment_sequence_id = str(self.V1p5Alignment_sequence_id)

        if self._is_empty(self.V1p5Alignment_segment):
            self.MissingRequiredField("V1p5Alignment_segment")
        if not isinstance(self.V1p5Alignment_segment, str):
            self.V1p5Alignment_segment = str(self.V1p5Alignment_segment)

        if self._is_empty(self.V1p5Alignment_call):
            self.MissingRequiredField("V1p5Alignment_call")
        if not isinstance(self.V1p5Alignment_call, str):
            self.V1p5Alignment_call = str(self.V1p5Alignment_call)

        if self._is_empty(self.V1p5Alignment_score):
            self.MissingRequiredField("V1p5Alignment_score")
        if not isinstance(self.V1p5Alignment_score, float):
            self.V1p5Alignment_score = float(self.V1p5Alignment_score)

        if self._is_empty(self.V1p5Alignment_cigar):
            self.MissingRequiredField("V1p5Alignment_cigar")
        if not isinstance(self.V1p5Alignment_cigar, str):
            self.V1p5Alignment_cigar = str(self.V1p5Alignment_cigar)

        if self.V1p5Alignment_rev_comp is not None and not isinstance(self.V1p5Alignment_rev_comp, Bool):
            self.V1p5Alignment_rev_comp = Bool(self.V1p5Alignment_rev_comp)

        if self.V1p5Alignment_identity is not None and not isinstance(self.V1p5Alignment_identity, float):
            self.V1p5Alignment_identity = float(self.V1p5Alignment_identity)

        if self.V1p5Alignment_support is not None and not isinstance(self.V1p5Alignment_support, float):
            self.V1p5Alignment_support = float(self.V1p5Alignment_support)

        if self.V1p5Alignment_sequence_start is not None and not isinstance(self.V1p5Alignment_sequence_start, int):
            self.V1p5Alignment_sequence_start = int(self.V1p5Alignment_sequence_start)

        if self.V1p5Alignment_sequence_end is not None and not isinstance(self.V1p5Alignment_sequence_end, int):
            self.V1p5Alignment_sequence_end = int(self.V1p5Alignment_sequence_end)

        if self.V1p5Alignment_germline_start is not None and not isinstance(self.V1p5Alignment_germline_start, int):
            self.V1p5Alignment_germline_start = int(self.V1p5Alignment_germline_start)

        if self.V1p5Alignment_germline_end is not None and not isinstance(self.V1p5Alignment_germline_end, int):
            self.V1p5Alignment_germline_end = int(self.V1p5Alignment_germline_end)

        if self.V1p5Alignment_rank is not None and not isinstance(self.V1p5Alignment_rank, int):
            self.V1p5Alignment_rank = int(self.V1p5Alignment_rank)

        if self.V1p5Alignment_data_processing_id is not None and not isinstance(self.V1p5Alignment_data_processing_id, str):
            self.V1p5Alignment_data_processing_id = str(self.V1p5Alignment_data_processing_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Rearrangement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Rearrangement"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Rearrangement"
    class_name: ClassVar[str] = "V1p5Rearrangement"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Rearrangement

    V1p5Rearrangement_sequence_id: str = None
    V1p5Rearrangement_sequence: str = None
    V1p5Rearrangement_rev_comp: Union[bool, Bool] = None
    V1p5Rearrangement_productive: Union[bool, Bool] = None
    V1p5Rearrangement_v_call: str = None
    V1p5Rearrangement_d_call: str = None
    V1p5Rearrangement_j_call: str = None
    V1p5Rearrangement_sequence_alignment: str = None
    V1p5Rearrangement_germline_alignment: str = None
    V1p5Rearrangement_junction: str = None
    V1p5Rearrangement_junction_aa: str = None
    V1p5Rearrangement_v_cigar: str = None
    V1p5Rearrangement_d_cigar: str = None
    V1p5Rearrangement_j_cigar: str = None
    V1p5Rearrangement_quality: Optional[str] = None
    V1p5Rearrangement_sequence_aa: Optional[str] = None
    V1p5Rearrangement_vj_in_frame: Optional[Union[bool, Bool]] = None
    V1p5Rearrangement_stop_codon: Optional[Union[bool, Bool]] = None
    V1p5Rearrangement_complete_vdj: Optional[Union[bool, Bool]] = None
    V1p5Rearrangement_locus: Optional[Union[str, "V1p5Locus"]] = None
    V1p5Rearrangement_d2_call: Optional[str] = None
    V1p5Rearrangement_c_call: Optional[str] = None
    V1p5Rearrangement_quality_alignment: Optional[str] = None
    V1p5Rearrangement_sequence_alignment_aa: Optional[str] = None
    V1p5Rearrangement_germline_alignment_aa: Optional[str] = None
    V1p5Rearrangement_np1: Optional[str] = None
    V1p5Rearrangement_np1_aa: Optional[str] = None
    V1p5Rearrangement_np2: Optional[str] = None
    V1p5Rearrangement_np2_aa: Optional[str] = None
    V1p5Rearrangement_np3: Optional[str] = None
    V1p5Rearrangement_np3_aa: Optional[str] = None
    V1p5Rearrangement_cdr1: Optional[str] = None
    V1p5Rearrangement_cdr1_aa: Optional[str] = None
    V1p5Rearrangement_cdr2: Optional[str] = None
    V1p5Rearrangement_cdr2_aa: Optional[str] = None
    V1p5Rearrangement_cdr3: Optional[str] = None
    V1p5Rearrangement_cdr3_aa: Optional[str] = None
    V1p5Rearrangement_fwr1: Optional[str] = None
    V1p5Rearrangement_fwr1_aa: Optional[str] = None
    V1p5Rearrangement_fwr2: Optional[str] = None
    V1p5Rearrangement_fwr2_aa: Optional[str] = None
    V1p5Rearrangement_fwr3: Optional[str] = None
    V1p5Rearrangement_fwr3_aa: Optional[str] = None
    V1p5Rearrangement_fwr4: Optional[str] = None
    V1p5Rearrangement_fwr4_aa: Optional[str] = None
    V1p5Rearrangement_v_score: Optional[float] = None
    V1p5Rearrangement_v_identity: Optional[float] = None
    V1p5Rearrangement_v_support: Optional[float] = None
    V1p5Rearrangement_d_score: Optional[float] = None
    V1p5Rearrangement_d_identity: Optional[float] = None
    V1p5Rearrangement_d_support: Optional[float] = None
    V1p5Rearrangement_d2_score: Optional[float] = None
    V1p5Rearrangement_d2_identity: Optional[float] = None
    V1p5Rearrangement_d2_support: Optional[float] = None
    V1p5Rearrangement_d2_cigar: Optional[str] = None
    V1p5Rearrangement_j_score: Optional[float] = None
    V1p5Rearrangement_j_identity: Optional[float] = None
    V1p5Rearrangement_j_support: Optional[float] = None
    V1p5Rearrangement_c_score: Optional[float] = None
    V1p5Rearrangement_c_identity: Optional[float] = None
    V1p5Rearrangement_c_support: Optional[float] = None
    V1p5Rearrangement_c_cigar: Optional[str] = None
    V1p5Rearrangement_v_sequence_start: Optional[int] = None
    V1p5Rearrangement_v_sequence_end: Optional[int] = None
    V1p5Rearrangement_v_germline_start: Optional[int] = None
    V1p5Rearrangement_v_germline_end: Optional[int] = None
    V1p5Rearrangement_v_alignment_start: Optional[int] = None
    V1p5Rearrangement_v_alignment_end: Optional[int] = None
    V1p5Rearrangement_d_sequence_start: Optional[int] = None
    V1p5Rearrangement_d_sequence_end: Optional[int] = None
    V1p5Rearrangement_d_germline_start: Optional[int] = None
    V1p5Rearrangement_d_germline_end: Optional[int] = None
    V1p5Rearrangement_d_alignment_start: Optional[int] = None
    V1p5Rearrangement_d_alignment_end: Optional[int] = None
    V1p5Rearrangement_d2_sequence_start: Optional[int] = None
    V1p5Rearrangement_d2_sequence_end: Optional[int] = None
    V1p5Rearrangement_d2_germline_start: Optional[int] = None
    V1p5Rearrangement_d2_germline_end: Optional[int] = None
    V1p5Rearrangement_d2_alignment_start: Optional[int] = None
    V1p5Rearrangement_d2_alignment_end: Optional[int] = None
    V1p5Rearrangement_j_sequence_start: Optional[int] = None
    V1p5Rearrangement_j_sequence_end: Optional[int] = None
    V1p5Rearrangement_j_germline_start: Optional[int] = None
    V1p5Rearrangement_j_germline_end: Optional[int] = None
    V1p5Rearrangement_j_alignment_start: Optional[int] = None
    V1p5Rearrangement_j_alignment_end: Optional[int] = None
    V1p5Rearrangement_c_sequence_start: Optional[int] = None
    V1p5Rearrangement_c_sequence_end: Optional[int] = None
    V1p5Rearrangement_c_germline_start: Optional[int] = None
    V1p5Rearrangement_c_germline_end: Optional[int] = None
    V1p5Rearrangement_c_alignment_start: Optional[int] = None
    V1p5Rearrangement_c_alignment_end: Optional[int] = None
    V1p5Rearrangement_cdr1_start: Optional[int] = None
    V1p5Rearrangement_cdr1_end: Optional[int] = None
    V1p5Rearrangement_cdr2_start: Optional[int] = None
    V1p5Rearrangement_cdr2_end: Optional[int] = None
    V1p5Rearrangement_cdr3_start: Optional[int] = None
    V1p5Rearrangement_cdr3_end: Optional[int] = None
    V1p5Rearrangement_fwr1_start: Optional[int] = None
    V1p5Rearrangement_fwr1_end: Optional[int] = None
    V1p5Rearrangement_fwr2_start: Optional[int] = None
    V1p5Rearrangement_fwr2_end: Optional[int] = None
    V1p5Rearrangement_fwr3_start: Optional[int] = None
    V1p5Rearrangement_fwr3_end: Optional[int] = None
    V1p5Rearrangement_fwr4_start: Optional[int] = None
    V1p5Rearrangement_fwr4_end: Optional[int] = None
    V1p5Rearrangement_v_sequence_alignment: Optional[str] = None
    V1p5Rearrangement_v_sequence_alignment_aa: Optional[str] = None
    V1p5Rearrangement_d_sequence_alignment: Optional[str] = None
    V1p5Rearrangement_d_sequence_alignment_aa: Optional[str] = None
    V1p5Rearrangement_d2_sequence_alignment: Optional[str] = None
    V1p5Rearrangement_d2_sequence_alignment_aa: Optional[str] = None
    V1p5Rearrangement_j_sequence_alignment: Optional[str] = None
    V1p5Rearrangement_j_sequence_alignment_aa: Optional[str] = None
    V1p5Rearrangement_c_sequence_alignment: Optional[str] = None
    V1p5Rearrangement_c_sequence_alignment_aa: Optional[str] = None
    V1p5Rearrangement_v_germline_alignment: Optional[str] = None
    V1p5Rearrangement_v_germline_alignment_aa: Optional[str] = None
    V1p5Rearrangement_d_germline_alignment: Optional[str] = None
    V1p5Rearrangement_d_germline_alignment_aa: Optional[str] = None
    V1p5Rearrangement_d2_germline_alignment: Optional[str] = None
    V1p5Rearrangement_d2_germline_alignment_aa: Optional[str] = None
    V1p5Rearrangement_j_germline_alignment: Optional[str] = None
    V1p5Rearrangement_j_germline_alignment_aa: Optional[str] = None
    V1p5Rearrangement_c_germline_alignment: Optional[str] = None
    V1p5Rearrangement_c_germline_alignment_aa: Optional[str] = None
    V1p5Rearrangement_junction_length: Optional[int] = None
    V1p5Rearrangement_junction_aa_length: Optional[int] = None
    V1p5Rearrangement_np1_length: Optional[int] = None
    V1p5Rearrangement_np2_length: Optional[int] = None
    V1p5Rearrangement_np3_length: Optional[int] = None
    V1p5Rearrangement_n1_length: Optional[int] = None
    V1p5Rearrangement_n2_length: Optional[int] = None
    V1p5Rearrangement_n3_length: Optional[int] = None
    V1p5Rearrangement_p3v_length: Optional[int] = None
    V1p5Rearrangement_p5d_length: Optional[int] = None
    V1p5Rearrangement_p3d_length: Optional[int] = None
    V1p5Rearrangement_p5d2_length: Optional[int] = None
    V1p5Rearrangement_p3d2_length: Optional[int] = None
    V1p5Rearrangement_p5j_length: Optional[int] = None
    V1p5Rearrangement_v_frameshift: Optional[Union[bool, Bool]] = None
    V1p5Rearrangement_j_frameshift: Optional[Union[bool, Bool]] = None
    V1p5Rearrangement_d_frame: Optional[int] = None
    V1p5Rearrangement_d2_frame: Optional[int] = None
    V1p5Rearrangement_consensus_count: Optional[int] = None
    V1p5Rearrangement_duplicate_count: Optional[int] = None
    V1p5Rearrangement_umi_count: Optional[int] = None
    V1p5Rearrangement_cell_id: Optional[str] = None
    V1p5Rearrangement_clone_id: Optional[str] = None
    V1p5Rearrangement_repertoire_id: Optional[str] = None
    V1p5Rearrangement_sample_processing_id: Optional[str] = None
    V1p5Rearrangement_data_processing_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5Rearrangement_sequence_id):
            self.MissingRequiredField("V1p5Rearrangement_sequence_id")
        if not isinstance(self.V1p5Rearrangement_sequence_id, str):
            self.V1p5Rearrangement_sequence_id = str(self.V1p5Rearrangement_sequence_id)

        if self._is_empty(self.V1p5Rearrangement_sequence):
            self.MissingRequiredField("V1p5Rearrangement_sequence")
        if not isinstance(self.V1p5Rearrangement_sequence, str):
            self.V1p5Rearrangement_sequence = str(self.V1p5Rearrangement_sequence)

        if self._is_empty(self.V1p5Rearrangement_rev_comp):
            self.MissingRequiredField("V1p5Rearrangement_rev_comp")
        if not isinstance(self.V1p5Rearrangement_rev_comp, Bool):
            self.V1p5Rearrangement_rev_comp = Bool(self.V1p5Rearrangement_rev_comp)

        if self._is_empty(self.V1p5Rearrangement_productive):
            self.MissingRequiredField("V1p5Rearrangement_productive")
        if not isinstance(self.V1p5Rearrangement_productive, Bool):
            self.V1p5Rearrangement_productive = Bool(self.V1p5Rearrangement_productive)

        if self._is_empty(self.V1p5Rearrangement_v_call):
            self.MissingRequiredField("V1p5Rearrangement_v_call")
        if not isinstance(self.V1p5Rearrangement_v_call, str):
            self.V1p5Rearrangement_v_call = str(self.V1p5Rearrangement_v_call)

        if self._is_empty(self.V1p5Rearrangement_d_call):
            self.MissingRequiredField("V1p5Rearrangement_d_call")
        if not isinstance(self.V1p5Rearrangement_d_call, str):
            self.V1p5Rearrangement_d_call = str(self.V1p5Rearrangement_d_call)

        if self._is_empty(self.V1p5Rearrangement_j_call):
            self.MissingRequiredField("V1p5Rearrangement_j_call")
        if not isinstance(self.V1p5Rearrangement_j_call, str):
            self.V1p5Rearrangement_j_call = str(self.V1p5Rearrangement_j_call)

        if self._is_empty(self.V1p5Rearrangement_sequence_alignment):
            self.MissingRequiredField("V1p5Rearrangement_sequence_alignment")
        if not isinstance(self.V1p5Rearrangement_sequence_alignment, str):
            self.V1p5Rearrangement_sequence_alignment = str(self.V1p5Rearrangement_sequence_alignment)

        if self._is_empty(self.V1p5Rearrangement_germline_alignment):
            self.MissingRequiredField("V1p5Rearrangement_germline_alignment")
        if not isinstance(self.V1p5Rearrangement_germline_alignment, str):
            self.V1p5Rearrangement_germline_alignment = str(self.V1p5Rearrangement_germline_alignment)

        if self._is_empty(self.V1p5Rearrangement_junction):
            self.MissingRequiredField("V1p5Rearrangement_junction")
        if not isinstance(self.V1p5Rearrangement_junction, str):
            self.V1p5Rearrangement_junction = str(self.V1p5Rearrangement_junction)

        if self._is_empty(self.V1p5Rearrangement_junction_aa):
            self.MissingRequiredField("V1p5Rearrangement_junction_aa")
        if not isinstance(self.V1p5Rearrangement_junction_aa, str):
            self.V1p5Rearrangement_junction_aa = str(self.V1p5Rearrangement_junction_aa)

        if self._is_empty(self.V1p5Rearrangement_v_cigar):
            self.MissingRequiredField("V1p5Rearrangement_v_cigar")
        if not isinstance(self.V1p5Rearrangement_v_cigar, str):
            self.V1p5Rearrangement_v_cigar = str(self.V1p5Rearrangement_v_cigar)

        if self._is_empty(self.V1p5Rearrangement_d_cigar):
            self.MissingRequiredField("V1p5Rearrangement_d_cigar")
        if not isinstance(self.V1p5Rearrangement_d_cigar, str):
            self.V1p5Rearrangement_d_cigar = str(self.V1p5Rearrangement_d_cigar)

        if self._is_empty(self.V1p5Rearrangement_j_cigar):
            self.MissingRequiredField("V1p5Rearrangement_j_cigar")
        if not isinstance(self.V1p5Rearrangement_j_cigar, str):
            self.V1p5Rearrangement_j_cigar = str(self.V1p5Rearrangement_j_cigar)

        if self.V1p5Rearrangement_quality is not None and not isinstance(self.V1p5Rearrangement_quality, str):
            self.V1p5Rearrangement_quality = str(self.V1p5Rearrangement_quality)

        if self.V1p5Rearrangement_sequence_aa is not None and not isinstance(self.V1p5Rearrangement_sequence_aa, str):
            self.V1p5Rearrangement_sequence_aa = str(self.V1p5Rearrangement_sequence_aa)

        if self.V1p5Rearrangement_vj_in_frame is not None and not isinstance(self.V1p5Rearrangement_vj_in_frame, Bool):
            self.V1p5Rearrangement_vj_in_frame = Bool(self.V1p5Rearrangement_vj_in_frame)

        if self.V1p5Rearrangement_stop_codon is not None and not isinstance(self.V1p5Rearrangement_stop_codon, Bool):
            self.V1p5Rearrangement_stop_codon = Bool(self.V1p5Rearrangement_stop_codon)

        if self.V1p5Rearrangement_complete_vdj is not None and not isinstance(self.V1p5Rearrangement_complete_vdj, Bool):
            self.V1p5Rearrangement_complete_vdj = Bool(self.V1p5Rearrangement_complete_vdj)

        if self.V1p5Rearrangement_locus is not None and not isinstance(self.V1p5Rearrangement_locus, V1p5Locus):
            self.V1p5Rearrangement_locus = V1p5Locus(self.V1p5Rearrangement_locus)

        if self.V1p5Rearrangement_d2_call is not None and not isinstance(self.V1p5Rearrangement_d2_call, str):
            self.V1p5Rearrangement_d2_call = str(self.V1p5Rearrangement_d2_call)

        if self.V1p5Rearrangement_c_call is not None and not isinstance(self.V1p5Rearrangement_c_call, str):
            self.V1p5Rearrangement_c_call = str(self.V1p5Rearrangement_c_call)

        if self.V1p5Rearrangement_quality_alignment is not None and not isinstance(self.V1p5Rearrangement_quality_alignment, str):
            self.V1p5Rearrangement_quality_alignment = str(self.V1p5Rearrangement_quality_alignment)

        if self.V1p5Rearrangement_sequence_alignment_aa is not None and not isinstance(self.V1p5Rearrangement_sequence_alignment_aa, str):
            self.V1p5Rearrangement_sequence_alignment_aa = str(self.V1p5Rearrangement_sequence_alignment_aa)

        if self.V1p5Rearrangement_germline_alignment_aa is not None and not isinstance(self.V1p5Rearrangement_germline_alignment_aa, str):
            self.V1p5Rearrangement_germline_alignment_aa = str(self.V1p5Rearrangement_germline_alignment_aa)

        if self.V1p5Rearrangement_np1 is not None and not isinstance(self.V1p5Rearrangement_np1, str):
            self.V1p5Rearrangement_np1 = str(self.V1p5Rearrangement_np1)

        if self.V1p5Rearrangement_np1_aa is not None and not isinstance(self.V1p5Rearrangement_np1_aa, str):
            self.V1p5Rearrangement_np1_aa = str(self.V1p5Rearrangement_np1_aa)

        if self.V1p5Rearrangement_np2 is not None and not isinstance(self.V1p5Rearrangement_np2, str):
            self.V1p5Rearrangement_np2 = str(self.V1p5Rearrangement_np2)

        if self.V1p5Rearrangement_np2_aa is not None and not isinstance(self.V1p5Rearrangement_np2_aa, str):
            self.V1p5Rearrangement_np2_aa = str(self.V1p5Rearrangement_np2_aa)

        if self.V1p5Rearrangement_np3 is not None and not isinstance(self.V1p5Rearrangement_np3, str):
            self.V1p5Rearrangement_np3 = str(self.V1p5Rearrangement_np3)

        if self.V1p5Rearrangement_np3_aa is not None and not isinstance(self.V1p5Rearrangement_np3_aa, str):
            self.V1p5Rearrangement_np3_aa = str(self.V1p5Rearrangement_np3_aa)

        if self.V1p5Rearrangement_cdr1 is not None and not isinstance(self.V1p5Rearrangement_cdr1, str):
            self.V1p5Rearrangement_cdr1 = str(self.V1p5Rearrangement_cdr1)

        if self.V1p5Rearrangement_cdr1_aa is not None and not isinstance(self.V1p5Rearrangement_cdr1_aa, str):
            self.V1p5Rearrangement_cdr1_aa = str(self.V1p5Rearrangement_cdr1_aa)

        if self.V1p5Rearrangement_cdr2 is not None and not isinstance(self.V1p5Rearrangement_cdr2, str):
            self.V1p5Rearrangement_cdr2 = str(self.V1p5Rearrangement_cdr2)

        if self.V1p5Rearrangement_cdr2_aa is not None and not isinstance(self.V1p5Rearrangement_cdr2_aa, str):
            self.V1p5Rearrangement_cdr2_aa = str(self.V1p5Rearrangement_cdr2_aa)

        if self.V1p5Rearrangement_cdr3 is not None and not isinstance(self.V1p5Rearrangement_cdr3, str):
            self.V1p5Rearrangement_cdr3 = str(self.V1p5Rearrangement_cdr3)

        if self.V1p5Rearrangement_cdr3_aa is not None and not isinstance(self.V1p5Rearrangement_cdr3_aa, str):
            self.V1p5Rearrangement_cdr3_aa = str(self.V1p5Rearrangement_cdr3_aa)

        if self.V1p5Rearrangement_fwr1 is not None and not isinstance(self.V1p5Rearrangement_fwr1, str):
            self.V1p5Rearrangement_fwr1 = str(self.V1p5Rearrangement_fwr1)

        if self.V1p5Rearrangement_fwr1_aa is not None and not isinstance(self.V1p5Rearrangement_fwr1_aa, str):
            self.V1p5Rearrangement_fwr1_aa = str(self.V1p5Rearrangement_fwr1_aa)

        if self.V1p5Rearrangement_fwr2 is not None and not isinstance(self.V1p5Rearrangement_fwr2, str):
            self.V1p5Rearrangement_fwr2 = str(self.V1p5Rearrangement_fwr2)

        if self.V1p5Rearrangement_fwr2_aa is not None and not isinstance(self.V1p5Rearrangement_fwr2_aa, str):
            self.V1p5Rearrangement_fwr2_aa = str(self.V1p5Rearrangement_fwr2_aa)

        if self.V1p5Rearrangement_fwr3 is not None and not isinstance(self.V1p5Rearrangement_fwr3, str):
            self.V1p5Rearrangement_fwr3 = str(self.V1p5Rearrangement_fwr3)

        if self.V1p5Rearrangement_fwr3_aa is not None and not isinstance(self.V1p5Rearrangement_fwr3_aa, str):
            self.V1p5Rearrangement_fwr3_aa = str(self.V1p5Rearrangement_fwr3_aa)

        if self.V1p5Rearrangement_fwr4 is not None and not isinstance(self.V1p5Rearrangement_fwr4, str):
            self.V1p5Rearrangement_fwr4 = str(self.V1p5Rearrangement_fwr4)

        if self.V1p5Rearrangement_fwr4_aa is not None and not isinstance(self.V1p5Rearrangement_fwr4_aa, str):
            self.V1p5Rearrangement_fwr4_aa = str(self.V1p5Rearrangement_fwr4_aa)

        if self.V1p5Rearrangement_v_score is not None and not isinstance(self.V1p5Rearrangement_v_score, float):
            self.V1p5Rearrangement_v_score = float(self.V1p5Rearrangement_v_score)

        if self.V1p5Rearrangement_v_identity is not None and not isinstance(self.V1p5Rearrangement_v_identity, float):
            self.V1p5Rearrangement_v_identity = float(self.V1p5Rearrangement_v_identity)

        if self.V1p5Rearrangement_v_support is not None and not isinstance(self.V1p5Rearrangement_v_support, float):
            self.V1p5Rearrangement_v_support = float(self.V1p5Rearrangement_v_support)

        if self.V1p5Rearrangement_d_score is not None and not isinstance(self.V1p5Rearrangement_d_score, float):
            self.V1p5Rearrangement_d_score = float(self.V1p5Rearrangement_d_score)

        if self.V1p5Rearrangement_d_identity is not None and not isinstance(self.V1p5Rearrangement_d_identity, float):
            self.V1p5Rearrangement_d_identity = float(self.V1p5Rearrangement_d_identity)

        if self.V1p5Rearrangement_d_support is not None and not isinstance(self.V1p5Rearrangement_d_support, float):
            self.V1p5Rearrangement_d_support = float(self.V1p5Rearrangement_d_support)

        if self.V1p5Rearrangement_d2_score is not None and not isinstance(self.V1p5Rearrangement_d2_score, float):
            self.V1p5Rearrangement_d2_score = float(self.V1p5Rearrangement_d2_score)

        if self.V1p5Rearrangement_d2_identity is not None and not isinstance(self.V1p5Rearrangement_d2_identity, float):
            self.V1p5Rearrangement_d2_identity = float(self.V1p5Rearrangement_d2_identity)

        if self.V1p5Rearrangement_d2_support is not None and not isinstance(self.V1p5Rearrangement_d2_support, float):
            self.V1p5Rearrangement_d2_support = float(self.V1p5Rearrangement_d2_support)

        if self.V1p5Rearrangement_d2_cigar is not None and not isinstance(self.V1p5Rearrangement_d2_cigar, str):
            self.V1p5Rearrangement_d2_cigar = str(self.V1p5Rearrangement_d2_cigar)

        if self.V1p5Rearrangement_j_score is not None and not isinstance(self.V1p5Rearrangement_j_score, float):
            self.V1p5Rearrangement_j_score = float(self.V1p5Rearrangement_j_score)

        if self.V1p5Rearrangement_j_identity is not None and not isinstance(self.V1p5Rearrangement_j_identity, float):
            self.V1p5Rearrangement_j_identity = float(self.V1p5Rearrangement_j_identity)

        if self.V1p5Rearrangement_j_support is not None and not isinstance(self.V1p5Rearrangement_j_support, float):
            self.V1p5Rearrangement_j_support = float(self.V1p5Rearrangement_j_support)

        if self.V1p5Rearrangement_c_score is not None and not isinstance(self.V1p5Rearrangement_c_score, float):
            self.V1p5Rearrangement_c_score = float(self.V1p5Rearrangement_c_score)

        if self.V1p5Rearrangement_c_identity is not None and not isinstance(self.V1p5Rearrangement_c_identity, float):
            self.V1p5Rearrangement_c_identity = float(self.V1p5Rearrangement_c_identity)

        if self.V1p5Rearrangement_c_support is not None and not isinstance(self.V1p5Rearrangement_c_support, float):
            self.V1p5Rearrangement_c_support = float(self.V1p5Rearrangement_c_support)

        if self.V1p5Rearrangement_c_cigar is not None and not isinstance(self.V1p5Rearrangement_c_cigar, str):
            self.V1p5Rearrangement_c_cigar = str(self.V1p5Rearrangement_c_cigar)

        if self.V1p5Rearrangement_v_sequence_start is not None and not isinstance(self.V1p5Rearrangement_v_sequence_start, int):
            self.V1p5Rearrangement_v_sequence_start = int(self.V1p5Rearrangement_v_sequence_start)

        if self.V1p5Rearrangement_v_sequence_end is not None and not isinstance(self.V1p5Rearrangement_v_sequence_end, int):
            self.V1p5Rearrangement_v_sequence_end = int(self.V1p5Rearrangement_v_sequence_end)

        if self.V1p5Rearrangement_v_germline_start is not None and not isinstance(self.V1p5Rearrangement_v_germline_start, int):
            self.V1p5Rearrangement_v_germline_start = int(self.V1p5Rearrangement_v_germline_start)

        if self.V1p5Rearrangement_v_germline_end is not None and not isinstance(self.V1p5Rearrangement_v_germline_end, int):
            self.V1p5Rearrangement_v_germline_end = int(self.V1p5Rearrangement_v_germline_end)

        if self.V1p5Rearrangement_v_alignment_start is not None and not isinstance(self.V1p5Rearrangement_v_alignment_start, int):
            self.V1p5Rearrangement_v_alignment_start = int(self.V1p5Rearrangement_v_alignment_start)

        if self.V1p5Rearrangement_v_alignment_end is not None and not isinstance(self.V1p5Rearrangement_v_alignment_end, int):
            self.V1p5Rearrangement_v_alignment_end = int(self.V1p5Rearrangement_v_alignment_end)

        if self.V1p5Rearrangement_d_sequence_start is not None and not isinstance(self.V1p5Rearrangement_d_sequence_start, int):
            self.V1p5Rearrangement_d_sequence_start = int(self.V1p5Rearrangement_d_sequence_start)

        if self.V1p5Rearrangement_d_sequence_end is not None and not isinstance(self.V1p5Rearrangement_d_sequence_end, int):
            self.V1p5Rearrangement_d_sequence_end = int(self.V1p5Rearrangement_d_sequence_end)

        if self.V1p5Rearrangement_d_germline_start is not None and not isinstance(self.V1p5Rearrangement_d_germline_start, int):
            self.V1p5Rearrangement_d_germline_start = int(self.V1p5Rearrangement_d_germline_start)

        if self.V1p5Rearrangement_d_germline_end is not None and not isinstance(self.V1p5Rearrangement_d_germline_end, int):
            self.V1p5Rearrangement_d_germline_end = int(self.V1p5Rearrangement_d_germline_end)

        if self.V1p5Rearrangement_d_alignment_start is not None and not isinstance(self.V1p5Rearrangement_d_alignment_start, int):
            self.V1p5Rearrangement_d_alignment_start = int(self.V1p5Rearrangement_d_alignment_start)

        if self.V1p5Rearrangement_d_alignment_end is not None and not isinstance(self.V1p5Rearrangement_d_alignment_end, int):
            self.V1p5Rearrangement_d_alignment_end = int(self.V1p5Rearrangement_d_alignment_end)

        if self.V1p5Rearrangement_d2_sequence_start is not None and not isinstance(self.V1p5Rearrangement_d2_sequence_start, int):
            self.V1p5Rearrangement_d2_sequence_start = int(self.V1p5Rearrangement_d2_sequence_start)

        if self.V1p5Rearrangement_d2_sequence_end is not None and not isinstance(self.V1p5Rearrangement_d2_sequence_end, int):
            self.V1p5Rearrangement_d2_sequence_end = int(self.V1p5Rearrangement_d2_sequence_end)

        if self.V1p5Rearrangement_d2_germline_start is not None and not isinstance(self.V1p5Rearrangement_d2_germline_start, int):
            self.V1p5Rearrangement_d2_germline_start = int(self.V1p5Rearrangement_d2_germline_start)

        if self.V1p5Rearrangement_d2_germline_end is not None and not isinstance(self.V1p5Rearrangement_d2_germline_end, int):
            self.V1p5Rearrangement_d2_germline_end = int(self.V1p5Rearrangement_d2_germline_end)

        if self.V1p5Rearrangement_d2_alignment_start is not None and not isinstance(self.V1p5Rearrangement_d2_alignment_start, int):
            self.V1p5Rearrangement_d2_alignment_start = int(self.V1p5Rearrangement_d2_alignment_start)

        if self.V1p5Rearrangement_d2_alignment_end is not None and not isinstance(self.V1p5Rearrangement_d2_alignment_end, int):
            self.V1p5Rearrangement_d2_alignment_end = int(self.V1p5Rearrangement_d2_alignment_end)

        if self.V1p5Rearrangement_j_sequence_start is not None and not isinstance(self.V1p5Rearrangement_j_sequence_start, int):
            self.V1p5Rearrangement_j_sequence_start = int(self.V1p5Rearrangement_j_sequence_start)

        if self.V1p5Rearrangement_j_sequence_end is not None and not isinstance(self.V1p5Rearrangement_j_sequence_end, int):
            self.V1p5Rearrangement_j_sequence_end = int(self.V1p5Rearrangement_j_sequence_end)

        if self.V1p5Rearrangement_j_germline_start is not None and not isinstance(self.V1p5Rearrangement_j_germline_start, int):
            self.V1p5Rearrangement_j_germline_start = int(self.V1p5Rearrangement_j_germline_start)

        if self.V1p5Rearrangement_j_germline_end is not None and not isinstance(self.V1p5Rearrangement_j_germline_end, int):
            self.V1p5Rearrangement_j_germline_end = int(self.V1p5Rearrangement_j_germline_end)

        if self.V1p5Rearrangement_j_alignment_start is not None and not isinstance(self.V1p5Rearrangement_j_alignment_start, int):
            self.V1p5Rearrangement_j_alignment_start = int(self.V1p5Rearrangement_j_alignment_start)

        if self.V1p5Rearrangement_j_alignment_end is not None and not isinstance(self.V1p5Rearrangement_j_alignment_end, int):
            self.V1p5Rearrangement_j_alignment_end = int(self.V1p5Rearrangement_j_alignment_end)

        if self.V1p5Rearrangement_c_sequence_start is not None and not isinstance(self.V1p5Rearrangement_c_sequence_start, int):
            self.V1p5Rearrangement_c_sequence_start = int(self.V1p5Rearrangement_c_sequence_start)

        if self.V1p5Rearrangement_c_sequence_end is not None and not isinstance(self.V1p5Rearrangement_c_sequence_end, int):
            self.V1p5Rearrangement_c_sequence_end = int(self.V1p5Rearrangement_c_sequence_end)

        if self.V1p5Rearrangement_c_germline_start is not None and not isinstance(self.V1p5Rearrangement_c_germline_start, int):
            self.V1p5Rearrangement_c_germline_start = int(self.V1p5Rearrangement_c_germline_start)

        if self.V1p5Rearrangement_c_germline_end is not None and not isinstance(self.V1p5Rearrangement_c_germline_end, int):
            self.V1p5Rearrangement_c_germline_end = int(self.V1p5Rearrangement_c_germline_end)

        if self.V1p5Rearrangement_c_alignment_start is not None and not isinstance(self.V1p5Rearrangement_c_alignment_start, int):
            self.V1p5Rearrangement_c_alignment_start = int(self.V1p5Rearrangement_c_alignment_start)

        if self.V1p5Rearrangement_c_alignment_end is not None and not isinstance(self.V1p5Rearrangement_c_alignment_end, int):
            self.V1p5Rearrangement_c_alignment_end = int(self.V1p5Rearrangement_c_alignment_end)

        if self.V1p5Rearrangement_cdr1_start is not None and not isinstance(self.V1p5Rearrangement_cdr1_start, int):
            self.V1p5Rearrangement_cdr1_start = int(self.V1p5Rearrangement_cdr1_start)

        if self.V1p5Rearrangement_cdr1_end is not None and not isinstance(self.V1p5Rearrangement_cdr1_end, int):
            self.V1p5Rearrangement_cdr1_end = int(self.V1p5Rearrangement_cdr1_end)

        if self.V1p5Rearrangement_cdr2_start is not None and not isinstance(self.V1p5Rearrangement_cdr2_start, int):
            self.V1p5Rearrangement_cdr2_start = int(self.V1p5Rearrangement_cdr2_start)

        if self.V1p5Rearrangement_cdr2_end is not None and not isinstance(self.V1p5Rearrangement_cdr2_end, int):
            self.V1p5Rearrangement_cdr2_end = int(self.V1p5Rearrangement_cdr2_end)

        if self.V1p5Rearrangement_cdr3_start is not None and not isinstance(self.V1p5Rearrangement_cdr3_start, int):
            self.V1p5Rearrangement_cdr3_start = int(self.V1p5Rearrangement_cdr3_start)

        if self.V1p5Rearrangement_cdr3_end is not None and not isinstance(self.V1p5Rearrangement_cdr3_end, int):
            self.V1p5Rearrangement_cdr3_end = int(self.V1p5Rearrangement_cdr3_end)

        if self.V1p5Rearrangement_fwr1_start is not None and not isinstance(self.V1p5Rearrangement_fwr1_start, int):
            self.V1p5Rearrangement_fwr1_start = int(self.V1p5Rearrangement_fwr1_start)

        if self.V1p5Rearrangement_fwr1_end is not None and not isinstance(self.V1p5Rearrangement_fwr1_end, int):
            self.V1p5Rearrangement_fwr1_end = int(self.V1p5Rearrangement_fwr1_end)

        if self.V1p5Rearrangement_fwr2_start is not None and not isinstance(self.V1p5Rearrangement_fwr2_start, int):
            self.V1p5Rearrangement_fwr2_start = int(self.V1p5Rearrangement_fwr2_start)

        if self.V1p5Rearrangement_fwr2_end is not None and not isinstance(self.V1p5Rearrangement_fwr2_end, int):
            self.V1p5Rearrangement_fwr2_end = int(self.V1p5Rearrangement_fwr2_end)

        if self.V1p5Rearrangement_fwr3_start is not None and not isinstance(self.V1p5Rearrangement_fwr3_start, int):
            self.V1p5Rearrangement_fwr3_start = int(self.V1p5Rearrangement_fwr3_start)

        if self.V1p5Rearrangement_fwr3_end is not None and not isinstance(self.V1p5Rearrangement_fwr3_end, int):
            self.V1p5Rearrangement_fwr3_end = int(self.V1p5Rearrangement_fwr3_end)

        if self.V1p5Rearrangement_fwr4_start is not None and not isinstance(self.V1p5Rearrangement_fwr4_start, int):
            self.V1p5Rearrangement_fwr4_start = int(self.V1p5Rearrangement_fwr4_start)

        if self.V1p5Rearrangement_fwr4_end is not None and not isinstance(self.V1p5Rearrangement_fwr4_end, int):
            self.V1p5Rearrangement_fwr4_end = int(self.V1p5Rearrangement_fwr4_end)

        if self.V1p5Rearrangement_v_sequence_alignment is not None and not isinstance(self.V1p5Rearrangement_v_sequence_alignment, str):
            self.V1p5Rearrangement_v_sequence_alignment = str(self.V1p5Rearrangement_v_sequence_alignment)

        if self.V1p5Rearrangement_v_sequence_alignment_aa is not None and not isinstance(self.V1p5Rearrangement_v_sequence_alignment_aa, str):
            self.V1p5Rearrangement_v_sequence_alignment_aa = str(self.V1p5Rearrangement_v_sequence_alignment_aa)

        if self.V1p5Rearrangement_d_sequence_alignment is not None and not isinstance(self.V1p5Rearrangement_d_sequence_alignment, str):
            self.V1p5Rearrangement_d_sequence_alignment = str(self.V1p5Rearrangement_d_sequence_alignment)

        if self.V1p5Rearrangement_d_sequence_alignment_aa is not None and not isinstance(self.V1p5Rearrangement_d_sequence_alignment_aa, str):
            self.V1p5Rearrangement_d_sequence_alignment_aa = str(self.V1p5Rearrangement_d_sequence_alignment_aa)

        if self.V1p5Rearrangement_d2_sequence_alignment is not None and not isinstance(self.V1p5Rearrangement_d2_sequence_alignment, str):
            self.V1p5Rearrangement_d2_sequence_alignment = str(self.V1p5Rearrangement_d2_sequence_alignment)

        if self.V1p5Rearrangement_d2_sequence_alignment_aa is not None and not isinstance(self.V1p5Rearrangement_d2_sequence_alignment_aa, str):
            self.V1p5Rearrangement_d2_sequence_alignment_aa = str(self.V1p5Rearrangement_d2_sequence_alignment_aa)

        if self.V1p5Rearrangement_j_sequence_alignment is not None and not isinstance(self.V1p5Rearrangement_j_sequence_alignment, str):
            self.V1p5Rearrangement_j_sequence_alignment = str(self.V1p5Rearrangement_j_sequence_alignment)

        if self.V1p5Rearrangement_j_sequence_alignment_aa is not None and not isinstance(self.V1p5Rearrangement_j_sequence_alignment_aa, str):
            self.V1p5Rearrangement_j_sequence_alignment_aa = str(self.V1p5Rearrangement_j_sequence_alignment_aa)

        if self.V1p5Rearrangement_c_sequence_alignment is not None and not isinstance(self.V1p5Rearrangement_c_sequence_alignment, str):
            self.V1p5Rearrangement_c_sequence_alignment = str(self.V1p5Rearrangement_c_sequence_alignment)

        if self.V1p5Rearrangement_c_sequence_alignment_aa is not None and not isinstance(self.V1p5Rearrangement_c_sequence_alignment_aa, str):
            self.V1p5Rearrangement_c_sequence_alignment_aa = str(self.V1p5Rearrangement_c_sequence_alignment_aa)

        if self.V1p5Rearrangement_v_germline_alignment is not None and not isinstance(self.V1p5Rearrangement_v_germline_alignment, str):
            self.V1p5Rearrangement_v_germline_alignment = str(self.V1p5Rearrangement_v_germline_alignment)

        if self.V1p5Rearrangement_v_germline_alignment_aa is not None and not isinstance(self.V1p5Rearrangement_v_germline_alignment_aa, str):
            self.V1p5Rearrangement_v_germline_alignment_aa = str(self.V1p5Rearrangement_v_germline_alignment_aa)

        if self.V1p5Rearrangement_d_germline_alignment is not None and not isinstance(self.V1p5Rearrangement_d_germline_alignment, str):
            self.V1p5Rearrangement_d_germline_alignment = str(self.V1p5Rearrangement_d_germline_alignment)

        if self.V1p5Rearrangement_d_germline_alignment_aa is not None and not isinstance(self.V1p5Rearrangement_d_germline_alignment_aa, str):
            self.V1p5Rearrangement_d_germline_alignment_aa = str(self.V1p5Rearrangement_d_germline_alignment_aa)

        if self.V1p5Rearrangement_d2_germline_alignment is not None and not isinstance(self.V1p5Rearrangement_d2_germline_alignment, str):
            self.V1p5Rearrangement_d2_germline_alignment = str(self.V1p5Rearrangement_d2_germline_alignment)

        if self.V1p5Rearrangement_d2_germline_alignment_aa is not None and not isinstance(self.V1p5Rearrangement_d2_germline_alignment_aa, str):
            self.V1p5Rearrangement_d2_germline_alignment_aa = str(self.V1p5Rearrangement_d2_germline_alignment_aa)

        if self.V1p5Rearrangement_j_germline_alignment is not None and not isinstance(self.V1p5Rearrangement_j_germline_alignment, str):
            self.V1p5Rearrangement_j_germline_alignment = str(self.V1p5Rearrangement_j_germline_alignment)

        if self.V1p5Rearrangement_j_germline_alignment_aa is not None and not isinstance(self.V1p5Rearrangement_j_germline_alignment_aa, str):
            self.V1p5Rearrangement_j_germline_alignment_aa = str(self.V1p5Rearrangement_j_germline_alignment_aa)

        if self.V1p5Rearrangement_c_germline_alignment is not None and not isinstance(self.V1p5Rearrangement_c_germline_alignment, str):
            self.V1p5Rearrangement_c_germline_alignment = str(self.V1p5Rearrangement_c_germline_alignment)

        if self.V1p5Rearrangement_c_germline_alignment_aa is not None and not isinstance(self.V1p5Rearrangement_c_germline_alignment_aa, str):
            self.V1p5Rearrangement_c_germline_alignment_aa = str(self.V1p5Rearrangement_c_germline_alignment_aa)

        if self.V1p5Rearrangement_junction_length is not None and not isinstance(self.V1p5Rearrangement_junction_length, int):
            self.V1p5Rearrangement_junction_length = int(self.V1p5Rearrangement_junction_length)

        if self.V1p5Rearrangement_junction_aa_length is not None and not isinstance(self.V1p5Rearrangement_junction_aa_length, int):
            self.V1p5Rearrangement_junction_aa_length = int(self.V1p5Rearrangement_junction_aa_length)

        if self.V1p5Rearrangement_np1_length is not None and not isinstance(self.V1p5Rearrangement_np1_length, int):
            self.V1p5Rearrangement_np1_length = int(self.V1p5Rearrangement_np1_length)

        if self.V1p5Rearrangement_np2_length is not None and not isinstance(self.V1p5Rearrangement_np2_length, int):
            self.V1p5Rearrangement_np2_length = int(self.V1p5Rearrangement_np2_length)

        if self.V1p5Rearrangement_np3_length is not None and not isinstance(self.V1p5Rearrangement_np3_length, int):
            self.V1p5Rearrangement_np3_length = int(self.V1p5Rearrangement_np3_length)

        if self.V1p5Rearrangement_n1_length is not None and not isinstance(self.V1p5Rearrangement_n1_length, int):
            self.V1p5Rearrangement_n1_length = int(self.V1p5Rearrangement_n1_length)

        if self.V1p5Rearrangement_n2_length is not None and not isinstance(self.V1p5Rearrangement_n2_length, int):
            self.V1p5Rearrangement_n2_length = int(self.V1p5Rearrangement_n2_length)

        if self.V1p5Rearrangement_n3_length is not None and not isinstance(self.V1p5Rearrangement_n3_length, int):
            self.V1p5Rearrangement_n3_length = int(self.V1p5Rearrangement_n3_length)

        if self.V1p5Rearrangement_p3v_length is not None and not isinstance(self.V1p5Rearrangement_p3v_length, int):
            self.V1p5Rearrangement_p3v_length = int(self.V1p5Rearrangement_p3v_length)

        if self.V1p5Rearrangement_p5d_length is not None and not isinstance(self.V1p5Rearrangement_p5d_length, int):
            self.V1p5Rearrangement_p5d_length = int(self.V1p5Rearrangement_p5d_length)

        if self.V1p5Rearrangement_p3d_length is not None and not isinstance(self.V1p5Rearrangement_p3d_length, int):
            self.V1p5Rearrangement_p3d_length = int(self.V1p5Rearrangement_p3d_length)

        if self.V1p5Rearrangement_p5d2_length is not None and not isinstance(self.V1p5Rearrangement_p5d2_length, int):
            self.V1p5Rearrangement_p5d2_length = int(self.V1p5Rearrangement_p5d2_length)

        if self.V1p5Rearrangement_p3d2_length is not None and not isinstance(self.V1p5Rearrangement_p3d2_length, int):
            self.V1p5Rearrangement_p3d2_length = int(self.V1p5Rearrangement_p3d2_length)

        if self.V1p5Rearrangement_p5j_length is not None and not isinstance(self.V1p5Rearrangement_p5j_length, int):
            self.V1p5Rearrangement_p5j_length = int(self.V1p5Rearrangement_p5j_length)

        if self.V1p5Rearrangement_v_frameshift is not None and not isinstance(self.V1p5Rearrangement_v_frameshift, Bool):
            self.V1p5Rearrangement_v_frameshift = Bool(self.V1p5Rearrangement_v_frameshift)

        if self.V1p5Rearrangement_j_frameshift is not None and not isinstance(self.V1p5Rearrangement_j_frameshift, Bool):
            self.V1p5Rearrangement_j_frameshift = Bool(self.V1p5Rearrangement_j_frameshift)

        if self.V1p5Rearrangement_d_frame is not None and not isinstance(self.V1p5Rearrangement_d_frame, int):
            self.V1p5Rearrangement_d_frame = int(self.V1p5Rearrangement_d_frame)

        if self.V1p5Rearrangement_d2_frame is not None and not isinstance(self.V1p5Rearrangement_d2_frame, int):
            self.V1p5Rearrangement_d2_frame = int(self.V1p5Rearrangement_d2_frame)

        if self.V1p5Rearrangement_consensus_count is not None and not isinstance(self.V1p5Rearrangement_consensus_count, int):
            self.V1p5Rearrangement_consensus_count = int(self.V1p5Rearrangement_consensus_count)

        if self.V1p5Rearrangement_duplicate_count is not None and not isinstance(self.V1p5Rearrangement_duplicate_count, int):
            self.V1p5Rearrangement_duplicate_count = int(self.V1p5Rearrangement_duplicate_count)

        if self.V1p5Rearrangement_umi_count is not None and not isinstance(self.V1p5Rearrangement_umi_count, int):
            self.V1p5Rearrangement_umi_count = int(self.V1p5Rearrangement_umi_count)

        if self.V1p5Rearrangement_cell_id is not None and not isinstance(self.V1p5Rearrangement_cell_id, str):
            self.V1p5Rearrangement_cell_id = str(self.V1p5Rearrangement_cell_id)

        if self.V1p5Rearrangement_clone_id is not None and not isinstance(self.V1p5Rearrangement_clone_id, str):
            self.V1p5Rearrangement_clone_id = str(self.V1p5Rearrangement_clone_id)

        if self.V1p5Rearrangement_repertoire_id is not None and not isinstance(self.V1p5Rearrangement_repertoire_id, str):
            self.V1p5Rearrangement_repertoire_id = str(self.V1p5Rearrangement_repertoire_id)

        if self.V1p5Rearrangement_sample_processing_id is not None and not isinstance(self.V1p5Rearrangement_sample_processing_id, str):
            self.V1p5Rearrangement_sample_processing_id = str(self.V1p5Rearrangement_sample_processing_id)

        if self.V1p5Rearrangement_data_processing_id is not None and not isinstance(self.V1p5Rearrangement_data_processing_id, str):
            self.V1p5Rearrangement_data_processing_id = str(self.V1p5Rearrangement_data_processing_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Clone(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Clone"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Clone"
    class_name: ClassVar[str] = "V1p5Clone"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Clone

    V1p5Clone_clone_id: str = None
    V1p5Clone_germline_alignment: str = None
    V1p5Clone_repertoire_id: Optional[str] = None
    V1p5Clone_data_processing_id: Optional[str] = None
    V1p5Clone_sequences: Optional[Union[str, List[str]]] = empty_list()
    V1p5Clone_v_call: Optional[str] = None
    V1p5Clone_d_call: Optional[str] = None
    V1p5Clone_j_call: Optional[str] = None
    V1p5Clone_junction: Optional[str] = None
    V1p5Clone_junction_aa: Optional[str] = None
    V1p5Clone_junction_length: Optional[int] = None
    V1p5Clone_junction_aa_length: Optional[int] = None
    V1p5Clone_germline_alignment_aa: Optional[str] = None
    V1p5Clone_v_alignment_start: Optional[int] = None
    V1p5Clone_v_alignment_end: Optional[int] = None
    V1p5Clone_d_alignment_start: Optional[int] = None
    V1p5Clone_d_alignment_end: Optional[int] = None
    V1p5Clone_j_alignment_start: Optional[int] = None
    V1p5Clone_j_alignment_end: Optional[int] = None
    V1p5Clone_junction_start: Optional[int] = None
    V1p5Clone_junction_end: Optional[int] = None
    V1p5Clone_umi_count: Optional[int] = None
    V1p5Clone_clone_count: Optional[int] = None
    V1p5Clone_seed_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5Clone_clone_id):
            self.MissingRequiredField("V1p5Clone_clone_id")
        if not isinstance(self.V1p5Clone_clone_id, str):
            self.V1p5Clone_clone_id = str(self.V1p5Clone_clone_id)

        if self._is_empty(self.V1p5Clone_germline_alignment):
            self.MissingRequiredField("V1p5Clone_germline_alignment")
        if not isinstance(self.V1p5Clone_germline_alignment, str):
            self.V1p5Clone_germline_alignment = str(self.V1p5Clone_germline_alignment)

        if self.V1p5Clone_repertoire_id is not None and not isinstance(self.V1p5Clone_repertoire_id, str):
            self.V1p5Clone_repertoire_id = str(self.V1p5Clone_repertoire_id)

        if self.V1p5Clone_data_processing_id is not None and not isinstance(self.V1p5Clone_data_processing_id, str):
            self.V1p5Clone_data_processing_id = str(self.V1p5Clone_data_processing_id)

        if not isinstance(self.V1p5Clone_sequences, list):
            self.V1p5Clone_sequences = [self.V1p5Clone_sequences] if self.V1p5Clone_sequences is not None else []
        self.V1p5Clone_sequences = [v if isinstance(v, str) else str(v) for v in self.V1p5Clone_sequences]

        if self.V1p5Clone_v_call is not None and not isinstance(self.V1p5Clone_v_call, str):
            self.V1p5Clone_v_call = str(self.V1p5Clone_v_call)

        if self.V1p5Clone_d_call is not None and not isinstance(self.V1p5Clone_d_call, str):
            self.V1p5Clone_d_call = str(self.V1p5Clone_d_call)

        if self.V1p5Clone_j_call is not None and not isinstance(self.V1p5Clone_j_call, str):
            self.V1p5Clone_j_call = str(self.V1p5Clone_j_call)

        if self.V1p5Clone_junction is not None and not isinstance(self.V1p5Clone_junction, str):
            self.V1p5Clone_junction = str(self.V1p5Clone_junction)

        if self.V1p5Clone_junction_aa is not None and not isinstance(self.V1p5Clone_junction_aa, str):
            self.V1p5Clone_junction_aa = str(self.V1p5Clone_junction_aa)

        if self.V1p5Clone_junction_length is not None and not isinstance(self.V1p5Clone_junction_length, int):
            self.V1p5Clone_junction_length = int(self.V1p5Clone_junction_length)

        if self.V1p5Clone_junction_aa_length is not None and not isinstance(self.V1p5Clone_junction_aa_length, int):
            self.V1p5Clone_junction_aa_length = int(self.V1p5Clone_junction_aa_length)

        if self.V1p5Clone_germline_alignment_aa is not None and not isinstance(self.V1p5Clone_germline_alignment_aa, str):
            self.V1p5Clone_germline_alignment_aa = str(self.V1p5Clone_germline_alignment_aa)

        if self.V1p5Clone_v_alignment_start is not None and not isinstance(self.V1p5Clone_v_alignment_start, int):
            self.V1p5Clone_v_alignment_start = int(self.V1p5Clone_v_alignment_start)

        if self.V1p5Clone_v_alignment_end is not None and not isinstance(self.V1p5Clone_v_alignment_end, int):
            self.V1p5Clone_v_alignment_end = int(self.V1p5Clone_v_alignment_end)

        if self.V1p5Clone_d_alignment_start is not None and not isinstance(self.V1p5Clone_d_alignment_start, int):
            self.V1p5Clone_d_alignment_start = int(self.V1p5Clone_d_alignment_start)

        if self.V1p5Clone_d_alignment_end is not None and not isinstance(self.V1p5Clone_d_alignment_end, int):
            self.V1p5Clone_d_alignment_end = int(self.V1p5Clone_d_alignment_end)

        if self.V1p5Clone_j_alignment_start is not None and not isinstance(self.V1p5Clone_j_alignment_start, int):
            self.V1p5Clone_j_alignment_start = int(self.V1p5Clone_j_alignment_start)

        if self.V1p5Clone_j_alignment_end is not None and not isinstance(self.V1p5Clone_j_alignment_end, int):
            self.V1p5Clone_j_alignment_end = int(self.V1p5Clone_j_alignment_end)

        if self.V1p5Clone_junction_start is not None and not isinstance(self.V1p5Clone_junction_start, int):
            self.V1p5Clone_junction_start = int(self.V1p5Clone_junction_start)

        if self.V1p5Clone_junction_end is not None and not isinstance(self.V1p5Clone_junction_end, int):
            self.V1p5Clone_junction_end = int(self.V1p5Clone_junction_end)

        if self.V1p5Clone_umi_count is not None and not isinstance(self.V1p5Clone_umi_count, int):
            self.V1p5Clone_umi_count = int(self.V1p5Clone_umi_count)

        if self.V1p5Clone_clone_count is not None and not isinstance(self.V1p5Clone_clone_count, int):
            self.V1p5Clone_clone_count = int(self.V1p5Clone_clone_count)

        if self.V1p5Clone_seed_id is not None and not isinstance(self.V1p5Clone_seed_id, str):
            self.V1p5Clone_seed_id = str(self.V1p5Clone_seed_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Tree(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Tree"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Tree"
    class_name: ClassVar[str] = "V1p5Tree"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Tree

    V1p5Tree_tree_id: str = None
    V1p5Tree_clone_id: str = None
    V1p5Tree_newick: str = None
    V1p5Tree_nodes: Optional[Union[Union[dict, "V1p5Node"], List[Union[dict, "V1p5Node"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5Tree_tree_id):
            self.MissingRequiredField("V1p5Tree_tree_id")
        if not isinstance(self.V1p5Tree_tree_id, str):
            self.V1p5Tree_tree_id = str(self.V1p5Tree_tree_id)

        if self._is_empty(self.V1p5Tree_clone_id):
            self.MissingRequiredField("V1p5Tree_clone_id")
        if not isinstance(self.V1p5Tree_clone_id, str):
            self.V1p5Tree_clone_id = str(self.V1p5Tree_clone_id)

        if self._is_empty(self.V1p5Tree_newick):
            self.MissingRequiredField("V1p5Tree_newick")
        if not isinstance(self.V1p5Tree_newick, str):
            self.V1p5Tree_newick = str(self.V1p5Tree_newick)

        self._normalize_inlined_as_dict(slot_name="V1p5Tree_nodes", slot_type=V1p5Node, key_name="V1p5Node_sequence_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Node(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Node"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Node"
    class_name: ClassVar[str] = "V1p5Node"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Node

    V1p5Node_sequence_id: str = None
    V1p5Node_sequence_alignment: Optional[str] = None
    V1p5Node_junction: Optional[str] = None
    V1p5Node_junction_aa: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5Node_sequence_id):
            self.MissingRequiredField("V1p5Node_sequence_id")
        if not isinstance(self.V1p5Node_sequence_id, str):
            self.V1p5Node_sequence_id = str(self.V1p5Node_sequence_id)

        if self.V1p5Node_sequence_alignment is not None and not isinstance(self.V1p5Node_sequence_alignment, str):
            self.V1p5Node_sequence_alignment = str(self.V1p5Node_sequence_alignment)

        if self.V1p5Node_junction is not None and not isinstance(self.V1p5Node_junction, str):
            self.V1p5Node_junction = str(self.V1p5Node_junction)

        if self.V1p5Node_junction_aa is not None and not isinstance(self.V1p5Node_junction_aa, str):
            self.V1p5Node_junction_aa = str(self.V1p5Node_junction_aa)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Cell(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Cell"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Cell"
    class_name: ClassVar[str] = "V1p5Cell"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Cell

    V1p5Cell_cell_id: str = None
    V1p5Cell_rearrangements: Union[str, List[str]] = None
    V1p5Cell_repertoire_id: str = None
    V1p5Cell_virtual_pairing: Union[bool, Bool] = None
    V1p5Cell_receptors: Optional[Union[str, List[str]]] = empty_list()
    V1p5Cell_data_processing_id: Optional[str] = None
    V1p5Cell_expression_study_method: Optional[Union[str, "V1p5ExpressionStudyMethod"]] = None
    V1p5Cell_expression_raw_doi: Optional[str] = None
    V1p5Cell_expression_index: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5Cell_cell_id):
            self.MissingRequiredField("V1p5Cell_cell_id")
        if not isinstance(self.V1p5Cell_cell_id, str):
            self.V1p5Cell_cell_id = str(self.V1p5Cell_cell_id)

        if self._is_empty(self.V1p5Cell_rearrangements):
            self.MissingRequiredField("V1p5Cell_rearrangements")
        if not isinstance(self.V1p5Cell_rearrangements, list):
            self.V1p5Cell_rearrangements = [self.V1p5Cell_rearrangements] if self.V1p5Cell_rearrangements is not None else []
        self.V1p5Cell_rearrangements = [v if isinstance(v, str) else str(v) for v in self.V1p5Cell_rearrangements]

        if self._is_empty(self.V1p5Cell_repertoire_id):
            self.MissingRequiredField("V1p5Cell_repertoire_id")
        if not isinstance(self.V1p5Cell_repertoire_id, str):
            self.V1p5Cell_repertoire_id = str(self.V1p5Cell_repertoire_id)

        if self._is_empty(self.V1p5Cell_virtual_pairing):
            self.MissingRequiredField("V1p5Cell_virtual_pairing")
        if not isinstance(self.V1p5Cell_virtual_pairing, Bool):
            self.V1p5Cell_virtual_pairing = Bool(self.V1p5Cell_virtual_pairing)

        if not isinstance(self.V1p5Cell_receptors, list):
            self.V1p5Cell_receptors = [self.V1p5Cell_receptors] if self.V1p5Cell_receptors is not None else []
        self.V1p5Cell_receptors = [v if isinstance(v, str) else str(v) for v in self.V1p5Cell_receptors]

        if self.V1p5Cell_data_processing_id is not None and not isinstance(self.V1p5Cell_data_processing_id, str):
            self.V1p5Cell_data_processing_id = str(self.V1p5Cell_data_processing_id)

        if self.V1p5Cell_expression_study_method is not None and not isinstance(self.V1p5Cell_expression_study_method, V1p5ExpressionStudyMethod):
            self.V1p5Cell_expression_study_method = V1p5ExpressionStudyMethod(self.V1p5Cell_expression_study_method)

        if self.V1p5Cell_expression_raw_doi is not None and not isinstance(self.V1p5Cell_expression_raw_doi, str):
            self.V1p5Cell_expression_raw_doi = str(self.V1p5Cell_expression_raw_doi)

        if self.V1p5Cell_expression_index is not None and not isinstance(self.V1p5Cell_expression_index, str):
            self.V1p5Cell_expression_index = str(self.V1p5Cell_expression_index)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5CellExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5CellExpression"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5CellExpression"
    class_name: ClassVar[str] = "V1p5CellExpression"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5CellExpression

    V1p5CellExpression_expression_id: str = None
    V1p5CellExpression_cell_id: str = None
    V1p5CellExpression_repertoire_id: str = None
    V1p5CellExpression_data_processing_id: str = None
    V1p5CellExpression_property_type: str = None
    V1p5CellExpression_property: Union[str, "V1p5Property"] = None
    V1p5CellExpression_value: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5CellExpression_expression_id):
            self.MissingRequiredField("V1p5CellExpression_expression_id")
        if not isinstance(self.V1p5CellExpression_expression_id, str):
            self.V1p5CellExpression_expression_id = str(self.V1p5CellExpression_expression_id)

        if self._is_empty(self.V1p5CellExpression_cell_id):
            self.MissingRequiredField("V1p5CellExpression_cell_id")
        if not isinstance(self.V1p5CellExpression_cell_id, str):
            self.V1p5CellExpression_cell_id = str(self.V1p5CellExpression_cell_id)

        if self._is_empty(self.V1p5CellExpression_repertoire_id):
            self.MissingRequiredField("V1p5CellExpression_repertoire_id")
        if not isinstance(self.V1p5CellExpression_repertoire_id, str):
            self.V1p5CellExpression_repertoire_id = str(self.V1p5CellExpression_repertoire_id)

        if self._is_empty(self.V1p5CellExpression_data_processing_id):
            self.MissingRequiredField("V1p5CellExpression_data_processing_id")
        if not isinstance(self.V1p5CellExpression_data_processing_id, str):
            self.V1p5CellExpression_data_processing_id = str(self.V1p5CellExpression_data_processing_id)

        if self._is_empty(self.V1p5CellExpression_property_type):
            self.MissingRequiredField("V1p5CellExpression_property_type")
        if not isinstance(self.V1p5CellExpression_property_type, str):
            self.V1p5CellExpression_property_type = str(self.V1p5CellExpression_property_type)

        if self._is_empty(self.V1p5CellExpression_value):
            self.MissingRequiredField("V1p5CellExpression_value")
        if not isinstance(self.V1p5CellExpression_value, float):
            self.V1p5CellExpression_value = float(self.V1p5CellExpression_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5Receptor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5Receptor"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5Receptor"
    class_name: ClassVar[str] = "V1p5Receptor"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5Receptor

    V1p5Receptor_receptor_id: str = None
    V1p5Receptor_receptor_hash: str = None
    V1p5Receptor_receptor_type: Union[str, "V1p5ReceptorType"] = None
    V1p5Receptor_receptor_variable_domain_1_aa: str = None
    V1p5Receptor_receptor_variable_domain_1_locus: Union[str, "V1p5ReceptorVariableDomain1Locus"] = None
    V1p5Receptor_receptor_variable_domain_2_aa: str = None
    V1p5Receptor_receptor_variable_domain_2_locus: Union[str, "V1p5ReceptorVariableDomain2Locus"] = None
    V1p5Receptor_receptor_ref: Optional[Union[str, List[str]]] = empty_list()
    V1p5Receptor_reactivity_measurements: Optional[Union[Union[dict, "V1p5ReceptorReactivity"], List[Union[dict, "V1p5ReceptorReactivity"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5Receptor_receptor_id):
            self.MissingRequiredField("V1p5Receptor_receptor_id")
        if not isinstance(self.V1p5Receptor_receptor_id, str):
            self.V1p5Receptor_receptor_id = str(self.V1p5Receptor_receptor_id)

        if self._is_empty(self.V1p5Receptor_receptor_hash):
            self.MissingRequiredField("V1p5Receptor_receptor_hash")
        if not isinstance(self.V1p5Receptor_receptor_hash, str):
            self.V1p5Receptor_receptor_hash = str(self.V1p5Receptor_receptor_hash)

        if self._is_empty(self.V1p5Receptor_receptor_type):
            self.MissingRequiredField("V1p5Receptor_receptor_type")
        if not isinstance(self.V1p5Receptor_receptor_type, V1p5ReceptorType):
            self.V1p5Receptor_receptor_type = V1p5ReceptorType(self.V1p5Receptor_receptor_type)

        if self._is_empty(self.V1p5Receptor_receptor_variable_domain_1_aa):
            self.MissingRequiredField("V1p5Receptor_receptor_variable_domain_1_aa")
        if not isinstance(self.V1p5Receptor_receptor_variable_domain_1_aa, str):
            self.V1p5Receptor_receptor_variable_domain_1_aa = str(self.V1p5Receptor_receptor_variable_domain_1_aa)

        if self._is_empty(self.V1p5Receptor_receptor_variable_domain_1_locus):
            self.MissingRequiredField("V1p5Receptor_receptor_variable_domain_1_locus")
        if not isinstance(self.V1p5Receptor_receptor_variable_domain_1_locus, V1p5ReceptorVariableDomain1Locus):
            self.V1p5Receptor_receptor_variable_domain_1_locus = V1p5ReceptorVariableDomain1Locus(self.V1p5Receptor_receptor_variable_domain_1_locus)

        if self._is_empty(self.V1p5Receptor_receptor_variable_domain_2_aa):
            self.MissingRequiredField("V1p5Receptor_receptor_variable_domain_2_aa")
        if not isinstance(self.V1p5Receptor_receptor_variable_domain_2_aa, str):
            self.V1p5Receptor_receptor_variable_domain_2_aa = str(self.V1p5Receptor_receptor_variable_domain_2_aa)

        if self._is_empty(self.V1p5Receptor_receptor_variable_domain_2_locus):
            self.MissingRequiredField("V1p5Receptor_receptor_variable_domain_2_locus")
        if not isinstance(self.V1p5Receptor_receptor_variable_domain_2_locus, V1p5ReceptorVariableDomain2Locus):
            self.V1p5Receptor_receptor_variable_domain_2_locus = V1p5ReceptorVariableDomain2Locus(self.V1p5Receptor_receptor_variable_domain_2_locus)

        if not isinstance(self.V1p5Receptor_receptor_ref, list):
            self.V1p5Receptor_receptor_ref = [self.V1p5Receptor_receptor_ref] if self.V1p5Receptor_receptor_ref is not None else []
        self.V1p5Receptor_receptor_ref = [v if isinstance(v, str) else str(v) for v in self.V1p5Receptor_receptor_ref]

        self._normalize_inlined_as_dict(slot_name="V1p5Receptor_reactivity_measurements", slot_type=V1p5ReceptorReactivity, key_name="V1p5ReceptorReactivity_ligand_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5ReceptorReactivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5ReceptorReactivity"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5ReceptorReactivity"
    class_name: ClassVar[str] = "V1p5ReceptorReactivity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5ReceptorReactivity

    V1p5ReceptorReactivity_ligand_type: Union[str, "V1p5LigandType"] = None
    V1p5ReceptorReactivity_antigen_type: Union[str, "V1p5AntigenType"] = None
    V1p5ReceptorReactivity_antigen: Union[str, "V1p5Antigen"] = None
    V1p5ReceptorReactivity_reactivity_method: Union[str, "V1p5ReactivityMethod"] = None
    V1p5ReceptorReactivity_reactivity_readout: Union[str, "V1p5ReactivityReadout"] = None
    V1p5ReceptorReactivity_reactivity_value: float = None
    V1p5ReceptorReactivity_reactivity_unit: str = None
    V1p5ReceptorReactivity_antigen_source_species: Optional[Union[str, "V1p5AntigenSourceSpecies"]] = None
    V1p5ReceptorReactivity_peptide_start: Optional[int] = None
    V1p5ReceptorReactivity_peptide_end: Optional[int] = None
    V1p5ReceptorReactivity_mhc_class: Optional[Union[str, "V1p5MhcClass"]] = None
    V1p5ReceptorReactivity_mhc_gene_1: Optional[Union[str, "V1p5MhcGene1"]] = None
    V1p5ReceptorReactivity_mhc_allele_1: Optional[str] = None
    V1p5ReceptorReactivity_mhc_gene_2: Optional[Union[str, "V1p5MhcGene2"]] = None
    V1p5ReceptorReactivity_mhc_allele_2: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5ReceptorReactivity_ligand_type):
            self.MissingRequiredField("V1p5ReceptorReactivity_ligand_type")
        if not isinstance(self.V1p5ReceptorReactivity_ligand_type, V1p5LigandType):
            self.V1p5ReceptorReactivity_ligand_type = V1p5LigandType(self.V1p5ReceptorReactivity_ligand_type)

        if self._is_empty(self.V1p5ReceptorReactivity_antigen_type):
            self.MissingRequiredField("V1p5ReceptorReactivity_antigen_type")
        if not isinstance(self.V1p5ReceptorReactivity_antigen_type, V1p5AntigenType):
            self.V1p5ReceptorReactivity_antigen_type = V1p5AntigenType(self.V1p5ReceptorReactivity_antigen_type)

        if self._is_empty(self.V1p5ReceptorReactivity_reactivity_method):
            self.MissingRequiredField("V1p5ReceptorReactivity_reactivity_method")
        if not isinstance(self.V1p5ReceptorReactivity_reactivity_method, V1p5ReactivityMethod):
            self.V1p5ReceptorReactivity_reactivity_method = V1p5ReactivityMethod(self.V1p5ReceptorReactivity_reactivity_method)

        if self._is_empty(self.V1p5ReceptorReactivity_reactivity_readout):
            self.MissingRequiredField("V1p5ReceptorReactivity_reactivity_readout")
        if not isinstance(self.V1p5ReceptorReactivity_reactivity_readout, V1p5ReactivityReadout):
            self.V1p5ReceptorReactivity_reactivity_readout = V1p5ReactivityReadout(self.V1p5ReceptorReactivity_reactivity_readout)

        if self._is_empty(self.V1p5ReceptorReactivity_reactivity_value):
            self.MissingRequiredField("V1p5ReceptorReactivity_reactivity_value")
        if not isinstance(self.V1p5ReceptorReactivity_reactivity_value, float):
            self.V1p5ReceptorReactivity_reactivity_value = float(self.V1p5ReceptorReactivity_reactivity_value)

        if self._is_empty(self.V1p5ReceptorReactivity_reactivity_unit):
            self.MissingRequiredField("V1p5ReceptorReactivity_reactivity_unit")
        if not isinstance(self.V1p5ReceptorReactivity_reactivity_unit, str):
            self.V1p5ReceptorReactivity_reactivity_unit = str(self.V1p5ReceptorReactivity_reactivity_unit)

        if self.V1p5ReceptorReactivity_peptide_start is not None and not isinstance(self.V1p5ReceptorReactivity_peptide_start, int):
            self.V1p5ReceptorReactivity_peptide_start = int(self.V1p5ReceptorReactivity_peptide_start)

        if self.V1p5ReceptorReactivity_peptide_end is not None and not isinstance(self.V1p5ReceptorReactivity_peptide_end, int):
            self.V1p5ReceptorReactivity_peptide_end = int(self.V1p5ReceptorReactivity_peptide_end)

        if self.V1p5ReceptorReactivity_mhc_class is not None and not isinstance(self.V1p5ReceptorReactivity_mhc_class, V1p5MhcClass):
            self.V1p5ReceptorReactivity_mhc_class = V1p5MhcClass(self.V1p5ReceptorReactivity_mhc_class)

        if self.V1p5ReceptorReactivity_mhc_allele_1 is not None and not isinstance(self.V1p5ReceptorReactivity_mhc_allele_1, str):
            self.V1p5ReceptorReactivity_mhc_allele_1 = str(self.V1p5ReceptorReactivity_mhc_allele_1)

        if self.V1p5ReceptorReactivity_mhc_allele_2 is not None and not isinstance(self.V1p5ReceptorReactivity_mhc_allele_2, str):
            self.V1p5ReceptorReactivity_mhc_allele_2 = str(self.V1p5ReceptorReactivity_mhc_allele_2)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p5SampleProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p5SampleProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p5SampleProcessing"
    class_name: ClassVar[str] = "V1p5SampleProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p5SampleProcessing

    V1p5Sample_sample_id: str = None
    V1p5Sample_sample_type: str = None
    V1p5Sample_tissue: Union[str, "V1p5Tissue"] = None
    V1p5Sample_anatomic_site: str = None
    V1p5Sample_disease_state_sample: str = None
    V1p5Sample_collection_time_point_relative: float = None
    V1p5Sample_collection_time_point_relative_unit: Union[str, "V1p5CollectionTimePointRelativeUnit"] = None
    V1p5Sample_collection_time_point_reference: str = None
    V1p5Sample_biomaterial_provider: str = None
    V1p5CellProcessing_tissue_processing: str = None
    V1p5CellProcessing_cell_subset: Union[str, "V1p5CellSubset"] = None
    V1p5CellProcessing_cell_phenotype: str = None
    V1p5CellProcessing_single_cell: Union[bool, Bool] = None
    V1p5CellProcessing_cell_number: int = None
    V1p5CellProcessing_cells_per_reaction: int = None
    V1p5CellProcessing_cell_storage: Union[bool, Bool] = None
    V1p5CellProcessing_cell_quality: str = None
    V1p5CellProcessing_cell_isolation: str = None
    V1p5CellProcessing_cell_processing_protocol: str = None
    V1p5NucleicAcidProcessing_template_class: Union[str, "V1p5TemplateClass"] = None
    V1p5NucleicAcidProcessing_template_quality: str = None
    V1p5NucleicAcidProcessing_template_amount: float = None
    V1p5NucleicAcidProcessing_template_amount_unit: Union[str, "V1p5TemplateAmountUnit"] = None
    V1p5NucleicAcidProcessing_library_generation_method: Union[str, "V1p5LibraryGenerationMethod"] = None
    V1p5NucleicAcidProcessing_library_generation_protocol: str = None
    V1p5NucleicAcidProcessing_library_generation_kit_version: str = None
    V1p5NucleicAcidProcessing_complete_sequences: Union[str, "V1p5CompleteSequences"] = None
    V1p5NucleicAcidProcessing_physical_linkage: Union[str, "V1p5PhysicalLinkage"] = None
    V1p5SequencingRun_sequencing_run_id: str = None
    V1p5SequencingRun_total_reads_passing_qc_filter: int = None
    V1p5SequencingRun_sequencing_platform: str = None
    V1p5SequencingRun_sequencing_facility: str = None
    V1p5SequencingRun_sequencing_run_date: str = None
    V1p5SequencingRun_sequencing_kit: str = None
    V1p5SampleProcessing_sample_processing_id: Optional[str] = None
    V1p5CellProcessing_cell_species: Optional[Union[str, "V1p5CellSpecies"]] = None
    V1p5NucleicAcidProcessing_pcr_target: Optional[Union[Union[dict, V1p5PCRTarget], List[Union[dict, V1p5PCRTarget]]]] = empty_list()
    V1p5SequencingRun_sequencing_files: Optional[Union[dict, V1p5SequencingData]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p5Sample_sample_id):
            self.MissingRequiredField("V1p5Sample_sample_id")
        if not isinstance(self.V1p5Sample_sample_id, str):
            self.V1p5Sample_sample_id = str(self.V1p5Sample_sample_id)

        if self._is_empty(self.V1p5Sample_sample_type):
            self.MissingRequiredField("V1p5Sample_sample_type")
        if not isinstance(self.V1p5Sample_sample_type, str):
            self.V1p5Sample_sample_type = str(self.V1p5Sample_sample_type)

        if self._is_empty(self.V1p5Sample_anatomic_site):
            self.MissingRequiredField("V1p5Sample_anatomic_site")
        if not isinstance(self.V1p5Sample_anatomic_site, str):
            self.V1p5Sample_anatomic_site = str(self.V1p5Sample_anatomic_site)

        if self._is_empty(self.V1p5Sample_disease_state_sample):
            self.MissingRequiredField("V1p5Sample_disease_state_sample")
        if not isinstance(self.V1p5Sample_disease_state_sample, str):
            self.V1p5Sample_disease_state_sample = str(self.V1p5Sample_disease_state_sample)

        if self._is_empty(self.V1p5Sample_collection_time_point_relative):
            self.MissingRequiredField("V1p5Sample_collection_time_point_relative")
        if not isinstance(self.V1p5Sample_collection_time_point_relative, float):
            self.V1p5Sample_collection_time_point_relative = float(self.V1p5Sample_collection_time_point_relative)

        if self._is_empty(self.V1p5Sample_collection_time_point_reference):
            self.MissingRequiredField("V1p5Sample_collection_time_point_reference")
        if not isinstance(self.V1p5Sample_collection_time_point_reference, str):
            self.V1p5Sample_collection_time_point_reference = str(self.V1p5Sample_collection_time_point_reference)

        if self._is_empty(self.V1p5Sample_biomaterial_provider):
            self.MissingRequiredField("V1p5Sample_biomaterial_provider")
        if not isinstance(self.V1p5Sample_biomaterial_provider, str):
            self.V1p5Sample_biomaterial_provider = str(self.V1p5Sample_biomaterial_provider)

        if self._is_empty(self.V1p5CellProcessing_tissue_processing):
            self.MissingRequiredField("V1p5CellProcessing_tissue_processing")
        if not isinstance(self.V1p5CellProcessing_tissue_processing, str):
            self.V1p5CellProcessing_tissue_processing = str(self.V1p5CellProcessing_tissue_processing)

        if self._is_empty(self.V1p5CellProcessing_cell_phenotype):
            self.MissingRequiredField("V1p5CellProcessing_cell_phenotype")
        if not isinstance(self.V1p5CellProcessing_cell_phenotype, str):
            self.V1p5CellProcessing_cell_phenotype = str(self.V1p5CellProcessing_cell_phenotype)

        if self._is_empty(self.V1p5CellProcessing_single_cell):
            self.MissingRequiredField("V1p5CellProcessing_single_cell")
        if not isinstance(self.V1p5CellProcessing_single_cell, Bool):
            self.V1p5CellProcessing_single_cell = Bool(self.V1p5CellProcessing_single_cell)

        if self._is_empty(self.V1p5CellProcessing_cell_number):
            self.MissingRequiredField("V1p5CellProcessing_cell_number")
        if not isinstance(self.V1p5CellProcessing_cell_number, int):
            self.V1p5CellProcessing_cell_number = int(self.V1p5CellProcessing_cell_number)

        if self._is_empty(self.V1p5CellProcessing_cells_per_reaction):
            self.MissingRequiredField("V1p5CellProcessing_cells_per_reaction")
        if not isinstance(self.V1p5CellProcessing_cells_per_reaction, int):
            self.V1p5CellProcessing_cells_per_reaction = int(self.V1p5CellProcessing_cells_per_reaction)

        if self._is_empty(self.V1p5CellProcessing_cell_storage):
            self.MissingRequiredField("V1p5CellProcessing_cell_storage")
        if not isinstance(self.V1p5CellProcessing_cell_storage, Bool):
            self.V1p5CellProcessing_cell_storage = Bool(self.V1p5CellProcessing_cell_storage)

        if self._is_empty(self.V1p5CellProcessing_cell_quality):
            self.MissingRequiredField("V1p5CellProcessing_cell_quality")
        if not isinstance(self.V1p5CellProcessing_cell_quality, str):
            self.V1p5CellProcessing_cell_quality = str(self.V1p5CellProcessing_cell_quality)

        if self._is_empty(self.V1p5CellProcessing_cell_isolation):
            self.MissingRequiredField("V1p5CellProcessing_cell_isolation")
        if not isinstance(self.V1p5CellProcessing_cell_isolation, str):
            self.V1p5CellProcessing_cell_isolation = str(self.V1p5CellProcessing_cell_isolation)

        if self._is_empty(self.V1p5CellProcessing_cell_processing_protocol):
            self.MissingRequiredField("V1p5CellProcessing_cell_processing_protocol")
        if not isinstance(self.V1p5CellProcessing_cell_processing_protocol, str):
            self.V1p5CellProcessing_cell_processing_protocol = str(self.V1p5CellProcessing_cell_processing_protocol)

        if self._is_empty(self.V1p5NucleicAcidProcessing_template_class):
            self.MissingRequiredField("V1p5NucleicAcidProcessing_template_class")
        if not isinstance(self.V1p5NucleicAcidProcessing_template_class, V1p5TemplateClass):
            self.V1p5NucleicAcidProcessing_template_class = V1p5TemplateClass(self.V1p5NucleicAcidProcessing_template_class)

        if self._is_empty(self.V1p5NucleicAcidProcessing_template_quality):
            self.MissingRequiredField("V1p5NucleicAcidProcessing_template_quality")
        if not isinstance(self.V1p5NucleicAcidProcessing_template_quality, str):
            self.V1p5NucleicAcidProcessing_template_quality = str(self.V1p5NucleicAcidProcessing_template_quality)

        if self._is_empty(self.V1p5NucleicAcidProcessing_template_amount):
            self.MissingRequiredField("V1p5NucleicAcidProcessing_template_amount")
        if not isinstance(self.V1p5NucleicAcidProcessing_template_amount, float):
            self.V1p5NucleicAcidProcessing_template_amount = float(self.V1p5NucleicAcidProcessing_template_amount)

        if self._is_empty(self.V1p5NucleicAcidProcessing_library_generation_method):
            self.MissingRequiredField("V1p5NucleicAcidProcessing_library_generation_method")
        if not isinstance(self.V1p5NucleicAcidProcessing_library_generation_method, V1p5LibraryGenerationMethod):
            self.V1p5NucleicAcidProcessing_library_generation_method = V1p5LibraryGenerationMethod(self.V1p5NucleicAcidProcessing_library_generation_method)

        if self._is_empty(self.V1p5NucleicAcidProcessing_library_generation_protocol):
            self.MissingRequiredField("V1p5NucleicAcidProcessing_library_generation_protocol")
        if not isinstance(self.V1p5NucleicAcidProcessing_library_generation_protocol, str):
            self.V1p5NucleicAcidProcessing_library_generation_protocol = str(self.V1p5NucleicAcidProcessing_library_generation_protocol)

        if self._is_empty(self.V1p5NucleicAcidProcessing_library_generation_kit_version):
            self.MissingRequiredField("V1p5NucleicAcidProcessing_library_generation_kit_version")
        if not isinstance(self.V1p5NucleicAcidProcessing_library_generation_kit_version, str):
            self.V1p5NucleicAcidProcessing_library_generation_kit_version = str(self.V1p5NucleicAcidProcessing_library_generation_kit_version)

        if self._is_empty(self.V1p5NucleicAcidProcessing_complete_sequences):
            self.MissingRequiredField("V1p5NucleicAcidProcessing_complete_sequences")
        if not isinstance(self.V1p5NucleicAcidProcessing_complete_sequences, V1p5CompleteSequences):
            self.V1p5NucleicAcidProcessing_complete_sequences = V1p5CompleteSequences(self.V1p5NucleicAcidProcessing_complete_sequences)

        if self._is_empty(self.V1p5NucleicAcidProcessing_physical_linkage):
            self.MissingRequiredField("V1p5NucleicAcidProcessing_physical_linkage")
        if not isinstance(self.V1p5NucleicAcidProcessing_physical_linkage, V1p5PhysicalLinkage):
            self.V1p5NucleicAcidProcessing_physical_linkage = V1p5PhysicalLinkage(self.V1p5NucleicAcidProcessing_physical_linkage)

        if self._is_empty(self.V1p5SequencingRun_sequencing_run_id):
            self.MissingRequiredField("V1p5SequencingRun_sequencing_run_id")
        if not isinstance(self.V1p5SequencingRun_sequencing_run_id, str):
            self.V1p5SequencingRun_sequencing_run_id = str(self.V1p5SequencingRun_sequencing_run_id)

        if self._is_empty(self.V1p5SequencingRun_total_reads_passing_qc_filter):
            self.MissingRequiredField("V1p5SequencingRun_total_reads_passing_qc_filter")
        if not isinstance(self.V1p5SequencingRun_total_reads_passing_qc_filter, int):
            self.V1p5SequencingRun_total_reads_passing_qc_filter = int(self.V1p5SequencingRun_total_reads_passing_qc_filter)

        if self._is_empty(self.V1p5SequencingRun_sequencing_platform):
            self.MissingRequiredField("V1p5SequencingRun_sequencing_platform")
        if not isinstance(self.V1p5SequencingRun_sequencing_platform, str):
            self.V1p5SequencingRun_sequencing_platform = str(self.V1p5SequencingRun_sequencing_platform)

        if self._is_empty(self.V1p5SequencingRun_sequencing_facility):
            self.MissingRequiredField("V1p5SequencingRun_sequencing_facility")
        if not isinstance(self.V1p5SequencingRun_sequencing_facility, str):
            self.V1p5SequencingRun_sequencing_facility = str(self.V1p5SequencingRun_sequencing_facility)

        if self._is_empty(self.V1p5SequencingRun_sequencing_run_date):
            self.MissingRequiredField("V1p5SequencingRun_sequencing_run_date")
        if not isinstance(self.V1p5SequencingRun_sequencing_run_date, str):
            self.V1p5SequencingRun_sequencing_run_date = str(self.V1p5SequencingRun_sequencing_run_date)

        if self._is_empty(self.V1p5SequencingRun_sequencing_kit):
            self.MissingRequiredField("V1p5SequencingRun_sequencing_kit")
        if not isinstance(self.V1p5SequencingRun_sequencing_kit, str):
            self.V1p5SequencingRun_sequencing_kit = str(self.V1p5SequencingRun_sequencing_kit)

        if self.V1p5SampleProcessing_sample_processing_id is not None and not isinstance(self.V1p5SampleProcessing_sample_processing_id, str):
            self.V1p5SampleProcessing_sample_processing_id = str(self.V1p5SampleProcessing_sample_processing_id)

        self._normalize_inlined_as_dict(slot_name="V1p5NucleicAcidProcessing_pcr_target", slot_type=V1p5PCRTarget, key_name="V1p5PCRTarget_pcr_target_locus", keyed=False)

        if self.V1p5SequencingRun_sequencing_files is not None and not isinstance(self.V1p5SequencingRun_sequencing_files, V1p5SequencingData):
            self.V1p5SequencingRun_sequencing_files = V1p5SequencingData(**as_dict(self.V1p5SequencingRun_sequencing_files))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4TimePoint(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4TimePoint"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4TimePoint"
    class_name: ClassVar[str] = "V1p4TimePoint"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4TimePoint

    V1p4TimePoint_label: Optional[str] = None
    V1p4TimePoint_value: Optional[float] = None
    V1p4TimePoint_unit: Optional[Union[str, "V1p4Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4TimePoint_label is not None and not isinstance(self.V1p4TimePoint_label, str):
            self.V1p4TimePoint_label = str(self.V1p4TimePoint_label)

        if self.V1p4TimePoint_value is not None and not isinstance(self.V1p4TimePoint_value, float):
            self.V1p4TimePoint_value = float(self.V1p4TimePoint_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4TimeInterval(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4TimeInterval"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4TimeInterval"
    class_name: ClassVar[str] = "V1p4TimeInterval"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4TimeInterval

    V1p4TimeInterval_min: Optional[float] = None
    V1p4TimeInterval_max: Optional[float] = None
    V1p4TimeInterval_unit: Optional[Union[str, "V1p4Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4TimeInterval_min is not None and not isinstance(self.V1p4TimeInterval_min, float):
            self.V1p4TimeInterval_min = float(self.V1p4TimeInterval_min)

        if self.V1p4TimeInterval_max is not None and not isinstance(self.V1p4TimeInterval_max, float):
            self.V1p4TimeInterval_max = float(self.V1p4TimeInterval_max)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4PhysicalQuantity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4PhysicalQuantity"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4PhysicalQuantity"
    class_name: ClassVar[str] = "V1p4PhysicalQuantity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4PhysicalQuantity

    V1p4PhysicalQuantity_quantity: Optional[float] = None
    V1p4PhysicalQuantity_unit: Optional[Union[str, "V1p4Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4PhysicalQuantity_quantity is not None and not isinstance(self.V1p4PhysicalQuantity_quantity, float):
            self.V1p4PhysicalQuantity_quantity = float(self.V1p4PhysicalQuantity_quantity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4TimeQuantity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4TimeQuantity"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4TimeQuantity"
    class_name: ClassVar[str] = "V1p4TimeQuantity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4TimeQuantity

    V1p4TimeQuantity_quantity: Optional[float] = None
    V1p4TimeQuantity_unit: Optional[Union[str, "V1p4Unit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4TimeQuantity_quantity is not None and not isinstance(self.V1p4TimeQuantity_quantity, float):
            self.V1p4TimeQuantity_quantity = float(self.V1p4TimeQuantity_quantity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Contributor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Contributor"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Contributor"
    class_name: ClassVar[str] = "V1p4Contributor"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Contributor

    V1p4Contributor_contributor_id: str = None
    V1p4Contributor_name: str = None
    V1p4Contributor_orcid_id: Optional[Union[str, "V1p4OrcidId"]] = None
    V1p4Contributor_affiliation: Optional[Union[str, "V1p4Affiliation"]] = None
    V1p4Contributor_affiliation_department: Optional[str] = None
    V1p4Contributor_contributions: Optional[Union[Union[dict, "V1p4ContributorContribution"], List[Union[dict, "V1p4ContributorContribution"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4Contributor_contributor_id):
            self.MissingRequiredField("V1p4Contributor_contributor_id")
        if not isinstance(self.V1p4Contributor_contributor_id, str):
            self.V1p4Contributor_contributor_id = str(self.V1p4Contributor_contributor_id)

        if self._is_empty(self.V1p4Contributor_name):
            self.MissingRequiredField("V1p4Contributor_name")
        if not isinstance(self.V1p4Contributor_name, str):
            self.V1p4Contributor_name = str(self.V1p4Contributor_name)

        if self.V1p4Contributor_affiliation_department is not None and not isinstance(self.V1p4Contributor_affiliation_department, str):
            self.V1p4Contributor_affiliation_department = str(self.V1p4Contributor_affiliation_department)

        self._normalize_inlined_as_dict(slot_name="V1p4Contributor_contributions", slot_type=V1p4ContributorContribution, key_name="V1p4ContributorContribution_role", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4ContributorContribution(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4ContributorContribution"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4ContributorContribution"
    class_name: ClassVar[str] = "V1p4ContributorContribution"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4ContributorContribution

    V1p4ContributorContribution_role: Union[str, "V1p4Role"] = None
    V1p4ContributorContribution_degree: Optional[Union[str, "V1p4Degree"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4ContributorContribution_role):
            self.MissingRequiredField("V1p4ContributorContribution_role")
        if not isinstance(self.V1p4ContributorContribution_role, V1p4Role):
            self.V1p4ContributorContribution_role = V1p4Role(self.V1p4ContributorContribution_role)

        if self.V1p4ContributorContribution_degree is not None and not isinstance(self.V1p4ContributorContribution_degree, V1p4Degree):
            self.V1p4ContributorContribution_degree = V1p4Degree(self.V1p4ContributorContribution_degree)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4RearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4RearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4RearrangedSequence"
    class_name: ClassVar[str] = "V1p4RearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4RearrangedSequence

    V1p4RearrangedSequence_sequence_id: str = None
    V1p4RearrangedSequence_sequence: str = None
    V1p4RearrangedSequence_derivation: Union[str, "V1p4Derivation"] = None
    V1p4RearrangedSequence_observation_type: Union[str, "V1p4ObservationType"] = None
    V1p4RearrangedSequence_repository_name: str = None
    V1p4RearrangedSequence_deposited_version: str = None
    V1p4RearrangedSequence_curation: Optional[str] = None
    V1p4RearrangedSequence_repository_ref: Optional[str] = None
    V1p4RearrangedSequence_sequence_start: Optional[int] = None
    V1p4RearrangedSequence_sequence_end: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4RearrangedSequence_sequence_id):
            self.MissingRequiredField("V1p4RearrangedSequence_sequence_id")
        if not isinstance(self.V1p4RearrangedSequence_sequence_id, str):
            self.V1p4RearrangedSequence_sequence_id = str(self.V1p4RearrangedSequence_sequence_id)

        if self._is_empty(self.V1p4RearrangedSequence_sequence):
            self.MissingRequiredField("V1p4RearrangedSequence_sequence")
        if not isinstance(self.V1p4RearrangedSequence_sequence, str):
            self.V1p4RearrangedSequence_sequence = str(self.V1p4RearrangedSequence_sequence)

        if self._is_empty(self.V1p4RearrangedSequence_derivation):
            self.MissingRequiredField("V1p4RearrangedSequence_derivation")
        if not isinstance(self.V1p4RearrangedSequence_derivation, V1p4Derivation):
            self.V1p4RearrangedSequence_derivation = V1p4Derivation(self.V1p4RearrangedSequence_derivation)

        if self._is_empty(self.V1p4RearrangedSequence_observation_type):
            self.MissingRequiredField("V1p4RearrangedSequence_observation_type")
        if not isinstance(self.V1p4RearrangedSequence_observation_type, V1p4ObservationType):
            self.V1p4RearrangedSequence_observation_type = V1p4ObservationType(self.V1p4RearrangedSequence_observation_type)

        if self._is_empty(self.V1p4RearrangedSequence_repository_name):
            self.MissingRequiredField("V1p4RearrangedSequence_repository_name")
        if not isinstance(self.V1p4RearrangedSequence_repository_name, str):
            self.V1p4RearrangedSequence_repository_name = str(self.V1p4RearrangedSequence_repository_name)

        if self._is_empty(self.V1p4RearrangedSequence_deposited_version):
            self.MissingRequiredField("V1p4RearrangedSequence_deposited_version")
        if not isinstance(self.V1p4RearrangedSequence_deposited_version, str):
            self.V1p4RearrangedSequence_deposited_version = str(self.V1p4RearrangedSequence_deposited_version)

        if self.V1p4RearrangedSequence_curation is not None and not isinstance(self.V1p4RearrangedSequence_curation, str):
            self.V1p4RearrangedSequence_curation = str(self.V1p4RearrangedSequence_curation)

        if self.V1p4RearrangedSequence_repository_ref is not None and not isinstance(self.V1p4RearrangedSequence_repository_ref, str):
            self.V1p4RearrangedSequence_repository_ref = str(self.V1p4RearrangedSequence_repository_ref)

        if self.V1p4RearrangedSequence_sequence_start is not None and not isinstance(self.V1p4RearrangedSequence_sequence_start, int):
            self.V1p4RearrangedSequence_sequence_start = int(self.V1p4RearrangedSequence_sequence_start)

        if self.V1p4RearrangedSequence_sequence_end is not None and not isinstance(self.V1p4RearrangedSequence_sequence_end, int):
            self.V1p4RearrangedSequence_sequence_end = int(self.V1p4RearrangedSequence_sequence_end)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4UnrearrangedSequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4UnrearrangedSequence"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4UnrearrangedSequence"
    class_name: ClassVar[str] = "V1p4UnrearrangedSequence"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4UnrearrangedSequence

    V1p4UnrearrangedSequence_sequence_id: str = None
    V1p4UnrearrangedSequence_sequence: str = None
    V1p4UnrearrangedSequence_repository_name: str = None
    V1p4UnrearrangedSequence_gff_seqid: str = None
    V1p4UnrearrangedSequence_gff_start: int = None
    V1p4UnrearrangedSequence_gff_end: int = None
    V1p4UnrearrangedSequence_strand: Union[str, "V1p4Strand"] = None
    V1p4UnrearrangedSequence_curation: Optional[str] = None
    V1p4UnrearrangedSequence_repository_ref: Optional[str] = None
    V1p4UnrearrangedSequence_patch_no: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4UnrearrangedSequence_sequence_id):
            self.MissingRequiredField("V1p4UnrearrangedSequence_sequence_id")
        if not isinstance(self.V1p4UnrearrangedSequence_sequence_id, str):
            self.V1p4UnrearrangedSequence_sequence_id = str(self.V1p4UnrearrangedSequence_sequence_id)

        if self._is_empty(self.V1p4UnrearrangedSequence_sequence):
            self.MissingRequiredField("V1p4UnrearrangedSequence_sequence")
        if not isinstance(self.V1p4UnrearrangedSequence_sequence, str):
            self.V1p4UnrearrangedSequence_sequence = str(self.V1p4UnrearrangedSequence_sequence)

        if self._is_empty(self.V1p4UnrearrangedSequence_repository_name):
            self.MissingRequiredField("V1p4UnrearrangedSequence_repository_name")
        if not isinstance(self.V1p4UnrearrangedSequence_repository_name, str):
            self.V1p4UnrearrangedSequence_repository_name = str(self.V1p4UnrearrangedSequence_repository_name)

        if self._is_empty(self.V1p4UnrearrangedSequence_gff_seqid):
            self.MissingRequiredField("V1p4UnrearrangedSequence_gff_seqid")
        if not isinstance(self.V1p4UnrearrangedSequence_gff_seqid, str):
            self.V1p4UnrearrangedSequence_gff_seqid = str(self.V1p4UnrearrangedSequence_gff_seqid)

        if self._is_empty(self.V1p4UnrearrangedSequence_gff_start):
            self.MissingRequiredField("V1p4UnrearrangedSequence_gff_start")
        if not isinstance(self.V1p4UnrearrangedSequence_gff_start, int):
            self.V1p4UnrearrangedSequence_gff_start = int(self.V1p4UnrearrangedSequence_gff_start)

        if self._is_empty(self.V1p4UnrearrangedSequence_gff_end):
            self.MissingRequiredField("V1p4UnrearrangedSequence_gff_end")
        if not isinstance(self.V1p4UnrearrangedSequence_gff_end, int):
            self.V1p4UnrearrangedSequence_gff_end = int(self.V1p4UnrearrangedSequence_gff_end)

        if self._is_empty(self.V1p4UnrearrangedSequence_strand):
            self.MissingRequiredField("V1p4UnrearrangedSequence_strand")
        if not isinstance(self.V1p4UnrearrangedSequence_strand, V1p4Strand):
            self.V1p4UnrearrangedSequence_strand = V1p4Strand(self.V1p4UnrearrangedSequence_strand)

        if self.V1p4UnrearrangedSequence_curation is not None and not isinstance(self.V1p4UnrearrangedSequence_curation, str):
            self.V1p4UnrearrangedSequence_curation = str(self.V1p4UnrearrangedSequence_curation)

        if self.V1p4UnrearrangedSequence_repository_ref is not None and not isinstance(self.V1p4UnrearrangedSequence_repository_ref, str):
            self.V1p4UnrearrangedSequence_repository_ref = str(self.V1p4UnrearrangedSequence_repository_ref)

        if self.V1p4UnrearrangedSequence_patch_no is not None and not isinstance(self.V1p4UnrearrangedSequence_patch_no, str):
            self.V1p4UnrearrangedSequence_patch_no = str(self.V1p4UnrearrangedSequence_patch_no)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SequenceDelineationV(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SequenceDelineationV"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SequenceDelineationV"
    class_name: ClassVar[str] = "V1p4SequenceDelineationV"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SequenceDelineationV

    V1p4SequenceDelineationV_sequence_delineation_id: str = None
    V1p4SequenceDelineationV_delineation_scheme: str = None
    V1p4SequenceDelineationV_fwr1_start: int = None
    V1p4SequenceDelineationV_fwr1_end: int = None
    V1p4SequenceDelineationV_cdr1_start: int = None
    V1p4SequenceDelineationV_cdr1_end: int = None
    V1p4SequenceDelineationV_fwr2_start: int = None
    V1p4SequenceDelineationV_fwr2_end: int = None
    V1p4SequenceDelineationV_cdr2_start: int = None
    V1p4SequenceDelineationV_cdr2_end: int = None
    V1p4SequenceDelineationV_fwr3_start: int = None
    V1p4SequenceDelineationV_fwr3_end: int = None
    V1p4SequenceDelineationV_cdr3_start: int = None
    V1p4SequenceDelineationV_unaligned_sequence: Optional[str] = None
    V1p4SequenceDelineationV_aligned_sequence: Optional[str] = None
    V1p4SequenceDelineationV_alignment_labels: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4SequenceDelineationV_sequence_delineation_id):
            self.MissingRequiredField("V1p4SequenceDelineationV_sequence_delineation_id")
        if not isinstance(self.V1p4SequenceDelineationV_sequence_delineation_id, str):
            self.V1p4SequenceDelineationV_sequence_delineation_id = str(self.V1p4SequenceDelineationV_sequence_delineation_id)

        if self._is_empty(self.V1p4SequenceDelineationV_delineation_scheme):
            self.MissingRequiredField("V1p4SequenceDelineationV_delineation_scheme")
        if not isinstance(self.V1p4SequenceDelineationV_delineation_scheme, str):
            self.V1p4SequenceDelineationV_delineation_scheme = str(self.V1p4SequenceDelineationV_delineation_scheme)

        if self._is_empty(self.V1p4SequenceDelineationV_fwr1_start):
            self.MissingRequiredField("V1p4SequenceDelineationV_fwr1_start")
        if not isinstance(self.V1p4SequenceDelineationV_fwr1_start, int):
            self.V1p4SequenceDelineationV_fwr1_start = int(self.V1p4SequenceDelineationV_fwr1_start)

        if self._is_empty(self.V1p4SequenceDelineationV_fwr1_end):
            self.MissingRequiredField("V1p4SequenceDelineationV_fwr1_end")
        if not isinstance(self.V1p4SequenceDelineationV_fwr1_end, int):
            self.V1p4SequenceDelineationV_fwr1_end = int(self.V1p4SequenceDelineationV_fwr1_end)

        if self._is_empty(self.V1p4SequenceDelineationV_cdr1_start):
            self.MissingRequiredField("V1p4SequenceDelineationV_cdr1_start")
        if not isinstance(self.V1p4SequenceDelineationV_cdr1_start, int):
            self.V1p4SequenceDelineationV_cdr1_start = int(self.V1p4SequenceDelineationV_cdr1_start)

        if self._is_empty(self.V1p4SequenceDelineationV_cdr1_end):
            self.MissingRequiredField("V1p4SequenceDelineationV_cdr1_end")
        if not isinstance(self.V1p4SequenceDelineationV_cdr1_end, int):
            self.V1p4SequenceDelineationV_cdr1_end = int(self.V1p4SequenceDelineationV_cdr1_end)

        if self._is_empty(self.V1p4SequenceDelineationV_fwr2_start):
            self.MissingRequiredField("V1p4SequenceDelineationV_fwr2_start")
        if not isinstance(self.V1p4SequenceDelineationV_fwr2_start, int):
            self.V1p4SequenceDelineationV_fwr2_start = int(self.V1p4SequenceDelineationV_fwr2_start)

        if self._is_empty(self.V1p4SequenceDelineationV_fwr2_end):
            self.MissingRequiredField("V1p4SequenceDelineationV_fwr2_end")
        if not isinstance(self.V1p4SequenceDelineationV_fwr2_end, int):
            self.V1p4SequenceDelineationV_fwr2_end = int(self.V1p4SequenceDelineationV_fwr2_end)

        if self._is_empty(self.V1p4SequenceDelineationV_cdr2_start):
            self.MissingRequiredField("V1p4SequenceDelineationV_cdr2_start")
        if not isinstance(self.V1p4SequenceDelineationV_cdr2_start, int):
            self.V1p4SequenceDelineationV_cdr2_start = int(self.V1p4SequenceDelineationV_cdr2_start)

        if self._is_empty(self.V1p4SequenceDelineationV_cdr2_end):
            self.MissingRequiredField("V1p4SequenceDelineationV_cdr2_end")
        if not isinstance(self.V1p4SequenceDelineationV_cdr2_end, int):
            self.V1p4SequenceDelineationV_cdr2_end = int(self.V1p4SequenceDelineationV_cdr2_end)

        if self._is_empty(self.V1p4SequenceDelineationV_fwr3_start):
            self.MissingRequiredField("V1p4SequenceDelineationV_fwr3_start")
        if not isinstance(self.V1p4SequenceDelineationV_fwr3_start, int):
            self.V1p4SequenceDelineationV_fwr3_start = int(self.V1p4SequenceDelineationV_fwr3_start)

        if self._is_empty(self.V1p4SequenceDelineationV_fwr3_end):
            self.MissingRequiredField("V1p4SequenceDelineationV_fwr3_end")
        if not isinstance(self.V1p4SequenceDelineationV_fwr3_end, int):
            self.V1p4SequenceDelineationV_fwr3_end = int(self.V1p4SequenceDelineationV_fwr3_end)

        if self._is_empty(self.V1p4SequenceDelineationV_cdr3_start):
            self.MissingRequiredField("V1p4SequenceDelineationV_cdr3_start")
        if not isinstance(self.V1p4SequenceDelineationV_cdr3_start, int):
            self.V1p4SequenceDelineationV_cdr3_start = int(self.V1p4SequenceDelineationV_cdr3_start)

        if self.V1p4SequenceDelineationV_unaligned_sequence is not None and not isinstance(self.V1p4SequenceDelineationV_unaligned_sequence, str):
            self.V1p4SequenceDelineationV_unaligned_sequence = str(self.V1p4SequenceDelineationV_unaligned_sequence)

        if self.V1p4SequenceDelineationV_aligned_sequence is not None and not isinstance(self.V1p4SequenceDelineationV_aligned_sequence, str):
            self.V1p4SequenceDelineationV_aligned_sequence = str(self.V1p4SequenceDelineationV_aligned_sequence)

        if not isinstance(self.V1p4SequenceDelineationV_alignment_labels, list):
            self.V1p4SequenceDelineationV_alignment_labels = [self.V1p4SequenceDelineationV_alignment_labels] if self.V1p4SequenceDelineationV_alignment_labels is not None else []
        self.V1p4SequenceDelineationV_alignment_labels = [v if isinstance(v, str) else str(v) for v in self.V1p4SequenceDelineationV_alignment_labels]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4AlleleDescription(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4AlleleDescription"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4AlleleDescription"
    class_name: ClassVar[str] = "V1p4AlleleDescription"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4AlleleDescription

    V1p4AlleleDescription_allele_description_id: str = None
    V1p4AlleleDescription_acknowledgements: Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]] = None
    V1p4AlleleDescription_release_version: int = None
    V1p4AlleleDescription_release_date: str = None
    V1p4AlleleDescription_release_description: str = None
    V1p4AlleleDescription_sequence: str = None
    V1p4AlleleDescription_coding_sequence: str = None
    V1p4AlleleDescription_locus: Union[str, "V1p4Locus"] = None
    V1p4AlleleDescription_sequence_type: Union[str, "V1p4SequenceType"] = None
    V1p4AlleleDescription_functional: Union[bool, Bool] = None
    V1p4AlleleDescription_inference_type: Union[str, "V1p4InferenceType"] = None
    V1p4AlleleDescription_species: Union[str, "V1p4Species"] = None
    V1p4AlleleDescription_allele_description_ref: Optional[str] = None
    V1p4AlleleDescription_label: Optional[str] = None
    V1p4AlleleDescription_aliases: Optional[Union[str, List[str]]] = empty_list()
    V1p4AlleleDescription_chromosome: Optional[int] = None
    V1p4AlleleDescription_species_subgroup: Optional[str] = None
    V1p4AlleleDescription_species_subgroup_type: Optional[Union[str, "V1p4SpeciesSubgroupType"]] = None
    V1p4AlleleDescription_status: Optional[Union[str, "V1p4Status"]] = None
    V1p4AlleleDescription_subgroup_designation: Optional[str] = None
    V1p4AlleleDescription_gene_designation: Optional[str] = None
    V1p4AlleleDescription_allele_designation: Optional[str] = None
    V1p4AlleleDescription_allele_similarity_cluster_designation: Optional[str] = None
    V1p4AlleleDescription_allele_similarity_cluster_member_id: Optional[str] = None
    V1p4AlleleDescription_j_codon_frame: Optional[Union[str, "V1p4JCodonFrame"]] = None
    V1p4AlleleDescription_gene_start: Optional[int] = None
    V1p4AlleleDescription_gene_end: Optional[int] = None
    V1p4AlleleDescription_utr_5_prime_start: Optional[int] = None
    V1p4AlleleDescription_utr_5_prime_end: Optional[int] = None
    V1p4AlleleDescription_leader_1_start: Optional[int] = None
    V1p4AlleleDescription_leader_1_end: Optional[int] = None
    V1p4AlleleDescription_leader_2_start: Optional[int] = None
    V1p4AlleleDescription_leader_2_end: Optional[int] = None
    V1p4AlleleDescription_v_rs_start: Optional[int] = None
    V1p4AlleleDescription_v_rs_end: Optional[int] = None
    V1p4AlleleDescription_d_rs_3_prime_start: Optional[int] = None
    V1p4AlleleDescription_d_rs_3_prime_end: Optional[int] = None
    V1p4AlleleDescription_d_rs_5_prime_start: Optional[int] = None
    V1p4AlleleDescription_d_rs_5_prime_end: Optional[int] = None
    V1p4AlleleDescription_j_cdr3_end: Optional[int] = None
    V1p4AlleleDescription_j_rs_start: Optional[int] = None
    V1p4AlleleDescription_j_rs_end: Optional[int] = None
    V1p4AlleleDescription_j_donor_splice: Optional[int] = None
    V1p4AlleleDescription_v_gene_delineations: Optional[Union[Union[dict, V1p4SequenceDelineationV], List[Union[dict, V1p4SequenceDelineationV]]]] = empty_list()
    V1p4AlleleDescription_unrearranged_support: Optional[Union[Union[dict, V1p4UnrearrangedSequence], List[Union[dict, V1p4UnrearrangedSequence]]]] = empty_list()
    V1p4AlleleDescription_rearranged_support: Optional[Union[Union[dict, V1p4RearrangedSequence], List[Union[dict, V1p4RearrangedSequence]]]] = empty_list()
    V1p4AlleleDescription_paralogs: Optional[Union[str, List[str]]] = empty_list()
    V1p4AlleleDescription_curation: Optional[str] = None
    V1p4AlleleDescription_curational_tags: Optional[Union[Union[str, "V1p4CurationalTags"], List[Union[str, "V1p4CurationalTags"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4AlleleDescription_allele_description_id):
            self.MissingRequiredField("V1p4AlleleDescription_allele_description_id")
        if not isinstance(self.V1p4AlleleDescription_allele_description_id, str):
            self.V1p4AlleleDescription_allele_description_id = str(self.V1p4AlleleDescription_allele_description_id)

        if self._is_empty(self.V1p4AlleleDescription_acknowledgements):
            self.MissingRequiredField("V1p4AlleleDescription_acknowledgements")
        self._normalize_inlined_as_dict(slot_name="V1p4AlleleDescription_acknowledgements", slot_type=V1p4Contributor, key_name="V1p4Contributor_contributor_id", keyed=False)

        if self._is_empty(self.V1p4AlleleDescription_release_version):
            self.MissingRequiredField("V1p4AlleleDescription_release_version")
        if not isinstance(self.V1p4AlleleDescription_release_version, int):
            self.V1p4AlleleDescription_release_version = int(self.V1p4AlleleDescription_release_version)

        if self._is_empty(self.V1p4AlleleDescription_release_date):
            self.MissingRequiredField("V1p4AlleleDescription_release_date")
        if not isinstance(self.V1p4AlleleDescription_release_date, str):
            self.V1p4AlleleDescription_release_date = str(self.V1p4AlleleDescription_release_date)

        if self._is_empty(self.V1p4AlleleDescription_release_description):
            self.MissingRequiredField("V1p4AlleleDescription_release_description")
        if not isinstance(self.V1p4AlleleDescription_release_description, str):
            self.V1p4AlleleDescription_release_description = str(self.V1p4AlleleDescription_release_description)

        if self._is_empty(self.V1p4AlleleDescription_sequence):
            self.MissingRequiredField("V1p4AlleleDescription_sequence")
        if not isinstance(self.V1p4AlleleDescription_sequence, str):
            self.V1p4AlleleDescription_sequence = str(self.V1p4AlleleDescription_sequence)

        if self._is_empty(self.V1p4AlleleDescription_coding_sequence):
            self.MissingRequiredField("V1p4AlleleDescription_coding_sequence")
        if not isinstance(self.V1p4AlleleDescription_coding_sequence, str):
            self.V1p4AlleleDescription_coding_sequence = str(self.V1p4AlleleDescription_coding_sequence)

        if self._is_empty(self.V1p4AlleleDescription_locus):
            self.MissingRequiredField("V1p4AlleleDescription_locus")
        if not isinstance(self.V1p4AlleleDescription_locus, V1p4Locus):
            self.V1p4AlleleDescription_locus = V1p4Locus(self.V1p4AlleleDescription_locus)

        if self._is_empty(self.V1p4AlleleDescription_sequence_type):
            self.MissingRequiredField("V1p4AlleleDescription_sequence_type")
        if not isinstance(self.V1p4AlleleDescription_sequence_type, V1p4SequenceType):
            self.V1p4AlleleDescription_sequence_type = V1p4SequenceType(self.V1p4AlleleDescription_sequence_type)

        if self._is_empty(self.V1p4AlleleDescription_functional):
            self.MissingRequiredField("V1p4AlleleDescription_functional")
        if not isinstance(self.V1p4AlleleDescription_functional, Bool):
            self.V1p4AlleleDescription_functional = Bool(self.V1p4AlleleDescription_functional)

        if self._is_empty(self.V1p4AlleleDescription_inference_type):
            self.MissingRequiredField("V1p4AlleleDescription_inference_type")
        if not isinstance(self.V1p4AlleleDescription_inference_type, V1p4InferenceType):
            self.V1p4AlleleDescription_inference_type = V1p4InferenceType(self.V1p4AlleleDescription_inference_type)

        if self.V1p4AlleleDescription_allele_description_ref is not None and not isinstance(self.V1p4AlleleDescription_allele_description_ref, str):
            self.V1p4AlleleDescription_allele_description_ref = str(self.V1p4AlleleDescription_allele_description_ref)

        if self.V1p4AlleleDescription_label is not None and not isinstance(self.V1p4AlleleDescription_label, str):
            self.V1p4AlleleDescription_label = str(self.V1p4AlleleDescription_label)

        if not isinstance(self.V1p4AlleleDescription_aliases, list):
            self.V1p4AlleleDescription_aliases = [self.V1p4AlleleDescription_aliases] if self.V1p4AlleleDescription_aliases is not None else []
        self.V1p4AlleleDescription_aliases = [v if isinstance(v, str) else str(v) for v in self.V1p4AlleleDescription_aliases]

        if self.V1p4AlleleDescription_chromosome is not None and not isinstance(self.V1p4AlleleDescription_chromosome, int):
            self.V1p4AlleleDescription_chromosome = int(self.V1p4AlleleDescription_chromosome)

        if self.V1p4AlleleDescription_species_subgroup is not None and not isinstance(self.V1p4AlleleDescription_species_subgroup, str):
            self.V1p4AlleleDescription_species_subgroup = str(self.V1p4AlleleDescription_species_subgroup)

        if self.V1p4AlleleDescription_species_subgroup_type is not None and not isinstance(self.V1p4AlleleDescription_species_subgroup_type, V1p4SpeciesSubgroupType):
            self.V1p4AlleleDescription_species_subgroup_type = V1p4SpeciesSubgroupType(self.V1p4AlleleDescription_species_subgroup_type)

        if self.V1p4AlleleDescription_status is not None and not isinstance(self.V1p4AlleleDescription_status, V1p4Status):
            self.V1p4AlleleDescription_status = V1p4Status(self.V1p4AlleleDescription_status)

        if self.V1p4AlleleDescription_subgroup_designation is not None and not isinstance(self.V1p4AlleleDescription_subgroup_designation, str):
            self.V1p4AlleleDescription_subgroup_designation = str(self.V1p4AlleleDescription_subgroup_designation)

        if self.V1p4AlleleDescription_gene_designation is not None and not isinstance(self.V1p4AlleleDescription_gene_designation, str):
            self.V1p4AlleleDescription_gene_designation = str(self.V1p4AlleleDescription_gene_designation)

        if self.V1p4AlleleDescription_allele_designation is not None and not isinstance(self.V1p4AlleleDescription_allele_designation, str):
            self.V1p4AlleleDescription_allele_designation = str(self.V1p4AlleleDescription_allele_designation)

        if self.V1p4AlleleDescription_allele_similarity_cluster_designation is not None and not isinstance(self.V1p4AlleleDescription_allele_similarity_cluster_designation, str):
            self.V1p4AlleleDescription_allele_similarity_cluster_designation = str(self.V1p4AlleleDescription_allele_similarity_cluster_designation)

        if self.V1p4AlleleDescription_allele_similarity_cluster_member_id is not None and not isinstance(self.V1p4AlleleDescription_allele_similarity_cluster_member_id, str):
            self.V1p4AlleleDescription_allele_similarity_cluster_member_id = str(self.V1p4AlleleDescription_allele_similarity_cluster_member_id)

        if self.V1p4AlleleDescription_j_codon_frame is not None and not isinstance(self.V1p4AlleleDescription_j_codon_frame, V1p4JCodonFrame):
            self.V1p4AlleleDescription_j_codon_frame = V1p4JCodonFrame(self.V1p4AlleleDescription_j_codon_frame)

        if self.V1p4AlleleDescription_gene_start is not None and not isinstance(self.V1p4AlleleDescription_gene_start, int):
            self.V1p4AlleleDescription_gene_start = int(self.V1p4AlleleDescription_gene_start)

        if self.V1p4AlleleDescription_gene_end is not None and not isinstance(self.V1p4AlleleDescription_gene_end, int):
            self.V1p4AlleleDescription_gene_end = int(self.V1p4AlleleDescription_gene_end)

        if self.V1p4AlleleDescription_utr_5_prime_start is not None and not isinstance(self.V1p4AlleleDescription_utr_5_prime_start, int):
            self.V1p4AlleleDescription_utr_5_prime_start = int(self.V1p4AlleleDescription_utr_5_prime_start)

        if self.V1p4AlleleDescription_utr_5_prime_end is not None and not isinstance(self.V1p4AlleleDescription_utr_5_prime_end, int):
            self.V1p4AlleleDescription_utr_5_prime_end = int(self.V1p4AlleleDescription_utr_5_prime_end)

        if self.V1p4AlleleDescription_leader_1_start is not None and not isinstance(self.V1p4AlleleDescription_leader_1_start, int):
            self.V1p4AlleleDescription_leader_1_start = int(self.V1p4AlleleDescription_leader_1_start)

        if self.V1p4AlleleDescription_leader_1_end is not None and not isinstance(self.V1p4AlleleDescription_leader_1_end, int):
            self.V1p4AlleleDescription_leader_1_end = int(self.V1p4AlleleDescription_leader_1_end)

        if self.V1p4AlleleDescription_leader_2_start is not None and not isinstance(self.V1p4AlleleDescription_leader_2_start, int):
            self.V1p4AlleleDescription_leader_2_start = int(self.V1p4AlleleDescription_leader_2_start)

        if self.V1p4AlleleDescription_leader_2_end is not None and not isinstance(self.V1p4AlleleDescription_leader_2_end, int):
            self.V1p4AlleleDescription_leader_2_end = int(self.V1p4AlleleDescription_leader_2_end)

        if self.V1p4AlleleDescription_v_rs_start is not None and not isinstance(self.V1p4AlleleDescription_v_rs_start, int):
            self.V1p4AlleleDescription_v_rs_start = int(self.V1p4AlleleDescription_v_rs_start)

        if self.V1p4AlleleDescription_v_rs_end is not None and not isinstance(self.V1p4AlleleDescription_v_rs_end, int):
            self.V1p4AlleleDescription_v_rs_end = int(self.V1p4AlleleDescription_v_rs_end)

        if self.V1p4AlleleDescription_d_rs_3_prime_start is not None and not isinstance(self.V1p4AlleleDescription_d_rs_3_prime_start, int):
            self.V1p4AlleleDescription_d_rs_3_prime_start = int(self.V1p4AlleleDescription_d_rs_3_prime_start)

        if self.V1p4AlleleDescription_d_rs_3_prime_end is not None and not isinstance(self.V1p4AlleleDescription_d_rs_3_prime_end, int):
            self.V1p4AlleleDescription_d_rs_3_prime_end = int(self.V1p4AlleleDescription_d_rs_3_prime_end)

        if self.V1p4AlleleDescription_d_rs_5_prime_start is not None and not isinstance(self.V1p4AlleleDescription_d_rs_5_prime_start, int):
            self.V1p4AlleleDescription_d_rs_5_prime_start = int(self.V1p4AlleleDescription_d_rs_5_prime_start)

        if self.V1p4AlleleDescription_d_rs_5_prime_end is not None and not isinstance(self.V1p4AlleleDescription_d_rs_5_prime_end, int):
            self.V1p4AlleleDescription_d_rs_5_prime_end = int(self.V1p4AlleleDescription_d_rs_5_prime_end)

        if self.V1p4AlleleDescription_j_cdr3_end is not None and not isinstance(self.V1p4AlleleDescription_j_cdr3_end, int):
            self.V1p4AlleleDescription_j_cdr3_end = int(self.V1p4AlleleDescription_j_cdr3_end)

        if self.V1p4AlleleDescription_j_rs_start is not None and not isinstance(self.V1p4AlleleDescription_j_rs_start, int):
            self.V1p4AlleleDescription_j_rs_start = int(self.V1p4AlleleDescription_j_rs_start)

        if self.V1p4AlleleDescription_j_rs_end is not None and not isinstance(self.V1p4AlleleDescription_j_rs_end, int):
            self.V1p4AlleleDescription_j_rs_end = int(self.V1p4AlleleDescription_j_rs_end)

        if self.V1p4AlleleDescription_j_donor_splice is not None and not isinstance(self.V1p4AlleleDescription_j_donor_splice, int):
            self.V1p4AlleleDescription_j_donor_splice = int(self.V1p4AlleleDescription_j_donor_splice)

        self._normalize_inlined_as_dict(slot_name="V1p4AlleleDescription_v_gene_delineations", slot_type=V1p4SequenceDelineationV, key_name="V1p4SequenceDelineationV_sequence_delineation_id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="V1p4AlleleDescription_unrearranged_support", slot_type=V1p4UnrearrangedSequence, key_name="V1p4UnrearrangedSequence_sequence_id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="V1p4AlleleDescription_rearranged_support", slot_type=V1p4RearrangedSequence, key_name="V1p4RearrangedSequence_sequence_id", keyed=False)

        if not isinstance(self.V1p4AlleleDescription_paralogs, list):
            self.V1p4AlleleDescription_paralogs = [self.V1p4AlleleDescription_paralogs] if self.V1p4AlleleDescription_paralogs is not None else []
        self.V1p4AlleleDescription_paralogs = [v if isinstance(v, str) else str(v) for v in self.V1p4AlleleDescription_paralogs]

        if self.V1p4AlleleDescription_curation is not None and not isinstance(self.V1p4AlleleDescription_curation, str):
            self.V1p4AlleleDescription_curation = str(self.V1p4AlleleDescription_curation)

        if not isinstance(self.V1p4AlleleDescription_curational_tags, list):
            self.V1p4AlleleDescription_curational_tags = [self.V1p4AlleleDescription_curational_tags] if self.V1p4AlleleDescription_curational_tags is not None else []
        self.V1p4AlleleDescription_curational_tags = [v if isinstance(v, V1p4CurationalTags) else V1p4CurationalTags(v) for v in self.V1p4AlleleDescription_curational_tags]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4GermlineSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4GermlineSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4GermlineSet"
    class_name: ClassVar[str] = "V1p4GermlineSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4GermlineSet

    V1p4GermlineSet_germline_set_id: str = None
    V1p4GermlineSet_acknowledgements: Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]] = None
    V1p4GermlineSet_release_version: int = None
    V1p4GermlineSet_release_description: str = None
    V1p4GermlineSet_release_date: str = None
    V1p4GermlineSet_germline_set_name: str = None
    V1p4GermlineSet_germline_set_ref: str = None
    V1p4GermlineSet_species: Union[str, "V1p4Species"] = None
    V1p4GermlineSet_locus: Union[str, "V1p4Locus"] = None
    V1p4GermlineSet_allele_descriptions: Union[Union[dict, V1p4AlleleDescription], List[Union[dict, V1p4AlleleDescription]]] = None
    V1p4GermlineSet_pub_ids: Optional[Union[str, List[str]]] = empty_list()
    V1p4GermlineSet_species_subgroup: Optional[str] = None
    V1p4GermlineSet_species_subgroup_type: Optional[Union[str, "V1p4SpeciesSubgroupType"]] = None
    V1p4GermlineSet_curation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4GermlineSet_germline_set_id):
            self.MissingRequiredField("V1p4GermlineSet_germline_set_id")
        if not isinstance(self.V1p4GermlineSet_germline_set_id, str):
            self.V1p4GermlineSet_germline_set_id = str(self.V1p4GermlineSet_germline_set_id)

        if self._is_empty(self.V1p4GermlineSet_acknowledgements):
            self.MissingRequiredField("V1p4GermlineSet_acknowledgements")
        self._normalize_inlined_as_dict(slot_name="V1p4GermlineSet_acknowledgements", slot_type=V1p4Contributor, key_name="V1p4Contributor_contributor_id", keyed=False)

        if self._is_empty(self.V1p4GermlineSet_release_version):
            self.MissingRequiredField("V1p4GermlineSet_release_version")
        if not isinstance(self.V1p4GermlineSet_release_version, int):
            self.V1p4GermlineSet_release_version = int(self.V1p4GermlineSet_release_version)

        if self._is_empty(self.V1p4GermlineSet_release_description):
            self.MissingRequiredField("V1p4GermlineSet_release_description")
        if not isinstance(self.V1p4GermlineSet_release_description, str):
            self.V1p4GermlineSet_release_description = str(self.V1p4GermlineSet_release_description)

        if self._is_empty(self.V1p4GermlineSet_release_date):
            self.MissingRequiredField("V1p4GermlineSet_release_date")
        if not isinstance(self.V1p4GermlineSet_release_date, str):
            self.V1p4GermlineSet_release_date = str(self.V1p4GermlineSet_release_date)

        if self._is_empty(self.V1p4GermlineSet_germline_set_name):
            self.MissingRequiredField("V1p4GermlineSet_germline_set_name")
        if not isinstance(self.V1p4GermlineSet_germline_set_name, str):
            self.V1p4GermlineSet_germline_set_name = str(self.V1p4GermlineSet_germline_set_name)

        if self._is_empty(self.V1p4GermlineSet_germline_set_ref):
            self.MissingRequiredField("V1p4GermlineSet_germline_set_ref")
        if not isinstance(self.V1p4GermlineSet_germline_set_ref, str):
            self.V1p4GermlineSet_germline_set_ref = str(self.V1p4GermlineSet_germline_set_ref)

        if self._is_empty(self.V1p4GermlineSet_locus):
            self.MissingRequiredField("V1p4GermlineSet_locus")
        if not isinstance(self.V1p4GermlineSet_locus, V1p4Locus):
            self.V1p4GermlineSet_locus = V1p4Locus(self.V1p4GermlineSet_locus)

        if self._is_empty(self.V1p4GermlineSet_allele_descriptions):
            self.MissingRequiredField("V1p4GermlineSet_allele_descriptions")
        self._normalize_inlined_as_dict(slot_name="V1p4GermlineSet_allele_descriptions", slot_type=V1p4AlleleDescription, key_name="V1p4AlleleDescription_allele_description_id", keyed=False)

        if not isinstance(self.V1p4GermlineSet_pub_ids, list):
            self.V1p4GermlineSet_pub_ids = [self.V1p4GermlineSet_pub_ids] if self.V1p4GermlineSet_pub_ids is not None else []
        self.V1p4GermlineSet_pub_ids = [v if isinstance(v, str) else str(v) for v in self.V1p4GermlineSet_pub_ids]

        if self.V1p4GermlineSet_species_subgroup is not None and not isinstance(self.V1p4GermlineSet_species_subgroup, str):
            self.V1p4GermlineSet_species_subgroup = str(self.V1p4GermlineSet_species_subgroup)

        if self.V1p4GermlineSet_species_subgroup_type is not None and not isinstance(self.V1p4GermlineSet_species_subgroup_type, V1p4SpeciesSubgroupType):
            self.V1p4GermlineSet_species_subgroup_type = V1p4SpeciesSubgroupType(self.V1p4GermlineSet_species_subgroup_type)

        if self.V1p4GermlineSet_curation is not None and not isinstance(self.V1p4GermlineSet_curation, str):
            self.V1p4GermlineSet_curation = str(self.V1p4GermlineSet_curation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4GenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4GenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4GenotypeSet"
    class_name: ClassVar[str] = "V1p4GenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4GenotypeSet

    V1p4GenotypeSet_receptor_genotype_set_id: str = None
    V1p4GenotypeSet_genotype_class_list: Optional[Union[Union[dict, "V1p4Genotype"], List[Union[dict, "V1p4Genotype"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4GenotypeSet_receptor_genotype_set_id):
            self.MissingRequiredField("V1p4GenotypeSet_receptor_genotype_set_id")
        if not isinstance(self.V1p4GenotypeSet_receptor_genotype_set_id, str):
            self.V1p4GenotypeSet_receptor_genotype_set_id = str(self.V1p4GenotypeSet_receptor_genotype_set_id)

        self._normalize_inlined_as_dict(slot_name="V1p4GenotypeSet_genotype_class_list", slot_type=V1p4Genotype, key_name="V1p4Genotype_receptor_genotype_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Genotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Genotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Genotype"
    class_name: ClassVar[str] = "V1p4Genotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Genotype

    V1p4Genotype_receptor_genotype_id: str = None
    V1p4Genotype_locus: Union[str, "V1p4Locus"] = None
    V1p4Genotype_documented_alleles: Optional[Union[Union[dict, "V1p4DocumentedAllele"], List[Union[dict, "V1p4DocumentedAllele"]]]] = empty_list()
    V1p4Genotype_undocumented_alleles: Optional[Union[Union[dict, "V1p4UndocumentedAllele"], List[Union[dict, "V1p4UndocumentedAllele"]]]] = empty_list()
    V1p4Genotype_deleted_genes: Optional[Union[Union[dict, "V1p4DeletedGene"], List[Union[dict, "V1p4DeletedGene"]]]] = empty_list()
    V1p4Genotype_inference_process: Optional[Union[str, "V1p4InferenceProcess"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4Genotype_receptor_genotype_id):
            self.MissingRequiredField("V1p4Genotype_receptor_genotype_id")
        if not isinstance(self.V1p4Genotype_receptor_genotype_id, str):
            self.V1p4Genotype_receptor_genotype_id = str(self.V1p4Genotype_receptor_genotype_id)

        if self._is_empty(self.V1p4Genotype_locus):
            self.MissingRequiredField("V1p4Genotype_locus")
        if not isinstance(self.V1p4Genotype_locus, V1p4Locus):
            self.V1p4Genotype_locus = V1p4Locus(self.V1p4Genotype_locus)

        self._normalize_inlined_as_dict(slot_name="V1p4Genotype_documented_alleles", slot_type=V1p4DocumentedAllele, key_name="V1p4DocumentedAllele_label", keyed=False)

        self._normalize_inlined_as_dict(slot_name="V1p4Genotype_undocumented_alleles", slot_type=V1p4UndocumentedAllele, key_name="V1p4UndocumentedAllele_allele_name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="V1p4Genotype_deleted_genes", slot_type=V1p4DeletedGene, key_name="V1p4DeletedGene_label", keyed=False)

        if self.V1p4Genotype_inference_process is not None and not isinstance(self.V1p4Genotype_inference_process, V1p4InferenceProcess):
            self.V1p4Genotype_inference_process = V1p4InferenceProcess(self.V1p4Genotype_inference_process)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4DocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4DocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4DocumentedAllele"
    class_name: ClassVar[str] = "V1p4DocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4DocumentedAllele

    V1p4DocumentedAllele_label: str = None
    V1p4DocumentedAllele_germline_set_ref: str = None
    V1p4DocumentedAllele_phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4DocumentedAllele_label):
            self.MissingRequiredField("V1p4DocumentedAllele_label")
        if not isinstance(self.V1p4DocumentedAllele_label, str):
            self.V1p4DocumentedAllele_label = str(self.V1p4DocumentedAllele_label)

        if self._is_empty(self.V1p4DocumentedAllele_germline_set_ref):
            self.MissingRequiredField("V1p4DocumentedAllele_germline_set_ref")
        if not isinstance(self.V1p4DocumentedAllele_germline_set_ref, str):
            self.V1p4DocumentedAllele_germline_set_ref = str(self.V1p4DocumentedAllele_germline_set_ref)

        if self.V1p4DocumentedAllele_phasing is not None and not isinstance(self.V1p4DocumentedAllele_phasing, int):
            self.V1p4DocumentedAllele_phasing = int(self.V1p4DocumentedAllele_phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4UndocumentedAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4UndocumentedAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4UndocumentedAllele"
    class_name: ClassVar[str] = "V1p4UndocumentedAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4UndocumentedAllele

    V1p4UndocumentedAllele_allele_name: str = None
    V1p4UndocumentedAllele_sequence: str = None
    V1p4UndocumentedAllele_phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4UndocumentedAllele_allele_name):
            self.MissingRequiredField("V1p4UndocumentedAllele_allele_name")
        if not isinstance(self.V1p4UndocumentedAllele_allele_name, str):
            self.V1p4UndocumentedAllele_allele_name = str(self.V1p4UndocumentedAllele_allele_name)

        if self._is_empty(self.V1p4UndocumentedAllele_sequence):
            self.MissingRequiredField("V1p4UndocumentedAllele_sequence")
        if not isinstance(self.V1p4UndocumentedAllele_sequence, str):
            self.V1p4UndocumentedAllele_sequence = str(self.V1p4UndocumentedAllele_sequence)

        if self.V1p4UndocumentedAllele_phasing is not None and not isinstance(self.V1p4UndocumentedAllele_phasing, int):
            self.V1p4UndocumentedAllele_phasing = int(self.V1p4UndocumentedAllele_phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4DeletedGene(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4DeletedGene"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4DeletedGene"
    class_name: ClassVar[str] = "V1p4DeletedGene"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4DeletedGene

    V1p4DeletedGene_label: str = None
    V1p4DeletedGene_germline_set_ref: str = None
    V1p4DeletedGene_phasing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4DeletedGene_label):
            self.MissingRequiredField("V1p4DeletedGene_label")
        if not isinstance(self.V1p4DeletedGene_label, str):
            self.V1p4DeletedGene_label = str(self.V1p4DeletedGene_label)

        if self._is_empty(self.V1p4DeletedGene_germline_set_ref):
            self.MissingRequiredField("V1p4DeletedGene_germline_set_ref")
        if not isinstance(self.V1p4DeletedGene_germline_set_ref, str):
            self.V1p4DeletedGene_germline_set_ref = str(self.V1p4DeletedGene_germline_set_ref)

        if self.V1p4DeletedGene_phasing is not None and not isinstance(self.V1p4DeletedGene_phasing, int):
            self.V1p4DeletedGene_phasing = int(self.V1p4DeletedGene_phasing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4MHCGenotypeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4MHCGenotypeSet"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4MHCGenotypeSet"
    class_name: ClassVar[str] = "V1p4MHCGenotypeSet"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4MHCGenotypeSet

    V1p4MHCGenotypeSet_mhc_genotype_set_id: str = None
    V1p4MHCGenotypeSet_mhc_genotype_list: Union[Union[dict, "V1p4MHCGenotype"], List[Union[dict, "V1p4MHCGenotype"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4MHCGenotypeSet_mhc_genotype_set_id):
            self.MissingRequiredField("V1p4MHCGenotypeSet_mhc_genotype_set_id")
        if not isinstance(self.V1p4MHCGenotypeSet_mhc_genotype_set_id, str):
            self.V1p4MHCGenotypeSet_mhc_genotype_set_id = str(self.V1p4MHCGenotypeSet_mhc_genotype_set_id)

        if self._is_empty(self.V1p4MHCGenotypeSet_mhc_genotype_list):
            self.MissingRequiredField("V1p4MHCGenotypeSet_mhc_genotype_list")
        self._normalize_inlined_as_dict(slot_name="V1p4MHCGenotypeSet_mhc_genotype_list", slot_type=V1p4MHCGenotype, key_name="V1p4MHCGenotype_mhc_genotype_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4MHCGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4MHCGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4MHCGenotype"
    class_name: ClassVar[str] = "V1p4MHCGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4MHCGenotype

    V1p4MHCGenotype_mhc_genotype_id: str = None
    V1p4MHCGenotype_mhc_class: Union[str, "V1p4MhcClass"] = None
    V1p4MHCGenotype_mhc_alleles: Union[Union[dict, "V1p4MHCAllele"], List[Union[dict, "V1p4MHCAllele"]]] = None
    V1p4MHCGenotype_mhc_genotyping_method: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4MHCGenotype_mhc_genotype_id):
            self.MissingRequiredField("V1p4MHCGenotype_mhc_genotype_id")
        if not isinstance(self.V1p4MHCGenotype_mhc_genotype_id, str):
            self.V1p4MHCGenotype_mhc_genotype_id = str(self.V1p4MHCGenotype_mhc_genotype_id)

        if self._is_empty(self.V1p4MHCGenotype_mhc_class):
            self.MissingRequiredField("V1p4MHCGenotype_mhc_class")
        if not isinstance(self.V1p4MHCGenotype_mhc_class, V1p4MhcClass):
            self.V1p4MHCGenotype_mhc_class = V1p4MhcClass(self.V1p4MHCGenotype_mhc_class)

        if self._is_empty(self.V1p4MHCGenotype_mhc_alleles):
            self.MissingRequiredField("V1p4MHCGenotype_mhc_alleles")
        if not isinstance(self.V1p4MHCGenotype_mhc_alleles, list):
            self.V1p4MHCGenotype_mhc_alleles = [self.V1p4MHCGenotype_mhc_alleles] if self.V1p4MHCGenotype_mhc_alleles is not None else []
        self.V1p4MHCGenotype_mhc_alleles = [v if isinstance(v, V1p4MHCAllele) else V1p4MHCAllele(**as_dict(v)) for v in self.V1p4MHCGenotype_mhc_alleles]

        if self.V1p4MHCGenotype_mhc_genotyping_method is not None and not isinstance(self.V1p4MHCGenotype_mhc_genotyping_method, str):
            self.V1p4MHCGenotype_mhc_genotyping_method = str(self.V1p4MHCGenotype_mhc_genotyping_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4MHCAllele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4MHCAllele"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4MHCAllele"
    class_name: ClassVar[str] = "V1p4MHCAllele"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4MHCAllele

    V1p4MHCAllele_allele_designation: Optional[str] = None
    V1p4MHCAllele_gene: Optional[Union[str, "V1p4Gene"]] = None
    V1p4MHCAllele_reference_set_ref: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4MHCAllele_allele_designation is not None and not isinstance(self.V1p4MHCAllele_allele_designation, str):
            self.V1p4MHCAllele_allele_designation = str(self.V1p4MHCAllele_allele_designation)

        if self.V1p4MHCAllele_reference_set_ref is not None and not isinstance(self.V1p4MHCAllele_reference_set_ref, str):
            self.V1p4MHCAllele_reference_set_ref = str(self.V1p4MHCAllele_reference_set_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SubjectGenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SubjectGenotype"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SubjectGenotype"
    class_name: ClassVar[str] = "V1p4SubjectGenotype"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SubjectGenotype

    V1p4SubjectGenotype_receptor_genotype_set: Optional[Union[dict, V1p4GenotypeSet]] = None
    V1p4SubjectGenotype_mhc_genotype_set: Optional[Union[dict, V1p4MHCGenotypeSet]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.V1p4SubjectGenotype_receptor_genotype_set is not None and not isinstance(self.V1p4SubjectGenotype_receptor_genotype_set, V1p4GenotypeSet):
            self.V1p4SubjectGenotype_receptor_genotype_set = V1p4GenotypeSet(**as_dict(self.V1p4SubjectGenotype_receptor_genotype_set))

        if self.V1p4SubjectGenotype_mhc_genotype_set is not None and not isinstance(self.V1p4SubjectGenotype_mhc_genotype_set, V1p4MHCGenotypeSet):
            self.V1p4SubjectGenotype_mhc_genotype_set = V1p4MHCGenotypeSet(**as_dict(self.V1p4SubjectGenotype_mhc_genotype_set))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Study(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Study"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Study"
    class_name: ClassVar[str] = "V1p4Study"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Study

    V1p4Study_study_id: str = None
    V1p4Study_study_title: str = None
    V1p4Study_study_type: Union[str, "V1p4StudyType"] = None
    V1p4Study_inclusion_exclusion_criteria: str = None
    V1p4Study_grants: str = None
    V1p4Study_contributors: Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]] = None
    V1p4Study_pub_ids: Union[str, List[str]] = None
    V1p4Study_keywords_study: Union[Union[str, "V1p4KeywordsStudy"], List[Union[str, "V1p4KeywordsStudy"]]] = None
    V1p4Study_study_description: Optional[str] = None
    V1p4Study_adc_publish_date: Optional[str] = None
    V1p4Study_adc_update_date: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4Study_study_id):
            self.MissingRequiredField("V1p4Study_study_id")
        if not isinstance(self.V1p4Study_study_id, str):
            self.V1p4Study_study_id = str(self.V1p4Study_study_id)

        if self._is_empty(self.V1p4Study_study_title):
            self.MissingRequiredField("V1p4Study_study_title")
        if not isinstance(self.V1p4Study_study_title, str):
            self.V1p4Study_study_title = str(self.V1p4Study_study_title)

        if self._is_empty(self.V1p4Study_inclusion_exclusion_criteria):
            self.MissingRequiredField("V1p4Study_inclusion_exclusion_criteria")
        if not isinstance(self.V1p4Study_inclusion_exclusion_criteria, str):
            self.V1p4Study_inclusion_exclusion_criteria = str(self.V1p4Study_inclusion_exclusion_criteria)

        if self._is_empty(self.V1p4Study_grants):
            self.MissingRequiredField("V1p4Study_grants")
        if not isinstance(self.V1p4Study_grants, str):
            self.V1p4Study_grants = str(self.V1p4Study_grants)

        if self._is_empty(self.V1p4Study_contributors):
            self.MissingRequiredField("V1p4Study_contributors")
        self._normalize_inlined_as_dict(slot_name="V1p4Study_contributors", slot_type=V1p4Contributor, key_name="V1p4Contributor_contributor_id", keyed=False)

        if self._is_empty(self.V1p4Study_pub_ids):
            self.MissingRequiredField("V1p4Study_pub_ids")
        if not isinstance(self.V1p4Study_pub_ids, list):
            self.V1p4Study_pub_ids = [self.V1p4Study_pub_ids] if self.V1p4Study_pub_ids is not None else []
        self.V1p4Study_pub_ids = [v if isinstance(v, str) else str(v) for v in self.V1p4Study_pub_ids]

        if self._is_empty(self.V1p4Study_keywords_study):
            self.MissingRequiredField("V1p4Study_keywords_study")
        if not isinstance(self.V1p4Study_keywords_study, list):
            self.V1p4Study_keywords_study = [self.V1p4Study_keywords_study] if self.V1p4Study_keywords_study is not None else []
        self.V1p4Study_keywords_study = [v if isinstance(v, V1p4KeywordsStudy) else V1p4KeywordsStudy(v) for v in self.V1p4Study_keywords_study]

        if self.V1p4Study_study_description is not None and not isinstance(self.V1p4Study_study_description, str):
            self.V1p4Study_study_description = str(self.V1p4Study_study_description)

        if self.V1p4Study_adc_publish_date is not None and not isinstance(self.V1p4Study_adc_publish_date, str):
            self.V1p4Study_adc_publish_date = str(self.V1p4Study_adc_publish_date)

        if self.V1p4Study_adc_update_date is not None and not isinstance(self.V1p4Study_adc_update_date, str):
            self.V1p4Study_adc_update_date = str(self.V1p4Study_adc_update_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Subject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Subject"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Subject"
    class_name: ClassVar[str] = "V1p4Subject"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Subject

    V1p4Subject_subject_id: str = None
    V1p4Subject_synthetic: Union[bool, Bool] = None
    V1p4Subject_species: Union[str, "V1p4Species"] = None
    V1p4Subject_sex: Union[str, "V1p4Sex"] = None
    V1p4Subject_age: Union[dict, V1p4TimeInterval] = None
    V1p4Subject_age_event: str = None
    V1p4Subject_ancestry_population: Union[str, "V1p4AncestryPopulation"] = None
    V1p4Subject_ethnicity: str = None
    V1p4Subject_race: str = None
    V1p4Subject_strain_name: str = None
    V1p4Subject_linked_subjects: str = None
    V1p4Subject_link_type: str = None
    V1p4Subject_location_birth: Optional[Union[str, "V1p4LocationBirth"]] = None
    V1p4Subject_diagnosis: Optional[Union[Union[dict, "V1p4Diagnosis"], List[Union[dict, "V1p4Diagnosis"]]]] = empty_list()
    V1p4Subject_genotype: Optional[Union[dict, V1p4SubjectGenotype]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4Subject_subject_id):
            self.MissingRequiredField("V1p4Subject_subject_id")
        if not isinstance(self.V1p4Subject_subject_id, str):
            self.V1p4Subject_subject_id = str(self.V1p4Subject_subject_id)

        if self._is_empty(self.V1p4Subject_synthetic):
            self.MissingRequiredField("V1p4Subject_synthetic")
        if not isinstance(self.V1p4Subject_synthetic, Bool):
            self.V1p4Subject_synthetic = Bool(self.V1p4Subject_synthetic)

        if self._is_empty(self.V1p4Subject_sex):
            self.MissingRequiredField("V1p4Subject_sex")
        if not isinstance(self.V1p4Subject_sex, V1p4Sex):
            self.V1p4Subject_sex = V1p4Sex(self.V1p4Subject_sex)

        if self._is_empty(self.V1p4Subject_age):
            self.MissingRequiredField("V1p4Subject_age")
        if not isinstance(self.V1p4Subject_age, V1p4TimeInterval):
            self.V1p4Subject_age = V1p4TimeInterval(**as_dict(self.V1p4Subject_age))

        if self._is_empty(self.V1p4Subject_age_event):
            self.MissingRequiredField("V1p4Subject_age_event")
        if not isinstance(self.V1p4Subject_age_event, str):
            self.V1p4Subject_age_event = str(self.V1p4Subject_age_event)

        if self._is_empty(self.V1p4Subject_ethnicity):
            self.MissingRequiredField("V1p4Subject_ethnicity")
        if not isinstance(self.V1p4Subject_ethnicity, str):
            self.V1p4Subject_ethnicity = str(self.V1p4Subject_ethnicity)

        if self._is_empty(self.V1p4Subject_race):
            self.MissingRequiredField("V1p4Subject_race")
        if not isinstance(self.V1p4Subject_race, str):
            self.V1p4Subject_race = str(self.V1p4Subject_race)

        if self._is_empty(self.V1p4Subject_strain_name):
            self.MissingRequiredField("V1p4Subject_strain_name")
        if not isinstance(self.V1p4Subject_strain_name, str):
            self.V1p4Subject_strain_name = str(self.V1p4Subject_strain_name)

        if self._is_empty(self.V1p4Subject_linked_subjects):
            self.MissingRequiredField("V1p4Subject_linked_subjects")
        if not isinstance(self.V1p4Subject_linked_subjects, str):
            self.V1p4Subject_linked_subjects = str(self.V1p4Subject_linked_subjects)

        if self._is_empty(self.V1p4Subject_link_type):
            self.MissingRequiredField("V1p4Subject_link_type")
        if not isinstance(self.V1p4Subject_link_type, str):
            self.V1p4Subject_link_type = str(self.V1p4Subject_link_type)

        self._normalize_inlined_as_dict(slot_name="V1p4Subject_diagnosis", slot_type=V1p4Diagnosis, key_name="V1p4Diagnosis_study_group_description", keyed=False)

        if self.V1p4Subject_genotype is not None and not isinstance(self.V1p4Subject_genotype, V1p4SubjectGenotype):
            self.V1p4Subject_genotype = V1p4SubjectGenotype(**as_dict(self.V1p4Subject_genotype))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Diagnosis(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Diagnosis"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Diagnosis"
    class_name: ClassVar[str] = "V1p4Diagnosis"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Diagnosis

    V1p4Diagnosis_study_group_description: str = None
    V1p4Diagnosis_disease_diagnosis: Union[str, "V1p4DiseaseDiagnosis"] = None
    V1p4Diagnosis_disease_length: Union[dict, V1p4TimeQuantity] = None
    V1p4Diagnosis_disease_stage: str = None
    V1p4Diagnosis_prior_therapies: str = None
    V1p4Diagnosis_immunogen: str = None
    V1p4Diagnosis_intervention: str = None
    V1p4Diagnosis_medical_history: str = None
    V1p4Diagnosis_diagnosis_timepoint: Optional[Union[dict, V1p4TimePoint]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4Diagnosis_study_group_description):
            self.MissingRequiredField("V1p4Diagnosis_study_group_description")
        if not isinstance(self.V1p4Diagnosis_study_group_description, str):
            self.V1p4Diagnosis_study_group_description = str(self.V1p4Diagnosis_study_group_description)

        if self._is_empty(self.V1p4Diagnosis_disease_length):
            self.MissingRequiredField("V1p4Diagnosis_disease_length")
        if not isinstance(self.V1p4Diagnosis_disease_length, V1p4TimeQuantity):
            self.V1p4Diagnosis_disease_length = V1p4TimeQuantity(**as_dict(self.V1p4Diagnosis_disease_length))

        if self._is_empty(self.V1p4Diagnosis_disease_stage):
            self.MissingRequiredField("V1p4Diagnosis_disease_stage")
        if not isinstance(self.V1p4Diagnosis_disease_stage, str):
            self.V1p4Diagnosis_disease_stage = str(self.V1p4Diagnosis_disease_stage)

        if self._is_empty(self.V1p4Diagnosis_prior_therapies):
            self.MissingRequiredField("V1p4Diagnosis_prior_therapies")
        if not isinstance(self.V1p4Diagnosis_prior_therapies, str):
            self.V1p4Diagnosis_prior_therapies = str(self.V1p4Diagnosis_prior_therapies)

        if self._is_empty(self.V1p4Diagnosis_immunogen):
            self.MissingRequiredField("V1p4Diagnosis_immunogen")
        if not isinstance(self.V1p4Diagnosis_immunogen, str):
            self.V1p4Diagnosis_immunogen = str(self.V1p4Diagnosis_immunogen)

        if self._is_empty(self.V1p4Diagnosis_intervention):
            self.MissingRequiredField("V1p4Diagnosis_intervention")
        if not isinstance(self.V1p4Diagnosis_intervention, str):
            self.V1p4Diagnosis_intervention = str(self.V1p4Diagnosis_intervention)

        if self._is_empty(self.V1p4Diagnosis_medical_history):
            self.MissingRequiredField("V1p4Diagnosis_medical_history")
        if not isinstance(self.V1p4Diagnosis_medical_history, str):
            self.V1p4Diagnosis_medical_history = str(self.V1p4Diagnosis_medical_history)

        if self.V1p4Diagnosis_diagnosis_timepoint is not None and not isinstance(self.V1p4Diagnosis_diagnosis_timepoint, V1p4TimePoint):
            self.V1p4Diagnosis_diagnosis_timepoint = V1p4TimePoint(**as_dict(self.V1p4Diagnosis_diagnosis_timepoint))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Sample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Sample"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Sample"
    class_name: ClassVar[str] = "V1p4Sample"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Sample

    V1p4Sample_sample_id: str = None
    V1p4Sample_sample_type: str = None
    V1p4Sample_tissue: Union[str, "V1p4Tissue"] = None
    V1p4Sample_anatomic_site: str = None
    V1p4Sample_disease_state_sample: str = None
    V1p4Sample_collection_time_point_relative: Union[dict, V1p4TimePoint] = None
    V1p4Sample_biomaterial_provider: str = None
    V1p4Sample_collection_location: Optional[Union[str, "V1p4CollectionLocation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4Sample_sample_id):
            self.MissingRequiredField("V1p4Sample_sample_id")
        if not isinstance(self.V1p4Sample_sample_id, str):
            self.V1p4Sample_sample_id = str(self.V1p4Sample_sample_id)

        if self._is_empty(self.V1p4Sample_sample_type):
            self.MissingRequiredField("V1p4Sample_sample_type")
        if not isinstance(self.V1p4Sample_sample_type, str):
            self.V1p4Sample_sample_type = str(self.V1p4Sample_sample_type)

        if self._is_empty(self.V1p4Sample_anatomic_site):
            self.MissingRequiredField("V1p4Sample_anatomic_site")
        if not isinstance(self.V1p4Sample_anatomic_site, str):
            self.V1p4Sample_anatomic_site = str(self.V1p4Sample_anatomic_site)

        if self._is_empty(self.V1p4Sample_disease_state_sample):
            self.MissingRequiredField("V1p4Sample_disease_state_sample")
        if not isinstance(self.V1p4Sample_disease_state_sample, str):
            self.V1p4Sample_disease_state_sample = str(self.V1p4Sample_disease_state_sample)

        if self._is_empty(self.V1p4Sample_collection_time_point_relative):
            self.MissingRequiredField("V1p4Sample_collection_time_point_relative")
        if not isinstance(self.V1p4Sample_collection_time_point_relative, V1p4TimePoint):
            self.V1p4Sample_collection_time_point_relative = V1p4TimePoint(**as_dict(self.V1p4Sample_collection_time_point_relative))

        if self._is_empty(self.V1p4Sample_biomaterial_provider):
            self.MissingRequiredField("V1p4Sample_biomaterial_provider")
        if not isinstance(self.V1p4Sample_biomaterial_provider, str):
            self.V1p4Sample_biomaterial_provider = str(self.V1p4Sample_biomaterial_provider)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4CellProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4CellProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4CellProcessing"
    class_name: ClassVar[str] = "V1p4CellProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4CellProcessing

    V1p4CellProcessing_tissue_processing: str = None
    V1p4CellProcessing_cell_subset: Union[str, "V1p4CellSubset"] = None
    V1p4CellProcessing_cell_phenotype: str = None
    V1p4CellProcessing_single_cell: Union[bool, Bool] = None
    V1p4CellProcessing_cell_number: int = None
    V1p4CellProcessing_cells_per_reaction: int = None
    V1p4CellProcessing_cell_storage: Union[bool, Bool] = None
    V1p4CellProcessing_cell_quality: str = None
    V1p4CellProcessing_cell_isolation: str = None
    V1p4CellProcessing_cell_processing_protocol: str = None
    V1p4CellProcessing_cell_label: Optional[str] = None
    V1p4CellProcessing_cell_species: Optional[Union[str, "V1p4CellSpecies"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4CellProcessing_tissue_processing):
            self.MissingRequiredField("V1p4CellProcessing_tissue_processing")
        if not isinstance(self.V1p4CellProcessing_tissue_processing, str):
            self.V1p4CellProcessing_tissue_processing = str(self.V1p4CellProcessing_tissue_processing)

        if self._is_empty(self.V1p4CellProcessing_cell_phenotype):
            self.MissingRequiredField("V1p4CellProcessing_cell_phenotype")
        if not isinstance(self.V1p4CellProcessing_cell_phenotype, str):
            self.V1p4CellProcessing_cell_phenotype = str(self.V1p4CellProcessing_cell_phenotype)

        if self._is_empty(self.V1p4CellProcessing_single_cell):
            self.MissingRequiredField("V1p4CellProcessing_single_cell")
        if not isinstance(self.V1p4CellProcessing_single_cell, Bool):
            self.V1p4CellProcessing_single_cell = Bool(self.V1p4CellProcessing_single_cell)

        if self._is_empty(self.V1p4CellProcessing_cell_number):
            self.MissingRequiredField("V1p4CellProcessing_cell_number")
        if not isinstance(self.V1p4CellProcessing_cell_number, int):
            self.V1p4CellProcessing_cell_number = int(self.V1p4CellProcessing_cell_number)

        if self._is_empty(self.V1p4CellProcessing_cells_per_reaction):
            self.MissingRequiredField("V1p4CellProcessing_cells_per_reaction")
        if not isinstance(self.V1p4CellProcessing_cells_per_reaction, int):
            self.V1p4CellProcessing_cells_per_reaction = int(self.V1p4CellProcessing_cells_per_reaction)

        if self._is_empty(self.V1p4CellProcessing_cell_storage):
            self.MissingRequiredField("V1p4CellProcessing_cell_storage")
        if not isinstance(self.V1p4CellProcessing_cell_storage, Bool):
            self.V1p4CellProcessing_cell_storage = Bool(self.V1p4CellProcessing_cell_storage)

        if self._is_empty(self.V1p4CellProcessing_cell_quality):
            self.MissingRequiredField("V1p4CellProcessing_cell_quality")
        if not isinstance(self.V1p4CellProcessing_cell_quality, str):
            self.V1p4CellProcessing_cell_quality = str(self.V1p4CellProcessing_cell_quality)

        if self._is_empty(self.V1p4CellProcessing_cell_isolation):
            self.MissingRequiredField("V1p4CellProcessing_cell_isolation")
        if not isinstance(self.V1p4CellProcessing_cell_isolation, str):
            self.V1p4CellProcessing_cell_isolation = str(self.V1p4CellProcessing_cell_isolation)

        if self._is_empty(self.V1p4CellProcessing_cell_processing_protocol):
            self.MissingRequiredField("V1p4CellProcessing_cell_processing_protocol")
        if not isinstance(self.V1p4CellProcessing_cell_processing_protocol, str):
            self.V1p4CellProcessing_cell_processing_protocol = str(self.V1p4CellProcessing_cell_processing_protocol)

        if self.V1p4CellProcessing_cell_label is not None and not isinstance(self.V1p4CellProcessing_cell_label, str):
            self.V1p4CellProcessing_cell_label = str(self.V1p4CellProcessing_cell_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4PCRTarget(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4PCRTarget"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4PCRTarget"
    class_name: ClassVar[str] = "V1p4PCRTarget"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4PCRTarget

    V1p4PCRTarget_pcr_target_locus: Union[str, "V1p4PcrTargetLocus"] = None
    V1p4PCRTarget_forward_pcr_primer_target_location: str = None
    V1p4PCRTarget_reverse_pcr_primer_target_location: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4PCRTarget_pcr_target_locus):
            self.MissingRequiredField("V1p4PCRTarget_pcr_target_locus")
        if not isinstance(self.V1p4PCRTarget_pcr_target_locus, V1p4PcrTargetLocus):
            self.V1p4PCRTarget_pcr_target_locus = V1p4PcrTargetLocus(self.V1p4PCRTarget_pcr_target_locus)

        if self._is_empty(self.V1p4PCRTarget_forward_pcr_primer_target_location):
            self.MissingRequiredField("V1p4PCRTarget_forward_pcr_primer_target_location")
        if not isinstance(self.V1p4PCRTarget_forward_pcr_primer_target_location, str):
            self.V1p4PCRTarget_forward_pcr_primer_target_location = str(self.V1p4PCRTarget_forward_pcr_primer_target_location)

        if self._is_empty(self.V1p4PCRTarget_reverse_pcr_primer_target_location):
            self.MissingRequiredField("V1p4PCRTarget_reverse_pcr_primer_target_location")
        if not isinstance(self.V1p4PCRTarget_reverse_pcr_primer_target_location, str):
            self.V1p4PCRTarget_reverse_pcr_primer_target_location = str(self.V1p4PCRTarget_reverse_pcr_primer_target_location)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4NucleicAcidProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4NucleicAcidProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4NucleicAcidProcessing"
    class_name: ClassVar[str] = "V1p4NucleicAcidProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4NucleicAcidProcessing

    V1p4NucleicAcidProcessing_template_class: Union[str, "V1p4TemplateClass"] = None
    V1p4NucleicAcidProcessing_template_quality: str = None
    V1p4NucleicAcidProcessing_template_amount: Union[dict, V1p4PhysicalQuantity] = None
    V1p4NucleicAcidProcessing_library_generation_method: Union[str, "V1p4LibraryGenerationMethod"] = None
    V1p4NucleicAcidProcessing_library_generation_protocol: str = None
    V1p4NucleicAcidProcessing_library_generation_kit_version: str = None
    V1p4NucleicAcidProcessing_complete_sequences: Union[str, "V1p4CompleteSequences"] = None
    V1p4NucleicAcidProcessing_physical_linkage: Union[str, "V1p4PhysicalLinkage"] = None
    V1p4NucleicAcidProcessing_pcr_target: Optional[Union[Union[dict, V1p4PCRTarget], List[Union[dict, V1p4PCRTarget]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4NucleicAcidProcessing_template_class):
            self.MissingRequiredField("V1p4NucleicAcidProcessing_template_class")
        if not isinstance(self.V1p4NucleicAcidProcessing_template_class, V1p4TemplateClass):
            self.V1p4NucleicAcidProcessing_template_class = V1p4TemplateClass(self.V1p4NucleicAcidProcessing_template_class)

        if self._is_empty(self.V1p4NucleicAcidProcessing_template_quality):
            self.MissingRequiredField("V1p4NucleicAcidProcessing_template_quality")
        if not isinstance(self.V1p4NucleicAcidProcessing_template_quality, str):
            self.V1p4NucleicAcidProcessing_template_quality = str(self.V1p4NucleicAcidProcessing_template_quality)

        if self._is_empty(self.V1p4NucleicAcidProcessing_template_amount):
            self.MissingRequiredField("V1p4NucleicAcidProcessing_template_amount")
        if not isinstance(self.V1p4NucleicAcidProcessing_template_amount, V1p4PhysicalQuantity):
            self.V1p4NucleicAcidProcessing_template_amount = V1p4PhysicalQuantity(**as_dict(self.V1p4NucleicAcidProcessing_template_amount))

        if self._is_empty(self.V1p4NucleicAcidProcessing_library_generation_method):
            self.MissingRequiredField("V1p4NucleicAcidProcessing_library_generation_method")
        if not isinstance(self.V1p4NucleicAcidProcessing_library_generation_method, V1p4LibraryGenerationMethod):
            self.V1p4NucleicAcidProcessing_library_generation_method = V1p4LibraryGenerationMethod(self.V1p4NucleicAcidProcessing_library_generation_method)

        if self._is_empty(self.V1p4NucleicAcidProcessing_library_generation_protocol):
            self.MissingRequiredField("V1p4NucleicAcidProcessing_library_generation_protocol")
        if not isinstance(self.V1p4NucleicAcidProcessing_library_generation_protocol, str):
            self.V1p4NucleicAcidProcessing_library_generation_protocol = str(self.V1p4NucleicAcidProcessing_library_generation_protocol)

        if self._is_empty(self.V1p4NucleicAcidProcessing_library_generation_kit_version):
            self.MissingRequiredField("V1p4NucleicAcidProcessing_library_generation_kit_version")
        if not isinstance(self.V1p4NucleicAcidProcessing_library_generation_kit_version, str):
            self.V1p4NucleicAcidProcessing_library_generation_kit_version = str(self.V1p4NucleicAcidProcessing_library_generation_kit_version)

        if self._is_empty(self.V1p4NucleicAcidProcessing_complete_sequences):
            self.MissingRequiredField("V1p4NucleicAcidProcessing_complete_sequences")
        if not isinstance(self.V1p4NucleicAcidProcessing_complete_sequences, V1p4CompleteSequences):
            self.V1p4NucleicAcidProcessing_complete_sequences = V1p4CompleteSequences(self.V1p4NucleicAcidProcessing_complete_sequences)

        if self._is_empty(self.V1p4NucleicAcidProcessing_physical_linkage):
            self.MissingRequiredField("V1p4NucleicAcidProcessing_physical_linkage")
        if not isinstance(self.V1p4NucleicAcidProcessing_physical_linkage, V1p4PhysicalLinkage):
            self.V1p4NucleicAcidProcessing_physical_linkage = V1p4PhysicalLinkage(self.V1p4NucleicAcidProcessing_physical_linkage)

        self._normalize_inlined_as_dict(slot_name="V1p4NucleicAcidProcessing_pcr_target", slot_type=V1p4PCRTarget, key_name="V1p4PCRTarget_pcr_target_locus", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SequencingRun(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SequencingRun"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SequencingRun"
    class_name: ClassVar[str] = "V1p4SequencingRun"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SequencingRun

    V1p4SequencingRun_sequencing_run_id: str = None
    V1p4SequencingRun_total_reads_passing_qc_filter: int = None
    V1p4SequencingRun_sequencing_platform: str = None
    V1p4SequencingRun_sequencing_facility: str = None
    V1p4SequencingRun_sequencing_run_date: str = None
    V1p4SequencingRun_sequencing_kit: str = None
    V1p4SequencingRun_sequencing_files: Optional[Union[dict, "V1p4SequencingData"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4SequencingRun_sequencing_run_id):
            self.MissingRequiredField("V1p4SequencingRun_sequencing_run_id")
        if not isinstance(self.V1p4SequencingRun_sequencing_run_id, str):
            self.V1p4SequencingRun_sequencing_run_id = str(self.V1p4SequencingRun_sequencing_run_id)

        if self._is_empty(self.V1p4SequencingRun_total_reads_passing_qc_filter):
            self.MissingRequiredField("V1p4SequencingRun_total_reads_passing_qc_filter")
        if not isinstance(self.V1p4SequencingRun_total_reads_passing_qc_filter, int):
            self.V1p4SequencingRun_total_reads_passing_qc_filter = int(self.V1p4SequencingRun_total_reads_passing_qc_filter)

        if self._is_empty(self.V1p4SequencingRun_sequencing_platform):
            self.MissingRequiredField("V1p4SequencingRun_sequencing_platform")
        if not isinstance(self.V1p4SequencingRun_sequencing_platform, str):
            self.V1p4SequencingRun_sequencing_platform = str(self.V1p4SequencingRun_sequencing_platform)

        if self._is_empty(self.V1p4SequencingRun_sequencing_facility):
            self.MissingRequiredField("V1p4SequencingRun_sequencing_facility")
        if not isinstance(self.V1p4SequencingRun_sequencing_facility, str):
            self.V1p4SequencingRun_sequencing_facility = str(self.V1p4SequencingRun_sequencing_facility)

        if self._is_empty(self.V1p4SequencingRun_sequencing_run_date):
            self.MissingRequiredField("V1p4SequencingRun_sequencing_run_date")
        if not isinstance(self.V1p4SequencingRun_sequencing_run_date, str):
            self.V1p4SequencingRun_sequencing_run_date = str(self.V1p4SequencingRun_sequencing_run_date)

        if self._is_empty(self.V1p4SequencingRun_sequencing_kit):
            self.MissingRequiredField("V1p4SequencingRun_sequencing_kit")
        if not isinstance(self.V1p4SequencingRun_sequencing_kit, str):
            self.V1p4SequencingRun_sequencing_kit = str(self.V1p4SequencingRun_sequencing_kit)

        if self.V1p4SequencingRun_sequencing_files is not None and not isinstance(self.V1p4SequencingRun_sequencing_files, V1p4SequencingData):
            self.V1p4SequencingRun_sequencing_files = V1p4SequencingData(**as_dict(self.V1p4SequencingRun_sequencing_files))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SequencingData(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SequencingData"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SequencingData"
    class_name: ClassVar[str] = "V1p4SequencingData"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SequencingData

    V1p4SequencingData_sequencing_data_id: str = None
    V1p4SequencingData_file_type: Union[str, "V1p4FileType"] = None
    V1p4SequencingData_filename: str = None
    V1p4SequencingData_read_direction: Union[str, "V1p4ReadDirection"] = None
    V1p4SequencingData_read_length: int = None
    V1p4SequencingData_paired_filename: str = None
    V1p4SequencingData_paired_read_direction: Union[str, "V1p4PairedReadDirection"] = None
    V1p4SequencingData_paired_read_length: int = None
    V1p4SequencingData_index_filename: Optional[str] = None
    V1p4SequencingData_index_length: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4SequencingData_sequencing_data_id):
            self.MissingRequiredField("V1p4SequencingData_sequencing_data_id")
        if not isinstance(self.V1p4SequencingData_sequencing_data_id, str):
            self.V1p4SequencingData_sequencing_data_id = str(self.V1p4SequencingData_sequencing_data_id)

        if self._is_empty(self.V1p4SequencingData_file_type):
            self.MissingRequiredField("V1p4SequencingData_file_type")
        if not isinstance(self.V1p4SequencingData_file_type, V1p4FileType):
            self.V1p4SequencingData_file_type = V1p4FileType(self.V1p4SequencingData_file_type)

        if self._is_empty(self.V1p4SequencingData_filename):
            self.MissingRequiredField("V1p4SequencingData_filename")
        if not isinstance(self.V1p4SequencingData_filename, str):
            self.V1p4SequencingData_filename = str(self.V1p4SequencingData_filename)

        if self._is_empty(self.V1p4SequencingData_read_direction):
            self.MissingRequiredField("V1p4SequencingData_read_direction")
        if not isinstance(self.V1p4SequencingData_read_direction, V1p4ReadDirection):
            self.V1p4SequencingData_read_direction = V1p4ReadDirection(self.V1p4SequencingData_read_direction)

        if self._is_empty(self.V1p4SequencingData_read_length):
            self.MissingRequiredField("V1p4SequencingData_read_length")
        if not isinstance(self.V1p4SequencingData_read_length, int):
            self.V1p4SequencingData_read_length = int(self.V1p4SequencingData_read_length)

        if self._is_empty(self.V1p4SequencingData_paired_filename):
            self.MissingRequiredField("V1p4SequencingData_paired_filename")
        if not isinstance(self.V1p4SequencingData_paired_filename, str):
            self.V1p4SequencingData_paired_filename = str(self.V1p4SequencingData_paired_filename)

        if self._is_empty(self.V1p4SequencingData_paired_read_direction):
            self.MissingRequiredField("V1p4SequencingData_paired_read_direction")
        if not isinstance(self.V1p4SequencingData_paired_read_direction, V1p4PairedReadDirection):
            self.V1p4SequencingData_paired_read_direction = V1p4PairedReadDirection(self.V1p4SequencingData_paired_read_direction)

        if self._is_empty(self.V1p4SequencingData_paired_read_length):
            self.MissingRequiredField("V1p4SequencingData_paired_read_length")
        if not isinstance(self.V1p4SequencingData_paired_read_length, int):
            self.V1p4SequencingData_paired_read_length = int(self.V1p4SequencingData_paired_read_length)

        if self.V1p4SequencingData_index_filename is not None and not isinstance(self.V1p4SequencingData_index_filename, str):
            self.V1p4SequencingData_index_filename = str(self.V1p4SequencingData_index_filename)

        if self.V1p4SequencingData_index_length is not None and not isinstance(self.V1p4SequencingData_index_length, int):
            self.V1p4SequencingData_index_length = int(self.V1p4SequencingData_index_length)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4DataProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4DataProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4DataProcessing"
    class_name: ClassVar[str] = "V1p4DataProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4DataProcessing

    V1p4DataProcessing_software_versions: str = None
    V1p4DataProcessing_paired_reads_assembly: str = None
    V1p4DataProcessing_quality_thresholds: str = None
    V1p4DataProcessing_primer_match_cutoffs: str = None
    V1p4DataProcessing_collapsing_method: str = None
    V1p4DataProcessing_data_processing_protocols: str = None
    V1p4DataProcessing_germline_database: str = None
    V1p4DataProcessing_data_processing_id: Optional[str] = None
    V1p4DataProcessing_primary_annotation: Optional[Union[bool, Bool]] = None
    V1p4DataProcessing_data_processing_files: Optional[Union[str, List[str]]] = empty_list()
    V1p4DataProcessing_germline_set_ref: Optional[str] = None
    V1p4DataProcessing_analysis_provenance_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4DataProcessing_software_versions):
            self.MissingRequiredField("V1p4DataProcessing_software_versions")
        if not isinstance(self.V1p4DataProcessing_software_versions, str):
            self.V1p4DataProcessing_software_versions = str(self.V1p4DataProcessing_software_versions)

        if self._is_empty(self.V1p4DataProcessing_paired_reads_assembly):
            self.MissingRequiredField("V1p4DataProcessing_paired_reads_assembly")
        if not isinstance(self.V1p4DataProcessing_paired_reads_assembly, str):
            self.V1p4DataProcessing_paired_reads_assembly = str(self.V1p4DataProcessing_paired_reads_assembly)

        if self._is_empty(self.V1p4DataProcessing_quality_thresholds):
            self.MissingRequiredField("V1p4DataProcessing_quality_thresholds")
        if not isinstance(self.V1p4DataProcessing_quality_thresholds, str):
            self.V1p4DataProcessing_quality_thresholds = str(self.V1p4DataProcessing_quality_thresholds)

        if self._is_empty(self.V1p4DataProcessing_primer_match_cutoffs):
            self.MissingRequiredField("V1p4DataProcessing_primer_match_cutoffs")
        if not isinstance(self.V1p4DataProcessing_primer_match_cutoffs, str):
            self.V1p4DataProcessing_primer_match_cutoffs = str(self.V1p4DataProcessing_primer_match_cutoffs)

        if self._is_empty(self.V1p4DataProcessing_collapsing_method):
            self.MissingRequiredField("V1p4DataProcessing_collapsing_method")
        if not isinstance(self.V1p4DataProcessing_collapsing_method, str):
            self.V1p4DataProcessing_collapsing_method = str(self.V1p4DataProcessing_collapsing_method)

        if self._is_empty(self.V1p4DataProcessing_data_processing_protocols):
            self.MissingRequiredField("V1p4DataProcessing_data_processing_protocols")
        if not isinstance(self.V1p4DataProcessing_data_processing_protocols, str):
            self.V1p4DataProcessing_data_processing_protocols = str(self.V1p4DataProcessing_data_processing_protocols)

        if self._is_empty(self.V1p4DataProcessing_germline_database):
            self.MissingRequiredField("V1p4DataProcessing_germline_database")
        if not isinstance(self.V1p4DataProcessing_germline_database, str):
            self.V1p4DataProcessing_germline_database = str(self.V1p4DataProcessing_germline_database)

        if self.V1p4DataProcessing_data_processing_id is not None and not isinstance(self.V1p4DataProcessing_data_processing_id, str):
            self.V1p4DataProcessing_data_processing_id = str(self.V1p4DataProcessing_data_processing_id)

        if self.V1p4DataProcessing_primary_annotation is not None and not isinstance(self.V1p4DataProcessing_primary_annotation, Bool):
            self.V1p4DataProcessing_primary_annotation = Bool(self.V1p4DataProcessing_primary_annotation)

        if not isinstance(self.V1p4DataProcessing_data_processing_files, list):
            self.V1p4DataProcessing_data_processing_files = [self.V1p4DataProcessing_data_processing_files] if self.V1p4DataProcessing_data_processing_files is not None else []
        self.V1p4DataProcessing_data_processing_files = [v if isinstance(v, str) else str(v) for v in self.V1p4DataProcessing_data_processing_files]

        if self.V1p4DataProcessing_germline_set_ref is not None and not isinstance(self.V1p4DataProcessing_germline_set_ref, str):
            self.V1p4DataProcessing_germline_set_ref = str(self.V1p4DataProcessing_germline_set_ref)

        if self.V1p4DataProcessing_analysis_provenance_id is not None and not isinstance(self.V1p4DataProcessing_analysis_provenance_id, str):
            self.V1p4DataProcessing_analysis_provenance_id = str(self.V1p4DataProcessing_analysis_provenance_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Repertoire(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Repertoire"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Repertoire"
    class_name: ClassVar[str] = "V1p4Repertoire"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Repertoire

    V1p4Repertoire_study: Union[dict, V1p4Study] = None
    V1p4Repertoire_subject: Union[dict, V1p4Subject] = None
    V1p4Repertoire_sample: Union[Union[dict, "V1p4SampleProcessing"], List[Union[dict, "V1p4SampleProcessing"]]] = None
    V1p4Repertoire_data_processing: Union[Union[dict, V1p4DataProcessing], List[Union[dict, V1p4DataProcessing]]] = None
    V1p4Repertoire_repertoire_id: Optional[str] = None
    V1p4Repertoire_repertoire_name: Optional[str] = None
    V1p4Repertoire_repertoire_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4Repertoire_study):
            self.MissingRequiredField("V1p4Repertoire_study")
        if not isinstance(self.V1p4Repertoire_study, V1p4Study):
            self.V1p4Repertoire_study = V1p4Study(**as_dict(self.V1p4Repertoire_study))

        if self._is_empty(self.V1p4Repertoire_subject):
            self.MissingRequiredField("V1p4Repertoire_subject")
        if not isinstance(self.V1p4Repertoire_subject, V1p4Subject):
            self.V1p4Repertoire_subject = V1p4Subject(**as_dict(self.V1p4Repertoire_subject))

        if self._is_empty(self.V1p4Repertoire_sample):
            self.MissingRequiredField("V1p4Repertoire_sample")
        self._normalize_inlined_as_dict(slot_name="V1p4Repertoire_sample", slot_type=V1p4SampleProcessing, key_name="V1p4Sample_sample_id", keyed=False)

        if self._is_empty(self.V1p4Repertoire_data_processing):
            self.MissingRequiredField("V1p4Repertoire_data_processing")
        self._normalize_inlined_as_dict(slot_name="V1p4Repertoire_data_processing", slot_type=V1p4DataProcessing, key_name="V1p4DataProcessing_software_versions", keyed=False)

        if self.V1p4Repertoire_repertoire_id is not None and not isinstance(self.V1p4Repertoire_repertoire_id, str):
            self.V1p4Repertoire_repertoire_id = str(self.V1p4Repertoire_repertoire_id)

        if self.V1p4Repertoire_repertoire_name is not None and not isinstance(self.V1p4Repertoire_repertoire_name, str):
            self.V1p4Repertoire_repertoire_name = str(self.V1p4Repertoire_repertoire_name)

        if self.V1p4Repertoire_repertoire_description is not None and not isinstance(self.V1p4Repertoire_repertoire_description, str):
            self.V1p4Repertoire_repertoire_description = str(self.V1p4Repertoire_repertoire_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4RepertoireGroup(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4RepertoireGroup"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4RepertoireGroup"
    class_name: ClassVar[str] = "V1p4RepertoireGroup"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4RepertoireGroup

    V1p4RepertoireGroup_repertoire_group_id: str = None
    V1p4RepertoireGroup_repertoires: Union[str, List[str]] = None
    V1p4RepertoireGroup_repertoire_group_name: Optional[str] = None
    V1p4RepertoireGroup_repertoire_group_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4RepertoireGroup_repertoire_group_id):
            self.MissingRequiredField("V1p4RepertoireGroup_repertoire_group_id")
        if not isinstance(self.V1p4RepertoireGroup_repertoire_group_id, str):
            self.V1p4RepertoireGroup_repertoire_group_id = str(self.V1p4RepertoireGroup_repertoire_group_id)

        if self._is_empty(self.V1p4RepertoireGroup_repertoires):
            self.MissingRequiredField("V1p4RepertoireGroup_repertoires")
        if not isinstance(self.V1p4RepertoireGroup_repertoires, list):
            self.V1p4RepertoireGroup_repertoires = [self.V1p4RepertoireGroup_repertoires] if self.V1p4RepertoireGroup_repertoires is not None else []
        self.V1p4RepertoireGroup_repertoires = [v if isinstance(v, str) else str(v) for v in self.V1p4RepertoireGroup_repertoires]

        if self.V1p4RepertoireGroup_repertoire_group_name is not None and not isinstance(self.V1p4RepertoireGroup_repertoire_group_name, str):
            self.V1p4RepertoireGroup_repertoire_group_name = str(self.V1p4RepertoireGroup_repertoire_group_name)

        if self.V1p4RepertoireGroup_repertoire_group_description is not None and not isinstance(self.V1p4RepertoireGroup_repertoire_group_description, str):
            self.V1p4RepertoireGroup_repertoire_group_description = str(self.V1p4RepertoireGroup_repertoire_group_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Alignment(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Alignment"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Alignment"
    class_name: ClassVar[str] = "V1p4Alignment"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Alignment

    V1p4Alignment_sequence_id: str = None
    V1p4Alignment_segment: str = None
    V1p4Alignment_call: str = None
    V1p4Alignment_score: float = None
    V1p4Alignment_cigar: str = None
    V1p4Alignment_rev_comp: Optional[Union[bool, Bool]] = None
    V1p4Alignment_identity: Optional[float] = None
    V1p4Alignment_support: Optional[float] = None
    V1p4Alignment_sequence_start: Optional[int] = None
    V1p4Alignment_sequence_end: Optional[int] = None
    V1p4Alignment_germline_start: Optional[int] = None
    V1p4Alignment_germline_end: Optional[int] = None
    V1p4Alignment_rank: Optional[int] = None
    V1p4Alignment_data_processing_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4Alignment_sequence_id):
            self.MissingRequiredField("V1p4Alignment_sequence_id")
        if not isinstance(self.V1p4Alignment_sequence_id, str):
            self.V1p4Alignment_sequence_id = str(self.V1p4Alignment_sequence_id)

        if self._is_empty(self.V1p4Alignment_segment):
            self.MissingRequiredField("V1p4Alignment_segment")
        if not isinstance(self.V1p4Alignment_segment, str):
            self.V1p4Alignment_segment = str(self.V1p4Alignment_segment)

        if self._is_empty(self.V1p4Alignment_call):
            self.MissingRequiredField("V1p4Alignment_call")
        if not isinstance(self.V1p4Alignment_call, str):
            self.V1p4Alignment_call = str(self.V1p4Alignment_call)

        if self._is_empty(self.V1p4Alignment_score):
            self.MissingRequiredField("V1p4Alignment_score")
        if not isinstance(self.V1p4Alignment_score, float):
            self.V1p4Alignment_score = float(self.V1p4Alignment_score)

        if self._is_empty(self.V1p4Alignment_cigar):
            self.MissingRequiredField("V1p4Alignment_cigar")
        if not isinstance(self.V1p4Alignment_cigar, str):
            self.V1p4Alignment_cigar = str(self.V1p4Alignment_cigar)

        if self.V1p4Alignment_rev_comp is not None and not isinstance(self.V1p4Alignment_rev_comp, Bool):
            self.V1p4Alignment_rev_comp = Bool(self.V1p4Alignment_rev_comp)

        if self.V1p4Alignment_identity is not None and not isinstance(self.V1p4Alignment_identity, float):
            self.V1p4Alignment_identity = float(self.V1p4Alignment_identity)

        if self.V1p4Alignment_support is not None and not isinstance(self.V1p4Alignment_support, float):
            self.V1p4Alignment_support = float(self.V1p4Alignment_support)

        if self.V1p4Alignment_sequence_start is not None and not isinstance(self.V1p4Alignment_sequence_start, int):
            self.V1p4Alignment_sequence_start = int(self.V1p4Alignment_sequence_start)

        if self.V1p4Alignment_sequence_end is not None and not isinstance(self.V1p4Alignment_sequence_end, int):
            self.V1p4Alignment_sequence_end = int(self.V1p4Alignment_sequence_end)

        if self.V1p4Alignment_germline_start is not None and not isinstance(self.V1p4Alignment_germline_start, int):
            self.V1p4Alignment_germline_start = int(self.V1p4Alignment_germline_start)

        if self.V1p4Alignment_germline_end is not None and not isinstance(self.V1p4Alignment_germline_end, int):
            self.V1p4Alignment_germline_end = int(self.V1p4Alignment_germline_end)

        if self.V1p4Alignment_rank is not None and not isinstance(self.V1p4Alignment_rank, int):
            self.V1p4Alignment_rank = int(self.V1p4Alignment_rank)

        if self.V1p4Alignment_data_processing_id is not None and not isinstance(self.V1p4Alignment_data_processing_id, str):
            self.V1p4Alignment_data_processing_id = str(self.V1p4Alignment_data_processing_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Rearrangement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Rearrangement"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Rearrangement"
    class_name: ClassVar[str] = "V1p4Rearrangement"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Rearrangement

    V1p4Rearrangement_sequence_id: str = None
    V1p4Rearrangement_sequence: str = None
    V1p4Rearrangement_rev_comp: Union[bool, Bool] = None
    V1p4Rearrangement_productive: Union[bool, Bool] = None
    V1p4Rearrangement_v_call: str = None
    V1p4Rearrangement_d_call: str = None
    V1p4Rearrangement_j_call: str = None
    V1p4Rearrangement_sequence_alignment: str = None
    V1p4Rearrangement_germline_alignment: str = None
    V1p4Rearrangement_junction: str = None
    V1p4Rearrangement_junction_aa: str = None
    V1p4Rearrangement_v_cigar: str = None
    V1p4Rearrangement_d_cigar: str = None
    V1p4Rearrangement_j_cigar: str = None
    V1p4Rearrangement_quality: Optional[str] = None
    V1p4Rearrangement_sequence_aa: Optional[str] = None
    V1p4Rearrangement_vj_in_frame: Optional[Union[bool, Bool]] = None
    V1p4Rearrangement_stop_codon: Optional[Union[bool, Bool]] = None
    V1p4Rearrangement_complete_vdj: Optional[Union[bool, Bool]] = None
    V1p4Rearrangement_locus: Optional[Union[str, "V1p4Locus"]] = None
    V1p4Rearrangement_locus_species: Optional[Union[str, "V1p4LocusSpecies"]] = None
    V1p4Rearrangement_d2_call: Optional[str] = None
    V1p4Rearrangement_c_call: Optional[str] = None
    V1p4Rearrangement_quality_alignment: Optional[str] = None
    V1p4Rearrangement_sequence_alignment_aa: Optional[str] = None
    V1p4Rearrangement_germline_alignment_aa: Optional[str] = None
    V1p4Rearrangement_np1: Optional[str] = None
    V1p4Rearrangement_np1_aa: Optional[str] = None
    V1p4Rearrangement_np2: Optional[str] = None
    V1p4Rearrangement_np2_aa: Optional[str] = None
    V1p4Rearrangement_np3: Optional[str] = None
    V1p4Rearrangement_np3_aa: Optional[str] = None
    V1p4Rearrangement_cdr1: Optional[str] = None
    V1p4Rearrangement_cdr1_aa: Optional[str] = None
    V1p4Rearrangement_cdr2: Optional[str] = None
    V1p4Rearrangement_cdr2_aa: Optional[str] = None
    V1p4Rearrangement_cdr3: Optional[str] = None
    V1p4Rearrangement_cdr3_aa: Optional[str] = None
    V1p4Rearrangement_fwr1: Optional[str] = None
    V1p4Rearrangement_fwr1_aa: Optional[str] = None
    V1p4Rearrangement_fwr2: Optional[str] = None
    V1p4Rearrangement_fwr2_aa: Optional[str] = None
    V1p4Rearrangement_fwr3: Optional[str] = None
    V1p4Rearrangement_fwr3_aa: Optional[str] = None
    V1p4Rearrangement_fwr4: Optional[str] = None
    V1p4Rearrangement_fwr4_aa: Optional[str] = None
    V1p4Rearrangement_v_score: Optional[float] = None
    V1p4Rearrangement_v_identity: Optional[float] = None
    V1p4Rearrangement_v_support: Optional[float] = None
    V1p4Rearrangement_d_score: Optional[float] = None
    V1p4Rearrangement_d_identity: Optional[float] = None
    V1p4Rearrangement_d_support: Optional[float] = None
    V1p4Rearrangement_d2_score: Optional[float] = None
    V1p4Rearrangement_d2_identity: Optional[float] = None
    V1p4Rearrangement_d2_support: Optional[float] = None
    V1p4Rearrangement_d2_cigar: Optional[str] = None
    V1p4Rearrangement_j_score: Optional[float] = None
    V1p4Rearrangement_j_identity: Optional[float] = None
    V1p4Rearrangement_j_support: Optional[float] = None
    V1p4Rearrangement_c_score: Optional[float] = None
    V1p4Rearrangement_c_identity: Optional[float] = None
    V1p4Rearrangement_c_support: Optional[float] = None
    V1p4Rearrangement_c_cigar: Optional[str] = None
    V1p4Rearrangement_v_sequence_start: Optional[int] = None
    V1p4Rearrangement_v_sequence_end: Optional[int] = None
    V1p4Rearrangement_v_germline_start: Optional[int] = None
    V1p4Rearrangement_v_germline_end: Optional[int] = None
    V1p4Rearrangement_v_alignment_start: Optional[int] = None
    V1p4Rearrangement_v_alignment_end: Optional[int] = None
    V1p4Rearrangement_d_sequence_start: Optional[int] = None
    V1p4Rearrangement_d_sequence_end: Optional[int] = None
    V1p4Rearrangement_d_germline_start: Optional[int] = None
    V1p4Rearrangement_d_germline_end: Optional[int] = None
    V1p4Rearrangement_d_alignment_start: Optional[int] = None
    V1p4Rearrangement_d_alignment_end: Optional[int] = None
    V1p4Rearrangement_d2_sequence_start: Optional[int] = None
    V1p4Rearrangement_d2_sequence_end: Optional[int] = None
    V1p4Rearrangement_d2_germline_start: Optional[int] = None
    V1p4Rearrangement_d2_germline_end: Optional[int] = None
    V1p4Rearrangement_d2_alignment_start: Optional[int] = None
    V1p4Rearrangement_d2_alignment_end: Optional[int] = None
    V1p4Rearrangement_j_sequence_start: Optional[int] = None
    V1p4Rearrangement_j_sequence_end: Optional[int] = None
    V1p4Rearrangement_j_germline_start: Optional[int] = None
    V1p4Rearrangement_j_germline_end: Optional[int] = None
    V1p4Rearrangement_j_alignment_start: Optional[int] = None
    V1p4Rearrangement_j_alignment_end: Optional[int] = None
    V1p4Rearrangement_c_sequence_start: Optional[int] = None
    V1p4Rearrangement_c_sequence_end: Optional[int] = None
    V1p4Rearrangement_c_germline_start: Optional[int] = None
    V1p4Rearrangement_c_germline_end: Optional[int] = None
    V1p4Rearrangement_c_alignment_start: Optional[int] = None
    V1p4Rearrangement_c_alignment_end: Optional[int] = None
    V1p4Rearrangement_cdr1_start: Optional[int] = None
    V1p4Rearrangement_cdr1_end: Optional[int] = None
    V1p4Rearrangement_cdr2_start: Optional[int] = None
    V1p4Rearrangement_cdr2_end: Optional[int] = None
    V1p4Rearrangement_cdr3_start: Optional[int] = None
    V1p4Rearrangement_cdr3_end: Optional[int] = None
    V1p4Rearrangement_fwr1_start: Optional[int] = None
    V1p4Rearrangement_fwr1_end: Optional[int] = None
    V1p4Rearrangement_fwr2_start: Optional[int] = None
    V1p4Rearrangement_fwr2_end: Optional[int] = None
    V1p4Rearrangement_fwr3_start: Optional[int] = None
    V1p4Rearrangement_fwr3_end: Optional[int] = None
    V1p4Rearrangement_fwr4_start: Optional[int] = None
    V1p4Rearrangement_fwr4_end: Optional[int] = None
    V1p4Rearrangement_v_sequence_alignment: Optional[str] = None
    V1p4Rearrangement_v_sequence_alignment_aa: Optional[str] = None
    V1p4Rearrangement_d_sequence_alignment: Optional[str] = None
    V1p4Rearrangement_d_sequence_alignment_aa: Optional[str] = None
    V1p4Rearrangement_d2_sequence_alignment: Optional[str] = None
    V1p4Rearrangement_d2_sequence_alignment_aa: Optional[str] = None
    V1p4Rearrangement_j_sequence_alignment: Optional[str] = None
    V1p4Rearrangement_j_sequence_alignment_aa: Optional[str] = None
    V1p4Rearrangement_c_sequence_alignment: Optional[str] = None
    V1p4Rearrangement_c_sequence_alignment_aa: Optional[str] = None
    V1p4Rearrangement_v_germline_alignment: Optional[str] = None
    V1p4Rearrangement_v_germline_alignment_aa: Optional[str] = None
    V1p4Rearrangement_d_germline_alignment: Optional[str] = None
    V1p4Rearrangement_d_germline_alignment_aa: Optional[str] = None
    V1p4Rearrangement_d2_germline_alignment: Optional[str] = None
    V1p4Rearrangement_d2_germline_alignment_aa: Optional[str] = None
    V1p4Rearrangement_j_germline_alignment: Optional[str] = None
    V1p4Rearrangement_j_germline_alignment_aa: Optional[str] = None
    V1p4Rearrangement_c_germline_alignment: Optional[str] = None
    V1p4Rearrangement_c_germline_alignment_aa: Optional[str] = None
    V1p4Rearrangement_junction_length: Optional[int] = None
    V1p4Rearrangement_junction_aa_length: Optional[int] = None
    V1p4Rearrangement_np1_length: Optional[int] = None
    V1p4Rearrangement_np2_length: Optional[int] = None
    V1p4Rearrangement_np3_length: Optional[int] = None
    V1p4Rearrangement_n1_length: Optional[int] = None
    V1p4Rearrangement_n2_length: Optional[int] = None
    V1p4Rearrangement_n3_length: Optional[int] = None
    V1p4Rearrangement_p3v_length: Optional[int] = None
    V1p4Rearrangement_p5d_length: Optional[int] = None
    V1p4Rearrangement_p3d_length: Optional[int] = None
    V1p4Rearrangement_p5d2_length: Optional[int] = None
    V1p4Rearrangement_p3d2_length: Optional[int] = None
    V1p4Rearrangement_p5j_length: Optional[int] = None
    V1p4Rearrangement_v_frameshift: Optional[Union[bool, Bool]] = None
    V1p4Rearrangement_j_frameshift: Optional[Union[bool, Bool]] = None
    V1p4Rearrangement_d_frame: Optional[int] = None
    V1p4Rearrangement_d2_frame: Optional[int] = None
    V1p4Rearrangement_consensus_count: Optional[int] = None
    V1p4Rearrangement_duplicate_count: Optional[int] = None
    V1p4Rearrangement_umi_count: Optional[int] = None
    V1p4Rearrangement_cell_id: Optional[str] = None
    V1p4Rearrangement_clone_id: Optional[str] = None
    V1p4Rearrangement_reactivity_id: Optional[str] = None
    V1p4Rearrangement_reactivity_ref: Optional[str] = None
    V1p4Rearrangement_repertoire_id: Optional[str] = None
    V1p4Rearrangement_sample_processing_id: Optional[str] = None
    V1p4Rearrangement_data_processing_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4Rearrangement_sequence_id):
            self.MissingRequiredField("V1p4Rearrangement_sequence_id")
        if not isinstance(self.V1p4Rearrangement_sequence_id, str):
            self.V1p4Rearrangement_sequence_id = str(self.V1p4Rearrangement_sequence_id)

        if self._is_empty(self.V1p4Rearrangement_sequence):
            self.MissingRequiredField("V1p4Rearrangement_sequence")
        if not isinstance(self.V1p4Rearrangement_sequence, str):
            self.V1p4Rearrangement_sequence = str(self.V1p4Rearrangement_sequence)

        if self._is_empty(self.V1p4Rearrangement_rev_comp):
            self.MissingRequiredField("V1p4Rearrangement_rev_comp")
        if not isinstance(self.V1p4Rearrangement_rev_comp, Bool):
            self.V1p4Rearrangement_rev_comp = Bool(self.V1p4Rearrangement_rev_comp)

        if self._is_empty(self.V1p4Rearrangement_productive):
            self.MissingRequiredField("V1p4Rearrangement_productive")
        if not isinstance(self.V1p4Rearrangement_productive, Bool):
            self.V1p4Rearrangement_productive = Bool(self.V1p4Rearrangement_productive)

        if self._is_empty(self.V1p4Rearrangement_v_call):
            self.MissingRequiredField("V1p4Rearrangement_v_call")
        if not isinstance(self.V1p4Rearrangement_v_call, str):
            self.V1p4Rearrangement_v_call = str(self.V1p4Rearrangement_v_call)

        if self._is_empty(self.V1p4Rearrangement_d_call):
            self.MissingRequiredField("V1p4Rearrangement_d_call")
        if not isinstance(self.V1p4Rearrangement_d_call, str):
            self.V1p4Rearrangement_d_call = str(self.V1p4Rearrangement_d_call)

        if self._is_empty(self.V1p4Rearrangement_j_call):
            self.MissingRequiredField("V1p4Rearrangement_j_call")
        if not isinstance(self.V1p4Rearrangement_j_call, str):
            self.V1p4Rearrangement_j_call = str(self.V1p4Rearrangement_j_call)

        if self._is_empty(self.V1p4Rearrangement_sequence_alignment):
            self.MissingRequiredField("V1p4Rearrangement_sequence_alignment")
        if not isinstance(self.V1p4Rearrangement_sequence_alignment, str):
            self.V1p4Rearrangement_sequence_alignment = str(self.V1p4Rearrangement_sequence_alignment)

        if self._is_empty(self.V1p4Rearrangement_germline_alignment):
            self.MissingRequiredField("V1p4Rearrangement_germline_alignment")
        if not isinstance(self.V1p4Rearrangement_germline_alignment, str):
            self.V1p4Rearrangement_germline_alignment = str(self.V1p4Rearrangement_germline_alignment)

        if self._is_empty(self.V1p4Rearrangement_junction):
            self.MissingRequiredField("V1p4Rearrangement_junction")
        if not isinstance(self.V1p4Rearrangement_junction, str):
            self.V1p4Rearrangement_junction = str(self.V1p4Rearrangement_junction)

        if self._is_empty(self.V1p4Rearrangement_junction_aa):
            self.MissingRequiredField("V1p4Rearrangement_junction_aa")
        if not isinstance(self.V1p4Rearrangement_junction_aa, str):
            self.V1p4Rearrangement_junction_aa = str(self.V1p4Rearrangement_junction_aa)

        if self._is_empty(self.V1p4Rearrangement_v_cigar):
            self.MissingRequiredField("V1p4Rearrangement_v_cigar")
        if not isinstance(self.V1p4Rearrangement_v_cigar, str):
            self.V1p4Rearrangement_v_cigar = str(self.V1p4Rearrangement_v_cigar)

        if self._is_empty(self.V1p4Rearrangement_d_cigar):
            self.MissingRequiredField("V1p4Rearrangement_d_cigar")
        if not isinstance(self.V1p4Rearrangement_d_cigar, str):
            self.V1p4Rearrangement_d_cigar = str(self.V1p4Rearrangement_d_cigar)

        if self._is_empty(self.V1p4Rearrangement_j_cigar):
            self.MissingRequiredField("V1p4Rearrangement_j_cigar")
        if not isinstance(self.V1p4Rearrangement_j_cigar, str):
            self.V1p4Rearrangement_j_cigar = str(self.V1p4Rearrangement_j_cigar)

        if self.V1p4Rearrangement_quality is not None and not isinstance(self.V1p4Rearrangement_quality, str):
            self.V1p4Rearrangement_quality = str(self.V1p4Rearrangement_quality)

        if self.V1p4Rearrangement_sequence_aa is not None and not isinstance(self.V1p4Rearrangement_sequence_aa, str):
            self.V1p4Rearrangement_sequence_aa = str(self.V1p4Rearrangement_sequence_aa)

        if self.V1p4Rearrangement_vj_in_frame is not None and not isinstance(self.V1p4Rearrangement_vj_in_frame, Bool):
            self.V1p4Rearrangement_vj_in_frame = Bool(self.V1p4Rearrangement_vj_in_frame)

        if self.V1p4Rearrangement_stop_codon is not None and not isinstance(self.V1p4Rearrangement_stop_codon, Bool):
            self.V1p4Rearrangement_stop_codon = Bool(self.V1p4Rearrangement_stop_codon)

        if self.V1p4Rearrangement_complete_vdj is not None and not isinstance(self.V1p4Rearrangement_complete_vdj, Bool):
            self.V1p4Rearrangement_complete_vdj = Bool(self.V1p4Rearrangement_complete_vdj)

        if self.V1p4Rearrangement_locus is not None and not isinstance(self.V1p4Rearrangement_locus, V1p4Locus):
            self.V1p4Rearrangement_locus = V1p4Locus(self.V1p4Rearrangement_locus)

        if self.V1p4Rearrangement_d2_call is not None and not isinstance(self.V1p4Rearrangement_d2_call, str):
            self.V1p4Rearrangement_d2_call = str(self.V1p4Rearrangement_d2_call)

        if self.V1p4Rearrangement_c_call is not None and not isinstance(self.V1p4Rearrangement_c_call, str):
            self.V1p4Rearrangement_c_call = str(self.V1p4Rearrangement_c_call)

        if self.V1p4Rearrangement_quality_alignment is not None and not isinstance(self.V1p4Rearrangement_quality_alignment, str):
            self.V1p4Rearrangement_quality_alignment = str(self.V1p4Rearrangement_quality_alignment)

        if self.V1p4Rearrangement_sequence_alignment_aa is not None and not isinstance(self.V1p4Rearrangement_sequence_alignment_aa, str):
            self.V1p4Rearrangement_sequence_alignment_aa = str(self.V1p4Rearrangement_sequence_alignment_aa)

        if self.V1p4Rearrangement_germline_alignment_aa is not None and not isinstance(self.V1p4Rearrangement_germline_alignment_aa, str):
            self.V1p4Rearrangement_germline_alignment_aa = str(self.V1p4Rearrangement_germline_alignment_aa)

        if self.V1p4Rearrangement_np1 is not None and not isinstance(self.V1p4Rearrangement_np1, str):
            self.V1p4Rearrangement_np1 = str(self.V1p4Rearrangement_np1)

        if self.V1p4Rearrangement_np1_aa is not None and not isinstance(self.V1p4Rearrangement_np1_aa, str):
            self.V1p4Rearrangement_np1_aa = str(self.V1p4Rearrangement_np1_aa)

        if self.V1p4Rearrangement_np2 is not None and not isinstance(self.V1p4Rearrangement_np2, str):
            self.V1p4Rearrangement_np2 = str(self.V1p4Rearrangement_np2)

        if self.V1p4Rearrangement_np2_aa is not None and not isinstance(self.V1p4Rearrangement_np2_aa, str):
            self.V1p4Rearrangement_np2_aa = str(self.V1p4Rearrangement_np2_aa)

        if self.V1p4Rearrangement_np3 is not None and not isinstance(self.V1p4Rearrangement_np3, str):
            self.V1p4Rearrangement_np3 = str(self.V1p4Rearrangement_np3)

        if self.V1p4Rearrangement_np3_aa is not None and not isinstance(self.V1p4Rearrangement_np3_aa, str):
            self.V1p4Rearrangement_np3_aa = str(self.V1p4Rearrangement_np3_aa)

        if self.V1p4Rearrangement_cdr1 is not None and not isinstance(self.V1p4Rearrangement_cdr1, str):
            self.V1p4Rearrangement_cdr1 = str(self.V1p4Rearrangement_cdr1)

        if self.V1p4Rearrangement_cdr1_aa is not None and not isinstance(self.V1p4Rearrangement_cdr1_aa, str):
            self.V1p4Rearrangement_cdr1_aa = str(self.V1p4Rearrangement_cdr1_aa)

        if self.V1p4Rearrangement_cdr2 is not None and not isinstance(self.V1p4Rearrangement_cdr2, str):
            self.V1p4Rearrangement_cdr2 = str(self.V1p4Rearrangement_cdr2)

        if self.V1p4Rearrangement_cdr2_aa is not None and not isinstance(self.V1p4Rearrangement_cdr2_aa, str):
            self.V1p4Rearrangement_cdr2_aa = str(self.V1p4Rearrangement_cdr2_aa)

        if self.V1p4Rearrangement_cdr3 is not None and not isinstance(self.V1p4Rearrangement_cdr3, str):
            self.V1p4Rearrangement_cdr3 = str(self.V1p4Rearrangement_cdr3)

        if self.V1p4Rearrangement_cdr3_aa is not None and not isinstance(self.V1p4Rearrangement_cdr3_aa, str):
            self.V1p4Rearrangement_cdr3_aa = str(self.V1p4Rearrangement_cdr3_aa)

        if self.V1p4Rearrangement_fwr1 is not None and not isinstance(self.V1p4Rearrangement_fwr1, str):
            self.V1p4Rearrangement_fwr1 = str(self.V1p4Rearrangement_fwr1)

        if self.V1p4Rearrangement_fwr1_aa is not None and not isinstance(self.V1p4Rearrangement_fwr1_aa, str):
            self.V1p4Rearrangement_fwr1_aa = str(self.V1p4Rearrangement_fwr1_aa)

        if self.V1p4Rearrangement_fwr2 is not None and not isinstance(self.V1p4Rearrangement_fwr2, str):
            self.V1p4Rearrangement_fwr2 = str(self.V1p4Rearrangement_fwr2)

        if self.V1p4Rearrangement_fwr2_aa is not None and not isinstance(self.V1p4Rearrangement_fwr2_aa, str):
            self.V1p4Rearrangement_fwr2_aa = str(self.V1p4Rearrangement_fwr2_aa)

        if self.V1p4Rearrangement_fwr3 is not None and not isinstance(self.V1p4Rearrangement_fwr3, str):
            self.V1p4Rearrangement_fwr3 = str(self.V1p4Rearrangement_fwr3)

        if self.V1p4Rearrangement_fwr3_aa is not None and not isinstance(self.V1p4Rearrangement_fwr3_aa, str):
            self.V1p4Rearrangement_fwr3_aa = str(self.V1p4Rearrangement_fwr3_aa)

        if self.V1p4Rearrangement_fwr4 is not None and not isinstance(self.V1p4Rearrangement_fwr4, str):
            self.V1p4Rearrangement_fwr4 = str(self.V1p4Rearrangement_fwr4)

        if self.V1p4Rearrangement_fwr4_aa is not None and not isinstance(self.V1p4Rearrangement_fwr4_aa, str):
            self.V1p4Rearrangement_fwr4_aa = str(self.V1p4Rearrangement_fwr4_aa)

        if self.V1p4Rearrangement_v_score is not None and not isinstance(self.V1p4Rearrangement_v_score, float):
            self.V1p4Rearrangement_v_score = float(self.V1p4Rearrangement_v_score)

        if self.V1p4Rearrangement_v_identity is not None and not isinstance(self.V1p4Rearrangement_v_identity, float):
            self.V1p4Rearrangement_v_identity = float(self.V1p4Rearrangement_v_identity)

        if self.V1p4Rearrangement_v_support is not None and not isinstance(self.V1p4Rearrangement_v_support, float):
            self.V1p4Rearrangement_v_support = float(self.V1p4Rearrangement_v_support)

        if self.V1p4Rearrangement_d_score is not None and not isinstance(self.V1p4Rearrangement_d_score, float):
            self.V1p4Rearrangement_d_score = float(self.V1p4Rearrangement_d_score)

        if self.V1p4Rearrangement_d_identity is not None and not isinstance(self.V1p4Rearrangement_d_identity, float):
            self.V1p4Rearrangement_d_identity = float(self.V1p4Rearrangement_d_identity)

        if self.V1p4Rearrangement_d_support is not None and not isinstance(self.V1p4Rearrangement_d_support, float):
            self.V1p4Rearrangement_d_support = float(self.V1p4Rearrangement_d_support)

        if self.V1p4Rearrangement_d2_score is not None and not isinstance(self.V1p4Rearrangement_d2_score, float):
            self.V1p4Rearrangement_d2_score = float(self.V1p4Rearrangement_d2_score)

        if self.V1p4Rearrangement_d2_identity is not None and not isinstance(self.V1p4Rearrangement_d2_identity, float):
            self.V1p4Rearrangement_d2_identity = float(self.V1p4Rearrangement_d2_identity)

        if self.V1p4Rearrangement_d2_support is not None and not isinstance(self.V1p4Rearrangement_d2_support, float):
            self.V1p4Rearrangement_d2_support = float(self.V1p4Rearrangement_d2_support)

        if self.V1p4Rearrangement_d2_cigar is not None and not isinstance(self.V1p4Rearrangement_d2_cigar, str):
            self.V1p4Rearrangement_d2_cigar = str(self.V1p4Rearrangement_d2_cigar)

        if self.V1p4Rearrangement_j_score is not None and not isinstance(self.V1p4Rearrangement_j_score, float):
            self.V1p4Rearrangement_j_score = float(self.V1p4Rearrangement_j_score)

        if self.V1p4Rearrangement_j_identity is not None and not isinstance(self.V1p4Rearrangement_j_identity, float):
            self.V1p4Rearrangement_j_identity = float(self.V1p4Rearrangement_j_identity)

        if self.V1p4Rearrangement_j_support is not None and not isinstance(self.V1p4Rearrangement_j_support, float):
            self.V1p4Rearrangement_j_support = float(self.V1p4Rearrangement_j_support)

        if self.V1p4Rearrangement_c_score is not None and not isinstance(self.V1p4Rearrangement_c_score, float):
            self.V1p4Rearrangement_c_score = float(self.V1p4Rearrangement_c_score)

        if self.V1p4Rearrangement_c_identity is not None and not isinstance(self.V1p4Rearrangement_c_identity, float):
            self.V1p4Rearrangement_c_identity = float(self.V1p4Rearrangement_c_identity)

        if self.V1p4Rearrangement_c_support is not None and not isinstance(self.V1p4Rearrangement_c_support, float):
            self.V1p4Rearrangement_c_support = float(self.V1p4Rearrangement_c_support)

        if self.V1p4Rearrangement_c_cigar is not None and not isinstance(self.V1p4Rearrangement_c_cigar, str):
            self.V1p4Rearrangement_c_cigar = str(self.V1p4Rearrangement_c_cigar)

        if self.V1p4Rearrangement_v_sequence_start is not None and not isinstance(self.V1p4Rearrangement_v_sequence_start, int):
            self.V1p4Rearrangement_v_sequence_start = int(self.V1p4Rearrangement_v_sequence_start)

        if self.V1p4Rearrangement_v_sequence_end is not None and not isinstance(self.V1p4Rearrangement_v_sequence_end, int):
            self.V1p4Rearrangement_v_sequence_end = int(self.V1p4Rearrangement_v_sequence_end)

        if self.V1p4Rearrangement_v_germline_start is not None and not isinstance(self.V1p4Rearrangement_v_germline_start, int):
            self.V1p4Rearrangement_v_germline_start = int(self.V1p4Rearrangement_v_germline_start)

        if self.V1p4Rearrangement_v_germline_end is not None and not isinstance(self.V1p4Rearrangement_v_germline_end, int):
            self.V1p4Rearrangement_v_germline_end = int(self.V1p4Rearrangement_v_germline_end)

        if self.V1p4Rearrangement_v_alignment_start is not None and not isinstance(self.V1p4Rearrangement_v_alignment_start, int):
            self.V1p4Rearrangement_v_alignment_start = int(self.V1p4Rearrangement_v_alignment_start)

        if self.V1p4Rearrangement_v_alignment_end is not None and not isinstance(self.V1p4Rearrangement_v_alignment_end, int):
            self.V1p4Rearrangement_v_alignment_end = int(self.V1p4Rearrangement_v_alignment_end)

        if self.V1p4Rearrangement_d_sequence_start is not None and not isinstance(self.V1p4Rearrangement_d_sequence_start, int):
            self.V1p4Rearrangement_d_sequence_start = int(self.V1p4Rearrangement_d_sequence_start)

        if self.V1p4Rearrangement_d_sequence_end is not None and not isinstance(self.V1p4Rearrangement_d_sequence_end, int):
            self.V1p4Rearrangement_d_sequence_end = int(self.V1p4Rearrangement_d_sequence_end)

        if self.V1p4Rearrangement_d_germline_start is not None and not isinstance(self.V1p4Rearrangement_d_germline_start, int):
            self.V1p4Rearrangement_d_germline_start = int(self.V1p4Rearrangement_d_germline_start)

        if self.V1p4Rearrangement_d_germline_end is not None and not isinstance(self.V1p4Rearrangement_d_germline_end, int):
            self.V1p4Rearrangement_d_germline_end = int(self.V1p4Rearrangement_d_germline_end)

        if self.V1p4Rearrangement_d_alignment_start is not None and not isinstance(self.V1p4Rearrangement_d_alignment_start, int):
            self.V1p4Rearrangement_d_alignment_start = int(self.V1p4Rearrangement_d_alignment_start)

        if self.V1p4Rearrangement_d_alignment_end is not None and not isinstance(self.V1p4Rearrangement_d_alignment_end, int):
            self.V1p4Rearrangement_d_alignment_end = int(self.V1p4Rearrangement_d_alignment_end)

        if self.V1p4Rearrangement_d2_sequence_start is not None and not isinstance(self.V1p4Rearrangement_d2_sequence_start, int):
            self.V1p4Rearrangement_d2_sequence_start = int(self.V1p4Rearrangement_d2_sequence_start)

        if self.V1p4Rearrangement_d2_sequence_end is not None and not isinstance(self.V1p4Rearrangement_d2_sequence_end, int):
            self.V1p4Rearrangement_d2_sequence_end = int(self.V1p4Rearrangement_d2_sequence_end)

        if self.V1p4Rearrangement_d2_germline_start is not None and not isinstance(self.V1p4Rearrangement_d2_germline_start, int):
            self.V1p4Rearrangement_d2_germline_start = int(self.V1p4Rearrangement_d2_germline_start)

        if self.V1p4Rearrangement_d2_germline_end is not None and not isinstance(self.V1p4Rearrangement_d2_germline_end, int):
            self.V1p4Rearrangement_d2_germline_end = int(self.V1p4Rearrangement_d2_germline_end)

        if self.V1p4Rearrangement_d2_alignment_start is not None and not isinstance(self.V1p4Rearrangement_d2_alignment_start, int):
            self.V1p4Rearrangement_d2_alignment_start = int(self.V1p4Rearrangement_d2_alignment_start)

        if self.V1p4Rearrangement_d2_alignment_end is not None and not isinstance(self.V1p4Rearrangement_d2_alignment_end, int):
            self.V1p4Rearrangement_d2_alignment_end = int(self.V1p4Rearrangement_d2_alignment_end)

        if self.V1p4Rearrangement_j_sequence_start is not None and not isinstance(self.V1p4Rearrangement_j_sequence_start, int):
            self.V1p4Rearrangement_j_sequence_start = int(self.V1p4Rearrangement_j_sequence_start)

        if self.V1p4Rearrangement_j_sequence_end is not None and not isinstance(self.V1p4Rearrangement_j_sequence_end, int):
            self.V1p4Rearrangement_j_sequence_end = int(self.V1p4Rearrangement_j_sequence_end)

        if self.V1p4Rearrangement_j_germline_start is not None and not isinstance(self.V1p4Rearrangement_j_germline_start, int):
            self.V1p4Rearrangement_j_germline_start = int(self.V1p4Rearrangement_j_germline_start)

        if self.V1p4Rearrangement_j_germline_end is not None and not isinstance(self.V1p4Rearrangement_j_germline_end, int):
            self.V1p4Rearrangement_j_germline_end = int(self.V1p4Rearrangement_j_germline_end)

        if self.V1p4Rearrangement_j_alignment_start is not None and not isinstance(self.V1p4Rearrangement_j_alignment_start, int):
            self.V1p4Rearrangement_j_alignment_start = int(self.V1p4Rearrangement_j_alignment_start)

        if self.V1p4Rearrangement_j_alignment_end is not None and not isinstance(self.V1p4Rearrangement_j_alignment_end, int):
            self.V1p4Rearrangement_j_alignment_end = int(self.V1p4Rearrangement_j_alignment_end)

        if self.V1p4Rearrangement_c_sequence_start is not None and not isinstance(self.V1p4Rearrangement_c_sequence_start, int):
            self.V1p4Rearrangement_c_sequence_start = int(self.V1p4Rearrangement_c_sequence_start)

        if self.V1p4Rearrangement_c_sequence_end is not None and not isinstance(self.V1p4Rearrangement_c_sequence_end, int):
            self.V1p4Rearrangement_c_sequence_end = int(self.V1p4Rearrangement_c_sequence_end)

        if self.V1p4Rearrangement_c_germline_start is not None and not isinstance(self.V1p4Rearrangement_c_germline_start, int):
            self.V1p4Rearrangement_c_germline_start = int(self.V1p4Rearrangement_c_germline_start)

        if self.V1p4Rearrangement_c_germline_end is not None and not isinstance(self.V1p4Rearrangement_c_germline_end, int):
            self.V1p4Rearrangement_c_germline_end = int(self.V1p4Rearrangement_c_germline_end)

        if self.V1p4Rearrangement_c_alignment_start is not None and not isinstance(self.V1p4Rearrangement_c_alignment_start, int):
            self.V1p4Rearrangement_c_alignment_start = int(self.V1p4Rearrangement_c_alignment_start)

        if self.V1p4Rearrangement_c_alignment_end is not None and not isinstance(self.V1p4Rearrangement_c_alignment_end, int):
            self.V1p4Rearrangement_c_alignment_end = int(self.V1p4Rearrangement_c_alignment_end)

        if self.V1p4Rearrangement_cdr1_start is not None and not isinstance(self.V1p4Rearrangement_cdr1_start, int):
            self.V1p4Rearrangement_cdr1_start = int(self.V1p4Rearrangement_cdr1_start)

        if self.V1p4Rearrangement_cdr1_end is not None and not isinstance(self.V1p4Rearrangement_cdr1_end, int):
            self.V1p4Rearrangement_cdr1_end = int(self.V1p4Rearrangement_cdr1_end)

        if self.V1p4Rearrangement_cdr2_start is not None and not isinstance(self.V1p4Rearrangement_cdr2_start, int):
            self.V1p4Rearrangement_cdr2_start = int(self.V1p4Rearrangement_cdr2_start)

        if self.V1p4Rearrangement_cdr2_end is not None and not isinstance(self.V1p4Rearrangement_cdr2_end, int):
            self.V1p4Rearrangement_cdr2_end = int(self.V1p4Rearrangement_cdr2_end)

        if self.V1p4Rearrangement_cdr3_start is not None and not isinstance(self.V1p4Rearrangement_cdr3_start, int):
            self.V1p4Rearrangement_cdr3_start = int(self.V1p4Rearrangement_cdr3_start)

        if self.V1p4Rearrangement_cdr3_end is not None and not isinstance(self.V1p4Rearrangement_cdr3_end, int):
            self.V1p4Rearrangement_cdr3_end = int(self.V1p4Rearrangement_cdr3_end)

        if self.V1p4Rearrangement_fwr1_start is not None and not isinstance(self.V1p4Rearrangement_fwr1_start, int):
            self.V1p4Rearrangement_fwr1_start = int(self.V1p4Rearrangement_fwr1_start)

        if self.V1p4Rearrangement_fwr1_end is not None and not isinstance(self.V1p4Rearrangement_fwr1_end, int):
            self.V1p4Rearrangement_fwr1_end = int(self.V1p4Rearrangement_fwr1_end)

        if self.V1p4Rearrangement_fwr2_start is not None and not isinstance(self.V1p4Rearrangement_fwr2_start, int):
            self.V1p4Rearrangement_fwr2_start = int(self.V1p4Rearrangement_fwr2_start)

        if self.V1p4Rearrangement_fwr2_end is not None and not isinstance(self.V1p4Rearrangement_fwr2_end, int):
            self.V1p4Rearrangement_fwr2_end = int(self.V1p4Rearrangement_fwr2_end)

        if self.V1p4Rearrangement_fwr3_start is not None and not isinstance(self.V1p4Rearrangement_fwr3_start, int):
            self.V1p4Rearrangement_fwr3_start = int(self.V1p4Rearrangement_fwr3_start)

        if self.V1p4Rearrangement_fwr3_end is not None and not isinstance(self.V1p4Rearrangement_fwr3_end, int):
            self.V1p4Rearrangement_fwr3_end = int(self.V1p4Rearrangement_fwr3_end)

        if self.V1p4Rearrangement_fwr4_start is not None and not isinstance(self.V1p4Rearrangement_fwr4_start, int):
            self.V1p4Rearrangement_fwr4_start = int(self.V1p4Rearrangement_fwr4_start)

        if self.V1p4Rearrangement_fwr4_end is not None and not isinstance(self.V1p4Rearrangement_fwr4_end, int):
            self.V1p4Rearrangement_fwr4_end = int(self.V1p4Rearrangement_fwr4_end)

        if self.V1p4Rearrangement_v_sequence_alignment is not None and not isinstance(self.V1p4Rearrangement_v_sequence_alignment, str):
            self.V1p4Rearrangement_v_sequence_alignment = str(self.V1p4Rearrangement_v_sequence_alignment)

        if self.V1p4Rearrangement_v_sequence_alignment_aa is not None and not isinstance(self.V1p4Rearrangement_v_sequence_alignment_aa, str):
            self.V1p4Rearrangement_v_sequence_alignment_aa = str(self.V1p4Rearrangement_v_sequence_alignment_aa)

        if self.V1p4Rearrangement_d_sequence_alignment is not None and not isinstance(self.V1p4Rearrangement_d_sequence_alignment, str):
            self.V1p4Rearrangement_d_sequence_alignment = str(self.V1p4Rearrangement_d_sequence_alignment)

        if self.V1p4Rearrangement_d_sequence_alignment_aa is not None and not isinstance(self.V1p4Rearrangement_d_sequence_alignment_aa, str):
            self.V1p4Rearrangement_d_sequence_alignment_aa = str(self.V1p4Rearrangement_d_sequence_alignment_aa)

        if self.V1p4Rearrangement_d2_sequence_alignment is not None and not isinstance(self.V1p4Rearrangement_d2_sequence_alignment, str):
            self.V1p4Rearrangement_d2_sequence_alignment = str(self.V1p4Rearrangement_d2_sequence_alignment)

        if self.V1p4Rearrangement_d2_sequence_alignment_aa is not None and not isinstance(self.V1p4Rearrangement_d2_sequence_alignment_aa, str):
            self.V1p4Rearrangement_d2_sequence_alignment_aa = str(self.V1p4Rearrangement_d2_sequence_alignment_aa)

        if self.V1p4Rearrangement_j_sequence_alignment is not None and not isinstance(self.V1p4Rearrangement_j_sequence_alignment, str):
            self.V1p4Rearrangement_j_sequence_alignment = str(self.V1p4Rearrangement_j_sequence_alignment)

        if self.V1p4Rearrangement_j_sequence_alignment_aa is not None and not isinstance(self.V1p4Rearrangement_j_sequence_alignment_aa, str):
            self.V1p4Rearrangement_j_sequence_alignment_aa = str(self.V1p4Rearrangement_j_sequence_alignment_aa)

        if self.V1p4Rearrangement_c_sequence_alignment is not None and not isinstance(self.V1p4Rearrangement_c_sequence_alignment, str):
            self.V1p4Rearrangement_c_sequence_alignment = str(self.V1p4Rearrangement_c_sequence_alignment)

        if self.V1p4Rearrangement_c_sequence_alignment_aa is not None and not isinstance(self.V1p4Rearrangement_c_sequence_alignment_aa, str):
            self.V1p4Rearrangement_c_sequence_alignment_aa = str(self.V1p4Rearrangement_c_sequence_alignment_aa)

        if self.V1p4Rearrangement_v_germline_alignment is not None and not isinstance(self.V1p4Rearrangement_v_germline_alignment, str):
            self.V1p4Rearrangement_v_germline_alignment = str(self.V1p4Rearrangement_v_germline_alignment)

        if self.V1p4Rearrangement_v_germline_alignment_aa is not None and not isinstance(self.V1p4Rearrangement_v_germline_alignment_aa, str):
            self.V1p4Rearrangement_v_germline_alignment_aa = str(self.V1p4Rearrangement_v_germline_alignment_aa)

        if self.V1p4Rearrangement_d_germline_alignment is not None and not isinstance(self.V1p4Rearrangement_d_germline_alignment, str):
            self.V1p4Rearrangement_d_germline_alignment = str(self.V1p4Rearrangement_d_germline_alignment)

        if self.V1p4Rearrangement_d_germline_alignment_aa is not None and not isinstance(self.V1p4Rearrangement_d_germline_alignment_aa, str):
            self.V1p4Rearrangement_d_germline_alignment_aa = str(self.V1p4Rearrangement_d_germline_alignment_aa)

        if self.V1p4Rearrangement_d2_germline_alignment is not None and not isinstance(self.V1p4Rearrangement_d2_germline_alignment, str):
            self.V1p4Rearrangement_d2_germline_alignment = str(self.V1p4Rearrangement_d2_germline_alignment)

        if self.V1p4Rearrangement_d2_germline_alignment_aa is not None and not isinstance(self.V1p4Rearrangement_d2_germline_alignment_aa, str):
            self.V1p4Rearrangement_d2_germline_alignment_aa = str(self.V1p4Rearrangement_d2_germline_alignment_aa)

        if self.V1p4Rearrangement_j_germline_alignment is not None and not isinstance(self.V1p4Rearrangement_j_germline_alignment, str):
            self.V1p4Rearrangement_j_germline_alignment = str(self.V1p4Rearrangement_j_germline_alignment)

        if self.V1p4Rearrangement_j_germline_alignment_aa is not None and not isinstance(self.V1p4Rearrangement_j_germline_alignment_aa, str):
            self.V1p4Rearrangement_j_germline_alignment_aa = str(self.V1p4Rearrangement_j_germline_alignment_aa)

        if self.V1p4Rearrangement_c_germline_alignment is not None and not isinstance(self.V1p4Rearrangement_c_germline_alignment, str):
            self.V1p4Rearrangement_c_germline_alignment = str(self.V1p4Rearrangement_c_germline_alignment)

        if self.V1p4Rearrangement_c_germline_alignment_aa is not None and not isinstance(self.V1p4Rearrangement_c_germline_alignment_aa, str):
            self.V1p4Rearrangement_c_germline_alignment_aa = str(self.V1p4Rearrangement_c_germline_alignment_aa)

        if self.V1p4Rearrangement_junction_length is not None and not isinstance(self.V1p4Rearrangement_junction_length, int):
            self.V1p4Rearrangement_junction_length = int(self.V1p4Rearrangement_junction_length)

        if self.V1p4Rearrangement_junction_aa_length is not None and not isinstance(self.V1p4Rearrangement_junction_aa_length, int):
            self.V1p4Rearrangement_junction_aa_length = int(self.V1p4Rearrangement_junction_aa_length)

        if self.V1p4Rearrangement_np1_length is not None and not isinstance(self.V1p4Rearrangement_np1_length, int):
            self.V1p4Rearrangement_np1_length = int(self.V1p4Rearrangement_np1_length)

        if self.V1p4Rearrangement_np2_length is not None and not isinstance(self.V1p4Rearrangement_np2_length, int):
            self.V1p4Rearrangement_np2_length = int(self.V1p4Rearrangement_np2_length)

        if self.V1p4Rearrangement_np3_length is not None and not isinstance(self.V1p4Rearrangement_np3_length, int):
            self.V1p4Rearrangement_np3_length = int(self.V1p4Rearrangement_np3_length)

        if self.V1p4Rearrangement_n1_length is not None and not isinstance(self.V1p4Rearrangement_n1_length, int):
            self.V1p4Rearrangement_n1_length = int(self.V1p4Rearrangement_n1_length)

        if self.V1p4Rearrangement_n2_length is not None and not isinstance(self.V1p4Rearrangement_n2_length, int):
            self.V1p4Rearrangement_n2_length = int(self.V1p4Rearrangement_n2_length)

        if self.V1p4Rearrangement_n3_length is not None and not isinstance(self.V1p4Rearrangement_n3_length, int):
            self.V1p4Rearrangement_n3_length = int(self.V1p4Rearrangement_n3_length)

        if self.V1p4Rearrangement_p3v_length is not None and not isinstance(self.V1p4Rearrangement_p3v_length, int):
            self.V1p4Rearrangement_p3v_length = int(self.V1p4Rearrangement_p3v_length)

        if self.V1p4Rearrangement_p5d_length is not None and not isinstance(self.V1p4Rearrangement_p5d_length, int):
            self.V1p4Rearrangement_p5d_length = int(self.V1p4Rearrangement_p5d_length)

        if self.V1p4Rearrangement_p3d_length is not None and not isinstance(self.V1p4Rearrangement_p3d_length, int):
            self.V1p4Rearrangement_p3d_length = int(self.V1p4Rearrangement_p3d_length)

        if self.V1p4Rearrangement_p5d2_length is not None and not isinstance(self.V1p4Rearrangement_p5d2_length, int):
            self.V1p4Rearrangement_p5d2_length = int(self.V1p4Rearrangement_p5d2_length)

        if self.V1p4Rearrangement_p3d2_length is not None and not isinstance(self.V1p4Rearrangement_p3d2_length, int):
            self.V1p4Rearrangement_p3d2_length = int(self.V1p4Rearrangement_p3d2_length)

        if self.V1p4Rearrangement_p5j_length is not None and not isinstance(self.V1p4Rearrangement_p5j_length, int):
            self.V1p4Rearrangement_p5j_length = int(self.V1p4Rearrangement_p5j_length)

        if self.V1p4Rearrangement_v_frameshift is not None and not isinstance(self.V1p4Rearrangement_v_frameshift, Bool):
            self.V1p4Rearrangement_v_frameshift = Bool(self.V1p4Rearrangement_v_frameshift)

        if self.V1p4Rearrangement_j_frameshift is not None and not isinstance(self.V1p4Rearrangement_j_frameshift, Bool):
            self.V1p4Rearrangement_j_frameshift = Bool(self.V1p4Rearrangement_j_frameshift)

        if self.V1p4Rearrangement_d_frame is not None and not isinstance(self.V1p4Rearrangement_d_frame, int):
            self.V1p4Rearrangement_d_frame = int(self.V1p4Rearrangement_d_frame)

        if self.V1p4Rearrangement_d2_frame is not None and not isinstance(self.V1p4Rearrangement_d2_frame, int):
            self.V1p4Rearrangement_d2_frame = int(self.V1p4Rearrangement_d2_frame)

        if self.V1p4Rearrangement_consensus_count is not None and not isinstance(self.V1p4Rearrangement_consensus_count, int):
            self.V1p4Rearrangement_consensus_count = int(self.V1p4Rearrangement_consensus_count)

        if self.V1p4Rearrangement_duplicate_count is not None and not isinstance(self.V1p4Rearrangement_duplicate_count, int):
            self.V1p4Rearrangement_duplicate_count = int(self.V1p4Rearrangement_duplicate_count)

        if self.V1p4Rearrangement_umi_count is not None and not isinstance(self.V1p4Rearrangement_umi_count, int):
            self.V1p4Rearrangement_umi_count = int(self.V1p4Rearrangement_umi_count)

        if self.V1p4Rearrangement_cell_id is not None and not isinstance(self.V1p4Rearrangement_cell_id, str):
            self.V1p4Rearrangement_cell_id = str(self.V1p4Rearrangement_cell_id)

        if self.V1p4Rearrangement_clone_id is not None and not isinstance(self.V1p4Rearrangement_clone_id, str):
            self.V1p4Rearrangement_clone_id = str(self.V1p4Rearrangement_clone_id)

        if self.V1p4Rearrangement_reactivity_id is not None and not isinstance(self.V1p4Rearrangement_reactivity_id, str):
            self.V1p4Rearrangement_reactivity_id = str(self.V1p4Rearrangement_reactivity_id)

        if self.V1p4Rearrangement_reactivity_ref is not None and not isinstance(self.V1p4Rearrangement_reactivity_ref, str):
            self.V1p4Rearrangement_reactivity_ref = str(self.V1p4Rearrangement_reactivity_ref)

        if self.V1p4Rearrangement_repertoire_id is not None and not isinstance(self.V1p4Rearrangement_repertoire_id, str):
            self.V1p4Rearrangement_repertoire_id = str(self.V1p4Rearrangement_repertoire_id)

        if self.V1p4Rearrangement_sample_processing_id is not None and not isinstance(self.V1p4Rearrangement_sample_processing_id, str):
            self.V1p4Rearrangement_sample_processing_id = str(self.V1p4Rearrangement_sample_processing_id)

        if self.V1p4Rearrangement_data_processing_id is not None and not isinstance(self.V1p4Rearrangement_data_processing_id, str):
            self.V1p4Rearrangement_data_processing_id = str(self.V1p4Rearrangement_data_processing_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Clone(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Clone"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Clone"
    class_name: ClassVar[str] = "V1p4Clone"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Clone

    V1p4Clone_clone_id: str = None
    V1p4Clone_germline_alignment: str = None
    V1p4Clone_repertoire_id: Optional[str] = None
    V1p4Clone_data_processing_id: Optional[str] = None
    V1p4Clone_sequences: Optional[Union[str, List[str]]] = empty_list()
    V1p4Clone_v_call: Optional[str] = None
    V1p4Clone_d_call: Optional[str] = None
    V1p4Clone_j_call: Optional[str] = None
    V1p4Clone_junction: Optional[str] = None
    V1p4Clone_junction_aa: Optional[str] = None
    V1p4Clone_junction_length: Optional[int] = None
    V1p4Clone_junction_aa_length: Optional[int] = None
    V1p4Clone_germline_alignment_aa: Optional[str] = None
    V1p4Clone_v_alignment_start: Optional[int] = None
    V1p4Clone_v_alignment_end: Optional[int] = None
    V1p4Clone_d_alignment_start: Optional[int] = None
    V1p4Clone_d_alignment_end: Optional[int] = None
    V1p4Clone_j_alignment_start: Optional[int] = None
    V1p4Clone_j_alignment_end: Optional[int] = None
    V1p4Clone_junction_start: Optional[int] = None
    V1p4Clone_junction_end: Optional[int] = None
    V1p4Clone_umi_count: Optional[int] = None
    V1p4Clone_clone_count: Optional[int] = None
    V1p4Clone_seed_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4Clone_clone_id):
            self.MissingRequiredField("V1p4Clone_clone_id")
        if not isinstance(self.V1p4Clone_clone_id, str):
            self.V1p4Clone_clone_id = str(self.V1p4Clone_clone_id)

        if self._is_empty(self.V1p4Clone_germline_alignment):
            self.MissingRequiredField("V1p4Clone_germline_alignment")
        if not isinstance(self.V1p4Clone_germline_alignment, str):
            self.V1p4Clone_germline_alignment = str(self.V1p4Clone_germline_alignment)

        if self.V1p4Clone_repertoire_id is not None and not isinstance(self.V1p4Clone_repertoire_id, str):
            self.V1p4Clone_repertoire_id = str(self.V1p4Clone_repertoire_id)

        if self.V1p4Clone_data_processing_id is not None and not isinstance(self.V1p4Clone_data_processing_id, str):
            self.V1p4Clone_data_processing_id = str(self.V1p4Clone_data_processing_id)

        if not isinstance(self.V1p4Clone_sequences, list):
            self.V1p4Clone_sequences = [self.V1p4Clone_sequences] if self.V1p4Clone_sequences is not None else []
        self.V1p4Clone_sequences = [v if isinstance(v, str) else str(v) for v in self.V1p4Clone_sequences]

        if self.V1p4Clone_v_call is not None and not isinstance(self.V1p4Clone_v_call, str):
            self.V1p4Clone_v_call = str(self.V1p4Clone_v_call)

        if self.V1p4Clone_d_call is not None and not isinstance(self.V1p4Clone_d_call, str):
            self.V1p4Clone_d_call = str(self.V1p4Clone_d_call)

        if self.V1p4Clone_j_call is not None and not isinstance(self.V1p4Clone_j_call, str):
            self.V1p4Clone_j_call = str(self.V1p4Clone_j_call)

        if self.V1p4Clone_junction is not None and not isinstance(self.V1p4Clone_junction, str):
            self.V1p4Clone_junction = str(self.V1p4Clone_junction)

        if self.V1p4Clone_junction_aa is not None and not isinstance(self.V1p4Clone_junction_aa, str):
            self.V1p4Clone_junction_aa = str(self.V1p4Clone_junction_aa)

        if self.V1p4Clone_junction_length is not None and not isinstance(self.V1p4Clone_junction_length, int):
            self.V1p4Clone_junction_length = int(self.V1p4Clone_junction_length)

        if self.V1p4Clone_junction_aa_length is not None and not isinstance(self.V1p4Clone_junction_aa_length, int):
            self.V1p4Clone_junction_aa_length = int(self.V1p4Clone_junction_aa_length)

        if self.V1p4Clone_germline_alignment_aa is not None and not isinstance(self.V1p4Clone_germline_alignment_aa, str):
            self.V1p4Clone_germline_alignment_aa = str(self.V1p4Clone_germline_alignment_aa)

        if self.V1p4Clone_v_alignment_start is not None and not isinstance(self.V1p4Clone_v_alignment_start, int):
            self.V1p4Clone_v_alignment_start = int(self.V1p4Clone_v_alignment_start)

        if self.V1p4Clone_v_alignment_end is not None and not isinstance(self.V1p4Clone_v_alignment_end, int):
            self.V1p4Clone_v_alignment_end = int(self.V1p4Clone_v_alignment_end)

        if self.V1p4Clone_d_alignment_start is not None and not isinstance(self.V1p4Clone_d_alignment_start, int):
            self.V1p4Clone_d_alignment_start = int(self.V1p4Clone_d_alignment_start)

        if self.V1p4Clone_d_alignment_end is not None and not isinstance(self.V1p4Clone_d_alignment_end, int):
            self.V1p4Clone_d_alignment_end = int(self.V1p4Clone_d_alignment_end)

        if self.V1p4Clone_j_alignment_start is not None and not isinstance(self.V1p4Clone_j_alignment_start, int):
            self.V1p4Clone_j_alignment_start = int(self.V1p4Clone_j_alignment_start)

        if self.V1p4Clone_j_alignment_end is not None and not isinstance(self.V1p4Clone_j_alignment_end, int):
            self.V1p4Clone_j_alignment_end = int(self.V1p4Clone_j_alignment_end)

        if self.V1p4Clone_junction_start is not None and not isinstance(self.V1p4Clone_junction_start, int):
            self.V1p4Clone_junction_start = int(self.V1p4Clone_junction_start)

        if self.V1p4Clone_junction_end is not None and not isinstance(self.V1p4Clone_junction_end, int):
            self.V1p4Clone_junction_end = int(self.V1p4Clone_junction_end)

        if self.V1p4Clone_umi_count is not None and not isinstance(self.V1p4Clone_umi_count, int):
            self.V1p4Clone_umi_count = int(self.V1p4Clone_umi_count)

        if self.V1p4Clone_clone_count is not None and not isinstance(self.V1p4Clone_clone_count, int):
            self.V1p4Clone_clone_count = int(self.V1p4Clone_clone_count)

        if self.V1p4Clone_seed_id is not None and not isinstance(self.V1p4Clone_seed_id, str):
            self.V1p4Clone_seed_id = str(self.V1p4Clone_seed_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Tree(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Tree"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Tree"
    class_name: ClassVar[str] = "V1p4Tree"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Tree

    V1p4Tree_tree_id: str = None
    V1p4Tree_clone_id: str = None
    V1p4Tree_newick: str = None
    V1p4Tree_nodes: Optional[Union[Union[dict, "V1p4Node"], List[Union[dict, "V1p4Node"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4Tree_tree_id):
            self.MissingRequiredField("V1p4Tree_tree_id")
        if not isinstance(self.V1p4Tree_tree_id, str):
            self.V1p4Tree_tree_id = str(self.V1p4Tree_tree_id)

        if self._is_empty(self.V1p4Tree_clone_id):
            self.MissingRequiredField("V1p4Tree_clone_id")
        if not isinstance(self.V1p4Tree_clone_id, str):
            self.V1p4Tree_clone_id = str(self.V1p4Tree_clone_id)

        if self._is_empty(self.V1p4Tree_newick):
            self.MissingRequiredField("V1p4Tree_newick")
        if not isinstance(self.V1p4Tree_newick, str):
            self.V1p4Tree_newick = str(self.V1p4Tree_newick)

        self._normalize_inlined_as_dict(slot_name="V1p4Tree_nodes", slot_type=V1p4Node, key_name="V1p4Node_sequence_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Node(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Node"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Node"
    class_name: ClassVar[str] = "V1p4Node"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Node

    V1p4Node_sequence_id: str = None
    V1p4Node_sequence_alignment: Optional[str] = None
    V1p4Node_junction: Optional[str] = None
    V1p4Node_junction_aa: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4Node_sequence_id):
            self.MissingRequiredField("V1p4Node_sequence_id")
        if not isinstance(self.V1p4Node_sequence_id, str):
            self.V1p4Node_sequence_id = str(self.V1p4Node_sequence_id)

        if self.V1p4Node_sequence_alignment is not None and not isinstance(self.V1p4Node_sequence_alignment, str):
            self.V1p4Node_sequence_alignment = str(self.V1p4Node_sequence_alignment)

        if self.V1p4Node_junction is not None and not isinstance(self.V1p4Node_junction, str):
            self.V1p4Node_junction = str(self.V1p4Node_junction)

        if self.V1p4Node_junction_aa is not None and not isinstance(self.V1p4Node_junction_aa, str):
            self.V1p4Node_junction_aa = str(self.V1p4Node_junction_aa)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Cell(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Cell"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Cell"
    class_name: ClassVar[str] = "V1p4Cell"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Cell

    V1p4Cell_cell_id: str = None
    V1p4Cell_repertoire_id: str = None
    V1p4Cell_virtual_pairing: Union[bool, Bool] = None
    V1p4Cell_data_processing_id: Optional[str] = None
    V1p4Cell_receptors: Optional[Union[str, List[str]]] = empty_list()
    V1p4Cell_cell_subset: Optional[Union[str, "V1p4CellSubset"]] = None
    V1p4Cell_cell_phenotype: Optional[str] = None
    V1p4Cell_cell_label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4Cell_cell_id):
            self.MissingRequiredField("V1p4Cell_cell_id")
        if not isinstance(self.V1p4Cell_cell_id, str):
            self.V1p4Cell_cell_id = str(self.V1p4Cell_cell_id)

        if self._is_empty(self.V1p4Cell_repertoire_id):
            self.MissingRequiredField("V1p4Cell_repertoire_id")
        if not isinstance(self.V1p4Cell_repertoire_id, str):
            self.V1p4Cell_repertoire_id = str(self.V1p4Cell_repertoire_id)

        if self._is_empty(self.V1p4Cell_virtual_pairing):
            self.MissingRequiredField("V1p4Cell_virtual_pairing")
        if not isinstance(self.V1p4Cell_virtual_pairing, Bool):
            self.V1p4Cell_virtual_pairing = Bool(self.V1p4Cell_virtual_pairing)

        if self.V1p4Cell_data_processing_id is not None and not isinstance(self.V1p4Cell_data_processing_id, str):
            self.V1p4Cell_data_processing_id = str(self.V1p4Cell_data_processing_id)

        if not isinstance(self.V1p4Cell_receptors, list):
            self.V1p4Cell_receptors = [self.V1p4Cell_receptors] if self.V1p4Cell_receptors is not None else []
        self.V1p4Cell_receptors = [v if isinstance(v, str) else str(v) for v in self.V1p4Cell_receptors]

        if self.V1p4Cell_cell_phenotype is not None and not isinstance(self.V1p4Cell_cell_phenotype, str):
            self.V1p4Cell_cell_phenotype = str(self.V1p4Cell_cell_phenotype)

        if self.V1p4Cell_cell_label is not None and not isinstance(self.V1p4Cell_cell_label, str):
            self.V1p4Cell_cell_label = str(self.V1p4Cell_cell_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Expression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Expression"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Expression"
    class_name: ClassVar[str] = "V1p4Expression"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Expression

    V1p4Expression_expression_id: str = None
    V1p4Expression_cell_id: str = None
    V1p4Expression_repertoire_id: str = None
    V1p4Expression_data_processing_id: str = None
    V1p4Expression_property_type: str = None
    V1p4Expression_property: Union[str, "V1p4Property"] = None
    V1p4Expression_value: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4Expression_expression_id):
            self.MissingRequiredField("V1p4Expression_expression_id")
        if not isinstance(self.V1p4Expression_expression_id, str):
            self.V1p4Expression_expression_id = str(self.V1p4Expression_expression_id)

        if self._is_empty(self.V1p4Expression_cell_id):
            self.MissingRequiredField("V1p4Expression_cell_id")
        if not isinstance(self.V1p4Expression_cell_id, str):
            self.V1p4Expression_cell_id = str(self.V1p4Expression_cell_id)

        if self._is_empty(self.V1p4Expression_repertoire_id):
            self.MissingRequiredField("V1p4Expression_repertoire_id")
        if not isinstance(self.V1p4Expression_repertoire_id, str):
            self.V1p4Expression_repertoire_id = str(self.V1p4Expression_repertoire_id)

        if self._is_empty(self.V1p4Expression_data_processing_id):
            self.MissingRequiredField("V1p4Expression_data_processing_id")
        if not isinstance(self.V1p4Expression_data_processing_id, str):
            self.V1p4Expression_data_processing_id = str(self.V1p4Expression_data_processing_id)

        if self._is_empty(self.V1p4Expression_property_type):
            self.MissingRequiredField("V1p4Expression_property_type")
        if not isinstance(self.V1p4Expression_property_type, str):
            self.V1p4Expression_property_type = str(self.V1p4Expression_property_type)

        if self._is_empty(self.V1p4Expression_value):
            self.MissingRequiredField("V1p4Expression_value")
        if not isinstance(self.V1p4Expression_value, float):
            self.V1p4Expression_value = float(self.V1p4Expression_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Receptor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Receptor"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Receptor"
    class_name: ClassVar[str] = "V1p4Receptor"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Receptor

    V1p4Receptor_receptor_id: str = None
    V1p4Receptor_receptor_hash: str = None
    V1p4Receptor_receptor_type: Union[str, "V1p4ReceptorType"] = None
    V1p4Receptor_receptor_variable_domain_1_aa: str = None
    V1p4Receptor_receptor_variable_domain_1_locus: Union[str, "V1p4ReceptorVariableDomain1Locus"] = None
    V1p4Receptor_receptor_variable_domain_2_aa: str = None
    V1p4Receptor_receptor_variable_domain_2_locus: Union[str, "V1p4ReceptorVariableDomain2Locus"] = None
    V1p4Receptor_receptor_ref: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4Receptor_receptor_id):
            self.MissingRequiredField("V1p4Receptor_receptor_id")
        if not isinstance(self.V1p4Receptor_receptor_id, str):
            self.V1p4Receptor_receptor_id = str(self.V1p4Receptor_receptor_id)

        if self._is_empty(self.V1p4Receptor_receptor_hash):
            self.MissingRequiredField("V1p4Receptor_receptor_hash")
        if not isinstance(self.V1p4Receptor_receptor_hash, str):
            self.V1p4Receptor_receptor_hash = str(self.V1p4Receptor_receptor_hash)

        if self._is_empty(self.V1p4Receptor_receptor_type):
            self.MissingRequiredField("V1p4Receptor_receptor_type")
        if not isinstance(self.V1p4Receptor_receptor_type, V1p4ReceptorType):
            self.V1p4Receptor_receptor_type = V1p4ReceptorType(self.V1p4Receptor_receptor_type)

        if self._is_empty(self.V1p4Receptor_receptor_variable_domain_1_aa):
            self.MissingRequiredField("V1p4Receptor_receptor_variable_domain_1_aa")
        if not isinstance(self.V1p4Receptor_receptor_variable_domain_1_aa, str):
            self.V1p4Receptor_receptor_variable_domain_1_aa = str(self.V1p4Receptor_receptor_variable_domain_1_aa)

        if self._is_empty(self.V1p4Receptor_receptor_variable_domain_1_locus):
            self.MissingRequiredField("V1p4Receptor_receptor_variable_domain_1_locus")
        if not isinstance(self.V1p4Receptor_receptor_variable_domain_1_locus, V1p4ReceptorVariableDomain1Locus):
            self.V1p4Receptor_receptor_variable_domain_1_locus = V1p4ReceptorVariableDomain1Locus(self.V1p4Receptor_receptor_variable_domain_1_locus)

        if self._is_empty(self.V1p4Receptor_receptor_variable_domain_2_aa):
            self.MissingRequiredField("V1p4Receptor_receptor_variable_domain_2_aa")
        if not isinstance(self.V1p4Receptor_receptor_variable_domain_2_aa, str):
            self.V1p4Receptor_receptor_variable_domain_2_aa = str(self.V1p4Receptor_receptor_variable_domain_2_aa)

        if self._is_empty(self.V1p4Receptor_receptor_variable_domain_2_locus):
            self.MissingRequiredField("V1p4Receptor_receptor_variable_domain_2_locus")
        if not isinstance(self.V1p4Receptor_receptor_variable_domain_2_locus, V1p4ReceptorVariableDomain2Locus):
            self.V1p4Receptor_receptor_variable_domain_2_locus = V1p4ReceptorVariableDomain2Locus(self.V1p4Receptor_receptor_variable_domain_2_locus)

        if not isinstance(self.V1p4Receptor_receptor_ref, list):
            self.V1p4Receptor_receptor_ref = [self.V1p4Receptor_receptor_ref] if self.V1p4Receptor_receptor_ref is not None else []
        self.V1p4Receptor_receptor_ref = [v if isinstance(v, str) else str(v) for v in self.V1p4Receptor_receptor_ref]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4Reactivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4Reactivity"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4Reactivity"
    class_name: ClassVar[str] = "V1p4Reactivity"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4Reactivity

    V1p4Reactivity_reactivity_id: str = None
    V1p4Reactivity_cell_id: str = None
    V1p4Reactivity_ligand_type: Union[str, "V1p4LigandType"] = None
    V1p4Reactivity_antigen_type: Union[str, "V1p4AntigenType"] = None
    V1p4Reactivity_antigen: Union[str, "V1p4Antigen"] = None
    V1p4Reactivity_reactivity_method: str = None
    V1p4Reactivity_reactivity_readout: str = None
    V1p4Reactivity_reactivity_value: float = None
    V1p4Reactivity_reactivity_unit: str = None
    V1p4Reactivity_repertoire_id: Optional[str] = None
    V1p4Reactivity_data_processing_id: Optional[str] = None
    V1p4Reactivity_antigen_source_species: Optional[Union[str, "V1p4AntigenSourceSpecies"]] = None
    V1p4Reactivity_peptide_start: Optional[int] = None
    V1p4Reactivity_peptide_end: Optional[int] = None
    V1p4Reactivity_peptide_sequence_aa: Optional[str] = None
    V1p4Reactivity_mhc_class: Optional[Union[str, "V1p4MhcClass"]] = None
    V1p4Reactivity_mhc_gene_1: Optional[Union[str, "V1p4MhcGene1"]] = None
    V1p4Reactivity_mhc_allele_1: Optional[str] = None
    V1p4Reactivity_mhc_gene_2: Optional[Union[str, "V1p4MhcGene2"]] = None
    V1p4Reactivity_mhc_allele_2: Optional[str] = None
    V1p4Reactivity_reactivity_ref: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4Reactivity_reactivity_id):
            self.MissingRequiredField("V1p4Reactivity_reactivity_id")
        if not isinstance(self.V1p4Reactivity_reactivity_id, str):
            self.V1p4Reactivity_reactivity_id = str(self.V1p4Reactivity_reactivity_id)

        if self._is_empty(self.V1p4Reactivity_cell_id):
            self.MissingRequiredField("V1p4Reactivity_cell_id")
        if not isinstance(self.V1p4Reactivity_cell_id, str):
            self.V1p4Reactivity_cell_id = str(self.V1p4Reactivity_cell_id)

        if self._is_empty(self.V1p4Reactivity_ligand_type):
            self.MissingRequiredField("V1p4Reactivity_ligand_type")
        if not isinstance(self.V1p4Reactivity_ligand_type, V1p4LigandType):
            self.V1p4Reactivity_ligand_type = V1p4LigandType(self.V1p4Reactivity_ligand_type)

        if self._is_empty(self.V1p4Reactivity_antigen_type):
            self.MissingRequiredField("V1p4Reactivity_antigen_type")
        if not isinstance(self.V1p4Reactivity_antigen_type, V1p4AntigenType):
            self.V1p4Reactivity_antigen_type = V1p4AntigenType(self.V1p4Reactivity_antigen_type)

        if self._is_empty(self.V1p4Reactivity_reactivity_method):
            self.MissingRequiredField("V1p4Reactivity_reactivity_method")
        if not isinstance(self.V1p4Reactivity_reactivity_method, str):
            self.V1p4Reactivity_reactivity_method = str(self.V1p4Reactivity_reactivity_method)

        if self._is_empty(self.V1p4Reactivity_reactivity_readout):
            self.MissingRequiredField("V1p4Reactivity_reactivity_readout")
        if not isinstance(self.V1p4Reactivity_reactivity_readout, str):
            self.V1p4Reactivity_reactivity_readout = str(self.V1p4Reactivity_reactivity_readout)

        if self._is_empty(self.V1p4Reactivity_reactivity_value):
            self.MissingRequiredField("V1p4Reactivity_reactivity_value")
        if not isinstance(self.V1p4Reactivity_reactivity_value, float):
            self.V1p4Reactivity_reactivity_value = float(self.V1p4Reactivity_reactivity_value)

        if self._is_empty(self.V1p4Reactivity_reactivity_unit):
            self.MissingRequiredField("V1p4Reactivity_reactivity_unit")
        if not isinstance(self.V1p4Reactivity_reactivity_unit, str):
            self.V1p4Reactivity_reactivity_unit = str(self.V1p4Reactivity_reactivity_unit)

        if self.V1p4Reactivity_repertoire_id is not None and not isinstance(self.V1p4Reactivity_repertoire_id, str):
            self.V1p4Reactivity_repertoire_id = str(self.V1p4Reactivity_repertoire_id)

        if self.V1p4Reactivity_data_processing_id is not None and not isinstance(self.V1p4Reactivity_data_processing_id, str):
            self.V1p4Reactivity_data_processing_id = str(self.V1p4Reactivity_data_processing_id)

        if self.V1p4Reactivity_peptide_start is not None and not isinstance(self.V1p4Reactivity_peptide_start, int):
            self.V1p4Reactivity_peptide_start = int(self.V1p4Reactivity_peptide_start)

        if self.V1p4Reactivity_peptide_end is not None and not isinstance(self.V1p4Reactivity_peptide_end, int):
            self.V1p4Reactivity_peptide_end = int(self.V1p4Reactivity_peptide_end)

        if self.V1p4Reactivity_peptide_sequence_aa is not None and not isinstance(self.V1p4Reactivity_peptide_sequence_aa, str):
            self.V1p4Reactivity_peptide_sequence_aa = str(self.V1p4Reactivity_peptide_sequence_aa)

        if self.V1p4Reactivity_mhc_class is not None and not isinstance(self.V1p4Reactivity_mhc_class, V1p4MhcClass):
            self.V1p4Reactivity_mhc_class = V1p4MhcClass(self.V1p4Reactivity_mhc_class)

        if self.V1p4Reactivity_mhc_allele_1 is not None and not isinstance(self.V1p4Reactivity_mhc_allele_1, str):
            self.V1p4Reactivity_mhc_allele_1 = str(self.V1p4Reactivity_mhc_allele_1)

        if self.V1p4Reactivity_mhc_allele_2 is not None and not isinstance(self.V1p4Reactivity_mhc_allele_2, str):
            self.V1p4Reactivity_mhc_allele_2 = str(self.V1p4Reactivity_mhc_allele_2)

        if not isinstance(self.V1p4Reactivity_reactivity_ref, list):
            self.V1p4Reactivity_reactivity_ref = [self.V1p4Reactivity_reactivity_ref] if self.V1p4Reactivity_reactivity_ref is not None else []
        self.V1p4Reactivity_reactivity_ref = [v if isinstance(v, str) else str(v) for v in self.V1p4Reactivity_reactivity_ref]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class V1p4SampleProcessing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AK_SCHEMA["V1p4SampleProcessing"]
    class_class_curie: ClassVar[str] = "ak_schema:V1p4SampleProcessing"
    class_name: ClassVar[str] = "V1p4SampleProcessing"
    class_model_uri: ClassVar[URIRef] = AK_SCHEMA.V1p4SampleProcessing

    V1p4Sample_sample_id: str = None
    V1p4Sample_sample_type: str = None
    V1p4Sample_tissue: Union[str, "V1p4Tissue"] = None
    V1p4Sample_anatomic_site: str = None
    V1p4Sample_disease_state_sample: str = None
    V1p4Sample_collection_time_point_relative: Union[dict, V1p4TimePoint] = None
    V1p4Sample_biomaterial_provider: str = None
    V1p4CellProcessing_tissue_processing: str = None
    V1p4CellProcessing_cell_subset: Union[str, "V1p4CellSubset"] = None
    V1p4CellProcessing_cell_phenotype: str = None
    V1p4CellProcessing_single_cell: Union[bool, Bool] = None
    V1p4CellProcessing_cell_number: int = None
    V1p4CellProcessing_cells_per_reaction: int = None
    V1p4CellProcessing_cell_storage: Union[bool, Bool] = None
    V1p4CellProcessing_cell_quality: str = None
    V1p4CellProcessing_cell_isolation: str = None
    V1p4CellProcessing_cell_processing_protocol: str = None
    V1p4NucleicAcidProcessing_template_class: Union[str, "V1p4TemplateClass"] = None
    V1p4NucleicAcidProcessing_template_quality: str = None
    V1p4NucleicAcidProcessing_template_amount: Union[dict, V1p4PhysicalQuantity] = None
    V1p4NucleicAcidProcessing_library_generation_method: Union[str, "V1p4LibraryGenerationMethod"] = None
    V1p4NucleicAcidProcessing_library_generation_protocol: str = None
    V1p4NucleicAcidProcessing_library_generation_kit_version: str = None
    V1p4NucleicAcidProcessing_complete_sequences: Union[str, "V1p4CompleteSequences"] = None
    V1p4NucleicAcidProcessing_physical_linkage: Union[str, "V1p4PhysicalLinkage"] = None
    V1p4SequencingRun_sequencing_run_id: str = None
    V1p4SequencingRun_total_reads_passing_qc_filter: int = None
    V1p4SequencingRun_sequencing_platform: str = None
    V1p4SequencingRun_sequencing_facility: str = None
    V1p4SequencingRun_sequencing_run_date: str = None
    V1p4SequencingRun_sequencing_kit: str = None
    V1p4SampleProcessing_sample_processing_id: Optional[str] = None
    V1p4Sample_collection_location: Optional[Union[str, "V1p4CollectionLocation"]] = None
    V1p4CellProcessing_cell_label: Optional[str] = None
    V1p4CellProcessing_cell_species: Optional[Union[str, "V1p4CellSpecies"]] = None
    V1p4NucleicAcidProcessing_pcr_target: Optional[Union[Union[dict, V1p4PCRTarget], List[Union[dict, V1p4PCRTarget]]]] = empty_list()
    V1p4SequencingRun_sequencing_files: Optional[Union[dict, V1p4SequencingData]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.V1p4Sample_sample_id):
            self.MissingRequiredField("V1p4Sample_sample_id")
        if not isinstance(self.V1p4Sample_sample_id, str):
            self.V1p4Sample_sample_id = str(self.V1p4Sample_sample_id)

        if self._is_empty(self.V1p4Sample_sample_type):
            self.MissingRequiredField("V1p4Sample_sample_type")
        if not isinstance(self.V1p4Sample_sample_type, str):
            self.V1p4Sample_sample_type = str(self.V1p4Sample_sample_type)

        if self._is_empty(self.V1p4Sample_anatomic_site):
            self.MissingRequiredField("V1p4Sample_anatomic_site")
        if not isinstance(self.V1p4Sample_anatomic_site, str):
            self.V1p4Sample_anatomic_site = str(self.V1p4Sample_anatomic_site)

        if self._is_empty(self.V1p4Sample_disease_state_sample):
            self.MissingRequiredField("V1p4Sample_disease_state_sample")
        if not isinstance(self.V1p4Sample_disease_state_sample, str):
            self.V1p4Sample_disease_state_sample = str(self.V1p4Sample_disease_state_sample)

        if self._is_empty(self.V1p4Sample_collection_time_point_relative):
            self.MissingRequiredField("V1p4Sample_collection_time_point_relative")
        if not isinstance(self.V1p4Sample_collection_time_point_relative, V1p4TimePoint):
            self.V1p4Sample_collection_time_point_relative = V1p4TimePoint(**as_dict(self.V1p4Sample_collection_time_point_relative))

        if self._is_empty(self.V1p4Sample_biomaterial_provider):
            self.MissingRequiredField("V1p4Sample_biomaterial_provider")
        if not isinstance(self.V1p4Sample_biomaterial_provider, str):
            self.V1p4Sample_biomaterial_provider = str(self.V1p4Sample_biomaterial_provider)

        if self._is_empty(self.V1p4CellProcessing_tissue_processing):
            self.MissingRequiredField("V1p4CellProcessing_tissue_processing")
        if not isinstance(self.V1p4CellProcessing_tissue_processing, str):
            self.V1p4CellProcessing_tissue_processing = str(self.V1p4CellProcessing_tissue_processing)

        if self._is_empty(self.V1p4CellProcessing_cell_phenotype):
            self.MissingRequiredField("V1p4CellProcessing_cell_phenotype")
        if not isinstance(self.V1p4CellProcessing_cell_phenotype, str):
            self.V1p4CellProcessing_cell_phenotype = str(self.V1p4CellProcessing_cell_phenotype)

        if self._is_empty(self.V1p4CellProcessing_single_cell):
            self.MissingRequiredField("V1p4CellProcessing_single_cell")
        if not isinstance(self.V1p4CellProcessing_single_cell, Bool):
            self.V1p4CellProcessing_single_cell = Bool(self.V1p4CellProcessing_single_cell)

        if self._is_empty(self.V1p4CellProcessing_cell_number):
            self.MissingRequiredField("V1p4CellProcessing_cell_number")
        if not isinstance(self.V1p4CellProcessing_cell_number, int):
            self.V1p4CellProcessing_cell_number = int(self.V1p4CellProcessing_cell_number)

        if self._is_empty(self.V1p4CellProcessing_cells_per_reaction):
            self.MissingRequiredField("V1p4CellProcessing_cells_per_reaction")
        if not isinstance(self.V1p4CellProcessing_cells_per_reaction, int):
            self.V1p4CellProcessing_cells_per_reaction = int(self.V1p4CellProcessing_cells_per_reaction)

        if self._is_empty(self.V1p4CellProcessing_cell_storage):
            self.MissingRequiredField("V1p4CellProcessing_cell_storage")
        if not isinstance(self.V1p4CellProcessing_cell_storage, Bool):
            self.V1p4CellProcessing_cell_storage = Bool(self.V1p4CellProcessing_cell_storage)

        if self._is_empty(self.V1p4CellProcessing_cell_quality):
            self.MissingRequiredField("V1p4CellProcessing_cell_quality")
        if not isinstance(self.V1p4CellProcessing_cell_quality, str):
            self.V1p4CellProcessing_cell_quality = str(self.V1p4CellProcessing_cell_quality)

        if self._is_empty(self.V1p4CellProcessing_cell_isolation):
            self.MissingRequiredField("V1p4CellProcessing_cell_isolation")
        if not isinstance(self.V1p4CellProcessing_cell_isolation, str):
            self.V1p4CellProcessing_cell_isolation = str(self.V1p4CellProcessing_cell_isolation)

        if self._is_empty(self.V1p4CellProcessing_cell_processing_protocol):
            self.MissingRequiredField("V1p4CellProcessing_cell_processing_protocol")
        if not isinstance(self.V1p4CellProcessing_cell_processing_protocol, str):
            self.V1p4CellProcessing_cell_processing_protocol = str(self.V1p4CellProcessing_cell_processing_protocol)

        if self._is_empty(self.V1p4NucleicAcidProcessing_template_class):
            self.MissingRequiredField("V1p4NucleicAcidProcessing_template_class")
        if not isinstance(self.V1p4NucleicAcidProcessing_template_class, V1p4TemplateClass):
            self.V1p4NucleicAcidProcessing_template_class = V1p4TemplateClass(self.V1p4NucleicAcidProcessing_template_class)

        if self._is_empty(self.V1p4NucleicAcidProcessing_template_quality):
            self.MissingRequiredField("V1p4NucleicAcidProcessing_template_quality")
        if not isinstance(self.V1p4NucleicAcidProcessing_template_quality, str):
            self.V1p4NucleicAcidProcessing_template_quality = str(self.V1p4NucleicAcidProcessing_template_quality)

        if self._is_empty(self.V1p4NucleicAcidProcessing_template_amount):
            self.MissingRequiredField("V1p4NucleicAcidProcessing_template_amount")
        if not isinstance(self.V1p4NucleicAcidProcessing_template_amount, V1p4PhysicalQuantity):
            self.V1p4NucleicAcidProcessing_template_amount = V1p4PhysicalQuantity(**as_dict(self.V1p4NucleicAcidProcessing_template_amount))

        if self._is_empty(self.V1p4NucleicAcidProcessing_library_generation_method):
            self.MissingRequiredField("V1p4NucleicAcidProcessing_library_generation_method")
        if not isinstance(self.V1p4NucleicAcidProcessing_library_generation_method, V1p4LibraryGenerationMethod):
            self.V1p4NucleicAcidProcessing_library_generation_method = V1p4LibraryGenerationMethod(self.V1p4NucleicAcidProcessing_library_generation_method)

        if self._is_empty(self.V1p4NucleicAcidProcessing_library_generation_protocol):
            self.MissingRequiredField("V1p4NucleicAcidProcessing_library_generation_protocol")
        if not isinstance(self.V1p4NucleicAcidProcessing_library_generation_protocol, str):
            self.V1p4NucleicAcidProcessing_library_generation_protocol = str(self.V1p4NucleicAcidProcessing_library_generation_protocol)

        if self._is_empty(self.V1p4NucleicAcidProcessing_library_generation_kit_version):
            self.MissingRequiredField("V1p4NucleicAcidProcessing_library_generation_kit_version")
        if not isinstance(self.V1p4NucleicAcidProcessing_library_generation_kit_version, str):
            self.V1p4NucleicAcidProcessing_library_generation_kit_version = str(self.V1p4NucleicAcidProcessing_library_generation_kit_version)

        if self._is_empty(self.V1p4NucleicAcidProcessing_complete_sequences):
            self.MissingRequiredField("V1p4NucleicAcidProcessing_complete_sequences")
        if not isinstance(self.V1p4NucleicAcidProcessing_complete_sequences, V1p4CompleteSequences):
            self.V1p4NucleicAcidProcessing_complete_sequences = V1p4CompleteSequences(self.V1p4NucleicAcidProcessing_complete_sequences)

        if self._is_empty(self.V1p4NucleicAcidProcessing_physical_linkage):
            self.MissingRequiredField("V1p4NucleicAcidProcessing_physical_linkage")
        if not isinstance(self.V1p4NucleicAcidProcessing_physical_linkage, V1p4PhysicalLinkage):
            self.V1p4NucleicAcidProcessing_physical_linkage = V1p4PhysicalLinkage(self.V1p4NucleicAcidProcessing_physical_linkage)

        if self._is_empty(self.V1p4SequencingRun_sequencing_run_id):
            self.MissingRequiredField("V1p4SequencingRun_sequencing_run_id")
        if not isinstance(self.V1p4SequencingRun_sequencing_run_id, str):
            self.V1p4SequencingRun_sequencing_run_id = str(self.V1p4SequencingRun_sequencing_run_id)

        if self._is_empty(self.V1p4SequencingRun_total_reads_passing_qc_filter):
            self.MissingRequiredField("V1p4SequencingRun_total_reads_passing_qc_filter")
        if not isinstance(self.V1p4SequencingRun_total_reads_passing_qc_filter, int):
            self.V1p4SequencingRun_total_reads_passing_qc_filter = int(self.V1p4SequencingRun_total_reads_passing_qc_filter)

        if self._is_empty(self.V1p4SequencingRun_sequencing_platform):
            self.MissingRequiredField("V1p4SequencingRun_sequencing_platform")
        if not isinstance(self.V1p4SequencingRun_sequencing_platform, str):
            self.V1p4SequencingRun_sequencing_platform = str(self.V1p4SequencingRun_sequencing_platform)

        if self._is_empty(self.V1p4SequencingRun_sequencing_facility):
            self.MissingRequiredField("V1p4SequencingRun_sequencing_facility")
        if not isinstance(self.V1p4SequencingRun_sequencing_facility, str):
            self.V1p4SequencingRun_sequencing_facility = str(self.V1p4SequencingRun_sequencing_facility)

        if self._is_empty(self.V1p4SequencingRun_sequencing_run_date):
            self.MissingRequiredField("V1p4SequencingRun_sequencing_run_date")
        if not isinstance(self.V1p4SequencingRun_sequencing_run_date, str):
            self.V1p4SequencingRun_sequencing_run_date = str(self.V1p4SequencingRun_sequencing_run_date)

        if self._is_empty(self.V1p4SequencingRun_sequencing_kit):
            self.MissingRequiredField("V1p4SequencingRun_sequencing_kit")
        if not isinstance(self.V1p4SequencingRun_sequencing_kit, str):
            self.V1p4SequencingRun_sequencing_kit = str(self.V1p4SequencingRun_sequencing_kit)

        if self.V1p4SampleProcessing_sample_processing_id is not None and not isinstance(self.V1p4SampleProcessing_sample_processing_id, str):
            self.V1p4SampleProcessing_sample_processing_id = str(self.V1p4SampleProcessing_sample_processing_id)

        if self.V1p4CellProcessing_cell_label is not None and not isinstance(self.V1p4CellProcessing_cell_label, str):
            self.V1p4CellProcessing_cell_label = str(self.V1p4CellProcessing_cell_label)

        self._normalize_inlined_as_dict(slot_name="V1p4NucleicAcidProcessing_pcr_target", slot_type=V1p4PCRTarget, key_name="V1p4PCRTarget_pcr_target_locus", keyed=False)

        if self.V1p4SequencingRun_sequencing_files is not None and not isinstance(self.V1p4SequencingRun_sequencing_files, V1p4SequencingData):
            self.V1p4SequencingRun_sequencing_files = V1p4SequencingData(**as_dict(self.V1p4SequencingRun_sequencing_files))

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

class ChainSimilarityType(EnumDefinitionImpl):

    exact_match = PermissibleValue(text="exact_match")
    exact_aa_match = PermissibleValue(text="exact_aa_match")
    cdr3_exact_match = PermissibleValue(text="cdr3_exact_match")
    cdr3_exact_aa_match = PermissibleValue(text="cdr3_exact_aa_match")
    cdr3_exact_aa_and_vj_match = PermissibleValue(text="cdr3_exact_aa_and_vj_match")

    _defn = EnumDefinition(
        name="ChainSimilarityType",
    )

class V1p5Unit(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="V1p5Unit",
    )

class V1p5Derivation(EnumDefinitionImpl):

    DNA = PermissibleValue(text="DNA")
    RNA = PermissibleValue(text="RNA")
    null = PermissibleValue(text="null")

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

    null = PermissibleValue(text="null")

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
    TRD = PermissibleValue(text="TRD")
    TRG = PermissibleValue(text="TRG")
    null = PermissibleValue(text="null")

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
    null = PermissibleValue(text="null")

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
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="V1p5SpeciesSubgroupType",
    )

class V1p5Status(EnumDefinitionImpl):

    active = PermissibleValue(text="active")
    draft = PermissibleValue(text="draft")
    retired = PermissibleValue(text="retired")
    withdrawn = PermissibleValue(text="withdrawn")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="V1p5Status",
    )

class V1p5JCodonFrame(EnumDefinitionImpl):

    null = PermissibleValue(text="null")

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
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="V1p5InferenceProcess",
    )

class V1p5MhcClass(EnumDefinitionImpl):

    null = PermissibleValue(text="null")

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
    null = PermissibleValue(text="null")

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
    null = PermissibleValue(text="null")

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
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="V1p5FileType",
    )

class V1p5ReadDirection(EnumDefinitionImpl):

    forward = PermissibleValue(text="forward")
    reverse = PermissibleValue(text="reverse")
    mixed = PermissibleValue(text="mixed")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="V1p5ReadDirection",
    )

class V1p5PairedReadDirection(EnumDefinitionImpl):

    forward = PermissibleValue(text="forward")
    reverse = PermissibleValue(text="reverse")
    mixed = PermissibleValue(text="mixed")
    null = PermissibleValue(text="null")

    _defn = EnumDefinition(
        name="V1p5PairedReadDirection",
    )

class V1p5ExpressionStudyMethod(EnumDefinitionImpl):

    flow_cytometry = PermissibleValue(text="flow_cytometry")
    null = PermissibleValue(text="null")

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

slots.chain_domain = Slot(uri=AK_SCHEMA.chain_domain, name="chain_domain", curie=AK_SCHEMA.curie('chain_domain'),
                   model_uri=AK_SCHEMA.chain_domain, domain=None, range=Optional[Union[str, ChainAkcId]])

slots.chain_codomain = Slot(uri=AK_SCHEMA.chain_codomain, name="chain_codomain", curie=AK_SCHEMA.curie('chain_codomain'),
                   model_uri=AK_SCHEMA.chain_codomain, domain=None, range=Optional[Union[str, ChainAkcId]])

slots.chain_similarity_type = Slot(uri=RDF.type, name="chain_similarity_type", curie=RDF.curie('type'),
                   model_uri=AK_SCHEMA.chain_similarity_type, domain=None, range=Optional[Union[str, "ChainSimilarityType"]])

slots.V1p5TimePoint_label = Slot(uri=AK_SCHEMA.V1p5TimePoint_label, name="V1p5TimePoint_label", curie=AK_SCHEMA.curie('V1p5TimePoint_label'),
                   model_uri=AK_SCHEMA.V1p5TimePoint_label, domain=None, range=Optional[str])

slots.V1p5TimePoint_value = Slot(uri=AK_SCHEMA.V1p5TimePoint_value, name="V1p5TimePoint_value", curie=AK_SCHEMA.curie('V1p5TimePoint_value'),
                   model_uri=AK_SCHEMA.V1p5TimePoint_value, domain=None, range=Optional[float])

slots.V1p5TimePoint_unit = Slot(uri=AK_SCHEMA.V1p5TimePoint_unit, name="V1p5TimePoint_unit", curie=AK_SCHEMA.curie('V1p5TimePoint_unit'),
                   model_uri=AK_SCHEMA.V1p5TimePoint_unit, domain=None, range=Optional[Union[str, "V1p5Unit"]])

slots.V1p5Acknowledgement_acknowledgement_id = Slot(uri=AK_SCHEMA.V1p5Acknowledgement_acknowledgement_id, name="V1p5Acknowledgement_acknowledgement_id", curie=AK_SCHEMA.curie('V1p5Acknowledgement_acknowledgement_id'),
                   model_uri=AK_SCHEMA.V1p5Acknowledgement_acknowledgement_id, domain=None, range=str)

slots.V1p5Acknowledgement_name = Slot(uri=AK_SCHEMA.V1p5Acknowledgement_name, name="V1p5Acknowledgement_name", curie=AK_SCHEMA.curie('V1p5Acknowledgement_name'),
                   model_uri=AK_SCHEMA.V1p5Acknowledgement_name, domain=None, range=str)

slots.V1p5Acknowledgement_institution_name = Slot(uri=AK_SCHEMA.V1p5Acknowledgement_institution_name, name="V1p5Acknowledgement_institution_name", curie=AK_SCHEMA.curie('V1p5Acknowledgement_institution_name'),
                   model_uri=AK_SCHEMA.V1p5Acknowledgement_institution_name, domain=None, range=str)

slots.V1p5Acknowledgement_orcid_id = Slot(uri=AK_SCHEMA.V1p5Acknowledgement_orcid_id, name="V1p5Acknowledgement_orcid_id", curie=AK_SCHEMA.curie('V1p5Acknowledgement_orcid_id'),
                   model_uri=AK_SCHEMA.V1p5Acknowledgement_orcid_id, domain=None, range=Optional[str])

slots.V1p5RearrangedSequence_sequence_id = Slot(uri=AK_SCHEMA.V1p5RearrangedSequence_sequence_id, name="V1p5RearrangedSequence_sequence_id", curie=AK_SCHEMA.curie('V1p5RearrangedSequence_sequence_id'),
                   model_uri=AK_SCHEMA.V1p5RearrangedSequence_sequence_id, domain=None, range=str)

slots.V1p5RearrangedSequence_sequence = Slot(uri=AK_SCHEMA.V1p5RearrangedSequence_sequence, name="V1p5RearrangedSequence_sequence", curie=AK_SCHEMA.curie('V1p5RearrangedSequence_sequence'),
                   model_uri=AK_SCHEMA.V1p5RearrangedSequence_sequence, domain=None, range=str)

slots.V1p5RearrangedSequence_derivation = Slot(uri=AK_SCHEMA.V1p5RearrangedSequence_derivation, name="V1p5RearrangedSequence_derivation", curie=AK_SCHEMA.curie('V1p5RearrangedSequence_derivation'),
                   model_uri=AK_SCHEMA.V1p5RearrangedSequence_derivation, domain=None, range=Union[str, "V1p5Derivation"])

slots.V1p5RearrangedSequence_observation_type = Slot(uri=AK_SCHEMA.V1p5RearrangedSequence_observation_type, name="V1p5RearrangedSequence_observation_type", curie=AK_SCHEMA.curie('V1p5RearrangedSequence_observation_type'),
                   model_uri=AK_SCHEMA.V1p5RearrangedSequence_observation_type, domain=None, range=Union[str, "V1p5ObservationType"])

slots.V1p5RearrangedSequence_curation = Slot(uri=AK_SCHEMA.V1p5RearrangedSequence_curation, name="V1p5RearrangedSequence_curation", curie=AK_SCHEMA.curie('V1p5RearrangedSequence_curation'),
                   model_uri=AK_SCHEMA.V1p5RearrangedSequence_curation, domain=None, range=Optional[str])

slots.V1p5RearrangedSequence_repository_name = Slot(uri=AK_SCHEMA.V1p5RearrangedSequence_repository_name, name="V1p5RearrangedSequence_repository_name", curie=AK_SCHEMA.curie('V1p5RearrangedSequence_repository_name'),
                   model_uri=AK_SCHEMA.V1p5RearrangedSequence_repository_name, domain=None, range=str)

slots.V1p5RearrangedSequence_repository_ref = Slot(uri=AK_SCHEMA.V1p5RearrangedSequence_repository_ref, name="V1p5RearrangedSequence_repository_ref", curie=AK_SCHEMA.curie('V1p5RearrangedSequence_repository_ref'),
                   model_uri=AK_SCHEMA.V1p5RearrangedSequence_repository_ref, domain=None, range=Optional[str])

slots.V1p5RearrangedSequence_deposited_version = Slot(uri=AK_SCHEMA.V1p5RearrangedSequence_deposited_version, name="V1p5RearrangedSequence_deposited_version", curie=AK_SCHEMA.curie('V1p5RearrangedSequence_deposited_version'),
                   model_uri=AK_SCHEMA.V1p5RearrangedSequence_deposited_version, domain=None, range=str)

slots.V1p5RearrangedSequence_sequence_start = Slot(uri=AK_SCHEMA.V1p5RearrangedSequence_sequence_start, name="V1p5RearrangedSequence_sequence_start", curie=AK_SCHEMA.curie('V1p5RearrangedSequence_sequence_start'),
                   model_uri=AK_SCHEMA.V1p5RearrangedSequence_sequence_start, domain=None, range=Optional[int])

slots.V1p5RearrangedSequence_sequence_end = Slot(uri=AK_SCHEMA.V1p5RearrangedSequence_sequence_end, name="V1p5RearrangedSequence_sequence_end", curie=AK_SCHEMA.curie('V1p5RearrangedSequence_sequence_end'),
                   model_uri=AK_SCHEMA.V1p5RearrangedSequence_sequence_end, domain=None, range=Optional[int])

slots.V1p5UnrearrangedSequence_sequence_id = Slot(uri=AK_SCHEMA.V1p5UnrearrangedSequence_sequence_id, name="V1p5UnrearrangedSequence_sequence_id", curie=AK_SCHEMA.curie('V1p5UnrearrangedSequence_sequence_id'),
                   model_uri=AK_SCHEMA.V1p5UnrearrangedSequence_sequence_id, domain=None, range=str)

slots.V1p5UnrearrangedSequence_sequence = Slot(uri=AK_SCHEMA.V1p5UnrearrangedSequence_sequence, name="V1p5UnrearrangedSequence_sequence", curie=AK_SCHEMA.curie('V1p5UnrearrangedSequence_sequence'),
                   model_uri=AK_SCHEMA.V1p5UnrearrangedSequence_sequence, domain=None, range=str)

slots.V1p5UnrearrangedSequence_curation = Slot(uri=AK_SCHEMA.V1p5UnrearrangedSequence_curation, name="V1p5UnrearrangedSequence_curation", curie=AK_SCHEMA.curie('V1p5UnrearrangedSequence_curation'),
                   model_uri=AK_SCHEMA.V1p5UnrearrangedSequence_curation, domain=None, range=Optional[str])

slots.V1p5UnrearrangedSequence_repository_name = Slot(uri=AK_SCHEMA.V1p5UnrearrangedSequence_repository_name, name="V1p5UnrearrangedSequence_repository_name", curie=AK_SCHEMA.curie('V1p5UnrearrangedSequence_repository_name'),
                   model_uri=AK_SCHEMA.V1p5UnrearrangedSequence_repository_name, domain=None, range=str)

slots.V1p5UnrearrangedSequence_repository_ref = Slot(uri=AK_SCHEMA.V1p5UnrearrangedSequence_repository_ref, name="V1p5UnrearrangedSequence_repository_ref", curie=AK_SCHEMA.curie('V1p5UnrearrangedSequence_repository_ref'),
                   model_uri=AK_SCHEMA.V1p5UnrearrangedSequence_repository_ref, domain=None, range=Optional[str])

slots.V1p5UnrearrangedSequence_patch_no = Slot(uri=AK_SCHEMA.V1p5UnrearrangedSequence_patch_no, name="V1p5UnrearrangedSequence_patch_no", curie=AK_SCHEMA.curie('V1p5UnrearrangedSequence_patch_no'),
                   model_uri=AK_SCHEMA.V1p5UnrearrangedSequence_patch_no, domain=None, range=Optional[str])

slots.V1p5UnrearrangedSequence_gff_seqid = Slot(uri=AK_SCHEMA.V1p5UnrearrangedSequence_gff_seqid, name="V1p5UnrearrangedSequence_gff_seqid", curie=AK_SCHEMA.curie('V1p5UnrearrangedSequence_gff_seqid'),
                   model_uri=AK_SCHEMA.V1p5UnrearrangedSequence_gff_seqid, domain=None, range=str)

slots.V1p5UnrearrangedSequence_gff_start = Slot(uri=AK_SCHEMA.V1p5UnrearrangedSequence_gff_start, name="V1p5UnrearrangedSequence_gff_start", curie=AK_SCHEMA.curie('V1p5UnrearrangedSequence_gff_start'),
                   model_uri=AK_SCHEMA.V1p5UnrearrangedSequence_gff_start, domain=None, range=int)

slots.V1p5UnrearrangedSequence_gff_end = Slot(uri=AK_SCHEMA.V1p5UnrearrangedSequence_gff_end, name="V1p5UnrearrangedSequence_gff_end", curie=AK_SCHEMA.curie('V1p5UnrearrangedSequence_gff_end'),
                   model_uri=AK_SCHEMA.V1p5UnrearrangedSequence_gff_end, domain=None, range=int)

slots.V1p5UnrearrangedSequence_strand = Slot(uri=AK_SCHEMA.V1p5UnrearrangedSequence_strand, name="V1p5UnrearrangedSequence_strand", curie=AK_SCHEMA.curie('V1p5UnrearrangedSequence_strand'),
                   model_uri=AK_SCHEMA.V1p5UnrearrangedSequence_strand, domain=None, range=Union[str, "V1p5Strand"])

slots.V1p5SequenceDelineationV_sequence_delineation_id = Slot(uri=AK_SCHEMA.V1p5SequenceDelineationV_sequence_delineation_id, name="V1p5SequenceDelineationV_sequence_delineation_id", curie=AK_SCHEMA.curie('V1p5SequenceDelineationV_sequence_delineation_id'),
                   model_uri=AK_SCHEMA.V1p5SequenceDelineationV_sequence_delineation_id, domain=None, range=str)

slots.V1p5SequenceDelineationV_delineation_scheme = Slot(uri=AK_SCHEMA.V1p5SequenceDelineationV_delineation_scheme, name="V1p5SequenceDelineationV_delineation_scheme", curie=AK_SCHEMA.curie('V1p5SequenceDelineationV_delineation_scheme'),
                   model_uri=AK_SCHEMA.V1p5SequenceDelineationV_delineation_scheme, domain=None, range=str)

slots.V1p5SequenceDelineationV_unaligned_sequence = Slot(uri=AK_SCHEMA.V1p5SequenceDelineationV_unaligned_sequence, name="V1p5SequenceDelineationV_unaligned_sequence", curie=AK_SCHEMA.curie('V1p5SequenceDelineationV_unaligned_sequence'),
                   model_uri=AK_SCHEMA.V1p5SequenceDelineationV_unaligned_sequence, domain=None, range=Optional[str])

slots.V1p5SequenceDelineationV_aligned_sequence = Slot(uri=AK_SCHEMA.V1p5SequenceDelineationV_aligned_sequence, name="V1p5SequenceDelineationV_aligned_sequence", curie=AK_SCHEMA.curie('V1p5SequenceDelineationV_aligned_sequence'),
                   model_uri=AK_SCHEMA.V1p5SequenceDelineationV_aligned_sequence, domain=None, range=Optional[str])

slots.V1p5SequenceDelineationV_fwr1_start = Slot(uri=AK_SCHEMA.V1p5SequenceDelineationV_fwr1_start, name="V1p5SequenceDelineationV_fwr1_start", curie=AK_SCHEMA.curie('V1p5SequenceDelineationV_fwr1_start'),
                   model_uri=AK_SCHEMA.V1p5SequenceDelineationV_fwr1_start, domain=None, range=int)

slots.V1p5SequenceDelineationV_fwr1_end = Slot(uri=AK_SCHEMA.V1p5SequenceDelineationV_fwr1_end, name="V1p5SequenceDelineationV_fwr1_end", curie=AK_SCHEMA.curie('V1p5SequenceDelineationV_fwr1_end'),
                   model_uri=AK_SCHEMA.V1p5SequenceDelineationV_fwr1_end, domain=None, range=int)

slots.V1p5SequenceDelineationV_cdr1_start = Slot(uri=AK_SCHEMA.V1p5SequenceDelineationV_cdr1_start, name="V1p5SequenceDelineationV_cdr1_start", curie=AK_SCHEMA.curie('V1p5SequenceDelineationV_cdr1_start'),
                   model_uri=AK_SCHEMA.V1p5SequenceDelineationV_cdr1_start, domain=None, range=int)

slots.V1p5SequenceDelineationV_cdr1_end = Slot(uri=AK_SCHEMA.V1p5SequenceDelineationV_cdr1_end, name="V1p5SequenceDelineationV_cdr1_end", curie=AK_SCHEMA.curie('V1p5SequenceDelineationV_cdr1_end'),
                   model_uri=AK_SCHEMA.V1p5SequenceDelineationV_cdr1_end, domain=None, range=int)

slots.V1p5SequenceDelineationV_fwr2_start = Slot(uri=AK_SCHEMA.V1p5SequenceDelineationV_fwr2_start, name="V1p5SequenceDelineationV_fwr2_start", curie=AK_SCHEMA.curie('V1p5SequenceDelineationV_fwr2_start'),
                   model_uri=AK_SCHEMA.V1p5SequenceDelineationV_fwr2_start, domain=None, range=int)

slots.V1p5SequenceDelineationV_fwr2_end = Slot(uri=AK_SCHEMA.V1p5SequenceDelineationV_fwr2_end, name="V1p5SequenceDelineationV_fwr2_end", curie=AK_SCHEMA.curie('V1p5SequenceDelineationV_fwr2_end'),
                   model_uri=AK_SCHEMA.V1p5SequenceDelineationV_fwr2_end, domain=None, range=int)

slots.V1p5SequenceDelineationV_cdr2_start = Slot(uri=AK_SCHEMA.V1p5SequenceDelineationV_cdr2_start, name="V1p5SequenceDelineationV_cdr2_start", curie=AK_SCHEMA.curie('V1p5SequenceDelineationV_cdr2_start'),
                   model_uri=AK_SCHEMA.V1p5SequenceDelineationV_cdr2_start, domain=None, range=int)

slots.V1p5SequenceDelineationV_cdr2_end = Slot(uri=AK_SCHEMA.V1p5SequenceDelineationV_cdr2_end, name="V1p5SequenceDelineationV_cdr2_end", curie=AK_SCHEMA.curie('V1p5SequenceDelineationV_cdr2_end'),
                   model_uri=AK_SCHEMA.V1p5SequenceDelineationV_cdr2_end, domain=None, range=int)

slots.V1p5SequenceDelineationV_fwr3_start = Slot(uri=AK_SCHEMA.V1p5SequenceDelineationV_fwr3_start, name="V1p5SequenceDelineationV_fwr3_start", curie=AK_SCHEMA.curie('V1p5SequenceDelineationV_fwr3_start'),
                   model_uri=AK_SCHEMA.V1p5SequenceDelineationV_fwr3_start, domain=None, range=int)

slots.V1p5SequenceDelineationV_fwr3_end = Slot(uri=AK_SCHEMA.V1p5SequenceDelineationV_fwr3_end, name="V1p5SequenceDelineationV_fwr3_end", curie=AK_SCHEMA.curie('V1p5SequenceDelineationV_fwr3_end'),
                   model_uri=AK_SCHEMA.V1p5SequenceDelineationV_fwr3_end, domain=None, range=int)

slots.V1p5SequenceDelineationV_cdr3_start = Slot(uri=AK_SCHEMA.V1p5SequenceDelineationV_cdr3_start, name="V1p5SequenceDelineationV_cdr3_start", curie=AK_SCHEMA.curie('V1p5SequenceDelineationV_cdr3_start'),
                   model_uri=AK_SCHEMA.V1p5SequenceDelineationV_cdr3_start, domain=None, range=int)

slots.V1p5SequenceDelineationV_alignment_labels = Slot(uri=AK_SCHEMA.V1p5SequenceDelineationV_alignment_labels, name="V1p5SequenceDelineationV_alignment_labels", curie=AK_SCHEMA.curie('V1p5SequenceDelineationV_alignment_labels'),
                   model_uri=AK_SCHEMA.V1p5SequenceDelineationV_alignment_labels, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p5AlleleDescription_allele_description_id = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_allele_description_id, name="V1p5AlleleDescription_allele_description_id", curie=AK_SCHEMA.curie('V1p5AlleleDescription_allele_description_id'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_allele_description_id, domain=None, range=str)

slots.V1p5AlleleDescription_allele_description_ref = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_allele_description_ref, name="V1p5AlleleDescription_allele_description_ref", curie=AK_SCHEMA.curie('V1p5AlleleDescription_allele_description_ref'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_allele_description_ref, domain=None, range=Optional[str])

slots.V1p5AlleleDescription_maintainer = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_maintainer, name="V1p5AlleleDescription_maintainer", curie=AK_SCHEMA.curie('V1p5AlleleDescription_maintainer'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_maintainer, domain=None, range=str)

slots.V1p5AlleleDescription_acknowledgements = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_acknowledgements, name="V1p5AlleleDescription_acknowledgements", curie=AK_SCHEMA.curie('V1p5AlleleDescription_acknowledgements'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_acknowledgements, domain=None, range=Optional[Union[Union[dict, V1p5Acknowledgement], List[Union[dict, V1p5Acknowledgement]]]])

slots.V1p5AlleleDescription_lab_address = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_lab_address, name="V1p5AlleleDescription_lab_address", curie=AK_SCHEMA.curie('V1p5AlleleDescription_lab_address'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_lab_address, domain=None, range=str)

slots.V1p5AlleleDescription_release_version = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_release_version, name="V1p5AlleleDescription_release_version", curie=AK_SCHEMA.curie('V1p5AlleleDescription_release_version'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_release_version, domain=None, range=int)

slots.V1p5AlleleDescription_release_date = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_release_date, name="V1p5AlleleDescription_release_date", curie=AK_SCHEMA.curie('V1p5AlleleDescription_release_date'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_release_date, domain=None, range=str)

slots.V1p5AlleleDescription_release_description = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_release_description, name="V1p5AlleleDescription_release_description", curie=AK_SCHEMA.curie('V1p5AlleleDescription_release_description'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_release_description, domain=None, range=str)

slots.V1p5AlleleDescription_label = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_label, name="V1p5AlleleDescription_label", curie=AK_SCHEMA.curie('V1p5AlleleDescription_label'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_label, domain=None, range=Optional[str])

slots.V1p5AlleleDescription_sequence = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_sequence, name="V1p5AlleleDescription_sequence", curie=AK_SCHEMA.curie('V1p5AlleleDescription_sequence'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_sequence, domain=None, range=str)

slots.V1p5AlleleDescription_coding_sequence = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_coding_sequence, name="V1p5AlleleDescription_coding_sequence", curie=AK_SCHEMA.curie('V1p5AlleleDescription_coding_sequence'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_coding_sequence, domain=None, range=str)

slots.V1p5AlleleDescription_aliases = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_aliases, name="V1p5AlleleDescription_aliases", curie=AK_SCHEMA.curie('V1p5AlleleDescription_aliases'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_aliases, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p5AlleleDescription_locus = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_locus, name="V1p5AlleleDescription_locus", curie=AK_SCHEMA.curie('V1p5AlleleDescription_locus'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_locus, domain=None, range=Union[str, "V1p5Locus"])

slots.V1p5AlleleDescription_chromosome = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_chromosome, name="V1p5AlleleDescription_chromosome", curie=AK_SCHEMA.curie('V1p5AlleleDescription_chromosome'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_chromosome, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_sequence_type = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_sequence_type, name="V1p5AlleleDescription_sequence_type", curie=AK_SCHEMA.curie('V1p5AlleleDescription_sequence_type'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_sequence_type, domain=None, range=Union[str, "V1p5SequenceType"])

slots.V1p5AlleleDescription_functional = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_functional, name="V1p5AlleleDescription_functional", curie=AK_SCHEMA.curie('V1p5AlleleDescription_functional'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_functional, domain=None, range=Union[bool, Bool])

slots.V1p5AlleleDescription_inference_type = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_inference_type, name="V1p5AlleleDescription_inference_type", curie=AK_SCHEMA.curie('V1p5AlleleDescription_inference_type'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_inference_type, domain=None, range=Union[str, "V1p5InferenceType"])

slots.V1p5AlleleDescription_species = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_species, name="V1p5AlleleDescription_species", curie=AK_SCHEMA.curie('V1p5AlleleDescription_species'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_species, domain=None, range=Union[str, "V1p5Species"])

slots.V1p5AlleleDescription_species_subgroup = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_species_subgroup, name="V1p5AlleleDescription_species_subgroup", curie=AK_SCHEMA.curie('V1p5AlleleDescription_species_subgroup'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_species_subgroup, domain=None, range=Optional[str])

slots.V1p5AlleleDescription_species_subgroup_type = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_species_subgroup_type, name="V1p5AlleleDescription_species_subgroup_type", curie=AK_SCHEMA.curie('V1p5AlleleDescription_species_subgroup_type'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_species_subgroup_type, domain=None, range=Optional[Union[str, "V1p5SpeciesSubgroupType"]])

slots.V1p5AlleleDescription_status = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_status, name="V1p5AlleleDescription_status", curie=AK_SCHEMA.curie('V1p5AlleleDescription_status'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_status, domain=None, range=Optional[Union[str, "V1p5Status"]])

slots.V1p5AlleleDescription_subgroup_designation = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_subgroup_designation, name="V1p5AlleleDescription_subgroup_designation", curie=AK_SCHEMA.curie('V1p5AlleleDescription_subgroup_designation'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_subgroup_designation, domain=None, range=Optional[str])

slots.V1p5AlleleDescription_gene_designation = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_gene_designation, name="V1p5AlleleDescription_gene_designation", curie=AK_SCHEMA.curie('V1p5AlleleDescription_gene_designation'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_gene_designation, domain=None, range=Optional[str])

slots.V1p5AlleleDescription_allele_designation = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_allele_designation, name="V1p5AlleleDescription_allele_designation", curie=AK_SCHEMA.curie('V1p5AlleleDescription_allele_designation'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_allele_designation, domain=None, range=Optional[str])

slots.V1p5AlleleDescription_allele_similarity_cluster_designation = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_allele_similarity_cluster_designation, name="V1p5AlleleDescription_allele_similarity_cluster_designation", curie=AK_SCHEMA.curie('V1p5AlleleDescription_allele_similarity_cluster_designation'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_allele_similarity_cluster_designation, domain=None, range=Optional[str])

slots.V1p5AlleleDescription_allele_similarity_cluster_member_id = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_allele_similarity_cluster_member_id, name="V1p5AlleleDescription_allele_similarity_cluster_member_id", curie=AK_SCHEMA.curie('V1p5AlleleDescription_allele_similarity_cluster_member_id'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_allele_similarity_cluster_member_id, domain=None, range=Optional[str])

slots.V1p5AlleleDescription_j_codon_frame = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_j_codon_frame, name="V1p5AlleleDescription_j_codon_frame", curie=AK_SCHEMA.curie('V1p5AlleleDescription_j_codon_frame'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_j_codon_frame, domain=None, range=Optional[Union[str, "V1p5JCodonFrame"]])

slots.V1p5AlleleDescription_gene_start = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_gene_start, name="V1p5AlleleDescription_gene_start", curie=AK_SCHEMA.curie('V1p5AlleleDescription_gene_start'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_gene_start, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_gene_end = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_gene_end, name="V1p5AlleleDescription_gene_end", curie=AK_SCHEMA.curie('V1p5AlleleDescription_gene_end'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_gene_end, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_utr_5_prime_start = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_utr_5_prime_start, name="V1p5AlleleDescription_utr_5_prime_start", curie=AK_SCHEMA.curie('V1p5AlleleDescription_utr_5_prime_start'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_utr_5_prime_start, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_utr_5_prime_end = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_utr_5_prime_end, name="V1p5AlleleDescription_utr_5_prime_end", curie=AK_SCHEMA.curie('V1p5AlleleDescription_utr_5_prime_end'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_utr_5_prime_end, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_leader_1_start = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_leader_1_start, name="V1p5AlleleDescription_leader_1_start", curie=AK_SCHEMA.curie('V1p5AlleleDescription_leader_1_start'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_leader_1_start, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_leader_1_end = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_leader_1_end, name="V1p5AlleleDescription_leader_1_end", curie=AK_SCHEMA.curie('V1p5AlleleDescription_leader_1_end'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_leader_1_end, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_leader_2_start = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_leader_2_start, name="V1p5AlleleDescription_leader_2_start", curie=AK_SCHEMA.curie('V1p5AlleleDescription_leader_2_start'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_leader_2_start, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_leader_2_end = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_leader_2_end, name="V1p5AlleleDescription_leader_2_end", curie=AK_SCHEMA.curie('V1p5AlleleDescription_leader_2_end'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_leader_2_end, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_v_rs_start = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_v_rs_start, name="V1p5AlleleDescription_v_rs_start", curie=AK_SCHEMA.curie('V1p5AlleleDescription_v_rs_start'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_v_rs_start, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_v_rs_end = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_v_rs_end, name="V1p5AlleleDescription_v_rs_end", curie=AK_SCHEMA.curie('V1p5AlleleDescription_v_rs_end'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_v_rs_end, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_d_rs_3_prime_start = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_d_rs_3_prime_start, name="V1p5AlleleDescription_d_rs_3_prime_start", curie=AK_SCHEMA.curie('V1p5AlleleDescription_d_rs_3_prime_start'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_d_rs_3_prime_start, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_d_rs_3_prime_end = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_d_rs_3_prime_end, name="V1p5AlleleDescription_d_rs_3_prime_end", curie=AK_SCHEMA.curie('V1p5AlleleDescription_d_rs_3_prime_end'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_d_rs_3_prime_end, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_d_rs_5_prime_start = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_d_rs_5_prime_start, name="V1p5AlleleDescription_d_rs_5_prime_start", curie=AK_SCHEMA.curie('V1p5AlleleDescription_d_rs_5_prime_start'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_d_rs_5_prime_start, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_d_rs_5_prime_end = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_d_rs_5_prime_end, name="V1p5AlleleDescription_d_rs_5_prime_end", curie=AK_SCHEMA.curie('V1p5AlleleDescription_d_rs_5_prime_end'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_d_rs_5_prime_end, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_j_cdr3_end = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_j_cdr3_end, name="V1p5AlleleDescription_j_cdr3_end", curie=AK_SCHEMA.curie('V1p5AlleleDescription_j_cdr3_end'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_j_cdr3_end, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_j_rs_start = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_j_rs_start, name="V1p5AlleleDescription_j_rs_start", curie=AK_SCHEMA.curie('V1p5AlleleDescription_j_rs_start'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_j_rs_start, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_j_rs_end = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_j_rs_end, name="V1p5AlleleDescription_j_rs_end", curie=AK_SCHEMA.curie('V1p5AlleleDescription_j_rs_end'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_j_rs_end, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_j_donor_splice = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_j_donor_splice, name="V1p5AlleleDescription_j_donor_splice", curie=AK_SCHEMA.curie('V1p5AlleleDescription_j_donor_splice'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_j_donor_splice, domain=None, range=Optional[int])

slots.V1p5AlleleDescription_v_gene_delineations = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_v_gene_delineations, name="V1p5AlleleDescription_v_gene_delineations", curie=AK_SCHEMA.curie('V1p5AlleleDescription_v_gene_delineations'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_v_gene_delineations, domain=None, range=Optional[Union[Union[dict, V1p5SequenceDelineationV], List[Union[dict, V1p5SequenceDelineationV]]]])

slots.V1p5AlleleDescription_unrearranged_support = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_unrearranged_support, name="V1p5AlleleDescription_unrearranged_support", curie=AK_SCHEMA.curie('V1p5AlleleDescription_unrearranged_support'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_unrearranged_support, domain=None, range=Optional[Union[Union[dict, V1p5UnrearrangedSequence], List[Union[dict, V1p5UnrearrangedSequence]]]])

slots.V1p5AlleleDescription_rearranged_support = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_rearranged_support, name="V1p5AlleleDescription_rearranged_support", curie=AK_SCHEMA.curie('V1p5AlleleDescription_rearranged_support'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_rearranged_support, domain=None, range=Optional[Union[Union[dict, V1p5RearrangedSequence], List[Union[dict, V1p5RearrangedSequence]]]])

slots.V1p5AlleleDescription_paralogs = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_paralogs, name="V1p5AlleleDescription_paralogs", curie=AK_SCHEMA.curie('V1p5AlleleDescription_paralogs'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_paralogs, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p5AlleleDescription_curation = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_curation, name="V1p5AlleleDescription_curation", curie=AK_SCHEMA.curie('V1p5AlleleDescription_curation'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_curation, domain=None, range=Optional[str])

slots.V1p5AlleleDescription_curational_tags = Slot(uri=AK_SCHEMA.V1p5AlleleDescription_curational_tags, name="V1p5AlleleDescription_curational_tags", curie=AK_SCHEMA.curie('V1p5AlleleDescription_curational_tags'),
                   model_uri=AK_SCHEMA.V1p5AlleleDescription_curational_tags, domain=None, range=Optional[Union[Union[str, "V1p5CurationalTags"], List[Union[str, "V1p5CurationalTags"]]]])

slots.V1p5GermlineSet_germline_set_id = Slot(uri=AK_SCHEMA.V1p5GermlineSet_germline_set_id, name="V1p5GermlineSet_germline_set_id", curie=AK_SCHEMA.curie('V1p5GermlineSet_germline_set_id'),
                   model_uri=AK_SCHEMA.V1p5GermlineSet_germline_set_id, domain=None, range=str)

slots.V1p5GermlineSet_author = Slot(uri=AK_SCHEMA.V1p5GermlineSet_author, name="V1p5GermlineSet_author", curie=AK_SCHEMA.curie('V1p5GermlineSet_author'),
                   model_uri=AK_SCHEMA.V1p5GermlineSet_author, domain=None, range=str)

slots.V1p5GermlineSet_lab_name = Slot(uri=AK_SCHEMA.V1p5GermlineSet_lab_name, name="V1p5GermlineSet_lab_name", curie=AK_SCHEMA.curie('V1p5GermlineSet_lab_name'),
                   model_uri=AK_SCHEMA.V1p5GermlineSet_lab_name, domain=None, range=str)

slots.V1p5GermlineSet_lab_address = Slot(uri=AK_SCHEMA.V1p5GermlineSet_lab_address, name="V1p5GermlineSet_lab_address", curie=AK_SCHEMA.curie('V1p5GermlineSet_lab_address'),
                   model_uri=AK_SCHEMA.V1p5GermlineSet_lab_address, domain=None, range=str)

slots.V1p5GermlineSet_acknowledgements = Slot(uri=AK_SCHEMA.V1p5GermlineSet_acknowledgements, name="V1p5GermlineSet_acknowledgements", curie=AK_SCHEMA.curie('V1p5GermlineSet_acknowledgements'),
                   model_uri=AK_SCHEMA.V1p5GermlineSet_acknowledgements, domain=None, range=Optional[Union[Union[dict, V1p5Acknowledgement], List[Union[dict, V1p5Acknowledgement]]]])

slots.V1p5GermlineSet_release_version = Slot(uri=AK_SCHEMA.V1p5GermlineSet_release_version, name="V1p5GermlineSet_release_version", curie=AK_SCHEMA.curie('V1p5GermlineSet_release_version'),
                   model_uri=AK_SCHEMA.V1p5GermlineSet_release_version, domain=None, range=int)

slots.V1p5GermlineSet_release_description = Slot(uri=AK_SCHEMA.V1p5GermlineSet_release_description, name="V1p5GermlineSet_release_description", curie=AK_SCHEMA.curie('V1p5GermlineSet_release_description'),
                   model_uri=AK_SCHEMA.V1p5GermlineSet_release_description, domain=None, range=str)

slots.V1p5GermlineSet_release_date = Slot(uri=AK_SCHEMA.V1p5GermlineSet_release_date, name="V1p5GermlineSet_release_date", curie=AK_SCHEMA.curie('V1p5GermlineSet_release_date'),
                   model_uri=AK_SCHEMA.V1p5GermlineSet_release_date, domain=None, range=str)

slots.V1p5GermlineSet_germline_set_name = Slot(uri=AK_SCHEMA.V1p5GermlineSet_germline_set_name, name="V1p5GermlineSet_germline_set_name", curie=AK_SCHEMA.curie('V1p5GermlineSet_germline_set_name'),
                   model_uri=AK_SCHEMA.V1p5GermlineSet_germline_set_name, domain=None, range=str)

slots.V1p5GermlineSet_germline_set_ref = Slot(uri=AK_SCHEMA.V1p5GermlineSet_germline_set_ref, name="V1p5GermlineSet_germline_set_ref", curie=AK_SCHEMA.curie('V1p5GermlineSet_germline_set_ref'),
                   model_uri=AK_SCHEMA.V1p5GermlineSet_germline_set_ref, domain=None, range=str)

slots.V1p5GermlineSet_pub_ids = Slot(uri=AK_SCHEMA.V1p5GermlineSet_pub_ids, name="V1p5GermlineSet_pub_ids", curie=AK_SCHEMA.curie('V1p5GermlineSet_pub_ids'),
                   model_uri=AK_SCHEMA.V1p5GermlineSet_pub_ids, domain=None, range=Optional[str])

slots.V1p5GermlineSet_species = Slot(uri=AK_SCHEMA.V1p5GermlineSet_species, name="V1p5GermlineSet_species", curie=AK_SCHEMA.curie('V1p5GermlineSet_species'),
                   model_uri=AK_SCHEMA.V1p5GermlineSet_species, domain=None, range=Union[str, "V1p5Species"])

slots.V1p5GermlineSet_species_subgroup = Slot(uri=AK_SCHEMA.V1p5GermlineSet_species_subgroup, name="V1p5GermlineSet_species_subgroup", curie=AK_SCHEMA.curie('V1p5GermlineSet_species_subgroup'),
                   model_uri=AK_SCHEMA.V1p5GermlineSet_species_subgroup, domain=None, range=Optional[str])

slots.V1p5GermlineSet_species_subgroup_type = Slot(uri=AK_SCHEMA.V1p5GermlineSet_species_subgroup_type, name="V1p5GermlineSet_species_subgroup_type", curie=AK_SCHEMA.curie('V1p5GermlineSet_species_subgroup_type'),
                   model_uri=AK_SCHEMA.V1p5GermlineSet_species_subgroup_type, domain=None, range=Optional[Union[str, "V1p5SpeciesSubgroupType"]])

slots.V1p5GermlineSet_locus = Slot(uri=AK_SCHEMA.V1p5GermlineSet_locus, name="V1p5GermlineSet_locus", curie=AK_SCHEMA.curie('V1p5GermlineSet_locus'),
                   model_uri=AK_SCHEMA.V1p5GermlineSet_locus, domain=None, range=Union[str, "V1p5Locus"])

slots.V1p5GermlineSet_allele_descriptions = Slot(uri=AK_SCHEMA.V1p5GermlineSet_allele_descriptions, name="V1p5GermlineSet_allele_descriptions", curie=AK_SCHEMA.curie('V1p5GermlineSet_allele_descriptions'),
                   model_uri=AK_SCHEMA.V1p5GermlineSet_allele_descriptions, domain=None, range=Union[Union[dict, V1p5AlleleDescription], List[Union[dict, V1p5AlleleDescription]]])

slots.V1p5GermlineSet_curation = Slot(uri=AK_SCHEMA.V1p5GermlineSet_curation, name="V1p5GermlineSet_curation", curie=AK_SCHEMA.curie('V1p5GermlineSet_curation'),
                   model_uri=AK_SCHEMA.V1p5GermlineSet_curation, domain=None, range=Optional[str])

slots.V1p5GenotypeSet_receptor_genotype_set_id = Slot(uri=AK_SCHEMA.V1p5GenotypeSet_receptor_genotype_set_id, name="V1p5GenotypeSet_receptor_genotype_set_id", curie=AK_SCHEMA.curie('V1p5GenotypeSet_receptor_genotype_set_id'),
                   model_uri=AK_SCHEMA.V1p5GenotypeSet_receptor_genotype_set_id, domain=None, range=str)

slots.V1p5GenotypeSet_genotype_class_list = Slot(uri=AK_SCHEMA.V1p5GenotypeSet_genotype_class_list, name="V1p5GenotypeSet_genotype_class_list", curie=AK_SCHEMA.curie('V1p5GenotypeSet_genotype_class_list'),
                   model_uri=AK_SCHEMA.V1p5GenotypeSet_genotype_class_list, domain=None, range=Optional[Union[Union[dict, V1p5Genotype], List[Union[dict, V1p5Genotype]]]])

slots.V1p5Genotype_receptor_genotype_id = Slot(uri=AK_SCHEMA.V1p5Genotype_receptor_genotype_id, name="V1p5Genotype_receptor_genotype_id", curie=AK_SCHEMA.curie('V1p5Genotype_receptor_genotype_id'),
                   model_uri=AK_SCHEMA.V1p5Genotype_receptor_genotype_id, domain=None, range=str)

slots.V1p5Genotype_locus = Slot(uri=AK_SCHEMA.V1p5Genotype_locus, name="V1p5Genotype_locus", curie=AK_SCHEMA.curie('V1p5Genotype_locus'),
                   model_uri=AK_SCHEMA.V1p5Genotype_locus, domain=None, range=Union[str, "V1p5Locus"])

slots.V1p5Genotype_documented_alleles = Slot(uri=AK_SCHEMA.V1p5Genotype_documented_alleles, name="V1p5Genotype_documented_alleles", curie=AK_SCHEMA.curie('V1p5Genotype_documented_alleles'),
                   model_uri=AK_SCHEMA.V1p5Genotype_documented_alleles, domain=None, range=Optional[Union[Union[dict, V1p5DocumentedAllele], List[Union[dict, V1p5DocumentedAllele]]]])

slots.V1p5Genotype_undocumented_alleles = Slot(uri=AK_SCHEMA.V1p5Genotype_undocumented_alleles, name="V1p5Genotype_undocumented_alleles", curie=AK_SCHEMA.curie('V1p5Genotype_undocumented_alleles'),
                   model_uri=AK_SCHEMA.V1p5Genotype_undocumented_alleles, domain=None, range=Optional[Union[Union[dict, V1p5UndocumentedAllele], List[Union[dict, V1p5UndocumentedAllele]]]])

slots.V1p5Genotype_deleted_genes = Slot(uri=AK_SCHEMA.V1p5Genotype_deleted_genes, name="V1p5Genotype_deleted_genes", curie=AK_SCHEMA.curie('V1p5Genotype_deleted_genes'),
                   model_uri=AK_SCHEMA.V1p5Genotype_deleted_genes, domain=None, range=Optional[Union[Union[dict, V1p5DeletedGene], List[Union[dict, V1p5DeletedGene]]]])

slots.V1p5Genotype_inference_process = Slot(uri=AK_SCHEMA.V1p5Genotype_inference_process, name="V1p5Genotype_inference_process", curie=AK_SCHEMA.curie('V1p5Genotype_inference_process'),
                   model_uri=AK_SCHEMA.V1p5Genotype_inference_process, domain=None, range=Optional[Union[str, "V1p5InferenceProcess"]])

slots.V1p5DocumentedAllele_label = Slot(uri=AK_SCHEMA.V1p5DocumentedAllele_label, name="V1p5DocumentedAllele_label", curie=AK_SCHEMA.curie('V1p5DocumentedAllele_label'),
                   model_uri=AK_SCHEMA.V1p5DocumentedAllele_label, domain=None, range=str)

slots.V1p5DocumentedAllele_germline_set_ref = Slot(uri=AK_SCHEMA.V1p5DocumentedAllele_germline_set_ref, name="V1p5DocumentedAllele_germline_set_ref", curie=AK_SCHEMA.curie('V1p5DocumentedAllele_germline_set_ref'),
                   model_uri=AK_SCHEMA.V1p5DocumentedAllele_germline_set_ref, domain=None, range=str)

slots.V1p5DocumentedAllele_phasing = Slot(uri=AK_SCHEMA.V1p5DocumentedAllele_phasing, name="V1p5DocumentedAllele_phasing", curie=AK_SCHEMA.curie('V1p5DocumentedAllele_phasing'),
                   model_uri=AK_SCHEMA.V1p5DocumentedAllele_phasing, domain=None, range=Optional[int])

slots.V1p5UndocumentedAllele_allele_name = Slot(uri=AK_SCHEMA.V1p5UndocumentedAllele_allele_name, name="V1p5UndocumentedAllele_allele_name", curie=AK_SCHEMA.curie('V1p5UndocumentedAllele_allele_name'),
                   model_uri=AK_SCHEMA.V1p5UndocumentedAllele_allele_name, domain=None, range=str)

slots.V1p5UndocumentedAllele_sequence = Slot(uri=AK_SCHEMA.V1p5UndocumentedAllele_sequence, name="V1p5UndocumentedAllele_sequence", curie=AK_SCHEMA.curie('V1p5UndocumentedAllele_sequence'),
                   model_uri=AK_SCHEMA.V1p5UndocumentedAllele_sequence, domain=None, range=str)

slots.V1p5UndocumentedAllele_phasing = Slot(uri=AK_SCHEMA.V1p5UndocumentedAllele_phasing, name="V1p5UndocumentedAllele_phasing", curie=AK_SCHEMA.curie('V1p5UndocumentedAllele_phasing'),
                   model_uri=AK_SCHEMA.V1p5UndocumentedAllele_phasing, domain=None, range=Optional[int])

slots.V1p5DeletedGene_label = Slot(uri=AK_SCHEMA.V1p5DeletedGene_label, name="V1p5DeletedGene_label", curie=AK_SCHEMA.curie('V1p5DeletedGene_label'),
                   model_uri=AK_SCHEMA.V1p5DeletedGene_label, domain=None, range=str)

slots.V1p5DeletedGene_germline_set_ref = Slot(uri=AK_SCHEMA.V1p5DeletedGene_germline_set_ref, name="V1p5DeletedGene_germline_set_ref", curie=AK_SCHEMA.curie('V1p5DeletedGene_germline_set_ref'),
                   model_uri=AK_SCHEMA.V1p5DeletedGene_germline_set_ref, domain=None, range=str)

slots.V1p5DeletedGene_phasing = Slot(uri=AK_SCHEMA.V1p5DeletedGene_phasing, name="V1p5DeletedGene_phasing", curie=AK_SCHEMA.curie('V1p5DeletedGene_phasing'),
                   model_uri=AK_SCHEMA.V1p5DeletedGene_phasing, domain=None, range=Optional[int])

slots.V1p5MHCGenotypeSet_mhc_genotype_set_id = Slot(uri=AK_SCHEMA.V1p5MHCGenotypeSet_mhc_genotype_set_id, name="V1p5MHCGenotypeSet_mhc_genotype_set_id", curie=AK_SCHEMA.curie('V1p5MHCGenotypeSet_mhc_genotype_set_id'),
                   model_uri=AK_SCHEMA.V1p5MHCGenotypeSet_mhc_genotype_set_id, domain=None, range=str)

slots.V1p5MHCGenotypeSet_mhc_genotype_list = Slot(uri=AK_SCHEMA.V1p5MHCGenotypeSet_mhc_genotype_list, name="V1p5MHCGenotypeSet_mhc_genotype_list", curie=AK_SCHEMA.curie('V1p5MHCGenotypeSet_mhc_genotype_list'),
                   model_uri=AK_SCHEMA.V1p5MHCGenotypeSet_mhc_genotype_list, domain=None, range=Union[Union[dict, V1p5MHCGenotype], List[Union[dict, V1p5MHCGenotype]]])

slots.V1p5MHCGenotype_mhc_genotype_id = Slot(uri=AK_SCHEMA.V1p5MHCGenotype_mhc_genotype_id, name="V1p5MHCGenotype_mhc_genotype_id", curie=AK_SCHEMA.curie('V1p5MHCGenotype_mhc_genotype_id'),
                   model_uri=AK_SCHEMA.V1p5MHCGenotype_mhc_genotype_id, domain=None, range=str)

slots.V1p5MHCGenotype_mhc_class = Slot(uri=AK_SCHEMA.V1p5MHCGenotype_mhc_class, name="V1p5MHCGenotype_mhc_class", curie=AK_SCHEMA.curie('V1p5MHCGenotype_mhc_class'),
                   model_uri=AK_SCHEMA.V1p5MHCGenotype_mhc_class, domain=None, range=Union[str, "V1p5MhcClass"])

slots.V1p5MHCGenotype_mhc_alleles = Slot(uri=AK_SCHEMA.V1p5MHCGenotype_mhc_alleles, name="V1p5MHCGenotype_mhc_alleles", curie=AK_SCHEMA.curie('V1p5MHCGenotype_mhc_alleles'),
                   model_uri=AK_SCHEMA.V1p5MHCGenotype_mhc_alleles, domain=None, range=Union[Union[dict, V1p5MHCAllele], List[Union[dict, V1p5MHCAllele]]])

slots.V1p5MHCGenotype_mhc_genotyping_method = Slot(uri=AK_SCHEMA.V1p5MHCGenotype_mhc_genotyping_method, name="V1p5MHCGenotype_mhc_genotyping_method", curie=AK_SCHEMA.curie('V1p5MHCGenotype_mhc_genotyping_method'),
                   model_uri=AK_SCHEMA.V1p5MHCGenotype_mhc_genotyping_method, domain=None, range=Optional[str])

slots.V1p5MHCAllele_allele_designation = Slot(uri=AK_SCHEMA.V1p5MHCAllele_allele_designation, name="V1p5MHCAllele_allele_designation", curie=AK_SCHEMA.curie('V1p5MHCAllele_allele_designation'),
                   model_uri=AK_SCHEMA.V1p5MHCAllele_allele_designation, domain=None, range=Optional[str])

slots.V1p5MHCAllele_gene = Slot(uri=AK_SCHEMA.V1p5MHCAllele_gene, name="V1p5MHCAllele_gene", curie=AK_SCHEMA.curie('V1p5MHCAllele_gene'),
                   model_uri=AK_SCHEMA.V1p5MHCAllele_gene, domain=None, range=Optional[Union[str, "V1p5Gene"]])

slots.V1p5MHCAllele_reference_set_ref = Slot(uri=AK_SCHEMA.V1p5MHCAllele_reference_set_ref, name="V1p5MHCAllele_reference_set_ref", curie=AK_SCHEMA.curie('V1p5MHCAllele_reference_set_ref'),
                   model_uri=AK_SCHEMA.V1p5MHCAllele_reference_set_ref, domain=None, range=Optional[str])

slots.V1p5SubjectGenotype_receptor_genotype_set = Slot(uri=AK_SCHEMA.V1p5SubjectGenotype_receptor_genotype_set, name="V1p5SubjectGenotype_receptor_genotype_set", curie=AK_SCHEMA.curie('V1p5SubjectGenotype_receptor_genotype_set'),
                   model_uri=AK_SCHEMA.V1p5SubjectGenotype_receptor_genotype_set, domain=None, range=Optional[Union[dict, V1p5GenotypeSet]])

slots.V1p5SubjectGenotype_mhc_genotype_set = Slot(uri=AK_SCHEMA.V1p5SubjectGenotype_mhc_genotype_set, name="V1p5SubjectGenotype_mhc_genotype_set", curie=AK_SCHEMA.curie('V1p5SubjectGenotype_mhc_genotype_set'),
                   model_uri=AK_SCHEMA.V1p5SubjectGenotype_mhc_genotype_set, domain=None, range=Optional[Union[dict, V1p5MHCGenotypeSet]])

slots.V1p5Study_study_id = Slot(uri=AK_SCHEMA.V1p5Study_study_id, name="V1p5Study_study_id", curie=AK_SCHEMA.curie('V1p5Study_study_id'),
                   model_uri=AK_SCHEMA.V1p5Study_study_id, domain=None, range=str)

slots.V1p5Study_study_title = Slot(uri=AK_SCHEMA.V1p5Study_study_title, name="V1p5Study_study_title", curie=AK_SCHEMA.curie('V1p5Study_study_title'),
                   model_uri=AK_SCHEMA.V1p5Study_study_title, domain=None, range=str)

slots.V1p5Study_study_type = Slot(uri=AK_SCHEMA.V1p5Study_study_type, name="V1p5Study_study_type", curie=AK_SCHEMA.curie('V1p5Study_study_type'),
                   model_uri=AK_SCHEMA.V1p5Study_study_type, domain=None, range=Union[str, "V1p5StudyType"])

slots.V1p5Study_study_description = Slot(uri=AK_SCHEMA.V1p5Study_study_description, name="V1p5Study_study_description", curie=AK_SCHEMA.curie('V1p5Study_study_description'),
                   model_uri=AK_SCHEMA.V1p5Study_study_description, domain=None, range=Optional[str])

slots.V1p5Study_inclusion_exclusion_criteria = Slot(uri=AK_SCHEMA.V1p5Study_inclusion_exclusion_criteria, name="V1p5Study_inclusion_exclusion_criteria", curie=AK_SCHEMA.curie('V1p5Study_inclusion_exclusion_criteria'),
                   model_uri=AK_SCHEMA.V1p5Study_inclusion_exclusion_criteria, domain=None, range=str)

slots.V1p5Study_grants = Slot(uri=AK_SCHEMA.V1p5Study_grants, name="V1p5Study_grants", curie=AK_SCHEMA.curie('V1p5Study_grants'),
                   model_uri=AK_SCHEMA.V1p5Study_grants, domain=None, range=str)

slots.V1p5Study_study_contact = Slot(uri=AK_SCHEMA.V1p5Study_study_contact, name="V1p5Study_study_contact", curie=AK_SCHEMA.curie('V1p5Study_study_contact'),
                   model_uri=AK_SCHEMA.V1p5Study_study_contact, domain=None, range=Optional[str])

slots.V1p5Study_collected_by = Slot(uri=AK_SCHEMA.V1p5Study_collected_by, name="V1p5Study_collected_by", curie=AK_SCHEMA.curie('V1p5Study_collected_by'),
                   model_uri=AK_SCHEMA.V1p5Study_collected_by, domain=None, range=str)

slots.V1p5Study_lab_name = Slot(uri=AK_SCHEMA.V1p5Study_lab_name, name="V1p5Study_lab_name", curie=AK_SCHEMA.curie('V1p5Study_lab_name'),
                   model_uri=AK_SCHEMA.V1p5Study_lab_name, domain=None, range=str)

slots.V1p5Study_lab_address = Slot(uri=AK_SCHEMA.V1p5Study_lab_address, name="V1p5Study_lab_address", curie=AK_SCHEMA.curie('V1p5Study_lab_address'),
                   model_uri=AK_SCHEMA.V1p5Study_lab_address, domain=None, range=str)

slots.V1p5Study_submitted_by = Slot(uri=AK_SCHEMA.V1p5Study_submitted_by, name="V1p5Study_submitted_by", curie=AK_SCHEMA.curie('V1p5Study_submitted_by'),
                   model_uri=AK_SCHEMA.V1p5Study_submitted_by, domain=None, range=str)

slots.V1p5Study_pub_ids = Slot(uri=AK_SCHEMA.V1p5Study_pub_ids, name="V1p5Study_pub_ids", curie=AK_SCHEMA.curie('V1p5Study_pub_ids'),
                   model_uri=AK_SCHEMA.V1p5Study_pub_ids, domain=None, range=str)

slots.V1p5Study_keywords_study = Slot(uri=AK_SCHEMA.V1p5Study_keywords_study, name="V1p5Study_keywords_study", curie=AK_SCHEMA.curie('V1p5Study_keywords_study'),
                   model_uri=AK_SCHEMA.V1p5Study_keywords_study, domain=None, range=Union[Union[str, "V1p5KeywordsStudy"], List[Union[str, "V1p5KeywordsStudy"]]])

slots.V1p5Study_adc_publish_date = Slot(uri=AK_SCHEMA.V1p5Study_adc_publish_date, name="V1p5Study_adc_publish_date", curie=AK_SCHEMA.curie('V1p5Study_adc_publish_date'),
                   model_uri=AK_SCHEMA.V1p5Study_adc_publish_date, domain=None, range=Optional[str])

slots.V1p5Study_adc_update_date = Slot(uri=AK_SCHEMA.V1p5Study_adc_update_date, name="V1p5Study_adc_update_date", curie=AK_SCHEMA.curie('V1p5Study_adc_update_date'),
                   model_uri=AK_SCHEMA.V1p5Study_adc_update_date, domain=None, range=Optional[str])

slots.V1p5Subject_subject_id = Slot(uri=AK_SCHEMA.V1p5Subject_subject_id, name="V1p5Subject_subject_id", curie=AK_SCHEMA.curie('V1p5Subject_subject_id'),
                   model_uri=AK_SCHEMA.V1p5Subject_subject_id, domain=None, range=str)

slots.V1p5Subject_synthetic = Slot(uri=AK_SCHEMA.V1p5Subject_synthetic, name="V1p5Subject_synthetic", curie=AK_SCHEMA.curie('V1p5Subject_synthetic'),
                   model_uri=AK_SCHEMA.V1p5Subject_synthetic, domain=None, range=Union[bool, Bool])

slots.V1p5Subject_species = Slot(uri=AK_SCHEMA.V1p5Subject_species, name="V1p5Subject_species", curie=AK_SCHEMA.curie('V1p5Subject_species'),
                   model_uri=AK_SCHEMA.V1p5Subject_species, domain=None, range=Union[str, "V1p5Species"])

slots.V1p5Subject_sex = Slot(uri=AK_SCHEMA.V1p5Subject_sex, name="V1p5Subject_sex", curie=AK_SCHEMA.curie('V1p5Subject_sex'),
                   model_uri=AK_SCHEMA.V1p5Subject_sex, domain=None, range=Union[str, "V1p5Sex"])

slots.V1p5Subject_age_min = Slot(uri=AK_SCHEMA.V1p5Subject_age_min, name="V1p5Subject_age_min", curie=AK_SCHEMA.curie('V1p5Subject_age_min'),
                   model_uri=AK_SCHEMA.V1p5Subject_age_min, domain=None, range=float)

slots.V1p5Subject_age_max = Slot(uri=AK_SCHEMA.V1p5Subject_age_max, name="V1p5Subject_age_max", curie=AK_SCHEMA.curie('V1p5Subject_age_max'),
                   model_uri=AK_SCHEMA.V1p5Subject_age_max, domain=None, range=float)

slots.V1p5Subject_age_unit = Slot(uri=AK_SCHEMA.V1p5Subject_age_unit, name="V1p5Subject_age_unit", curie=AK_SCHEMA.curie('V1p5Subject_age_unit'),
                   model_uri=AK_SCHEMA.V1p5Subject_age_unit, domain=None, range=Union[str, "V1p5AgeUnit"])

slots.V1p5Subject_age_event = Slot(uri=AK_SCHEMA.V1p5Subject_age_event, name="V1p5Subject_age_event", curie=AK_SCHEMA.curie('V1p5Subject_age_event'),
                   model_uri=AK_SCHEMA.V1p5Subject_age_event, domain=None, range=str)

slots.V1p5Subject_ancestry_population = Slot(uri=AK_SCHEMA.V1p5Subject_ancestry_population, name="V1p5Subject_ancestry_population", curie=AK_SCHEMA.curie('V1p5Subject_ancestry_population'),
                   model_uri=AK_SCHEMA.V1p5Subject_ancestry_population, domain=None, range=str)

slots.V1p5Subject_ethnicity = Slot(uri=AK_SCHEMA.V1p5Subject_ethnicity, name="V1p5Subject_ethnicity", curie=AK_SCHEMA.curie('V1p5Subject_ethnicity'),
                   model_uri=AK_SCHEMA.V1p5Subject_ethnicity, domain=None, range=str)

slots.V1p5Subject_race = Slot(uri=AK_SCHEMA.V1p5Subject_race, name="V1p5Subject_race", curie=AK_SCHEMA.curie('V1p5Subject_race'),
                   model_uri=AK_SCHEMA.V1p5Subject_race, domain=None, range=str)

slots.V1p5Subject_strain_name = Slot(uri=AK_SCHEMA.V1p5Subject_strain_name, name="V1p5Subject_strain_name", curie=AK_SCHEMA.curie('V1p5Subject_strain_name'),
                   model_uri=AK_SCHEMA.V1p5Subject_strain_name, domain=None, range=str)

slots.V1p5Subject_linked_subjects = Slot(uri=AK_SCHEMA.V1p5Subject_linked_subjects, name="V1p5Subject_linked_subjects", curie=AK_SCHEMA.curie('V1p5Subject_linked_subjects'),
                   model_uri=AK_SCHEMA.V1p5Subject_linked_subjects, domain=None, range=str)

slots.V1p5Subject_link_type = Slot(uri=AK_SCHEMA.V1p5Subject_link_type, name="V1p5Subject_link_type", curie=AK_SCHEMA.curie('V1p5Subject_link_type'),
                   model_uri=AK_SCHEMA.V1p5Subject_link_type, domain=None, range=str)

slots.V1p5Subject_diagnosis = Slot(uri=AK_SCHEMA.V1p5Subject_diagnosis, name="V1p5Subject_diagnosis", curie=AK_SCHEMA.curie('V1p5Subject_diagnosis'),
                   model_uri=AK_SCHEMA.V1p5Subject_diagnosis, domain=None, range=Optional[Union[Union[dict, V1p5Diagnosis], List[Union[dict, V1p5Diagnosis]]]])

slots.V1p5Subject_genotype = Slot(uri=AK_SCHEMA.V1p5Subject_genotype, name="V1p5Subject_genotype", curie=AK_SCHEMA.curie('V1p5Subject_genotype'),
                   model_uri=AK_SCHEMA.V1p5Subject_genotype, domain=None, range=Optional[Union[dict, V1p5SubjectGenotype]])

slots.V1p5Diagnosis_study_group_description = Slot(uri=AK_SCHEMA.V1p5Diagnosis_study_group_description, name="V1p5Diagnosis_study_group_description", curie=AK_SCHEMA.curie('V1p5Diagnosis_study_group_description'),
                   model_uri=AK_SCHEMA.V1p5Diagnosis_study_group_description, domain=None, range=str)

slots.V1p5Diagnosis_disease_diagnosis = Slot(uri=AK_SCHEMA.V1p5Diagnosis_disease_diagnosis, name="V1p5Diagnosis_disease_diagnosis", curie=AK_SCHEMA.curie('V1p5Diagnosis_disease_diagnosis'),
                   model_uri=AK_SCHEMA.V1p5Diagnosis_disease_diagnosis, domain=None, range=Union[str, "V1p5DiseaseDiagnosis"])

slots.V1p5Diagnosis_disease_length = Slot(uri=AK_SCHEMA.V1p5Diagnosis_disease_length, name="V1p5Diagnosis_disease_length", curie=AK_SCHEMA.curie('V1p5Diagnosis_disease_length'),
                   model_uri=AK_SCHEMA.V1p5Diagnosis_disease_length, domain=None, range=str)

slots.V1p5Diagnosis_disease_stage = Slot(uri=AK_SCHEMA.V1p5Diagnosis_disease_stage, name="V1p5Diagnosis_disease_stage", curie=AK_SCHEMA.curie('V1p5Diagnosis_disease_stage'),
                   model_uri=AK_SCHEMA.V1p5Diagnosis_disease_stage, domain=None, range=str)

slots.V1p5Diagnosis_prior_therapies = Slot(uri=AK_SCHEMA.V1p5Diagnosis_prior_therapies, name="V1p5Diagnosis_prior_therapies", curie=AK_SCHEMA.curie('V1p5Diagnosis_prior_therapies'),
                   model_uri=AK_SCHEMA.V1p5Diagnosis_prior_therapies, domain=None, range=str)

slots.V1p5Diagnosis_immunogen = Slot(uri=AK_SCHEMA.V1p5Diagnosis_immunogen, name="V1p5Diagnosis_immunogen", curie=AK_SCHEMA.curie('V1p5Diagnosis_immunogen'),
                   model_uri=AK_SCHEMA.V1p5Diagnosis_immunogen, domain=None, range=str)

slots.V1p5Diagnosis_intervention = Slot(uri=AK_SCHEMA.V1p5Diagnosis_intervention, name="V1p5Diagnosis_intervention", curie=AK_SCHEMA.curie('V1p5Diagnosis_intervention'),
                   model_uri=AK_SCHEMA.V1p5Diagnosis_intervention, domain=None, range=str)

slots.V1p5Diagnosis_medical_history = Slot(uri=AK_SCHEMA.V1p5Diagnosis_medical_history, name="V1p5Diagnosis_medical_history", curie=AK_SCHEMA.curie('V1p5Diagnosis_medical_history'),
                   model_uri=AK_SCHEMA.V1p5Diagnosis_medical_history, domain=None, range=str)

slots.V1p5Sample_sample_id = Slot(uri=AK_SCHEMA.V1p5Sample_sample_id, name="V1p5Sample_sample_id", curie=AK_SCHEMA.curie('V1p5Sample_sample_id'),
                   model_uri=AK_SCHEMA.V1p5Sample_sample_id, domain=None, range=str)

slots.V1p5Sample_sample_type = Slot(uri=AK_SCHEMA.V1p5Sample_sample_type, name="V1p5Sample_sample_type", curie=AK_SCHEMA.curie('V1p5Sample_sample_type'),
                   model_uri=AK_SCHEMA.V1p5Sample_sample_type, domain=None, range=str)

slots.V1p5Sample_tissue = Slot(uri=AK_SCHEMA.V1p5Sample_tissue, name="V1p5Sample_tissue", curie=AK_SCHEMA.curie('V1p5Sample_tissue'),
                   model_uri=AK_SCHEMA.V1p5Sample_tissue, domain=None, range=Union[str, "V1p5Tissue"])

slots.V1p5Sample_anatomic_site = Slot(uri=AK_SCHEMA.V1p5Sample_anatomic_site, name="V1p5Sample_anatomic_site", curie=AK_SCHEMA.curie('V1p5Sample_anatomic_site'),
                   model_uri=AK_SCHEMA.V1p5Sample_anatomic_site, domain=None, range=str)

slots.V1p5Sample_disease_state_sample = Slot(uri=AK_SCHEMA.V1p5Sample_disease_state_sample, name="V1p5Sample_disease_state_sample", curie=AK_SCHEMA.curie('V1p5Sample_disease_state_sample'),
                   model_uri=AK_SCHEMA.V1p5Sample_disease_state_sample, domain=None, range=str)

slots.V1p5Sample_collection_time_point_relative = Slot(uri=AK_SCHEMA.V1p5Sample_collection_time_point_relative, name="V1p5Sample_collection_time_point_relative", curie=AK_SCHEMA.curie('V1p5Sample_collection_time_point_relative'),
                   model_uri=AK_SCHEMA.V1p5Sample_collection_time_point_relative, domain=None, range=float)

slots.V1p5Sample_collection_time_point_relative_unit = Slot(uri=AK_SCHEMA.V1p5Sample_collection_time_point_relative_unit, name="V1p5Sample_collection_time_point_relative_unit", curie=AK_SCHEMA.curie('V1p5Sample_collection_time_point_relative_unit'),
                   model_uri=AK_SCHEMA.V1p5Sample_collection_time_point_relative_unit, domain=None, range=Union[str, "V1p5CollectionTimePointRelativeUnit"])

slots.V1p5Sample_collection_time_point_reference = Slot(uri=AK_SCHEMA.V1p5Sample_collection_time_point_reference, name="V1p5Sample_collection_time_point_reference", curie=AK_SCHEMA.curie('V1p5Sample_collection_time_point_reference'),
                   model_uri=AK_SCHEMA.V1p5Sample_collection_time_point_reference, domain=None, range=str)

slots.V1p5Sample_biomaterial_provider = Slot(uri=AK_SCHEMA.V1p5Sample_biomaterial_provider, name="V1p5Sample_biomaterial_provider", curie=AK_SCHEMA.curie('V1p5Sample_biomaterial_provider'),
                   model_uri=AK_SCHEMA.V1p5Sample_biomaterial_provider, domain=None, range=str)

slots.V1p5CellProcessing_tissue_processing = Slot(uri=AK_SCHEMA.V1p5CellProcessing_tissue_processing, name="V1p5CellProcessing_tissue_processing", curie=AK_SCHEMA.curie('V1p5CellProcessing_tissue_processing'),
                   model_uri=AK_SCHEMA.V1p5CellProcessing_tissue_processing, domain=None, range=str)

slots.V1p5CellProcessing_cell_subset = Slot(uri=AK_SCHEMA.V1p5CellProcessing_cell_subset, name="V1p5CellProcessing_cell_subset", curie=AK_SCHEMA.curie('V1p5CellProcessing_cell_subset'),
                   model_uri=AK_SCHEMA.V1p5CellProcessing_cell_subset, domain=None, range=Union[str, "V1p5CellSubset"])

slots.V1p5CellProcessing_cell_phenotype = Slot(uri=AK_SCHEMA.V1p5CellProcessing_cell_phenotype, name="V1p5CellProcessing_cell_phenotype", curie=AK_SCHEMA.curie('V1p5CellProcessing_cell_phenotype'),
                   model_uri=AK_SCHEMA.V1p5CellProcessing_cell_phenotype, domain=None, range=str)

slots.V1p5CellProcessing_cell_species = Slot(uri=AK_SCHEMA.V1p5CellProcessing_cell_species, name="V1p5CellProcessing_cell_species", curie=AK_SCHEMA.curie('V1p5CellProcessing_cell_species'),
                   model_uri=AK_SCHEMA.V1p5CellProcessing_cell_species, domain=None, range=Optional[Union[str, "V1p5CellSpecies"]])

slots.V1p5CellProcessing_single_cell = Slot(uri=AK_SCHEMA.V1p5CellProcessing_single_cell, name="V1p5CellProcessing_single_cell", curie=AK_SCHEMA.curie('V1p5CellProcessing_single_cell'),
                   model_uri=AK_SCHEMA.V1p5CellProcessing_single_cell, domain=None, range=Union[bool, Bool])

slots.V1p5CellProcessing_cell_number = Slot(uri=AK_SCHEMA.V1p5CellProcessing_cell_number, name="V1p5CellProcessing_cell_number", curie=AK_SCHEMA.curie('V1p5CellProcessing_cell_number'),
                   model_uri=AK_SCHEMA.V1p5CellProcessing_cell_number, domain=None, range=int)

slots.V1p5CellProcessing_cells_per_reaction = Slot(uri=AK_SCHEMA.V1p5CellProcessing_cells_per_reaction, name="V1p5CellProcessing_cells_per_reaction", curie=AK_SCHEMA.curie('V1p5CellProcessing_cells_per_reaction'),
                   model_uri=AK_SCHEMA.V1p5CellProcessing_cells_per_reaction, domain=None, range=int)

slots.V1p5CellProcessing_cell_storage = Slot(uri=AK_SCHEMA.V1p5CellProcessing_cell_storage, name="V1p5CellProcessing_cell_storage", curie=AK_SCHEMA.curie('V1p5CellProcessing_cell_storage'),
                   model_uri=AK_SCHEMA.V1p5CellProcessing_cell_storage, domain=None, range=Union[bool, Bool])

slots.V1p5CellProcessing_cell_quality = Slot(uri=AK_SCHEMA.V1p5CellProcessing_cell_quality, name="V1p5CellProcessing_cell_quality", curie=AK_SCHEMA.curie('V1p5CellProcessing_cell_quality'),
                   model_uri=AK_SCHEMA.V1p5CellProcessing_cell_quality, domain=None, range=str)

slots.V1p5CellProcessing_cell_isolation = Slot(uri=AK_SCHEMA.V1p5CellProcessing_cell_isolation, name="V1p5CellProcessing_cell_isolation", curie=AK_SCHEMA.curie('V1p5CellProcessing_cell_isolation'),
                   model_uri=AK_SCHEMA.V1p5CellProcessing_cell_isolation, domain=None, range=str)

slots.V1p5CellProcessing_cell_processing_protocol = Slot(uri=AK_SCHEMA.V1p5CellProcessing_cell_processing_protocol, name="V1p5CellProcessing_cell_processing_protocol", curie=AK_SCHEMA.curie('V1p5CellProcessing_cell_processing_protocol'),
                   model_uri=AK_SCHEMA.V1p5CellProcessing_cell_processing_protocol, domain=None, range=str)

slots.V1p5PCRTarget_pcr_target_locus = Slot(uri=AK_SCHEMA.V1p5PCRTarget_pcr_target_locus, name="V1p5PCRTarget_pcr_target_locus", curie=AK_SCHEMA.curie('V1p5PCRTarget_pcr_target_locus'),
                   model_uri=AK_SCHEMA.V1p5PCRTarget_pcr_target_locus, domain=None, range=Union[str, "V1p5PcrTargetLocus"])

slots.V1p5PCRTarget_forward_pcr_primer_target_location = Slot(uri=AK_SCHEMA.V1p5PCRTarget_forward_pcr_primer_target_location, name="V1p5PCRTarget_forward_pcr_primer_target_location", curie=AK_SCHEMA.curie('V1p5PCRTarget_forward_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.V1p5PCRTarget_forward_pcr_primer_target_location, domain=None, range=str)

slots.V1p5PCRTarget_reverse_pcr_primer_target_location = Slot(uri=AK_SCHEMA.V1p5PCRTarget_reverse_pcr_primer_target_location, name="V1p5PCRTarget_reverse_pcr_primer_target_location", curie=AK_SCHEMA.curie('V1p5PCRTarget_reverse_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.V1p5PCRTarget_reverse_pcr_primer_target_location, domain=None, range=str)

slots.V1p5NucleicAcidProcessing_template_class = Slot(uri=AK_SCHEMA.V1p5NucleicAcidProcessing_template_class, name="V1p5NucleicAcidProcessing_template_class", curie=AK_SCHEMA.curie('V1p5NucleicAcidProcessing_template_class'),
                   model_uri=AK_SCHEMA.V1p5NucleicAcidProcessing_template_class, domain=None, range=Union[str, "V1p5TemplateClass"])

slots.V1p5NucleicAcidProcessing_template_quality = Slot(uri=AK_SCHEMA.V1p5NucleicAcidProcessing_template_quality, name="V1p5NucleicAcidProcessing_template_quality", curie=AK_SCHEMA.curie('V1p5NucleicAcidProcessing_template_quality'),
                   model_uri=AK_SCHEMA.V1p5NucleicAcidProcessing_template_quality, domain=None, range=str)

slots.V1p5NucleicAcidProcessing_template_amount = Slot(uri=AK_SCHEMA.V1p5NucleicAcidProcessing_template_amount, name="V1p5NucleicAcidProcessing_template_amount", curie=AK_SCHEMA.curie('V1p5NucleicAcidProcessing_template_amount'),
                   model_uri=AK_SCHEMA.V1p5NucleicAcidProcessing_template_amount, domain=None, range=float)

slots.V1p5NucleicAcidProcessing_template_amount_unit = Slot(uri=AK_SCHEMA.V1p5NucleicAcidProcessing_template_amount_unit, name="V1p5NucleicAcidProcessing_template_amount_unit", curie=AK_SCHEMA.curie('V1p5NucleicAcidProcessing_template_amount_unit'),
                   model_uri=AK_SCHEMA.V1p5NucleicAcidProcessing_template_amount_unit, domain=None, range=Union[str, "V1p5TemplateAmountUnit"])

slots.V1p5NucleicAcidProcessing_library_generation_method = Slot(uri=AK_SCHEMA.V1p5NucleicAcidProcessing_library_generation_method, name="V1p5NucleicAcidProcessing_library_generation_method", curie=AK_SCHEMA.curie('V1p5NucleicAcidProcessing_library_generation_method'),
                   model_uri=AK_SCHEMA.V1p5NucleicAcidProcessing_library_generation_method, domain=None, range=Union[str, "V1p5LibraryGenerationMethod"])

slots.V1p5NucleicAcidProcessing_library_generation_protocol = Slot(uri=AK_SCHEMA.V1p5NucleicAcidProcessing_library_generation_protocol, name="V1p5NucleicAcidProcessing_library_generation_protocol", curie=AK_SCHEMA.curie('V1p5NucleicAcidProcessing_library_generation_protocol'),
                   model_uri=AK_SCHEMA.V1p5NucleicAcidProcessing_library_generation_protocol, domain=None, range=str)

slots.V1p5NucleicAcidProcessing_library_generation_kit_version = Slot(uri=AK_SCHEMA.V1p5NucleicAcidProcessing_library_generation_kit_version, name="V1p5NucleicAcidProcessing_library_generation_kit_version", curie=AK_SCHEMA.curie('V1p5NucleicAcidProcessing_library_generation_kit_version'),
                   model_uri=AK_SCHEMA.V1p5NucleicAcidProcessing_library_generation_kit_version, domain=None, range=str)

slots.V1p5NucleicAcidProcessing_pcr_target = Slot(uri=AK_SCHEMA.V1p5NucleicAcidProcessing_pcr_target, name="V1p5NucleicAcidProcessing_pcr_target", curie=AK_SCHEMA.curie('V1p5NucleicAcidProcessing_pcr_target'),
                   model_uri=AK_SCHEMA.V1p5NucleicAcidProcessing_pcr_target, domain=None, range=Optional[Union[Union[dict, V1p5PCRTarget], List[Union[dict, V1p5PCRTarget]]]])

slots.V1p5NucleicAcidProcessing_complete_sequences = Slot(uri=AK_SCHEMA.V1p5NucleicAcidProcessing_complete_sequences, name="V1p5NucleicAcidProcessing_complete_sequences", curie=AK_SCHEMA.curie('V1p5NucleicAcidProcessing_complete_sequences'),
                   model_uri=AK_SCHEMA.V1p5NucleicAcidProcessing_complete_sequences, domain=None, range=Union[str, "V1p5CompleteSequences"])

slots.V1p5NucleicAcidProcessing_physical_linkage = Slot(uri=AK_SCHEMA.V1p5NucleicAcidProcessing_physical_linkage, name="V1p5NucleicAcidProcessing_physical_linkage", curie=AK_SCHEMA.curie('V1p5NucleicAcidProcessing_physical_linkage'),
                   model_uri=AK_SCHEMA.V1p5NucleicAcidProcessing_physical_linkage, domain=None, range=Union[str, "V1p5PhysicalLinkage"])

slots.V1p5SequencingRun_sequencing_run_id = Slot(uri=AK_SCHEMA.V1p5SequencingRun_sequencing_run_id, name="V1p5SequencingRun_sequencing_run_id", curie=AK_SCHEMA.curie('V1p5SequencingRun_sequencing_run_id'),
                   model_uri=AK_SCHEMA.V1p5SequencingRun_sequencing_run_id, domain=None, range=str)

slots.V1p5SequencingRun_total_reads_passing_qc_filter = Slot(uri=AK_SCHEMA.V1p5SequencingRun_total_reads_passing_qc_filter, name="V1p5SequencingRun_total_reads_passing_qc_filter", curie=AK_SCHEMA.curie('V1p5SequencingRun_total_reads_passing_qc_filter'),
                   model_uri=AK_SCHEMA.V1p5SequencingRun_total_reads_passing_qc_filter, domain=None, range=int)

slots.V1p5SequencingRun_sequencing_platform = Slot(uri=AK_SCHEMA.V1p5SequencingRun_sequencing_platform, name="V1p5SequencingRun_sequencing_platform", curie=AK_SCHEMA.curie('V1p5SequencingRun_sequencing_platform'),
                   model_uri=AK_SCHEMA.V1p5SequencingRun_sequencing_platform, domain=None, range=str)

slots.V1p5SequencingRun_sequencing_facility = Slot(uri=AK_SCHEMA.V1p5SequencingRun_sequencing_facility, name="V1p5SequencingRun_sequencing_facility", curie=AK_SCHEMA.curie('V1p5SequencingRun_sequencing_facility'),
                   model_uri=AK_SCHEMA.V1p5SequencingRun_sequencing_facility, domain=None, range=str)

slots.V1p5SequencingRun_sequencing_run_date = Slot(uri=AK_SCHEMA.V1p5SequencingRun_sequencing_run_date, name="V1p5SequencingRun_sequencing_run_date", curie=AK_SCHEMA.curie('V1p5SequencingRun_sequencing_run_date'),
                   model_uri=AK_SCHEMA.V1p5SequencingRun_sequencing_run_date, domain=None, range=str)

slots.V1p5SequencingRun_sequencing_kit = Slot(uri=AK_SCHEMA.V1p5SequencingRun_sequencing_kit, name="V1p5SequencingRun_sequencing_kit", curie=AK_SCHEMA.curie('V1p5SequencingRun_sequencing_kit'),
                   model_uri=AK_SCHEMA.V1p5SequencingRun_sequencing_kit, domain=None, range=str)

slots.V1p5SequencingRun_sequencing_files = Slot(uri=AK_SCHEMA.V1p5SequencingRun_sequencing_files, name="V1p5SequencingRun_sequencing_files", curie=AK_SCHEMA.curie('V1p5SequencingRun_sequencing_files'),
                   model_uri=AK_SCHEMA.V1p5SequencingRun_sequencing_files, domain=None, range=Optional[Union[dict, V1p5SequencingData]])

slots.V1p5SequencingData_sequencing_data_id = Slot(uri=AK_SCHEMA.V1p5SequencingData_sequencing_data_id, name="V1p5SequencingData_sequencing_data_id", curie=AK_SCHEMA.curie('V1p5SequencingData_sequencing_data_id'),
                   model_uri=AK_SCHEMA.V1p5SequencingData_sequencing_data_id, domain=None, range=str)

slots.V1p5SequencingData_file_type = Slot(uri=AK_SCHEMA.V1p5SequencingData_file_type, name="V1p5SequencingData_file_type", curie=AK_SCHEMA.curie('V1p5SequencingData_file_type'),
                   model_uri=AK_SCHEMA.V1p5SequencingData_file_type, domain=None, range=Union[str, "V1p5FileType"])

slots.V1p5SequencingData_filename = Slot(uri=AK_SCHEMA.V1p5SequencingData_filename, name="V1p5SequencingData_filename", curie=AK_SCHEMA.curie('V1p5SequencingData_filename'),
                   model_uri=AK_SCHEMA.V1p5SequencingData_filename, domain=None, range=str)

slots.V1p5SequencingData_read_direction = Slot(uri=AK_SCHEMA.V1p5SequencingData_read_direction, name="V1p5SequencingData_read_direction", curie=AK_SCHEMA.curie('V1p5SequencingData_read_direction'),
                   model_uri=AK_SCHEMA.V1p5SequencingData_read_direction, domain=None, range=Union[str, "V1p5ReadDirection"])

slots.V1p5SequencingData_read_length = Slot(uri=AK_SCHEMA.V1p5SequencingData_read_length, name="V1p5SequencingData_read_length", curie=AK_SCHEMA.curie('V1p5SequencingData_read_length'),
                   model_uri=AK_SCHEMA.V1p5SequencingData_read_length, domain=None, range=int)

slots.V1p5SequencingData_paired_filename = Slot(uri=AK_SCHEMA.V1p5SequencingData_paired_filename, name="V1p5SequencingData_paired_filename", curie=AK_SCHEMA.curie('V1p5SequencingData_paired_filename'),
                   model_uri=AK_SCHEMA.V1p5SequencingData_paired_filename, domain=None, range=str)

slots.V1p5SequencingData_paired_read_direction = Slot(uri=AK_SCHEMA.V1p5SequencingData_paired_read_direction, name="V1p5SequencingData_paired_read_direction", curie=AK_SCHEMA.curie('V1p5SequencingData_paired_read_direction'),
                   model_uri=AK_SCHEMA.V1p5SequencingData_paired_read_direction, domain=None, range=Union[str, "V1p5PairedReadDirection"])

slots.V1p5SequencingData_paired_read_length = Slot(uri=AK_SCHEMA.V1p5SequencingData_paired_read_length, name="V1p5SequencingData_paired_read_length", curie=AK_SCHEMA.curie('V1p5SequencingData_paired_read_length'),
                   model_uri=AK_SCHEMA.V1p5SequencingData_paired_read_length, domain=None, range=int)

slots.V1p5SequencingData_index_filename = Slot(uri=AK_SCHEMA.V1p5SequencingData_index_filename, name="V1p5SequencingData_index_filename", curie=AK_SCHEMA.curie('V1p5SequencingData_index_filename'),
                   model_uri=AK_SCHEMA.V1p5SequencingData_index_filename, domain=None, range=Optional[str])

slots.V1p5SequencingData_index_length = Slot(uri=AK_SCHEMA.V1p5SequencingData_index_length, name="V1p5SequencingData_index_length", curie=AK_SCHEMA.curie('V1p5SequencingData_index_length'),
                   model_uri=AK_SCHEMA.V1p5SequencingData_index_length, domain=None, range=Optional[int])

slots.V1p5DataProcessing_data_processing_id = Slot(uri=AK_SCHEMA.V1p5DataProcessing_data_processing_id, name="V1p5DataProcessing_data_processing_id", curie=AK_SCHEMA.curie('V1p5DataProcessing_data_processing_id'),
                   model_uri=AK_SCHEMA.V1p5DataProcessing_data_processing_id, domain=None, range=Optional[str])

slots.V1p5DataProcessing_primary_annotation = Slot(uri=AK_SCHEMA.V1p5DataProcessing_primary_annotation, name="V1p5DataProcessing_primary_annotation", curie=AK_SCHEMA.curie('V1p5DataProcessing_primary_annotation'),
                   model_uri=AK_SCHEMA.V1p5DataProcessing_primary_annotation, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5DataProcessing_software_versions = Slot(uri=AK_SCHEMA.V1p5DataProcessing_software_versions, name="V1p5DataProcessing_software_versions", curie=AK_SCHEMA.curie('V1p5DataProcessing_software_versions'),
                   model_uri=AK_SCHEMA.V1p5DataProcessing_software_versions, domain=None, range=str)

slots.V1p5DataProcessing_paired_reads_assembly = Slot(uri=AK_SCHEMA.V1p5DataProcessing_paired_reads_assembly, name="V1p5DataProcessing_paired_reads_assembly", curie=AK_SCHEMA.curie('V1p5DataProcessing_paired_reads_assembly'),
                   model_uri=AK_SCHEMA.V1p5DataProcessing_paired_reads_assembly, domain=None, range=str)

slots.V1p5DataProcessing_quality_thresholds = Slot(uri=AK_SCHEMA.V1p5DataProcessing_quality_thresholds, name="V1p5DataProcessing_quality_thresholds", curie=AK_SCHEMA.curie('V1p5DataProcessing_quality_thresholds'),
                   model_uri=AK_SCHEMA.V1p5DataProcessing_quality_thresholds, domain=None, range=str)

slots.V1p5DataProcessing_primer_match_cutoffs = Slot(uri=AK_SCHEMA.V1p5DataProcessing_primer_match_cutoffs, name="V1p5DataProcessing_primer_match_cutoffs", curie=AK_SCHEMA.curie('V1p5DataProcessing_primer_match_cutoffs'),
                   model_uri=AK_SCHEMA.V1p5DataProcessing_primer_match_cutoffs, domain=None, range=str)

slots.V1p5DataProcessing_collapsing_method = Slot(uri=AK_SCHEMA.V1p5DataProcessing_collapsing_method, name="V1p5DataProcessing_collapsing_method", curie=AK_SCHEMA.curie('V1p5DataProcessing_collapsing_method'),
                   model_uri=AK_SCHEMA.V1p5DataProcessing_collapsing_method, domain=None, range=str)

slots.V1p5DataProcessing_data_processing_protocols = Slot(uri=AK_SCHEMA.V1p5DataProcessing_data_processing_protocols, name="V1p5DataProcessing_data_processing_protocols", curie=AK_SCHEMA.curie('V1p5DataProcessing_data_processing_protocols'),
                   model_uri=AK_SCHEMA.V1p5DataProcessing_data_processing_protocols, domain=None, range=str)

slots.V1p5DataProcessing_data_processing_files = Slot(uri=AK_SCHEMA.V1p5DataProcessing_data_processing_files, name="V1p5DataProcessing_data_processing_files", curie=AK_SCHEMA.curie('V1p5DataProcessing_data_processing_files'),
                   model_uri=AK_SCHEMA.V1p5DataProcessing_data_processing_files, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p5DataProcessing_germline_database = Slot(uri=AK_SCHEMA.V1p5DataProcessing_germline_database, name="V1p5DataProcessing_germline_database", curie=AK_SCHEMA.curie('V1p5DataProcessing_germline_database'),
                   model_uri=AK_SCHEMA.V1p5DataProcessing_germline_database, domain=None, range=str)

slots.V1p5DataProcessing_germline_set_ref = Slot(uri=AK_SCHEMA.V1p5DataProcessing_germline_set_ref, name="V1p5DataProcessing_germline_set_ref", curie=AK_SCHEMA.curie('V1p5DataProcessing_germline_set_ref'),
                   model_uri=AK_SCHEMA.V1p5DataProcessing_germline_set_ref, domain=None, range=Optional[str])

slots.V1p5DataProcessing_analysis_provenance_id = Slot(uri=AK_SCHEMA.V1p5DataProcessing_analysis_provenance_id, name="V1p5DataProcessing_analysis_provenance_id", curie=AK_SCHEMA.curie('V1p5DataProcessing_analysis_provenance_id'),
                   model_uri=AK_SCHEMA.V1p5DataProcessing_analysis_provenance_id, domain=None, range=Optional[str])

slots.V1p5Repertoire_repertoire_id = Slot(uri=AK_SCHEMA.V1p5Repertoire_repertoire_id, name="V1p5Repertoire_repertoire_id", curie=AK_SCHEMA.curie('V1p5Repertoire_repertoire_id'),
                   model_uri=AK_SCHEMA.V1p5Repertoire_repertoire_id, domain=None, range=Optional[str])

slots.V1p5Repertoire_repertoire_name = Slot(uri=AK_SCHEMA.V1p5Repertoire_repertoire_name, name="V1p5Repertoire_repertoire_name", curie=AK_SCHEMA.curie('V1p5Repertoire_repertoire_name'),
                   model_uri=AK_SCHEMA.V1p5Repertoire_repertoire_name, domain=None, range=Optional[str])

slots.V1p5Repertoire_repertoire_description = Slot(uri=AK_SCHEMA.V1p5Repertoire_repertoire_description, name="V1p5Repertoire_repertoire_description", curie=AK_SCHEMA.curie('V1p5Repertoire_repertoire_description'),
                   model_uri=AK_SCHEMA.V1p5Repertoire_repertoire_description, domain=None, range=Optional[str])

slots.V1p5Repertoire_study = Slot(uri=AK_SCHEMA.V1p5Repertoire_study, name="V1p5Repertoire_study", curie=AK_SCHEMA.curie('V1p5Repertoire_study'),
                   model_uri=AK_SCHEMA.V1p5Repertoire_study, domain=None, range=Union[dict, V1p5Study])

slots.V1p5Repertoire_subject = Slot(uri=AK_SCHEMA.V1p5Repertoire_subject, name="V1p5Repertoire_subject", curie=AK_SCHEMA.curie('V1p5Repertoire_subject'),
                   model_uri=AK_SCHEMA.V1p5Repertoire_subject, domain=None, range=Union[dict, V1p5Subject])

slots.V1p5Repertoire_sample = Slot(uri=AK_SCHEMA.V1p5Repertoire_sample, name="V1p5Repertoire_sample", curie=AK_SCHEMA.curie('V1p5Repertoire_sample'),
                   model_uri=AK_SCHEMA.V1p5Repertoire_sample, domain=None, range=Union[Union[dict, V1p5SampleProcessing], List[Union[dict, V1p5SampleProcessing]]])

slots.V1p5Repertoire_data_processing = Slot(uri=AK_SCHEMA.V1p5Repertoire_data_processing, name="V1p5Repertoire_data_processing", curie=AK_SCHEMA.curie('V1p5Repertoire_data_processing'),
                   model_uri=AK_SCHEMA.V1p5Repertoire_data_processing, domain=None, range=Union[Union[dict, V1p5DataProcessing], List[Union[dict, V1p5DataProcessing]]])

slots.V1p5RepertoireGroupDetail_repertoire_id = Slot(uri=AK_SCHEMA.V1p5RepertoireGroupDetail_repertoire_id, name="V1p5RepertoireGroupDetail_repertoire_id", curie=AK_SCHEMA.curie('V1p5RepertoireGroupDetail_repertoire_id'),
                   model_uri=AK_SCHEMA.V1p5RepertoireGroupDetail_repertoire_id, domain=None, range=Optional[str])

slots.V1p5RepertoireGroupDetail_repertoire_description = Slot(uri=AK_SCHEMA.V1p5RepertoireGroupDetail_repertoire_description, name="V1p5RepertoireGroupDetail_repertoire_description", curie=AK_SCHEMA.curie('V1p5RepertoireGroupDetail_repertoire_description'),
                   model_uri=AK_SCHEMA.V1p5RepertoireGroupDetail_repertoire_description, domain=None, range=Optional[str])

slots.V1p5RepertoireGroupDetail_time_point = Slot(uri=AK_SCHEMA.V1p5RepertoireGroupDetail_time_point, name="V1p5RepertoireGroupDetail_time_point", curie=AK_SCHEMA.curie('V1p5RepertoireGroupDetail_time_point'),
                   model_uri=AK_SCHEMA.V1p5RepertoireGroupDetail_time_point, domain=None, range=Optional[Union[dict, V1p5TimePoint]])

slots.V1p5RepertoireGroup_repertoire_group_id = Slot(uri=AK_SCHEMA.V1p5RepertoireGroup_repertoire_group_id, name="V1p5RepertoireGroup_repertoire_group_id", curie=AK_SCHEMA.curie('V1p5RepertoireGroup_repertoire_group_id'),
                   model_uri=AK_SCHEMA.V1p5RepertoireGroup_repertoire_group_id, domain=None, range=str)

slots.V1p5RepertoireGroup_repertoire_group_name = Slot(uri=AK_SCHEMA.V1p5RepertoireGroup_repertoire_group_name, name="V1p5RepertoireGroup_repertoire_group_name", curie=AK_SCHEMA.curie('V1p5RepertoireGroup_repertoire_group_name'),
                   model_uri=AK_SCHEMA.V1p5RepertoireGroup_repertoire_group_name, domain=None, range=Optional[str])

slots.V1p5RepertoireGroup_repertoire_group_description = Slot(uri=AK_SCHEMA.V1p5RepertoireGroup_repertoire_group_description, name="V1p5RepertoireGroup_repertoire_group_description", curie=AK_SCHEMA.curie('V1p5RepertoireGroup_repertoire_group_description'),
                   model_uri=AK_SCHEMA.V1p5RepertoireGroup_repertoire_group_description, domain=None, range=Optional[str])

slots.V1p5RepertoireGroup_repertoires = Slot(uri=AK_SCHEMA.V1p5RepertoireGroup_repertoires, name="V1p5RepertoireGroup_repertoires", curie=AK_SCHEMA.curie('V1p5RepertoireGroup_repertoires'),
                   model_uri=AK_SCHEMA.V1p5RepertoireGroup_repertoires, domain=None, range=Union[Union[dict, V1p5RepertoireGroupDetail], List[Union[dict, V1p5RepertoireGroupDetail]]])

slots.V1p5Alignment_sequence_id = Slot(uri=AK_SCHEMA.V1p5Alignment_sequence_id, name="V1p5Alignment_sequence_id", curie=AK_SCHEMA.curie('V1p5Alignment_sequence_id'),
                   model_uri=AK_SCHEMA.V1p5Alignment_sequence_id, domain=None, range=str)

slots.V1p5Alignment_segment = Slot(uri=AK_SCHEMA.V1p5Alignment_segment, name="V1p5Alignment_segment", curie=AK_SCHEMA.curie('V1p5Alignment_segment'),
                   model_uri=AK_SCHEMA.V1p5Alignment_segment, domain=None, range=str)

slots.V1p5Alignment_rev_comp = Slot(uri=AK_SCHEMA.V1p5Alignment_rev_comp, name="V1p5Alignment_rev_comp", curie=AK_SCHEMA.curie('V1p5Alignment_rev_comp'),
                   model_uri=AK_SCHEMA.V1p5Alignment_rev_comp, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5Alignment_call = Slot(uri=AK_SCHEMA.V1p5Alignment_call, name="V1p5Alignment_call", curie=AK_SCHEMA.curie('V1p5Alignment_call'),
                   model_uri=AK_SCHEMA.V1p5Alignment_call, domain=None, range=str)

slots.V1p5Alignment_score = Slot(uri=AK_SCHEMA.V1p5Alignment_score, name="V1p5Alignment_score", curie=AK_SCHEMA.curie('V1p5Alignment_score'),
                   model_uri=AK_SCHEMA.V1p5Alignment_score, domain=None, range=float)

slots.V1p5Alignment_identity = Slot(uri=AK_SCHEMA.V1p5Alignment_identity, name="V1p5Alignment_identity", curie=AK_SCHEMA.curie('V1p5Alignment_identity'),
                   model_uri=AK_SCHEMA.V1p5Alignment_identity, domain=None, range=Optional[float])

slots.V1p5Alignment_support = Slot(uri=AK_SCHEMA.V1p5Alignment_support, name="V1p5Alignment_support", curie=AK_SCHEMA.curie('V1p5Alignment_support'),
                   model_uri=AK_SCHEMA.V1p5Alignment_support, domain=None, range=Optional[float])

slots.V1p5Alignment_cigar = Slot(uri=AK_SCHEMA.V1p5Alignment_cigar, name="V1p5Alignment_cigar", curie=AK_SCHEMA.curie('V1p5Alignment_cigar'),
                   model_uri=AK_SCHEMA.V1p5Alignment_cigar, domain=None, range=str)

slots.V1p5Alignment_sequence_start = Slot(uri=AK_SCHEMA.V1p5Alignment_sequence_start, name="V1p5Alignment_sequence_start", curie=AK_SCHEMA.curie('V1p5Alignment_sequence_start'),
                   model_uri=AK_SCHEMA.V1p5Alignment_sequence_start, domain=None, range=Optional[int])

slots.V1p5Alignment_sequence_end = Slot(uri=AK_SCHEMA.V1p5Alignment_sequence_end, name="V1p5Alignment_sequence_end", curie=AK_SCHEMA.curie('V1p5Alignment_sequence_end'),
                   model_uri=AK_SCHEMA.V1p5Alignment_sequence_end, domain=None, range=Optional[int])

slots.V1p5Alignment_germline_start = Slot(uri=AK_SCHEMA.V1p5Alignment_germline_start, name="V1p5Alignment_germline_start", curie=AK_SCHEMA.curie('V1p5Alignment_germline_start'),
                   model_uri=AK_SCHEMA.V1p5Alignment_germline_start, domain=None, range=Optional[int])

slots.V1p5Alignment_germline_end = Slot(uri=AK_SCHEMA.V1p5Alignment_germline_end, name="V1p5Alignment_germline_end", curie=AK_SCHEMA.curie('V1p5Alignment_germline_end'),
                   model_uri=AK_SCHEMA.V1p5Alignment_germline_end, domain=None, range=Optional[int])

slots.V1p5Alignment_rank = Slot(uri=AK_SCHEMA.V1p5Alignment_rank, name="V1p5Alignment_rank", curie=AK_SCHEMA.curie('V1p5Alignment_rank'),
                   model_uri=AK_SCHEMA.V1p5Alignment_rank, domain=None, range=Optional[int])

slots.V1p5Alignment_data_processing_id = Slot(uri=AK_SCHEMA.V1p5Alignment_data_processing_id, name="V1p5Alignment_data_processing_id", curie=AK_SCHEMA.curie('V1p5Alignment_data_processing_id'),
                   model_uri=AK_SCHEMA.V1p5Alignment_data_processing_id, domain=None, range=Optional[str])

slots.V1p5Rearrangement_sequence_id = Slot(uri=AK_SCHEMA.V1p5Rearrangement_sequence_id, name="V1p5Rearrangement_sequence_id", curie=AK_SCHEMA.curie('V1p5Rearrangement_sequence_id'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_sequence_id, domain=None, range=str)

slots.V1p5Rearrangement_sequence = Slot(uri=AK_SCHEMA.V1p5Rearrangement_sequence, name="V1p5Rearrangement_sequence", curie=AK_SCHEMA.curie('V1p5Rearrangement_sequence'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_sequence, domain=None, range=str)

slots.V1p5Rearrangement_quality = Slot(uri=AK_SCHEMA.V1p5Rearrangement_quality, name="V1p5Rearrangement_quality", curie=AK_SCHEMA.curie('V1p5Rearrangement_quality'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_quality, domain=None, range=Optional[str])

slots.V1p5Rearrangement_sequence_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_sequence_aa, name="V1p5Rearrangement_sequence_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_sequence_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_sequence_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_rev_comp = Slot(uri=AK_SCHEMA.V1p5Rearrangement_rev_comp, name="V1p5Rearrangement_rev_comp", curie=AK_SCHEMA.curie('V1p5Rearrangement_rev_comp'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_rev_comp, domain=None, range=Union[bool, Bool])

slots.V1p5Rearrangement_productive = Slot(uri=AK_SCHEMA.V1p5Rearrangement_productive, name="V1p5Rearrangement_productive", curie=AK_SCHEMA.curie('V1p5Rearrangement_productive'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_productive, domain=None, range=Union[bool, Bool])

slots.V1p5Rearrangement_vj_in_frame = Slot(uri=AK_SCHEMA.V1p5Rearrangement_vj_in_frame, name="V1p5Rearrangement_vj_in_frame", curie=AK_SCHEMA.curie('V1p5Rearrangement_vj_in_frame'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_vj_in_frame, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5Rearrangement_stop_codon = Slot(uri=AK_SCHEMA.V1p5Rearrangement_stop_codon, name="V1p5Rearrangement_stop_codon", curie=AK_SCHEMA.curie('V1p5Rearrangement_stop_codon'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_stop_codon, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5Rearrangement_complete_vdj = Slot(uri=AK_SCHEMA.V1p5Rearrangement_complete_vdj, name="V1p5Rearrangement_complete_vdj", curie=AK_SCHEMA.curie('V1p5Rearrangement_complete_vdj'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_complete_vdj, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5Rearrangement_locus = Slot(uri=AK_SCHEMA.V1p5Rearrangement_locus, name="V1p5Rearrangement_locus", curie=AK_SCHEMA.curie('V1p5Rearrangement_locus'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_locus, domain=None, range=Optional[Union[str, "V1p5Locus"]])

slots.V1p5Rearrangement_v_call = Slot(uri=AK_SCHEMA.V1p5Rearrangement_v_call, name="V1p5Rearrangement_v_call", curie=AK_SCHEMA.curie('V1p5Rearrangement_v_call'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_v_call, domain=None, range=str)

slots.V1p5Rearrangement_d_call = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d_call, name="V1p5Rearrangement_d_call", curie=AK_SCHEMA.curie('V1p5Rearrangement_d_call'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d_call, domain=None, range=str)

slots.V1p5Rearrangement_d2_call = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d2_call, name="V1p5Rearrangement_d2_call", curie=AK_SCHEMA.curie('V1p5Rearrangement_d2_call'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d2_call, domain=None, range=Optional[str])

slots.V1p5Rearrangement_j_call = Slot(uri=AK_SCHEMA.V1p5Rearrangement_j_call, name="V1p5Rearrangement_j_call", curie=AK_SCHEMA.curie('V1p5Rearrangement_j_call'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_j_call, domain=None, range=str)

slots.V1p5Rearrangement_c_call = Slot(uri=AK_SCHEMA.V1p5Rearrangement_c_call, name="V1p5Rearrangement_c_call", curie=AK_SCHEMA.curie('V1p5Rearrangement_c_call'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_c_call, domain=None, range=Optional[str])

slots.V1p5Rearrangement_sequence_alignment = Slot(uri=AK_SCHEMA.V1p5Rearrangement_sequence_alignment, name="V1p5Rearrangement_sequence_alignment", curie=AK_SCHEMA.curie('V1p5Rearrangement_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_sequence_alignment, domain=None, range=str)

slots.V1p5Rearrangement_quality_alignment = Slot(uri=AK_SCHEMA.V1p5Rearrangement_quality_alignment, name="V1p5Rearrangement_quality_alignment", curie=AK_SCHEMA.curie('V1p5Rearrangement_quality_alignment'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_quality_alignment, domain=None, range=Optional[str])

slots.V1p5Rearrangement_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_sequence_alignment_aa, name="V1p5Rearrangement_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_germline_alignment = Slot(uri=AK_SCHEMA.V1p5Rearrangement_germline_alignment, name="V1p5Rearrangement_germline_alignment", curie=AK_SCHEMA.curie('V1p5Rearrangement_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_germline_alignment, domain=None, range=str)

slots.V1p5Rearrangement_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_germline_alignment_aa, name="V1p5Rearrangement_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_junction = Slot(uri=AK_SCHEMA.V1p5Rearrangement_junction, name="V1p5Rearrangement_junction", curie=AK_SCHEMA.curie('V1p5Rearrangement_junction'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_junction, domain=None, range=str)

slots.V1p5Rearrangement_junction_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_junction_aa, name="V1p5Rearrangement_junction_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_junction_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_junction_aa, domain=None, range=str)

slots.V1p5Rearrangement_np1 = Slot(uri=AK_SCHEMA.V1p5Rearrangement_np1, name="V1p5Rearrangement_np1", curie=AK_SCHEMA.curie('V1p5Rearrangement_np1'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_np1, domain=None, range=Optional[str])

slots.V1p5Rearrangement_np1_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_np1_aa, name="V1p5Rearrangement_np1_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_np1_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_np1_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_np2 = Slot(uri=AK_SCHEMA.V1p5Rearrangement_np2, name="V1p5Rearrangement_np2", curie=AK_SCHEMA.curie('V1p5Rearrangement_np2'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_np2, domain=None, range=Optional[str])

slots.V1p5Rearrangement_np2_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_np2_aa, name="V1p5Rearrangement_np2_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_np2_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_np2_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_np3 = Slot(uri=AK_SCHEMA.V1p5Rearrangement_np3, name="V1p5Rearrangement_np3", curie=AK_SCHEMA.curie('V1p5Rearrangement_np3'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_np3, domain=None, range=Optional[str])

slots.V1p5Rearrangement_np3_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_np3_aa, name="V1p5Rearrangement_np3_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_np3_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_np3_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_cdr1 = Slot(uri=AK_SCHEMA.V1p5Rearrangement_cdr1, name="V1p5Rearrangement_cdr1", curie=AK_SCHEMA.curie('V1p5Rearrangement_cdr1'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_cdr1, domain=None, range=Optional[str])

slots.V1p5Rearrangement_cdr1_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_cdr1_aa, name="V1p5Rearrangement_cdr1_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_cdr1_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_cdr1_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_cdr2 = Slot(uri=AK_SCHEMA.V1p5Rearrangement_cdr2, name="V1p5Rearrangement_cdr2", curie=AK_SCHEMA.curie('V1p5Rearrangement_cdr2'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_cdr2, domain=None, range=Optional[str])

slots.V1p5Rearrangement_cdr2_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_cdr2_aa, name="V1p5Rearrangement_cdr2_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_cdr2_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_cdr2_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_cdr3 = Slot(uri=AK_SCHEMA.V1p5Rearrangement_cdr3, name="V1p5Rearrangement_cdr3", curie=AK_SCHEMA.curie('V1p5Rearrangement_cdr3'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_cdr3, domain=None, range=Optional[str])

slots.V1p5Rearrangement_cdr3_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_cdr3_aa, name="V1p5Rearrangement_cdr3_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_cdr3_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_cdr3_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_fwr1 = Slot(uri=AK_SCHEMA.V1p5Rearrangement_fwr1, name="V1p5Rearrangement_fwr1", curie=AK_SCHEMA.curie('V1p5Rearrangement_fwr1'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_fwr1, domain=None, range=Optional[str])

slots.V1p5Rearrangement_fwr1_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_fwr1_aa, name="V1p5Rearrangement_fwr1_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_fwr1_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_fwr1_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_fwr2 = Slot(uri=AK_SCHEMA.V1p5Rearrangement_fwr2, name="V1p5Rearrangement_fwr2", curie=AK_SCHEMA.curie('V1p5Rearrangement_fwr2'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_fwr2, domain=None, range=Optional[str])

slots.V1p5Rearrangement_fwr2_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_fwr2_aa, name="V1p5Rearrangement_fwr2_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_fwr2_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_fwr2_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_fwr3 = Slot(uri=AK_SCHEMA.V1p5Rearrangement_fwr3, name="V1p5Rearrangement_fwr3", curie=AK_SCHEMA.curie('V1p5Rearrangement_fwr3'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_fwr3, domain=None, range=Optional[str])

slots.V1p5Rearrangement_fwr3_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_fwr3_aa, name="V1p5Rearrangement_fwr3_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_fwr3_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_fwr3_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_fwr4 = Slot(uri=AK_SCHEMA.V1p5Rearrangement_fwr4, name="V1p5Rearrangement_fwr4", curie=AK_SCHEMA.curie('V1p5Rearrangement_fwr4'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_fwr4, domain=None, range=Optional[str])

slots.V1p5Rearrangement_fwr4_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_fwr4_aa, name="V1p5Rearrangement_fwr4_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_fwr4_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_fwr4_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_v_score = Slot(uri=AK_SCHEMA.V1p5Rearrangement_v_score, name="V1p5Rearrangement_v_score", curie=AK_SCHEMA.curie('V1p5Rearrangement_v_score'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_v_score, domain=None, range=Optional[float])

slots.V1p5Rearrangement_v_identity = Slot(uri=AK_SCHEMA.V1p5Rearrangement_v_identity, name="V1p5Rearrangement_v_identity", curie=AK_SCHEMA.curie('V1p5Rearrangement_v_identity'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_v_identity, domain=None, range=Optional[float])

slots.V1p5Rearrangement_v_support = Slot(uri=AK_SCHEMA.V1p5Rearrangement_v_support, name="V1p5Rearrangement_v_support", curie=AK_SCHEMA.curie('V1p5Rearrangement_v_support'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_v_support, domain=None, range=Optional[float])

slots.V1p5Rearrangement_v_cigar = Slot(uri=AK_SCHEMA.V1p5Rearrangement_v_cigar, name="V1p5Rearrangement_v_cigar", curie=AK_SCHEMA.curie('V1p5Rearrangement_v_cigar'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_v_cigar, domain=None, range=str)

slots.V1p5Rearrangement_d_score = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d_score, name="V1p5Rearrangement_d_score", curie=AK_SCHEMA.curie('V1p5Rearrangement_d_score'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d_score, domain=None, range=Optional[float])

slots.V1p5Rearrangement_d_identity = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d_identity, name="V1p5Rearrangement_d_identity", curie=AK_SCHEMA.curie('V1p5Rearrangement_d_identity'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d_identity, domain=None, range=Optional[float])

slots.V1p5Rearrangement_d_support = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d_support, name="V1p5Rearrangement_d_support", curie=AK_SCHEMA.curie('V1p5Rearrangement_d_support'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d_support, domain=None, range=Optional[float])

slots.V1p5Rearrangement_d_cigar = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d_cigar, name="V1p5Rearrangement_d_cigar", curie=AK_SCHEMA.curie('V1p5Rearrangement_d_cigar'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d_cigar, domain=None, range=str)

slots.V1p5Rearrangement_d2_score = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d2_score, name="V1p5Rearrangement_d2_score", curie=AK_SCHEMA.curie('V1p5Rearrangement_d2_score'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d2_score, domain=None, range=Optional[float])

slots.V1p5Rearrangement_d2_identity = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d2_identity, name="V1p5Rearrangement_d2_identity", curie=AK_SCHEMA.curie('V1p5Rearrangement_d2_identity'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d2_identity, domain=None, range=Optional[float])

slots.V1p5Rearrangement_d2_support = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d2_support, name="V1p5Rearrangement_d2_support", curie=AK_SCHEMA.curie('V1p5Rearrangement_d2_support'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d2_support, domain=None, range=Optional[float])

slots.V1p5Rearrangement_d2_cigar = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d2_cigar, name="V1p5Rearrangement_d2_cigar", curie=AK_SCHEMA.curie('V1p5Rearrangement_d2_cigar'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d2_cigar, domain=None, range=Optional[str])

slots.V1p5Rearrangement_j_score = Slot(uri=AK_SCHEMA.V1p5Rearrangement_j_score, name="V1p5Rearrangement_j_score", curie=AK_SCHEMA.curie('V1p5Rearrangement_j_score'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_j_score, domain=None, range=Optional[float])

slots.V1p5Rearrangement_j_identity = Slot(uri=AK_SCHEMA.V1p5Rearrangement_j_identity, name="V1p5Rearrangement_j_identity", curie=AK_SCHEMA.curie('V1p5Rearrangement_j_identity'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_j_identity, domain=None, range=Optional[float])

slots.V1p5Rearrangement_j_support = Slot(uri=AK_SCHEMA.V1p5Rearrangement_j_support, name="V1p5Rearrangement_j_support", curie=AK_SCHEMA.curie('V1p5Rearrangement_j_support'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_j_support, domain=None, range=Optional[float])

slots.V1p5Rearrangement_j_cigar = Slot(uri=AK_SCHEMA.V1p5Rearrangement_j_cigar, name="V1p5Rearrangement_j_cigar", curie=AK_SCHEMA.curie('V1p5Rearrangement_j_cigar'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_j_cigar, domain=None, range=str)

slots.V1p5Rearrangement_c_score = Slot(uri=AK_SCHEMA.V1p5Rearrangement_c_score, name="V1p5Rearrangement_c_score", curie=AK_SCHEMA.curie('V1p5Rearrangement_c_score'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_c_score, domain=None, range=Optional[float])

slots.V1p5Rearrangement_c_identity = Slot(uri=AK_SCHEMA.V1p5Rearrangement_c_identity, name="V1p5Rearrangement_c_identity", curie=AK_SCHEMA.curie('V1p5Rearrangement_c_identity'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_c_identity, domain=None, range=Optional[float])

slots.V1p5Rearrangement_c_support = Slot(uri=AK_SCHEMA.V1p5Rearrangement_c_support, name="V1p5Rearrangement_c_support", curie=AK_SCHEMA.curie('V1p5Rearrangement_c_support'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_c_support, domain=None, range=Optional[float])

slots.V1p5Rearrangement_c_cigar = Slot(uri=AK_SCHEMA.V1p5Rearrangement_c_cigar, name="V1p5Rearrangement_c_cigar", curie=AK_SCHEMA.curie('V1p5Rearrangement_c_cigar'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_c_cigar, domain=None, range=Optional[str])

slots.V1p5Rearrangement_v_sequence_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_v_sequence_start, name="V1p5Rearrangement_v_sequence_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_v_sequence_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_v_sequence_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_v_sequence_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_v_sequence_end, name="V1p5Rearrangement_v_sequence_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_v_sequence_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_v_sequence_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_v_germline_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_v_germline_start, name="V1p5Rearrangement_v_germline_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_v_germline_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_v_germline_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_v_germline_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_v_germline_end, name="V1p5Rearrangement_v_germline_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_v_germline_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_v_germline_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_v_alignment_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_v_alignment_start, name="V1p5Rearrangement_v_alignment_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_v_alignment_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_v_alignment_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_v_alignment_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_v_alignment_end, name="V1p5Rearrangement_v_alignment_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_v_alignment_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_v_alignment_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_d_sequence_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d_sequence_start, name="V1p5Rearrangement_d_sequence_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_d_sequence_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d_sequence_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_d_sequence_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d_sequence_end, name="V1p5Rearrangement_d_sequence_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_d_sequence_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d_sequence_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_d_germline_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d_germline_start, name="V1p5Rearrangement_d_germline_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_d_germline_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d_germline_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_d_germline_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d_germline_end, name="V1p5Rearrangement_d_germline_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_d_germline_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d_germline_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_d_alignment_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d_alignment_start, name="V1p5Rearrangement_d_alignment_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_d_alignment_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d_alignment_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_d_alignment_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d_alignment_end, name="V1p5Rearrangement_d_alignment_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_d_alignment_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d_alignment_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_d2_sequence_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d2_sequence_start, name="V1p5Rearrangement_d2_sequence_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_d2_sequence_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d2_sequence_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_d2_sequence_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d2_sequence_end, name="V1p5Rearrangement_d2_sequence_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_d2_sequence_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d2_sequence_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_d2_germline_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d2_germline_start, name="V1p5Rearrangement_d2_germline_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_d2_germline_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d2_germline_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_d2_germline_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d2_germline_end, name="V1p5Rearrangement_d2_germline_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_d2_germline_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d2_germline_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_d2_alignment_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d2_alignment_start, name="V1p5Rearrangement_d2_alignment_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_d2_alignment_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d2_alignment_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_d2_alignment_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d2_alignment_end, name="V1p5Rearrangement_d2_alignment_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_d2_alignment_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d2_alignment_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_j_sequence_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_j_sequence_start, name="V1p5Rearrangement_j_sequence_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_j_sequence_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_j_sequence_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_j_sequence_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_j_sequence_end, name="V1p5Rearrangement_j_sequence_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_j_sequence_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_j_sequence_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_j_germline_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_j_germline_start, name="V1p5Rearrangement_j_germline_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_j_germline_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_j_germline_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_j_germline_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_j_germline_end, name="V1p5Rearrangement_j_germline_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_j_germline_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_j_germline_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_j_alignment_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_j_alignment_start, name="V1p5Rearrangement_j_alignment_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_j_alignment_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_j_alignment_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_j_alignment_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_j_alignment_end, name="V1p5Rearrangement_j_alignment_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_j_alignment_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_j_alignment_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_c_sequence_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_c_sequence_start, name="V1p5Rearrangement_c_sequence_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_c_sequence_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_c_sequence_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_c_sequence_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_c_sequence_end, name="V1p5Rearrangement_c_sequence_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_c_sequence_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_c_sequence_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_c_germline_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_c_germline_start, name="V1p5Rearrangement_c_germline_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_c_germline_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_c_germline_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_c_germline_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_c_germline_end, name="V1p5Rearrangement_c_germline_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_c_germline_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_c_germline_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_c_alignment_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_c_alignment_start, name="V1p5Rearrangement_c_alignment_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_c_alignment_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_c_alignment_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_c_alignment_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_c_alignment_end, name="V1p5Rearrangement_c_alignment_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_c_alignment_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_c_alignment_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_cdr1_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_cdr1_start, name="V1p5Rearrangement_cdr1_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_cdr1_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_cdr1_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_cdr1_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_cdr1_end, name="V1p5Rearrangement_cdr1_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_cdr1_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_cdr1_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_cdr2_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_cdr2_start, name="V1p5Rearrangement_cdr2_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_cdr2_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_cdr2_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_cdr2_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_cdr2_end, name="V1p5Rearrangement_cdr2_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_cdr2_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_cdr2_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_cdr3_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_cdr3_start, name="V1p5Rearrangement_cdr3_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_cdr3_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_cdr3_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_cdr3_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_cdr3_end, name="V1p5Rearrangement_cdr3_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_cdr3_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_cdr3_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_fwr1_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_fwr1_start, name="V1p5Rearrangement_fwr1_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_fwr1_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_fwr1_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_fwr1_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_fwr1_end, name="V1p5Rearrangement_fwr1_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_fwr1_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_fwr1_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_fwr2_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_fwr2_start, name="V1p5Rearrangement_fwr2_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_fwr2_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_fwr2_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_fwr2_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_fwr2_end, name="V1p5Rearrangement_fwr2_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_fwr2_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_fwr2_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_fwr3_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_fwr3_start, name="V1p5Rearrangement_fwr3_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_fwr3_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_fwr3_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_fwr3_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_fwr3_end, name="V1p5Rearrangement_fwr3_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_fwr3_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_fwr3_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_fwr4_start = Slot(uri=AK_SCHEMA.V1p5Rearrangement_fwr4_start, name="V1p5Rearrangement_fwr4_start", curie=AK_SCHEMA.curie('V1p5Rearrangement_fwr4_start'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_fwr4_start, domain=None, range=Optional[int])

slots.V1p5Rearrangement_fwr4_end = Slot(uri=AK_SCHEMA.V1p5Rearrangement_fwr4_end, name="V1p5Rearrangement_fwr4_end", curie=AK_SCHEMA.curie('V1p5Rearrangement_fwr4_end'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_fwr4_end, domain=None, range=Optional[int])

slots.V1p5Rearrangement_v_sequence_alignment = Slot(uri=AK_SCHEMA.V1p5Rearrangement_v_sequence_alignment, name="V1p5Rearrangement_v_sequence_alignment", curie=AK_SCHEMA.curie('V1p5Rearrangement_v_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_v_sequence_alignment, domain=None, range=Optional[str])

slots.V1p5Rearrangement_v_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_v_sequence_alignment_aa, name="V1p5Rearrangement_v_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_v_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_v_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_d_sequence_alignment = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d_sequence_alignment, name="V1p5Rearrangement_d_sequence_alignment", curie=AK_SCHEMA.curie('V1p5Rearrangement_d_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d_sequence_alignment, domain=None, range=Optional[str])

slots.V1p5Rearrangement_d_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d_sequence_alignment_aa, name="V1p5Rearrangement_d_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_d_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_d2_sequence_alignment = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d2_sequence_alignment, name="V1p5Rearrangement_d2_sequence_alignment", curie=AK_SCHEMA.curie('V1p5Rearrangement_d2_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d2_sequence_alignment, domain=None, range=Optional[str])

slots.V1p5Rearrangement_d2_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d2_sequence_alignment_aa, name="V1p5Rearrangement_d2_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_d2_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d2_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_j_sequence_alignment = Slot(uri=AK_SCHEMA.V1p5Rearrangement_j_sequence_alignment, name="V1p5Rearrangement_j_sequence_alignment", curie=AK_SCHEMA.curie('V1p5Rearrangement_j_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_j_sequence_alignment, domain=None, range=Optional[str])

slots.V1p5Rearrangement_j_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_j_sequence_alignment_aa, name="V1p5Rearrangement_j_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_j_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_j_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_c_sequence_alignment = Slot(uri=AK_SCHEMA.V1p5Rearrangement_c_sequence_alignment, name="V1p5Rearrangement_c_sequence_alignment", curie=AK_SCHEMA.curie('V1p5Rearrangement_c_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_c_sequence_alignment, domain=None, range=Optional[str])

slots.V1p5Rearrangement_c_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_c_sequence_alignment_aa, name="V1p5Rearrangement_c_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_c_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_c_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_v_germline_alignment = Slot(uri=AK_SCHEMA.V1p5Rearrangement_v_germline_alignment, name="V1p5Rearrangement_v_germline_alignment", curie=AK_SCHEMA.curie('V1p5Rearrangement_v_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_v_germline_alignment, domain=None, range=Optional[str])

slots.V1p5Rearrangement_v_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_v_germline_alignment_aa, name="V1p5Rearrangement_v_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_v_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_v_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_d_germline_alignment = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d_germline_alignment, name="V1p5Rearrangement_d_germline_alignment", curie=AK_SCHEMA.curie('V1p5Rearrangement_d_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d_germline_alignment, domain=None, range=Optional[str])

slots.V1p5Rearrangement_d_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d_germline_alignment_aa, name="V1p5Rearrangement_d_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_d_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_d2_germline_alignment = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d2_germline_alignment, name="V1p5Rearrangement_d2_germline_alignment", curie=AK_SCHEMA.curie('V1p5Rearrangement_d2_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d2_germline_alignment, domain=None, range=Optional[str])

slots.V1p5Rearrangement_d2_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d2_germline_alignment_aa, name="V1p5Rearrangement_d2_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_d2_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d2_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_j_germline_alignment = Slot(uri=AK_SCHEMA.V1p5Rearrangement_j_germline_alignment, name="V1p5Rearrangement_j_germline_alignment", curie=AK_SCHEMA.curie('V1p5Rearrangement_j_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_j_germline_alignment, domain=None, range=Optional[str])

slots.V1p5Rearrangement_j_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_j_germline_alignment_aa, name="V1p5Rearrangement_j_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_j_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_j_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_c_germline_alignment = Slot(uri=AK_SCHEMA.V1p5Rearrangement_c_germline_alignment, name="V1p5Rearrangement_c_germline_alignment", curie=AK_SCHEMA.curie('V1p5Rearrangement_c_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_c_germline_alignment, domain=None, range=Optional[str])

slots.V1p5Rearrangement_c_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p5Rearrangement_c_germline_alignment_aa, name="V1p5Rearrangement_c_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p5Rearrangement_c_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_c_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p5Rearrangement_junction_length = Slot(uri=AK_SCHEMA.V1p5Rearrangement_junction_length, name="V1p5Rearrangement_junction_length", curie=AK_SCHEMA.curie('V1p5Rearrangement_junction_length'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_junction_length, domain=None, range=Optional[int])

slots.V1p5Rearrangement_junction_aa_length = Slot(uri=AK_SCHEMA.V1p5Rearrangement_junction_aa_length, name="V1p5Rearrangement_junction_aa_length", curie=AK_SCHEMA.curie('V1p5Rearrangement_junction_aa_length'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_junction_aa_length, domain=None, range=Optional[int])

slots.V1p5Rearrangement_np1_length = Slot(uri=AK_SCHEMA.V1p5Rearrangement_np1_length, name="V1p5Rearrangement_np1_length", curie=AK_SCHEMA.curie('V1p5Rearrangement_np1_length'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_np1_length, domain=None, range=Optional[int])

slots.V1p5Rearrangement_np2_length = Slot(uri=AK_SCHEMA.V1p5Rearrangement_np2_length, name="V1p5Rearrangement_np2_length", curie=AK_SCHEMA.curie('V1p5Rearrangement_np2_length'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_np2_length, domain=None, range=Optional[int])

slots.V1p5Rearrangement_np3_length = Slot(uri=AK_SCHEMA.V1p5Rearrangement_np3_length, name="V1p5Rearrangement_np3_length", curie=AK_SCHEMA.curie('V1p5Rearrangement_np3_length'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_np3_length, domain=None, range=Optional[int])

slots.V1p5Rearrangement_n1_length = Slot(uri=AK_SCHEMA.V1p5Rearrangement_n1_length, name="V1p5Rearrangement_n1_length", curie=AK_SCHEMA.curie('V1p5Rearrangement_n1_length'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_n1_length, domain=None, range=Optional[int])

slots.V1p5Rearrangement_n2_length = Slot(uri=AK_SCHEMA.V1p5Rearrangement_n2_length, name="V1p5Rearrangement_n2_length", curie=AK_SCHEMA.curie('V1p5Rearrangement_n2_length'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_n2_length, domain=None, range=Optional[int])

slots.V1p5Rearrangement_n3_length = Slot(uri=AK_SCHEMA.V1p5Rearrangement_n3_length, name="V1p5Rearrangement_n3_length", curie=AK_SCHEMA.curie('V1p5Rearrangement_n3_length'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_n3_length, domain=None, range=Optional[int])

slots.V1p5Rearrangement_p3v_length = Slot(uri=AK_SCHEMA.V1p5Rearrangement_p3v_length, name="V1p5Rearrangement_p3v_length", curie=AK_SCHEMA.curie('V1p5Rearrangement_p3v_length'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_p3v_length, domain=None, range=Optional[int])

slots.V1p5Rearrangement_p5d_length = Slot(uri=AK_SCHEMA.V1p5Rearrangement_p5d_length, name="V1p5Rearrangement_p5d_length", curie=AK_SCHEMA.curie('V1p5Rearrangement_p5d_length'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_p5d_length, domain=None, range=Optional[int])

slots.V1p5Rearrangement_p3d_length = Slot(uri=AK_SCHEMA.V1p5Rearrangement_p3d_length, name="V1p5Rearrangement_p3d_length", curie=AK_SCHEMA.curie('V1p5Rearrangement_p3d_length'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_p3d_length, domain=None, range=Optional[int])

slots.V1p5Rearrangement_p5d2_length = Slot(uri=AK_SCHEMA.V1p5Rearrangement_p5d2_length, name="V1p5Rearrangement_p5d2_length", curie=AK_SCHEMA.curie('V1p5Rearrangement_p5d2_length'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_p5d2_length, domain=None, range=Optional[int])

slots.V1p5Rearrangement_p3d2_length = Slot(uri=AK_SCHEMA.V1p5Rearrangement_p3d2_length, name="V1p5Rearrangement_p3d2_length", curie=AK_SCHEMA.curie('V1p5Rearrangement_p3d2_length'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_p3d2_length, domain=None, range=Optional[int])

slots.V1p5Rearrangement_p5j_length = Slot(uri=AK_SCHEMA.V1p5Rearrangement_p5j_length, name="V1p5Rearrangement_p5j_length", curie=AK_SCHEMA.curie('V1p5Rearrangement_p5j_length'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_p5j_length, domain=None, range=Optional[int])

slots.V1p5Rearrangement_v_frameshift = Slot(uri=AK_SCHEMA.V1p5Rearrangement_v_frameshift, name="V1p5Rearrangement_v_frameshift", curie=AK_SCHEMA.curie('V1p5Rearrangement_v_frameshift'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_v_frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5Rearrangement_j_frameshift = Slot(uri=AK_SCHEMA.V1p5Rearrangement_j_frameshift, name="V1p5Rearrangement_j_frameshift", curie=AK_SCHEMA.curie('V1p5Rearrangement_j_frameshift'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_j_frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p5Rearrangement_d_frame = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d_frame, name="V1p5Rearrangement_d_frame", curie=AK_SCHEMA.curie('V1p5Rearrangement_d_frame'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d_frame, domain=None, range=Optional[int])

slots.V1p5Rearrangement_d2_frame = Slot(uri=AK_SCHEMA.V1p5Rearrangement_d2_frame, name="V1p5Rearrangement_d2_frame", curie=AK_SCHEMA.curie('V1p5Rearrangement_d2_frame'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_d2_frame, domain=None, range=Optional[int])

slots.V1p5Rearrangement_consensus_count = Slot(uri=AK_SCHEMA.V1p5Rearrangement_consensus_count, name="V1p5Rearrangement_consensus_count", curie=AK_SCHEMA.curie('V1p5Rearrangement_consensus_count'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_consensus_count, domain=None, range=Optional[int])

slots.V1p5Rearrangement_duplicate_count = Slot(uri=AK_SCHEMA.V1p5Rearrangement_duplicate_count, name="V1p5Rearrangement_duplicate_count", curie=AK_SCHEMA.curie('V1p5Rearrangement_duplicate_count'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_duplicate_count, domain=None, range=Optional[int])

slots.V1p5Rearrangement_umi_count = Slot(uri=AK_SCHEMA.V1p5Rearrangement_umi_count, name="V1p5Rearrangement_umi_count", curie=AK_SCHEMA.curie('V1p5Rearrangement_umi_count'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_umi_count, domain=None, range=Optional[int])

slots.V1p5Rearrangement_cell_id = Slot(uri=AK_SCHEMA.V1p5Rearrangement_cell_id, name="V1p5Rearrangement_cell_id", curie=AK_SCHEMA.curie('V1p5Rearrangement_cell_id'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_cell_id, domain=None, range=Optional[str])

slots.V1p5Rearrangement_clone_id = Slot(uri=AK_SCHEMA.V1p5Rearrangement_clone_id, name="V1p5Rearrangement_clone_id", curie=AK_SCHEMA.curie('V1p5Rearrangement_clone_id'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_clone_id, domain=None, range=Optional[str])

slots.V1p5Rearrangement_repertoire_id = Slot(uri=AK_SCHEMA.V1p5Rearrangement_repertoire_id, name="V1p5Rearrangement_repertoire_id", curie=AK_SCHEMA.curie('V1p5Rearrangement_repertoire_id'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_repertoire_id, domain=None, range=Optional[str])

slots.V1p5Rearrangement_sample_processing_id = Slot(uri=AK_SCHEMA.V1p5Rearrangement_sample_processing_id, name="V1p5Rearrangement_sample_processing_id", curie=AK_SCHEMA.curie('V1p5Rearrangement_sample_processing_id'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_sample_processing_id, domain=None, range=Optional[str])

slots.V1p5Rearrangement_data_processing_id = Slot(uri=AK_SCHEMA.V1p5Rearrangement_data_processing_id, name="V1p5Rearrangement_data_processing_id", curie=AK_SCHEMA.curie('V1p5Rearrangement_data_processing_id'),
                   model_uri=AK_SCHEMA.V1p5Rearrangement_data_processing_id, domain=None, range=Optional[str])

slots.V1p5Clone_clone_id = Slot(uri=AK_SCHEMA.V1p5Clone_clone_id, name="V1p5Clone_clone_id", curie=AK_SCHEMA.curie('V1p5Clone_clone_id'),
                   model_uri=AK_SCHEMA.V1p5Clone_clone_id, domain=None, range=str)

slots.V1p5Clone_repertoire_id = Slot(uri=AK_SCHEMA.V1p5Clone_repertoire_id, name="V1p5Clone_repertoire_id", curie=AK_SCHEMA.curie('V1p5Clone_repertoire_id'),
                   model_uri=AK_SCHEMA.V1p5Clone_repertoire_id, domain=None, range=Optional[str])

slots.V1p5Clone_data_processing_id = Slot(uri=AK_SCHEMA.V1p5Clone_data_processing_id, name="V1p5Clone_data_processing_id", curie=AK_SCHEMA.curie('V1p5Clone_data_processing_id'),
                   model_uri=AK_SCHEMA.V1p5Clone_data_processing_id, domain=None, range=Optional[str])

slots.V1p5Clone_sequences = Slot(uri=AK_SCHEMA.V1p5Clone_sequences, name="V1p5Clone_sequences", curie=AK_SCHEMA.curie('V1p5Clone_sequences'),
                   model_uri=AK_SCHEMA.V1p5Clone_sequences, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p5Clone_v_call = Slot(uri=AK_SCHEMA.V1p5Clone_v_call, name="V1p5Clone_v_call", curie=AK_SCHEMA.curie('V1p5Clone_v_call'),
                   model_uri=AK_SCHEMA.V1p5Clone_v_call, domain=None, range=Optional[str])

slots.V1p5Clone_d_call = Slot(uri=AK_SCHEMA.V1p5Clone_d_call, name="V1p5Clone_d_call", curie=AK_SCHEMA.curie('V1p5Clone_d_call'),
                   model_uri=AK_SCHEMA.V1p5Clone_d_call, domain=None, range=Optional[str])

slots.V1p5Clone_j_call = Slot(uri=AK_SCHEMA.V1p5Clone_j_call, name="V1p5Clone_j_call", curie=AK_SCHEMA.curie('V1p5Clone_j_call'),
                   model_uri=AK_SCHEMA.V1p5Clone_j_call, domain=None, range=Optional[str])

slots.V1p5Clone_junction = Slot(uri=AK_SCHEMA.V1p5Clone_junction, name="V1p5Clone_junction", curie=AK_SCHEMA.curie('V1p5Clone_junction'),
                   model_uri=AK_SCHEMA.V1p5Clone_junction, domain=None, range=Optional[str])

slots.V1p5Clone_junction_aa = Slot(uri=AK_SCHEMA.V1p5Clone_junction_aa, name="V1p5Clone_junction_aa", curie=AK_SCHEMA.curie('V1p5Clone_junction_aa'),
                   model_uri=AK_SCHEMA.V1p5Clone_junction_aa, domain=None, range=Optional[str])

slots.V1p5Clone_junction_length = Slot(uri=AK_SCHEMA.V1p5Clone_junction_length, name="V1p5Clone_junction_length", curie=AK_SCHEMA.curie('V1p5Clone_junction_length'),
                   model_uri=AK_SCHEMA.V1p5Clone_junction_length, domain=None, range=Optional[int])

slots.V1p5Clone_junction_aa_length = Slot(uri=AK_SCHEMA.V1p5Clone_junction_aa_length, name="V1p5Clone_junction_aa_length", curie=AK_SCHEMA.curie('V1p5Clone_junction_aa_length'),
                   model_uri=AK_SCHEMA.V1p5Clone_junction_aa_length, domain=None, range=Optional[int])

slots.V1p5Clone_germline_alignment = Slot(uri=AK_SCHEMA.V1p5Clone_germline_alignment, name="V1p5Clone_germline_alignment", curie=AK_SCHEMA.curie('V1p5Clone_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p5Clone_germline_alignment, domain=None, range=str)

slots.V1p5Clone_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p5Clone_germline_alignment_aa, name="V1p5Clone_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p5Clone_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p5Clone_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p5Clone_v_alignment_start = Slot(uri=AK_SCHEMA.V1p5Clone_v_alignment_start, name="V1p5Clone_v_alignment_start", curie=AK_SCHEMA.curie('V1p5Clone_v_alignment_start'),
                   model_uri=AK_SCHEMA.V1p5Clone_v_alignment_start, domain=None, range=Optional[int])

slots.V1p5Clone_v_alignment_end = Slot(uri=AK_SCHEMA.V1p5Clone_v_alignment_end, name="V1p5Clone_v_alignment_end", curie=AK_SCHEMA.curie('V1p5Clone_v_alignment_end'),
                   model_uri=AK_SCHEMA.V1p5Clone_v_alignment_end, domain=None, range=Optional[int])

slots.V1p5Clone_d_alignment_start = Slot(uri=AK_SCHEMA.V1p5Clone_d_alignment_start, name="V1p5Clone_d_alignment_start", curie=AK_SCHEMA.curie('V1p5Clone_d_alignment_start'),
                   model_uri=AK_SCHEMA.V1p5Clone_d_alignment_start, domain=None, range=Optional[int])

slots.V1p5Clone_d_alignment_end = Slot(uri=AK_SCHEMA.V1p5Clone_d_alignment_end, name="V1p5Clone_d_alignment_end", curie=AK_SCHEMA.curie('V1p5Clone_d_alignment_end'),
                   model_uri=AK_SCHEMA.V1p5Clone_d_alignment_end, domain=None, range=Optional[int])

slots.V1p5Clone_j_alignment_start = Slot(uri=AK_SCHEMA.V1p5Clone_j_alignment_start, name="V1p5Clone_j_alignment_start", curie=AK_SCHEMA.curie('V1p5Clone_j_alignment_start'),
                   model_uri=AK_SCHEMA.V1p5Clone_j_alignment_start, domain=None, range=Optional[int])

slots.V1p5Clone_j_alignment_end = Slot(uri=AK_SCHEMA.V1p5Clone_j_alignment_end, name="V1p5Clone_j_alignment_end", curie=AK_SCHEMA.curie('V1p5Clone_j_alignment_end'),
                   model_uri=AK_SCHEMA.V1p5Clone_j_alignment_end, domain=None, range=Optional[int])

slots.V1p5Clone_junction_start = Slot(uri=AK_SCHEMA.V1p5Clone_junction_start, name="V1p5Clone_junction_start", curie=AK_SCHEMA.curie('V1p5Clone_junction_start'),
                   model_uri=AK_SCHEMA.V1p5Clone_junction_start, domain=None, range=Optional[int])

slots.V1p5Clone_junction_end = Slot(uri=AK_SCHEMA.V1p5Clone_junction_end, name="V1p5Clone_junction_end", curie=AK_SCHEMA.curie('V1p5Clone_junction_end'),
                   model_uri=AK_SCHEMA.V1p5Clone_junction_end, domain=None, range=Optional[int])

slots.V1p5Clone_umi_count = Slot(uri=AK_SCHEMA.V1p5Clone_umi_count, name="V1p5Clone_umi_count", curie=AK_SCHEMA.curie('V1p5Clone_umi_count'),
                   model_uri=AK_SCHEMA.V1p5Clone_umi_count, domain=None, range=Optional[int])

slots.V1p5Clone_clone_count = Slot(uri=AK_SCHEMA.V1p5Clone_clone_count, name="V1p5Clone_clone_count", curie=AK_SCHEMA.curie('V1p5Clone_clone_count'),
                   model_uri=AK_SCHEMA.V1p5Clone_clone_count, domain=None, range=Optional[int])

slots.V1p5Clone_seed_id = Slot(uri=AK_SCHEMA.V1p5Clone_seed_id, name="V1p5Clone_seed_id", curie=AK_SCHEMA.curie('V1p5Clone_seed_id'),
                   model_uri=AK_SCHEMA.V1p5Clone_seed_id, domain=None, range=Optional[str])

slots.V1p5Tree_tree_id = Slot(uri=AK_SCHEMA.V1p5Tree_tree_id, name="V1p5Tree_tree_id", curie=AK_SCHEMA.curie('V1p5Tree_tree_id'),
                   model_uri=AK_SCHEMA.V1p5Tree_tree_id, domain=None, range=str)

slots.V1p5Tree_clone_id = Slot(uri=AK_SCHEMA.V1p5Tree_clone_id, name="V1p5Tree_clone_id", curie=AK_SCHEMA.curie('V1p5Tree_clone_id'),
                   model_uri=AK_SCHEMA.V1p5Tree_clone_id, domain=None, range=str)

slots.V1p5Tree_newick = Slot(uri=AK_SCHEMA.V1p5Tree_newick, name="V1p5Tree_newick", curie=AK_SCHEMA.curie('V1p5Tree_newick'),
                   model_uri=AK_SCHEMA.V1p5Tree_newick, domain=None, range=str)

slots.V1p5Tree_nodes = Slot(uri=AK_SCHEMA.V1p5Tree_nodes, name="V1p5Tree_nodes", curie=AK_SCHEMA.curie('V1p5Tree_nodes'),
                   model_uri=AK_SCHEMA.V1p5Tree_nodes, domain=None, range=Optional[Union[Union[dict, V1p5Node], List[Union[dict, V1p5Node]]]])

slots.V1p5Node_sequence_id = Slot(uri=AK_SCHEMA.V1p5Node_sequence_id, name="V1p5Node_sequence_id", curie=AK_SCHEMA.curie('V1p5Node_sequence_id'),
                   model_uri=AK_SCHEMA.V1p5Node_sequence_id, domain=None, range=str)

slots.V1p5Node_sequence_alignment = Slot(uri=AK_SCHEMA.V1p5Node_sequence_alignment, name="V1p5Node_sequence_alignment", curie=AK_SCHEMA.curie('V1p5Node_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p5Node_sequence_alignment, domain=None, range=Optional[str])

slots.V1p5Node_junction = Slot(uri=AK_SCHEMA.V1p5Node_junction, name="V1p5Node_junction", curie=AK_SCHEMA.curie('V1p5Node_junction'),
                   model_uri=AK_SCHEMA.V1p5Node_junction, domain=None, range=Optional[str])

slots.V1p5Node_junction_aa = Slot(uri=AK_SCHEMA.V1p5Node_junction_aa, name="V1p5Node_junction_aa", curie=AK_SCHEMA.curie('V1p5Node_junction_aa'),
                   model_uri=AK_SCHEMA.V1p5Node_junction_aa, domain=None, range=Optional[str])

slots.V1p5Cell_cell_id = Slot(uri=AK_SCHEMA.V1p5Cell_cell_id, name="V1p5Cell_cell_id", curie=AK_SCHEMA.curie('V1p5Cell_cell_id'),
                   model_uri=AK_SCHEMA.V1p5Cell_cell_id, domain=None, range=str)

slots.V1p5Cell_rearrangements = Slot(uri=AK_SCHEMA.V1p5Cell_rearrangements, name="V1p5Cell_rearrangements", curie=AK_SCHEMA.curie('V1p5Cell_rearrangements'),
                   model_uri=AK_SCHEMA.V1p5Cell_rearrangements, domain=None, range=Union[str, List[str]])

slots.V1p5Cell_receptors = Slot(uri=AK_SCHEMA.V1p5Cell_receptors, name="V1p5Cell_receptors", curie=AK_SCHEMA.curie('V1p5Cell_receptors'),
                   model_uri=AK_SCHEMA.V1p5Cell_receptors, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p5Cell_repertoire_id = Slot(uri=AK_SCHEMA.V1p5Cell_repertoire_id, name="V1p5Cell_repertoire_id", curie=AK_SCHEMA.curie('V1p5Cell_repertoire_id'),
                   model_uri=AK_SCHEMA.V1p5Cell_repertoire_id, domain=None, range=str)

slots.V1p5Cell_data_processing_id = Slot(uri=AK_SCHEMA.V1p5Cell_data_processing_id, name="V1p5Cell_data_processing_id", curie=AK_SCHEMA.curie('V1p5Cell_data_processing_id'),
                   model_uri=AK_SCHEMA.V1p5Cell_data_processing_id, domain=None, range=Optional[str])

slots.V1p5Cell_expression_study_method = Slot(uri=AK_SCHEMA.V1p5Cell_expression_study_method, name="V1p5Cell_expression_study_method", curie=AK_SCHEMA.curie('V1p5Cell_expression_study_method'),
                   model_uri=AK_SCHEMA.V1p5Cell_expression_study_method, domain=None, range=Optional[Union[str, "V1p5ExpressionStudyMethod"]])

slots.V1p5Cell_expression_raw_doi = Slot(uri=AK_SCHEMA.V1p5Cell_expression_raw_doi, name="V1p5Cell_expression_raw_doi", curie=AK_SCHEMA.curie('V1p5Cell_expression_raw_doi'),
                   model_uri=AK_SCHEMA.V1p5Cell_expression_raw_doi, domain=None, range=Optional[str])

slots.V1p5Cell_expression_index = Slot(uri=AK_SCHEMA.V1p5Cell_expression_index, name="V1p5Cell_expression_index", curie=AK_SCHEMA.curie('V1p5Cell_expression_index'),
                   model_uri=AK_SCHEMA.V1p5Cell_expression_index, domain=None, range=Optional[str])

slots.V1p5Cell_virtual_pairing = Slot(uri=AK_SCHEMA.V1p5Cell_virtual_pairing, name="V1p5Cell_virtual_pairing", curie=AK_SCHEMA.curie('V1p5Cell_virtual_pairing'),
                   model_uri=AK_SCHEMA.V1p5Cell_virtual_pairing, domain=None, range=Union[bool, Bool])

slots.V1p5CellExpression_expression_id = Slot(uri=AK_SCHEMA.V1p5CellExpression_expression_id, name="V1p5CellExpression_expression_id", curie=AK_SCHEMA.curie('V1p5CellExpression_expression_id'),
                   model_uri=AK_SCHEMA.V1p5CellExpression_expression_id, domain=None, range=str)

slots.V1p5CellExpression_cell_id = Slot(uri=AK_SCHEMA.V1p5CellExpression_cell_id, name="V1p5CellExpression_cell_id", curie=AK_SCHEMA.curie('V1p5CellExpression_cell_id'),
                   model_uri=AK_SCHEMA.V1p5CellExpression_cell_id, domain=None, range=str)

slots.V1p5CellExpression_repertoire_id = Slot(uri=AK_SCHEMA.V1p5CellExpression_repertoire_id, name="V1p5CellExpression_repertoire_id", curie=AK_SCHEMA.curie('V1p5CellExpression_repertoire_id'),
                   model_uri=AK_SCHEMA.V1p5CellExpression_repertoire_id, domain=None, range=str)

slots.V1p5CellExpression_data_processing_id = Slot(uri=AK_SCHEMA.V1p5CellExpression_data_processing_id, name="V1p5CellExpression_data_processing_id", curie=AK_SCHEMA.curie('V1p5CellExpression_data_processing_id'),
                   model_uri=AK_SCHEMA.V1p5CellExpression_data_processing_id, domain=None, range=str)

slots.V1p5CellExpression_property_type = Slot(uri=AK_SCHEMA.V1p5CellExpression_property_type, name="V1p5CellExpression_property_type", curie=AK_SCHEMA.curie('V1p5CellExpression_property_type'),
                   model_uri=AK_SCHEMA.V1p5CellExpression_property_type, domain=None, range=str)

slots.V1p5CellExpression_property = Slot(uri=AK_SCHEMA.V1p5CellExpression_property, name="V1p5CellExpression_property", curie=AK_SCHEMA.curie('V1p5CellExpression_property'),
                   model_uri=AK_SCHEMA.V1p5CellExpression_property, domain=None, range=Union[str, "V1p5Property"])

slots.V1p5CellExpression_value = Slot(uri=AK_SCHEMA.V1p5CellExpression_value, name="V1p5CellExpression_value", curie=AK_SCHEMA.curie('V1p5CellExpression_value'),
                   model_uri=AK_SCHEMA.V1p5CellExpression_value, domain=None, range=float)

slots.V1p5Receptor_receptor_id = Slot(uri=AK_SCHEMA.V1p5Receptor_receptor_id, name="V1p5Receptor_receptor_id", curie=AK_SCHEMA.curie('V1p5Receptor_receptor_id'),
                   model_uri=AK_SCHEMA.V1p5Receptor_receptor_id, domain=None, range=str)

slots.V1p5Receptor_receptor_hash = Slot(uri=AK_SCHEMA.V1p5Receptor_receptor_hash, name="V1p5Receptor_receptor_hash", curie=AK_SCHEMA.curie('V1p5Receptor_receptor_hash'),
                   model_uri=AK_SCHEMA.V1p5Receptor_receptor_hash, domain=None, range=str)

slots.V1p5Receptor_receptor_type = Slot(uri=AK_SCHEMA.V1p5Receptor_receptor_type, name="V1p5Receptor_receptor_type", curie=AK_SCHEMA.curie('V1p5Receptor_receptor_type'),
                   model_uri=AK_SCHEMA.V1p5Receptor_receptor_type, domain=None, range=Union[str, "V1p5ReceptorType"])

slots.V1p5Receptor_receptor_variable_domain_1_aa = Slot(uri=AK_SCHEMA.V1p5Receptor_receptor_variable_domain_1_aa, name="V1p5Receptor_receptor_variable_domain_1_aa", curie=AK_SCHEMA.curie('V1p5Receptor_receptor_variable_domain_1_aa'),
                   model_uri=AK_SCHEMA.V1p5Receptor_receptor_variable_domain_1_aa, domain=None, range=str)

slots.V1p5Receptor_receptor_variable_domain_1_locus = Slot(uri=AK_SCHEMA.V1p5Receptor_receptor_variable_domain_1_locus, name="V1p5Receptor_receptor_variable_domain_1_locus", curie=AK_SCHEMA.curie('V1p5Receptor_receptor_variable_domain_1_locus'),
                   model_uri=AK_SCHEMA.V1p5Receptor_receptor_variable_domain_1_locus, domain=None, range=Union[str, "V1p5ReceptorVariableDomain1Locus"])

slots.V1p5Receptor_receptor_variable_domain_2_aa = Slot(uri=AK_SCHEMA.V1p5Receptor_receptor_variable_domain_2_aa, name="V1p5Receptor_receptor_variable_domain_2_aa", curie=AK_SCHEMA.curie('V1p5Receptor_receptor_variable_domain_2_aa'),
                   model_uri=AK_SCHEMA.V1p5Receptor_receptor_variable_domain_2_aa, domain=None, range=str)

slots.V1p5Receptor_receptor_variable_domain_2_locus = Slot(uri=AK_SCHEMA.V1p5Receptor_receptor_variable_domain_2_locus, name="V1p5Receptor_receptor_variable_domain_2_locus", curie=AK_SCHEMA.curie('V1p5Receptor_receptor_variable_domain_2_locus'),
                   model_uri=AK_SCHEMA.V1p5Receptor_receptor_variable_domain_2_locus, domain=None, range=Union[str, "V1p5ReceptorVariableDomain2Locus"])

slots.V1p5Receptor_receptor_ref = Slot(uri=AK_SCHEMA.V1p5Receptor_receptor_ref, name="V1p5Receptor_receptor_ref", curie=AK_SCHEMA.curie('V1p5Receptor_receptor_ref'),
                   model_uri=AK_SCHEMA.V1p5Receptor_receptor_ref, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p5Receptor_reactivity_measurements = Slot(uri=AK_SCHEMA.V1p5Receptor_reactivity_measurements, name="V1p5Receptor_reactivity_measurements", curie=AK_SCHEMA.curie('V1p5Receptor_reactivity_measurements'),
                   model_uri=AK_SCHEMA.V1p5Receptor_reactivity_measurements, domain=None, range=Optional[Union[Union[dict, V1p5ReceptorReactivity], List[Union[dict, V1p5ReceptorReactivity]]]])

slots.V1p5ReceptorReactivity_ligand_type = Slot(uri=AK_SCHEMA.V1p5ReceptorReactivity_ligand_type, name="V1p5ReceptorReactivity_ligand_type", curie=AK_SCHEMA.curie('V1p5ReceptorReactivity_ligand_type'),
                   model_uri=AK_SCHEMA.V1p5ReceptorReactivity_ligand_type, domain=None, range=Union[str, "V1p5LigandType"])

slots.V1p5ReceptorReactivity_antigen_type = Slot(uri=AK_SCHEMA.V1p5ReceptorReactivity_antigen_type, name="V1p5ReceptorReactivity_antigen_type", curie=AK_SCHEMA.curie('V1p5ReceptorReactivity_antigen_type'),
                   model_uri=AK_SCHEMA.V1p5ReceptorReactivity_antigen_type, domain=None, range=Union[str, "V1p5AntigenType"])

slots.V1p5ReceptorReactivity_antigen = Slot(uri=AK_SCHEMA.V1p5ReceptorReactivity_antigen, name="V1p5ReceptorReactivity_antigen", curie=AK_SCHEMA.curie('V1p5ReceptorReactivity_antigen'),
                   model_uri=AK_SCHEMA.V1p5ReceptorReactivity_antigen, domain=None, range=Union[str, "V1p5Antigen"])

slots.V1p5ReceptorReactivity_antigen_source_species = Slot(uri=AK_SCHEMA.V1p5ReceptorReactivity_antigen_source_species, name="V1p5ReceptorReactivity_antigen_source_species", curie=AK_SCHEMA.curie('V1p5ReceptorReactivity_antigen_source_species'),
                   model_uri=AK_SCHEMA.V1p5ReceptorReactivity_antigen_source_species, domain=None, range=Optional[Union[str, "V1p5AntigenSourceSpecies"]])

slots.V1p5ReceptorReactivity_peptide_start = Slot(uri=AK_SCHEMA.V1p5ReceptorReactivity_peptide_start, name="V1p5ReceptorReactivity_peptide_start", curie=AK_SCHEMA.curie('V1p5ReceptorReactivity_peptide_start'),
                   model_uri=AK_SCHEMA.V1p5ReceptorReactivity_peptide_start, domain=None, range=Optional[int])

slots.V1p5ReceptorReactivity_peptide_end = Slot(uri=AK_SCHEMA.V1p5ReceptorReactivity_peptide_end, name="V1p5ReceptorReactivity_peptide_end", curie=AK_SCHEMA.curie('V1p5ReceptorReactivity_peptide_end'),
                   model_uri=AK_SCHEMA.V1p5ReceptorReactivity_peptide_end, domain=None, range=Optional[int])

slots.V1p5ReceptorReactivity_mhc_class = Slot(uri=AK_SCHEMA.V1p5ReceptorReactivity_mhc_class, name="V1p5ReceptorReactivity_mhc_class", curie=AK_SCHEMA.curie('V1p5ReceptorReactivity_mhc_class'),
                   model_uri=AK_SCHEMA.V1p5ReceptorReactivity_mhc_class, domain=None, range=Optional[Union[str, "V1p5MhcClass"]])

slots.V1p5ReceptorReactivity_mhc_gene_1 = Slot(uri=AK_SCHEMA.V1p5ReceptorReactivity_mhc_gene_1, name="V1p5ReceptorReactivity_mhc_gene_1", curie=AK_SCHEMA.curie('V1p5ReceptorReactivity_mhc_gene_1'),
                   model_uri=AK_SCHEMA.V1p5ReceptorReactivity_mhc_gene_1, domain=None, range=Optional[Union[str, "V1p5MhcGene1"]])

slots.V1p5ReceptorReactivity_mhc_allele_1 = Slot(uri=AK_SCHEMA.V1p5ReceptorReactivity_mhc_allele_1, name="V1p5ReceptorReactivity_mhc_allele_1", curie=AK_SCHEMA.curie('V1p5ReceptorReactivity_mhc_allele_1'),
                   model_uri=AK_SCHEMA.V1p5ReceptorReactivity_mhc_allele_1, domain=None, range=Optional[str])

slots.V1p5ReceptorReactivity_mhc_gene_2 = Slot(uri=AK_SCHEMA.V1p5ReceptorReactivity_mhc_gene_2, name="V1p5ReceptorReactivity_mhc_gene_2", curie=AK_SCHEMA.curie('V1p5ReceptorReactivity_mhc_gene_2'),
                   model_uri=AK_SCHEMA.V1p5ReceptorReactivity_mhc_gene_2, domain=None, range=Optional[Union[str, "V1p5MhcGene2"]])

slots.V1p5ReceptorReactivity_mhc_allele_2 = Slot(uri=AK_SCHEMA.V1p5ReceptorReactivity_mhc_allele_2, name="V1p5ReceptorReactivity_mhc_allele_2", curie=AK_SCHEMA.curie('V1p5ReceptorReactivity_mhc_allele_2'),
                   model_uri=AK_SCHEMA.V1p5ReceptorReactivity_mhc_allele_2, domain=None, range=Optional[str])

slots.V1p5ReceptorReactivity_reactivity_method = Slot(uri=AK_SCHEMA.V1p5ReceptorReactivity_reactivity_method, name="V1p5ReceptorReactivity_reactivity_method", curie=AK_SCHEMA.curie('V1p5ReceptorReactivity_reactivity_method'),
                   model_uri=AK_SCHEMA.V1p5ReceptorReactivity_reactivity_method, domain=None, range=Union[str, "V1p5ReactivityMethod"])

slots.V1p5ReceptorReactivity_reactivity_readout = Slot(uri=AK_SCHEMA.V1p5ReceptorReactivity_reactivity_readout, name="V1p5ReceptorReactivity_reactivity_readout", curie=AK_SCHEMA.curie('V1p5ReceptorReactivity_reactivity_readout'),
                   model_uri=AK_SCHEMA.V1p5ReceptorReactivity_reactivity_readout, domain=None, range=Union[str, "V1p5ReactivityReadout"])

slots.V1p5ReceptorReactivity_reactivity_value = Slot(uri=AK_SCHEMA.V1p5ReceptorReactivity_reactivity_value, name="V1p5ReceptorReactivity_reactivity_value", curie=AK_SCHEMA.curie('V1p5ReceptorReactivity_reactivity_value'),
                   model_uri=AK_SCHEMA.V1p5ReceptorReactivity_reactivity_value, domain=None, range=float)

slots.V1p5ReceptorReactivity_reactivity_unit = Slot(uri=AK_SCHEMA.V1p5ReceptorReactivity_reactivity_unit, name="V1p5ReceptorReactivity_reactivity_unit", curie=AK_SCHEMA.curie('V1p5ReceptorReactivity_reactivity_unit'),
                   model_uri=AK_SCHEMA.V1p5ReceptorReactivity_reactivity_unit, domain=None, range=str)

slots.V1p5SampleProcessing_sample_processing_id = Slot(uri=AK_SCHEMA.V1p5SampleProcessing_sample_processing_id, name="V1p5SampleProcessing_sample_processing_id", curie=AK_SCHEMA.curie('V1p5SampleProcessing_sample_processing_id'),
                   model_uri=AK_SCHEMA.V1p5SampleProcessing_sample_processing_id, domain=None, range=Optional[str])

slots.V1p4TimePoint_label = Slot(uri=AK_SCHEMA.V1p4TimePoint_label, name="V1p4TimePoint_label", curie=AK_SCHEMA.curie('V1p4TimePoint_label'),
                   model_uri=AK_SCHEMA.V1p4TimePoint_label, domain=None, range=Optional[str])

slots.V1p4TimePoint_value = Slot(uri=AK_SCHEMA.V1p4TimePoint_value, name="V1p4TimePoint_value", curie=AK_SCHEMA.curie('V1p4TimePoint_value'),
                   model_uri=AK_SCHEMA.V1p4TimePoint_value, domain=None, range=Optional[float])

slots.V1p4TimePoint_unit = Slot(uri=AK_SCHEMA.V1p4TimePoint_unit, name="V1p4TimePoint_unit", curie=AK_SCHEMA.curie('V1p4TimePoint_unit'),
                   model_uri=AK_SCHEMA.V1p4TimePoint_unit, domain=None, range=Optional[Union[str, "V1p4Unit"]])

slots.V1p4TimeInterval_min = Slot(uri=AK_SCHEMA.V1p4TimeInterval_min, name="V1p4TimeInterval_min", curie=AK_SCHEMA.curie('V1p4TimeInterval_min'),
                   model_uri=AK_SCHEMA.V1p4TimeInterval_min, domain=None, range=Optional[float])

slots.V1p4TimeInterval_max = Slot(uri=AK_SCHEMA.V1p4TimeInterval_max, name="V1p4TimeInterval_max", curie=AK_SCHEMA.curie('V1p4TimeInterval_max'),
                   model_uri=AK_SCHEMA.V1p4TimeInterval_max, domain=None, range=Optional[float])

slots.V1p4TimeInterval_unit = Slot(uri=AK_SCHEMA.V1p4TimeInterval_unit, name="V1p4TimeInterval_unit", curie=AK_SCHEMA.curie('V1p4TimeInterval_unit'),
                   model_uri=AK_SCHEMA.V1p4TimeInterval_unit, domain=None, range=Optional[Union[str, "V1p4Unit"]])

slots.V1p4PhysicalQuantity_quantity = Slot(uri=AK_SCHEMA.V1p4PhysicalQuantity_quantity, name="V1p4PhysicalQuantity_quantity", curie=AK_SCHEMA.curie('V1p4PhysicalQuantity_quantity'),
                   model_uri=AK_SCHEMA.V1p4PhysicalQuantity_quantity, domain=None, range=Optional[float])

slots.V1p4PhysicalQuantity_unit = Slot(uri=AK_SCHEMA.V1p4PhysicalQuantity_unit, name="V1p4PhysicalQuantity_unit", curie=AK_SCHEMA.curie('V1p4PhysicalQuantity_unit'),
                   model_uri=AK_SCHEMA.V1p4PhysicalQuantity_unit, domain=None, range=Optional[Union[str, "V1p4Unit"]])

slots.V1p4TimeQuantity_quantity = Slot(uri=AK_SCHEMA.V1p4TimeQuantity_quantity, name="V1p4TimeQuantity_quantity", curie=AK_SCHEMA.curie('V1p4TimeQuantity_quantity'),
                   model_uri=AK_SCHEMA.V1p4TimeQuantity_quantity, domain=None, range=Optional[float])

slots.V1p4TimeQuantity_unit = Slot(uri=AK_SCHEMA.V1p4TimeQuantity_unit, name="V1p4TimeQuantity_unit", curie=AK_SCHEMA.curie('V1p4TimeQuantity_unit'),
                   model_uri=AK_SCHEMA.V1p4TimeQuantity_unit, domain=None, range=Optional[Union[str, "V1p4Unit"]])

slots.V1p4Contributor_contributor_id = Slot(uri=AK_SCHEMA.V1p4Contributor_contributor_id, name="V1p4Contributor_contributor_id", curie=AK_SCHEMA.curie('V1p4Contributor_contributor_id'),
                   model_uri=AK_SCHEMA.V1p4Contributor_contributor_id, domain=None, range=str)

slots.V1p4Contributor_name = Slot(uri=AK_SCHEMA.V1p4Contributor_name, name="V1p4Contributor_name", curie=AK_SCHEMA.curie('V1p4Contributor_name'),
                   model_uri=AK_SCHEMA.V1p4Contributor_name, domain=None, range=str)

slots.V1p4Contributor_orcid_id = Slot(uri=AK_SCHEMA.V1p4Contributor_orcid_id, name="V1p4Contributor_orcid_id", curie=AK_SCHEMA.curie('V1p4Contributor_orcid_id'),
                   model_uri=AK_SCHEMA.V1p4Contributor_orcid_id, domain=None, range=Optional[Union[str, "V1p4OrcidId"]])

slots.V1p4Contributor_affiliation = Slot(uri=AK_SCHEMA.V1p4Contributor_affiliation, name="V1p4Contributor_affiliation", curie=AK_SCHEMA.curie('V1p4Contributor_affiliation'),
                   model_uri=AK_SCHEMA.V1p4Contributor_affiliation, domain=None, range=Optional[Union[str, "V1p4Affiliation"]])

slots.V1p4Contributor_affiliation_department = Slot(uri=AK_SCHEMA.V1p4Contributor_affiliation_department, name="V1p4Contributor_affiliation_department", curie=AK_SCHEMA.curie('V1p4Contributor_affiliation_department'),
                   model_uri=AK_SCHEMA.V1p4Contributor_affiliation_department, domain=None, range=Optional[str])

slots.V1p4Contributor_contributions = Slot(uri=AK_SCHEMA.V1p4Contributor_contributions, name="V1p4Contributor_contributions", curie=AK_SCHEMA.curie('V1p4Contributor_contributions'),
                   model_uri=AK_SCHEMA.V1p4Contributor_contributions, domain=None, range=Optional[Union[Union[dict, V1p4ContributorContribution], List[Union[dict, V1p4ContributorContribution]]]])

slots.V1p4ContributorContribution_role = Slot(uri=AK_SCHEMA.V1p4ContributorContribution_role, name="V1p4ContributorContribution_role", curie=AK_SCHEMA.curie('V1p4ContributorContribution_role'),
                   model_uri=AK_SCHEMA.V1p4ContributorContribution_role, domain=None, range=Union[str, "V1p4Role"])

slots.V1p4ContributorContribution_degree = Slot(uri=AK_SCHEMA.V1p4ContributorContribution_degree, name="V1p4ContributorContribution_degree", curie=AK_SCHEMA.curie('V1p4ContributorContribution_degree'),
                   model_uri=AK_SCHEMA.V1p4ContributorContribution_degree, domain=None, range=Optional[Union[str, "V1p4Degree"]])

slots.V1p4RearrangedSequence_sequence_id = Slot(uri=AK_SCHEMA.V1p4RearrangedSequence_sequence_id, name="V1p4RearrangedSequence_sequence_id", curie=AK_SCHEMA.curie('V1p4RearrangedSequence_sequence_id'),
                   model_uri=AK_SCHEMA.V1p4RearrangedSequence_sequence_id, domain=None, range=str)

slots.V1p4RearrangedSequence_sequence = Slot(uri=AK_SCHEMA.V1p4RearrangedSequence_sequence, name="V1p4RearrangedSequence_sequence", curie=AK_SCHEMA.curie('V1p4RearrangedSequence_sequence'),
                   model_uri=AK_SCHEMA.V1p4RearrangedSequence_sequence, domain=None, range=str)

slots.V1p4RearrangedSequence_derivation = Slot(uri=AK_SCHEMA.V1p4RearrangedSequence_derivation, name="V1p4RearrangedSequence_derivation", curie=AK_SCHEMA.curie('V1p4RearrangedSequence_derivation'),
                   model_uri=AK_SCHEMA.V1p4RearrangedSequence_derivation, domain=None, range=Union[str, "V1p4Derivation"])

slots.V1p4RearrangedSequence_observation_type = Slot(uri=AK_SCHEMA.V1p4RearrangedSequence_observation_type, name="V1p4RearrangedSequence_observation_type", curie=AK_SCHEMA.curie('V1p4RearrangedSequence_observation_type'),
                   model_uri=AK_SCHEMA.V1p4RearrangedSequence_observation_type, domain=None, range=Union[str, "V1p4ObservationType"])

slots.V1p4RearrangedSequence_curation = Slot(uri=AK_SCHEMA.V1p4RearrangedSequence_curation, name="V1p4RearrangedSequence_curation", curie=AK_SCHEMA.curie('V1p4RearrangedSequence_curation'),
                   model_uri=AK_SCHEMA.V1p4RearrangedSequence_curation, domain=None, range=Optional[str])

slots.V1p4RearrangedSequence_repository_name = Slot(uri=AK_SCHEMA.V1p4RearrangedSequence_repository_name, name="V1p4RearrangedSequence_repository_name", curie=AK_SCHEMA.curie('V1p4RearrangedSequence_repository_name'),
                   model_uri=AK_SCHEMA.V1p4RearrangedSequence_repository_name, domain=None, range=str)

slots.V1p4RearrangedSequence_repository_ref = Slot(uri=AK_SCHEMA.V1p4RearrangedSequence_repository_ref, name="V1p4RearrangedSequence_repository_ref", curie=AK_SCHEMA.curie('V1p4RearrangedSequence_repository_ref'),
                   model_uri=AK_SCHEMA.V1p4RearrangedSequence_repository_ref, domain=None, range=Optional[str])

slots.V1p4RearrangedSequence_deposited_version = Slot(uri=AK_SCHEMA.V1p4RearrangedSequence_deposited_version, name="V1p4RearrangedSequence_deposited_version", curie=AK_SCHEMA.curie('V1p4RearrangedSequence_deposited_version'),
                   model_uri=AK_SCHEMA.V1p4RearrangedSequence_deposited_version, domain=None, range=str)

slots.V1p4RearrangedSequence_sequence_start = Slot(uri=AK_SCHEMA.V1p4RearrangedSequence_sequence_start, name="V1p4RearrangedSequence_sequence_start", curie=AK_SCHEMA.curie('V1p4RearrangedSequence_sequence_start'),
                   model_uri=AK_SCHEMA.V1p4RearrangedSequence_sequence_start, domain=None, range=Optional[int])

slots.V1p4RearrangedSequence_sequence_end = Slot(uri=AK_SCHEMA.V1p4RearrangedSequence_sequence_end, name="V1p4RearrangedSequence_sequence_end", curie=AK_SCHEMA.curie('V1p4RearrangedSequence_sequence_end'),
                   model_uri=AK_SCHEMA.V1p4RearrangedSequence_sequence_end, domain=None, range=Optional[int])

slots.V1p4UnrearrangedSequence_sequence_id = Slot(uri=AK_SCHEMA.V1p4UnrearrangedSequence_sequence_id, name="V1p4UnrearrangedSequence_sequence_id", curie=AK_SCHEMA.curie('V1p4UnrearrangedSequence_sequence_id'),
                   model_uri=AK_SCHEMA.V1p4UnrearrangedSequence_sequence_id, domain=None, range=str)

slots.V1p4UnrearrangedSequence_sequence = Slot(uri=AK_SCHEMA.V1p4UnrearrangedSequence_sequence, name="V1p4UnrearrangedSequence_sequence", curie=AK_SCHEMA.curie('V1p4UnrearrangedSequence_sequence'),
                   model_uri=AK_SCHEMA.V1p4UnrearrangedSequence_sequence, domain=None, range=str)

slots.V1p4UnrearrangedSequence_curation = Slot(uri=AK_SCHEMA.V1p4UnrearrangedSequence_curation, name="V1p4UnrearrangedSequence_curation", curie=AK_SCHEMA.curie('V1p4UnrearrangedSequence_curation'),
                   model_uri=AK_SCHEMA.V1p4UnrearrangedSequence_curation, domain=None, range=Optional[str])

slots.V1p4UnrearrangedSequence_repository_name = Slot(uri=AK_SCHEMA.V1p4UnrearrangedSequence_repository_name, name="V1p4UnrearrangedSequence_repository_name", curie=AK_SCHEMA.curie('V1p4UnrearrangedSequence_repository_name'),
                   model_uri=AK_SCHEMA.V1p4UnrearrangedSequence_repository_name, domain=None, range=str)

slots.V1p4UnrearrangedSequence_repository_ref = Slot(uri=AK_SCHEMA.V1p4UnrearrangedSequence_repository_ref, name="V1p4UnrearrangedSequence_repository_ref", curie=AK_SCHEMA.curie('V1p4UnrearrangedSequence_repository_ref'),
                   model_uri=AK_SCHEMA.V1p4UnrearrangedSequence_repository_ref, domain=None, range=Optional[str])

slots.V1p4UnrearrangedSequence_patch_no = Slot(uri=AK_SCHEMA.V1p4UnrearrangedSequence_patch_no, name="V1p4UnrearrangedSequence_patch_no", curie=AK_SCHEMA.curie('V1p4UnrearrangedSequence_patch_no'),
                   model_uri=AK_SCHEMA.V1p4UnrearrangedSequence_patch_no, domain=None, range=Optional[str])

slots.V1p4UnrearrangedSequence_gff_seqid = Slot(uri=AK_SCHEMA.V1p4UnrearrangedSequence_gff_seqid, name="V1p4UnrearrangedSequence_gff_seqid", curie=AK_SCHEMA.curie('V1p4UnrearrangedSequence_gff_seqid'),
                   model_uri=AK_SCHEMA.V1p4UnrearrangedSequence_gff_seqid, domain=None, range=str)

slots.V1p4UnrearrangedSequence_gff_start = Slot(uri=AK_SCHEMA.V1p4UnrearrangedSequence_gff_start, name="V1p4UnrearrangedSequence_gff_start", curie=AK_SCHEMA.curie('V1p4UnrearrangedSequence_gff_start'),
                   model_uri=AK_SCHEMA.V1p4UnrearrangedSequence_gff_start, domain=None, range=int)

slots.V1p4UnrearrangedSequence_gff_end = Slot(uri=AK_SCHEMA.V1p4UnrearrangedSequence_gff_end, name="V1p4UnrearrangedSequence_gff_end", curie=AK_SCHEMA.curie('V1p4UnrearrangedSequence_gff_end'),
                   model_uri=AK_SCHEMA.V1p4UnrearrangedSequence_gff_end, domain=None, range=int)

slots.V1p4UnrearrangedSequence_strand = Slot(uri=AK_SCHEMA.V1p4UnrearrangedSequence_strand, name="V1p4UnrearrangedSequence_strand", curie=AK_SCHEMA.curie('V1p4UnrearrangedSequence_strand'),
                   model_uri=AK_SCHEMA.V1p4UnrearrangedSequence_strand, domain=None, range=Union[str, "V1p4Strand"])

slots.V1p4SequenceDelineationV_sequence_delineation_id = Slot(uri=AK_SCHEMA.V1p4SequenceDelineationV_sequence_delineation_id, name="V1p4SequenceDelineationV_sequence_delineation_id", curie=AK_SCHEMA.curie('V1p4SequenceDelineationV_sequence_delineation_id'),
                   model_uri=AK_SCHEMA.V1p4SequenceDelineationV_sequence_delineation_id, domain=None, range=str)

slots.V1p4SequenceDelineationV_delineation_scheme = Slot(uri=AK_SCHEMA.V1p4SequenceDelineationV_delineation_scheme, name="V1p4SequenceDelineationV_delineation_scheme", curie=AK_SCHEMA.curie('V1p4SequenceDelineationV_delineation_scheme'),
                   model_uri=AK_SCHEMA.V1p4SequenceDelineationV_delineation_scheme, domain=None, range=str)

slots.V1p4SequenceDelineationV_unaligned_sequence = Slot(uri=AK_SCHEMA.V1p4SequenceDelineationV_unaligned_sequence, name="V1p4SequenceDelineationV_unaligned_sequence", curie=AK_SCHEMA.curie('V1p4SequenceDelineationV_unaligned_sequence'),
                   model_uri=AK_SCHEMA.V1p4SequenceDelineationV_unaligned_sequence, domain=None, range=Optional[str])

slots.V1p4SequenceDelineationV_aligned_sequence = Slot(uri=AK_SCHEMA.V1p4SequenceDelineationV_aligned_sequence, name="V1p4SequenceDelineationV_aligned_sequence", curie=AK_SCHEMA.curie('V1p4SequenceDelineationV_aligned_sequence'),
                   model_uri=AK_SCHEMA.V1p4SequenceDelineationV_aligned_sequence, domain=None, range=Optional[str])

slots.V1p4SequenceDelineationV_fwr1_start = Slot(uri=AK_SCHEMA.V1p4SequenceDelineationV_fwr1_start, name="V1p4SequenceDelineationV_fwr1_start", curie=AK_SCHEMA.curie('V1p4SequenceDelineationV_fwr1_start'),
                   model_uri=AK_SCHEMA.V1p4SequenceDelineationV_fwr1_start, domain=None, range=int)

slots.V1p4SequenceDelineationV_fwr1_end = Slot(uri=AK_SCHEMA.V1p4SequenceDelineationV_fwr1_end, name="V1p4SequenceDelineationV_fwr1_end", curie=AK_SCHEMA.curie('V1p4SequenceDelineationV_fwr1_end'),
                   model_uri=AK_SCHEMA.V1p4SequenceDelineationV_fwr1_end, domain=None, range=int)

slots.V1p4SequenceDelineationV_cdr1_start = Slot(uri=AK_SCHEMA.V1p4SequenceDelineationV_cdr1_start, name="V1p4SequenceDelineationV_cdr1_start", curie=AK_SCHEMA.curie('V1p4SequenceDelineationV_cdr1_start'),
                   model_uri=AK_SCHEMA.V1p4SequenceDelineationV_cdr1_start, domain=None, range=int)

slots.V1p4SequenceDelineationV_cdr1_end = Slot(uri=AK_SCHEMA.V1p4SequenceDelineationV_cdr1_end, name="V1p4SequenceDelineationV_cdr1_end", curie=AK_SCHEMA.curie('V1p4SequenceDelineationV_cdr1_end'),
                   model_uri=AK_SCHEMA.V1p4SequenceDelineationV_cdr1_end, domain=None, range=int)

slots.V1p4SequenceDelineationV_fwr2_start = Slot(uri=AK_SCHEMA.V1p4SequenceDelineationV_fwr2_start, name="V1p4SequenceDelineationV_fwr2_start", curie=AK_SCHEMA.curie('V1p4SequenceDelineationV_fwr2_start'),
                   model_uri=AK_SCHEMA.V1p4SequenceDelineationV_fwr2_start, domain=None, range=int)

slots.V1p4SequenceDelineationV_fwr2_end = Slot(uri=AK_SCHEMA.V1p4SequenceDelineationV_fwr2_end, name="V1p4SequenceDelineationV_fwr2_end", curie=AK_SCHEMA.curie('V1p4SequenceDelineationV_fwr2_end'),
                   model_uri=AK_SCHEMA.V1p4SequenceDelineationV_fwr2_end, domain=None, range=int)

slots.V1p4SequenceDelineationV_cdr2_start = Slot(uri=AK_SCHEMA.V1p4SequenceDelineationV_cdr2_start, name="V1p4SequenceDelineationV_cdr2_start", curie=AK_SCHEMA.curie('V1p4SequenceDelineationV_cdr2_start'),
                   model_uri=AK_SCHEMA.V1p4SequenceDelineationV_cdr2_start, domain=None, range=int)

slots.V1p4SequenceDelineationV_cdr2_end = Slot(uri=AK_SCHEMA.V1p4SequenceDelineationV_cdr2_end, name="V1p4SequenceDelineationV_cdr2_end", curie=AK_SCHEMA.curie('V1p4SequenceDelineationV_cdr2_end'),
                   model_uri=AK_SCHEMA.V1p4SequenceDelineationV_cdr2_end, domain=None, range=int)

slots.V1p4SequenceDelineationV_fwr3_start = Slot(uri=AK_SCHEMA.V1p4SequenceDelineationV_fwr3_start, name="V1p4SequenceDelineationV_fwr3_start", curie=AK_SCHEMA.curie('V1p4SequenceDelineationV_fwr3_start'),
                   model_uri=AK_SCHEMA.V1p4SequenceDelineationV_fwr3_start, domain=None, range=int)

slots.V1p4SequenceDelineationV_fwr3_end = Slot(uri=AK_SCHEMA.V1p4SequenceDelineationV_fwr3_end, name="V1p4SequenceDelineationV_fwr3_end", curie=AK_SCHEMA.curie('V1p4SequenceDelineationV_fwr3_end'),
                   model_uri=AK_SCHEMA.V1p4SequenceDelineationV_fwr3_end, domain=None, range=int)

slots.V1p4SequenceDelineationV_cdr3_start = Slot(uri=AK_SCHEMA.V1p4SequenceDelineationV_cdr3_start, name="V1p4SequenceDelineationV_cdr3_start", curie=AK_SCHEMA.curie('V1p4SequenceDelineationV_cdr3_start'),
                   model_uri=AK_SCHEMA.V1p4SequenceDelineationV_cdr3_start, domain=None, range=int)

slots.V1p4SequenceDelineationV_alignment_labels = Slot(uri=AK_SCHEMA.V1p4SequenceDelineationV_alignment_labels, name="V1p4SequenceDelineationV_alignment_labels", curie=AK_SCHEMA.curie('V1p4SequenceDelineationV_alignment_labels'),
                   model_uri=AK_SCHEMA.V1p4SequenceDelineationV_alignment_labels, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4AlleleDescription_allele_description_id = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_allele_description_id, name="V1p4AlleleDescription_allele_description_id", curie=AK_SCHEMA.curie('V1p4AlleleDescription_allele_description_id'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_allele_description_id, domain=None, range=str)

slots.V1p4AlleleDescription_allele_description_ref = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_allele_description_ref, name="V1p4AlleleDescription_allele_description_ref", curie=AK_SCHEMA.curie('V1p4AlleleDescription_allele_description_ref'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_allele_description_ref, domain=None, range=Optional[str])

slots.V1p4AlleleDescription_acknowledgements = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_acknowledgements, name="V1p4AlleleDescription_acknowledgements", curie=AK_SCHEMA.curie('V1p4AlleleDescription_acknowledgements'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_acknowledgements, domain=None, range=Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]])

slots.V1p4AlleleDescription_release_version = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_release_version, name="V1p4AlleleDescription_release_version", curie=AK_SCHEMA.curie('V1p4AlleleDescription_release_version'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_release_version, domain=None, range=int)

slots.V1p4AlleleDescription_release_date = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_release_date, name="V1p4AlleleDescription_release_date", curie=AK_SCHEMA.curie('V1p4AlleleDescription_release_date'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_release_date, domain=None, range=str)

slots.V1p4AlleleDescription_release_description = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_release_description, name="V1p4AlleleDescription_release_description", curie=AK_SCHEMA.curie('V1p4AlleleDescription_release_description'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_release_description, domain=None, range=str)

slots.V1p4AlleleDescription_label = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_label, name="V1p4AlleleDescription_label", curie=AK_SCHEMA.curie('V1p4AlleleDescription_label'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_label, domain=None, range=Optional[str])

slots.V1p4AlleleDescription_sequence = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_sequence, name="V1p4AlleleDescription_sequence", curie=AK_SCHEMA.curie('V1p4AlleleDescription_sequence'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_sequence, domain=None, range=str)

slots.V1p4AlleleDescription_coding_sequence = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_coding_sequence, name="V1p4AlleleDescription_coding_sequence", curie=AK_SCHEMA.curie('V1p4AlleleDescription_coding_sequence'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_coding_sequence, domain=None, range=str)

slots.V1p4AlleleDescription_aliases = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_aliases, name="V1p4AlleleDescription_aliases", curie=AK_SCHEMA.curie('V1p4AlleleDescription_aliases'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_aliases, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4AlleleDescription_locus = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_locus, name="V1p4AlleleDescription_locus", curie=AK_SCHEMA.curie('V1p4AlleleDescription_locus'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_locus, domain=None, range=Union[str, "V1p4Locus"])

slots.V1p4AlleleDescription_chromosome = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_chromosome, name="V1p4AlleleDescription_chromosome", curie=AK_SCHEMA.curie('V1p4AlleleDescription_chromosome'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_chromosome, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_sequence_type = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_sequence_type, name="V1p4AlleleDescription_sequence_type", curie=AK_SCHEMA.curie('V1p4AlleleDescription_sequence_type'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_sequence_type, domain=None, range=Union[str, "V1p4SequenceType"])

slots.V1p4AlleleDescription_functional = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_functional, name="V1p4AlleleDescription_functional", curie=AK_SCHEMA.curie('V1p4AlleleDescription_functional'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_functional, domain=None, range=Union[bool, Bool])

slots.V1p4AlleleDescription_inference_type = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_inference_type, name="V1p4AlleleDescription_inference_type", curie=AK_SCHEMA.curie('V1p4AlleleDescription_inference_type'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_inference_type, domain=None, range=Union[str, "V1p4InferenceType"])

slots.V1p4AlleleDescription_species = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_species, name="V1p4AlleleDescription_species", curie=AK_SCHEMA.curie('V1p4AlleleDescription_species'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_species, domain=None, range=Union[str, "V1p4Species"])

slots.V1p4AlleleDescription_species_subgroup = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_species_subgroup, name="V1p4AlleleDescription_species_subgroup", curie=AK_SCHEMA.curie('V1p4AlleleDescription_species_subgroup'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_species_subgroup, domain=None, range=Optional[str])

slots.V1p4AlleleDescription_species_subgroup_type = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_species_subgroup_type, name="V1p4AlleleDescription_species_subgroup_type", curie=AK_SCHEMA.curie('V1p4AlleleDescription_species_subgroup_type'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_species_subgroup_type, domain=None, range=Optional[Union[str, "V1p4SpeciesSubgroupType"]])

slots.V1p4AlleleDescription_status = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_status, name="V1p4AlleleDescription_status", curie=AK_SCHEMA.curie('V1p4AlleleDescription_status'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_status, domain=None, range=Optional[Union[str, "V1p4Status"]])

slots.V1p4AlleleDescription_subgroup_designation = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_subgroup_designation, name="V1p4AlleleDescription_subgroup_designation", curie=AK_SCHEMA.curie('V1p4AlleleDescription_subgroup_designation'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_subgroup_designation, domain=None, range=Optional[str])

slots.V1p4AlleleDescription_gene_designation = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_gene_designation, name="V1p4AlleleDescription_gene_designation", curie=AK_SCHEMA.curie('V1p4AlleleDescription_gene_designation'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_gene_designation, domain=None, range=Optional[str])

slots.V1p4AlleleDescription_allele_designation = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_allele_designation, name="V1p4AlleleDescription_allele_designation", curie=AK_SCHEMA.curie('V1p4AlleleDescription_allele_designation'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_allele_designation, domain=None, range=Optional[str])

slots.V1p4AlleleDescription_allele_similarity_cluster_designation = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_allele_similarity_cluster_designation, name="V1p4AlleleDescription_allele_similarity_cluster_designation", curie=AK_SCHEMA.curie('V1p4AlleleDescription_allele_similarity_cluster_designation'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_allele_similarity_cluster_designation, domain=None, range=Optional[str])

slots.V1p4AlleleDescription_allele_similarity_cluster_member_id = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_allele_similarity_cluster_member_id, name="V1p4AlleleDescription_allele_similarity_cluster_member_id", curie=AK_SCHEMA.curie('V1p4AlleleDescription_allele_similarity_cluster_member_id'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_allele_similarity_cluster_member_id, domain=None, range=Optional[str])

slots.V1p4AlleleDescription_j_codon_frame = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_j_codon_frame, name="V1p4AlleleDescription_j_codon_frame", curie=AK_SCHEMA.curie('V1p4AlleleDescription_j_codon_frame'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_j_codon_frame, domain=None, range=Optional[Union[str, "V1p4JCodonFrame"]])

slots.V1p4AlleleDescription_gene_start = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_gene_start, name="V1p4AlleleDescription_gene_start", curie=AK_SCHEMA.curie('V1p4AlleleDescription_gene_start'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_gene_start, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_gene_end = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_gene_end, name="V1p4AlleleDescription_gene_end", curie=AK_SCHEMA.curie('V1p4AlleleDescription_gene_end'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_gene_end, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_utr_5_prime_start = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_utr_5_prime_start, name="V1p4AlleleDescription_utr_5_prime_start", curie=AK_SCHEMA.curie('V1p4AlleleDescription_utr_5_prime_start'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_utr_5_prime_start, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_utr_5_prime_end = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_utr_5_prime_end, name="V1p4AlleleDescription_utr_5_prime_end", curie=AK_SCHEMA.curie('V1p4AlleleDescription_utr_5_prime_end'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_utr_5_prime_end, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_leader_1_start = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_leader_1_start, name="V1p4AlleleDescription_leader_1_start", curie=AK_SCHEMA.curie('V1p4AlleleDescription_leader_1_start'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_leader_1_start, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_leader_1_end = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_leader_1_end, name="V1p4AlleleDescription_leader_1_end", curie=AK_SCHEMA.curie('V1p4AlleleDescription_leader_1_end'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_leader_1_end, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_leader_2_start = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_leader_2_start, name="V1p4AlleleDescription_leader_2_start", curie=AK_SCHEMA.curie('V1p4AlleleDescription_leader_2_start'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_leader_2_start, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_leader_2_end = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_leader_2_end, name="V1p4AlleleDescription_leader_2_end", curie=AK_SCHEMA.curie('V1p4AlleleDescription_leader_2_end'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_leader_2_end, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_v_rs_start = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_v_rs_start, name="V1p4AlleleDescription_v_rs_start", curie=AK_SCHEMA.curie('V1p4AlleleDescription_v_rs_start'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_v_rs_start, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_v_rs_end = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_v_rs_end, name="V1p4AlleleDescription_v_rs_end", curie=AK_SCHEMA.curie('V1p4AlleleDescription_v_rs_end'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_v_rs_end, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_d_rs_3_prime_start = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_d_rs_3_prime_start, name="V1p4AlleleDescription_d_rs_3_prime_start", curie=AK_SCHEMA.curie('V1p4AlleleDescription_d_rs_3_prime_start'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_d_rs_3_prime_start, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_d_rs_3_prime_end = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_d_rs_3_prime_end, name="V1p4AlleleDescription_d_rs_3_prime_end", curie=AK_SCHEMA.curie('V1p4AlleleDescription_d_rs_3_prime_end'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_d_rs_3_prime_end, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_d_rs_5_prime_start = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_d_rs_5_prime_start, name="V1p4AlleleDescription_d_rs_5_prime_start", curie=AK_SCHEMA.curie('V1p4AlleleDescription_d_rs_5_prime_start'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_d_rs_5_prime_start, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_d_rs_5_prime_end = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_d_rs_5_prime_end, name="V1p4AlleleDescription_d_rs_5_prime_end", curie=AK_SCHEMA.curie('V1p4AlleleDescription_d_rs_5_prime_end'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_d_rs_5_prime_end, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_j_cdr3_end = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_j_cdr3_end, name="V1p4AlleleDescription_j_cdr3_end", curie=AK_SCHEMA.curie('V1p4AlleleDescription_j_cdr3_end'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_j_cdr3_end, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_j_rs_start = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_j_rs_start, name="V1p4AlleleDescription_j_rs_start", curie=AK_SCHEMA.curie('V1p4AlleleDescription_j_rs_start'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_j_rs_start, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_j_rs_end = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_j_rs_end, name="V1p4AlleleDescription_j_rs_end", curie=AK_SCHEMA.curie('V1p4AlleleDescription_j_rs_end'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_j_rs_end, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_j_donor_splice = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_j_donor_splice, name="V1p4AlleleDescription_j_donor_splice", curie=AK_SCHEMA.curie('V1p4AlleleDescription_j_donor_splice'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_j_donor_splice, domain=None, range=Optional[int])

slots.V1p4AlleleDescription_v_gene_delineations = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_v_gene_delineations, name="V1p4AlleleDescription_v_gene_delineations", curie=AK_SCHEMA.curie('V1p4AlleleDescription_v_gene_delineations'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_v_gene_delineations, domain=None, range=Optional[Union[Union[dict, V1p4SequenceDelineationV], List[Union[dict, V1p4SequenceDelineationV]]]])

slots.V1p4AlleleDescription_unrearranged_support = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_unrearranged_support, name="V1p4AlleleDescription_unrearranged_support", curie=AK_SCHEMA.curie('V1p4AlleleDescription_unrearranged_support'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_unrearranged_support, domain=None, range=Optional[Union[Union[dict, V1p4UnrearrangedSequence], List[Union[dict, V1p4UnrearrangedSequence]]]])

slots.V1p4AlleleDescription_rearranged_support = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_rearranged_support, name="V1p4AlleleDescription_rearranged_support", curie=AK_SCHEMA.curie('V1p4AlleleDescription_rearranged_support'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_rearranged_support, domain=None, range=Optional[Union[Union[dict, V1p4RearrangedSequence], List[Union[dict, V1p4RearrangedSequence]]]])

slots.V1p4AlleleDescription_paralogs = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_paralogs, name="V1p4AlleleDescription_paralogs", curie=AK_SCHEMA.curie('V1p4AlleleDescription_paralogs'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_paralogs, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4AlleleDescription_curation = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_curation, name="V1p4AlleleDescription_curation", curie=AK_SCHEMA.curie('V1p4AlleleDescription_curation'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_curation, domain=None, range=Optional[str])

slots.V1p4AlleleDescription_curational_tags = Slot(uri=AK_SCHEMA.V1p4AlleleDescription_curational_tags, name="V1p4AlleleDescription_curational_tags", curie=AK_SCHEMA.curie('V1p4AlleleDescription_curational_tags'),
                   model_uri=AK_SCHEMA.V1p4AlleleDescription_curational_tags, domain=None, range=Optional[Union[Union[str, "V1p4CurationalTags"], List[Union[str, "V1p4CurationalTags"]]]])

slots.V1p4GermlineSet_germline_set_id = Slot(uri=AK_SCHEMA.V1p4GermlineSet_germline_set_id, name="V1p4GermlineSet_germline_set_id", curie=AK_SCHEMA.curie('V1p4GermlineSet_germline_set_id'),
                   model_uri=AK_SCHEMA.V1p4GermlineSet_germline_set_id, domain=None, range=str)

slots.V1p4GermlineSet_acknowledgements = Slot(uri=AK_SCHEMA.V1p4GermlineSet_acknowledgements, name="V1p4GermlineSet_acknowledgements", curie=AK_SCHEMA.curie('V1p4GermlineSet_acknowledgements'),
                   model_uri=AK_SCHEMA.V1p4GermlineSet_acknowledgements, domain=None, range=Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]])

slots.V1p4GermlineSet_release_version = Slot(uri=AK_SCHEMA.V1p4GermlineSet_release_version, name="V1p4GermlineSet_release_version", curie=AK_SCHEMA.curie('V1p4GermlineSet_release_version'),
                   model_uri=AK_SCHEMA.V1p4GermlineSet_release_version, domain=None, range=int)

slots.V1p4GermlineSet_release_description = Slot(uri=AK_SCHEMA.V1p4GermlineSet_release_description, name="V1p4GermlineSet_release_description", curie=AK_SCHEMA.curie('V1p4GermlineSet_release_description'),
                   model_uri=AK_SCHEMA.V1p4GermlineSet_release_description, domain=None, range=str)

slots.V1p4GermlineSet_release_date = Slot(uri=AK_SCHEMA.V1p4GermlineSet_release_date, name="V1p4GermlineSet_release_date", curie=AK_SCHEMA.curie('V1p4GermlineSet_release_date'),
                   model_uri=AK_SCHEMA.V1p4GermlineSet_release_date, domain=None, range=str)

slots.V1p4GermlineSet_germline_set_name = Slot(uri=AK_SCHEMA.V1p4GermlineSet_germline_set_name, name="V1p4GermlineSet_germline_set_name", curie=AK_SCHEMA.curie('V1p4GermlineSet_germline_set_name'),
                   model_uri=AK_SCHEMA.V1p4GermlineSet_germline_set_name, domain=None, range=str)

slots.V1p4GermlineSet_germline_set_ref = Slot(uri=AK_SCHEMA.V1p4GermlineSet_germline_set_ref, name="V1p4GermlineSet_germline_set_ref", curie=AK_SCHEMA.curie('V1p4GermlineSet_germline_set_ref'),
                   model_uri=AK_SCHEMA.V1p4GermlineSet_germline_set_ref, domain=None, range=str)

slots.V1p4GermlineSet_pub_ids = Slot(uri=AK_SCHEMA.V1p4GermlineSet_pub_ids, name="V1p4GermlineSet_pub_ids", curie=AK_SCHEMA.curie('V1p4GermlineSet_pub_ids'),
                   model_uri=AK_SCHEMA.V1p4GermlineSet_pub_ids, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4GermlineSet_species = Slot(uri=AK_SCHEMA.V1p4GermlineSet_species, name="V1p4GermlineSet_species", curie=AK_SCHEMA.curie('V1p4GermlineSet_species'),
                   model_uri=AK_SCHEMA.V1p4GermlineSet_species, domain=None, range=Union[str, "V1p4Species"])

slots.V1p4GermlineSet_species_subgroup = Slot(uri=AK_SCHEMA.V1p4GermlineSet_species_subgroup, name="V1p4GermlineSet_species_subgroup", curie=AK_SCHEMA.curie('V1p4GermlineSet_species_subgroup'),
                   model_uri=AK_SCHEMA.V1p4GermlineSet_species_subgroup, domain=None, range=Optional[str])

slots.V1p4GermlineSet_species_subgroup_type = Slot(uri=AK_SCHEMA.V1p4GermlineSet_species_subgroup_type, name="V1p4GermlineSet_species_subgroup_type", curie=AK_SCHEMA.curie('V1p4GermlineSet_species_subgroup_type'),
                   model_uri=AK_SCHEMA.V1p4GermlineSet_species_subgroup_type, domain=None, range=Optional[Union[str, "V1p4SpeciesSubgroupType"]])

slots.V1p4GermlineSet_locus = Slot(uri=AK_SCHEMA.V1p4GermlineSet_locus, name="V1p4GermlineSet_locus", curie=AK_SCHEMA.curie('V1p4GermlineSet_locus'),
                   model_uri=AK_SCHEMA.V1p4GermlineSet_locus, domain=None, range=Union[str, "V1p4Locus"])

slots.V1p4GermlineSet_allele_descriptions = Slot(uri=AK_SCHEMA.V1p4GermlineSet_allele_descriptions, name="V1p4GermlineSet_allele_descriptions", curie=AK_SCHEMA.curie('V1p4GermlineSet_allele_descriptions'),
                   model_uri=AK_SCHEMA.V1p4GermlineSet_allele_descriptions, domain=None, range=Union[Union[dict, V1p4AlleleDescription], List[Union[dict, V1p4AlleleDescription]]])

slots.V1p4GermlineSet_curation = Slot(uri=AK_SCHEMA.V1p4GermlineSet_curation, name="V1p4GermlineSet_curation", curie=AK_SCHEMA.curie('V1p4GermlineSet_curation'),
                   model_uri=AK_SCHEMA.V1p4GermlineSet_curation, domain=None, range=Optional[str])

slots.V1p4GenotypeSet_receptor_genotype_set_id = Slot(uri=AK_SCHEMA.V1p4GenotypeSet_receptor_genotype_set_id, name="V1p4GenotypeSet_receptor_genotype_set_id", curie=AK_SCHEMA.curie('V1p4GenotypeSet_receptor_genotype_set_id'),
                   model_uri=AK_SCHEMA.V1p4GenotypeSet_receptor_genotype_set_id, domain=None, range=str)

slots.V1p4GenotypeSet_genotype_class_list = Slot(uri=AK_SCHEMA.V1p4GenotypeSet_genotype_class_list, name="V1p4GenotypeSet_genotype_class_list", curie=AK_SCHEMA.curie('V1p4GenotypeSet_genotype_class_list'),
                   model_uri=AK_SCHEMA.V1p4GenotypeSet_genotype_class_list, domain=None, range=Optional[Union[Union[dict, V1p4Genotype], List[Union[dict, V1p4Genotype]]]])

slots.V1p4Genotype_receptor_genotype_id = Slot(uri=AK_SCHEMA.V1p4Genotype_receptor_genotype_id, name="V1p4Genotype_receptor_genotype_id", curie=AK_SCHEMA.curie('V1p4Genotype_receptor_genotype_id'),
                   model_uri=AK_SCHEMA.V1p4Genotype_receptor_genotype_id, domain=None, range=str)

slots.V1p4Genotype_locus = Slot(uri=AK_SCHEMA.V1p4Genotype_locus, name="V1p4Genotype_locus", curie=AK_SCHEMA.curie('V1p4Genotype_locus'),
                   model_uri=AK_SCHEMA.V1p4Genotype_locus, domain=None, range=Union[str, "V1p4Locus"])

slots.V1p4Genotype_documented_alleles = Slot(uri=AK_SCHEMA.V1p4Genotype_documented_alleles, name="V1p4Genotype_documented_alleles", curie=AK_SCHEMA.curie('V1p4Genotype_documented_alleles'),
                   model_uri=AK_SCHEMA.V1p4Genotype_documented_alleles, domain=None, range=Optional[Union[Union[dict, V1p4DocumentedAllele], List[Union[dict, V1p4DocumentedAllele]]]])

slots.V1p4Genotype_undocumented_alleles = Slot(uri=AK_SCHEMA.V1p4Genotype_undocumented_alleles, name="V1p4Genotype_undocumented_alleles", curie=AK_SCHEMA.curie('V1p4Genotype_undocumented_alleles'),
                   model_uri=AK_SCHEMA.V1p4Genotype_undocumented_alleles, domain=None, range=Optional[Union[Union[dict, V1p4UndocumentedAllele], List[Union[dict, V1p4UndocumentedAllele]]]])

slots.V1p4Genotype_deleted_genes = Slot(uri=AK_SCHEMA.V1p4Genotype_deleted_genes, name="V1p4Genotype_deleted_genes", curie=AK_SCHEMA.curie('V1p4Genotype_deleted_genes'),
                   model_uri=AK_SCHEMA.V1p4Genotype_deleted_genes, domain=None, range=Optional[Union[Union[dict, V1p4DeletedGene], List[Union[dict, V1p4DeletedGene]]]])

slots.V1p4Genotype_inference_process = Slot(uri=AK_SCHEMA.V1p4Genotype_inference_process, name="V1p4Genotype_inference_process", curie=AK_SCHEMA.curie('V1p4Genotype_inference_process'),
                   model_uri=AK_SCHEMA.V1p4Genotype_inference_process, domain=None, range=Optional[Union[str, "V1p4InferenceProcess"]])

slots.V1p4DocumentedAllele_label = Slot(uri=AK_SCHEMA.V1p4DocumentedAllele_label, name="V1p4DocumentedAllele_label", curie=AK_SCHEMA.curie('V1p4DocumentedAllele_label'),
                   model_uri=AK_SCHEMA.V1p4DocumentedAllele_label, domain=None, range=str)

slots.V1p4DocumentedAllele_germline_set_ref = Slot(uri=AK_SCHEMA.V1p4DocumentedAllele_germline_set_ref, name="V1p4DocumentedAllele_germline_set_ref", curie=AK_SCHEMA.curie('V1p4DocumentedAllele_germline_set_ref'),
                   model_uri=AK_SCHEMA.V1p4DocumentedAllele_germline_set_ref, domain=None, range=str)

slots.V1p4DocumentedAllele_phasing = Slot(uri=AK_SCHEMA.V1p4DocumentedAllele_phasing, name="V1p4DocumentedAllele_phasing", curie=AK_SCHEMA.curie('V1p4DocumentedAllele_phasing'),
                   model_uri=AK_SCHEMA.V1p4DocumentedAllele_phasing, domain=None, range=Optional[int])

slots.V1p4UndocumentedAllele_allele_name = Slot(uri=AK_SCHEMA.V1p4UndocumentedAllele_allele_name, name="V1p4UndocumentedAllele_allele_name", curie=AK_SCHEMA.curie('V1p4UndocumentedAllele_allele_name'),
                   model_uri=AK_SCHEMA.V1p4UndocumentedAllele_allele_name, domain=None, range=str)

slots.V1p4UndocumentedAllele_sequence = Slot(uri=AK_SCHEMA.V1p4UndocumentedAllele_sequence, name="V1p4UndocumentedAllele_sequence", curie=AK_SCHEMA.curie('V1p4UndocumentedAllele_sequence'),
                   model_uri=AK_SCHEMA.V1p4UndocumentedAllele_sequence, domain=None, range=str)

slots.V1p4UndocumentedAllele_phasing = Slot(uri=AK_SCHEMA.V1p4UndocumentedAllele_phasing, name="V1p4UndocumentedAllele_phasing", curie=AK_SCHEMA.curie('V1p4UndocumentedAllele_phasing'),
                   model_uri=AK_SCHEMA.V1p4UndocumentedAllele_phasing, domain=None, range=Optional[int])

slots.V1p4DeletedGene_label = Slot(uri=AK_SCHEMA.V1p4DeletedGene_label, name="V1p4DeletedGene_label", curie=AK_SCHEMA.curie('V1p4DeletedGene_label'),
                   model_uri=AK_SCHEMA.V1p4DeletedGene_label, domain=None, range=str)

slots.V1p4DeletedGene_germline_set_ref = Slot(uri=AK_SCHEMA.V1p4DeletedGene_germline_set_ref, name="V1p4DeletedGene_germline_set_ref", curie=AK_SCHEMA.curie('V1p4DeletedGene_germline_set_ref'),
                   model_uri=AK_SCHEMA.V1p4DeletedGene_germline_set_ref, domain=None, range=str)

slots.V1p4DeletedGene_phasing = Slot(uri=AK_SCHEMA.V1p4DeletedGene_phasing, name="V1p4DeletedGene_phasing", curie=AK_SCHEMA.curie('V1p4DeletedGene_phasing'),
                   model_uri=AK_SCHEMA.V1p4DeletedGene_phasing, domain=None, range=Optional[int])

slots.V1p4MHCGenotypeSet_mhc_genotype_set_id = Slot(uri=AK_SCHEMA.V1p4MHCGenotypeSet_mhc_genotype_set_id, name="V1p4MHCGenotypeSet_mhc_genotype_set_id", curie=AK_SCHEMA.curie('V1p4MHCGenotypeSet_mhc_genotype_set_id'),
                   model_uri=AK_SCHEMA.V1p4MHCGenotypeSet_mhc_genotype_set_id, domain=None, range=str)

slots.V1p4MHCGenotypeSet_mhc_genotype_list = Slot(uri=AK_SCHEMA.V1p4MHCGenotypeSet_mhc_genotype_list, name="V1p4MHCGenotypeSet_mhc_genotype_list", curie=AK_SCHEMA.curie('V1p4MHCGenotypeSet_mhc_genotype_list'),
                   model_uri=AK_SCHEMA.V1p4MHCGenotypeSet_mhc_genotype_list, domain=None, range=Union[Union[dict, V1p4MHCGenotype], List[Union[dict, V1p4MHCGenotype]]])

slots.V1p4MHCGenotype_mhc_genotype_id = Slot(uri=AK_SCHEMA.V1p4MHCGenotype_mhc_genotype_id, name="V1p4MHCGenotype_mhc_genotype_id", curie=AK_SCHEMA.curie('V1p4MHCGenotype_mhc_genotype_id'),
                   model_uri=AK_SCHEMA.V1p4MHCGenotype_mhc_genotype_id, domain=None, range=str)

slots.V1p4MHCGenotype_mhc_class = Slot(uri=AK_SCHEMA.V1p4MHCGenotype_mhc_class, name="V1p4MHCGenotype_mhc_class", curie=AK_SCHEMA.curie('V1p4MHCGenotype_mhc_class'),
                   model_uri=AK_SCHEMA.V1p4MHCGenotype_mhc_class, domain=None, range=Union[str, "V1p4MhcClass"])

slots.V1p4MHCGenotype_mhc_alleles = Slot(uri=AK_SCHEMA.V1p4MHCGenotype_mhc_alleles, name="V1p4MHCGenotype_mhc_alleles", curie=AK_SCHEMA.curie('V1p4MHCGenotype_mhc_alleles'),
                   model_uri=AK_SCHEMA.V1p4MHCGenotype_mhc_alleles, domain=None, range=Union[Union[dict, V1p4MHCAllele], List[Union[dict, V1p4MHCAllele]]])

slots.V1p4MHCGenotype_mhc_genotyping_method = Slot(uri=AK_SCHEMA.V1p4MHCGenotype_mhc_genotyping_method, name="V1p4MHCGenotype_mhc_genotyping_method", curie=AK_SCHEMA.curie('V1p4MHCGenotype_mhc_genotyping_method'),
                   model_uri=AK_SCHEMA.V1p4MHCGenotype_mhc_genotyping_method, domain=None, range=Optional[str])

slots.V1p4MHCAllele_allele_designation = Slot(uri=AK_SCHEMA.V1p4MHCAllele_allele_designation, name="V1p4MHCAllele_allele_designation", curie=AK_SCHEMA.curie('V1p4MHCAllele_allele_designation'),
                   model_uri=AK_SCHEMA.V1p4MHCAllele_allele_designation, domain=None, range=Optional[str])

slots.V1p4MHCAllele_gene = Slot(uri=AK_SCHEMA.V1p4MHCAllele_gene, name="V1p4MHCAllele_gene", curie=AK_SCHEMA.curie('V1p4MHCAllele_gene'),
                   model_uri=AK_SCHEMA.V1p4MHCAllele_gene, domain=None, range=Optional[Union[str, "V1p4Gene"]])

slots.V1p4MHCAllele_reference_set_ref = Slot(uri=AK_SCHEMA.V1p4MHCAllele_reference_set_ref, name="V1p4MHCAllele_reference_set_ref", curie=AK_SCHEMA.curie('V1p4MHCAllele_reference_set_ref'),
                   model_uri=AK_SCHEMA.V1p4MHCAllele_reference_set_ref, domain=None, range=Optional[str])

slots.V1p4SubjectGenotype_receptor_genotype_set = Slot(uri=AK_SCHEMA.V1p4SubjectGenotype_receptor_genotype_set, name="V1p4SubjectGenotype_receptor_genotype_set", curie=AK_SCHEMA.curie('V1p4SubjectGenotype_receptor_genotype_set'),
                   model_uri=AK_SCHEMA.V1p4SubjectGenotype_receptor_genotype_set, domain=None, range=Optional[Union[dict, V1p4GenotypeSet]])

slots.V1p4SubjectGenotype_mhc_genotype_set = Slot(uri=AK_SCHEMA.V1p4SubjectGenotype_mhc_genotype_set, name="V1p4SubjectGenotype_mhc_genotype_set", curie=AK_SCHEMA.curie('V1p4SubjectGenotype_mhc_genotype_set'),
                   model_uri=AK_SCHEMA.V1p4SubjectGenotype_mhc_genotype_set, domain=None, range=Optional[Union[dict, V1p4MHCGenotypeSet]])

slots.V1p4Study_study_id = Slot(uri=AK_SCHEMA.V1p4Study_study_id, name="V1p4Study_study_id", curie=AK_SCHEMA.curie('V1p4Study_study_id'),
                   model_uri=AK_SCHEMA.V1p4Study_study_id, domain=None, range=str)

slots.V1p4Study_study_title = Slot(uri=AK_SCHEMA.V1p4Study_study_title, name="V1p4Study_study_title", curie=AK_SCHEMA.curie('V1p4Study_study_title'),
                   model_uri=AK_SCHEMA.V1p4Study_study_title, domain=None, range=str)

slots.V1p4Study_study_type = Slot(uri=AK_SCHEMA.V1p4Study_study_type, name="V1p4Study_study_type", curie=AK_SCHEMA.curie('V1p4Study_study_type'),
                   model_uri=AK_SCHEMA.V1p4Study_study_type, domain=None, range=Union[str, "V1p4StudyType"])

slots.V1p4Study_study_description = Slot(uri=AK_SCHEMA.V1p4Study_study_description, name="V1p4Study_study_description", curie=AK_SCHEMA.curie('V1p4Study_study_description'),
                   model_uri=AK_SCHEMA.V1p4Study_study_description, domain=None, range=Optional[str])

slots.V1p4Study_inclusion_exclusion_criteria = Slot(uri=AK_SCHEMA.V1p4Study_inclusion_exclusion_criteria, name="V1p4Study_inclusion_exclusion_criteria", curie=AK_SCHEMA.curie('V1p4Study_inclusion_exclusion_criteria'),
                   model_uri=AK_SCHEMA.V1p4Study_inclusion_exclusion_criteria, domain=None, range=str)

slots.V1p4Study_grants = Slot(uri=AK_SCHEMA.V1p4Study_grants, name="V1p4Study_grants", curie=AK_SCHEMA.curie('V1p4Study_grants'),
                   model_uri=AK_SCHEMA.V1p4Study_grants, domain=None, range=str)

slots.V1p4Study_contributors = Slot(uri=AK_SCHEMA.V1p4Study_contributors, name="V1p4Study_contributors", curie=AK_SCHEMA.curie('V1p4Study_contributors'),
                   model_uri=AK_SCHEMA.V1p4Study_contributors, domain=None, range=Union[Union[dict, V1p4Contributor], List[Union[dict, V1p4Contributor]]])

slots.V1p4Study_pub_ids = Slot(uri=AK_SCHEMA.V1p4Study_pub_ids, name="V1p4Study_pub_ids", curie=AK_SCHEMA.curie('V1p4Study_pub_ids'),
                   model_uri=AK_SCHEMA.V1p4Study_pub_ids, domain=None, range=Union[str, List[str]])

slots.V1p4Study_keywords_study = Slot(uri=AK_SCHEMA.V1p4Study_keywords_study, name="V1p4Study_keywords_study", curie=AK_SCHEMA.curie('V1p4Study_keywords_study'),
                   model_uri=AK_SCHEMA.V1p4Study_keywords_study, domain=None, range=Union[Union[str, "V1p4KeywordsStudy"], List[Union[str, "V1p4KeywordsStudy"]]])

slots.V1p4Study_adc_publish_date = Slot(uri=AK_SCHEMA.V1p4Study_adc_publish_date, name="V1p4Study_adc_publish_date", curie=AK_SCHEMA.curie('V1p4Study_adc_publish_date'),
                   model_uri=AK_SCHEMA.V1p4Study_adc_publish_date, domain=None, range=Optional[str])

slots.V1p4Study_adc_update_date = Slot(uri=AK_SCHEMA.V1p4Study_adc_update_date, name="V1p4Study_adc_update_date", curie=AK_SCHEMA.curie('V1p4Study_adc_update_date'),
                   model_uri=AK_SCHEMA.V1p4Study_adc_update_date, domain=None, range=Optional[str])

slots.V1p4Subject_subject_id = Slot(uri=AK_SCHEMA.V1p4Subject_subject_id, name="V1p4Subject_subject_id", curie=AK_SCHEMA.curie('V1p4Subject_subject_id'),
                   model_uri=AK_SCHEMA.V1p4Subject_subject_id, domain=None, range=str)

slots.V1p4Subject_synthetic = Slot(uri=AK_SCHEMA.V1p4Subject_synthetic, name="V1p4Subject_synthetic", curie=AK_SCHEMA.curie('V1p4Subject_synthetic'),
                   model_uri=AK_SCHEMA.V1p4Subject_synthetic, domain=None, range=Union[bool, Bool])

slots.V1p4Subject_species = Slot(uri=AK_SCHEMA.V1p4Subject_species, name="V1p4Subject_species", curie=AK_SCHEMA.curie('V1p4Subject_species'),
                   model_uri=AK_SCHEMA.V1p4Subject_species, domain=None, range=Union[str, "V1p4Species"])

slots.V1p4Subject_sex = Slot(uri=AK_SCHEMA.V1p4Subject_sex, name="V1p4Subject_sex", curie=AK_SCHEMA.curie('V1p4Subject_sex'),
                   model_uri=AK_SCHEMA.V1p4Subject_sex, domain=None, range=Union[str, "V1p4Sex"])

slots.V1p4Subject_age = Slot(uri=AK_SCHEMA.V1p4Subject_age, name="V1p4Subject_age", curie=AK_SCHEMA.curie('V1p4Subject_age'),
                   model_uri=AK_SCHEMA.V1p4Subject_age, domain=None, range=Union[dict, V1p4TimeInterval])

slots.V1p4Subject_age_event = Slot(uri=AK_SCHEMA.V1p4Subject_age_event, name="V1p4Subject_age_event", curie=AK_SCHEMA.curie('V1p4Subject_age_event'),
                   model_uri=AK_SCHEMA.V1p4Subject_age_event, domain=None, range=str)

slots.V1p4Subject_ancestry_population = Slot(uri=AK_SCHEMA.V1p4Subject_ancestry_population, name="V1p4Subject_ancestry_population", curie=AK_SCHEMA.curie('V1p4Subject_ancestry_population'),
                   model_uri=AK_SCHEMA.V1p4Subject_ancestry_population, domain=None, range=Union[str, "V1p4AncestryPopulation"])

slots.V1p4Subject_location_birth = Slot(uri=AK_SCHEMA.V1p4Subject_location_birth, name="V1p4Subject_location_birth", curie=AK_SCHEMA.curie('V1p4Subject_location_birth'),
                   model_uri=AK_SCHEMA.V1p4Subject_location_birth, domain=None, range=Optional[Union[str, "V1p4LocationBirth"]])

slots.V1p4Subject_ethnicity = Slot(uri=AK_SCHEMA.V1p4Subject_ethnicity, name="V1p4Subject_ethnicity", curie=AK_SCHEMA.curie('V1p4Subject_ethnicity'),
                   model_uri=AK_SCHEMA.V1p4Subject_ethnicity, domain=None, range=str)

slots.V1p4Subject_race = Slot(uri=AK_SCHEMA.V1p4Subject_race, name="V1p4Subject_race", curie=AK_SCHEMA.curie('V1p4Subject_race'),
                   model_uri=AK_SCHEMA.V1p4Subject_race, domain=None, range=str)

slots.V1p4Subject_strain_name = Slot(uri=AK_SCHEMA.V1p4Subject_strain_name, name="V1p4Subject_strain_name", curie=AK_SCHEMA.curie('V1p4Subject_strain_name'),
                   model_uri=AK_SCHEMA.V1p4Subject_strain_name, domain=None, range=str)

slots.V1p4Subject_linked_subjects = Slot(uri=AK_SCHEMA.V1p4Subject_linked_subjects, name="V1p4Subject_linked_subjects", curie=AK_SCHEMA.curie('V1p4Subject_linked_subjects'),
                   model_uri=AK_SCHEMA.V1p4Subject_linked_subjects, domain=None, range=str)

slots.V1p4Subject_link_type = Slot(uri=AK_SCHEMA.V1p4Subject_link_type, name="V1p4Subject_link_type", curie=AK_SCHEMA.curie('V1p4Subject_link_type'),
                   model_uri=AK_SCHEMA.V1p4Subject_link_type, domain=None, range=str)

slots.V1p4Subject_diagnosis = Slot(uri=AK_SCHEMA.V1p4Subject_diagnosis, name="V1p4Subject_diagnosis", curie=AK_SCHEMA.curie('V1p4Subject_diagnosis'),
                   model_uri=AK_SCHEMA.V1p4Subject_diagnosis, domain=None, range=Optional[Union[Union[dict, V1p4Diagnosis], List[Union[dict, V1p4Diagnosis]]]])

slots.V1p4Subject_genotype = Slot(uri=AK_SCHEMA.V1p4Subject_genotype, name="V1p4Subject_genotype", curie=AK_SCHEMA.curie('V1p4Subject_genotype'),
                   model_uri=AK_SCHEMA.V1p4Subject_genotype, domain=None, range=Optional[Union[dict, V1p4SubjectGenotype]])

slots.V1p4Diagnosis_study_group_description = Slot(uri=AK_SCHEMA.V1p4Diagnosis_study_group_description, name="V1p4Diagnosis_study_group_description", curie=AK_SCHEMA.curie('V1p4Diagnosis_study_group_description'),
                   model_uri=AK_SCHEMA.V1p4Diagnosis_study_group_description, domain=None, range=str)

slots.V1p4Diagnosis_diagnosis_timepoint = Slot(uri=AK_SCHEMA.V1p4Diagnosis_diagnosis_timepoint, name="V1p4Diagnosis_diagnosis_timepoint", curie=AK_SCHEMA.curie('V1p4Diagnosis_diagnosis_timepoint'),
                   model_uri=AK_SCHEMA.V1p4Diagnosis_diagnosis_timepoint, domain=None, range=Optional[Union[dict, V1p4TimePoint]])

slots.V1p4Diagnosis_disease_diagnosis = Slot(uri=AK_SCHEMA.V1p4Diagnosis_disease_diagnosis, name="V1p4Diagnosis_disease_diagnosis", curie=AK_SCHEMA.curie('V1p4Diagnosis_disease_diagnosis'),
                   model_uri=AK_SCHEMA.V1p4Diagnosis_disease_diagnosis, domain=None, range=Union[str, "V1p4DiseaseDiagnosis"])

slots.V1p4Diagnosis_disease_length = Slot(uri=AK_SCHEMA.V1p4Diagnosis_disease_length, name="V1p4Diagnosis_disease_length", curie=AK_SCHEMA.curie('V1p4Diagnosis_disease_length'),
                   model_uri=AK_SCHEMA.V1p4Diagnosis_disease_length, domain=None, range=Union[dict, V1p4TimeQuantity])

slots.V1p4Diagnosis_disease_stage = Slot(uri=AK_SCHEMA.V1p4Diagnosis_disease_stage, name="V1p4Diagnosis_disease_stage", curie=AK_SCHEMA.curie('V1p4Diagnosis_disease_stage'),
                   model_uri=AK_SCHEMA.V1p4Diagnosis_disease_stage, domain=None, range=str)

slots.V1p4Diagnosis_prior_therapies = Slot(uri=AK_SCHEMA.V1p4Diagnosis_prior_therapies, name="V1p4Diagnosis_prior_therapies", curie=AK_SCHEMA.curie('V1p4Diagnosis_prior_therapies'),
                   model_uri=AK_SCHEMA.V1p4Diagnosis_prior_therapies, domain=None, range=str)

slots.V1p4Diagnosis_immunogen = Slot(uri=AK_SCHEMA.V1p4Diagnosis_immunogen, name="V1p4Diagnosis_immunogen", curie=AK_SCHEMA.curie('V1p4Diagnosis_immunogen'),
                   model_uri=AK_SCHEMA.V1p4Diagnosis_immunogen, domain=None, range=str)

slots.V1p4Diagnosis_intervention = Slot(uri=AK_SCHEMA.V1p4Diagnosis_intervention, name="V1p4Diagnosis_intervention", curie=AK_SCHEMA.curie('V1p4Diagnosis_intervention'),
                   model_uri=AK_SCHEMA.V1p4Diagnosis_intervention, domain=None, range=str)

slots.V1p4Diagnosis_medical_history = Slot(uri=AK_SCHEMA.V1p4Diagnosis_medical_history, name="V1p4Diagnosis_medical_history", curie=AK_SCHEMA.curie('V1p4Diagnosis_medical_history'),
                   model_uri=AK_SCHEMA.V1p4Diagnosis_medical_history, domain=None, range=str)

slots.V1p4Sample_sample_id = Slot(uri=AK_SCHEMA.V1p4Sample_sample_id, name="V1p4Sample_sample_id", curie=AK_SCHEMA.curie('V1p4Sample_sample_id'),
                   model_uri=AK_SCHEMA.V1p4Sample_sample_id, domain=None, range=str)

slots.V1p4Sample_sample_type = Slot(uri=AK_SCHEMA.V1p4Sample_sample_type, name="V1p4Sample_sample_type", curie=AK_SCHEMA.curie('V1p4Sample_sample_type'),
                   model_uri=AK_SCHEMA.V1p4Sample_sample_type, domain=None, range=str)

slots.V1p4Sample_tissue = Slot(uri=AK_SCHEMA.V1p4Sample_tissue, name="V1p4Sample_tissue", curie=AK_SCHEMA.curie('V1p4Sample_tissue'),
                   model_uri=AK_SCHEMA.V1p4Sample_tissue, domain=None, range=Union[str, "V1p4Tissue"])

slots.V1p4Sample_anatomic_site = Slot(uri=AK_SCHEMA.V1p4Sample_anatomic_site, name="V1p4Sample_anatomic_site", curie=AK_SCHEMA.curie('V1p4Sample_anatomic_site'),
                   model_uri=AK_SCHEMA.V1p4Sample_anatomic_site, domain=None, range=str)

slots.V1p4Sample_disease_state_sample = Slot(uri=AK_SCHEMA.V1p4Sample_disease_state_sample, name="V1p4Sample_disease_state_sample", curie=AK_SCHEMA.curie('V1p4Sample_disease_state_sample'),
                   model_uri=AK_SCHEMA.V1p4Sample_disease_state_sample, domain=None, range=str)

slots.V1p4Sample_collection_time_point_relative = Slot(uri=AK_SCHEMA.V1p4Sample_collection_time_point_relative, name="V1p4Sample_collection_time_point_relative", curie=AK_SCHEMA.curie('V1p4Sample_collection_time_point_relative'),
                   model_uri=AK_SCHEMA.V1p4Sample_collection_time_point_relative, domain=None, range=Union[dict, V1p4TimePoint])

slots.V1p4Sample_collection_location = Slot(uri=AK_SCHEMA.V1p4Sample_collection_location, name="V1p4Sample_collection_location", curie=AK_SCHEMA.curie('V1p4Sample_collection_location'),
                   model_uri=AK_SCHEMA.V1p4Sample_collection_location, domain=None, range=Optional[Union[str, "V1p4CollectionLocation"]])

slots.V1p4Sample_biomaterial_provider = Slot(uri=AK_SCHEMA.V1p4Sample_biomaterial_provider, name="V1p4Sample_biomaterial_provider", curie=AK_SCHEMA.curie('V1p4Sample_biomaterial_provider'),
                   model_uri=AK_SCHEMA.V1p4Sample_biomaterial_provider, domain=None, range=str)

slots.V1p4CellProcessing_tissue_processing = Slot(uri=AK_SCHEMA.V1p4CellProcessing_tissue_processing, name="V1p4CellProcessing_tissue_processing", curie=AK_SCHEMA.curie('V1p4CellProcessing_tissue_processing'),
                   model_uri=AK_SCHEMA.V1p4CellProcessing_tissue_processing, domain=None, range=str)

slots.V1p4CellProcessing_cell_subset = Slot(uri=AK_SCHEMA.V1p4CellProcessing_cell_subset, name="V1p4CellProcessing_cell_subset", curie=AK_SCHEMA.curie('V1p4CellProcessing_cell_subset'),
                   model_uri=AK_SCHEMA.V1p4CellProcessing_cell_subset, domain=None, range=Union[str, "V1p4CellSubset"])

slots.V1p4CellProcessing_cell_phenotype = Slot(uri=AK_SCHEMA.V1p4CellProcessing_cell_phenotype, name="V1p4CellProcessing_cell_phenotype", curie=AK_SCHEMA.curie('V1p4CellProcessing_cell_phenotype'),
                   model_uri=AK_SCHEMA.V1p4CellProcessing_cell_phenotype, domain=None, range=str)

slots.V1p4CellProcessing_cell_label = Slot(uri=AK_SCHEMA.V1p4CellProcessing_cell_label, name="V1p4CellProcessing_cell_label", curie=AK_SCHEMA.curie('V1p4CellProcessing_cell_label'),
                   model_uri=AK_SCHEMA.V1p4CellProcessing_cell_label, domain=None, range=Optional[str])

slots.V1p4CellProcessing_cell_species = Slot(uri=AK_SCHEMA.V1p4CellProcessing_cell_species, name="V1p4CellProcessing_cell_species", curie=AK_SCHEMA.curie('V1p4CellProcessing_cell_species'),
                   model_uri=AK_SCHEMA.V1p4CellProcessing_cell_species, domain=None, range=Optional[Union[str, "V1p4CellSpecies"]])

slots.V1p4CellProcessing_single_cell = Slot(uri=AK_SCHEMA.V1p4CellProcessing_single_cell, name="V1p4CellProcessing_single_cell", curie=AK_SCHEMA.curie('V1p4CellProcessing_single_cell'),
                   model_uri=AK_SCHEMA.V1p4CellProcessing_single_cell, domain=None, range=Union[bool, Bool])

slots.V1p4CellProcessing_cell_number = Slot(uri=AK_SCHEMA.V1p4CellProcessing_cell_number, name="V1p4CellProcessing_cell_number", curie=AK_SCHEMA.curie('V1p4CellProcessing_cell_number'),
                   model_uri=AK_SCHEMA.V1p4CellProcessing_cell_number, domain=None, range=int)

slots.V1p4CellProcessing_cells_per_reaction = Slot(uri=AK_SCHEMA.V1p4CellProcessing_cells_per_reaction, name="V1p4CellProcessing_cells_per_reaction", curie=AK_SCHEMA.curie('V1p4CellProcessing_cells_per_reaction'),
                   model_uri=AK_SCHEMA.V1p4CellProcessing_cells_per_reaction, domain=None, range=int)

slots.V1p4CellProcessing_cell_storage = Slot(uri=AK_SCHEMA.V1p4CellProcessing_cell_storage, name="V1p4CellProcessing_cell_storage", curie=AK_SCHEMA.curie('V1p4CellProcessing_cell_storage'),
                   model_uri=AK_SCHEMA.V1p4CellProcessing_cell_storage, domain=None, range=Union[bool, Bool])

slots.V1p4CellProcessing_cell_quality = Slot(uri=AK_SCHEMA.V1p4CellProcessing_cell_quality, name="V1p4CellProcessing_cell_quality", curie=AK_SCHEMA.curie('V1p4CellProcessing_cell_quality'),
                   model_uri=AK_SCHEMA.V1p4CellProcessing_cell_quality, domain=None, range=str)

slots.V1p4CellProcessing_cell_isolation = Slot(uri=AK_SCHEMA.V1p4CellProcessing_cell_isolation, name="V1p4CellProcessing_cell_isolation", curie=AK_SCHEMA.curie('V1p4CellProcessing_cell_isolation'),
                   model_uri=AK_SCHEMA.V1p4CellProcessing_cell_isolation, domain=None, range=str)

slots.V1p4CellProcessing_cell_processing_protocol = Slot(uri=AK_SCHEMA.V1p4CellProcessing_cell_processing_protocol, name="V1p4CellProcessing_cell_processing_protocol", curie=AK_SCHEMA.curie('V1p4CellProcessing_cell_processing_protocol'),
                   model_uri=AK_SCHEMA.V1p4CellProcessing_cell_processing_protocol, domain=None, range=str)

slots.V1p4PCRTarget_pcr_target_locus = Slot(uri=AK_SCHEMA.V1p4PCRTarget_pcr_target_locus, name="V1p4PCRTarget_pcr_target_locus", curie=AK_SCHEMA.curie('V1p4PCRTarget_pcr_target_locus'),
                   model_uri=AK_SCHEMA.V1p4PCRTarget_pcr_target_locus, domain=None, range=Union[str, "V1p4PcrTargetLocus"])

slots.V1p4PCRTarget_forward_pcr_primer_target_location = Slot(uri=AK_SCHEMA.V1p4PCRTarget_forward_pcr_primer_target_location, name="V1p4PCRTarget_forward_pcr_primer_target_location", curie=AK_SCHEMA.curie('V1p4PCRTarget_forward_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.V1p4PCRTarget_forward_pcr_primer_target_location, domain=None, range=str)

slots.V1p4PCRTarget_reverse_pcr_primer_target_location = Slot(uri=AK_SCHEMA.V1p4PCRTarget_reverse_pcr_primer_target_location, name="V1p4PCRTarget_reverse_pcr_primer_target_location", curie=AK_SCHEMA.curie('V1p4PCRTarget_reverse_pcr_primer_target_location'),
                   model_uri=AK_SCHEMA.V1p4PCRTarget_reverse_pcr_primer_target_location, domain=None, range=str)

slots.V1p4NucleicAcidProcessing_template_class = Slot(uri=AK_SCHEMA.V1p4NucleicAcidProcessing_template_class, name="V1p4NucleicAcidProcessing_template_class", curie=AK_SCHEMA.curie('V1p4NucleicAcidProcessing_template_class'),
                   model_uri=AK_SCHEMA.V1p4NucleicAcidProcessing_template_class, domain=None, range=Union[str, "V1p4TemplateClass"])

slots.V1p4NucleicAcidProcessing_template_quality = Slot(uri=AK_SCHEMA.V1p4NucleicAcidProcessing_template_quality, name="V1p4NucleicAcidProcessing_template_quality", curie=AK_SCHEMA.curie('V1p4NucleicAcidProcessing_template_quality'),
                   model_uri=AK_SCHEMA.V1p4NucleicAcidProcessing_template_quality, domain=None, range=str)

slots.V1p4NucleicAcidProcessing_template_amount = Slot(uri=AK_SCHEMA.V1p4NucleicAcidProcessing_template_amount, name="V1p4NucleicAcidProcessing_template_amount", curie=AK_SCHEMA.curie('V1p4NucleicAcidProcessing_template_amount'),
                   model_uri=AK_SCHEMA.V1p4NucleicAcidProcessing_template_amount, domain=None, range=Union[dict, V1p4PhysicalQuantity])

slots.V1p4NucleicAcidProcessing_library_generation_method = Slot(uri=AK_SCHEMA.V1p4NucleicAcidProcessing_library_generation_method, name="V1p4NucleicAcidProcessing_library_generation_method", curie=AK_SCHEMA.curie('V1p4NucleicAcidProcessing_library_generation_method'),
                   model_uri=AK_SCHEMA.V1p4NucleicAcidProcessing_library_generation_method, domain=None, range=Union[str, "V1p4LibraryGenerationMethod"])

slots.V1p4NucleicAcidProcessing_library_generation_protocol = Slot(uri=AK_SCHEMA.V1p4NucleicAcidProcessing_library_generation_protocol, name="V1p4NucleicAcidProcessing_library_generation_protocol", curie=AK_SCHEMA.curie('V1p4NucleicAcidProcessing_library_generation_protocol'),
                   model_uri=AK_SCHEMA.V1p4NucleicAcidProcessing_library_generation_protocol, domain=None, range=str)

slots.V1p4NucleicAcidProcessing_library_generation_kit_version = Slot(uri=AK_SCHEMA.V1p4NucleicAcidProcessing_library_generation_kit_version, name="V1p4NucleicAcidProcessing_library_generation_kit_version", curie=AK_SCHEMA.curie('V1p4NucleicAcidProcessing_library_generation_kit_version'),
                   model_uri=AK_SCHEMA.V1p4NucleicAcidProcessing_library_generation_kit_version, domain=None, range=str)

slots.V1p4NucleicAcidProcessing_pcr_target = Slot(uri=AK_SCHEMA.V1p4NucleicAcidProcessing_pcr_target, name="V1p4NucleicAcidProcessing_pcr_target", curie=AK_SCHEMA.curie('V1p4NucleicAcidProcessing_pcr_target'),
                   model_uri=AK_SCHEMA.V1p4NucleicAcidProcessing_pcr_target, domain=None, range=Optional[Union[Union[dict, V1p4PCRTarget], List[Union[dict, V1p4PCRTarget]]]])

slots.V1p4NucleicAcidProcessing_complete_sequences = Slot(uri=AK_SCHEMA.V1p4NucleicAcidProcessing_complete_sequences, name="V1p4NucleicAcidProcessing_complete_sequences", curie=AK_SCHEMA.curie('V1p4NucleicAcidProcessing_complete_sequences'),
                   model_uri=AK_SCHEMA.V1p4NucleicAcidProcessing_complete_sequences, domain=None, range=Union[str, "V1p4CompleteSequences"])

slots.V1p4NucleicAcidProcessing_physical_linkage = Slot(uri=AK_SCHEMA.V1p4NucleicAcidProcessing_physical_linkage, name="V1p4NucleicAcidProcessing_physical_linkage", curie=AK_SCHEMA.curie('V1p4NucleicAcidProcessing_physical_linkage'),
                   model_uri=AK_SCHEMA.V1p4NucleicAcidProcessing_physical_linkage, domain=None, range=Union[str, "V1p4PhysicalLinkage"])

slots.V1p4SequencingRun_sequencing_run_id = Slot(uri=AK_SCHEMA.V1p4SequencingRun_sequencing_run_id, name="V1p4SequencingRun_sequencing_run_id", curie=AK_SCHEMA.curie('V1p4SequencingRun_sequencing_run_id'),
                   model_uri=AK_SCHEMA.V1p4SequencingRun_sequencing_run_id, domain=None, range=str)

slots.V1p4SequencingRun_total_reads_passing_qc_filter = Slot(uri=AK_SCHEMA.V1p4SequencingRun_total_reads_passing_qc_filter, name="V1p4SequencingRun_total_reads_passing_qc_filter", curie=AK_SCHEMA.curie('V1p4SequencingRun_total_reads_passing_qc_filter'),
                   model_uri=AK_SCHEMA.V1p4SequencingRun_total_reads_passing_qc_filter, domain=None, range=int)

slots.V1p4SequencingRun_sequencing_platform = Slot(uri=AK_SCHEMA.V1p4SequencingRun_sequencing_platform, name="V1p4SequencingRun_sequencing_platform", curie=AK_SCHEMA.curie('V1p4SequencingRun_sequencing_platform'),
                   model_uri=AK_SCHEMA.V1p4SequencingRun_sequencing_platform, domain=None, range=str)

slots.V1p4SequencingRun_sequencing_facility = Slot(uri=AK_SCHEMA.V1p4SequencingRun_sequencing_facility, name="V1p4SequencingRun_sequencing_facility", curie=AK_SCHEMA.curie('V1p4SequencingRun_sequencing_facility'),
                   model_uri=AK_SCHEMA.V1p4SequencingRun_sequencing_facility, domain=None, range=str)

slots.V1p4SequencingRun_sequencing_run_date = Slot(uri=AK_SCHEMA.V1p4SequencingRun_sequencing_run_date, name="V1p4SequencingRun_sequencing_run_date", curie=AK_SCHEMA.curie('V1p4SequencingRun_sequencing_run_date'),
                   model_uri=AK_SCHEMA.V1p4SequencingRun_sequencing_run_date, domain=None, range=str)

slots.V1p4SequencingRun_sequencing_kit = Slot(uri=AK_SCHEMA.V1p4SequencingRun_sequencing_kit, name="V1p4SequencingRun_sequencing_kit", curie=AK_SCHEMA.curie('V1p4SequencingRun_sequencing_kit'),
                   model_uri=AK_SCHEMA.V1p4SequencingRun_sequencing_kit, domain=None, range=str)

slots.V1p4SequencingRun_sequencing_files = Slot(uri=AK_SCHEMA.V1p4SequencingRun_sequencing_files, name="V1p4SequencingRun_sequencing_files", curie=AK_SCHEMA.curie('V1p4SequencingRun_sequencing_files'),
                   model_uri=AK_SCHEMA.V1p4SequencingRun_sequencing_files, domain=None, range=Optional[Union[dict, V1p4SequencingData]])

slots.V1p4SequencingData_sequencing_data_id = Slot(uri=AK_SCHEMA.V1p4SequencingData_sequencing_data_id, name="V1p4SequencingData_sequencing_data_id", curie=AK_SCHEMA.curie('V1p4SequencingData_sequencing_data_id'),
                   model_uri=AK_SCHEMA.V1p4SequencingData_sequencing_data_id, domain=None, range=str)

slots.V1p4SequencingData_file_type = Slot(uri=AK_SCHEMA.V1p4SequencingData_file_type, name="V1p4SequencingData_file_type", curie=AK_SCHEMA.curie('V1p4SequencingData_file_type'),
                   model_uri=AK_SCHEMA.V1p4SequencingData_file_type, domain=None, range=Union[str, "V1p4FileType"])

slots.V1p4SequencingData_filename = Slot(uri=AK_SCHEMA.V1p4SequencingData_filename, name="V1p4SequencingData_filename", curie=AK_SCHEMA.curie('V1p4SequencingData_filename'),
                   model_uri=AK_SCHEMA.V1p4SequencingData_filename, domain=None, range=str)

slots.V1p4SequencingData_read_direction = Slot(uri=AK_SCHEMA.V1p4SequencingData_read_direction, name="V1p4SequencingData_read_direction", curie=AK_SCHEMA.curie('V1p4SequencingData_read_direction'),
                   model_uri=AK_SCHEMA.V1p4SequencingData_read_direction, domain=None, range=Union[str, "V1p4ReadDirection"])

slots.V1p4SequencingData_read_length = Slot(uri=AK_SCHEMA.V1p4SequencingData_read_length, name="V1p4SequencingData_read_length", curie=AK_SCHEMA.curie('V1p4SequencingData_read_length'),
                   model_uri=AK_SCHEMA.V1p4SequencingData_read_length, domain=None, range=int)

slots.V1p4SequencingData_paired_filename = Slot(uri=AK_SCHEMA.V1p4SequencingData_paired_filename, name="V1p4SequencingData_paired_filename", curie=AK_SCHEMA.curie('V1p4SequencingData_paired_filename'),
                   model_uri=AK_SCHEMA.V1p4SequencingData_paired_filename, domain=None, range=str)

slots.V1p4SequencingData_paired_read_direction = Slot(uri=AK_SCHEMA.V1p4SequencingData_paired_read_direction, name="V1p4SequencingData_paired_read_direction", curie=AK_SCHEMA.curie('V1p4SequencingData_paired_read_direction'),
                   model_uri=AK_SCHEMA.V1p4SequencingData_paired_read_direction, domain=None, range=Union[str, "V1p4PairedReadDirection"])

slots.V1p4SequencingData_paired_read_length = Slot(uri=AK_SCHEMA.V1p4SequencingData_paired_read_length, name="V1p4SequencingData_paired_read_length", curie=AK_SCHEMA.curie('V1p4SequencingData_paired_read_length'),
                   model_uri=AK_SCHEMA.V1p4SequencingData_paired_read_length, domain=None, range=int)

slots.V1p4SequencingData_index_filename = Slot(uri=AK_SCHEMA.V1p4SequencingData_index_filename, name="V1p4SequencingData_index_filename", curie=AK_SCHEMA.curie('V1p4SequencingData_index_filename'),
                   model_uri=AK_SCHEMA.V1p4SequencingData_index_filename, domain=None, range=Optional[str])

slots.V1p4SequencingData_index_length = Slot(uri=AK_SCHEMA.V1p4SequencingData_index_length, name="V1p4SequencingData_index_length", curie=AK_SCHEMA.curie('V1p4SequencingData_index_length'),
                   model_uri=AK_SCHEMA.V1p4SequencingData_index_length, domain=None, range=Optional[int])

slots.V1p4DataProcessing_data_processing_id = Slot(uri=AK_SCHEMA.V1p4DataProcessing_data_processing_id, name="V1p4DataProcessing_data_processing_id", curie=AK_SCHEMA.curie('V1p4DataProcessing_data_processing_id'),
                   model_uri=AK_SCHEMA.V1p4DataProcessing_data_processing_id, domain=None, range=Optional[str])

slots.V1p4DataProcessing_primary_annotation = Slot(uri=AK_SCHEMA.V1p4DataProcessing_primary_annotation, name="V1p4DataProcessing_primary_annotation", curie=AK_SCHEMA.curie('V1p4DataProcessing_primary_annotation'),
                   model_uri=AK_SCHEMA.V1p4DataProcessing_primary_annotation, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4DataProcessing_software_versions = Slot(uri=AK_SCHEMA.V1p4DataProcessing_software_versions, name="V1p4DataProcessing_software_versions", curie=AK_SCHEMA.curie('V1p4DataProcessing_software_versions'),
                   model_uri=AK_SCHEMA.V1p4DataProcessing_software_versions, domain=None, range=str)

slots.V1p4DataProcessing_paired_reads_assembly = Slot(uri=AK_SCHEMA.V1p4DataProcessing_paired_reads_assembly, name="V1p4DataProcessing_paired_reads_assembly", curie=AK_SCHEMA.curie('V1p4DataProcessing_paired_reads_assembly'),
                   model_uri=AK_SCHEMA.V1p4DataProcessing_paired_reads_assembly, domain=None, range=str)

slots.V1p4DataProcessing_quality_thresholds = Slot(uri=AK_SCHEMA.V1p4DataProcessing_quality_thresholds, name="V1p4DataProcessing_quality_thresholds", curie=AK_SCHEMA.curie('V1p4DataProcessing_quality_thresholds'),
                   model_uri=AK_SCHEMA.V1p4DataProcessing_quality_thresholds, domain=None, range=str)

slots.V1p4DataProcessing_primer_match_cutoffs = Slot(uri=AK_SCHEMA.V1p4DataProcessing_primer_match_cutoffs, name="V1p4DataProcessing_primer_match_cutoffs", curie=AK_SCHEMA.curie('V1p4DataProcessing_primer_match_cutoffs'),
                   model_uri=AK_SCHEMA.V1p4DataProcessing_primer_match_cutoffs, domain=None, range=str)

slots.V1p4DataProcessing_collapsing_method = Slot(uri=AK_SCHEMA.V1p4DataProcessing_collapsing_method, name="V1p4DataProcessing_collapsing_method", curie=AK_SCHEMA.curie('V1p4DataProcessing_collapsing_method'),
                   model_uri=AK_SCHEMA.V1p4DataProcessing_collapsing_method, domain=None, range=str)

slots.V1p4DataProcessing_data_processing_protocols = Slot(uri=AK_SCHEMA.V1p4DataProcessing_data_processing_protocols, name="V1p4DataProcessing_data_processing_protocols", curie=AK_SCHEMA.curie('V1p4DataProcessing_data_processing_protocols'),
                   model_uri=AK_SCHEMA.V1p4DataProcessing_data_processing_protocols, domain=None, range=str)

slots.V1p4DataProcessing_data_processing_files = Slot(uri=AK_SCHEMA.V1p4DataProcessing_data_processing_files, name="V1p4DataProcessing_data_processing_files", curie=AK_SCHEMA.curie('V1p4DataProcessing_data_processing_files'),
                   model_uri=AK_SCHEMA.V1p4DataProcessing_data_processing_files, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4DataProcessing_germline_database = Slot(uri=AK_SCHEMA.V1p4DataProcessing_germline_database, name="V1p4DataProcessing_germline_database", curie=AK_SCHEMA.curie('V1p4DataProcessing_germline_database'),
                   model_uri=AK_SCHEMA.V1p4DataProcessing_germline_database, domain=None, range=str)

slots.V1p4DataProcessing_germline_set_ref = Slot(uri=AK_SCHEMA.V1p4DataProcessing_germline_set_ref, name="V1p4DataProcessing_germline_set_ref", curie=AK_SCHEMA.curie('V1p4DataProcessing_germline_set_ref'),
                   model_uri=AK_SCHEMA.V1p4DataProcessing_germline_set_ref, domain=None, range=Optional[str])

slots.V1p4DataProcessing_analysis_provenance_id = Slot(uri=AK_SCHEMA.V1p4DataProcessing_analysis_provenance_id, name="V1p4DataProcessing_analysis_provenance_id", curie=AK_SCHEMA.curie('V1p4DataProcessing_analysis_provenance_id'),
                   model_uri=AK_SCHEMA.V1p4DataProcessing_analysis_provenance_id, domain=None, range=Optional[str])

slots.V1p4Repertoire_repertoire_id = Slot(uri=AK_SCHEMA.V1p4Repertoire_repertoire_id, name="V1p4Repertoire_repertoire_id", curie=AK_SCHEMA.curie('V1p4Repertoire_repertoire_id'),
                   model_uri=AK_SCHEMA.V1p4Repertoire_repertoire_id, domain=None, range=Optional[str])

slots.V1p4Repertoire_repertoire_name = Slot(uri=AK_SCHEMA.V1p4Repertoire_repertoire_name, name="V1p4Repertoire_repertoire_name", curie=AK_SCHEMA.curie('V1p4Repertoire_repertoire_name'),
                   model_uri=AK_SCHEMA.V1p4Repertoire_repertoire_name, domain=None, range=Optional[str])

slots.V1p4Repertoire_repertoire_description = Slot(uri=AK_SCHEMA.V1p4Repertoire_repertoire_description, name="V1p4Repertoire_repertoire_description", curie=AK_SCHEMA.curie('V1p4Repertoire_repertoire_description'),
                   model_uri=AK_SCHEMA.V1p4Repertoire_repertoire_description, domain=None, range=Optional[str])

slots.V1p4Repertoire_study = Slot(uri=AK_SCHEMA.V1p4Repertoire_study, name="V1p4Repertoire_study", curie=AK_SCHEMA.curie('V1p4Repertoire_study'),
                   model_uri=AK_SCHEMA.V1p4Repertoire_study, domain=None, range=Union[dict, V1p4Study])

slots.V1p4Repertoire_subject = Slot(uri=AK_SCHEMA.V1p4Repertoire_subject, name="V1p4Repertoire_subject", curie=AK_SCHEMA.curie('V1p4Repertoire_subject'),
                   model_uri=AK_SCHEMA.V1p4Repertoire_subject, domain=None, range=Union[dict, V1p4Subject])

slots.V1p4Repertoire_sample = Slot(uri=AK_SCHEMA.V1p4Repertoire_sample, name="V1p4Repertoire_sample", curie=AK_SCHEMA.curie('V1p4Repertoire_sample'),
                   model_uri=AK_SCHEMA.V1p4Repertoire_sample, domain=None, range=Union[Union[dict, V1p4SampleProcessing], List[Union[dict, V1p4SampleProcessing]]])

slots.V1p4Repertoire_data_processing = Slot(uri=AK_SCHEMA.V1p4Repertoire_data_processing, name="V1p4Repertoire_data_processing", curie=AK_SCHEMA.curie('V1p4Repertoire_data_processing'),
                   model_uri=AK_SCHEMA.V1p4Repertoire_data_processing, domain=None, range=Union[Union[dict, V1p4DataProcessing], List[Union[dict, V1p4DataProcessing]]])

slots.V1p4RepertoireGroup_repertoire_group_id = Slot(uri=AK_SCHEMA.V1p4RepertoireGroup_repertoire_group_id, name="V1p4RepertoireGroup_repertoire_group_id", curie=AK_SCHEMA.curie('V1p4RepertoireGroup_repertoire_group_id'),
                   model_uri=AK_SCHEMA.V1p4RepertoireGroup_repertoire_group_id, domain=None, range=str)

slots.V1p4RepertoireGroup_repertoire_group_name = Slot(uri=AK_SCHEMA.V1p4RepertoireGroup_repertoire_group_name, name="V1p4RepertoireGroup_repertoire_group_name", curie=AK_SCHEMA.curie('V1p4RepertoireGroup_repertoire_group_name'),
                   model_uri=AK_SCHEMA.V1p4RepertoireGroup_repertoire_group_name, domain=None, range=Optional[str])

slots.V1p4RepertoireGroup_repertoire_group_description = Slot(uri=AK_SCHEMA.V1p4RepertoireGroup_repertoire_group_description, name="V1p4RepertoireGroup_repertoire_group_description", curie=AK_SCHEMA.curie('V1p4RepertoireGroup_repertoire_group_description'),
                   model_uri=AK_SCHEMA.V1p4RepertoireGroup_repertoire_group_description, domain=None, range=Optional[str])

slots.V1p4RepertoireGroup_repertoires = Slot(uri=AK_SCHEMA.V1p4RepertoireGroup_repertoires, name="V1p4RepertoireGroup_repertoires", curie=AK_SCHEMA.curie('V1p4RepertoireGroup_repertoires'),
                   model_uri=AK_SCHEMA.V1p4RepertoireGroup_repertoires, domain=None, range=Union[str, List[str]])

slots.V1p4Alignment_sequence_id = Slot(uri=AK_SCHEMA.V1p4Alignment_sequence_id, name="V1p4Alignment_sequence_id", curie=AK_SCHEMA.curie('V1p4Alignment_sequence_id'),
                   model_uri=AK_SCHEMA.V1p4Alignment_sequence_id, domain=None, range=str)

slots.V1p4Alignment_segment = Slot(uri=AK_SCHEMA.V1p4Alignment_segment, name="V1p4Alignment_segment", curie=AK_SCHEMA.curie('V1p4Alignment_segment'),
                   model_uri=AK_SCHEMA.V1p4Alignment_segment, domain=None, range=str)

slots.V1p4Alignment_rev_comp = Slot(uri=AK_SCHEMA.V1p4Alignment_rev_comp, name="V1p4Alignment_rev_comp", curie=AK_SCHEMA.curie('V1p4Alignment_rev_comp'),
                   model_uri=AK_SCHEMA.V1p4Alignment_rev_comp, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4Alignment_call = Slot(uri=AK_SCHEMA.V1p4Alignment_call, name="V1p4Alignment_call", curie=AK_SCHEMA.curie('V1p4Alignment_call'),
                   model_uri=AK_SCHEMA.V1p4Alignment_call, domain=None, range=str)

slots.V1p4Alignment_score = Slot(uri=AK_SCHEMA.V1p4Alignment_score, name="V1p4Alignment_score", curie=AK_SCHEMA.curie('V1p4Alignment_score'),
                   model_uri=AK_SCHEMA.V1p4Alignment_score, domain=None, range=float)

slots.V1p4Alignment_identity = Slot(uri=AK_SCHEMA.V1p4Alignment_identity, name="V1p4Alignment_identity", curie=AK_SCHEMA.curie('V1p4Alignment_identity'),
                   model_uri=AK_SCHEMA.V1p4Alignment_identity, domain=None, range=Optional[float])

slots.V1p4Alignment_support = Slot(uri=AK_SCHEMA.V1p4Alignment_support, name="V1p4Alignment_support", curie=AK_SCHEMA.curie('V1p4Alignment_support'),
                   model_uri=AK_SCHEMA.V1p4Alignment_support, domain=None, range=Optional[float])

slots.V1p4Alignment_cigar = Slot(uri=AK_SCHEMA.V1p4Alignment_cigar, name="V1p4Alignment_cigar", curie=AK_SCHEMA.curie('V1p4Alignment_cigar'),
                   model_uri=AK_SCHEMA.V1p4Alignment_cigar, domain=None, range=str)

slots.V1p4Alignment_sequence_start = Slot(uri=AK_SCHEMA.V1p4Alignment_sequence_start, name="V1p4Alignment_sequence_start", curie=AK_SCHEMA.curie('V1p4Alignment_sequence_start'),
                   model_uri=AK_SCHEMA.V1p4Alignment_sequence_start, domain=None, range=Optional[int])

slots.V1p4Alignment_sequence_end = Slot(uri=AK_SCHEMA.V1p4Alignment_sequence_end, name="V1p4Alignment_sequence_end", curie=AK_SCHEMA.curie('V1p4Alignment_sequence_end'),
                   model_uri=AK_SCHEMA.V1p4Alignment_sequence_end, domain=None, range=Optional[int])

slots.V1p4Alignment_germline_start = Slot(uri=AK_SCHEMA.V1p4Alignment_germline_start, name="V1p4Alignment_germline_start", curie=AK_SCHEMA.curie('V1p4Alignment_germline_start'),
                   model_uri=AK_SCHEMA.V1p4Alignment_germline_start, domain=None, range=Optional[int])

slots.V1p4Alignment_germline_end = Slot(uri=AK_SCHEMA.V1p4Alignment_germline_end, name="V1p4Alignment_germline_end", curie=AK_SCHEMA.curie('V1p4Alignment_germline_end'),
                   model_uri=AK_SCHEMA.V1p4Alignment_germline_end, domain=None, range=Optional[int])

slots.V1p4Alignment_rank = Slot(uri=AK_SCHEMA.V1p4Alignment_rank, name="V1p4Alignment_rank", curie=AK_SCHEMA.curie('V1p4Alignment_rank'),
                   model_uri=AK_SCHEMA.V1p4Alignment_rank, domain=None, range=Optional[int])

slots.V1p4Alignment_data_processing_id = Slot(uri=AK_SCHEMA.V1p4Alignment_data_processing_id, name="V1p4Alignment_data_processing_id", curie=AK_SCHEMA.curie('V1p4Alignment_data_processing_id'),
                   model_uri=AK_SCHEMA.V1p4Alignment_data_processing_id, domain=None, range=Optional[str])

slots.V1p4Rearrangement_sequence_id = Slot(uri=AK_SCHEMA.V1p4Rearrangement_sequence_id, name="V1p4Rearrangement_sequence_id", curie=AK_SCHEMA.curie('V1p4Rearrangement_sequence_id'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_sequence_id, domain=None, range=str)

slots.V1p4Rearrangement_sequence = Slot(uri=AK_SCHEMA.V1p4Rearrangement_sequence, name="V1p4Rearrangement_sequence", curie=AK_SCHEMA.curie('V1p4Rearrangement_sequence'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_sequence, domain=None, range=str)

slots.V1p4Rearrangement_quality = Slot(uri=AK_SCHEMA.V1p4Rearrangement_quality, name="V1p4Rearrangement_quality", curie=AK_SCHEMA.curie('V1p4Rearrangement_quality'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_quality, domain=None, range=Optional[str])

slots.V1p4Rearrangement_sequence_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_sequence_aa, name="V1p4Rearrangement_sequence_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_sequence_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_sequence_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_rev_comp = Slot(uri=AK_SCHEMA.V1p4Rearrangement_rev_comp, name="V1p4Rearrangement_rev_comp", curie=AK_SCHEMA.curie('V1p4Rearrangement_rev_comp'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_rev_comp, domain=None, range=Union[bool, Bool])

slots.V1p4Rearrangement_productive = Slot(uri=AK_SCHEMA.V1p4Rearrangement_productive, name="V1p4Rearrangement_productive", curie=AK_SCHEMA.curie('V1p4Rearrangement_productive'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_productive, domain=None, range=Union[bool, Bool])

slots.V1p4Rearrangement_vj_in_frame = Slot(uri=AK_SCHEMA.V1p4Rearrangement_vj_in_frame, name="V1p4Rearrangement_vj_in_frame", curie=AK_SCHEMA.curie('V1p4Rearrangement_vj_in_frame'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_vj_in_frame, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4Rearrangement_stop_codon = Slot(uri=AK_SCHEMA.V1p4Rearrangement_stop_codon, name="V1p4Rearrangement_stop_codon", curie=AK_SCHEMA.curie('V1p4Rearrangement_stop_codon'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_stop_codon, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4Rearrangement_complete_vdj = Slot(uri=AK_SCHEMA.V1p4Rearrangement_complete_vdj, name="V1p4Rearrangement_complete_vdj", curie=AK_SCHEMA.curie('V1p4Rearrangement_complete_vdj'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_complete_vdj, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4Rearrangement_locus = Slot(uri=AK_SCHEMA.V1p4Rearrangement_locus, name="V1p4Rearrangement_locus", curie=AK_SCHEMA.curie('V1p4Rearrangement_locus'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_locus, domain=None, range=Optional[Union[str, "V1p4Locus"]])

slots.V1p4Rearrangement_locus_species = Slot(uri=AK_SCHEMA.V1p4Rearrangement_locus_species, name="V1p4Rearrangement_locus_species", curie=AK_SCHEMA.curie('V1p4Rearrangement_locus_species'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_locus_species, domain=None, range=Optional[Union[str, "V1p4LocusSpecies"]])

slots.V1p4Rearrangement_v_call = Slot(uri=AK_SCHEMA.V1p4Rearrangement_v_call, name="V1p4Rearrangement_v_call", curie=AK_SCHEMA.curie('V1p4Rearrangement_v_call'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_v_call, domain=None, range=str)

slots.V1p4Rearrangement_d_call = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d_call, name="V1p4Rearrangement_d_call", curie=AK_SCHEMA.curie('V1p4Rearrangement_d_call'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d_call, domain=None, range=str)

slots.V1p4Rearrangement_d2_call = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d2_call, name="V1p4Rearrangement_d2_call", curie=AK_SCHEMA.curie('V1p4Rearrangement_d2_call'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d2_call, domain=None, range=Optional[str])

slots.V1p4Rearrangement_j_call = Slot(uri=AK_SCHEMA.V1p4Rearrangement_j_call, name="V1p4Rearrangement_j_call", curie=AK_SCHEMA.curie('V1p4Rearrangement_j_call'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_j_call, domain=None, range=str)

slots.V1p4Rearrangement_c_call = Slot(uri=AK_SCHEMA.V1p4Rearrangement_c_call, name="V1p4Rearrangement_c_call", curie=AK_SCHEMA.curie('V1p4Rearrangement_c_call'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_c_call, domain=None, range=Optional[str])

slots.V1p4Rearrangement_sequence_alignment = Slot(uri=AK_SCHEMA.V1p4Rearrangement_sequence_alignment, name="V1p4Rearrangement_sequence_alignment", curie=AK_SCHEMA.curie('V1p4Rearrangement_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_sequence_alignment, domain=None, range=str)

slots.V1p4Rearrangement_quality_alignment = Slot(uri=AK_SCHEMA.V1p4Rearrangement_quality_alignment, name="V1p4Rearrangement_quality_alignment", curie=AK_SCHEMA.curie('V1p4Rearrangement_quality_alignment'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_quality_alignment, domain=None, range=Optional[str])

slots.V1p4Rearrangement_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_sequence_alignment_aa, name="V1p4Rearrangement_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_germline_alignment = Slot(uri=AK_SCHEMA.V1p4Rearrangement_germline_alignment, name="V1p4Rearrangement_germline_alignment", curie=AK_SCHEMA.curie('V1p4Rearrangement_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_germline_alignment, domain=None, range=str)

slots.V1p4Rearrangement_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_germline_alignment_aa, name="V1p4Rearrangement_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_junction = Slot(uri=AK_SCHEMA.V1p4Rearrangement_junction, name="V1p4Rearrangement_junction", curie=AK_SCHEMA.curie('V1p4Rearrangement_junction'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_junction, domain=None, range=str)

slots.V1p4Rearrangement_junction_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_junction_aa, name="V1p4Rearrangement_junction_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_junction_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_junction_aa, domain=None, range=str)

slots.V1p4Rearrangement_np1 = Slot(uri=AK_SCHEMA.V1p4Rearrangement_np1, name="V1p4Rearrangement_np1", curie=AK_SCHEMA.curie('V1p4Rearrangement_np1'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_np1, domain=None, range=Optional[str])

slots.V1p4Rearrangement_np1_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_np1_aa, name="V1p4Rearrangement_np1_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_np1_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_np1_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_np2 = Slot(uri=AK_SCHEMA.V1p4Rearrangement_np2, name="V1p4Rearrangement_np2", curie=AK_SCHEMA.curie('V1p4Rearrangement_np2'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_np2, domain=None, range=Optional[str])

slots.V1p4Rearrangement_np2_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_np2_aa, name="V1p4Rearrangement_np2_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_np2_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_np2_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_np3 = Slot(uri=AK_SCHEMA.V1p4Rearrangement_np3, name="V1p4Rearrangement_np3", curie=AK_SCHEMA.curie('V1p4Rearrangement_np3'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_np3, domain=None, range=Optional[str])

slots.V1p4Rearrangement_np3_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_np3_aa, name="V1p4Rearrangement_np3_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_np3_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_np3_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_cdr1 = Slot(uri=AK_SCHEMA.V1p4Rearrangement_cdr1, name="V1p4Rearrangement_cdr1", curie=AK_SCHEMA.curie('V1p4Rearrangement_cdr1'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_cdr1, domain=None, range=Optional[str])

slots.V1p4Rearrangement_cdr1_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_cdr1_aa, name="V1p4Rearrangement_cdr1_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_cdr1_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_cdr1_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_cdr2 = Slot(uri=AK_SCHEMA.V1p4Rearrangement_cdr2, name="V1p4Rearrangement_cdr2", curie=AK_SCHEMA.curie('V1p4Rearrangement_cdr2'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_cdr2, domain=None, range=Optional[str])

slots.V1p4Rearrangement_cdr2_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_cdr2_aa, name="V1p4Rearrangement_cdr2_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_cdr2_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_cdr2_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_cdr3 = Slot(uri=AK_SCHEMA.V1p4Rearrangement_cdr3, name="V1p4Rearrangement_cdr3", curie=AK_SCHEMA.curie('V1p4Rearrangement_cdr3'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_cdr3, domain=None, range=Optional[str])

slots.V1p4Rearrangement_cdr3_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_cdr3_aa, name="V1p4Rearrangement_cdr3_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_cdr3_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_cdr3_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_fwr1 = Slot(uri=AK_SCHEMA.V1p4Rearrangement_fwr1, name="V1p4Rearrangement_fwr1", curie=AK_SCHEMA.curie('V1p4Rearrangement_fwr1'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_fwr1, domain=None, range=Optional[str])

slots.V1p4Rearrangement_fwr1_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_fwr1_aa, name="V1p4Rearrangement_fwr1_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_fwr1_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_fwr1_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_fwr2 = Slot(uri=AK_SCHEMA.V1p4Rearrangement_fwr2, name="V1p4Rearrangement_fwr2", curie=AK_SCHEMA.curie('V1p4Rearrangement_fwr2'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_fwr2, domain=None, range=Optional[str])

slots.V1p4Rearrangement_fwr2_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_fwr2_aa, name="V1p4Rearrangement_fwr2_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_fwr2_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_fwr2_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_fwr3 = Slot(uri=AK_SCHEMA.V1p4Rearrangement_fwr3, name="V1p4Rearrangement_fwr3", curie=AK_SCHEMA.curie('V1p4Rearrangement_fwr3'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_fwr3, domain=None, range=Optional[str])

slots.V1p4Rearrangement_fwr3_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_fwr3_aa, name="V1p4Rearrangement_fwr3_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_fwr3_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_fwr3_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_fwr4 = Slot(uri=AK_SCHEMA.V1p4Rearrangement_fwr4, name="V1p4Rearrangement_fwr4", curie=AK_SCHEMA.curie('V1p4Rearrangement_fwr4'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_fwr4, domain=None, range=Optional[str])

slots.V1p4Rearrangement_fwr4_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_fwr4_aa, name="V1p4Rearrangement_fwr4_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_fwr4_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_fwr4_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_v_score = Slot(uri=AK_SCHEMA.V1p4Rearrangement_v_score, name="V1p4Rearrangement_v_score", curie=AK_SCHEMA.curie('V1p4Rearrangement_v_score'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_v_score, domain=None, range=Optional[float])

slots.V1p4Rearrangement_v_identity = Slot(uri=AK_SCHEMA.V1p4Rearrangement_v_identity, name="V1p4Rearrangement_v_identity", curie=AK_SCHEMA.curie('V1p4Rearrangement_v_identity'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_v_identity, domain=None, range=Optional[float])

slots.V1p4Rearrangement_v_support = Slot(uri=AK_SCHEMA.V1p4Rearrangement_v_support, name="V1p4Rearrangement_v_support", curie=AK_SCHEMA.curie('V1p4Rearrangement_v_support'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_v_support, domain=None, range=Optional[float])

slots.V1p4Rearrangement_v_cigar = Slot(uri=AK_SCHEMA.V1p4Rearrangement_v_cigar, name="V1p4Rearrangement_v_cigar", curie=AK_SCHEMA.curie('V1p4Rearrangement_v_cigar'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_v_cigar, domain=None, range=str)

slots.V1p4Rearrangement_d_score = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d_score, name="V1p4Rearrangement_d_score", curie=AK_SCHEMA.curie('V1p4Rearrangement_d_score'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d_score, domain=None, range=Optional[float])

slots.V1p4Rearrangement_d_identity = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d_identity, name="V1p4Rearrangement_d_identity", curie=AK_SCHEMA.curie('V1p4Rearrangement_d_identity'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d_identity, domain=None, range=Optional[float])

slots.V1p4Rearrangement_d_support = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d_support, name="V1p4Rearrangement_d_support", curie=AK_SCHEMA.curie('V1p4Rearrangement_d_support'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d_support, domain=None, range=Optional[float])

slots.V1p4Rearrangement_d_cigar = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d_cigar, name="V1p4Rearrangement_d_cigar", curie=AK_SCHEMA.curie('V1p4Rearrangement_d_cigar'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d_cigar, domain=None, range=str)

slots.V1p4Rearrangement_d2_score = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d2_score, name="V1p4Rearrangement_d2_score", curie=AK_SCHEMA.curie('V1p4Rearrangement_d2_score'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d2_score, domain=None, range=Optional[float])

slots.V1p4Rearrangement_d2_identity = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d2_identity, name="V1p4Rearrangement_d2_identity", curie=AK_SCHEMA.curie('V1p4Rearrangement_d2_identity'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d2_identity, domain=None, range=Optional[float])

slots.V1p4Rearrangement_d2_support = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d2_support, name="V1p4Rearrangement_d2_support", curie=AK_SCHEMA.curie('V1p4Rearrangement_d2_support'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d2_support, domain=None, range=Optional[float])

slots.V1p4Rearrangement_d2_cigar = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d2_cigar, name="V1p4Rearrangement_d2_cigar", curie=AK_SCHEMA.curie('V1p4Rearrangement_d2_cigar'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d2_cigar, domain=None, range=Optional[str])

slots.V1p4Rearrangement_j_score = Slot(uri=AK_SCHEMA.V1p4Rearrangement_j_score, name="V1p4Rearrangement_j_score", curie=AK_SCHEMA.curie('V1p4Rearrangement_j_score'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_j_score, domain=None, range=Optional[float])

slots.V1p4Rearrangement_j_identity = Slot(uri=AK_SCHEMA.V1p4Rearrangement_j_identity, name="V1p4Rearrangement_j_identity", curie=AK_SCHEMA.curie('V1p4Rearrangement_j_identity'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_j_identity, domain=None, range=Optional[float])

slots.V1p4Rearrangement_j_support = Slot(uri=AK_SCHEMA.V1p4Rearrangement_j_support, name="V1p4Rearrangement_j_support", curie=AK_SCHEMA.curie('V1p4Rearrangement_j_support'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_j_support, domain=None, range=Optional[float])

slots.V1p4Rearrangement_j_cigar = Slot(uri=AK_SCHEMA.V1p4Rearrangement_j_cigar, name="V1p4Rearrangement_j_cigar", curie=AK_SCHEMA.curie('V1p4Rearrangement_j_cigar'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_j_cigar, domain=None, range=str)

slots.V1p4Rearrangement_c_score = Slot(uri=AK_SCHEMA.V1p4Rearrangement_c_score, name="V1p4Rearrangement_c_score", curie=AK_SCHEMA.curie('V1p4Rearrangement_c_score'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_c_score, domain=None, range=Optional[float])

slots.V1p4Rearrangement_c_identity = Slot(uri=AK_SCHEMA.V1p4Rearrangement_c_identity, name="V1p4Rearrangement_c_identity", curie=AK_SCHEMA.curie('V1p4Rearrangement_c_identity'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_c_identity, domain=None, range=Optional[float])

slots.V1p4Rearrangement_c_support = Slot(uri=AK_SCHEMA.V1p4Rearrangement_c_support, name="V1p4Rearrangement_c_support", curie=AK_SCHEMA.curie('V1p4Rearrangement_c_support'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_c_support, domain=None, range=Optional[float])

slots.V1p4Rearrangement_c_cigar = Slot(uri=AK_SCHEMA.V1p4Rearrangement_c_cigar, name="V1p4Rearrangement_c_cigar", curie=AK_SCHEMA.curie('V1p4Rearrangement_c_cigar'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_c_cigar, domain=None, range=Optional[str])

slots.V1p4Rearrangement_v_sequence_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_v_sequence_start, name="V1p4Rearrangement_v_sequence_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_v_sequence_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_v_sequence_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_v_sequence_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_v_sequence_end, name="V1p4Rearrangement_v_sequence_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_v_sequence_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_v_sequence_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_v_germline_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_v_germline_start, name="V1p4Rearrangement_v_germline_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_v_germline_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_v_germline_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_v_germline_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_v_germline_end, name="V1p4Rearrangement_v_germline_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_v_germline_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_v_germline_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_v_alignment_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_v_alignment_start, name="V1p4Rearrangement_v_alignment_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_v_alignment_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_v_alignment_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_v_alignment_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_v_alignment_end, name="V1p4Rearrangement_v_alignment_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_v_alignment_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_v_alignment_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_d_sequence_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d_sequence_start, name="V1p4Rearrangement_d_sequence_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_d_sequence_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d_sequence_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_d_sequence_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d_sequence_end, name="V1p4Rearrangement_d_sequence_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_d_sequence_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d_sequence_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_d_germline_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d_germline_start, name="V1p4Rearrangement_d_germline_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_d_germline_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d_germline_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_d_germline_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d_germline_end, name="V1p4Rearrangement_d_germline_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_d_germline_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d_germline_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_d_alignment_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d_alignment_start, name="V1p4Rearrangement_d_alignment_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_d_alignment_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d_alignment_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_d_alignment_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d_alignment_end, name="V1p4Rearrangement_d_alignment_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_d_alignment_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d_alignment_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_d2_sequence_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d2_sequence_start, name="V1p4Rearrangement_d2_sequence_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_d2_sequence_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d2_sequence_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_d2_sequence_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d2_sequence_end, name="V1p4Rearrangement_d2_sequence_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_d2_sequence_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d2_sequence_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_d2_germline_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d2_germline_start, name="V1p4Rearrangement_d2_germline_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_d2_germline_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d2_germline_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_d2_germline_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d2_germline_end, name="V1p4Rearrangement_d2_germline_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_d2_germline_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d2_germline_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_d2_alignment_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d2_alignment_start, name="V1p4Rearrangement_d2_alignment_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_d2_alignment_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d2_alignment_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_d2_alignment_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d2_alignment_end, name="V1p4Rearrangement_d2_alignment_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_d2_alignment_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d2_alignment_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_j_sequence_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_j_sequence_start, name="V1p4Rearrangement_j_sequence_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_j_sequence_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_j_sequence_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_j_sequence_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_j_sequence_end, name="V1p4Rearrangement_j_sequence_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_j_sequence_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_j_sequence_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_j_germline_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_j_germline_start, name="V1p4Rearrangement_j_germline_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_j_germline_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_j_germline_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_j_germline_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_j_germline_end, name="V1p4Rearrangement_j_germline_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_j_germline_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_j_germline_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_j_alignment_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_j_alignment_start, name="V1p4Rearrangement_j_alignment_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_j_alignment_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_j_alignment_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_j_alignment_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_j_alignment_end, name="V1p4Rearrangement_j_alignment_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_j_alignment_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_j_alignment_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_c_sequence_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_c_sequence_start, name="V1p4Rearrangement_c_sequence_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_c_sequence_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_c_sequence_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_c_sequence_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_c_sequence_end, name="V1p4Rearrangement_c_sequence_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_c_sequence_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_c_sequence_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_c_germline_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_c_germline_start, name="V1p4Rearrangement_c_germline_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_c_germline_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_c_germline_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_c_germline_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_c_germline_end, name="V1p4Rearrangement_c_germline_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_c_germline_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_c_germline_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_c_alignment_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_c_alignment_start, name="V1p4Rearrangement_c_alignment_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_c_alignment_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_c_alignment_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_c_alignment_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_c_alignment_end, name="V1p4Rearrangement_c_alignment_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_c_alignment_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_c_alignment_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_cdr1_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_cdr1_start, name="V1p4Rearrangement_cdr1_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_cdr1_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_cdr1_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_cdr1_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_cdr1_end, name="V1p4Rearrangement_cdr1_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_cdr1_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_cdr1_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_cdr2_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_cdr2_start, name="V1p4Rearrangement_cdr2_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_cdr2_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_cdr2_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_cdr2_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_cdr2_end, name="V1p4Rearrangement_cdr2_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_cdr2_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_cdr2_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_cdr3_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_cdr3_start, name="V1p4Rearrangement_cdr3_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_cdr3_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_cdr3_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_cdr3_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_cdr3_end, name="V1p4Rearrangement_cdr3_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_cdr3_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_cdr3_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_fwr1_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_fwr1_start, name="V1p4Rearrangement_fwr1_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_fwr1_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_fwr1_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_fwr1_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_fwr1_end, name="V1p4Rearrangement_fwr1_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_fwr1_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_fwr1_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_fwr2_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_fwr2_start, name="V1p4Rearrangement_fwr2_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_fwr2_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_fwr2_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_fwr2_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_fwr2_end, name="V1p4Rearrangement_fwr2_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_fwr2_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_fwr2_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_fwr3_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_fwr3_start, name="V1p4Rearrangement_fwr3_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_fwr3_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_fwr3_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_fwr3_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_fwr3_end, name="V1p4Rearrangement_fwr3_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_fwr3_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_fwr3_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_fwr4_start = Slot(uri=AK_SCHEMA.V1p4Rearrangement_fwr4_start, name="V1p4Rearrangement_fwr4_start", curie=AK_SCHEMA.curie('V1p4Rearrangement_fwr4_start'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_fwr4_start, domain=None, range=Optional[int])

slots.V1p4Rearrangement_fwr4_end = Slot(uri=AK_SCHEMA.V1p4Rearrangement_fwr4_end, name="V1p4Rearrangement_fwr4_end", curie=AK_SCHEMA.curie('V1p4Rearrangement_fwr4_end'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_fwr4_end, domain=None, range=Optional[int])

slots.V1p4Rearrangement_v_sequence_alignment = Slot(uri=AK_SCHEMA.V1p4Rearrangement_v_sequence_alignment, name="V1p4Rearrangement_v_sequence_alignment", curie=AK_SCHEMA.curie('V1p4Rearrangement_v_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_v_sequence_alignment, domain=None, range=Optional[str])

slots.V1p4Rearrangement_v_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_v_sequence_alignment_aa, name="V1p4Rearrangement_v_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_v_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_v_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_d_sequence_alignment = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d_sequence_alignment, name="V1p4Rearrangement_d_sequence_alignment", curie=AK_SCHEMA.curie('V1p4Rearrangement_d_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d_sequence_alignment, domain=None, range=Optional[str])

slots.V1p4Rearrangement_d_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d_sequence_alignment_aa, name="V1p4Rearrangement_d_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_d_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_d2_sequence_alignment = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d2_sequence_alignment, name="V1p4Rearrangement_d2_sequence_alignment", curie=AK_SCHEMA.curie('V1p4Rearrangement_d2_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d2_sequence_alignment, domain=None, range=Optional[str])

slots.V1p4Rearrangement_d2_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d2_sequence_alignment_aa, name="V1p4Rearrangement_d2_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_d2_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d2_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_j_sequence_alignment = Slot(uri=AK_SCHEMA.V1p4Rearrangement_j_sequence_alignment, name="V1p4Rearrangement_j_sequence_alignment", curie=AK_SCHEMA.curie('V1p4Rearrangement_j_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_j_sequence_alignment, domain=None, range=Optional[str])

slots.V1p4Rearrangement_j_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_j_sequence_alignment_aa, name="V1p4Rearrangement_j_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_j_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_j_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_c_sequence_alignment = Slot(uri=AK_SCHEMA.V1p4Rearrangement_c_sequence_alignment, name="V1p4Rearrangement_c_sequence_alignment", curie=AK_SCHEMA.curie('V1p4Rearrangement_c_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_c_sequence_alignment, domain=None, range=Optional[str])

slots.V1p4Rearrangement_c_sequence_alignment_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_c_sequence_alignment_aa, name="V1p4Rearrangement_c_sequence_alignment_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_c_sequence_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_c_sequence_alignment_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_v_germline_alignment = Slot(uri=AK_SCHEMA.V1p4Rearrangement_v_germline_alignment, name="V1p4Rearrangement_v_germline_alignment", curie=AK_SCHEMA.curie('V1p4Rearrangement_v_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_v_germline_alignment, domain=None, range=Optional[str])

slots.V1p4Rearrangement_v_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_v_germline_alignment_aa, name="V1p4Rearrangement_v_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_v_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_v_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_d_germline_alignment = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d_germline_alignment, name="V1p4Rearrangement_d_germline_alignment", curie=AK_SCHEMA.curie('V1p4Rearrangement_d_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d_germline_alignment, domain=None, range=Optional[str])

slots.V1p4Rearrangement_d_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d_germline_alignment_aa, name="V1p4Rearrangement_d_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_d_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_d2_germline_alignment = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d2_germline_alignment, name="V1p4Rearrangement_d2_germline_alignment", curie=AK_SCHEMA.curie('V1p4Rearrangement_d2_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d2_germline_alignment, domain=None, range=Optional[str])

slots.V1p4Rearrangement_d2_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d2_germline_alignment_aa, name="V1p4Rearrangement_d2_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_d2_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d2_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_j_germline_alignment = Slot(uri=AK_SCHEMA.V1p4Rearrangement_j_germline_alignment, name="V1p4Rearrangement_j_germline_alignment", curie=AK_SCHEMA.curie('V1p4Rearrangement_j_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_j_germline_alignment, domain=None, range=Optional[str])

slots.V1p4Rearrangement_j_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_j_germline_alignment_aa, name="V1p4Rearrangement_j_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_j_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_j_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_c_germline_alignment = Slot(uri=AK_SCHEMA.V1p4Rearrangement_c_germline_alignment, name="V1p4Rearrangement_c_germline_alignment", curie=AK_SCHEMA.curie('V1p4Rearrangement_c_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_c_germline_alignment, domain=None, range=Optional[str])

slots.V1p4Rearrangement_c_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p4Rearrangement_c_germline_alignment_aa, name="V1p4Rearrangement_c_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p4Rearrangement_c_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_c_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p4Rearrangement_junction_length = Slot(uri=AK_SCHEMA.V1p4Rearrangement_junction_length, name="V1p4Rearrangement_junction_length", curie=AK_SCHEMA.curie('V1p4Rearrangement_junction_length'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_junction_length, domain=None, range=Optional[int])

slots.V1p4Rearrangement_junction_aa_length = Slot(uri=AK_SCHEMA.V1p4Rearrangement_junction_aa_length, name="V1p4Rearrangement_junction_aa_length", curie=AK_SCHEMA.curie('V1p4Rearrangement_junction_aa_length'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_junction_aa_length, domain=None, range=Optional[int])

slots.V1p4Rearrangement_np1_length = Slot(uri=AK_SCHEMA.V1p4Rearrangement_np1_length, name="V1p4Rearrangement_np1_length", curie=AK_SCHEMA.curie('V1p4Rearrangement_np1_length'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_np1_length, domain=None, range=Optional[int])

slots.V1p4Rearrangement_np2_length = Slot(uri=AK_SCHEMA.V1p4Rearrangement_np2_length, name="V1p4Rearrangement_np2_length", curie=AK_SCHEMA.curie('V1p4Rearrangement_np2_length'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_np2_length, domain=None, range=Optional[int])

slots.V1p4Rearrangement_np3_length = Slot(uri=AK_SCHEMA.V1p4Rearrangement_np3_length, name="V1p4Rearrangement_np3_length", curie=AK_SCHEMA.curie('V1p4Rearrangement_np3_length'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_np3_length, domain=None, range=Optional[int])

slots.V1p4Rearrangement_n1_length = Slot(uri=AK_SCHEMA.V1p4Rearrangement_n1_length, name="V1p4Rearrangement_n1_length", curie=AK_SCHEMA.curie('V1p4Rearrangement_n1_length'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_n1_length, domain=None, range=Optional[int])

slots.V1p4Rearrangement_n2_length = Slot(uri=AK_SCHEMA.V1p4Rearrangement_n2_length, name="V1p4Rearrangement_n2_length", curie=AK_SCHEMA.curie('V1p4Rearrangement_n2_length'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_n2_length, domain=None, range=Optional[int])

slots.V1p4Rearrangement_n3_length = Slot(uri=AK_SCHEMA.V1p4Rearrangement_n3_length, name="V1p4Rearrangement_n3_length", curie=AK_SCHEMA.curie('V1p4Rearrangement_n3_length'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_n3_length, domain=None, range=Optional[int])

slots.V1p4Rearrangement_p3v_length = Slot(uri=AK_SCHEMA.V1p4Rearrangement_p3v_length, name="V1p4Rearrangement_p3v_length", curie=AK_SCHEMA.curie('V1p4Rearrangement_p3v_length'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_p3v_length, domain=None, range=Optional[int])

slots.V1p4Rearrangement_p5d_length = Slot(uri=AK_SCHEMA.V1p4Rearrangement_p5d_length, name="V1p4Rearrangement_p5d_length", curie=AK_SCHEMA.curie('V1p4Rearrangement_p5d_length'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_p5d_length, domain=None, range=Optional[int])

slots.V1p4Rearrangement_p3d_length = Slot(uri=AK_SCHEMA.V1p4Rearrangement_p3d_length, name="V1p4Rearrangement_p3d_length", curie=AK_SCHEMA.curie('V1p4Rearrangement_p3d_length'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_p3d_length, domain=None, range=Optional[int])

slots.V1p4Rearrangement_p5d2_length = Slot(uri=AK_SCHEMA.V1p4Rearrangement_p5d2_length, name="V1p4Rearrangement_p5d2_length", curie=AK_SCHEMA.curie('V1p4Rearrangement_p5d2_length'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_p5d2_length, domain=None, range=Optional[int])

slots.V1p4Rearrangement_p3d2_length = Slot(uri=AK_SCHEMA.V1p4Rearrangement_p3d2_length, name="V1p4Rearrangement_p3d2_length", curie=AK_SCHEMA.curie('V1p4Rearrangement_p3d2_length'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_p3d2_length, domain=None, range=Optional[int])

slots.V1p4Rearrangement_p5j_length = Slot(uri=AK_SCHEMA.V1p4Rearrangement_p5j_length, name="V1p4Rearrangement_p5j_length", curie=AK_SCHEMA.curie('V1p4Rearrangement_p5j_length'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_p5j_length, domain=None, range=Optional[int])

slots.V1p4Rearrangement_v_frameshift = Slot(uri=AK_SCHEMA.V1p4Rearrangement_v_frameshift, name="V1p4Rearrangement_v_frameshift", curie=AK_SCHEMA.curie('V1p4Rearrangement_v_frameshift'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_v_frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4Rearrangement_j_frameshift = Slot(uri=AK_SCHEMA.V1p4Rearrangement_j_frameshift, name="V1p4Rearrangement_j_frameshift", curie=AK_SCHEMA.curie('V1p4Rearrangement_j_frameshift'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_j_frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.V1p4Rearrangement_d_frame = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d_frame, name="V1p4Rearrangement_d_frame", curie=AK_SCHEMA.curie('V1p4Rearrangement_d_frame'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d_frame, domain=None, range=Optional[int])

slots.V1p4Rearrangement_d2_frame = Slot(uri=AK_SCHEMA.V1p4Rearrangement_d2_frame, name="V1p4Rearrangement_d2_frame", curie=AK_SCHEMA.curie('V1p4Rearrangement_d2_frame'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_d2_frame, domain=None, range=Optional[int])

slots.V1p4Rearrangement_consensus_count = Slot(uri=AK_SCHEMA.V1p4Rearrangement_consensus_count, name="V1p4Rearrangement_consensus_count", curie=AK_SCHEMA.curie('V1p4Rearrangement_consensus_count'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_consensus_count, domain=None, range=Optional[int])

slots.V1p4Rearrangement_duplicate_count = Slot(uri=AK_SCHEMA.V1p4Rearrangement_duplicate_count, name="V1p4Rearrangement_duplicate_count", curie=AK_SCHEMA.curie('V1p4Rearrangement_duplicate_count'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_duplicate_count, domain=None, range=Optional[int])

slots.V1p4Rearrangement_umi_count = Slot(uri=AK_SCHEMA.V1p4Rearrangement_umi_count, name="V1p4Rearrangement_umi_count", curie=AK_SCHEMA.curie('V1p4Rearrangement_umi_count'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_umi_count, domain=None, range=Optional[int])

slots.V1p4Rearrangement_cell_id = Slot(uri=AK_SCHEMA.V1p4Rearrangement_cell_id, name="V1p4Rearrangement_cell_id", curie=AK_SCHEMA.curie('V1p4Rearrangement_cell_id'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_cell_id, domain=None, range=Optional[str])

slots.V1p4Rearrangement_clone_id = Slot(uri=AK_SCHEMA.V1p4Rearrangement_clone_id, name="V1p4Rearrangement_clone_id", curie=AK_SCHEMA.curie('V1p4Rearrangement_clone_id'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_clone_id, domain=None, range=Optional[str])

slots.V1p4Rearrangement_reactivity_id = Slot(uri=AK_SCHEMA.V1p4Rearrangement_reactivity_id, name="V1p4Rearrangement_reactivity_id", curie=AK_SCHEMA.curie('V1p4Rearrangement_reactivity_id'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_reactivity_id, domain=None, range=Optional[str])

slots.V1p4Rearrangement_reactivity_ref = Slot(uri=AK_SCHEMA.V1p4Rearrangement_reactivity_ref, name="V1p4Rearrangement_reactivity_ref", curie=AK_SCHEMA.curie('V1p4Rearrangement_reactivity_ref'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_reactivity_ref, domain=None, range=Optional[str])

slots.V1p4Rearrangement_repertoire_id = Slot(uri=AK_SCHEMA.V1p4Rearrangement_repertoire_id, name="V1p4Rearrangement_repertoire_id", curie=AK_SCHEMA.curie('V1p4Rearrangement_repertoire_id'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_repertoire_id, domain=None, range=Optional[str])

slots.V1p4Rearrangement_sample_processing_id = Slot(uri=AK_SCHEMA.V1p4Rearrangement_sample_processing_id, name="V1p4Rearrangement_sample_processing_id", curie=AK_SCHEMA.curie('V1p4Rearrangement_sample_processing_id'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_sample_processing_id, domain=None, range=Optional[str])

slots.V1p4Rearrangement_data_processing_id = Slot(uri=AK_SCHEMA.V1p4Rearrangement_data_processing_id, name="V1p4Rearrangement_data_processing_id", curie=AK_SCHEMA.curie('V1p4Rearrangement_data_processing_id'),
                   model_uri=AK_SCHEMA.V1p4Rearrangement_data_processing_id, domain=None, range=Optional[str])

slots.V1p4Clone_clone_id = Slot(uri=AK_SCHEMA.V1p4Clone_clone_id, name="V1p4Clone_clone_id", curie=AK_SCHEMA.curie('V1p4Clone_clone_id'),
                   model_uri=AK_SCHEMA.V1p4Clone_clone_id, domain=None, range=str)

slots.V1p4Clone_repertoire_id = Slot(uri=AK_SCHEMA.V1p4Clone_repertoire_id, name="V1p4Clone_repertoire_id", curie=AK_SCHEMA.curie('V1p4Clone_repertoire_id'),
                   model_uri=AK_SCHEMA.V1p4Clone_repertoire_id, domain=None, range=Optional[str])

slots.V1p4Clone_data_processing_id = Slot(uri=AK_SCHEMA.V1p4Clone_data_processing_id, name="V1p4Clone_data_processing_id", curie=AK_SCHEMA.curie('V1p4Clone_data_processing_id'),
                   model_uri=AK_SCHEMA.V1p4Clone_data_processing_id, domain=None, range=Optional[str])

slots.V1p4Clone_sequences = Slot(uri=AK_SCHEMA.V1p4Clone_sequences, name="V1p4Clone_sequences", curie=AK_SCHEMA.curie('V1p4Clone_sequences'),
                   model_uri=AK_SCHEMA.V1p4Clone_sequences, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4Clone_v_call = Slot(uri=AK_SCHEMA.V1p4Clone_v_call, name="V1p4Clone_v_call", curie=AK_SCHEMA.curie('V1p4Clone_v_call'),
                   model_uri=AK_SCHEMA.V1p4Clone_v_call, domain=None, range=Optional[str])

slots.V1p4Clone_d_call = Slot(uri=AK_SCHEMA.V1p4Clone_d_call, name="V1p4Clone_d_call", curie=AK_SCHEMA.curie('V1p4Clone_d_call'),
                   model_uri=AK_SCHEMA.V1p4Clone_d_call, domain=None, range=Optional[str])

slots.V1p4Clone_j_call = Slot(uri=AK_SCHEMA.V1p4Clone_j_call, name="V1p4Clone_j_call", curie=AK_SCHEMA.curie('V1p4Clone_j_call'),
                   model_uri=AK_SCHEMA.V1p4Clone_j_call, domain=None, range=Optional[str])

slots.V1p4Clone_junction = Slot(uri=AK_SCHEMA.V1p4Clone_junction, name="V1p4Clone_junction", curie=AK_SCHEMA.curie('V1p4Clone_junction'),
                   model_uri=AK_SCHEMA.V1p4Clone_junction, domain=None, range=Optional[str])

slots.V1p4Clone_junction_aa = Slot(uri=AK_SCHEMA.V1p4Clone_junction_aa, name="V1p4Clone_junction_aa", curie=AK_SCHEMA.curie('V1p4Clone_junction_aa'),
                   model_uri=AK_SCHEMA.V1p4Clone_junction_aa, domain=None, range=Optional[str])

slots.V1p4Clone_junction_length = Slot(uri=AK_SCHEMA.V1p4Clone_junction_length, name="V1p4Clone_junction_length", curie=AK_SCHEMA.curie('V1p4Clone_junction_length'),
                   model_uri=AK_SCHEMA.V1p4Clone_junction_length, domain=None, range=Optional[int])

slots.V1p4Clone_junction_aa_length = Slot(uri=AK_SCHEMA.V1p4Clone_junction_aa_length, name="V1p4Clone_junction_aa_length", curie=AK_SCHEMA.curie('V1p4Clone_junction_aa_length'),
                   model_uri=AK_SCHEMA.V1p4Clone_junction_aa_length, domain=None, range=Optional[int])

slots.V1p4Clone_germline_alignment = Slot(uri=AK_SCHEMA.V1p4Clone_germline_alignment, name="V1p4Clone_germline_alignment", curie=AK_SCHEMA.curie('V1p4Clone_germline_alignment'),
                   model_uri=AK_SCHEMA.V1p4Clone_germline_alignment, domain=None, range=str)

slots.V1p4Clone_germline_alignment_aa = Slot(uri=AK_SCHEMA.V1p4Clone_germline_alignment_aa, name="V1p4Clone_germline_alignment_aa", curie=AK_SCHEMA.curie('V1p4Clone_germline_alignment_aa'),
                   model_uri=AK_SCHEMA.V1p4Clone_germline_alignment_aa, domain=None, range=Optional[str])

slots.V1p4Clone_v_alignment_start = Slot(uri=AK_SCHEMA.V1p4Clone_v_alignment_start, name="V1p4Clone_v_alignment_start", curie=AK_SCHEMA.curie('V1p4Clone_v_alignment_start'),
                   model_uri=AK_SCHEMA.V1p4Clone_v_alignment_start, domain=None, range=Optional[int])

slots.V1p4Clone_v_alignment_end = Slot(uri=AK_SCHEMA.V1p4Clone_v_alignment_end, name="V1p4Clone_v_alignment_end", curie=AK_SCHEMA.curie('V1p4Clone_v_alignment_end'),
                   model_uri=AK_SCHEMA.V1p4Clone_v_alignment_end, domain=None, range=Optional[int])

slots.V1p4Clone_d_alignment_start = Slot(uri=AK_SCHEMA.V1p4Clone_d_alignment_start, name="V1p4Clone_d_alignment_start", curie=AK_SCHEMA.curie('V1p4Clone_d_alignment_start'),
                   model_uri=AK_SCHEMA.V1p4Clone_d_alignment_start, domain=None, range=Optional[int])

slots.V1p4Clone_d_alignment_end = Slot(uri=AK_SCHEMA.V1p4Clone_d_alignment_end, name="V1p4Clone_d_alignment_end", curie=AK_SCHEMA.curie('V1p4Clone_d_alignment_end'),
                   model_uri=AK_SCHEMA.V1p4Clone_d_alignment_end, domain=None, range=Optional[int])

slots.V1p4Clone_j_alignment_start = Slot(uri=AK_SCHEMA.V1p4Clone_j_alignment_start, name="V1p4Clone_j_alignment_start", curie=AK_SCHEMA.curie('V1p4Clone_j_alignment_start'),
                   model_uri=AK_SCHEMA.V1p4Clone_j_alignment_start, domain=None, range=Optional[int])

slots.V1p4Clone_j_alignment_end = Slot(uri=AK_SCHEMA.V1p4Clone_j_alignment_end, name="V1p4Clone_j_alignment_end", curie=AK_SCHEMA.curie('V1p4Clone_j_alignment_end'),
                   model_uri=AK_SCHEMA.V1p4Clone_j_alignment_end, domain=None, range=Optional[int])

slots.V1p4Clone_junction_start = Slot(uri=AK_SCHEMA.V1p4Clone_junction_start, name="V1p4Clone_junction_start", curie=AK_SCHEMA.curie('V1p4Clone_junction_start'),
                   model_uri=AK_SCHEMA.V1p4Clone_junction_start, domain=None, range=Optional[int])

slots.V1p4Clone_junction_end = Slot(uri=AK_SCHEMA.V1p4Clone_junction_end, name="V1p4Clone_junction_end", curie=AK_SCHEMA.curie('V1p4Clone_junction_end'),
                   model_uri=AK_SCHEMA.V1p4Clone_junction_end, domain=None, range=Optional[int])

slots.V1p4Clone_umi_count = Slot(uri=AK_SCHEMA.V1p4Clone_umi_count, name="V1p4Clone_umi_count", curie=AK_SCHEMA.curie('V1p4Clone_umi_count'),
                   model_uri=AK_SCHEMA.V1p4Clone_umi_count, domain=None, range=Optional[int])

slots.V1p4Clone_clone_count = Slot(uri=AK_SCHEMA.V1p4Clone_clone_count, name="V1p4Clone_clone_count", curie=AK_SCHEMA.curie('V1p4Clone_clone_count'),
                   model_uri=AK_SCHEMA.V1p4Clone_clone_count, domain=None, range=Optional[int])

slots.V1p4Clone_seed_id = Slot(uri=AK_SCHEMA.V1p4Clone_seed_id, name="V1p4Clone_seed_id", curie=AK_SCHEMA.curie('V1p4Clone_seed_id'),
                   model_uri=AK_SCHEMA.V1p4Clone_seed_id, domain=None, range=Optional[str])

slots.V1p4Tree_tree_id = Slot(uri=AK_SCHEMA.V1p4Tree_tree_id, name="V1p4Tree_tree_id", curie=AK_SCHEMA.curie('V1p4Tree_tree_id'),
                   model_uri=AK_SCHEMA.V1p4Tree_tree_id, domain=None, range=str)

slots.V1p4Tree_clone_id = Slot(uri=AK_SCHEMA.V1p4Tree_clone_id, name="V1p4Tree_clone_id", curie=AK_SCHEMA.curie('V1p4Tree_clone_id'),
                   model_uri=AK_SCHEMA.V1p4Tree_clone_id, domain=None, range=str)

slots.V1p4Tree_newick = Slot(uri=AK_SCHEMA.V1p4Tree_newick, name="V1p4Tree_newick", curie=AK_SCHEMA.curie('V1p4Tree_newick'),
                   model_uri=AK_SCHEMA.V1p4Tree_newick, domain=None, range=str)

slots.V1p4Tree_nodes = Slot(uri=AK_SCHEMA.V1p4Tree_nodes, name="V1p4Tree_nodes", curie=AK_SCHEMA.curie('V1p4Tree_nodes'),
                   model_uri=AK_SCHEMA.V1p4Tree_nodes, domain=None, range=Optional[Union[Union[dict, V1p4Node], List[Union[dict, V1p4Node]]]])

slots.V1p4Node_sequence_id = Slot(uri=AK_SCHEMA.V1p4Node_sequence_id, name="V1p4Node_sequence_id", curie=AK_SCHEMA.curie('V1p4Node_sequence_id'),
                   model_uri=AK_SCHEMA.V1p4Node_sequence_id, domain=None, range=str)

slots.V1p4Node_sequence_alignment = Slot(uri=AK_SCHEMA.V1p4Node_sequence_alignment, name="V1p4Node_sequence_alignment", curie=AK_SCHEMA.curie('V1p4Node_sequence_alignment'),
                   model_uri=AK_SCHEMA.V1p4Node_sequence_alignment, domain=None, range=Optional[str])

slots.V1p4Node_junction = Slot(uri=AK_SCHEMA.V1p4Node_junction, name="V1p4Node_junction", curie=AK_SCHEMA.curie('V1p4Node_junction'),
                   model_uri=AK_SCHEMA.V1p4Node_junction, domain=None, range=Optional[str])

slots.V1p4Node_junction_aa = Slot(uri=AK_SCHEMA.V1p4Node_junction_aa, name="V1p4Node_junction_aa", curie=AK_SCHEMA.curie('V1p4Node_junction_aa'),
                   model_uri=AK_SCHEMA.V1p4Node_junction_aa, domain=None, range=Optional[str])

slots.V1p4Cell_cell_id = Slot(uri=AK_SCHEMA.V1p4Cell_cell_id, name="V1p4Cell_cell_id", curie=AK_SCHEMA.curie('V1p4Cell_cell_id'),
                   model_uri=AK_SCHEMA.V1p4Cell_cell_id, domain=None, range=str)

slots.V1p4Cell_repertoire_id = Slot(uri=AK_SCHEMA.V1p4Cell_repertoire_id, name="V1p4Cell_repertoire_id", curie=AK_SCHEMA.curie('V1p4Cell_repertoire_id'),
                   model_uri=AK_SCHEMA.V1p4Cell_repertoire_id, domain=None, range=str)

slots.V1p4Cell_data_processing_id = Slot(uri=AK_SCHEMA.V1p4Cell_data_processing_id, name="V1p4Cell_data_processing_id", curie=AK_SCHEMA.curie('V1p4Cell_data_processing_id'),
                   model_uri=AK_SCHEMA.V1p4Cell_data_processing_id, domain=None, range=Optional[str])

slots.V1p4Cell_receptors = Slot(uri=AK_SCHEMA.V1p4Cell_receptors, name="V1p4Cell_receptors", curie=AK_SCHEMA.curie('V1p4Cell_receptors'),
                   model_uri=AK_SCHEMA.V1p4Cell_receptors, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4Cell_cell_subset = Slot(uri=AK_SCHEMA.V1p4Cell_cell_subset, name="V1p4Cell_cell_subset", curie=AK_SCHEMA.curie('V1p4Cell_cell_subset'),
                   model_uri=AK_SCHEMA.V1p4Cell_cell_subset, domain=None, range=Optional[Union[str, "V1p4CellSubset"]])

slots.V1p4Cell_cell_phenotype = Slot(uri=AK_SCHEMA.V1p4Cell_cell_phenotype, name="V1p4Cell_cell_phenotype", curie=AK_SCHEMA.curie('V1p4Cell_cell_phenotype'),
                   model_uri=AK_SCHEMA.V1p4Cell_cell_phenotype, domain=None, range=Optional[str])

slots.V1p4Cell_cell_label = Slot(uri=AK_SCHEMA.V1p4Cell_cell_label, name="V1p4Cell_cell_label", curie=AK_SCHEMA.curie('V1p4Cell_cell_label'),
                   model_uri=AK_SCHEMA.V1p4Cell_cell_label, domain=None, range=Optional[str])

slots.V1p4Cell_virtual_pairing = Slot(uri=AK_SCHEMA.V1p4Cell_virtual_pairing, name="V1p4Cell_virtual_pairing", curie=AK_SCHEMA.curie('V1p4Cell_virtual_pairing'),
                   model_uri=AK_SCHEMA.V1p4Cell_virtual_pairing, domain=None, range=Union[bool, Bool])

slots.V1p4Expression_expression_id = Slot(uri=AK_SCHEMA.V1p4Expression_expression_id, name="V1p4Expression_expression_id", curie=AK_SCHEMA.curie('V1p4Expression_expression_id'),
                   model_uri=AK_SCHEMA.V1p4Expression_expression_id, domain=None, range=str)

slots.V1p4Expression_cell_id = Slot(uri=AK_SCHEMA.V1p4Expression_cell_id, name="V1p4Expression_cell_id", curie=AK_SCHEMA.curie('V1p4Expression_cell_id'),
                   model_uri=AK_SCHEMA.V1p4Expression_cell_id, domain=None, range=str)

slots.V1p4Expression_repertoire_id = Slot(uri=AK_SCHEMA.V1p4Expression_repertoire_id, name="V1p4Expression_repertoire_id", curie=AK_SCHEMA.curie('V1p4Expression_repertoire_id'),
                   model_uri=AK_SCHEMA.V1p4Expression_repertoire_id, domain=None, range=str)

slots.V1p4Expression_data_processing_id = Slot(uri=AK_SCHEMA.V1p4Expression_data_processing_id, name="V1p4Expression_data_processing_id", curie=AK_SCHEMA.curie('V1p4Expression_data_processing_id'),
                   model_uri=AK_SCHEMA.V1p4Expression_data_processing_id, domain=None, range=str)

slots.V1p4Expression_property_type = Slot(uri=AK_SCHEMA.V1p4Expression_property_type, name="V1p4Expression_property_type", curie=AK_SCHEMA.curie('V1p4Expression_property_type'),
                   model_uri=AK_SCHEMA.V1p4Expression_property_type, domain=None, range=str)

slots.V1p4Expression_property = Slot(uri=AK_SCHEMA.V1p4Expression_property, name="V1p4Expression_property", curie=AK_SCHEMA.curie('V1p4Expression_property'),
                   model_uri=AK_SCHEMA.V1p4Expression_property, domain=None, range=Union[str, "V1p4Property"])

slots.V1p4Expression_value = Slot(uri=AK_SCHEMA.V1p4Expression_value, name="V1p4Expression_value", curie=AK_SCHEMA.curie('V1p4Expression_value'),
                   model_uri=AK_SCHEMA.V1p4Expression_value, domain=None, range=float)

slots.V1p4Receptor_receptor_id = Slot(uri=AK_SCHEMA.V1p4Receptor_receptor_id, name="V1p4Receptor_receptor_id", curie=AK_SCHEMA.curie('V1p4Receptor_receptor_id'),
                   model_uri=AK_SCHEMA.V1p4Receptor_receptor_id, domain=None, range=str)

slots.V1p4Receptor_receptor_hash = Slot(uri=AK_SCHEMA.V1p4Receptor_receptor_hash, name="V1p4Receptor_receptor_hash", curie=AK_SCHEMA.curie('V1p4Receptor_receptor_hash'),
                   model_uri=AK_SCHEMA.V1p4Receptor_receptor_hash, domain=None, range=str)

slots.V1p4Receptor_receptor_type = Slot(uri=AK_SCHEMA.V1p4Receptor_receptor_type, name="V1p4Receptor_receptor_type", curie=AK_SCHEMA.curie('V1p4Receptor_receptor_type'),
                   model_uri=AK_SCHEMA.V1p4Receptor_receptor_type, domain=None, range=Union[str, "V1p4ReceptorType"])

slots.V1p4Receptor_receptor_variable_domain_1_aa = Slot(uri=AK_SCHEMA.V1p4Receptor_receptor_variable_domain_1_aa, name="V1p4Receptor_receptor_variable_domain_1_aa", curie=AK_SCHEMA.curie('V1p4Receptor_receptor_variable_domain_1_aa'),
                   model_uri=AK_SCHEMA.V1p4Receptor_receptor_variable_domain_1_aa, domain=None, range=str)

slots.V1p4Receptor_receptor_variable_domain_1_locus = Slot(uri=AK_SCHEMA.V1p4Receptor_receptor_variable_domain_1_locus, name="V1p4Receptor_receptor_variable_domain_1_locus", curie=AK_SCHEMA.curie('V1p4Receptor_receptor_variable_domain_1_locus'),
                   model_uri=AK_SCHEMA.V1p4Receptor_receptor_variable_domain_1_locus, domain=None, range=Union[str, "V1p4ReceptorVariableDomain1Locus"])

slots.V1p4Receptor_receptor_variable_domain_2_aa = Slot(uri=AK_SCHEMA.V1p4Receptor_receptor_variable_domain_2_aa, name="V1p4Receptor_receptor_variable_domain_2_aa", curie=AK_SCHEMA.curie('V1p4Receptor_receptor_variable_domain_2_aa'),
                   model_uri=AK_SCHEMA.V1p4Receptor_receptor_variable_domain_2_aa, domain=None, range=str)

slots.V1p4Receptor_receptor_variable_domain_2_locus = Slot(uri=AK_SCHEMA.V1p4Receptor_receptor_variable_domain_2_locus, name="V1p4Receptor_receptor_variable_domain_2_locus", curie=AK_SCHEMA.curie('V1p4Receptor_receptor_variable_domain_2_locus'),
                   model_uri=AK_SCHEMA.V1p4Receptor_receptor_variable_domain_2_locus, domain=None, range=Union[str, "V1p4ReceptorVariableDomain2Locus"])

slots.V1p4Receptor_receptor_ref = Slot(uri=AK_SCHEMA.V1p4Receptor_receptor_ref, name="V1p4Receptor_receptor_ref", curie=AK_SCHEMA.curie('V1p4Receptor_receptor_ref'),
                   model_uri=AK_SCHEMA.V1p4Receptor_receptor_ref, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4Reactivity_reactivity_id = Slot(uri=AK_SCHEMA.V1p4Reactivity_reactivity_id, name="V1p4Reactivity_reactivity_id", curie=AK_SCHEMA.curie('V1p4Reactivity_reactivity_id'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_reactivity_id, domain=None, range=str)

slots.V1p4Reactivity_cell_id = Slot(uri=AK_SCHEMA.V1p4Reactivity_cell_id, name="V1p4Reactivity_cell_id", curie=AK_SCHEMA.curie('V1p4Reactivity_cell_id'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_cell_id, domain=None, range=str)

slots.V1p4Reactivity_repertoire_id = Slot(uri=AK_SCHEMA.V1p4Reactivity_repertoire_id, name="V1p4Reactivity_repertoire_id", curie=AK_SCHEMA.curie('V1p4Reactivity_repertoire_id'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_repertoire_id, domain=None, range=Optional[str])

slots.V1p4Reactivity_data_processing_id = Slot(uri=AK_SCHEMA.V1p4Reactivity_data_processing_id, name="V1p4Reactivity_data_processing_id", curie=AK_SCHEMA.curie('V1p4Reactivity_data_processing_id'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_data_processing_id, domain=None, range=Optional[str])

slots.V1p4Reactivity_ligand_type = Slot(uri=AK_SCHEMA.V1p4Reactivity_ligand_type, name="V1p4Reactivity_ligand_type", curie=AK_SCHEMA.curie('V1p4Reactivity_ligand_type'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_ligand_type, domain=None, range=Union[str, "V1p4LigandType"])

slots.V1p4Reactivity_antigen_type = Slot(uri=AK_SCHEMA.V1p4Reactivity_antigen_type, name="V1p4Reactivity_antigen_type", curie=AK_SCHEMA.curie('V1p4Reactivity_antigen_type'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_antigen_type, domain=None, range=Union[str, "V1p4AntigenType"])

slots.V1p4Reactivity_antigen = Slot(uri=AK_SCHEMA.V1p4Reactivity_antigen, name="V1p4Reactivity_antigen", curie=AK_SCHEMA.curie('V1p4Reactivity_antigen'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_antigen, domain=None, range=Union[str, "V1p4Antigen"])

slots.V1p4Reactivity_antigen_source_species = Slot(uri=AK_SCHEMA.V1p4Reactivity_antigen_source_species, name="V1p4Reactivity_antigen_source_species", curie=AK_SCHEMA.curie('V1p4Reactivity_antigen_source_species'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_antigen_source_species, domain=None, range=Optional[Union[str, "V1p4AntigenSourceSpecies"]])

slots.V1p4Reactivity_peptide_start = Slot(uri=AK_SCHEMA.V1p4Reactivity_peptide_start, name="V1p4Reactivity_peptide_start", curie=AK_SCHEMA.curie('V1p4Reactivity_peptide_start'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_peptide_start, domain=None, range=Optional[int])

slots.V1p4Reactivity_peptide_end = Slot(uri=AK_SCHEMA.V1p4Reactivity_peptide_end, name="V1p4Reactivity_peptide_end", curie=AK_SCHEMA.curie('V1p4Reactivity_peptide_end'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_peptide_end, domain=None, range=Optional[int])

slots.V1p4Reactivity_peptide_sequence_aa = Slot(uri=AK_SCHEMA.V1p4Reactivity_peptide_sequence_aa, name="V1p4Reactivity_peptide_sequence_aa", curie=AK_SCHEMA.curie('V1p4Reactivity_peptide_sequence_aa'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_peptide_sequence_aa, domain=None, range=Optional[str])

slots.V1p4Reactivity_mhc_class = Slot(uri=AK_SCHEMA.V1p4Reactivity_mhc_class, name="V1p4Reactivity_mhc_class", curie=AK_SCHEMA.curie('V1p4Reactivity_mhc_class'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_mhc_class, domain=None, range=Optional[Union[str, "V1p4MhcClass"]])

slots.V1p4Reactivity_mhc_gene_1 = Slot(uri=AK_SCHEMA.V1p4Reactivity_mhc_gene_1, name="V1p4Reactivity_mhc_gene_1", curie=AK_SCHEMA.curie('V1p4Reactivity_mhc_gene_1'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_mhc_gene_1, domain=None, range=Optional[Union[str, "V1p4MhcGene1"]])

slots.V1p4Reactivity_mhc_allele_1 = Slot(uri=AK_SCHEMA.V1p4Reactivity_mhc_allele_1, name="V1p4Reactivity_mhc_allele_1", curie=AK_SCHEMA.curie('V1p4Reactivity_mhc_allele_1'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_mhc_allele_1, domain=None, range=Optional[str])

slots.V1p4Reactivity_mhc_gene_2 = Slot(uri=AK_SCHEMA.V1p4Reactivity_mhc_gene_2, name="V1p4Reactivity_mhc_gene_2", curie=AK_SCHEMA.curie('V1p4Reactivity_mhc_gene_2'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_mhc_gene_2, domain=None, range=Optional[Union[str, "V1p4MhcGene2"]])

slots.V1p4Reactivity_mhc_allele_2 = Slot(uri=AK_SCHEMA.V1p4Reactivity_mhc_allele_2, name="V1p4Reactivity_mhc_allele_2", curie=AK_SCHEMA.curie('V1p4Reactivity_mhc_allele_2'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_mhc_allele_2, domain=None, range=Optional[str])

slots.V1p4Reactivity_reactivity_method = Slot(uri=AK_SCHEMA.V1p4Reactivity_reactivity_method, name="V1p4Reactivity_reactivity_method", curie=AK_SCHEMA.curie('V1p4Reactivity_reactivity_method'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_reactivity_method, domain=None, range=str)

slots.V1p4Reactivity_reactivity_readout = Slot(uri=AK_SCHEMA.V1p4Reactivity_reactivity_readout, name="V1p4Reactivity_reactivity_readout", curie=AK_SCHEMA.curie('V1p4Reactivity_reactivity_readout'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_reactivity_readout, domain=None, range=str)

slots.V1p4Reactivity_reactivity_value = Slot(uri=AK_SCHEMA.V1p4Reactivity_reactivity_value, name="V1p4Reactivity_reactivity_value", curie=AK_SCHEMA.curie('V1p4Reactivity_reactivity_value'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_reactivity_value, domain=None, range=float)

slots.V1p4Reactivity_reactivity_unit = Slot(uri=AK_SCHEMA.V1p4Reactivity_reactivity_unit, name="V1p4Reactivity_reactivity_unit", curie=AK_SCHEMA.curie('V1p4Reactivity_reactivity_unit'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_reactivity_unit, domain=None, range=str)

slots.V1p4Reactivity_reactivity_ref = Slot(uri=AK_SCHEMA.V1p4Reactivity_reactivity_ref, name="V1p4Reactivity_reactivity_ref", curie=AK_SCHEMA.curie('V1p4Reactivity_reactivity_ref'),
                   model_uri=AK_SCHEMA.V1p4Reactivity_reactivity_ref, domain=None, range=Optional[Union[str, List[str]]])

slots.V1p4SampleProcessing_sample_processing_id = Slot(uri=AK_SCHEMA.V1p4SampleProcessing_sample_processing_id, name="V1p4SampleProcessing_sample_processing_id", curie=AK_SCHEMA.curie('V1p4SampleProcessing_sample_processing_id'),
                   model_uri=AK_SCHEMA.V1p4SampleProcessing_sample_processing_id, domain=None, range=Optional[str])

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