class Node(object):
    ### 初始化结点，对结点的数据域和指针域进行初始化为None
    def __init__(self):
        self.data = None
        self.next = None


class LinkQueue(object):
    ### 初始化链式队列，新建一个结点，将头指针与尾指针都放在该结点
    def __init__(self):
        tNode = Node()
        self.front = tNode
        self.rear = tNode

    ### 判断链式队列是否为空，若头指针与尾指针相同则队列为空
    def IsEmptyQueue(self):
        if self.front == self.rear:
            iQueue = True
        else:
            iQueue = False
        return(iQueue)

    ### 进队函数
    def EnQueue(self, new):
        tNode = Node()
        tNode.data = new
        self.rear.next = tNode # 新的结点加在现在队尾后面（队尾指针就是队尾结点）
        self.rear = tNode # 用新的队尾结点给队尾指针赋值

    ### 出队函数
    def DeQueue(self):
        if self.IsEmptyQueue():
            print("队列为空")
            return
        else:
            tNode = self.front.next # 获取头结点，头指针位于头节点之前，指向头节点
            self.front.next = tNode.next # 头指针指向头节点之后的结点
            if self.rear == tNode: # 如果头节点也是尾结点（尾指针），相当于队列就最后一个元素，那尾指针需要重新指向头指针
                self.rear = self.front
            return tNode.data # 返回头节点数据

    ### 获取队头元素
    def GetHead(self):
        if self.IsEmptyQueue():
            print("队列为空")
            return
        else:
            return self.front.next.data

    ### 通过输入数据创建一个队列
    def CreateQueueByInput(self):
        data = input("请输入元素（继续输入请按回车键，结束请输入“#”）：")
        while data != '#':
            self.EnQueue(data)
            data = input("请输入元素：")

MyLinkQueue = LinkQueue()
MyLinkQueue.CreateQueueByInput()
print(MyLinkQueue.GetHead())