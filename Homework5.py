"""HW5. asyncio and Threads

Results:
    Asyncio:
        1: 18.242701292037964
        2: 18.3756046295166
        3: 18.201203107833862
    Threading:
        1:  18.59894299507141
        2:  18.244040727615356
        3:  18.212700843811035
"""

import asyncio
import glob
import os
import threading
import time

import aiohttp
import requests

URLS = [
    "https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz",
    "https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz",
    "https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz"
]

asc_dir = "./asyncio"
thr_dir = "./threading"

os.makedirs(asc_dir, exist_ok=True)
os.makedirs(thr_dir, exist_ok=True)

for f_name in glob.glob(asc_dir + "/*"):
    os.remove(f_name)

for f_name in glob.glob(thr_dir + "/*"):
    os.remove(f_name)


# ### Asyncio

async def asyncio_download(session, url):
    async with session.get(url) as response:
        filename = os.path.join(asc_dir, os.path.basename(url))

        start_t = time.time()

        with open(filename, 'wb') as f_handle:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                f_handle.write(chunk)
        await response.release()

        return time.time() - start_t


async def asuncio_main(urls):
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(
            *[asyncio_download(session, url) for url in urls])
        print(result)
        print(sum(result))


# ### Threading

def threading_download(url):
    r = requests.get(url, stream=True)

    filename = os.path.join(thr_dir, os.path.basename(url))

    start_t = time.time()

    with open(filename, 'wb') as f:
        for chunk in r.iter_content(1024):
            if chunk:
                f.write(chunk)

    print("{}: {}".format(url, time.time() - start_t))


def threading_main(urls):
    download_thread = [threading.Thread(target=threading_download, args=(url,))
                       for url in urls]

    for t in download_thread:
        t.start()

    for t in download_thread:
        t.join()


if __name__ == '__main__':
    start = time.time()
    threading_main(URLS)
    print("Overall threads: {}".format(time.time() - start))

    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asuncio_main(URLS))
    print("Overall asyncio: {}".format(time.time() - start))
