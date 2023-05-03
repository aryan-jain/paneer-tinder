from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CuisineRatings:
    """Stores ratings from 0 to 5 for cuisine types."""

    italian: int = 0
    mexican: int = 0
    chinese: int = 0
    indian: int = 0
    american: int = 0
    thai: int = 0
    greek: int = 0
    japanese: int = 0
    vietnamese: int = 0
    ramen: int = 0
    maggi: int = 0

    def add_rating(self, cuisine_type, rating):
        """Add a rating to a cuisine type."""
        setattr(self, cuisine_type, rating)

    def view_ratings(self):
        """View ratings for each cuisine type."""
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")

    def top_three(self):
        """View top three cuisine types by score."""
        sorted_ratings = sorted(self.__dict__.items(), key=lambda x: x[1], reverse=True)
        print(sorted_ratings[:3])

    def matches(self, other: CuisineRatings) -> list[tuple]:
        """Return a dictionary of cuisine types that match."""
        matches = {}
        for attr, value in self.__dict__.items():
            other_val = getattr(other, attr)
            if value > 0 and other_val > 0:
                match_val = (value + other_val) / 2
                if match_val > 3:
                    matches[attr] = match_val

        return (
            sorted(matches.items(), key=lambda x: x[1], reverse=True)[:3]
            if matches
            else []
        )
