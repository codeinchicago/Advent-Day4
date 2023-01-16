#sequence of four characters which are different

count = 0
#Shift the count over by 3, check if len(set([0:4])) is the same as 4.

# text = 'aabcda'
# print(text[0:4])
# a=set(text[0:4])

# print(len(a))


# 5,6,10,11

with open("day06_input.txt") as f:
    lines = f.readlines()

    for line in lines:
        searching = True
        count = 0
        line = line.strip()
        while searching:
            evaluating = line[count:count+4]
            if len(set(evaluating)) == 4:
                print(f"Found it at {count+4}. {evaluating}")
                searching = False
            count += 1