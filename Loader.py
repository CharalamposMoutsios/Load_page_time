import time

import requests


def check_loading_time(url):
    """Function to check the loading time of a URL."""
    start_time = time.time()  # Record the start time
    response = requests.get(url)  # Send a GET request to the URL
    end_time = time.time()  # Record the end time
    loading_time = end_time - start_time  # Calculate the loading time in seconds
    return loading_time

# Example usage
url = "https://www.google.com"
loading_time = check_loading_time(url)
print(f"Loading time of {url}: {loading_time:.2f} seconds")
