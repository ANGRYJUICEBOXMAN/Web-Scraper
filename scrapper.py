import requests
import os

class SongScraper:
    def __init__(self, artist, title):
        # Initialize the SongScraper with artist and title
        self.artist = artist
        self.title = title
        # Construct the API URL using the artist and title
        self.api_url = f"https://api.lyrics.ovh/v1/{artist}/{title}"

    def get_lyrics(self):
        try:
            # Make a GET request to the lyrics.ovh API
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json().get('lyrics')  # Extract lyrics from the JSON response
        except requests.exceptions.RequestException as e:
            # Handle exceptions during the request
            print(f"Error fetching lyrics: {e}")
            return None

    def save_lyrics_to_file(self, artist, title, lyrics):
        # Create a folder to store lyrics if it doesn't exist
        folder_path = 'lyrics_folder'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Create a filename based on artist and title
        filename = f"{artist}_{title}.txt"
        # Join the folder path and filename to create the full file path
        file_path = os.path.join(folder_path, filename)

        # Write the lyrics to a text file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(lyrics)

        # Print a message indicating the successful saving of lyrics
        print(f"Lyrics saved to: {file_path}")

    def scrape_and_save_lyrics(self):
        # Retrieve lyrics using the get_lyrics method
        lyrics = self.get_lyrics()

        # Check if lyrics were successfully obtained
        if lyrics:
            # Save the lyrics to a file using save_lyrics_to_file
            self.save_lyrics_to_file(self.artist, self.title, lyrics)


# Example usage:
if __name__ == "__main__":
    artist_name = "John Lennon"
    song_title = "Imagine"

    # Create an instance of SongScraper with artist and title
    scraper = SongScraper(artist_name, song_title)
    # Call the scrape_and_save_lyrics method to fetch and save the lyrics
    scraper.scrape_and_save_lyrics()
