import os
import yt_dlp
from urllib.parse import urlparse, parse_qs

def create_folder_if_not_exists(folder_name):
    base_path = "/mnt/c/Desktop/classroom"
    folder_path = os.path.join(base_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Folder '{folder_path}' has been created or already exists.")
    return folder_path


def extract_playlist_url(video_url):
    parsed_url = urlparse(video_url)
    query_params = parse_qs(parsed_url.query)
    playlist_id = query_params.get('list')

    if playlist_id:
        playlist_url = f"https://www.youtube.com/playlist?list={playlist_id[0]}"
        return playlist_url
    else:
        return video_url
    

def download_playlist(video_url, save_path):
    # Ensure the save path exists
    folder_path = create_folder_if_not_exists(folder_name)
    # os.makedirs(save_path, exist_ok=True)
    playlist_url = extract_playlist_url(video_url)

    ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Download the best video and audio separately, merge them
    'outtmpl': os.path.join(folder_path, '%(title)s.%(ext)s'),  # Set output template for file naming
    'merge_output_format': 'mp4',  # Merge video and audio into mp4 (if necessary)
    'postprocessors': [{  # Ensure post-processing to combine video and audio
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # Convert to mp4
    }],
    'noplaylist': False,  # To ensure playlist downloading works
}

    # Use yt-dlp to download the playlist
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


video_url = "https://www.youtube.com/watch?v=or_6-KB9Eyg&pp=ygUPZG9ja2VyIHR1dG9yaWFs"
folder_name = "2_new_cfn"
download_playlist(video_url, folder_name)



    
















# video_url = "https://www.youtube.com/watch?v=0Sh9OySCyb4&pp=ygUSY2xvdWRmb3JtYXRpb24gYXdz"
# save_path = "C:\Desktop\classrooom"
# download_playlist(video_url, save_path)
