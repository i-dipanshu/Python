content = '''Donkey is an shitty.
kind of  shit.
he always shit.0
okay that was sucker but eating shit
oh fuck it got even bitchy now a days'''

words = ['shit', 'fuck', 'shitty', 'bitchy', 'sucker']

with open('Chapter 9\sensor.txt', 'w') as f:
    f.write(content)

with open('Chapter 9\sensor.txt') as f:
    content = f.read()

for word in words:
    content = content.replace(word,'#^$#@$^#')

with open('Chapter 9\sensor.txt', 'w') as f:
    content = f.write(content)