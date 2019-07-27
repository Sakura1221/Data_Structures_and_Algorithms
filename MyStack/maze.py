from MyStack.LinkStack import LinkStack

class Maze(object):
    ###当前位置到达右，下，左，上相邻位置所需移动的坐标
    Directions = [(0,1), (1,0), (0,-1), (-1,0)]

    ###判断当前位置是否可以通行且未经过
    def IsPossiblePass(self, mazeroute, position):
        if mazeroute[position[0]][position[1]] == 0: # 经过的位置被赋值为2，不能通过设置为-1，能通过但未经过设置为0
            route = True
        else:
            route = False
        return route

    ###将走过的位置设置为2
    def PassedMark(self, mazeroute, position):
        mazeroute[position[0]][position[1]] = 2 # 迷宫使用二位数组表示

    ###输出迷宫从出口到入口路径的函数
    def PrintRoute(self, Exit, st):
        print("从出口到入口的路径为：")
        print(Exit,end='')
        i = 1
        while st.IsEmptyStack() != True:
            print(st.PopStack()[0], end='')
            i = i+1
            if i % 10 == 0:
                print() # print输出后自带一个换行

    ###寻找迷宫路径
    def FindMazeRoute(self, mazeroute, Enter, Exit):
        st = LinkStack() # 走过路径以及该路径下一个待检验方向组成的栈
        position = Enter # 当前位置设置为起点
        nxt = 0 # 从当前位置向下一个位置的移动方向0(右)，1（下），2（左），3（上）
        while True: # 不停循环，完成
            if position == Exit: # 如果当前位置为出口，则输出迷宫路线
                self.PrintRoute(Exit,st)
                return
            else:
                self.PassedMark(mazeroute, position) # 当前位置不为出口，将当前位置标记为已经过位置
                for i in range(nxt, 4): # 按照右下左上的位置依次查找可通行且未经过的位置，若尝试过的方向不再尝试
                    nextposition = (position[0] + self.Directions[i][0], # 根据当前位置与方向确定下一个位置
                                    position[1] + self.Directions[i][1])
                    if self.IsPossiblePass(mazeroute, nextposition): # 如果下一个位置能通行且未经过
                        st.PushStack((position, i+1)) # 将当前位置和下一个可能通行方向压入栈内
                        position = nextposition # 更新当前位置为下一位置
                        nxt = 0 # 下一个位置依然从右方向开始尝试
                        break # 跳出for循环
                else: # 若for循环内执行了break语句，则else不会执行，也即当所有方向都不能通行或者已经经过时执行
                    if st.IsEmptyStack(): # 如果栈为空，则表示已经退回起点之前了
                        break # 跳出while循环
                    else:
                        position, nxt = st.PopStack() # 如果栈不为空则表明还有后退的机会，同时返回上一位置与该位置下一个尝试方向
        print("没有找到通过迷宫的路径") # while循环外部，若循环跳出执行

MyMaze = Maze()
mazeroute = [[1,1,0,1,0,1,1],
             [1,0,0,1,0,0,1],
             [1,0,1,1,1,0,1],
             [1,0,0,1,0,0,1],
             [1,1,0,0,0,1,1],
             [1,1,1,1,1,1,1]]
MyMaze.FindMazeRoute(mazeroute, (0,2), (0,4))