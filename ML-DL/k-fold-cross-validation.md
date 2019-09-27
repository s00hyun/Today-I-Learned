# K-Fold Cross-Validation
> [A Gentle Introduction to k-fold Cross-Validation](https://machinelearningmastery.com/k-fold-cross-validation/)을 요약 및 번역했습니다.  

## Cross-validation
* 한정된 데이터 샘플에서 머신러닝 모델을 평가하기 위해 사용되는 resampling procedure이다.
* parameter: k (single parameter)
	* 주어진 데이터 샘플이 몇 개의 그룹으로 쪼개질 것인지를 나타냄
	* k=10이면 10-fold cross-validation이라고 부르기도 함
* 일반적인 상황에서 모델이 어떻게 작동할 것인지 한정된 샘플을 이용해 측정(estimate)하는 경우 사용된다.
* 이해가 간단하고, 다른 방법(simple train/test split)보다 일반적으로 모델의 성능(skill)이 덜 편향되거나 덜 optimistic한 방향으로 측정되므로 많이 사용되고 있다. 

## General Procedure
1. dataset을 random하게 섞는다(shuffle).
2. dataset을 k개의 그룹으로, 거의 동일한 크기로 나눈다.
3. unique한 각 그룹에 대해:
	1. 하나의 그룹을 hold out 또는 테스트 데이터셋으로 정한다. (The first fold)
	2. 나머지 그룹들은 훈련 데이터셋으로 정한다. (remaining k-1 folds)
		* 각 데이터 샘플은 hold out set에서 1번 사용되고, 모델 훈련에 k-1번 사용된다.
	3. 모델을 훈련 데이터셋에 fitting 한 후, 테스트셋으로 평가한다.
		* loop 내에서 데이터를 준비해야 데이터가 모델에 유출되지 않는다.
	4. 평가된 점수를 저장해두고 모델은 버린다.
4. 모델 평가 점수들을 이용해 모델의 성능을 요약한다.
	* 보통 모델 성능 점수들의 평균을 이용한다.
	* 표준 편차, 표준 오차와 같은 성능 점수의 분산(variance)도 측정해 보기

## Configuration of k
* k값은 데이터 샘플에 대해 매우 신중하게 결정되어야 한다.
* k를 잘못 선택하면, 분산이나 편향(bias)이 커지는 등 등 모델의 성능이 잘 대표하지 못할 수 있다. 
	* 분산은 모델 fitting에 사용되는 데이터에 따라 크게 달라질 수 있다.
	* 편향의 예: 모델의 성능이 과대평가될 수 있다.
* k값을 결정하는 데에 종종 사용되는 3가지 전략들
	* Representative: k값은 각 훈련/테스트 데이터 샘플 그룹들이 더 넓은 범위의 데이터셋을 통계적으로 대표할 수 있을 만큼 충분히 크게 선택되어야 한다.
	* k=10: k값이 10으로 고정된다. 실험적으로 발견된 값으로, 일반적으로 모델의 성능의 bias가 작게 측정된다.
	* k=n: k값이 n으로 고정되는데, 여기서 n은 각 테스트 샘플이 hold out 데이터셋에서 사용되기 위한 데이터셋의 크기를 말한다. 이러한 접근법을 leave-one-out cross-validation이라고 부른다.
* 응용 머신러닝(applied machine learning) 분야에서 k=10은 매우 흔하게 사용된다. 만약 당신이 당신의 데이터셋에 사용할 k값을 찾는 데에 어려움이 있다면 추천하는 방법이다.
* 만약 선택한 k값이 데이터 샘플을 균등하게 나눠주지 못한다면, 한 그룹이 예제들의 나머지를 가지게 될 것이다. 데이터 샘플을 나눌 때에는 동일한 갯수의 샘플을 가지는 k개의 그룹으로 나누는 것이 좋은데, 그렇게 하면 모델 평가 점수 샘플들이 모두 동등해진다.




