"""12.Write a function that accepts a list and returns the smallest element."""
def smallest_element(lst):
    return min(lst)
nums = list(map(int, input("Enter numbers: ").split()))
print("The largest element is:", smallest_element(nums))
