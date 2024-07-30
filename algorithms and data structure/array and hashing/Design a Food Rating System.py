from typing import List


# initialise O(n)
# change rating O(n)
# highest rating O(1)
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # food: cuisine
        self.cuisine_map = {foods[i]: cuisines[i] for i in range(len(foods))}

        # cuisine: [food, rating]
        self.highest_rating_food = {}
        # cuisine:[[food, rating]]
        self.cuisine_food_rating = {}

        for i in range(len(cuisines)):
            c = cuisines[i]
            f = foods[i]
            r = ratings[i]

            if c not in self.cuisine_food_rating:
                self.cuisine_food_rating[c] = [[f, r]]
            else:
                self.cuisine_food_rating[c].append([f, r])

            if c not in self.highest_rating_food:
                self.highest_rating_food[c] = [f, r]
            else:
                current_highest_rating_food = self.highest_rating_food[c][0]
                current_highest_rating = self.highest_rating_food[c][1]
                
                if r > current_highest_rating or (r == current_highest_rating and f < current_highest_rating_food):
                    self.highest_rating_food[c] = [f, r]

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.cuisine_map[food]

        highest_rating = -float('inf')
        highest_rating_food = chr(ord('z')+1)

        food_ratings = self.cuisine_food_rating[c]

        for i in range(len(food_ratings)):

            f = food_ratings[i][0]

            if f == food:
                food_ratings[i][1] = newRating

            r = food_ratings[i][1]

            if (r > highest_rating) or (r == highest_rating and f < highest_rating_food):
                highest_rating = r
                highest_rating_food = f
        
            self.highest_rating_food[c] = [highest_rating_food, highest_rating]
            

    def highestRated(self, cuisine: str) -> str:
        highest_rating_food = self.highest_rating_food[cuisine][0]
        return highest_rating_food

# initialise: O(n log n)
# changeRating: O(log n) for both add and remove
# highestRated: O(1)
from collections import defaultdict

from sortedcontainers import SortedSet


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine_map = {}
        self.cuisine_food_rating = defaultdict(SortedSet)
        self.food_rating = {}

        for i in range(len(foods)):
            f = foods[i]
            r = ratings[i]
            c = cuisines[i]

            self.cuisine_map[f] = c
            self.cuisine_food_rating[c].add((-r,f))
            self.food_rating[f] = r

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.cuisine_map[food]
        r = self.food_rating[food]
        self.cuisine_food_rating[c].remove((-r, food))
        self.cuisine_food_rating[c].add((-newRating, food))

        self.food_rating[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_food_rating[cuisine][0][1]