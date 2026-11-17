num = int(input("Enter a number: "))
t = num
numLen = 0
while (t > 0):
    numLen = numLen + 1
    t = int(t / 10)
if numLen >= 4:
    numLen = int(numLen / 2)
    chk = 0
    while (num > 0):
      rem = num % 10
      if chk == numLen:
        midone = rem
      elif (chk == numLen - 1):
        midtwo = rem
      num = int(num / 10)
      chk = chk + 1
    prod = midone * midtwo
    print("\nProduct of the two middle products is: " + str(midone) + " * " + str(midtwo) + " = " + str(prod))
else:
   print("\nThe number does not have a minimum of four digits.")