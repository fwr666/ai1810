height = float(input("请输入身高(单位:米)"))
weight = float(input("请输入体重(单位:公斤)"))
BMI = weight / height ** 2
if BMI < 18.5:
    print(" BMI < 18.5       体重过轻",BMI)
elif 18.5 <= BMI <24:
    print("18.5 <= BMI < 24 正常范围",BMI) 
elif BMI >= 24:
    print("BMI >= 24        体重过重",BMI)