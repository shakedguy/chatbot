from dotenv import load_dotenv
from os import environ

load_dotenv()


OPEN_AI_API_KEY = environ.get('OPEN_AI_API_KEY')
OPEN_AI_ORGANIZATION = environ.get('OPEN_AI_ORGANIZATION')
