# This is the main program that imports the functionality of other modules and orchestrates the process.

from module_1.article_scraper import ArticleScraper
from module_2.file_handler import FileHandler
import sys

def main(args):
    if len(args) != 2:
        print("Usage: python3 run.py <URLs/File/argument>")
        return

    source = args[1]
    if source.lower() == "file":
        # Read URLs from file
        urls = FileHandler.read_urls_from_file("website_urls.txt")
        if not urls:
            print("No URLs found in the file.")
            return
    else:
        urls = [source]

    for url in urls:
        # Scrape article content
        article_content = ArticleScraper.scrape_article(url)
        if article_content:
            # Save article content to a file
            filename = FileHandler.get_filename(url) + ".txt"
            FileHandler.save_article_content(article_content, filename)

if __name__ == "__main__":
    main(sys.argv)
