mkdir -p ~/.streamlit/

echo "\
[theme]
primaryColor="#FF3B3F"
base="dark"
backgroundColor="#F5F5F5"
secondaryBackgroundColor="#85A7FF"
font="roboto"
textColor="#000000"

[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml