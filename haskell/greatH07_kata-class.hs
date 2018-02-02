data Bool = False | True
data Shape = Circle Float Float Float | Rectangle Float Float Float Float

data Point = Point Float Float deriving(Show)
data Shape = Circle Point Float | Rectangle Point Point

-- greatH06を参照 座標をPointで定義したのでこのようにかける
area :: Shape -> Float
area (Circle _ r) = pi * r ^ 2
area (Rectangle (Point x1 y1) (Point x2 y2)) = (abs $ x2 - x1) * (abs $ y2 - y1)
-- コンストラクタはパターンマッチに使える フィールドを名前に束縛すればOK

-- ghci> Circle 10 20 5
-- 上記は実行できない　なぜならCircleがShow型クラスに所属していないから
data Shape = Circle Point Float | Rectangle Point Point deriving(Show)

data Point = Point Float Float deriving(Show)
data Shape = Circle Point Float | Rectangle Point Point deriving(Show)

data Person = Person { 	firstName :: String
					,	lastName :: String
					,	age :: Int
					,	height :: Float
					,	phoneNumber :: String
					,	flavor :: String } deriving (Show)

data Vector a = Vector a a a deriving (Show)
-- Vector Int とすれば　ベクトル座標をInt型で受け取るVector Int型が作れる

data Day = Sunday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday deriving (Eq, Ord, Enum, Bounded, Show, Read)
data Either a b = Left a | Right b deriving (Eq, Ord, Read, Show)

data Tree a = EmptyTree | Node a (Tree a) (Tree a) deriving (Show)
singleton :: a -> Tree a
singleton x = Node x EmptyTree EmptyTree
treeInsert :: (Ord a) => a -> Tree a -> Tree a
treeInsert x (Node a left right)
  | x == a = Node x left right
  | x <  a = Node a (treeInsert x left) right
  | x >  a = Node a left (treeInsert)