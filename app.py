import streamlit as st
import pandas as pd

st.set_page_config(page_title="Laporan RNS Puskesmas Kota Baru 2026", layout="wide")

st.title("📊 Dashboard Laporan Rujukan Non Spesialistik (RNS)")
st.subheader("Puskesmas Kota Baru - Tahun 2026")

file_path = "RNS PUSKESMAS KOTA BARU 2026.xlsx"

@st.cache_data
def load_data(file):
    xls = pd.ExcelFile(file)
    sheets = xls.sheet_names
    return sheets

try:
    sheets = load_data(file_path)
    selected_sheet = st.sidebar.selectbox("Pilih Bulan (Periode)", sheets)
    
    # Load selected sheet
    df_raw = pd.read_excel(file_path, sheet_name=selected_sheet)
    
    # Display header info
    st.markdown(f"### Periode Bulan: **{selected_sheet} 2026**")
    
    # Extract meta info if possible
    puskesmas = df_raw.iloc[1, 3] if df_raw.shape[0] > 1 else "-"
    pj = df_raw.iloc[2, 3] if df_raw.shape[0] > 2 else "-"
    hp = df_raw.iloc[3, 3] if df_raw.shape[0] > 3 else "-"
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Nama Puskesmas", str(puskesmas).replace(":", "").strip())
    col2.metric("Penanggung Jawab", str(pj).replace(":", "").strip())
    col3.metric("No. HP", str(hp).replace(":", "").strip())
    
    st.divider()
    
    # Read table starting from row 6 or 7
    # Let's inspect data table structure
    df_table = pd.read_excel(file_path, sheet_name=selected_sheet, skiprows=6)
    st.dataframe(df_table, use_container_width=True)

except Exception as e:
    st.error(f"Terjadi kesalahan saat memuat file: {e}")
