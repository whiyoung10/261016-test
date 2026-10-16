import streamlit as st


st.set_page_config(page_title="그림으로 배우는 곱셈", page_icon="🍎")

DEFAULT_VALUES = {"multiplicand": 2, "multiplier": 3, "picture": "사과"}
PICTURES = {"사과": "🍎", "별": "⭐", "꽃": "🌸"}


def reset_inputs():
    """위젯이 다시 그려지기 전에 모든 입력을 처음 상태로 돌립니다."""
    for key, value in DEFAULT_VALUES.items():
        st.session_state[key] = value


for key, value in DEFAULT_VALUES.items():
    if key not in st.session_state:
        st.session_state[key] = value


st.markdown(
    """
    <style>
        [data-testid="stWidgetLabel"] p,
        [data-testid="stRadio"] label p {
            font-size: 1.2rem;
        }
        [data-testid="stNumberInput"] input {
            font-size: 1.6rem;
            font-weight: 700;
        }
        [data-testid="stMarkdownContainer"] p {
            font-size: 1.2rem;
        }
        .stButton button {
            min-height: 3rem;
        }
        .stButton button p {
            font-size: 1.2rem;
        }
        .array-scroll {
            overflow-x: auto;
            padding: 1rem;
            border: 2px solid rgba(91, 156, 102, 0.35);
            border-radius: 1rem;
            background: rgba(91, 156, 102, 0.08);
        }
        .picture-array {
            display: grid;
            gap: 0.75rem;
            width: max-content;
            margin: 0 auto;
        }
        .picture-row {
            display: grid;
            grid-template-columns: repeat(var(--columns), 3.5rem);
            gap: 0.75rem;
        }
        .picture-cell {
            display: grid;
            place-items: center;
            width: 3.5rem;
            height: 3.5rem;
            font-size: 2.5rem;
            line-height: 1;
        }
        .multiplication-result {
            margin-top: 1.25rem;
            text-align: center;
            font-size: clamp(2.5rem, 7vw, 3.5rem);
            font-weight: 800;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("그림으로 배우는 곱셈")
st.write("같은 개수의 그림을 여러 줄에 놓으며 곱셈을 배워요.")
st.write("1부터 9까지 숫자를 골라 보세요.")

left, right = st.columns(2)
with left:
    multiplicand = st.number_input(
        "한 줄에 놓을 그림 수(피승수)",
        min_value=1,
        max_value=9,
        step=1,
        key="multiplicand",
    )
with right:
    multiplier = st.number_input(
        "줄 수(승수)",
        min_value=1,
        max_value=9,
        step=1,
        key="multiplier",
    )

picture = st.radio("어떤 그림을 놓을까요?", list(PICTURES), horizontal=True, key="picture")
st.button("초기화", on_click=reset_inputs)

total = multiplicand * multiplier
emoji = PICTURES[picture]

st.subheader("그림을 살펴봐요")
st.write(f"한 줄에 **{multiplicand}개씩**, **{multiplier}줄** 놓았어요.")

# 한 줄의 칸 수를 고정해 좁은 화면에서도 배열이 바뀌지 않게 합니다.
row_html = '<div class="picture-row">' + (
    f'<span class="picture-cell" aria-hidden="true">{emoji}</span>' * multiplicand
) + "</div>"
st.markdown(
    '<div class="array-scroll" tabindex="0">'
    f'<div class="picture-array" style="--columns: {multiplicand};" '
    f'role="img" aria-label="{picture}가 한 줄에 {multiplicand}개씩 '
    f'{multiplier}줄, 모두 {total}개 있어요.">'
    + row_html * multiplier
    + "</div></div>",
    unsafe_allow_html=True,
)

st.markdown(
    f'<div class="multiplication-result" role="status" aria-live="polite">'
    f"{multiplicand} × {multiplier} = {total}</div>",
    unsafe_allow_html=True,
)
st.write(f"그림은 모두 **{total}개**예요.")
