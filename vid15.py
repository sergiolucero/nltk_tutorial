# sentdex NLTK tutorial videos, part 15
# https://www.youtube.com/watch?v=nla4C-VYNEU
import nltk
import random
from nltk.corpus import movie_reviews

from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = [w.lower() for w in movie_reviews.words()]
all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]

def find_features(document):
    words = set(document)
    features = {w: (w in words) for w in word_features}
    return features
    
featuresets = [(find_features(rev), category) for (rev, category) in documents]

training_set = featuresets[:1900]
testing_set = featuresets[1900:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
    
classifiers = {'Multinomial':   MultinomialNB,
                'Bernoulli':    BernoulliNB,
                'Logistic':     LogisticRegression,
                'SGD':          SGDClassifier,
                'SVC':          SVC,
                'LinearSVC':    LinearSVC,
                'NuSVC':        NuSVC
                }
                
print("Original Naive Bayes Algo accuracy percent:", 
      (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

for classifier_name, classifier in classifiers.iteritems():
    this_classifier = SklearnClassifier(classifier())
    this_classifier.train(training_set)
    print("%s_classifier accuracy percent:" %(classifier_name), 
          (nltk.classify.accuracy(this_classifier, testing_set))*100)


                