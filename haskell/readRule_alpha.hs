import Text.Parsec
import Control.Applicative ((<$>), (<*>), (<*), (*>))

testtest = (+)

eval m fs = foldl (\x f -> f x) <$> m <*> fs
apply f m = flip f <$> m

-- expr = term, {("+", term) | ("-", term)}
expr = eval term $ many $
        char '+' *> apply (testtest) term
    <|> char '-' *> apply (-) term

-- term = factor, {("*", factor) | ("/", factor)}
term = eval factor $ many $
        char '*' *> apply (*) factor
    <|> char '/' *> apply div factor

-- factor = [spaces], ("(", expr, ")") | number, [spaces]
factor = spaces
      *> (char '(' *> expr <* char ')' <|> number)
     <*  spaces

number = read <$> many1 digit

main = do
    parseTest expr "1 + 2"