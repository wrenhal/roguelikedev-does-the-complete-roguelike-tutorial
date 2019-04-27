import tcod as libtcod

import textwrap

# Class for individual messages within the log itself
class Message:
    def __init__(self, text, color=libtcod.blue):
        self.text = text
        self.color = color

# Class to read in the Message Log one message at a time and then display
class MessageLog:
    def __init__(self, x, width, height):
        self.messages = []
        self.x = x
        self.width = width
        self.height = height

    def add_message(self, message):
        # Split the message if necessary, among multiple lines
        new_msg_lines = textwrap.wrap(message.text, self.width)

        for line in new_msg_lines:
            # If the buffer is full, remove the first line to make room for the new one
            if len(self.messages) == self.height:
                del self.messages[0]

            # Add the new line as a Message object, with the text and the color
            self.messages.append(Message(line, message.color))