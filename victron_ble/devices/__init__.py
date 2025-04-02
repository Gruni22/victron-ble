import struct
from typing import Dict, Optional, Type

from victron_ble.devices.base import Device, DeviceData
from victron_ble.devices.battery_monitor import (
    AuxMode,
    BatteryMonitor,
    BatteryMonitorData,
)
from victron_ble.devices.battery_sense import BatterySense, BatterySenseData
from victron_ble.devices.dc_energy_meter import DcEnergyMeter, DcEnergyMeterData
from victron_ble.devices.dcdc_converter import DcDcConverter, DcDcConverterData
from victron_ble.devices.inverter import Inverter, InverterData
from victron_ble.devices.lynx_smart_bms import LynxSmartBMS, LynxSmartBMSData
from victron_ble.devices.orion_xs import OrionXS, OrionXSData
from victron_ble.devices.smart_battery_protect import (
    SmartBatteryProtect,
    SmartBatteryProtectData,
)
from victron_ble.devices.smart_lithium import SmartLithium, SmartLithiumData
from victron_ble.devices.solar_charger import SolarCharger, SolarChargerData
from victron_ble.devices.smart_charger import SmartCharger, SmartChargerData
from victron_ble.devices.vebus import VEBus, VEBusData

__all__ = [
    "AuxMode",
    "Device",
    "DeviceData",
    "BatteryMonitor",
    "BatteryMonitorData",
    "BatterySense",
    "BatterySenseData",
    "DcDcConverter",
    "DcDcConverterData",
    "DcEnergyMeter",
    "DcEnergyMeterData",
    "Inverter",
    "InverterData",
    "OrionXS",
    "OrionXSData",
    "SmartBatteryProtect",
    "SmartBatteryProtectData",
    "SmartLithium",
    "SmartLithiumData",
    "SmartBatteryProtect",
    "SmartBatteryProtectData",
    "LynxSmartBMS",
    "LynxSmartBMSData",
    "SolarCharger",
    "SolarChargerData",
    "SmartCharger",
    "SmartChargerData",
    "VEBus",
    "VEBusData",
]

# Add to this list if a device should be forced to use a particular implementation
# instead of relying on the identifier in the advertisement
MODEL_PARSER_OVERRIDE: Dict[int, Type[Device]] = {
    0xA3A4: BatterySense,  # Smart Battery Sense
    0xA3A5: BatterySense,  # Smart Battery Sense
    0xA300: SmartCharger,  # Blue Smart Charger - Generic
    0xA301: SmartCharger,  # Blue Smart IP65 Charger 12|10
    0xA302: SmartCharger,  # Blue Smart IP65 Charger 12|15
    0xA303: SmartCharger,  # Blue Smart IP65 Charger 24|8
    0xA304: SmartCharger,  # Blue Smart IP65 Charger 12|5
    0xA305: SmartCharger,  # Blue Smart IP65 Charger 12|7
    0xA306: SmartCharger,  # Blue Smart IP65 Charger 24|5
    0xA307: SmartCharger,  # Blue Smart IP65 Charger 12|4
    0xA308: SmartCharger,  # Blue Smart IP65s Charger 12|4
    0xA309: SmartCharger,  # Blue Smart IP65s Charger 12|5
    0xA30A: SmartCharger,  # Blue Smart IP65 Charger 12|25
    0xA30B: SmartCharger,  # Blue Smart IP65 Charger 24|13
    0xA30C: SmartCharger,  # Blue Smart IP65 Charger 6V/12V-1.1A
    0xA30D: SmartCharger,  # Blue Smart IP65s Charger 12/4
    0xA30E: SmartCharger,  # Blue Smart IP65s Charger 12/5
    0xA30F: SmartCharger,  # Blue Smart IP65 Charger 12/7
    0xA310: SmartCharger,  # Blue Smart IP67 Charger 12|7
    0xA311: SmartCharger,  # Blue Smart IP67 Charger 12|13
    0xA312: SmartCharger,  # Blue Smart IP67 Charger 24|5
    0xA313: SmartCharger,  # Blue Smart IP67 Charger 12|17
    0xA314: SmartCharger,  # Blue Smart IP67 Charger 12|25
    0xA315: SmartCharger,  # Blue Smart IP67 Charger 24|8
    0xA316: SmartCharger,  # Blue Smart IP67 Charger 24|12
    0xA317: SmartCharger,  # Blue Smart IP67 Charger 12/7
    0xA318: SmartCharger,  # Blue Smart IP67 Charger 12/13
    0xA319: SmartCharger,  # Blue Smart IP67 Charger 24/5
    0xA31A: SmartCharger,  # Blue Smart IP67 Charger 12/17
    0xA31B: SmartCharger,  # Blue Smart IP67 Charger 12/25
    0xA31C: SmartCharger,  # Blue Smart IP67 Charger 24/8
    0xA31D: SmartCharger,  # Blue Smart IP67 Charger 24/12
    0xA320: SmartCharger,  # Blue Smart IP22 Charger 12|15 (1)
    0xA321: SmartCharger,  # Blue Smart IP22 Charger 12|15 (3)
    0xA322: SmartCharger,  # Blue Smart IP22 Charger 12|20 (1)
    0xA323: SmartCharger,  # Blue Smart IP22 Charger 12|20 (3)
    0xA324: SmartCharger,  # Blue Smart IP22 Charger 12|30 (1)
    0xA325: SmartCharger,  # Blue Smart IP22 Charger 12|30 (3)
    0xA326: SmartCharger,  # Blue Smart IP22 Charger 24|8 (1)
    0xA327: SmartCharger,  # Blue Smart IP22 Charger 24|8 (3)
    0xA328: SmartCharger,  # Blue Smart IP22 Charger 24|12 (1)
    0xA329: SmartCharger,  # Blue Smart IP22 Charger 24|12 (3)
    0xA32A: SmartCharger,  # Blue Smart IP22 Charger 24|16 (1)
    0xA32B: SmartCharger,  # Blue Smart IP22 Charger 24|16 (3)
    0xA32C: SmartCharger,  # Blue Smart IP22 Charger 12/15 (1)
    0xA32D: SmartCharger,  # Blue Smart IP22 Charger 12/15 (3)
    0xA32E: SmartCharger,  # Blue Smart IP22 Charger 12/20 (1)
    0xA32F: SmartCharger,  # Blue Smart IP22 Charger 12/20 (3)
    0xA330: SmartCharger,  # Blue Smart IP22 Charger 12/30 (1)
    0xA331: SmartCharger,  # Blue Smart IP22 Charger 12/30 (3)
    0xA332: SmartCharger,  # Blue Smart IP22 Charger 24/8 (1)
    0xA333: SmartCharger,  # Blue Smart IP22 Charger 24/8 (3)
    0xA334: SmartCharger,  # Blue Smart IP22 Charger 24/12 (1)
    0xA335: SmartCharger,  # Blue Smart IP22 Charger 24/12 (3)
    0xA336: SmartCharger,  # Blue Smart IP22 Charger 24/16 (1)
    0xA337: SmartCharger,  # Blue Smart IP22 Charger 24/16 (3)
    0xA338: SmartCharger,  # Blue Smart IP65 Charger 12/10
    0xA339: SmartCharger,  # Blue Smart IP65 Charger 12/15
    0xA33A: SmartCharger,  # Blue Smart IP65 Charger 24/5
    0xA33B: SmartCharger,  # Blue Smart IP65 Charger 24/8
    0xA33C: SmartCharger,  # Blue Smart IP65 Charger 12/5
}


def detect_device_type(data: bytes) -> Optional[Type[Device]]:
    try:
        model_id = struct.unpack("<H", data[2:4])[0]
        mode = struct.unpack("<B", data[4:5])[0]
    except IndexError:
        return None

    # Model ID-based preferences
    match = MODEL_PARSER_OVERRIDE.get(model_id)
    if match:
        return match

    # Defaults
    if mode == 0x2:  # BatteryMonitor
        return BatteryMonitor
    elif mode == 0xD:  # DcEnergyMeter
        return DcEnergyMeter
    elif mode == 0x8:  # AcCharger
        pass
    elif mode == 0x4:  # DcDcConverter
        return DcDcConverter
    elif mode == 0x3:  # Inverter
        return Inverter
    elif mode == 0x6:  # InverterRS
        pass
    elif mode == 0xA:  # LynxSmartBMS
        return LynxSmartBMS
    elif mode == 0xB:  # MultiRS
        pass
    elif (
        mode == 0x5
    ):  # SmartLithium (commercially Lithium Battery Smart / LiFePO4 Battery Smart)
        return SmartLithium
    elif mode == 0x9:  # SmartBatteryProtect
        return SmartBatteryProtect
    elif mode == 0x1:  # SolarCharger
        return SolarCharger
    elif mode == 0xC:  # VE.Bus
        return VEBus
    elif mode == 0xF:  # Orion XS
        return OrionXS

    return None
