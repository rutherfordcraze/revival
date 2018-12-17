# Generate proofs for the Weiß revival.
# Super rough. Will be updated further.

import time
from drawBot import *

f = CurrentFont()
#f.testInstall()
fontName = ('%s-%s' % (f.info.familyName, f.info.styleName)).replace(' ', '')

margins = 30
footer = 90
totalPages = 5

if fontName in installedFonts():
    font(fontName)
else:
    print(str(fontName) + " is not installed.")
    exit()

if f is None:
    print("No font open.")
    exit()
    
newDrawing() # because why shouldn't RF drawbot and standalone drawbot have totally different stack behaviours?
newPage('A4Landscape')
boxQuarterW = width() / 2 - margins * 1.5
boxQuarterH = height() / 2 - margins - footer / 2
boxThirdW = width() / 3 - margins * 1.5
boxThirdH = height() - margins - footer
boxDecameronW = 204
boxDecameronH = boxThirdH
rendertime = time.strftime('%y%m%d at %H%M', time.localtime())
rendertimeShort = time.strftime('%y%m%d_%H%M', time.localtime())


##################################################


def GridBox(boxType):
    if boxType is 't1':
        return(margins, footer, boxThirdW, boxThirdH)
    elif boxType is 't2':
        return(margins * 2 + boxThirdW, footer, boxThirdW, boxThirdH)
    elif boxType is 't3':
        return(margins * 3 + boxThirdW * 2, footer, boxThirdW, boxThirdH)
        
    elif boxType is 'q1':
        return(margins, footer + margins + boxQuarterH, boxQuarterW, boxQuarterH)
    elif boxType is 'q2':
        return(margins, footer, boxQuarterW, boxQuarterH)
    elif boxType is 'q3':
        return(margins * 2 + boxQuarterW, footer + margins + boxQuarterH, boxQuarterW, boxQuarterH)
    elif boxType is 'q4':
        return(margins * 2 + boxQuarterW, footer, boxQuarterW, boxQuarterH)
    elif boxType is 'q2b':
        return(margins, footer, boxQuarterW * 0.66, boxQuarterH)
    elif boxType is 'q4b':
        return(margins * 2 + boxQuarterW, footer, boxQuarterW / 2, boxQuarterH)
        
    elif boxType is 'd1':
        return(margins, footer, boxDecameronW, boxDecameronH)
    elif boxType is 'd2':
        return(margins * 2 + boxDecameronW, footer, boxDecameronW, boxDecameronH)
        
    elif boxType is 'footer':
        return(margins, margins / 2, width() - margins * 2, 30)
        
    else:
        print("Grid box type " + str(boxType) + " is not recognised.")
        return None
        
        
##################################################


# Page 1 (Comparisons)
def Page1():
    pageInfoStr = "Page 1 of " + str(totalPages) + ": Comparisons. Rendered on " + rendertime
    pageInfo = FormattedString(pageInfoStr, fontSize = 8, lineHeight = 10, fill = (0.5))
    textBox(pageInfo, GridBox('footer'))
    
    comparisonString1 = """und den Zweck erreicht sah, um dessentwillen sie, die Palermitanerin, sich zur Schwester eines Perugi-aners gemacht und ihre Schlingen ausgelegt hatte, bekümmerte sie sich nicht mehr um jenen, sondern schloß eilends die Tür zu, aus welcher er herausge-treten war, als er fiel.\n Andreuccio rief inzwischen, da ihm das Kind nicht antwortete, immer stärker, doch es half ihm nichts. Nun erst fing er an, argwöhnisch zu werden, und begann allzu spät zu erraten,daß er betrogen worden war. Er kletterte über die kleine Mauer, welche das Gäßchen von der Straße trennte, ging an die Haus-tür, die ihm noch wohlbekannt war, klopfte und rüttelte lange daran und rief hinauf, aber alles ver-gebens. Jetzt sah er sein Unglück klar ein, weinte und sagte: „O Himmel, in welcher kurzen Zeit habe ich eine Schwester und fünfhundert Goldgulden ein-gebüßt!” In dieser Weise redete er noch weiter und fing dann wieder an zu klopfen und zu rufen. End-lich machte er solch einen Lärm, daß viele der näch-sten Nachbarn darüber erwachten und aufstanden, als sie es nicht mehr ertragen konnten. Inzwischen           (16)"""
    comparisonString2 = """erwiderte sie dagegen, „habe ich denn niemand in meinem Hause, um sagen zu lassen, daß man nicht auf dich warten soll? Hoflicher aber wäre es gegen mich und im Grunde nur deine Schuldigkeit, wenn  du deinen Gefährten sagen ließest, sie sollten hier- her zum Abendessen kommen. Dann könntet ihr nachher, wenn ihr anders wolltet, in Gesellschaft   nach Hause gehen.” Andreuccio erwiderte, die Ge-fährten möchte er für den Abend nicht. Da sie es   aber einmal so haben wolle, solle sie nach Gefallen über ihn selbst verfügen. Darauf tat sie, als ließe sie im Wirtshaus bestellen, daß man ihn nicht zum       Essen erwarten möchte, und nach mancherlei andern     Gesprächen setzten sie sich zu Tisch, wo sie auf das glänzendste mit zehlreichen Schüsseln bedient      wurden und das Essen durch die List des Mädchens sich bis tief in die Nacht hinein ausdehnte.
Als sie endlich vom Tisch aufgestanden waren und Andreuccio nach Hause gehen wollte, erklärte sie, daß sie das keinesfalls zugeben werde. Neapel sei überhaupt nicht der Ort, am wenigsten für einen Fremden, um in der Nacht darin umherzugehen.           (13)"""

    comparison1 = FormattedString(comparisonString1, font = fontName, fontSize = 9.5, lineHeight = 14.875, fill = (0), tracking = -0.05, align = 'justified')
    comparison2 = FormattedString(comparisonString2, font = fontName, fontSize = 9.5, lineHeight = 14.875, fill = (0), tracking = -0.05, align = 'justified')
    textBox(comparison1, GridBox('d1'))
    textBox(comparison2, GridBox('d2'))
    
    characterSet = ''
    
    for i, glyphName in enumerate(f.glyphOrder):
        g = f[glyphName]
        if g.unicode is not None:
            c = chr(g.unicode)
            characterSet += c + " "
            
    characters = FormattedString(characterSet, font = fontName, fontSize = 32, lineHeight = 40, fill = (0))
    textBox(characters, GridBox('t3'))


##################################################


# Page 2 (Texture)
def Page2():
    newPage('A4Landscape')
    pageInfoStr = "Page 2 of " + str(totalPages) + ": Texture. Rendered on " + rendertime
    pageInfo = FormattedString(pageInfoStr, fontSize = 8, lineHeight = 10, fill = (0.5))
    textBox(pageInfo, GridBox('footer'))
    
    textureStrMaj = "PERCEPTION NUMERIST BARMAIDS COASTMAN EUGREGARINIDA BULTEN TEETHER SUPERIMPOSE IRANIC HARPIST LORICATING SUBDURE CHALAZA UNDILUTE CHALAZE CORRECTIONS DISCOMPOSES GRANDIOSO EMBOUCHMENT SHEARWATERS MOLLISIOSE BANKRIDER CONCERTATION AUNTLIEST SCHLAURAFFENLAND DISCOMPOSED DIAMONDWORK SCISSORS OPTIONALIZE UNSPELLED CALISTHENICAL ELEEMOSINAR ANTIHEMORRHAGIC MUGGISH THICKISH UNSPELLER DEGERMING DURESS CONSENTED PROPIOLATE CENTERED GRUFFINESS UNDERMEASURING CHAGRINING CEREBROVASCULAR CONSENTER ABANGA REACTIVATION SUPERVENING CENTERER TRANSVESTITISM REDISTILLING BETALLOW ABSOLUTISTIC GLUEING BREADTHS FABRICATIONS CARMINATIVES PLECTRIDIUM VISITATIONAL ABDOMINOCENTESIS UNGENERICAL DIADELPHIA DIADELPHIC NONCHEMIST PHLOEMS BUGLOSS SUBSCAPULAR BRASEROS PINPRICKS LUSTERLESSNESS MONADIC CLAVIERISTIC COMMANDING PEPPERCORN IDIOBLASTIC CHUDDER CREMASTERIC SCINCIDOID CENTRODESMOSE NORITE UNPROPORTIONABLENESS SKAINSMATE ROTAMEN CASHMERETTE NONPROTRACTILE SCROFULOSIS ZOOGEOLOGICAL UNTHANKED ENSLAVE COATIMONDIE THRACIAN OUTSPRUING INSPIRITER PSEUDODIVINE CATALIN VERDUGO PRESIGNIFIED CLOPPING INSPIRITED OVERSELL THUNDERSTICK SABRING TAILPIPES HOBBING UNCARVED BOGGLING CAESURA LICKING GALENOBISMUTITE SPIROMETRIC NEBULIZE AFTERCURE TRAGIONS RHIZOCEPHALAN DECIAN SPORADIN MAHMOUD INTERTRANSVERSALIS MILANAISE SPORADIC BIGGIES COFACTOR COMBUSTION KANTELETAR GNARRED INDIFFERENTIAL WHELKED PATERNAL UNFAMOUS RAPHIDES ANOINTING WHELKER UNFREEMAN POSITRON LOKAOSE POSTBOOK TORCEL REDISTURB BUTTONLESS CONIFICATION LOUPING RIGHTWARD COSINUSOID MALARIAL INDURITE OUTSWELL CENTENIER BENTHAMITE MALARIAS IRRENEWABLE LIMEBERRIES PSEUDACONIN RUSSIANIZATION PHERECRATIAN SHASTRAS ASPARAGIC RETHREADS ASPARAGIN HARIFFE PREHNITIC UNTRUSTFUL"
    textureStrMin = "holographs protomanganese resettles fulmines canalize sociol resettled canterburies vapourescent calappa azulite prognoses sonlike caninal revaluating hopelessness michaelmastide cedrela camaldolensian somewheres observing salwin overthwart allows unsanctitude somnivolent oozooid metagelatin soonish dichrooscopic multilirate semiconductors undiagramed lemurlike carucage pecunial likeminded vivianite triacetate archpriest pleurococcus streite unprompted watershake carnous sheetage interagencies calligraphers antinode elbowpiece undreamed saddlestead odontormae harambee ethionic semimechanical berginize tapioca chargeful satellitic talemongering brachiolarian preevolutionist untempered monotheletic tautologized aerobiosis intergossiping subrectangular tautologizer hemileia redemptional electrodesiccate khakis sipapu sweetheartdom inducteous sprekelia semianatropal demitone huspil federalizes waggonsmith misanthropia bosomer misanthropic haematocrit departure disserviceable flatnose spoutlike preperfect grande spermatogenous multivitamin sprenging unprized heptanchus lochetic stereobate microstress osteophone pechili giddies unrecusant cozeier assaulting masora metaphosphorous cashableness unadjacent oversmitten reacclimatize pherephatta spallable predeserving concreted submembranaceous unwirable concreter concretes prodition milestone outmode endopodite woolworth encephalotome uncanonised gummaker manteltree phoroscope metoposcopist antepenuit fabling pseudosacrilegious somacule vulnerose reactivator parthenon applicate blushfulness superjacent theologians undetached legumins protopin podophthalmitic leiotropic idiotized biologic postvenous preimpose comminated antilogarithm ultraoptimistic"
    textureStrMix = "Impress Staroobriadtsi Spectrofluorimeter Rutherfordite Imprese Impresa Searchant Augment Misfits Unmown Antiparliamentarians Disuniters Unplaned Unprecipitate Critize Manhattanize Orchils Reacts Monoculist Homecrofting Thermospheric Bethorned Ellwand Unmortal Unsawn Hatchling Desecrated Preimagine Utriculose Desecrater Desecrates Septentrio Dendron Torrentlike Punnage Chiave Nonconclusiveness Pickableness Foreboard Uncudgelled Uninsular Woaded Raffinose Uniparental Steins Retrogress Flapper Rupiahs Flappet Trabant Preconceivable Flapped Urinates Distraite Rhizoneure Mediocris Linguistics Tumultuate Cosmopolises Balisaurs Septation Promontories Amplifiable Ottavino Accursedness Negligent Waughted Arcuate Potwalling Stearrhea Dewlapped Dipetto Overprompt Picograms Woader Cachibou Murkish Underparticipation Overhollow Matchings Reapologize Oligosideric Radiative Readding Amburbial Geiger Psammogenous Barotraumata Nonperseverant Endothecia Pillmaker Pitprop Unprecedentedness Coalize Tubulosaccular Shochets Ratiocination Theists Induction Botcheries Disorb Spadicose Antelucan Gospelist Fawning Scoinson Shegets Daimonic Beclothed Recalibrating Cainozoic Chlorocresol Beclothes Agrobacterium Jedcock Spannermen Algedonics Tonners Patrilinies Motorphobe Marvelling Molluscoidan Molluscoidal Rondelle Automa Foeless Multigerm Clacker Redknees Clacket Belabored Nubbling Hardish Academe Unimpeding Clacked Grumness Weavable Orleanist Orleanism Reopposition Stipple Unaccountable Stopwater Misjudgement Cannings Unelected Primeros Scurfiness Cribella Tubemaker Oraculate Polarization Nominatival Neuroleptanalgesia Carpogonium Trichomatous Combat Unsteaming Antithalian Leechkin Antitank Acoelous Abmodalities"
    
    textureMaj = FormattedString(textureStrMaj, font = fontName, fontSize = 10, lineHeight = 12, fill = (0))
    textureMin = FormattedString(textureStrMin, font = fontName, fontSize = 10, lineHeight = 12, fill = (0))
    textureMix = FormattedString(textureStrMix, font = fontName, fontSize = 10, lineHeight = 12, fill = (0))
    
    textBox(textureMaj, GridBox('t1'))
    textBox(textureMin, GridBox('t2'))
    textBox(textureMix, GridBox('t3'))


##################################################


# Page 3 (Size 1)
def Page3():
    newPage('A4Landscape')
    pageInfoStr = "Page 3 of " + str(totalPages) + ": Size 1. Rendered on " + rendertime
    pageInfo = FormattedString(pageInfoStr, fontSize = 8, lineHeight = 10, fill = (0.5))
    textBox(pageInfo, GridBox('footer'))

    strUC = "LIKEMINDED VIVIANITE TRIACETATE ARCHPRIEST PLEUROCOCCUS STREITE UNPROMPTED WATERSHAKE CARNOUS SHEETAGE INTERAGENCIES CALLIGRAPHERS ANTINODE ELBOWPIECE UNDREAMED SADDLESTEAD ODONTORMAE HARAMBEE ETHIONIC SEMIMECHANICAL BERGINIZE TAPIOCA CHARGEFUL SATELLITIC TALEMONGERING BRACHIOLARIAN PREEVOLUTIONIST UNTEMPERED MONOTHELETIC TAUTOLOGIZED AEROBIOSIS INTERGOSSIPING SUBRECTANGULAR TAUTOLOGIZER HEMILEIA REDEMPTIONAL ELECTRODESICCATE KHAKIS SIPAPU SWEETHEARTDOM INDUCTEOUS SPREKELIA SEMIANATROPAL"
    strLC = "Belabored nubbling hardish academe unimpeding clacked grumness weavable orleanist orleanism reopposition stipple unaccountable stopwater misjudgement cannings unelected primeros scurfiness cribella tubemaker oraculate polarization nominatival neuroleptanalgesia carpogonium trichomatous combat unsteaming antithalian leechkin antitank acoelous abmodalities"
    
    uc48 = FormattedString(strUC, font = fontName, fontSize = 36, lineHeight = 40, fill = (0))
    lc48 = FormattedString(strLC, font = fontName, fontSize = 36, lineHeight = 40, fill = (0))
    uc24 = FormattedString(strUC, font = fontName, fontSize = 24, lineHeight = 32, fill = (0))
    lc24 = FormattedString(strLC, font = fontName, fontSize = 24, lineHeight = 32, fill = (0))
    
    textBox(uc48, GridBox('q1'))
    textBox(lc48, GridBox('q3'))
    textBox(uc24, GridBox('q2'))
    textBox(lc24, GridBox('q4'))


##################################################


# Page 4 (Size 2)
def Page4():
    newPage('A4Landscape')
    pageInfoStr = "Page 4 of " + str(totalPages) + ": Size 2. Rendered on " + rendertime
    pageInfo = FormattedString(pageInfoStr, fontSize = 8, lineHeight = 10, fill = (0.5))
    textBox(pageInfo, GridBox('footer'))
    
    referenceText = "Erwiderte sie dagegen, „habe ich denn niemand in meinem Hause, um sagen zu lassen, daß man nicht auf dich warten soll? Hoflicher aber wäre es gegen mich und im Grunde nur deine Schuldigkeit, wenn du deinen Gefährten sagen ließest, sie sollten hier- her zum Abendessen kommen. Dann könntet ihr nachher, wenn ihr anders wolltet, in Gesellschaft nach Hause gehen.” Andreuccio erwiderte, die Ge-fährten möchte er für den Abend nicht. Da sie es aber einmal so haben wolle, solle sie nach Gefallen über ihn selbst verfügen. Darauf tat sie, als ließe sie im Wirtshaus bestellen, daß man ihn nicht zum Essen erwarten möchte, und nach mancherlei andern Gesprächen setzten sie sich zu Tisch, wo sie auf das glänzendste mit zehlreichen Schüsseln bedient wurden und das Essen durch die List des Mädchens sich bis tief in die Nacht hinein ausdehnte. Als sie endlich vom Tisch aufgestanden waren und Andreuccio nach Hause gehen wollte, erklärte sie, daß sie das keinesfalls zugeben werde. Neapel sei überhaupt nicht der Ort, am wenigsten für einen Fremden, um in der Nacht darin umherzugehen. Erwiderte sie dagegen, „habe ich denn niemand in meinem Hause, um sagen zu lassen, daß man nicht auf dich warten soll? Hoflicher aber wäre es gegen mich und im Grunde nur deine Schuldigkeit, wenn du deinen Gefährten sagen ließest, sie sollten hier- her zum Abendessen kommen. Dann könntet ihr nachher, wenn ihr anders wolltet, in Gesellschaft nach Hause gehen.” Andreuccio erwiderte, die Ge-fährten möchte er für den Abend nicht. Da sie es aber einmal so haben wolle, solle sie nach Gefallen über ihn selbst verfügen. Darauf tat sie, als ließe sie im Wirtshaus bestellen, daß man ihn nicht zum Essen erwarten möchte, und nach mancherlei andern Gesprächen setzten sie sich zu Tisch, wo sie auf das glänzendste mit zehlreichen Schüsseln bedient wurden und das Essen durch die List des Mädchens sich bis tief in die Nacht hinein ausdehnte. Als sie endlich vom Tisch aufgestanden waren und Andreuccio nach Hause gehen wollte, erklärte sie, daß sie das keinesfalls zugeben werde. Neapel sei überhaupt nicht der Ort, am wenigsten für einen Fremden, um in der Nacht darin umherzugehen."
    
    ref12 = FormattedString("12pt\n" + referenceText, font = fontName, fontSize = 12, lineHeight = 17, fill = (0))
    ref10 = FormattedString("10pt\n" + referenceText, font = fontName, fontSize = 10, lineHeight = 14, fill = (0))
    ref8 = FormattedString("8pt\n" + referenceText, font = fontName, fontSize = 8, lineHeight = 10, fill = (0))
    ref6 = FormattedString("6pt\n" + referenceText, font = fontName, fontSize = 6, lineHeight = 8, tracking = 0.1, fill = (0))
    
    textBox(ref12, GridBox('q1'))
    textBox(ref10, GridBox('q3'))
    textBox(ref8, GridBox('q2b'))
    textBox(ref6, GridBox('q4b'))


##################################################


# Page 5 (Language)
def Page5():
    newPage('A4Landscape')
    pageInfoStr = "Page 5 of " + str(totalPages) + ": EN/DE/NL comparisons. Rendered on " + rendertime
    pageInfo = FormattedString(pageInfoStr, fontSize = 8, lineHeight = 10, fill = (0.5))
    textBox(pageInfo, GridBox('footer'))
    
    referenceEN = "Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System after Mercury. In English, Mars carries a name of the Roman god of war, and is often referred to as the \"Red Planet\" because the reddish iron oxide prevalent on its surface gives it a reddish appearance that is distinctive among the astronomical bodies visible to the naked eye. Mars is a terrestrial planet with a thin atmosphere, having surface features reminiscent both of the impact craters of the Moon and the valleys, deserts, and polar ice caps of Earth. The rotational period and seasonal cycles of Mars are likewise similar to those of Earth, as is the tilt that produces the seasons. Mars is the site of Olympus Mons, the largest volcano and second-highest known mountain in the Solar System, and of Valles Marineris, one of the largest canyons in the Solar System. The smooth Borealis basin in the northern hemisphere covers 40 percent of the planet and may be a giant impact feature. Mars has two moons, Phobos and Deimos, which are small and irregularly shaped. These may be captured asteroids, similar to 5261 Eureka, a Mars trojan. There are ongoing investigations assessing the past habitability potential of Mars, as well as the possibility of extant life. Future astrobiology missions are planned, including the Mars 2020 and ExoMars rovers. Liquid water cannot exist on the surface of Mars due to low atmospheric pressure, which is less than 1 percent of the Earth's, except at the lowest elevations for short periods. The two polar ice caps appear to be made largely of water. The volume of water ice in the south polar ice cap, if melted, would be sufficient to cover the entire planetary surface to a depth of 11 meters (36 ft). In November 2016, NASA reported finding a large amount of underground ice in the Utopia Planitia region of Mars. The volume of water detected has been estimated to be equivalent to the volume of water in Lake Superior. Mars can easily be seen from Earth with the naked eye, as can its reddish coloring. Its apparent magnitude reaches −2.94, which is surpassed only by Jupiter, Venus, the Moon, and the Sun. Optical ground-based telescopes are typically limited to resolving features about 300 kilometers (190 mi) across when Earth and Mars are closest because of Earth's atmosphere."
    referenceDE = "Der Mars ist, von der Sonne aus gezählt, der vierte Planet im Sonnensystem und der äußere Nachbar der Erde. Er zählt zu den erdähnlichen (terrestrischen) Planeten. Sein Durchmesser ist mit knapp 6800 Kilometer etwa halb so groß wie der der Erde, sein Volumen beträgt gut ein Siebtel des Erdvolumens. Damit ist der Mars nach dem Merkur der zweitkleinste Planet des Sonnensystems, hat jedoch eine vielfältige Geologie und die höchsten Vulkane des Sonnensystems. Mit einer durchschnittlichen Entfernung von 228 Millionen Kilometern ist er rund 1,5-mal so weit von der Sonne entfernt wie die Erde. Die Masse des Mars beträgt etwa ein Zehntel der Erdmasse. Die Fallbeschleunigung auf seiner Oberfläche beträgt 3,69 ms2, dies entspricht etwa 38 prozent der irdischen. Mit einer Dichte von 3,9 gcm3 weist der Mars den geringsten Wert der terrestrischen Planeten auf. Deshalb ist die Schwerkraft auf ihm sogar geringfügig niedriger als auf dem kleineren, jedoch dichteren Merkur. Der Mars wird oft auch als der Rote Planet bezeichnet. Diese Färbung geht auf Eisenoxid-Staub (Rost) zurück, der sich auf der Oberfläche und in der dünnen CO2-Atmosphäre verteilt hat. Seine orange- bis blutrote Farbe und seine Helligkeitsschwankungen am irdischen Nachthimmel sind auch der Grund für seine Namensgebung nach dem römischen Kriegsgott Mars. In größeren Fernrohren deutlich sichtbar sind die zwei Polkappen und mehrere dunkle Ebenen, die sich im Frühjahr etwas verfärben. Fotos von Raumsonden zeigen eine teilweise mit Kratern bedeckte Oberfläche und starke Spuren früherer Tektonik (tiefe Canyons und einen über 20 km hohen Vulkan). Marsroboter haben schon mehrere Gebiete geologisch untersucht. Der Mars besitzt zwei kleine, unregelmäßig geformte Monde, die 1877 entdeckt wurden: Phobos und Deimos (griechisch für Furcht und Schrecken)."
    referenceNL = "Mars is vanaf de zon geteld de vierde planeet van ons zonnestelsel, om de zon draaiend in een baan tussen die van de Aarde en die van Jupiter. De planeet is kleiner dan de Aarde en met een (maximale) magnitude van -2,9 minder helder dan Venus en meestal minder helder dan Jupiter. Mars wordt wel de rode planeet genoemd maar is in werkelijkheid eerder okerkleurig. De planeet is vernoemd naar de Romeinse god van de oorlog. Mars is gemakkelijk met het blote oog te bespeuren, vooral in de maanden rond een oppositie. 's Nachts is Mars dan te zien als een heldere roodachtige \"ster\" die evenwel door haar relatieve nabijheid geen puntbron is maar een schijfje. Daarom flonkert Mars niet zoals bv. de verre rode reuzenster Aldebaran. Mars is een terrestrische planeet met een ijle atmosfeer. Het oppervlak is op sommige plekken net zoals dat van de Maan bezaaid met inslagkraters, terwijl op andere plaatsen net zoals op de Aarde, vulkanen, valleien, zandduinen en poolkappen voorkomen. Verder komen ook de rotatieperiode (\"dag\") en de wisselingen van de seizoenen op Mars bij benadering overeen met die van de Aarde. Voor de tijd van de ruimtevaart werd vaak gedacht dat leven en vloeibaar water op Mars voorkwamen. Nadat in 1965 de ruimtesonde Mariner 4 langs Mars vloog, werd aangenomen dat geen van beide het geval kon zijn. In 2003 ontdekte de ESA-sonde Mars Express water in de vorm van waterdamp en ijs op Mars. In 2008 werden door de ruimtesonde Phoenix ijsmonsters rechtstreeks onderzocht. Waarnemingen door de Mars Reconnaissance Orbiter hebben mogelijk stromend water ontdekt tijdens de warmste maanden op Mars. In 2015 maakte NASA bekend dat er bewijs gevonden is voor stromend water. In 2017 werd die stellige bewering echter ingetrokken. Mars heeft twee manen, Phobos en Deimos, beide kleine, onregelmatig gevormde objecten. Mogelijk zijn deze twee manen door de zwaartekracht van Mars ingevangen planetoïden."
    
    EN = FormattedString(referenceEN, font = fontName, fontSize = 10, lineHeight = 12, fill = (0))
    DE = FormattedString(referenceDE, font = fontName, fontSize = 10, lineHeight = 12, fill = (0))
    NL = FormattedString(referenceNL, font = fontName, fontSize = 10, lineHeight = 12, fill = (0))
    
    textBox(EN, GridBox('t1'))
    textBox(DE, GridBox('t2'))
    textBox(NL, GridBox('t3'))
    

##################################################


Page1()
Page2()
Page3()
Page4()
Page5()
saveImage("Proofs/Proof-" + rendertimeShort + ".pdf")
