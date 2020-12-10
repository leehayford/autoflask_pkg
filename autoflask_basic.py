# # _autoflask_basic_
#
# #### What it do :
# - creates a near-blank, one-page, **flask web app** in `~/your_projects_directory/your_project_name`, hence forth writen as: _~/../_
# - creates and activates a **virtual environment**
#     - installs **flask** and dependencies
#     - creates **~/../src/** and therein creates and edits:
#         - _~/../src/templates/base.html_
#         - _~/../src/templates/home.html_
#         - _~/../src/templates/data.html_
#         - _~/../src/static/styles/main.css_
#         - _~/../src/static/js/main.js_
#         - _~/../src/static/media/_
#         - _~/../src/app.py_ `FLASK_APP=app.py`
#         - _~/../src/sum_app.py_
#         - _~/../src/requirements.txt_ `~/$ pip freeze > requirements.txt`
#         - _~/../src/.git/_ `~/$ git commit -m 'your_project_name bones'`
#
# ---
#
# #### How to do :
#
# 1. Clone this repo into _~/your_projects_directory/_
#
# 2. `~/$ cd your_projects_directory`
#
# 3. `~/$ python autoflask_basic.py your_project_name`
#
# 4. Autoflask makes the files described above
#
# 5. `~/$ cd your_project_name/src`
#
# 6. `~/../src/$ export FLASK_APP=app.py` (win `~/> set FLASK_APP=app.py`)
#
# 7. `~/../src/$ export FLASK_DEBUG=1` (win `~/> set FLASK_DEBUG=1`)
#
# 8. `~/src/$ flask run`
#
# ### result ###
#      * Serving Flask app "app.py"
#      * Environment: production
#        WARNING: This is a development server. Do not use it in a production deployment.
#        Use a production WSGI server instead.
#      * Debug mode: on
#      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
#      * Restarting with stat
#      * Debugger is active!
#      * Debugger PIN: xxx-xxx-xxx
#
# 9. Go to **localhost:5000 / home** to see your empty home page.
#   - _~/../src/templates/home.html_\
#   - _~/../src/templates/data.html_\
#    are presented in a block, in the body of\
#   _~/../src/templates/base.html_;\
#  all of those files need `your_attention`.
#   - _~/../src/static/css/main.css_\
#   is styling those html files... nearly... `your_attention(main.css).also`.
#
# 10. Check out **localhost:5000 / data**\
#     this is here to remind me to add in the stuff for a database
#
# 11. Open _~/.../_ in a code editor and make stuff happen avec the html, css, js, and py.
# Allons-y!
#

import sys
import os
import fileinput

os.system( f'clear' )

# set constants according to platform
SL = ''
MAKE_FILE = ''
PROJECT = str(sys.argv[1]) # project_name
START_CHROME = ''
if(sys.platform == 'win32'):
    SL = '\\'
    MAKE_FILE = f'type nul >'
    ACTIVATE_VENV = f'{ PROJECT }{ SL }scripts{ SL }activate_this.py'
    START_CHROME = f'start chrome 127.0.0.1:5000'

elif(sys.platform == 'linux'):
    SL = '/'
    MAKE_FILE = f'touch'
    ACTIVATE_VENV = f'{ PROJECT }{ SL }bin{ SL }activate_this.py'
    START_CHROME = f'start chrome localhost:5000'

# virtual environment
PROJECT_SRC = f'{ PROJECT }{ SL }src{ SL }'

# templates
TEMPLATES = f'{ PROJECT_SRC }templates{ SL }'

# static
STATIC = f'{ PROJECT_SRC }static{ SL }'
STYLES = f'{ STATIC }styles{ SL }'
JS = f'{ STATIC }js{ SL }'
MEDIA = f'{ STATIC }media{ SL }'
D = '"'
URL_STYLES_MAIN = "href=" + D + "{{ url_for('static', filename='styles/main.css') }}" + D # print(URL_STYLES_MAIN)
URL_JS_MAIN = "src=" + D + "{{ url_for('static', filename='js/main.js') }}" + D # print(URL_JS_MAIN)


os.system( f'virtualenv { PROJECT }' )

# activate virtual environment
with open(ACTIVATE_VENV) as f:
    code = compile(f.read(), ACTIVATE_VENV, 'exec')
    exec(code, dict(__file__=ACTIVATE_VENV))

    print(f'project: { PROJECT }')

    os.system( f'pip install flask')

    os.system( f'mkdir { PROJECT_SRC }')

# create html templates
    os.system( f'mkdir { TEMPLATES }')

    #edit { TEMPLATES }base.html

    basehtml ='<!doctype html>\n'
    basehtml +='<html  lang="en">\n'
    basehtml +='\t\t<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">\n'
    basehtml +='\t<head>\n'
    basehtml +='\t\t<meta charset="UTF-8">\n'
    basehtml +='\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    basehtml +='\t\t<meta http-equiv="X-UACompatible" content="ie=edge">\n'
    basehtml +='\t\t{% if title %}\n'
    basehtml +=f'\t\t\t<title>{ PROJECT }' + ' - {{ title }}</title>\n'
    basehtml +='\t\t{% else %}\n'
    basehtml +=f'\t\t\t<title>{ PROJECT }</title>\n'
    basehtml +='\t\t{% endif %}\n'
    basehtml +='\t\t<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">\n'
    basehtml +=f'\t\t<link rel="stylesheet" type="text/css" { URL_STYLES_MAIN } >\n'
    basehtml +='\t\t<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>\n'
    basehtml +=f'\t\t<script type="text/javascript" { URL_JS_MAIN } ></script>\n'
    basehtml +='\t</head>\n'
    basehtml +='\t<body>\n'
    basehtml +=f'\t\t<header id="base-header"><div>{ TEMPLATES } base.html header - { sys.platform }</div></header>\n'
    basehtml +='\t\t{% block content %}{% endblock content %}\n'
    basehtml +=f'\t\t<footer id="base-footer"><div>{ TEMPLATES } base.html footer - { sys.platform }</div></footer>\n'
    basehtml +='\t</body>\n'
    basehtml +='</html>\n'
    with open( f'{ TEMPLATES }base.html', "a") as b:
        b.write(basehtml)

    #edit { TEMPLATES }home.html"
    homehtml ='{% extends "base.html" %}\n'
    homehtml +='{% block content %}\n'
    homehtml +=f'\t<div id=app-home>{ TEMPLATES }home.html content</div>\n'
    homehtml +='{% endblock content %}\n'
    with open(f'{ TEMPLATES }home.html', "a") as h:
        h.write(homehtml)

    #edit { TEMPLATES }data.html"
    datahtml ='{% extends "base.html" %}\n'
    datahtml +='{% block content %}\n'
    datahtml +=f'\t<div id=app-data>{ TEMPLATES }data.html content</div>\n'
    datahtml += '\t{% for thing in stuff %}\n'
    datahtml += '\t\t<h2>{{ thing.name }}</h2>\n'
    datahtml += '\t\t<p>{{ thing.thing }}</p>\n'
    datahtml += '\t{% endfor %}\n'
    datahtml +='{% endblock content %}\n'
    with open(f'{ TEMPLATES }data.html', "a") as h:
        h.write(datahtml)

# create static/styles, static/js, static/media
    os.system( f'mkdir { STATIC }')

    maincss ='* { \nmargin: 0px;\npadding: 0px;\nbox-sizing: border-box;\nfont-family: Roboto;\n--red: rgb(180, 0, 0);\n--green: rgb(0, 180, 0);\n--blue: rgb(0, 0, 180);\n--shite: rgb(180, 180, 0);\n }\n'
    maincss +='#base-header { \ncolor: var(--red); \n}\n'
    maincss +='#base-footer { \ncolor: var(--green); \n}\n'
    maincss +='#app-home { \ncolor: var(--blue); \n}\n'
    maincss +='#app-data { \ncolor: var(--shite); \n}\n'
    os.system( f'mkdir { STYLES }')
    with open(f'{ STYLES }main.css', "a") as h:
        h.write(maincss)

    os.system( f'mkdir { JS }')
    with open(f'{ JS }main.js', "a") as h:
        h.write(f'console.log("Ready")')

    os.system( f'mkdir { MEDIA }')

# create app.py, sum_app.py
    apppy = 'from flask import Flask, render_template\n'
    apppy += 'from datetime import timedelta\n'
    apppy += 'from sum_app import sum\n'
    apppy += 'app = Flask(__name__)\n'
    apppy += 'app.config["SEND_FILE_MAX_AGE_DEFAULT"] = timedelta(seconds=1)\n'
    apppy += 'stuff = [\n'
    apppy += '\t{ "name": "jeff", "thing": "sum du things du jeff:" + str(sum(3, 7)) },\n'
    apppy += '\t{ "name": "steve", "thing": "sum du things du steve:" + str(sum(5, 8)) },\n'
    apppy += '\t{ "name": "alan", "thing": "sum du things du alan:" + str(sum(2, 3)) }\n'
    apppy += ']\n'
    apppy += '@app.route("/")\n'
    apppy += '@app.route("/home")\n'
    apppy += 'def home():\n'
    apppy += '\treturn render_template("home.html", stuff=stuff, title="Home")\n'
    apppy += '@app.route("/data")\n'
    apppy += 'def data():\n'
    apppy += '\treturn render_template("data.html", stuff=stuff, title="Data")\n'
    with open(f'{ PROJECT_SRC }app.py', "a") as h:
        h.write(apppy)

    with open(f'{ PROJECT_SRC }sum_app.py', "a") as h:
        h.write(f'def sum(a, b): return a+b\n')

# create requirements file for deployment ...
    os.system(f'pip freeze > { PROJECT_SRC }requirements.txt')

# initiate git repository and commit
    os.system(f'cd { PROJECT_SRC }; git init')
    os.system(f'cd { PROJECT_SRC }; git config user.email "{ PROJECT }@autoflask_basic.com"')
    os.system(f'cd { PROJECT_SRC }; git config user.name "{ PROJECT }"')
    os.system(f'cd { PROJECT_SRC }; git add .')
    os.system(f'cd { PROJECT_SRC }; git commit -m "{ PROJECT } bones"')

# #slap ass
#     print(f'***\nproject directory:\n { os.getcwd() }{ SL }{ PROJECT }\n***\n')
#
#     # TODO: open common code editors...
#     #print(f'***\n< enter > to skip\n\t< a > to open in atom\n\t< v > to open vscode\n\t< s > to open in sublime\n***\n')
#     #if(input() == 'a'): os.system(f'atom  { PROJECT }')
#     #elif(input() == 'v'): os.system(f'code { PROJECT }')
#     #elif(input() == 's'): os.system(f'sub { PROJECT }')
#
    print(f'shall we run the server now? y/n:')
    if(input() == 'y'):

        #os.system( START_CHROME ) # TODO: open common browsers... add, test browser options...
        os.system(f'cd { PROJECT_SRC }; export FLASK_APP=app.py')
        os.system(f'cd { PROJECT_SRC }; export FLASK_DEBUG=1')
        os.system(f'cd { PROJECT_SRC }; flask run')
