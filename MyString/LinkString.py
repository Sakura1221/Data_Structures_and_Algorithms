### 结点类
class Node(object):
    def __init__(self):
        self.data = None
        self.next = None


### 链串类
class LinkString(object):
    ### 初始化链串，对链串的头、尾指针以及长度初始化
    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.length = 0

    ### 根据输入创建链串
    def CreateString(self):
        string = input("\n请输入字符串，按回车键结束输入：")
        while self.length < len(string): # 用链长度与字符串长度作比较
            tString = Node()
            tString.data = string[self.length] # 将字符串所有字符当作单独结点，分开存储，且
            self.tail.next = tString # 新字符加在尾指针（结点）之后
            self.tail = tString # 尾指针移动到新的尾结点
            self.length += 1

    ### 复制串
    def CopyString(self, linkstr):
        self.head = linkstr.head
        self.tail = linkstr.tail
        self.length = linkstr.length

    ### 连接串
    def ConcatString(self, linkstr):
        self.tail.next = linkstr.head.next
        self.tail = linkstr.tail
        self.length += linkstr.length
