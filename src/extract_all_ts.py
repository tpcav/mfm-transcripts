import json
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from youtube_transcript_api.formatters import JSONFormatter

def generate_transcript(video_id):
    try:
        # Must be a single transcript.
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        script = ""

        for text in transcript:
            t = text["text"]
            if t != '[Music]':
                script += t + " "

        return script, len(script.split())
    except TranscriptsDisabled:
        # Return an empty string and 0 if the transcript is disabled
        return "", 0

# Open the text file in read mode
with open('urls.txt', 'r') as file:
    # Read the list of video IDs from the file
    video_ids = file.read().splitlines()

# Get the total number of videos
total_videos = len(video_ids)

# Initialize a counter for the current video
current_video = 1

# Loop through the list of video IDs
for video_id in video_ids:
    print(f'Processing video {current_video} of {total_videos}')
    transcript, no_of_words = generate_transcript(video_id)

    formatter = JSONFormatter()

    # .format_transcript(transcript) turns the transcript into a JSON string.
    json_formatted = formatter.format_transcript(transcript)

    # Create a dictionary to store the transcript data
    transcript_data = {
        'video_id': video_id,
        'transcript': transcript,
        'word_count': no_of_words
    }

    # Write the transcript data to a JSON file
    with open('video.json', 'w', encoding='utf-8') as json_file:
        json.dump(transcript_data, json_file, ensure_ascii=False)

    # Increment the counter for the current video
    current_video += 1