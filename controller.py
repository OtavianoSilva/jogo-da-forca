from model import Model
from view import View

class Controller(Model, View):
    def __init__(self, life: int) -> None:
        self.life = life
 
    def def_word(self) -> None:
        #self.word = self.get_word()
        self.word = list('banana')
    def def_guess_word(self) -> None:
        self.guess_word = list('_'*len(self.word))


    def start_game(self) -> None:
        while not self.lose_won():
            guess_letter = input("Digite um palpite: ") 
            
            if self.try_letter(guess_letter) == False:
                self.life_subtract()
            
            else:
                for x in self.try_letter(guess_letter):
                    self.guess_word[x] = guess_letter
                    
            print(self.guess_word)
        
            if self.lose_won() == True:
                print('Você ganhou')
                break
            elif self.lose_won() == False:
                print('Você perdeu')
                break

        
            
                
    #retorna a posição da letra na palavra ou false se não estiver
    def try_letter(self, letter: str) -> int or bool:
        letter_position = []
        for x in range(len(self.word)):
            if self.word[x] == letter.lower():
                letter_position.append(x)
        
        if letter_position == []:
            return False
        else:
            return letter_position

    def life_subtract(self) -> None:
        self.life -= 1

    def lose_won(self) -> bool:
        if self.life == 0:
            return False
        
        elif self.word == self.guess_word:
            return True
        
        else:
            pass
            
        
palavra1 = Controller(5)
palavra1.def_word()
palavra1.def_guess_word()
palavra1.start_game()