import tensorflow as tf

from utils import backbone
from api import object_counting_api

input_video = "./input_images_and_videos/Night Time Traffic Camera video.mp4"


detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_coco_2018_01_28', 'mscoco_label_map.pbtxt')

is_color_recognition_enabled = True 
roi = 237 
deviation = 4.5 
custom_object_name = 'Vehicle' 

object_counting_api.cumulative_object_counting_y_axis(input_video, detection_graph, category_index, is_color_recognition_enabled, roi, deviation, custom_object_name) # counting all the objects
