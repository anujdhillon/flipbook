# flipbook

The repo contains the source code from which converts a collection of images to MP4, PDF or GIF format. I also developed it's standalone executable for Windows which is present at the link 

The commands for the language are to be written in a .flp file and executed as follows ->
.\compiler.exe .\sample.flp

The language currently has support for two datatypes
- `flipbook`
- `int`

Since performing arithmetic operations with ints require complex binary expression tree parsers, I decided to exclude that functionality. Currently ints cannot be used for any purpose whatsoever and are created only for demonstration purposes.

The newline characted is used as separators for different statements and any statement starting with # is treated as a comment and ignored by the compiler.

A new flipbook object is created as follows ->
-`new flipbook fb`

To set width and height of the window, use ->
-`set fb width 500`
-`set fb height 500`

This creates an empty flipbook.

Now you can add images to the flipbook ->
-`add file img1.png to fb`
-`add file img2.png to fb`

You can also add some parameters such as how many frames you want in transition ->
-`add file img3.png to fb smoothness 150`

Adding all the files manually can be tiring. So just keep your files in a folder and add the folder together. Maybe you want the files to have increasing frames as they are being added to create a slow down effect in the end.
-`add folder evolution to fb type linear`

Finally, you can export the flipbook as MP4, GIF or PDF.
-`release fb as evolution.mp4`


