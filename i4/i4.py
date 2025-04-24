import requests
import pandas as pd
from bs4 import BeautifulSoup

# 1. Access HTML content
def access_html():
    """
    Accesses HTML content from a webpage and prints the title.

    Pros:
    - Great for scraping visible website content.
    - No need for complex authentication or credentials.

    Cons:
    - Page structure may change over time.
    - May require user-agent headers or deal with CAPTCHA.
    """
    url = "https://selinaliu8.github.io/portfolio-react/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print("HTML Title:", soup.title.string)

# 2. Access data from an API
def access_api():
    """
    Accesses structured data via HTTP API (JSONPlaceholder) and prints sample.

    Pros:
    - Structured, easy-to-parse.
    - Many public APIs available for testing and learning.

    Cons:
    - May require keys or rate limits.
    - Internet connection needed.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()
    print("First post from API:")
    print(data[0])

# 3. Access CSV from a URL
def access_csv():
    """
    Loads CSV data from a web URL and shows top rows.

    Pros:
    - Lightweight format.
    - Easy to load into pandas for data analysis.

    Cons:
    - Requires download or access URL.
    - Format may vary (delimiter, encoding).

    Make sure you have `pandas` installed: pip install pandas
    """
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv"
    df = pd.read_csv(url)
    print("CSV Preview:")
    print(df.head())

# Run all
if __name__ == "__main__":
    access_html()
    access_api()
    access_csv()