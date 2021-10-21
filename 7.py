S=str(input('Introduceti sirul: '))
print(S)
t=0
for i in S:
    if i=='A':
        t+=1
print('Numarul de aparitii a lui "A"= ',t)
S2=''
for i in S:
    if i=='A':
        S2+='*'
    else:
        S2+=i
print('Sirul obtinut prin substituirea caracterului "A" prin caracterul "*"= ',S2)
S3=''
for i in S:
    if i!='B':
        S3+=i
print('Sirul obtinut prin radierea caracterului "B" = ',S3)
aparitiima=0
for i in range(0,len(S)):
    if (S[i]=='M')and(S[i+1]=='A'):
        aparitiima+=1
print('Numarul de aparitii a silabei "MA"= ',aparitiima)
S4=''
Sc1=S
for i in range(0,len(Sc1)):
    if (S[i]=='M')and(S[i+1]=='A'):
        S4+='TA'
    else:
        S4+=S[i]
print('Sirul obtinut prin substituirea silabei "MA" prin silaba "TA"= ',S4)
S5=''
Sc2=S
for i in range(0,len(Sc2)):
    if (S[i]=='T')and(S[i+1]=='O'):
        S5+=S[i]    
print('Sirul obtinut prin radierea silabei "TO" = ',S5)
print('Sirul scris invers= ',S[::-1])