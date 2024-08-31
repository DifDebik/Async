import requests
import asyncio

urls = ['https://www.infoworld.com/wp-content/uploads/2024/06/1200px-burmese_python_02-100637340-orig.jpg',
        'https://cdn.thenewstack.io/media/2024/02/49cf830e-david-clode-vec5yfuvcgs-unsplash.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Ball_python_lucy.JPG/640px-Ball_python_lucy.JPG',
        'https://i.natgeofe.com/k/3373927f-fa15-4c55-bf49-73f44073b768/burmese-python-tree_2x3.jpg',
        'https://cdn.britannica.com/28/239528-050-D89C8118/reticulated-python-Malayopython-reticulatus.jpg',]


async def download(url):
    filename = url.rsplit('/', 1)[1]
    response = requests.get(url, stream=True)

    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                await asyncio.sleep(0)  # yield control to event_loop so that the other tasks would run

    print('Done')


async def main():
    tasks = [download(i) for i in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
