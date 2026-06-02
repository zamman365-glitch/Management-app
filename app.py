import json
import random
import string
from pathlib import Path
import streamlit as st

# ─────────────────────────────────────────────
# Page config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="NovBank",
    page_icon="🏦",
    layout="centered",
)

# ─────────────────────────────────────────────
# Custom CSS — dark luxury aesthetic
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --gold:   #C9A84C;
    --gold2:  #E8C97A;
    --dark:   #0D0D0D;
    --dark2:  #161616;
    --dark3:  #1E1E1E;
    --border: #2A2A2A;
    --muted:  #6B6B6B;
    --white:  #F5F5F0;
}

/* Global reset */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--dark) !important;
    color: var(--white) !important;
}

.stApp {
    background-color: var(--dark) !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }

/* ── Bank Header ── */
.bank-header {
    text-align: center;
    padding: 2.5rem 0 1.5rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 2rem;
}
.bank-logo {
    font-family: 'Playfair Display', serif;
    font-size: 2.6rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    color: var(--gold);
    line-height: 1;
}
.bank-tagline {
    font-size: 0.75rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--muted);
    margin-top: 0.3rem;
}

/* ── Cards / panels ── */
.card {
    background: var(--dark3);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.6rem 2rem;
    margin-bottom: 1.2rem;
}
.card-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    color: var(--gold);
    margin-bottom: 1rem;
    letter-spacing: 0.03em;
}

/* ── Balance chip ── */
.balance-chip {
    display: inline-block;
    background: linear-gradient(135deg, #C9A84C 0%, #E8C97A 100%);
    color: #0D0D0D;
    font-weight: 600;
    font-size: 1.4rem;
    border-radius: 8px;
    padding: 0.4rem 1.1rem;
    letter-spacing: 0.02em;
}

/* ── Account number pill ── */
.acc-pill {
    display: inline-block;
    background: var(--dark2);
    border: 1px solid var(--border);
    color: var(--muted);
    font-size: 0.78rem;
    letter-spacing: 0.18em;
    border-radius: 20px;
    padding: 0.25rem 0.8rem;
    font-family: monospace;
}

/* ── Stat row ── */
.stat-row {
    display: flex;
    gap: 1rem;
    margin: 0.4rem 0;
}
.stat-label {
    color: var(--muted);
    font-size: 0.82rem;
    min-width: 110px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}
.stat-value {
    color: var(--white);
    font-size: 0.92rem;
}

/* ── Tabs ── */
div[data-testid="stTabs"] > div:first-child {
    border-bottom: 1px solid var(--border);
    gap: 0;
}
button[data-baseweb="tab"] {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: var(--muted) !important;
    background: transparent !important;
    border: none !important;
    padding: 0.7rem 1.2rem !important;
}
button[data-baseweb="tab"][aria-selected="true"] {
    color: var(--gold) !important;
    border-bottom: 2px solid var(--gold) !important;
}

/* ── Inputs ── */
div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input {
    background-color: var(--dark2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--white) !important;
    font-family: 'DM Sans', sans-serif !important;
    padding: 0.55rem 0.9rem !important;
}
div[data-testid="stTextInput"] input:focus,
div[data-testid="stNumberInput"] input:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 2px rgba(201,168,76,0.15) !important;
}
label[data-testid="stWidgetLabel"] p {
    color: var(--muted) !important;
    font-size: 0.78rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.12em !important;
}

/* ── Buttons ── */
div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #C9A84C 0%, #A07830 100%) !important;
    color: #0D0D0D !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    padding: 0.55rem 1.6rem !important;
    transition: opacity 0.2s !important;
}
div[data-testid="stButton"] > button:hover {
    opacity: 0.88 !important;
}

/* ── Alerts ── */
div[data-testid="stAlert"] {
    border-radius: 8px !important;
    border: 1px solid var(--border) !important;
    font-size: 0.88rem !important;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: var(--dark2) !important;
    border-right: 1px solid var(--border) !important;
}
section[data-testid="stSidebar"] * {
    color: var(--white) !important;
}

/* ── Selectbox ── */
div[data-testid="stSelectbox"] > div {
    background: var(--dark2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--white) !important;
}

/* ── Divider ── */
hr {
    border-color: var(--border) !important;
    margin: 1.2rem 0 !important;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Bank logic (ported from original)
# ─────────────────────────────────────────────
DATABASE = "database.json"

def load_data():
    p = Path(DATABASE)
    if p.exists():
        with open(p) as f:
            return json.loads(f.read())
    return []

def save_data(data):
    with open(DATABASE, "w") as f:
        f.write(json.dumps(data, indent=2))

def generate_account():
    alpha = random.choices(string.ascii_letters, k=8)
    num   = random.choices(string.digits, k=4)
    acc   = alpha + num
    random.shuffle(acc)
    return "".join(acc)

def find_user(data, accno, pin):
    matches = [u for u in data if u["AccountNo."] == accno and u["pin"] == int(pin)]
    return matches[0] if matches else None

# ─────────────────────────────────────────────
# Header
# ─────────────────────────────────────────────
st.markdown("""
<div class="bank-header">
    <div class="bank-logo">✦ NovBank</div>
    <div class="bank-tagline">Private &amp; Secure Banking</div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Tabs
# ─────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Create Account",
    "Deposit",
    "Withdraw",
    "My Details",
    "Update Info",
    "Close Account",
])

# ─────────────────────────────────── TAB 1 ──
with tab1:
    st.markdown('<div class="card-title">Open a New Account</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name", placeholder="Jane Doe")
        age  = st.number_input("Age", min_value=0, max_value=120, step=1, value=None, placeholder="25")
    with col2:
        email = st.text_input("Email Address", placeholder="jane@example.com")
        pin   = st.text_input("4-digit PIN", type="password", placeholder="••••", max_chars=4)

    if st.button("Open Account →", key="create"):
        if not all([name, age, email, pin]):
            st.error("Please fill in all fields.")
        elif int(age) < 12:
            st.error("Applicant must be at least 12 years old.")
        elif len(pin) != 4 or not pin.isdigit():
            st.error("PIN must be exactly 4 digits.")
        else:
            data   = load_data()
            new_acc = generate_account()
            data.append({
                "name":       name,
                "age":        int(age),
                "email":      email,
                "AccountNo.": new_acc,
                "pin":        int(pin),
                "balance":    0,
            })
            save_data(data)
            st.success("Account created successfully!")
            st.markdown(f"""
            <div class="card" style="margin-top:1rem">
                <div class="card-title">Your Account Details</div>
                <div class="stat-row"><span class="stat-label">Name</span><span class="stat-value">{name}</span></div>
                <div class="stat-row"><span class="stat-label">Account No.</span><span class="acc-pill">{new_acc}</span></div>
                <div style="margin-top:0.6rem; font-size:0.78rem; color:var(--muted)">
                    ⚠️ Save your Account Number — you'll need it to log in.
                </div>
            </div>
            """, unsafe_allow_html=True)

# ─────────────────────────────────── TAB 2 ──
with tab2:
    st.markdown('<div class="card-title">Deposit Funds</div>', unsafe_allow_html=True)

    acc_dep = st.text_input("Account Number", key="dep_acc", placeholder="e.g. aB3kXm9z1Q2w")
    pin_dep = st.text_input("PIN", type="password", key="dep_pin", placeholder="••••", max_chars=4)
    amt_dep = st.number_input("Amount (₹)", min_value=1, step=100, key="dep_amt", value=None, placeholder="1000")

    if st.button("Deposit →", key="do_deposit"):
        if not acc_dep or not pin_dep or not amt_dep:
            st.error("Fill all fields.")
        else:
            data = load_data()
            user = find_user(data, acc_dep, pin_dep)
            if not user:
                st.error("Invalid account number or PIN.")
            else:
                user["balance"] += int(amt_dep)
                save_data(data)
                st.success(f"₹{amt_dep:,} deposited successfully.")
                st.markdown(f"""
                <div class="card">
                    <div class="stat-row"><span class="stat-label">Account Holder</span><span class="stat-value">{user['name']}</span></div>
                    <div class="stat-row"><span class="stat-label">New Balance</span>
                        <span class="balance-chip">₹{user['balance']:,}</span>
                    </div>
                </div>""", unsafe_allow_html=True)

# ─────────────────────────────────── TAB 3 ──
with tab3:
    st.markdown('<div class="card-title">Withdraw Funds</div>', unsafe_allow_html=True)

    acc_wd = st.text_input("Account Number", key="wd_acc", placeholder="e.g. aB3kXm9z1Q2w")
    pin_wd = st.text_input("PIN", type="password", key="wd_pin", placeholder="••••", max_chars=4)
    amt_wd = st.number_input("Amount (₹)", min_value=1, step=100, key="wd_amt", value=None, placeholder="500")

    if st.button("Withdraw →", key="do_withdraw"):
        if not acc_wd or not pin_wd or not amt_wd:
            st.error("Fill all fields.")
        else:
            data = load_data()
            user = find_user(data, acc_wd, pin_wd)
            if not user:
                st.error("Invalid account number or PIN.")
            elif int(amt_wd) > user["balance"]:
                st.error(f"Insufficient balance. Available: ₹{user['balance']:,}")
            else:
                user["balance"] -= int(amt_wd)
                save_data(data)
                st.success(f"₹{amt_wd:,} withdrawn successfully.")
                st.markdown(f"""
                <div class="card">
                    <div class="stat-row"><span class="stat-label">Account Holder</span><span class="stat-value">{user['name']}</span></div>
                    <div class="stat-row"><span class="stat-label">Remaining Balance</span>
                        <span class="balance-chip">₹{user['balance']:,}</span>
                    </div>
                </div>""", unsafe_allow_html=True)

# ─────────────────────────────────── TAB 4 ──
with tab4:
    st.markdown('<div class="card-title">Account Details</div>', unsafe_allow_html=True)

    acc_det = st.text_input("Account Number", key="det_acc", placeholder="e.g. aB3kXm9z1Q2w")
    pin_det = st.text_input("PIN", type="password", key="det_pin", placeholder="••••", max_chars=4)

    if st.button("View Details →", key="do_details"):
        if not acc_det or not pin_det:
            st.error("Please enter account number and PIN.")
        else:
            data = load_data()
            user = find_user(data, acc_det, pin_det)
            if not user:
                st.error("Invalid account number or PIN.")
            else:
                st.markdown(f"""
                <div class="card">
                    <div class="card-title">{user['name']}</div>
                    <div class="stat-row"><span class="stat-label">Account No.</span><span class="acc-pill">{user['AccountNo.']}</span></div>
                    <div class="stat-row"><span class="stat-label">Age</span><span class="stat-value">{user['age']}</span></div>
                    <div class="stat-row"><span class="stat-label">Email</span><span class="stat-value">{user['email']}</span></div>
                    <hr>
                    <div class="stat-row"><span class="stat-label">Balance</span>
                        <span class="balance-chip">₹{user['balance']:,}</span>
                    </div>
                </div>""", unsafe_allow_html=True)

# ─────────────────────────────────── TAB 5 ──
with tab5:
    st.markdown('<div class="card-title">Update Account Info</div>', unsafe_allow_html=True)

    acc_upd = st.text_input("Account Number", key="upd_acc", placeholder="e.g. aB3kXm9z1Q2w")
    pin_upd = st.text_input("Current PIN", type="password", key="upd_pin", placeholder="••••", max_chars=4)

    st.markdown("<div style='font-size:0.78rem; color:var(--muted); margin:0.5rem 0;'>Leave fields blank to keep current values.</div>", unsafe_allow_html=True)

    col_u1, col_u2 = st.columns(2)
    with col_u1:
        new_name  = st.text_input("New Name", placeholder="Optional")
    with col_u2:
        new_email = st.text_input("New Email", placeholder="Optional")
    new_pin = st.text_input("New PIN", type="password", placeholder="Optional – 4 digits", max_chars=4)

    if st.button("Save Changes →", key="do_update"):
        if not acc_upd or not pin_upd:
            st.error("Account number and current PIN are required.")
        else:
            data = load_data()
            user = find_user(data, acc_upd, pin_upd)
            if not user:
                st.error("Invalid account number or PIN.")
            else:
                if new_pin and (len(new_pin) != 4 or not new_pin.isdigit()):
                    st.error("New PIN must be exactly 4 digits.")
                else:
                    if new_name:  user["name"]  = new_name
                    if new_email: user["email"] = new_email
                    if new_pin:   user["pin"]   = int(new_pin)
                    save_data(data)
                    st.success("Account updated successfully.")

# ─────────────────────────────────── TAB 6 ──
with tab6:
    st.markdown('<div class="card-title">Close Account</div>', unsafe_allow_html=True)
    st.markdown("<div style='font-size:0.85rem; color:#c0392b; margin-bottom:1rem;'>⚠️ This action is permanent and cannot be undone.</div>", unsafe_allow_html=True)

    acc_del = st.text_input("Account Number", key="del_acc", placeholder="e.g. aB3kXm9z1Q2w")
    pin_del = st.text_input("PIN", type="password", key="del_pin", placeholder="••••", max_chars=4)
    confirm = st.checkbox("I understand this will permanently close my account.")

    if st.button("Close Account →", key="do_delete"):
        if not acc_del or not pin_del:
            st.error("Fill all fields.")
        elif not confirm:
            st.warning("Please confirm you want to close the account.")
        else:
            data = load_data()
            user = find_user(data, acc_del, pin_del)
            if not user:
                st.error("Invalid account number or PIN.")
            else:
                data = [u for u in data if not (u["AccountNo."] == acc_del and u["pin"] == int(pin_del))]
                save_data(data)
                st.success(f"Account for {user['name']} has been permanently closed.")