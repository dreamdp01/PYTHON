a =[1,2,3,4,5,6,7,8,9]
print(a)
print(a[3])

#크기가 N이고, 모든 값이 0인 1차원 리스트 초기화 
n =10
b=[0]*n
print(b)

print(a[-1]) # 뒤에서 첫 번째 원소 출력
print(a[-3]) # 뒤에서 세 번째 원소 출력

a[3] = 7 # 네 번째 원소 값 변경
print(a) # 변경된 값 확인
print(a[1 : 4]) # 문자열과 같이 인덱스/슬라이딩 출력

array = [i for i in range(10)]
print(array)

array = [i for i in range(10) if i %2 ==1] #컴프리헨션 
print(array)

array =[]
for i in range(10):
    if i %2==1:
        array.append(i)
print(array)
#위 리스트 컴프리헨션이 없는 코드 