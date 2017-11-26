# Clue-Less
Clue-Less GUI code and images.

## Get PyDev for Eclipse IDE
In Eclipse, navigate to Help > Eclipse Marketplace...

Search for PyDev, and install.

## Convert .ui files to .py files
Navigate to the "pyuic5.bat" file within your Python folder (e.g., C:\Users\<id>\AppData\Local\Programs\Python\Python35-52\Lib\site-packages\PyQt5).

In the command line execute the following command:
pyuic5 <project location>\ClueLess.ui >> <project location>\ClueLess.py

e.g., pyuic5 D:\Documents\eclipse-oxygen-workspace\Clue-Less\ClueLess.ui >> D:\Documents\eclipse-oxygen-workspace\Clue-Less\ClueLess.py
