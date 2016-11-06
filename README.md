# Moodify
Take a song and put it through a given algorithm in order to get percentage breakdown of moods ex. Angry, Frustrated, Happy, Sad (Find amount of presence - MOodiness). Then possibly provide songs scheduled so that they would be played negative to positive progression.

# Links
Indigitous Hack Project Desc: https://indigitous.org/projects/?filter_challenge=musicfinder

Moodify Project Desc - https://indigitous.org/projects/upliftify/

IBM Tone Analyzer - https://tone-analyzer-demo.mybluemix.net/

# Steps to use this code repo
1. Fork/Clone repo

2. First, either create a script or manually put all songs into the '/txt/' folder without the song name or artist. (We made the filename contain name of song and artist)

3. Run 'addperiod.py' in order to take all files from txt and translate them into files with periods at the end, adding them into '/txt_period/'

4. Go to '/txt_period/' and execute command 'file -i *'. Remove anything that is 'iso-8859-1' or 'unknown8bit', or move them to '/corrupted_files/'. This will prevent IBM Watson from issuing an error over calls of invalid bytes

	NOTE: IBM Watson Tone Analyzer analyzes based on sentences with periods, so make sure the songs aren't greater than 1000 lines (max of 1000 sentences)

4. Set up an IBM Watson account.

5. Create an app for IBM Watson Tone Analyzer.

6. Get username and password

7. Insert into 'tone_analyzer.py' your username and password and uncomment lines associated with IBM Watson API calls

8. Run 'tone_analyzer.py' to put json files from API calls to IBM Watson into '/json/' folder (Will take about 7-9 seconds per API call)

9. Run 'max_mood_genre.py' in '/songs_to_moods/' folder to populate folders of tones ('/Anger/', '/Joy/', '/Sadness/', '/Fear/', and '/Disgust/') with all files that's max pertains to that genre.

10. Run 'max_mood_all.py' in '/songs_to_moods/' folder to populate '/All/' folder with all files

	NOTE: Data in '/All/', '/Anger/', '/Joy/', '/Sadness/', '/Fear/', and '/Disgust/' consists of:
	
	filename
	
	whole max tone
	
	whole max tone value
	
	percentages of all tones with values for song, max sentence (5 total)
	
	max sentence
	
	sentence max tone
	
	sentence max tone value

11. Run 'sort_data_genre.py' to sort all data so that they are ordered in '/Sorted_Tones/' by the tone value from low to high.
