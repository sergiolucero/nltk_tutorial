# code from the tutorial
# Natural Language Processing With Python and NLTK
# First video: https://www.youtube.com/watch?v=FLZvOKSCkxY
# Playlist link: http://tinyurl.com/nltk-tutorial

from nltk.tokenize import sent_tokenize, word_tokenize

some_text = "any ideas what you'd like to cook for Sunday? I am sending out \
               individual promos and would like to present what you're going to make"

print(sent_tokenize(some_text))
               
for word in word_tokenize(some_text):
    print word