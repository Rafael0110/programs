import System.Environment
import System.Process
main = do
  args <- getArgs
  -- wait . head $ args
  runCommand $ head $ args
  line <- getLine
  print line

wait = (>>= waitForProcess) . runCommand