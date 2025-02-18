from pydantic import BaseModel


class MemberSchema(BaseModel):
    name: str
    username: str
    email: str
    password: str


class User(BaseModel):
    username: str


class LoginForm(BaseModel):
    email: str
    password: str
