import colorsys

boolStr = {
    True: "true",
    False: "false"
}

def boolToString(v: bool): # To fix the dumb python syntax
    return boolStr[v]

def rgbToDecimal( r:int, g:int, b:int ):
    return round(r/255), round(g/255), round(b/255)

def svNumFix(n: float):
    return int(round(n*254, 0))

def hueNumFix(n: float):
    return int(round(n*65535))

def rgbToHsv( r:int, g:int, b:int ):
    R, G, B = rgbToDecimal(r, g, b)
    H, S, V = colorsys.rgb_to_hsv(R, G, B)
    return hueNumFix(H), svNumFix(S), svNumFix(V)
