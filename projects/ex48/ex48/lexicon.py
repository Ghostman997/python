def scan(s):
    directions = ('north', 'south', 'east', 'west')
    verbs = ('go', 'eat', 'kill')
    stops = ('the', 'in', 'of')
    nouns = ('bear', 'princess')
   #s = s.lower()
    s = s.split()
    sout = []
    for sin in s:
        found = 0
        for dir in directions:
            if dir == sin:
                sout.append(('direction', dir))
                found = 1
                break
        for ver in verbs:
            if ver == sin:
                sout.append(('verb', ver))
                found = 1
                break
        for sto in stops:
            if sto == sin:
                sout.append(('stop', sto))
                found = 1
                break
        for nou in nouns:
            if nou == sin:
                sout.append(('noun', nou))
                found = 1
                break
        try:
            numbers = int(sin)
            sout.append(('number', numbers))
            found = 1
        except ValueError:
            pass
        if found == 0:
            # return [('direction',dir)]
            sout.append(('error', sin))
   #print s
   #print sin
    return sout

#print scan('north east south')
#print scan('go eat kill')
#print scan('the in of')
#print scan('bear princess')
#print scan('bear IAS princess')
#print scan("3 91234")
