import Data.List
-- ghci> :m Data.List
import Data.List (nub, sort)
-- nubとsortだけどimport
import Data.List hiding (nub)
-- nub以外をimport
import gualified Data.Map
-- gualified（修飾付きインポート）
-- 名前の被った関数があれば Data.Map.filter というように記述
import gualified Data.Map as M
-- 名前の被った関数があれば M.filter というように記述

import Data.List
nub -- リストの重複を削除
words -- 文字列を空白区切でリスト化
group -- リストの隣接する同じ値をまとめる
sort -- 言わずもがなソート関数
tails -- tailを再帰的に適用
isPrefixOf -- あるリストがあるリストの前にあるかを判定
find -- リストの中に対象があるかないかをMaybe型で返す

import Data.Char
ord -- コード化
chr -- 文字化
digitToInt -- 16進数にも対応

wordNums = map (\ws -> (head ws, length ws)) . group . sort . words
needle `isIn` haystack = any (needle `isPrefixOf`) (tails haystack)
encode offset msg = map (\c -> chr $ ord c + offset) msg
decode shift msg = encode (negate shift) msg -- negate x = (-x)
digitSum = sum . map digitToInt . show
firstTo n = find (\x -> digitSum x == n) [1..]
string2digits = map digitToInt . filter isDigit