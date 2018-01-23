# coding: utf-8
import binary_tree
import tree

x=tree.tree(1000)
y=tree.tree(2000)
z=tree.tree(3000)
w=tree.tree(6)
v=tree.tree(7)
r = tree.tree(8)
u = tree.tree(2)
x.AddSuccessor(y)
x.AddSuccessor(z)
c=tree.tree(5)
z.AddSuccessor(c)
y.AddSuccessor(w)
y.AddSuccessor(v)
w.AddSuccessor(r)
y.AddSuccessor(u)            
     
      
        
test = binary_tree.binary_tree(100)
test2 = binary_tree.binary_tree(200)
test3 = binary_tree.binary_tree(300)
test4 = binary_tree.binary_tree(400)
test5 = binary_tree.binary_tree(500)
test6 = binary_tree.binary_tree(600)
test7 = binary_tree.binary_tree(7)

test.AddLeft(test2)
test.AddRight(test3)
test2.AddLeft(test4)
test2.AddRight(test5)

test3.AddLeft(test6)

test5.AddRight(test7)

#print test.store[1][0].store[0]
#print test.store[0]
#print test.store[2][0].store[0]


a = tree.tree('A')
b = tree.tree('B')
c = tree.tree('C')
d = tree.tree('D')
e = tree.tree('E')
f = tree.tree('F')
g = tree.tree('G')
h = tree.tree('H')
i = tree.tree('I')
j = tree.tree('J')
k = tree.tree('K')
l = tree.tree('L')

a.AddSuccessor(b)
a.AddSuccessor(c)
a.AddSuccessor(d)
a.AddSuccessor(e)

b.AddSuccessor(f)
b.AddSuccessor(g)

c.AddSuccessor(h)
c.AddSuccessor(i)
c.AddSuccessor(j)

e.AddSuccessor(k)
k.AddSuccessor(l)



print x.Get_LevelOrder()
x.Print_DepthFirst()

convertedbinary = x.ConvertToBinaryTree()
print convertedbinary.Get_LevelOrder()
convertedbinary.Print_DepthFirst()


#print convertedbinary.store[0] #1000
#print convertedbinary.store[1][0].store[0] #2000
#print convertedbinary.store[1][0].store[1][0].store[0] #6
#print convertedbinary.store[1][0].store[2][0].store[0] #3000
#print convertedbinary.store[1][0].store[1][0].store[1][0].store[0] #8
#print convertedbinary.store[1][0].store[1][0].store[2][0].store[0] #7
#print convertedbinary.store[1][0].store[2][0].store[1][0].store[0] #5
#print convertedbinary.store[1][0].store[1][0].store[2][0].store[2][0].store[0] #2

restoredTree = convertedbinary.ConvertToTree()

print restoredTree[1].Get_LevelOrder()
restoredTree[1].Print_DepthFirst()
