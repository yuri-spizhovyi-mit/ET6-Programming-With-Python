import requests

# Proxy to test (Replace with your proxy IP and port)
proxy = "41.65.163.82:1976"

# Set up proxies dictionary
proxies = {
    "http": f"http://{proxy}",
    "https": f"http://{proxy}",  # Some proxies only support HTTP
}

# Website to test (should return the external IP)
test_url = "http://ifconfig.me"

try:
    response = requests.get(test_url, proxies=proxies, timeout=10)

    if response.status_code == 200:
        print(f"✅ Proxy is working! Your IP: {response.text.strip()}")
    else:
        print(f"⚠️ Proxy responded with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"❌ Proxy failed: {e}")
