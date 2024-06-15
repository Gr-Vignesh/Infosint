from halo import Halo
import requests
from bs4 import BeautifulSoup
import re

spinner = Halo(text=' Scanning', spinner='dots')
cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = '\033[1;33;40m'
G = green

def recon():
    image = input(cyan + "Enter the image path >> ")
    try:
        spinner.start()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        url = 'https://www.google.com/searchbyimage/upload'
        with open(image, 'rb') as img:
            secondurl = {'encoded_image': (image, img), 'image_content': ''}
            response = requests.post(url, files=secondurl, allow_redirects=False)
        
        # Debug: Print response status and headers
        print(f"POST response status: {response.status_code}")
        print(f"POST response headers: {response.headers}")

        fetch = response.headers.get('Location')

        if not fetch:
            print(red + "Failed to get redirect URL from Google.")
            spinner.stop()
            return

        req = requests.get(fetch, headers=headers)

        # Debug: Print GET response status and headers
        print(f"GET response status: {req.status_code}")
        print(f"GET response headers: {req.headers}")

        socialmedia = ["instagram", "facebook", "twitter", "linkedin", "github"]
        linklist = []

        print(G + "[+] Scan started......")
        print(G + "Checking whether the image is associated in any social media")
        for site in socialmedia:
            print(G + f"Scanning started in {site.capitalize()}")

        if req.status_code == 200:
            soup = BeautifulSoup(req.content, 'html.parser')

            # Debug: Print the first few lines of the HTML content
            print("HTML content preview:")
            print(soup.prettify()[:1000])  # Print first 1000 characters of prettified HTML

            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                # Extract the actual URL if it's a Google redirect link
                match = re.search(r"(?P<url>https?://[^\s]+)", href)
                if match:
                    url = match.group("url")
                    if any(sm in url for sm in socialmedia):
                        linklist.append(url)
                        print(cyan + "[+]" + url)

            if not linklist:
                print(red + "No social media links associated with this image")
        else:
            print(red + f"Failed to retrieve the search results from Google. Status code: {req.status_code}")

        spinner.stop()
    except Exception as e:
        print(red + str(e))
        spinner.stop()

if __name__ == "__main__":
    recon()
