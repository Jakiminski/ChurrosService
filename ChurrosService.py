import os, sys
import time
import random
from SMWinservice import SMWinservice
import hash4dup

# CLASSE DE UM SERVIÇO DO WINDOWS SERVICE
class Churros (SMWinservice):
	_svc_name_ = 'Churros'
	_svc_display_name_ = 'Churros Service'
	_svc_description_ = 'Fornece churros com recheio de doce de leite aos usuários que rodarem esse serviço.'

	def start(self):
		self.isrunning = True

	def stop(self):
		self.isrunning = False

	def main(self):
		while self.isrunning:
			time.sleep(15)
			
			
# entry point of the module: copy and paste into the new module
# ensuring you are calling the "parse_command_line" of the new created class
if __name__ == '__main__':
	Churros.parse_command_line()
