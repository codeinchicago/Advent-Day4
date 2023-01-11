#Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

max = 0
max2 = 0
max3 = 0
count = 0
with open("day01_input.txt") as f:
    lines = f.readlines()
    newstuff = []
    for line in lines:
        if line.strip() == "":
            count = 0
            # print("Nothing here.")
        else:
            # print(line)
            count += int(line)
            # print(f"count is {count}")
            # print(f"\n{max},{max2},{max3} is the maximum.")
            if count > max:
                max3 = max2
                max2 = max
                max = count
            elif count > max2:
                max3 = max2
                max2 = count
            elif count > max3:
                max3 = count
    #print(f"\n{max},{max2},{max3} is the maximum.")
    print(max + max2 + max3)
    # print(f"\n is the maximum.")

        # pair1, pair2 = a.split(" ")
        # lower1, higher1 = [int(value) for value in pair1.split(",")]
        # lower2, higher2 = [int(value) for value in pair2.split(",")]
        # if lower1 >= lower2 and higher1 <= higher2:
        #     count += 1
        #     print(lower1,higher1,lower2,higher2)
        # elif lower2 >= lower1 and higher2 <= higher1:
        #     count += 1
        #     print(lower1,higher1,lower2,higher2)
        # print("Count is:")   
        # print(count)
