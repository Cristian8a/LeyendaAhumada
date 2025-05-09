from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Configuración del correo
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USER = 'tu_correo@gmail.com'  # Reemplaza con tu correo
EMAIL_PASSWORD = 'tu_contraseña'    # Reemplaza con tu contraseña
OWNER_EMAIL = 'correo_del_dueño@gmail.com'  # Reemplaza con el correo del dueño

# Caracoles

@app.route('/contact', methods=['POST'])
def contact_form():
    try:
        # Obtener datos del formulario
        data = request.json
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if not name or not email or not message:
            return jsonify({'error': 'Todos los campos son obligatorios'}), 400

        # Crear el correo
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = OWNER_EMAIL
        msg['Subject'] = f'Nuevo mensaje de contacto de {name}'

        body = f"Nombre: {name}\nCorreo: {email}\n\nMensaje:\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        # Enviar el correo
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USER, OWNER_EMAIL, msg.as_string())

        return jsonify({'message': 'Mensaje enviado correctamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)