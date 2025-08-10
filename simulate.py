import time, random, requests

url = "http://localhost:8000/api/data"
for i in range(10):
    data = {
        "timestamp": time.time(),
        "temperature": 20 + random.random()*5,
        "pressure": 1 + random.random()*0.1,
        "current": 0.5 + random.random()*0.2
    }
    res = requests.post(url, json=data)
    print(res.json())
    time.sleep(1)
