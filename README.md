<p align="center"><img src="https://github.com/fischpo/Capra-Cleaver/blob/main/capra.ico?raw=true"></p>

# Capra-Cleaver
A script using ffmpeg to seamlessly cut videos, making sure that the final output has no loss in quality.


# Features
- <b>Cut videos into multiple parts</b>


- <b>Remove parts from a video</b>

# Installation
If you have python installed, you can directly run the script;
Otherwise, you can install the exe from [Releases](https://github.com/fischpo/Capra-Cleaver/releases).

Also, make sure you have FFmpeg installed.
You can install it from [here](https://www.ffmpeg.org/download.html)

# Basic Formats:
### Text File:
```
/ for comments place / in the beginning
base=path of directory
file_name start_timestamp end_timestamp
```
### Settings:
 `cleave_way`

If set to true, the script will remove parts from the video. Otherwise, it will cut the video into parts.You can also set it to auto, so that value is set in cmd using *-c* argument.

`vfor`

It includes a list of file formats the script will accept. You can add a format not here, only it should be supported by ffmpeg.

`skip_choice`

Set it to true if you want to avoid the video from being cut into specific timestamps.

`cm_logs`

If set to true, it will create a log file containing the script output. Also, the script won't display any output on screen.

`fflogs`

You can set it to true if you would like the ffmpeg output as logs.

`avoid_negative_ts`

This decides what happens if the video has a negative timestamp.
For more clarity, you can refer to the [docs](https://ffmpeg.org/ffmpeg-all.html).

### Command Line:
```
cleaver.exe -c True
cleaver.exe -f {Path to text file}
cleaver.exe -e {Path where cut file is stored}
cleaver.exe -e {Path} -f {Path to text file} -c False
cleaver.exe -c True -e {Path} -f {Path to text file}
```

# How To Use?

You can either use Capra Cleaver as a script or an executable.

FFmpeg should be in the directory of the script or should be an environment variable.

When the script is first executed, it will create an environment file which is basically your settings.

You can pass a text file in the following [format](https://github.com/fischpo/Capra-Cleaver#basic-formats) as an argument.

The script will also create cleave.txt when no argument is passed which will become the default text file to be used in case of no argument.

## Following snippets aim to clarify the usage:
> Here we are using the default text file and a folder in desktop.
### Setting:
```
cleave_way=auto
```
### Text File:
```
base=C:\Users\{name}\Desktop\Ebi

ebi.mkv 01:52 02:46

ebi 2.mp4 00:55 01:26 11:25 16:30 20:00 24:22

ebi_3.mp4 10:35 01:35:00
```
### Text File with new feature:
```
base=C:\Users\{name}\Desktop\Ebi

|| 01:52 02:46

|2| 00:55 01:26 11:25 16:30 20:00 24:22

|3| 10:35 01:35:00
```
### Cut into parts :
```
capra.exe -c false
```
This will cleave the files according to the specified timestamps.   
   
  
### Remove parts :
```
capra.exe -c true
```
This will remove the specified timestamps.


# Possible solutions for issues in video
While the videos are successfully cut most of the time , there may be times when it doesn't work.

This is due to the fact that the cut needs to be at keyframes.

If there is some delay between removed parts of a video then either change the timestamps by a few seconds or change the value of `avoid_negative_ts` in settings.

If the cut videos are of incorrect timestamp then try adjusting the timestamps by a few seconds.

Incorrect timestamp / Delay may also be caused by subtitles in a video so try cutting without the subs.
