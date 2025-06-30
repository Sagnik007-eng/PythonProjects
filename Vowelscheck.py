vowel={'a','e','i','o','u'}
class vowelsCheck:
    def __init__(self,s1):
        self.s1=s1
    def vowel_check(self):
        count=0
        for i in self.s1:
            if i in vowel:
                count+=1
        print(f'thr r {count} vowels')

v1=vowelsCheck('Artificial Intelligence is the future')
v1.vowel_check()