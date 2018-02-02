-- Haskell 代数的データ型 超入門

-- 列挙型 (enum)
data Color1 = Blue1 | Red1 | Green1 | White1 deriving Show
  -- 小文字で始めてはいけない
  -- 変数・関数が小文字で始まるのと対になる
  -- deriving Show を最後尾につけることでprint可能

data Color2 = Blue2 | Red2 | Green2 | White2 deriving (Show,Enum)
  -- 型クラス(Enum)を指定すれば数値と相互変換が可能に
  -- fromEnum  列挙型→数値  0始まり
  -- toEnum    数値→列挙型  ::で変換する型を指定，範囲外はエラー

-- 真偽値を表すBoolは標準ライブラリPreludeで定義された列挙型
data Bool = False | True deriving (Eq, Ord, Enum, Read, Show, Bounded)
  -- Eq      : ==や/=で比較可能
  -- Ord     : 順番を持つ，<や>で大小比較可能
  -- Read    : 文字列から変換可能
  -- Bounded : 最小値と最大値をもつ

-- 直積型
data Point = Point Int Int deriving Show
offset (Point x1 y1) (Point x2 y2) = Point (x1 + x2) (y1 + y2)

main = do
  -- 列挙型
  -- print Blue1
  -- print $ fromEnum Blue2
  -- print $ fromEnum Red2
  -- print $ fromEnum Green2
  -- print $ fromEnum White2
  -- print (toEnum 0 :: Color2)
  -- print (toEnum 1 :: Color2)
  -- print (toEnum 2 :: Color2)
  -- print (toEnum 3 :: Color2)

  -- 直積型
  let a = Point 2 3
      b = Point 1 1
      c = offset a b
  print c