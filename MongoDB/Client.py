class Client(object):

    def __init__(self, RFC, name, direction, name_com):
        self.RFC = RFC
        self.name = name
        self.direction = direction
        self.name_com = name_com


    def __repr__(self):
        return "\n RFC del Cliente: %s \n Nombre: %s \n Dirección: %s \n Empresa Asociada: %s " % (self.RFC, self.name, self.direction, self.name_com)



# primer commit

