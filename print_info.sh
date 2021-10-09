#!/bin/sh


echo "time:" `date` >info.txt
echo "user:" $USER >>info.txt
echo "os:" `uname` >>info.txt
echo "num folders in" ` pwd ./` ":" `ls -l | grep "^d"|wc -l` >>info.txt
echo "num files in "` pwd ./` ":" `ls -l | grep "^-"|wc -l` >>info.txt

