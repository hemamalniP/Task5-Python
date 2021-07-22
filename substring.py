def string(str1, delim):
    word = ""
    num = 0
    str1 += delim
    l = len(str1)
    list1 = []
    for i in range(l):
        if (str1[i] != delim):
            word += str1[i]
 
        else:
            if (len(word) != 0):
                list1.append(word)
            word = ""
  
    return list1
 

if __name__ == '__main__':
    str = input()
    delim = ','
 
    res = string(str, delim)
    for x in range(len(res)):
        print(res[x])
