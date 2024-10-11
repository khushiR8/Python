def int_num():
    num_list=[]
    for i in range(4):
        n=int(input('enter a number:'))
        num_list.append(n)
    return num_list

def mult(num_list):
    result=1
    for number in num_list:
        result*=number
    return result

numbers=int_num()
product=mult(numbers)
print(f"The product of the numbers is: {product}")
