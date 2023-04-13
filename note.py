from datetime import datetime


class Note:
    id = 0
    name = ""
    date = ""
    text = ""

    def set_id(self, value):
        self.id = value

    def set_name(self, name):
        self.name = name

    def set_text(self, text):
        self.text = text

    def update_date(self):
        self.date = datetime.now().strftime('%Y, %B %d, %A | %H:%M')

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_text(self):
        return self.text
