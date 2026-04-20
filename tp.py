# app.py

import streamlit as st
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import io

# -------------------------------
# 1. Load Models
# -------------------------------
@st.cache_resource
def load_model(model_name):
    processor = BlipProcessor.from_pretrained(model_name)
    model = BlipForConditionalGeneration.from_pretrained(model_name)
    return processor, model

# Sidebar - Model Selection
st.sidebar.title("⚙️ Settings")
model_choice = st.sidebar.selectbox(
    "Choose a model:",
    [
        "Salesforce/blip-image-captioning-base",
        "Salesforce/blip-image-captioning-large",
    ]
)

processor, model = load_model(model_choice)

# Move model to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# -------------------------------
# 2. App Title & Description
# -------------------------------
st.title("🖼️ Image Caption Generator")


st.markdown("""
### 📌 Features
- Choose different BLIP models
- Generate **multiple captions** with beam search
- Download or copy captions
""")

# -------------------------------
# 3. File Uploader
# -------------------------------
uploaded_file = st.file_uploader("📂 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load and show image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="📸 Uploaded Image", use_column_width=True)

    # Caption Generation Options
    st.sidebar.subheader("🔧 Caption Settings")
    num_beams = st.sidebar.slider("Beam Search (quality)", 1, 10, 3)
    max_len = st.sidebar.slider("Max Caption Length", 10, 50, 30)

    # Generate Caption
    with st.spinner("✨ Generating caption..."):
        inputs = processor(images=image, return_tensors="pt").to(device)
        output = model.generate(**inputs, num_beams=num_beams, max_length=max_len)
        caption = processor.decode(output[0], skip_special_tokens=True)

    # Show Caption
    st.success("✅ Caption Generated!")
    st.markdown(f"### 📝 Caption: *{caption}*")

    # Download Caption
    caption_bytes = io.BytesIO(caption.encode())
    st.download_button("⬇️ Download Caption", caption_bytes, "caption.txt")

    # Option to save dataset entry
    if st.button("💾 Save to Dataset"):
        with open("captions_dataset.csv", "a", encoding="utf-8") as f:
            f.write(f"{uploaded_file.name},{caption}\n")
        st.info("Saved to captions_dataset.csv ✅")



        
