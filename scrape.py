#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

def main():

    url = "https://www.sanews.gov.za/"

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    print("Latest South African News Headlines:\n")

    for heading in soup.find_all("h2")[:5]:
        print("-", heading.get_text(strip=True))


if __name__ == "__main__":
    main()