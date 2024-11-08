import unittest
import os
from core.video_processing import resize_video, add_watermark



class TestVideoProcessing(unittest.TestCase):
   '''Test cases for the video processing functions.'''


   def setUp(self):
       self.video_path = os.path.abspath("tests/files/test_video.mp4")
       self.output_video_path = os.path.abspath("tests/files/resized_test_video.mp4")
       self.watermarked_video_path = os.path.abspath("tests/files/watermarked_test_video.mp4")
       self.width = 640
       self.height = 360
       self.watermark_text = "KieuHoaB2111982"


   def test_resize_video(self):
       '''Test the resize_video function.'''
       result_path = resize_video(self.video_path, self.output_video_path, self.width, self.height)
       self.assertEqual(result_path, self.output_video_path)
       self.assertTrue(os.path.exists(result_path))


   def test_add_watermark(self):
       '''Test the add_watermark function.'''
       # Thêm watermark vào video đã resize
       result_path = add_watermark(self.output_video_path, self.watermark_text, self.watermarked_video_path)
       self.assertEqual(result_path, self.watermarked_video_path)
       self.assertTrue(os.path.exists(result_path))


#    def tearDown(self):
#        '''Log output file status but do not delete it.'''
#        if os.path.exists(self.output_video_path):
#            print(f"[INFO] Output video '{self.output_video_path}' đã được tạo mới.")
#        if os.path.exists(self.watermarked_video_path):
#            print(f"[INFO] Watermarked video '{self.watermarked_video_path}' đã được tạo mới.")




if __name__ == "__main__":
   unittest.main()
