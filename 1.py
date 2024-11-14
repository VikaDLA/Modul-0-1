# while 1 > 0:
#     print('Hello World!')
#
# print('Goodbye!')
# from collections.abc import dict_items

# for i in 1, 2, 3, 4:
# for i in 'Hello':
# # print('ok')
#     print(i)
# list_ = ['one', 'two', 'three']
# for i in list_:
#     print(i)

# list_ = ['one', 'two', 'three']
# for i in list_:
#     if i == 'three':
#         list_.remove(i)
#
# print(list_)

# list_ = ['one', 'two', 'three']
# for i in range(len(list_)):
#     print(list_[i])
#     print(i)
#
# print(list_)

# list_ = ['one', 'two', 'three']
# for i in range(len(list_)):
#     list_ [i] = '123'
#
# print(list_)

# list_ = ['one', 'two', 'three']
# list_2 = [2, 3, 4, 6, 1]
# sum_ = 0
# for i in range(len(list_2)):
#     sum_ += list_2[i]
#
# print(sum_)

# for i in range(1, 11):
#     for j in  range(1, 11):
#         print(f'{i} x {j} = {i * j}')

# dict_ =  {'a': 1, 'b': 2, 'c': 3}

# for i in  dict_:
#      print(i, dict_[i])

# dict_ =  {'a': 1, 'b': 2, 'c': 3}
# for i, k in  dict_.items():
#      print(i, k)

# def say_hello(name):
#     print('Hello' , name)

# say_hello('Vika')
# say_hello('Oleg')

# import random
# def lottery():
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win = random.choice(tickets)
#     return win
# win = lottery() + lottery()
# print(win)

    # lose = random.choice(tickets)

import random
# def lottery(mon, thue):
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(tickets)
#     tickets.remove(win1)
#     win2 = random.choice(tickets)
#     print(mon, thue)
#     return win1, win2
#
# win1, win2 = lottery(mon:'mon', thue: "thue")
# print(win1, win2)

# def lottery(*args, **kwargs):
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(tickets)
#     tickets.remove(win1)
#     win2 = random.choice(tickets)
#     print(*args)
#     return win1, win2
#
#
# win1, win2 = lottery(2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(win1, win2)


def test(a=2, b=True):
    print(a, b)


# test(False, 'ok')
test(*[1, 2])

