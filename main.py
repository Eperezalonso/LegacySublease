from flask import Flask, render_template, request, redirect, url_for, flash
import os
from datetime import datetime

app = Flask(__name__)
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
        #add actual photos here
        'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800&h=600&fit=crop',
        'https://images.unsplash.com/photo-1560448075-bb485b067938?w=800&h=600&fit=crop',
        'https://images.unsplash.com/photo-1560448204-60394e4be125?w=800&h=600&fit=crop'
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
    app.run(debug=True, host='0.0.0.0', port=5001)
