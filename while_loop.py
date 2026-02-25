# print num 1 to 5
i=1
while i <=5:
    print(i)
    i=i+1
    
# sum of num take user input 
n = int(input("Enter a number: ")) 
sum = 0
num = 1
while num <= n:
    sum += num  
    num += 1    
print("The sum is:", sum)

#print 1 to 20 in odd number

num = 1
while num <= 20:
    if num % 2 != 0:  
        print(num)
    num += 1  

#print table of 4

num = 1
while num <= 10:
    print(4 * num) 
    num += 1
    

#print revers num 1 to 10 

num = 10
while num >= 1:
    print(num)
    num -= 1
    
#find larzest num in list

numbers = [3, 1, 9, 4, 6, 2]
max_num = numbers[0]
index = 1
while index < len(numbers):
    if numbers[index] > max_num:
        max_num = numbers[index]
    index += 1
print("The largest number is:", max_num)

#print even num between 1 to 20

num = 2
while num <= 20:
    print(num)
    num += 2
