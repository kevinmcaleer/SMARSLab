""" models the command history class """


class CommandHistory(object):
    """ models the command history object """
    history = []

    def __init__(self):
        self.history.append("*** new history ***")

    def append(self, command):
        """ adds a command to the command history """
        print(len(self.history))
        if len(self.history) < 10:
            self.history.append(command)
        elif len(self.history) == 10:
            for command_item in range(0, 9):
                self.history[command_item] = self.history[command_item+1]
            self.history.pop()
            self.history.append(command)

    def clear(self):
        """ clears the command history """
        self.history = []
