class Iunit:

    def __init__(self, v, u):
        self.v = v
        self.u = u
        self.n = self.norm_unit()

    def norm_unit(self):
        '''
        returns feet
        '''
        if self.u == 'inch':
            self.v = self.v / 12
        if self.u == 'feet':
            return self.v
        if self.u == 'yard':
            self.v = self.v * 3
        if self.u == 'mile':
            self.v = self.v * 528

        return self.v

    def to_inches(self):
        print(self.n*12)

    def to_feet(self):
        print(self.n)

    def to_yards(self):
        print( self.n  / 3)

    def to_miles(self):
        print(self.n / 5280)

    def to_nmiles(self):
        print( self.n / 6076.1)

    def to_cable(self):
        print (self.n /607.61)

    def to_fathom(self):
        print(self.n / 6.0761)



inch = Iunit(100, 'yard')
inch.to_miles()
