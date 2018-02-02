-- main =
--   print "abc" >>= \_ ->
--   print "edf" >>= \_ ->
--   print "ghi" >>= \_ ->
--   print "jkl" >>= \_ ->
--   print "mno"

import Control.Monad
import System.Random
import Data.IORef

dice :: IO Int
dice = getStdRandom $ randomR(1,6)

main = do
  -- a <- newIORef =<< ( getStdRandom $ randomR (0, 9) :: IO Int)
  -- a' <- readIORef a
  -- writeIORef a (a' + 1)
  -- print =<< readIORef a
  print $ replicate 5 1
  print =<< replicateM 5 (return 1)
  print =<< replicateM 5 dice