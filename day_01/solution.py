# coding=utf-8

"""
Solution to Day 1 of AOC22.
"""

from functools import reduce
from operator import add

class Elf():
    """
    An Elf, with their associated
    calorie content.
    """
    def __init__(self, stash:list):
        """
        Each elf has their own calorie
        stash of snacks. Count the total
        stash per Elf, store their stash
        as a list
        :param stash:
        """
        self.stash = stash
        self.total_cals = reduce(add, stash)

class Inventory():
    """
    An inventory of the snacks for each elf.
    """
    def __init__(self, elf_calorie_list:str):
        """
        We are provided with a calorie list
        per elf.
        """
        self.elf_calorie_list = elf_calorie_list

    def read_list(self):
        """
        A method to read the calorie list.
        """
        snack_calories_per_elf = []
        with open(self.elf_calorie_list, "r") as f:
            lines = f.readlines()
            snack_list = []
            for i, line in enumerate(lines):
                if line != "\n":
                    snack_list.append(float(line))
                    if i == (len(lines)-1):
                        snack_calories_per_elf.append(snack_list)
                else:
                    snack_calories_per_elf.append(snack_list)
                    snack_list = []
        self.snack_list_per_elf = snack_calories_per_elf

    def get_elves(self):
        """
        Generate 
        """
        elves = []
        for sublist in self.snack_list_per_elf:
            elves.append(Elf(sublist))
        self.elves = elves

    def get_max_calories(self):
        """

        """
        max_cals = [elf.total_cals for elf in self.elves]
        self.max_cals = max_cals
        self.max_cals.sort(reverse=True)
        print("Max calories carried by elf: ", max(self.max_cals))

    def get_top_3_calories(self):
        """
        """
        print(self.max_cals[0:3])
        print("Total Calories of top 3 elves: ", reduce(add, self.max_cals[0:3]))

if __name__ == "__main__":
    example_inventory = Inventory("./example.txt")
    example_inventory.read_list()
    example_inventory.get_elves()
    example_inventory.get_max_calories()
    example_inventory.get_top_3_calories()

    first_challenge_inventory = Inventory("./inputs_1.txt")
    first_challenge_inventory.read_list()
    first_challenge_inventory.get_elves()
    first_challenge_inventory.get_max_calories()
    first_challenge_inventory.get_top_3_calories()


