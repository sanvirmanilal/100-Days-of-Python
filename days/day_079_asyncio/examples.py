"""Worked learning example for day 079; independent of the exercises."""

def main():
    import asyncio
    async def echo(value):
        await asyncio.sleep(0)
        return value

    async def main():
        print(await asyncio.gather(echo("a"), echo("b")))

    asyncio.run(main())


if __name__ == "__main__":
    main()
