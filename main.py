import customtkinter

# Définition de la classe Operation
class Operation():
    # Méthode pour gérer les clics sur les boutons
    def click(self, num):
        print(num)

# Définition de la classe Interface
class Interface():
    # Initialisation de l'interface
    def __init__(self) -> None:
        # Création de la fenêtre principale
        self.master = customtkinter.CTk()
        self.master.title("calculatrice")
        self.master.geometry("600x360")
        self.master.resizable(False, False)

        # Label pour l'interface
        self.label = customtkinter.CTkLabel(self.master, text='Basic and Advanced')
        self.label.pack()

        # Cadre pour le champ de saisie
        self.frame_champ_saisi = customtkinter.CTkFrame(self.master)
        self.frame_champ_saisi.pack(expand=True)

        # Cadre pour les boutons
        self.frame_bouttons = customtkinter.CTkFrame(self.master)
        self.frame_bouttons.pack(expand=True)

        # Cadre pour les boutons basiques
        self.bouttons_basic = customtkinter.CTkFrame(self.frame_bouttons, fg_color='transparent')
        self.bouttons_basic.grid(row=0, column=0, padx=10)

        # Cadre pour les boutons avancés
        self.bouttons_avance = customtkinter.CTkFrame(self.frame_bouttons, fg_color='transparent')
        self.bouttons_avance.grid(row=0, column=1)

        # Champ de saisie
        self.champ_saisi = customtkinter.CTkTextbox(self.frame_champ_saisi, width=500, height=50)
        self.champ_saisi.pack()
        self.champ_saisi.configure(state='disable')

    # Méthode pour créer les boutons
    def create(self):
        # Boutons numériques et opérateurs basiques
        self.button1 = customtkinter.CTkButton(self.bouttons_basic, text='1', command=lambda: self.click('1'), width=50)
        self.button1.grid(row=0, column=0, padx = 10, pady = 10)
        self.button2 = customtkinter.CTkButton(self.bouttons_basic, text='2', command=lambda: self.click('2'), width=50)
        self.button2.grid(row=0, column=1, pady = 10)
        self.button3 = customtkinter.CTkButton(self.bouttons_basic, text='3', command=lambda: self.click('3'), width=50)
        self.button3.grid(row=0, column=2, padx = 10, pady = 10)
        
        self.division = customtkinter.CTkButton(self.bouttons_basic, text='/', command=lambda: self.click('/'), width=70 )
        self.division.grid(row=0, column=3, pady = 10)

        self.button4 = customtkinter.CTkButton(self.bouttons_basic, text='4', command=lambda: self.click('4'), width=50)
        self.button4.grid(row=1, column=0)
        
        self.button5 = customtkinter.CTkButton(self.bouttons_basic, text='5', command=lambda: self.click('5'), width=50)
        self.button5.grid(row=1, column=1, padx = 10)
        self.button6 = customtkinter.CTkButton(self.bouttons_basic, text='6', command=lambda: self.click('6'), width=50)
        self.button6.grid(row=1, column=2, padx = 10, pady = 10 )
        
        self.produit = customtkinter.CTkButton(self.bouttons_basic, text='X', command=lambda: self.click('*') , width=70)
        self.produit.grid(row=1, column=3, pady = 10)
        
        self.button7 = customtkinter.CTkButton(self.bouttons_basic, text='7', command=lambda: self.click('7'), width=50)
        self.button7.grid(row=2, column=0, padx = 10, pady = 10)
        self.button8 = customtkinter.CTkButton(self.bouttons_basic, text='8', command=lambda: self.click('8'), width=50)
        self.button8.grid(row=2, column=1, padx = 10, pady = 10)
        self.button9 = customtkinter.CTkButton(self.bouttons_basic, text='9', command=lambda: self.click('9'), width=50)
        self.button9.grid(row=2, column=2, padx = 10, pady = 10)
        
        self.soustraction = customtkinter.CTkButton(self.bouttons_basic, text='-', command=lambda: self.click('-'), width=70 )
        self.soustraction.grid(row=2, column=3, pady = 10)
        
        self.button0 = customtkinter.CTkButton(self.bouttons_basic, text='0', command=lambda: self.click('0'), width=50)
        self.button0.grid(row=3, column=0)
        
        self.virgule = customtkinter.CTkButton(self.bouttons_basic, text='.', width=50)
        self.virgule.grid(row = 3, column = 1 , padx = 10)
        
        self.effacer = customtkinter.CTkButton(self.bouttons_basic, text='x', width=50, fg_color = 'red', command=self.erase)
        self.effacer.grid(row=3, column=2)

        self.addition = customtkinter.CTkButton(self.bouttons_basic, text='+', command=lambda: self.click('+'), width=70 )
        self.addition.grid(row=3, column=3)
    
        # Boutons pour les fonctionnalités avancées
        factorielle = customtkinter.CTkButton(self.bouttons_avance, text='fact', width=50, command=lambda: self.click('fact'))
        factorielle.grid(row = 0, column = 0, padx = 10)
        log = customtkinter.CTkButton(self.bouttons_avance, text='log', width=50, command=lambda: self.click('log'))
        log.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        log_neperien = customtkinter.CTkButton(self.bouttons_avance, text='ln', width=50, command=lambda: self.click('ln'))
        log_neperien.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        cosinus = customtkinter.CTkButton(self.bouttons_avance, text='cos', width=50, command=lambda: self.click('cos'))
        cosinus.grid(row = 0, column = 2, padx = 10, pady = 10)

        sinus = customtkinter.CTkButton(self.bouttons_avance, text='ln', width=50, command=lambda: self.click('sin'))
        sinus.grid(row = 0, column = 3, padx = 10, pady = 10)
        
        tang = customtkinter.CTkButton(self.bouttons_avance, text='ln', width=50, command=lambda: self.click('tan'))
        tang.grid(row = 1, column = 0, padx = 10, pady = 10)

        radical = customtkinter.CTkButton(self.bouttons_avance, text='rad', width=50, command=lambda: self.click('rad'))
        radical.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        paranthese_ouvrante = customtkinter.CTkButton(self.bouttons_avance, text='(', width=50, command=lambda: self.click('('))
        paranthese_ouvrante.grid(row = 1, column = 2, padx = 10, pady = 10)
        
        paranthese_fermante = customtkinter.CTkButton(self.bouttons_avance, text=')', width=50, command=lambda: self.click(')'))
        paranthese_fermante.grid(row = 1, column = 3, padx = 10, pady = 10)
        
        # Bouton pour effectuer une opération
        operer = customtkinter.CTkButton(self.bouttons_avance, text='=', width=50, height=60, command=lambda: self.equal, fg_color='green')
        operer.grid(row=2, column=0, padx=10, pady=10)

        # Boucle principale pour l'interface
        self.master.mainloop()

    # Méthode pour gérer les clics sur les boutons numériques et opérateurs basiques
    def click(self, num):
        self.champ_saisi.configure(state='normal')
        temp = self.champ_saisi.get(1.0, customtkinter.END)
        self.champ_saisi.delete(1.0, customtkinter.END)
        self.champ_saisi.insert(customtkinter.END, temp.strip('\n') + " " + num)
        self.champ_saisi.configure(state='disable')

    # Méthode pour effacer le dernier caractère du champ de saisie
    def erase(self):
        self.champ_saisi.configure(state='normal')
        temp = self.champ_saisi.get(1.0, customtkinter.END)
        temp = temp[:-2]
        self.champ_saisi.delete(1.0, customtkinter.END)
        self.champ_saisi.insert(customtkinter.END, temp)
        self.champ_saisi.configure(state='disable')

    # Méthode pour évaluer l'expression dans le champ de saisie
    def equal(self):
        pass

# Création de l'interface
interface = Interface().create()
