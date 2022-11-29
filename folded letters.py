#Użyj listy składanej, aby stworzyć listę sześcianów (potęgi trzeciej) liczb z zakresu od 1 do 10. 
#Następnie użyj pętli for in, aby zwrócić w konsoli liczby niepodzielne przez 2.

list=[ i**3 for i in range (1,11) if i%2!=0]

print(list)

