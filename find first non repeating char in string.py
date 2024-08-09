def nonrepeatingchar(x):
    freq={}
    for i in x:
        freq[i]=freq.get(i,0)+1
    
    for j in x:
        if freq[j]==1:
            return j
        
    return -1

st=str(input("Enter string: "))
index=nonrepeatingchar(st)
if index==-1:
    print("No non repeating character in the string")
else:
    print("The first non repeating character in string is ",str(index))
