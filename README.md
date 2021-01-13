# MemeDB
An internet culture database with relevant user functionalities

Project Description:
The Internet Artifact Vault Charles Thomas and Jahnavi Vyas
Our team has chosen to create an internet culture searchable web application. Our application will serve as a database of internet cultural artifacts that are text, images, or videos. Users will be able to search by subject, description, or tag through the artifacts. They can filter by subculture and source. The types of artifacts include composable memes, unique memes, copy pastas, and gif/videos. Each of the artifacts can belong to a subculture and must be posted to at most one source. Users can search for all artifacts of one subculture. Users can add their own artifacts to the database. The goal of this project is to provide a thorough source of internet artifacts limited to the scope of things that belong to the internet and meme culture.

Entity Sets, Relationship Sets, Business Rules:

Entity Sets: ​Meme, Memetexts, Internet Personality, Real Life Community, Subculture,
Aesthetic, Source, Era

Memetexts​:
Texts that overlay composable memes. Primary key: ID
Each memetext overlays at least one meme.

Fig. 1
Text​ ​is the meme text itself. For example, the memetext “when you email...minute” overlays the Tired Incredibles composable meme.

Memes​:
Memes that optionally take memetexts as overlays.
Primary key: ID
Attributes: Subject, Tags, Description, Content, Category, Format
Each meme must be posted on at least one source. Each meme belongs to at most one subculture and at least one aesthetic.

Subject is one word or phrase that describes the subject of the meme. For example: It’s Free Real Estate or Salt Bae uniquely identifies a composable meme image without further tags or description. However, many composable and unique memes cannot be uniquely identifiable with a subject alone. There are many Harold memes, but they all have the same subject: ​Harold​. For this reason, tags are required.
Tags​ ​is a set of words that provide potential hits when the user makes a search.
 
The two above composable memes have the same subject, Harold, but they have a different set of tags. The left has ​sitting, happy, thumbs up, glasses, computer, table, blue shirt, bright, smile. The right has ​standing, happy, phone, phone call, suit, bright.
Description​ ​is a 256 character limited paragraph. Fig. 2 may have the description “Harold sits at a desk in front of a computer, green apple, phone, and glasses. A lamp and alarm clock are in the background.”
Content is a url link to the meme itself.
Category includes unique memes, composable memes, and copy pastas. Format includes images, text, or video.
Subcultures​:
A broad classification of a set of memes. For example, ​Prequel memes​ are based on the star wars prequel movies. ​Political compass memes​ use the political compass as a format. A subculture can refer to a source material (star wars), a format (political compass), or any number of things. A meme belongs to a maximum of one subculture.
Primary key: Name
Attributes: Description, Popularity

Sources​:
Websites that have memes. Twitter, Reddit, Instagram, Facebook, Tik Tok etc. A meme is from a maximum of one originating source.
Primary key: Website
Attributes: Description

Real Life Community:
Real life community is a set of people that are defined by some common attribute but are not necessarily a subculture. For example, American musicians are a real life community. A meme can belong to multiple communities.

Primary Key: Name
Attributes: Description, Language
Aesthetic:
Aesthetic is a set of visual principles underlying the work of a particular meme. For example, a ‘deep fried’ aesthetic uses high saturation and low resolution. A meme can have an aesthetic. Primary Key: Name
Attributes: Description, Colors

Internet Personality:
An internet personality is someone on the internet with a following who posts memes. For example, Elon Musk is known for posting memes and starting trends on his social media accounts. A meme is posted, or originates from, one internet personality. An internet personality can belong to many subcultures and real life communities.

Primary Key: Name
Attributes: Description, Popularity

Era:
Era refers to a period in internet history. Early internet, mid internet, and modern are all different eras in internet history. Each meme can only belong to one era.
Primary Key: Name
Attributes: Origin Year, ending year, description

Translation of the ER diagram:
We translated the diagram to the relational schema using the techniques in class. We created tables for all the entity sets in the diagram and tables for all the relationship sets. None of the relationship sets or entity sets have been combined into the same table.

Entity Tables:
● Subculture
● Meme
● Aesthetic
● Real Life Community
● Internet Personality
● Meme Text
● Source
● Era
Relationship Tables:
● Meme_text_overlays
● Meme_posted_on
● Meme_has_an
● Meme_belongs_to
● meme_in_era
● personality_belongs_to_subculture ● personality_belongs_to_community ● personality_posts
● community_circulates

Data Acquisition:
● Dummy Data was created with currently existing memes within Internet Culture. We sought to find memes with easily recognizable sources, posters, aesthetics, etc.
● We created a schema.sql file to store our tables of entities and relationships. In a separate file called load.sql, we created the dummy data using the definitions in schema.sql.
● For each dummy data, we used insert statements to load the meme into the corresponding table (meme, internet personality, etc).
● The create table statements are executed prior to the insert statements.


User Interface:
Our team will use a simple user interface that provides all our currently supported functionality on a single web page. On this page, our application users are provided with the following functionalities:
- Choose and view from the set of all memes.
- List all meme communities a selected internet personality belongs to
- List all real life communities a selected internet personality belongs to
- List memes by aesthetic
- List memes from a given era
- List memes from a given source
