import os
from dotenv import load_dotenv


def load_env():
    from dotenv import load_dotenv
    load_dotenv()
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
