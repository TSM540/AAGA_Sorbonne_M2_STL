# ça ne marche pas, et pas envie de le faire marcher
# PR si vous avez la patience :) 

def knuth_random_generator(X):
    trace = []
    
    Y = X // 10**9  # Step 1
    trace.append((1, X, Y))

    for _ in range(Y + 1):  # Repeat steps based on Y+1
        Z = (X // 10**8) % 10  # Step 2
        trace.append((2, X, Y))

        step = 3 + Z  # Jump to step (3 + Z)
        if step == 3:  # Step 3
            if X < 5 * 10**9:
                X = X + 5 * 10**9
            trace.append((3, X, Y))

        elif step == 4:  # Step 4
            X = (X**2 // 10**5) % 10**10
            trace.append((4, X, Y))

        elif step == 5:  # Step 5
            X = (1001001001 * X) % 10**10
            trace.append((5, X, Y))

        elif step == 6:  # Step 6
            if X < 10**8:
                X = X + 9814055677
            else:
                X = 10**10 - X
            trace.append((6, X, Y))

        elif step == 7:  # Step 7
            X = 10**5 * (X % 10**5) + (X // 10**5)
            trace.append((7, X, Y))

        elif step == 8:  # Step 8
            X = (1001001001 * X) % 10**10
            trace.append((8, X, Y))

        elif step == 9:  # Step 9
            X = int(''.join(str(int(digit) - 1 if int(digit) > 0 else 0) for digit in str(X)))
            trace.append((9, X, Y))

        elif step == 10:  # Step 10
            if X < 10**5:
                X = X**2 + 99999
            else:
                X = X - 99999
            trace.append((10, X, Y))

        elif step == 11:  # Step 11
            while X < 10**9:
                X = 10 * X
            trace.append((11, X, Y))

        elif step == 12:  # Step 12
            X = (X * (X - 1) // 10**5) % 10**10
            trace.append((12, X, Y))

        # Step 13 - check if we decrement Y and loop back
        if Y > 0:
            Y = Y - 1
            trace.append((13, X, Y))
        else:
            break  # End of algorithm

    return trace


# Test the algorithm with X = 6065038420 and print trace
X = 6065038420
trace_output = knuth_random_generator(X)
for step, X, Y in trace_output:
    print(f"Step {step}: X = {X}, Y = {Y}")
# print(trace_output)