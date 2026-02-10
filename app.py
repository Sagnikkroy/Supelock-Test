from fastapi import FastAPI, Request
from supelock_middleware.middleware import SupelockMiddleware

app = FastAPI()
app.add_middleware(SupelockMiddleware)


@app.post("/orders")
async def create_order(request: Request):
    return {
        "trust_level": request.state.supelock_trust,
        "payload": request.state.supelock_payload
    }
