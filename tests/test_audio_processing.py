'''Test cases for the audio processing functions.'''

import unittest
import os
from core.audio_processing import extract_audio

class TestAudioProcessing(unittest.TestCase):
    '''Test cases for the audio processing functions.'''
    def setUp(self):
        # Paths to test files (replace these with actual test paths as needed)
        self.video_path = "tests/files/test_video.mp4"
        self.output_audio_path = "tests/files/test_audio.mp3"

    def test_extract_audio(self):
        '''Test the extract_audio function.'''
        # Run the extract_audio function and capture the returned path
        result_path = extract_audio(self.video_path, self.output_audio_path)

        # Check if the returned path is correct and if the file was created
        self.assertEqual(result_path, self.output_audio_path)
        self.assertTrue(os.path.exists(result_path))

    def tearDown(self):
        '''Clean up the test files after tests.'''
        # Cleanup test files
        if os.path.exists(self.output_audio_path):
            os.remove(self.output_audio_path)

if __name__ == "__main__":
    unittest.main()
