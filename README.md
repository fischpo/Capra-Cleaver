<p align="center"><img src="https://github.com/Mushroom-po/Capra-Cleaver/blob/main/capra.ico?raw=true"></p>

# Capra-Cleaver
A script using ffmpeg to seamlessly cut videos, making sure that the final output has no loss in quality.


# Features
- <b>Cut videos into any number of segments</b>


- <b>Remove segments from a video</b>

# Installation
Make sure you have FFmpeg installed.
You can install it from the following site :

https://www.ffmpeg.org/download.html

The FFmpeg provided with the Capra-Cleaver executable can be installed from here:

https://github.com/BtbN/FFmpeg-Builds

If you have python installed, you can directly run the script;

Otherwise, you can install the exe from [Releases](https://github.com/Mushroom-po/Capra-Cleaver/releases).
# Basic Formats:
Text File:
```
/ for comments place / in the beginning
base=path of directory
file_name start_timestamp end_timestamp
```
Settings:
```
# false: split a video into segments, true: remove parts from a video, auto: pass value as argument in command line

cleave_way=false

# supported video formats, add a format not here

vfor=[mkv,mp4,mov,wmv,avi]

# true: skip specific timestamps on execution

skip_choice=false

# true: output as logs

cm_logs=false

# true: ffmpeg output as logs

fflogs=false

# value: make_zero , auto , make_non_negative , disabled

avoid_negative_ts=make_zero
```

Command Line:
```
cleaver.exe -c True
cleaver.exe -f {Path to text file}
cleaver.exe -f {Path to text file} -c False
cleaver.exe -c True -f {Path to text file}
```

# How To Use?

You can either use Capra Cleaver as a script or an executable.

FFmpeg should be in the directory of the script or should be an environment variable.

When the script is first executed, it will create an environment file which is basically your settings.

You can pass a text file in the following [format](https://github.com/Mushroom-po/Capra-Cleaver#basic-formats) as an argument.

The script will also create cleave.txt when no argument is passed which will become the default text file to be used in case of no argument.

## Following snippets aim to clarify the usage:
> Here we are using the default text file and a folder in downloads.
##### Setting:
```
cleave_way=auto
```
##### Text File:
```
base=C:\Users\{name}\Desktop\Ebi wan

ebi.mkv 01:52 02:46

ebi 2.mp4 00:55 01:26 11:25 16:30 20:00 24:22

ebi_3.mp4 10:35 01:35:00
```
## Cleave into segments :
```
capra.exe -c false
```
   ##### This will cleave the files according to the specified timestamps.   
   
  
## Remove segments :
```
capra.exe -c true
```
   ##### This will remove the specified timestamps.


# Possible solutions for issues in video
While the videos are successfully cleaved most of the time , there may be times when it doesn't work.

If there is some delay between removed parts of a video then either change the timestamps by a few seconds or change the value of `avoid_negative_ts` in settings.

If the cleaved videos are of incorrect timestamp then try adjusting the timestamps by a few seconds.

Incorrect timestamp / Delay may also be caused by subtitles in a video so try cleaving without the subs.

# License

This is licensed under GPL-3.0-or-later.
Check out [License](https://github.com/Mushroom-po/Capra-Cleaver/blob/main/LICENSE) for more info.
