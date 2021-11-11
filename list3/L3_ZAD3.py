def counting_chars_without_ifs(filename):
    """
    Count the number of all characters appearing in given file.
    :param fiename: file .txt with the text
    :return: dictionary with every character that appeared in the given file
    """
    file_ref = open(filename, 'r')
    text = file_ref.read()
    low_text = text.lower()
    striped_text = ''.join(low_text.split())
    char_count = {i:striped_text.count(i) for i in set(striped_text)}  
    return char_count