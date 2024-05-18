# Author: Barini Simhadri
# Date: 20-02-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link: https://youtu.be/tcgzH4xOTgU

from html.parser import HTMLParser
from collections import Counter
from urllib.request import urlopen
from urllib.parse import urljoin
from urllib.parse import urlparse

class CDMHTMLParser(HTMLParser):
    """
    Custom HTML parser to extract text from CDM webpages.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = ""  # Initialize variable to store extracted text
        self.in_content = False  # Flag to indicate whether currently inside content

    def handle_starttag(self, tag, attrs):
        # Check if the tag is a paragraph or a div (content)
        if tag == "p" or tag == "div":
            self.in_content = True  # Set flag to True indicating start of content

    def handle_endtag(self, tag):
        # Check if the tag is closing a paragraph or a div
        if tag == "p" or tag == "div":
            self.in_content = False  # Set flag to False indicating end of content

    def handle_data(self, data):
        # If currently inside content, append the data to the text
        if self.in_content:
            self.text += data  # Append data to text

def crawl_cdm_website(start_url, max_links):
    """
    Crawl through the CDM website and count the occurrence of words.

    Args:
        start_url (str): The starting URL of the website.
        max_links (int): Maximum number of links to visit.

    Returns:
        list: A list of tuples containing the most common words and their counts.
    """
    visited_links = set()  # Track visited links to avoid revisiting
    word_counter = Counter()  # Counter to count word occurrences
    links_to_visit = [start_url]  # Initialize links to visit with the start URL

    # Continue crawling while there are links to visit and not exceeding max_links
    while links_to_visit and len(visited_links) < max_links:
        url = links_to_visit.pop(0)  # Get the first URL from the list
        visited_links.add(url)  # Add the URL to visited_links set

        try:
            response = urlopen(url)  # Open the URL
            if 'text/html' in response.getheader('Content-Type'):  # Check if HTML content
                html_content = response.read().decode('utf-8')  # Read and decode HTML content
                parser = CDMHTMLParser()  # Create an instance of the custom HTML parser
                parser.feed(html_content)  # Feed HTML content to the parser
                words = parser.text.split()  # Split the extracted text into words
                word_counter.update(words)  # Update word counter with word occurrences

                # Extract links from the webpage
                for tag, attrs in parser.links:
                    if tag == 'a' and 'href' in attrs:  # Check if it's an anchor tag with href attribute
                        link = attrs['href']  # Get the value of href attribute (the link)
                        # Ensure the link is within the CDM domain
                        if urlparse(link).netloc == 'cdm.depaul.edu':
                            full_link = urljoin(url, link)  # Resolve relative URLs
                            if full_link not in visited_links:  # Check if the link has not been visited
                                links_to_visit.append(full_link)  # Add the link to links_to_visit list
        except Exception as e:
            print(f"Error crawling {url}: {e}")  # Print error message if any

    # Return the 25 most common words
    return word_counter.most_common(25)

if __name__ == "__main__":
    start_url = "http://cdm.depaul.edu"
    max_links = 10000
    common_words = crawl_cdm_website(start_url, max_links)
    print("The 25 most common words on the CDM website are:")
    for word, count in common_words:
        print(f"{word}: {count}")