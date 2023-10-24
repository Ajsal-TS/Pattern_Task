#Task is to print pattern
#Total rows can be taken as input


def pattern(row):
    count=0
    k=0
#for top rows
    for i in range(0,int(row/2)):
        for j in range(0,int(row/2)-i+1):
        #for putting space
            print(end=" ")    


        while (count!=(i*2)+1):
            print("*",end="")           #print star without going to new line
            count=count+1

    #for getting top rows max count of no of stars
        k=count
        count=0                        
    #for new line
        print() 

    print(end=" ")        

#for middle line of pattern

    while (count!=k+2):
        print("*",end="")
        count=count+1
    print()

#for bottom rows
#k+2 has the value of no of stars inside middle row.
    count=1

    for i in range(0,int(row/2)):

        for j in range(0,i+2):
            print(end=" ")
        while count<=k:
            print("*",end="")
            count=count+1
        k=k-2
        count=1
        print()

    


if __name__=="__main__":
    rows=int(input("enter the total row no"))  #enter odd no as input
    pattern(rows)

