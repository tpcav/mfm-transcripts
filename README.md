# mfm-transcripts
<<<<<<< HEAD
# mfm-yt-transcripts
=======

This repo uses Python to extract YouTube channel video URLs and mass transcript data from those videos.

Download or clone this repo to get started `git clone https://github.com/tpcav/mfm-transcripts.git`. Or see the `main.py` file which has the code for the YouTube Transcript API for Python.

## I. Packages
- JSON Decoder `import json`
- YouTube Transcript API `pip install youtube-transcript-api`
- Once downloaded to start DEMO run: `main.py`

## II. Getting all channel video URLs without YouTube API

1. Go to the YouTube Channel's video page
2. Inspect Element
3. Go to the console
4. Copy this first `var scroll = setInterval(function(){ window.scrollBy(0, 1000)}, 1000);` This code scrolls to the bottom of the channels video page, to the first video.
5. Copy this seconde `window.clearInterval(scroll); console.clear(); urls = $$('a'); urls.forEach(function(v,i,a){if (v.id=="video-title-link"){console.log('\t'+v.title+'\t'+v.href+'\t')}});` This code returns a list in the console of all of the titles and URLs of all the videos of a channel.

## III. Format the links Google Sheets, Excel, etc

### For example:
1. This is a full URL `https://www.youtube.com/watch?v=2dOCPr355TQ`
2. We just want the last part `2dOCPr355TQ` This is the video id.
4. The video ids can be used by the YouTube Transcript API to get the transcript data


## IV. Using youtube-transcript-api 

See `main.py`

## VI. Video Tutorial

TODO, add video file
>>>>>>> f21b92f16b68d1477f2c5be4c429b892b5241b9c
