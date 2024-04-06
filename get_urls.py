from typing import List
import requests
import json
import datetime

def get_company_quarterly_transcript_urls(ticker: str) -> List[str]:
    """
    Call the seekingalpha API to get the JSON data of the company's quarterly earnings call transcript.
    Extract the URLS of the most recent 5 years of quarterly earnings call transcript.
    Save the URLs into a list and return the list.
    :param ticker:
    :return: a list of URLs
    """
    # Define the base URL for the API call
    with open('cookie2.txt', 'r') as file:
        text = file.read()
 
    base_url = f'https://seekingalpha.com/api/v3/symbols/{ticker}/transcripts'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "cookie": text
        }

    # Make the API call
    response = requests.get(base_url, headers=headers)

    # Parse the JSON data from the response
    data = response.json()['data']

    # Extract the URLs of the transcripts
    transcript_urls = ["https://seekingalpha.com/" + quarterly_data['links']['self'] for quarterly_data in data]

    # Filter the URLs to only include the most recent 5 years of transcripts
    # This assumes that the URLs are sorted in reverse chronological order
    recent_transcript_urls = transcript_urls[:30]  # 4 quarters per year for 5 years

    # print(recent_transcript_urls)

    return recent_transcript_urls

get_company_quarterly_transcript_urls("aapl")

# if __name == "__main":
#     apple_transcripts_urls = get_company_quarterly_transcript_urls('AAPL')
#     print(apple_transcripts_urls)
#     breakpoint()