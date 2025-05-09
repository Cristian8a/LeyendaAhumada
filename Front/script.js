var swiper = new Swiper('.mySwiper', {
    slidesPerView: 1,
    centeredSlides: true,
    loop: true,
    spacebetween: 30,
    grabCursor: true,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
    },
    breakpoints: {
        991: {
            slidesPerView: 3,
        }
    }
});


document.getElementById('myForm').addEventListener('submit', function (event) {
    event.preventDefault();

    var formData = new FormData(this);
    var email = formData.get('email');
    var message = formData.get('message');

    // Send email using EmailJS
    emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', {
        to_email: 'your-email@example.com',
        from_name: formData.get('name'),
        message: message
    }).then(function (response) {
        console.log('Email sent successfully!', response.status, response.text);
    }, function (error) {
        console.error('Failed to send email.', error);
    });

    // Send SMS using Twilio
    fetch('https://api.twilio.com/2010-04-01/Accounts/YOUR_ACCOUNT_SID/Messages.json', {
        method: 'POST',
        headers: {
            'Authorization': 'Basic ' + btoa('YOUR_ACCOUNT_SID:YOUR_AUTH_TOKEN'),
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            To: 'your-phone-number',
            From: 'your-twilio-phone-number',
            Body: `Name: ${formData.get('name')}\nEmail: ${email}\nMessage: ${message}`
        })
    }).then(response => response.json())
        .then(data => {
            console.log('SMS sent successfully!', data);
        }).catch(error => {
            console.error('Failed to send SMS.', error);
        });
});