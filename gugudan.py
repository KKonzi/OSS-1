print("=========1~8단=========\n")
for x in range(1, 9):
    print("------- [" + str(x) + "단] -------")
    for y in range(1, 9):
        print(x, "X", y, "=", x*y)
print("---------------------")