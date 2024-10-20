import sys


input = sys.stdin.readline
bowls = [int(input()) for _ in range(3)]
print(sorted(bowls)[1])

'''
# Who is in the middle? 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 6213 | 4604 | 4370 | 75.384% |

## 문제

In the story Goldilocks and the Three Bears, each bear had a bowl of porridge to eat while sitting at his/her favourite chair. What the story didn’t tell us is that Goldilocks moved the bowls around on the table, so the bowls were not at the right seats anymore. The bowls can be sorted by weight with the lightest bowl being the Baby Bear’s bowl, the medium bowl being the Mama Bear’s bowl and the heaviest bowl being the Papa Bear’s bowl. Write a program that reads in three weights and prints out the weight of Mama Bear’s bowl. You may assume all weights are positive integers less than 100.

## 예제 입력 1 복사

```
10
5
8

```

## 예제 출력 1 복사

```
8

```

## 출처

[Olympiad](https://www.acmicpc.net/category/2) > [Canadian Computing Competition & Olympiad](https://www.acmicpc.net/category/173) > [2007](https://www.acmicpc.net/category/180) > [CCC 2007 Junior Division](https://www.acmicpc.net/category/detail/793) 1번

## 알고리즘 분류

- [구현](https://www.acmicpc.net/problem/tag/102)

## 메모
'''