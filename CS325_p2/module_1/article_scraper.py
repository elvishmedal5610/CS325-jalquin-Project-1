# SOLID Principle: Single Responsibility Principle (SRP)
# This module focuses on the single responsibility of scraping articles from URLs.

import requests
from bs4 import BeautifulSoup

class ArticleScraper:
    """
    ArticleScraper class is responsible for scraping articles from provided URLs.
    """

    @staticmethod
    def scrape_article(url):
        """
        Scrapes the content of the news article from the provided URL.
        Returns the article content as a string.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for any HTTP errors
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extracting the main content of the article
            article_content = soup.find('div', class_='article-body')  # Adjust class name according to the website structure
            if article_content is None:
                raise ValueError("Article content not found")

            # Filtering out unwanted elements like advertisements, comments, etc.
            unwanted_elements = article_content.find_all(['script', 'style'])
            for element in unwanted_elements:
                element.extract()

            return article_content.get_text(separator='\n')
        except Exception as e:
            print(f"Error fetching content from {url}: {e}")
            return None
