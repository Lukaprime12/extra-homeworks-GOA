class rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

class square:

    def __init__(self, length, width):
        super().__init__(length,width)

    def are(self):
        return self.length*self.width
    
class cube(rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    
    def are(self):
        return self.length*self.width