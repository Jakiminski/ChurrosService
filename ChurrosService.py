import os, sys
import time
import random
import traceback
from SMWinservice import SMWinservice
import hash4dup
			
# CLASSE DE UM SERVIÇO DO WINDOWS SERVICE
class Churros (SMWinservice):
	_svc_name_ = 'Churros'
	_svc_display_name_ = 'Churros Service'
	_svc_description_ = 'Apaga arquivos duplicatas dentro de um diretório.'

	def start(self):
		self.isrunning = True

	def stop(self):
		self.isrunning = False

	def main(self):
		
		while self.isrunning:
			try:
				folder = 'C:\\Users\\famil\\Desktop\\Jonas\\SO2\\ChurrosService'
				folders = hash4dup.allpaths(folder,[folder,])
				#print('All paths found.')
				
				duplicates = {}
				for f in folders: # Iterate the folders given
					#print(f)
					# Find the duplicated files and append them to the dups
					if os.path.exists(f):
						print('Searching duplicates inside:\t\'{}\''.format(f))
						hash4dup.joinDicts(duplicates, hash4dup.findDup(f))
				
				#print('Making log.')
				logfile = open('C:\\Users\\famil\\Desktop\\Jonas\\SO2\\ChurrosService\\DeleteLog.txt', 'a+')
				
				self.isrunning = not hash4dup.results(duplicates, logfile)
				time.sleep(15)
			except Exception:
				print(traceback.format_exc())
			    # or
				print(sys.exc_info()[2])


			# lista com todas as pastas e subpastas
			


		'''
		while self.isrunning:
			time.sleep(15)
		'''
		'''
			# lista com todas as pastas e subpastas
			folder = 'C:\\Users\\famil\\Desktop\\Jonas\\SO2\\ChurrosService\\root'
			folders = allpaths(folder,[folder,])

			duplicates = {}
			for f in folders: # Iterate the folders given
				#print(f)
				# Find the duplicated files and append them to the dups
				if os.path.exists(f):
					joinDicts(duplicates, findDup(f))
				results(duplicates)

		'''	
			
# entry point of the module: copy and paste into the new module
# ensuring you are calling the "parse_command_line" of the new created class
if __name__ == '__main__':
	Churros.parse_command_line()
