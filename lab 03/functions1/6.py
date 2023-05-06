def reversesoilemdi(sentence):
    words = sentence.split()
    words.reverse()
    print(''.join(words))
s = input()
reversesoilemdi(s)