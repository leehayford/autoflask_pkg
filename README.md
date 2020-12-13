# _autoflask_pkg_

#### What it do :
- creates a near-blank, one-page, **flask web app** in `~/your_projects_directory/your_project_name`, hence forth written as: **_~/../_**
- creates and activates a **virtual environment**
- installs **flask** and dependencies
- creates and edits:
    - _~/../src/templates/base.html_
    - _~/../src/templates/home.html_
    - _~/../src/templates/data.html_
    - _~/../src/static/styles/main.css_
    - _~/../src/static/js/main.js_
    - _~/../src/static/media/_
    - _~/../src/app.py_ `FLASK_APP=app.py`
    - _~/../src/sum_app.py_  
    - _~/../src/requirements.txt_ `~/$ pip freeze > requirements.txt`
    - _~/../src/.git/_ `~/$ git commit -m 'your_project_name bones'`

---

#### How to do :

1. Clone this repo into _~/your_projects_directory/_

2. `~/$ cd your_projects_directory`

3. `~/$ python autoflask_basic.py your_project_name`

4. Autoflask makes the files described above

5. `~/$ y` to fire it up and have a look.

    Or `~/$ n` to start it up later (see steps below):

        `~/$ cd your_project_name`\
        `~/$ source bin/activate` (win `~/> scripts\activate`)\
        `(env) ~/$ cd src`\
        `(env) ~/../src/$ export FLASK_APP=app.py` (win `~/> set FLASK_APP=app.py`)\
        `(env) ~/../src/$ export FLASK_DEBUG=1` (win `~/> set FLASK_DEBUG=1`)\
        `(env) ~/src/$ flask run`\

### result ###
     * Serving Flask app "app.py"
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: on
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: xxx-xxx-xxx

9. Go to **localhost:5000 / home** to see your empty home page.
  - _~/../src/templates/home.html_\
  - _~/../src/templates/data.html_\
   are presented in a block, in the body of\
  _~/../src/templates/base.html_;\
 all of those files need `your_attention`.
  - _~/../src/static/css/main.css_\
  is styling those html files... nearly... `your_attention(main.css).also`.

10. Check out **localhost:5000 / data**\
    this is here to remind me to add in the stuff for a database

11. Open _~/.../_ in a code editor and make stuff happen avec the html, css, js, and py.
Allons-y!     
