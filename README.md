# 💎 LUMINA — Premium Electronics Store

A modern, Apple-inspired premium electronics storefront built with **Python and Streamlit**.

LUMINA provides a polished shopping experience with product categories, a dynamic shopping bag, checkout flow, multiple payment-method interfaces, and a responsive product grid.

## ✨ Features

* 🛍️ **Premium Electronics Storefront**
* 📦 Product catalog organized by:

  * Computing
  * Audio
  * Mobile
  * Creative
  * Smart Home
  * Gaming
* 🔎 Category-based product filtering
* 🛒 Dynamic shopping bag using Streamlit session state
* ⚡ **Buy Now** and **Add to Bag** functionality
* 💳 Checkout interface with:

  * Card
  * Apple Pay
  * Crypto
* 🧾 Automatic subtotal, tax, and total calculation
* 🎨 Custom premium UI with CSS
* 📱 Responsive three-column product layout
* 🎉 Order confirmation animation
* 🖼️ Product imagery from Unsplash
* ⚡ Cached product catalog for improved performance

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* HTML/CSS
* Streamlit Session State
* Unsplash image URLs

## 📁 Project Structure

```text
LUMINA/
│
├── app.py
├── README.md
└── requirements.txt
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/lumina-store.git
cd lumina-store
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

Create a `requirements.txt` file containing:

```text
streamlit
```

Then run:

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🛒 How It Works

### Product Catalog

The application generates a curated product catalog containing products across six departments. Product information includes a product ID, name, category, price, and image.

### Shopping Bag

The shopping bag is maintained using Streamlit's `session_state`. Users can add multiple quantities of products or immediately purchase a product using **Buy Now**.

### Checkout

The checkout page calculates:

```text
Subtotal = Product Price × Quantity
Tax      = Subtotal × 8%
Total    = Subtotal + Tax
```

The interface provides Card, Apple Pay, and Crypto payment options.

## 🎨 Design

LUMINA uses a minimalist premium aesthetic featuring:

* Inter and Outfit typography
* Light background
* White product cards
* Blue accent color
* Rounded buttons
* Sticky navigation
* Responsive product grid
* Apple-inspired visual styling

The application's design system and navigation styling are defined through custom CSS injected into Streamlit.

## ⚠️ Important Notes

This project is currently a **frontend/demo e-commerce application**.

The checkout interface does **not process real payments**, and the product catalog is generated locally rather than connected to a production database.

Prices are randomly selected from a predefined set when the catalog is generated.

For a production application, consider adding:

* Real payment processing
* Database integration
* User authentication
* Persistent shopping carts
* Product search
* Inventory management
* Order history
* Secure payment handling
* Backend/API integration

## 📸 Preview

Add a screenshot of your application here:

```markdown
![LUMINA Store Preview](screenshots/preview.png)
```

## 🔮 Future Improvements

* [ ] Add product search
* [ ] Add product detail pages
* [ ] Add user authentication
* [ ] Connect a database
* [ ] Integrate Stripe or another payment provider
* [ ] Add persistent orders
* [ ] Add inventory tracking
* [ ] Add product reviews and ratings
* [ ] Add dark mode
* [ ] Deploy to Streamlit Community Cloud

## 📄 License

This project is available for educational and personal use.

---

### Made with ❤️ using Python + Streamlit

**LUMINA — Premium Electronics**
