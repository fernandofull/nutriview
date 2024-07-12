import streamlit as st

st.set_page_config(
page_title=" Nutriview",
page_icon="🏋🏻‍♂️",

)

st.title("Cálculo de IMC")
st.divider()

st.write("""
O Índice de Massa Corporal (IMC) é uma medida usada para avaliar se uma pessoa está em um peso saudável em relação à sua altura.
""")

st.write("""
As categorias ajudam a identificar se uma pessoa está em uma faixa de peso saudável, 
mas é importante lembrar que o IMC é apenas um indicador e não substitui uma avaliação médica completa.
         


""")


st.markdown(
    """
    <div class="card" style="padding: 20px; max-width: 600px; margin: auto;">
        <h2 class="card-title">Classificação do IMC</h2>
        <ul class="list-group list-group-flush">
            <li class="list-group-item">Abaixo de 18,5: Abaixo do peso</li>
            <li class="list-group-item">18,5 a 24,9: Peso normal</li>
            <li class="list-group-item">25 a 29,9: Sobrepeso</li>
            <li class="list-group-item">30 a 34,9: Obesidade grau I</li>
            <li class="list-group-item">35 a 39,9: Obesidade grau II</li>
            <li class="list-group-item">40 ou mais: Obesidade grau III (ou mórbida)</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# unsafe_allow_html=True permite que o streamlite processe html.

altura = st.text_input("Altura (cm)")
peso = st.text_input("Peso (kg)" )



calcular = st.button("Calcular")

if calcular:
    if altura and peso:
        imc = int(peso) / ((int(altura) / 100) ** 2)
        st.success(f"Seu IMC é **{round(imc, 2)}**")

    else:
        st.warning("Preencha todos os campos")