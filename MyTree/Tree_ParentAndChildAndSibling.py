"""
双亲孩子兄弟表示法，在二叉树表示法基础上为每个结点增加parent域
存储树的结点时，每个结点包括4个部分，即结点值data、该结点双亲结点的索引pParent，该结点第一个孩子结点的索引pFirstChild、
该结点下一个兄弟结点索引pNextSibling
便于查找结点的孩子结点和兄弟结点，从当前结点查找双亲结点比较困难，最坏要访问树中所有结点
"""

class TreeNode(object):
    def __init__(self):
        self.data = '#'
        self.pParent = None
        self.pFirstChild = None
        self.pNextSibling = None