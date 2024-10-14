# Import everything needed to edit video clips
from moviepy.editor import *
 
# loading video dsa gfg intro video
original = VideoFileClip("input/video.mp4")
 
edit = VideoFileClip("input/christina.mp4")

name = original.subclip(0, 1)
unedit = original.subclip(1.5,)
 
# concatenating both the clips
final = concatenate_videoclips([edit, unedit])
#writing the video into a file / saving the combined video
final.write_videofile("results/merged_output.mp4", audio_codec="aac")
 
