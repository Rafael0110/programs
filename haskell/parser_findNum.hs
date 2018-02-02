import Text.ParserCombinators.Parsec

number :: Parser Integer
number = do ds <- many1 digit
            return (read ds)

run :: String -> String
run input = case parse number "Test" input of
				    Left   err -> show err
				    Right  val -> show val