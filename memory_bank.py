"""Create a Memory Bank in Google Vertex AI."""

import os

from dotenv import load_dotenv
from vertexai import Client

load_dotenv()

client = Client(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location="us-central1",
)

agent_engine = client.agent_engines.create()
print(agent_engine)
