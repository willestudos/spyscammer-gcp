from loguru import logger

from app.models.model import MembersAccount
from app.repository.base import BaseRepository


logger.remove()
logger.add(sink=lambda msg: print(msg, end=""), format="{time:YYYY-MM-DD HH:mm:ss} {level} {message}")

class MembersRepository(BaseRepository):
    def __init__(self):
        super().__init__(MembersAccount)

    def create(self, body):
        email = body['email']
        member_exist = self.get_member(email)

        if member_exist is not None:
            logger.error(f'| Existe um cadastro com este e-mail -- {body["email"]}')
            return f"Existe um membro cadastrado com este e-mail!"
        logger.info(f'| E-mail cadastrado com sucesso -- {body["email"]}')
        return self.collection(**body).save()

    def get_member(self, email):
        documents = self.collection.objects(email=email).first()

        if documents is not None:
            return documents.to_mongo().to_dict()
        return documents

    def session_member(self, email, password):
        session = self.collection.objects(email=email[0], password=password).first()

        if session is not None:
            return session.to_mongo().to_dict()
        return session
