from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint, get_flashed_messages
from models import app, User, db


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        second_name = request.form['second_name']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        confirm_password = request.form['confirm_password']
        date_of_birth = request.form['date_of_birth']
        gender = request.form['gender']
        city = request.form['city']
        state = request.form['state']
        user_type = request.form['type']

        # Validate the form data
        if not first_name or not second_name or not email or not password or not confirm_password:
            flash('Please fill out all required fields', 'error')
            return redirect(url_for('login'))

        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('login'))

        # Check if the email is already registered
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email address already exists', 'error')
            return redirect(url_for('login'))

        # Hash the password
        hashed_password = generate_password_hash(password, method='sha256')

        # Save the uploaded image if present
        f = request.files['image']
        filename = secure_filename(f.filename)
        f.save('static/uploads/' + filename)
        # Create a new user object
        new_user = User(
            first_name=first_name,
            second_name=second_name,
            email=email,
            password=hashed_password,
            phone=phone,
            date_of_birth=date_of_birth,
            gender=gender,
            city=city,
            country=country,
            major=major,
            type=user_type,
            image=filename.encode('utf-8')
        )

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        flash('Your account has been created successfully. Please log in.', 'success')
        return redirect(url_for('/'))
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
