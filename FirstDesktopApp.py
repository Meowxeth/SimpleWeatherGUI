import PySimpleGUI as sg
from getWeather import CheckWeather as cw

sg.theme("DarkTeal1")
layout = [
    [sg.Text("Location Unknown.", key='WeatherLocation')],
    [sg.Text(size=(50, 5), key='weather_status')],
    [sg.Text("Type in the location"), sg.Input(key='UserInput')],
    [sg.Text(size=(50, 1), key='-OUTPUT-')],
    [sg.Button('Search'), sg.Button('Quit')]
]

window = sg.Window('Weather Report', layout)


while True:
    event, values = window.read()
    if event in [sg.WIN_CLOSED, 'Exit']:
        break
    if event == 'Search':
        test = cw(0, '', '', values['UserInput'])
        test.makeUrl()
        if test.callAPI() == False:
            window['WeatherLocation'].update('Invalid City')
            window['-OUTPUT-'].update('Try typing in a city.')

        else:
            returned_data = test.showStats()
            window['WeatherLocation'].update(values['UserInput'])
            window['weather_status'].update('Temperature: ' +
                                            str(returned_data[0]) +
                                            ' C\n' + 'Humidity: '
                                            + str(returned_data[1]) + '%\n' + 'Feels like: '
                                            + str(returned_data[2]) + ' C')
            window['-OUTPUT-'].update('Showing the weather for ' + values['UserInput'] +
                                      "! Thanks for trying my weather app")

window.close()
