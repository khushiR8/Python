class rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height
        
    @property 
    def width(self):
        return self._width
        
    @width.setter
    def width(self,value):
        self._width=value
            
    @property 
    def height(self):
       return self._height
        
    @height.setter
    def height(self,value):
     self._height=value    
        
    @property
    def area(self):
        return self._width * self._height
       
def main():
    rect=rectangle(4,5)
    print('Width:',rect.width)
    print('Height:',rect.height)
    print('Area:',rect.area)
    
    rect.width=6               #updates width
    rect.height=7              #updates height
    
    print('Updated Width:',rect.width)
    print('Updated Height:',rect.height)
    print('Updated Area:',rect.area)
    
main()         
            