# GetCommentAutomation
Automation tool to get comment from youtube videos

## Installation From CMD/Terminal

```
$ py -m pip install lxml 
$ py -m pip install cssselect
$ py -m pip install requests
```

### Run Program

```
$ py getcomment.py --youtubeid [...] --output [file]
```
With webID contains - (Dash) in the beginning
```
$ py getcomment.py -y=-idwithdash --output [file]
Or
$ py getcomment.py --youtubeid=-idwithdash --output [file] 
```
