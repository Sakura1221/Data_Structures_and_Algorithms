class SequenceStack(object):
    ### 初始化栈函数
    def __init__(self, max):
        self.MaxStackSize = max
        self.s = [None for x in range(0, self.MaxStackSize)]
        self.top = -1

    ### 判断栈是否为空
    def IsEmptyStack(self):
        if self.top == -1:
            iTop = True
        else:
            iTop = False
        return iTop

    ### 进栈函数
    def PushStack(self, new):
        if self.top < self.MaxStackSize - 1:
            self.top += 1
            self.s[self.top] = new
        else:
            print("栈满")
            return

    ### 出栈函数
    def PopStack(self):
        if self.IsEmptyStack():
            print("栈为空")
            return
        else:
            iTop = self.top
            self.top -= 1
            return self.s[iTop]

    ### 获取栈顶元素
    def GetTopStack(self):
        if self.IsEmptyStack():
            print("栈为空")
            return
        else:
            return self.s[self.top]

    ### 遍历栈内元素
    def TraverseStack(self):
        if self.IsEmptyStack():
            print("栈为空")
            return
        else:
            for i in range(0, self.top + 1):
                print(self.s[i],end=' ')