#! /usr/bin/python3

import random
from nicegui import ui

filepath = "/Users/Hunter/PycharmProjects/valorant-agent-randomizer/images/"

master_list = ['Jett', 'Neon', 'Phoenix', 'Raze', 'Reyna', 'Yoru',
	'Breach', 'Fade', 'Gekko', 'KAYO', 'Skye', 'Sova',
	'Astra', 'Brimstone', 'Harbor', 'Omen', 'Viper',
	'Chamber', 'Cypher', 'Deadlock', 'Killjoy', 'Sage']
temp_list = master_list[:]

ui.label('Valorant agent randomizer').style('color: #888; font-size: 300%; font-weight: bold')

### Toggle in-list callback function	
def toggle_cb(agent_name):
	if (agent_name in temp_list):
		temp_list.remove(agent_name)
	elif (agent_name not in temp_list):
		temp_list.append(agent_name)		

### Duelist class, column
with ui.row():
	with ui.column():
		with ui.row():
			ui.image(filepath + 'Duelist.png').classes('w-16')
		ui.label('Duelist')
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Jett.jpeg')
			ui.switch(text='Jett', value=True, on_change=lambda: toggle_cb('Jett'))
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Neon.jpeg')
			ui.switch(text='Neon', value=True, on_change=lambda: toggle_cb('Neon'))
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Phoenix.jpeg')
			ui.switch(text='Phoenix', value=True, on_change=lambda: toggle_cb('Phoenix'))
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Raze.jpeg')
			ui.switch(text='Raze', value=True, on_change=lambda: toggle_cb('Raze'))
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Reyna.jpeg')
			ui.switch(text='Reyna', value=True, on_change=lambda: toggle_cb('Reyna'))
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Yoru.jpeg')
			ui.switch(text='Yoru', value=True, on_change=lambda: toggle_cb('Yoru'))

### Initiator class, column
	with ui.column():
		with ui.row():
			ui.image(filepath + 'Initiator.png').classes('w-16')
		ui.label('Initiator')
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Breach.jpeg')
			ui.switch(text='Breach', value=True, on_change=lambda: toggle_cb('Breach'))
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Fade.jpeg')
			ui.switch(text='Fade', value=True, on_change=lambda: toggle_cb('Fade'))
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Gekko.jpeg')
			ui.switch(text='Gekko', value=True, on_change=lambda: toggle_cb('Gekko'))
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'KAYO.jpeg')
			ui.switch(text='KAYO', value=True, on_change=lambda: toggle_cb('KAYO'))
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Skye.jpeg')
			ui.switch(text='Skye', value=True, on_change=lambda: toggle_cb('Skye'))
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Sova.jpeg')
			ui.switch(text='Sova', value=True, on_change=lambda: toggle_cb('Sova'))
		
### Controller class, column
	with ui.column():
		with ui.row():
			ui.image(filepath + 'Controller.png').classes('w-16')
		ui.label('Controller')
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Astra.jpeg')
			ui.switch(text='Astra', value=True, on_change=lambda: toggle_cb('Astra')) 
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Brimstone.jpeg')
			ui.switch(text='Brimstone', value=True, on_change=lambda: toggle_cb('Brimstone')) 
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Harbor.jpeg')
			ui.switch(text='Harbor', value=True, on_change=lambda: toggle_cb('Harbor')) 
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Omen.jpeg')
			ui.switch(text='Omen', value=True, on_change=lambda: toggle_cb('Omen')) 
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Viper.jpeg')
			ui.switch(text='Viper', value=True, on_change=lambda: toggle_cb('Viper')) 
	
### Sentinel class, column
	with ui.column():
		with ui.row():
			ui.image(filepath + 'Sentinel.png').classes('w-16')
		ui.label('Sentinel')	
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Chamber.jpeg')
			ui.switch(text='Chamber', value=True, on_change=lambda: toggle_cb('Chamber'))
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Cypher.jpeg')
			ui.switch(text='Cypher', value=True, on_change=lambda: toggle_cb('Cypher'))
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Deadlock.jpeg')
			ui.switch(text='Deadlock', value=True, on_change=lambda: toggle_cb('Deadlock'))
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Killjoy.jpeg')
			ui.switch(text='Killjoy', value=True, on_change=lambda: toggle_cb('Killjoy'))
		with ui.row():
			with ui.avatar():
				ui.image(filepath + 'Sage.jpeg')
			ui.switch(text='Sage', value=True, on_change=lambda: toggle_cb('Sage'))
			
	
	
	
	with ui.column():		
			
	### Randomize is-clicked callback function
		def randomize_cb():
			agent_pick = random.choice(temp_list)	
			container.clear()
			with container:
				ui.label('You should play:')
				with ui.avatar():
					ui.image(filepath + agent_pick + '.jpeg')
				ui.label(agent_pick)
				ui.image(filepath + agent_pick + '_Art.png').classes('w-96')
		
		with ui.row():

			with ui.button('RANDOMIZE!', on_click=lambda: randomize_cb()):
				ui.image(filepath + 'random_icon.png')
			### change where these 2 lines are for output location
			global container
			container = ui.column()
			###
	
		
			
ui.link('GitHub', 'https://github.com/hdg630/valorant-agent-randomizer')
	
### Launch the user interface (dark mode)
dark = ui.dark_mode()
dark.enable()
ui.run(title='Valorant agent randomizer', on_air=True)
	

# COMMENT AS NEEDED: Buttons to display the lists (in terminal)
#ui.button('Print Master List', on_click=lambda: print(master_list))
#ui.button('Print Temporary List', on_click=lambda: print(temp_list))	
	
	
