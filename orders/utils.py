# -*- coding: utf-8 -*-
# @Author: exc-cpereira
# @Date:   2025-08-19 09:47:10
# @Last Modified by:   exc-cpereira
# @Last Modified time: 2025-08-19 12:30:22
# orders/utils.py
from django.core.mail import send_mail
from django.conf import settings

def send_order_status_email(order):
    subject = f"Actualización de tu pedido en {settings.ECOMMERCE_NAME}"

    # Lista de productos en “tarjetas”
    items_html = "".join([
        f"""
        <div style="
            background-color: #f9f3f6;
            border-radius: 10px;
            padding: 10px 15px;
            margin-bottom: 10px;
            border: 1px solid #e0d6db;
            box-shadow: 1px 1px 3px rgba(0,0,0,0.05);
            font-size: 15px;
        ">
            {item.quantity} x {item.product.name}
        </div>
        """
        for item in order.items.all()
    ])

    # Lista de productos en texto plano
    items_text = "\n".join([
        f"- {item.quantity} x {item.product.name}"
        for item in order.items.all()
    ])

    # Mensaje según el estado
    estados_texto = {
        "pending": "Tu pedido ha sido solicitado. Te informaremos sobre su estado en la brevedad posible 🛒",
        "processing": "Tu pedido está siendo procesado ⚙️",
        "shipped": "Tu pedido fue enviado 🚚",
        "completed": "Tu pedido fue completado ✅",
        "cancelled": "Tu pedido fue cancelado ❌"
    }
    estado_mensaje = estados_texto.get(order.status, "Actualización de tu pedido")

    # Mensaje plano
    message = f"""
Hola {order.full_name},

{estado_mensaje}

Productos de tu pedido:
{items_text}

Gracias por confiar en {settings.ECOMMERCE_NAME}.
"""

    # HTML con tarjetas de productos, logo, botón y contacto
    logo_url = settings.LOGO_URL  # Logo público
    order_url = "https://google.com.py"  # Link al pedido

    html_message = f"""
<html>
  <body style="font-family: Arial, sans-serif; background-color: #f7f7f7; padding: 20px; color: #333;">
    <table align="center" width="600" style="background: #ffffff; border-radius: 10px; padding: 20px;">
      <tr>
        <td align="center" style="padding-bottom: 20px;">
          <img src="{logo_url}" alt="Logo" width="120" style="margin-bottom: 10px;">
          <p style="font-size: 18px;">Hola <b>{order.full_name}</b>,</p>
          <p style="font-size: 16px;">{estado_mensaje}</p>
        </td>
      </tr>

      <tr>
        <td>
          <h3 style="color: #264653;">📦 Productos en tu pedido:</h3>
          {items_html}
        </td>
      </tr>

      <tr>
        <td align="center" style="padding: 20px;">
          <a href="{order_url}" style="
              display: inline-block;
              background-color: #f7c6d0;  /* Botón rosadito */
              color: #333;
              padding: 12px 25px;
              text-decoration: none;
              border-radius: 5px;
              font-weight: bold;
              margin-top: 10px;">
            Ver mi pedido
          </a>
        </td>
      </tr>

      <tr>
        <td align="center" style="padding: 15px 0 5px 0; font-size: 14px; color: #6c757d;">
          Gracias por confiar en nosotros
        </td>
      </tr>

      <tr>
        <td align="center" style="padding-bottom: 10px; font-size: 14px; color: #6c757d;">
            Contáctanos: 
            <a href="https://wa.me/{settings.COMUNICATION_PHONE}" style="text-decoration: none; color: #333;">
              <img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/WhatsApp_icon.png" width="18" style="vertical-align: middle; margin-right:5px;">
            </a>
            &nbsp;|&nbsp;
            <a href="{settings.COMUNICATION_SOCIAL}" style="text-decoration: none; color: #d97cae;">
              <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="18" style="vertical-align: middle; margin-right:5px;">
            </a>
            &nbsp;|&nbsp;
            <a href="mailto:{settings.COMUNICATION_EMAIL}" style="color: #d97cae;">
              <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" width="18" style="vertical-align: middle; margin-right:5px;">
            </a>
        </td>
      </tr>
    </table>
  </body>
</html>
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [order.email],
        fail_silently=False,
        html_message=html_message
    )
