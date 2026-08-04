import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://httpbin.org"

response = requests.get(
    f"{BASE_URL}/basic-auth/student/pass123",
    auth=HTTPBasicAuth("student", "pass123"),
)

print(response.status_code)
print(response.json())


