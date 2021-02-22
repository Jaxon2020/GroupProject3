f = open('http_access_log.log', 'r')
data = f.read()
occurrences = data.count('1994')

print('number of occurrences :', occurrences)
