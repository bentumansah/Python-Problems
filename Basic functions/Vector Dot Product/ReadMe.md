# 🎯 Dot Product Calculator in Python

A lightweight and educational Python utility for computing the **dot product** of two vectors. This project showcases two clean and effective methods — one classic and one Pythonic — to help you master vector operations in pure Python.

---

## ✨ Features

- 📌 **Dot Product Computation** for 1D vectors
- 💡 **Two Implementation Styles**:
  - Classic loop-based approach with intermediate products
  - Elegant one-liner using `zip()` and `sum()`
- 🧼 **Pure Python** – No external libraries
- 🧠 **Great for Learning** – Understand both step-by-step and idiomatic Python

---

## 🚀 What Is the Dot Product?

The **dot product** (or scalar product) of two equal-length vectors is the sum of the products of corresponding entries.  
Mathematically:

```

dot(v1, v2) = v1[0]*v2[0] + v1[1]*v2[1] + ... + v1[n]*v2[n]

```

---

## 🧰 Method 1 – Step-by-Step Loop with Tracking

> Ideal for beginners and educators who want to see all operations.

✅ **Example**:

```python
v1 = [1, 2, 3]
v2 = [4, 5, 6]
print(dot(v1, v2))  # Output: 32
```

---

## 🧪 Method 2 – Pythonic List Comprehension

> Fast, clean, and expressive using built-in functions.

✅ **Example**:

```python
v1 = [7, 8]
v2 = [9, 10]
print(dot(v1, v2))  # Output: 7*9 + 8*10 = 143
```

---

## 🧠 Performance & Notes

| Method                 | Style       | Time Complexity | Space Complexity                    |
| ---------------------- | ----------- | --------------- | ----------------------------------- |
| Loop-Based             | Educational | O(n)            | O(n) (stores intermediate products) |
| Pythonic Comprehension | Concise     | O(n)            | O(1) (no extra storage)             |

⚠️ **Note**:

- Vectors must be the **same length**.
- No built-in error checking is implemented.

---

## ▶️ Test case

```python
if __name__ == "__main__":
    v1 = [1, 3, -5]
    v2 = [4, -2, -1]
    print(dot(v1, v2))  # Output: 1*4 + 3*(-2) + (-5)*(-1) = 3
```

---

## 🎓 Educational Use Case

This tool is perfect for:

- Linear algebra tutorials
- High school or college coding exercises
- AI/ML vector math demos
- Embedded systems needing lightweight math functions

---

## 🤝 Contributing

Feel free to contribute by:

- Adding error handling (e.g., unequal lengths)
- Supporting multidimensional arrays
- Writing test cases with `unittest` or `pytest`

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

**Happy Dotting!** 🎯
