def nonrepeatingchar(x):
    freq={}
    for i in x:
        freq[i]=freq.get(i,0)+1
    
    for j in x:
        if freq[j]==1:
            return j
        
    return ("No unique element in string")

st=str(input("Enter string: "))
print("The first non repeating character in string is ",nonrepeatingchar(st))