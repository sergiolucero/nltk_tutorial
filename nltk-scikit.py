# with help from the tutorial
# Natural Language Processing With Python and NLTK
# https://www.youtube.com/watch?v=FLZvOKSCkxY

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
# nltk.download()

injeet_text = "any ideas what you'd like to cook for Sunday? I am sending out \
               individual promos and would like to present what you're going to make"
               
for word in word_tokenize(injeet_text):
    print word