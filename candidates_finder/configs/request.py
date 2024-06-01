from dotenv import load_dotenv
from os import getenv

load_dotenv()

COLUMNS_LIST: list = [
    "name",
    "company",
    "blog",
    "email",
    "bio",
    "public_repos",
    "followers",
    "following",
    "created_at"
]
PROFILE_KEY: str = 'url'
FOLLOWERS_URL: str = 'https://api.github.com/users/calilisantos/followers'
TOKEN: str = getenv("GITHUB_PAT")
HEADERS: dict = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"Bearer {TOKEN}"
}
