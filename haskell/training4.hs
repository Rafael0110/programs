main = do

  let f g = g 2 3
  print $ (\g -> g 1 2) $ (\x -> \y -> x + y)
  print $ f (\x -> \y -> x + y) -- add
  print $ f (\x -> \y -> x * y) -- mul


  let add   x y = x + y
  let add'  x = \y -> x + y
  let add'' = \x -> \y -> x + y
  -- 引数を１つずつ分割して関数をネスとさせることをカリー化という
  -- Haskellでは複数の引数を取る関数は自動的にカリー化される
  print $ add   2 3
  print $ add'  2 3
  print $ add'' 2 3

  let add2 = add 2
  print $ add2 3
  print $ (add 2) 3
  print $ add 2 3
  -- 部分適用は一部の引数を固定化して新しい関数を作り出す考え
  -- カリー化されるから利用できるが，カリー化とは別物

  print $ f (+)
  print $ f (*)
  -- 演算子を関数化することで高階関数に渡すことができる

  let f xs g = [g x | x <- xs]
  print $ f [1..5] $ (*) 2

  let f g = g 5
  print $ f $ (-) 2

  print [f $ \x -> 2 + x, f (2 +)]
  print [f $ \x -> x + 2, f (+ 2)]
  print [f $ \x -> 2 - x, f (2 -)]
  print [f $ \x -> x - 2, f (+(-2)), f $ subtract 2]

  print [f (2 `div`), f (`div` 2)]

  _ <- print "hello"
  return ()
  a <- print "hello"
  print a