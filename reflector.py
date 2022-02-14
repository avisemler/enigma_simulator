class Reflector:
    """
    Implements the component that performs a substitution cipher
    on the message after having passed through the rotors once.
    """
    def __init__(self, links, config):
        #links is a list, such that the first letter in alphabet
        #gets mapped to the first letter in link, and so forth
        self.links = links.lower()
        self.config = config

    def get_output(self, letter):
        """
        Maps a letter to its destination.
        """
        return self.links[self.config.alphabet.index(letter)]