-- Haskell アクション 超入門
import System.Random

-- 参照透過性
add x y = x + y
  -- 同じ引数には常に同じ値を返す
  -- Haskellでは参照透過性のない関数は定義不可
  -- 関数内部の状態が変化することを副作用と呼び，参照透過性と対立する

-- アクション
  -- 副作用が扱えないと困ることもある
  -- 乱数を返すような関数は，関数と区別して"アクション"と呼ぶ
  -- 関数に限らず，時刻取得やファイル読み込みなど副作用が正日ものはすべてアクションを用いる

randAlpha = getStdRandom $ randomR ('A','Z')

dice :: IO Int
dice = getStdRandom $ randomR (1, 6)

main = do
  -- print $ add 1 2

  -- r <- randAlpha
  -- print r
    -- アクションから値を取り出すには <- を使用する
    -- <- はdoブロックの中でしか使えない

  -- randAlpha >>= print
  -- print =<< randAlpha
    -- アクションから値を取り出して関数に渡すには =<< を使用する
    -- 漏斗のようなもので，アクションから関数に値をドリップしているイメージ
    -- アクション版の $ だと思えば良い

  print =<< dice
  print =<< dice
  print =<< dice