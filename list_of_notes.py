import pickle
from note import Note
from view import View


class ListOfNotes:
    notes = []
    view = View()
    index = 0
    index_stack = []

    def init(self):
        try:
            with open('notes.cvs', 'rb') as file:
                self.notes = pickle.load(file)
                self.index = len(self.notes)
            with open('indexes.cvs', 'rb') as file:
                self.index_stack = pickle.load(file)
        except EOFError:
            self.notes = []
            self.view = View()
            self.index = 0
            self.index_stack = []

    def add_note(self):
        note = Note()
        note.set_name(self.view.input_note_name())
        note.set_text(self.view.input_note_text())
        note.update_date()
        if len(self.index_stack) == 0:
            note.set_id(self.index)
        else:
            note.set_id(self.index_stack.pop())
        self.notes.append(note)
        self.index = len(self.notes)
        self.view.info_note_msg('add')

    def delete_note(self, note):
        self.index_stack.append(note.get_id())
        self.notes.remove(note)
        if len(self.notes) == 0:
            self.index_stack.clear()
        self.view.info_note_msg('del')


    def read_all_notes(self):
        self.view.show_read_all_banner(len(self.notes))
        for note in self.notes:
            self.view.show_note(note)

    def manage_note_by_id(self):
        commands =  {1: self.view.show_note,
                     2: self.view.edit_note,
                     3: self.delete_note}
        flag = False
        self.view.show_manage_note_menu()
        choice = self.view.input_number(len(commands.keys()), 'menu')
        value = self.view.input_number(self.index, 'id')
        for note in self.notes:
            if note.get_id() == value:
                commands[choice](note)
                flag = True
        if not flag:
            self.view.not_found()

    def save_notes_to_file(self):
        with open('notes.cvs', 'wb') as file:
            pickle.dump(self.notes, file,
                        protocol=pickle.HIGHEST_PROTOCOL)
        with open('indexes.cvs', 'wb') as file:
            pickle.dump(self.index_stack, file,
                        protocol=pickle.HIGHEST_PROTOCOL)
        self.view.saved_info()
