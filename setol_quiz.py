import streamlit as st
import pandas as pd

def main():
    st.title("🧠 랜덤 퀴즈 프로그램")
    
    if "questions_to_solve" not in st.session_state:
        st.session_state.questions_to_solve = None
    if "questions_solved" not in st.session_state:
        st.session_state.questions_solved = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "quiz" not in st.session_state:
        st.session_state.quiz = None

    if st.session_state.questions_to_solve is None:
        num = st.number_input("몇 문제를 풀고 싶나요?", min_value=1, max_value=100, step=1)
        if st.button("퀴즈 시작"):
            st.session_state.questions_to_solve = num
            st.session_state.quiz = load_random_question()
            st.rerun()
    else:
        if st.session_state.quiz is N   one:
            st.session_state.quiz = load_random_question()
        
        question = st.session_state.quiz['문제']
        answer = st.session_state.quiz['답']
        
        st.subheader(f"문제 {st.session_state.questions_solved + 1}")
        st.write(question)
        
        user_answer = st.text_input("정답을 입력하세요:")

        if st.button("제출"):
            if user_answer.strip() == str(answer).strip():
                st.success("정답입니다!")
                st.session_state.score += 1
            else:
                st.error(f"틀렸습니다. 정답은 {answer}")
            st.session_state.questions_solved += 1

            if st.session_state.questions_solved >= st.session_state.questions_to_solve:
                st.success(f"퀴즈 종료! 총 점수: {st.session_state.score} / {st.session_state.questions_to_solve}")
                st.balloons()
                # 세션 초기화
                for key in ["questions_to_solve", "questions_solved", "score", "quiz"]:
                    st.session_state.pop(key)
            else:
                st.session_state.quiz = load_random_question()
                st.rerun()

def load_random_question():
    df = pd.read_excel("study_question_template.xlsx")
    return df.sample(n=1).iloc[0]

if __name__ == "__main__":
    main()
