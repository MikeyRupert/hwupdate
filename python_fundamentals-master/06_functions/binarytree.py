def parent(node):
    if node is node.tree.root:
        return None
    else:
        x = node
        y = node
        while True:
            if is_thread(y):
                p = y.right
                if p is None or p.left is not node:
                    p = x
                    while not is_thread(p.left):
                        p = p.left
                    p = p.left
                return p
            elif is_thread(x):
                p = x.left
                if p is None or p.right is not node:
                    p = y
                    while not is_thread(p.right):
                        p = p.right
                    p = p.right
                return p
            x = x.left
            y = y.right