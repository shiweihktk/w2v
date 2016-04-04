def creathash(str1):
    sum=0
    for i in range(0,len(str1),1):
        if ord(str1[i])>255:
            num=ord(str1[i])
            gaowei=int((num&65280)/256)
            sum=sum*2+gaowei
            diwei=num&255
            sum=sum*2+diwei
            print(diwei)
            print(gaowei)
        else:
            sum=sum*2+ord(str1[i])
        if sum>18446744073709551615:
           sum=sum&1844674407370955165
    return sum
    #hash1=hashlib.md5()
    #hash1.update(str)
    #return int(hash1.hexdigest(),16)
#a='我爱打篮球。阿卡；啊打发了肯德基；啊；就；阿的江；啊打发；付款的叫法地方；阿洛菲啊付款；带上飞机啊；了受到法律是会计法律房间打扫房间阿三啊；来得及伐交到了；放假啊都浪费粮食的肌肤啊放假啊的肌肤；垃圾的身份了；啊就发了；打飞机啊两地分居阿三顶顶；啊煞风景啊算法。'
#b='i like playing game.'
#print(creathash(a))
#print(creathash(b))