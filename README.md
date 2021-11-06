# flipbook

The repo contains the source code from which converts a collection of images to MP4, PDF or GIF format. I also developed it's standalone executable for Windows which is present at the link 

The commands for the language are to be written in a .flp file and executed as follows ->
.\compiler.exe .\sample.flp

The language currently has support for two datatypes
- flipbook
- int

Since performing arithmetic operations with ints require complex binary expression tree parsers, I decided to exclude that functionality. Currently ints cannot be used for any purpose whatsoever and are created only for demonstration purposes.

A new flipbook object is created as follows ->
`new flipbook fb`
