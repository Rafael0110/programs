import Data.Char
import Control.Exception

parseTest p s = do
    print $ fst $ p s
    `catch` \(SomeException e) ->
        putStr $ show e

anyChar   (x:xs)       = (x, xs)
satisfy f (x:xs) | f x = (x, xs)

char c = satisfy (== c)         -- 追加
digit  = satisfy isDigit        -- 追加
letter = satisfy isLetter       -- 追加

main = do
    parseTest (char 'a') "abc"  -- OK
    parseTest (char 'a') "123"  -- NG
    parseTest digit  "abc"      -- NG
    parseTest digit  "123"      -- OK
    parseTest letter "abc"      -- OK
    parseTest letter "123"      -- NG