import math
class claseFraccion():
    __op=str
    def __init__(self,v1):
        self.__op=v1
    def simplificar(self,v1):
        dos=True
        tres=True
        porDenominador=True
        param1=math.modf((v1[0])/v1[1])
        if (param1[0]==0):
            param2=math.modf((v1[0])/v1[1])
            if (param2[0]==0):
                v1[0]=int(v1[0]/v1[1])
                v1[1]=int(v1[1]/v1[1])
                porDenominador=True
            else:
                porDenominador=False
        else:
            porDenominador=False
        if (porDenominador==False):
            while(dos==True or tres==True):
                if (v1[1]!=1):
                    
                    param1=math.modf((v1[0])/2)
                    if (param1[0]==0):
                        param2=math.modf((v1[1])/2)
                        if (param2[0]==0):
                            v1[0]=int(v1[0]/2)
                            v1[1]=int(v1[1]/2)
                            dos=True
                        else:
                            dos=False
                    else:
                        dos=False
                    param1=math.modf((v1[0])/3)
                    if (param1[0]==0):
                        param2=math.modf((v1[1])/3)
                        if (param2[0]==0):
                            v1[0]=int(v1[0]/3)
                            v1[1]=int(v1[1]/3)
                            tres=True
                        else:
                                tres=False
                    else:
                        tres=False
                else:
                    dos=False
                    tres=False
            
    def __add__(self,other):
        import re
        other.__op=other.__op.split("/")
        self.__op=self.__op.split("/")
        other.__op[0]=int(other.__op[0])
        other.__op[1]=int(other.__op[1])
        self.__op[0]=int(self.__op[0])
        self.__op[1]=int(self.__op[1])

        if (other.__op[1]==self.__op[1]):
            self.__op[0]+=other.__op[0]
        else:
            y=self.__op[1]*other.__op[1]
            self.__op[0]=self.__op[0]*other.__op[1]+self.__op[1]*other.__op[0]
            self.__op[1]=y
        self.simplificar(self.__op)
        self.__op[0]=str(self.__op[0])
        self.__op[1]=str(self.__op[1])
        x="/".join(self.__op)
        return(x)

    def __sub__(self, other):
        import re
        other.__op=other.__op.split("/")
        self.__op=self.__op.split("/")
        other.__op[0]=int(other.__op[0])
        other.__op[1]=int(other.__op[1])
        self.__op[0]=int(self.__op[0])
        self.__op[1]=int(self.__op[1])
        if (other.__op[1]==self.__op[1]):
            self.__op[0]-=other.__op[0]
        else:
            y=self.__op[1]*other.__op[1]
            self.__op[0]=self.__op[0]*other.__op[1]-self.__op[1]*other.__op[0]
            self.__op[1]=y
        self.simplificar(self.__op)
        self.__op[0]=str(self.__op[0])
        self.__op[1]=str(self.__op[1])
        x="/".join(self.__op)
        return(x)
    def __mul__(self, other):
        import re
        other.__op=other.__op.split("/")
        self.__op=self.__op.split("/")
        other.__op[0]=int(other.__op[0])
        other.__op[1]=int(other.__op[1])
        self.__op[0]=int(self.__op[0])
        self.__op[1]=int(self.__op[1])
        self.__op[0]*=other.__op[0]
        self.__op[1]*=other.__op[1]
        self.simplificar(self.__op)
        self.__op[0]=str(self.__op[0])
        self.__op[1]=str(self.__op[1])
        x="/".join(self.__op)
        return(x)


    def __truediv__(self, other):
        import re
        other.__op=other.__op.split("/")
        self.__op=self.__op.split("/")
        other.__op[0]=int(other.__op[0])
        other.__op[1]=int(other.__op[1])
        self.__op[0]=int(self.__op[0])
        self.__op[1]=int(self.__op[1])
        self.__op[0]*=other.__op[1]
        self.__op[1]*=other.__op[0]
        self.simplificar(self.__op)
        self.__op[0]=str(self.__op[0])
        self.__op[1]=str(self.__op[1])
        x="/".join(self.__op)
        return(x)