import streamlit as st
import pandas as pd

st.set_page_config(page_title="مصرف الخليفي", page_icon="🏦")

USER = "admin"
PASS = "Khalifi2026"

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.title("🏦 مصرف الخليفي - تسجيل دخول")
    st.info("المنظومة محمية - خاص بالإدارة")
    u = st.text_input("اسم المستخدم")
    p = st.text_input("كلمة المرور", type="password")
    if st.button("دخول"):
        if u == USER and p == PASS:
            st.session_state.login = True
            st.rerun()
        else:
            st.error("خطأ في البيانات!")
    st.stop()

st.title("🏦 مصرف الخليفي - Al Khalifi Bank")
st.success("تم تسجيل الدخول ✅")

if st.button("تسجيل خروج"):
    st.session_state.login = False
    st.rerun()

accounts = [
    {"رقم الحساب": "1001", "الاسم": "أحمد محمد", "الرصيد": 12500},
    {"رقم الحساب": "1002", "الاسم": "فاطمة علي", "الرصيد": 8700},
    {"رقم الحساب": "1003", "الاسم": "محمد الخليفي", "الرصيد": 25000},
]

df = pd.DataFrame(accounts)
st.table(df)
total = df["الرصيد"].sum()
st.metric("إجمالي الأرصدة", f"{total} د.ل")
st.success("النظام يعمل بنجاح - محمي بكلمة مرور 🔐")
