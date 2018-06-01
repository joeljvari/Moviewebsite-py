import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
	                     "nice movie about toys",
	                     "https://resizing.flixster.com/OD2Yrbt-xldV7SH2i90XkjcNUoY=/206x305/v1.bTsxMTIwNzIwNztqOzE3NTg5OzEyMDA7MjE5MDsyOTIw",
	                     "https://www.youtube.com/watch?v=JcpWXaA2qeg")
#print(toy_story.story_line)
avatar = media.Movie("Avatar",
	                  "alien humans in other planet",
	                  "https://www.halon.com/wp-content/uploads/2010/07/avatar_poster1.jpg",
	                  "https://www.youtube.com/watch?v=uZNHIU3uHT4")
#print(avatar.story_line)
interstellar = media.Movie("Interstellar",
	                       "earth is becoming hostileand it a quist to same humanity.modarn day space drama",
	                       "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
	                       "https://www.youtube.com/watch?v=0vxOhd4qlnA")
#interstellar.show_trailer()
iron_man = media.Movie("Iron Man",
	                   "When an industrialist is captured, he constructs a high-tech armoured suit to escape. Once he manages to escape, he decides to use his suit to fight against evil forces and save the world.",
	                   "http://www.gstatic.com/tv/thumb/movieposters/170620/p170620_p_v8_ak.jpg",
	                   "https://www.youtube.com/watch?v=8hYlB38asDY")

cars = media.Movie("Cars 3",
	               "Blindsided by a new generation of blazing-fast cars, the legendary Lighting McQueen finds himself pushed out of the sport that he loves. Hoping to get back in the game, he turns to Cruz Ramirez, an eager young technician who has her own plans for winning. With inspiration from the Fabulous Hudson Hornet and a few unexpected turns, No. 95 prepares to compete on Piston Cup Racing's biggest stage.",
	               "http://t3.gstatic.com/images?q=tbn:ANd9GcScCXoxJL2rdif-y-lYk_H0jgH_eyFrAXk7yfpUW43xpLW8AmHk",
	               "https://www.youtube.com/watch?v=2LeOH9AGJQM")

captain_america= media.Movie("Captain America: The Winter Soldier",
	                         "nice movie about toys",
	                         "http://t2.gstatic.com/images?q=tbn:ANd9GcTPv762hfzO92t4wllf9dNrV5zrbPzFn0XnwjHRWH20dBTuotSW",
	                         "https://www.youtube.com/watch?v=7SlILk2WMTI")

avengers = media.Movie("Marvel's Avengers: Age of Ultron",
	                    "nice movie about people showing off how tough they are with there toys",
	                    "http://static.comicvine.com/uploads/original/9/95970/4529342-avengers__age_of_ultron_poster__fm__by_krallbaki-d8gdz0n.jpg",
	                    "https://www.youtube.com/watch?v=JAUoeqvedMo")

love = media.Movie("Love 2015",
	                "Murphy is an American living in Paris who enters a highly sexually and emotionally charged relationship with the unstable Electra. Unaware of the seismic effect it will have on their relationship, they invite their pretty neighbor into their bed.",
	                "https://images-na.ssl-images-amazon.com/images/I/41V4EEPve0L.jpg",
	                "https://www.youtube.com/watch?v=h6dbr_E-Yl8")

valerian = media.Movie("Valerian and the City of a Thousand Planets",
	                    "nice movie about toys",
	                    "http://t2.gstatic.com/images?q=tbn:ANd9GcRgqAzC-TzVfX3bi0WWqaaCPuJB2VMYY6cTSVYdIF5hxT8hHdwW",
	                    "https://www.youtube.com/watch?v=NNrK7xVG3PM")

movies = [toy_story,avatar,interstellar,iron_man,cars,captain_america,avengers,love]
fresh_tomatoes.open_movies_page(movies)
