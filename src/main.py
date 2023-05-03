import argparse
import os
import time

from db.database import CuisineRatings
from utils import get_rating


def main():
    p1 = CuisineRatings()
    p2 = CuisineRatings()

    print(f"Pass the computer to {args.person1.title()}.")
    for cuisine in p1.__dict__:
        if cuisine not in args.ignore:
            p1.add_rating(cuisine, get_rating(cuisine))
            print("\033[1A" + "\033[K")  # Hide the rating.

    print(f"Pass the computer to {args.person2.title()}.")
    for cuisine in p2.__dict__:
        if cuisine not in args.ignore:
            p2.add_rating(cuisine, get_rating(cuisine))
            print("\033[1A" + "\033[K")  # Hide the rating.

    print(f"Calculating your matches...")
    time.sleep(1)

    matches = p1.matches(p2)
    if not matches:
        print(
            f"No matches found. Prioritizing {args.person1.title()}'s ratings \
                because let's be honest, everyone stays happier this way."
        )
        print(f"Top three cuisines for {args.person1.title()}:")
        for c, r in p1.top_three():
            print(f"{c.title()}: {r}")

    else:
        print(
            f"Top three cuisines for {args.person1.title()} and {args.person2.title()}:"
        )
        for c, r in matches:
            print(f"{c.title()}: {r}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=f"Rate your current mood to eat a particular cuisine. {list(CuisineRatings().__dict__.keys())}"
    )
    parser.add_argument(
        "-i",
        "--ignore",
        type=str,
        nargs="+",
        help="Cuisine types to ignore.",
        required=False,
        default=[],
    )
    parser.add_argument(
        "-p1",
        "--person1",
        type=str,
        help="Name of person 1. (Put the name of the female here in heterosexual relationships)",
        required=False,
        default="Person 1",
    )
    parser.add_argument(
        "-p2",
        "--person2",
        type=str,
        help="Name of person 2.",
        required=False,
        default="Person 2",
    )
    parser.add_argument("-z", "--zip-code", type=int, help="Zip code.", required=True)
    parser.add_argument(
        "-k",
        "--api-key",
        type=str,
        help="Yelp API key. [Env: YELP_API_KEY]",
        required=False,
        default=os.environ.get("YELP_API_KEY"),
    )
    args = parser.parse_args()

    main()
