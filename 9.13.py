class Artist:
    def __init__(self, name='unknown', birth_year=-1, death_year=-1):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    def print_info(self):
        year_info = ''
        if self.birth_year >= 0 and self.death_year < 0:
            year_info = str(self.birth_year) + " to present"
        elif self.birth_year < 0:
            year_info = "unknown"
        else:
            year_info = str(self.birth_year) + " to " + str(self.death_year)
        print(f"Artist: {self.name} ({year_info})")
        # TODO: Define constructor with parameters to initialize instance attributes
    #       (name, birth_year, death_year)

    # TODO: Define print_info() method


class Artwork:
    def __init__(self, title='unknown', year_created=-1, artist='Artist'):
        self.title = title
        self.year_created = year_created
        self.artist = artist

    def print_info(self):
        self.artist.print_info()
        print(f"Title: {self.title}, {self.year_created}")
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (title, year_created, artist)

    # TODO: Define print_info() method


if __name__ == "__main__":
    user_artist_name = input()
    user_birth_year = int(input())
    user_death_year = int(input())
    user_title = input()
    user_year_created = int(input())

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)

    new_artwork.print_info()