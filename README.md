# MultivendorEcommerce

Developing an E-Commerce Website with Various Functionalities

Group Project
Course: Object Oriented Programming
Under the supervision of Dr. Subhrakanta Panda

Group Members:
Krishankant Pandey 
Divya Sharma
Aman Ladda
Ayush Kumar Singh

The backend is bulit using Django Framework and the Front end using HTML, CSS and Jinja2 Templating
As python was the preffered language of the group, we decided to use Django on the backend.
Django has excellent admin panel, excellent ORM, very good documentation and multiple such features. 

The Project has following features:
1. Login Page of the website irrespective of the type of user i.e.,
Customer/Retailer/Wholesaler along with an option to sign in using Google account.

2. The website has 2 factor authentication with OTP. 
This functionality is enabled across all types of useri.e., Customer/Retailer/Wholesaler

3. The sign-up has multiple functionalities such as password confirmation, Type of user,
user details including the address and their geospatial location secured using a two-stage user
verification of password and OTP.

4. User (Any type of user or anonymous) can search products based on category.
User can also search product by name of features (The query search in the title and Description of the project

Along with the many APIs that come included with Django Following external APIs were used

1. Google API (For logging in with google)
2. Twilio API (For sending OTP on the user's Phone no.)
3. Q API (For searching through the products)

User can be either a Buyer, Seller, Wholesaler. all will have corresponding functionalities.
Following are the Features:

1. Cart
2. Order Status (It is updated by the seller)
3. Search product based on Category, Title, feature, Distance of seller from the user.
4. Buyer, Seller and Wholesaler panel
5. Add Review
6. Similar Product Suggestion
7. Two Factor Authentication
8. Seller can buy products from wholesaler
and other fundamental features of a E-Commerce
