from mycroft import MycroftSkill, intent_file_handler


class RoombaMaster(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('master.roomba.intent')
    def handle_master_roomba(self, message):
        self.speak_dialog('master.roomba')


def create_skill():
    return RoombaMaster()

