word = ('piano', 'corinthians', 'maria', 'izabelle', 'cachorro', 'ciclope', 'software')
for w in word:
    print(f'\nNa palavra {w.upper()} contém', end=' ')
    for vogal in w:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')
