BACKGROUND = "#F6B4F0" #El rosadito del bg de home
BACKGROUND2 = "#FFD3F6" #Un color rosa blanco que uso para el fondo de las opciones de dulces
BACKGROUND3 = "#c14775" #Un color rosa fuerte oscuro rojo enblanquecido para fondo de dulces múltiples.
BACKGROUND4 = "#8d47c1" #Un color rosa fuerte oscuro azulado enblanquecido para fondo de dulces múltiples.
FONT = ("Light Calibri", 16)
FONT2 = ("Light Calibri", 25)
FONT3 = ("Light Calibri", 13)

COMPONENT = "#FFFFFF" #Color bg de los cuadros (blanco)
COMPONENT2 = "#E75097" #Color bg de los radiobuttons antes de presionarse (rosa fuerte un poco rojo)
COMPONENT2_1 = "#f9abd4" #Color bg de los cuadros tras presionarse (rosa fuerte un poco rojoso enblanquecido)
COMPONENT3 = "#f54f6d" #BOTONES
COMPONENT4 = "#AC3939" #Color bg de los botones al presionarse (rojo oscuro)
COMPONENT5 = "#E8E8E8" #Color gris muy claro para la label
COMPONENT6 = "#981aa0" #Color bg de los cuadros (rosa fuerte oscuro, o morado)
COMPONENT7 = "#c13163" #Color bg de los radiobuttons que son multiples (rosa fuerte oscuro o morado rojoso)
COMPONENT8 = "#5f1aa0" #Color bg de los radiobuttons que son mixtos (rosa fuerte oscuro o morado azuloso)
TEXT = "#000000" #Color de las letras (negro)
TEXT2 = "#FFFFFF" #Color de las letras (blanco)
TEXT3 = "#4A4A4A" #Color de las letras (gris)

STYLEENTRY = {
    "font": FONT3,
    "background": "#ffffff",
    "foreground": "#000000",
    "relief": "solid",
    "bd": 1,
}

STYLEBUTTON = {
    "font": FONT,
     "bg": COMPONENT3,
     "fg": TEXT,
}

STYLEBUTTON2 = {
    "font": FONT3,
     "bg": COMPONENT3,
     "fg": TEXT
}


STYLEBUTTON3 = {
    "font": FONT3,
     "bg": COMPONENT3,
     "fg": TEXT2
}


STYLELABEL = {
    "font": FONT,
     "bg": COMPONENT,
     "fg": TEXT
}

STYLELABEL2 = {
    "font": FONT2,
     "bg": COMPONENT,
     "fg": TEXT,
}
STYLELABEL3 = {
    "font": FONT2,
     "bg": COMPONENT,
     "fg": TEXT,
     "highlightbackground": COMPONENT5,
     "highlightthickness":7
}

STYLELABEL4 = {
    "font": FONT3,
     "bg": COMPONENT,
     "fg": TEXT,
     "highlightbackground": COMPONENT5,
     "highlightthickness":5
}

STYLESELECT = {
    "font": FONT,
     "bg": COMPONENT2,
     "fg": TEXT2
}

STYLESELECT2 = {
    "font": FONT,
     "bg": COMPONENT7,
     "fg": TEXT2
}

STYLESELECT3 = {
    "font": FONT,
     "bg": COMPONENT8,
     "fg": TEXT2
}

STYLECALCULUS = {
     "bg": COMPONENT6,
     "fg": TEXT2

}
STYLETABLA = {
     "font": FONT3,
     "background": COMPONENT6,
     "foreground": TEXT2,
     "fieldbackground": BACKGROUND2,
     "rowheight": 25
}

STYLETOP = {
    "font": FONT2,
     "bg": COMPONENT2,
     "fg": TEXT2,
}

STYLECATEGORY = {
     "bg": COMPONENT2,
     "fg": TEXT2,
}