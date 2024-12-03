import requests
import os

def download_file(url, destFile):
    if not os.path.exists(destFile):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(destFile, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print(f"\033[42m\033[30mData set downloaded\033[0m")
        else:
            print(f"\033[41m\033[97mFailed to download file. StatusCode: {response.status_code}\033[0m")
    else:
        print(f"\033[42m\033[30mThe Dataset is already downloaded\033[0m")
        
currDir = os.path.dirname(os.path.abspath(__file__))
destFile = os.path.join(currDir, "downloaded_text.txt")
url = "https://raw.githubusercontent.com/amankharwal/Website-data/master/text.txt"

download_file(url, destFile)