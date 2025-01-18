def get_middle_element(lst):
    if not lst:
        return None  # Return None if the list is empty
    mid_index = len(lst) // 2
    return lst[mid_index]

# Example usage
my_list = [1, 2, 3, 4, 5]
print(get_middle_element(my_list))  # Output: 3
