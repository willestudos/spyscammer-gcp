import json

from app.schemas.member_tools_schema import InfoDataSchema, IPData


def scammer_adjust_payload(data):

    data_scammer = InfoDataSchema(
        id_member="willch3",
        selfie=data.get("selfie"),
        ip_data=IPData(
            ip=data.get("ip_data")["ip"],
            city = data.get("ip_data")["city"],
            region_code = data.get("ip_data")["region_code"],
            postal = data.get("ip_data")["postal"],
            latitude = str(data.get("ip_data")["latitude"]),
            longitude = str(data.get("ip_data")["longitude"]),
            org = data.get("ip_data")["org"],
        ),
        location=f"https://www.google.com/maps/place/{data.get('latitude')}+{data.get('longitude')}",
    )
    return data_scammer.dict()