import pitzer
from tkinter import *
import sympy
x1, x2,x3,x4,x5,x6= sympy.symbols('x1, x2,x3,x4,x5,x6')  # 声明符号变量，否则会认为没有定义

x=[x1, x2,x3,x4,x5,x6]
func_1=[1]#v1或者v2
root= Tk()
root.title('基于Pitzer模型的水盐相图计算程序 V1.0')
root.geometry('500x640') # 小写英文字母 x

lm=[]#名称
lx=[]
wd=[25]#温度
llm=[]#存价态
llx=[]#存价态
lllm=[]#重摩尔浓度
lllx=[]#重摩尔浓度
def run1():
     a = inp1.get()
     txt.insert(END, '输入%s\n'%a)
     lm.append(a)
     a = x[0]
     txt.insert(END, '输入%s\n'%a)
     lllm.append(a)
def run2():
     b = inp2.get()
     txt.insert(END, '输入%s\n'%b)
     lm.append(b)
     b = x[1]
     txt.insert(END, '输入%s\n'%b)
     lllm.append(b)
def run3():
     c = inp3.get()
     txt.insert(END, '输入%s\n'%c)
     lm.append(c)
     c = x[2]
     txt.insert(END, '输入%s\n'%c)
     lllm.append(c)
def run4():
     d = inp4.get()
     txt.insert(END, '输入%s\n'%d)
     lx.append(d)
     d = x[3]
     txt.insert(END, '输入%s\n'%d)
     lllx.append(d)
def run5():
     e = inp5.get()
     txt.insert(END, '输入%s\n'%e)
     lx.append(e)
     e = x[4]
     txt.insert(END, '输入%s\n'%e)
     lllx.append(e)
def run6():
     f = inp6.get()
     txt.insert(END, '输入%s\n'%f)
     lx.append(f)
     f = x[5]
     txt.insert(END, '输入%s\n'%f)
     lllx.append(f)
def run7():
     g = inp7.get()
     txt.insert(END, '输入%s\n'%g)
     wd[0]=int(g)

lb1 = Label(root, text='阳离子及初始浓度')
lb1.place(relx=0.05, rely=0, relwidth=0.3, relheight=0.1)
lb2 = Label(root, text='阴离子及初始浓度')
lb2.place(relx=0.55, rely=0, relwidth=0.3, relheight=0.1)
lb3 = Label(root, text='离子全部不带电荷小写输入\n没有则不输入')
lb3.place(relx=0.25, rely=0.4, relwidth=0.45, relheight=0.15)
lb4 = Label(root, text='离子\n\n初始浓度')
lb4.place(relx=0.8, rely=0.1, relwidth=0.3, relheight=0.1)
lb5 = Label(root, text='温度默认25℃')
lb5.place(relx=0.3, rely=0, relwidth=0.3, relheight=0.1)

inp1 = Entry(root)
inp1.place(relx=0.05, rely=0.1, relwidth=0.1, relheight=0.05)
btn1 = Button(root, text='输入', command=run1)
btn1.place(relx=0.05, rely=0.2, relwidth=0.1, relheight=0.05)

inp2 = Entry(root)
inp2.place(relx=0.15, rely=0.1, relwidth=0.1, relheight=0.05)
btn2 = Button(root, text='输入', command=run2)
btn2.place(relx=0.15, rely=0.2, relwidth=0.1, relheight=0.05)

inp3 = Entry(root)
inp3.place(relx=0.25, rely=0.1, relwidth=0.1, relheight=0.05)
btn3 = Button(root, text='输入', command=run3)
btn3.place(relx=0.25, rely=0.2, relwidth=0.1, relheight=0.05)

inp4 = Entry(root)
inp4.place(relx=0.55, rely=0.1, relwidth=0.1, relheight=0.05)
btn4 = Button(root, text='输入', command=run4)
btn4.place(relx=0.55, rely=0.2, relwidth=0.1, relheight=0.05)

inp5 = Entry(root)
inp5.place(relx=0.65, rely=0.1, relwidth=0.1, relheight=0.05)
btn5 = Button(root, text='输入', command=run5)
btn5.place(relx=0.65, rely=0.2, relwidth=0.1, relheight=0.05)

inp6 = Entry(root)
inp6.place(relx=0.75, rely=0.1, relwidth=0.1, relheight=0.05)
btn6 = Button(root, text='输入', command=run6)
btn6.place(relx=0.75, rely=0.2, relwidth=0.1, relheight=0.05)

inp7 = Entry(root)
inp7.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.05)
btn7 = Button(root, text='输入温度/℃', command=run7)
btn7.place(relx=0.375, rely=0.2, relwidth=0.15, relheight=0.05)




#在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框
txt = Text(root)
txt.place(relx=0, rely=0.6, relwidth=1, relheight=0.4)
#检查项
def out():
    print(' 阳离子为',lm,'初始浓度为',lllm,'\n','阴离子为',lx,'初始浓度为',lllx,'\n','温度为',wd[0])
Button(root,text='确认输入',command=out).place(relx=0.4, rely=0.3, relwidth=0.1, relheight=0.05)
#进入计算
def js():
     txt.insert(END, '输入固相\n')
     root.destroy()
Button(root,text='输入固相',command=js).place(relx=0.4, rely=0.36, relwidth=0.1, relheight=0.05)

root.mainloop()


#2轮
jstj=[]
vm=len(lm)
vx=len(lx)
v=vm+vx
t=wd[0]
jt=pitzer.jt
if t==25:
     Ay=pitzer.Ay_25
     pitzer11=pitzer.pitzer11_25
     OZYL=pitzer.OZYL_25
     OZYLCYy=pitzer.OZYLCYy_25
     phcs=pitzer.phcs_25
elif t==0:
     Ay=pitzer.Ay_0
     pitzer11=pitzer.pitzer11_0
     OZYL=pitzer.OZYL_0
     OZYLCYy=pitzer.OZYLCYy_0
     phcs=pitzer.phcs_0
elif t==15:
     Ay=pitzer.Ay_15
     pitzer11=pitzer.pitzer11_15
     OZYL=pitzer.OZYL_15
     OZYLCYy=pitzer.OZYLCYy_15
     phcs=pitzer.phcs_15
elif t==35:
     Ay=pitzer.Ay_35
     pitzer11=pitzer.pitzer11_35
     OZYL=pitzer.OZYL_35
     OZYLCYy=pitzer.OZYLCYy_35
     phcs=pitzer.phcs_35
elif t==50:
     Ay=pitzer.Ay_50
     pitzer11=pitzer.pitzer11_50
     OZYL=pitzer.OZYL_50
     OZYLCYy=pitzer.OZYLCYy_50
     phcs=pitzer.phcs_50

else :
     print('温度未录入')
zmin=999999999
for i in range(vm):
    llm.append(jt[lm[i]])
for i in range(vx):
    llx.append(jt[lx[i]])
#现阶段为2-1
gx1=[]#平衡时固相组成
gx2=[]
gx3=[]
gx4=[]
gxsl1=[]#平衡时固相组成
gxsl2=[]
gxsl3=[]
gxsl4=[]
root1= Tk()
root1.title('基于Pitzer模型的水盐相图计算程序 V1.0')
root1.geometry('500x640') # 小写英文字母 x

def run1():
     a = inp1.get()
     b = inp2.get()
     c = inp3.get()
     d = inp4.get()
     e = inp5.get()
     f = inp51.get()
     g=inp52.get()
     h=inp53.get()
     i=inp54.get()
     j=inp55.get()
     txt.insert(END, '固相1已输入\n')
     gx1.append(a)
     gx1.append(b)
     gx1.append(c)
     gx1.append(d)
     gx1.append(e)
     gxsl1.append(f)
     gxsl1.append(g)
     gxsl1.append(h)
     gxsl1.append(i)
     gxsl1.append(j)
def run2():
     a = inp11.get()
     b = inp12.get()
     c = inp13.get()
     d = inp14.get()
     e = inp15.get()
     f = inp511.get()
     g=inp512.get()
     h=inp513.get()
     i=inp514.get()
     j=inp515.get()
     txt.insert(END, '固相2已输入\n')
     gx2.append(a)
     gx2.append(b)
     gx2.append(c)
     gx2.append(d)
     gx2.append(e)
     gxsl2.append(f)
     gxsl2.append(g)
     gxsl2.append(h)
     gxsl2.append(i)
     gxsl2.append(j)
def run3():
     a = inp21.get()
     b = inp22.get()
     c = inp23.get()
     d = inp24.get()
     e = inp25.get()
     f = inp521.get()
     g=inp522.get()
     h=inp523.get()
     i=inp524.get()
     j=inp525.get()
     txt.insert(END, '固相3已输入\n')
     gx3.append(a)
     gx3.append(b)
     gx3.append(c)
     gx3.append(d)
     gx3.append(e)
     gxsl3.append(f)
     gxsl3.append(g)
     gxsl3.append(h)
     gxsl3.append(i)
     gxsl3.append(j)
def run4():
     a = inp31.get()
     b = inp32.get()
     c = inp33.get()
     d = inp34.get()
     e = inp35.get()
     f = inp531.get()
     g=inp532.get()
     h=inp533.get()
     i=inp534.get()
     j=inp535.get()
     txt.insert(END, '固相4已输入\n')
     gx4.append(a)
     gx4.append(b)
     gx4.append(c)
     gx4.append(d)
     gx4.append(e)
     gxsl4.append(f)
     gxsl4.append(g)
     gxsl4.append(h)
     gxsl4.append(i)
     gxsl4.append(j)
def run5():
    a = inp131.get()
    txt.insert(END, '计算方式已输入\n')
    jstj.append(int(a))
lb1 = Label(root1, text='输入平衡固相离子组成\n没有则留空,每个输入都要点，水输入h2o')
lb1.place(relx=0.35, rely=0, relwidth=0.5, relheight=0.05)
lb2= Label(root1, text='固相1')
lb2.place(relx=0, rely=0.1, relwidth=0.1, relheight=0.05)
lb222= Label(root1, text='个数')
lb222.place(relx=0, rely=0.15, relwidth=0.1, relheight=0.04)
lb223= Label(root1, text='个数')
lb223.place(relx=0, rely=0.25, relwidth=0.1, relheight=0.04)
lb224= Label(root1, text='个数')
lb224.place(relx=0, rely=0.35, relwidth=0.1, relheight=0.04)
lb225= Label(root1, text='个数')
lb225.place(relx=0, rely=0.45, relwidth=0.1, relheight=0.04)
lb3 = Label(root1, text='离子1')
lb3.place(relx=0.1, rely=0.05, relwidth=0.1, relheight=0.05)
lb4 = Label(root1, text='离子2')
lb4.place(relx=0.2, rely=0.05, relwidth=0.1, relheight=0.05)
lb5 = Label(root1, text='离子3')
lb5.place(relx=0.3, rely=0.05, relwidth=0.1, relheight=0.05)
lb6 = Label(root1, text='离子4')
lb6.place(relx=0.4, rely=0.05, relwidth=0.1, relheight=0.05)
lb7 = Label(root1, text='H2O')
lb7.place(relx=0.5, rely=0.05, relwidth=0.1, relheight=0.05)
lb12= Label(root1, text='固相2')
lb12.place(relx=0, rely=0.2, relwidth=0.1, relheight=0.05)
lb22= Label(root1, text='固相3')
lb22.place(relx=0, rely=0.3, relwidth=0.1, relheight=0.05)
lb32= Label(root1, text='固相4')
lb32.place(relx=0, rely=0.4, relwidth=0.1, relheight=0.05)
lb132= Label(root1, text='计算方式')
lb132.place(relx=0.8, rely=0.3, relwidth=0.1, relheight=0.05)


inp1 = Entry(root1)
inp1.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.05)
inp2 = Entry(root1)
inp2.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05)
inp3 = Entry(root1)
inp3.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.05)
inp4 = Entry(root1)
inp4.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.05)
inp5 = Entry(root1)
inp5.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.05)
inp11 = Entry(root1)
inp11.place(relx=0.1, rely=0.2, relwidth=0.1, relheight=0.05)
inp12 = Entry(root1)
inp12.place(relx=0.2, rely=0.2, relwidth=0.1, relheight=0.05)
inp13 = Entry(root1)
inp13.place(relx=0.3, rely=0.2, relwidth=0.1, relheight=0.05)
inp14 = Entry(root1)
inp14.place(relx=0.4, rely=0.2, relwidth=0.1, relheight=0.05)
inp15 = Entry(root1)
inp15.place(relx=0.5, rely=0.2, relwidth=0.1, relheight=0.05)
inp21 = Entry(root1)
inp21.place(relx=0.1, rely=0.3, relwidth=0.1, relheight=0.05)
inp22 = Entry(root1)
inp22.place(relx=0.2, rely=0.3, relwidth=0.1, relheight=0.05)
inp23 = Entry(root1)
inp23.place(relx=0.3, rely=0.3, relwidth=0.1, relheight=0.05)
inp24 = Entry(root1)
inp24.place(relx=0.4, rely=0.3, relwidth=0.1, relheight=0.05)
inp25 = Entry(root1)
inp25.place(relx=0.5, rely=0.3, relwidth=0.1, relheight=0.05)
inp31 = Entry(root1)
inp31.place(relx=0.1, rely=0.4, relwidth=0.1, relheight=0.05)
inp32 = Entry(root1)
inp32.place(relx=0.2, rely=0.4, relwidth=0.1, relheight=0.05)
inp33 = Entry(root1)
inp33.place(relx=0.3, rely=0.4, relwidth=0.1, relheight=0.05)
inp34 = Entry(root1)
inp34.place(relx=0.4, rely=0.4, relwidth=0.1, relheight=0.05)
inp35 = Entry(root1)
inp35.place(relx=0.5, rely=0.4, relwidth=0.1, relheight=0.05)

inp51 = Entry(root1)
inp51.place(relx=0.1, rely=0.15, relwidth=0.1, relheight=0.04)
inp52 = Entry(root1)
inp52.place(relx=0.2, rely=0.15, relwidth=0.1, relheight=0.04)
inp53 = Entry(root1)
inp53.place(relx=0.3, rely=0.15, relwidth=0.1, relheight=0.04)
inp54 = Entry(root1)
inp54.place(relx=0.4, rely=0.15, relwidth=0.1, relheight=0.04)
inp55 = Entry(root1)
inp55.place(relx=0.5, rely=0.15, relwidth=0.1, relheight=0.04)
inp511 = Entry(root1)
inp511.place(relx=0.1, rely=0.25, relwidth=0.1, relheight=0.04)
inp512 = Entry(root1)
inp512.place(relx=0.2, rely=0.25, relwidth=0.1, relheight=0.04)
inp513 = Entry(root1)
inp513.place(relx=0.3, rely=0.25, relwidth=0.1, relheight=0.04)
inp514 = Entry(root1)
inp514.place(relx=0.4, rely=0.25, relwidth=0.1, relheight=0.04)
inp515 = Entry(root1)
inp515.place(relx=0.5, rely=0.25, relwidth=0.1, relheight=0.04)
inp521 = Entry(root1)
inp521.place(relx=0.1, rely=0.35, relwidth=0.1, relheight=0.04)
inp522 = Entry(root1)
inp522.place(relx=0.2, rely=0.35, relwidth=0.1, relheight=0.04)
inp523 = Entry(root1)
inp523.place(relx=0.3, rely=0.35, relwidth=0.1, relheight=0.04)
inp524 = Entry(root1)
inp524.place(relx=0.4, rely=0.35, relwidth=0.1, relheight=0.04)
inp525 = Entry(root1)
inp525.place(relx=0.5, rely=0.35, relwidth=0.1, relheight=0.04)
inp531 = Entry(root1)
inp531.place(relx=0.1, rely=0.45, relwidth=0.1, relheight=0.04)
inp532 = Entry(root1)
inp532.place(relx=0.2, rely=0.45, relwidth=0.1, relheight=0.04)
inp533 = Entry(root1)
inp533.place(relx=0.3, rely=0.45, relwidth=0.1, relheight=0.04)
inp534 = Entry(root1)
inp534.place(relx=0.4, rely=0.45, relwidth=0.1, relheight=0.04)
inp535 = Entry(root1)
inp535.place(relx=0.5, rely=0.45, relwidth=0.1, relheight=0.04)
inp131 = Entry(root1)
inp131.place(relx=0.8, rely=0.35, relwidth=0.1, relheight=0.04)

btn1 = Button(root1, text='输入', command=run1)
btn1.place(relx=0.6, rely=0.12, relwidth=0.1, relheight=0.05)
btn2 = Button(root1, text='输入', command=run2)
btn2.place(relx=0.6, rely=0.22, relwidth=0.1, relheight=0.05)
btn3 = Button(root1, text='输入', command=run3)
btn3.place(relx=0.6, rely=0.31, relwidth=0.1, relheight=0.05)
btn4 = Button(root1, text='输入', command=run4)
btn4.place(relx=0.6, rely=0.42, relwidth=0.1, relheight=0.05)
btn5 = Button(root1, text='输入', command=run5)
btn5.place(relx=0.8, rely=0.42, relwidth=0.1, relheight=0.05)

txt = Text(root1)
txt.place(relx=0, rely=0.6, relwidth=1, relheight=0.4)

def js():
     txt.insert(END, '开始计算\n')
     func_1[0]=int(1)
     root1.destroy()

def tj():
    func_1[0]=2
    root1.destroy()
Button(root1,text='开始计算',command=js).place(relx=0.4, rely=0.5, relwidth=0.1, relheight=0.05)
Button(root1,text='图解',command=tj).place(relx=0.8, rely=0.5, relwidth=0.1, relheight=0.05)
root1.mainloop()

for i in range(5):
    if gx1[4-i]=='':
        gx1.remove('')
    if gx2[4-i]=='':
        gx2.remove('')
    if gx3[4-i]=='':
        gx3.remove('')
    if gx4[4-i]=='':
        gx4.remove('')
    if gxsl1[4-i]=='':
        gxsl1.remove('')
    if gxsl2[4-i]=='':
        gxsl2.remove('')
    if gxsl3[4-i]=='':
        gxsl3.remove('')
    if gxsl4[4-i]=='':
        gxsl4.remove('')

xgx=[]#除空白
xgxsl=[]
def qw():
    if gx1!=[]:
        xgx.append(gx1)
    if gx2!=[]:
        xgx.append(gx2)
    if gx3!=[]:
        xgx.append(gx3)
    if gx4!=[]:
        xgx.append(gx4)
def ww():
    if gxsl1!=[]:
        xgxsl.append(gxsl1)
    if gxsl2!=[]:
        xgxsl.append(gxsl2)
    if gxsl3!=[]:
        xgxsl.append(gxsl3)
    if gxsl4!=[]:
        xgxsl.append(gxsl4)
qw()
ww()
print('固相',xgx)
print('对应数量',xgxsl)
xxx=[0,0,0]#平衡阳浓度
yyy=[0,0,0]
kkk=[]#平衡K




def ys(vm,vx):
            z=0.0000
            for i in range(vm):
                z+=lllm[i]*llm[i]
            for j in range(vx-1):
                z-=llx[j]*lllx[j]
            lllx[vx-1]=z/llx[vx-1]#最后阴离子浓度由计算得
            F=0.000
            I=0.000000
            for i in range(vm) :
                I+=0.5*lllm[i]*llm[i]*llm[i]
            for i in range(vx) :
                I+=0.5*lllx[i]*llx[i]*llx[i]
            #print('溶液离子强度为',I)
            sI=sympy.sqrt(I)
            e1=sympy.exp(-2*sI)
            Z=0.0000000
            for i in range(vm):
                 Z+=llm[i]*lllm[i]
            for i in range(vx):
                Z+=llx[i]*lllx[i]
            #print(Z)
            def g(x):
                gx=2*(1-(1+x)*sympy.exp(-x))/x/x
                return gx
            def g1(x):
                g1x=-2*(1-(1+x+x*x/2)*sympy.exp(-x))/x/x
                return g1x
            gs=vm*vx
            fenzi=[]#存放化合物
            By=[]#存放化合物 第二维里系数By
            B=[]#存放化合物 第二维里系数B
            B11=[]#存放化合物 第二维里系数B导数
            lzph=[]#存放离子配合ij
            WL1XSy=[]#存放离子 第二维里系数
            WL2XS=[]#存放离子 第二维里系数
            WL3XS11=[]#存放离子 第二维里系数倒数
            for i in range(vm):
                for j in range(vx):
                    fzs=lm[i]+lx[j]
                    fenzi.append(fzs)
                    if llm[i]==2 & llx[j]==2:
                        a1=1.4
                        a2=12
                        B0=pitzer11[fzs][0]
                        B1=pitzer11[fzs][1]
                        C=pitzer11[fzs][2]
                        B2=pitzer11[fzs][3]
                        By.append(B0+B1*sympy.exp(-a1*sI)+B2*sympy.exp(-a2*sI))
                        B.append(B0+B1*g(a1*sI)+B2*g(a2*sI))
                        B11.append(B1*g1(a1*sI)/I+B2*g1(a2*sI)/I)
                        F+=(B1*g1(a1*sI)+B2*g1(a2*sI))/I*lllm[i]*lllx[j]
                    else:
                        a1=2
                        B0=pitzer11[fzs][0]
                        B1=pitzer11[fzs][1]
                        C=pitzer11[fzs][2]
                        By.append(B0+B1*sympy.exp(-a1*sI))
                        B.append(B0+B1*g(a1*sI))
                        B11.append(B1*g1(a1*sI)/I)
                        F+=B1*g1(a1*sI)/I*lllm[i]*lllx[j]

            F+=-Ay*(sI/(1+1.2*sI)+2/1.2*sympy.log((1+1.2*sI)))

            #不同的同号离子间有O作用
            for i in range(vm):
                for j in range(vm):
                    if j>i:
                        lzij=lm[i]+lm[j]
                        lzph.append(lzij)
                        lzij=lm[j]+lm[i]
                        lzph.append(lzij)
                        if llm[i]==llm[j]:
                          EOij=0
                          EOij1=0
                        else:
                          def J(x):
                             return x/(4+4.581*(x**(-0.7237))*sympy.exp(-0.012*(x**0.528)))
                          def J1(x):
                             return (4+4.581*(x**-0.7237)*sympy.exp(-0.012*(x**0.528)))**(-1)+((4+4.581*(x**-0.7237)*sympy.exp(-0.012*(x**0.528)))**(-2))*(4.581*x*sympy.exp(-0.012*(x**0.528))*(0.7237*(x**(-1-0.7237))+0.012*0.528*(x**(0.528-1))*(x**-0.7237)))
                          #J与J’查表JJ'，公式不用
                          Xij=6*llm[i]*llm[j]*Ay*sI
                          Jij=J(Xij)
                          Jij1=J1(Xij)

                          Xii=6*llm[i]*llm[i]*Ay*sI
                          Jii=J(Xii)
                          Jii1=J1(Xii)

                          Xjj=6*llm[j]*llm[j]*Ay*sI
                          Jjj=J(Xjj)
                          Jjj1=J1(Xjj)

                          EOij=llm[i]*llm[j]/4/I*(Jij-Jii/2-Jjj/2)
                          EOij1=-EOij/I+llm[i]*llm[j]/8/I/I*(Xij*Jij1-Xii*Jii1/2-Xjj*Jjj1/2)
                        #print('%s与%s的EOij与EOij’为'%(lm[i],lm[j]),EOij,EOij1)
                        WL1XSy.append(OZYL[lm[i]+lm[j]][0]+EOij+I*EOij1)
                        WL2XS.append(EOij+OZYL[lm[i]+lm[j]][0])
                        WL3XS11.append(EOij1)
                        WL1XSy.append(OZYL[lm[i]+lm[j]][0]+EOij+I*EOij1)
                        WL2XS.append(EOij+OZYL[lm[i]+lm[j]][0])
                        WL3XS11.append(EOij1)
                        F+=lllm[i]*lllm[j]*EOij1
            for i in range(vx):
                for j in range(vx):
                    if j>i:
                        lzij=lx[i]+lx[j]
                        lzph.append(lzij)
                        lzij=lx[j]+lx[i]
                        lzph.append(lzij)
                        if llx[i]==llx[j]:
                          EOij=0
                          EOij1=0
                        else:
                          def J(x):
                             return x/(4+4.581*(x**(-0.7237))*sympy.exp(-0.012*(x**0.528)))
                          def J1(x):
                             return (4+4.581*(x**-0.7237)*sympy.exp(-0.012*(x**0.528)))**(-1)+((4+4.581*(x**-0.7237)*sympy.exp(-0.012*(x**0.528)))**(-2))*(4.581*x*sympy.exp(-0.012*(x**0.528))*(0.7237*(x**(-1-0.7237))+0.012*0.528*(x**(0.528-1))*(x**-0.7237)))
                        #J与J’用公式
                          Xij=6*llx[i]*llx[j]*Ay*sI
                          Jij=J(Xij)
                          Jij1=J1(Xij)

                          Xii=6*llx[i]*llx[i]*Ay*sI
                          Jii=J(Xii)
                          Jii1=J1(Xii)

                          Xjj=6*llx[j]*llx[j]*Ay*sI
                          Jjj=J(Xjj)
                          Jjj1=J1(Xjj)

                          EOij=llx[i]*llx[j]/4/I*(Jij-Jii/2-Jjj/2)
                          EOij1=-EOij/I+llx[i]*llx[j]/8/I/I*(Xij*Jij1-Xii*Jii1/2-Xjj*Jjj1/2)
                        #print('%s与%s的EOij与EOij’为'%(lx[i],lx[j]),EOij,EOij1)
                        WL1XSy.append(OZYL[lx[i]+lx[j]][0]+EOij+I*EOij1)
                        WL2XS.append(EOij+OZYL[lx[i]+lx[j]][0])
                        WL3XS11.append(EOij1)
                        WL1XSy.append(OZYL[lx[i]+lx[j]][0]+EOij+I*EOij1)
                        WL2XS.append(EOij+OZYL[lx[i]+lx[j]][0])
                        WL3XS11.append(EOij1)
                        F+=lllx[i]*lllx[j]*EOij1
            #print('F=',F)
            Z=0.0
            for i in range(vm):
                    Z+=llm[i]*lllm[i]
            for i in range(vx):
                    Z+=llx[i]*lllx[i]
            #print('Z=',Z)
            rYy=[]#存放阳离子的r
            rY=[]
            for i in range(vm):#M
                #离子为lm[i],价态为llm[i],摩尔浓度lllm[i]
                Inr=F*llm[i]*llm[i]
                for ij in range(vm):
                    for q in range(vx):
                        Inr+=llm[i]*lllm[ij]*lllx[q]*pitzer11[lm[ij]+lx[q]][2]/2/sympy.sqrt(llm[ij]*llx[q])
                for opop in range(vx):
                    Inr+=lllx[opop]*(2*B[fenzi.index(lm[i]+lx[opop])]+Z*pitzer11[lm[i]+lx[opop]][2]/2/sympy.sqrt(llm[i]*llx[opop]))
                for j in range(vm):#c
                    if i!=j :
                        if j<vm :
                            Inr+=lllm[j]*2*WL2XS[lzph.index(lm[i]+lm[j])]
                            for q in range(vx):#A
                                Inr+=lllm[j]*lllx[q]*OZYLCYy[lm[i]+lm[j]+lx[q]]
                        if j>=vm:
                            j=0
                            Inr+=lllm[j]*2*WL2XS[lzph.index(lm[i]+lm[j])]
                            for q in range(vx):#A
                                Inr+=lllm[j]*lllx[q]*OZYLCYy[lm[i]+lm[j]+lx[q]]
                for mm in range(vx):
                    for nn in range(vx):
                        if mm < nn:
                            Inr+=lllx[mm]*lllx[nn]*OZYLCYy[lx[mm]+lx[nn]+lm[i]]
                r=sympy.exp(Inr)
                #print('%s的r为'%lm[i],r)
                rYy.append(r)
            for i in range(vx):#M
                #离子为lm[i],价态为llm[i],摩尔浓度lllm[i]
                Inr=F*llx[i]*llx[i]
                for ij in range(vx):
                    for q in range(vm):
                        Inr+=llx[i]*lllx[ij]*lllm[q]*pitzer11[lm[q]+lx[ij]][2]/2/sympy.sqrt(llx[ij]*llm[q])
                for opop in range(vm):
                    Inr+=lllm[opop]*(2*B[fenzi.index(lm[opop]+lx[i])]+Z*pitzer11[lm[opop]+lx[i]][2]/2/sympy.sqrt(llx[i]*llm[opop]))
                for j in range(vx):#c
                    if i!=j :
                        if j<vx :
                            Inr+=lllx[j]*2*WL2XS[lzph.index(lx[i]+lx[j])]
                            for q in range(vm):#A
                                Inr+=lllx[j]*lllm[q]*OZYLCYy[lx[i]+lx[j]+lm[q]]
                        if j>=vx:
                            j=0
                            Inr+=lllx[j]*2*WL2XS[lzph.index(lx[i]+lx[j])]
                            for q in range(vm):#A
                                Inr+=lllx[j]*lllm[q]*OZYLCYy[lx[i]+lx[j]+lm[q]]
                for mm in range(vm):
                    for nn in range(vm):
                        if mm < nn:
                            Inr+=lllm[mm]*lllm[nn]*OZYLCYy[lm[mm]+lm[nn]+lx[i]]
                r=sympy.exp(Inr)
                #print('%s的r为'%lx[i],r)
                rY.append(r)
            dy=0
            for i in range(vm):
                dy+=lllm[i]
            for i in range(vx):
                dy+=lllx[i]
            dr=-Ay*I**1.5/(1+1.2*sympy.sqrt(I))
            ds=0
            for i in range(vm):
                for j in range(vx):
                    ds+=lllm[i]*lllx[j]*(By[fenzi.index(lm[i]+lx[j])]+Z*pitzer11[lm[i]+lx[j]][2]/2/sympy.sqrt(llm[i]*llx[j]))

            qwe=0
            for i in range(vm):
                for j in range(vm):
                    if j>i:
                      qwe+=lllm[i]*lllm[j]*WL1XSy[lzph.index(lm[i]+lm[j])]
                      for q in range(vx):
                        qwe+=lllm[i]*lllm[j]*lllx[q]*OZYLCYy[lm[i]+lm[j]+lx[q]]
            dw=0
            for i in range(vx):
                for j in range(vx):
                  if j >i :
                     dw+=lllx[i]*lllx[j]*WL1XSy[lzph.index(lx[i]+lx[j])]
                     for q in range(vm):
                        dw+=lllx[i]*lllx[j]*lllm[q]*OZYLCYy[lx[i]+lx[j]+lm[q]]
            dl=0#无中性粒子dq
            whh=1+2*(dr+ds+qwe+dw+dl)/dy
            #print('渗透系数为',whh)
            wh=sympy.exp(-whh*dy/55.508)
            #print("水的活度为",wh)
            sll1=len(xgx)#固相数
            sl=[]#第i个固相的每个离子数量
            for i in range(sll1):
                sl.append(len(xgx[i]))
            Kk=[]#计算k
            Jsyz=[]#别人实验k
            for i in range(sll1):
                K=1
                zz=''
                for j in range(sl[i]):
                    if xgx[i][j] in lm:
                        l1=lm.index(xgx[i][j])
                        K=K*(lllm[l1]*rYy[l1])**float(xgxsl[i][j])
                        zz+=xgx[i][j]
                    elif xgx[i][j] in lx:
                        l2=lx.index(xgx[i][j])
                        K=K*(lllx[l2]*rY[l2])**float(xgxsl[i][j])
                        zz+=xgx[i][j]
                    elif xgx[i][j]=='h2o':
                        K=K*wh**float(xgxsl[i][j])
                        zz+='_'
                        zz+=str(xgxsl[i][j])
                Kk.append(K)
                jsyz=phcs[zz]
                Jsyz.append(jsyz)

            for i in range(sll1):
                print(Jsyz[i]-Kk[i])
                huitua.append(Jsyz[i]-Kk[i])


def yys(vm,vx):
            z=0.0000
            for i in range(vx):
                z+=lllx[i]*llx[i]
            for j in range(vm-1):
                z-=llm[j]*lllm[j]
            lllm[vm-1]=z/llm[vm-1]
            F=0.000
            I=0.000000
            for i in range(vm) :
                I+=0.5*lllm[i]*llm[i]*llm[i]
            for i in range(vx) :
                I+=0.5*lllx[i]*llx[i]*llx[i]
            #print('溶液离子强度为',I)
            sI=sympy.sqrt(I)
            e1=sympy.exp(-2*sI)
            Z=0.0000000
            for i in range(vm):
                 Z+=llm[i]*lllm[i]
            for i in range(vx):
                Z+=llx[i]*lllx[i]
            #print(Z)
            def g(x):
                gx=2*(1-(1+x)*sympy.exp(-x))/x/x
                return gx
            def g1(x):
                g1x=-2*(1-(1+x+x*x/2)*sympy.exp(-x))/x/x
                return g1x
            gs=vm*vx
            fenzi=[]#存放化合物
            By=[]#存放化合物 第二维里系数By
            B=[]#存放化合物 第二维里系数B
            B11=[]#存放化合物 第二维里系数B导数
            lzph=[]#存放离子配合ij
            WL1XSy=[]#存放离子 第二维里系数
            WL2XS=[]#存放离子 第二维里系数
            WL3XS11=[]#存放离子 第二维里系数倒数
            for i in range(vm):
                for j in range(vx):
                    fzs=lm[i]+lx[j]
                    fenzi.append(fzs)
                    if llm[i]==2 & llx[j]==2:
                        a1=1.4
                        a2=12
                        B0=pitzer11[fzs][0]
                        B1=pitzer11[fzs][1]
                        C=pitzer11[fzs][2]
                        B2=pitzer11[fzs][3]
                        By.append(B0+B1*sympy.exp(-a1*sI)+B2*sympy.exp(-a2*sI))
                        B.append(B0+B1*g(a1*sI)+B2*g(a2*sI))
                        B11.append(B1*g1(a1*sI)/I+B2*g1(a2*sI)/I)
                        F+=(B1*g1(a1*sI)+B2*g1(a2*sI))/I*lllm[i]*lllx[j]
                    else:
                        a1=2
                        B0=pitzer11[fzs][0]
                        B1=pitzer11[fzs][1]
                        C=pitzer11[fzs][2]
                        By.append(B0+B1*sympy.exp(-a1*sI))
                        B.append(B0+B1*g(a1*sI))
                        B11.append(B1*g1(a1*sI)/I)
                        F+=B1*g1(a1*sI)/I*lllm[i]*lllx[j]

            F+=-Ay*(sI/(1+1.2*sI)+2/1.2*sympy.log((1+1.2*sI)))

            #不同的同号离子间有O作用
            for i in range(vm):
                for j in range(vm):
                    if j>i:
                        lzij=lm[i]+lm[j]
                        lzph.append(lzij)
                        lzij=lm[j]+lm[i]
                        lzph.append(lzij)
                        if llm[i]==llm[j]:
                          EOij=0
                          EOij1=0
                        else:
                          def J(x):
                             return x/(4+4.581*(x**(-0.7237))*sympy.exp(-0.012*(x**0.528)))
                          def J1(x):
                             return (4+4.581*(x**-0.7237)*sympy.exp(-0.012*(x**0.528)))**(-1)+((4+4.581*(x**-0.7237)*sympy.exp(-0.012*(x**0.528)))**(-2))*(4.581*x*sympy.exp(-0.012*(x**0.528))*(0.7237*(x**(-1-0.7237))+0.012*0.528*(x**(0.528-1))*(x**-0.7237)))                         #J与J’查表JJ'，公式不用
                          Xij=6*llm[i]*llm[j]*Ay*sI
                          Jij=J(Xij)
                          Jij1=J1(Xij)

                          Xii=6*llm[i]*llm[i]*Ay*sI
                          Jii=J(Xii)
                          Jii1=J1(Xii)

                          Xjj=6*llm[j]*llm[j]*Ay*sI
                          Jjj=J(Xjj)
                          Jjj1=J1(Xjj)

                          EOij=llm[i]*llm[j]/4/I*(Jij-Jii/2-Jjj/2)
                          EOij1=-EOij/I+llm[i]*llm[j]/8/I/I*(Xij*Jij1-Xii*Jii1/2-Xjj*Jjj1/2)
                        #print('%s与%s的EOij与EOij’为'%(lm[i],lm[j]),EOij,EOij1)
                        WL1XSy.append(OZYL[lm[i]+lm[j]][0]+EOij+I*EOij1)
                        WL2XS.append(EOij+OZYL[lm[i]+lm[j]][0])
                        WL3XS11.append(EOij1)
                        WL1XSy.append(OZYL[lm[i]+lm[j]][0]+EOij+I*EOij1)
                        WL2XS.append(EOij+OZYL[lm[i]+lm[j]][0])
                        WL3XS11.append(EOij1)
                        F+=lllm[i]*lllm[j]*EOij1
            for i in range(vx):
                for j in range(vx):
                    if j>i:
                        lzij=lx[i]+lx[j]
                        lzph.append(lzij)
                        lzij=lx[j]+lx[i]
                        lzph.append(lzij)
                        if llx[i]==llx[j]:
                          EOij=0
                          EOij1=0
                        else:
                          def J(x):
                             return x/(4+4.581*(x**(-0.7237))*sympy.exp(-0.012*(x**0.528)))
                          def J1(x):
                             return (4+4.581*(x**-0.7237)*sympy.exp(-0.012*(x**0.528)))**(-1)+((4+4.581*(x**-0.7237)*sympy.exp(-0.012*(x**0.528)))**(-2))*(4.581*x*sympy.exp(-0.012*(x**0.528))*(0.7237*(x**(-1-0.7237))+0.012*0.528*(x**(0.528-1))*(x**-0.7237)))
                         #J与J’用公式
                          Xij=6*llx[i]*llx[j]*Ay*sI
                          Jij=J(Xij)
                          Jij1=J1(Xij)

                          Xii=6*llx[i]*llx[i]*Ay*sI
                          Jii=J(Xii)
                          Jii1=J1(Xii)

                          Xjj=6*llx[j]*llx[j]*Ay*sI
                          Jjj=J(Xjj)
                          Jjj1=J1(Xjj)

                          EOij=llx[i]*llx[j]/4/I*(Jij-Jii/2-Jjj/2)
                          EOij1=-EOij/I+llx[i]*llx[j]/8/I/I*(Xij*Jij1-Xii*Jii1/2-Xjj*Jjj1/2)
                        #print('%s与%s的EOij与EOij’为'%(lx[i],lx[j]),EOij,EOij1)
                        WL1XSy.append(OZYL[lx[i]+lx[j]][0]+EOij+I*EOij1)
                        WL2XS.append(EOij+OZYL[lx[i]+lx[j]][0])
                        WL3XS11.append(EOij1)
                        WL1XSy.append(OZYL[lx[i]+lx[j]][0]+EOij+I*EOij1)
                        WL2XS.append(EOij+OZYL[lx[i]+lx[j]][0])
                        WL3XS11.append(EOij1)
                        F+=lllx[i]*lllx[j]*EOij1
            #print('F=',F)
            Z=0.0
            for i in range(vm):
                    Z+=llm[i]*lllm[i]
            for i in range(vx):
                    Z+=llx[i]*lllx[i]
            #print('Z=',Z)
            rYy=[]#存放阳离子的r
            rY=[]
            for i in range(vm):#M
                #离子为lm[i],价态为llm[i],摩尔浓度lllm[i]
                Inr=F*llm[i]*llm[i]
                for ij in range(vm):
                    for q in range(vx):
                        Inr+=llm[i]*lllm[ij]*lllx[q]*pitzer11[lm[ij]+lx[q]][2]/2/sympy.sqrt(llm[ij]*llx[q])
                for opop in range(vx):
                    Inr+=lllx[opop]*(2*B[fenzi.index(lm[i]+lx[opop])]+Z*pitzer11[lm[i]+lx[opop]][2]/2/sympy.sqrt(llm[i]*llx[opop]))
                for j in range(vm):#c
                    if i!=j :
                        if j<vm :
                            Inr+=lllm[j]*2*WL2XS[lzph.index(lm[i]+lm[j])]
                            for q in range(vx):#A
                                Inr+=lllm[j]*lllx[q]*OZYLCYy[lm[i]+lm[j]+lx[q]]
                        if j>=vm:
                            j=0
                            Inr+=lllm[j]*2*WL2XS[lzph.index(lm[i]+lm[j])]
                            for q in range(vx):#A
                                Inr+=lllm[j]*lllx[q]*OZYLCYy[lm[i]+lm[j]+lx[q]]
                for mm in range(vx):
                    for nn in range(vx):
                        if mm < nn:
                            Inr+=lllx[mm]*lllx[nn]*OZYLCYy[lx[mm]+lx[nn]+lm[i]]
                r=sympy.exp(Inr)
                #print('%s的r为'%lm[i],r)
                rYy.append(r)
            for i in range(vx):#M
                #离子为lm[i],价态为llm[i],摩尔浓度lllm[i]
                Inr=F*llx[i]*llx[i]
                for ij in range(vx):
                    for q in range(vm):
                        Inr+=llx[i]*lllx[ij]*lllm[q]*pitzer11[lm[q]+lx[ij]][2]/2/sympy.sqrt(llx[ij]*llm[q])
                for opop in range(vm):
                    Inr+=lllm[opop]*(2*B[fenzi.index(lm[opop]+lx[i])]+Z*pitzer11[lm[opop]+lx[i]][2]/2/sympy.sqrt(llx[i]*llm[opop]))
                for j in range(vx):#c
                    if i!=j :
                        if j<vx :
                            Inr+=lllx[j]*2*WL2XS[lzph.index(lx[i]+lx[j])]
                            for q in range(vm):#A
                                Inr+=lllx[j]*lllm[q]*OZYLCYy[lx[i]+lx[j]+lm[q]]
                        if j>=vx:
                            j=0
                            Inr+=lllx[j]*2*WL2XS[lzph.index(lx[i]+lx[j])]
                            for q in range(vm):#A
                                Inr+=lllx[j]*lllm[q]*OZYLCYy[lx[i]+lx[j]+lm[q]]
                for mm in range(vm):
                    for nn in range(vm):
                        if mm < nn:
                            Inr+=lllm[mm]*lllm[nn]*OZYLCYy[lm[mm]+lm[nn]+lx[i]]
                r=sympy.exp(Inr)
                #print('%s的r为'%lx[i],r)
                rY.append(r)
            dy=0
            for i in range(vm):
                dy+=lllm[i]
            for i in range(vx):
                dy+=lllx[i]
            dr=-Ay*I**1.5/(1+1.2*sympy.sqrt(I))
            ds=0
            for i in range(vm):
                for j in range(vx):
                    ds+=lllm[i]*lllx[j]*(By[fenzi.index(lm[i]+lx[j])]+Z*pitzer11[lm[i]+lx[j]][2]/2/sympy.sqrt(llm[i]*llx[j]))

            qwe=0
            for i in range(vm):
                for j in range(vm):
                    if j>i:
                      qwe+=lllm[i]*lllm[j]*WL1XSy[lzph.index(lm[i]+lm[j])]
                      for q in range(vx):
                        qwe+=lllm[i]*lllm[j]*lllx[q]*OZYLCYy[lm[i]+lm[j]+lx[q]]
            dw=0
            for i in range(vx):
                for j in range(vx):
                  if j >i :
                     dw+=lllx[i]*lllx[j]*WL1XSy[lzph.index(lx[i]+lx[j])]
                     for q in range(vm):
                        dw+=lllx[i]*lllx[j]*lllm[q]*OZYLCYy[lx[i]+lx[j]+lm[q]]
            dl=0#无中性粒子dq
            whh=1+2*(dr+ds+qwe+dw+dl)/dy
            #print('渗透系数为',whh)
            wh=sympy.exp(-whh*dy/55.508)
            #print("水的活度为",wh)
            sll1=len(xgx)#固相数
            sl=[]#第i个固相的每个离子数量
            for i in range(sll1):
                sl.append(len(xgx[i]))
            Kk=[]#计算k
            Jsyz=[]#别人实验k
            for i in range(sll1):
                K=1
                zz=''
                for j in range(sl[i]):
                    if xgx[i][j] in lm:
                        l1=lm.index(xgx[i][j])
                        K=K*(lllm[l1]*rYy[l1])**float(xgxsl[i][j])
                        zz+=xgx[i][j]
                    elif xgx[i][j] in lx:
                        l2=lx.index(xgx[i][j])
                        K=K*(lllx[l2]*rY[l2])**float(xgxsl[i][j])
                        zz+=xgx[i][j]
                    elif xgx[i][j]=='h2o':
                        K=K*wh**float(xgxsl[i][j])
                        zz+='_'
                        zz+=str(xgxsl[i][j])
                Kk.append(K)
                jsyz=phcs[zz]
                Jsyz.append(jsyz)

            for i in range(sll1):
                print(Jsyz[i]-Kk[i])
                huitua.append(Jsyz[i]-Kk[i])


huitua=[]
#ys(vm,vx)

#一般而言，1次4种固相，多的排到下一次，手动记录固相
f1=func_1[0]
#下面功能2无法使用
from scipy.optimize import root
from math import *
def func_2():
    if f1==2:
        import matplotlib.pyplot as plt
        import numpy as np
        #from numpy import *
        def main():
            fig = plt.figure(figsize=(9,9))
            # 设置x和y的坐标范围
            x11=np.arange(0,15,0.01)#开始，结束，精度
            x12=np.arange(0,15,0.01)
            x11,x12=np.meshgrid(x11,x12)

            zz=huitua[0]
            z=zz.subs([(x1,x11),(x2,x12)])
            plt.contour(x11,x12,z,0)#最后一个为0，不然多条线，默认绿色

            #z=huitua[1]
            #plt.contour(x1,x2,z,0,colors=['r'])

            plt.xlabel("mol/kg水", fontproperties='simhei', fontsize=10, color='green')#x轴
            plt.ylabel("mol/kg水", fontproperties='simhei', fontsize=10, color='green')
            plt.show()

        #main()
        print("待开发")

    elif f1==1:


        fff=int(jstj[0])
        sel=int(jstj[1])
        def xh(fff):
            if fff==-3:
                yys(vm,vx)
                jsgs=3
                chuzhi=[]
                dingzhi=[]
                if sel==123:#x4,5,6的浓度变
                    for i in range(jsgs):
                        o=float(input("%s的初始浓度为"%lx[i]))
                        chuzhi.append(o)
                    def f123(x):
                            eqs=[]
                            for i in range(jsgs):
                                zz=huitua[i]
                                z=zz.subs([(x4,x[0]),(x5,x[1]),(x6,x[2])])
                                eqs.append(z)
                            return eqs
                    z=root(f123,chuzhi).x#存放解
                    for i in range(jsgs):
                        print('%s为'%lx[i],z[i])
                elif sel==12:#x4,5的浓度变
                    for i in range(2):
                        o=float(input("%s的初始浓度为"%lx[i]))
                        chuzhi.append(o)
                    dingzhi.append(float(input("%s的浓度为"%lx[2])))
                    def f12(x):
                            eqs=[]
                            for i in range(2):#x4,5固体
                                zz=huitua[i]
                                z=zz.subs([(x4,x[0]),(x5,x[1]),(x6,dingzhi[0])])
                                eqs.append(z)
                            return eqs
                    z=root(f12,chuzhi).x#存放解
                    print('%s为'%lx[0],z[0],'\n%s为'%lx[1],z[1],'\n%s为'%lx[2],dingzhi[0])

            elif fff==3:
                ys(vm,vx)
                jsgs=3
                chuzhi=[]
                dingzhi=[]
                if sel==123:#x1，2，3的浓度变
                    for i in range(jsgs):
                        o=float(input("%s的初始浓度为"%lm[i]))
                        chuzhi.append(o)
                    def f123(x):
                            eqs=[]
                            for i in range(jsgs):
                                zz=huitua[i]
                                z=zz.subs([(x1,x[0]),(x2,x[1]),(x3,x[2])])
                                eqs.append(z)
                            return eqs
                    z=root(f123,chuzhi).x#存放解
                    for i in range(jsgs):
                        print('%s为'%lm[i],z[i])
                elif sel==12:#x1,2的浓度变
                    for i in range(2):
                        o=float(input("%s的初始浓度为"%lm[i]))
                        chuzhi.append(o)
                    dingzhi.append(float(input("%s的浓度为"%lm[2])))
                    def f12(x):
                            eqs=[]
                            for i in range(2):#x1,2固
                                zz=huitua[i]
                                z=zz.subs([(x1,x[0]),(x2,x[1]),(x3,dingzhi[0])])
                                eqs.append(z)
                            return eqs
                    z=root(f12,chuzhi).x#存放解
                    print('%s为'%lm[0],z[0],'\n%s为'%lm[1],z[1],'\n%s为'%lm[2],dingzhi[0])


            elif fff==2:
                ys(vm,vx)
                jsgs=2
                chuzhi=[]
                dingzhi=[]
                if sel==12:#x1，2的浓度变
                    for i in range(jsgs):
                        o=float(input("%s的初始浓度为"%lm[i]))
                        chuzhi.append(o)
                    def f12(x):
                            eqs=[]
                            for i in range(jsgs):
                                zz=huitua[i]
                                z=zz.subs([(x1,x[0]),(x2,x[1])])
                                eqs.append(z)
                            return eqs
                    z=root(f12,chuzhi).x#存放解
                    for i in range(jsgs):
                        print('%s为'%lm[i],z[i])
                elif sel==1:#x1的浓度变
                    chuzhi.append(float(input("%s的初始浓度为"%lm[0])))#理论上不需要输入，但考虑到多解（0点），输入接近的
                    dingzhi.append(float(input("%s的浓度为"%lm[1])))
                    def f1(x):
                        eqs=[]
                        zz=huitua[1]#应是lm【1】的固相
                        z=zz.subs([(x1,x[0]),(x2,dingzhi[0])])
                        eqs.append(z)
                        return eqs
                    z=root(f1,chuzhi).x#存放解
                    print('%s为'%lm[0],z[0],'\n%s为'%lm[1],dingzhi[0])
                elif sel==2:#x2的浓度变
                    dingzhi.append(float(input("%s的浓度为"%lm[0])))
                    chuzhi.append(float(input("%s的初始浓度为"%lm[1])))
                    def f1(x):
                        eqs=[]
                        zz=huitua[0]
                        z=zz.subs([(x2,x[0]),(x1,dingzhi[0])])
                        eqs.append(z)
                        return eqs
                    z=root(f1,chuzhi).x#存放解
                    print('%s为'%lm[0],dingzhi[0],'\n%s为'%lm[1],z[0])


            elif fff==-2:
                yys(vm,vx)
                jsgs=2
                chuzhi=[]
                dingzhi=[]
                if sel==12:#x4，5的浓度变
                    for i in range(jsgs):
                        o=float(input("%s的初始浓度为"%lx[i]))
                        chuzhi.append(o)
                    def f12(x):
                            eqs=[]
                            for i in range(jsgs):
                                zz=huitua[i]
                                z=zz.subs([(x4,x[0]),(x5,x[1])])
                                eqs.append(z)
                            return eqs
                    z=root(f12,chuzhi).x#存放解
                    for i in range(jsgs):
                        print('%s为'%lx[i],z[i])
                elif sel==1:#x4的浓度变
                    chuzhi.append(float(input("%s的初始浓度为"%lx[0])))#理论上不需要输入，但考虑到多解（0点），输入接近的
                    dingzhi.append(float(input("%s的浓度为"%lx[1])))
                    def f1(x):
                        eqs=[]
                        zz=huitua[1]#应是lx【1】的固相
                        z=zz.subs([(x4,x[0]),(x5,dingzhi[0])])
                        eqs.append(z)
                        return eqs
                    z=root(f1,chuzhi).x#存放解
                    print('%s为'%lx[0],z[0],'\n%s为'%lx[1],dingzhi[0])
                elif sel==2:#x5的浓度变
                    dingzhi.append(float(input("%s的浓度为"%lx[0])))
                    chuzhi.append(float(input("%s的初始浓度为"%lx[1])))
                    def f1(x):
                        eqs=[]
                        zz=huitua[0]
                        z=zz.subs([(x5,x[0]),(x4,dingzhi[0])])
                        eqs.append(z)
                        return eqs
                    z=root(f1,chuzhi).x#存放解
                    print('%s为'%lx[0],dingzhi[0],'\n%s为'%lx[1],z[0])


            elif fff==-22:
                print("未设计")

            else:
                print("未设计")
        xh(fff)

func_2()

x=int(input("继续？1确认"))
while x==1:
    huitua=[]
    y=int(input("计算体系为："))
    z=int(input("计算方式为："))
    jstj[0]=y
    jstj[1]=z
    func_2()
