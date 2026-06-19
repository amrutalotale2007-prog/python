def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    return lst

numbers = [10, 20, 30, 40]
print("Updated List:", swap(numbers, 0, 2))
