
default :
	python3 main.py

test :
	python3 -m unittest tests/test_github_token.py

clean :
	rm -f test.txt

