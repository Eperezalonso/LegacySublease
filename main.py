from flask import Flask, render_template, request, redirect, url_for, flash
import os
from datetime import datetime

app = Flask(__name__, static_folder='static')
app.secret_key = 'your-secret-key-here'  # Change this in production

# Sample apartment data - customize this with your actual apartment details
apartment_data = {
    'title': 'The Legacy 4 Bedroom Apartment',
    'address': '616 E Washington St',
    'city': 'Ann Arbor, MI',
    'price': 1600,
    'available_date': 'January 1, 2025',
    'lease_end': 'July 31, 2025',
    'bedrooms': 4,
    'bathrooms': 4,
    'description': 'Spacious and modern apartment with updated appliances, hardwood floors, and a private balcony. Perfect location near downtown Ann Arbor and Central Campus.',
    'amenities': [
        'In-unit washer/dryer',
        'Dishwasher',
        'Central air conditioning',
        'Hardwood floors',
        'Pet-friendly',
        'Fitness center access',
        'Pool access'
    ],
    'utilities': 'All Utilities Included',
    'contact_name': 'Enrique Perezalonso',
    'contact_email': 'perezalonsoenrique@gmail.com',
    'contact_phone': '(305) 546-9205',
    'photos': [
        # Local photos - place your apartment photos in the static/images folder
        '/static/images/pool.png',
        '/static/images/kitchen.png',
        '/static/images/living_room.png',
        '/static/images/room.png',
        '/static/images/outside.png',
        '/static/images/room2.png'
    ]
}

@app.route('/')
def index():
    return render_template('index.html', apartment=apartment_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        
        # Here you would typically send an email or save to database
        # For now, we'll just flash a success message
        flash(f'Thank you {name}! Your message has been sent. We\'ll get back to you soon.', 'success')
        return redirect(url_for('index'))
    
    return render_template('contact.html', apartment=apartment_data)



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))
