'''
This file contains the unit tests for the video_processing module.
'''

import unittest
import os
from core.video_processing import resize_video

class TestVideoProcessing(unittest.TestCase):
    '''Test cases for the video processing functions.'''

    def setUp(self):
        self.video_path = "tests/files/test_video.mp4"
        self.output_video_path = "tests/files/resized_test_video.mp4"
        self.width = 640
        self.height = 360

    def test_resize_video(self):
        '''Test the resize_video function.'''
        result_path = resize_video(self.video_path, self.output_video_path, self.width, self.height)
        self.assertEqual(result_path, self.output_video_path)
        self.assertTrue(os.path.exists(result_path))

    def tearDown(self):
        if os.path.exists(self.output_video_path):
            os.remove(self.output_video_path)

if __name__ == "__main__":
    unittest.main()
