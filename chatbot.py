print("Hey there! This is the Desktop-Anywhere Chatbot")
while True:
	command = input("Your chatbot is waiting for your command: ")
	
	if(command=="hey" or command=="Hey" or command=="What's up?"):
		print("Are you having a good day boss?")

	elif command=="time":
		from datetime import datetime
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		print("The time is: " + current_time)

	elif command=="git repo":
		command = "cd Desktop/TY_EDI; source edi/bin/activate;bash git.sh"
		import appscript
		appscript.app ('Terminal').do_script ( command )