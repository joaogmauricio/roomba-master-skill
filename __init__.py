from mycroft import MycroftSkill, intent_handler
import os.path

class RoombaMaster(MycroftSkill):

	_rooms = []

	def initialize(self):
		self.register_entity_file('room.entity')
		self.register_entity_file('cleaning_robot.entity')
		filename = os.path.dirname(__file__) + '/locale/en-us/room.entity'
		with open (filename, mode='r') as rooms_file:
			self._rooms = rooms_file.read().splitlines()

	@intent_handler('start.cleaning.intent')
	def handle_start_cleaning(self, message):
		room_utterance = message.data.get('room')
		for room in self._rooms:
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

