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
    base_url = f'https://seekingalpha.com/api/v3/symbols/{ticker}/transcripts'

    # Make the API call
    response = requests.get(base_url)

    # Parse the JSON data from the response
    data = response.json()['data']

    # Extract the URLs of the transcripts
    transcript_urls = ["https://seekingalpha.com" + quarterly_data['links']['self'] for quarterly_data in data]

    # Filter the URLs to only include the most recent 5 years of transcripts
    # This assumes that the URLs are sorted in reverse chronological order
    recent_transcript_urls = transcript_urls[:20]  # 4 quarters per year for 5 years

    return recent_transcript_urls

if __name__ == "__main__":
    apple_transcripts_urls = get_company_quarterly_transcript_urls('AAPL')
    print(apple_transcripts_urls)
    breakpoint()
