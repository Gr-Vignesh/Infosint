import requests

cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = '\033[1;33;40m'

def check_sql_injection(url):
    # List of SQL injection payloads to test
    payloads = ["'", "\"", "1=1", "1'or'1'='1", "1'or 1=1--", "' or 1=1--", "') or ('1'='1--"]
    
    for payload in payloads:
        # Construct the request with the payload
        data = {"param": payload}
        response = requests.get(url, params=data)
        # Check if the response contains any indications of SQL injection vulnerability
        if "error" in response.text.lower() or "exception" in response.text.lower():
            print(f"Potential SQL Injection Vulnerability Found with Payload: {payload}")
            return
    
    print("No SQL Injection Vulnerabilities Found.")

if __name__ == "__main__":
    website_url = input("Enter the URL to test for SQL injection: ")
    check_sql_injection(website_url)
