from pytube import YouTube
from tqdm import tqdm

def progress_callback(stream, chunk, bytes_remaining):
    # Calculate the progress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    
    # Update the tqdm progress bar
    tqdm_bar.update(len(chunk))

def download_youtube_video(url):
    try:
        # Create a YouTube object
        yt = YouTube(url, on_progress_callback=progress_callback)
        
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        
        # Initialize the tqdm progress bar
        global tqdm_bar
        tqdm_bar = tqdm(total=stream.filesize, unit='B', unit_scale=True, desc=yt.title)
        
        # Download the video
        print(f"Downloading: {yt.title}")
        stream.download()
        print("Download completed!")
        
        # Close the tqdm progress bar
        tqdm_bar.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # URL of the YouTube video you want to download
    video_url = input("Enter the URL of the YouTube video: ")
    download_youtube_video(video_url)




