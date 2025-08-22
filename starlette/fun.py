import asyncio

async def q():
    print("답이 하나도 안맞잖아")
    await asyncio.sleep(3)

async def a():
    print("하지만 빨랐죠")

async def main():
    # asyncio.gather 안에서는 여러 코루틴을 동시에 실행할 수 있음
    await asyncio.gather(q(), a())

if __name__ == "__main__":
    asyncio.run(main())
