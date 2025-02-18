from fastapi_login import LoginManager

SECRET = "#6)#++1b6g1*ae47&+pk@3u!@$usmo-@87tqygsr1e#@+_-#*b"

manager = LoginManager(SECRET, token_url="auth/token")

@manager.user_loader
def get_user(username: str):
    user