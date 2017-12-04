def divis(line):
    for i, x in enumerate(line):
        for y in line[i+1:]:
            if (x >= y) and (x % y == 0):
                return x // y
            elif (y > x) and (y % x == 0):
                return y // x

if __name__ == "__main__":
    with open("problem2_input.txt") as f:
        inp = list([int(i) for i in line.strip().split(" ")] for line in f.readlines())
    print(sum(max(l) - min(l) for l in inp))
    print(sum(divis(l) for l in inp))
