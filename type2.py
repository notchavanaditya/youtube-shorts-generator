import csv
import os
import random
import textwrap
from moviepy.editor import *
from moviepy.video.fx import all as vfx
from tqdm import tqdm

# ... (keep the existing get_random_file_from_folder and create_video functions)

def get_random_file_from_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith(('.mp4','.mp3', '.avi', '.webm'))]
    if not files:
        raise ValueError(f"No files found in folder: {folder_path}")
    return os.path.join(folder_path, random.choice(files))

def create_video(header_text, quote_part1, quote_part2, output_filename, video_folder, audio_folder):
    tqdm.write(f"Creating video: {output_filename}")
    background_video_path = get_random_file_from_folder(video_folder)
    background_video = VideoFileClip(background_video_path, audio=False)

    while background_video.duration < 10:
        background_video = concatenate_videoclips([background_video, background_video])

    background_video = background_video.subclip(0, 10)
    background_video = vfx.crop(background_video, width=1080, height=1920)

    video_width = 1080
    video_height = 1920

    header_clip = TextClip(header_text, fontsize=40, color='white', size=(video_width, None)).set_duration(10)
    header_clip = header_clip.set_position((video_width / 2, video_height * 0.3)).set_position(('center', 'top'))
    header_clip = header_clip.on_color(size=(header_clip.w + 10, header_clip.h + 10), color=(0, 0, 0), pos=(5, 5))  # Set background color with padding

    quote_part1_lines = textwrap.wrap(quote_part1, width=20)
    quote_part1_text = '\n'.join(quote_part1_lines)

    quote_part1_clip = TextClip(quote_part1_text, fontsize=80, color='black', stroke_color='black', stroke_width=6, size=(video_width, None)).set_duration(7)
    quote_part1_clip = quote_part1_clip.set_position((video_width/2, video_height/3)).set_position(('center', 'center'))

    quote_part2_lines = textwrap.wrap(quote_part2, width=20)
    quote_part2_text = '\n'.join(quote_part2_lines)

    quote_part2_clip = TextClip(quote_part2_text, fontsize=80, color='black', stroke_color='black', stroke_width=6, size=(video_width, None)).set_duration(2).set_start(8)
    quote_part2_clip = quote_part2_clip.set_position((video_width/2, video_height/3)).set_position(('center', 'center'))

    credit_text = "@dailyfactsedu"
    credit_fontsize = 28
    credit_margin_x = video_width * 0.1  # Adjust the value to set the left and right margins
    credit_margin_y = video_height * 0.2  # Adjust the value to set the top and bottom margins

    credit_clip = TextClip(credit_text, fontsize=credit_fontsize, color='white', stroke_color='black', stroke_width=2, size=(video_width - 3 * credit_margin_x, None)).set_duration(10)
    credit_x = (video_width - credit_clip.w) / 2  # Calculate the x position for center alignment
    credit_clip = credit_clip.set_position((credit_x, video_height - credit_margin_y))

    final_clip = CompositeVideoClip([background_video, header_clip, quote_part1_clip, quote_part2_clip, credit_clip])
    final_clip = final_clip.resize((video_width, video_height))

    background_audio_path = get_random_file_from_folder(audio_folder)
    background_audio = AudioFileClip(background_audio_path).subclip(0, 10)
    final_clip = final_clip.set_audio(background_audio)

    final_clip.write_videofile(output_filename, fps=24, threads=8)
    tqdm.write(f"{output_filename} created successfully.")

def process_rows(rows, video_folder, audio_folder, output_folder):
    with tqdm(total=len(rows), desc="Processing CSV rows") as pbar:
        for row in rows:
            row_number = row[0]
            header_text = row[1]
            quote_part1 = row[2]
            quote_part2 = row[3]
            output_filename = f"{output_folder}/{row_number}_{quote_part1}.mp4"
            create_video(header_text, quote_part1, quote_part2, output_filename, video_folder, audio_folder)
            pbar.update()

video_folder = "/home/grimarc/Disks/Os/Youtube Short Generator/background/videos"
audio_folder = "/home/grimarc/Disks/Os/Youtube Short Generator/background/audios"
output_folder = "/home/grimarc/Disks/Os/Youtube Short Generator/output"

with open('data.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    rows = list(csv_reader)

    process_rows(rows, video_folder, audio_folder, output_folder)
