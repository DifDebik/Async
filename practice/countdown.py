import asyncio


async def countdown(name: str, start_time: int, delay=0) -> str:
    await asyncio.sleep(delay)
    while start_time > 0:
        print(f'{name} will finish in {start_time} seconds')
        await asyncio.sleep(1)
        start_time -= 1

    print('Beep Beep')


async def main():
    countdown1 = countdown('countdown 1', 20, delay=6)
    countdown2 = countdown('countdown 2', 10, delay=3)
    countdown3 = countdown('countdown 3', 5, delay=1)

    await asyncio.gather(countdown1, countdown2, countdown3)

if __name__ == "__main__":
    asyncio.run(main())
