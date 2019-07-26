### 结点类，用来创建一个结点
class Node(object):
    ### 初始化结点
    def __init__(self):
        self.data = None
        self.next = None

###链栈类
class LinkStack(object):
    ### 初始化链栈函数,创建一个链栈结点，并利用结点对栈指针初始化
    def __init__(self):
        self.top = Node()
        # 被赋值一个类/函数，实际上都是一个地址，赋值对象被调用就执行相应地址的类/函数

    ### 判断链栈是否为空
    def IsEmptyStack(self):
        if self.top.next == None:
            iTop = True
        else:
            iTop = False
        return iTop

    ### 进栈函数
    def PushStack(self, new):
        tNode = Node()
        tNode.data = new # 向新结点内的数据域赋值
        tNode.next = self.top.next # 新结点指向栈指针指向位置（栈顶）
        self.top.next = tNode # 栈指针指向新的栈顶结点

    ### 出栈函数
    def PopStack(self):
        if self.IsEmptyStack() == True:
            print('栈为空')
            return
        else:
            tNode = self.top.next # 根据栈指针找到栈顶结点
            self.top.next = tNode.next # 修改栈指针指向栈顶结点下面一个结点
            return tNode.data # 返回栈顶结点

    ### 获取栈顶元素
    def GetTopStack(self):
            if self.IsEmptyStack():
                print("栈为空")
                return
            else:
                return self.top.next.data

    ### 通过用户输入创建一个链栈
    def CreateStackByInput(self):
        data = input("请输入元素（继续输入请按回车键，结束请输入”#“）：")
        while data != '#':
            self.PushStack(data)
            data = input("请输入元素：")

    ### 获取栈的长度
    def GetStackLength(self):
        top = self.top # 不能直接对头指针进行操作，会改变栈的结构
        length = 0
        if self.IsEmptyStack():
            length = 0
        else:
            while (top.next != None):
                length += 1
                top = top.next
        return length
    ### 遍历整个链栈

if __name__ == '__main__':
    MyStack = LinkStack()
    MyStack.CreateStackByInput()
    print(MyStack.GetStackLength())