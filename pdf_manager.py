# pdf_manager.py
import glob
import os
from datetime import datetime
from PyPDF2 import PdfFileReader, PdfFileWriter


# def datetime_format(): - Finish
# now = datetime.now()
# return {}

def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    fname = fname.split()
    fname = "_".join(fname)
    files = []
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output_filename = '{}_page_{}.pdf'.format(
            fname, page+1)
        files.append(output_filename)

        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(output_filename))

    folder_path = os.path.dirname(os.path.abspath(path))
    folder_path += "/" + fname
    if os.path.isdir(folder_path):
        # Remove forward slash - helper function
        # Year 4d - Month 2d - Date 2d - Hour - Minute - Second
        folder_path = folder_path + str(datetime.now())
    os.mkdir(folder_path)

    for file in files:
        os.rename(file, folder_path + "/" + file)


def run_splitter():
    path = os.path.expanduser(input("Splitter: Please input the file path: "))
    pdf_splitter(path)
    print ("Split successful")


def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()

    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        if path.endswith(".pdf"):
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)


def run_merger():
    in_path = os.path.expanduser(input("Please input the path: "))
    paths = glob.glob(os.path.join(in_path, "*.pdf"))
    paths.sort()
    if " " in in_path:
        in_path = in_path.split()
        in_path = "_".join(in_path)
    merger(os.path.basename(in_path) + "_merged" + ".pdf", paths)
    print("\nMerge Successful.")


if __name__ == "__main__":
    continue_session = True

    while (continue_session):
        choice = input("Welcome to the PDF Splitter and Merger. Please enter 1\
 to use the Splitter, 2 to use the Merger, or any other key to quit: ")
        if choice == "1":
            run_splitter()
        elif choice == "2":
            run_merger()
        else:
            continue_session = False
