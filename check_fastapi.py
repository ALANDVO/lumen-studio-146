#!/usr/bin/env python3
from fastapi.testclient import TestClient
from main import app

def main():
    client = TestClient(app)

    # health check
    resp = client.get("/health")
    assert resp.status_code == 200, f"Health check failed: {resp.status_code}"
    data = resp.json()
    assert data == {"status": "ok"}, f"Unexpected health response: {data}"
    print("Health check passed")

    # root endpoint
    resp2 = client.get("/")
    assert resp2.status_code == 200, f"Root endpoint failed: {resp2.status_code}"
    data2 = resp2.json()
    assert "message" in data2, f"Unexpected root response: {data2}"
    print("Root endpoint passed")

    print("All FastAPI checks passed")

    return True

if __name__ == "__main__":
    main()
