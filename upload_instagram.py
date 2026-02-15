import requests
import json

class InstagramUploader:
    def __init__(self, access_token, video_path, caption):
        self.access_token = access_token
        self.video_path = video_path
        self.caption = caption
        self.video_id = None

    def upload_video(self):
        # Step 1: Upload the video
        upload_url = f'https://graph-video.facebook.com/v12.0/me/media?access_token={self.access_token}'
        video_file = open(self.video_path, 'rb')
        files = {'video_file': video_file}
        response = requests.post(upload_url, files=files)

        if response.status_code == 200:
            self.video_id = response.json()['id']
            print('Video uploaded successfully!')
        else:
            print('Failed to upload video:', response.json())

    def publish_video(self):
        if not self.video_id:
            print('No video uploaded to publish.')
            return

        # Step 2: Publish the video
        publish_url = f'https://graph.facebook.com/v12.0/{self.video_id}/publish?access_token={self.access_token}'
        data = {'caption': self.caption}
        response = requests.post(publish_url, json=data)

        if response.status_code == 200:
            print('Video published successfully!')
        else:
            print('Failed to publish video:', response.json())

# Example Usage
# uploader = InstagramUploader('YOUR_ACCESS_TOKEN', 'path_to_your_video.mp4', 'Your Video Caption')
# uploader.upload_video()
# uploader.publish_video()