"""
🌻 Una flor amarilla para ti — app de Streamlit

INSTALAR:  pip install streamlit
CORRER:    streamlit run app.py
MÚSICA:    pon un archivo "cancion.mp3" junto a este app.py (opcional)

PERSONALIZA solo el bloque "TU CONTENIDO".
Cambia únicamente lo que está entre comillas; nunca el nombre de la variable.
"""

import random
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

# ──────────────────────────────────────────────────────────────
# TU CONTENIDO  (edita solo esto)
# ──────────────────────────────────────────────────────────────

NOMBRE = "Frida"

TITULO = "Hoy 21 de Septiembre..."

NOTA = """
Te traigo una flor amarilla porque hoy me gustaría recordarte cuánto te quiero.

Las flores amarillas son las que se regalan sin motivo, solo porque alguien te alegra
el día con solo existir. Eso haces tú: entras a un cuarto y lo llenas de luz.

Gracias por escucharme sin prisa, por reírte de mis chistes malos y por
quedarte también en los días en que no tengo nada interesante que decir.

Esta flor no se marchita al igual que mi cariño y amistad por ti.
"""

FIRMA = "— Juan Z"

FRASES = [
    "Gracias por estar siempre.",
    "Contigo los días pesados se hacen más ligeros.",
    "Uno de los días más felices de mi vida fue cuando te conocí",
    "Eres de las personas que se quedan, y eso vale muchísimo.",
    "Cuidas a la gente de una forma muy bonita.",
    "Me alegra mucho que seas mi mejor amiga.",
    "Todo es más divertido cuando andas cerca.",
    "Espero que hoy y siempre recuerdes lo especial que eres",
]

CANCION = "cancion.mp3"

# ──────────────────────────────────────────────────────────────

st.set_page_config(page_title=f"Una flor para {NOMBRE} 🌻", page_icon="🌻", layout="centered")

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,600&family=Karla:wght@300;400;600&display=swap');
:root{ --crema:#FFFBF0; --mantequilla:#FFF0C2; --sol:#F9C846; --ambar:#E09B1E; --tierra:#5A4526; }
.stApp{
  background:
    radial-gradient(900px 520px at 50% -8%, #FFE9A8 0%, rgba(255,233,168,0) 62%),
    linear-gradient(180deg, var(--crema) 0%, #FFF6DF 100%);
  background-attachment: fixed;
}
.stApp, .stApp p, .stApp li{ font-family:'Karla', system-ui, sans-serif; color:var(--tierra); }
.block-container{ padding-top:3rem; padding-bottom:4rem; max-width:720px; }
#MainMenu, footer, header{ visibility:hidden; }
iframe{ background:transparent; }

.saludo{ font-size:.95rem; letter-spacing:.14em; color:var(--ambar); text-align:center; margin-bottom:.4rem; }
.titulo{ font-family:'Fraunces',serif; font-weight:600; font-size:clamp(2.4rem,7vw,3.6rem);
         line-height:1.04; text-align:center; margin:0 0 .6rem; }
.titulo em{ font-style:italic; font-weight:300; color:var(--ambar); }
.subtitulo{ text-align:center; font-weight:300; max-width:34ch; margin:0 auto 1.8rem; opacity:.85; }

.stButton > button{
  width:100%; border:none; border-radius:999px; padding:.85rem 1.4rem;
  background:linear-gradient(135deg,var(--sol),var(--ambar));
  color:#3E2F17; font-family:'Karla',sans-serif; font-weight:600; font-size:1.02rem;
  box-shadow:0 10px 24px -10px rgba(224,155,30,.75);
  transition:transform .18s ease, box-shadow .18s ease;
}
.stButton > button:hover{ transform:translateY(-2px); color:#3E2F17;
  box-shadow:0 16px 30px -12px rgba(224,155,30,.9); }
.stButton > button:focus-visible{ outline:3px solid var(--ambar); outline-offset:3px; }

.nota{ position:relative; background:#FFFDF7; border:1px solid #F2E3B8; border-radius:22px;
       padding:2rem 1.9rem 1.6rem; box-shadow:0 26px 50px -34px rgba(90,69,38,.45);
       animation:subir .8s ease-out both .2s; }
@keyframes subir{ from{opacity:0; transform:translateY(22px)} to{opacity:1; transform:none} }
.nota p{ font-family:'Fraunces',serif; font-weight:300; font-size:1.08rem; line-height:1.75; margin:0 0 1rem; }
.nota .firma{ font-family:'Karla',sans-serif; font-weight:600; font-size:.95rem;
              color:var(--ambar); text-align:right; margin:0; }

.frase{ background:var(--mantequilla); border-left:4px solid var(--sol); border-radius:0 16px 16px 0;
        padding:1.1rem 1.3rem; margin:.3rem 0; font-family:'Fraunces',serif; font-size:1.05rem; }

@media (prefers-reduced-motion: reduce){ .nota{ animation:none } }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────
# LA FLOR  ·  se dibuja dentro de un iframe (components.html)
# para que Streamlit no filtre el SVG ni sus animaciones
# ──────────────────────────────────────────────────────────────

def flor_html(n_petalos: int = 14, lluvia: bool = False) -> str:
    petalos = "".join(
        f'<g transform="rotate({i * 360 / n_petalos} 200 195)">'
        f'<ellipse class="petalo" cx="200" cy="108" rx="22" ry="66" fill="url(#oro)" '
        f'style="animation-delay:{0.5 + i * 0.055:.2f}s"/></g>'
        for i in range(n_petalos)
    )

    flores = ""
    if lluvia:
        flores = "".join(
            '<span class="gota" style="left:{l}%;font-size:{s}px;'
            'animation-duration:{d:.1f}s;animation-delay:{r:.1f}s">{e}</span>'.format(
                l=random.randint(0, 95), s=random.randint(16, 32),
                d=random.uniform(3.0, 5.2), r=random.uniform(0, 1.2),
                e=random.choice(["🌻", "🌼", "💛", "🌸"]),
            )
            for _ in range(28)
        )

    return f"""
<!DOCTYPE html><html><head><meta charset="utf-8"><style>
  html,body{{margin:0;background:transparent;overflow:hidden}}
  .maceta{{display:flex;justify-content:center;align-items:flex-start;height:100%}}
  svg{{width:min(440px,88vw);animation:mecer 6.5s ease-in-out infinite;transform-origin:50% 100%}}
  @keyframes mecer{{0%,100%{{transform:rotate(-2.2deg)}}50%{{transform:rotate(2.2deg)}}}}
  .petalo{{transform-box:view-box;transform-origin:200px 195px;
           animation:abrir .8s cubic-bezier(.2,1.5,.4,1) backwards}}
  @keyframes abrir{{from{{transform:scale(.05);opacity:0}}to{{transform:scale(1);opacity:1}}}}
  .centro{{transform-box:view-box;transform-origin:200px 195px;
           animation:latir 3.4s ease-in-out infinite 1.4s}}
  @keyframes latir{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.035)}}}}
  .tallo{{stroke-dasharray:420;stroke-dashoffset:420;animation:crecer 1s ease-out forwards}}
  @keyframes crecer{{to{{stroke-dashoffset:0}}}}
  .hoja{{opacity:0;animation:hojita .6s ease-out forwards .8s}}
  @keyframes hojita{{to{{opacity:1}}}}
  .gota{{position:fixed;top:-10%;animation:caer linear forwards}}
  @keyframes caer{{to{{transform:translateY(120vh) rotate(420deg);opacity:.15}}}}
  @media (prefers-reduced-motion:reduce){{
    svg,.petalo,.centro,.hoja,.gota{{animation:none!important;opacity:1!important;transform:none!important}}
    .tallo{{stroke-dashoffset:0!important;animation:none!important}}
  }}
</style></head><body>
<div class="maceta">
<svg viewBox="0 0 400 430" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-label="Una flor amarilla abriéndose">
  <defs>
    <linearGradient id="oro" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFE68A"/><stop offset="55%" stop-color="#F9C846"/>
      <stop offset="100%" stop-color="#E09B1E"/>
    </linearGradient>
    <radialGradient id="corazon">
      <stop offset="0%" stop-color="#8A6A2F"/><stop offset="100%" stop-color="#4E3A17"/>
    </radialGradient>
  </defs>
  <path class="tallo" d="M200 240 C 196 300, 204 350, 200 424" stroke="#7FA653"
        stroke-width="9" stroke-linecap="round" fill="none"/>
  <path class="hoja" d="M200 320 C 152 300, 128 330, 132 356 C 166 362, 192 348, 200 320 Z" fill="#7FA653"/>
  <path class="hoja" d="M200 366 C 246 348, 272 376, 266 400 C 232 404, 208 392, 200 366 Z"
        fill="#6E9349" style="animation-delay:1s"/>
  {petalos}
  <circle class="centro" cx="200" cy="195" r="52" fill="url(#corazon)"/>
  <circle class="centro" cx="200" cy="195" r="38" fill="none" stroke="#6B5124" stroke-width="6"
          stroke-dasharray="3 7" stroke-linecap="round" opacity=".7"/>
</svg>
</div>{flores}
</body></html>
"""


# ──────────────────────────────────────────────────────────────

st.session_state.setdefault("abierto", False)
st.session_state.setdefault("frase", None)
st.session_state.setdefault("lluvia", False)

if not st.session_state.abierto:
    st.markdown(f'<p class="saludo">para {NOMBRE}</p>', unsafe_allow_html=True)
    st.markdown(f'<h1 class="titulo">{TITULO}</h1>', unsafe_allow_html=True)
    _, centro, _ = st.columns([1, 2, 1])
    with centro:
        if st.button("Sube el volúmen y da click aquí", use_container_width=True):
            st.session_state.abierto = True
            st.rerun()

else:
    st.markdown(f'<p class="saludo">para {NOMBRE}</p>', unsafe_allow_html=True)

    # la flor, en su propio iframe
    components.html(flor_html(lluvia=st.session_state.lluvia), height=470, scrolling=False)
    st.session_state.lluvia = False  # la lluvia cae una sola vez por clic

    parrafos = "".join(f"<p>{p.strip()}</p>" for p in NOTA.strip().split("\n\n"))
    st.markdown(f'<div class="nota">{parrafos}<p class="firma">{FIRMA}</p></div>',
                unsafe_allow_html=True)

    st.write("")

    # música de fondo (un solo reproductor)
    ruta = Path(__file__).parent / CANCION
    if ruta.exists():
        with st.expander("🎵 Música", expanded=True):
            audio = ruta.read_bytes()
            try:
                st.audio(audio, format="audio/mp3", autoplay=True, loop=True)
            except TypeError:  # Streamlit viejito: sin autoplay/loop
                st.audio(audio, format="audio/mp3")

    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("¿Te digo algo bonito? 💛", use_container_width=True):
            opciones = [f for f in FRASES if f != st.session_state.frase]
            st.session_state.frase = random.choice(opciones or FRASES)
    with col_b:
        if st.button("Lluvia de flores 🌸", use_container_width=True):
            st.session_state.lluvia = True
            st.balloons()
            st.rerun()

    if st.session_state.frase:
        st.markdown(f'<div class="frase">{st.session_state.frase}</div>', unsafe_allow_html=True)

    st.write("")
    if st.button("Volver al inicio", use_container_width=True):
        st.session_state.update(abierto=False, frase=None, lluvia=False)
        st.rerun()