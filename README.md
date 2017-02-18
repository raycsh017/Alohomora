# Alohomora
A simple python script for opening up websites I use for work.

## What you need
- Python 2

## How to use
1. Place your links to websites in a text file, in `src` folder. As an example, I included `web.txt` inside the `src` folder. 
2. Run Alohomora with the name of the text file given as the first argument. For example:
```bash
python alohomora.py web
```

## Note
- By default, Alohomora uses Chrome browser and opens up a new browser by running `open http://google.com` on the terminal.
- Currently, Alohomora is only able to open up tabs on the opened browser window.