#challenges for sharing on social media

def challenge_1():
    # follow me for more challenges
    # www.linkedin.com/in/datajulian
    solution = 'love this challenges ♥ !'
    for i in range(2,1000,2):
        # for cycle doesnt have a break statement so will execute else block at the end
        if i%2==1:
            if i<500:
                solution = 'crazy!'
            else:
                solution = 'sure!'
    else:
        solution = 'unexpected!' # final solution will be this one
    return solution

