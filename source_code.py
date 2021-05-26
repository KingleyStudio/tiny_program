import os
import datetime

variables = {}

def init():
	os.system("cls")
	os.system("color 0f")

	print("Tiny program by KingleyStudio 2021 v1.01")
	print()

def calc():
	print("Enter EXIT to exit")
	while True:
		example = input("Enter an example >>> ")
		if example == "EXIT":
			menu()
		else:
			try:
				print(eval(example))
			except ZeroDivisionError:
				print("ERROR: Division by zero")
			except:
				print("ERROR: Invalid syntax")

def clock():
	print(datetime.datetime.now().strftime("%d.%m.%Y %H:%M"))

def menu():
	global variables
	while True:
		command = input(">>> ")
		command = command.split()
		if command[0] == "OUT":
			if command[1].startswith("/"):
				try:
					print(variables[command[1]])
				except:
					print(f"ERROR: Variable named {command[1]} was not found or does not exist")
			else:
				print(" ".join(command[1:]))
		if command[0].startswith("/"):
			command[0].lower()
			variables[command[0]] = "No value here"
		if command[0] == "ASSIGN":
			try:
				var = command[1].lower()
				value1 = command[2]
			except:
				print("ERROR: Invalid syntax")
			else:
				if value1 == "VALUE":
					try:
						value2 = command[3:]
					except:
						print("ERROR: Invalid syntax")
					else:
						variables[command[1]] = " ".join(value2)
				elif value1 == "EXAM":
					try:
						value2 = " ".join(command[3:])
					except:
						print("ERROR: Invalid syntax")
					else:
						try:
							variables[command[1]] = eval(value2)
						except:
							variables[command[1]] = " ".join(value2)
				elif value1 == "INPUT":
					value = input("Enter a value >>> ")
					variables[command[1]] = value
				else:
					print("No value here")
		if command[0] == "START":
			if command[1].lower() == "calc":
				calc()
			elif command[1].lower() == "clock":
				clock()
			else:
				print("ERROR: Program not found")
		if command[0] == "NEWFOLDER":
			try:
				path = command[1]
			except:
				print("ERROR: No path specified")
			else:
				os.mkdir(path)
		if command[0] == "READFILE":
			try:
				path = command[1]
			except:
				print("ERROR: No path specified")
			else:
				try:
					file = open(path, "r")
					content = file.read()
				except FileNotFoundError:
					print("ERROR: File not found")
				else:
					length = len(content)
					if length >= 1000000:
						print("ERROR: File length is too long")
					else:
						print(content)
					file.close()
		if command[0] == "CLR":
			os.system("cls")
		if command[0] == "EXECUTE":
			execute = input("Enter a windows-command >>> ")
			os.system(execute)
		else:
			print("ERROR: Syntax error")

init()
menu()
