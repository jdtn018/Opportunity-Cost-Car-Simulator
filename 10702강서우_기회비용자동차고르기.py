import streamlit as st

# 1. 차종 데이터 (2차원 리스트 구조: [차종명, 가격(만원), 크기, 색깔])
cars = [
    ["자동차 A", 800, "대형", "흰색"],
    ["자동차 B", 700, "대형", "검은색"],
    ["자동차 C", 600, "소형", "검은색"]
]

# 2. 만족도 점수 계산 함수
def calculate_score(car, user_money, user_size, user_color):
    score = 100  # 기본점수(10점) + 3개 조건(각 30점) = 100점

    if car[1] > user_money:
        score -= 30
    if car[2] != user_size:
        score -= 30
    if car[3] != user_color:
        score -= 30

    return score

# --- Streamlit 사용자 입력 화면 (input() 대신 st 위젯 사용) ---
st.title("🚗 기회비용: 효율적인 차종 고르기")
st.write("원하는 조건을 선택하면 가장 합리적인 차종을 계산해 드립니다.")

st.divider()

# 기존 input() 부분을 웹 UI로 변경
selected_car = st.selectbox("1/ 처음 마음에 둔 차종을 선택하세요:", ["자동차 A", "자동차 B", "자동차 C"])
user_money = st.radio("2/ 예산(돈)을 선택하세요 (만원):", [600, 700], horizontal=True)
user_size = st.radio("3/ 원하는 크기를 선택하세요:", ["소형", "대형"], horizontal=True)
user_color = st.radio("4/ 원하는 색깔을 선택하세요:", ["흰색", "검은색"], horizontal=True)

# 버튼을 눌렀을 때 결과 계산 및 출력
if st.button("합리적인 차종 분석하기", type="primary"):
    # 3. 반복문을 이용해 각 차종의 만족도 점수 계산
    satisfaction_scores = []
    for car in cars:
        score = calculate_score(car, user_money, user_size, user_color)
        satisfaction_scores.append(score)

    # 4. 가장 점수가 높은 합리적인 차종 찾기
    best_index = 0
    for i in range(len(satisfaction_scores)):
        if satisfaction_scores[i] > satisfaction_scores[best_index]:
            best_index = i

    best_car = cars[best_index][0]

    # --- 결과 출력 화면 (print() 대신 st.write, st.success 등 사용) ---
    st.divider()
    st.subheader("📊 분석 결과")
    st.write(f"**★ 사용자 만족도 점수 리스트:** `{satisfaction_scores}`")

    for i in range(len(cars)):
        st.write(f"- **{cars[i][0]}**: {satisfaction_scores[i]}점 (가격: {cars[i][1]}만원 / {cars[i][2]} / {cars[i][3]})")

    # 처음 선택한 차종의 점수 안내
    for i in range(len(cars)):
        if cars[i][0].replace(" ", "") == selected_car.replace(" ", ""):
            st.info(f"▶ 처음 선택한 **[{cars[i][0]}]**의 만족도 점수는 **{satisfaction_scores[i]}점**입니다.")

    st.success(f"💡 결론: **{best_car}**를 선택하는 것이 가장 합리적입니다!")
