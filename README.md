# 🔍 Typo Detection Module for Python

**Lightweight, fast, and smart typo detection without any AI or heavy libraries.**

This module helps detect typos in user input using clever logic instead of machine learning. Perfect for CLI tools, forms, or text processing apps where accuracy and speed matter.

---

## 🚀 Features

- ✅ No AI, no bloat – pure logic-based detection
- 🧠 Detects swaps, missing letters, extra letters, etc.
- 📚 Compare against dictionaries or files
- 🔁 Batch typo checking
- ⚡ Super lightweight — no dependencies!

---

## 📦 Installation

Just download [`typo_detection.py`](typo_detection.py) from this repository and import it in your Python project.

```python
from typo_detection import *
```
No `pip install`, no setup, Just use it like a helper file! When you import it, make sure it's in the same directory as your project you're using it in.
## 🛠️ Functions
1. `is_typo(word1, word2)`
Check if a word is a typo of another.
```python
is_typo('hello', 'hlelo') # True
```
2. `string_difference(str1, str2)`
Get the number and list of character-level differences.

```python
string_difference("hello", "hlelo")  
# Output: (2, [('e', 'l'), ('l', 'e')])
```
3. `check_typos(pairs)`
Check a list of (correct_word, typo) pairs.

```python
check_typos([("hello", "hlelo"), ("hello", "world")])
# Output: ([True, False], ["hello", None])
```
4. `check_from_dictionary(word, dictionary, return_closest=False)`
Suggest matching words from a list. If return_closest=True, returns only the best match, even if multiple words have the same difference.

```python
dictionary = ["the", "eth", "abcd", "world", "hello"]
check_from_dictionary("teh", dictionary, return_closest=True)
# Output: 'the'
```
5. `check_from_file(word, file_path, return_closest=False)`
Same as above, but loads dictionary from a .txt file (space or line-separated words).

```python
check_from_file("teh", "dictionary.txt", return_closest=True)
# Output: 'the'
```
## 📖 Full Help
Each function is fully documented. Use Python's built-in help():

```python
help(is_typo) # Or the function name you need help on.
```
## 🤖 Why Not Use AI?
Because this is:

Faster ⏩

Simpler 💡

Lightweight 🧩

Easier to integrate into projects (Not complicated or hard to understand)

No large models, no RAM hogging — just clean, understandable logic. 
***Using heavy AI processing = More complexity, less efficient.***

## 🧑‍💻 Created By
Dhananjoy Bhuyan, 12-year-old coder & builder 🚀
GitHub: [https://github.com/DhananjoyBhuyan](https://github.com/DhananjoyBhuyan)
Feel free to give ⭐️ if you like the project!
