
print("Howdy! Welcome to TCMG 412 Team 9 Using Python Project.")
print("This code is intended to analyze and parse a log file and display outputs for total requests made and requests made in the last year (data from 1994).")
print("Team 9: Juan Quiroz, Jaxon Reeves, Jose Obregon, Joseph Yeh.")

# The command below opens and reads the log file
f = open('http_access_log.log', 'r')

# The program then counts the number of lines from 1994
number_of_lines= 0
x= 1994
count = 0
# The program continues by counting the total number of lines from the log file
for line in f :
    line =line.strip("/n")
    number_of_lines += 1 
# The log file is closed
f.close ()

# The results of the total requests made and total requests made in the last year of 1994 are displayed 
print("The total requests that has been made is: ", number_of_lines, " and the total request made last year is ", )
print("Thank you for running our code! -Team 9")
