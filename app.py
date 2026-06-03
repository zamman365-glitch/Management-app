import streamlit as st
import json
import random
import string
from pathlib import Path

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="VaultX — Modern Banking",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Sora', sans-serif;
}

/* ── Background ── */
.stApp {
    background: linear-gradient(135deg, #0f0c29 0%, #1a1a2e 50%, #16213e 100%);
    min-height: 100vh;
}

/* ── Hide default elements ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; max-width: 680px; }

/* ── Hero Banner ── */
.hero-banner {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 20px;
    padding: 2rem 2.5rem;
    margin-bottom: 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.06) 0%, transparent 60%);
    animation: shimmer 4s ease-in-out infinite;
}
@keyframes shimmer {
    0%, 100% { transform: translate(-20%, -20%); }
    50% { transform: translate(20%, 20%); }
}
.hero-title {
    font-size: 2.2rem;
    font-weight: 700;
    color: white;
    letter-spacing: -1px;
    margin: 0;
}
.hero-sub {
    color: rgba(255,255,255,0.7);
    font-size: 0.95rem;
    margin-top: 0.25rem;
}

/* ── Section Card ── */
.section-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 1.8rem;
    margin-bottom: 1.5rem;
    backdrop-filter: blur(10px);
}

/* ── Balance Card ── */
.balance-card {
    background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
    border-radius: 16px;
    padding: 1.5rem 2rem;
    color: white;
    margin-bottom: 1rem;
}
.balance-label {
    font-size: 0.8rem;
    opacity: 0.8;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 500;
}
.balance-amount {
    font-family: 'Space Mono', monospace;
    font-size: 2.4rem;
    font-weight: 700;
    line-height: 1.2;
}

/* ── Info Row ── */
.info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.7rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.07);
    color: rgba(255,255,255,0.85);
    font-size: 0.9rem;
}
.info-label { color: rgba(255,255,255,0.45); font-size: 0.8rem; }
.info-value { font-weight: 500; font-family: 'Space Mono', monospace; font-size: 0.85rem; }

/* ── Status Badges ── */
.badge-success {
    background: rgba(56,239,125,0.15);
    color: #38ef7d;
    border: 1px solid rgba(56,239,125,0.3);
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.5px;
}
.badge-warning {
    background: rgba(255,193,7,0.15);
    color: #ffc107;
    border: 1px solid rgba(255,193,7,0.3);
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
}
.badge-danger {
    background: rgba(255,82,82,0.15);
    color: #ff5252;
    border: 1px solid rgba(255,82,82,0.3);
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
}

/* ── Streamlit overrides ── */
.stTextInput input, .stNumberInput input {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 10px !important;
    color: white !important;
    font-family: 'Sora', sans-serif !important;
    padding: 0.6rem 1rem !important;
}
.stTextInput input:focus, .stNumberInput input:focus {
    border-color: #667eea !important;
    box-shadow: 0 0 0 2px rgba(102,126,234,0.25) !important;
}
label, .stTextInput label, .stNumberInput label {
    color: rgba(255,255,255,0.6) !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.5px !important;
}
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.7rem 2rem !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.5px !important;
    transition: opacity 0.2s, transform 0.1s !important;
    cursor: pointer !important;
}
.stButton > button:hover {
    opacity: 0.9 !important;
    transform: translateY(-1px) !important;
}
.stButton > button:active { transform: translateY(0px) !important; }

.stSelectbox > div > div {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 10px !important;
    color: white !important;
}
.stSuccess, [data-testid="stSuccessMessage"] {
    background: rgba(56,239,125,0.1) !important;
    border: 1px solid rgba(56,239,125,0.3) !important;
    border-radius: 10px !important;
    color: #38ef7d !important;
}
.stError, [data-testid="stErrorMessage"] {
    background: rgba(255,82,82,0.1) !important;
    border: 1px solid rgba(255,82,82,0.3) !important;
    border-radius: 10px !important;
    color: #ff5252 !important;
}
.stWarning, [data-testid="stWarningMessage"] {
    background: rgba(255,193,7,0.1) !important;
    border: 1px solid rgba(255,193,7,0.3) !important;
    border-radius: 10px !important;
    color: #ffc107 !important;
}
div[role="radiogroup"] label {
    color: rgba(255,255,255,0.85) !important;
    font-size: 0.9rem !important;
    font-weight: 400 !important;
}
.stRadio > label { color: rgba(255,255,255,0.5) !important; }
h1, h2, h3 { color: white !important; font-family: 'Sora', sans-serif !important; }
p { color: rgba(255,255,255,0.8) !important; }
hr { border-color: rgba(255,255,255,0.1) !important; }
</style>
""", unsafe_allow_html=True)


# ─── Database Helpers ─────────────────────────────────────────────────────────
DATABASE = "vaultx_database.json"

def load_data():
    if Path(DATABASE).exists():
        with open(DATABASE) as f:
            return json.loads(f.read())
    return []

def save_data(data):
    with open(DATABASE, "w") as f:
        f.write(json.dumps(data, indent=2))

def generate_account_no():
    alpha = random.choices(string.ascii_uppercase, k=6)
    num   = random.choices(string.digits, k=4)
    acc   = alpha + num
    random.shuffle(acc)
    return "VX-" + "".join(acc)

def find_user(data, accno, pin):
    return next((u for u in data if u["AccountNo"] == accno and u["pin"] == int(pin)), None)


# ─── Session State ────────────────────────────────────────────────────────────
if "data" not in st.session_state:
    st.session_state.data = load_data()

if "page" not in st.session_state:
    st.session_state.page = "home"


# ─── Hero Banner ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
    <p class="hero-title">🏦 VaultX</p>
    <p class="hero-sub">Modern Banking — Secure · Simple · Smart</p>
</div>
""", unsafe_allow_html=True)


# ─── Navigation ──────────────────────────────────────────────────────────────
menu_options = [
    "🏠  Home",
    "➕  Create Account",
    "💰  Deposit",
    "💸  Withdraw",
    "👁️   View Details",
    "✏️   Update Details",
    "🗑️   Delete Account",
]

page = st.radio("", menu_options, horizontal=False, label_visibility="collapsed")
st.markdown("<hr>", unsafe_allow_html=True)


# ─── Pages ────────────────────────────────────────────────────────────────────

# ── HOME ──────────────────────────────────────────────────────────────────────
if page == "🏠  Home":
    data = st.session_state.data
    total_users    = len(data)
    total_balance  = sum(u.get("balance", 0) for u in data)
    avg_balance    = round(total_balance / total_users, 2) if total_users else 0

    st.markdown("### 📊 Bank Overview")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Accounts", total_users)
    with col2:
        st.metric("Total Deposits", f"₹{total_balance:,.2f}")
    with col3:
        st.metric("Avg Balance", f"₹{avg_balance:,.2f}")

    st.markdown("<br>", unsafe_allow_html=True)

    if data:
        st.markdown("### 👥 Recent Accounts")
        for user in reversed(data[-5:]):
            balance = user.get("balance", 0)
            badge_class = "badge-success" if balance > 0 else "badge-warning"
            st.markdown(f"""
            <div class="section-card" style="padding:1rem 1.5rem; margin-bottom:0.75rem;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <div style="color:white; font-weight:600; font-size:1rem;">{user['name']}</div>
                        <div style="color:rgba(255,255,255,0.4); font-size:0.75rem; font-family:'Space Mono', monospace;">{user['AccountNo']}</div>
                    </div>
                    <div style="text-align:right;">
                        <div style="color:#38ef7d; font-family:'Space Mono', monospace; font-weight:700;">₹{balance:,.2f}</div>
                        <span class="{badge_class}">Active</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No accounts yet. Create one to get started!")


# ── CREATE ACCOUNT ────────────────────────────────────────────────────────────
elif page == "➕  Create Account":
    st.markdown("### ➕ Open New Account")
    st.markdown("<p style='color:rgba(255,255,255,0.5); font-size:0.85rem;'>Fill in the details below to create your VaultX account.</p>", unsafe_allow_html=True)

    with st.container():
        name  = st.text_input("Full Name", placeholder="e.g. Rahul Sharma")
        age   = st.number_input("Age", min_value=1, max_value=120, step=1, value=18)
        email = st.text_input("Email Address", placeholder="e.g. rahul@email.com")
        col1, col2 = st.columns(2)
        with col1:
            pin  = st.text_input("4-digit PIN", type="password", max_chars=4, placeholder="••••")
        with col2:
            pin2 = st.text_input("Confirm PIN", type="password", max_chars=4, placeholder="••••")

        if st.button("🚀 Create Account"):
            if not all([name, age, email, pin, pin2]):
                st.error("⚠️ Please fill in all fields.")
            elif age < 12:
                st.error("❌ Minimum age to open an account is 12 years.")
            elif len(pin) != 4 or not pin.isdigit():
                st.error("❌ PIN must be exactly 4 digits.")
            elif pin != pin2:
                st.error("❌ PINs do not match.")
            else:
                acc_no = generate_account_no()
                new_user = {
                    "name": name,
                    "age": int(age),
                    "email": email,
                    "AccountNo": acc_no,
                    "pin": int(pin),
                    "balance": 0
                }
                st.session_state.data.append(new_user)
                save_data(st.session_state.data)

                st.success("✅ Account created successfully!")
                st.markdown(f"""
                <div class="balance-card" style="margin-top:1rem;">
                    <div class="balance-label">Your Account Number</div>
                    <div class="balance-amount" style="font-size:1.6rem; letter-spacing:2px;">{acc_no}</div>
                    <div style="margin-top:0.5rem; opacity:0.8; font-size:0.85rem;">Welcome aboard, {name}! 🎉</div>
                </div>
                """, unsafe_allow_html=True)


# ── DEPOSIT ───────────────────────────────────────────────────────────────────
elif page == "💰  Deposit":
    st.markdown("### 💰 Deposit Money")

    accno  = st.text_input("Account Number", placeholder="VX-XXXXXX")
    pin    = st.text_input("PIN", type="password", max_chars=4, placeholder="••••")
    amount = st.number_input("Amount (₹)", min_value=1, step=100, value=1000)

    if st.button("💳 Deposit Now"):
        user = find_user(st.session_state.data, accno.strip(), pin)
        if not user:
            st.error("❌ Invalid account number or PIN.")
        elif amount <= 0:
            st.error("❌ Enter a valid deposit amount.")
        else:
            user["balance"] += amount
            save_data(st.session_state.data)
            st.success(f"✅ ₹{amount:,.2f} deposited successfully!")
            st.markdown(f"""
            <div class="balance-card">
                <div class="balance-label">New Balance</div>
                <div class="balance-amount">₹{user['balance']:,.2f}</div>
                <div style="margin-top:0.4rem; opacity:0.75; font-size:0.8rem;">
                    Account: {user['AccountNo']} | Holder: {user['name']}
                </div>
            </div>
            """, unsafe_allow_html=True)


# ── WITHDRAW ──────────────────────────────────────────────────────────────────
elif page == "💸  Withdraw":
    st.markdown("### 💸 Withdraw Money")

    accno  = st.text_input("Account Number", placeholder="VX-XXXXXX")
    pin    = st.text_input("PIN", type="password", max_chars=4, placeholder="••••")
    amount = st.number_input("Amount (₹)", min_value=1, step=100, value=500)

    if st.button("🏧 Withdraw"):
        user = find_user(st.session_state.data, accno.strip(), pin)
        if not user:
            st.error("❌ Invalid account number or PIN.")
        elif amount > user["balance"]:
            st.error(f"❌ Insufficient balance. Available: ₹{user['balance']:,.2f}")
        else:
            user["balance"] -= amount
            save_data(st.session_state.data)
            st.success(f"✅ ₹{amount:,.2f} withdrawn successfully!")
            st.markdown(f"""
            <div class="balance-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
                <div class="balance-label">Remaining Balance</div>
                <div class="balance-amount">₹{user['balance']:,.2f}</div>
                <div style="margin-top:0.4rem; opacity:0.75; font-size:0.8rem;">
                    Account: {user['AccountNo']} | Holder: {user['name']}
                </div>
            </div>
            """, unsafe_allow_html=True)


# ── VIEW DETAILS ──────────────────────────────────────────────────────────────
elif page == "👁️   View Details":
    st.markdown("### 👁️ Account Details")

    accno = st.text_input("Account Number", placeholder="VX-XXXXXX")
    pin   = st.text_input("PIN", type="password", max_chars=4, placeholder="••••")

    if st.button("🔍 Fetch Details"):
        user = find_user(st.session_state.data, accno.strip(), pin)
        if not user:
            st.error("❌ Invalid account number or PIN.")
        else:
            initials = "".join(w[0].upper() for w in user["name"].split()[:2])
            balance  = user.get("balance", 0)

            st.markdown(f"""
            <div class="section-card">
                <div style="display:flex; align-items:center; gap:1rem; margin-bottom:1.5rem;">
                    <div style="width:56px; height:56px; border-radius:50%;
                                background: linear-gradient(135deg, #667eea, #764ba2);
                                display:flex; align-items:center; justify-content:center;
                                font-weight:700; font-size:1.2rem; color:white; flex-shrink:0;">
                        {initials}
                    </div>
                    <div>
                        <div style="color:white; font-weight:600; font-size:1.15rem;">{user['name']}</div>
                        <span class="badge-success">Active Account</span>
                    </div>
                </div>
                <div class="balance-card" style="margin-bottom:1rem;">
                    <div class="balance-label">Current Balance</div>
                    <div class="balance-amount">₹{balance:,.2f}</div>
                </div>
                <div class="info-row"><span class="info-label">Account No.</span>
                    <span class="info-value">{user['AccountNo']}</span></div>
                <div class="info-row"><span class="info-label">Full Name</span>
                    <span class="info-value" style="font-family:'Sora',sans-serif;">{user['name']}</span></div>
                <div class="info-row"><span class="info-label">Age</span>
                    <span class="info-value">{user['age']} yrs</span></div>
                <div class="info-row"><span class="info-label">Email</span>
                    <span class="info-value" style="font-family:'Sora',sans-serif;">{user['email']}</span></div>
                <div class="info-row" style="border:none;"><span class="info-label">PIN</span>
                    <span class="info-value">••••</span></div>
            </div>
            """, unsafe_allow_html=True)


# ── UPDATE DETAILS ────────────────────────────────────────────────────────────
elif page == "✏️   Update Details":
    st.markdown("### ✏️ Update Account Details")
    st.markdown("<p style='color:rgba(255,255,255,0.45); font-size:0.82rem;'>Leave fields blank to keep existing values.</p>", unsafe_allow_html=True)

    accno = st.text_input("Account Number", placeholder="VX-XXXXXX")
    pin   = st.text_input("Current PIN", type="password", max_chars=4, placeholder="••••")

    if accno and pin:
        user = find_user(st.session_state.data, accno.strip(), pin)
        if user:
            st.markdown("<br>", unsafe_allow_html=True)
            new_name  = st.text_input("New Name", placeholder=f"Current: {user['name']}")
            new_email = st.text_input("New Email", placeholder=f"Current: {user['email']}")
            new_pin   = st.text_input("New PIN", type="password", max_chars=4, placeholder="Leave blank to keep current")

            if st.button("💾 Save Changes"):
                changed = []
                if new_name.strip():
                    user["name"] = new_name.strip()
                    changed.append("name")
                if new_email.strip():
                    user["email"] = new_email.strip()
                    changed.append("email")
                if new_pin.strip():
                    if len(new_pin) == 4 and new_pin.isdigit():
                        user["pin"] = int(new_pin)
                        changed.append("PIN")
                    else:
                        st.error("❌ New PIN must be exactly 4 digits.")
                        st.stop()

                save_data(st.session_state.data)
                if changed:
                    st.success(f"✅ Updated: {', '.join(changed)}")
                else:
                    st.info("ℹ️ No changes were made.")
        else:
            if pin:
                st.error("❌ Invalid account number or PIN.")


# ── DELETE ACCOUNT ────────────────────────────────────────────────────────────
elif page == "🗑️   Delete Account":
    st.markdown("### 🗑️ Delete Account")

    st.markdown("""
    <div style="background:rgba(255,82,82,0.1); border:1px solid rgba(255,82,82,0.3);
                border-radius:12px; padding:1rem 1.25rem; margin-bottom:1.5rem;">
        <div style="color:#ff5252; font-weight:600; margin-bottom:0.25rem;">⚠️ Permanent Action</div>
        <div style="color:rgba(255,255,255,0.6); font-size:0.85rem;">
            Deleting your account is irreversible. All your data and balance will be permanently removed.
        </div>
    </div>
    """, unsafe_allow_html=True)

    accno   = st.text_input("Account Number", placeholder="VX-XXXXXX")
    pin     = st.text_input("PIN", type="password", max_chars=4, placeholder="••••")
    confirm = st.checkbox("I understand this action is permanent and cannot be undone.")

    if st.button("🗑️ Delete My Account", disabled=not confirm):
        user = find_user(st.session_state.data, accno.strip(), pin)
        if not user:
            st.error("❌ Invalid account number or PIN.")
        else:
            name = user["name"]
            st.session_state.data.remove(user)
            save_data(st.session_state.data)
            st.warning(f"🗑️ Account for **{name}** has been permanently deleted.")


# ─── Footer ───────────────────────────────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; color:rgba(255,255,255,0.2); font-size:0.75rem; padding-bottom:2rem;">
    VaultX Banking System · Built with Streamlit · Secured with love 🔐
</div>
""", unsafe_allow_html=True)