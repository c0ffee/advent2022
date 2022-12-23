from operator import length_hint 

with open("input.txt", "r") as f:
  result = 0
  wrongitems = list()
  while (line := f.readline()):
    arr = list(line.strip())
    len = int(length_hint(arr))
    done = False
    for i in range(int(len/2)):
        if done == True:
           break
        for j in range(int(len/2), len):
          if arr[i] == arr[j]:
            wrongitems.append(arr[i])
            #print("Match: " + arr[i])
            val = ord(arr[i])
            if val < 97:
                prio = val - 65 + 27
            else:
                prio = val - 97 + 1
            result = result + prio
            done = True
            break
  print(result)

with open("input.txt", "r") as f:
  result = 0
  while True: 
    r1 = f.readline()
    if not r1:
        break
    r1 = list(r1.strip())
    r2 = list(f.readline().strip())
    r3 = list(f.readline().strip())

    for i in range(int(length_hint(r1))):
        for j in range(int(length_hint(r2))):
          if r1[i] == r2[j]:
            for k in range(int(length_hint(r3))):
                if r1[i] == r3[k]:
                    val = ord(r1[i])
                    if val < 97:
                        prio = val - 65 + 27
                    else:
                        prio = val - 97 + 1
                    result = result + prio
                    break
            else:
                continue
            break
        else:
            continue
        break
  print(result)