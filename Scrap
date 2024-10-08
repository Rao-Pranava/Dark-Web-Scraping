import requests
from bs4 import BeautifulSoup
import sys
import time
import subprocess
import argparse
import os

# Function to simulate typing prompt
def typing_prompt(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)  # Adjust this for typing speed
    return input()

# Function to scrape onion links
def scrape_onion_links(onion_url, keyword=None, open_in_browser=False):
    try:
        # Fetch the page via Tor (since Whonix routes through Tor automatically)
        response = requests.get(onion_url)
        
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all links with '.onion' in them
            onion_links = set()
            for link in soup.find_all('a', href=True):
                href = link['href']
                if ".onion" in href:
                    onion_links.add(href)

            # Create a folder named Dump if it doesn't exist
            dump_folder = 'Dump'
            os.makedirs(dump_folder, exist_ok=True)  # Create Dump folder if it doesn't exist

            # Write the links to a file
            output_file = os.path.join(dump_folder, 'Onion_links.txt')
            with open(output_file, 'w') as file:
                for onion_link in onion_links:
                    file.write(f"{onion_link}\n")
            print(f"Onion links have been saved to {output_file}")
        
            # If a keyword is provided, search for it on the page
            if keyword:
                keyword_count = response.text.lower().count(keyword.lower())
                
                if keyword_count > 0:
                    print(f"The keyword '{keyword}' was found {keyword_count} times on the page.")
                    
                    # If open_in_browser flag is set, open the site in the Tor browser
                    if open_in_browser:
                        print(f"Opening {onion_url} in the Tor browser...")
                        subprocess.run(['torbrowser', onion_url])
                else:
                    print(f"The keyword '{keyword}' was not found on the page.")
        else:
            print(f"Failed to retrieve page. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Argument parser for command-line arguments
    parser = argparse.ArgumentParser(description='Scrape Onion links from a specified URL and search for a keyword if desired.')
    
    # Argument for the Onion URL
    parser.add_argument('onion_url', help='The Onion URL to scrape')
    
    # Optional argument for the keyword search
    parser.add_argument('--keyword', '-k', help='Keyword to search for on the scraped page')
    
    # Optional flag to open the page in the Tor browser
    parser.add_argument('--open', '-o', action='store_true', help='Open the Onion URL in the Tor browser if the keyword is found')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Run the scraping function with the provided arguments
    scrape_onion_links(args.onion_url, keyword=args.keyword, open_in_browser=args.open)
