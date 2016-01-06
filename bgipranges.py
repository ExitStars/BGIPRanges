#-*-coding:utf-8-*-
#Modüller
from random import randrange
from threading import Thread
from sys import argv, exit
from requests import post
from socket import socket
from re import findall
from os import system

#Taslaklar
country = {"de":"GERMANY", "fr":"FRANCE", "it":"ITALY", "uk":"UNITED+KINGDOM", "am":"ARMENIA",
"il":"ISRAEL", "ru":"RUSSIAN+FEDERATION", "cn":"CHINA", "us":"UNITED+STATES", "nl":"Netherlands",
"dk":"DENMARK", "gr":"GREECE"}
iplist = []
oflist = []
# http://services.ce3c.be/ciprg/?countrys=ITALY&format=by+input&format2=%3Cipstart%3E{startip}%3C%2Fipstart%3E%0D%0A%3Cipend%3E{endip}%3C%2Fipend%3E%0D%0A%0D%0A%3Cnetmask%3E{netmask}%3C%2Fnetmask%3E%0D%0A%0D%0A

#Renkler
bold = "\033[1m"
underline = "\033[4m"
green = "\033[92m"
blue = "\033[94m"
yellow = "\033[93m"
red = "\033[91m"
endcolor = "\033[0m"

def logo():
	system("clear")
	print bold+"\t\t\t    BGIPRanges | IP Scanner"+endcolor
	print bold+"\t\t\t------------------------------"+endcolor
	print "\t\t\t--==[ {}Cyber Warrior Team{} ]==--".format(green,endcolor)
	print "\t\t\t--==[  {}Bug Researachers{}  ]==--".format(blue,endcolor)
	print "\t\t\t--==[      {}CoderLab{}      ]==--".format(yellow, endcolor)
	print bold+"\t\t\t------------------------------"+endcolor

def help():
	print "How To Usage:"
	print "\t"+bold+red+"root@linux"+endcolor+":"+bold+blue+"~/coderlab"+endcolor+"# {} [Internet Country Code]".format(argv[0])
	c_code, s_code = country.keys(), country.values()
	for i in range(12):
		print "\t\t"+bold+green+"Code: "+endcolor+str(c_code[i])+" | "+bold+green+"Country: "+endcolor+str(s_code[i])

def iprange(code):
	print bold+yellow+"Operation:"+endcolor, code
	ranges = post("""http://services.ce3c.be/ciprg/?countrys="""+code+"""&format=by+input&format2=%3Cipstart%3E{startip}%3C%2Fipstart%3E%0D%0A%3Cipend%3E{endip}%3C%2Fipend%3E%0D%0A%0D%0A%3Cnetmask%3E{netmask}%3C%2Fnetmask%3E%0D%0A%0D%0A""")
	start_ip = findall("<ipstart>(.*?)</ipstart>", ranges.text)
	end_ip = findall("<ipend>(.*?)</ipend>", ranges.text)
	total_ip = len(start_ip)
	for i in range(total_ip):
		ip_start, ip_end = start_ip[i].split("."), end_ip[i].split(".")
		Thread(target=scan, args=(ip_start, ip_end)).start()
		#scan(ip_start, ip_end)
	
def scan(ip_start, ip_end):
	scan = 1
	while scan <= pac:
		target = GenerateIP(ip_start[0], ip_start[1], ip_start[2], ip_start[3], ip_end[0], ip_end[1], ip_end[2], ip_end[3])
		try:
			if target in iplist and target in oflist:
				pass
			else:
				soc = socket()
				soc.connect((target, 80))
				print "> "+target
				soc.close()
		except KeyboardInterrupt:
			exit(1)
		except:
			pass
		finally:
			scan += 1

def GenerateIP(ipstart0, ipstart1, ipstart2, ipstart3, ipend0, ipend1, ipend2, ipend3):
   ip0 = randrange(int(ipstart0),int(ipend0)+1)
   ip1 = randrange(int(ipstart1),int(ipend1)+1)
   ip2 = randrange(int(ipstart2),int(ipend2)+1)
   ip3 = randrange(int(ipstart3),int(ipend3)+1)
   return str(ip0)+"."+str(ip1)+"."+str(ip2)+"."+str(ip3)

logo()
if len(argv) == 2:
	code = country[argv[1]]
	pac = raw_input(bold+blue+"How Many Times?: "+endcolor)
	iprange(code)
else:
	help()
