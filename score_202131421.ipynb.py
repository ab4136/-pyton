from functools import reduce

data = input("1회차 ~ 15회차 점수를 입력해주세요.")

mid = int(input("중간고사 성적을 입력해주세요?"))

fin = int(input("기말고사 성적을 입력해주세요?"))


print(data.split())
a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15 = map(int,data.split())


numbers =  map(int,data.split())

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)


avg = result/15

a = avg * 0.4

b = mid * 0.3

c = fin * 0.3

score = a + b + c
if 100 >= score >= 90:
    grade = "A"
elif 90 > score >= 80:
    grade = "B"
elif 80 > score >= 70:
    grade = "C"
elif 70 > score >= 60:
    grade = "D"
elif score < 60:
    grade = "F"

print(" %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | 평균값  %6.2f | 비중  %6.2f |"
    %(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,result, avg,a))


print("과제 반영점수(40%)" , a, "중간 반영점수(30%)" , b, "기말 반영점수(30%)" , c)


print("성적은" + grade + "입니다.")
1회차 ~ 15회차 점수를 입력해주세요.90 90 90 90 90 90 90 90 90 90 90 90 90 90 90
중간고사 성적을 입력해주세요?90
기말고사 성적을 입력해주세요?90
['90', '90', '90', '90', '90', '90', '90', '90', '90', '90', '90', '90', '90', '90', '90']
  90 |  90 |  90 |  90 |  90 |  90 |  90 |  90 |  90 |  90 |  90 |  90 |  90 |  90 |  90 | 1350 | 평균값   90.00 | 비중   36.00 |
과제 반영점수(40%) 36.0 중간 반영점수(30%) 27.0 기말 반영점수(30%) 27.0
성적은A입니다.
