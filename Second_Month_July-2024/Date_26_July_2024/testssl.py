import ssl
import certifi

print("Certificate path:", certifi.where())

try:
    ssl.create_default_context(cafile=certifi.where())
    print("SSL certificates are set up correctly.")
except Exception as e:
    print("SSL setup error:", e)