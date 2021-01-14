class asteroid:
    #Initializing
    def __init__(self, size, pos, vel):
        self.size = size
        self.pos = pos
        self.vel = vel
        
    def get_size(self):
        return self.size
    def get_pos(self):
        return self.pos
    def get_vel(self):
        return self.vel

    def set_pos(self, p):
        self.pos = p
    def set_vel(self, v):
        self.vel = v
    def set_size(self,s):
        self.size = s

class missile:
    #Initializing
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        
    def get_pos(self):
        return self.pos
    def get_vel(self):
        return self.vel

    def set_pos(self, p):
        self.pos = p
    def set_vel(self, v):
        self.vel = v

class bomb:
    #Initializing
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        
    def get_pos(self):
        return self.pos
    def get_vel(self):
        return self.vel

    def set_pos(self, p):
        self.pos = p
    def set_vel(self, v):
        self.vel = v
