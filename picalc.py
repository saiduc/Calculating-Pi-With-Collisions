class block():
    def __init__(self, position, mass):
        self.x = position   # block position
        self.m = mass       # block mass
        self.v = 0          # block velocity

    def move(self):
        """
        moves the block over 1 unit of time
        simply adds velocity to current position
        """
        self.x = self.x + self.v

    def collide(self, block):
        self.v = (2*block.m*block.v + self.m*self.v -
                  block.m*self.v)/(self.m+block.m)

    def reflect(self):
        self.v = -1*self.v

    def willCollide(self, block):
        if self.v >= 0 and block.v >= 0:
            if block.v > self.v:
                return False
            else:
                return True
        else:
            return True


blockA = block(1, 1)
blockB = block(5, 100)

# testing
print(blockA.x)
blockA.v = 1
blockA.move()
print(blockA.x)
