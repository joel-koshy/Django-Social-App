# Social Media Platform

## Overview
This project is a **containerzed social media website** built using Django, containerized with Docker, and deployed on **Google Cloud Run** for seamless scalability. The platform allows users to share images, interact with posts, and manage profiles efficiently. It leverages a **PostgreSQL database** with **third normal form (3NF) normalization** for optimized query performance and an **image storage bucket** for handling media content.


## Application Screenshots
Below are some images showcasing the user interface and key features of the app:

![Home Feed](./readme_images/homepage.png)
*Home feed displaying user posts with images and interactions.*

![Post Detail](./readme_images/comment.png)
*Detailed view of a post with comments and likes.*

![User Profile](./readme_images/saved_post.png)
*User profile page showing saved posts and follower count.*

## Database Schema
The following diagram represents the **normalized** database schema used in the project:

![Database Schema](./readme_images/schema.png)
*Entity-relationship diagram illustrating the 3NF-normalized database design.*


## Features
- **User Authentication**: Secure login and registration system using Django's authentication framework.
- **Post Management**: Users can upload, edit, and delete image-based posts.
- **Database Optimization**: PostgreSQL database follows **3NF normalization**, reducing redundancy and improving query efficiency.
- **Image Hosting**: Integrated **AWS S3-compatible storage** for scalable and efficient image handling.
- **Scalability & Deployment**: 
  - **Dockerized application** ensures consistency across environments.
  - **Google Cloud Run** provides automatic scaling and cost efficiency.
  - **Django ORM & Migrations** streamline schema updates and data management.


## Tech Stack
- **Backend**: Django (Python)
- **Database**: PostgreSQL,
- **Containerization**: Docker
- **Hosting & Deployment**: Google Cloud Run
- **Storage**: AWS S3-compatible bucket for image hosting

