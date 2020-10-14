#challenges for sharing on social media

def challenge_1():
    # follow me for more challenges
    # www.linkedin.com/in/datajulian
    solution = 'love this challenge ♥ !'
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

data =  {   'challenge':'Python_101',
            'responsible': 'Joe the business man',
            'values':[
            {'name':'Anita' ,'scores':{'1st':40,'2nd':50,'final':90}},
            {'name':'Alvaro','scores':{'1st':35,'2nd':39,'final':74}},
            {'name':'Yeison','scores':{'1st':25,'2nd':20,'final':45}},
            {'name':'Julian','scores':{'1st':11,'2nd':17,'final':28}}]}

data['values'][1]['scores']['final']
data['values']['Alvaro']['scores']['final']
data['values']['name']['Alvaro']['scores']['final']
data['Python_101']['values']['name']['Alvaro']['scores'][2]
data['Python_101']['values'][2]['scores']['final'][1]

def challenge_2(data):
    # return alvaro's final score
    alvaro_final_score =  # can you finish the code for me IOU1. - Joe
    return alvaro_final_score


def challenge_3():
    a,b,c=1,2,3
    secret  = a + b + c
    try:
        a = 'I '; b = '♥ '; c = 'Python.'
        secret = a + b + c
    except:
        secret += 4
    else:
        return secret
    return secret * 2
