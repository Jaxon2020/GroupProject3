f = open('http_access_log.log', 'r')

number_of_lines= 0
x= 1994
count = 0

for line in f :
    line =line.strip("/n")
    number_of_lines += 1 


f.close ()

print("The total requests that has been made is: ", number_of_lines, ' and the total request made last year is ', )