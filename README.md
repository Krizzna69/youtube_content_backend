# YouTube Content Optimizer Backend

```markdown name=backend/README.md
# YouTube Content Optimizer - Backend

## Overview

This is the backend service for the YouTube Content Optimizer, an AI-powered tool that helps content creators enhance the discoverability and appeal of their videos. Using Google's Gemini AI, this API generates optimized titles, descriptions, tags, and thumbnail text suggestions based on video content input.

## Features

- **AI-Powered Content Generation**: Leverages Google's Gemini API to create engaging, SEO-optimized content
- **Multiple Generation Types**: Generate titles, descriptions, tags, and thumbnail text
- **Customizable Parameters**: Control tone, length, and style of generated content
- **REST API**: Simple endpoints for easy integration with any frontend
- **Optional YouTube API Integration**: Can be connected to YouTube Data API for analytics and direct publishing

## Architecture

```
backend/
├── app/                    # Core application modules
│   ├── __init__.py         # Package initialization
│   ├── gemini_client.py    # Gemini API integration
│   ├── optimizers.py       # Content optimization logic
│   └── youtube_api.py      # Optional YouTube API integration
├── api.py                  # Flask API endpoints
├── requirements.txt        # Project dependencies
└── README.md               # This file
```

## Requirements

- Python 3.8 or higher
- Google Gemini API key
- (Optional) YouTube Data API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Krizzna69/youtube_content_backend.git
   
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the backend directory:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   YOUTUBE_API_KEY=your_youtube_api_key_here  # Optional
   ```

## API Endpoints

### Generate Title

Generates an optimized title for a YouTube video.

- **URL:** `/api/generate-title`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "summary": "A detailed description or summary of your video content",
    "category": "Technology"
  }
  ```
- **Response:**
  ```json
  {
    "title": "Optimized YouTube title here"
  }
  ```

### Generate Description

Generates an SEO-optimized description for a YouTube video.

- **URL:** `/api/generate-description`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "summary": "A detailed description or summary of your video content",
    "category": "Technology",
    "tone": "informative",
    "includeTimestamps": true
  }
  ```
- **Response:**
  ```json
  {
    "description": "Optimized YouTube description with timestamps here..."
  }
  ```

### Suggest Tags

Generates relevant tags for a YouTube video.

- **URL:** `/api/suggest-tags`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "summary": "A detailed description or summary of your video content",
    "category": "Technology",
    "count": 10
  }
  ```
- **Response:**
  ```json
  {
    "tags": ["tag1", "tag2", "tag3", "...]
  }
  ```

### Thumbnail Text Suggestions

Generates text suggestions for video thumbnails.

- **URL:** `/api/thumbnail-text`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "summary": "A detailed description or summary of your video content",
    "title": "Your video title"
  }
  ```
- **Response:**
  ```json
  {
    "suggestions": ["Text 1", "Text 2", "Text 3"]
  }
  ```

## Running the Server

Start the Flask development server:

```bash
python api.py
```

By default, the server runs at `http://localhost:5000`.

## Configuration Options

You can customize the behavior of the API by modifying the following:

- **Gemini API Parameters**: Edit `gemini_client.py` to change temperature, max tokens, etc.
- **Optimization Prompts**: Modify the prompts in `optimizers.py` to change the output style.
- **Flask Settings**: Adjust CORS settings, debug mode, etc. in `api.py`.

## Integration with YouTube API (Optional)

To enable YouTube API integration:

1. Obtain credentials from the [Google Developer Console](https://console.developers.google.com/)
2. Add your credentials to the `.env` file
3. Uncomment the YouTube API routes in `api.py`

## Error Handling

The API returns appropriate HTTP status codes and error messages:

- **400 Bad Request**: Missing required parameters
- **401 Unauthorized**: Invalid API key
- **500 Internal Server Error**: Server-side issues or API rate limits

## Future Improvements

- Add caching to reduce API calls
- Implement user authentication
- Add analytics for generated content performance
- Support more languages
- Expand to other social media platforms

## License

[MIT License](LICENSE)
```

This README provides comprehensive documentation for your backend folder, including setup instructions, API endpoint details, and configuration options. You can customize it further based on specific details of your implementation.