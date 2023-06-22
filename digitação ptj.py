from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from functools import partial
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import time
import random as r
from datetime import timedelta,datetime

class MyApp(App):
    frase = ''
    lvl1 = 'asdfg çlkjh ' * 5
    
    def build(self):
        layout = FloatLayout()
        self.caixa_txt = TextInput(multiline=True,size_hint=(None,None),size=(300,100),pos_hint={'x':0.2,'y':0.2})
        texto = Label(text=self.lvl1,font_size=20,pos_hint={'x':0.01,'y':0.2})
        self.timing = Label(text='00:00',font_size=20,pos_hint={'x':0.01,'y':0.15})
        start = Button(text='START',size_hint=(None,None),size=(100,100),pos_hint={'x':0.35,'y':0.01})
        
        self.frase = texto.text.rstrip()
       
        
        self.caixa_txt.bind(text=self.armazena)
        start.bind(on_release=lambda *args:(self.iniciar_cronometro(*args),self.limpa_texto(*args)))
        layout.add_widget(self.caixa_txt)
        layout.add_widget(texto)
        layout.add_widget(self.timing)
        layout.add_widget(start)
        return layout
    
    def armazena(self, instance,value):
        txt = value
        len_txt = len(txt)
        len_lvl=len(self.lvl1)
        
        print(txt,'\n',self.frase[:len_txt])
        
        if txt == self.frase[:len_txt]:
            instance.foreground_color = (0,0,1,1)
            print('FUNCIONA')
        else:
            instance.foreground_color = (1,0,0,1)
            
        if len_txt + 1  == len_lvl:
            instance.readonly=True
            self.finalizar_cronometro
            print('oi')
            
    def iniciar_cronometro(self, *args):
        Clock.schedule_interval(self.atualizar_tempo, 0.1)
        self.tempo_inicial = datetime.now()

    def atualizar_tempo(self, dt):
        tempo_atual = datetime.now() - self.tempo_inicial
        minutos = tempo_atual.seconds // 60
        segundos = tempo_atual.seconds % 60
        self.timing.text = '{:02d}:{:02d}'.format(minutos, segundos)

    def finalizar_cronometro(self):
        Clock.unschedule(self.atualizar_tempo)
    
    def limpa_texto(self,*args):
        self.caixa_txt.text=''
        self.caixa_txt.focus=True
   
if __name__ == '__main__':
    MyApp().run()