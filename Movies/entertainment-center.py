'''This file is where the instances of the Movie class are initialized. Each instance is initialized by accessing the
media.py file and using the Movie class constructor __init__'''

#importing the media.py and fresh_tomatoes.py files
import media
import fresh_tomatoes

'''Instances of Movie with their title, storyline, poster/cover graphic, youtube trailer. These instances are called
by the open_movies_page method within the fresh_tomatoes.py file.'''

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc", 83, "22/04/1996")

avatar = media.Movie("Avatar", "A marine on an alien planet.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=cRdxXPV9GNQ", 78, "17/12/2009")

blade_runner = media.Movie("Blade Runner", "A story of an officer investigating run away androids.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Blade_Runner_poster.jpg/220px-Blade_Runner_poster.jpg",
                           "https://www.youtube.com/watch?v=eogpIG53Cis", 82, "09/09/1982")

dredd = media.Movie("Dredd", "Judge Dredd, a law enforcer given the power of judge, jury and executioner in a vast, dystopic metropolis called Mega-City One that lies in a post-apocalyptic wasteland.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/1/16/Dredd2012Poster.jpg/220px-Dredd2012Poster.jpg",
                           "https://www.youtube.com/watch?v=qVIba2N6MTA", 71, "07/09/2012")

pacific_rim = media.Movie("Pacific Rim", "Huge alien monsters called Kaijus emerge from an interdimensional portal.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Pacific_Rim_FilmPoster.jpeg/220px-Pacific_Rim_FilmPoster.jpeg",
                           "https://www.youtube.com/watch?v=A85EtOalcsM", 70, "12/07/2013")

thor_ragnarok = media.Movie("Thor Ragnarok", "Thor, held captive on the planet Sakaar without his hammer Mjolnir, must win a gladiatorial duel.",
                           "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
                           "https://www.youtube.com/watch?v=ue80QwXMRHg", "NA", "24/10/2017")

movies = [toy_story, avatar, blade_runner, dredd, pacific_rim, thor_ragnarok]
#function call receiving the movie objects as input, and outputting a formatted site with all of the relevant content
fresh_tomatoes.open_movies_page(movies)
