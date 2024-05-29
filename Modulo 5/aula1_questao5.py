import emoji

print('Emojis disponiveis')
print(f'{emoji.emojize(":red_heart:")}  - :red_heart:')
print(f'{emoji.emojize(":thumbs_up:")}  - :thumbs_up:')
print(f'{emoji.emojize(":thinking_face:")}  - :thinking_face:')
print(f'{emoji.emojize(":partying_face:")}  - :partying_face:')

print('')
print('Digite uma frase e ela será emojizada:')
frase = input('')
frase_emojizada = emoji.emojize(frase)
print('')
print('Frase emojizada:')
print(frase_emojizada)