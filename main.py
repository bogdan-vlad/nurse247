import os
from collections import namedtuple

from flask import (
    Flask,
    render_template,
    url_for,
    request,
    session,
    redirect,
)

# from upload_blob.upload import upload_blob

import sqlite3

DB_FILE = 'register.db'

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')


@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/register_new_form', methods=['GET', 'POST'])
def register_new_form():
    global group1_provide
    global group2_provide
    global group3_provide

    title = request.form['title']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    telephone = request.form['telephone']
    email = request.form['email']
    nationality = request.form['nationality']
    nino = request.form['nino']
    address = request.form['address']
    postcode = request.form['postcode']
    dob = request.form['dob']
    tpe = request.form['tpe']
    perm_uk = request.form['perm_uk']
    nmc = request.form['nmc']
    nmc_expiry = request.form['nmc_expiry']
    group1 = request.form['group1']
    group1_provide = request.form['group1_provide']
    group2 = request.form['group2']
    group2_provide = request.form['group2_provide']
    group3 = request.form['group3']
    group3_provide = request.form['group3_provide']
    group4 = request.form['group4']
    # attachment = request.files['myFile[]']
    # from werkzeug.utils import secure_filename
    # import os.path
    # import tempfile

    # with tempfile.NamedTemporaryFile() as temp:
    #     attachment.save(temp.name)

    # UPLOAD = '/home/bogdan/projects/nurse247/uploads'
    # app.config['UPLOAD'] = UPLOAD

    # f_name = secure_filename(attachment.filename)
    # attachment.save(os.path.join(app.config['UPLOAD'], f_name))

    if nmc and nmc_expiry is not None:
        is_nmc = nmc
        is_nmc_expiry = nmc_expiry
    else:
        is_nmc = 'N/A'
        is_nmc_expiry = 'N/A'

    if group1 == "yes":
        group1_provide = request.form['group1_provide']
    elif group2 == "yes":
        group2_provide = request.form['group2_provide']
    elif group3 == "yes":
        group3_provide = request.form['group3_provide']

    import smtplib

    EMAIL = 'compliance@yournurse247.co.uk'
    PASSWORD = 'Bristol2020!'

    send_from = email
    to = 'compliance@yournurse247.co.uk'
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.image import MIMEImage
    from email.mime.base import MIMEBase
    from email import encoders
    import os.path

    msg = MIMEMultipart()

    body = """
    <html>
    <head></head>
      <body>
        <p class="thick">Title: %s</p>
        <p class="thick">First name: %s | Last name: %s</p>
        <p class="thick">Telephone number: %s | Email: %s</p>
        <p class="thick">Nationality: %s | National Insurance Number: %s</p>
        <p class="thick">Address: %s | Postcode: %s</p>
        <p class="thick">Date of Birth: %s</p>
        <p class="thick">Are there any restrictions to your residence withing the UK that
        might your right to take up employment in the UK? %s</p>
        <p class="thick">If your application is successful, would you require
        permission to work in the UK? %s</p>
        <p class="thick">NMC/GMC/GDC pin (if applicable): %s | Expiry date: %s</p>
        <p class="thick">Do you have any unspent* Criminal convictions? : %s | %s</p>
        <p class="thick">Are you / have been under / or undergoing any clinical
        investigation, disciplinary or suspension process
        pending or otherwise? : %s | %s</p>
        <p class="thick">Do you have any health issues or a disability relevant
        which may make it difficult for you to carry out functions which
        are essential for the role you seek? : %s | %s</p>
        <p class="thick">Please tick the appropriate box to confirm that you have read
        and understood the above information. : <br>%s</p>
      </body>
    </html>
    """ % (
        title,
        first_name,
        last_name,
        telephone,
        email,
        nationality,
        nino,
        address,
        postcode,
        dob,
        tpe,
        perm_uk,
        is_nmc,
        is_nmc_expiry,
        group1,
        group1_provide,
        group2,
        group2_provide,
        group3,
        group3_provide,
        group4,
    )
    # message = MIMEText(body, 'html')
    text = 'New Application %s %s' % (first_name, last_name)

    msg['FROM'] = send_from
    msg['TO'] = to
    msg['Subject'] = text

    msg.attach(MIMEText(body, 'html'))

    # filename = os.path.basename(temp.name)
    # file_cv = open(temp.name, "rb")
    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload(file_cv.read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename=%s" % filename)

    # msg.attach(part)

    print('Before')
    try:
        print('Started...')
        s = smtplib.SMTP('smtp.gmail.com', 587)
        print('Conn to SMTP')
        s.starttls()
        s.login('compliance@yournurse247.co.uk', 'Bristol2020!')
        s.sendmail(send_from, to, msg.as_string())
        s.quit()
    except:
        print('Error, not send')
    print('Success')

    # conn = sqlite3.connect(DB_FILE)
    # cursor = conn.cursor()
    # statement = 'INSERT INTO test (' \
    #             'first_name,' \
    #             'last_name,' \
    #             'telephone,' \
    #             'email, tpe, dob) VALUES (?, ?, ?, ?, ?, ?)'
    # cursor.execute(statement, (first_name, last_name, telephone, email, tpe, dob))
    # conn.commit()
    # conn.close()
    return redirect('/confirmation')


if __name__ == "__main__":
    app.run(debug=True)
