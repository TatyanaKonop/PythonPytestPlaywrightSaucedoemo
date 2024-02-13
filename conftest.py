from dotenv import load_dotenv


load_dotenv() # credentials like token, login, password download from .env or secrets
# show route fixtures
pytest_plugins = [
    'fixtures.page',
    'fixtures.user_auth'
]