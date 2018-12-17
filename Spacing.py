# Generate proof documents for checking spacing

import time
from drawBot import *

point_sizes = [16, 12, 10, 8, 6]
basic_set = """nnnnnnnnnnnnnnnnnnnnn
nunununununununununun
niuiniuiniuiniuiniuin
bqbqbqbqbqbqbqbqbqbqbq
bdpqbdpqbdpqbdpqbdpqbdpq
niupdniubqniupdniubqniupdniubqniu
uinpduinbquinpduinbquinpduinbquin
uonipodiuoniboqiuonipodiuoniboqi
nouiqobinouiqobinouiqobinouiqobi
nanbncndnenfngnhninjnknlnmnnnonpnqnrnsntnunvnwnxnynzn
oaobocodoeofogohoiojokolomonooopoqorosotouovowoxoyozo
niuaniubniucniudniueniufniugniuhniuiniujniukniulniumniu
niunniuoniupniuqniurniusniutniuuniuvniuwniuxniuyniuzniu

HHHHHHHHHHHHHHHHHHHHH
HIHIHIHIHIHIHIHIHIHIH
HOHOHOHOHOHOHOHOHOHOH
OOOOOOOOOOOOOOOOOOOOO
HAHBHCHDHEHFHGHHHIHJHKHLHMHNHOHPHQHRHSHTHUHVHWHXHYHZH
OAOBOCODOEOFOGOHOIOJOKOLOMONOOOPOQOROSOTOUOVOWOXOYOZO
HIHAHIHBHIHCHIHDHIHEHIHFHIHGHIHHHIHIHIHJHIHKHIHLHIHMHIH
HIHNHIHOHIHPHIHQHIHRHIHSHIHTHIHUHIHVHIHWHIHXHIHYHIHZHIH"""

proc_set = ['nn', 'oo']
proc_upr = ['HH', 'OO']
totalPages = len(point_sizes)
proc_str = ""

f = CurrentFont()
fontName = ('%s-%s' % (f.info.familyName, f.info.styleName)).replace(' ', '')

if fontName in installedFonts():
    font(fontName)
else:
    print(str(fontName) + " is not installed.")

if f is None:
    print("No font open.")


##################################################


newDrawing()
newPage('A4Landscape')
margins = 30
footer = 90
rendertime = time.strftime('%y%m%d at %H%M', time.localtime())
rendertimeShort = time.strftime('%y%m%d_%H%M', time.localtime())

def GridBox(boxType):
    if boxType is 'full':
        return(margins, footer, width() - margins * 2, height() - margins - footer)

    elif boxType is 'half':
        return(margins, footer, width() / 2 - margins * 2, height() - margins - footer)
        
    elif boxType is 'footer':
        return(margins, margins / 2, width() - margins * 2, 30)
        
    else:
        print("Grid box type " + str(boxType) + " is not recognised.")
        return None

newDrawing()
        
        
##################################################


for pointsize in point_sizes:
    newPage('A4Landscape')

    pageInfoStr = str(fontName) + " — Spacing Test, Page " + str(pageCount()) + ". Rendered on " + rendertime
    pageInfo = FormattedString(pageInfoStr, fontSize = 8, lineHeight = 10, fill = (0.5))
    textBox(pageInfo, GridBox('footer'))

    spacingText = FormattedString(basic_set, font = fontName, fontSize = pointsize, lineHeight = pointsize * 1.25, fill = (0))
    textBox(spacingText, GridBox('full'))


all_chars = []
    
for i, glyphName in enumerate(f.glyphOrder):
    g = f[glyphName]
    if g.unicode is not None:
        c = chr(g.unicode)
        all_chars.append(c)

for i in range(len(proc_set)):
    for char in all_chars:
        if char.isupper():
            proc_str += proc_upr[i] + char + proc_upr[i]
        else:
            proc_str += proc_set[i] + char + proc_set[i]

while len(proc_str):
    newPage('A4Landscape')
    pageInfoStr = str(fontName) + " — Spacing Test, Page " + str(pageCount()) + ". Rendered on " + rendertime
    pageInfo = FormattedString(pageInfoStr, fontSize = 8, lineHeight = 10, fill = (0.5))
    textBox(pageInfo, GridBox('footer'))

    font(fontName, 12)
    proc_str = textBox(proc_str, GridBox('half'))

saveImage("Proofs/spacing-" + rendertimeShort + ".pdf")
