class Organism:
    """
    Organism contains a variety of genes which work together and mutate to form offsprings.
    """
    def __init__(self,size,num):
        self.size = size  #Initaialises size
        # Creates a list by calling the class Gene(size) n times
        self.genes = [Gene(size) for i in range(num)]

    def mutate(self):

   """
   To optimise the process, we divide mutate()
   If the number of genes is less than 250, then each gene is mutated
   Otherwise a random sample of genes is chosen from gene list and is then mutated
   """

        if len(self.genes) < 250:
            for g in self.genes:

                if MUTATION_CHANCE < random.random(): # random.random() gives float in [0,1)
                    g.mutate()

        else:
            k = MUTATION_CHANCE*int(len(self.genes))
            for g in random.sample(self.genes,k):
                g.mutate()

        #To add random gene
        if ADD_GENE_CHANCE < random.random():
            self.genes.append(Gene(self.size)) #Call to Gene to add to genes list

        #To randomly remove genes

        if REM_GENE_CHANCE < random.random() and len(self.genes)>0:
          self.genes.remove(random.choice(self.genes))

    def drawImage(self):
    """
    Draws image using genes
    """

        image = Image.new("RGB",self.size,(255,255,255)) #new() passes parameters mode,size,color
        #255,255,255 is white

        canvas = ImageDraw.Draw(image)
        for g in self.genes:
            color = (g.color.r,g.color.g,g.color.b)

            canvas.ellipse((g.pos.x-int(g.diameter/2),g.pos.y-int(g.diameter/2), g.pos.x+int(g.diameter/2), g.pos.y+int(g.diameter/2)), fill = color)
        return image

def fitness(im1,im2):

    """
    Fitness function calculates the difference between pixels of target image and current image and sums it.
    We are trying to minimize this function
    """

    arr1 = np.array(im1,np.int16) # Creates array of image to easily calculate the difference between pixels.
    arr2 = np.array(im2,np.int16) #np.int16 is used to change the dtype


    dif = np.sum(np.abs(arr1-arr2))

    return (dif/255 * 100)/arr1.size
