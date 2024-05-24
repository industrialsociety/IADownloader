import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_file(url, folder):
    local_filename = os.path.join(folder, url.split('/')[-1])
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def download_all_files_from_collection(url):
    folder_name = "downloaded_files"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the URL: {url}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=True)
    for link in links:
        file_url = urljoin(url, link['href'])
        if any(ext in file_url for ext in ['.pdf', '.txt', '.zip', '.jpg', '.png', '.mp3', '.mp4']):
            print(f"Downloading: {file_url}")
            download_file(file_url, folder_name)

if __name__ == "__main__":
    collection_url = input("Enter the URL: ")
    download_all_files_from_collection(collection_url)
