import os
import pathlib

from dotenv import load_dotenv

curr_dir = pathlib.Path(__file__).parent.resolve()
load_dotenv(dotenv_path=curr_dir.parent / ".env")

print(os.getenv("DB_USER"))
