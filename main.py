#print(*filter(lambda x: 10 < x < 20, map(int, input().split())))

# def get_normalized_coordinates(Xs, Ys):
#     # Объединяем входные списки в список кортежей
#     route = list(zip(Xs, Ys))
    
#     # Получаем стартовые координаты (первую точку маршрута)
#     start_x, start_y = route[0]
    
#     # Нормализуем маршрут, используя map и lambda
#     normalized_route = list(map(lambda point: (point[0] - start_x, point[1] - start_y), route))
    
#     return normalized_route

# def F(n):
#     if n <= 5:
#         return n
#     elif n % 3 == 0:
#         return n + F(n // 3 + 2)
#     else:
#         return n + F(n + 3)

# n = 1
# while True:
#     try:
#         result = F(n)
#         if result > 1000:
#             print(n)
#             break
#     except RecursionError:
#         pass  # Если происходит переполнение стека, просто игнорируем и продолжаем дальше
#     n += 1

# def process_user_id(user_id):
#     if len(str(user_id)) == 6:
#         print('Welcome! ')
#     elif len(str(user_id)) != 6:
#         raise IncorrectUserIdError('It should contain 6 digits!')
#     elif not isinstance(user_id):
#         raise TypeError('Write down only integers!')
#     return True
# inputik = process_user_id(input('Write down: '))
import asyncio
import time 

async def print_temp():
    await asyncio.sleep(2)
    print('Temperature is OK! ')

async def print_pressure():
    await asyncio.sleep(3)
    print('Pressure is OK! ')

async def print_uranium_level():
    await asyncio.sleep(1)
    print('Uranium level is OK! ')

async def main():
    start_time = time.time()
    print('PROCESS STARTED')
    await asyncio.gather(
        print_temp(),
        print_pressure(),
        print_uranium_level()
    )
    end_time = time.time()
    spent_time = end_time - start_time
    print(f'{spent_time} was spent ')

asyncio.run(main())

