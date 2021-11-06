# flipbook

The repo contains the source code from which converts a collection of images to MP4, PDF or GIF format. I also developed it's standalone executable for Windows which can be downloaded from the link https://drive.google.com/file/d/1jq_tQKaI5vh-QFtaGffVDlOzcrJDAAgZ/view?usp=sharing

The commands for the language are to be written in a .flp file and executed as follows ->
.\compiler.exe .\sample.flp

The language currently has support for two datatypes
- `flipbook`
- `int`

Since performing arithmetic operations with ints require complex binary expression tree parsers, I decided to exclude that functionality. Currently ints cannot be used for any purpose whatsoever and are created only for demonstration purposes.

The newline characted is used as separators for different statements and any statement starting with # is treated as a comment and ignored by the compiler.

A new flipbook object is created as follows ->
- `new flipbook fb`

To set width and height of the window, use ->
- `set fb width 500`
- `set fb height 500`

This creates an empty flipbook.

Now you can add images to the flipbook ->
- `add file img1.png to fb`
- `add file img2.png to fb`

You can also add some parameters such as how many frames you want in transition ->
- `add file img3.png to fb smoothness 150`

Adding all the files manually can be tiring. So just keep your files in a folder and add the folder together. Maybe you want the files to have increasing frames as they are being added to create a slow down effect in the end.
- `add folder evolution to fb type linear`

Finally, you can export the flipbook as MP4, GIF or PDF.
- `release fb as evolution.mp4`

There are other useful features also
- Joining one flipbook with another, via command `add reel fb2 to fb1`
- Changing fps of the output, via command `set fb fps 60`

This assignment took me roughly 12-13 hours. I spend 1.5-2 hours designing the Flipbook class and its features. Then a large chunk of my time was spent on developing the parser for the language. This involved rejecting multiple ideas which seemed feasible at first but seemed to be taking too much time later. For example, loops. For loops to be workable, a proper integer datatype was also needed so I scrapped that idea. Then last 1-2 hours were used to convert the script into the executable. There were some problems with the newer versions of python apparently.

Overall this was a fun exercise. The last time I tried to make a parser was in my first year in Introductory Computer Science Course COL100 since I am not a CS major.
If you have any queries, please feel free to contact me at anuj.dhillon.14@gmail.com.


