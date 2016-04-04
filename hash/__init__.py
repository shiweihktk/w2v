def creathash(str1):
    sum=0
    for i in range(0,len(str1),1):
        if ord(str1[i])>255:
            num=ord(str1[i])
            gaowei=int((num&65280)/256)
            sum=sum*255+gaowei
            diwei=num&255
            sum=sum*255+diwei
            print(diwei)
            print(gaowei)
        else:
            sum=sum*255+ord(str1[i])
    return sum
    #hash1=hashlib.md5()
    #hash1.update(str)
    #return int(hash1.hexdigest(),16)
#a='我爱打篮球。'
#b='i like playing game.'
#print(creathash(a))
#print(creathash(b))