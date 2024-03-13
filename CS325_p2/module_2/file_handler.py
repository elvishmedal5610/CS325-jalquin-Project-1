# SOLID Principle: Open/Closed Principle (OCP)
# This module is open for extension (e.g., adding new file handling methods) but closed for modification.

import os

class FileHandler:
    """
    FileHandler class is responsible for handling file operations.
    """

    @staticmethod
    def save_article_content(content, filename):
        """
        Saves the article content to a file.
        """
        try:
            filepath = os.path.join("Data", "processed", filename)
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"Article saved as {filename}")
        except Exception as e:
            print(f"Error saving article content to file: {e}")

    @staticmethod
    def read_urls_from_file(filename):
        """
        Reads URLs from a text file and returns a list of URLs.
        """
        try:
            filepath = os.path.join("Data", "raw", filename)
            with open(filepath, 'r') as f:
                urls = f.read().splitlines()
            return urls
        except Exception as e:
            print(f"Error reading URLs from file: {e}")
            return []

    @staticmethod
    def get_filename(url):
        """
        Extracts the filename from a URL.
        """
        return url.split('/')[-1]
