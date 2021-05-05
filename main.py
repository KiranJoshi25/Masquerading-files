
#Library imports
import os
import binascii
import pathlib
import csv
import time 
results = []
count_files = 0 

#dictionary of file extension and header, key value pair
dictionary = {'.jpg': b'ffd8f','.py': b'66726',
              '.html': b'3c484','.mp4': b'00000','.txt': b'41737' ,'.png': b'89504',
              '.pdf': b'25504','.exe': b'4d5a7','.docx': b'504b0' 
              }



#function to get a key from dictionaary
def get_key(value):

    for i in dictionary:
        if dictionary[i] == value:
            return i



#get files appearing extension
def get_file_extension(file):

    file_extension = pathlib.Path(file).suffix
    return file_extension


#get file header
def get_file_header(file):

    with open(file, 'rb') as f:
        content = f.read()
        hex_i = binascii.hexlify(content)
        R = hex_i[0:5]
        #print(file)
        #print(R)
        key = get_key(R)
        return key




#scan file and compare header
def scan_file(filename):

    file_ext = get_file_extension(filename)
    #print("appearing",file_ext)
    key = get_file_header(filename)

    #print("actual",key)
    
    if file_ext != key:
    	if key == None:
    		pass
    	else:
        	results.append([filename,file_ext,key])





# read the files from every directory
def read_dir(path):

    for root, directories, filenames in os.walk(path):
        for directory in directories:
            os.path.join(root, directory)
        for filename in filenames:
            scan_file(os.path.join(root,filename))
            count_files+=1
# function to append the result in a csv file
def append_results(results):
    with open('result.csv', 'w') as f:
        W = csv.writer(f)
        W.writerow(["filename","appearing extension","actual extension"])
        W.writerows(results)
        W.writerow(["found {} masquerading files".format(len(results))])



# directory path goes here 
path = "New folder"


#measuring a running timme of the program code and calling the functions
start = time.time()
read_dir(path)
append_results(results)
end = time.time()
print("Scanned {} files in {} seconds".format(count_files,end - start))

