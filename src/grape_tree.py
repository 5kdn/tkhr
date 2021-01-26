#!/usr/bin/env python3
"""
    [問題]
        葡萄のパズル
        ①②③
         ④⑤
          ⑥
        ④ = |①-②|
        ⑤ = |②-③|
        ⑥ = |④-⑤|
        となるような数

    [制約]
        - 数字の重複不可
        - 取りうる数字の範囲は1 ≦ n ≦ 段数(段数+1)/2

    [出力]
        全組み合わせを出力
"""

from typing import List, Tuple
from itertools import permutations


def show_grape_tree(grape_tree: List[List[int]]) -> None:
    prefix = '  '
    for i in range(len(grape_tree)):
        print(prefix * i, end='')
        for j in grape_tree[i]:
            print(f'({j:>2})', end='')
        print('')
    print('---')


def recursion(grape_tree:List[List[int]], appearance:List[bool], max_val:int) -> Tuple[List[List[int]], bool]:
    last_stage = grape_tree[-1]
    new_stage = []
    for i in range(len(last_stage)-1):
        val = abs(last_stage[i] - last_stage[i+1])
        if val == 0 or val > max_val:
            # 範囲外
            return (grape_tree, False)
        elif appearance[val]:
            # すでにその数字は使われている
            return (grape_tree, False)
        appearance[val] = True

        new_stage.append( val )
    grape_tree.append(new_stage)

    if len(new_stage) > 1:
        return recursion(grape_tree, appearance, max_val)
    show_grape_tree(grape_tree)
    return (grape_tree, True)


if __name__ == '__main__':
    stage = int(input('段数:'))
    max_val = stage * (stage + 1) // 2
    stage1 = permutations(range(1, max_val+1), stage)

    for s1 in stage1:
        grape_tree = [list(s1)]
        appearance = [False] * (max_val + 1)
        for i in s1:
            appearance[i] = True
        recursion(grape_tree, appearance, max_val)
