texts = input('Ingresa un texto: ').lower().strip()
text_list = texts.split(' ')
letters = input('Ingrese 3 letras separadas por una coma: ').strip().split(',')
count_letters = {}

n_palabras = len(text_list)

for letter in letters:
    n_letters = texts.count(letter.strip().lower())
    count_letters[letter] = n_letters

texto_invertido = ' '.join(text_list[::-1])


################################################################
print(f"El número de palabras del texto es {n_palabras}")
print("Numero de veces por cada letra:")
for key, value in count_letters.items():
    print(f"Letra: {key} -- Número de veces: {value}")

print(f"Primera letra del texto: {texts[0]}")
print(f"Última letra del texto: {texts[-1]}")
print(f"Texto invertido: {texto_invertido}")
print(f"La palabra 'Python' esta dentro del texto?: {'python' in text_list}")
