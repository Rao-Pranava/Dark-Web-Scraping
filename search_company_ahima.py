import requests
from bs4 import BeautifulSoup
import os
import argparse

def search_company_on_ahima(company_name):
    # Base URL for Ahima search
    base_url = "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q="
    
    # Replace spaces with '+' for the query string
    query = company_name.replace(" ", "+")
    search_url = f"{base_url}{query}"

    # Create a folder named Dump if it doesn't exist
    dump_folder = 'Dump'
    os.makedirs(dump_folder, exist_ok=True)  # Create Dump folder if it doesn't exist

    # Function to avoid overwriting existing files
    def get_unique_filename(filename_base, extension):
        counter = 1
        filename = f"{filename_base}{extension}"
        while os.path.exists(filename):
            filename = f"{filename_base} {counter}{extension}"
            counter += 1
        return filename

    # Create filenames based on the company name
    sanitized_company_name = company_name.replace(" ", "_")  # Replace spaces with underscores for the filename
    exact_match_file = get_unique_filename(os.path.join(dump_folder, f'{sanitized_company_name}-Ahema-link'), '.txt')
    alter_match_file = get_unique_filename(os.path.join(dump_folder, f'alter-{sanitized_company_name}-ahima'), '.txt')

    try:
        # Fetch the Ahima search results page
        response = requests.get(search_url)

        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            with open(exact_match_file, 'w') as exact_file, open(alter_match_file, 'w') as alter_file:
                found_links = False  # Flag to check if any links were found
                all_links_found = False  # Flag for all links

                # Search for links containing the company name in the search results
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    # If the link text matches the company name
                    if company_name.lower() in link.text.lower():  
                        exact_file.write(f"{href}\n")
                        found_links = True
                    # Save all links to alter_match_file regardless of name matching
                    alter_file.write(f"{href}\n")
                    all_links_found = True

                # Output based on exact match
                if found_links:
                    print(f"Links related to '{company_name}' have been saved to '{exact_match_file}'.")
                else:
                    print(f"No exact links found for the company '{company_name}' on Ahima.")
                    if all_links_found:
                        save_all = input(f"Do you want to save all links found on Ahima to '{alter_match_file}'? (yes/no): ")
                        if save_all.lower() == 'yes':
                            print(f"All links have been saved to '{alter_match_file}'.")
                            print(f"You can manually search through this link: '{search_url}'")
                        else:
                            print("All links not saved.")
                    else:
                        print("No links found at all.")

        else:
            print(f"Failed to retrieve Ahima search results. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description='Search for a company on Ahima and save related links.')
    
    # Add argument for company name
    parser.add_argument('company_name', help='The name of the company to search for on Ahima')
    
    # Parse arguments
    args = parser.parse_args()

    # Pass the company name to the function
    search_company_on_ahima(args.company_name)
