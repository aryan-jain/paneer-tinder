import json
import traceback
from enum import Enum
from typing import Union

import requests


class YelpSortBy(Enum):
    BEST_MATCH = "best_match"
    RATING = "rating"
    REVIEW_COUNT = "review_count"
    DISTANCE = "distance"


def get_rating(cuisine: str) -> int:
    """Get a rating from the user."""
    while True:
        try:
            rating = int(input(f"Rate {cuisine.title()} from 0 to 5: "))
            if 0 <= rating <= 5:
                return rating
            else:
                print("Rating must be between 0 and 5.")
        except ValueError:
            print("Rating must be an integer.")


def get_top_restaurants(
    zip_code: Union[int, str],
    cuisine: str,
    api_key: str,
    limit=5,
    sort_by=YelpSortBy.BEST_MATCH,
):
    """
    Get a list of top 10 highest rated restaurants
    of the provided cuisine near the provided ZIP code
    from Yelp that are open now.
    """
    # Define Yelp API endpoint and parameters
    url = "https://api.yelp.com/v3/businesses/search"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    params = {
        "location": str(zip_code),
        "categories": cuisine,
        "sort_by": sort_by,
        "open_now": True,
        "limit": limit,
    }
    try:
        # Send GET request to Yelp API and get response data
        response = requests.get(url, headers=headers, params=params)
        data = json.loads(response.text)

        # Extract the top 10 highest-rated restaurants from response data
        restaurants = []
        for business in data["businesses"]:
            name = business["name"]
            rating = business["rating"]
            address = ", ".join(business["location"]["display_address"])
            restaurants.append(
                {
                    "name": name,
                    "rating": rating,
                    "#ratings": business["review_count"],
                    "address": address,
                }
            )

        # Return list of top 10 highest-rated restaurants
        return restaurants
    except Exception:
        print("Error retrieving data from Yelp API.")
        traceback.print_exc()
        return []
