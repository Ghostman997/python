def scan(s):
    directions = ('north', 'south', 'east', 'west')
    s = s.lower()
    s = s.split()
    sout = []
    for sin in s:
        found = 0
        for dir in directions:
            if dir == sin:
                sout.append(('direction', dir))
                found = 1
                break
        if found == 0:
            # return [('direction',dir)]
            sout.append(('error', None))
    return sout

#print scan('north east south')


