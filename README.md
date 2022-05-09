# umd-email-bot

For my final project in JOUR328O, I set out to build a reporting tool that could instantly notify The Diamondback newsroom’s Slack when a new campus message – or email from the president’s office – was dispatched.

Of course, the app can help the newsroom break news quickly, but its need comes in large part from the university’s switch to only sending these messages to university email addresses. Many students – and Diamondback reporters – aren’t checking those emails nearly as frequently as they might check other emails. Plus, the emails don’t come at the same time for each email address. Thus, it was necessary to find a way to pull each email by bypassing the inconsistent email system that often goes unchecked.

Scraping the campus messages from the university website allows The Diamondback to see each message as soon as it starts to exist on the page of the university’s website. When the Slack bot identifies a new message, it scrapes the data from the website, pulling the email title, link, date and description. The bot then delivers an alert to Slack with a link to the full email, the title and date of the email. In a thread, the bot replies to the alert message with the beginning of the email so reporters and editors alike can get a sense of the email just from Slack itself.

Over the course of this project, I ran into an expanse of problems. First, I had trouble figuring out the relationship between the yml file and Python. At a point, I remember seeing more than 90 GitHub Actions failed messages fill my inbox. I tried to do too much with the yml file, but I later moved the actions I tried to do in the yml file into Python. Specifically, in Python, I added code that would only send Slack messages if there was new data, rather than turning to the yml file to try to do this.

Another major hiccup in the same vein was ensuring that I loaded in all of my libraries in the yml file. Since this class was the first time I began exploring yml files, I did not realize that I would need to load every single library that I was using Python in my yml file. Once I loaded in each library, the scrape was able to run error-free.

I also initially struggled to connect to Slack. In an old repository for my first Slack bot, I was able to get the same bot to run, but I struggled to get the email bot to run in Slack. Once I indicated the channel in the yml and pulled the correct token from Slack, I was able to begin sending messages in Slack from my new email bot repository.

I used BeautifulSoup to scrape the data, which came to me pretty easily. However, one day, when I sat down to make progress on the app, I found that all of the lists I had created were empty. I could not figure out why, at first, but when I double-checked what I had against the web page’s source code, I found that the HTML backing the message page on the university website had changed. It took some time, but I was able to adjust all of the code to the newly named sections, among other HTML elements.


… to be continued
