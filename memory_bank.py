from vertexai import Client

client = Client(
    project="secure-site-476315-p9",
    location="us-central1",
)

agent_engine = client.agent_engines.create()
print(agent_engine)
