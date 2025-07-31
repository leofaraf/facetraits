from dataclasses import dataclass
from enum import Enum

@dataclass
class Symmetry:
    # Based on comparing distance of diff. parts of body
    score: float

class ChinType(Enum):
    RECTANGULAR = "Rectangular"
    POINTED = "Pointed"
    ROUNDED = "Rounded"
    RECESSED = "Recessed"
    PROTRUDING = "Protruding"
    UNKNOWN = "Unknown"

@dataclass
class Chin:
    chin_width_to_face_width_ratio: float
    chin_type: ChinType

@dataclass
class Jawline:
    jawline_to_face_width_ratio: float

@dataclass
class Forehead:
    face_height_ratio: float