from translate import Translator

frase = input('digite sua frase: ')
res = input('1 para Eng - Pt, 2 para Pt - Eng')

if res == 1:
    s = Translator(from_lang="english", to_lang = "Portuguese")
    res = s.translate(frase)
    print(res)
    
if res == 2:
    s = Translator(from_lang="Portuguese", to_lang = "english")
    res = s.translate(frase)
    print(res)

