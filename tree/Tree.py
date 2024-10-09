class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')

    def size(self, root):
        if root is None:
            return 0
        l_count = self.size(root.left)
        r_count = self.size(root.right)
        return l_count + r_count + 1

    def depth(self, root):
        if root is None:
            return 0
        l_depth = self.depth(root.left)
        r_depth = self.depth(root.right)
        return l_depth + 1 if l_depth > r_depth else r_depth + 1

    def search(self, root, data):
        if root is None:
            print('Root is empty')
            return False
        if root.data == data:
            return True
        return self.search(root.left, data) | self.search(root.right, data)


if __name__ == '__main__':
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)
    node.right.left = Node(6)
    node.right.right = Node(7)

    print("Inorder Traversal:")
    node.inorder(node)
    print("\nPreorder Traversal:")
    node.preorder(node)
    print("\nPostorder Traversal:")
    node.postorder(node)
    print()
    print(f'size is {node.size(node)}')
    print(f'depth is {node.depth(node)}')
    print(f'search is {node.search(node, 5)}')
