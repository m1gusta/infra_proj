import os

from fastapi import FastAPI


app = FastAPI(
    title="Mini Infrastructure App",
    version="1.0.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "message": "Hello from Mini Infrastructure App"
    }


@app.get("/health")
async def health() -> dict[str, str]:
    return {
        "status": "ok"
    }


@app.get("/info")
async def info() -> dict[str, str]:
    return {
        "application": "mini-infra-template",
        "version": "1.0.0",
        "hostname": os.getenv("HOSTNAME", "unknown"),
    }