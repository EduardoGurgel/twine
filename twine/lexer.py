from typing import Iterable
from lark import Token
from .grammar import GRAMMAR

def lex(src: str) -> Iterable[Token]:
    """
    Analiza o código fonte e retorna uma sequência de tokens.
    """
    return GRAMMAR.lex(src)


    #yield Token("IDENTIFIER", "main")
    #yield Token("EQUAL", "=")
    #yield Token("F", "f")
    #yield Token("LPAR", "(")
    #yield Token("RETURNS", "returns")
    #yield Token("IDENTIFIER", "integer")
    #yield Token("RPAR", ")")
    #yield Token("INTEGER", "42") 
