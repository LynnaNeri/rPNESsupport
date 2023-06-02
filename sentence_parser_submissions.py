import os
import pandas as pd
import stanza #https://stanfordnlp.github.io/stanza/index.html
stanza.download('en') # download English model

#Retrieves each document as a panda dataframe ands adds it to a list.
submissions = []
submission_count = 0
for num in range(3):
  url = 'https://raw.githubusercontent.com/LynnaNeri/rPNESsupport/main/submissions/' + str(submission_count) + '.csv'
  submissions.append(pd.read_csv(url)) #https://towardsdatascience.com/3-ways-to-load-csv-files-into-colab-7c14fcbdcb92
  submission_count += 1

#Create a list of each entry with its list of ids.
all_submissions=[]
for item in submissions:
  li = item['selftext'].tolist()
  ide = item['id'].tolist()
  all_submissions.append((ide,li))

#Attach the id to the entry.
sorted_submissions = []
for item in all_submissions:
  count = 0
  idlist = item[0]
  textlist = item[1]
  for id in item[0]:
    sorted_submissions.append((id,textlist[count]))
    count+=1

#Parse each entry.
nlp = stanza.Pipeline('en') # initialize English neural pipeline
parsed_submissions = open("parsed_submissions.txt", "w") #https://www.scaler.com/topics/python/how-to-write-a-file-in-python/
count = 0
for submission in sorted_submissions:
  entry = submission[1]
  try:
    doc = nlp(entry)
    parsed_submissions.write(str((submission[0],doc)))
    print(os.path.abspath('parsed_submissions.txt'), count)
  except:
    print('Empty text.')
  count += 1