import requests
import re

def scrape_news_headlines(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            headlines = []

            headline_pattern = r'<h2.*?>(.*?)<\/h2>'
            headline_matches = re.findall(headline_pattern, html_content, re.DOTALL | re.IGNORECASE)

            for index, headline_text in enumerate(headline_matches, start=1):
                headline_text = re.sub('<[^<]+?>', '', headline_text).strip()
                headlines.append(f"{index}. {headline_text}")

            return headlines
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return []

def main():
    url = "http://indianexpress.com"  
    print("Latest News Headlines:")
    headlines = scrape_news_headlines(url)

    if headlines:
        for headline in headlines:
            print(headline)
    else:
        print("No headlines found.")

if __name__ == "__main__":
    main()
