import os


def make_new_filename(row):

    output_name='output_%s.csv'
    
    x = './' + (output_name  % row)
    
    return(x)

def split(filehandler, num_of_rows, keep_headers):
    """
    Splits a CSV file into x number of rows 
        """
    import csv

    index = 1
    #can specify the delimiter here
    delimiter=','
    
    #defining the reader
    reader = csv.reader(filehandler, delimiter=delimiter)

    #making the first file
    current_out_path = make_new_filename(1)
    print(current_out_path)

    current_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
    
    current_limit = num_of_rows
##    
    if keep_headers:

        #for the first row keep the headers
        headers = reader.next()
        current_writer.writerow(headers)
        
    for i, row in enumerate(reader):

        # if you're at the Size limit time to output all you've read
        if i + 1 > current_limit:
            
            index += 1
            current_out_path = make_new_filename(index)
            current_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
            
            if keep_headers:
                current_writer.writerow(headers)

        #otherwise just keep writing
        current_writer.writerow(row)
##
def main():

    num_rows = input('Enter number of rows: ')
    keep_headers = raw_input('Keep headers? (yes/no) :')
    file_name = raw_input('Enter the file name:')

    if keep_headers == 'yes':
        keep_headers = True
    else:
        keep_headers= False


    split(open(file_name, 'r'),num_rows, keep_headers)
    
    print('now go make megan a coffee')
    


main()
