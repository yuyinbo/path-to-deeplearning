# 作者: 余殷博
# cangj87@gmail.com


class Node(object):
    """
    节点类
    """

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """
    树类
    """

    def __init__(self):
        self.root = None
        self.queue = []  # 辅助队列

    def add_node(self, elem):
        node = Node(elem)
        self.queue.append(node)
        # 判断树根是否为None
        if self.root is None:
            self.root = node
        elif self.queue[0].lchild is None:
            self.queue[0].lchild = node
        # 如果辅助队列头的左孩子为空，则将新节点作为左孩子
        elif self.queue[0].rchild is None:
            self.queue[0].rchild = node
            self.queue.pop(0)
            # 队头的孩子满了，出队

    def pre_order(self, current_node: Node):
        if current_node:
            print(current_node.elem, end=' ')
            self.pre_order(current_node.lchild)
            self.pre_order(current_node.rchild)

    def mid(self):
        pass


if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 11):
        tree.add_node(i)
    tree.pre_order(tree.root)
