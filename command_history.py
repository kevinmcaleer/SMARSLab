""" models the command history class """


class CommandHistory(object):
    """ models the command history object """

    history = []

    def __init__(self):
        self.history.append("*** new history ***")

    def append(self, command):
        """ adds a command to the command history """    
        self.history.append(command)

    def clear(self):
        """ clears the command history """
        self.history = []

    def get_history(self):
        """ get all command history """
        return self.history

    def get_last_ten(self):
        """ get last 10 command history """
        return self.history[-10:]
