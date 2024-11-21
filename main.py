import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import os
import base64

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

client = OpenAI()

st.title("Descrição de Imagens com GPT-4o-mini")

uploaded_file = st.file_uploader("Escolha uma imagem...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1]
    save_path = f"image.{file_extension}"
    print(save_path)
    
    with open(save_path, "wb+") as f:
        f.write(uploaded_file.read())
        f.seek(0)
        imagem_base64 = base64.b64encode(f.read()).decode('utf-8')


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Descreva a imagem fornecida"
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{imagem_base64}"}
                    }
                ]
            }],
        max_tokens=300,
    )

    image_description = response.choices[0].message.content
    
    st.write(image_description)
