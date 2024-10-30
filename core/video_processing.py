"""
This module contains functions for processing videos.

Functions:
    resize_video(video_path, output_video_path, width, height):
"""

from moviepy.editor import VideoFileClip

def resize_video(video_path, output_video_path, width, height):
    """
    Resizes the input video to the specified width and height.

    Parameters:
        video_path (str): Path to the original video file.
        output_video_path (str): Path to save the resized video.
        width (int): Target width for the video.
        height (int): Target height for the video.

    Returns:
        str: Path to the resized video.
    """
    video = VideoFileClip(video_path)
    resized_video = video.resize(newsize=(width, height))
    resized_video.write_videofile(output_video_path)
    resized_video.close()
    video.close()
    return output_video_path
