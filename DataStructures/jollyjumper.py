s = [1, 4, 2, 3]
setjolly = set() 
for i in range(1, len(s)):
    setjolly.add(i)
setdiff = set()
for i in range(len(s) - 1):
    setdiff.add(abs(s[i] - s[i+1]))

if setdiff == setjolly:
    print("Jolly Jumper")
else:
    print("Not Jolly Jumper")

