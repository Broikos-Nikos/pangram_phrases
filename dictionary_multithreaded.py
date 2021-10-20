import csv
import time
import logging
#from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing.pool import ThreadPool

logging.basicConfig(filename='unique_letter_phrases.log', level=logging.DEBUG)
lettercheck='Start phrase check'
start_time = time.time()
dictionary = []
phrases_min_length = []


print('Start: '+str(start_time))
logging.info('Start: '+str(start_time))

with open('dictionary.csv', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        dictionary.append(row[0].lower().strip())
print('Finished importing dictionary: '+str(time.time() - start_time))
logging.info('Finished importing dictionary: '+str(time.time() - start_time))

unique_lettered_words = []
for row in dictionary:
    if( (len(set(row)) == len(row)) ):
        unique_lettered_words.append(row.strip())
print('Finished filtering unique lettered words: '+str(time.time() - start_time))
logging.info('Finished filtering unique lettered words: '+str(time.time() - start_time))

unique_lettered_words=sorted(unique_lettered_words)
unique_lettered_words = unique_lettered_words[1::10]

unique_lettered_2words = []    
for word1 in unique_lettered_words:
    for word2 in unique_lettered_words:
        if( (len(set(""+word1+word2)) == len(""+word1+word2)) ):
            unique_lettered_2words.append((""+word1+word2).strip())
print('Finished filtering unique lettered 2 words: '+str(time.time() - start_time))
logging.info('Finished filtering unique lettered 2 words: '+str(time.time() - start_time))

unique_lettered_4words = []
unique_lettered_2words_length = len(unique_lettered_2words)
middle_index = unique_lettered_2words_length//2




def my_function(phrase1):
    global unique_lettered_2words
    global unique_lettered_4words
    for phrase2 in unique_lettered_2words[:middle_index]:
        if( (len(set(""+phrase1+phrase2)) == len(""+phrase1+phrase2)) ):
            #print('checking: '+phrase1+''+phrase2)
            unique_lettered_4words.append(""+phrase1+phrase2)
            #return (""+phrase1+phrase2)
            




pool = ThreadPool(6)
pool.map(my_function, unique_lettered_2words[:middle_index])
#unique_lettered_4words=pool.map(my_function, unique_lettered_2words[:middle_index])








unique_lettered_5words = []
for word in unique_lettered_words:
    for phrase in unique_lettered_4words:
        if( lettercheck!=word[0] ):
            print(lettercheck+": "+str(time.time() - start_time) )
            lettercheck=word[0]
        if( (len(set(""+word+phrase)) == len(""+word+phrase)) ):
            #print(""+word+phrase)
            unique_lettered_5words.append(""+word+phrase)
print('Finished filtering unique lettered 5 words: '+str(time.time() - start_time))
logging.info('Finished filtering unique lettered 5 words: '+str(time.time() - start_time))





phrasescsv = open('phrases.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(phrasescsv)
for item in unique_lettered_5words:
    writer.writerow([item])
    if( len(item)>18 ):
        phrases_min_length.append(item)
    


print('Finished phrases: '+str(time.time() - start_time))
logging.info('Finished phrases: '+str(time.time() - start_time))
logging.info('---')




