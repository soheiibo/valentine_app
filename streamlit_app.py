import streamlit as st
import streamlit.components.v1 as components
from datetime import date

st.set_page_config(page_title="💘 Valentine?", page_icon="💘", layout="centered")

# --- Read URL params ---
params = st.query_params
accepted = params.get("yes", "0") == "1"

# --- Styling ---
st.markdown("""
<style>
:root { --pink: #ff4d8d; --bg: rgba(255,77,141,0.10); }
.block-container { max-width: 720px; padding-top: 2.2rem; }
.title { font-size: 44px; font-weight: 900; letter-spacing: -0.5px; }
.subtitle { font-size: 18px; opacity: .85; margin-top: -8px; }
.card {
border: 1px solid rgba(255,255,255,.12);
background: var(--bg);
border-radius: 22px;
padding: 18px 18px 10px 18px;
}
.small { font-size: 13px; opacity: .75; }
hr { border: none; border-top: 1px solid rgba(255,255,255,.12); margin: 16px 0; }
</style>
""", unsafe_allow_html=True)

# --- Top header ---
st.markdown('<div class="title">💘 Hello Ma vie</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">J\'ai une question (très) importante…</div>', unsafe_allow_html=True)
st.write("")


with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    if not accepted:
        st.markdown("### Madame, Will you be my Valentine? ")
        st.write("")

        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if st.button("✅ YES", use_container_width=True, key="yes_btn"):
                st.query_params["yes"] = "1"
                st.rerun()
        
        with col3:
            # Bouton NO avec animation qui s'échappe
            html_no = """
            <div style="position: relative; height: 80px; width: 100%;">
            <button id="noBtn" style="
                position: absolute; left: 0; top: 0;
                padding: 10px 20px; border-radius: 8px; border: 2px solid #ff4d8d;
                background: rgba(255,77,141,.1); color: #ff4d8d; font-weight: bold; font-size: 16px;
                cursor: pointer; transition: all 0.1s; white-space: nowrap;
            ">❌ NO</button>
            <script>
            const noBtn = document.getElementById("noBtn");
            function moveNoButton(){
                const container = noBtn.parentElement;
                const containerRect = container.getBoundingClientRect();
                const btnWidth = 70;
                const btnHeight = 40;
                
                const maxX = Math.max(0, containerRect.width - btnWidth);
                const maxY = Math.max(0, containerRect.height - btnHeight);
                
                const x = Math.random() * maxX;
                const y = Math.random() * maxY;
                
                noBtn.style.left = x + "px";
                noBtn.style.top = y + "px";
            }
            noBtn.addEventListener("mouseenter", moveNoButton);
            noBtn.addEventListener("click", (e) => { 
                e.preventDefault(); 
                e.stopPropagation();
                moveNoButton(); 
                return false;
            });
            </script>
            </div>
            """
            components.html(html_no, height=90)
        
        st.write("")
        st.markdown("#### Petit bonus 💌")
        st.caption("Si tu cliques sur YES, il y a une surprise.")

    else:
        st.balloons()
        st.markdown("### Yes 💖")
        st.success("it's fixed : **my Valentine**.")
        st.write("")

        st.markdown("#### 📅 Le plan")
        st.markdown("""
- **Quand :** 13/14 février, 
- **Où :** on va trouver notre petit coin de paradis 🌴
- **Dress code :** on s'habille pas comme Claudia ✨
- **Programme :** dîner + moment chill ensemble 🕯️
""")

        st.markdown("#### 🎁 My secret message to Ryma")
        st.info("After 2 years, it's finally the day we meet. it was so complicated to find you Among 4 billion women on Earth 💞")

        st.markdown("---")
        if st.button("↩️ Revenir à la question"):
            st.query_params.clear()

    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.markdown('<div class="small">Codé avec amour 🧑‍💻💗</div>', unsafe_allow_html=True)
