### 游戏规则：n个人围成圈，从1开始报数，报到k的退出，从下一个人继续报数，最后留下的是第几个人

from MyQueue.CircularLinkQueue import CircularLinkQueue as Queue
class CircleGame(object):
    ### 模拟游戏的函数
    def Game(self,n,k): # 输入总人数与要出去的数字
        qu = Queue()
        i = 1
        while i <= n: # 先将编号数据入队
            qu.EnQueue(i)
            i = i + 1
        print("队内的编号顺序为：", end = '')
        qu.QueueTraverse()
        print("\n出队顺序为：")
        count = 0
        while qu.GetQueueLength() != 1: # 当队列内元素超过1时
            iNum = 1 # 从1开始数
            while iNum != k : # 当数字不为k时，将队首出队，然后入队到队尾
                tData = qu.DeQueue()
                qu.EnQueue(tData)
                iNum += 1
            print(qu.DeQueue(), end = ' ') # 数字为k时，队首出队
            count += 1
            if count % 10 == 0:
                print()
        print('\n最后剩下的人编号是：', end = ' ')
        qu.QueueTraverse()

    ###游戏测试函数
    def TestGame(self):
        PeopleNum = int(input('请输入总人数：'))
        Gap = int(input('请输入要出去的数字：'))
        if PeopleNum > 0 and Gap > 0 and Gap <= PeopleNum:
            self.Game(PeopleNum,Gap)
        else:
            print('输入不符合要求！')

CircleGame().TestGame()