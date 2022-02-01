from tkinter import *

COR = '#3784BA'

class Principal( object ) :
    def __init__( self, instancia) :

        # Criando frames

        self.frame_1 = Frame( instancia )
        self.frame_2 = Frame( instancia )
        self.frame_3 = Frame( instancia )
        self.frame_4 = Frame( instancia )
        self.frame_5 = Frame( instancia )
        

        # Criando entradas, botões e mensagens
        self.enter_dados = Entry( self.frame_1 )
        self.button_calcular = Button( self.frame_2, text= 'Calcular' )
        self.mensage = Label( self.frame_3, text= 'Resultado', fg= 'blue' )

        # empacotamento
        self.enter_dados.pack( )
        self.button_calcular.pack( )
        self.mensage.pack()

        # Empacotamento de frames
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack(pady= 20)
        self.frame_5.pack()

    # Botões 
        self.botões = ('Comb(n, k)', 'binomial(n, x, p)', 'poisson(l, x, t)', 'soma(n, p, maior, menor = 0)', 'media', 'desvio', 'moda', 'mediana', 'variancia', 'p(x > k)', 'p(x >= k)', 'p(x < k)', 'p(x <= k)', 'p(k1 < x < k2)', 'p(k1 <= x < k2)', 'p(k1 < x <= k2)', 'p(k1 <= x <= k2)')


        for x in range(len(self.botões)) :
            if (x%3) == 0:
                subframe = Frame( self.frame_5 )
                subframe.pack()
            
            b = Button( subframe, text= self.botões[x], bg= 'green', width= 25 )

            b.pack(side= LEFT)

        self.button_del = Button( subframe, text= 'Del', bg= 'red', width= 25 )
        self.button_del.pack()




instancia = Tk()

Principal(instancia)

instancia.title('Hello World')

instancia.geometry('800x600')

instancia['bg'] = COR

instancia.mainloop()














