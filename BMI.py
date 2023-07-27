M = input('輸入體重: ')
H = input('輸入身高(單位:公尺): ')
M = float(M)
H = float(H)
BMI = M / (H * H)
print(BMI)
if BMI < 18.5 :
    print('體重過輕')
elif BMI >= 18.5 and BMI < 24 :
    print('體重正常')
elif BMI >= 24 and BMI < 27 :
    print('體重過重')
elif BMI >= 27 and BMI < 30 :
    print('輕度肥胖')
elif BMI >= 30 and BMI < 35 :
    print('中度肥胖')
else :
    print('重度肥胖')