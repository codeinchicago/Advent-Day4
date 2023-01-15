
count = 0
with open("day04_input.txt") as f:
    lines = f.readlines()
    newstuff = []
    for line in lines:
        line = line.strip()
        b = line.replace(","," ")
        a = b.replace("-",",")
        pair1, pair2 = a.split(" ")
        lower1, higher1 = [int(value) for value in pair1.split(",")]
        lower2, higher2 = [int(value) for value in pair2.split(",")]
        if lower1 >= lower2 and higher1 <= higher2:
            count += 1
            #print(lower1,higher1,lower2,higher2)
        elif lower2 >= lower1 and higher2 <= higher1:
            count += 1
            #print(lower1,higher1,lower2,higher2)
        #print("Count is:")
    print(count)
