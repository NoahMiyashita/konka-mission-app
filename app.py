import streamlit as st

# --- セッション状態初期化 ---
if 'points' not in st.session_state:
    st.session_state.points = 0

# --- 魂華データベース ---
konka_info = {
    "魂華": {
        "name": "魂華（Konka）",
        "desc": "魂の中心軸を司るタイプ。自分の人生を“物語化”することで力を発揮する。",
        "missions": [
            "今まで絶対やらなかった行動を1つ実行",
            "『人生を10倍速で変えるなら？』という問いに動く",
            "誰かの魂を動かす投稿を発信する"
        ]
    },
    "風華": {
        "name": "風華（Aeris）",
        "desc": "伝達と変容の力を持つタイプ。風のように、時代をつなぐ存在。",
        "missions": [
            "知らない10人に自分のアイデアを話す",
            "沈黙が怖い場に飛び込む",
            "“伝わる”表現を模索して1日動く"
        ]
    },
    "焔華": {
        "name": "焔華（Ignis）",
        "desc": "情熱と破壊のエネルギーを内包する炎のタイプ。感情が源。",
        "missions": [
            "怒りを創作に変えて表現する",
            "24時間、情熱だけで過ごす",
            "感情の火を外に出してみる"
        ]
    },
    # 必要に応じて残りの魂華（澄華、根華、空華、光華、闇華、命華）もここに追加してください
}

# --- UI ---
st.title("🔥 魂の飛び級ミッション™️")

st.markdown("魂華タイプを選択してください（自動診断は今後追加）")

selected_konka = st.selectbox("魂華タイプ", list(konka_info.keys()))

if selected_konka:
    data = konka_info[selected_konka]
    st.subheader(f"🌸 {data['name']}")
    st.write(data["desc"])

    st.markdown("### 🎯 あなたへの飛び級ミッション")
    for mission in data["missions"]:
        st.markdown(f"- {mission}")

    st.markdown("### 🌱 ミッションに挑戦したら『発酵ポイント』を加算！")
    if st.button("＋挑戦した！"):
        st.session_state.points += 1
        st.success("ナイスチャレンジ！魂が発酵中…")

    # 称号表示
    level = st.session_state.points
    if level < 3:
        st.info(f"魂Lv：🌱 幼芽（{level}pt）")
    elif level < 6:
        st.info(f"魂Lv：🌿 発芽（{level}pt）")
    elif level < 10:
        st.info(f"魂Lv：🌸 開花（{level}pt）")
    else:
        st.success(f"魂Lv：🌕 神話級（{level}pt）")
