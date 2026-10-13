import streamlit as st
import pandas as pd

st.set_page_config(page_title="مصرف الخليفي", layout="wide")
st.title("🏦 مصرف الخليفي - Al Khalifi Bank")
st.write("نظام إدارة الحسابات - بنغازي")

accounts = [
    {"رقم الحساب": "1001", "الاسم": "أحمد محمد", "الرصيد": 12500},
    {"رقم الحساب": "1002", "الاسم": "فاطمة علي", "الرصيد": 8700},
    {"رقم الحساب": "1003", "الاسم": "محمد الخليفي", "الرصيد": 25000},
]

df = pd.DataFrame(accounts)
st.table(df)
st.success("النظام يعمل بنجاح ✅")
st.metric("إجمالي الأرصدة", f"{df['الرصيد'].sum()} د.ل")