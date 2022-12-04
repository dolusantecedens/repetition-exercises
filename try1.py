


numbers = [5,32,56,2,2,16,7,10,23,100]
mean_number = 0





numbers=[round(i,-1) for i in numbers]
a=0

a=min(numbers)
numbers.remove(a)
b=max(numbers)
numbers.remove(b)

c=sum(numbers)
mean_number=sum(numbers)/len(numbers)

print(mean_number)
