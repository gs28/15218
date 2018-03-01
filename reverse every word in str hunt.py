sentence="hi guvi"
def reverse_words(sentence):        
     return " ".join((lambda x : [i[::-1] for i in x])(sentence.split(" ")))
print(reverse_words(sentence))
