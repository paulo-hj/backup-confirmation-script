from datetime import datetime
from apps.admcore import models
global models
global datetime
import smtplib
global smtplib
import email.message
global email
import psutil
global psutil
import sys 
global sys

class InfoServidor(object):
    def infoDataHora(self):
        dataEHora = datetime.now()
        dataEHora = dataEHora.strftime("%d/%m/%Y - %H:%M")
        return dataEHora
    
    def memoriaTotalServidor(self):
        #Coverte a memória total para giga.
        kilobytesTotal = self.memoriaTuple[0] / 1024.0
        megabytesTotal = kilobytesTotal / 1024
        gigabytesTotal = megabytesTotal / 1024
        return gigabytesTotal
    
    def memoriaDisponivelServidor(self):
        #Coverte a memória disponível para giga.
        kilobytesDisponivel = self.memoriaTuple[1] / 1024.0
        megabytesDisponivel = kilobytesDisponivel / 1024
        gigabytesDisponivel = megabytesDisponivel / 1024
        return gigabytesDisponivel

    def memoriaUsadaServidor(self):
        #Coverte a memória usada para giga.
        kilobytesUsada = self.memoriaTuple[3] / 1024.0
        megabytesUsada = kilobytesUsada / 1024
        gigabytesUsada = megabytesUsada / 1024
        return gigabytesUsada

    def discoTotalServidor(self):
        #Coverte o disco total para giga.
        kilobytesDiskTotal = self.diskTupla[0] / 1024.0
        megabytesDiskTotal = kilobytesDiskTotal / 1024
        gigabytesDiskTotal = megabytesDiskTotal / 1024
        return gigabytesDiskTotal

    def discoDisponivelServidor(self):
        #Coverte o disco disponível para giga.
        kilobytesDiskDisponivel = self.diskTupla[2] / 1024.0
        megabytesDiskDisponivel = kilobytesDiskDisponivel / 1024
        gigabytesDiskDisponivel = megabytesDiskDisponivel / 1024
        return gigabytesDiskDisponivel

    def discoUsadoServidor(self):
        #Coverte o disco usado para giga.
        kilobytesDiskUsado = self.diskTupla[1] / 1024.0
        megabytesDiskUsado = kilobytesDiskUsado / 1024
        gigabytesDiskUsado = megabytesDiskUsado / 1024
        return gigabytesDiskUsado

class ClienteSmtp(object):
    def envioSmtp(self):
        email_content = """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" style="font-family:arial, 'helvetica neue', helvetica, sans-serif">
        <head>
        <meta charset="UTF-8">
        <meta content="width=device-width, initial-scale=1" name="viewport">
        <meta name="x-apple-disable-message-reformatting">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta content="telephone=no" name="format-detection">
        <title>Novo modelo de e-mail 2022-07-29</title><!--[if (mso 16)]>
        <style type="text/css">
        a {text-decoration: none;}
        </style>
        <![endif]--><!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]--><!--[if gte mso 9]>
        <xml>
        <o:OfficeDocumentSettings>
        <o:AllowPNG></o:AllowPNG>
        <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
        </xml>
        <![endif]-->
        <style type="text/css">
        #outlook a {
        padding:0;
        }
        .es-button {
        mso-style-priority:100!important;
        text-decoration:none!important;
        }
        a[x-apple-data-detectors] {
        color:inherit!important;
        text-decoration:none!important;
        font-size:inherit!important;
        font-family:inherit!important;
        font-weight:inherit!important;
        line-height:inherit!important;
        }
        .es-desk-hidden {
        display:none;
        float:left;
        overflow:hidden;
        width:0;
        max-height:0;
        line-height:0;
        mso-hide:all;
        }
        [data-ogsb] .es-button {
        border-width:0!important;
        padding:15px 30px 15px 30px!important;
        }
        td .es-button-border:hover a.es-button-1 {
        background:#adadad!important;
        border-color:#adadad!important;
        }
        td .es-button-border-2:hover {
        border-style:solid solid solid solid!important;
        background:#adadad!important;
        border-color:#42d159 #42d159 #42d159 #42d159!important;
        }
        [data-ogsb] .es-button.es-button-3 {
        padding:10px 25px 10px 15px!important;
        }
        @media only screen and (max-width:600px) {p, ul li, ol li, a { line-height:150%!important } h1, h2, h3, h1 a, h2 a, h3 a { line-height:120% } h1 { font-size:30px!important; text-align:center } h2 { font-size:26px!important; text-align:center } h3 { font-size:20px!important; text-align:center } .es-header-body h1 a, .es-content-body h1 a, .es-footer-body h1 a { font-size:30px!important } .es-header-body h2 a, .es-content-body h2 a, .es-footer-body h2 a { font-size:26px!important } .es-header-body h3 a, .es-content-body h3 a, .es-footer-body h3 a { font-size:20px!important } .es-menu td a { font-size:16px!important } .es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a { font-size:16px!important } .es-content-body p, .es-content-body ul li, .es-content-body ol li, .es-content-body a { font-size:16px!important } .es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a { font-size:16px!important } .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a { font-size:12px!important } *[class="gmail-fix"] { display:none!important } .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3 { text-align:center!important } .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3 { text-align:right!important } .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3 { text-align:left!important } .es-m-txt-r img, .es-m-txt-c img, .es-m-txt-l img { display:inline!important } .es-button-border { display:block!important } a.es-button, button.es-button { font-size:20px!important; display:block!important; border-left-width:0px!important; border-right-width:0px!important } .es-adaptive table, .es-left, .es-right { width:100%!important } .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header { width:100%!important; max-width:600px!important } .es-adapt-td { display:block!important; width:100%!important } .adapt-img { width:100%!important; height:auto!important } .es-m-p0 { padding:0!important } .es-m-p0r { padding-right:0!important } .es-m-p0l { padding-left:0!important } .es-m-p0t { padding-top:0!important } .es-m-p0b { padding-bottom:0!important } .es-m-p20b { padding-bottom:20px!important } .es-mobile-hidden, .es-hidden { display:none!important } tr.es-desk-hidden, td.es-desk-hidden, table.es-desk-hidden { width:auto!important; overflow:visible!important; float:none!important; max-height:inherit!important; line-height:inherit!important } tr.es-desk-hidden { display:table-row!important } table.es-desk-hidden { display:table!important } td.es-desk-menu-hidden { display:table-cell!important } .es-menu td { width:1%!important } table.es-table-not-adapt, .esd-block-html table { width:auto!important } table.es-social { display:inline-block!important } table.es-social td { display:inline-block!important } .es-m-p5 { padding:5px!important } .es-m-p5t { padding-top:5px!important } .es-m-p5b { padding-bottom:5px!important } .es-m-p5r { padding-right:5px!important } .es-m-p5l { padding-left:5px!important } .es-m-p10 { padding:10px!important } .es-m-p10t { padding-top:10px!important } .es-m-p10b { padding-bottom:10px!important } .es-m-p10r { padding-right:10px!important } .es-m-p10l { padding-left:10px!important } .es-m-p15 { padding:15px!important } .es-m-p15t { padding-top:15px!important } .es-m-p15b { padding-bottom:15px!important } .es-m-p15r { padding-right:15px!important } .es-m-p15l { padding-left:15px!important } .es-m-p20 { padding:20px!important } .es-m-p20t { padding-top:20px!important } .es-m-p20r { padding-right:20px!important } .es-m-p20l { padding-left:20px!important } .es-m-p25 { padding:25px!important } .es-m-p25t { padding-top:25px!important } .es-m-p25b { padding-bottom:25px!important } .es-m-p25r { padding-right:25px!important } .es-m-p25l { padding-left:25px!important } .es-m-p30 { padding:30px!important } .es-m-p30t { padding-top:30px!important } .es-m-p30b { padding-bottom:30px!important } .es-m-p30r { padding-right:30px!important } .es-m-p30l { padding-left:30px!important } .es-m-p35 { padding:35px!important } .es-m-p35t { padding-top:35px!important } .es-m-p35b { padding-bottom:35px!important } .es-m-p35r { padding-right:35px!important } .es-m-p35l { padding-left:35px!important } .es-m-p40 { padding:40px!important } .es-m-p40t { padding-top:40px!important } .es-m-p40b { padding-bottom:40px!important } .es-m-p40r { padding-right:40px!important } .es-m-p40l { padding-left:40px!important } .es-desk-hidden { display:table-row!important; width:auto!important; overflow:visible!important; max-height:inherit!important } }
        </style>
        </head>
        <body style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0">
        <div class="es-wrapper-color" style="background-color:#F7F7F7"><!--[if gte mso 9]>
        <v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
        <v:fill type="tile" color="#f7f7f7"></v:fill>
        </v:background>
        <![endif]-->
        <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top;background-color:#F7F7F7">
        <tr>
        <td valign="top" style="padding:0;Margin:0">
        <table class="es-content es-visible-simple-html-only" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%">
        <tr>
        <td class="es-stripe-html" align="center" style="padding:0;Margin:0">
        <table class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#ffffff;border-right:1px solid transparent;border-left:1px solid transparent;width:800px" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center">
        <tr>
        <td align="left" bgcolor="#ffffff" style="padding:0;Margin:0;padding-left:20px;padding-right:20px;padding-top:30px;background-color:#ffffff;border-radius:10px">
        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
        <tr>
        <td class="es-m-p0r" valign="top" align="center" style="padding:0;Margin:0;width:758px">
        <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
        <tr>
        <td align="center" style="padding:0;Margin:0;font-size:0px"><img class="adapt-img" src="https://tsmx.sgp.net.br/media/img/LOGO.png" alt style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" width="304" height="118"></td>
        </tr>
        <tr>
        <td style="padding:0;Margin:0">
        <blockquote type="cite">
        <div style="margin:0;padding:0;background:#f4f4f4">
        <table cellpadding="10" cellspacing="0" border="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;width:0">
        <tr>
        <td align="center" style="padding:0;Margin:0">
        <table cellpadding="0" cellspacing="0" border="0" width="680" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;border:0;width:auto;max-width:680px">
        <tr>
        <td style="padding:15px 0 20px 0;Margin:0;background-color:#ffffff;border:2px solid #e8e8e8;border-bottom:2px solid #e8e8e8">
        <table border="0" cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background:#ffffff;width:680px">
        <tr>
        <td style="padding:0;Margin:0;width:15px"></td>
        <td style="padding:0;Margin:0;width:650px">
        <table cellpadding="0" cellspacing="0" border="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
        <tr>
        <td style="padding:0;Margin:0">
        <table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;margin:5px 10px;border:2px solid #e8e8e8;padding:0" cellpadding="5" cellspacing="0" width="630px">
        <tr style="background-color:#f4f4f4">
        <th align="left">Backup:</th>
        </tr>
        <tr style="background-color:#ffffff">
        <th align="left">Data:</th>
        <td align="left" style="padding:0;Margin:0">29-07-2022</td>
        </tr>
        <tr style="background-color:#f4f4f4">
        <th align="left">Hora de Inicio:</th>
        <td align="left" style="padding:0;Margin:0">03:00:02</td>
        </tr>
        <tr style="background-color:#ffffff">
        <th align="left">Hora de Termino:</th>
        <td style="padding:0;Margin:0">05:08:15</td>
        </tr>
        <tr style="background-color:#f4f4f4">
        <th align="left">Tamanho do arquivo de backup:</th>
        <td style="padding:0;Margin:0">9.57 GB</td>
        </tr>
        <tr style="background-color:#ffffff">
        <th align="left">Status:</th>
        <td style="padding:0;Margin:0;color:#4caf50">sucesso</td>
        </tr>
        <tr style="background-color:#f4f4f4">
        <th align="left">IP do Servidor:</th>
        <td align="left" style="padding:0;Margin:0">
        <table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
        <tr>
        <td align="left" style="padding:0;Margin:0">lo:</td>
        <td align="left" style="padding:0;Margin:0">127.0.0.1</td>
        </tr>
        </table>
        <table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
        <tr>
        <td align="left" style="padding:0;Margin:0">ens18:</td>
        <td align="left" style="padding:0;Margin:0">170.81.42.152</td>
        </tr>
        </table>
        <table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
        <tr>
        <td align="left" style="padding:0;Margin:0">ppp0:</td>
        <td align="left" style="padding:0;Margin:0">192.168.199.1</td>
        </tr>
        </table></td>
        </tr>
        <tr style="background-color:#ffffff">
        <th align="left">Informa  es do Disco:</th>
        <td align="left" style="padding:0;Margin:0">
        <table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
        <tr>
        <td align="left" style="padding:0;Margin:0">Disco:</td>
        <td align="left" style="padding:0;Margin:0">/</td>
        </tr>
        <tr>
        <td align="left" style="padding:0;Margin:0">Em Uso:</td>
        <td align="left" style="padding:0;Margin:0">27.08 Gb</td>
        </tr>
        <tr>
        <td align="left" style="padding:0;Margin:0">Dispon vel:</td>
        <td align="left" style="padding:0;Margin:0">437.72 Gb</td>
        </tr>
        <tr>
        <td align="left" style="padding:0;Margin:0">Total:</td>
        <td align="left" style="padding:0;Margin:0">489.74 Gb</td>
        </tr>
        <tr>
        <td align="left" style="padding:0;Margin:0"> Porcentagem de uso: </td>
        <td align="left" style="padding:0;Margin:0">
        <table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;border:2px solid #293a4a;margin:1px;padding:0" cellpadding="0" cellspacing="0" width="100%">
        <tr>
        <td style="padding:0;Margin:0;background-color:#4caf50;color:white" align="center" width="6%">6%</td>
        <td style="padding:0;Margin:0;background-color:#ffffff" width="94%"></td>
        </tr>
        </table></td>
        </tr>
        </table>
        <hr style="Margin:0">
        <table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
        <tr>
        <td align="left" style="padding:0;Margin:0">Disco:</td>
        <td align="left" style="padding:0;Margin:0">/var/www/bkp</td>
        </tr>
        <tr>
        <td align="left" style="padding:0;Margin:0">Em Uso:</td>
        <td align="left" style="padding:0;Margin:0">75.99 Gb</td>
        </tr>
        <tr>
        <td align="left" style="padding:0;Margin:0">Dispon vel:</td>
        <td align="left" style="padding:0;Margin:0">390.14 Gb</td>
        </tr>
        <tr>
        <td align="left" style="padding:0;Margin:0">Total:</td>
        <td align="left" style="padding:0;Margin:0">491.15 Gb</td>
        </tr>
        <tr>
        <td align="left" style="padding:0;Margin:0"> Porcentagem de uso: </td>
        <td align="left" style="padding:0;Margin:0">
        <table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;border:2px solid #293a4a;margin:1px;padding:0" cellpadding="0" cellspacing="0" width="100%">
        <tr>
        <td style="padding:0;Margin:0;background-color:#4caf50;color:white" align="center" width="17%">17%</td>
        <td style="padding:0;Margin:0;background-color:#ffffff" width="83%"></td>
        </tr>
        </table></td>
        </tr>
        </table>
        <hr style="Margin:0">
        <table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
        <tr>
        <td align="left" style="padding:0;Margin:0">Disco:</td>
        <td align="left" style="padding:0;Margin:0">/boot</td>
        </tr>
        <tr>
        <td align="left" style="padding:0;Margin:0">Em Uso:</td>
        <td align="left" style="padding:0;Margin:0">0.09 Gb</td>
        </tr>
        <tr>
        <td align="left" style="padding:0;Margin:0">Dispon vel:</td>
        <td align="left" style="padding:0;Margin:0">0.35 Gb</td>
        </tr>
        <tr>
        <td align="left" style="padding:0;Margin:0">Total:</td>
        <td align="left" style="padding:0;Margin:0">0.46 Gb</td>
        </tr>
        <tr>
        <td align="left" style="padding:0;Margin:0"> Porcentagem de uso: </td>
        <td align="left" style="padding:0;Margin:0">
        <table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;border:2px solid #293a4a;margin:1px;padding:0" cellpadding="0" cellspacing="0" width="100%">
        <tr>
        <td style="padding:0;Margin:0;background-color:#4caf50;color:white" align="center" width="21%">21%</td>
        <td style="padding:0;Margin:0;background-color:#ffffff" width="79%"></td>
        </tr>
        </table></td>
        </tr>
        </table>
        <hr style="Margin:0"></td>
        </tr>
        </table></td>
        </tr>
        <tr>
        <td style="padding:0;Margin:0"></td>
        </tr>
        </table></td>
        <td style="padding:0;Margin:0;width:15px"></td>
        </tr>
        </table></td>
        </tr>
        </table></td>
        </tr>
        </table>
        </div>
        </blockquote></td>
        </tr>
        </table></td>
        </tr>
        </table></td>
        </tr>
        </table></td>
        </tr>
        </table>
        <table cellpadding="0" cellspacing="0" class="es-footer es-visible-simple-html-only" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top">
        <tr>
        <td class="es-stripe-html" align="center" style="padding:0;Margin:0">
        <table class="es-footer-body" align="center" cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:800px">
        <tr class="es-visible-simple-html-only">
        <td class="es-struct-html" align="left" style="Margin:0;padding-top:5px;padding-bottom:5px;padding-left:20px;padding-right:25px;border-radius:5px;background-color:#093e4b" bgcolor="#093e4b">
        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
        <tr>
        <td align="left" style="padding:0;Margin:0;width:755px">
        <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
        <tr>
        <td align="center" style="padding:0;Margin:0;font-size:0">
        <table cellpadding="0" cellspacing="0" class="es-table-not-adapt es-social" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
        <tr>
        <td align="center" valign="top" style="padding:0;Margin:0;padding-right:40px"><a target="_blank" href="https://www.youtube.com/c/SGPTSMX/videos" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:underline;color:#CCCCCC;font-size:14px"><img title="Youtube" src="https://vumqey.stripocdn.email/content/assets/img/social-icons/circle-white-bordered/youtube-circle-white-bordered.png" alt="Yt" height="32" width="32" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic"></a></td>
        <td align="center" valign="top" style="padding:0;Margin:0;padding-right:40px"><a target="_blank" href="http://sgp8.hospedagemdesites.ws/" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:underline;color:#CCCCCC;font-size:14px"><img title="Site" src="https://vumqey.stripocdn.email/content/assets/img/other-icons/circle-white-bordered/globe-circle-white-bordered.png" alt="World" height="32" width="32" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic"></a></td>
        <td align="center" valign="top" style="padding:0;Margin:0;padding-right:40px"><a target="_blank" href="tel:(84) 9-9118-2908" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:underline;color:#CCCCCC;font-size:14px"><img title="Suporte Técnico" src="https://vumqey.stripocdn.email/content/assets/img/messenger-icons/circle-white-bordered/whatsapp-circle-white-bordered.png" alt="Whatsapp" height="32" width="32" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic"></a></td>
        <td align="center" valign="top" style="padding:0;Margin:0"><a target="_blank" href="tel:(84) 9-9117-8963" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:underline;color:#CCCCCC;font-size:14px"><img title="Suporte Sistema" src="https://vumqey.stripocdn.email/content/assets/img/messenger-icons/circle-white-bordered/whatsapp-circle-white-bordered.png" alt="Whatsapp" height="32" width="32" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic"></a></td>
        </tr>
        </table></td>
        </tr>
        </table></td>
        </tr>
        </table></td>
        </tr>
        </table></td>
        </tr>
        </table></td>
        </tr>
        </table>
        </div>
        </body>
        </html>
        """.encode('ascii','ignore').decode('ascii')
        smtplib.SMTP('smtp.gmail.com:587')
        msg = email.message.Message()
        msg['Subject'] = 'Backup SGP'
        msg['From'] = self.email
        msg['To'] = self.email
        password = self.senha
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(email_content)
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string())
        print("ok")
        print(self.memoriaTotalServidor())
        print(self.status)

    def dadosSmtp(self):
        eSmtp = models.ConfigSmtp.objects.filter().order_by("id")
        for i in eSmtp:
            self.email = str(i.email_host_user)
            self.senha = str(i.email_host_password)
            ativado = i.email_active
            self.nome = str(i.email_name)
            if ativado:
                self.envioSmtp()
            
class Main(ClienteSmtp, InfoServidor):
    def __init__(self):
        self.status = str(sys.argv[1])
        self.memoriaTuple = psutil.virtual_memory()
        self.diskTupla = psutil.disk_usage('/')
        self.dadosSmtp()
Main()
