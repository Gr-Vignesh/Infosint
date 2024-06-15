import requests
from bs4 import BeautifulSoup

R = '\033[1;31;40m' 
G = '\033[1;32;40m'
C = '\033[1;36;40m'
Y = '\033[1;33;40m'

def Links():
    print(Y + "Note : http://example.com")
    url = input("Enter the URL (http:// >> ")
    print('')
    print(G + "[+] Fetching links.....")
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            lin = link.get('href')
            if lin and lin.startswith('http'):
                print(C + "[+] ", lin)
        print(G + "Fetched Successfully...")
    except requests.RequestException as e:
        print(R + "Error fetching the URL:", e)
    
if __name__ == "__main__":
    Links()
