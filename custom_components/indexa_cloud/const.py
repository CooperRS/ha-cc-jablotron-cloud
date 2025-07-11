"""Constants for the Jablotron Cloud integration."""

from enum import StrEnum

DOMAIN = "indexa_cloud"

SERVICE_ID = "service-id"
SERVICE_TYPE = "service-type"

COMP_ID = "cloud-component-id"
DEVICE_ID = "object-device-id"
PG_STATE = "state"
PG_STATE_OFF = "OFF"

SERVICES_WITHOUT_PG = ["FUTURA2", "AMBIENTA", "VOLTA", "LOGBOOK"]

class Actions(StrEnum):
    """Actions to control sections."""

    ARM = "ARM"
    DISARM = "DISARM"
    PARTIAL_ARM = "PARTIAL_ARM"
