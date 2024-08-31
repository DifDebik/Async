import requests
import asyncio

urls = ['https://www.infoworld.com/wp-content/uploads/2024/06/1200px-burmese_python_02-100637340-orig.jpg',
        'https://cdn.thenewstack.io/media/2024/02/49cf830e-david-clode-vec5yfuvcgs-unsplash.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Ball_python_lucy.JPG/640px-Ball_python_lucy.JPG',
        'https://i.natgeofe.com/k/3373927f-fa15-4c55-bf49-73f44073b768/burmese-python-tree_2x3.jpg',
        'https://cdn.britannica.com/28/239528-050-D89C8118/reticulated-python-Malayopython-reticulatus.jpg',]


async def download(url):
    loop = asyncio.get_running_loop()
    image = await loop.run_in_executor(None, requests.get, url)
    filename = url.rsplit('/', 1)[1]

    with open(filename, 'wb') as f:
        f.write(image.content)

    print('Done')


async def main():
    tasks = [download(url) for url in urls]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
