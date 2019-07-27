class CircularSequenceQueue(object):
    ### 初始化队列
    def __init__(self, max):
        self.MaxQueueSize = max
        self.s = [None for x in range(0, self.MaxQueueSize)]
        self.front = 0
        self.rear = 0

    ### 判断队列是否为空
    def IsEmptyQueue(self):
        if self.front == self.rear:
            iQueue = True
        else:
            iQueue = False
        return iQueue

    ### 元素进队
    def EnQueue(self, new):
        if (self.rear+1) % self.MaxQueueSize != self.front: # 如果队列不满（循环队列最多存储MaxQueueSize-1个元素）
            self.rear = (self.rear+1) % self.MaxQueueSize # 尾指针后移，达到MaxQueueSize就设为0
            self.s[self.rear] = new # 将新元素放在尾指针位置（队列的头指针要占一个位置）
        else:
            print("队列已满，无法进队")
            return

    ### 元素出队
    def DeQueue(self):
        if self.IsEmptyQueue():
            print("队列为空，无法出队")
            return
        else:
            self.front = (self.front+1) % self.MaxQueueSize # 头指针向后移到头节点位置，达到MaxQueueSize就设为0
            return self.s[self.front] # 返回头结点数据

    ### 获得头节点
    def GetHead(self):
        if self.IsEmptyQueue():
            print("队列为空，无法输出队头元素")
            return
        else:
            return self.s[self.front+1] # 头指针位于头节点前方

    ### 根据输入创建一个循环队列
    def CreateQueueByInput(self):
        data = input("请输入元素（继续输入请按回车键，结束请输入“#”）：")
        while data != '#':
            self.EnQueue(data)
            data = input("请输入元素：")