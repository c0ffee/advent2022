with open("input.txt", "r") as f:
  result = 0
  score = 0
  while (round := f.readline()):
    match round.strip():
        case "A X":
            score = 1 + 3 
        case "A Y":
            score = 2 + 6
        case "A Z":
            score = 3 + 0
        case "B X":
            score = 1 + 0
        case "B Y":
            score = 2 + 3
        case "B Z":
            score = 3 + 6
        case "C X":
            score = 1 + 6
        case "C Y":
            score = 2 + 0
        case "C Z":
            score = 3 + 3
        case _:
            print("the fuck")
    result = result + score
  print(result)

handpoints = {"A": 1, "B": 2, "C": 3}
with open("input.txt", "r") as f:
  result = 0
  score = 0
  while (round := f.readline()):
    (hand, outcome) = round.strip().split(" ")
    if hand == "A":
        if outcome == "X":
            ownhand = "C"
            score = 0
        elif outcome == "Y":
            ownhand = hand
            score = 3
        elif outcome == "Z":
            ownhand = "B"
            score = 6
    elif hand == "B":
        if outcome == "X":
            ownhand = "A"
            score = 0
        elif outcome == "Y":
            ownhand = hand
            score = 3
        elif outcome == "Z":
            ownhand = "C"
            score = 6
    elif hand == "C":
        if outcome == "X":
            ownhand = "B"
            score = 0
        elif outcome == "Y":
            ownhand = hand
            score = 3
        elif outcome == "Z":
            ownhand = "A"
            score = 6
    result = result + score + handpoints[ownhand]
  print(result)
