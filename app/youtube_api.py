import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pickle

# YouTube API scopes
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']


def get_authenticated_service():
    """Get authenticated YouTube API service."""
    credentials = None

    # Load credentials from token.pickle if available
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)

    # If credentials not valid, refresh or create new ones
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
            credentials = flow.run_local_server(port=8080)

        # Save credentials for future use
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    return build('youtube', 'v3', credentials=credentials)


class YouTubeAPIClient:
    """Client for interacting with the YouTube Data API."""

    def __init__(self):
        self.youtube = get_authenticated_service()

    def get_channel_videos(self, channel_id=None, max_results=10):
        """Get videos from a channel or authenticated user's channel."""
        try:
            if channel_id:
                # Get videos from specific channel
                request = self.youtube.search().list(
                    part="snippet",
                    channelId=channel_id,
                    maxResults=max_results,
                    order="date",
                    type="video"
                )
            else:
                # Get videos from authenticated user's channel
                request = self.youtube.videos().list(
                    part="snippet,statistics",
                    mine=True,
                    maxResults=max_results
                )

            response = request.execute()
            return response.get('items', [])

        except HttpError as e:
            print(f"YouTube API error: {e}")
            return []

    def update_video_metadata(self, video_id, title=None, description=None, tags=None):
        """Update a video's metadata (title, description, tags)."""
        try:
            # First, get the current video data
            video_response = self.youtube.videos().list(
                part="snippet",
                id=video_id
            ).execute()

            if not video_response['items']:
                return False, "Video not found"

            # Get the snippet
            snippet = video_response['items'][0]['snippet']

            # Update only the fields that are provided
            if title:
                snippet['title'] = title
            if description:
                snippet['description'] = description
            if tags:
                snippet['tags'] = tags

            # Update the video
            response = self.youtube.videos().update(
                part="snippet",
                body={
                    "id": video_id,
                    "snippet": snippet
                }
            ).execute()

            return True, response

        except HttpError as e:
            error_message = f"YouTube API error: {e}"
            return False, error_message

    def get_video_analytics(self, video_id):
        """Get basic analytics for a video."""
        try:
            # Get video statistics
            stats_response = self.youtube.videos().list(
                part="statistics",
                id=video_id
            ).execute()

            if not stats_response['items']:
                return None

            return stats_response['items'][0]['statistics']

        except HttpError as e:
            print(f"YouTube API error: {e}")
            return None