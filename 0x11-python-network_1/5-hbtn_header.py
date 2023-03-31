#!/usr/bin/python3
"""
Python script that sends a request to the URL and
displays the value of a variable in the response header
"""
import requests
import sys


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python3 script.py <URL>")
        r = requests.get(sys.argv[1])
        r.raise_for_status() # Raise an exception if the request fails
        print(r.headers['X-Request-Id'])
    except (requests.exceptions.RequestException, ValueError) as e:
        print("Error:", e)
        sys.exit(1)
