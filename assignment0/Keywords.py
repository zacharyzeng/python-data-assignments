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


list = all_articles
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


list = all_articles
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

print(rank_list[0:15])
    


    
