# Moodify
Take a song and put it through a given algorithm in order to get percentage breakdown of moods ex. Angry, Frustrated, Happy, Sad (Find amount of presence - MOodiness). Then possibly provide songs scheduled so that they would be played negative to positive progression.

# Links
Indigitous Hack Project Desc: https://indigitous.org/projects/?filter_challenge=musicfinder

Moodify Project Desc - https://indigitous.org/projects/upliftify/

IBM Tone Analyzer - https://tone-analyzer-demo.mybluemix.net/

# Additional Features
- Add this tool onto a mobile/web platform for others to use

- Have songs recommended/scheduled to play either on Spotify, Pandora, etc...

# Steps to use this code repo
1. Fork/Clone repo

2. First, either create a script or manually put all songs into the '/txt/' folder without the song name or artist. (We made the filename contain name of song and artist). 
	
	NOTE: Make sure that songs are stored stanza by stanza. Different computers (Mac, Windows, Linuz, etc...) can encode the information differently based on how lyrics are stored

3. Run 'addperiod.py' in order to take all files from txt and translate them into files with periods at the end, adding them into '/txt_period/'

	NOTE: IBM Watson Tone Analyzer analyzes based on sentences with periods, so make sure the songs aren't greater than 1000 lines (max of 1000 sentences)

4. Go to '/txt_period/' and execute command 'file -i *'. Remove anything that is 'iso-8859-1' or 'unknown8bit', or move them to '/corrupted_files/'. This will prevent IBM Watson from issuing an error over calls of invalid bytes

5. Set up an IBM Watson account.

6. Create an app for IBM Watson Tone Analyzer.

7. Get username and password

8. Insert into 'tone_analyzer.py' your username and password and uncomment lines associated with IBM Watson API calls

9. Run 'tone_analyzer.py' to put json files from API calls to IBM Watson into '/json/' folder (Will take about 5+ seconds per API call, so make sure you have a hobby before you run a lot of files)

10. Run 'max_mood_genre.py' in '/songs_to_moods/' folder to populate folders of tones ('/Anger/', '/Joy/', '/Sadness/', '/Fear/', and '/Disgust/') with all files that's max pertains to that genre.

11. Run 'max_mood_all.py' in '/songs_to_moods/' folder to populate '/All/' folder with all files

	NOTE: Data in '/All/', '/Anger/', '/Joy/', '/Sadness/', '/Fear/', and '/Disgust/' consists of:
	
	filename
	
	whole max tone
	
	whole max tone value
	
	percentages of all tones with values for song, max sentence (5 total)
	
	max sentence
	
	sentence max tone
	
	sentence max tone value

12. Run 'sort_data_genre.py' to sort all data so that they are ordered in '/Sorted_Tones/' by the tone value from low to high.

	NOTE: Data in '/Sorted_Tones/' + TONE + '_low_to_high.txt' consists of a repeat of data sorted from low to high as:

	filename

	sorted tone value

	NOTE: Any errors discovered in working with files will be recorded in '/corrupted_files/failures/' folder associated with the given python file. There may be repeats since errors are appended to the file. Errors will be saved in this format: 'filename.txt: ERRORMSG'

13. Run analyzetopic.py to build and pickle a Gensim vocabulary for all the songs in the dataset.

14. Change the TRAIN_VOCAB flag to 0 so that users of the analyzetopic module (such as cluster_songs_by_mood) will not cause the vocabulary to rebuild (takes a lot of time), but load from the pickle instead.

15. Use cluster_songs_by_mood's two functions to recognize topics from songs and pickle this data, or to cluster songs by their top-ranked topic and print them.


# Directory Hiearchy:

.

├── data

│   ├── corrupted_files

│   ├── images

│   │   ├── anger

│   │   ├── disgust

│   │   ├── fear

│   │   ├── joy

│   │   └── sadness

│   ├── json

│   ├── topic_groupings

│   └── txt

│       ├── failure_log

│       ├── original_song_lyrics

│       ├── original_song_lyrics_with_periods

│       ├── sorted_by_tone_value_songs

│       ├── tone_analyzed_songs

│       │   ├── All

│       │   ├── Anger

│       │   ├── Disgust

│       │   ├── Fear

│       │   ├── Joy

│       │   └── Sadness

│       └── topic_analyzed_songs

│           └── songs_to_topics

├── example output

├── scripts

└── server

    ├── __pycache__

    ├── static

    └── templates