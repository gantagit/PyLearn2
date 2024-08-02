import ssl
import certifi
import os
import requests

print("Certificate path:", certifi.where())

try:
    ssl.create_default_context(cafile=certifi.where())
    print("SSL certificates are set up correctly.")
except Exception as e:
    print("SSL setup error:", e)

os.environ['SSL_CERT_FILE'] = 'C:/Users/gvk97/PycharmProjects/PyLearn2/.venv/Lib/site-packages/certifi/cacert.pem'

response = requests.get('https://restful-booker.herokuapp.com/booking')
print(response.status_code)
