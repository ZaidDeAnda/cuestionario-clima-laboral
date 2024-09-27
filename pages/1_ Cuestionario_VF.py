import streamlit as st

from utils.config import Config
from utils.database import get_mongo_client

st.header("Evaluación clima laboral 2024")

st.write("Favor de responder a la siguiente encuesta haciendo click en las cajas para un 'Sí' y dejando vacía para un 'No'")

form_dict = {}

with st.form("formulario"):

    form_dict["secretaria"] = st.text_input("Subsecretaría y/o dirección a la que perteneces")

    st.subheader("Liderazgo")

    liderazo_cols = st.columns([4,1])

    liderazo_cols[0].write("Se preocupa mi jefe por transmitir los valores, la misión y objetivos de la secretaría")
    form_dict["liderazgo_1"] = liderazo_cols[1].checkbox("Sí/No", key="liderazgo_1")

    liderazo_cols[0].write("Mis tareas y objetivos están definidos claramente por parte de mi jefe")
    form_dict["liderazgo_2"] = liderazo_cols[1].checkbox("Sí/No", key="liderazgo_2")

    liderazo_cols[0].write("El trato por parte de mi jefe es justo y evita favoritismos.")
    form_dict["liderazgo_3"] = liderazo_cols[1].checkbox("Sí/No", key="liderazgo_3")

    liderazo_cols[0].write("Recibo retroalimentación constantemente de mi jefe para corregir y hacer mejor mi trabajo.")
    form_dict["liderazgo_4"] = liderazo_cols[1].checkbox("Sí/No", key="liderazgo_4")

    st.divider()

    st.subheader("Crecimiento y desarrollo")

    crecimiento_cols = st.columns([4,1])

    crecimiento_cols[0].write("La capacitación que recibo me ayuda para hacer mi trabajo eficiente.")
    form_dict["crecimiento_1"] = crecimiento_cols[1].checkbox("Sí/No", key="crecimiento_1")

    crecimiento_cols[0].write("Existen en la Secretaría planes de carrera y desarrollo para los servidores públicos.")
    form_dict["crecimiento_2"] = crecimiento_cols[1].checkbox("Sí/No", key="crecimiento_2")

    crecimiento_cols[0].write("En la Secretaría se cuenta con un proceso de evaluación de desempeño que me sirve para mejorar en mi trabajo y crecer profesionalmente.")
    form_dict["crecimiento_3"] = crecimiento_cols[1].checkbox("Sí/No", key="crecimiento_3")

    crecimiento_cols[0].write("Cuando hay una vacante, ¿primero se considera buscar un candidato interno de la Secretaría?")
    form_dict["crecimiento_4"] = crecimiento_cols[1].checkbox("Sí/No", key="crecimiento_4")

    st.divider()

    st.subheader("Trabajo en equipo")

    equipo_cols = st.columns([4,1])

    equipo_cols[0].write("Estoy consciente de cómo mi trabajo contribuye a la realización de los objetivos del área.")
    form_dict["equipo_1"] = equipo_cols[1].checkbox("Sí/No", key="equipo_1")

    equipo_cols[0].write("Me siento parte de un equipo de trabajo.")
    form_dict["equipo_2"] = equipo_cols[1].checkbox("Sí/No", key="equipo_2")

    equipo_cols[0].write("Considero que en mi equipo, en ocasiones, modificamos la manera de trabajar para bien de la Secretaría.")
    form_dict["equipo_3"] = equipo_cols[1].checkbox("Sí/No", key="equipo_3")

    st.divider()

    st.subheader("Beneficio y recompensas")

    beneficios_cols = st.columns([4,1])

    beneficios_cols[0].write("Existen diferentes formas de recompensar a los trabajadores.")
    form_dict["beneficios_1"] = beneficios_cols[1].checkbox("Sí/No", key="beneficios_1")

    beneficios_cols[0].write("La Secretaría realiza ajustes o incrementos de sueldo de forma periódica.")
    form_dict["beneficios_2"] = beneficios_cols[1].checkbox("Sí/No", key="beneficios_2")

    beneficios_cols[0].write("En la Secretaría se otorgan estímulos a los trabajadores para mejorar su desempeño.")
    form_dict["beneficios_3"] = beneficios_cols[1].checkbox("Sí/No", key="beneficios_3")

    st.divider()

    st.subheader("Satisfacción laboral")

    satisfaccion_cols = st.columns([4,1])

    satisfaccion_cols[0].write("Las personas disfrutan trabajar en esta institución.")
    form_dict["satisfaccion_1"] = satisfaccion_cols[1].checkbox("Sí/No", key="satisfaccion_1")

    satisfaccion_cols[0].write("En nuestra Secretaría las personas se sienten satisfechas en el trabajo.")
    form_dict["satisfaccion_2"] = satisfaccion_cols[1].checkbox("Sí/No", key="satisfaccion_2")

    satisfaccion_cols[0].write("Casi nunca pienso en buscar trabajo en otra institución o lugar de trabajo.")
    form_dict["satisfaccion_3"] = satisfaccion_cols[1].checkbox("Sí/No", key="satisfaccion_3")

    st.divider()

    st.subheader("Comunicación")

    comunicacion_cols = st.columns([4,1])

    comunicacion_cols[0].write("Los canales de comunicación en la institución están claramente definidos y son accesibles.")
    form_dict["comunicacion_1"] = comunicacion_cols[1].checkbox("Sí/No", key="comunicacion_1")

    comunicacion_cols[0].write("La comunicación entre mi departamento y otras áreas es constante y de confianza para solucionar problemas.")
    form_dict["comunicacion_2"] = comunicacion_cols[1].checkbox("Sí/No", key="comunicacion_2")

    comunicacion_cols[0].write("Los cambios y asuntos importantes de la Secretaría son comunicados a todo el personal.")
    form_dict["comunicacion_3"] = comunicacion_cols[1].checkbox("Sí/No", key="comunicacion_3")

    st.divider()

    st.subheader("Inclusión")

    inclusion_cols = st.columns([4,1])

    inclusion_cols[0].write("En la Secretaría hay un ambiente de respeto y no discriminación hacia las diferencias y preferencias sexuales.")
    form_dict["inclusion_1"] = inclusion_cols[1].checkbox("Sí/No", key="inclusion_1")

    inclusion_cols[0].write("En mi área de trabajo cuento con espacios, mobiliario y equipo adecuado para que todo el personal pueda laborar, incluyendo al personal con discapacidad.")
    form_dict["inclusion_2"] = inclusion_cols[1].checkbox("Sí/No", key="inclusion_2")

    inclusion_cols[0].write("Si reporto algún asunto relacionado con la igualdad de género o prácticas discriminatorias, se le da seguimiento.")
    form_dict["inclusion_3"] = inclusion_cols[1].checkbox("Sí/No", key="inclusion_3")

    st.divider()

    if st.form_submit_button("Enviar formulario"):
        config = Config()
        client = get_mongo_client(config)
        collection = client["ambiente_laboral"]["formulario_bool"]
        collection.insert_one(form_dict)
        st.success("Datos enviados correctamente")