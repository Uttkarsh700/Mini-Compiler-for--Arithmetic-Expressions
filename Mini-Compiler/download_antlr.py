import urllib.request
import os

def download_antlr():
    url = "https://www.antlr.org/download/antlr-4.9.2-complete.jar"
    filename = "antlr-4.9.2-complete.jar"
    
    print(f"Downloading {filename}...")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Error downloading file: {str(e)}")
        return False
    return True

if __name__ == "__main__":
    download_antlr() 