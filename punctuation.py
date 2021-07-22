punc='''!()-_*&^%$#@!~{}|\/?:;"'<>,.`[]'''
inp=input()
no_punc=" "
for char in inp:
    if char not in punc:
        no_punc=no_punc+char
        
print(no_punc)
