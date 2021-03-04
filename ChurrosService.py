import time
import random
from pathlib import Path
from SMWinservice import SMWinservice 

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
		i = 0
		while self.isrunning:
			random.seed()
			x = random.randint(1,100000)
			Path(f'C:\\Users\\famil\\Desktop\\Jonas\\SO2\\ChurrosService\\pastaalvo\\{x}_copia.txt').touch()
			time.sleep(5)

# entry point of the module: copy and paste into the new module
# ensuring you are calling the "parse_command_line" of the new created class
if __name__ == '__main__':
	Churros.parse_command_line()