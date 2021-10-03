import random
pl_pos = 1
com_pos = 1
def banmen():
    print("・"*(pl_pos-1) + "P" + "・"*(30-pl_pos) + "Goal")
    print("・"*(com_pos-1) + "C" + "・"*(30-com_pos) + "Goal")
banmen()
print("Start")
while True:
# あなたのコマ
    input("Enterを押すとあなたのコマが進みます")
    rp = random.randint(1,6)
    pl_pos = pl_pos + rp
    print("あなたのサイコロの目は"+str(rp))
    if pl_pos > 30:
        pl_pos = 30
    banmen()
    if pl_pos == 30:
        print("あなたの勝ちです")
        break
# コンピュータのコマ
    input("Enterを押すとコンピュータのコマが進みます")
    rc = random.randint(1,6)
    com_pos = com_pos + rc
    print("コンピュータのサイコロの目は"+str(rc))
    if com_pos > 30:
        com_pos = 30
    banmen()
    if com_pos == 30:
        print("コンピュータの勝ちです")
        break