import os
import pandas as pd
import stanza #https://stanfordnlp.github.io/stanza/index.html
stanza.download('en') # download English model

#Retrieves each document as a panda dataframe ands adds it to a list.
comments = []
comment_count = 0
for num in range(3):
  url = 'https://raw.githubusercontent.com/LynnaNeri/rPNESsupport/main/comments/' + str(comment_count) + '.csv'
  comments.append(pd.read_csv(url)) #https://towardsdatascience.com/3-ways-to-load-csv-files-into-colab-7c14fcbdcb92
  comment_count += 1

#Create a list of each entry with its list of ids.
all_comments=[]
for item in comments:
  li = item['body'].tolist()
  ide = item['id'].tolist()
  all_comments.append((ide,li))

#Attach the id to the entry.
sorted_comments = []
for item in all_comments:
  count = 0
  idlist = item[0]
  textlist = item[1]
  for id in item[0]:
    sorted_comments.append((id,textlist[count]))
    count+=1

#Parse each entry.
nlp = stanza.Pipeline('en') # initialize English neural pipeline
parsed_comments = open("parsed_comments.txt", "w") #https://www.scaler.com/topics/python/how-to-write-a-file-in-python/
count = 0
for comment in sorted_comments:
  entry = comment[1]
  try:
    doc = nlp(entry)
    parsed_comments.write(str((comment[0],doc)))
    print(os.path.abspath('parsed_comments.txt'), count)
  except:
    print('Empty text.')
  count += 1