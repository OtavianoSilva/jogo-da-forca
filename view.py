from tkinter import *

class View(Tk):

    FONT = ("Helvetica", 16)
    CATEGORYS = ["Animal",'fruta','profissão','famoso','marca',
                 'anime','pais','idioma','comida','mitologia']

    def __init__(self) -> None:
        super().__init__()
        self.geometry("400x600")
        self.create_menu()

        self.mainloop()

    def create_menu(self) -> None:
        
        self.title("Menu")

        label_text = "Bem vindo ao jogo da forca\nEscolha seu modo de jogo:"

        self.menu_label = Label(self, text=label_text, font=self.FONT)
        self.menu_label.place(x=70, y=50)

        mode = ["Fácil", "Médio", "Difícil"]
        buttons_text = ["Fácil\nPalavra pequena\nVárias vidas",
                        "Médio\nPalavra média\nNem tantas vidas",
                        "Difícil\nPalavra grande\nPoucas vidas"]
        y = 200
        self.buttons = []
        for i in range(3):
            button = Button(self, text=buttons_text[i],
                            command=lambda i=i:self.set_mode(mode[i]),
                            font=self.FONT)
            button.place(x=115, y=y)
            self.buttons.append(button)
            y+=100
    
    def set_mode(self, mode:str) -> None:
        self.mode = mode
        self.menu_label.destroy()
        for butt in self.buttons:
            butt.destroy()
        self.create_category_selector()

    def create_category_selector(self) -> None:
        label_text = "Selecione a categoria para jogar"
        self.menu_label = Label(self, text=label_text,
                                font=self.FONT)
        self.menu_label.pack()
        self.buttons=[]
        x=50
        y=100
        for i in range(len(self.CATEGORYS)):
            button = Button(self,text=self.CATEGORYS[i],
                            command=lambda i=i:self.set_category(
                self.CATEGORYS[i] ), font=self.FONT)
            button.place(x=x,y=y)
            self.buttons.append(button)
            y+=80
            if i==4:
                x=275
                y=100

    def set_category(self, category:str) -> None:
        self.category=category
        self.menu_label.destroy()
        for butt in self.buttons:
            butt.destroy()

    def start_game(self, guess_word:str,lifes:int) -> None: 
        label_text=str(lifes)
        self.life_counter=Label(self, text=label_text)
        self.life_counter.pack()
        
teste = View()