# coding:utf-8
import asyncio
import random
import time


async def a():
    for i in range(10):
        print(i, 'a')
        # time.sleep 是cpu级别的阻塞，同步、异步失效，需要更换成asyncio
        # asyncio.sleep 的则是业务级别的等待
        await asyncio.sleep(random.random() * 2)
    return 'a function'


async def b():
    for i in range(10):
        print(i, 'b')
        await asyncio.sleep(random.random() * 2)
    return 'b function'


async def main():
    result = await asyncio.gather(
        a(),
        b()
    )
    print(result)

if __name__ == '__main__':
    start = time.time()
    # a()
    # b()
    asyncio.run(main())
    print(time.time() - start)

