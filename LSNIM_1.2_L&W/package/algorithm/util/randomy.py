#coding=utf-8
#import random as rm

def random_pick(seq,probabilities,x):
        #import random
        #print(rm.random())
	#x = rm.uniform(0,1)
        cumulative_probability = 0.0
        for item, item_probability in zip(seq, probabilities): # !!! must in increamental order !!!
                cumulative_probability += item_probability
                if x < cumulative_probability: 
                        break
        return item

def random_picks(seq,relative_odds):
        table=[z for x,y in zip(seq,relative_odds) for z in [x]*y]
        while True:
                yield random.choice(table)

def weighted_choice_sub(weights):
        rnd=random.random()*sum(weights)
        for i,w in enumerate(weights):
                rnd-=w
                if rnd<0:
                        return i
                        
                        
def random_p(p,x):
        if x<p:
                return 1
        else:
                return 0
        