import media
import sys
sys.path.insert(0, "ud036_StarterCode")  #  helps us import fresh_tomatos
import fresh_tomatoes

def main():
    inception = media.Movie("Inception",  #  name
        "A movie about dreams",  #  description
        "https://www.youtube.com/watch?v=97CDCk2n-Nw",  #  trailer
        "movie_posters/inception.jpg")  #  poster
    intersteller = media.Movie("Intersteller",
        "Post epocolyptic last generation of humans",
        "https://youtu.be/8EdxTFS3fD0",
        "movie_posters/Interstellar_film_poster.jpg")
    the_matrix = media.Movie("The Matrix",
        "People stuck in boxes",
        "https://www.youtube.com/watch?v=pcW78sj91Qg",
        "movie_posters/The_Matrix_Poster.jpg")
    taken = media.Movie("Taken",
        "Daughter gets kidnapped",
        "https://www.youtube.com/watch?v=pbA-tBrHNfI",
        "movie_posters/Taken_film_poster.jpg")
    marley_and_me = media.Movie("Marley and Me",
        "A really awesome dog",
        "https://www.youtube.com/watch?v=gaKwEPW6wys",
        "movie_posters/MarleyPoster.jpg")
    rocky = media.Movie("Rocky",
        "Boxing",
        "https://www.youtube.com/watch?v=Wif1EzGQ9Fk",
        "movie_posters/rocky.jpg" )
    founder = media.Movie("The Founder",
        "McDonalds founder movie",
        "https://www.youtube.com/watch?v=ksLZEepQ0nA",
        "movie_posters/The_Founder_poster.png")

    #  All the youtube links work on my computer which is in Santa Cruz, CA

    #  populating the list that gets passes into frest_tomatos.py
    movies_list = [inception,
        intersteller, the_matrix,
        taken, marley_and_me, rocky,
        founder]

    #  finally calling the function that generates the html code
    fresh_tomatoes.open_movies_page(movies_list)

if __name__ == "__main__":  #  if this file is run like
#  python entertainment_centre.py then it will run the main function above
    main()
