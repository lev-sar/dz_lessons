# Задание 1_____________________________
# def odd_number(x):
#     for num in range(1, x + 1, 2):
#         yield num
#
#
# num_to_20 = odd_number(21)
# print(next(num_to_20))
# print(next(num_to_20))
# print(*num_to_20)

# Задание 1.b_____________________________
# x = int(input('Введите число'))
# num_gen = (i for i in range(1, x + 1, 2))
#
# print(num_gen)
# print(list(num_gen))

# Задание 3________________________________

# from itertools import zip_longest, islice
#
#
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена']
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
#
# gen = ((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses, fillvalue=None))
# print(*islice(gen,len(tutors)), sep='\n')

# Задание 4 _________________________________
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# print([x for i, x in enumerate(src[1:], start=1) if x > src[i - 1]])

# Задание 5____________________________________
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# print([x for x in src if src.count(x) == 1])