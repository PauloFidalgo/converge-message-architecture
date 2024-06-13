from dataclasses import dataclass

@dataclass
class gnbRadioSensing:
    periodicity: int
    iq_samples: float

@dataclass
class gnbPlacement:
    x: int
    y: int
    z: int

@dataclass
class F1:
    remote_ip: str
    remote_port: int
    local_ip: str
    local_port: int

@dataclass
class BandConfiguration:
    band: int
    ssbArfcn: int
    pointAArfcn: int


@dataclass
class RU:
    bandConfiguration: BandConfiguration
    bandwidthMHz: int
    tddConfiguration: str
    logicalAntRx: int
    logicalAntTx: int

@dataclass
class O_RU:
    7_2: 7_2
    RU: RU

@dataclass
class O_DU:
    F1: F1
    7_2: 7_2
    RU: RU

@dataclass
class O_CU:
    CN: CN
    F1: F1

@dataclass
class gnbConfiguration:
    O_CU: O_CU
    O_DU: O_DU
    O_RU: O_RU
    CgNB_placement: gnbPlacement
    CgNB_radio_sensing: gnbRadioSensing


