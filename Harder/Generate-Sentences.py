list1 = ["I", "Love", "Coding"]
list2 = ["Python", "is", "Awesome"]
list3 = ["Let's", "Build", "Projects"]
list4 = ['hi', 'huh?']

list5 =['ophelia']
list6 = ["that's some beautiful code"]
list7 = ['my', 'name', 'is', 'ryan']
list8 = ['hi ', 'you']
list9 =['hey', 'mom']
# Generate all possible 1 to 9 -word sentences and do it for each list

from itertools import permutations
def generate_sentences(word_list):
    sentences = []
    for r in range(1, len(word_list) + 1):
        for perm in permutations(word_list, r):
            sentence = ' '.join(perm)
            sentences.append(sentence)
    return sentences

sentences_list1 = generate_sentences(list1)
sentences_list2 = generate_sentences(list2)
sentences_list3 = generate_sentences(list3)
sentences_list4 = generate_sentences(list4)
sentences_list5 = generate_sentences(list5)
sentences_list6 = generate_sentences(list6)
sentences_list7 = generate_sentences(list7)
sentences_list8 = generate_sentences(list8)
sentences_list9 = generate_sentences(list9)         
one = sentences_list1
two = sentences_list2
three = sentences_list3
four = sentences_list4
five = sentences_list5
six = sentences_list6
seven = sentences_list7
eight = sentences_list8
nine = sentences_list9
all_sentences = one + two + three + four + five + six + seven + eight + nine
for sentence in all_sentences:
    print(sentence)