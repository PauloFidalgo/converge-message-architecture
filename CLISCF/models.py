from dataclasses import dataclass
from typing import List

@dataclass
class RadioSensingConfiguration:
    time_step: float
    sensing_custom_phase_profile: List[float]

@dataclass
class PreConfiguredBeam:
    source_angle: List[float]
    destination_angle: List[float]
    beam_width: int

@dataclass
class RadioCommunicationsConfiguration:
    pre_configured_beam: PreConfiguredBeam
    custom_phase_profile: List[float]