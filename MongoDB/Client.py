class Client(object):

    def __init__(self, RFC, name, direction):
        self.RFC = RFC
        self.name = name
        self.direction = direction


    def __repr__(self):
        return "\n RFC del Cliente: %s \n Nombre: %s \n Dirección: %s \n" % (self.RFC, self.name, self.direction)



# primer commit

