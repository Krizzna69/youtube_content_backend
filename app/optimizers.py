from app.gemini_client import GeminiClient


class ContentOptimizer:
    """YouTube content optimization using Gemini AI."""

    def __init__(self):
        self.client = GeminiClient()

    def generate_title(self, summary, target_length=60):
        """Generate an engaging, SEO-optimized title.

        Args:
            summary (str): Video summary or content description
            target_length (int): Target title length

        Returns:
            str: Optimized title
        """
        prompt = f"""
        As a YouTube SEO expert, create a highly clickable, engaging title for a video with the following content:

        {summary}

        The title should:
        - Be no longer than {target_length} characters
        - Include relevant keywords for search optimization
        - Be engaging and create curiosity
        - Not be clickbait or misleading
        - Follow current YouTube best practices

        Return only the title text and nothing else.
        """

        return self.client.generate_content(prompt, temperature=0.8)

    def suggest_tags(self, summary, count=10):
        """Generate SEO-optimized tags for a video.

        Args:
            summary (str): Video summary or content description
            count (int): Number of tags to generate

        Returns:
            list: List of suggested tags
        """
        prompt = f"""
        As a YouTube SEO expert, suggest {count} highly effective tags for a video with the following content:

        {summary}

        The tags should:
        - Include a mix of broad, medium-tail, and long-tail keywords
        - Be relevant to the video content
        - Include trending and searchable terms
        - Not exceed 500 characters in total

        Return only a comma-separated list of tags with no additional text.
        """

        tags_text = self.client.generate_content(prompt, temperature=0.7)
        return [tag.strip() for tag in tags_text.split(',')]

    def write_description(self, summary, tone="informative", include_timestamps=False):
        """Generate an SEO-optimized video description.

        Args:
            summary (str): Video summary or content description
            tone (str): Tone of the description (informative, conversational, professional)
            include_timestamps (bool): Whether to include timestamp placeholders

        Returns:
            str: Optimized video description
        """
        prompt = f"""
        As a YouTube SEO expert, write a compelling description for a video with the following content:

        {summary}

        The description should:
        - Have a {tone} tone
        - Include relevant keywords naturally 
        - Have a clear call-to-action
        - Be formatted with paragraphs and spacing for readability
        - Be 150-200 words in length
        {"- Include 3-5 timestamp placeholders for key moments" if include_timestamps else ""}

        Follow YouTube best practices for descriptions that maximize engagement and discoverability.
        """

        return self.client.generate_content(prompt, temperature=0.7, max_output_tokens=1000)

    def thumbnail_text_suggestions(self, title, summary):
        """Generate text suggestions for video thumbnail.

        Args:
            title (str): Video title
            summary (str): Video summary

        Returns:
            list: List of thumbnail text suggestions
        """
        prompt = f"""
        As a YouTube thumbnail designer, suggest 3 short text options to overlay on a thumbnail for a video with:

        Title: {title}
        Content: {summary}

        The text suggestions should:
        - Be very short (1-4 words each)
        - Be highly attention-grabbing
        - Create curiosity or emotion
        - Complement the title without repeating it exactly

        Return only the 3 options as a numbered list with no additional text.
        """

        suggestions = self.client.generate_content(prompt, temperature=0.9)
        return [line.strip() for line in suggestions.split('\n') if line.strip()]