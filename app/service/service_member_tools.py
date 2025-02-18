from app.repository.member_tools_repository import MemberToolsRepository

class ServiceMemberTools:
    def __init__(self):
        self.member_tolls_repository = MemberToolsRepository()


    def create_data_scammer(self, data):
        response = self.member_tolls_repository.create(data)
        return response