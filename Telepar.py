#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telethon
from telethon import TelegramClient, events, sync
import os

'''
Programa que accede a tu cuenta de telegram y permite ejecutar diversas tareas mediante un menú interactivo.
'''


# Introducir aquí el api_id y el api_hash que puedes obtener en https://my.telegram.org, dentro de 'API Development'.
api_id = xxxxxx
api_hash = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

#Crea la primera conexión del programa. Te pedirá tu número de teléfono y el pin que te llegue a tu cuenta de  telegram.
client = TelegramClient('session_name', api_id, api_hash)
client.start()

########################################################################################################################


nombre=(client.get_me().first_name)
apellido=(client.get_me().last_name)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Descomenta si quieres imprimir las opciones de colores:
# print(bcolors.BOLD + 'bold' + bcolors.ENDC)
# print(bcolors.FAIL + 'fail' + bcolors.ENDC)
# print(bcolors.HEADER + 'header' + bcolors.ENDC)
# print(bcolors.OKBLUE + 'okblue' + bcolors.ENDC)
# print(bcolors.OKGREEN + 'okgreen' + bcolors.ENDC)
# print(bcolors.UNDERLINE + 'underline' + bcolors.ENDC)
# print(bcolors.WARNING + 'warning' + bcolors.ENDC)


def cabecera():
	'''
	Función que imprime una cabecera con tu nombre de usuario.
	'''
	print (bcolors.HEADER + "")
	print('#'*50,'\n')
	print('Estás logeado como:',nombre,apellido,'\n')
	print('#'*50,'\n'*2 + bcolors.ENDC)
	return ""



def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu.
	"""
	os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print (cabecera(),bcolors.UNDERLINE + "Selecciona una opción: \n" + bcolors.ENDC)
	print (bcolors.OKGREEN + "\t1 - Imprimir información de tu usuario.")
	print 					("\t2 - Imprimir los chats y los canales de tu telegram.")
	print 					("\t3 - Enviar un mensaje a un chat.")
	print 					("\t4 - Imprimir los 3 últimos mensajes en los que aparezca un texto.")
	print 					("\t5 - Reenviarte un mensaje en el que aparezca un texto que tu quieras.")
	print 					("\t6 - (En desarrollo)")
	print 					("\t9 - salir" + bcolors.ENDC)


########################################################################################################################



while True:
	# Mostramos el menu
	menu()
	# solicituamos una opción al usuario
	opcionMenu = input(bcolors.WARNING + "\nIntroduce un numero: " + bcolors.ENDC)
	if opcionMenu == "1":
		print (client.get_me().stringify())
		input(bcolors.WARNING + "Has pulsado la opción 1...\npulsa una tecla para continuar" + bcolors.ENDC)

	elif opcionMenu == "2":
		dialogs = client.get_dialogs()
		for i in dialogs:
			print(i.title)
		input(bcolors.WARNING + "Has pulsado la opción 2...\npulsa una tecla para continuar" + bcolors.ENDC)   

	elif opcionMenu == "3":
		chat = input("Introduce el nombre del chat: ") 
		mensaje_enviar= input("Introduce el mensaje que quieres enviar: ")
		client.send_message(chat, mensaje_enviar)
		input(bcolors.WARNING + "Has pulsado la opción 3...\npulsa una tecla para continuar" + bcolors.ENDC)

	elif opcionMenu == "4":
		chat = input("Introduce el nombre del chat "+  bcolors.OKGREEN + "(puedes consultarlos desde la opción 2) " + bcolors.ENDC +  "del que quieras reenviarte el mensaje: ")        
		texto = input("Introduce el texto que quieres que aparezca: ")
		espaciador=(bcolors.OKGREEN + "#"*50 + bcolors.ENDC)
		print(espaciador)
		for message in client.iter_messages(chat, search=texto, limit=3):	
			try:
				print(message.message, message.date, '\n', espaciador, "\n")
			except (RuntimeError, RuntimeWarning, ZeroDivisionError, ValueError, TypeError):
    				print("El chat o canal no existe o no está bien escrito. Tambien puede que no exista el texto...")
			continue
    # code to deal with the exception
		input(bcolors.WARNING + "Has pulsado la opción 4...\npulsa una tecla para continuar" + bcolors.ENDC)

	elif opcionMenu == "5":
		chat = input("Introduce el nombre del chat "+  bcolors.OKGREEN + "(puedes consultarlos desde la opción 2) " + bcolors.ENDC +  "del que quieras reenviarte el mensaje: ")        
		texto = input("Introduce el texto que debe aparecer en el mensaje: ")
		print("\nReenviando...")
		print("...tan pronto publiquen un nuevo mensaje en el canal \"",chat,"\" que contenga el texto \"",texto,"\", \néste será reenviado a tu canal \"Mensajes guardados.\" ")
		print("Pulsa \"Ctrl+C\" para detener y volver al menú principal")

		for message in client.iter_messages(chat, search=texto, limit=1):
			message_id = message.id
			client.send_message('me', message)
		while True:
			try:
				for message in client.iter_messages(chat, search=texto, min_id=(message_id)):
					client.send_message('me', message)
					message_id=message.id			
			except KeyboardInterrupt:
				break				
		else:
			input(bcolors.WARNING + "En este chat o canal no hay ningún mensaje con el texto que tu indicas.\npulsa una tecla para continuar" + bcolors.ENDC)


	elif opcionMenu == "6":
		print("pulsa \"Ctrl+C\" para detener y volver al menú principal")

		for message in client.iter_messages('Xiaomi Chollos', search='Note 7 4/64', limit=1):
			message_id = message.id
			client.send_message('me', message)
		while True:
			try:
				for message in client.iter_messages('Xiaomi Chollos', search='Note 7 4/64', min_id=(message_id)):
					client.send_message('me', message)				
			except KeyboardInterrupt:
				break				
		else:
			input(bcolors.WARNING + "En este chat o canal no hay ningún mensaje con el texto que tu indicas.\npulsa una tecla para continuar" + bcolors.ENDC)


	elif opcionMenu == "9":
		os.system('clear')
		print(cabecera(),bcolors.WARNING + "\nHasta luego!\n\n\n" + bcolors.ENDC)
		break

	else:
		print ("")
		input(bcolors.FAIL + "No has pulsado ninguna opción correcta...\npulsa una tecla para continuar" + bcolors.ENDC)


