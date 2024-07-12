import streamlit as st

st.set_page_config(
page_title=" Nutriview",
page_icon="🏋🏻‍♂️",

)

st.title("Cálculo de necessidade calórica diária")
st.divider()

st.write("""
    O sistema usa a fórmula de Mifflin-St Jeor que é amplamente aceita e considerada mais precisa do que a fórmula de Harris-Benedict, 
    especialmente para a população moderna.
    
    A fórmula é utilizada para calcular a Taxa Metabólica Basal (TMB), 
    a quantidade mínima de calorias que seu corpo precisa em repouso para funcionar. 
    
    A TMB pode ser ajustada para levar em consideração o nível de atividade física, resultando na TDEE (Total Daily Energy Expenditure), 
    ou Gasto Energético Diário Total.
    
    Vamos calcular a necessidade calórica levando em consideração sua altura, idade, peso e fatores de atividade física informados.
""")

altura_input = st.text_input("Altura (cm)", "")
peso_input = st.text_input("Peso (kg)", "")
idade_input = st.text_input("Idade (anos)", "")

sexo = st.radio("Sexo", ["Masculino", "Feminino"])

atividade = st.selectbox("Grau de atividade física", ("Sedentário", "Levemente ativo", "Moderadamente ativo", "Altamente ativo", "Extremamente ativo"))

calcular = st.button("Calcular")

if calcular:
    # Verificar se os inputs não estão vazios
    if altura_input and peso_input and idade_input:
        altura = int(altura_input)
        peso = int(peso_input)
        idade = int(idade_input)
        
        if sexo == "Masculino":
            tmb = (10 * peso) + (6.25 * altura) - (5 * idade) + 5 
        elif sexo == "Feminino":           
            tmb = (10 * peso) + (6.25 * altura) - (5 * idade) - 161
        else:
            tmb = 0  # Valor padrão, caso não seja Masculino ou Feminino

        # Definir o fator de atividade
        if atividade == "Sedentário":
            fator_atividade = 1.2
        elif atividade == "Levemente ativo":
            fator_atividade = 1.375
        elif atividade == "Moderadamente ativo":
            fator_atividade = 1.55
        elif atividade == "Altamente ativo":
            fator_atividade = 1.725
        elif atividade == "Extremamente ativo":
            fator_atividade = 1.9
        else:
            fator_atividade = 0  # Valor padrão, caso não corresponda a uma atividade

        calorias_diarias = tmb * fator_atividade

        st.success(f"Sua TMB é **{round(tmb, 2)}** e sua necessidade calórica diária é **{round(calorias_diarias, 2)}**")
    else:
        st.warning("Por favor, preencha todos os campos.")
