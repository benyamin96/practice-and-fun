class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node=Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right
            else:
                if temp.left is None :
                    temp.left = new_node
                    return True
                temp=temp.left
    
    def contains(self, value):
        temp=self.root
        while temp is not None:
            if value < temp.value:
                temp=temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def get_min_value(self):
        temp = self.root
        while temp.left:
            temp = temp.left
        return temp.value



my_tree=BinarySearchTree()

my_tree.insert(52)
my_tree.insert(28)
my_tree.insert(89)
my_tree.insert(80)
my_tree.insert(2)
my_tree.insert(22)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

print(my_tree.contains(100))
print("Min Value in the tree: ", my_tree.get_min_value())
