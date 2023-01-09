

# from Tree import TreeNode, Tree
#
# f = print
# def print(adres: 'TreeNode') -> None:
#     if isinstance(adres, TreeNode):
#         f(adres.value)
#     else:
#         f(adres)
#
#
# root = TreeNode('F')
# root.add(TreeNode('C'))
# root.add(TreeNode('G'))
# root.add(TreeNode('S'))
# root.add(TreeNode('T'))
# root.add(TreeNode('Y'))
# root.for_each_deep_first(print)
# root.for_each_level_order(print)
# # root.show(TreeNode('T'))
#from BinarySearchTree import *

from Sortowanie import *

l1= [6,1 ,1, 1, 1, 7, 3, 4, 9, 2, 5, 8, 0]
l2= [8, 5, 4, 2, 1, 7, 9, 6, 0, 3]
l3= [3, 4, 0, 7, 1, 5, 2, 8, 9, 6]
l4= [3, 4, 1, 2, 5, 0, 9, 8, 6, 7]
l5= [3, 5, 8, 7, 1, 6, 9, 4, 0, 2]
l6= [0, 7, 9, 4, 8, 6, 5, 3, 2, 1]
l7= [9, 2, 1, 5, 8, 0, 6, 4, 3, 7]
l8= [4, 5, 2, 7, 0, 9, 1, 3, 6, 8]
l9= [0, 8, 2, 7, 6, 3, 9, 1, 5, 4]
l0= [2, 0, 7, 3, 4, 5, 8, 6, 9, 1]

print('ASCENDING ORDER')
print(l1)
print('BubbleSort: ')
bubble_sort(l1)
print(l1)
print('---------------------')
print(l2)
print('insertion_sort: ')
insertion_sort(l2)
print(l2)
print('---------------------')
print(l8)
print('selection_sort: ')
selection_sort(l8)
print(l8)
print('\n')
print('DESCENDING ORDER')


print(l5)
print('BubbleSort: ')
bubble_sort_descending(l5)
print(l5)
print('---------------------')
print(l4)
print('insertion_sort: ')
insertion_sort_descending(l4)
print(l4)
print('---------------------')
print(l9)
print('selection_sort: ')
selection_sort_descending(l9)
print(l9)
print('\n')










