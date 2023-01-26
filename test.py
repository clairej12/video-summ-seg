import cv2
video_path = "/home/jielin/claire/video-summ/video-summ-seg/test.mp4"

capture = cv2.VideoCapture(video_path)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)


print("isOpened:", capture.isOpened())
print("height:", frame_height)
print("width:", frame_width)
