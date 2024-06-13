from dataclasses import dataclass

@dataclass
class RadioSensingConfiguration:
    time_step: float
    sensing_custom_phase_profile: list

@dataclass
class PreConfiguredBeam:
    source_angle: list
    destination_angle: list
    beam_width: int

@dataclass
class RadioCommunicationsConfiguration:
    pre_configures_beam: PreConfiguredBeam
    custom_phase_profile: list
