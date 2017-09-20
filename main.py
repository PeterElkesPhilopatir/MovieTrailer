import media
import fresh_tomatoes

avatar = media.Movie("Avatar",
                     "A hybrid human-alien called an"
                     " Avatar is created to facilitate communication"
                     " with the indigenous Na'vis"
                     " from the planet Pandora.",
                     "http://avatarblog.typepad.com/.a/6a0120a6b2c140970c012876c79e1a970c-800wi",  # NOQA
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

print(avatar.poster_image_url)

gladiator = media.Movie("Gladiator",
                        "When a Roman general is betrayed and his "
                        "family murdered by an emperor's corrupt son"
                        ", he comes to Rome as a gladiator to seek revenge.",
                        "http://i.imgur.com/2maCz21.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=ol67qo3WhJk"
                        )
fury = media.Movie("Fury",
                   "A grizzled tank commander makes tough decisions as"
                   "he and his crew fight their"
                   "way across Germany in April, 1945.",
                   "http://3.bp.blogspot.com/-xvwJ2DpjcOM/VNUN1i75mUI/A"
                   "AAAAAAAABo/nQ-i8Xq8Ous/s1600/fury_movie-wide.jpg",
                   # NOQA
                   "https://www.youtube.com/watch?v=-OGvZoIrXpg")

interstellar = media.Movie("Interstellar",
                           "A team of explorers "
                           "travel through a wormhole "
                           "in space in an attempt to"
                           "ensurehumanity's survival.",
                           "https://s-media-cache-ak0.pinimg.com/736x/07/29/5"
                           "a/07295a499d75c4934cd376a42ba19397.jpg",
                           # NOQA
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E"
                           )

zootopia = media.Movie("Zootopia",
                       "In a city of anthropomorphic animals,"
                       " a rookie bunny"
                       "cop and a cynical"
                       " con artist fox must work"
                       "together to uncover a conspiracy.",
                       "http://cdn3-www.comingsoon.net/assets/uploads/"
                       "gallery/zootopia"
                       "/c55463169023e916571b0361c592cd6c0f630904.jpg",
                       # NOQA
                       "https://www.youtube.com/watch?v=bY73vFGhSVk")

dangal = media.Movie("Dangal",
                     "Biographical sports "
                     "drama on former wrestler "
                     "Mahavir Singh Phogat and his two wrestler "
                     "daughters' struggle towards glory at the"
                     "Commonwealth Games in the face of societal oppression.",
                     "http://hercreativepalace.com/"
                     "wp-content/uploads/2016/12/"
                     "Dangal-poster-large-LISTICLE.jpg",
                     # NOQA
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g"
                     )
movies = [avatar, gladiator, interstellar, fury, dangal, zootopia]

fresh_tomatoes.open_movies_page(movies)
