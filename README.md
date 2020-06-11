# E-Paper News
A program which pulls the latest headlines and displays them to a Raspberry Pi E-Paper HAT

## Setting up the Raspberry Pi

`sudo raspi-config`

In order to use this program you must enable SPI, this is for the E-Ink Display.

Option 5 - Interfacing Options >> Option 4 - Enable SPI >> Yes

## Dependencies
This program requires the drivers for your respective Waveshare E-Ink Display. This can be found on the Waveshare github page.
I have included the drivers for my board, as well as the epdconfig.py file.

In addition, you will need to install NewsAPI for python from the following command:

`$pip3 install newsapi-python`

Note: You will need to create your own NewsAPI key in order for this program to work correctly!

## Installing the program

`git clone https://github.com/hscot/e_paper_News`

## Using The Program

In order to use this program, simply copy your API key, and paste it into the sections within e-paper.py which require it. After that, you're good to go! Enter the following command:

`python3 e-paper.py`

And the E-Ink should flash a few times, then display the information of the top 5 headlines per your source, in your desired language.

Note: My sample source is "Die-Zeit", a German newspaper, so just be aware you will have to change the source to your desired language.
