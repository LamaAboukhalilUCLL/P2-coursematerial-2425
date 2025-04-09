class LengthConverter():
    def __init__(self,meter=0, inch=0, feet=0) :
        self._meter = self 
        self._inch = self
        self._feet = self

    @property 
    def meter (self):
        return self._meter
    @meter.setter
    def meter (self, value):
        self._meter = value
        self._inch= 39.37* value
        self._feet  = 3.28 *value

    @property
    def inch(self):
        return self._inch
    @inch.setter
    def inch (self, value):
        self._inch = value
        self._meter = value * 0.0254
        self._feet = value * 0.0833333

    @property
    def feet (self):
        return self._feet
    @feet.setter 
    def feet (self, value):
        self._feet = value
        self._meter = value * 0.3048     #we are updating the value and storing it for thje next object call
        self._inch = value * 12

        