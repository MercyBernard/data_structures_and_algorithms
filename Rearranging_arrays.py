a = [3, 5, 2, 6, 8, 4, 4, 6, 4, 4, 3]
x = 5

def rearrange_array(a, x):
    pivot = a[5]

    less_than = []
    equal_to = []
    greater_than = []

    for i in a:
        if i < pivot:
            less_than.append(i)
        elif i == pivot:
            equal_to.append(i)
        else:
            greater_than.append(i)

    result = less_than + equal_to + greater_than
    return result

output_array = rearrange_array(a, x)
print(output_array)