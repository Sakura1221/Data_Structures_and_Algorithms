"""
孩子表示法
此方法除了与双亲表示法一样建立了存储所有结点的数组
数组元素值包括结点数据与结点第一个孩子结点的索引
还建立了由各结点的孩子结点组成的孩子链表
头结点为最左边的孩子结点，数据域保存结点自身的索引，指针域保存下一个兄弟结点索引
查找某结点的孩子结点很方便
查找某个结点的双亲结点时，最坏要访问所有数组元素与链表结点
"""

class TreeNode(object):
    def __init__(self):
        self.data = '#'
        self.FirstChild = None

class ChildNode(object):
    def __init__(self):
        self.index = -1
        self.NextSibling = None