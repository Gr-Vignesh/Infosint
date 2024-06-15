from clickjack import ClickJacking
from hostheader import HostHeader
from subdomain import fuzz
from reverseip import ReverseIP
from sqlinjection import check_sql_injection

cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = '\033[1;33;40m'

def Webvuln():
    while True:
        inp = input("Vulnerability >> ")
        if inp == '1':
            ClickJacking()
        elif inp == '2':
            HostHeader()
        elif inp == '3':
            fuzz()
        elif inp == '4':
            ReverseIP()
        elif inp == '5':
            website_url = input("Enter the URL to test for SQL injection: ")
            check_sql_injection(website_url)
        elif inp == 'help':
            print(green + """
                   1. ClickJacking,
                   2. Host header injection,
                   3. Subdomain Enumeration,
                   4. Reverse IP,
                   5. SQL injection
                   """)
        else:
            print(red + "Invalid choice")

def check_sql_injection(url):
    # Add SQL injection vulnerability checking code here
    # This function should test the target URL for SQL injection vulnerabilities
    print(green + "Checking for SQL Injection vulnerabilities...")

if __name__ == "__main__":
    Webvuln()
