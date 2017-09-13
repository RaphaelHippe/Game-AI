# Solution of Einstein's Zebra Puzzle (http://en.wikipedia.org/wiki/Zebra_Puzzle)

import itertools


def imright(h1, h2):
    return h1 - h2  == 1


def nextto(h1, h2):
    return abs(h1 - h2) == 1


def zebra_puzzle_slow():
    houses = [first, _, middle, _, _] = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA, Englishman, Spaniard, Ukranian, Japanese, Norwegian)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                if Norwegian == first
                for (red, green, ivory, yellow, blue) in orderings
                if Englishman == red and imright(green, ivory) and nextto(Norwegian, blue)
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard == dog
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee == green and Ukranian == tea and milk == middle
                for (Parliaments, Gold, Chesterfields, Kools, Lucky_Strike) in orderings
                if Gold == snails and Kools == yellow and nextto(Chesterfields, fox) and nextto(Kools, horse) and Lucky_Strike == oj and Parliaments == Japanese
                # if Norwegian == first
                # if Englishman == red and imright(green, ivory) and nextto(Norwegian, blue)
                # if Spaniard == dog
                # if coffee == green and Ukranian == tea and milk == middle
                # if Gold == snails and Kools == yellow and nextto(Chesterfields, fox) and nextto(Kools, horse) and Lucky_Strike == oj and Parliaments == Japanese

)

if __name__ == '__main__':
    print zebra_puzzle_slow()
