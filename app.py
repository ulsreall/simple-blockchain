import streamlit as st
from blockchain import Blockchain

# Inisialisasi blockchain hanya sekali
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = Blockchain()

st.title("🧱 Simple Blockchain Simulator")

# Input transaksi
sender = st.text_input("Pengirim", value="A")
receiver = st.text_input("Penerima", value="B")
if st.button("Tambah Transaksi"):
    data = f"{sender} -> {receiver}"
    st.session_state.blockchain.add_block(data)
    st.success("Transaksi ditambahkan ke blockchain!")

# Tampilkan blockchain
st.subheader("⛓ Blockchain Saat Ini")
for block in st.session_state.blockchain.chain:
    with st.expander(f"Block #{block.index}"):
        st.write(f"📅 Timestamp: {block.timestamp}")
        st.write(f"📄 Data: {block.data}")
        st.write(f"🔢 Nonce: {block.nonce}")
        st.write(f"🔗 Hash: `{block.hash}`")
        st.write(f"⬅️ Prev Hash: `{block.previous_hash}`")

# Validasi
st.subheader("✅ Validasi Blockchain")
is_valid = st.session_state.blockchain.is_valid()
st.write("Status:", "🟢 Valid" if is_valid else "🔴 Tidak Valid")
