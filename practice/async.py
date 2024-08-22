import asyncio
import asyncpg

query = '''INSERT INTO some_test_table VALUES ($1, $2, $3)'''


async def make_request(db_pool):
    await db_pool.fetch(query, 1, 'some_string', 3)
    await asyncio.sleep(.1)


async def main():
    chunk = 200
    tasks = []
    pended = 0

    db_pool = await asyncpg.create_pool('postgresql://postgres:postgres@127.0.0.1/postgres')

    for i in range(10000):
        tasks.append(asyncio.create_task(make_request(db_pool)))
        pended += 1
        if len(tasks) == chunk or pended == 10000:
            await asyncio.gather(*tasks)
            tasks = []
            print(pended)


asyncio.run(main())
