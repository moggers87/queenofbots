.PHONY: serve
serve:
	FLASK_APP=queenofbots FLASK_ENV=development flask run

.PHONY: worker
worker:
	rq worker
