import sys


input = sys.stdin.readline
N = int(input())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
M = int(input())
C = list(map(int, input().strip().split()))

result = []
for c in C:
    save = c
    for idx, (a, b) in enumerate(zip(A, B)):
        if a == 0:
            B[idx] = save
            save = b
    result.append(str(save))
print(' '.join(result))

'''
# queuestack

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 (추가 시간 없음) | 1024 MB (추가 메모리 없음) | 13449 | 4831 | 4066 | 34.964% |

## 문제

한가롭게 방학에 놀고 있던 도현이는 갑자기 재밌는 자료구조를 생각해냈다. 그 자료구조의 이름은 queuestack이다.

queuestack의 구조는 다음과 같다. 1$1$번, 2$2$번, ... , 𝑁$N$번의 자료구조(queue 혹은 stack)가 나열되어있으며, 각각의 자료구조에는 한 개의 원소가 들어있다.

queuestack의 작동은 다음과 같다.

- $x_0$을 입력받는다.
    
    𝑥0
    
- $x_0$을 $1$번 자료구조에 삽입한 뒤 $1$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 $x_1$이라 한다.
    
    𝑥0
    
    1
    
    1
    
    𝑥1
    
- $x_1$을 $2$번 자료구조에 삽입한 뒤 $2$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 $x_2$이라 한다.
    
    𝑥1
    
    2
    
    2
    
    𝑥2
    
- ...
- $x_{N-1}$을 $N$번 자료구조에 삽입한 뒤 $N$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 $x_N$이라 한다.
    
    𝑥𝑁−1
    
    𝑁
    
    𝑁
    
    𝑥𝑁
    
- $x_N$을 리턴한다.
    
    𝑥𝑁
    

도현이는 길이 𝑀$M$의 수열 𝐶$C$를 가져와서 수열의 원소를 앞에서부터 차례대로 queuestack에 삽입할 것이다. 이전에 삽입한 결과는 남아 있다. (예제 1$1$ 참고)

queuestack에 넣을 원소들이 주어졌을 때, 해당 원소를 넣은 리턴값을 출력하는 프로그램을 작성해보자.

## 입력

첫째 줄에 queuestack을 구성하는 자료구조의 개수 𝑁$N$이 주어진다. (1≤𝑁≤100000$1 \leq N \leq 100\,000$)

둘째 줄에 길이 𝑁$N$의 수열 𝐴$A$가 주어진다. 𝑖$i$번 자료구조가 큐라면 𝐴𝑖=0$A_i = 0$, 스택이라면 𝐴𝑖=1$A_i = 1$이다.

셋째 줄에 길이 𝑁$N$의 수열 𝐵$B$가 주어진다. 𝐵𝑖$B_i$는 𝑖$i$번 자료구조에 들어 있는 원소이다. (1≤𝐵𝑖≤1000000000$1 \leq B_i \leq 1\,000\,000\,000$)

넷째 줄에 삽입할 수열의 길이 𝑀$M$이 주어진다. (1≤𝑀≤100000$1 \leq M \leq 100\,000$)

다섯째 줄에 queuestack에 삽입할 원소를 담고 있는 길이 𝑀$M$의 수열 𝐶$C$가 주어진다. (1≤𝐶𝑖≤1000000000$1 \leq C_i \leq 1\,000\,000\,000$)

입력으로 주어지는 모든 수는 정수이다.

## 출력

수열 𝐶$C$의 원소를 차례대로 queuestack에 삽입했을 때의 리턴값을 공백으로 구분하여 출력한다.

## 예제 입력 1

```
4
0 1 1 0
1 2 3 4
3
2 4 7

```

## 예제 출력 1

```
4 1 2

```

각 상태에 대한 큐스택 내부를 표현하면 다음과 같다.

- 초기 상태 : $[1, 2, 3, 4]$
    
    [1,2,3,4]
    
- 첫 번째 원소 삽입 : $[2, 2, 3, 1]$
    
    [2,2,3,1]
    
- 두 번째 원소 삽입 : $[4, 2, 3, 2]$
    
    [4,2,3,2]
    
- 세 번째 원소 삽입 : $[7, 2, 3, 4]$
    
    [7,2,3,4]
    

## 예제 입력 2

```
5
1 1 1 1 1
1 2 3 4 5
3
1 3 5

```

## 예제 출력 2

```
1 3 5

```

## 출처

[Camp](https://www.acmicpc.net/category/220) > [ICPC Sinchon Algorithm Camp](https://www.acmicpc.net/category/499) > [2022 ICPC Sinchon Winter Algorithm Camp Contest](https://www.acmicpc.net/category/797) > [초급](https://www.acmicpc.net/category/detail/3028) C번

- 문제를 검수한 사람: [gratus907](https://www.acmicpc.net/user/gratus907), [Green55](https://www.acmicpc.net/user/Green55), [gumgood](https://www.acmicpc.net/user/gumgood), [kyo20111](https://www.acmicpc.net/user/kyo20111), [lky7674](https://www.acmicpc.net/user/lky7674), [mjhmjh1104](https://www.acmicpc.net/user/mjhmjh1104), [tony9402](https://www.acmicpc.net/user/tony9402)
- 문제를 만든 사람: [swoon](https://www.acmicpc.net/user/swoon)

## 알고리즘 분류

- [자료 구조](https://www.acmicpc.net/problem/tag/175)
- [스택](https://www.acmicpc.net/problem/tag/71)
- [덱](https://www.acmicpc.net/problem/tag/73)
- [큐](https://www.acmicpc.net/problem/tag/72)

## 메모

문제 이해하면 쉬움.

A는 큐인지 스텍인지 알려주고

B가 리스트 형태로 원소들이 들어가있음.

M 개의 C 가 주어지는데

각 C를 입력 받았을 때

B의 길이만큼 큐이면 해당 idx에 값을 넣고 넣어져 있던 값을 리턴함.

스텍이면 넣고 그 값을 그대로 빼기 때문에 그냥 패스하면 됨.
'''
