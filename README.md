# witch-way-wormwood
Half-duplex, turn-based fantasy game with Python and TCP connectivity.

== Copied/pasted directly from Google Docs unedited for now ==
== Will be updated and cleaned up as time goes on ==

Game Desc/Documentation/Guide
Synopsis
On the Southbound Marble lies a fallen tower of ivory, covered in soot and twisting vines.

It is said those who journey into its depths will find the answer to all their problems.

There was once a great prophet who predicted the collapse of the tower. Their child grew up to become another prophet, foreseeing events both tragic and mirthful. The child says that one day there will be someone who goes into the tower’s remains and reap its rewards.

There’s a rumor that the tower leads to an alternate dimension.

Many have braved the marble expanse, never to be seen again.

Today, you decide that your pain ends.

Classes
	Sine
Sine uses the Wormwood Wand.
Sine has the most magical attunement.
Sine is colored blue.
Sine Equipment
Cerulean Circlet
Cobalt Crown
Wormwood Wizarding Hat
Sine uses their Wand to stab enemies at close range. At a distance they can also cast spells.

	Cosine is Sine’s enemy.
Cosine is very calm and cold.

	Tangent
Tangent uses the Tarragon Tourmaline.
Tangent has the ability to foresee the three most possible abilities or attacks from an enemy.
Tangent is colored yellow.
Tangent Equipment
Tangerine Tome
Tangent is able to withstand much damage. They have high health and armor. They manipulate their tourmaline to shapeshift it into armor or a weapon, or they can use it as magical orbs.

	Cotangent is Tangent’s enemy.
Cotangent is reckless and domineering.

	Secant uses the Salicylic Scissors.
Secant uses poison to damage enemies over time.
Secant has potionmaking and potionusing expertise.
Secant is colored red.
Secant has really low HP and armor, but they are very effective for dealing damage over time. They fight in close range. Secant can go into Frenzy Mode after a set amount of turns or damage dealt.

	Cosecant is Secant’s enemy.
Cosecant is silly and chaotic.

Players are assigned one class. There can only be one class used per player. The third, unused class becomes either their friend or adversary (haven’t decided yet).

When players affect their environment, it inadvertently affects the other player’s environment too.

Why are you going into the Fallen Tower?
(Player types freely, seeds some rng for some game affecting thing)

Questionnaire
1. You have many regrets.
	Yes
	No
	Maybe
2. It is easy for you to lie.
	Yes
	No
	Sometimes
3. You are not your father.
	Yes
	No
	Usually
4. You are not your mother.
	Yes
	No
	Usually
5. You are a social butterfly.
	Yes
	No
	Sometimes
6. You feel afraid.
	Yes
	No
	Not now
7. You are happy.
	Yes
	No
	All the time
8. You feel fine.
Of course
Not at all
9. You are lost.
Yeah
I know my way
10. There is salt in the air.
	Yes (Desert biome)
	No (Lush biome)
	Sometimes (Seaside biome)
9. What color is the door?
	Chartreuse
	Absinthe
	There is no door
10. The body smells like:
	Spring
	Sirloin
	There is no body
11. Who is behind you?
	Nobody
	I don’t know
	[Hidden choice for new game plus?]
12. How many steps will you take?
	A few (Short)
	Many (Medium)
	As many as I need (Infinite)
13. The air is:
	Crisp (Easy)
	Heavy (Medium)
	Absolute (Hard)
14. Will you take a sip?
	No
	If I must
15. The chime tastes like:
	Yellow
	Violet
	Nothing
16. Which sounds more beautiful:
	The sun after an intense storm
	The barren earth before it is salted
17. Do you break promises?
	Yes
	Never
	Only if I have to
18. ???????????
	Yes
	No
	[Hidden choice for newgame+]
19. Are you hurt?
	Yes (Briefly, “Your Pain Ends Soon.”
	No
20. Will the sun set today?
	Yes (Night mode)
	No (There will be no NPCs in the overworld)
	Maybe (messed up day/night cycle)

Technical Docs
	Composition
Files are separated into different .py files.

Modules include calculations for player attributes.

	Usage
How to Start the Program
First compile, then run ./www

How to Terminate the Program Early
Ctrl+C to force close (assuming graceful exit), or type in EXIT and then Confirm.

Character Attributes
Health
Magical Affinity
Physical Strength
Intelligence
Charisma
Sanity

Hidden Traits (morality scale)
Outward Beauty
Inner Beauty

Combat Actions
Physical Attack
Magic Attack
Use Item
Shield
Skip Turn
Ailments
Fear
Confusion
In Love
Poisoned
Asleep
Enemies
Onyx Lynx
Sphinx of Black Quartz
Iodine Star
Gray Absoluteness
Serpentine Oryx
Alabaster Aster
Consumables
Health Potion
Noxious Potion
Armor
Breastplate
Chestplate
Greaves
Braces
Weapons
Wormwood Wand
Glass Cannon
Volph’s Wane
Charlatan Shears
Serendipitous Scissors
NPCs
Puraitine
Lylax
Maughnark

Summary
Savefiles are not available at this time.

Players progress through the Tower, whose length and difficulty are determined by the cryptic questionnaire at the beginning.

Players are assigned a class, Sine, Cosine, or Secant which each have their own unique abilities, kits, and playstyles. The third unused class will be the two players’ adversary.

As players enter the Tower, they are quickly separated and must solve puzzles and fight enemies to progress.

When the players reach the bottom of the tower, they will encounter Wormwood, an entity of light that asks them more cryptic questions, which will affect each player’s ending, and the overall ending of the game.

Technical Features
Randomization
Half duplex communication
TCP Sockets


Future Work/Planned Updates
Full duplex support where players can act whenever they want, and the server responds accordingly.

Savefile support.
