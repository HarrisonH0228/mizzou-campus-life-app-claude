Claude Code:

What did Claude Code do this week that would have taken you a meaningful amount of time to do manually?
- Claude Code designed the entire skeleton for the website and also fetched all of the data to put into the website by itself.
What did it get wrong? Where did it overshoot, misunderstand, or produce something you had to throw out?
- It created the system prompt for the chatbot I wanted in my website, but the chatbot was directing me to other websites, so I had to add a line to the system prompt to prioritize information from its own guide.
When did you use /plan and did it change what you let it do?
- I used plan to help design the skeleton frame and scaffolding for the website
What would you put in CLAUDE.md at the start of a project, based on what you learned this week?
- I would put key design decisions not to be questioned alongside how the file architecture will be designed, as well as more important information Claude needs to know like what language the project is in, etc.

The Cursor handoff:

When did you switch to Cursor and why?
- I switched to Cursor after having Claude fill in the information on the website because the Day 4/5 guide told me to
Was it the right call? Give a specific example where Cursor did something better.
- I think it was the right call because this was when I was testing Render and Cursor was actually able to see the website itself rather than Claude just estimating how it works.
Is there anything you did in Cursor that you wish Claude Code could have done?
- I wish Claude Code was able to see the website and even have a browser to view the website (I know it's in a terminal so it might not really work but thats just my idea)

The Claude API:

What is your system prompt doing in your project? Could you explain it to someone who has never seen Claude before?
- My system prompt tells my chatbot who it is and what role it's playing, it's the most important part of a chatbot because what's the point of having a chatbot if it's just regular Claude Chat integrated into a website?
Write out your system prompt here. Then write a version that's twice as specific. Which one would produce better results and why?
    "You are a helpful campus life guide for the University of Missouri (Mizzou). "
    "Answer questions about campus dining, housing, transportation, academics, student organizations, "
    "events, health services, and general campus life. Be friendly, concise, and accurate. "
    "Always answer with information from this guide and not from the internet when possible."
    "If you don't know something specific, suggest where the student might find the answer."

    "You are a helpful campus life guide designed for students or parents researching or exploring the University of Missouri - Columbia (Mizzou)"
    "Answer questions about campus dining, housing, transportation, academic, student organizations, events, health services, and general campus life. Be friendly, concise, accurate, and keep your responses simple enough for the average guest to understand"
    "Always answer with information from this guide and not from the internet when possible."
    "If you don't know something specific, it's fine to suggest where the student might find the answer."

    I predict the 2nd system prompt will perform better to my liking because I narrowed down what identity I want the chatbot to have.
How is calling the API directly different from using Claude Chat? What does that difference give you?
- Using the API will let you add a system prompt, and also not require the user to have a Claude Chat subscription. Using Claude chat requires a subscription typically and also would be harder to design for the average user, using the API makes it easier for our users.
If you used streaming, what was the user experience difference? If you didn't, why not?
- I didn't use streaming, it makes the response take a little longer. Streaming would make the conversation look more natural to the user, and perhaps make them more comfortable talking to the API.
Across the full toolkit so far — Claude Chat, Cursor, Claude Code:

Give each tool one sentence: what it's actually for
Claude Chat - Helpful code advice for experienced developers
Cursor - AI integrated IDE that features AI coding tools for all kinds of developers
Claude Code - AI agent terminal tool for all kinds of developers

Which tool do you reach for first when starting a new project?
- I'd likely use Claude Code because it can understand my intentions a little better

What are you still uncertain about?
- I'm not really sure how I'd use all 3 of them on a project, it feels like a lot to be remembering to use these 3 different tools, I typically just stick with one and maybe use another for a unique issue.