### 这是一个阶乘的递归与非递归实现

### 递归方法，本质上是函数栈
"""当程序执行到某个函数时，将这个函数进行入栈操作，在入栈之前，通常需要完成三件事。

　　1、将所有的实参、返回地址等信息传递给被调函数保存。

　　2、为被调函数的局部变量分配存储区。

　　3、将控制转移到被调函数入口。

当一个函数完成之后会进行出栈操作，出栈之前同样要完成三件事。

　　1、保存被调函数的计算结果。

　　2、释放被调函数的数据区。

　　3、依照被调函数保存的返回地址将控制转移到调用函数。"""

def Factorial1(n):
    if n == 1:
        return 1
    else:
        return n * Factorial1(n-1)


### 非递归方法，将函数栈转化为数据栈
### 存储的信息和执行步骤更少，占用内存少，效率更高，但代码更复杂
from MyStack.LinkedStack import LinkStack
class FactElements(object):
    ###初始化阶乘函数的信息，使用类来包裹数据
    def __init__(self):
        self.LabelN = None # 用来判断出口的标志信息
        self.N = None # 当前乘数
        self.F = None # 累乘结果

    def Factorial(self,n):
        FE = FactElements() # 实例化一个阶乘对象
        FE.LabelN = 2 # 标志出口，对应栈内元素数量为1的情况
        FE.N = n # 乘数n
        st = LinkStack() # 链栈用于保存阶乘信息
        st.PushStack(FE) # 出口的信息压入栈内
        while True:
            tFE = st.GetTopStack()
            if tFE.N >= 1: # 判断乘数是否大于等于1
                temp = FactElements()
                temp.LabelN = 1
                temp.N = tFE.N - 1
                st.PushStack(temp) # 先保存乘数与相应的是否栈底标签信息
            else:
                tFE.F = 1 # 累乘结果初值
                break
        while True:
            tFE = st.GetTopStack() # 头结点元素
            if tFE.LabelN == 1: # 未到栈底
                st.PopStack() # 已计算过的乘数出栈
                temp = st.GetTopStack() # 下一个结点元素
                temp.F = tFE.F * temp.N # 上一个累乘结果与下一个乘数相乘
            tFE = st.GetTopStack()
            if tFE.LabelN == 2: # 阶乘结果保存在栈底元素内，输出即可
                tFE = st.PopStack()
                f = tFE.F
                break
        print(f"求解的结果为: {tFE.N}! = {f}") # f开头表示format格式化输出

### 下面是未保存标志信息的方法2，区别在于判断是否到栈底的条件
### 上面入栈是存储了标志信息运算速度更快
### 下面的方法使用栈的长度进行判断，因为是链栈，所以需要遍历，速度更慢
from MyStack.LinkedStack import LinkStack
class FactElements_V2(object):
    ###初始化阶乘函数的信息，使用类来包裹数据
    def __init__(self):
        self.N = None # 当前乘数
        self.F = None # 累乘结果

    def Factorial(self,n):
        FE = FactElements_V2() # 实例化一个阶乘对象
        FE.N = n # 乘数n
        st = LinkStack() # 链栈用于保存阶乘信息
        st.PushStack(FE) # 出口的信息压入栈内
        while True:
            tFE = st.GetTopStack()
            if tFE.N >= 1: # 判断乘数是否大于等于1
                temp = FactElements_V2()
                temp.N = tFE.N - 1
                st.PushStack(temp) # 先保存乘数与相应的是否栈底标签信息
            else:
                tFE.F = 1 # 累乘结果初值
                break
        while True:
            tFE = st.GetTopStack() # 头结点元素
            if st.GetStackLength() != 1: # 未到栈底
                st.PopStack() # 已计算过的乘数出栈
                temp = st.GetTopStack() # 下一个结点元素
                temp.F = tFE.F * temp.N # 上一个累乘结果与下一个乘数相乘
            else:
                tFE = st.PopStack()
                f = tFE.F
                break
        print(f"求解的结果为: {tFE.N}! = {f}") # f开头表示format格式化输出

FactElements_V2().Factorial(5)