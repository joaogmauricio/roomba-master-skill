from mycroft import MycroftSkill, intent_handler

class RoombaMaster(MycroftSkill):

    rooms = []

    def initialize(self):
        self.register_entity_file('room.entity')
        self.register_entity_file('cleaning_robot.entity')
        with open ('/opt/mycroft/skills/roomba-master-skill/locale/en-us/room.entity') as rooms_file:
            self.rooms = rooms_file.read().splitlines()

    @intent_handler('start.cleaning.intent')
    def handle_start_cleaning(self, message):
        room_utterance = message.data.get('room')
        for room in self.rooms:
            if room in room_utterance:
                self.speak_dialog('comply', {'room': room})

    @intent_handler('stop.cleaning.intent')
    def handle_stop_cleaning(self, message):
        self.speak('OK. Vou parar de limpar.')
        self.speak('OK! I will stop cleaning.')

    def stop(self):
        pass

def create_skill():
    return RoombaMaster()

