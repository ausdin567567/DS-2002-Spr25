#!/usr/bin/env python3

import os

fav_color = input("What is your favorite color? ")
fav_team = input("What is your favorite football team? ")
have_coded = input("Have you ever coded on IntellJ? ")

os.environ["FAV_COLOR"] = fav_color
os.environ["FAV_TEAM"] = fav_team
os.environ["HAVE_CODED"] = have_coded

print(f"Favorite Color: {os.getenv('FAV_COLOR')}")
print(f"Favorite Team: {os.getenv('FAV_TEAM')}")
print(f"Ever Coded on IntellJ: {os.getenv('HAVE_CODED')}")
