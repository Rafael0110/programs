#!/usr/bin/env python
#coding: utf-8

# --- 整数ループ ---
for i in xrange(6):
  print i
# xrangeはrangeと違い一気にメモリを確保しない
# python3ではrangeがxrangeと同様の動作

# --- コレクションのループ
colors = ['red', 'green', 'blue', 'yellow']
for color in colors:
  print color
# forでは単数系と複数形を使うことで，何をループしているかわかりやすい

# --- 逆順ループ ---
colors = ['red', 'green', 'blue', 'yellow']
for color in reversed(colors):
  print colors
# reversedはlistにのみ対応

# --- コレクションと要素番号のループ ---
colors = ['red', 'green', 'blue', 'yellow']
for i, color in enumerate(colors):
  print i, '-->', color
# enumerateで要素番号がとれる

# --- 複数のコレクションを同時にループ
for name, color in zip(names, colors):
  print name, '-->', color
# itertoolsモジュールのizipがメモリに対しても優しい
# python3ではzipがizipに相当
# itertoolsは便利な関数が豊富（combinationsやproduct）

# --- 複数のループ終了条件
def find(seq, tgt):
  for i, value in enumerate(seq):
    if value == tgt:
      break
  else:
    return -1
  return i
# forが最後まで実行されたときelseへ飛ぶ

# --- keyとvalueでのループ
for k, v in d.iteritems():
  print k, '-->', v
# itemsでもバリューはとれるが，要素数がでかい場合はメモリを使う
# 基本的にtupleで取り出される

# --- anyとall
if all(x < 10 for x in l):
    print("All numbers are less than 10")
if any(x >= 10 for x in l):
    print("All numbers are less than 10")
# flag使ってループ回す必要なし


# --- ペアから辞書の作成
names = ['raymond', 'rachel', 'mattew']
colors = ['red', 'green', 'blue']
d = dict(izip(names, colors))
# キーとバリューの候補が既にリストに存在する場合はzipする

# --- 内包表記でdictをいじる
d = {k : d[k] for k in d if not k.startswith('r')}
# こういうのもありだよね

# --- 辞書によるカウント
colors = ['red', 'green', 'red', 'blue', 'green', 'red']
d = {}
for color in colors:
  d[color] = d.get(color, 0) + 1
# 辞書objectのgetを使うと，keyがないとき渡した値をvalueでセットしてくれる
d = defaultdict(int)
for color in colors:
    d[color] += 1
# defaultdictで登録されてないkeyが呼び出されると自動で登録をする

# --- collections 
import collections
dict = collections.defaultdict(int)
dict["a"] += 1
print dict
# 先に型を指定できる

# --- collections module の Counter
from collections import Counter
c = Counter([1,1,2,3,3,4])
print(dict(c))
print(c.most_common(2))
# Counterはiterableなものの要素の数を数える
# できたものはkeyに要素，valueに数が入る
# most_common(n)で再頻出の要素からn個を取り出す

# --- 辞書によるグルーピング
names = ['raymond', 'rachel', 'matthew', 'ronger', 'betty', 'melissa', 'judith', 'charlie']
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
# 辞書のvalueをlistにするとき
# int同様にlistは空リストを返す

# --- 辞書でpop ---
while d:
  key, value = d.popitem()
  print key, '-->', value

# --- 展開して代入 ---
def fibonacci(n):
  x, y = 0, 1
  for i in range(n):
    print x
    x, y = y, x+y
# x,yへの代入が同時に行われる

# --- 内包表記で二重ループ ---
[inner for outer in init for inner in outer]
# 左から順に処理を読んで，頭にくるものがリストに格納されるもの

# --- キーワード引数
twitter_search('@obama', retweets=False, numtweets=20, popular=True)
# 関数の定義を確認しなくても何を設定しているのか丸分かり

# --- 名前付きタプル
Point = namedtuple('Point3d', 'x y z')
point = Point(10,20,30)
>>> point
Point3d(x=10, y=20, z=30)
>>> print point.x, point.y, point.z
10 20 30
>>> print point[0], point[1], point[2]
10 20 30
# tupleの振る舞いに加え，objectのように参照が可能　構造体っぽい

# --- 一括代入
def fibonacci(n):
  x, y = 0, 1
  for i in range(n):
    print x
    x, y = y, x+y
# 一時変数をなくせる
# x,yは同時に代入されているので問題無し
x, y, dx, dy = ( x + dx * t,
                 y + dy * t,
                 influence(m, x, y, dx, dy, partial='x'),
                 influence(m, x, y, dx, dy, partial='y'))
# 極論，こんな代入も大いにアリ

# --- sortにオプションを
dict = {"a":1,"b":2,"c":1}
print sorted(dict.items(),key=lambda x:x[1],reverse=True)
# keyで指定したものをソートする

# --- Python公式ドキュメントによるそーと
from operator import itemgetter, attrgetter
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

print(sorted(student_tuples, key=itemgetter(2))) # ==> [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
print(sorted(student_objects, key=attrgetter('age'))) # ==> [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
# gradeでソートしてさらにageでソートする場合
print(sorted(student_tuples, key=itemgetter(1,2))) # ==> [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
print(sorted(student_objects, key=attrgetter('grade', 'age'))) # ==> 上と一緒
















