
import sys
from frequencies import frequencies


with open(sys.argv[1], "rt") as f:      # open file (Index position[1] because [0] is the file itself
    content = frequencies(f.read())     # create content variable by calling the def frequencies
                                        # frequencies calculates the frequency of each character in file
                                        # and creates a dict with letter: frequency pairs

sort_freqs = dict(sorted(content.items(), key=lambda item: item[1], reverse=True))
                                        # sort the entries in the dict by most frequent (-> reverse=True)

# BONUS POINTS
totalChars = sum(sort_freqs.values())   # use the sum() method to sum up all the frequencies of all characters
freq_percent = {}

for key in sort_freqs.keys():           # iterate over each key and get its value
    val = sort_freqs.get(key)
    freq_percent[key] = round(((val * 1.0) / totalChars) * 100, 2)
                                        # divide by the total sum of frequencies and round to two decimals
print(sort_freqs)
print(freq_percent)
