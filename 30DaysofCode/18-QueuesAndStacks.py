class Solution:

    def __init__(self):
        self.char_queue = []
        self.char_stack = []

    def pushCharacter(self, ch):
        self.char_stack.append(ch)

    def enqueueCharacter(self, ch):
        self.char_queue.append(ch)

    def popCharacter(self):
        return self.char_stack.pop()

    def dequeueCharacter(self):
        return self.char_queue.pop(0)
