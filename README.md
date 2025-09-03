# Apartment Sublease Advertisement Website

A modern, responsive Flask web application for advertising your apartment sublease. Features a beautiful UI, contact forms, and application submission capabilities.

## Features

- 🏠 **Modern Design**: Clean, professional layout with responsive design
- 📱 **Mobile Friendly**: Optimized for all device sizes
- 📸 **Photo Gallery**: Display multiple apartment photos
- 📝 **Contact Form**: Easy way for potential tenants to reach out
- 🎨 **Beautiful UI**: Gradient backgrounds, smooth animations, and modern styling
- 📍 **Navigation**: Smooth scrolling navigation with active states

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Customize Your Apartment Details

Edit the `apartment_data` dictionary in `main.py` with your actual apartment information:

```python
apartment_data = {
    'title': 'Your Apartment Title',
    'address': 'Your Actual Address',
    'city': 'Your City, State',
    'price': 1800,  # Your actual rent
    'deposit': 500,  # Your security deposit
    'available_date': 'January 15, 2025',
    'lease_end': 'August 31, 2025',
    'bedrooms': 2,
    'bathrooms': 2,
    'square_feet': 950,
    'description': 'Your apartment description...',
    'amenities': [
        'Your actual amenities...',
    ],
    'utilities': 'Your utility information...',
    'contact_name': 'Your Name',
    'contact_email': 'your.email@example.com',
    'contact_phone': '(555) 123-4567',
    'photos': [
        'URL to your actual photos...',
    ]
}
```

### 3. Add Your Photos

Replace the placeholder photo URLs with your actual apartment photos. You can:
- Upload photos to a service like Imgur, Google Drive, or Dropbox
- Use local file paths (place photos in a `static` folder)
- Use any publicly accessible image URL

### 4. Run the Application

```bash
python main.py
```

The website will be available at `http://localhost:5000`

## Customization Options

### Colors and Styling

The application uses a modern color scheme with:
- Primary gradient: Blue to purple (`#667eea` to `#764ba2`)
- Accent color: Orange-red (`#ff6b6b`)
- Background: Light gray (`#f8f9fa`)

You can customize these colors by editing the CSS in the HTML templates.

### Adding More Sections

To add additional sections (e.g., neighborhood information, nearby amenities):

1. Add the data to the `apartment_data` dictionary
2. Create a new section in `templates/index.html`
3. Add a navigation link

### Form Handling

Currently, the forms display success messages but don't actually send emails or save data. To implement actual functionality:

1. **Email Integration**: Use Flask-Mail or similar service
2. **Database Storage**: Add SQLAlchemy or similar ORM
3. **File Uploads**: Add file handling for photo uploads

## File Structure

```
LegacySublease/
├── main.py              # Flask application and routes
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── templates/          # HTML templates
    ├── index.html      # Main listing page
    └── contact.html    # Contact form page
```

## Deployment

### Local Development
- Run with `python main.py`
- Access at `http://localhost:5000`

### Production Deployment
For production use, consider:
- Using a production WSGI server (Gunicorn, uWSGI)
- Setting `debug=False` in production
- Using environment variables for sensitive data
- Adding HTTPS/SSL certificates
- Setting up a proper domain name

### Cloud Deployment Options
- **Heroku**: Easy deployment with Git
- **AWS**: EC2 or Elastic Beanstalk
- **Google Cloud**: App Engine or Compute Engine
- **DigitalOcean**: Droplets or App Platform

## Security Notes

- Change the `secret_key` in production
- Validate and sanitize all form inputs
- Implement rate limiting for forms
- Use HTTPS in production
- Consider adding CAPTCHA for forms

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Contributing

Feel free to customize this application for your needs. The code is structured to be easily modifiable and extensible.

## License

This project is open source and available under the MIT License.

---

**Need Help?** Customize the apartment details in `main.py`, add your photos, and you're ready to go! The application includes everything needed for a professional apartment sublease advertisement.
