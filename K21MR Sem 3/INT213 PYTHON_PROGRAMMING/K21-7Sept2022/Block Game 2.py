t = int(input())
for i in range(t):
    n = input()
    if(str(n) == str(n)[::-1]):
        print("wins")
    else:
        print("loses")