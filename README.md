#hackathon2023

TTRPG Game Finding Script

Overview We are building a groupfinding app for people that play tabletop roleplaying games such as Dungeons and Dragons. The problem players of these games have is the difficulty of finding a stable group of people to play consistently with. A D&D game is a long term hobby, and the liklihood that every would-be player will have a group of 4-5 friends willing to commit to playing at the same time every week for 4-6 hours at a time is extremely low. Even if they know enough people ready and willing to do so, what's even less likely is that those 4-5 people are free at the same time every week. People have jobs, families, plans, and expecting every one of the millions of people interested in playing to have that holy grail of a social circle is just not realistic. In fact, most of them are massive nerds who already have a smaller than average IRL social circle.

That's where we come in. These games are popular online via discord and other voice chat apps, and that opens up the whole world as potential gaming group members. The schedule problem still remains, but now its about narrowing it down and finding who your people are in an international sea of potentials.

Goals

We want to have a usable--if low-tech--version of a service that users can enter their scheduling information into which will then match them with a group of 5 schedule-compatible players.
If possible we want to implement more granual and customizable filtration of players and group requirements such as age
Implement a method by which potential DMs are rationed evenly between
Deliverable We are stripping down the solution to the easiest possible version to make. Using google forms and discord as our primary connection points to the end user.

The google form will accept player schedule and contact information then write that information to a .csv From there, we will input the results into a python script that will sort through the users and make groups of 5 players with compatible schedules. From there, we will copy paste the output into a discord channel and tag the users in each group. This isn't super scalable, but should suffice and can easily be automated through the use of a discord bot later down the line.

The final product will be a Google form, a python grouping script, and a discord channel.

Resources
