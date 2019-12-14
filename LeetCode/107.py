res = []
cur_layer_node = [root]
while cur_layer_node:
    cur_layer_val = []
    next_layer_node = []
    for node in cur_layer_node:
        if node:
            cur_layer_val.append(node.val)
            next_layer_node.extend([node.left,node.right])
    if cur_layer_val:
        res.insert(0,cur_layer_val)
    cur_layer_node = next_layer_node
return res