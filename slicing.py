#Dana jest lista: [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0].
#Zadeklaruj ją w Pythonie, utwórz liste która nie zawiera innych liczb niz równe zero.
#Potem użyj tej samej techniki do zwrócenia listy, 
#która zawiera wszystkie inne liczby tylko nie zera z tej kolekcji.


list=[2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]

list2=[]
list2=[ i for i in list if i==0]
print(list2)

list3=[]

list3=[ i for i in list if i>=1]

print(list3)