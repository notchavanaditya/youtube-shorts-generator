# youtube-shorts-generator
This code is a Python script for generating motivational videos with random backgrounds and audio. It uses the  library to manipulate video and audio files, and the  library to read data from a CSV file.

Motivational Video Generator
===========================

A Python script for generating motivational videos with random backgrounds and audio.

Requirements
------------

* Python 3.7 or higher
* `moviepy` library
* `csv` library

Usage
-----

1. Install the required packages by running `pip install moviepy`.
2. Prepare a CSV file with the following columns:
	* `row_number`: The row number in the CSV file.
	* `header_text`: The text to be displayed at the top of the video.
	* `quote_part1`: The first part of the motivational quote.
	* `quote_part2`: The second part of the motivational quote.
2. Place the CSV file in the same directory as the script.
3. Update the `video_folder`, `audio_folder`, and `output_folder` variables in the script with the paths to your video, audio, and output directories.
4. Run the script using `python motivational_video_generator.py`.
5. The script will generate a video for each row in the CSV file and save it to the output folder.

Notes
-----

* The script uses the `moviepy` library to manipulate video and audio files.
* The `csv` library is used to read data from the CSV file.
* Put your background audios and videos in the folder '/background/audios' & '/background/videos'
* The script selects a random background video and audio file for each video.
* The text overlays are added to the video using the `moviepy` library.
* The script can be customized to use different data sources or video/audio files.
