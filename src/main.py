import asyncio

from api import run_api
from config import HOST, PORT


async def run_server():
    print(HOST, PORT)
    await run_api(HOST, PORT)


if __name__ == '__main__':
    try:
        asyncio.run(run_server())
    except (KeyboardInterrupt, SystemExit):
        # TODO: Log something...
        pass
