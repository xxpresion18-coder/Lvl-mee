from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
import datetime

class Player:
    def __init__(self):
        self.level = 1
        self.xp = 0

    def add_xp(self, xp):
        self.xp += xp
        if self.xp >= self.level * 100:
            self.xp -= self.level * 100
            self.level += 1

player = Player()

QUESTS = [
    {"name": "Aleargă 2 km", "xp": 50},
    {"name": "100 flotări", "xp": 60},
    {"name": "150 abdomene", "xp": 70},
    {"name": "5 min plank", "xp": 40},
]

class UI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        with self.canvas.before:
            Color(0.02, 0.03, 0.08, 1)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)

        self.title = Label(text=self.stats(), font_size=24, color=(0.2,0.6,1,1))
        self.add_widget(self.title)

        for q in QUESTS:
            btn = Button(text=f"{q['name']} (+{q['xp']} XP)", background_color=(0,0.2,0.5,1))
            btn.bind(on_press=lambda x, q=q: self.complete(q))
            self.add_widget(btn)

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def stats(self):
        return f"LEVEL {player.level} | XP {player.xp}/{player.level*100}"

    def refresh(self):
        self.title.text = self.stats()

    def complete(self, quest):
        player.add_xp(quest["xp"])
        self.refresh()

class MainApp(App):
    def build(self):
        return UI()

MainApp().run()
