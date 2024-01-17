import sys


input = sys.stdin.readline
grade = {'A+': 4.5, 'A0': 4, 'B+': 3.5, 'B0':3, 'C+': 2.5, 'C0':2, 'D+': 1.5, 'D0': 1, 'F': 0}
score = 0
t_score = 0
for _ in range(20):
    _class, _time, _grade = input().strip().split()
    if _grade != 'P':
        score += float(_time) * grade[_grade]
        t_score += float(_time)
if score != 0:
    print(score / t_score)
else:
    print(0)

'''
# 너의 평점은 스페셜 저지

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 1024 MB | 42285 | 18744 | 16609 | 44.996% |

## 문제

인하대학교 컴퓨터공학과를 졸업하기 위해서는, 전공평점이 3.3 이상이거나 졸업고사를 통과해야 한다. 그런데 아뿔싸, 치훈이는 깜빡하고 졸업고사를 응시하지 않았다는 사실을 깨달았다!

치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.

전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.

인하대학교 컴퓨터공학과의 등급에 따른 과목평점은 다음 표와 같다.

| A+ | 4.5 |
| --- | --- |
| A0 | 4.0 |
| B+ | 3.5 |
| B0 | 3.0 |
| C+ | 2.5 |
| C0 | 2.0 |
| D+ | 1.5 |
| D0 | 1.0 |
| F | 0.0 |

P/F 과목의 경우 등급이 `P`또는 `F`로 표시되는데, 등급이 `P`인 과목은 계산에서 제외해야 한다.

과연 치훈이는 무사히 졸업할 수 있을까?

## 입력

**20**줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.

## 출력

치훈이의 전공평점을 출력한다.

정답과의 절대오차 또는 상대오차가 10−4\(10^{-4}\) 이하이면 정답으로 인정한다.

## 제한

- 1 ≤ 과목명의 길이 ≤ 50
- 과목명은 알파벳 대소문자 또는 숫자로만 이루어져 있으며, 띄어쓰기 없이 주어진다. 입력으로 주어지는 모든 과목명은 서로 다르다.
- 학점은 `1.0`,`2.0`,`3.0`,`4.0`중 하나이다.
- 등급은 `A+`,`A0`,`B+`,`B0`,`C+`,`C0`,`D+`,`D0`,`F`,`P`중 하나이다.
- 적어도 한 과목은 등급이 `P`가 아님이 보장된다.

## 예제 입력 1

```
ObjectOrientedProgramming1 3.0 A+
IntroductiontoComputerEngineering 3.0 A+
ObjectOrientedProgramming2 3.0 A0
CreativeComputerEngineeringDesign 3.0 A+
AssemblyLanguage 3.0 A+
InternetProgramming 3.0 B0
ApplicationProgramminginJava 3.0 A0
SystemProgramming 3.0 B0
OperatingSystem 3.0 B0
WirelessCommunicationsandNetworking 3.0 C+
LogicCircuits 3.0 B0
DataStructure 4.0 A+
MicroprocessorApplication 3.0 B+
EmbeddedSoftware 3.0 C0
ComputerSecurity 3.0 D+
Database 3.0 C+
Algorithm 3.0 B0
CapstoneDesigninCSE 3.0 B+
CompilerDesign 3.0 D0
ProblemSolving 4.0 P

```

## 예제 출력 1

```
3.284483

```

## 예제 입력 2

```
BruteForce 3.0 F
Greedy 1.0 F
DivideandConquer 2.0 F
DynamicProgramming 3.0 F
DepthFirstSearch 4.0 F
BreadthFirstSearch 3.0 F
ShortestPath 4.0 F
DisjointSet 2.0 F
MinimumSpanningTree 2.0 F
TopologicalSorting 1.0 F
LeastCommonAncestor 2.0 F
SegmentTree 4.0 F
EulerTourTechnique 3.0 F
StronglyConnectedComponent 2.0 F
BipartiteMatching 2.0 F
MaximumFlowProblem 3.0 F
SuffixArray 1.0 F
HeavyLightDecomposition 4.0 F
CentroidDecomposition 3.0 F
SplayTree 1.0 F

```

## 예제 출력 2

```
0.000000

```

## 노트

예제 1은 치훈이의 실제 전공과목 성적이다.

## 출처

[University](https://www.acmicpc.net/category/5) > [인하대학교](https://www.acmicpc.net/category/336) > [2022 인하대학교 프로그래밍 경진대회(IUPC)](https://www.acmicpc.net/category/detail/3124) B번

- 문제를 검수한 사람: [39dll](https://www.acmicpc.net/user/39dll), [gumgood](https://www.acmicpc.net/user/gumgood), [jh05013](https://www.acmicpc.net/user/jh05013), [jhnah917](https://www.acmicpc.net/user/jhnah917), [ruz](https://www.acmicpc.net/user/ruz), [yooshnn](https://www.acmicpc.net/user/yooshnn), [yuja](https://www.acmicpc.net/user/yuja)
- 문제를 만든 사람: [wjdclgns12](https://www.acmicpc.net/user/wjdclgns12)

## 알고리즘 분류

[보기](https://www.acmicpc.net/problem/25206#)

## 메모

문제 자세히 읽어야함….
'''