
# Question 1

def my_func(x1, x2, x3):
    num = [x1, x2, x3]
    check=0
    for i in num:
        if (type(i)) == (int):
            check=1
            return ("Error: parameters should be float")
        if (type(i)) != (float):
            check=1
            return ("None")
    if (x1 + x2 + x3) == 0 and check==0:
        return ("Not a number – denominator equals zero")
    if check==0:
        return ((x1 + x2 + x3) * (x2 + x3) * x3) / (x1 + x2 + x3)


print(my_func(1.0, 2.0, 'a'))



# Question 2

def revword(word:str):
    word=word.lower()[::-1]
    return word

def countword():
    myfile=open('text.txt','r')
    counter=1
    for i in myfile:
        line=i.split()
        if len(line)==1:
            firstword=i.strip()
        for j in line:
            word=revword(j)
            if word==firstword:
                counter=counter+1
    return counter



print(countword())
