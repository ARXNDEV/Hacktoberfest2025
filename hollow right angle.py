N = int(input())

star = "*"

for i in range(1, N + 1):
    if i == 1:
        print(star)
    elif i < N:
        line = star + " " + "  " * (i - 2) + star
        print(line)
    else:
        line = " ".join([star] * N)
        print(line)
