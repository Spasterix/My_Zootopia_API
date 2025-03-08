"""
Module for fetching animal data from the API-Ninjas Animals API.
"""
import os
import sys
import requests
from typing import Dict, List
from dotenv import load_dotenv

# Load environment variables
if not load_dotenv():
    print("Error: .env file not found. Please create a .env file with your API_KEY.")
    sys.exit(1)

# API Constants
API_KEY = os.getenv('API_KEY')
if not API_KEY:
    print("Error: API_KEY not found in .env file. Please add API_KEY=your_api_key to your .env file.")
    sys.exit(1)

API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name: str) -> List[Dict]:
    """
    Fetches the animals data for the animal 'animal_name'.
    
    Args:
        animal_name (str): Name of the animal to search for

    Returns:
        List[Dict]: a list of animals, each animal is a dictionary:
        {
            'name': str,
            'taxonomy': {
                'kingdom': str,
                'phylum': str,
                'class': str,
                'order': str,
                'family': str,
                'genus': str,
                'scientific_name': str
            },
            'locations': List[str],
            'characteristics': {
                'diet': str,
                'type': str,
                'skin_type': str,
                'lifespan': str,
                ...
            }
        }
    """
    try:
        response = requests.get(
            API_URL,
            params={"name": animal_name},
            headers={"X-Api-Key": API_KEY}
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return [] 