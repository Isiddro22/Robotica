Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nomad = {'type':'rover','color':'black','processor':'Jetson TX1'}
>>> BARB = {'type':'test-bed','color':'black','type':'wheeled'}
>>> myRobots = {'BARB':'WIP','Nomad':Nomad,'Llamabot':'WIP'}
>>> robots = ["nomad","Ponginator","Alfred"]
>>> for robot in robots :
	print(robot)

nomad
Ponginator
Alfred
>>> for name,data in Nomad.items():
	print(name + ': ' + data)

type: rover
color: black
processor: Jetson TX1
>>> for num,robot in enumerate(robots):
	print(num,robot)

0 nomad
1 Ponginator
2 Alfred
>>> count=1
>>> while count <5:
	print(count)
	count = count+1

1
2
3
4
>>> 
