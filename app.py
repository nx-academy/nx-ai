import requests

BASE_URL = "https://raw.githubusercontent.com/nx-academy/nx-academy.github.io/refs/heads/main/src/pages/cours"


def main():
    sample_url = f"{BASE_URL}/docker-et-docker-compose/chapitres/decouverte-docker.md"
    
    response = requests.get(sample_url)
    if response.status_code == 200:
        with open("decouverte-docker.md", "w", encoding="utf-8") as file:
            file.write(response.text)
            
        print(f"✅ File saved and downloaded as : {"decouverte-docker"}")
        
    else:
        print(f"❌ Error when downloading the file ({response.status_code}) : {sample_url}")
    
    

if __name__ == "__main__":
    main()
