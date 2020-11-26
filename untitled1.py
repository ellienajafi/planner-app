import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # initialize infinte keywords
    
    def __init__ (self, **kwargs):
        #call grid layout constructor
        super(MyGridLayout,self).__init__(**kwargs)
        
        #set columns
        self. cols =2
        
        #add widgets
        self.Add_widget(Label(text= "name:"))
        #add input box
        self.name= TextInput(miltiline=False)
        self.add_widget(self.name)
        
        #add widgets
        self.Add_widget(Label(text= "favorite pizza:"))
        #add input box
        self.pizza= TextInput(miltiline=False)
        self.add_widget(self.pizza)
        
class MyApp (App):
    def build(self):
        return MyGridLayout