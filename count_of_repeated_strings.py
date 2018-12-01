from collections import defaultdict
tally = defaultdict(int)
text = "one two two three three three"
for i in text.split():
    tally[i] += 1
print tally