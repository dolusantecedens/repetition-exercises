#Stwórz nową listę i ją wydrukuj. 
# Nowa lista powinna zawierać tylko liczby pierwsze z poprzedniej listy.



list=[1, 2, 3, 5, 6, 11, 12, 18, 19, 21]

first_num=[]

for i in list:
    x=0
    for a in range(2,i):
        if i%a==0:
            x=1
    if x!=1:
        first_num.append(i)
    if i==1:
        first_num.remove(i)
        
print(first_num)