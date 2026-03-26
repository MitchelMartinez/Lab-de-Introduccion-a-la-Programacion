import streamlit as st
import base64

class LoginStreamlitApp:
    def __init__(self) -> None:
        self.usuario_correcto = "admin"
        self.contrasena_correcta = "Admin2026"

        if "autenticado" not in st.session_state:
            st.session_state.autenticado = False

    # 🔹 Convertir imagen a base64
    def get_base64(self, file):
        with open(file, "rb") as f:
            return base64.b64encode(f.read()).decode()

    def ejecutar(self) -> None:
        st.set_page_config(page_title="Login Streamlit", page_icon="🔐", layout="wide")

        # 🌌 Fondo (usa tu imagen local)
        bg = self.get_base64("fondo.jpg")

        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bg}");
            background-size: cover;
            background-position: center;
        }}

        .card {{
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.6);
            transition: 0.3s;
        }}

        .card:hover {{
            transform: scale(1.05);
        }}

        .card-img {{
            height: 200px;
            background-size: cover;
            background-position: center;
        }}

        .card-body {{
            padding: 20px;
            background: linear-gradient(135deg, #800020, #4B0000);
            color: white;
            text-align: center;
        }}

        .card-title {{
            font-size: 22px;
            font-weight: bold;
        }}

        </style>
        """, unsafe_allow_html=True)

        if st.session_state.autenticado:
            self.mostrar_menu()
        else:
            self.mostrar_login()

    def mostrar_login(self) -> None:
        st.title("🔐 Login")

        with st.form("form_login"):
            usuario = st.text_input("Usuario")
            contrasena = st.text_input("Contraseña", type="password")
            enviar = st.form_submit_button("Ingresar", use_container_width=True)

        if enviar:
            if usuario.strip() == self.usuario_correcto and contrasena.strip() == self.contrasena_correcta:
                st.session_state.autenticado = True
                st.rerun()
            else:
                st.error("Credenciales incorrectas")

    def mostrar_menu(self) -> None:
        # ❌ X = cerrar sesión
        col1, col2 = st.columns([10,1])
        with col2:
            if st.button("❌"):
                st.session_state.autenticado = False
                st.rerun()

        st.title("🌌 Menú del sistema")

        col1, col2, col3 = st.columns(3)

        # 🪐 PLANETA
        planeta = self.get_base64("planeta.png")
        with col1:
            st.markdown(f"""
            <div class="card">
                <div class="card-img" style="background-image:url('data:image/jpg;base64,{planeta}');"></div>
                <div class="card-body">
                    <div class="card-title">Clasificar número</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # 🕳️ AGUJERO NEGRO
        agujero = self.get_base64("agujero.jpg")
        with col2:
            st.markdown(f"""
            <div class="card">
                <div class="card-img" style="background-image:url('data:image/jpg;base64,{agujero}');"></div>
                <div class="card-body">
                    <div class="card-title">Categoría de edad</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # ✨ CUÁSAR
        cuasar = self.get_base64("cuasar.jpg")
        with col3:
            st.markdown(f"""
            <div class="card">
                <div class="card-img" style="background-image:url('data:image/jpg;base64,{cuasar}');"></div>
                <div class="card-body">
                    <div class="card-title">Calcular tarifa</div>
                </div>
            </div>
            """, unsafe_allow_html=True)


# Ejecutar app
app = LoginStreamlitApp()
app.ejecutar()