
import sys
from frequencies import frequencies


class Line:                                        # create the class "Line"

    def __init__(self, content: str):              # prompt to enter type(str)
        self.content = content                     # store content of line
        self.length = len(self.content)            # get length of line

    def __repr__(self):                            # representation method
        length = self.length
        return f'({length})' + self.content        # output: (length of line) line content

    def __lt__(self, other_value):                 # less than method to check line length
        if self.length < other_value.length:       # check len(line) against other lines
            return self.length
        else:
            return "Line longer than other length"

    def __eq__(self, other_value):                 # equal method to check line length
        if self.length == other_value.length:      # check len(line) == other lines
            return self.length
        else:
            return "Line not equal to other length"


with open(sys.argv[1], "r") as f:                  # open file (Index position[1] because [0] is the file itself

    filtered = filter(lambda line: line.strip() != '', f)       # strips file of empty lines

    mapped = map(lambda line: Line(line.strip()), filtered)     # maps each remaining line to an instance of Line

    sorted_list = list(sorted(mapped))             # use the __lt__ and __eq__ methods to sort lines

# BONUS POINTS
    print("\n".join(repr(line) for line in sorted_list))        # joins the lines from the sorted list


# P a r t   3 #

    keys = list(repr(line) for line in sorted_list)             # instances of Line as keys

    values = [frequencies(line.content) for line in sorted_list]  # frequency of each character in each line

# BONUS POINTS
    line_dict = {k: v for (k, v) in zip(keys, values)}          # create a dict with key, value pairs for each line

    print(line_dict)
