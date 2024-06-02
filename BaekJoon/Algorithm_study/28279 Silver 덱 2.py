import sys
from collections import deque


input = sys.stdin.readline
N = int(input())
que = deque()
for _ in range(N):
    command = input().strip()
    if command == '3':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif command == '4':
        if que:
            print(que.pop())
        else:
            print(-1)
    elif command == '5':
        print(len(que))
    elif command == '6':
        if que:
            print(0)
        else:
            print(1)
    elif command == '7':
        if que:
            print(que[0])
        else:
            print(-1)
    elif command == '8':
        if que:
            print(que[-1])
        else:
            print(-1)
    else:
        command, num = command.split()
        if command == '1':
            que.appendleft(num)
        elif command == '2':
            que.append(num)

'''
# 덱 2

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 1024 MB | 11917 | 5818 | 5194 | 50.237% |

## 문제

정수를 저장하는 덱을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

1. `1 X`: 정수 를 덱의 앞에 넣는다. (1 ≤  ≤ 100,000)
    
    X
    
    X
    
2. `2 X`: 정수 를 덱의 뒤에 넣는다. (1 ≤  ≤ 100,000)
    
    X
    
    X
    
3. `3`: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 `1`을 대신 출력한다.
4. `4`: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 `1`을 대신 출력한다.
5. `5`: 덱에 들어있는 정수의 개수를 출력한다.
6. `6`: 덱이 비어있으면 `1`, 아니면 `0`을 출력한다.
7. `7`: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 `1`을 대신 출력한다.
8. `8`: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 `1`을 대신 출력한다.

## 입력

첫째 줄에 명령의 수 N이 주어진다. (1 ≤ N ≤ 1,000,000)

둘째 줄부터 N개 줄에 명령이 하나씩 주어진다.

출력을 요구하는 명령은 하나 이상 주어진다.

## 출력

출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력한다.

## 예제 입력 1

```
11
6
1 3
1 8
7
8
3
2 5
1 2
5
4
4

```

## 예제 출력 1

```
1
8
3
8
3
5
3

```

## 출처

- 문제를 만든 사람: [kiwiyou](https://www.acmicpc.net/user/kiwiyou)
- 문제를 검수한 사람: [sorohue](https://www.acmicpc.net/user/sorohue), [ufshg](https://www.acmicpc.net/user/ufshg), [wapas](https://www.acmicpc.net/user/wapas), [wider93](https://www.acmicpc.net/user/wider93), [yup0927](https://www.acmicpc.net/user/yup0927)

## 알고리즘 분류

- [자료 구조](https://www.acmicpc.net/problem/tag/175)
- [덱](https://www.acmicpc.net/problem/tag/73)

## 메모

deque 사용하면 금방 풀림.

[파이썬 Deque - pop, push 리스트보다 빠름](https://www.notion.so/Deque-pop-push-64372aac99ea4b4a83b5feb6f61f70ec?pvs=21)
'''