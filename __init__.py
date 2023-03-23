from mycroft import MycroftSkill, intent_file_handler


class RoombaMaster(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('start.cleaning.intent')
    def handle_start_cleaning(self, message):
        self.speak_dialog('comply.dialog')

    @intent_file_handler('stop.cleaning.intent')
    def handle_start_cleaning(self, message):
        self.speak('OK. Vou parar de limpar.')
        self.speak('OK! I will stop cleaning.')


def create_skill():
    return RoombaMaster()

