################################################
# Created by Djordje Rajic for needs in RO
# course. Convert .toy file to verilog file
# DISCLAIMER
# This is not an official program, it is quick
# solution for a problem that was at hand
# feel free to improve this program.
#################################################


import os.path  # We need to check if file exists


listCom = []
listNum = []
newListNum = []
filename = input("Enter filename with extension:")
# Check if file exists
if not os.path.isfile(filename):
    print("File does not exist!")
    exit(-1)

# Open file and save values after space in list
# TODO: We should really check if file is valid
with open(filename, 'r') as file:
    for row in file:
        number, command = row.split()
        listCom.append(command)
        listNum.append(number)

# We need to get rid of : in our numbering, this step is not
# necessary but it makes me feel better

for num in listNum:
    newListNum.append(num.replace(":", ""))

# Some messages for the user
print("Your code")
print("-----------------------")
for line in listCom:
    print(line)
print("-----------------------")

out_file = open("output.v", "w")

for line, number in zip(listCom, newListNum):
    out_file.write("toy_i.mem_i.mem['h" + number + "] = 'h" + line +
                   ";\n")

out_file.close()
print("File has been created : output.v")
print("-----------------------")
print("Bye!")
