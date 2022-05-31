# e621-md5-python-For-hydrus

 convert md5 WebM from e621 to a e621 mp4 URL

This is so you can get the mp4 version of the WebM File hosted on e621.net.

## Todo

Check the ["Projects"](https://github.com/users/Dividedby0KSJ/projects/1) For the current todo list and In Progress items.

## Why

lets say you have A iphone want want to watch a... wholsom video on e621.net.

All Apple devices dont natraly support WebM encoding.
But e621 provides a mp4 version for most of there WebM files (Not All but most of them).

So you can watch it on the website becues its giving you the .mp4 version instead of the .WebM version.

But now you want to dlownload it.
When you click "download" it will try to download the original .WebM file, not the compatible .mp4 file.

a simple way to fix it on the spot is to just change the end of the URL from .WebM to .mp4

but if you have bulk downloaded a lot of video files you dont have the url, and if you have renamed the file it makes it harder.

## Hydrus

This gets even harder when you use [Hydrus](https://github.com/hydrusnetwork/hydrus) to download a lot of video from e621 and use a program like [Hydrus-Web](https://github.com/floogulinc/hydrus-web) or [
Hybooru](https://github.com/funmaker/Hybooru) to stream it to your devices that dont support WebM encoding.

When complet this tool will let you batch download the mp4 version of the file from hydrus and add them to your spank_ba- ... wholsom colection :)

Right now the only [Hydrus](https://github.com/hydrusnetwork/hydrus) intergration is manaly batch copy the md5's and add the output urls to the [Hydrus](https://github.com/hydrusnetwork/hydrus) downloader

## Setup

make 2 text files.

```text
URL.txt
&
md5.txt
```

- Add the md5's to the md5 file and run the program.
- Check the URL file for a list of urls to download.
