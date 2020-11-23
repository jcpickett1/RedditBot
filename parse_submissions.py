import pandas as pd
import nltk

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier


submissions_data = pd.read_csv('cleaned_submissions.csv', index_col=0)

train_set = submissions_data[:380]
test_set = submissions_data[380:]


#set x as training set minus category column
x = train_set.drop(columns='category')
y = train_set.category
bools = pd.DataFrame(x.drop(columns=['subreddit','title']))
unstruc = pd.DataFrame(x[['subreddit', 'title']])

#vectorize title field
cvec = CountVectorizer(stop_words='english').fit(unstruc['title'])
titles_vector = cvec.transform(unstruc['title'])
titles_vector = pd.DataFrame(titles_vector.todense(), columns=cvec.get_feature_names())
titles_vector.index.rename('index',inplace=True)

#vectorize subreddit field
cvec = CountVectorizer(stop_words='english').fit(unstruc['subreddit'])
subreddits_vector = cvec.transform(unstruc['subreddit'])
subreddits_vector = pd.DataFrame(subreddits_vector.todense(), columns=cvec.get_feature_names())
subreddits_vector.index.rename('index', inplace=True)

super_data = titles_vector.merge(subreddits_vector, on='index')
super_data = super_data.merge(bools, on='index')

X_train, X_test, Y_train, Y_test = train_test_split( super_data, y, test_size=0.33)

# lr = LogisticRegression()
lr = MLPClassifier()

lr.fit(X_train, Y_train)
score = lr.score(X_test, Y_test)
print(score)
print('exited cleanly')