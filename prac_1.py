#학생의 이름, 전공, 학번 입력받아 출력하기
st_name=input('what is your name?')
st_major=input('what is your major?')
st_id=input('what is your student id?')
st_grade=int(input('what is your grade?'))
#출력하려는 문장
message=f'Hello, {st_id} {st_name}! Your major is {st_major}'
#출력
print(message)
