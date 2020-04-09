# PlutoniumSearch
A low-tech distributed brute-force approach of cellular automata pattern searching as a Golly script.

Lastest build: v1.1.1

## Requires

This script should be run within [Golly](http://golly.sourceforge.net/).

## How to use

Open Golly, go to `File > Run Script`, and open the script in the dialog.

Then enter the search space you want to search throughly.

The whole symmetrical-along-one-axis 8x8 (hard-coded) search space is divided into 256 slices (still hard-coded), each of which can be searched seperately. You'll have to specify a interval of search space by entering the starting slice and the ending slice. If you want to search only one slice, then the two numbers should be the same.

Then the search should begin. On the status bar (the upper-left corner) you will see how many patterns have been tested. If it founds something interesting it will save it as a text file called "pxx_y.txt" where xx is the period and y is the ID of the interesting pattern **under the folder you store the script**. (If your script is under D:/PlutoniumSearch for example, the result files should also be under the D:/PlutoniumSearch folder.)

An interesting pattern can be an oscillator or a spaceship, the program does not seperate them for effeciency reasons. For the same reason, the patterns may also be composed of smaller boring oscillators.

Unfortunately almost all of the results are boring, but no one will know until it is uploaded onto the Catagolue stdin.

## Where to upload your results

[Here](https://conwaylife.com/forums/viewtopic.php?f=11&t=4267&p=87836#p87836) or for Chinese users, [here](https://github.com/HuntingBot/Celluar-Automata/issues/114).
