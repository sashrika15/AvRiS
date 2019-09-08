import os
from copy import deepcopy
import random
import multiprocessing
import numpy as np
from PIL import Image,ImageDraw
from IPython.display import display


class Gene:
    def __init__(self,size):
        self.size = size #Points to the *INSTANCE* value of size which is equal to or points to the same value as size
        self.diameter = random.randint(5,15) #Randomly sets the diameter between 5,15 <educated guess>
        self.pos = Point(random.randint(0,size[0]),random.randint(0,size[1]))
        """ 
        Now the pos instance variable points to the object 
        of Random class which is being passed with these parameters.
        """
        self.color = Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)) #same as above but for Color class
        self.params = ["diameter","pos","color"] 
        """
        params holds "diameter" as a string because 
        when we mutate we, need to choose which attribute to mutate 
        not which value, hence this is just a list to hold what params we have
        """

    def mutate(self):
        """
        np.random.normal uses gaussian distribution, it is the closest to true random and much easier to use against a
        normal random.randint function. Basically it is easier to plot.
        Explanation for Params: np.random.normal(mean,std_dev, size). Size in our case is a one dimensional array 
        which stores the random values that the np.random.normal() function will return. We can call it "number of circles" in our case. 
        Other values of size can be np.random.normal(mean,std, size(3,3)). This will return random values and store them in a 3,3 matrix.
        """
        mutation_size = max(1,int(round(random.gauss(15,4))))/100
        """
        Changed the mutation by using random.randint rather than the gaussian one 
        after observing that the gaussian random never really gave an output of more than 0.25
        """

        #Decide what will be mutated, just randomly picking onr of the three params
        mutation_type = random.choice(self.params)

        #Mutate the thing
        if mutation_type == "diameter":
            """
            Over here, what we are providing a range between self.diameter*x where x=1-mutation size and self.diameter*y where =1+mutation size
            Basically we add or subtract from 1 because the mutation has to be small
            """
            self.diameter = max(1,random.randint(int(self.diameter*(1-mutation_size)),int(self.diameter*(1+mutation_size))))
            return self.diameter
            #same thing here
        elif mutation_type == "pos":
            x = max(0,random.randint(int(self.pos.x*(1-mutation_size)),int(self.pos.x*(1+mutation_size))))
            y = max(0,random.randint(int(self.pos.y*(1-mutation_size)),int(self.pos.y*(1+mutation_size))))
            self.pos = Point(min(x,self.size[0]),min(y,self.size[1]))
            return self.pos
        elif mutation_type == "color":
            r = min(max(0,random.randint(int(self.color.r*(1-mutation_size)),int(self.color.r*(1+mutation_size)))),255)
            g = min(max(0,random.randint(int(self.color.g*(1-mutation_size)),int(self.color.g*(1+mutation_size)))),255)
            b = min(max(0,random.randint(int(self.color.b*(1-mutation_size)),int(self.color.b*(1+mutation_size)))),255)
            self.color = Color(r,g,b)
            return self.color

