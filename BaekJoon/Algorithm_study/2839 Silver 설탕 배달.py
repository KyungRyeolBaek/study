import sys


input = sys.stdin.readline
N = int(input())
a = N // 5
count = 0
while a >= 0:
    b, c = divmod(N - (a * 5), 3)
    if c == 0:
        break
    else:
        a -= 1
if a + b == 0 or c != 0:
    print(-1)
else:
    print(a + b)

'''
# 설탕 배달 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 328085 | 124004 | 92589 | 37.284% |

## 문제

상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

## 출력

상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

## 예제 입력 1

```
18

```

## 예제 출력 1

```
4

```

## 예제 입력 2

```
4

```

## 예제 출력 2

```
-1

```

## 예제 입력 3

```
6

```

## 예제 출력 3

```
2

```

## 예제 입력 4

```
9

```

## 예제 출력 4

```
3

```

## 예제 입력 5

```
11

```

## 예제 출력 5

```
3

```

## 출처

[Contest](https://www.acmicpc.net/category/45) > [Croatian Open Competition in Informatics](https://www.acmicpc.net/category/17) > [COCI 2010/2011](https://www.acmicpc.net/category/20) > [Contest #7](https://www.acmicpc.net/category/detail/81) 1번

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 데이터를 추가한 사람: [hyunynim](https://www.acmicpc.net/user/hyunynim), [jh05013](https://www.acmicpc.net/user/jh05013)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [다이나믹 프로그래밍](https://www.acmicpc.net/problem/tag/25)
- [그리디 알고리즘](https://www.acmicpc.net/problem/tag/33)

## 메모

5로 나눴을때의 최대 몫에서부터 남은 부분을 3으로 나눴을 때 딱 떨어지는지 확인.

안떨어지면 남은 부분 5씩 증가해서 3으로 나눠 떨어지는지 확인

값이 없을 때 그리고 나머지부분이 조금이라도 남아있으면 -1, 그 외는 두 몫의 합.
```

```

## 예제 출력 2

```
-1

```

## 예제 입력 3

```
6

```

## 예제 출력 3

```
2

```

## 예제 입력 4

```
9

```

## 예제 출력 4

```
3

```

## 예제 입력 5

```
11

```

## 예제 출력 5

```
3

```

## 출처

[Contest](https://www.acmicpc.net/category/45) > [Croatian Open Competition in Informatics](https://www.acmicpc.net/category/17) > [COCI 2010/2011](https://www.acmicpc.net/category/20) > [Contest #7](https://www.acmicpc.net/category/detail/81) 1번

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 데이터를 추가한 사람: [hyunynim](https://www.acmicpc.net/user/hyunynim), [jh05013](https://www.acmicpc.net/user/jh05013)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [다이나믹 프로그래밍](https://www.acmicpc.net/problem/tag/25)
- [그리디 알고리즘](https://www.acmicpc.net/problem/tag/33)

## 메모

5로 나눴을때의 최대 몫에서부터 남은 부분을 3으로 나눴을 때 딱 떨어지는지 확인.

안떨어지면 남은 부분 5씩 증가해서 3으로 나눠 떨어지는지 확인

값이 없을 때 -1, 그 외는 두 몫의 합.
'''