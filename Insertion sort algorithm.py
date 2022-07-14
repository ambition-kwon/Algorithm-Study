#Algorithm Study 3-2
#삽입 정렬
#시간복잡도가 최악(O(n^2))인 알고리즘 중에서는 가장 빠른 방법
#worst, average -> O(n^2) / best -> O(n)
#탐색 범위를 한칸씩 늘리면서 정렬하는 알고리즘.
#5개의 원카드가 있을 때, 최초엔 2개를 정렬, 한개추가 후 3개 정렬한다고 생각하면 편함
#정렬 수를 늘리는건 순방향, 비교하는건 역방향임

array = list(range(1000000)) #O(N)의 증명 / O(N)이 없다면 실행 불가일 것임

for i in range(1, len(array)): #최초 2개부터 비교하기 때문에 index 1시작
	for j in range(i, 0, -1): #j-1때문에 j최소값은 1이 되어야 함
		if array[j] < array[j-1]:
			array[j], array[j-1] = array[j-1], array[j]
		else: break #등호가 정확하다면 이후엔 이미 '정렬'상태일 것이므로 종료
		#더 빠른 속도를 위한 코드임(O(N)이 될 수 있는 원인)

print(array)



