# 파일이름 :
# 작 성 자 :
name7 = input("이름을 입력하시오: ")
write7 = int(input("당신의 글쓰기 점수를 입력하시오: "))
python7 = int(input("당신의 파이썬 점수를 입력하시오: "))
lastAverage7 = float(input("당신의 지난학기 평균을 입력하시오: "))

average7 = (write7 + python7) / 2
diff7 = average7 - lastAverage7

print(f"\n{name7} 학생의 글쓰기 점수는 {write7}, 파이썬 점수는 {python7}입니다.")
print(f"평균은 {average7}이고. 지난 학기와 차이는 {diff7} 입니다.")
