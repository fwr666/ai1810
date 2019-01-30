

#   4,算出１００～９９９范围内的水仙花数 Narcissistic Numer
#    水仙花数是指百位的三次方＋十位的三次方＋个位的三次方

for bai in range(1,100):
    for shi in range(0,100):
        for ge in range(0,100):
            print(ge)
            # if bai**3 +shi**3+ge**3 == bai*100 + shi*10 + ge:
            #     print(bai*100 + shi*10 + ge)
