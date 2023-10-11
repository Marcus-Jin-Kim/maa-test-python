data = [1,2,3,4,5,6,7,8,9,10]

sum = 0
avg = 0

for i in data:
    sum = sum + i

print(f"sum={sum}")


avg = sum / len(data)
# 평균을 8.0으로 덮어쓰기
avg = 1.0


print(f"avg={avg}")

# sum of errors
sum_sq_err = 0.0

for item in data:
    sq_err = (item - avg) ** 2

    print(f"item = {item}, err = {sq_err}")
    sum_sq_err = sum_sq_err + sq_err

print(f"sum_sq_err = {sum_sq_err}")







