

hello:
	@echo "hello"

run:
	@source .venv/bin/activate; python AOC/app.py $(day)


requirements:
	@poetry export \
	--format requirements.txt \
	--output requirements.txt \
	--without-hashes
