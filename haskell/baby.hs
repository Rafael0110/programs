import Data.Char
import Debug.Trace

--removeNonUppercase :: [Char] -> [Char]
--removeNonUppercase st = [ c | c <-st, c `elme` ['A'..'Z']]

addThree :: Int -> Int -> Int -> Int
addThree x y z = x + y+ z

factorial :: Integer -> Integer
factorial n = product [1..n]

circumference :: Float -> Float
circumference r = 2 * pi * r

circumference' :: Double -> Double
circumference' r = 2 * pi * r

fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

fib' :: Int -> Int
fib' n
	| n == 0 = 0
	| n == 1 = 1
	| n > 1 = fib (n-1) + fib (n-2)

fact :: Int -> Int
fact n
	| n == 0 = 1
	| otherwise = n * fact (n-1)

fact' :: Int -> Int
fact' 0 = 1
fact' n
	| n > 0 = n * fact' (n-1)
	| otherwise = 0

first (x:_) = x

length' [] = 0
length' (_:xs) = 1 + length' xs

sum' :: Num t => [t] -> t
sum' [] = 0
sum' (x:xs) = x + sum' xs

product' [] = 1
product' (x:xs) = x * product' xs

take' _ [] = []
take' n _  | n < 1 = []
take' n (x:xs) = x : take' (n-1) xs

drop' 1 (_:xs) = xs
drop' n (_:xs) = drop' (n-1) xs

reverse' [] = []
reverse' (x:xs) = reverse' xs ++ [x]

--rot13 [] = []
--rot13 (x:xs)
--	| ord 'Z' < ord x + 13 < ord 'a' = chr(mod(ord x + 13 ord 'Z') + ord 'A') ++ rot13 xs
--	| ord 'z' < ord x + 13			 = chr(mod(ord x + 13 ord 'z') + ord 'a') ++ rot13 xs
--	| otherwise = chr(ord x + 13)  ++ rot13 xs