class Win_verification():
    """
    Class to centralize winning verification
    """

    def __init__():
        pass

    def v(b, p):
        """
        Returns true if p wins on board b, else false
        """

        # Checks all possible 3 in a row options
        if (b[0][0] == p and b[0][1] == p and b[0][2] == p): return True
        if (b[1][0] == p and b[1][1] == p and b[1][2] == p): return True
        if (b[2][0] == p and b[2][1] == p and b[2][2] == p): return True

        if (b[0][0] == p and b[1][0] == p and b[2][0] == p): return True
        if (b[0][1] == p and b[1][1] == p and b[2][1] == p): return True
        if (b[0][2] == p and b[1][2] == p and b[2][2] == p): return True

        if (b[0][0] == p and b[1][1] == p and b[2][2] == p): return True
        if (b[2][0] == p and b[1][1] == p and b[0][2] == p): return True

        return False