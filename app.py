import streamlit as st
import random
import time
from datetime import datetime

# 1. SITE CONFIGURATION
st.set_page_config(
    page_title="LUMINA | Premium Electronics",
    layout="wide",
    page_icon="💎",
    initial_sidebar_state="expanded"
)

# 2. DESIGN SYSTEM
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@300;600;800&display=swap');
    
    :root {
        --bg-light: #FBFBFD;
        --card-bg: #FFFFFF;
        --primary: #000000;
        --accent: #0071E3;
        --text-main: #1D1D1F;
        --text-dim: #86868B;
        --border: #D2D2D7;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: var(--bg-light);
    }

    .nav-header {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(20px);
        padding: 0.8rem 5%;
        margin: -5rem -5rem 0rem -5rem;
        border-bottom: 1px solid rgba(0,0,0,0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: sticky;
        top: 0;
        z-index: 999;
    }

    /* Sub-nav for Categories */
    .category-bar {
        display: flex;
        justify-content: center;
        gap: 2rem;
        padding: 1rem 0;
        background: var(--bg-light);
        border-bottom: 1px solid var(--border);
        margin-bottom: 2rem;
    }

    div.stButton > button {
        border-radius: 8px !important;
    }
    
    .buy-now-btn button {
        background-color: var(--accent) !important;
        color: white !important;
        border: none !important;
        width: 100%;
    }

    .add-bag-btn button {
        background-color: transparent !important;
        color: var(--accent) !important;
        border: 1px solid var(--accent) !important;
        width: 100%;
    }

    /* Category Pill Styling */
    .stSelectbox label { display: none; }
    </style>
""", unsafe_allow_html=True)

# 3. DATA ENGINE
@st.cache_data
def load_curated_catalog():
    product_images = {
        "Lumina Book Air": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=600",
        "Titan Desktop G1": "https://images.unsplash.com/photo-1587831990711-23ca6441447b?w=600",
        "Vision Monitor 32\"": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=600",
        "Lumina Echo Pro": "https://images.unsplash.com/photo-1589003077984-894e133dabab?w=600",
        "Sonic Wireless Buds": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=600",
        "Studio Over-Ear": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600",
        "Lumina Phone 12": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=600",
        "Phone 12 Ultra": "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=600",
        "Focus X1 Camera": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=600",
        "Aura Hub": "https://images.unsplash.com/photo-1558002038-103792e17734?w=600",
        "Nova Console": "https://images.unsplash.com/photo-1486401899868-0e435ed85128?w=600",
        "Lumina VR Visor": "https://images.unsplash.com/photo-1622979135225-d2ba269cf1ac?w=600",
        "PureAir Purifier": "https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=600",
        "Smart Lock Pro": "https://images.unsplash.com/photo-1550009158-9ebf69173e03?w=600",
        "Cinema Prime Lens": "https://images.unsplash.com/photo-1617005082133-5ec8404396b2?w=600",
    }
    catalog = {
        "Computing": ["Lumina Book Air", "Titan Desktop G1", "Vision Monitor 32\""],
        "Audio": ["Lumina Echo Pro", "Sonic Wireless Buds", "Studio Over-Ear"],
        "Mobile": ["Lumina Phone 12", "Phone 12 Ultra"],
        "Creative": ["Focus X1 Camera", "Cinema Prime Lens"],
        "Smart Home": ["Aura Hub", "PureAir Purifier", "Smart Lock Pro"],
        "Gaming": ["Nova Console", "Lumina VR Visor"]
    }
    db = {}
    i = 0
    for cat, items in catalog.items():
        for name in items:
            pid = f"LMN-{2000 + i}"
            db[pid] = {
                "name": name,
                "cat": cat,
                "price": random.choice([149.00, 599.00, 999.00, 1299.00]),
                "img": product_images.get(name, "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=600")
            }
            i += 1
    return db

PRODUCTS = load_curated_catalog()

if 'cart' not in st.session_state: st.session_state.cart = {}
if 'page' not in st.session_state: st.session_state.page = "store"
if 'selected_cat' not in st.session_state: st.session_state.selected_cat = "All Departments"

# --- NAVBAR ---
st.markdown(f"""
    <div class="nav-header">
        <div style='font-family: "Outfit"; font-weight: 800; font-size: 1.5rem; letter-spacing: -1.5px;'>LUMINA</div>
        <div style='display: flex; gap: 30px; align-items: center;'>
            <div style='font-size: 1rem; font-weight: 500; color: var(--text-dim);'>Support</div>
            <div style='font-size: 1rem; font-weight: 500; color: var(--text-dim);'>Account</div>
            <div style='background: black; color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;'>
                Bag: {sum(st.session_state.cart.values())}
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# ---------------- STORE FRONT ----------------
if st.session_state.page == "store":
    # --- CATEGORY SUB-NAV ---
    categories = ["All Departments"] + sorted(list(set(p['cat'] for p in PRODUCTS.values())))
    
    # We use columns to simulate a centered horizontal menu
    cat_cols = st.columns(len(categories))
    for i, cat in enumerate(categories):
        with cat_cols[i]:
            # Highlight the selected category
            is_active = st.session_state.selected_cat == cat
            if st.button(cat, key=f"cat_{cat}", use_container_width=True, type="secondary" if not is_active else "primary"):
                st.session_state.selected_cat = cat
                st.rerun()

    st.markdown("---")

    # Filtered Items
    display_items = [
        (pid, item) for pid, item in PRODUCTS.items() 
        if st.session_state.selected_cat == "All Departments" or item['cat'] == st.session_state.selected_cat
    ]

    if not display_items:
        st.info("No products found in this category.")
    else:
        # Grid Display
        for i in range(0, len(display_items), 3):
            cols = st.columns(3)
            for idx, (pid, item) in enumerate(display_items[i : i + 3]):
                with cols[idx]:
                    with st.container(border=True):
                        st.image(item['img'], use_container_width=True)
                        st.caption(item['cat'])
                        st.markdown(f"**{item['name']}**")
                        st.markdown(f"### ${item['price']:,.2f}")
                        
                        b1, b2 = st.columns(2)
                        with b1:
                            st.markdown('<div class="buy-now-btn">', unsafe_allow_html=True)
                            if st.button("Buy Now", key=f"buy_{pid}"):
                                st.session_state.cart = {pid: 1}
                                st.session_state.page = "checkout"
                                st.rerun()
                            st.markdown('</div>', unsafe_allow_html=True)
                        with b2:
                            st.markdown('<div class="add-bag-btn">', unsafe_allow_html=True)
                            if st.button("Add to Bag", key=f"add_{pid}"):
                                st.session_state.cart[pid] = st.session_state.cart.get(pid, 0) + 1
                                st.toast(f"Added {item['name']}")
                            st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.cart:
        st.sidebar.subheader("Shopping Bag")
        for pid, qty in st.session_state.cart.items():
            st.sidebar.write(f"**{PRODUCTS[pid]['name']}** (x{qty})")
        if st.sidebar.button("Go to Checkout", use_container_width=True):
            st.session_state.page = "checkout"
            st.rerun()

# ---------------- CHECKOUT ----------------
elif st.session_state.page == "checkout":
    st.markdown("## Checkout")
    col1, col2 = st.columns([1.8, 1])
    
    with col1:
        if st.button("← Back"):
            st.session_state.page = "store"
            st.rerun()
            
        st.subheader("Payment Details")
        pay_type = st.radio("Method", ["Card", "Apple Pay", "Crypto"], horizontal=True)
        
        with st.container(border=True):
            if pay_type == "Card":
                st.text_input("Card Number")
                c1, c2 = st.columns(2)
                c1.text_input("Expiry")
                c2.text_input("CVV")
            elif pay_type == "Apple Pay":
                st.success("Apple Pay detected. Verify with TouchID/FaceID.")
            else:
                st.code("bc1qxy2kgdy6jrsqqyq2...")

    with col2:
        st.subheader("Summary")
        with st.container(border=True):
            sub = sum(PRODUCTS[p]['price'] * q for p, q in st.session_state.cart.items())
            st.write(f"Subtotal: ${sub:,.2f}")
            st.write(f"Tax: ${sub*0.08:,.2f}")
            st.divider()
            st.write(f"### Total: ${sub*1.08:,.2f}")
            if st.button("Place Order", type="primary", use_container_width=True):
                st.balloons()
                st.session_state.cart = {}
                time.sleep(2)
                st.session_state.page = "store"
                st.rerun()

st.markdown("<br><center><p style='color: #86868B; font-size: 0.7rem;'>LUMINA 2026. Designed in California.</p></center>", unsafe_allow_html=True)