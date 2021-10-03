pl_pos = 1
com_pos = 1
def banmen():
    print("・"*(pl_pos-1) + "P" + "・"*(30-pl_pos) + "Goal")
    print("・"*(com_pos-1) + "C" + "・"*(30-com_pos) + "Goal")
while True:
    banmen()
    input("Enterを押すとコマが進む")
    pl_pos = pl_pos +1
    com_pos = com_pos + 2