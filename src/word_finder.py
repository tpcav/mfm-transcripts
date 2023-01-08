def search_for_idea(transcript, num_words_after=20):
  # Initialize an empty list to store the results
  results = []

  # Iterate through the list of dictionaries
  for line in transcript:
    # Split the line's transcript into a list of individual words
    words = line['transcript'].split()

    # Initialize a counter to keep track of our current position in the list
    i = 0

    # Iterate through the list of words
    while i < len(words):
      # Check if the current word is "idea"
      if words[i] == "idea":
        # If it is, add the word and the next `num_words_after` words to the results list
        result = {
          'transcript': words[i:i+num_words_after+1]
        }
        results.append(result)
      # Increment the counter to move to the next word
      i += 1

  # Return the list of results
  return results

transcript = [
  {
    "video_id": "kd_CEW4WksY",
    "transcript": "This is the first line of the transcript. It doesn't contain the word idea."
  },
  {
    "video_id": "kd_CEW4WksY",
    "transcript": "This is the second line of the transcript. It has the word idea in it."
  },
  {
    "video_id": "kd_CEW4WksY",
    "transcript": "This is the third line of the transcript. It also contains the word idea."
  },
  {
    "video_id": "kd_CEW4WksY",
    "transcript": "This is the fourth line of the transcript. It does not contain the word idea."
  }
]

print(search_for_idea(transcript))