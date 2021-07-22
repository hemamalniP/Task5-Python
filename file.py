str1=input()
file1=open("/home/root63/Desktop/vowel.txt","r")
str2=file1.read()
if str1 in str2:
	print("TRUE")
else:
	print("FALSE")
file1.close()    
    
