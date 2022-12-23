with open("input.txt","r") as f:
    result = 0
    while (line := f.readline()):
      (r1, r2) = line.strip().split(",")
      (r1_l, r1_r) = r1.split("-")
      (r2_l, r2_r) = r2.split("-")
      r1_l = int(r1_l) 
      r1_r = int(r1_r) 
      r2_l = int(r2_l) 
      r2_r = int(r2_r) 
      if (r1_l >= r2_l) and (r1_r <= r2_r):
            #print(r1 + " in " + r2)
            result = result + 1
      elif (r2_l >= r1_l) and (r2_r <= r1_r):
            #print(r2 + " in " + r1)
            result = result + 1
    print(result)

with open("input.txt","r") as f:
    result = 0
    while (line := f.readline()):
      (r1, r2) = line.strip().split(",")
      r1 = list(map(int, r1.split("-")))
      r2 = list(map(int, r2.split("-")))
      if (r1[0] >= r2[0]) and (r1[0] <= r2[1]):
            #print(r1 + " in " + r2)
            result = result + 1
      elif (r2[0] >= r1[0]) and (r2[0] <= r1[1]):
            #print(r2 + " in " + r1)
            result = result + 1
    print(result)