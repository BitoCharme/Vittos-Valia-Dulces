import tkinter as tk
from constantes import style, config
from screens.Candy import *

class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.dulce = tk.StringVar(self, value="Turron Mani Arcor 220 g")
        self.search_var = tk.StringVar()  # Variable para el texto del buscador
        self.init_widgets()

    def move_to_candy(self):
        self.controller.cual = self.dulce.get()
        if self.get_dulce_value()[0] == "@":
            self.controller.show_frame(self.controller.multiple)
            self.controller.multiple.create_new_widgets(self.controller.multiple_frame, self.get_dulce_value())
        elif self.get_dulce_value()[0] == "%":
            self.controller.show_frame(self.controller.mix)
            self.controller.mix.create_new_widgets(self.controller.mix_frame, self.get_dulce_value())
        else:
            self.controller.show_frame(self.controller.candy)
            self.controller.candy.create_new_widgets(self.controller.candy_frame, self.get_dulce_value())

    def get_dulce_value(self):
        return self.dulce.get()

    def move_to_creation(self):
        self.controller.show_frame(self.controller.creation)

    def move_to_comparison(self):
        self.controller.show_frame(self.controller.comparison)

    def init_widgets(self):
        tk.Label(
            text="Cálculo de la valía de dulces",
            justify=tk.CENTER,
            **style.STYLELABEL2
        ).pack(side=tk.TOP, fill=tk.BOTH, expand=False, padx=22, pady=11)

        self.optionsFrame = tk.Frame(self)
        self.optionsFrame.configure(background=style.BACKGROUND)
        self.optionsFrame.pack(side=tk.BOTTOM, fill=tk.X, expand=True, padx=22, pady=11)

        tk.Label(
            self.optionsFrame,
            text='🍡🍬 Elige el dulce y luego presiona "Ir al dulce" 🍭🍫',
            justify=tk.CENTER,
            **style.STYLELABEL
        ).pack(side=tk.TOP, fill=tk.X, expand=True, padx=22, pady=7)

        self.text = tk.Text(self.optionsFrame, wrap="word", background=style.BACKGROUND2)
        self.vsb = tk.Scrollbar(self.optionsFrame, command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.create_radiobuttons()

        tk.Button(
            self,
            text="Ir al dulce",
            command=self.move_to_candy,
            **style.STYLEBUTTON,
            relief=tk.FLAT,
            activebackground=style.COMPONENT4,
            activeforeground=style.TEXT,
        ).pack(side=tk.TOP, fill=tk.X, padx=22, pady=11)

        tk.Button(
            self,
            text="Añadir dulce",
            command=self.move_to_creation,
            **style.STYLEBUTTON,
            relief=tk.FLAT,
            activebackground=style.COMPONENT4,
            activeforeground=style.TEXT,
        ).pack(side=tk.TOP, fill=tk.X, padx=22, pady=11)

        tk.Button(
            self,
            text="Comparar dulces",
            command=self.move_to_comparison,
            **style.STYLEBUTTON,
            relief=tk.FLAT,
            activebackground=style.COMPONENT4,
            activeforeground=style.TEXT,
        ).pack(side=tk.TOP, fill=tk.X, padx=22, pady=11)

        # Campo de entrada para el buscador
        search_entry = tk.Entry(
            self,
            textvariable=self.search_var,
            **style.STYLEENTRY
        )
        search_entry.pack(side=tk.TOP, fill=tk.X, padx=22, pady=4)
        search_entry.insert(0, 'Escribe aquí el nombre de un dulce y luego presiona "Enter" para buscarlo')
        # Vincular el evento Enter al método update_radiobuttons
        search_entry.bind("<Return>", lambda event: self.update_radiobuttons())

    def create_radiobuttons(self, filter_text=""):
        self.text.configure(state="normal")
        self.text.delete("1.0", "end")
        
        def add_radiobutton(value, style_args):
            if value[0] == "@" or value[0] == "%":
                radiobutton = tk.Radiobutton(
                    self.optionsFrame,
                    text=value[1:-1],
                    variable=self.dulce,
                    value=value,
                    **style_args
                )

            else:
                radiobutton = tk.Radiobutton(
                    self.optionsFrame,
                    text=value,
                    variable=self.dulce,
                    value=value,
                    **style_args
                )
            self.text.window_create("insert", window=radiobutton, padx=10, pady=10)

        # Crear Radiobuttons según el tipo, aplicando el filtro
        for (key, value) in config.DULCES.items():
            if filter_text.lower() in value.lower():
                if value[0] == "@":
                    add_radiobutton(value, {
                        "activebackground": "#ee8cda",
                        "activeforeground": style.TEXT,
                        "indicatoron": 0,
                        "selectcolor": style.COMPONENT3,
                        **style.STYLESELECT2
                    })
                elif value[0] == "%":
                    add_radiobutton(value, {
                        "activebackground": style.BACKGROUND,
                        "activeforeground": style.TEXT,
                        "indicatoron": 0,
                        "selectcolor": style.COMPONENT3,
                        **style.STYLESELECT3
                    })
                else:
                    add_radiobutton(value, {
                        "activebackground": style.BACKGROUND,
                        "activeforeground": style.TEXT,
                        "indicatoron": 0,
                        "selectcolor": style.COMPONENT2_1,
                        **style.STYLESELECT
                    })

        self.text.configure(state="disabled")

    def update_radiobuttons(self):
        # Actualizar radiobuttons basados en el texto del buscador
        filter_text = self.search_var.get()
        self.create_radiobuttons(filter_text)

    def tkraise(self, *args, **kwargs):
        # Llamar al método tkraise original
        super().tkraise(*args, **kwargs)
        # Esto actualiza la lista de dulces
        config.actualizar_dulces()
        # Volver a crear los Radiobuttons al mostrar el frame
        self.create_radiobuttons()
