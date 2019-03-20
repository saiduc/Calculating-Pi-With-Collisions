from fractions import Fraction


class block:
    def __init__(self, position, mass):
        self.x = position        # block position
        self.m = mass            # block mass
        self.v = Fraction(0, 1)   # block velocity

    def reflect(self):
        """
        reverses velocity for elastic collision with wall of infinite mass
        """
        self.v = -1*self.v


def collide(leftBlock, rightBlock):
    """
    collides the two blocks and updates their velocities
    uses formulae derived from conservation of energy and momentum expressions
    """
    v_A = leftBlock.v
    v_B = rightBlock.v
    m_A = leftBlock.m
    m_B = rightBlock.m
    v_A_new = (2*v_B*m_B + m_A*v_A - m_B*v_A)/(m_A + m_B)
    v_B_new = (2*v_A*m_A + m_B*v_B - m_A*v_B)/(m_A + m_B)
    leftBlock.v = v_A_new
    rightBlock.v = v_B_new
    return


def update(leftBlock, rightBlock):
    """
    updates position of blocks by adding velocity multiplied by timeToCollide
    this is necessary instead of moving by fixed time quanta, since otherwise
    there is a possibility of blocks passing over each other
    """
    t = timeToCollide(leftBlock, rightBlock)
    leftBlock.x = leftBlock.x + t*leftBlock.v
    rightBlock.x = rightBlock.x + t*rightBlock.v
    return


def timeToCollide(leftBlock, rightBlock):
    """
    calculates time before the next collision between the two blocks
    """
    # both blocks moving right but rightBlock is faster, so no future collision
    if rightBlock.v >= leftBlock.v >= 0:
        return float("inf")

    # blocks moving towards each other
    elif leftBlock.v >= 0 >= rightBlock.v:
        return Fraction(rightBlock.x - leftBlock.x, leftBlock.v - rightBlock.v)

    # blocks moving left but leftBlock is faster so will collide with wall first
    elif (rightBlock.v >= 0 and leftBlock.v < 0) or (leftBlock.v <= rightBlock.v < 0):
        return Fraction(-leftBlock.x, leftBlock.v)

    # leftBlock currently at wall
    elif leftBlock.x == 0:
        # rightBlock too fast for leftBlock to catch up so no future collisions
        if rightBlock.v >= abs(leftBlock.v):
            return float("inf")
        # rightBlock moving left or slow enough for leftBlock to catch up
        else:
            return Fraction(rightBlock.x, abs(leftBlock.v)-rightBlock.v)

    # blocks moving left but rightBlock faster so will collide with leftBlock
    else:
        return min(Fraction(-leftBlock.x, leftBlock.v),
                   Fraction(rightBlock.x-leftBlock.x, leftBlock.v-rightBlock.v))


if __name__ == '__main__':
    # define initial values for blockA and blockB
    # mass of blockB is a power of 100. Number of digits of pi is power+1
    blockA = block(Fraction(50, 10), 1)
    blockB = block(Fraction(70, 10), 100**2)
    blockB.v = Fraction(-1, 1)

    # speeds up program by limiting float length
    blockA.x = blockA.x.limit_denominator(2**16)
    blockB.x = blockB.x.limit_denominator(2**16)
    blockA.v = blockA.v.limit_denominator(2**16)
    blockB.v = blockB.v.limit_denominator(2**16)

    counter = 0
    while timeToCollide(blockA, blockB) != float("inf"):
        update(blockA, blockB)

        if blockA.x == blockB.x != 0:
            collide(blockA, blockB)
            counter += 1

        elif blockA.x == 0 != blockB.x:
            blockA.reflect()
            counter += 1

        elif blockA.x == blockB.x == 0:
            blockA.reflect()
            blockB.reflect()
            counter += 2

        else:
            pass
    print("pi is", counter)
