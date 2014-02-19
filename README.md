mindmaps-2-tex-converter
========================


This python code takes as input a mindmap and converts it either into a nice Latexed list or into beamer slides.

To create mindmaps I can recommend free mind : [project page and download](http://freemind.sourceforge.net/wiki/index.php/Main_Page)





Usage: download files. Then open python interpreter e.g. ipython and type

    from texcreator import *

    convert_mm_2_beamer('/path/to/MindMap.mm','/path/to/beamer.tex')

    convert_mm_2_tex('/path/to/MindMap.mm','/path/to/list.tex')


On UNIX system texcreator can be used standalone (map to list only) using

    chomd +x 'texcreator.py'

Needs to be run only once to make the script executable. And invoking it
with

    ./texconverter.py <map_file> <desired_path_for_list>


afterwards create pdf from latex file in command line as follows:

    pdflatex /path/to/beamer.tex


Enjoy!
