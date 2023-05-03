# paneer-tinder
A simple app that will take away all the stress of deciding where to eat between you and your spouse. We know you missed the joy of swiping right endlessly on your phones, but haven't been able to ever since you got into this relationship. Enter, Paneer-Tinder! Instead of swiping right and left on people, you and your spouse will rate cuisine choices from 0 to 5 based on your mood. Then the app will list your top 3 matches on cuisine and present you with a list of highly rated Yelp restaurants that are open now nearby.

### Usage:
```
    python3 main.py [-h] [-i IGNORE [IGNORE ...]] [-p1 PERSON1] [-p2 PERSON2] -z ZIP_CODE [-k API_KEY]

Rate your current mood to eat a particular cuisine. ['italian', 'mexican', 'chinese', 'indian', 'american', 'thai', 'greek', 'japanese', 'vietnamese',
'ramen', 'maggi']

options:
  -h, --help            show this help message and exit
  -i IGNORE [IGNORE ...], --ignore IGNORE [IGNORE ...]
                        Cuisine types to ignore.
  -p1 PERSON1, --person1 PERSON1
                        Name of person 1. (Put the name of the female here in heterosexual relationships)
  -p2 PERSON2, --person2 PERSON2
                        Name of person 2.
  -z ZIP_CODE, --zip-code ZIP_CODE
                        Zip code.
  -k API_KEY, --api-key API_KEY
                        Yelp API key. [Env: YELP_API_KEY]
```