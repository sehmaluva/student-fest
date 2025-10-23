import os, sys
import getopt 

def convert_word_to_pdf(word_file, pdf_file): 
    '''
    Import convert to turn .docx to .pdf
    word_file : str, path to input .docx file
    pdf_file : str, path to output .pdf file
    '''
    try:
        from docx2pdf import convert
    except ImportError:
        print("The 'docx2pdf' library is not installed. Please install it using 'pip install docx2pdf'.")
        sys.exit(1)

    try:
        convert(word_file, pdf_file) #Use convert function from docx2pdf to turn .docx into .pdf
        print(f"Successfully converted '{word_file}' to '{pdf_file}'")
    except Exception as e:
        print(f"An error occurred during conversion: {e}") 

def help():
    print("Usage: Word file (.docx) to PDF file (.pdf) converter")
    print("-w: input .docx folder.")
    print("-o: output .pdf folder.")
    print("-h: display this help message.")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:],'w:o:h')
    except getopt.GetoptError:
        print("Usage: python Word-PDFConverter.py -w inputfolder -o outputfolder")
        sys.exit(1)

    #Get input and output folder from command line arguments
    for opt, arg in opts:
        if opt == '-w':
            inputfolder = arg
        elif opt == '-o':
            outputfolder = arg
        elif opt == '-h':
            help()
            sys.exit()
        else:
            print(f"{opt} is not defined. Please use -h for options list.")
            sys.exit(3)
    
    if not os.path.exists(inputfolder):
        print(f"{inputfolder} not exist.")
        sys.exit(2)

    if not os.path.exists(outputfolder):
        os.makedirs(outputfolder)

    counter = 0
    
    #Loop through all .docx files until all converted to .pdf 
    #Keeps track of how many total .docx files converted
    for filename in os.listdir(inputfolder): 
        if filename.lower().endswith('.docx'):
            f1 = os.path.join(inputfolder, filename)
            f2 = os.path.join(outputfolder, filename[:-5] + ".pdf")
            convert_word_to_pdf(word_file = f1, pdf_file = f2) 
            counter += 1
    print(f"Converted {counter} files.")

                        
            
    


if __name__ == "__main__":
    main()