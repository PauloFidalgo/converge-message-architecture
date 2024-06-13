from dataclasses import dataclass

@dataclass
class GnbRadioSensing:
    periodicity: int
    iq_samples: float

@dataclass
class GnbPlacement:
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
    ssb_arfcn: int
    point_a_arfcn: int

@dataclass
class RU:
    band_configuration: BandConfiguration
    bandwidth_mhz: int
    tdd_configuration: str
    logical_ant_rx: int
    logical_ant_tx: int

@dataclass
class ORU:
    seven_two: 'SevenTwo'
    ru: RU

@dataclass
class ODU:
    f1: F1
    seven_two: 'SevenTwo'
    ru: RU

@dataclass
class OCU:
    cn: 'CN'
    f1: F1

@dataclass
class GnbConfiguration:
    o_cu: OCU
    o_du: ODU
    o_ru: ORU
    cg_nb_placement: GnbPlacement
    cg_nb_radio_sensing: GnbRadioSensing
