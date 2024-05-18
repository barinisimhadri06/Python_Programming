# Author: Barini Simhadri
# Date: 07-03-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link: https://youtu.be/jDtBGg2RYBk

import pandas as pd

# Define a function to load and process the data
def process_data(artists_file, tracks_file):
    """
    Load and process the artists and tracks data.
    """
    # Load artists data into a DataFrame
    artists_df = pd.read_csv(artists_file, sep='\t')

    # Load tracks data into a DataFrame
    tracks_df = pd.read_csv(tracks_file, sep='\t')

    return artists_df, tracks_df

# Define a function to identify and print the artist with maximum followers
def max_followers_artist(artists_df):
    """
    Identify and print the artist with the maximum number of followers.
    """
    # Find the row with maximum followers
    max_followers_row = artists_df.loc[artists_df['followers'].idxmax()]

    # Print the name and genre of the artist with maximum followers
    print(f"Artist with maximum followers: {max_followers_row['name']} ({max_followers_row['genres']})")

# Define a function to identify and print the most productive artist
def most_productive_artist(tracks_df, artists_df):
    """
    Identify and print the most productive artist in terms of the number of tracks.

    """
    # Count the number of tracks for each artist
    track_counts = tracks_df['id_artists'].str.split(', ').explode().value_counts()

    # Get the artist ID with the maximum number of tracks
    max_tracks_artist_id = track_counts.idxmax()

    # Get the artist's name using the ID
    most_productive_artist_name = artists_df.loc[artists_df['id'] == max_tracks_artist_id, 'name'].values[0]

    # Print the name of the most productive artist
    print(f"Most productive artist: {most_productive_artist_name}")

# Define a function to summarize genres
def summarize_genres(genres):
    """
    Summarize the genres.
    """
    # Create a DataFrame to store the summary
    genre_summary = pd.DataFrame(columns=['genre', 'total N', 'Av. followers'])

    # Iterate through each genre
    for genre in genres:
        # Count the number of artists with this genre
        total_artists = len(artists_df[artists_df['genres'].str.contains(genre)])

        # Calculate the average number of followers for artists with this genre
        avg_followers = artists_df[artists_df['genres'].str.contains(genre)]['followers'].mean()

        # Append the summary to the DataFrame
        genre_summary = genre_summary.append({'genre': genre, 'total N': total_artists, 'Av. followers': avg_followers}, ignore_index=True)

    # Convert the list to a DataFrame
    genre_summary_df = pd.DataFrame(genre_summary)

    return genre_summary_df

# Define a function to get genre variants
def get_genre_variants(genre):
    """
    Get variants of a given genre.
    """
    # Split the genre string by space
    genre_parts = genre.split()

    # Get all possible combinations of genre parts
    genre_variants = [' '.join(genre_parts[:i+1]) for i in range(len(genre_parts))]

    return genre_variants

# Define a function to summarize artist performance
def summarize_artist_performance(name):
    """
    Summarize the performance of an artist.
    """
    # Find the artist in the artists DataFrame
    artist_row = artists_df.loc[artists_df['name'] == name]

    # Get the artist's ID
    artist_id = artist_row['id'].values[0]

    # Count the number of tracks performed by the artist
    total_tracks = len(tracks_df[tracks_df['id_artists'].str.contains(artist_id)])

    # Count the number of solo tracks performed by the artist
    solo_tracks = len(tracks_df[(tracks_df['id_artists'].str.contains(artist_id)) & (tracks_df['id_artists'].str.count(artist_id) == 1)])

    # Count the number of collaborative tracks performed by the artist
    collab_tracks = total_tracks - solo_tracks

    # Calculate the average popularity of total, solo, and collaborative tracks
    avg_popularity_total = tracks_df[tracks_df['id_artists'].str.contains(artist_id)]['popularity'].mean()
    avg_popularity_solo = tracks_df[(tracks_df['id_artists'].str.contains(artist_id)) & (tracks_df['id_artists'].str.count(artist_id) == 1)]['popularity'].mean()
    avg_popularity_collab = tracks_df[(tracks_df['id_artists'].str.contains(artist_id)) & (tracks_df['id_artists'].str.count(artist_id) > 1)]['popularity'].mean()

    # Count the number of unique collaborators
    unique_collaborators = len(tracks_df[tracks_df['id_artists'].str.contains(artist_id)]['id_artists'].str.split(', ').explode().unique()) - 1

    # Print the summary
    print(f"Summary for {name}:")
    print(f"Number of tracks: {total_tracks}")
    print(f"Number of solo tracks: {solo_tracks}")
    print(f"Number of collaborative tracks: {collab_tracks}")
    print(f"Average popularity of total tracks: {avg_popularity_total}")
    print(f"Average popularity of solo tracks: {avg_popularity_solo}")
    print(f"Average popularity of collaborative tracks: {avg_popularity_collab}")
    print(f"Number of unique collaborators: {unique_collaborators}")

# Load and process the data
artists_file = "C:/Users/bunty/Desktop/DSC430/week_8/hw/artists.tsv"
tracks_file = "C:/Users/bunty/Desktop/DSC430/week_8/hw/tracks.tsv"
artists_df, tracks_df = process_data(artists_file, tracks_file)

# Question 1: Identify and print the name and genre of the artist with the maximum number of followers.
max_followers_artist = artists_df.loc[artists_df['followers'].idxmax()]
print(f"Artist with maximum followers: {max_followers_artist['name']} ({max_followers_artist['genres']})")

# Question 2: Identify and print the name of the most productive artist in terms of the number of tracks performed.
track_counts = tracks_df['id_artists'].str.split(', ').explode().value_counts()
most_productive_artist_id = track_counts.idxmax()
most_productive_artist_name = artists_df.loc[artists_df['id'] == most_productive_artist_id, 'name'].values[0]
print(f"Most productive artist: {most_productive_artist_name}")

# Question 3: Write a function called summarize_genres(genres) that takes a list of genres and returns a DataFrame.
def summarize_genres(genres):
    summary = []
    for genre in genres:
        total_artists = len(artists_df[artists_df['genres'].str.contains(genre)])
        avg_followers = artists_df[artists_df['genres'].str.contains(genre)]['followers'].mean()
        summary.append({'genre': genre, 'total N': total_artists, 'Av. followers': avg_followers})
    return pd.DataFrame(summary)

# Question 4: Write a function called get_genre_variants(genre) that takes a genre string and returns an array that includes all variants of that genre.
def get_genre_variants(genre):
    return artists_df[artists_df['genres'].str.contains(genre)]['genres'].unique()

# Question 5: Write a function called summarize_artist_performance(name) that takes an artist’s name and prints the following values.
def summarize_artist_performance(name):
    artist = artists_df[artists_df['name'] == name]
    artist_id = artist['id'].iloc[0]
    total_tracks = len(tracks_df[tracks_df['id_artists'].str.contains(artist_id)])
    solo_tracks = len(tracks_df[(tracks_df['id_artists'].str.contains(artist_id)) & (tracks_df['id_artists'].str.count(artist_id) == 1)])
    collab_tracks = total_tracks - solo_tracks
    avg_total_popularity = tracks_df[tracks_df['id_artists'].str.contains(artist_id)]['popularity'].mean()
    avg_solo_popularity = tracks_df[(tracks_df['id_artists'].str.contains(artist_id)) & (tracks_df['id_artists'].str.count(artist_id) == 1)]['popularity'].mean()
    avg_collab_popularity = tracks_df[(tracks_df['id_artists'].str.contains(artist_id)) & (tracks_df['id_artists'].str.count(artist_id) > 1)]['popularity'].mean()
    unique_collaborators = len(tracks_df[tracks_df['id_artists'].str.contains(artist_id)]['id_artists'].str.split(', ').explode().unique()) - 1
    print(f"Summary for {name}:")
    print(f"Number of tracks: {total_tracks}")
    print(f"Number of solo tracks: {solo_tracks}")
    print(f"Number of collaborative tracks: {collab_tracks}")
    print(f"Average popularity of total tracks: {avg_total_popularity}")
    print(f"Average popularity of solo tracks: {avg_solo_popularity}")
    print(f"Average popularity of collaborative tracks: {avg_collab_popularity}")
    print(f"Number of unique collaborators: {unique_collaborators}")

# Test the functions
genres = ['jazz', 'pop', 'rock']
print("Genre Summary:")
print(summarize_genres(genres))
print("Variants of jazz:")
print(get_genre_variants('jazz'))
summarize_artist_performance("Michael Jackson")