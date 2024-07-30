# Single Url Video Downlaod
# One At Time 

# import instaloader

# def download_instagram_videos(profile_name):
#     # Create an Instaloader instance
#     L = instaloader.Instaloader()

#     # Load the Instagram profile
#     profile = instaloader.Profile.from_username(L.context, profile_name)

#     # Counter for naming files
#     counter = 1

#     # Loop through posts in the profile
#     for post in profile.get_posts():
#         if post.is_video:
#             # Download the video post
#             L.download_post(post, target=f"{profile_name}_{counter}")
#             counter += 1

#     print(f"Downloaded {counter - 1} videos from {profile_name}")

# if __name__ == "__main__":
#     # Instagram profile username
#     profile_name = input("Enter the Instagram profile username: ")
#     download_instagram_videos(profile_name)



# Multipe Time 
# Series can Be Given 

import instaloader
import os

def download_instagram_videos(profile_name, start_from=1, end_at=None, save_path='downloads'):
    # Create the save path directory if it does not exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Create an Instaloader instance
    L = instaloader.Instaloader()

    # Load the Instagram profile
    profile = instaloader.Profile.from_username(L.context, profile_name)

    # List to hold all video posts
    video_posts = [post for post in profile.get_posts() if post.is_video]

    # Check if end_at is provided and within range
    if end_at is None or end_at > len(video_posts):
        end_at = len(video_posts)

    # Loop through video posts from start_from to end_at
    for idx, post in enumerate(video_posts[start_from-1:end_at], start=start_from):
        try:
            # Download the video post
            filename = f"{idx:04d}_{post.date_utc.strftime('%Y%m%d_%H%M%S')}.mp4"  # Serial number and date
            print(f"Downloading {filename}")
            L.download_post(post, target=os.path.join(save_path, filename))
        except Exception as e:
            print(f"Failed to download video {idx}: {e}")

    print(f"Downloaded {end_at - start_from + 1} videos from {profile_name}")

if __name__ == "__main__":
    # Instagram profile username
    profile_name = input("Enter the Instagram profile username: ")
    start_from = int(input("Enter the starting position (1 for the first video): "))
    end_at = int(input("Enter the ending position (leave blank for all remaining videos): ") or 0)
    end_at = None if end_at == 0 else end_at

    download_instagram_videos(profile_name, start_from, end_at)

