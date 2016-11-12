#-*-coding:utf-8-*-
__author__ = 'sww16164'
import numpy as np,pandas as pd,uniout
na={'用户A':[{'a':1,'b':1,'c':1}],'用户B':[{'b':2,'c':2,'d':2}],'用户C':[{'a':3,'b':3,'c':3,'f':3}],'用户D':[{'z':4,'x':4,'y':4,'s':4}],'用户E':[{'a':1,'b':2,'c':2}]}
#数字用来代表对产品的喜欢程度，0到5分
data=np.array([na])
class xietong():
    def __init__(self,data):
        #初始化
        self.data=data
    def xiangsidu(self,main,username,ls,username2='用户B'):
        #计算相似度
        fenzi=0
        A=0
        B=0
        if type(ls).__name__ =='list':
            for goods in ls:
                fenzi=fenzi+self.data[0][username][0].get(goods,0)*self.data[0][username2][0].get(goods,0)
                A=A+self.data[0][username][0].get(goods,0)**2
                #计算A的模
                B=B+self.data[0][username2][0].get(goods,0)**2
                #计算B的模
        if A*B !=0:
            return fenzi/((A**(1.0/2))*(B**(1.0/2)))
        else:
            return  0
        pass
    def tuisong(self,username):
        #输入姓名猜测他喜欢的线路
        tuijian=[['用户1','用户2','相似度','物品']]
        for username2 in self.data[0].keys():
             if username2!=username:
                lsA=self.data[0][username][0].keys()#A的物品list
                lsB=self.data[0][username2][0].keys()#B的物品list
                lsCHA=list(set(lsB).difference(set(lsA)))#返回两个用户购买物品的差集,B买了，但A没买
                if len(lsCHA)>0:
                    ls=lsA+lsB
                    ls = list(set(ls))#出去重复商品
                    xsd=self.xiangsidu(self,username,ls,username2)#计算相似度
                    lsT=[[username,username2,xsd,lsCHA[0]]]
                    tuijian=tuijian+lsT
        tuijian.sort(key=lambda x:x[2],reverse=True)#按相似度降序排序
        print '和用户：',username,'相似度最高的是：',tuijian[1][1],'相似度',tuijian[1][2],'推荐物品:',tuijian[1][3]
        pass
if  __name__=='__main__':
    a=xietong(data)
    print a.tuisong('用户D')#这里改用户就好了