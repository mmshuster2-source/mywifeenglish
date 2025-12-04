import streamlit as st
import streamlit.components.v1 as components

# Настройка страницы
st.set_page_config(layout="wide")

# Читаем твой HTML файл
# Убедись, что файл index.html лежит рядом с этим скриптом в репозитории
try:
    with open("index.html", "r", encoding="utf-8") as f:
        source_code = f.read()
    
    # Выводим его на экран
    components.html(source_code, height=800, scrolling=True)
except FileNotFoundError:
    st.error("Файл index.html не найден в репозитории!")