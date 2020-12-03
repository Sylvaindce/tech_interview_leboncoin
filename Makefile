PYTHON    =	python3

PYTEST    = pytest

SRC       = src/map_solver

MAIN_PROG = find_square.py

EXE_NAME  = find_square


all:		$(EXE_NAME)

$(EXE_NAME):	
			@ln -s $(SRC)/$(MAIN_PROG) ./$(EXE_NAME)
			@chmod +x ./$(EXE_NAME)

run:		
			$(PYTHON) $(SRC)/$(MAIN_PROG)

py-test:	
			PYTHONPATH=$(SRC) $(PYTEST)

test:		py-test

clean-pyc:
			@find . -name "*.pyc" -exec rm -f {} +
			@find . -name "*.pyo" -exec rm -f {} +
			@find . -name ".pytest_cache" -exec rm -rf {} +
			@find . -name "__pycache__" -exec rm -rf {} +

clean:		clean-pyc

fclean:		clean
			@rm ./$(EXE_NAME)

re:			fclean all

.PHONY: 	all run test clean fclean re