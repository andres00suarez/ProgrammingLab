def sum_list  (numbers):
    """Returns the sum of a list of numbers."""
    sum = 0
    if numbers == []:
        return None   # Return None if the list is empty
    for number in numbers:
        sum += number
    return sum