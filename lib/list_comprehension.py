#!/usr/bin/env python3


def return_evens(num_list):
    """Returns a list of even numbers from an inputted list"""
    return [n for n in num_list if n % 2 == 0]


def make_exclamation(sentence_list):
    """Adds an exclamation mark to each string element from an inputted list"""
    exclamation_list = list((s + "!") for s in sentence_list)
    return exclamation_list
