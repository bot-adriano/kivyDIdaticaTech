from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor=(14/255,61/255,76/255,1)
Window.size= (400,600)


class Comp(BoxLayout):
    def calc(self):
        pr1 = float(self.ids.preco1.text)
        ps1 = float(self.ids.peso1.text)
        pr2 = float(self.ids.preco2.text)
        ps2 = float(self.ids.peso2.text)
        total1=round(pr1 / ps1 * 1000,2)
        total2=round(pr2 / ps2 * 1000,2)

        self.ids.prod1.text=str(total1)
        self.ids.prod2.text=str(total2)
        diferenca=round((pr1 / ps1) / (pr2 / ps2) * 100,2)
        self.ids.dif.text=str(diferenca)+ " %"




class Comparador(App):
    def build(self):
     return Comp()

Comparador().run()