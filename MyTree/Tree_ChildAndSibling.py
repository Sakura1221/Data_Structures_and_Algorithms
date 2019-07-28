"""
孩子兄弟表示法（又称为二叉树表示法或二叉链表表示法）
存储树的结点时，每个结点包括3各部分，即结点值data、该结点第一个孩子结点的索引pFirstChild、
该结点下一个兄弟结点索引pNextSibling
便于查找结点的孩子结点和兄弟结点，从当前结点查找双亲结点比较困难，最坏要访问树中所有结点
"""

class TreeNode(object):
    def __init__(self):
        self.data = '#'
        self.pFirstChild = None
        self.pNextSibling = None