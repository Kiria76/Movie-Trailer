import fresh_tomatoes
import media

moana = media.Movie(

    "Moana",
    "This is a beautiful story of a princess struggling to help her people.",
    "https://vignette.wikia.nocookie.net/disney/images/8/8b/"
    "Moana_soundtrack.jpg/revision/latest?cb=20161004073641",
    "https://www.youtube.com/watch?v=LKFuXETZUsI"
    )

star_wars_the_last_jedi = media.Movie(
    "Star Wars: The Last Jedi",
    "This movie is more of a star adventure",
    "https://encrypted-tbn0.gstatic.com/"
    "images?q=tbn:ANd9GcRZ08p58d7zouKP2BABTfky9D3xpejmd5U_tMEhlc1jS11rCVIY",
    "https://www.youtube.com/watch?v=Q0CbN8sfihY")

the_hobbit_the_battle_of_the_five_armies = media.Movie(
    "The Hobbit: The Battle of the Five Armies",
    "The Battle of Five Armies was a battle waged between"
    "the Orcs and the Wargs of the Misty Mountains",
    "https://encrypted-tbn0.gstatic.com/"
    "images?q=tbn:ANd9GcS8O1n9dmEjTPJrsVS6GXMfhWQITKyIFolqM41Vdobu2wanlniB",
    "https://www.youtube.com/watch?v=ZSzeFFsKEt4")

the_lion_king = media.Movie(
    "The Lion king",
    "The action of the film revolves around the lion cub Simba"
    "and the arduous search for his place in the circle of life.",
    "https://encrypted-tbn0.gstatic.com/"
    "images?q=tbn:ANd9GcRy2CwzvqxqRE_wcsPUgKKsdZYTZ2RfaBTan5tr3DGI3uWN0Xh-DA",
    "https://www.youtube.com/watch?v=qRbjMur9Xjo")

the_little_mermaid = media.Movie(
    "The Little Mermaid",
    "Ariel, the youngest daughter of King Triton,"
    "ruler of the sea people, is dissatisfied with her life in the sea",
    "https://encrypted-tbn0.gstatic.com/"
    "images?q=tbn:ANd9GcT-TxhMOE9IlnqTDPeIK9znwQQE5PfjAfYNUeKbEcbDfeiLygF1",
    "https://www.youtube.com/watch?v=ZGZX5-PAwR8")

the_lord_of_the_rings = media.Movie(
    "The Lord of the Rings",
    "The story tells of the Dark Lord Sauron (Sala Baker),"
    "who is seeking the One Ring",
    "https://upload.wikimedia.org/wikipedia/en/9/9d/"
    "The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
    "https://www.youtube.com/watch?v=V75dMMIW2B4")

movies = [moana, star_wars_the_last_jedi, the_hobbit_the_battle_of_the_five_armies,
          the_lion_king, the_little_mermaid, the_lord_of_the_rings]
fresh_tomatoes.open_movies_page(movies)
