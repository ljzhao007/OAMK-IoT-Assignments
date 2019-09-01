# Week 1 - Python tools for Data Analysis

***Note**: I had installed Python 3 before checking these exercises and troubleshooting problems with WSL took a very long time so I attached the `-V` commands.*

```bash
$ python3 -V
Python 3.6.8

$ pip3 -V
pip 19.2.3 from /home/arpad/.local/lib/python3.6/site-packages/pip (python 3.6)

$ pipenv --version
pipenv, version 2018.11.26
```
```
$ pipenv install numpy

Installing numpy…
Adding numpy to Pipfile's [packages]…
✔ Installation Succeeded
Installing dependencies from Pipfile.lock (a5c2a6)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 2/2 — 00:00:01
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.


$ pipenv install scipy

Installing scipy…
Adding scipy to Pipfile's [packages]…
✔ Installation Succeeded
Installing dependencies from Pipfile.lock (a5c2a6)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 2/2 — 00:00:01
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run


$ pipenv install pandas

Installing pandas…
Adding pandas to Pipfile's [packages]…
✔ Installation Succeeded
Pipfile.lock (fb81dd) out of date, updating to (a5c2a6)…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
✔ Success!
Updated Pipfile.lock (fb81dd)!
Installing dependencies from Pipfile.lock (fb81dd)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 6/6 — 00:00:02
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.


$ pipenv install scikit-learn

Installing scikit-learn…
Adding scikit-learn to Pipfile's [packages]…
✔ Installation Succeeded
Pipfile.lock (0628d8) out of date, updating to (fb81dd)…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
✔ Success!
Updated Pipfile.lock (0628d8)!
Installing dependencies from Pipfile.lock (0628d8)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 8/8 — 00:00:03
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```