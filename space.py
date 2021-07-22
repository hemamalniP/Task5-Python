list1=["Apple","","Orange","Banana","","Mango","Watermelon"]
res=[]
for i in list1:
    if i.strip():
        res.append(i)
print(str(res))
