# TIL

###6월 11일

####점근적 복잡도
시간 복잡도와 공간복잡도에 관해 배움. 시간복잡도는 간략하게 말하면 입력값과 문제를 해결하는데 걸리는 시간과의 상관관계를 말하고, 공간 복잡도는 입력값과 문제를 해결하는 데 걸리는 공간과의 상관관계를 말함.
시간복잡도를 대체로 더 중요하게 여기고 입력값이 많아져도 걸리는 시간이 덜 늘어나는 알고리즘이 좋은 알고리즘이 될 수 있다고 함. 아닐수도 있고

####Array | Linked List
Array는 배열이고 특정 원소를 조회하는 경우에 사용하는 것이 유리하고 LinkedList는 중간에 데이터를 삽입하고 삭제하는일이 빈번할때 사용하는 것이 좋음
파이썬에서는 list가 Array로 구현되있고 동적배열을 사용해서 배열의 길이가 늘어나도 시간복잡도가 O(1)로 걸리도록 설계 되있음!! 링크드리스트 관련해선 공부가 더 필요할듯 백준 1158번 문제푸는데 꽤나 애먹었음.

####Class
클래스는 분류나 집합 같은 속성과 기능을 총칭하는 개념!
객체는 유일무이한 사물이고 클래스는 그걸 아우르는 말이다. 그러니까 클래스 = 사람 이면 객체는 내가 될수도 있고 옆집 뒷집 등 다양한 사람들이 될 수 있는 것

####이진탐색
1~100중에서 특정 숫자를 찾아야 할 때 1부터 100까지 하나하나 다 찾아서 비교하는게 아니고 반 나눠서 업다운으로 비교하고 다시 반을 잘라서 비교하는 식으로 특정 숫자를 찾는 방식.
업다운 게임이랑 거의 동일함. 이게 순차적으로 찾는거보다 빅오표기법을 기반으로 봤을때 말도안되게 빨라지는듯

####재귀함수
재귀는 어떠한 것을 정의할 때 자기 자신을 참조하는 것을 말한다. 그니까 함수가 자기자신을 호출해서 쓰는 함수를 말함. 대표적으로 팩토리얼이랑 피보나치 등이 있음
