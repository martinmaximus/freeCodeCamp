import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
            #print(self.contents)
    
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        else:
            drawn_balls = list()
            for i in range(num_balls):
                random_ball = random.choice(self.contents)
                drawn_balls.append(random_ball)
                self.contents.remove(random_ball)
            #print(len(self.contents))    
            return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for experiment in range(num_experiments):
        expected_balls_list = list()
        for key, value in expected_balls.items():
            for i in range(value):
                expected_balls_list.append(key)
            #print(expected_balls_list)
    
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        for color in drawn_balls:
            if color in expected_balls_list:
                expected_balls_list.remove(color)
        if len(expected_balls_list) == 0:
            count += 1
        
    prob = count/num_experiments
    
    return prob






hat = Hat(black=6,red=4,green=3)
probability = experiment(hat=hat, expected_balls={"red":2,"green":1}, num_balls_drawn=4, num_experiments=2000)

print(probability, hat.contents)