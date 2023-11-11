def convert_to_python_case(text):
    uppers = [elem for elem in text if elem == elem.upper() and elem.isalpha()]
    strn = ''
    for i in range(len(text)):
        if text[i] in uppers and i != 0:
            strn += "*"
        strn += text[i]
    text = '_'.join(strn.lower().split('*'))
    return text

# считываем данные
txt = 'ConvertToInt32'

# вызываем функцию
print(convert_to_python_case(txt))