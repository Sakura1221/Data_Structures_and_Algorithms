"""
使用链式存储，不必对二叉树进行编号
定义一个结点类，保存结点值，左孩子结点域，右孩子结点域，双亲结点域
"""

class LinkedBinaryTreeNode(object):
    def __init__(self):
        self.data = '#'
        self.LeftChild = None
        self.RightChild = None
        self.Parent = None

class LinkedBinaryTree(object):
    # 二叉树的创建，空结点都设置为#，方便读取
    def __init__(self):
        pass

    # 访问二叉树结点
    def VisitBinaryTreeNode(self,BinaryTreeNode):
        if BinaryTreeNode.data is not '#':
            print(BinaryTreeNode.data)

    # 先序遍历二叉树的递归方法
    def PreOrder(self,Root):
        if Root is not None:
            self.VisitBinaryTreeNode(Root)
            self.PreOrder(Root.LeftChild)
            self.PreOrder(Root.RightChild)

    # 先序遍历二叉树的非递归方法
    # 先序递归的顺序是，根结点，左子结点，右子结点
    # 每个子节点从上至下遍历完所有左子结点，然后从下至上遍历所有右结点
    def PreOrderNonRecursive(self,Root):
        StackTreeNode = [] # 存储结点的栈
        tTreeNode = Root # 保存根结点的变量
        while len(StackTreeNode)>0 or tTreeNode is not None:
            # 一直循环跳转到下一层的左孩子结点，直到左孩子结点为空
            # 最后的空结点#也会入栈，但是不打印
            while tTreeNode is not None:
                self.VisitBinaryTreeNode(tTreeNode)
                StackTreeNode.append(tTreeNode) # 结点遍历后入栈
                tTreeNode = tTreeNode.LeftChild # 根节点被赋值给左孩子结点
            if len(StackTreeNode)>0:
                tTreeNode = StackTreeNode.pop()
                tTreeNode = tTreeNode.RightChild