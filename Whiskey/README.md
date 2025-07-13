# Scotch Whiskey Recommendation System 

## Overview

This project presents a proof-of-concept for a **Scotch Whiskey Recommendation System** aimed at improving the customer service experience in whiskey shops. The application enables shop employees to efficiently assist customers seeking information on specific whiskeys or personalized whiskey recommendations. Built with a simple CSV file-based backend, this system demonstrates how a basic recommendation engine can be implemented using Python and Flask.

The application features two types of users: **managers** and **shop employees**. Managers manage shop data, customer information, and upload files for maintaining the recommendation system, while shop employees directly interact with customers, track purchases, update whiskey preferences, and provide recommendations.

The recommendation engine uses a **k-nearest neighbors (k-NN)** algorithm to suggest whiskey distilleries based on customer preferences, past purchases, and reviews.

## Key Features

### 1. **User Roles**
   - **Managers**: Add/remove shops, set discounts, register customers, and upload files to update the recommendation system.
   - **Shop Employees**: Record customer purchases, update preferences, recommend whiskeys, and assist customers with reviews and product explanations.

### 2. **Recommendation System**
   - Uses a k-NN algorithm to recommend whiskeys based on customer preferences and past purchases.
   - Provides recommendations even for customers with no preferences, offering options based on review scores and popular products.
   - Allows customers to manually add their favorite distilleries if not already in the system.

### 3. **Discount Tiers**
   - Customers are placed into four discount tiers based on their purchase history:
     - **Basic**: No discount, but can register favorite whiskeys.
     - **Silver**: 5% discount after 10 purchases.
     - **Gold**: 10% discount after 25 purchases.
     - **Platinum**: 15% discount after 50 purchases.

### 4. **Shop Types**
   - **Pop-Up Shops**: Carry a limited selection (up to 3 distilleries) and offer special discounts.
   - **Permanent Shops**: Have a broader selection but may not carry all distilleries.

### 5. **CSV-Based Data Storage**
   - All system data, including customer information, whiskey details, and reviews, are stored in CSV files (`whiskey86.csv` for taste categories and `whiskeyreview2020.csv` for customer reviews).

## System Components

### 1. **Recommendation Engine**
   The recommendation system is built using the **k-NN** algorithm. It takes into account:
   - **Taste Categories**: Whiskey preferences (e.g., flavor, strength) for distilleries.
   - **Purchase History**: Recommends based on past purchases, especially distilleries previously bought.
   - **Customer Reviews**: Ranks distilleries by the average review score from all customers.

### 2. **Manager Interface**
   Managers can:
   - Add/remove shops and set discounts.
   - Register new customers and track their preferences and purchase history.
   - Upload whiskey data files (e.g., `whiskey86.csv`, `whiskeyreview2020.csv`) for the recommendation system.

### 3. **Shop Employee Interface**
   Shop employees can:
   - Record customer purchases and update preferences.
   - Make whiskey recommendations based on customer profiles and available distilleries.
   - Provide reviews and recommendations for customers, especially **Gold** and **Platinum** customers, about upcoming events.

### 4. **Customer Tracking**
   - Customer data is tracked using a **customer ID**, including:
     - Purchase history.
     - Favorite whiskeys and distilleries.
     - Loyalty status and associated discounts.

## UML Class Diagram

Included in the repository is an **UML class diagram** outlining the ideal structure of the application, which helps visualize the relationships between the main components.
<br>
<div align="center">
<img src="Whiskey UML.jpg" width="500"/>
</div>

## Flask Application

This proof-of-concept application is implemented using **Flask**, a lightweight Python web framework. The Flask app provides a simple interface for managers and shop employees to interact with the system and make customer interactions smoother.

## Testing and Documentation

- The project is thoroughly documented with clean, **Pythonic** code following best practices.
- Extensive tests have been implemented, including edge cases and exception handling, to ensure smooth operation in various scenarios.
- The codebase includes well-documented functions, and this README guides users through setup, functionality, and potential future improvements.

## Future Improvements

- **Database Integration**: Transition to a scalable database system for better performance and management.
- **UI Enhancements**: Improve the front-end to make customer interactions more intuitive and user-friendly.
- **E-commerce Integration**: Enable online purchasing and integrate with e-commerce platforms.

## Datasets

This project uses two key datasets from **Kaggle**:

1. **Scotch Whisky Dataset**: Contains detailed information on Scotch whiskey distilleries, including taste categories.
2. **Scotch Whiskey Reviews Update 2020**: Provides customer reviews and ratings for various whiskeys.

These datasets are essential for driving the recommendation engine and offering personalized suggestions to customers.


