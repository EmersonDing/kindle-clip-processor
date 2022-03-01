#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_path = 'resource/clip.txt'
output_path = 'resource/output.txt'
chunk_delimiter = '=========='


def get_file():
    f = open(input_path, 'r')
    return f


def get_file_string(f):
    s = ''
    for line in f:
        s += line
    return s


def get_raw_chunk(s):
    """
    Chunk is combined with title | metadata | paragraph, e.g.:
    ```
        舞!舞!舞!
        - 您在位置 #133-134的标注 | 添加于 2015年9月24日星期四 上午5:08:43
        我这人决没有什么不正常。 我的确如此认为。
    ```
    """
    return s.split(chunk_delimiter)


def normalize_chunks(chunks):
    """
    filter empty lines.
    transform string to list.
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
        # Some clips have email addr in title, e.g. "title (email)"
        title = chunk[0].replace('(bingshuishenshi@126.com)', '')
        if dict.get(title) is None:
            dict[title] = []
        dict[title].append(chunk[2])
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
    print("*" * 10)
    print("Title:")
    for chunk in chunk_dict:
        print(chunk)
    print("*" * 10)


def output_file(chunk_dict):
    f = open(output_path, 'w')

    f.write("Titles \n")
    for chunk in chunk_dict:
        f.write(chunk + '\n')
    f.write("{} \n\n".format("=" * 10))

    f.write("Novels \n")
    for chunk in chunk_dict:
        f.write(chunk + '\n')
        for line in chunk_dict[chunk]:
            f.write(line + '\n\n')
        f.write('\n\n')

    f.close()


if __name__ == '__main__':
    f = get_file()
    s = get_file_string(f)
    raw_chunks = get_raw_chunk(s)
    normalized_chunks = normalize_chunks(raw_chunks)
    test_chunks(normalized_chunks)
    chunk_dict = classify_chunks(normalized_chunks)
    print_titles(chunk_dict)
    print_chunk_dict(chunk_dict)
    output_file(chunk_dict)
