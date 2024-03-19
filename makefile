init:
	@python3 -m flask db init
	@python3 -m flask db migrate
	@python3 -m flask db upgrade
server:
	@python3 -m flask run --debug