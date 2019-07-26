class SequenceList(object):
    ### 初始化顺序表
    def __init__(self):
        self.SeqList = []

    ### 根据输入创建顺序表
    def CreateSequenceListByInput(self):
        data = input("请输入元素（继续输入请按回车键，结束请输入“#”）：")
        while data != '#':
            self.SeqList.append(data)
            data = input("请输入元素：")

    ### 查找元素值
    def FindElement(self, key):
        if key in self.SeqList:
            pos = self.SeqList.index(key)
            print(f"查找成功！值为 {key} 的元素位于顺序表第 {pos} 个位置")
        else:
            print(f"查找失败！顺序表内不存在值为 {key} 的元素")

    ### 指定位置插入元素
    def InsertElement(self, pos, element):
        self.SeqList.insert(pos, element)
        print(f"插入元素后，当前顺序表为：\n{self.SeqList}")

    ### 指定位置删除元素
    def DeleteElement(self,pos):
        self.SeqList.remove(self.SeqList[pos])
        print(f"删除元素后顺序表为：\n{self.SeqList}")

    ### 遍历顺序表
    def TraverseElement(self):
        SeqListLen = len(self.SeqList)
        for i in range(0, SeqListLen):
            print(f"第{i+1}个元素的值为{self.SeqList[i]}")