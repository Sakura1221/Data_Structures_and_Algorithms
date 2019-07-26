### 单链表结点类
class Node(object):
    ### 初始化结点
    def __init__(self):
        self.data = None
        self.next = None


### 单链表类
class SingleLinkedList(object):
    ### 初始化头结点
    def __init__(self):
        self.head = Node()

    ### 判断链表是否为空
    def IsEmptyLinkedList(self):
        if self.head == None:
            return True
        else:
            return False

    ### 尾端插入元素
    def InsertElementInTail(self, new):
        pNode = self.head # 链表要从头开始索引
        tNode = Node()
        tNode.data = new
        while pNode.next != None:
            pNode = pNode.next
        pNode.next = tNode

    ### 首端插入元素
    def InsertElementInHead(self, new):
        head = self.head
        tNode = Node()
        tNode.data = new
        tNode.next = head.next
        head.next = tNode

    ### 根据输入创建单链表
    def CreateSingleLinkedList(self):
        data = input("请输入元素（继续输入请按回车键，结束请输入”#“）：")
        while data != '#':
            self.InsertElementInTail(data)
            data = input("请输入元素：")

    ### 查找指定元素位置
    def FindElement(self, key):
        pos = 0
        pNode = self.head
        if self.IsEmptyLinkedList():
            print("当前单链表为空！")
            return
        else:
            while pNode.next != None and pNode.data != key:
                pNode = pNode.next
                pos += 1
            if pNode.data == key:
                print(f"查找成功！值为 {key} 的元素位于单链表第 {pos} 个位置")
            else:
                print(f"查找失败！单链表内不存在值为 {key} 的元素")

    ### 删除第一个指定元素
    def DeleteElement(self, element):
        pNode = self.head
        cNode = self.head
        if self.IsEmptyLinkedList():
            print("当前单链表为空！")
            return
        else:
            while pNode.next != None and pNode.data != element:
                cNode = pNode # 先备份一下前面的结点
                pNode = pNode.next
            if pNode.data == element: # 找到要删除的结点
                cNode.next = pNode.next # 将待删除结点的前后两个结点连起来
                del pNode # 删除待删除的结点
            else:
                print(f"删除失败！当前单链表不存在含有元素{element}的结点")

    ### 遍历单链表
    def TraverseElement(self):
        pNode = self.head
        if self.IsEmptyLinkedList():
            print("当前单链表为空！")
            return
        else:
            print("当前的单链表为：")
            while(pNode.next != None):
                print(f"{pNode.next.data}->",end='')
                pNode = pNode.next
            print("None")


MyList = SingleLinkedList()
MyList.CreateSingleLinkedList()
MyList.TraverseElement()