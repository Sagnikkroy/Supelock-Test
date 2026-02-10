from supelock import Actor

actor = Actor("didle-agent")

response = actor.request(
    method="POST",
    url="http://127.0.0.1:8000/orders",
    intent={"action": "create_order"},
    json={"amount": 100}
)

print(response.json())
