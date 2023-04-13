import asyncio
import aiohttp        
import aiofiles
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--n', default=10)
parser.add_argument('--save_path', default="artifacts\\easy")
args = parser.parse_args()


async def load_pic(url, save_path):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            pic_id = resp.headers["Picsum-Id"]
            async with aiofiles.open(save_path + "\\" + pic_id + '.jpg', 'wb') as f:   
                await f.write(await resp.read())

async def main(url, n, save_path):
    await asyncio.gather(
        *(load_pic(url, save_path) for _ in range(n))
    )

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(main("https://picsum.photos/200", args.n, args.save_path))
        loop.run_forever()
    finally:
        loop.close()
    