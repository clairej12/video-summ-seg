import cv2
import sys
import os
import time
import pdb

def getSampledFrameList(video, new_fps):
    t1 = time.time()
    print("Sampling to {} FPS".format(new_fps))
    FRAME_RATE = video.get(cv2.CAP_PROP_FPS)
    skip = int(FRAME_RATE / new_fps)
    print('{}/{} -> {}'.format(FRAME_RATE,new_fps,skip))

    def getFrameList(vid, skip):
        frame_list = []
        ret, frame = vid.read()
        i = 0
        while ret:
            if skip < 1 or i%skip == 0:
                frame_list.append(frame)
            ret, frame = vid.read()
            i += 1
        print('{} frames read from {} total'.format(len(frame_list), vid.get(cv2.CAP_PROP_FRAME_COUNT)))
        vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
        return frame_list

    frame_list = getFrameList(video, skip)
    print("Done in {} Sec".format(round(time.time()-t1)))
    return frame_list

def getSampledInputVideo(video, filename, out_dir, fps, width, height):
    vidname = filename.split('/')[-1]
    name = out_dir+'/{}_fps_{}.{}'.format(vidname.split('.')[0],fps,vidname.split('.')[1])
    print('downsampled video: ', name)
    if os.path.exists(name):
        return name
    frame_list = getSampledFrameList(video,fps)
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    # pdb.set_trace()
    output_video = cv2.VideoWriter(name,fourcc,fps,(int(width),int(height)))
    for frame in frame_list:
        output_video.write(frame)
    output_video.release()
    return name

if __name__ == '__main__':
    pdb.set_trace()
    filename = sys.argv[1]
    out_dir = sys.argv[2]
    fps = int(sys.argv[3])
    video = cv2.VideoCapture(filename)
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    getSampledInputVideo(video, filename, out_dir, fps, width, height)

# /data/jielin/claire/video-summ-segments/animals/amphibians/ANIAMP0021/segment_0.mp4
# /data/jielin/msmo/video/animals/amphibians/ANIAMP0022.mp4