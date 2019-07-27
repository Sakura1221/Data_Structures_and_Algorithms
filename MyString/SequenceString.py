class SequenceString(object):
    ### 初始化串
    def __init__(self, max):
        self.MaxStringSize = max
        self.chars = ""
        self.length = 0

    ### 判断串是否为空
    def IsEmptyString(self):
        if self.length == 0:
            return True
        else:
            return False

    ### 根据输入创建串
    def CreateString(self):
        string = input("请输入字符串，按回车键结束输入")
        if len(string) > self.MaxStringSize:
            print("输入的字符序列超出分配的存储空间，超过的部分无法存入当前串中")
            self.chars = string[:self.MaxStringSize]
        else:
            self.chars = string
