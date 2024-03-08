# Autoform

## The What
This tool aims to automate Google Form completion, **without seeing the form prior to completing it**, based on knowledge regarding the basic structure of the form and types of questions asked (such as name, address, and other form-specific questions).

## The Why
My goal here is to make it as flexible as possible without using/training AI models to keep the solution lightweight and runnable on any PC. I was motivated by several friends having trouble registering for debating tournaments, which often use Google Forms for registration purposes. Such registration forms are often very similar, but not identical - sometimes a certain question is open-ended, sometimes it's a radio input, and sometimes it uses a dropdown.

## The How
The project is still in development. As of now, it consists of an interface for interacting with Google Forms if their structure is known, using Selenium. Currently, I'm working on the question-answer matching element, which matches the answer to the question based on keywords present in the question and the answer preset by the user.
