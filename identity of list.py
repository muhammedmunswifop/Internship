"""create two lists with the same content and check their identity using is."""
list1 = [1, 2, 3]
list2 = [1, 2, 3]
if list1 is list2:
    print("list1 and list2 are identical.")
else:   
    print("list1 and list2 are not identical.")