from app.models.model import DataScammer
from app.repository.base import BaseRepository
from app.schemas.member_tools_schema import InfoDataSchema


class MemberToolsRepository(BaseRepository):

    def __init__(self):
        super().__init__(DataScammer)

    def create(self, body):
        if not isinstance(body, dict):
            body = body.to_mongo().to_dict()
        response = self.collection(**body).save()
        return response
