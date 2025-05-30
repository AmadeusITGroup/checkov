from dataclasses import dataclass
from enum import Enum
from typing import List, Any


@dataclass
class CustomAttributes:
    BLOCK_NAME = "block_name_"
    BLOCK_TYPE = "block_type_"
    FILE_PATH = "file_path_"
    CONFIG = "config_"
    ATTRIBUTES = "attributes_"
    LABEL = "label_"
    ID = "id_"
    HASH = "hash"
    RENDERING_BREADCRUMBS = "rendering_breadcrumbs_"
    SOURCE = "source_"
    RESOURCE_TYPE = "resource_type"
    RESOURCE_ID = "resource_id"
    SOURCE_MODULE = "source_module_"
    MODULE_DEPENDENCY = "module_dependency_"
    MODULE_DEPENDENCY_NUM = "module_dependency_num_"
    ENCRYPTION = "encryption_"
    ENCRYPTION_DETAILS = "encryption_details_"
    TF_RESOURCE_ADDRESS = "__address__"
    PROVIDER_ADDRESS = "__provider_address__"
    REFERENCES = "references_"
    FOREACH_ATTRS = "foreach_attrs_"
    SOURCE_MODULE_OBJECT = "source_module_object_"
    CONNECTED_NODE = "connected_node"
    VIRTUAL_RESOURCES = "virtual_resources"


def props(cls: Any) -> List[str]:
    return [i for i in cls.__dict__.keys() if i[:1] != "_"]


def wrap_reserved_attributes(attribute: str, prefix: str = '_') -> str:
    return f"{prefix}{attribute}"


reserved_attribute_names = props(CustomAttributes)
reserved_attributes_to_scan = [CustomAttributes.RESOURCE_TYPE]


class EncryptionValues(str, Enum):
    ENCRYPTED = "ENCRYPTED"
    UNENCRYPTED = "UNENCRYPTED"


class EncryptionTypes(str, Enum):
    KMS_VALUE = "KMS"
    NODE_TO_NODE = "node-to-node"
    DEFAULT_KMS = "Default KMS"
    AES256 = "AES256"
    AWS_KMS_VALUE = "aws:kms"
