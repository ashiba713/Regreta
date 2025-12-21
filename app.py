import streamlit as st

st.title("Regret-Minimization Career Decision Engine")

try:
    from career_data import CAREERS
    from input_handler import get_student_profile
    from simulator import simulate_career
    from regret_calculator import calculate_regret
    from recommender import recommend

    st.write("✅ Modules loaded")

    interest = st.slider("Interest in technical work", 0, 10, 5)
    skill = st.slider("Skill readiness", 0, 10, 5)
    risk = st.selectbox("Risk tolerance", ["Low", "Medium", "High"])
    finance = st.selectbox("Financial pressure", ["Low", "Medium", "High"])
    grind = st.selectbox("Willingness to grind", ["Low", "Medium", "High"])
    stability = st.selectbox("Need for long-term stability", ["Low", "Medium", "High"])

    if st.button("Simulate Career Futures"):
        student = get_student_profile(
            interest, skill, risk, finance, grind, stability
        )

        results = []

        for career, params in CAREERS.items():
            outcomes = simulate_career(params, student)
            regret_data = calculate_regret(outcomes)

            results.append({
                "career": career,
                **regret_data
            })

        best = min(results, key=lambda x: x["worst_regret"])

        st.subheader("Career Comparison")
        st.table(results)

        st.success(
            f"Recommended Career: {best['career']} (Minimum Worst-Case Regret)"
        )

except Exception as e:
    st.error("❌ App crashed")
    st.exception(e)
