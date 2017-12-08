
default :
	python3 github_token/main.py

tests :
	python3 -m unittest discover

clean :
	rm -f test.txt

