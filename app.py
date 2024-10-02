import streamlit as st
from utils.config import Config
from utils.database import get_mongo_client
from utils.authentication import check_password

st.set_page_config(
    page_title="Evaluación clima laboral",
    page_icon="📝"
)

st.header("Pre-evaluación clima laboral SII")

if check_password():

    st.write("Favor de responder a la siguiente encuesta moviendo el cursor/slider a la posición que mejor refleje tu opinión al respecto.")

    form_dict = {}

    with st.form("formulario"):

        form_dict["secretaria"] = st.text_input("Subsecretaría y/o dirección a la que perteneces")

        st.subheader("Liderazgo")

        st.write("Se preocupa mi jefe por transmitir los valores, la misión y objetivos de la secretaría")
        form_dict["liderazgo_1"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="liderazgo_1", value="A veces", label_visibility="collapsed")

        st.write("Mis tareas y objetivos están definidos claramente por parte de mi jefe")
        form_dict["liderazgo_2"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="liderazgo_2", value="A veces", label_visibility="collapsed")

        st.write("El trato por parte de mi jefe es justo y evita favoritismos.")
        form_dict["liderazgo_3"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="liderazgo_3", value="A veces", label_visibility="collapsed")

        st.write("Recibo retroalimentación constantemente de mi jefe para corregir y hacer mejor mi trabajo.")
        form_dict["liderazgo_4"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="liderazgo_4", value="A veces", label_visibility="collapsed")

        st.divider()

        st.subheader("Crecimiento y desarrollo")

        st.write("La capacitación que recibo me ayuda para hacer mi trabajo eficiente.")
        form_dict["crecimiento_1"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="crecimiento_1", value="A veces", label_visibility="collapsed")

        st.write("Existen en la Secretaría planes de carrera y desarrollo para los servidores públicos.")
        form_dict["crecimiento_2"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="crecimiento_2", value="A veces", label_visibility="collapsed")

        st.write("En la Secretaría se cuenta con un proceso de evaluación de desempeño que me sirve para mejorar en mi trabajo y crecer profesionalmente.")
        form_dict["crecimiento_3"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="crecimiento_3", value="A veces", label_visibility="collapsed")

        st.write("Cuando hay una vacante, ¿primero se considera buscar un candidato interno de la Secretaría?")
        form_dict["crecimiento_4"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="crecimiento_4", value="A veces", label_visibility="collapsed")

        st.divider()

        st.subheader("Trabajo en equipo")

        st.write("Estoy consciente de cómo mi trabajo contribuye a la realización de los objetivos del área.")
        form_dict["equipo_1"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="equipo_1", value="A veces", label_visibility="collapsed")

        st.write("Me siento parte de un equipo de trabajo.")
        form_dict["equipo_2"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="equipo_2", value="A veces", label_visibility="collapsed")

        st.write("Considero que en mi equipo, en ocasiones, modificamos la manera de trabajar para bien de la Secretaría.")
        form_dict["equipo_3"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="equipo_3", value="A veces", label_visibility="collapsed")

        st.divider()

        st.subheader("Beneficio y recompensas")

        st.write("Existen diferentes formas de recompensar a los trabajadores.")
        form_dict["beneficios_1"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="beneficios_1", value="A veces", label_visibility="collapsed")

        st.write("La Secretaría realiza ajustes o incrementos de sueldo de forma periódica.")
        form_dict["beneficios_2"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="beneficios_2", value="A veces", label_visibility="collapsed")

        st.write("En la Secretaría se otorgan estímulos a los trabajadores para mejorar su desempeño.")
        form_dict["beneficios_3"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="beneficios_3", value="A veces", label_visibility="collapsed")

        st.divider()

        st.subheader("Satisfacción laboral")

        st.write("Las personas disfrutan trabajar en esta institución.")
        form_dict["satisfaccion_1"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="satisfaccion_1", value="A veces", label_visibility="collapsed")

        st.write("En nuestra Secretaría las personas se sienten satisfechas en el trabajo.")
        form_dict["satisfaccion_2"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="satisfaccion_2", value="A veces", label_visibility="collapsed")

        st.write("Casi nunca pienso en buscar trabajo en otra institución o lugar de trabajo.")
        form_dict["satisfaccion_3"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="satisfaccion_3", value="A veces", label_visibility="collapsed")

        st.divider()

        st.subheader("Comunicación")

        st.write("Los canales de comunicación en la institución están claramente definidos y son accesibles.")
        form_dict["comunicacion_1"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="comunicacion_1", value="A veces", label_visibility="collapsed")

        st.write("La comunicación entre mi departamento y otras áreas es constante y de confianza para solucionar problemas.")
        form_dict["comunicacion_2"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="comunicacion_2", value="A veces", label_visibility="collapsed")

        st.write("Los cambios y asuntos importantes de la Secretaría son comunicados a todo el personal.")
        form_dict["comunicacion_3"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="comunicacion_3", value="A veces", label_visibility="collapsed")

        st.divider()

        st.subheader("Inclusión")

        st.write("En la Secretaría hay un ambiente de respeto y no discriminación hacia las diferencias y preferencias sexuales.")
        form_dict["inclusion_1"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="inclusion_1", value="A veces", label_visibility="collapsed")

        st.write("En mi área de trabajo cuento con espacios, mobiliario y equipo adecuado para que todo el personal pueda laborar, incluyendo al personal con discapacidad.")
        form_dict["inclusion_2"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="inclusion_2", value="A veces", label_visibility="collapsed")

        st.write("Si reporto algún asunto relacionado con la igualdad de género o prácticas discriminatorias, se le da seguimiento.")
        form_dict["inclusion_3"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="inclusion_3", value="A veces", label_visibility="collapsed")

        st.divider()

        st.subheader("Igualdad de género")

        st.write("¿Las funciones o actividades de trabajo que realizas se distribuyen de acuerdo a la responsabilidad de tu puesto?")
        form_dict["igualdad_1"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="igualdad_1", value="A veces", label_visibility="collapsed")

        st.write("¿Puedes acercarte a te jefa/e inmediata/o para hablar sobre cuestiones relacionadas con horarios que te estén afectando?")
        form_dict["igualdad_2"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="igualdad_2", value="A veces", label_visibility="collapsed")

        st.write("¿Actualmente consideras que has sido sujeto de algún “castigo” como: aislamiento de sus compañeras/os, cambio de lugar repentinamente, falta de instrucciones, menosprecio del esfuerzo o propuestas, imposición de tareas sin los medios para realizarlas, aumento de jornada laboral,  etc.?")
        form_dict["igualdad_3"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="igualdad_3", value="A veces", label_visibility="collapsed")

        st.write("¿Tu jefa/e inmediato ha condicionado tu situación laboral a cambio de alguna relación o acto sexual?")
        form_dict["igualdad_4"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="igualdad_4", value="A veces", label_visibility="collapsed")

        st.write("¿Has recibido acercamientos excesivos, miradas insinuantes o gestos de carácter sexual por parte de algún compañero/a?")
        form_dict["igualdad_5"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="igualdad_5", value="A veces", label_visibility="collapsed")

        st.write("¿Te ha generado incomodidad algún chiste, piropo, conversaciones de contenido sexual por parte de alguna persona colaboradora dentro de tu Unidad Administrativa?")
        form_dict["igualdad_6"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="igualdad_6", value="A veces", label_visibility="collapsed")

        st.write("¿Conoces las campañas internas de promoción de igualdad laboral, no discriminación, acoso sexual y hostigamiento sexual?")
        form_dict["igualdad_7"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="igualdad_7", value="A veces", label_visibility="collapsed")

        st.write("¿En caso de ser acosada/o u hostigada/o sexual o laboralmente sabes a qué autoridad puedes dirigirse para denunciarlo?")
        form_dict["igualdad_8"] = st.select_slider("slider", ["Siempre", "A veces", "Nunca"], key="igualdad_8", value="A veces", label_visibility="collapsed")

        if st.form_submit_button("Enviar formulario"):
            config = Config()
            client = get_mongo_client(config)
            collection = client["ambiente_laboral"]["formulario_slider"]
            collection.insert_one(form_dict)
            st.success("Datos enviados correctamente")