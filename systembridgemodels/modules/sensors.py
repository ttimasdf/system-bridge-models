"""System."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class SensorsWindowsSensor:
    """Sensors Windows Sensor."""

    id: str
    name: str
    type: str
    value: float | int | str | None = None


@dataclass
class SensorsWindowsHardware:
    """Sensors Windows Hardware."""

    id: str
    name: str
    type: str
    subhardware: list[SensorsWindowsHardware]
    sensors: list[SensorsWindowsSensor]

@dataclass
class SensorsNVIDIAChipset:
    id: int
    name: str
    flags: str
    vendor_id: int
    vendor_name: str


@dataclass
class SensorsNVIDIADisplay:
    id: int
    name: str
    active: bool
    available: bool
    connected: bool
    dynamic: bool
    aspect_horizontal: int
    aspect_vertical: int
    brightness_current: int
    brightness_default: int
    brightness_max: int
    brightness_min: int
    color_depth: str
    connection_type: str
    pixel_clock: int
    refresh_rate: int
    resolution_horizontal: int
    resolution_vertical: int


@dataclass
class SensorsNVIDIADriver:
    branch_version: str
    interface_version: str
    version: int


@dataclass
class SensorsNVIDIAGPUs:
    id: int
    name: str
    bios_oem_revision: int | None = None
    bios_revision: int | None = None
    bios_version: str | None = None
    current_fan_speed_level: int | None = None
    current_fan_speed_rpm: int | None = None
    driver_model: int | None = None
    memory_available: int | None = None
    memory_capacity: int | None = None
    memory_maker: str | None = None
    serial: str | None = None
    system_type: str | None = None
    type: str | None = None


@dataclass
class SensorsNVIDIA:
    chipset: SensorsNVIDIAChipset
    displays: list[SensorsNVIDIADisplay]
    driver: SensorsNVIDIADriver
    gpus: list[SensorsNVIDIAGPUs]

@dataclass
class SensorsWindows:
    """Sensors Windows."""

    hardware: list[SensorsWindowsHardware] | None = None
    nvidia: SensorsNVIDIA | None = None


@dataclass
class Sensors:
    """Sensors."""

    # TODO: Add fan model
    fans: Any | None = None
    # TODO: Add temperatures model
    temperatures: Any | None = None
    windows_sensors: SensorsWindows | None = None
