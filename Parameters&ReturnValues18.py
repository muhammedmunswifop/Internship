"""18.Write a function that accepts a list and returns only the even numbers."""
def even_numbers(lst):
    even_list = []
    for num in lst:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(even_numbers(numbers))