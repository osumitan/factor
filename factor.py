#!/usr/bin/python3
# factor.py
# 素因数分解

import sys
import math

# 因数クラス
class Factor:
	# コンストラクタ
	# @param num 因数
	def __init__(self, num):
		self.num = int(num)
		self.pow = 1

# 表示
# @param org 元の数値
# @param factors 因数リスト
def display(org, factors):
	slist = []
	# 因数でループ
	for i in range(len(factors)):
		f = factors[i]
		x = "x " if (i > 0) else ""
		h = "^" if (f.pow >= 2) else ""
		p = "{0:d}".format(f.pow) if (f.pow >= 2) else ""
		slist.append("{}{}{}{}".format(x, f.num, h, p))
	print("{0} = {1}".format(str(org), " ".join(slist)))

# 因数を追加
# @param num 因数
# @param factors 因数リスト
def append_factor(num, factors):
	for i in range(len(factors)):
		f = factors[i]
		# 因数がすでにあれば指数を追加
		if f.num == num:
			f.pow += 1
			return
	# 因数がなければ追加
	factors.append(Factor(num))

# 次の素数
# @param primes 素数リスト
# @param pmax 最大素数
# @return 次の素数（None:最大を超えたら終了）
def next_prime(primes, pmax):
	# 現素数より大きい奇数から探す（最初は3）
	n = (primes[-1] + 2) if (primes[-1] != 2) else 3
	while True:
		# 最大素数を超えたら終了
		if n > pmax:
			return None
		# 今までの素数で割り切れるか
		b = False
		x = int(math.sqrt(n))
		for i in range(len(primes)):
			if n > x:
				break
			if (n % primes[i]) == 0:
				b = True
				break
		if b:
			# 割り切れたら素数ではない→次の素数を探す
			n += 2
			continue
		else:
			# 次の素数を返す
			primes.append(n)
			return n

# 素因数分解
# @param org 元数値
# @return 処理結果
def get_factor_list(org):
	# 因数リスト初期化
	factors = []
	# 素数リスト初期化
	primes = [2]
	# 現数初期化
	n = org
	# 最大素数
	pmax = int(math.sqrt(org))
	# ループ
	while True:
		# 最大の素数で割ってみる
		p = primes[-1]
		if (n % p) == 0:
			# 割り切れたら因数に追加
			append_factor(p, factors)
			n /= p
			# 現数が1になったら終了
			if n == 1:
				break
		else:
			# 割り切れなかったら次の素数を探す
			if next_prime(primes, pmax) is None:
				# 最大素数以下で見つからなければ終了
				break
	# 残った現数を因数に加える
	if n > 1:
		append_factor(n, factors)
	# 結果を返す
	return factors

# 引数チェック
# @param args 引数
# @return 数値（エラー時はNone）
def check_args(args):
	try:
		num = int(args[1])
		if num < 2:
			raise ValueError(num)
		return num
	except BaseException as e:
		sys.stderr.write("usage:\n")
		sys.stderr.write("factor.py [num]\n")
		sys.stderr.write("  num: int, required(>=2)\n")
		return None

# メイン
def main():
	result = -1
	# 引数チェック
	org = check_args(sys.argv)
	if org is not None:
		# 素因数分解
		factors = get_factor_list(org)
		# 表示
		display(org, factors)
		# 正常終了
		result = 0
	# 終了
	sys.exit(result)

main()

