# PlutoniumSearch
A low-tech distributed brute-force approach of cellular automata pattern searching as a Golly script.

Lastest build: v2.0

## What's new

### v2.0

- Completely rewritten.

## Requires

This script should be run within [Golly](http://golly.sourceforge.net/)

## How to use

(Assuming PlutoniumSearch v1. Will be replaced soon.)

Open Golly, go to `Control > Set Rule...` and set the rule to `B2n3/S23-q`. Then go to `File > Run Script...`, and open the script in the dialog.

Then enter the search space you want to search throughly by specifying the starting slice, the ending slice and the number of preset cells.

The whole symmetrical-along-one-axis 8x8 search space is divided into 256 slices, each of which can be searched seperately with 8 preset cells. A single slice will generally take two or three days, but it depends on your machine. You can divide a slice and only search the first half by multiplying the slice ID by two and then increase the preset cells by one (the next half should be `sliceID * 2 + 1`.)

Then the search should begin. On the status bar (the upper-left corner) you will see how many patterns have been searched. If it founds something interesting it will save it as a text file called "pxx_y.rle" that can be opened with Golly where xx is the period and y is the ID of the interesting pattern **under the folder you store the script**. (If your script is under D:/PlutoniumSearch for example, the result files should also be under the D:/PlutoniumSearch folder.) 

An interesting pattern can be an oscillator or a spaceship, the program does not seperate them for effeciency reasons. For the same reason, the patterns may also be composed of smaller boring oscillators.

Unfortunately almost all of the results are boring, but no one will know until it is uploaded onto the Catagolue stdin.

## Where to upload your results

[Here](https://conwaylife.com/forums/viewtopic.php?f=11&t=4267&p=87836#p87836) or for Chinese users, [here](https://github.com/HuntingBot/Celluar-Automata/issues/114).
