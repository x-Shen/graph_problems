class avl_tree:
    def __init__(self,key,value,parent):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
        self.balance_factor = 0
        
    def has_left_child(self):
        if self.left != None:
            return True
        return False
    def has_right_child(self):
        if self.right != None:
            return True
        return False
    def is_left_child(self):
        if self.parent == None:
            return False
        if self.parent.left.value == self.value:
            return True
        return False
    def is_right_child(self):
        if self.parent == None:
            return False
        if self.parent.right.value == self.value:
            return True
        return False
    def put(self, key, value, cur_node):
        if cur_node.key == None:
            cur_node.key = key
            cur_node.value = value
            return
        if key < cur_node.value:
            if cur_node.has_left_child():
                self.put(key,value,cur_node.left)
            else:
                cur_node.left = avl_tree(key,value,cur_node)
                self.balance(cur_node.left)
        else:
            if cur_node.has_right_child():
                self.put(key,value,cur_node.right)
            else:
                cur_node.right = avl_tree(key,value,cur_node)
                self.balance(cur_node.right)
                
    def rebalance(self,node):
        if node.balance_factor < 0:
            if node.right.balanceFactor > 0:
                self.rotate_right(node.right)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
            
        elif node.balance_factor > 0:
            if node.left.balance_factor < 0:
                self.rotate_left(node.left)
                self.rotate_right(node)
            else:
                self.rotate_right(node)
                
    def balance(self,node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1
            if node.parent.balance_factor != 0:
                self.balance(node.parent)

    def rotate_left(self,rot_root):
        new_root = rot_root.right
        rot_root.right = new_root.left
        if new_root.left != None:
            new_root.left.parent = rot_root
            new_root.parent = rot_root.parent
        if rot_root.parent == None:
            self.root = new_root
        else:
            if rot_root.is_left_child():
                rot_root.parent.left = new_root
            else:
                rot_root.parent.right= new_root
        new_root.left = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = rot_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(rot_root.balance_factor, 0)

    def rotate_right(self,rot_root):
        new_root = rot_root.left
        rot_root.left = new_root.right
        if new_root.right != None:
            new_root.right.parent = rot_root
            new_root.parent = rot_root.parent
        if rotRoot.parent == None:
            self.root = new_root
        else:
            if rot_root.is_right_child():
                rot_root.parent.right = new_root
            else:
                rot_root.parent.left= new_root
        new_root.left = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = rot_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        newRoot.balance_factor = new_root.balance_factor + 1 + max(rot_root.balance_factor, 0)
    def search(self,cur_node,key):
        if cur_node.left == None and cur_node.right == None and cur_node.key != key:
            return False
        if cur_node.key == key:
           return True
        elif key < cur_node.key:
            return self.search(cur_node.left,key)
        else:
            return self.search(cur_node.right,key)
        


class improved_adjacent_list:
    def __init__(self,nodes,edges):
        self.list = []
        self.node_c = len(nodes)
        for node in nodes:
            # nodes are list of integer
            self.list.append((node,avl_tree(None,None)))
        for edge in edges:
            #e edges are tuples (start,dest, weight)
            self.list[edge[0]][1].put(edge[1], weight,self.list[edge[0]][1])
    
    def search(self,s,d):
       tree = self.list[s][1]
       return tree.search(tree, d)

    def add_node(self):
        self.list.append((self.node_c+1,avl_tree(None,None)))
        self.node_c+=1
        
    def add_edge(self,s,d,w):
        self.list[s][1].put(d,w,self.list[s][1])
    def del_node(self,s):
        self.list[s] = None
    def del_edge(self,s,d,w):
        pass
       
                             
            
    
                
