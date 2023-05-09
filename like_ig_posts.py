import requests
import time

ACCESS_TOKEN = "your_access_token"
HASHTAGS = ["hashtag1", "hashtag2"]

def get_recent_posts(hashtag):
    url = f"https://graph.instagram.com/v12.0/ig_hashtag_search?user_id={user_id}&q={hashtag}&access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    data = response.json()
    return data['data']

def like_post(media_id):
    url = f"https://graph.instagram.com/{media_id}/likes?access_token={ACCESS_TOKEN}"
    response = requests.post(url)
    return response.status_code == 200

while True:
    for hashtag in HASHTAGS:
        posts = get_recent_posts(hashtag)
        for post in posts:
            media_id = post['id']
            if like_post(media_id):
                print(f"Liked post {media_id}")
            time.sleep(10)  # Add delay between actions
    time.sleep(3600)  # Wait an hour before checking again
