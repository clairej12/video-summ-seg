#!/bin/bash

cat=$1 # take first cmd line arg
DIR=/mnt/data1/jielin/msmo/annotation/; # /data/jielin/msmo/video/;
OUT=/mnt/data1/claire/video-summ/segments/; # /home/jielin/claire/video-summ/keyframes/sift/;
VID=/mnt/data1/jielin/msmo/video/;
HOMEDIR=$PWD;

# echo $DIR$cat
for subcat in $DIR$cat/*;do
    echo $subcat
    for annotation in `find $subcat -name "*2[1-9].json"`;do
        cd $HOMEDIR
        name=${annotation##*/};
        folder_name=${name%.json};
        # echo $name
        # echo $folder_name
        trunc=$(dirname "$subcat")
        subfolder=$(basename "$trunc")/$(basename "$subcat")
        outfolder=$OUT$subfolder/$folder_name
        video=$VID$subfolder/$folder_name".mp4"
        # echo $annotation
        # echo $video
        echo $outfolder
        mkdir -p $outfolder
        python segment.py $annotation $video $outfolder
    done
done