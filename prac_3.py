#튜플,리스트 연습
book='초보자도 간단히 단숨에 배우는 파이썬',2020, '조인석', '터닝포인트'
stoper='keep'
print(book)
while True:
    x=int(input('제목-1, 출판년도-2, 저자-3, 출판사-4 중 원하는 항목의 번호를 입력하시오'))
    print('요청하신 정보는 ',book[x-1], '입니다')
    stoper=input('그만하고 싶다면 \'quit\'을 입력하시오. 아니면 아무 문자를 입력하시오')
    if stoper == 'quit':
        print('프로그램이 종료되었습니다')
        break
    else:
        continue