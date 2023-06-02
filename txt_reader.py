#Create a program that can read a list of dictionaries in string format and return it to its original format.
#This was not used in the final product.
def text_read(fl):
    f = open(fl, 'r')
    text = ''
    for sentence in f:
        for letter in sentence:
            if letter != '\n' and letter != ' ':
                if letter == '[':
                    text += '|'
                elif letter == ']':
                    text += '|'
                elif letter == '{':
                    text += '['
                elif letter == '}':
                    text += ']'
                else:
                    text += letter
    text = text.split('|')
    te = []
    for sent in text:
        tex = ''
        for letter in sent:
            if letter == '[':
                tex += '|'
            elif letter == ']':
                tex += '|'
            else:
                tex += letter
        tex = tex.split('|')
        te.append(tex)
    final = []
    for lis in te:
        temp = []
        for l in lis:
            l = l.split(',')
            temp.append(l)
        final.append(temp)
    return final

def text_enumerator(processed_file):
    line_number = 0
    text_enu = []
    for item in processed_file:
        for sentence in item:
            for aspect in sentence:
                if "text" in aspect:
                    text_enu.append((aspect, line_number))
                    line_number += 1
    return text_enu

human_annotations_proc = text_read('PNES_annotations_formatted.txt')
human_annotations_num = text_enumerator(human_annotations_proc)
comment_proc = text_read('parsed_comments.txt')
comment_num = text_enumerator(comment_proc)

def find_matching_tuples(list_1, list_2):
    matches = []

    for set_1, set_2 in zip(list_1, list_2):
        matching_set = []

        for sublist_1, sublist_2 in zip(set_1, set_2):
            matching_tuples = []
            matched_indices = set()

            for tuple_1 in sublist_1:
                string_1 = tuple_1[0]

                for j, tuple_2 in enumerate(sublist_2):
                    if j in matched_indices:
                        continue

                    string_2 = tuple_2[0]

                    if string_1 == string_2:
                        matching_tuples.append(tuple_1)
                        matched_indices.add(j)
                        break

            matching_set.append(matching_tuples)

        matches.append(matching_set)

    return matches



print(find_matching_tuples(human_annotations_num,comment_num))