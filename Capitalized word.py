words = ['this', 'is', 'just', 'a', 'test']
capitalize_words =[x.capitalize() for x in words]

print('words:', words)
print('capitalized words:',capitalize_words)

words = ['helo','world','foo','bar','test', 'python', 'is','awesome']
short_words = [x for x in words if len(x) <= 3]
other_words = [x for x in words if x not in short_words ]
words_with_e = [ x for x in words if x.count('e')>=1]


print('words:',words)
print('short words:',short_words)
print('other words:', other_words)
print('words with "e":', words_with_e)