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
    <div style="border: 2px solid #4CAF50; border-radius: 10px; padding: 20px; background-color: #f9f9f9; max-width: 600px; margin: auto;">
        <h2>Classificação do IMC</h2>
        <ul>
            <li>Abaixo de 18,5: Abaixo do peso</li>
            <li>18,5 a 24,9: Peso normal</li>
            <li>25 a 29,9: Sobrepeso</li>
            <li>30 a 34,9: Obesidade grau I</li>
            <li>35 a 39,9: Obesidade grau II</li>
            <li>40 ou mais: Obesidade grau III (ou mórbida)</li>
        </ul>
    </div>
    <br><br>
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