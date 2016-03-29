import os
import random
class word(object):
    degree=0
    bianhao=0#词语序号，用于索引
    word=''
    codelen=0#char
    def __init__(self):
        self.point=[]#nt
        self.code1=[]
        self.vec=[]
def creattree(word):
    binary=[]
    count=[]
    parent_node=[]
    code=[]
    point=[]
    for i in range(40):
        code.append('')
        point.append(0)
    for i in range(2*len(word)+1):
        binary.append(0)
        parent_node.append(0)
        count.append(0)
    for i in range(len(word)):
        count[i]=int(word[i].degree)
        count[i+len(word)]=1e15
    pos1 = len(word) - 1
    pos2 = len(word)
    #Following algorithm constructs the Huffman tree by adding one node at a time
    for i in range(len(words)-1):
        # First, find two smallest nodes 'min1, min2'
        if pos1>=0:
            if count[pos1]<count[pos2]:
                min1i = pos1
                pos1=pos1-1
            else:
                min1i = pos2
                pos2=pos2+1
        else:
            min1i = pos2
            pos2=pos2+1
        if pos1>=0:
           if count[pos1]<count[pos2]:
                min2i = pos1
                pos1=pos1-1
           else:
                min2i = pos2
                pos2=pos2+1
        else:
            min2i = pos2
            pos2=pos2+1
        count[len(word) + i] = count[min1i] + count[min2i]
        parent_node[min1i] = len(word) + i
        parent_node[min2i] = len(word) + i
        binary[min2i] = 1
    # Now assign binary code to each vocabulary word
    for a in range(len(word)):
        b = a
        i = 0
        while 1:
            code[i]=binary[b]
            point[i]=b
            i=i+1
            b=parent_node[b]
            if b==(len(word)*2-2):
                break
        words[a].codelen = i
    #    words[a].point[0]=len(words)-2
        for b in range(i):
            word[a].code1.insert(0,code[b])
            word[a].point.insert(0,point[b]-len(words))
    del(count)
    del(binary)
    del(parent_node)
    return word
def creatindex(cishu1,cishu2,words):
    for i in range(cishu1):
        for xunhuan in range(cishu2):
            if words[xunhuan].degree<words[xunhuan+1].degree:
                tempw=words[xunhuan].word
                words[xunhuan].word=words[xunhuan+1].word
                words[xunhuan+1].word=tempw
                tempi=words[xunhuan].degree
                words[xunhuan].degree=words[xunhuan+1].degree
                words[xunhuan+1].degree=tempi
        cishu2-=1
    if i%100==0:
        print(i)
def vec_default(a,size):
    for i in range(size):
        a[i]=(random.random()-0.5)/size
    return a
def net_default(a,size,voc_size):
    for i in range(voc_size):
        for b in range(size):
            a[i][b]=0
    return a
def createindextable(words):#创建词索引表，调用该函数传入词对象列表返回table列表
    table = []
    i = 0
    a = 0
    for a in range(len(words)):
        table.append('')
    for i in range(len(words)):
        wordhash = hash(words[i])
        ind = wordhash % len(words)
        if table[ind] == '':
            temp=['','']
            temp[0] = words[i]
            temp[1] = i
            table[ind] = temp
            continue
        while 1:
            ind = ind + 1
            if ind == len(words):
                ind = 0
            if table[ind] != '':
                continue
            else:
                temp=['','']
                temp[0] = words[i]
                temp[1] = i
                table[ind] = temp

                break
    return table
fin=open('G:\\新建文件夹\\程序\\word2vec_wanwei版\\degreesum\\zongbiao.txt','r')
strfile=fin.read()
strline=strfile.split('\n')
hangshu=len(strline)
strword=[]
words=[]
for i in range(hangshu):
    strword.append(strline[i].split('\t'))
    words.append(word())
for i in range(hangshu-1):
    words[i].word=strword[i][0]
    if strword[i][1]=='':
        words[i].degree=0
    else:
        words[i].degree=int(strword[i][1])
del(strword)
cishu1=len(words)-1
cishu2=len(words)-1
creatindex(cishu1,cishu2,words)
fout=open('G:\\新建文件夹\\程序\\word2vec_wanwei版\\w2v\\jieguo.txt','w')
creattree(words)
for c in range(len(words)):
    t=str(words[c].code1[0:words[c].codelen])
    fout.write(words[c].word+'\t'+str(words[c].codelen)+'\t'+t+'\t'+'\n')