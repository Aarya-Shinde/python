#fibonacci series 

# eg- [0, 1, 1]
# [0, 1, 1, 2]   
# [0, 1, 1, 2, 3]

inp = 5
series = [0, 1]
for i in range(0, inp - 2) :

    num1 = series[i]
    num2 = series[i + 1]

    num3 = num2 + num1

    series.append(num3)
    print(series)


    


