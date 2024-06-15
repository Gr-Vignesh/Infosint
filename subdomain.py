import requests

cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = '\033[1;33;40m'

def fuzz():
    try:
        dom = input("Enter Domain >> ")
        url = f"https://sonar.omnisint.io/subdomains/{dom}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data:  # Check if data is not empty
                print(cyan + "Enumerating Subdomains ^-^ .....")
                for subdomain in data:
                    print(green + "[+]" + subdomain)
                print(Y + "Subdomain Enumeration Success")
            else:
                print(red + "No subdomains found for the specified domain.")
        else:
            print(red + f"Error fetching data. Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(red + "An error occurred:", e)
    except Exception as ex:
        print(red + "An unexpected error occurred:", ex)

if __name__ == "__main__":
    fuzz()
