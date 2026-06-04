from .mapper.registry_mapper_ir12_04_10 import REGISTRY_MAPPER as ir12_04_10
from .mapper.registry_mapper_ir14_1_0_10_0 import REGISTRY_MAPPER as ir14_1_0_10_0
from .mapper.registry_mapper_ir14_1_0_5_0 import REGISTRY_MAPPER as ir14_1_0_5_0
from .mapper.registry_mapper_ir14_1_0_11_0 import REGISTRY_MAPPER as ir14_1_0_11_0

DOMAIN = "regulus"
NAME = "Regulus Heat Pump"
COMPANY = "Regulus"
IR_VERSION_OPTIONS = ["12_04_10", "14_1_0_5_0", "14_1_0_10_0", "14_1_0_11_0"]
POLLING_INTERVAL = 5
REGISTRY_MAPPERS = {
    "12_04_10": ir12_04_10,
    "14_1_0_5_0": ir14_1_0_5_0,
    "14_1_0_10_0": ir14_1_0_10_0,
    "14_1_0_11_0": ir14_1_0_11_0,
}
