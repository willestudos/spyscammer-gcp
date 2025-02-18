from app.repository.members_repository import MembersRepository


class ServiceMember:
    def __init__(self):
        self.member_repository = MembersRepository()

    def create_member(self, data):

        response = self.member_repository.create(data)
        if response == "Existe um membro cadastrado com este e-mail!":
            return f"{response}"
        respose = f"Cadastro criado com sucesso"

        return respose

    def get_auth_member(self, email, password):
        response = self.member_repository.session_member(email=email, password=password)
        return response
