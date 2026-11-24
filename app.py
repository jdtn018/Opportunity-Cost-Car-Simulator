# 1. 차종 데이터 (2차원 리스트 구조: [차종명, 가격(만원), 크기, 색깔])
cars = [
    ["자동차 A", 700, "대형", "흰색"],
    ["자동차 B", 700, "대형", "검은색"],
    ["자동차 C", 600, "소형", "검은색"]
]

# 2. 만족도 점수 계산 함수 (만점 100점 기준, 조건 불만족 시 -30점씩 차감 -> 최저 기본점수 10점)
def calculate_score(car, user_money, user_size, user_color):
    score = 100  # 기본점수(10점) + 3개 조건(각 30점) = 100점
    
    # 조건 1: 돈(예산) 판단 - 내 예산보다 차 가격이 비싸면 불만족
    if car[1] > user_money:
        score -= 30
        
    # 조건 2: 크기 판단
    if car[2] != user_size:
        score -= 30
        
    # 조건 3: 색깔 판단
    if car[3] != user_color:
        score -= 30
        
    return score

# --- 초기 안내: 차종별 특징 리스트 먼저 보여주기 ---
print("=== [기회비용: 효율적인 차종 고르기] ===")
print("\n[차종별 특징 리스트]")
for car in cars:
    print(f"- {car[0]}: {car[1]}만원 / {car[2]} / {car[3]}")
print("-" * 36)

# --- 사용자 조건 입력 화면 ---
user_money = int(input("1/ 돈 입력 [600 / 700] (숫자만 입력): ").replace("만원", "").strip())
user_size = input("2/ 크기 입력 [소형 / 대형]: ").strip()
user_color = input("3/ 색깔 입력 [흰색 / 검은색]: ").strip()

# 3. 반복문을 이용해 각 차종의 만족도 점수를 계산하고 리스트에 저장
satisfaction_scores = []
for car in cars:
    score = calculate_score(car, user_money, user_size, user_color)
    satisfaction_scores.append(score)

# 4. 반복문과 조건문을 이용해 최고 점수를 찾고, 동점 차종까지 모두 리스트에 저장
max_score = satisfaction_scores[0]
for score in satisfaction_scores:
    if score > max_score:
        max_score = score

best_cars = []
for i in range(len(satisfaction_scores)):
    if satisfaction_scores[i] == max_score:
        best_cars.append(cars[i][0])

# --- 결과 출력 화면 ---
print("\n------- [결과 출력 화면] -------")
print(f"★ 사용자 만족도 점수 리스트: {satisfaction_scores}")

for i in range(len(cars)):
    print(f"- {cars[i][0]}: {satisfaction_scores[i]}점")

# if - elif - else 조건문을 활용한 최종 결과 출력
if len(best_cars) == 1:
    print(f"\n{best_cars[0]}를 선택하는 것이 가장 합리적이다!")
elif len(best_cars) == 2:
    print(f"\n{best_cars[0]} 또는 {best_cars[1]}를 선택하는 것이 가장 합리적이다!")
else:
    print(f"\n{' 또는 '.join(best_cars)}를 선택하는 것이 가장 합리적이다!")
