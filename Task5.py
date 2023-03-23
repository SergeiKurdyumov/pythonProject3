Rus = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
Eng = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
N = abs(int(input('Введите 0, если играем в русской раскладке, либо 1, если в английской: ')))
word = input('Введите слово: ').upper()
if N == 1:
	print('Вы получаете', sum([k for i in word for k, v in Eng.items() if i in v]), 'очков')
elif N == 0:
	print('Вы получаете', sum([k for i in word for k, v in Rus.items() if i in v]), 'очков')
else:
    print('Вы играете не по правилам!')