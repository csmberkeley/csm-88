def bathtub(n):
    """Simulates a battle between the jedi and darth vader over a populace
    of rubber duckies.

    >>> annihilator = bathtub(500)
    >>> darth_vader = annihilator(10)
    >>> darth_vader()
    490 duckies left
    >>> obi_wan = annihilator(-20)
    >>> obi_wan()
    510 duckies left
    >>> darth_vader()
    500 duckies left
    """
    def duckie_annihilator(rate):
        def duckie():
            nonlocal n
            n = n - rate
            print(n, 'duckies left')
        return duckie
    return duckie_annihilator
