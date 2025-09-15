import pandas
df=pandas.read_csv('F:/Python/nato_phonetic_alphabet.csv')

phonetcis={v.letter:v.code for (k,v) in df.iterrows()}
print(phonetcis)

name=input('Enter Your name')

l=[phonetcis[i.upper()] for i in name]
print(l)