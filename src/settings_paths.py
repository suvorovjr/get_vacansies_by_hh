import os
from pathlib import Path

path = Path(__file__).parent
AREAS_HH = Path.joinpath(path, "areas_hh.json")
AREAS_SUPERJOB = Path.joinpath(path, "areas_super_job.json")
VACANSIES_JSON = Path.joinpath(path, "vacancies.json")
API_KEY_SUPERJOB = os.environ.get("API_SUPERJOB")
