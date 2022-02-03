from flask import Blueprint,render_template,request,flash

auth=Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data=request.form
    print(data)
    return render_template("login.html",text="Test",user="C0mplex")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method=="POST":
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        if len(email)<4:
            flash('Email 4 ta belgidan ko`p bo`lishi kerak.',category='error')
        elif len(firstName)<2:
            flash('Ism 2 ta belgidan ko`p bo`lishi kerak.', category='error')
        elif password1!=password2:
            flash('Parollar bir-biriga mos kelmaydi.', category='error')

        elif len(password1)<7:
            flash('Parol 7 ta belgina ko`p bo`lishi kerak.', category='error')
        else:
            flash('Ro`yxatdan o`tdingiz', category='success')
    return render_template("sign_up.html")