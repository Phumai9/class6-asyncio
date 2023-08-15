import asyncio
import time

async def print_after(message, delay):
    """Print a message after the specified delay (in seconds)"""
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")

async def main():
    # Use asyncio.gather to run two coroutines concurrently:
    await asyncio.gather(print_after("word!", 2),
                         print_after("word!", 1)
                         )

asyncio.run(main())

# Tue Aug 15 13:16:18 2023 - word!
# Tue Aug 15 13:16:19 2023 - word!