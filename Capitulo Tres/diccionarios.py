Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nomad={'type':'rover','color':'black','processor':'JetsonTX1'}
>>> print(Nomad['type'])
rover
>>> BARB={'type':'test-bed','color':'black','type':'wheeled'}
>>> BARB
{'color': 'black', 'type': 'wheeled'}
>>> myRobots ={'BARB':'WIP','Nomad':Nomad,'Llambot':'WIP'}
>>> myRobots
{'BARB': 'WIP', 'Nomad': {'color': 'black', 'type': 'rover', 'processor': 'JetsonTX1'}, 'Llambot': 'WIP'}
>>> myRobots=['Llamabot']='Getting to it'
SyntaxError: can't assign to literal
>>>  myRobots['Llamabot']='Getting to it'
 
  File "<pyshell#7>", line 2
    myRobots['Llamabot']='Getting to it'
    ^
IndentationError: unexpected indent
>>> myRobots=['Llamabot']='Getting to it'
SyntaxError: can't assign to literal
>>> myRobots['Llamabot']='Getting to it'
>>> myRobots
{'BARB': 'WIP', 'Nomad': {'color': 'black', 'type': 'rover', 'processor': 'JetsonTX1'}, 'Llamabot': 'Getting to it', 'Llambot': 'WIP'}
>>> del myRobots['Llamabot']
>>> myRobots
{'BARB': 'WIP', 'Nomad': {'color': 'black', 'type': 'rover', 'processor': 'JetsonTX1'}, 'Llambot': 'WIP'}
>>> workingRobots=myRobots.copy()
>>> workingRobots
{'BARB': 'WIP', 'Nomad': {'color': 'black', 'type': 'rover', 'processor': 'JetsonTX1'}, 'Llambot': 'WIP'}
>>> otherRobots={'Rasbot-pi':'Pi-bot from book','spiderbot':'broken'}
>>> myRobots.update(otherRobots)
>>> myRobots
{'BARB': 'WIP', 'Nomad': {'color': 'black', 'type': 'rover', 'processor': 'JetsonTX1'}, 'Rasbot-pi': 'Pi-bot from book', 'Llambot': 'WIP', 'spiderbot': 'broken'}
>>> 
