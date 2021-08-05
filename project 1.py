# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
1 вопрос
2 вопрос
3 вопрос
4 вопрос
5 вопрос

6 вопрос
data = pd.read_csv('movie_bd_v5.csv')
data['profit'] = data['revenue'] - data['budget']
profit_max = data['profit'].max()
film = data[data.profit == profit_max]
film ['original_title']

7 вопрос
8 вопрос
9 вопрос

10 вопрос
data = pd.read_csv('movie_bd_v5.csv') #обращаемся к дата фрейму
data['profit'] = data['revenue'] - data['budget']#вычисляем профит
films_2012_2014 =data[data.release_year.between(2012,2014)]# собрали  фильмы 2012_2014 в датафрейм
films_2012_2014[(films_2012_2014.profit==films_2012_2014.profit.min())].original_title #выделим название самого убыточного

11 вопрос
def by_genres():
    from itertools import chain
    list_of_genres = []
    for genre in list(data.genres):
        genre = genre.split("|")
        list_of_genres.append(genre)
    list_of_genres = list(chain(*list_of_genres))
    return list_of_genres
    for genre in list(set(list_of_genres)):
        data[genre] = data.genres.str.contains(genre, na = False)
l_o_g = by_genres()

12 вопрос
data = pd.read_csv('movie_bd_v5.csv')
data['profit'] = data['revenue']-data['budget']
profit_film = data[data.profit > 0].copy() # выбираем из дф фильмы с положительным профитом
profit_film.genres = profit_film.genres.str.split('|') # в столбце с жанрами строки в ячейках преобразуем в списки
profit_genres = profit_film.genres.explode() # применяем explode к столбцу с жанрами, чтобы в каждой ячейке было по одному жанру
profit_genres.value_counts() # в полученной серии подсчитываем количество каждого из значений (жанров)

13 вопрос
import pandas as pd
import pandas as pd
sample = pd.DataFrame(['Иванов|Петров', 'Смирнов|Попов',
                      'Кузнецов|Иванов'], columns=['surname'])
sample['revenue'] = [100,200,300]
sample['title'] = ['фильм1','фильм2','фильм3']
# преобразуем строки в списки
sample.surname = sample.surname.str.split('|')
print(sample)
              surname  revenue   title
0    [Иванов, Петров]      100  фильм1
1    [Смирнов, Попов]      200  фильм2
2  [Кузнецов, Иванов]      300  фильм3


14 вопрос
data_tmp = data[data.genres.str.contains("Action")]
data_tmp=data_tmp['director'].str.cat(sep='|') # превращаем все в одну строку
data_tmp=pd.Series(data_tmp.split('|')) # создаем список разделяя строку по '|'
data_tmp=data_tmp.value_counts(ascending=False) # считаем количество элементов строке
data_tmp

15 вопрос
import pandas as pd
data = pd.read_csv('movie_bd_v5.csv')
data.cast = data.cast.apply(lambda x: str(x).split('|'))
data = data.explode('cast')
data[data.release_year == 2012].groupby('cast').revenue.sum().sort_values(ascending=False).head()
cast
Chris Hemsworth      2027450773
Denis Leary          1629460639
Anne Hathaway        1522851057
Robert Downey Jr.    1519557910
Mark Ruffalo         1519557910

16 вопрос
17 вопрос
18 вопрос

19 вопрос
data = pd.read_csv('movie_bd_v5.csv')
data = data.groupby(['release_year']).revenue.sum().sort_values(ascending=False).index[0]
data

20 вопрос
data.loc[224,['production_companies','profit']]
production_companies    Warner Bros.|Warner Bros. Interactive Entertai...
profit                                                           -2514873
Name: 224, dtype: object

21 вопрос
data['release_date'].str.split('/')
0         [6, 9, 2015]
1        [5, 13, 2015]
2        [3, 18, 2015]
3       [12, 15, 2015]
4         [4, 1, 2015]
             ...
1884     [7, 13, 2000]
1885    [10, 27, 2000]
1886     [6, 30, 2000]
1887     [2, 16, 2000]
1888     [7, 19, 2000]
data['release_date'].str.split('/').apply(lambda x: x[0])
0        6
1        5
2        3
3       12
4        4
        ..
1884     7
1885    10
1886     6
1887     2
1888     7
data['release_date'].str.split('/').apply(lambda x: x[0]).value_counts()
9     227
12    190
10    186
8     161
3     156
4     149
6     147
11    146
7     142
5     140
2     135
1     110


22 вопрос
months_rel = months_rel.sort_index()
months_rel

23 вопрос
import pandas as pd
data = pd.read_csv('movie_bd_v5.csv')
data['release_date'] = pd.to_datetime(data['release_date'])
data_winter = data[data['release_date'].dt.month.isin([1, 2, 12])]
data_winter['director'] = data_winter['director'].str.split('|')
data_winter = data_winter.explode('director')
data_winter.groupby('director')['imdb_id'].count().sort_values(ascending=False)


24 вопрос
data.orogonal_title = data.orogonal_title.apply(lambda x: len(x))
data.groupby('production_companies').orogonal_title.max().sort_values(ascending = False)

25 вопрос
data2=data.copy(deep=True)
data2['title_length'] = data2['overview_words_length'].apply(lambda x: len(x.split()))
data2['production_companies'] = data2['production_companies'].str.split('|')
data2=data2.explode('production_companies')
data2.groupby('production_companies')['title_length'].agg(['max', 'mean','sum']).sort_values("mean", ascending = False).head(20)

26 вопрос

27 вопрос
movie_pair = data.copy()
movie_pair.cast = movie_pair.cast.str.split('|') # разделяем cast на списки
movie_pair = movie_pair.assign(actor = movie_pair.cast) # дублируем колонку cast
movie_pair = movie_pair.explode('actor') # разделяем списки актеров
movie_pair = movie_pair.groupby(['actor'])['cast'].sum() #группируем по актерам складывая cast
def self_filter(row):
    return [element for element in row[1] if element != row[0]]
movie_pair = movie_pair.reset_index()
movie_pair['cast'] = movie_pair.apply(self_filter,axis=1)
movie_pair