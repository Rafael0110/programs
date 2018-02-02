module Many where
import Text.Parsec
import Control.Applicative ((<$>), (*>), (<*), (<*>))
import Control.Monad
import Data.Char

testMany = join <$> (many1 pWord <* spaces <* optional (string "A+" *> spaces) <* eof)

pWord = join <$> (many1 $ try pABAC) -- try を追加

pABAC = spaces *> (try (string "AB") <|> try (string "AC"))

main = do
  parseTest testMany "ABAC AB A+ "