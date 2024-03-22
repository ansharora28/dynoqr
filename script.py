import qrcode

def generate_qr(url, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

website_url = "https://indiafoss.net/Chennai/2024"
qr_code_filename = "chennaifoss2.png"

generate_qr(website_url, qr_code_filename)