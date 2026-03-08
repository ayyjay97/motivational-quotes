# Motivational Quote Microservice

## Description
This microservice provides a lightweight backend solution for serving random motivational quotes. It listens for HTTP GET requests and retrieves a randomly selected quote and its associated author from a local JSON dataset (`quotes.json`). The service then returns this information in a structured JSON format, making it easy to integrate daily inspiration into dashboards, health trackers, or other applications.

## How to Programmatically REQUEST Data
To request data from this microservice, you must send an HTTP GET request to the `/get_quote` endpoint. 

Because this is a simple retrieval operation, no JSON payload or parameters are required in the body of your request.

**Example Request using Python's `requests` library:**
```python
import requests

# Ensure the microservice is running locally on port 5003
url = '[http://127.0.0.1:5003/get_quote](http://127.0.0.1:5003/get_quote)'

# Send the GET request
response = requests.get(url)
```

## How to Programmatically RECEIVE Data

The microservice processes the request and responds with a JSON object containing the randomized quote data.

The successful response payload includes two keys:

* `quote`: A string containing the motivational text.

* `author`: A string indicating the person who said or wrote the quote.

**Expected JSON Response:**

```JSON
{
  "quote": "Discipline is doing what you hate to do, but nonetheless doing it like you love it.",
  "author": "Mike Tyson"
}
```

**Example of receiving and parsing the data in Python:**

```Python
# Check if the request was successful
if response.status_code == 200:
    # Parse the incoming JSON response
    data = response.json()
    
    # Extract the individual data points
    quote_text = data['quote']
    quote_author = data['author']
    
    print(f"Quote: {quote_text}")
    print(f"Author: {quote_author}")
else:
    # Handle any errors returned by the microservice (e.g., file not found)
    error_data = response.json()
    print(f"Error: {error_data.get('error')}")
```
