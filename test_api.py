import subprocess
import time
import requests
import pytest
import sys

BASE = "http://127.0.0.1:8000"

@pytest.fixture(scope="session", autouse=True)
def start_server():
    # Start the Flask app
    proc = subprocess.Popen([sys.executable, "app.py"])
    time.sleep(2)  # wait 2 seconds for server to start

    # Check if server is running
    try:
        r = requests.get(f"{BASE}/status")
        assert r.status_code == 200
    except:
        proc.kill()
        raise RuntimeError("Server did not start")

    yield  # run the tests

    # After tests, stop server
    proc.terminate()
    try:
        proc.wait(timeout=2)
    except:
        proc.kill()

def test_status():
    r = requests.get(f"{BASE}/status")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_sum():
    r = requests.get(f"{BASE}/sum?a=2&b=3")
    assert r.status_code == 200
    assert r.json()["sum"] == 5
