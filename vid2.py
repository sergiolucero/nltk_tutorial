# sentdex tutorial videos, part 2
# https://www.youtube.com/watch?v=w36-U-ccajM

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

example_sentence = "This is an example showing off stop word filtration."
stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sentence)

filtered_sentence = [w for w in words if w not in stop_words]
        
print(filtered_sentence)