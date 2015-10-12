import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "Avatar poster link",
                     "Avatar trailer link")
#print(avatar.storyline)
#toy_story.show_trailer()

#movies = [toy_story, avatar]
#fresh_tomatoes.open_movies_page(movies)

print media.Movie.__name__
print media.Movie.__module__