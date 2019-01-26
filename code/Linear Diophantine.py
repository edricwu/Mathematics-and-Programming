def printIfVerbose(verbose, msg):
    if verbose:
        print(msg)

class LinearDiophantine:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.GCD = 0
        self.verbose = True

    def findGCD(self):
        # Euclidean Algorithm for finding Greatest Common Divisor of a and b
        
        printIfVerbose(self.verbose,"running findGCD() ...")
        a = self.a
        b = self.b
        r = -1
        printIfVerbose(self.verbose,"GCD({},{})".format(a,b))
        while r!=0:
            r = a % b
            printIfVerbose(self.verbose,"= GCD({},{}) => {} - {}.{} = {}".format(a,b,a,a//b,b,r))
            a = b
            b = r
        printIfVerbose(self.verbose,"= {}".format(a))
        self.GCD = a
        printIfVerbose(self.verbose,"findGCD() done!")

    def isSolvable(self):
        # Bezout's Identity, equation has integer solution only if c is multiple
        # of gcd(a,b) => c = k.gcd(a,b) for positive integer k
        
        printIfVerbose(self.verbose,"running isSolvable() ...")
        if self.GCD == 0:
            self.findGCD()
        if self.c % self.GCD != 0:
            printIfVerbose(self.verbose,"False, since {} is not divisible by GCD({},{})={}".format(
                self.c, self.a, self.b, self.GCD))
            printIfVerbose(self.verbose,"isSolvable() done!")
            return False
        else:
            printIfVerbose(self.verbose,
                           "{} is divisible by {}, hence it is solveable.".format(
                               self.c, self.d))
            printIfVerbose(self.verbose,"True")
            printIfVerbose(self.verbose,"isSolvable() done!")
            return True

    def solve(self):
        # Using Euclidean Algorithm
        
        printIfVerbose(self.verbose,"running solve() ...")
        var = []
        const = []
        a = self.a
        b = self.b
        r = -1
        printIfVerbose(self.verbose,"GCD({},{})".format(a,b))
        while r!=0:
            r = a % b
            var.append(a)
            const.append(-(a//b))
            printIfVerbose(self.verbose,"{} - {}.{} = {}".format(a,a//b,b,r))
            a = b
            b = r
        printIfVerbose(self.verbose,"GCD = {}".format(a))
        self.GCD = a
        if self.c % self.GCD != 0:
            printIfVerbose(self.verbose,"No solution, since {} is not divisible by GCD({},{})={}".format(
                self.c, self.a, self.b, self.GCD))
            return None
        else:
            printIfVerbose(self.verbose,
                           "Since {} is divisible by GCD({},{})={}, hence there exist integer solution".format(
                               self.c, self.a, self.b, self.GCD)) 
        printIfVerbose(self.verbose, "Reversing ...\n")
        var = var[::-1]
        const.pop()
        const = const[::-1]
        y = 1
        x = 0
        n = len(const)
        for i in range(n):
            x,y = y,y*const[i] + x
            if i != n-1:
                printIfVerbose(self.verbose,
                               "{}.{} + {}.{} = {} <=> {}.{} + {}.({} - {}.{}) = {}".format(
                                   x, var[i+1], y, var[i], self.GCD, x, var[i+1], y, var[i+2], -const[i+1], var[i+1], self.GCD))
            else:
                printIfVerbose(self.verbose,"\n")
        x = x*self.c/self.GCD
        y = y*self.c/self.GCD
        printIfVerbose(self.verbose, "X = {} + {} x t, Y = {} - {} x t".format(x, self.b/self.GCD, y, self.a/self.GCD))
        return x, y
        
        
