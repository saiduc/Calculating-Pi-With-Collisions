class block():
    def __init__(self, position, mass):
        self.x = position   # block position
        self.m = mass       # block mass
        self.p = 0          # block momentum
        self.v = 0          # block velocity

    def move(self):
        """
        moves the block over 1 unit of time
        simply adds velocity to current position
        """
        self.x = self.x + self.v


blockA = block(1, 1)
blockB = block(5, 100)

# testing
print(blockA.x)
blockA.v = 1
blockA.move()
print(blockA.x)
