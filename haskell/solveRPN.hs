solveRPN :: String -> Double
solveRPN = head . foldl calc [] . words
  where calc (x:y:ys) "*" = (y * x):ys
        calc (x:y:ys) "+" = (y + x):ys
        calc (x:y:ys) "-" = (y - x):ys
        calc (x:y:ys) "/" = (y / x):ys
        calc (x:y:ys) "^" = (y ** x):ys
        calc (x:xs) "ln" = log x:xs
        calc xs "sum" = [sum xs]
        calc xs numberString = read numberString:xs