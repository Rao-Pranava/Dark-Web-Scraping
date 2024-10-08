# Dark-Web-Scraping
A Scraping tool for Dark Web..... nothing that serious, but fun.

# Clone
Clone this perticuarl code into the computer where tor is configured (I have personally not tested on any other platforms other than Whonix, so if you get any error, please do raise a Issue)

```
git clone https://github.com/Rao-Pranava/Dark-Web-Scraping.git
```

# Scrap.py
How this version works:

## Arguments:

* `onion_url`: You must specify the Onion URL to scrape.
* `--keyword` or `-k`: Optional keyword to search for on the page.
* `--open` or `-o`: Optional flag to open the Onion URL in the Tor browser if the keyword is found.

## Command-Line Usage:

* To scrape an Onion URL without a keyword:

```
python3 Scrap.py http://exampleonion.onion
```

* To scrape an Onion URL and search for a keyword:

```
python3 Scrap.py http://exampleonion.onion --keyword secret
```

* To scrape an Onion URL, search for a keyword, and open it in the Tor browser:

```
python3 Scrap.py http://exampleonion.onion --keyword secret --open
```

### Help Option (`--help`):

* Running the following command will display the help message:

```
python3 Scrap.py --help
```

This will output:
```
usage: Scrap.py [-h] [--keyword KEYWORD] [--open] onion_url

Scrape Onion links from a specified URL and search for a keyword if desired.

positional arguments:
  onion_url            The Onion URL to scrape

optional arguments:
  -h, --help           show this help message and exit
  --keyword KEYWORD, -k KEYWORD
                       Keyword to search for on the scraped page
  --open, -o           Open the Onion URL in the Tor browser if the keyword is found
```

# search_company_ahima.py

How this version works:
You can run the script like this:

```
python3 search_company_ahima.py "Company"
```

The --help option provides a description of how to use the script:

```
python3 search_company_ahima.py --help
```

This will display:

```
usage: search_company_ahima.py [-h] company_name

Search for a company on Ahima and save related links.

positional arguments:
  company_name  The name of the company to search for on Ahima

optional arguments:
  -h, --help    show this help message and exit
```
