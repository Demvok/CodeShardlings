# объявление функции
def is_correct_bracket(text):
    while "()" in text:
        text = text.replace("()", "", 1)
        print(text)
    if len(text) == 0:
        return True
    return False
# считываем данные
txt = '((()())(()()))((()())(()()))'

# вызываем функцию
print(is_correct_bracket(txt))