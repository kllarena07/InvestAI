from bs4 import BeautifulSoup
import requests
from FileIntoS3 import create_file_in_s3
from get_urls import *

def scrape_text(url):
    with open('cookie.txt', 'r') as file:
        text = file.read()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "cookie": text
    }

    response = requests.get(url, headers=headers)
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")

    full_title = soup.find('title').get_text()
    title = full_title.split(" | ")[0]
    
    paragraphs = soup.find_all('p')

    para_chunks = []
    for paragraph in paragraphs:
        para_text = paragraph.get_text()
        para_chunks.append(para_text)
    print(para_chunks)

    with open(f"{title}.json", "w") as file:
        json.dump(para_chunks, file, indent=2)

    return para_chunks

# def main(ticker):
#     urls = [get_company_quarterly_transcript_urls(ticker)]
#     for url in urls[:3]:
#         print(url)
#         scrape_text(url)

# main("mdb")

scrape_text("https://seekingalpha.com/article/4608938-mongodb-inc-mdb-q1-2024-earnings-call-transcript")
