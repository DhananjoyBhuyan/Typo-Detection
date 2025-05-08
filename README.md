# Python project, runs in python only.
# Detect typos with ease!!!
Just download the [typo_detection.py](typo_detection.py) file from this repo.
It is way better than normal typo detectors, it has a solid logic and a lot of functions. Plus, it's simple and easy to use. If you're taking user inputs, this can be very helpful, way better than other typo detectors.
## Functions in it:
1. is_typo(correct_word, typo) Detects and tells if it's a typo.
2. string_difference(string1, string2) Tells the difference in the strings.
3. check_typos(pairs) Checks a batch of (correct, typo) pairs
4. check_from_dictionary(word, dictionary, return_closest=default False) if return_closest is True, return the closest word, else return a list of suggested words, and if return_closest is given but 2 words have the same number of differences like `typo=teh` and `words = ['the', 'eth']`, then also it will return 'the' because it's the closest even if 'eth' has the same number of differences. It has a seperate part of code to handle words with same number of differences.
5. check_from_file(word, file_path, return_closest) Same as check_from_dictionary, but it loads the dictionary from the file.
# Check `help(function_name)` for more details about each function.
