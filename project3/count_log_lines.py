f = open('http_access_log.log', 'r')

number_of_lines= 0

for line in f :
    line =line.strip("/n")

    number_of_lines += 1 

f.close ()

print("The total requests that has been made last year is: ", number_of_lines)