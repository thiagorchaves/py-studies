# a = lambda x, y: x + y
# print(a(5,6))
# quadrado = []

# for x in range(1,11):
#     quadrado.append((lambda x: x **2)(x))

# print(quadrado)

print(list(map(lambda x: x **2, range(1,11))))

