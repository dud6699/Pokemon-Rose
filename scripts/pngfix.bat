#!/bin/bash

# run script from D:\Drive Files\Game_Files\scripts with Git Bash
# bash ./pngfix "../p"

find "$1" -type f -iname '*.png' -exec ./pngcrush_1_8_11_w64.exe -s -ow -rem iCCP '{}' \;
