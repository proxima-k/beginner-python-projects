# https://github.com/jorgegonzalez/beginner-projects#chickens-and-rabbits

def solve(numheads,numlegs):
    solution = "No solution"
    for i in range(numheads+1):
        j=numheads-i
        if (2*i) + (4*j) == numlegs:
            solution = i,j

    return solution

nheads = 35
nlegs = 94

solution = solve(nheads,nlegs)

print(solution)
