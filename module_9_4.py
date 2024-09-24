import random

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda chr_1, chr_2: chr_1 == chr_2, first, second))
print(result)


def get_advances_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for new_data in data_set:
                file.write(str(new_data) + '\n')

    return write_everything


write = get_advances_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', '5', 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        word = random.choice(self.words)
        return word


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
