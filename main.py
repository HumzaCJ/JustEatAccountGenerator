import requests
import tls_client
session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
from faker import Faker

fake = Faker()

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json;v=2',
    'origin': 'https://www.just-eat.co.uk',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.just-eat.co.uk/',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'x-jet-application': 'OneWeb',
}

json_data = {
    'registrationSource': 'native',
    'fullName': fake.name(),
    'password': f"{fake.password(length=16, special_chars=True, digits=True, upper_case=True, lower_case=True)}_",
    'emailAddress': fake.email(),
}

response = session.post(
    'https://uk.api.just-eat.io/consumers/uk', headers=headers, json=json_data)

print(response.status_code)
print(f"Login Email: {json_data['emailAddress']}")
print(f"Login Password: {json_data['password']}")
print(f"Login Full Name: {json_data['fullName']}")
print(f"\n")
print(f"Notice: Status code 201 means successful, anything else you can assume it's an error")
