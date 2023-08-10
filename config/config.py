import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

AUTOTEST_REF_KEY = os.environ.get("AUTOTEST_KEY")
HEADLESS_MODE = os.environ.get("HEADLESS_MODE")
RUN_BROWSER = os.environ.get("BROWSER")
