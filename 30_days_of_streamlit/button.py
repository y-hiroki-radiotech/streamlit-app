import streamlit as st

st.header('st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


def isValidEmail(email):
    # 文字列全体に対して、@で始まらないこと、スペースが存在しないこと、@が一つのみであることを確認する
    if email.find('@') > 0:
        if email.find(' ') == -1:
            if email.count('@') == 1:
                # 文字列全体に対して確認が終わったので、@の後ろに.を確認する
                if email.find('@') < email.find('.'):
                    return True
    return False