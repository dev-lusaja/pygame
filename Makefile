.PHONY: soccer snake breakout

venv-create:
	python3 -m venv venv

venv-install-libs:
	venv/bin/pip3.6 install -r requirements.txt

soccer:
	venv/bin/python3 soccer/main.py

snake:
	venv/bin/python3 snake/main.py

breakout:
	venv/bin/python3 breakout/main.py