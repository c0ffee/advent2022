with open("input.txt", "r") as f:
    highscore = 0
    tmp = 0
    while line := f.readline():
        if line == "\n":
            print("New elf his score " + str(tmp) + " vs highscore " + str(highscore))
            if tmp > highscore:
                highscore = tmp
            tmp = 0
        else:
            tmp = tmp + int(line)
    print("Highscore: " + str(highscore))

