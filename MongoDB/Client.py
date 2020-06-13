class Client(object):

    def __init__(self, RFC, name, direction):
        self.RFC = RFC
        self.name = name
        self.direction = direction


    def __repr__(self):
        return "\n RFC del Cliente: %s \n Nombre: %s \n Dirección: %s \n" % (self.RFC, self.name, self.direction)


<<<<<<< HEAD
# init commit
=======
# primer commit
>>>>>>> 2ac8aa69ab4da3d2baf31e5613712c0c593db89c
