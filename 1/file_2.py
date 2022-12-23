with open("input.txt", "r") as f:
    highscore = [0,0,0,0]
    tmp = 0
    while line := f.readline():
        if line == "\n":
            print("New elf his score " + str(tmp) + " vs highscore " + str(highscore))
            highscore[3] = tmp
            highscore.sort(reverse=True)
            tmp = 0
        else:
            tmp = tmp + int(line)
    highscore[3] = 0
    print(highscore)
    print("Highscore: " + str(highscore[0]+highscore[1]+highscore[2]))

