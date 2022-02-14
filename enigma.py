class Enigma:
    """
    This class uses composition of the various components of the enigma
    to encode messages.
    """
    def __init__(self, rotors, plugboard, reflector):
        #conventionally, the rotors are listed in the opposite order
        #to the way in which the current actually passes through them.
        #reverse the rotor list to be compatible with this.
        self.rotors = rotors[::-1]
        self.plugboard = plugboard
        self.reflector = reflector

    def encode(self, message):
        """
        Outputs an encoded version of the message.
        """
        result = ""
        for letter in message:
            #First the letters pass through the plugboard
            letter = self.plugboard.transform(letter)

            #rotate any rotor that need rotating according to the turnover
            #system
            turn_next = True  #records if the next rotor should be turned.
            #the value is initially true so that the first rotor always gets turned.
            for rotor in self.rotors:
                if turn_next:
                    rotor.turn()
                if rotor.should_turn_next():
                    turn_next = True
                else:
                    turn_next = False

            for rotor in self.rotors:
                #Send the letter through each rotor
                letter = rotor.get_output(letter)

            #After passing through the rotors once, reflect
            letter = self.reflector.get_output(letter)

            #pass through the rotors in reverse
            for rotor in reversed(self.rotors):
                letter = rotor.get_output(letter, reverse=True)
            letter = self.plugboard.transform(letter)

            #append the letter from the output of the process the result
            result += letter
        return result

    def get_settings(self):
        result = []
        for rotor in self.rotors:
            result.append(rotor.get_top_letter())
        return result[::-1]

    def reset(self):
        """
        Returns each rotor to its initial setting.
        """
        for rotor in self.rotors:
            rotor.reset()
