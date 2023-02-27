from asyncio import sleep,run

class Foo: 
    def __aiter__(self):
        self.i = 0
        return self 
    async def __anext__(self):
        await sleep(1)
        self.i += 1
        return self.i 
#
async def using_async_for():
    async for bar in Foo():
        print(bar)
        if bar >= 10:
            break 
 #       
async def using_aiter_anext():
    ai = aiter(Foo())
    try: 
        while True:
            bar = await anext(ai)
            print(bar)
            if bar >= 10:
                break
    except StopAsyncIteration:
        return 

async def main():
    print('Using async for:')
    await using_async_for()
    
    print("Using aiter/anext")
    await using_aiter_anext()

if __name__ == '__main__':
    run(main())