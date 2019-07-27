class Node(object):
    ### 初始化结点，对结点的数据域和指针域进行初始化为None
    def __init__(self):
        self.data = None
        self.next = None


class CircularLinkQueue(object):
    ### 初始化链式队列，新建一个结点，将尾指针放在该结点
    ### 同时该结点指向自身（相当于头指针也放在该节点）
    ### 因为使用尾指针也可找到头节点，故不再额外设置头指针
    def __init__(self):
        tNode = Node()
        self.rear = tNode
        tNode.next = tNode

    ### 判断链式队列是否为空，若尾指针指向自己，则队列为空
    def IsEmptyQueue(self):
        if self.rear.next == self.rear: # 尾指针与头指针相同，rear是尾指针，rear.next相当于头指针
            iQueue = True
        else:
            iQueue = False
        return iQueue

    ### 进队函数
    def EnQueue(self, new):
        tNode = Node()
        tNode.data = new
        ###接下来两步顺序不能反，如果尾指针先指向结点，会找不到头指针
        tNode.next = self.rear.next  # 该结点指向头指针
        self.rear.next = tNode # 队尾结点指向该结点
        self.rear = tNode # 将队尾指针放置在新的队尾结点，rear.next也即头结点位置依旧保持不变

    ### 出队函数
    def DeQueue(self):
        if self.IsEmptyQueue():
            print("队列为空")
            return
        else:
            tNode = self.rear.next.next # 获取头结点，头指针位于头节点之前，指向头节点
            self.rear.next.next = tNode.next # 头指针指向头节点之后的结点
            if self.rear == tNode: # 如果头节点也是尾结点（尾指针），相当于队列就最后一个元素，那尾指针需要重新指向头指针
                self.rear = self.rear.next # 进队出队，头指针所在位置始终为初始化位置，保持不变，只是指向位置改变
            return tNode.data # 返回头节点数据

    ### 获取队头元素
    def GetHead(self):
        if self.IsEmptyQueue():
            print("队列为空")
            return
        else:
            return self.rear.next.next.data

    ### 通过输入数据创建一个队列
    def CreateQueueByInput(self):
        data = input("请输入元素（继续输入请按回车键，结束请输入“#”）：")
        while data != '#':
            self.EnQueue(data)
            data = input("请输入元素：")

    ### 遍历队列
    def QueueTraverse(self):
        front = self.rear.next
        if self.IsEmptyQueue():
            print("队列为空")
            return
        else:
            j = 0
            while(front != self.rear):
                j += 1
                print(front.next.data, end = ' ')
                if j % 10 == 0:
                    print()
                front = front.next
            return

    ### 获取队列长度
    def GetQueueLength(self):
        length = 0
        front = self.rear.next # 不能直接对队列指针操作，要赋值给其他变量操作
        if self.IsEmptyQueue():
            length = 0
        else:
            while (front != self.rear):
                length += 1
                front = front.next
        return length


if __name__ == '__main__':
    MyLinkQueue = CircularLinkQueue()
    MyLinkQueue.CreateQueueByInput()
    MyLinkQueue.QueueTraverse()
    print('\n'+ str(MyLinkQueue.GetQueueLength()))