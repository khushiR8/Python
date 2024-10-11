def int(i,r=0.07):
    years=0
    cur_val=i
    print('investment:',int)
    while cur_val < i*2:
        cur_val+=cur_val*i
        years+=1
        
    return years

print(f"Years to double the investment (default rate): {int(1000)} years")
print(f"Years to double the investment (5% rate): {int(1000, 0.05)} years")
    
    
    