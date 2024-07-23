import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    await asyncio.sleep(1)
    for i in range(1, 6):
        print(f'Силач {name} поднял {i} шар')
        await asyncio.sleep(2)
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    await asyncio.sleep(1/3)
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    await asyncio.sleep(1/4)
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await asyncio.sleep(1/5)
    await task1
    await task2
    await task3


asyncio.run(start_tournament())