import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

AUTOTEST_REF_KEY = os.environ.get("AUTOTEST_KEY")
RUN_BROWSER = os.environ.get("RUN_BROWSER")
