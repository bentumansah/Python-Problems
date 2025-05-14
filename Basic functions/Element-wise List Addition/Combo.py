def add_two_lists_loop(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result

def add_two_lists_zip(a, b):
    return [x + y for x, y in zip(a, b)]

if __name__ == "__main__":
    a = [10, 20, 30]
    b = [5, 3, 1]

    print("Loop method:", add_two_lists_loop(a, b))  # Output: [15, 23, 31]
    print("Zip method:", add_two_lists_zip(a, b))    # Output: [15, 23, 31]