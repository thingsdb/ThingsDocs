import asyncio
from thingsdb.client import Client


async def work(client: Client):
    pass


async def main():
    client = Client()
    client.set_default_scope('//todos')
    await client.connect('localhost')  # Replace if needed
    try:
        await client.authenticate('<TOKEN_OR_USERNAME_AND_PASSWORD>')
        await work(client)
    finally:
        client.close()
        await client.wait_closed()


asyncio.run(main())
