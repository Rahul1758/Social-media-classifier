# Social-media-classifier

## Table of Content
  * [Demo](#demo)
  * [Objective](#objective)
  * [Motivation](#motivation)
  * [Approach](#approach)
  * [Data](#data)
  * [Packages/Libraries](#packageslibraries)
  * [Installation](#installation)
  * [To Do](#to-do)
  * [Contact](#contact)

## Demo
Link: [https://share.streamlit.io/rahul1758/social-media-classifier/app.py](https://share.streamlit.io/rahul1758/social-media-classifier/app.py)
![](https://github.com/Rahul1758/Social-media-classifier/blob/master/img_readme/app_screenshot.jpg)

## Objective
The Objective of this Project was to develop a **Image classifier** for Restaurant Referral system that **identifes which Social-media platform the input image (scanned from the diner's smartphone) belongs to (i.e. Instagram, Facebook, Twitter, Others)**. This could help the Restaurant understand the demographics of Customers, the platform they get referred from the most and then strategise to increase their Social-media presence accordingly.

## Motivation
This project was a part of Internship program. It was developed for a Client looking to automate some tasks of Restaurant Referral system. The scenario plays out like this:
> Suppose you run a restaurant and you have a discount offer for customers who come to dine at your restaurant based on their friend's/colleague's recommendation/referral. You reach the restaurant and show the profile page of your referrer where restaurant staff will scan the page. This is where the following app can be used. It processes the scanned image to identify the Social-media platform the customer got the recommendation from. This information can be stored for further use.

## Approach
I'll using **Transfer-Learning** method to train a CNN model using **Inception_v3** pretrained weights and then add custom layers for **Multiclass classification** purpose.

## Data 
I prepared custom dataset by collecting 150 images of profile pages for each Social-media platform (Instagram, Facebook, Twitter). These images were clicked using smartphone back camera to mimick the real-time scenario, which is important because you want the training data to represent the real-time data. Due to sensitivity of the data, I've not uploaded the dataset in the repository.

## Packages/Libraries
* Streamlit
* TensorFlow

## Installation
The Code is written in Python 3.8. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```
Then run the following command which runs the Webapp locally:
```
streamlit run app.py
```
That's it!!

## To Do
* Enlarge the dataset by collecting more images for each of the platform.

## Contact
If you have suggestions for improvement or any other query, you can reach me at following platform:
  * [Linkedin](https://www.linkedin.com/in/rahul-menon-515702a7/)
