import asyncio
import time

async def example(message):
    print(f"{time.ctime()} - start of :", message)
    await asyncio.sleep(1)
    print(f"{time.ctime()} - end of :", message)

async def main():
    # Start coroutine twice (hopefully they start!)
    first_awaitable = example("First call")
    second_awaitable = example("Second call")
    # wait for coroutines to finish
    await first_awaitable
    await second_awaitable

asyncio.run(main())

# Tue Aug 15 13:15:39 2023 - start of : First call
# Tue Aug 15 13:15:40 2023 - end of : First call
# Tue Aug 15 13:15:40 2023 - start of : Second call
# Tue Aug 15 13:15:41 2023 - end of : Second call