#! /usr/bin/python3

import random

from nicegui import ui

global container

filepath = "/Users/Hunter/PycharmProjects/valorant-agent-randomizer/images/"
master_list = ['Jett', 'Neon', 'Phoenix', 'Raze', 'Reyna', 'Yoru',
               'Breach', 'Fade', 'Gekko', 'KAYO', 'Skye', 'Sova',
               'Astra', 'Brimstone', 'Harbor', 'Omen', 'Viper',
               'Chamber', 'Cypher', 'Deadlock', 'Killjoy', 'Sage']
temp_list = master_list[:]

ui.label('Valorant agent randomizer').style('color: #888; font-size: 300%; font-weight: bold')


def toggle_cb(agent_name):
    if agent_name in temp_list:
        temp_list.remove(agent_name)
    elif agent_name not in temp_list:
        temp_list.append(agent_name)


def class_column(class_ui_name):
    with ui.row():
        ui.image(filepath + class_ui_name + '.png').classes('w-16')
    ui.label(class_ui_name)


def agent_ui(agent_ui_name):
    with ui.row():
        with ui.avatar():
            ui.image(filepath + agent_ui_name + '.jpeg')
        ui.switch(text=agent_ui_name, value=True, on_change=lambda: toggle_cb(agent_ui_name))


# Sort agent classes by column
with ui.row():
    with ui.column():
        class_column('Duelist')
        agent_ui('Jett'), agent_ui('Neon'), agent_ui('Phoenix'), agent_ui('Raze'), agent_ui('Reyna'), agent_ui('Yoru')
    with ui.column():
        class_column('Initiator')
        agent_ui('Breach'), agent_ui('Fade'), agent_ui('Gekko'), agent_ui('KAYO'), agent_ui('Skye'), agent_ui('Sova')
    with ui.column():
        class_column('Controller')
        agent_ui('Astra'), agent_ui('Brimstone'), agent_ui('Harbor'), agent_ui('Omen'), agent_ui('Viper')
    with ui.column():
        class_column('Sentinel')
        agent_ui('Chamber'), agent_ui('Cypher'), agent_ui('Deadlock'), agent_ui('Killjoy'), agent_ui('Sage')

    with ui.column():
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
            container = ui.column()

dark = ui.dark_mode()
dark.enable()
ui.switch(text='Dark Mode', value=True, on_change=lambda: dark.toggle())

ui.link('GitHub', 'https://github.com/hdg630/valorant-agent-randomizer')

# COMMENT AS NEEDED: Buttons to display the lists (in terminal)
# ui.button('Print Master List', on_click=lambda: print(master_list))
# ui.button('Print Temporary List', on_click=lambda: print(temp_list))

ui.run(title='Valorant agent randomizer', reload=False)
