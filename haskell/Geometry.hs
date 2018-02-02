-- 幾何学モジュール
module Geometry
( sphereVolume
, sphereArea
, cubeVolume
, cubeArea
, cubidArea
, cuboidVolume
) where

sphereVolume :: Float -> Float
sphereVolume radius = (4.0 / 3.0) * pi * (radius ^ 3)

sphereArea :: Float -> Float
sphereArea radius = 4 * pi * (radius ^ 2)

cubeVolume :: Float -> Float
cubeVolume side = cuboidVolume side side side

cubeArea :: Float -> Float
cubeArea side = cubeidArea side side side

cuboidVolume  :: Float -> Float -> Float -> Float
cuboidVolume a b c = rectArea a b * c

cubidArea :: Float -> Float -> Float -> Float
cubidArea a b c = rectArea a b * 2 + rectArea a c * 2 + rectArea c b * 2

rectArea :: Float -> Float -> Float
rectArea a b = a * b

-- エクスポートしてないrectAreaはモジュールをインポートしても利用されない
-- Geometryをインポートするには，同じディレクトリにある状態でimportを行う必要がある