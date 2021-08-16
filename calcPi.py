import time

# pi can be calculated by the infinite series
# 1/1 - 1/3 + 1/5 - 1/7 + ...


def calcPi():
    denom = 1
    pi = 0
    odd = True

    while True:
        # add the odd terms
        if odd:
            pi += (1/denom)
        # subtract the even terms
        else:
            pi -= (1/denom)

        # display output
        time.sleep(0.1)
        print(pi*4)

        # increment denominator
        denom += 2

        # change parity of odd
        odd = not odd


# run the program, unless function is imported
if __name__ == "__main__":
    calcPi()
