# GetCommentAutomation
Automation tool to get comment from youtube videos

## Installation From CMD/Terminal with Python3

```
$ py -m pip install lxml 
$ py -m pip install cssselect
$ py -m pip install requests
```
### To Get YoutubeID
From URL: https://www.youtube.com/watch?v=OGLFirnHHes&...
YoutubeID: OGLFirnHHes

### Run Program

```
$ py getcomment.py --youtubeid [...] --output [file]
```
With YoutubeID contains - (Dash) in the beginning
```
$ py getcomment.py -y=-idwithdash --output [file]
```
Or
```
$ py getcomment.py --youtubeid=-idwithdash --output [file] 
```
