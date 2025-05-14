# 🥈 Second Largest Element in an Array (Python)

A compact and educational Python utility showcasing **three distinct approaches** to find the second largest element in an array. Great for coding interviews, algorithm practice, and real-world logic implementations.

---

## ✨ Features

- ✅ **Three Implementations**:
  - Double Traversal (Simple and clear)
  - Single Traversal (Optimized)
  - Sorting-based (Straightforward)
- 🧠 **Great for Learning**: Helps understand trade-offs in algorithm design.
- 🧩 **No Dependencies**: 100% pure Python.
- 📎 **Reusable Code**: Easily integrable into other projects or teaching material.

---

## 🔧 Method 1 – Sorting-Based Approach

> Sort the array, then traverse backward from the second last element to find the second largest.

### ✅ Example 1

```python
arr = [10, 5, 10]
print(getSecondLargest_sorted(arr))  # Output: 5
```

### ⏱️1st Time Complexity

- **O(n log n)**: Due to sorting.
- **Space**: O(1)

---

## ⚡ Method 2 – Double Traversal (Naive)

> Traverse the array twice: once to find the maximum, and once to find the second maximum.

### ✅ Example 2

```python
arr = [10, 10, 10]
print(getSecondLargest_double_traversal(arr))  # Output: -1
```

### ⏱️ 2nd Time Complexity

- **O(n)**: Two separate traversals.
- **Space**: O(1)

---

## 🔍 Method 3 – Single Traversal (Optimized)

> Track both the largest and second largest in one pass.

### ✅ Example 3

```python
arr = [12, 35, 1, 10, 34, 1]
print(getSecondLargest_single_traversal(arr))  # Output: 34
```

### ⏱️ 3rd Time Complexity

- **O(n)**: Single traversal.
- **Space**: O(1)

---

## 🧠 Test case

```python
if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]

    print("Double Traversal:", getSecondLargest_double_traversal(arr))
    print("Single Traversal:", getSecondLargest_single_traversal(arr))
    print("Sorted Approach:", getSecondLargest_sorted(arr))
```

---

## 📝 Notes

- ⚠️ **Assumes integer values**. Modify as needed for floats or other types.
- 📈 All methods return `-1` if no second distinct largest element is found.
- 🧪 Good practice for sorting, iteration, and logic implementation.

---

## 🤝 Contributing

Improvements and optimizations are welcome!
Ideas:

- Add input validation.
- Handle arrays with fewer than two elements.
- Use Python's `heapq` or `set` for alternate methods.

Fork the repo, make your changes, and submit a pull request!

---

## 📄 License (MIT)

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
```

---

**Happy Coding!** 💡 Explore logic, learn patterns, and master algorithms.
