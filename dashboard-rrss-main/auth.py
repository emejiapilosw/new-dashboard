import streamlit as st
import bcrypt


def check_password(username: str, password: str) -> bool:
    if "users" not in st.secrets:
        return False
    if username not in st.secrets["users"]:
        return False
    stored_hash = st.secrets["users"][username].encode()
    return bcrypt.checkpw(password.encode(), stored_hash)


def login() -> bool:
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if st.session_state.authenticated:
        return True

    def _clear_login_inputs():
        st.session_state["login_user"] = ""
        st.session_state["login_pass"] = ""

    # Centered premium card
    left, center, right = st.columns([1.15, 1.0, 1.15])

    with center:
        st.markdown(
            """<div class="glass hero" style="padding:1.25rem 1.25rem;">
                <div class="pill">🔐 Acceso</div>
                <div style="font-size:1.6rem;font-weight:800;margin-top:.65rem;">Dashboard RRSS</div>
                <div style="color:var(--muted);margin-top:.3rem;">
                    Inicia sesión para ver KPIs y comparativos de performance.
                </div>
            </div>""",
            unsafe_allow_html=True,
        )

        st.markdown("""<div style="height:.75rem;"></div>""", unsafe_allow_html=True)

        username = st.text_input("Usuario", placeholder="Tu usuario", key="login_user")
        password = st.text_input("Contraseña", type="password", placeholder="Tu contraseña", key="login_pass")

        c1, c2 = st.columns([1, 1])
        with c1:
            submit = st.button("Ingresar", use_container_width=True)
        with c2:
            st.button("Limpiar", use_container_width=True, on_click=_clear_login_inputs)

        if submit:
            if check_password(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Credenciales incorrectas")

        st.caption("Tip: si estás en modo demo, revisa los usuarios en *Secrets* de Streamlit.")

    return False


def logout() -> None:
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()
