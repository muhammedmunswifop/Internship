"""11.Write a function that accepts a list and returns the largest element."""
def largest_element(lst):
    return max(lst)
nums = list(map(int, input("Enter numbers: ").split()))
print("The largest element is:", largest_element(nums))
