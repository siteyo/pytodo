import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

TEST_DIR: str = os.environ["TEST_DIR"]
TEST_FILENAME: str = os.environ["TEST_FILENAME"]
