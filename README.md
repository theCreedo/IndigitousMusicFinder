# Moodify
Take a song and put it through a given algorithm in order to get percentage breakdown of moods ex. Angry, Frustrated, Happy, Sad (Find amount of presence - Moodiness). Furthermore, take a set of those songs and assert through natural language processing in order to create topics for groups of songs. Finally provide the songs scheduled so that they would be shown from negative to positive progression.

# Links
Moodify Presentation Video: https://www.youtube.com/watch?v=NDC10z1V3Fw&feature=youtu.be

Moodify Project Desc - https://indigitous.org/projects/upliftify/

# Additional Enhancements/Features
- Find a dataset consisting of song lyric words - Expand on list of songs for analyzing

- Choose a better collection of songs (one genre, instead of the top 100 on the US charts, and top Christian songs)

- Have a censor mapping on songs to prevent coarse language from being very explicitly shown

- Get a data set of all artists who state in their bio their Christian or have factors associated to it

- Find a way to train the pipeline on “music by Christians”

- Store intermediate stages of metadata/processed data for each song to a database rather than in folders

- Add this tool onto a mobile/web platform for others to use

- Suggest a “playlist” based on the user’s situation or need

- Play recommended/scheduled songs on a platform

- Tweak some parameters in topic analysis to produce better topics

# Steps to use this code repo
1. Fork/Clone repo

2. First, either create a script or manually put all songs into the `/data/txt/original_song_lyrics/` folder with the song name or artist. (We made sure the filename contained name of song and artist). For our files, we made it so that later it would remove the 
	
	NOTE: Make sure that songs are stored stanza by stanza, with each stanza separated by an empty line. Be wary of Windows's lack of normalization on encoding format; if possible, store new songs as text files of `utf-8`, for IBM Watson's sake.

	NOTE: All files should be formatted with song name on first line and artist name on second line. Then lyrics after that, line by line.

3. Run `addperiod.py` in order to take all files from txt and translate them into files with periods at the end, adding them into `/data/txt/original_song_lyrics_with_periods/`

	NOTE: IBM Watson Tone Analyzer analyzes based on sentences with periods, so make sure the songs aren't greater than 1000 lines (max of 1000 sentences)

4. Go to `/data/txt/original_song_lyrics_with_periods/` and execute command `file -i *`. Remove anything that is `iso-8859-1` or `unknown8bit`, or move them to `/corrupted_files/`. This will prevent IBM Watson from issuing an error over calls of invalid bytes

5. Set up an IBM Watson Bluemix account.

6. Create an app for IBM Watson Tone Analyzer.

7. Get username and password for Tone Analyzer app

8. Insert into `tone_analyzer.py` your username and password and uncomment lines associated with IBM Watson API calls

9. Run `tone_analyzer.py` to put json files from API calls to IBM Watson into `/data/json/` folder (Will take about 5+ seconds per API call, so make sure you have a hobby before you run a lot of files)

10. Run `max_mood_genre.py` to populate folders of tones (`/data/txt/tone_analyzed_songs/Anger/`, `/.../Joy/`, `/.../Sadness/`, `/.../Fear/`, and `/.../Disgust/`) with all files that's max pertains to that genre.

11. Run `max_mood_all.py` to populate `/data/txt/tone_analyzed_songs/All/` folder with all files

	NOTE: Data in `/data/txt/tone_analyzed_songs/All/`, `/.../Anger/`, `/.../Joy/`, `/.../Sadness/`, `/.../Fear/`, and `/.../Disgust/` consists of:
	
```
	filename
	whole max tone
	whole max tone value
	percentages of all tones with values for song, max sentence (5 total)
	max sentence
	sentence max tone
	sentence max tone value
```

12. Run `sort_data_genre.py` to sort all data so that they are ordered in `/data/txt/sorted_by_tone_value_songs/` by the tone value from low to high.

	NOTE: Data in `/.../sorted_by_tone_value_songs/` + TONE + `_low_to_high.txt` consists of a repeat of data sorted from 
```
	filename
	sorted tone value
```

	NOTE: Any errors discovered in working with files will be recorded in `/data/txt/failure_log/` folder associated with the given python file. There may be repeats since errors are appended to the file. Errors will be saved in this format: `data - time : filename.txt: ERRORMSG`

13. Run `topic_analyzer.py` to build and pickle a Gensim vocabulary for all the songs in the dataset.


14. Change the `TRAIN_VOCAB` flag to 0 so that users of the `topic_analyzer.py` module (such as `cluster_songs_by_mood.py`) will not cause the vocabulary to rebuild (takes a lot of time), but load from the pickle instead.

15. Use `cluster_songs_by_mood.py's` two functions to recognize topics from songs and pickle this data, or to cluster songs by their top-ranked topic and print them.

# Directory Hiearchy

```
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
	│       ├── refined_song_lyrics
	│       ├── sorted_by_tone_value_songs
	│       ├── tone_analyzed_songs
	│       │   ├── All
	│       │   ├── Anger
	│       │   ├── Disgust
	│       │   ├── Fear
	│       │   ├── Joy
	│       │   └── Sadness
	│       └── topic_analyzed_songs
	├── example output
	├── scripts
	└── server
	    ├── __pycache__
	    ├── static
	    └── templates
```

