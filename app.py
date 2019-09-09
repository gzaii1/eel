import eel

# from test import my_python_function
eel.init('web')
web_app_options = {
    'mode':'chrome-app',#or 'chrome'
    'port':8090,
    'chromeFlags':["--start-fullscreen"]
}

@eel.expose
def my_python_function(a,b):
    print(a,b,a + b)

eel.start('main.html',options=web_app_options)
