s1=input("Enter the first string: ")
s2=input("Enter the second string: ")
s3=set(s1)
s4=set(s2)
if (len(s1)==len(s2)) and (s3==s4):
    print(True)
else:
    print(False)