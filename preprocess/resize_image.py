
path = '/fs/vulcan-projects/misc_forensics/DATA_FUXIAO/frame_and_transcript/1461652993187717123/keyframes_ff/frame_0.jpg'

import cv2


src = cv2.imread(path, cv2.IMREAD_UNCHANGED)
print(src.shape)
#percent by which the image is resized
scale_percent = 50

#calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)
# dsize
dsize = (256, 256)
# resize image
output = cv2.resize(src, dsize)
print(output.shape)

cv2.imwrite('./sample.jpg',output)
