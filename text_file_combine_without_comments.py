import os

out_name = "output.txt"
if os.path.exists(out_name):
    os.remove(out_name)

all_text = ""
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt"):
        f = open(filename)
        all_text = all_text + filename[5:] + "\n\n" + f.read()
        f.close()

f = open(out_name,"w")
f.write(all_text)
f.close()
