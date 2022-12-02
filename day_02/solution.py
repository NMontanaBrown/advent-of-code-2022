# coding=utf-8

"""
Solution for day 2 of AOC22.
"""

class StrategyGuide():
    """
    To parse and interpret the elves strategy
    guide to win Rock Paper Scissors tournament.
    """
    def __init__(self, input_txt:str):
        """
        Takes an input .txt file, stores is at as
        a class param.
        """
        self.input = input_txt

    def parse_txt_file(self):
        """
        We parse the txt file
        and convert it into a list for
        the elf tactic and your tactic.
        """
        dict_tactics_elf = {"A":0, "B":1, "C":2}
        dict_tactics_yours = {"X":0, "Y":1, "Z":2}
        your_tactic = []
        elf_tactic = []
        with open(self.input, "r") as f:
            lines = f.readlines()
            for line in lines:
                tactics = line.rstrip().split(" ")
                elf_tactic.append(dict_tactics_elf[tactics[0]])
                your_tactic.append(dict_tactics_yours[tactics[1]])
        self.your_tactic = your_tactic
        self.elf_tactic = elf_tactic

    def interpret_tactics_solution_1(self):
        """
        For solution 1, we interpret the
        elf tactic (column 1) as what the elf
        will play, and your tactic (column 2)
        as what you will play. Playing Rock, paper,
        scissors has score (1, 2, 3) associated to it.
        Winning, Drawing, Losing has a (0, 3, 6) cost
        associated to it.
        """
        dict_personal_score = {0:1, 1:2, 2:3}
        dict_outcomes = {0:{0:3, 1:6, 2:0
                           },
                        1: {0:0, 1:3, 2:6},
                        2: {0:6, 1:0, 2:3}
                        }
        running_score = 0
        for i, item in enumerate(self.elf_tactic):
            personal_score = dict_personal_score[self.your_tactic[i]]
            outcome = dict_outcomes[item][self.your_tactic[i]]
            running_score += personal_score + outcome
        self.tournament_score = running_score

    def interpret_tactics_solution_2(self):
        """
        For solution 1, we interpret the
        elf tactic (column 1) as what the elf
        will play, and column 2 as the outcome (W, D, L).
        Playing Rock, paper,
        scissors has score (1, 2, 3) associated to it.
        Winning, Drawing, Losing has a (0, 3, 6) cost
        associated to it. Read the score for the part
        (R, P, S) as
        depending on what the elf plays, and desired
        outcome.
        """
        dict_personal_score = {0:0, 1:3, 2:6}
        dict_outcomes = {0:{0:3, 1:1, 2:2
                           },
                        1: {0:1, 1:2, 2:3},
                        2: {0:2, 1:3, 2:1}
                        }
        running_score = 0
        for i, item in enumerate(self.elf_tactic):
            personal_score = dict_personal_score[self.your_tactic[i]]
            outcome = dict_outcomes[item][self.your_tactic[i]]
            running_score += personal_score + outcome
        self.tournament_score = running_score


if __name__ == "__main__":
    example_guide = StrategyGuide("./example.txt")
    example_guide.parse_txt_file()
    example_guide.interpret_tactics_solution_1()
    print("Result example guide: ", example_guide.tournament_score)
    example_guide.interpret_tactics_solution_2()
    print("Result example guide second solution: ", example_guide.tournament_score)

    soln1_guide = StrategyGuide("./inputs.txt")
    soln1_guide.parse_txt_file()
    soln1_guide.interpret_tactics_solution_1()
    print("Result soln1 guide: ", soln1_guide.tournament_score)
    soln1_guide.interpret_tactics_solution_2()
    print("Result soln1 guide second solution: ", soln1_guide.tournament_score)

