import Text.ParserCombinators.Parsec
import Text.ParserCombinators.Parsec.Expr
import Text.ParserCombinators.Parsec.Language
import qualified Text.ParserCombinators.Parsec.Token as P

lexer :: P.TokenParser ()
lexer = P.makeTokenParser (haskellDef { reservedOpNames = ["ATTACK", "DRAW", "NEGOTIATION", "BUILD"]
 })

natural     = P.natural lexer
parens      = P.parens lexer
reservedOp  = P.reservedOp lexer

expr :: Parser Integer
expr = buildExpressionParser table term <?> "expression"
  where
    table =  [[binop "ATTACK" (*) AssocLeft, binop "DRAW" div AssocLeft,
             binop "NEGOTIATION" (+) AssocLeft, binop "BUILD" (-) AssocLeft]]
    binop s op assoc = Infix (do{ reservedOp s; return op } <?> "operator") assoc
    unary s op = Prefix (do{ reservedOp s; return op })

term :: Parser Integer
term =
  do {
    parens expr;
  } <|> do {
    n <- natural;
    return n
  } <?>
    "term"

stmt :: Parser Integer
stmt = do
  e <- expr
  eof
  return e

main = do
  print $ parse stmt "" "ATTACK 1"