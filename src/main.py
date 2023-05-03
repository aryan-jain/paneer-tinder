import argparse
import os
import time

from db.database import CuisineRatings
from utils import YelpSortBy, get_rating, get_top_restaurants


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

    matches: list[tuple[str, int]] = p1.matches(p2)
    if not matches:
        print(
            f"No matches found. Prioritizing {args.person1.title()}'s ratings \
                because let's be honest, everyone stays happier this way."
        )
        print(f"Top three cuisines for {args.person1.title()}:")
        matches: list[tuple[str, int]] = p1.top_three()
    else:
        print(
            f"Top three cuisines for {args.person1.title()} and {args.person2.title()}:"
        )

    for c, r in matches:
        print(f"{c.title()}: {r}")
        if c == "maggi":
            print(
                "You're a match made in heaven. \
                    Go get some Maggi noodles."
            )
        else:
            for restaurant in get_top_restaurants(args.zip_code, c, args.api_key):
                print(f"\t{restaurant}")


def str2yelpsortby(s: str) -> YelpSortBy:
    try:
        return YelpSortBy(s)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"Invalid sort by value: {s}. Must be one of {[x.lower for x in YelpSortBy.__members__.keys()]}."
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=f"Rate your current mood to eat a particular cuisine. {list(CuisineRatings().__dict__.keys())}\
            \nExample: python3 main.py -i vietnamese ramen -p1 Jane -p2 John -z 95048"
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
    parser.add_argument(
        "-s",
        "--sort-by",
        type=str2yelpsortby,
        help="Sort Yelp listings by. (best_match/rating/review_count/distance)[Default: best_match]",
        required=False,
        default="best_match",
    )
    args = parser.parse_args()

    main()
