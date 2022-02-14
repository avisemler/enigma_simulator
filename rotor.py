class Rotor:
    def __init__(self, links, rotation, move_next, config):
        """
        Each 'physical' part of the disk has a letter associated to it.

        Links is a string showing the substiutions used compared to normal
        alphabet.

        A 'pointer' is kept to the top of the disk, which is changed when the disk
        rotates.

        rotation: the Grundstellung - the initial rotation of the rotor
        move_next: the letter whose presence at the top of the wheel causes the
                    next rotor to be rotated an extra time - the British called
                    this 'turnover'
        """
        self.links = links.lower()
        self.rotation = rotation
        #store the original value to let the rotor be reset
        self.original_rotation = rotation
        self.move_next = move_next
        self.config = config

    def get_output(self, letter, reverse=False):
        """
        Returns the value that a given letter would get sent to given the current
        state of the rotor.
        """
        rotated_letter = self.rotate(letter, self.rotation)
        return self.rotate(self.get_connected(rotated_letter, reverse=reverse), -self.rotation)

    def get_connected(self, letter, reverse):
        #reverse is a boolean for the direction of the flow of current
        #through the rotor
        if not reverse:
            return self.links[self.config.alphabet.index(letter)]
        else:
            return self.config.alphabet[self.links.index(letter)]

    def rotate(self, letter, amount):
        """
        Returns the letter corresponding to the location that would be reached
        by rotating a given letter (position) a given amount.
        """
        position = (self.config.alphabet.index(letter) + amount) % 26
        return self.config.alphabet[position]

    def get_top_letter(self):
        """
        Returns the letter that would be visible at the top of a physical rotor
        with the current rotation.
        """
        return self.config.alphabet[self.rotation]

    def turn(self):
        self.rotation += 1

    def should_turn_next(self):
        """
        Returns true if the next rotor should move according to the turnover system.
        """
        return self.get_top_letter() == self.move_next

    def reset(self):
        """
        Revert to the initial state of the rotor.
        """
        self.rotation = self.original_rotation