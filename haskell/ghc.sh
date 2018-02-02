#!/bin/bash

basename=$1 # 引数からファイル名を受取る
filename=${basename%.*} # 拡張子を取った名前

ghc -o ${filename} ${filename}.hs
rm ${filename}.hi
rm ${filename}.o
./${filename}