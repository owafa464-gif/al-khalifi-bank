import streamlit as st
import pandas as pd

st.set_page_config(page_title="مصرف الخليفي - نظام حقيقي", page_icon="🏦", layout="wide")

# --- ذاكرة المصرف ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "accounts" not in st.session_state:
    st.session_state.accounts = {
        "1001 - أحمد الخليفي": 15000,
        "1002 - وفاء علي": 12000,
        "1003 - محمد سالم": 19200,
    }
if "history" not in st.session_state:
    st.session_state.history = []

# --- تسجيل الدخول ---
def login_page():
    st.title("🏦 مصرف الخليفي - تسجيل دخول")
    st.warning("🔐 منظومة حقيقية محمية - خاص بالإدارة فقط")
    u = st.text_input("اسم المستخدم")
    p = st.text_input("كلمة المرور", type="password")
    if st.button("دخول للمنظومة", type="primary"):
        if u == "admin" and p == "Khalifi2026":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("خطأ في البيانات - تأكدي من الحروف")

if not st.session_state.logged_in:
    login_page()
    st.stop()

# --- بعد الدخول - المنظومة الحقيقية ---
st.sidebar.title("🏦 لوحة التحكم")
st.sidebar.success("الموظف: admin")
if st.sidebar.button("تسجيل خروج"):
    st.session_state.logged_in = False
    st.rerun()

st.title("🏦 مصرف الخليفي - النظام المصرفي الحقيقي")
total = sum(st.session_state.accounts.values())
c1, c2, c3 = st.columns(3)
c1.metric("إجمالي الأرصدة", f"{total} د.ل")
c2.metric("عدد العملاء", len(st.session_state.accounts))
c3.metric("حالة النظام", "يعمل ✅")

st.divider()

# --- عمليات السحب والإيداع ---
st.subheader("💸 تنفيذ عملية مصرفية حقيقية")

col1, col2, col3, col4 = st.columns(4)
with col1:
    client = st.selectbox("اختار العميل", list(st.session_state.accounts.keys()))
with col2:
    amount = st.number_input("المبلغ (د.ل)", min_value=100, step=100)
with col3:
    op = st.radio("نوع العملية", ["إيداع 💰", "سحب 💸"])
with col4:
    st.write("")
    st.write("")
    do_it = st.button("تنفيذ الآن ✅", type="primary", use_container_width=True)

if do_it:
    current = st.session_state.accounts[client]
    if "سحب" in op:
        if current >= amount:
            st.session_state.accounts[client] -= amount
            st.session_state.history.append(f"سحب {amount} من {client} - الرصيد الجديد {st.session_state.accounts[client]}")
            st.success(f"تم سحب {amount} د.ل من {client} بنجاح! الرصيد الجديد: {st.session_state.accounts[client]}")
        else:
            st.error(f"رصيد غير كافي! رصيد {client} هو {current} فقط")
    else:
        st.session_state.accounts[client] += amount
        st.session_state.history.append(f"إيداع {amount} الى {client} - الرصيد الجديد {st.session_state.accounts[client]}")
        st.success(f"تم إيداع {amount} د.ل الى {client} بنجاح! الرصيد الجديد: {st.session_state.accounts[client]}")
    st.rerun()

st.divider()

c_a, c_b = st.columns([2,1])
with c_a:
    st.subheader("📋 أرصدة العملاء الحالية")
    df = pd.DataFrame(list(st.session_state.accounts.items()), columns=["الحساب", "الرصيد"])
    st.dataframe(df, use_container_width=True)

with c_b:
    st.subheader("📜 سجل العمليات")
    if st.session_state.history:
        for h in reversed(st.session_state.history[-10:]):
            st.text(f"• {h}")
    else:
        st.info("لم تتم أي عملية بعد")
