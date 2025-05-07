#!/usr/bin/env python3

def return_evens(num_list):
    even_list= [num_list[i] for i in range(len(num_list)) if num_list[i]%2 == 0]
    return even_list

def make_exclamation(sentence_list):
    exclamated = [f"{sentence}!" for sentence in sentence_list]
    return exclamated