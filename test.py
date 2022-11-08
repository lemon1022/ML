n, m, e = map(int, "5 8 8".split(" "))
v = list(map(int, "2,1,4,3,5".split(",")))
w = list(map(int, "1,4,2,3,5".split(",")))
b = list(map(int, "2,3,5,2,4".split(",")))
w.insert(0,0)
v.insert(0,0)
b.insert(0,0)
# dp = [[[0 for i in range(1000)] for i in range(1000)] for i in range(1000)]