# 🔢 Matrix Multiplication Utility in Python

A compact and flexible Python module that demonstrates two efficient techniques for performing **matrix multiplication**. Whether you're a student, developer, or educator, this tool is perfect for learning and integrating linear algebra operations into your projects.

---

## ✨ Features

- 🧮 **Matrix Multiplication**: Multiply two 2D lists (matrices) in pure Python.
- 🛠️ **Two Implementations**:
  - **Nested Loop Approach** (classic, educational)
  - **List Comprehension Approach** (Pythonic and concise)
- 💡 **No Dependencies**: Built with pure Python — no NumPy required!
- 📚 **Great for Learning**: Understand both fundamental and modern Python styles.

---

## 📌 Prerequisites

- Python 3.6+
- Two valid matrices where the **number of columns in A equals the number of rows in B**

---

## 1️⃣ Method 1 — Classic Nested Loop Implementation

> A step-by-step approach using explicit loops for clarity and control.

✅ **Example**:

```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(array_mult(A, B))  # Output: [[19, 22], [43, 50]]
```

---

## 2️⃣ Method 2 — List Comprehension Style (Concise & Pythonic)

> Elegant and faster for small to medium matrices using `zip` and comprehensions.

✅ **Example**:

```python
A = [[2, 3], [4, 5]]
B = [[6, 7], [8, 9]]
print(array_mult(A, B))  # Output: [[36, 41], [64, 73]]
```

---

## 🧠 Performance & Notes

| Method             | Style            | Time Complexity | Space Complexity |
| ------------------ | ---------------- | --------------- | ---------------- |
| Nested Loops       | Classic          | O(n × m × p)    | O(n × p)         |
| List Comprehension | Pythonic & Clean | O(n × m × p)    | O(n × p)         |

- `A`: n × m matrix
- `B`: m × p matrix
- Result: n × p matrix

📝 **Note**: The function assumes all rows are of equal length (well-formed matrices). No internal validation is performed for mismatched sizes.

---

## ▶️ Test case

```python
if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]

    print(array_mult(A, B))
    # Output: [[58, 64], [139, 154]]
```

---

## 🧪 Suggested Enhancements

- Add matrix validation for robustness.
- Raise exceptions for dimension mismatches.
- Extend for NumPy backend optionally.

---

## 🤝 Contributing

Pull requests are welcome!
You can help improve performance, add type annotations, or support sparse matrices.

Steps:

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Submit a Pull Request 🚀

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

**Happy Coding!** 🧮 Let your matrices multiply with elegance.
