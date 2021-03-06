import csv

texts = ['trade-wars-news1.txt','trade-wars-news2.txt','trade-wars-news3.txt','trade-wars-news4.txt','trade-wars-news5.txt']
trade_wars_news = []
for i in texts:
    f = open(i,'r')
    contents=f.read()
    trade_wars_news.append(contents)
# trade_wars_news

all_articles = []
for i in range(5):                    ## helped by helper
    words = trade_wars_news[i].split()
    for m in words:
        all_articles.append(m)
# all_articles

meaningful_words = []                 ## helped by Gaochao
stop_words = ["the", "and", "of", "a", "in","to","that","is","on","as","with","The","for","it",
              "has","are","not","have","its","from","would","be","at","an","which","by","up",
              "this","said","also","will","about","more","last","was","been","they","see","if",
             "In","I","but","he"]
for m in all_articles:
    if m not in stop_words:
        meaningful_words.append(m)

list = meaningful_words
dict_words_frequency={}
for n in list:
    dict_words_frequency[n]=list.count(n)
#dict_words_frequency

list_words_frequency = []
for i in dict_words_frequency:
    f = dict_words_frequency[i]
    
    list_words_frequency.append((i,f))
# print(list_words_frequency)

rank = list_words_frequency
rank_list = sorted(rank,key=lambda a:a[1],reverse = True) ## Google for the syntax
rank_list[0:15]
# rank_list


with open('keywords.csv','w',newline='') as g:
    writer = csv.writer(g)
    header = ['Keyword','Frequency']
    writer.writerow(header)
    writer.writerows(rank_list[0:15])
print(rank_list[0:15])
    


    
