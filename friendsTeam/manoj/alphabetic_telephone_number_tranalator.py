number = input("Enter a telephone number").upper()
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", \
             "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", \
             "W", "X", "Y", "Z"]
numeric = ["2","2","2","3","3","3","4","4","4","5","5","5","6","6","6","7","7","7","7","8","8","8","9","9","9","9"]
xx = ""
for i in number:
    if i == "-":
        xx = xx + "-"
    else:
        if i.isdigit():
            xx = xx + i
        else:
            char = alpha.index(i)
            xx = xx  + numeric[char]
print(xx)
