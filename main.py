# 1 - m
for i in range(1, 11):
    i *= 1
    print(i)



# 2 - m
royxat = [1, 2, 3, 4, 5, 6, 7, 8]
print(royxat)

for i in royxat:
    i *= 2
    print(i)



# 3 - m
def talaba(ism, familiya, yosh, ball):
    ism = " "
    familiya = " "
    yosh = 0
    ball = 0

    print(f"Ismi: {ism} Familiyasi: {familiya}, yoshi: {yosh} Toplagan bali: {ball}")

res = talaba('Ali', 'Yodgorov', 19, 187)
print(res)



# 4 - m
numbers = [2, 5, 8, 10, 15, 34, 2]
print(numbers)

if numbers % 5 == 0:
    print('5 ga bolinadi')

else:
    print('5 ga bolinmaydi')




# 5 - m
lugat = {
    'ism' : "Ali",
    'yosh': 20,
    'boy': 17.8
}

print(lugat)
