s = input('암호화된 문자열을 입력하세요 :')
mo = ['a','e','i','o']
lst =[]

for i in range(len(s)):
    if (s[i-1] in mo and s[i] =='g') or (s[i] in mo and s[i+1] =='g') :
        #if s[i+1] =='g':
        
        continue 
        
    else:
        lst.append(s[i])
    
print(''.join(lst))


