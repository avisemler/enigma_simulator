class Plugboard:
    """
    Swaps given pairs of letters.
    """
    def __init__(self, settings_string):
        self.pairs = settings_string.split(" ")
        
    def transform(self, letter):
        for pair in self.pairs:
            if letter in pair:
                if pair[0] == letter:
                    return pair[1]
                else:
                    return pair[0]
        return letter
