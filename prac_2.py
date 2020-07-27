#while문, 조건문 연습
print('이 프로그램은 점수를 입력하면 성적을 출력해주는 프로그램입니다.')
st_name=''
st_score=4.5
p_again=''

while p_again != 'quit':
    st_name=input('What is your name?')
    message=f'Hi! {st_name}, '
    st_score=float(input('put your score here>>'))
    
    if st_score >= 4.5:
        print('Your score is A+')
    elif (st_score < 4.5) and (st_score >= 4.0):
        print('Your score is A0')
    elif (st_score < 4.0) and (st_score >= 3.5):
        print('Your score is B+')
    elif (st_score < 3.5) and (st_score >= 3.0):
        print('Your score is B0')
    elif (st_score < 3.0) and (st_score >= 2.5):
        print('Your score is C+')
    elif (st_score < 2.5) and (st_score >= 2.0):
        print('Your score is C0')
    elif (st_score < 2.0) and (st_score >= 1.5):
        print('Your score is D+')
    elif (st_score < 1.5) and (st_score >= 1.0):
        print('Your score is D0')
    else:
        print('You fail the class')
    
    p_again=input('''\'quit\' if you want to stop,
    else push any key>>''')
    
    if p_again == 'quit':
        print('program finished')