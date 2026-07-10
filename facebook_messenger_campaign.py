import requests
import json

# Facebook Messenger API endpoint
MESSENGER_API_URL = 'https://graph.facebook.com/v8.0/me/messages'

# Replace with your Page access token
PAGE_ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'

def send_message(recipient_id, message_text):
    message = {
        'recipient': {'id': recipient_id},
        'message': {'text': message_text}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(MESSENGER_API_URL,
                             params={'access_token': PAGE_ACCESS_TOKEN},
                             headers=headers,
                             data=json.dumps(message))
    return response.json()

# Replace 'RECIPIENT_ID' with the actual recipient Id
if __name__ == '__main__':
    recipient_id = 'RECIPIENT_ID'  # For example, user ID of a friend
    message_text = 'Check out SERENSTAR platform: https://serenstar.com'
    response = send_message(recipient_id, message_text)
    print(response)