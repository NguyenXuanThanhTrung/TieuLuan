from googleapiclient.discovery import build
import yt_dlp
import os

def search_videos_by_topic(topic, max_results=10): #Lấy list IDs của các video
    api_key = 'AIzaSyCGJ9R2KjUhqRMcIfC1mkyoLSvPcQ6lM1o'

    youtube = build('youtube', 'v3', developerKey=api_key)
    response = youtube.search().list(
        part='snippet',
        q=topic,
        type='video',
        maxResults=max_results
    ).execute()

    video_ids = [item['id']['videoId'] for item in response['items']]
    return video_ids

def download_video(video_id, output_path): #Tải video từ list IDs
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    try:
        print(f"Đang thử tải video: {video_url}")
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s')
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Video với ID {video_id} đã được tải xuống thành công.")
    except Exception as e:
        print(f"Lỗi trong quá trình tải xuống video với ID {video_id}: {str(e)}")
        print(f"Loại lỗi: {type(e)}")

# Chủ đề để tìm kiếm video
topic = 'chú hề ma quái'

# Số lượng video tối đa cần lấy
max_results = 7

# Thư mục đầu ra cho video tải xuống
output_path = '.'

# Lấy danh sách video theo chủ đề
video_ids = search_videos_by_topic(topic, max_results)

# Tải xuống từng video theo ID và lưu vào thư mục đầu ra
for video_id in video_ids:
    download_video(video_id, output_path) 