from typing import Dict, Any

from flask import current_app
from postmarker.core import PostmarkClient

def enviar_email(destinatario: str, assunto: str, email: str) -> Dict[Any, Any ]:

    postmark = PostmarkClient(server_token=current_app.config["SERVER_TOKEN"],
                              account_token=current_app.config["ACCOUNT_TOKEN"])
    resultado = postmark.emails.send(

        From='danielle.caldeira@aluno.ifsp.edu.br',
        To=destinatario,
        Subject=assunto,
        TextBody=email,
    )
    return resultado