class Counter():
    def __init__(self, checkpoint=100):
        self.count = 0
        self.checkpoint = checkpoint
        self.last_count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.last_count += 1
        self.count = 0

    def get_count(self):
        return self.last_count

    def is_checkpoint(self):
        self.increment()
        if self.count == self.checkpoint:
            self.reset()
            return True
        else :
            return False