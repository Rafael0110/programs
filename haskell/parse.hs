import System.Random
import Data.Map
import Data.List

hand = []
talon = shuffle [(color,num) | color <- ["black","white"], num <- [0..11]]

-- draw place num = 

shuffle [] = return []
shuffle xs = do
    n <- getStdRandom $ randomR (0, length xs - 1) :: IO Int
    xs' <- shuffle $ take n xs ++ drop (n + 1) xs
    return $ (xs !! n) : xs'
-- draw place num
--   | num == 0 = print hand
--   | num > 0 = do
--       (:) (head . shuffle place) hand
--       draw place (num - 1)
-- main = do
--   draw talon 3