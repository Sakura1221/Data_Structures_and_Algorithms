### 广义表结点类
class GLNode(object):
    def __init__(self):
        self.tag = 1 # 标志域，用来区分子表结点（1）原子结点（0）
        self.union = None # 联合域是子表结点指示表头的指针与原子结点值域的统一表示（存储结点数据）
        self.next = None # 指针域是子表结点指示表尾的指针域与原子结点指针域的统一表示（存储结点指向）


### 广义表类
class GList(object):
    ### 根据书写形式串（字符串要先转换成列表）创建广义表
    def CreateGList(self, Table):
        if len(Table) > 0:
            tTable = Table.pop(0) # 读取第一个字符
            tGLNode = GLNode() # 创建一个空广义表结点
            if tTable == '(': # 只有# ( 原子 三种情况
                tGLNode.tag = 1 # 左括号代表子表
                tGLNode.union = self.CreateGList(Table) # 子表的值域存在嵌套，使用递归实现
            elif tTable == '#':
                tGLNode = None # “(#)”代表空表
            else:
                tGLNode.tag = 0 # 如果第一个字符为‘(’会产生递归，如果为‘#’则后面的‘)’会被剔除，则必为原子结点
                tGLNode.union = tTable
        else:
            tGLNode = None # 形式串为空，输出None
        if len(Table) > 0:
            tTable = Table.pop(0) # 读取下一个字符，只有')'与‘,’两种情况
        if tGLNode != None: # 空表无指针域，可写可不写
            if tTable == ',':
                tGLNode.next = self.CreateGList(Table) # 逗号表示指向下一个子表或原子，使用递归实现
            else:
                tGLNode.next = None # 非逗号，即括号，指针域为None，表示该子表内原子遍历完毕，返回上一层级的联合域（对应的左右括号）
        return tGLNode # 两个递归的存在，保证一个子表内的所有元素遍历完成后才能返回，作为上一层迭代的联合域

MyGLNode = GList()
Table = '((#),(a),(b,(c,d,e)))'
MyGLNode.CreateGList(list(Table))