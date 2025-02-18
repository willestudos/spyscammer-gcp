from typing import Optional

from pydantic import BaseModel


class IPData(BaseModel):
    ip: Optional[str]
    city: Optional[str]
    region_code: Optional[str]
    postal: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    org: Optional[str]

class InfoDataSchema(BaseModel):
    id_member: Optional[str]
    # latitude: Optional[float]
    # longitude: Optional[float]
    selfie: Optional[str]
    ip_data: Optional[IPData]
    location: Optional[str]