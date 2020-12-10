
import sys
import os
import fileinput

PROJECT = 'project_name'
SL = '/'
# virtual environment
PROJECT_SRC = f'{ PROJECT }{ SL }src{ SL }'

# templates
TEMPLATES = f'{ PROJECT_SRC }templates{ SL }'

D = '"'
URL_STYLES_MAIN = "href=" + D + "{{ url_for('static', filename='styles/main.css') }}" + D # print(URL_STYLES_MAIN)
URL_JS_MAIN = "src=" + D + "{{ url_for('static', filename='js/main.js') }}" + D # print(URL_JS_MAIN)

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

print(basehtml)
