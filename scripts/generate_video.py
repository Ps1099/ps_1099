#!/usr/bin/env python3
import json
import os
import requests
from datetime import datetime

HEYGEN_API_KEY = os.getenv('HEYGEN_API_KEY')
HEYGEN_API_URL = 'https://api.heygen.com/v1/video_requests'

def load_topics():
    with open('config/topics.json', 'r') as f:
        return json.load(f)

def generate_video():
    topics = load_topics()
    topic = topics['topics'][0]  # Get first topic for this run
    
    headers = {
        'X-Api-Key': HEYGEN_API_KEY,
        'Content-Type': 'application/json'
    }
    
    payload = {
        'caption': topic['title'],
        'dimension': {
            'width': 1080,
            'height': 1920
        }
    }
    
    try:
        response = requests.post(HEYGEN_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        video_data = response.json()
        video_id = video_data.get('data', {}).get('video_id')
        
        print(f'Video generated successfully with ID: {video_id}')
        
        # Save video ID for upload scripts
        with open('video_id.txt', 'w') as f:
            f.write(video_id)
        
        return video_id
    except requests.exceptions.RequestException as e:
        print(f'Error generating video: {e}')
        raise

if __name__ == '__main__':
    generate_video()