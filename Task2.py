list=[1,2,3,4,5,6,7,8,9,10]
e_list=list[0:5]
r_list=e_list[-1:-len(e_list)-1:-1]
print(f"Original list: {list}")
print(f"Extracted first five elements: {e_list}")
print(f"Reversed extracted elements: {r_list}")
e_list.reverse()
print(f"Reversed extracted elements: {e_list}")