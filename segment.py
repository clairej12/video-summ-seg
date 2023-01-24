from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import json
import sys
import pdb

def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def main(metafile,filename,out_dir):
    f = open(metafile)
    annotation = json.load(f)
    segments = annotation["summary"]
    for seg in segments:
        start_str = seg["start_time"]
        start = get_sec(start_str)
        end_str = seg["end_time"]
        end = get_sec(end_str)
        outfile = out_dir + "/segment_" + str(seg["segment"]) + ".mp4"
        print(outfile)
        ffmpeg_extract_subclip(filename, start, end, targetname=outfile)

if __name__ == '__main__':
    annotation = sys.argv[1]
    video = sys.argv[2]
    outdir = sys.argv[3]
    main(annotation,video,outdir)

# python segment.py /mnt/data1/jielin/msmo/annotation/animals/amphibians/ANIAMP0022.json /mnt/data1/jielin/msmo/video/animals/amphibians/ANIAMP0022.mp4 /mnt/data1/claire/video-summ/segments/animals/amphibians/ANIAMP0022