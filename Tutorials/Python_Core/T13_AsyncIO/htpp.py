import asyncio
import aiohttp


# Define a coroutine to download a file from a given URL
async def download_file(url, session):
    # Use aiohttp to send a GET request to the URL
    async with session.get(url) as response:
        # Extract the filename from the URL
        filename = url.split("/")[-1]
        # Open the file for writing in binary mode
        with open(filename, "wb") as f:
            # Read the response in chunks
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                # Write the chunk to the file
                f.write(chunk)
        print(f"Downloaded {url} to {filename}")


# Define the main coroutine
async def main():
    # List of URLs to download
    urls = [
        "https://example.com/file1.html",
        "https://example.com/file2.html",
        "https://example.com/file3.html",
    ]
    # Create an aiohttp session
    async with aiohttp.ClientSession() as session:
        # Create a list of tasks to download the files concurrently
        tasks = [download_file(url, session) for url in urls]
        print(tasks)
        # Wait for all tasks to complete
        await asyncio.gather(*tasks)


# Run the main coroutine using asyncio.run
asyncio.run(main(), debug=True)
