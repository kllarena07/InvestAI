from bs4 import BeautifulSoup
import requests
from FileIntoS3 import create_file_in_s3

def scrape_text(url):
    with open('cookie.txt', 'r') as file:
        text = file.read()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "cookie": text
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    full_title = soup.find('title').get_text()
    title = full_title.split(" | ")[0]
    
    paragraphs = soup.find_all('p')

    para_chunks = []
    for paragraph in paragraphs:
        para_text = paragraph.get_text()
        para_chunks.append(para_text)

    return para_chunks, title

(chunks, title) = scrape_text("https://seekingalpha.com/article/4666957-meta-platforms-inc-meta-q4-2023-earnings-call-transcript")
create_file_in_s3(title, chunks)
