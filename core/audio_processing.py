from moviepy.editor import VideoFileClip

def extract_audio(video_path, output_audio_path):
    """
    Extracts audio from a video file, saves it, and returns the audio file path.

    Parameters:
        video_path (str): Path to the video file.
        output_audio_path (str): Path to save the extracted audio.

    Returns:
        str: Path to the saved audio file.
    """
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_audio_path)
    audio.close()
    video.close()
    
    return output_audio_path
