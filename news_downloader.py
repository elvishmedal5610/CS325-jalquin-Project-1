import os
import requests
from bs4 import BeautifulSoup

def get_article_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        article_content = soup.find('div', class_='article-body__content')  # Adjust class name according to the website structure
        if article_content is None:
            raise ValueError("Article content not found")

        unwanted_elements = article_content.find_all(['script', 'style'])
        for element in unwanted_elements:
            element.extract()

        return article_content.get_text(separator='\n')
    except Exception as e:
        print(f"Error fetching content from {url}: {e}")
        return None

def download_articles(urls_file):
    with open(urls_file, 'r') as f:
        urls = f.read().splitlines()

    for idx, url in enumerate(urls):
        article_content = get_article_content(url)
        if article_content:
            filename = f"article_{idx+1}.txt"
            with open(filename, 'w') as f:
                f.write(article_content)
            print(f"Article {idx+1} saved as {filename}")

if __name__ == "__main__":
    urls_file = "website_urls.txt"  # Change this to the name of your URLs text file
    download_articles(urls_file)

