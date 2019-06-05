Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> robots = ["nomad","Ponginator","Alfred"]
>>> robots
['nomad', 'Ponginator', 'Alfred']
>>> myRobot = robots[0]
>>> myRobot
'nomad'
>>> myRobot.capitalize()
'Nomad'
>>> for robot in robots:
	if robot=="Nomad":
		print("This is Nomad")
	else:
		print(robot + " is not Nomad")
this is Nomad
SyntaxError: invalid syntax
>>> for robot in robots:
	if robot=="Nomad":
		print("This is Nomad")
	else:
		print(robot + " is not Nomad")
	
		
this is Nomad
SyntaxError: invalid syntax
>>> 
>>> for robot in robots:
	if robot=="Nomad":
		print("This is Nomad")
	else:
		print(robot + " is not Nomad")

nomad is not Nomad
Ponginator is not Nomad
Alfred is not Nomad
>>> myRobot="Nomad"
>>> myRobot=="Ponginator"
False
>>> myRobot=="Nomad"
True
>>> for robot un robots:
	
SyntaxError: invalid syntax
>>> for robot in robots:
	if robot =="Ponginator" or robot == "Alfred":
		print("these aren't the droids i'm  looking for.")

these aren't the droids i'm  looking for.
these aren't the droids i'm  looking for.
>>> 
