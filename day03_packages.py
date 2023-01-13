'''#To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?'''

'''
Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.
'''


score = 0
with open("day03_input.txt") as f:
    lines = f.readlines()

    for line in lines:
        half1 = len(line)//2

        word1 = line[:half1]
        word2 = line[half1:]

        set1 = set(word1)
        set2 = set(word2)

        common = set1.intersection(set2)
        neat = ''.join(common)
        #print(neat)
        #print(common)

        #Getting the values
        if str(neat).islower():
            #print(f"{neat},{ord(neat)},{(ord(neat) - 96)}")
            score += (ord(neat) - 96)
        elif str(neat).isupper():
            #print(f"{neat},{ord(neat)},{(ord(neat) - 64)}")
            score += (ord(neat) - 38)
        else:
            print("Not a letter.")

    print(score)

