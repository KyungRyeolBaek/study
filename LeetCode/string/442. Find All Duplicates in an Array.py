class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        nums = sorted(nums)
        for idx in range(len(nums) - 1):
            if nums[idx] == nums[idx + 1]:
                res.append(nums[idx])
        return res

# another sol
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                res.append(num)
            else:
                nums[num-1] = -nums[num-1]
        return res

'''
442 . 배열에서 모든 중복 찾기
중간

4592

212

목록에 추가

공유하다
정수 배열 주어 nums길이를 n모든 곳 정수 nums의 범위에있는 [1, n]각각의 정수 표시 되면 또는 두번 반환 나타나는 모든 정수 배열 배를 .

O(n) 시간 에 따라 실행되고 일정한 추가 공간만 사용 하는 알고리즘을 작성해야 합니다  .

 

예 1:

입력: 숫자 = [4,3,2,7,8,2,3,1]
 출력: [2,3]
예 2:

입력: 숫자 = [1,1,2]
 출력: [1]
예 3:

입력: 숫자 = [1]
 출력: []
 

제약:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
의 각 요소는 한 번 또는 두 번nums 나타납니다 .
'''