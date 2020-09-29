# Milestone 3 Project - Meatblog

Meatblog has been built using my learnings and knowledge of all the Code Academy Full Stack Developer Course modules learnt so far. This includes HTML, CSS, JavaScript, Python, Flask and MongoDB.

The website is a fully responsive, custom-built website which has been designed and built with the users wants and needs first, whilst maintaining high design standards.

You can view the live website here: [Meatblog](https://meatblog.herokuapp.com/)

The purpose of the website is to provide an online, Meat-based recipe blog which has been and continues to be compiled by a community of users, in addition to the site owner.

The owner wanted to create this website to support and increase traffic to their other business, Meatbox, a fresh meat delivery company.

Recipes will be visible to non-registered users, but users must register to be able to post and edit their own recipes.

Meatblog was a site idea I previously had a go at designing and building some years ago, but due to my lack of knowledge at the time, it was never what I wanted it to be and did not stay live for very long. It was template design-based and had no interactive features, database or user submission functionality. I thought this project would be the perfect time to bring the site idea back to life, and properly this time.

You can view the live website here: [Meatblog](https://meatblog.herokuapp.com/)

## UX
The site owner is a fan of cooking and cooking meat-based dishes. As a contrast to the many meat-free/vegan websites which has become popular in recent years, they wish to create a recipe website based solely on meat dishes.

The website providees some recipes from the site owner for others to share and follow, but also encourage other users to create a free account and share recipes of their own.

The website makes adding, editing and deleting recipes easy and straightforward for external users, with the ability to share recipes to social channels.

## New External User Goals:
* As a new user, I want to be able to view recipes to cook
* As a new user, I want to be able to register for the website and post my own recipes

## Frequent User Goals:
* As a frequent user, I want to be able to share my own recipes to the website and with the community in an easy way
* As a frequent user, I want to be find new recipes to cook
* As a frequent user, I want to be able to share recipes that I like to my social network pages

## Returning External User Goals:
* As a returning user, I want to be able to edit/update my posted recipes
* As a returning user, I want to be able to delete my posted recipes

## Site Owner User Goals:
* As the site owner, I want to share my meat-based recipes
* As the site owner, I want to drive traffic from this site to upsell from the fresh meat delivery business.


## Wireframes
Using the user stories above, I put together the wireframes for Meatblog using [Balsamiq](https://balsamiq.com/). The wireframes covered desktop, tablet and mobile formats. 

Due to the navigation items changing depending on whether a user is signed in or not, a number of additional wireframes were needed to be created to show the difference. For example, when a user is not signed in to the site, they cannot view the ‘Add Recipe’ page and can see buttons in the main navigation for ‘Sign Up’ and ‘Sign In.’ 

When a user has registered/signed into the site, these buttons are hidden and ‘Sign Out’ becomes visible, as does ‘Add a Recipe.

[You can view all of the wireframes here](static/readme_docs/wireframes.pdf)

Below are is the homepage wireframes for desktop, mobile and tablet, with both navigation views for a signed in user, and a non signed in/new user.

![Homepage Wireframes Desktop](static/readme_docs/wireframes_desktop.jpg)
![Homepage Wireframes Device](static/readme_docs/wireframes_device.jpg)

## Changes to wireframes:
Whilst I was in the process of building the website, I decided to make a few small amends to my initial wireframes.

Removal of Delete button from Find Recipe page: I decided to only have the ‘delete recipe’ button within the ‘Edit Recipe’ page rather than the Find a Recipe page also. I felt that there were too many buttons on the ‘Find a Recipe’ page and I did not want to confuse users or take away from the main part of the page – viewing the recipes themselves. Removing the Delete button from this section made the page much cleaner and improved usability of the page.

Added image on Find a Recipe page: I decided to add an image to each recipe on the ‘Find a Recipe’ page. I felt that being a recipe website, the visual cue for each recipe would be important in the section. I feel that the overall result is a huge improvement and make the page much more visually appealing, as well as making recipes easier to find.

Adding form helpers: I decided to add form helper information to the following pages: ‘Sign up’, ‘Add Recipe’ and ‘Edit Recipe.’ Initially, the helpers were to provide the user-specific instructions on how to upload a recipe to the website so that it would be formatted correctly (each item must be on a new line) and to explain to a user what is expected to upload an image. Another reason I decided to add helpers was due to my mentor testing the website and not being able to sign up. I decided that I should make it clear what would be accepted as a username, password etc. (A-Z, numbers but not special characters).

## Scope
* Users can find meat based recipes to cook themselves
* Users can sign up to the website
* User can submit their own recipes to the website
* Users can edit and delete their recipes from the website
* Users can click through to order fresh meat to make their recipes

