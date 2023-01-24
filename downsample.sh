#!/bin/bash

cat=$1 # take first cmd line arg
DIR=/data/jielin/claire/video-summ-segments/; # /mnt/data1/jielin/msmo/annotation/; 
HOMEDIR=$PWD;
fps='1'

# echo $DIR$cat
for subcat in $DIR$cat/*;do
    # echo $subcat
    for video in $subcat/*;do
    # echo $video
        for seg in `find $video -name "segment_*[0-9].mp4"`;do
            cd $HOMEDIR
            name=${seg##*/};
            echo $seg
            trunc=$(dirname "$video")
            subfolder=$(basename "$trunc")/$(basename "$video")
            outfolder=$video/downsample
            # echo $annotation
            # echo $video
            # echo $outfolder
            mkdir -p $outfolder
            python downsample.py $seg $outfolder $fps
        done
    done
done