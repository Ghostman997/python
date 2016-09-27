def scan(s):
      directions = ('north', 'south', 'east', 'west')
     # s = s.lower()
     # s = s.split()
      for dir in directions:
        if dir == s:
            return [('direction',dir)]
        return ('error', None)


#print scan('north')


