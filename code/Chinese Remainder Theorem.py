def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def printIfVerbose(verbose, msg):
    if verbose:
        print(msg)

class CRT:
    def __init__(self, mods, verbose = True):
        self.mods = mods
        self.verbose = verbose

    # Search by Sieveing Algorithm
    def SBS(self):
        # Ordering the equations from the largest divisor
        self.mods.sort(key=lambda x:x[1], reverse=True)
        x = 0
        printIfVerbose(self.verbose,
                       "Ordering the equations from the largest divisor:")
        for eq in self.mods:
            printIfVerbose(self.verbose, "X = {} mod {}".format(eq[0],eq[1]))
        # Perform the search by sieving method
        for i in range(len(self.mods)):
            if (x == 0):
                x = self.mods[i][0]
                lcm = self.mods[i][1]
                #printIfVerbose(self.verbose,
                #               "solving: X = {} mod {} <=> X = {} + {} x t\n          X = {} mod {}\n".format(
                #                   self.mods[i][0], lcm, self.mods[i][0], lcm, self.mods[i+1][0], self.mods[i+1][1]))
                continue
            printIfVerbose(self.verbose,
                           "\nsolving: X = {} mod {} <=> X = {} + {} x t\n         X = {} mod {}".format(
                               x, lcm, self.mods[i-1][0], lcm, self.mods[i][0], self.mods[i][1]))
            # if not equal to the equation, add x by the lcm of previous divisor
            printIfVerbose(self.verbose, "trying t from 0 to {}".format(self.mods[i][1]-1))
            t = 0
            while x % self.mods[i][1] != self.mods[i][0]:
                printIfVerbose(self.verbose, "t={} -> X={} (not satisfied, since {} mod {} != {})".format(t, x, x, self.mods[i][1], self.mods[i][0]))
                x += lcm
                t += 1
            printIfVerbose(self.verbose, "t={} -> X={} (satisfied, since {} mod {} = {})".format(t, x, x, self.mods[i][1], self.mods[i][0]))
            lcm = lcm*self.mods[i][1]/gcd(lcm,self.mods[i][1])
            printIfVerbose(self.verbose, "Equations reduced to: X = {} mod {}".format(x, lcm))
        printIfVerbose(self.verbose, "X = {} + {} x t".format(x, lcm))
        return x
            

    # Ibn Tahir 
    def IbnTahir(self):
        x = 0

        for i in range(len(self.mods)):
            if i==0:
                eq = "X = a{} x r{}".format(i, i)
                continue
            eq += " + a{} x r{}".format(i, i)
        eq += " + k x gcd\n"
        printIfVerbose(self.verbose, "{}".format(eq))
        
        # computing LCM of the divisors
        for i in self.mods:
            if (i == self.mods[0]):
                lcm = i[1]
                m = i[1]
                continue
            m = m*i[1]
            
            # if there exist pair of non relatively prime divisors, then it cannot
            # be solve using IbnTahir's Method
            if gcd(lcm,i[1]) != 1:
                printIfVerbose(self.verbose,
                               "Cannot use Ibn Tahir's Method because there exist non-relative prime integers among the divisor")
                return None
            lcm = lcm*i[1]
        cis = []
        for i in range(len(self.mods)):
            incr = m/self.mods[i][1]
            ci = incr
            printIfVerbose(self.verbose, "Finding a{}: multiple of {} and have value of 1 mod {}".format(i, incr, self.mods[i][1]))
            while ci % self.mods[i][1] != 1:
                printIfVerbose(self.verbose, "a{} = {} not satisfied because {} mod {} != 1".format(i, ci, ci, self.mods[i][0]))
                ci += incr
            printIfVerbose(self.verbose, "a{} = {} satisfied, because {} mod {} = 1\n".format(i, ci, ci, self.mods[i][0]))
            cis.append(ci)
            x += ci*self.mods[i][0]
        x = x % lcm
        for i in range(len(cis)):
            if i==0:
                eq = "{} x r{}".format(cis[i], i)
                continue
            eq += " + {} x r{}".format(cis[i], i)
        eq += " + k x {}".format(lcm)
        printIfVerbose(self.verbose, "The general solution is {}".format(eq))
        return x
            
        
            
