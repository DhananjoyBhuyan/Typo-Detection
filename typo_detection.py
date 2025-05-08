#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 22:04:55 2025

Created by: Dhananjoy Bhuyan

This typo detection module can help with typos, if you often do typing mistake or you type in a hurry where you can make typos, then use this module, for example if you are taking user input, and user needs to enter some keywords for certain things, then you can use this module, so if the user makes a typo then this module can help to detect and help with that.

Functions of this module:
1. is_typo(word, typo): Checks if typo is a typo of a word. Then returns two things, True and the corrected word if typo is really a typo. If it's not a typo then it just returns false and nothing else.

2. string_difference(str1, str2): returns two things, the differences between the strings and the NUMBER of differences.

3. check_typos(pairs): Check multiple pairs of (string, typo) and return 2 lists, one list of boolean values and one of corrected words, if corrected words[element] is None, that means that was not a typo.

4. check_from_dictionary(word, dictionary, return_closest): Checks if the word is a typo of any of the words in the dictionary, it returns a list of tuples where each tuple has 2 elements: the suggested correction, the number of differences between the suggested word and the provided typo. IF return_closest is set to True, this function will only return the closest word.

5. check_from_file(word, file_path): Same as check_from_dictionary, just loads the dictionary from a given text file, so the second argument needs to be the file path to the text file.

For detailed information on each function, please call "help(<function name>)".

Usage:

>>> is_typo("hello", "hlelo")
True
>>> is_typo("the", "teh")
True
>>> is_typo("haha", "hah")
True
>>> is_typo("world", "hahaha")
False
>>> string_difference("hello", "hlelo")
(2, [('e', 'l'), ('l', 'e')])
>>> check_typos([("hello", "hlelo"), ("hello", "world"), ("hello", "hallo")])
([True, False, True], ["hello", None, "hello"])
>>> dictionary = ["hello", "world", "the"]
>>> check_from_dictionary("teh", dictionary)
[("the", 2)]
>>> dictionary.append("eth")
>>> check_from_dictionary("teh", dictionary)
[("the", 2), ("eth", 2)]
>>> check_from_dictionary("teh", dictionary, return_closest=True)
"the"
>>> check_from_file("teh", "/home/username/AllFiles/dictionary.txt")
[("the", 2), ("tehe", 1), ("eth", 2)]
>>>
>>>

Yaaaay!!

"""

__version__ = "1.0.0"

__all__ = [
    "__version__",
    "is_typo",
    "string_difference",
    "check_typos",
    "check_from_dictionary",
    "check_from_file"]

from typing import List, Optional


def is_typo(string1: str, string2: str) -> (bool, Optional[str]):
    def typo_detect(string: str, typo: str) -> (bool, Optional[str]):
        string = string.lower()
        typo = typo.lower()
        """
        Checks if the second string argument is a typo of the first.
    
        Parameters
        ----------
        string : str
            The main correct string
        typo : str
            The typo
    
        Returns
        -------
        bool, Optional[str]
            True, corrected word if it's a typo of a string else False.
    
        """
        if string == typo:
            return True, string

        l1, l2 = len(string), len(typo)

        if l1 == l2:
            # Case 1: One character is swapped (i.e., only one mismatch)
            diff = [c for c, c2 in zip(typo, string) if c != c2]
            if len(diff) == 1:

                typo = list(typo)
                for i in range(len(typo)):
                    o = typo[i]
                    typo[i] = string[i]
                    if ''.join(typo) == string:
                        return True, string
                    typo[i] = o

            # Case 2: Two adjacent characters flipped
            elif len(diff) == 2:
                for i in range(len(typo) - 1):
                    flipped = typo[i:i + 2][::-1]
                    if ''.join(flipped) == string[i:i + 2]:
                        return True, string

        elif l1 == l2 + 1:
            # Case 3: One extra character in 'string'
            for i in range(len(typo) + 1):
                if string[:i] + string[i+1:] == typo:
                    return True, string

        elif l1 == l2 + 2:
            # Case 4: Two extra characters in 'string'
            for i in range(len(typo) + 1):
                if string[:i] + string[i+2:] == typo:
                    return True, string

        return False
    return typo_detect(string1, string2) or typo_detect(string2, string1)


def string_difference(str1: str, str2: str) -> tuple:
    """
    Return the number of differences and what are the differences, where differece[i] = (c1, c2) c1 and c2 are characters that don't match in both strings, c1 from str1 and c2 from str2

    Parameters
    ----------
    str1 : str
        One of the strings to compare
    str2 : str
        One of the strings to compare

    Returns
    -------
    tuple
        Returns the number of differences and what are the differences, where differece[i] = (c1, c2) c1 and c2 are characters that don't match in both strings, c1 from string1 and c2 from string2

    """
    s1 = str1[:]
    s2 = str2[:]
    if len(str1) < len(str2):
        s1 += " "*(len(str2) - len(str1))
    elif len(str2) < len(str1):
        s2 += " "*(len(str1) - len(str2))
    else:
        pass

    differences = [(c1, c2)
                   for c1, c2 in zip(s1, s2) if c1 != c2]

    return len(differences), differences


def check_typos(pairs: List[tuple[str, str]]) -> tuple[List[bool], List[str]]:
    """


    Parameters
    ----------
    pairs : List[tuple[str, str]]
        pairs of compare.
        These pairs should have the correct string as first element and the given typo as the second.

    Returns
    -------
    (tuple[List[bool], List[str]])
        List of bools, True for is_typo and False for not is_typo.
        List of corrected words.
    """
    typo_bool = []
    correct_words = []
    for w, t in pairs:
        if is_typo(w, t):
            typo_bool.append(True)
            correct_words.append(w)
        else:
            typo_bool.append(False)
            correct_words.append(None)
    return typo_bool, correct_words


def check_from_dictionary(word: str, dictionary: List[str], return_closest: bool = False) -> List[tuple[str, int]]:
    """
    Check the word in a dictionary and return a list of suggested words from the dictionary.

    Parameters
    ----------
    word : str
        The word to check
    dictionary : List[str]
        List of correct words.
    return_closest : bool (default=False)
        if True, this function will return only the word which is closest to the typo.
    Returns
    -------
    string
        the closest word.
    OR
    List[tuple[str, int]]
        List of tuples, where each tuple has 2 elements, suggested word and the difference between the suggested word and the given typo word.

    """
    suggested_words = []
    for i in dictionary:
        if is_typo(i, word):
            suggested_words.append((i, string_difference(i, word)[0]))
    if return_closest == True:
        closest = []
        min_till_now = float('inf')
        for i in suggested_words:
            if i[1] < min_till_now:
                min_till_now = i[1]
        for i in suggested_words:
            if i[1] == min_till_now:
                closest.append(i[0])

        if len(closest) > 1:
            words = {}
            for i in closest:
                for j in range(len(word)):
                    if j == 0:
                        if i[j] == word[j]:
                            if i in words:
                                words[i] += 1
                            else:
                                words[i] = 1
                        else:
                            break
                    else:
                        if i[j] == word[j] and i[j - 1] == word[j - 1]:
                            if i in words:
                                words[i] += 1
                            else:
                                words[i] = 1
                        else:
                            break

            words = {v: k for k, v in words.items()}
            return words[max(list(words.keys()))]
        return closest[0]

    return suggested_words


def check_from_file(word: str, path: str, return_closest: bool = False) -> List[tuple[str, int]]:
    """
    It is same as the detect_typo.check_from_dictionary function, the thing is that it loads the dictionary from a file, the words should be written space or line seperated in the file and it should be a text file.

    Parameters
    ----------
    word : str
        The word to check.
    path : str
        Path to the dictionary file.
    return_closest : bool, default = False
        This works same as the one in the check_from_dictionary() function.
    Returns
    -------
    List[tuple[str, int]]
        List of tuples, where each tuple has 2 elements, suggested word and the difference between the suggested word and the given typo word.


    """
    with open(path) as f:
        words = f.read().split()

    return check_from_dictionary(word, words, True) if return_closest else check_from_dictionary(word, words)
