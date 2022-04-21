def geomprog(m):
    n = 2
    for i in range(m):
        yield n
        n *= 2
gen_iter = geomprog(10)

print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
