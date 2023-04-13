from list_of_notes import ListOfNotes
from view import View


class Menu:
    view = View()
    notes = ListOfNotes()
    commands = {1: notes.add_note, 2: notes.manage_note_by_id, 3: notes.read_all_notes,
                  4: notes.save_notes_to_file}

    def start(self):
        self.view.greeting()
        while(True):
            self.view.show_main_menu()
            choice = self.view.input_number(len(self.commands.keys()), 'menu')
            if choice == 0:
                self.view.exit_msg()
                break
            else:
                self.commands[choice]()