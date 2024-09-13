from moviepy.editor import *

text = "Chúc mừng sinh nhật!"

text_clip = TextClip(text, fontsize=70, color='white', bg_color='blue', size=(640, 480), method='caption')

text_clip = text_clip.set_duration(5)

audio_clip = AudioFileClip("path_to_your_audio_file.mp3").subclip(0, 5)

video_clip = text_clip.set_audio(audio_clip)

video_clip.write_videofile("birthday_video.mp4", fps=24)
