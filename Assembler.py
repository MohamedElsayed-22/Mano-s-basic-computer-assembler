
import utilities

individual_line = []
lst1 = [] 
pass1 = {}
pass2 = {}
st = ""

reference_elements = []
#reference instruction set file
instruction = open('instructions.txt', 'r')
reference = instruction.readlines()
for i in reference:
    reference_elements.append(i.split())
    
    
#Loading the source assembly code
assembly = open('assemblyCode2.txt', 'r')
lines = assembly.readlines()

#omitting the comments. 
for line in lines:
    word = ""
    for character in line:
        if character =="/":
            break
        else:
            word += character
    lst1.append(word)

#creating a nested list where for each line in the file, there exists a list. 
splitted_Data_list = []

#creating variable x that can solve the issue of the empty space at the beginning of some lines.
for line in lst1:
    x = ''
    if line[0] == "\t":
        x = "none"
    if x == '':
        y = line.split()
    else:
        y = line.split()
        y.insert(0, x)
    splitted_Data_list.append(y)

print(splitted_Data_list)
def conversion():
    """
    This function goes through the first pass through calling it directly while the second pass is 
    called in the first pass based on the condition mentioned in the flowchart.
    """
    #Doing the first pass
    def first_pass():
        location_counter = 0
        for i in splitted_Data_list:
            if i[1] == "ORG":
                location_counter = utilities.convert_to_decimal(i[2]) - 2
                # print(location_counter)
            elif i[1] == "END":
                second_pass()
            location_counter += 1

            if i[0] != "none":
                pass1[i[0]] = utilities.convert_to_hexa(location_counter)
                
               
    #Doing the second pass
    def second_pass():
        location_counter = 0
        for i in splitted_Data_list:
            if i[1] == "ORG":
                location_counter = utilities.convert_to_decimal(i[2]) - 2
            location_counter += 1
            if i[1] == "END":
                print("Done!")
            #creating the hexadecimal of the MRI codes
            for k in range (7):
                if i[1] in reference_elements[k]:
                    if (len(i) > 3):
                        pass2[utilities.convert_to_hexa(location_counter)] = reference_elements[k][3]
                    else:
                        pass2[utilities.convert_to_hexa(location_counter)] = reference_elements[k][1]
            #inserting the addresses of the symbolic address
            if (len(i) > 2):
                if (i[2] in pass1):
                    pass2[utilities.convert_to_hexa(location_counter)] += str(pass1[i[2]])
                    
            #converting the non-MRI to hexadecimal code
            for k in range(7, len(reference_elements)):
                if i[1] in reference_elements[k]:
                    pass2[utilities.convert_to_hexa(location_counter)] = reference_elements[k][1]
                if i[1] == ',' and i[2] in reference_elements[k]:
                    pass2[utilities.convert_to_hexa(location_counter)] = reference_elements[k][1]
                #error handling in case of being neither MRI nor non-MRI
                elif i[1] == None:
                    print("Error in line of code")
                
            #including the variables in which the hexa value is stored
            if "HEX" in i:
                num = ''
                for j in range(len(i[3]), 4):
                    num += '0'
                pass2[utilities.convert_to_hexa(location_counter)] = num + i[3]
            #Converting the decimal number to hexadecimal 
            if "DEC" in i:
                hexa = 0
                num = ''
                if int(i[3]) > 0:
                    hexa = hex(int(i[3]))
                    for i in range(len(str(hexa)[2:]), 4):
                        num += '0' 
                else:
                    hexa = utilities.cal_hexa(int(i[3]))
                
                pass2[utilities.convert_to_hexa(location_counter)] = num + str(hexa)[2:]
    first_pass()
            
#calling the function of conversion
conversion()                   

#writing the extracted hexadecimal code in another file
with open("hexadecimal Code.txt", 'w') as output_file: 
    for key, value in pass2.items(): 
        output_file.write('%s    %s\n' % (key, value))




print(pass2)
print(f"\n{pass1}")            
            
        