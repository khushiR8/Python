import random

def toss_coin(num_tosses):
    head=0
    tail=0
    for i in range(num_tosses):
        toss=random.randint(0,1)
        if toss==1:
            head+=1
        else:
            tail+=1
            
    return head,tail

def main():
    num_tosses=int(input('enter number of tosses:'))
    head,tail=toss_coin(num_tosses)
    
    print(f"Number of heads: {head}")
    print(f"Number of tails: {tail}")  

main()      
       
        
        