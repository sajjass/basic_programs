def divisions(below, *dividers):
    return (n for n in xrange(below) if 0 in (n % d for d in dividers))
    #empty = []
    #for n in xrange(below):
    #    for d in dividers:
    #        if n%d == 0:
    #            empty.append(n)
    #return empty

print(sum(divisions(1000, 3, 5)))