from string import Template
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))
t = Template('Return the $item to $owner.')
#d = dict(item='unladen swallow')
print(t.safe_substitute(item='unladen swallow', owner='Pepe'))
#print(t.substitute(d))
