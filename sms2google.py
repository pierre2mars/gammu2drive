#!/usr/bin/python

import time
import gdata.spreadsheet.service
from os import listdir
from os.path import isfile, join
from shutil import move
from time import sleep

email = 'sms.to.drive@gmail.com'
password = 'tarteauxconcombres'
sms_directory='/var/spool/gammu/inbox'	
weight = '180'
# Find this value in the url with 'key=XXX' and copy XXX below
spreadsheet_key = '0AkxrtdFUAM2JdHVESUozY2pkcGl1QWxGdEZ6MVJPWlE'
# All spreadsheets have worksheets. I think worksheet #1 by default always
# has a value of 'od6'
worksheet_id = 'od6'

spr_client = gdata.spreadsheet.service.SpreadsheetsService()
spr_client.email = email
spr_client.password = password
spr_client.source = 'Example Spreadsheet Writing Application'
spr_client.ProgrammaticLogin()



# Prepare the dictionary to write
dict = {}
dict['date'] = time.strftime('%m/%d/%Y')
dict['time'] = time.strftime('%H:%M:%S')
dict['from'] = 'toto'
dict['text'] = 'bring the milk'
while 1:
	only_files = [ f for f in listdir(sms_directory) if isfile(join(sms_directory,f)) ]
	if only_files <> []: 
		print only_files
		for f in only_files:
			year    = f[2:6]
			month   = f[6:8]
			day     = f[8:10]
			hour    = f[11:13]
			minute  = f[13:15]
			second  = f[15:17]
			sender  = f[21:33]
			date = year + '/' + month + '/' + day 
			time = hour + ':' + minute + ':' + second
			f_file = open(sms_directory + '/' + f, 'r')
			message = f_file.read();
			f_file.close()
			move (sms_directory + '/' + f, sms_directory + '/old')	
			print date, time, sender, message;
			dict['date']    = date
			dict['time']    = time
			dict['from']  = sender
			dict['text'] = message

			entry = spr_client.InsertRow(dict, spreadsheet_key, worksheet_id)
			if isinstance(entry, gdata.spreadsheet.SpreadsheetsList):
				print "Insert row succeeded."
			else:
				print "Insert row failed."

	sleep(1)
