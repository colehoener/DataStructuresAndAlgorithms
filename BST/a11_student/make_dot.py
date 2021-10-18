from bst_key import node, BST

#Opens and clears file
def get_file(target):
    try:
        f = open(target, 'r+')
        f.truncate(0)
        return f
    except FileNotFoundError:
        print("File not found {}".format(target))

#writes each node to the file
def dot(node, f):
    if node.left:
        f.write('\tnode_%d [ label="%d"];\n' % ((node.getLeft()).getValue(), (node.getLeft()).getValue()))
        dot(node.left, f)
    else:
        f.write('\tnode_null_l_%d [label="Null", shape=none];\n' % node.getValue())

    if node.right:
        f.write('\tnode_%d [ label="%d"];\n' % ((node.getRight()).getValue(), (node.getRight()).getValue()))
        dot(node.right, f)
    else:
        f.write('\tnode_null_r_%d [label="Null", shape=none];\n' % node.getValue())

#writes each nodes child to file
def dot2(node, f):
    if node.left:
        f.write('\tnode_%d -> node_%d;\n' % (node.value, node.left.value))
        dot2(node.left, f)
    else:
        f.write('\tnode_%d -> node_null_l_%d;\n' % (node.value, node.getValue()))

    if node.right:
        f.write('\tnode_%d -> node_%d;\n' % (node.value, node.right.value))
        dot2(node.right, f)
    else:
        f.write('\tnode_%d -> node_null_r_%d;\n' % (node.value, node.getValue()))


#prompts user
print("Enter list of intergers (space seperated):")
integersInput = input()
integers = [int(i) for i in integersInput.split(' ')]

tree = BST()
for x in integers:
    tree.insert(x)

print("Enter Target file (some.dot):")
target = input()
f = get_file(target)

#starts writing to file
f.write("digraph {\n")
f.write('\tnode_%d [ label="%d"];\n' % ((tree.getRoot()).getValue(), (tree.getRoot()).getValue()))
dot(tree.getRoot(), f)
dot2(tree.getRoot(), f)
#end of file        
f.write('}')

print("Dot Code saved in %s" % target)