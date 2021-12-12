from Scripts.Doom.estaticos.salas import SALAS
from py_stealth.methods import GetX, GetY, Self

def get_my_room():
    myx = GetX(Self())
    myy = GetY(Self())
    for sala in SALAS.keys():
        for quadrado in SALAS[sala]:
            if ((myx >= quadrado['xi']) and (myx <= quadrado['xf'])) and ((myy >= quadrado['yi']) and (myy <= quadrado['yf'])):
                return sala

