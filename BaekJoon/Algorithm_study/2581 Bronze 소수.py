import sys
import math


# 소수 판별 함수
def is_prime_number(x):
    if x < 2:
        return False # 2 이하 소수 아님
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


input = sys.stdin.readline
M = int(input().strip())
N = int(input().strip())
prime_list = []
for num in range(M, N + 1):
    if is_prime_number(num):
        prime_list.append(num)

if prime_list:
    print(sum(prime_list))
    print(prime_list[0])
else:
    print(-1)

'''
# 소수

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 143275 | 56792 | 47792 | 39.383% |

## 문제

자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

## 입력

입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

## 출력

M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.

단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

## 예제 입력 1

```
60
100

```

## 예제 출력 1

```
620
61

```

## 예제 입력 2

```
64
65

```

## 예제 출력 2

```
-1

```

## 출처

[Olympiad](https://www.acmicpc.net/category/2) > [한국정보올림피아드](https://www.acmicpc.net/category/55) > [한국정보올림피아드시․도지역본선](https://www.acmicpc.net/category/57) > [지역본선 2006](https://www.acmicpc.net/category/70) > [중등부](https://www.acmicpc.net/category/detail/368) 1번

- 문제의 오타를 찾은 사람: [jh05013](https://www.acmicpc.net/user/jh05013), [sky1357](https://www.acmicpc.net/user/sky1357)
- 데이터를 추가한 사람: [kyaryunha](https://www.acmicpc.net/user/kyaryunha), [snapflip20](https://www.acmicpc.net/user/snapflip20)
- 잘못된 데이터를 찾은 사람: [myungwoo](https://www.acmicpc.net/user/myungwoo)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [정수론](https://www.acmicpc.net/problem/tag/95)
- [소수 판정](https://www.acmicpc.net/problem/tag/9)

## 메모

### 문제 풀이

```python

```

# 소수

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 143275 | 56792 | 47792 | 39.383% |

## 문제

자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

## 입력

입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

## 출력

M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.

단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

## 예제 입력 1

```
60
100

```

## 예제 출력 1

```
620
61

```

## 예제 입력 2

```
64
65

```

## 예제 출력 2

```
-1

```

## 출처

[Olympiad](https://www.acmicpc.net/category/2) > [한국정보올림피아드](https://www.acmicpc.net/category/55) > [한국정보올림피아드시․도지역본선](https://www.acmicpc.net/category/57) > [지역본선 2006](https://www.acmicpc.net/category/70) > [중등부](https://www.acmicpc.net/category/detail/368) 1번

- 문제의 오타를 찾은 사람: [jh05013](https://www.acmicpc.net/user/jh05013), [sky1357](https://www.acmicpc.net/user/sky1357)
- 데이터를 추가한 사람: [kyaryunha](https://www.acmicpc.net/user/kyaryunha), [snapflip20](https://www.acmicpc.net/user/snapflip20)
- 잘못된 데이터를 찾은 사람: [myungwoo](https://www.acmicpc.net/user/myungwoo)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [정수론](https://www.acmicpc.net/problem/tag/95)
- [소수 판정](https://www.acmicpc.net/problem/tag/9)

## 메모

소수 판별 함수 사용.

[소수 판별](https://www.notion.so/7ef40f8788104ac98a41cd5296c8929e?pvs=21)
'''