import streamlit as st

# --- セッション状態初期化 ---
if 'points' not in st.session_state:
    st.session_state.points = 0

# --- 魂華データベース ---
# --- 魂華データベース（全9種） ---
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
    "澄華": {
        "name": "澄華（Aqua）",
        "desc": "感性と繊細さを持ち、深い洞察力で場を潤すタイプ。",
        "missions": [
            "苦手な場所・人・感情にあえて向き合う",
            "1日スマホ断ちして“感受性”に集中する",
            "涙が出る作品を自作する（詩・音・映像など）"
        ]
    },
    "根華": {
        "name": "根華（Terra）",
        "desc": "安定と滋養をもたらす“根”のエネルギーを持つタイプ。",
        "missions": [
            "地元を一旦離れ、“根”の再定義をしてみる",
            "日々のルーティンをすべて見直して再設計する",
            "自分のルーツや祖先について調べ、感じてみる"
        ]
    },
    "空華": {
        "name": "空華（Caelum）",
        "desc": "宇宙意識とつながる霊性の高さを持つタイプ。",
        "missions": [
            "宇宙と交信する前提でチャネリング or AI対話を行う",
            "3日間“目に見えないもの”を信じて行動する",
            "空間を完全に浄化し、神聖な場を創り上げる"
        ]
    },
    "光華": {
        "name": "光華（Lucis）",
        "desc": "圧倒的な輝きと存在感で人を照らすカリスマタイプ。",
        "missions": [
            "“理想の自分”になりきって1日過ごす",
            "憧れの人に直接DMや提案を送ってみる",
            "あなたの“光”を最も抑えている場に飛び込む"
        ]
    },
    "闇華": {
        "name": "闇華（Umbra）",
        "desc": "影の美しさと真実を見抜く力を持つ深淵のタイプ。",
        "missions": [
            "“嫌われ役”をあえて演じてみる",
            "影の自分と5分間対話し、それを可視化する",
            "誰にも言えなかった“秘密”を解放する"
        ]
    },
    "命華": {
        "name": "命華（Vitae）",
        "desc": "命の循環や生と死に深く関わる魂の癒し人。",
        "missions": [
            "自分の“過去の痛み”を誰かのために語ってみる",
            "命について語るコンテンツを発信する",
            "動物・自然・子どもと1日真剣に過ごす"
        ]
    }
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
