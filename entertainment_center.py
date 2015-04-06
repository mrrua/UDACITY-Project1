import media 
import fresh_tomatoes

#Creation of 6 movie objects & their information. Each variable is on its own line and should reference the movies: Name, Plot, Poster Image, Youtube Trailer Link, IMDb Page, and Release Date
avatar = media.Movie("Avatar",
                     "In the future, Jake, a paraplegic war veteran, is brought to another planet, Pandora, which is inhabited by the Na'vi, a humanoid race with their own language and culture. Those from Earth find themselves at odds with each other and the local culture.",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8",
                     "http://www.imdb.com/title/tt0499549/",
                     2009)

gladiator = media.Movie("Gladiator",
                        "Maximus is a powerful Roman general, loved by the people and the ageing Emperor, Marcus Aurelius. Before his death, the Emperor chooses Maximus to be his heir over his own son, Commodus, and a power struggle leaves Maximus and his family condemned to death. The powerful general is unable to save his family, and his loss of will allows him to get captured and put into the Gladiator games until he dies. The only desire that fuels him now is the chance to rise to the top so that he will be able to look into the eyes of the man who will feel his revenge.",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/8/8d/Gladiator_ver1.jpg/220px-Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=IvTT29cavKo",
                        "http://www.imdb.com/title/tt0172495/",
                        2000)

troy = media.Movie("Troy",
                   "It is the year 1250 B.C. during the late Bronze age. Two emerging nations begin to clash after Paris, the Trojan prince, convinces Helen, Queen of Sparta, to leave her husband, Menelaus, and sail with him back to Troy. After Menelaus finds out that his wife was taken by the Trojans, he asks his brother Agamemnon to help him get her back. Agamemnon sees this as an opportunity for power. So they set off with 1,000 ships holding 50,000 Greeks to Troy. With the help of Achilles, the Greeks are able to fight the never before defeated Trojans. But they come to a stop by Hector, Prince of Troy. The whole movie shows their battle struggles and the foreshadowing of fate.",
                   "http://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Troy2004Poster.jpg/220px-Troy2004Poster.jpg",
                   "https://www.youtube.com/watch?v=znTLzRJimeY",
                   "http://www.imdb.com/title/tt0332452/",
                   2004)

the_departed = media.Movie("The Departed",
                           "Two just-graduated officers from Massachusetts State Police Academy follow opposite sides of the law: Billy Costigan is assigned to work undercover with the Irish mobster Frank Costello to get evidences to arrest him. His true identity is known only by his superiors Dignam and Oliver Queenan. The protégée of Costello, Colin Sullivan, is promoted in the Massachusetts State Police and is the informer of Costello. Each police officer gives his best effort trying to disclose the identity of the other 'rat.'",
                           "http://upload.wikimedia.org/wikipedia/en/thumb/5/50/Departed234.jpg/220px-Departed234.jpg",
                           "https://www.youtube.com/watch?v=auYbpnEwBBg",
                           "http://www.imdb.com/title/tt0407887/",
                           2006)

any_given_sunday = media.Movie("Any Given Sunday",
                               "When a devastating hit knocks a professional football legend and quarterback Cap Rooney out of the game, a young, unknown third-stringer is called in to replace him. Having ridden the bench for years because of a string of bad luck stories and perhaps insufficient character, Willie Beaman seizes what may be his last chance, and lights up the field with a raw display of athletic prowess. His stunning performance over several games is so outstanding and fresh it seems to augur a new era in the history of this Miami franchise, and forces aging coach Tony D'Amato to reevaluate his time-tested values and strategies and begin to confront the fact that the game, as well as post-modern life may be passing him by. Adding to the pressure on D'Amato to win at any cost is the aggressive young President/Co-owner of the team, Christina Pagniacci, now coming into her own after her father's death. Christina's driving desire to prove herself in a male dominated world is intensified by her focus on the marketing and business of football, in which all coaches and players are merely properties.",
                               "http://upload.wikimedia.org/wikipedia/en/thumb/8/80/Any_Given_Sunday.jpg/220px-Any_Given_Sunday.jpg",
                               "https://www.youtube.com/watch?v=RN7sKvaHDlA",
                               "http://www.imdb.com/title/tt0146838/",
                               1999)

man_of_steel = media.Movie("Man of Steel",
                           "Kal-El, son of Jor-El and Lara is sent to Earth after his home planet: Krypton leads to a complete incineration. Now taking the name \"Clark Kent\", he then discovers his true persona when he is guided to become Superman: A hero committed to protect Earth's fate and the harm that threatens it. However, General Zod, a citizen of Krypton and it's military leader looks at Earth's fate differently and decides to use it with a sacrifice for all humans. Superman, with the help of present military and news reporter Lois Lane makes an alliance together to stop Zod from obliterating human existence.",
                           "http://upload.wikimedia.org/wikipedia/en/thumb/8/85/ManofSteelFinalPoster.jpg/220px-ManofSteelFinalPoster.jpg",
                           "https://www.youtube.com/watch?v=T6DJcgm3wNY",
                           "http://www.imdb.com/title/tt0770828/",
                           2013)

#Creates an array of the above created movie objects
movies = [avatar, gladiator, troy, the_departed, any_given_sunday, man_of_steel]
#Calls the script that builds our HTML page
fresh_tomatoes.open_movies_page(movies)

