import requests
import webbrowser
from bs4 import BeautifulSoup

cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = '\033[1;33;40m'

def Nameinfo():
    try:
        name = input("Enter the Full Name  >> ")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Search Google for the name
        url = "https://www.google.com/search?q=" + name
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        socialmedia = ["instagram", "facebook", "twitter", "linkedin", "github", "scholar", "hackerearth", "hackerrank", "hackerone", "tiktok", "youtube", "books", "researchgate", "publons", "orcid", "maps"]
        linklist = []

        # Extract links from Google search results
        for g in soup.find_all('div', class_='g'):
            anchors = g.find_all('a')
            if anchors and 'href' in anchors[0]:
                linklist.append(anchors[0]['href'])

        foundedlinks = []
        for i in socialmedia:
            sm = str(i)
            for j in linklist:
                if sm in j:
                    foundedlinks.append(j)
                    print(cyan + "[+]" + j)

        if not foundedlinks:
            print(red + "No social media links found.")
        else:
            # Open the found social media links
            for link in foundedlinks:
                webbrowser.open(link)

        # Search for PDF documents related to the name
        print(red + "[-] Checking for any pdf documents associated with this name ...")
        pdf_url = "https://www.google.com/search?q=%22" + name + "%22+filetype%3Apdf&oq=%22" + name + "%22+filetype%3Apdf"
        pdf_response = requests.get(pdf_url, headers=headers)
        pdf_soup = BeautifulSoup(pdf_response.content, 'html.parser')

        # Extract PDF links from Google search results
        pdf_links = pdf_soup.find_all('div', class_='g')
        if not pdf_links:
            print(red + "No PDF documents found.")
        else:
            for pdf_link in pdf_links:
                if 'href' in pdf_link.a:
                    print(green + "[+]" + pdf_link.a['href'])
    except requests.RequestException as e:
        print(red + "Error fetching data:", e)
    except Exception as ex:
        print(red + "An error occurred:", ex)

if __name__ == "__main__":
    Nameinfo()
