from tkinter import *
from functools import partial

AZUL = '#3784BA'
VERDE = '#90ee90'


class Principal( object ) :
    def __init__( self, instancia) :

        # Criando frames
        self.frame_logo = Frame( instancia )
        self.framebutton = Frame( instancia )
        self.frame_1 = Frame( instancia )
        self.frame_2 = Frame( instancia )
        self.frameb = Frame( instancia , bg= AZUL )
        self.frame_3 = Frame( instancia )
        self.frame_4 = Frame( instancia )
        self.frame_5 = Frame( instancia )
        
        # Colocando logo Python
        logo = PhotoImage( file= 'bg_python.gif' )
        self.logo = Label( self.frame_logo )
        self.logo.image = logo
        self.logo['image'] = logo

        # Criando Checkbuttons
        self.cond_binomial = False
        self.binomial = Checkbutton( self.framebutton, text= 'Binomial Mode', font= self.font(tam= 23), bg = AZUL, command= self.act_binomial ) # Checkbutton Binomial
        
        self.cond_poisson = False
        self.poisson = Checkbutton( self.framebutton, text= 'Poisson Mode', font= self.font(tam= 23), bg= AZUL, command= self.act_poisson  )  # Checkbutton Poisson


        # Criando entradas, botões e mensagens
        self.enter_dados = Entry( self.frame_1, font= self.font(tam= 10)  )
        self.button_calcular = Button( self.frame_2, text= 'Calcular', bg= VERDE ,font= self.font(tam= 14), command= self.Calcular )


        # Espaços e botões
        #self.criar()


        # Resultado
        self.mensage = Label( self.frame_3, text= 'Resultado', fg= 'blue', font= self.font(tam= 12) )

        # Empacotamento de frames
        self.frame_logo.pack(pady= 10)
        self.framebutton.pack()
        self.frame_1.pack( )
        self.frame_2.pack( )
        self.frameb.pack()
        self.frame_3.pack( pady= 20 )
        self.frame_5.pack( )


        # empacotamento
        self.logo.pack( )
        self.binomial.pack( side= LEFT )
        self.poisson.pack( side= RIGHT )
        self.enter_dados.pack( )
        self.button_calcular.pack( )
        self.mensage.pack( )


    # Botões 

        botões = ('Comb(n, k)', 'binomial(n, x, p)', 'poisson(l, x, t)', 'soma(n, p, maior, menor = 0)', 'media', 'desvio', 'moda', 'mediana', 'variancia', 'p(x > k)', 'p(x >= k)', 'p(x < k)', 'p(x <= k)', 'p(k1 < x < k2)', 'p(k1 <= x < k2)', 'p(k1 < x <= k2)', 'p(k1 <= x <= k2)')


        for x in range(len(botões)) :
            if (x%3) == 0:
                subframe = Frame( self.frame_5)
                subframe.pack( )
            
            b = Button( subframe, text= botões[x], bg= 'green',  width= 25 , command= partial( self.ColocaTexto, botões[x] ) )

            b.pack(side= LEFT)

        self.button_del = Button( subframe, text= 'Del', bg= 'red' ,width= 25 )
        self.button_del.pack( )


    def destruir( self ) :

        self.but1.destroy( )
        self.ent.destroy( )
        self.ent2.destroy( )
        self.but2.destroy( )

    
    def criar( self ) : 

        # Espaços e botões
        self.but1 = Button( self.frameb , text= 'm = ', bg= 'gray' )
        self.ent = Entry( self.frameb )
        self.but2 = Button( self.frameb , text= 'p = ', bg= 'gray' )
        self.ent2 = Entry( self.frameb )


    def Mostrar_buttons( self ) :
        
        self.but1.pack( side= LEFT, pady= 13 )
        self.ent.pack( side= LEFT , pady = 13)
        self.but2.pack( side= LEFT,  )
        self.ent2.pack( side= LEFT )

    
    def Tirar_buttons( self ) : 

        self.but1.pack_forget( )
        self.ent.pack_forget( )
        self.but2.pack_forget( )
        self.ent2.pack_forget( )
    

    def Calcular ( self ) : 
   
        self.MSG( var= self.mensage, msg= self.enter_dados.get( ) , cor= 'green' )
        self.enter_dados.delete( 0 , END )

        
    def font( self , fonte= 'Verdana',tam= 36 ) :

        return ( fonte , str( tam ), 'bold' )

    
    def ColocaTexto( self, texto ) :

        self.enter_dados.insert( END , texto )


    def MSG( self, var = True , msg= '', cor= 'red' ) :

        var[ 'text' ] = msg
        var[ 'fg' ] = cor

    
    def act_binomial( self ) :

    
        self.cond_binomial = not self.cond_binomial

        
        if self.cond_binomial :

            if self.cond_poisson :
                self.MSG( var= self.mensage, msg= 'BINOMIAL ATIVADO', cor= 'green' )        
    
                self.cond_poisson = False
                self.poisson.deselect( )

            else :
                self.criar()
                self.Mostrar_buttons( )
                self.MSG( var= self.but1, msg= 'n', cor= 'black'  )
                self.MSG( var= self.but2, msg= 'p', cor= 'black'  )

        
        else :

            self.MSG(var= self.mensage, msg= 'BINOMIAL DESATIVADO' )
 
            self.destruir( )

        
    
    def act_poisson( self ) :

        self.cond_poisson = not self.cond_poisson

        if self.cond_poisson :
            
            self.MSG( var= self.mensage, msg= 'POISSON ATIVADO', cor= 'green' )
            
            if self.cond_binomial : 

                self.cond_binomial = False
                self.binomial.deselect( )
            
            else : 

                self.criar( )
                self.Mostrar_buttons()

                self.MSG( var= self.but1, msg= 'l', cor= 'black')
                self.MSG( var= self.but2, msg= 't', cor= 'black')
        else :

            self.MSG( var= self.mensage, msg= 'POISSON DESATIVADO' )

            self.destruir( )



instancia = Tk( )

Principal(instancia)

instancia.title('Calculadora')

instancia.geometry('800x600')

instancia['bg'] = AZUL

instancia.mainloop()