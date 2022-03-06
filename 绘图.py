import matplotlib.pyplot as plt
import numpy as np
from numpy import *


def main():
    fig = plt.figure(figsize=(8,8))
	# 设置x和y的坐标范围
    x1=np.arange(0,15,0.01)#开始，结束，精度
    x2=np.arange(0,15,0.01)
    # 转化为网格
    x1,x2=np.meshgrid(x1,x2)
    x4=x1
    x5=x2



    plt.contour(x1,x2,z,0)#最后一个为0，不然多条线，默认绿色

    plt.contour(x1,x2,z,0,colors=['r'])



    plt.contour(x1,x2,z,0,colors=['b'])

    #plt.contour(x1,x2,z,0,colors=['g'])
    #plt.contour(x1,x2,z,colors=['k', 'k', 'k','r','r'], linestyles=['--','--', '-', '--','--'],levels=[-1,-.5, 0, .5,1])会画5条


    plt.xlabel("x1 mol/kg水", fontproperties='simhei', fontsize=10, color='green')#x轴
    plt.ylabel("x2 mol/kg水", fontproperties='simhei', fontsize=10, color='green')


    #plt.savefig(r'C:/Users/20180124/Desktop/图.png')
    plt.show()





main()


#matlab作图替换元素
# y=input("1")
# y=y.replace("**",".^")
# y=y.replace("/","./")
# y=y.replace("*",".*")
# y=y.replace("x1","x")
# y=y.replace("x2","y")
# y=y.replace("x3","z")
# print(y)
