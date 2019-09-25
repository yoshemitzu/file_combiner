import os # import a module to allow us to work with system files easily

out_name = "output.txt" # a name for the output file
if os.path.exists(out_name): # check if there's already an output file
    os.remove(out_name) # remove the output file if it exists already

all_text = "" # initialize a variable to store the text in
for filename in os.listdir(os.getcwd()): # iterate over all the files in the current directory
    if filename.endswith(".txt"): # ignore non-.txt files (like the script we're running)
        f = open(filename) # open the text file for reading and declare variable f to refer to this file
        all_text = all_text + filename[5:] + "\n\n" + f.read() # append the filename, a couple line breaks, and the text of each file. Python will add a line break between each by default
        # the filename[5:] part above will omit the first 4 characters of each filename from the text we append.
        f.close() # close the file for reading

f = open(out_name,"w") # open the output text file for writing
f.write(all_text) # write the text variable we created above to the file
f.close() # close the output text file when we're done with it.
