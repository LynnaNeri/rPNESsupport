#Import data.
import human_annotations as human
import parsed_comments as comments
import parsed_submissions as submissions

#Create data variables.
a = human.human_annotations
c = comments.parsed_comments
s = submissions.parsed_submissions

#Create a list of all of the sentences.
test_data = []
for a_sentence in a:
    for c_sentence in c:
        if a_sentence[0] == c_sentence[0]:
            test_data.append(c_sentence)
    for s_sentence in s:
        if a_sentence[0] == s_sentence[0]:
            test_data.append(s_sentence[0])

#Create list of the Stanza annotations.
test_words = []
for ann in test_data:
    for sl in ann[1:]:
        for s in sl:
            for w in s:
                for key in w.keys():
                    if (key == "head") or (key == "deprel"):
                        test_words.append((ann[0], key, w[key]))

#Create list of the human annotations.
a_words = []
for annotation in a:
    for sentence_list in annotation[1:]:
        for sentence in sentence_list:
            for word in sentence:
                for key in word.keys():
                    if (key == "head") or (key == "deprel"):
                        a_words.append((annotation[0], key, word[key])) 

#Compare the Stanza and the human annotations.
matching_keys = 0
mismatching_keys = 0
matching_words = []
mismatching_words = []
for i in a_words: #https://devqa.io/python-compare-two-lists-of-dictionaries/
    if i in test_words:
        matching_words.append(i)
    else:
        mismatching_words.append(i)

#Find the percentage of matching annotaions.
total_keys = len(matching_words) + len(mismatching_words)
accuracy = len(matching_words)/total_keys

print("Matching Keys:", len(matching_words))
print("Mismatching Keys:", len(mismatching_words))
print("Accuracy:", accuracy)

#Create a list of Stanza's annotations for head.
h_test_words = []
for ann in test_data:
    for sl in ann[1:]:
        for s in sl:
            for w in s:
                for key in w.keys():
                    if (key == "head"):
                        h_test_words.append((ann[0], key, w[key]))

#Create a list of human annotations for head.
h_a_words = []
for annotation in a:
    for sentence_list in annotation[1:]:
        for sentence in sentence_list:
            for word in sentence:
                for key in word.keys():
                    if (key == "head"):
                        h_a_words.append((annotation[0], key, word[key])) 

#Compare the Stanza and human annotations for head.
h_matching_keys = 0
h_mismatching_keys = 0
h_matching_words = []
h_mismatching_words = []
for i in h_a_words: #https://devqa.io/python-compare-two-lists-of-dictionaries/
    if i in h_test_words:
        h_matching_words.append(i)
    else:
        h_mismatching_words.append(i)

#Find the percentage of matching annotations for head.
h_total_keys = len(h_matching_words) + len(h_mismatching_words)
h_accuracy = len(h_matching_words)/h_total_keys

print("Head Matching Keys:", len(h_matching_words))
print("Head Mismatching Keys:", len(h_mismatching_words))
print("Head Accuracy:", h_accuracy)

#Make a list of Stanza's deprel annotations.
d_test_words = []
for ann in test_data:
    for sl in ann[1:]:
        for s in sl:
            for w in s:
                for key in w.keys():
                    if (key == "deprel"):
                        d_test_words.append((ann[0], key, w[key]))

#Make a list of human deprel annotations.
d_a_words = []
for annotation in a:
    for sentence_list in annotation[1:]:
        for sentence in sentence_list:
            for word in sentence:
                for key in word.keys():
                    if (key == "deprel"):
                        d_a_words.append((annotation[0], key, word[key])) 

#Compare the Stanza and human deprel annotations.
d_matching_keys = 0
d_mismatching_keys = 0
d_matching_words = []
d_mismatching_words = []
for i in d_a_words: #https://devqa.io/python-compare-two-lists-of-dictionaries/
    if i in d_test_words:
        d_matching_words.append(i)
    else:
        d_mismatching_words.append(i)

#Find the percentage of matching annotations for deprel.
d_total_keys = len(d_matching_words) + len(d_mismatching_words)
d_accuracy = len(d_matching_words)/d_total_keys

print("Deprel Matching Keys:", len(d_matching_words))
print("Deprel Mismatching Keys:", len(d_mismatching_words))
print("Deprel Accuracy:", d_accuracy)