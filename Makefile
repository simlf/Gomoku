##
## EPITECH PROJECT, 2022
## louis.maestre@epitech.eu
## File description:
## Makefile
##

SRC = 	src/main.py

NAME	=	pbrain-gomoku-ai

$(NAME):
		@cp -rf $(SRC) $@
		@chmod +x $(NAME) $@

clean:
	rm -f $(NAME)

fclean:	clean

all: $(NAME)

re: fclean all
