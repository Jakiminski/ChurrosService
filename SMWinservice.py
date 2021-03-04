'''
1. Instalar Win32 API para Python:  "pip install pywin32"
2. Abrir SUPER + R e inserir: "services.msc" para visualizar os serviços
'''

import socket
import win32serviceutil
import servicemanager
import win32event
import win32service

# CLASSE BASE EM PYTHON PARA CRIAR UM SERVIÇO DO WINDOWS SERVICE
class SMWinservice (win32serviceutil.ServiceFramework):
	_svc_name_ = 'pythonService'
	_svc_display_name_ = 'Python Service'
	_svc_description_ = 'Python Service Description'

	@classmethod
	def parse_command_line(cls):
		win32serviceutil.HandleCommandLine(cls)

	def __init__(self, args):
		win32serviceutil.ServiceFramework.__init__(self, args)
		self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
		socket.setdefaulttimeout(120)

	def SvcStop(self):
		# Chamado quando o serviço for parado
		self.stop()
		self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
		win32event.SetEvent(self.hWaitStop)

	def SvcDoRun(self):
		#Chamado quando o serviço for iniciado
		self.start()
		servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE, servicemanager.PYS_SERVICE_STARTED,(self._svc_name_, ''))
		self.main()

	def start(self):
		#Override to add logic before the start (eg. running condition)
		pass

	def stop(self):
		#Override to add logic before the stop (eg. invalidating running condition)
		pass

	def main(self):
		#Main class to be ovverridden to add logic
		pass

# entry point of the module: copy and paste into the new module
# ensuring you are calling the "parse_command_line" of the new created class
if __name__ == '__main__':
	SMWinservice.parse_command_line()