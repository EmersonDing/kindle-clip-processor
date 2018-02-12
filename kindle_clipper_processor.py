#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_path = 'resource/clip.txt'
output_path = 'resource/output.txt'
chunk_seperator = '=========='


def get_file():
    f = open(input_path, 'r')
    return f

def get_file_string(f):
    s = ''
    for line in f:
        s += line
    return s

def get_chunk(s):
    chunks = s.split(chunk_seperator)
    return chunks

def shaping_chunks(chunks):
    """
    filter empty lines
    shaping string to list
    """
    new_chunks = []
    for chunk in chunks:
        lines = chunk.split('\n')
        new_chunk = list(filter(lambda line: line != '', lines))
        new_chunks.append(new_chunk)
    return new_chunks

def classify_chunks(chunks):
    dict = {}
    for chunk in chunks:
        if len(chunk) <= 2:
            continue
        chunk[0] = chunk[0].replace('(bingshuishenshi@126.com)', '')
        if dict.get(chunk[0]) == None:
            dict[chunk[0]] = []
        dict[chunk[0]].append(chunk[2])
    return dict

def test_chunks(chunks):
    for chunk in chunks:
        if len(chunk) > 3:
            print('chunk size test fail')
            return
    print('chunk size test success')

def print_chunk_dict(chunk_dict):
    for chunk in chunk_dict:
        print('**********')
        print(chunk)
        for line in chunk_dict[chunk]:
            print(line, '\n')
        print('\n')

def print_titles(chunk_dict):
    print("*"*10)
    print("Title:")
    for chunk in chunk_dict:
        print(chunk)
    print("*"*10)

def output_file(chunk_dict):
    f = open(output_path, 'w')
    for chunk in chunk_dict:
        f.write(chunk + '\n')
        for line in chunk_dict[chunk]:
            f.write(line + '\n\n')
        f.write('\n\n')

if __name__ == '__main__':
    f = get_file()
    s = get_file_string(f)
    chunks = get_chunk(s)
    chunks = shaping_chunks(chunks)
    test_chunks(chunks)
    chunk_dict = classify_chunks(chunks)
    print_titles(chunk_dict)
    print_chunk_dict(chunk_dict)
    output_file(chunk_dict)

