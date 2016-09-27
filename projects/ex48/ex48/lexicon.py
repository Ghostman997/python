def scan(s):
      directions = ('north', 'south', 'east', 'west')
      for dir in directions:
        if dir == s:
            return('direction', dir)
        return ('error', None)


#print scan('north')


