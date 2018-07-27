# PDF Manager
This program has two capabilities, to split a PDF into a folder of its pages
as PDFs and to merge a folder of PDF pages into one PDF. The program prompts
the user to input a choice - run the Splitter, the Merger, or to quit. Should
the user choose the Splitter or the Merger, the user will be prompted to input
the path to be managed. This program was created to sort double page playbills
and single page playbills contained in a single PDF for proper pagination.

## PDF Manager
#### Running
In Terminal, cd into the folder where the download is desired. Enter ``python3
pdf_manager.py`` Full pathname may be needed. Follow the prompt, entering 1
to use the Splitter, 2 to use the Merger, or any other key to quit. The program
will keep running until a force quit or until any other key is entered. Then follow
instructions to enter the proper path.

### Splitter
Enter the full pathname of the PDF to be split. The program will split the
PDF into its respective pages, naming the resulting PDFs according to their
lsidy file title and their specific page number. The PDFs are sorted into a
folder named after the lsidy file title.

### Merger
Enter the full pathname of the folder to be merged. The program will merge the folder
into one PDF, named for the lsidy file, containing the word "merged". Merging a folder
does not destroy the folder.

## Installation
Download the folder.

## Authors
Program adapted from the original written by Mike from Mouse vs. Python
(https://www.blog.pythonlibrary.org/2018/04/11/splitting-and-merging-pdfs-with-python/)

Alec Escobar
Anastasia Hutnick 
