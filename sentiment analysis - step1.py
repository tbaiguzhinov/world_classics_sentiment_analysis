from google.cloud import language_v1
import csv
import nltk.data
import nltk
nltk.download('punkt')


client = language_v1.LanguageServiceClient()

path = r"war_and_peace.txt"

with open(path, "r", encoding='utf-8') as file:
    full_text = file.read()

#Splitting the text into sentences
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
text_list = tokenizer.tokenize(full_text)

f = open("war_and_peace.csv", 'w', encoding='UTF8', newline='')
writer = csv.writer(f)

for text in text_list:
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request={"document": document}).document_sentiment
    score = sentiment.score
    row = [text, score]
    writer.writerow(row)
f.close()