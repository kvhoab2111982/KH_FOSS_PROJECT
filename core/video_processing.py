from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

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

def add_watermark(video_path, watermark_text, output_video_path, position=('right', 'bottom')):
    """
    Adds a watermark to the input video at the specified position.

    Parameters:
        video_path (str): Path to the original video file.
        watermark_text (str): Text to be used as the watermark.
        output_video_path (str): Path to save the watermarked video.
        position (tuple): Position of the watermark ('left', 'right', 'top', 'bottom').

    Returns:
        str: Path to the watermarked video.
    """
    video = VideoFileClip(video_path)

    watermark = TextClip(
        watermark_text,
        fontsize=24,
        color='white',
        font='Arial',
        stroke_color='black',
        stroke_width=1,
        method='caption'  
    ).set_duration(video.duration).set_opacity(0.6)


    if position == ('right', 'bottom'):
        watermark = watermark.set_position(("right", "bottom"))
    elif position == ('left', 'bottom'):
        watermark = watermark.set_position(("left", "bottom"))
    elif position == ('right', 'top'):
        watermark = watermark.set_position(("right", "top"))
    elif position == ('left', 'top'):
        watermark = watermark.set_position(("left", "top"))
    else:
        watermark = watermark.set_position(("center", "center"))

    watermarked_video = CompositeVideoClip([video, watermark])


    watermarked_video.write_videofile(output_video_path, codec='libx264', audio_codec='aac')


    video.close()
    watermarked_video.close()
    return output_video_path
