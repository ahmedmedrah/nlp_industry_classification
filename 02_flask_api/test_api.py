import requests

url = 'http://localhost:5000/predict'
r = requests.post(url,json={"job_title":"accountant"})

print(r.json())